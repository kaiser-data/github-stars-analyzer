// Pre-computes the knowledge graph so the browser does zero math.
// Outputs:
//   public/data/graph.json        — nodes+links ready for react-force-graph-3d
//   public/data/graph-context.json — compact summary for LLM question answering
//
// Run: node scripts/precompute.mjs
// (automatically called by npm run refresh)

import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { createRequire } from 'node:module';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, '..');
const require = createRequire(import.meta.url);

// ── deps (same ones used in the browser) ───────────────────────────────────
const { default: Graph } = await import('graphology');
const { default: louvain } = await import('graphology-communities-louvain');
const pagerank = await import('graphology-metrics/centrality/pagerank.js');
const { forceSimulation, forceLink, forceManyBody, forceCenter } = await import('d3-force-3d');

// ── load classified data ────────────────────────────────────────────────────
const classified = JSON.parse(readFileSync(join(root, 'public/data/classified.json'), 'utf8'));
const repos = classified.repos;
console.log(`⚙  Pre-computing graph for ${repos.length} repos…`);

// ── helpers ─────────────────────────────────────────────────────────────────
function jaccard(a, b) {
  if (!a.size || !b.size) return 0;
  let inter = 0;
  for (const x of a) if (b.has(x)) inter++;
  return inter / (a.size + b.size - inter);
}

// ── build graphology graph (identical logic to GraphProvider.jsx) ───────────
const g = new Graph({ type: 'undirected', multi: false });
const topicSets = new Map();
const authorSets = new Map();

for (const r of repos) {
  topicSets.set(r.id, new Set(r.topics ?? []));
  authorSets.set(r.id, new Set((r.authors_90d ?? []).map(a => a.login).filter(Boolean)));
  g.addNode(`repo:${r.id}`, {
    id: r.id, full_name: r.full_name, description: r.description,
    stars: r.stars, primary_language: r.primary_language, topics: r.topics ?? [],
    lifecycle_stage: r.lifecycle_stage, health_score: r.health_score,
    bus_factor: r.bus_factor, age_days: r.age_days, days_since_push: r.days_since_push,
    commits_90d: r.commits_90d, unique_authors_90d: r.unique_authors_90d,
    open_issues: r.open_issues, releases_total: r.releases_total,
    momentum: r.momentum, stratum: r.stratum, url: r.url, owner: r.owner,
  });
}

// O(n²) kNN sweep
const K = 4, STRONG = 1.0;
const pairsOf = repos.map(() => []);
for (let i = 0; i < repos.length; i++) {
  const a = repos[i];
  const aTopic = topicSets.get(a.id), aAuthor = authorSets.get(a.id);
  for (let j = i + 1; j < repos.length; j++) {
    const b = repos[j];
    let w = jaccard(aTopic, topicSets.get(b.id));
    w += jaccard(aAuthor, authorSets.get(b.id)) * 2;
    if (a.primary_language && a.primary_language === b.primary_language) w += 0.05;
    if (a.owner === b.owner) w += 0.5;
    if (w === 0) continue;
    pairsOf[i].push([j, w]);
    pairsOf[j].push([i, w]);
  }
}

const keepEdges = new Set();
for (let i = 0; i < repos.length; i++) {
  const pairs = pairsOf[i];
  if (!pairs.length) continue;
  pairs.sort((x, y) => y[1] - x[1]);
  for (let k = 0; k < Math.min(K, pairs.length); k++) keepEdges.add(i < pairs[k][0] ? `${i}-${pairs[k][0]}` : `${pairs[k][0]}-${i}`);
  for (const [j, w] of pairs) {
    if (w < STRONG) break;
    keepEdges.add(i < j ? `${i}-${j}` : `${j}-${i}`);
  }
}

let edgeCount = 0;
for (let i = 0; i < repos.length; i++) {
  for (const [j, w] of pairsOf[i]) {
    if (j <= i || !keepEdges.has(`${i}-${j}`)) continue;
    const a = repos[i], b = repos[j];
    const aTopic = topicSets.get(a.id), bTopic = topicSets.get(b.id);
    const aAuthor = authorSets.get(a.id), bAuthor = authorSets.get(b.id);
    g.addEdge(`repo:${a.id}`, `repo:${b.id}`, {
      weight: w,
      shared_topics: [...aTopic].filter(t => bTopic.has(t)),
      shared_authors: [...aAuthor].filter(u => bAuthor.has(u)),
    });
    edgeCount++;
  }
}

// Orphan fallback
const stagePivots = new Map();
for (const r of repos) {
  const cur = stagePivots.get(r.lifecycle_stage);
  if (!cur || r.stars > cur.stars) stagePivots.set(r.lifecycle_stage, r);
}
for (const r of repos) {
  if (g.degree(`repo:${r.id}`) > 0) continue;
  const pivot = stagePivots.get(r.lifecycle_stage);
  if (!pivot || pivot.id === r.id) continue;
  g.addEdge(`repo:${r.id}`, `repo:${pivot.id}`, { weight: 0.05, shared_topics: [], shared_authors: [] });
  edgeCount++;
}

// Louvain + PageRank
const louvainDetail = louvain.detailed(g, { getEdgeWeight: 'weight' });
g.forEachNode((n) => g.setNodeAttribute(n, 'community', louvainDetail.communities[n]));
const communityCount = new Set(Object.values(louvainDetail.communities)).size;
pagerank.default.assign(g, { getEdgeWeight: 'weight', alpha: 0.85, maxIterations: 100, tolerance: 1e-6 });
g.forEachNode((n) => g.setNodeAttribute(n, 'degree', g.degree(n)));

console.log(`   ${g.order} nodes · ${edgeCount} edges · ${communityCount} communities`);

// ── run force simulation to convergence ─────────────────────────────────────
console.log('   Running force simulation…');

const fgNodes = [];
g.forEachNode((nid, attrs) => {
  const pr = attrs.pagerank ?? 0;
  fgNodes.push({
    id: nid,
    val: 1 + Math.log10(1 + (attrs.stars ?? 0)) * 1.4 + pr * 50,
    _attrs: attrs,
  });
});

const fgLinks = [];
g.forEachEdge((eid, attrs, src, tgt) => {
  fgLinks.push({ source: src, target: tgt, weight: attrs.weight ?? 1, shared_topics: attrs.shared_topics ?? [], shared_authors: attrs.shared_authors ?? [] });
});

// Clone for simulation (d3 mutates nodes)
const simNodes = fgNodes.map(n => ({ id: n.id }));
const simLinks = fgLinks.map(l => ({ source: l.source, target: l.target }));

const sim = forceSimulation(simNodes, 3)
  .force('link', forceLink(simLinks).id(d => d.id).distance(60))
  .force('charge', forceManyBody().strength(-120))
  .force('center', forceCenter())
  .stop();

for (let i = 0; i < 300; i++) sim.tick();

// Map computed positions back by id
const posById = new Map(simNodes.map(n => [n.id, { x: n.x ?? 0, y: n.y ?? 0, z: n.z ?? 0 }]));

// ── assemble graph.json ──────────────────────────────────────────────────────
const COMMUNITY_PALETTE = [
  '#ef4444','#f59e0b','#10b981','#3b82f6','#a78bfa',
  '#ec4899','#06b6d4','#84cc16','#f97316','#8b5cf6',
  '#14b8a6','#eab308','#22c55e','#0ea5e9','#d946ef',
];

const STAGE_COLOR = { Hot:'#ef4444', Rising:'#f59e0b', Classic:'#10b981', Mature:'#3b82f6', Declining:'#a78bfa', Abandoned:'#6b7280' };

const nodes = fgNodes.map(n => {
  const a = n._attrs;
  const pos = posById.get(n.id);
  return {
    id: n.id, val: n.val,
    full_name: a.full_name, description: a.description,
    stars: a.stars, primary_language: a.primary_language, topics: a.topics,
    lifecycle_stage: a.lifecycle_stage, health_score: a.health_score,
    bus_factor: a.bus_factor, unique_authors_90d: a.unique_authors_90d,
    commits_90d: a.commits_90d, open_issues: a.open_issues,
    releases_total: a.releases_total, momentum: a.momentum,
    age_days: a.age_days, days_since_push: a.days_since_push,
    stratum: a.stratum, url: a.url, owner: a.owner,
    community: a.community ?? 0,
    pagerank: +(a.pagerank ?? 0).toFixed(6),
    degree: a.degree ?? 0,
    color: COMMUNITY_PALETTE[(a.community ?? 0) % COMMUNITY_PALETTE.length],
    x: +pos.x.toFixed(2), y: +pos.y.toFixed(2), z: +pos.z.toFixed(2),
  };
});

const links = fgLinks.map(l => ({
  source: l.source, target: l.target,
  weight: +l.weight.toFixed(3),
  shared_topics: l.shared_topics,
  shared_authors: l.shared_authors,
}));

// Community metadata
const communityMeta = {};
for (const n of nodes) {
  const c = n.community;
  if (!communityMeta[c]) communityMeta[c] = { repos: [], topics: new Map(), languages: new Map() };
  communityMeta[c].repos.push({ full_name: n.full_name, stars: n.stars, pagerank: n.pagerank });
  for (const t of n.topics) communityMeta[c].topics.set(t, (communityMeta[c].topics.get(t) ?? 0) + 1);
  if (n.primary_language) communityMeta[c].languages.set(n.primary_language, (communityMeta[c].languages.get(n.primary_language) ?? 0) + 1);
}

const communities = {};
for (const [cid, meta] of Object.entries(communityMeta)) {
  meta.repos.sort((a, b) => b.pagerank - a.pagerank);
  communities[cid] = {
    size: meta.repos.length,
    color: COMMUNITY_PALETTE[parseInt(cid) % COMMUNITY_PALETTE.length],
    top_repos: meta.repos.slice(0, 5).map(r => r.full_name),
    top_topics: [...meta.topics.entries()].sort((a, b) => b[1] - a[1]).slice(0, 8).map(([t]) => t),
    top_language: [...meta.languages.entries()].sort((a, b) => b[1] - a[1])[0]?.[0] ?? null,
  };
}

const stats = { nodeCount: nodes.length, edgeCount: links.length, communityCount };

const graphJson = { nodes, links, stats, communities, computed_at: new Date().toISOString() };
writeFileSync(join(root, 'public/data/graph.json'), JSON.stringify(graphJson));
console.log(`   ✓ wrote public/data/graph.json (${(JSON.stringify(graphJson).length / 1e6).toFixed(1)} MB)`);

// ── assemble graph-context.json (compact LLM context) ───────────────────────
const lifecycleDist = {};
const languageDist = {};
for (const n of nodes) {
  lifecycleDist[n.lifecycle_stage] = (lifecycleDist[n.lifecycle_stage] ?? 0) + 1;
  if (n.primary_language) languageDist[n.primary_language] = (languageDist[n.primary_language] ?? 0) + 1;
}

const topByPagerank = [...nodes].sort((a, b) => b.pagerank - a.pagerank).slice(0, 20).map(n => ({
  full_name: n.full_name, stars: n.stars, community: n.community,
  lifecycle_stage: n.lifecycle_stage, topics: n.topics.slice(0, 5),
}));

const communityContext = Object.entries(communities).map(([id, c]) => ({
  id: parseInt(id), size: c.size,
  top_repos: c.top_repos,
  top_topics: c.top_topics,
  top_language: c.top_language,
})).sort((a, b) => b.size - a.size);

const graphContext = {
  summary: {
    total_repos: nodes.length,
    total_edges: links.length,
    communities: communityCount,
    lifecycle_distribution: lifecycleDist,
    top_languages: Object.entries(languageDist).sort((a, b) => b[1] - a[1]).slice(0, 10).map(([lang, count]) => ({ lang, count })),
  },
  most_influential: topByPagerank,
  communities: communityContext,
  computed_at: new Date().toISOString(),
};

writeFileSync(join(root, 'public/data/graph-context.json'), JSON.stringify(graphContext));
console.log(`   ✓ wrote public/data/graph-context.json`);
console.log('Done.');
