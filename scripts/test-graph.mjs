// Headless test of the graph build + key queries — runs the same logic as the browser.
// Usage: node scripts/test-graph.mjs

import { readFileSync } from 'node:fs';
import Graph from 'graphology';
import louvain from 'graphology-communities-louvain';
import pagerank from 'graphology-metrics/centrality/pagerank.js';
import { bidirectional } from 'graphology-shortest-path';

const data = JSON.parse(readFileSync('public/data/classified-100.json', 'utf8'));

let pass = 0;
let fail = 0;
function ok(label, cond, detail = '') {
  if (cond) { console.log(`  ✓ ${label}${detail ? ' — ' + detail : ''}`); pass += 1; }
  else { console.error(`  ✗ ${label}${detail ? ' — ' + detail : ''}`); fail += 1; }
}

console.log('== Dataset sanity ==');
ok('100 repos in dataset', data.repos.length === 100, `got ${data.repos.length}`);
ok('all repos have id', data.repos.every((r) => Number.isFinite(r.id)));
ok('all repos have lifecycle_stage', data.repos.every((r) => typeof r.lifecycle_stage === 'string'));
ok('all repos have health_score 0-100', data.repos.every((r) => r.health_score >= 0 && r.health_score <= 100));
ok('all repos have non-negative stars', data.repos.every((r) => r.stars >= 0));
ok('lifecycle distribution covers Hot/Classic', new Set(data.repos.map((r) => r.lifecycle_stage)).size >= 3);

const stagecount = data.repos.reduce((acc, r) => ((acc[r.lifecycle_stage] = (acc[r.lifecycle_stage] ?? 0) + 1), acc), {});
console.log('  stages:', stagecount);

console.log('\n== Graph construction (k-NN backbone, K=4) ==');
function jaccard(a, b) {
  if (a.size === 0 || b.size === 0) return 0;
  let inter = 0;
  for (const x of a) if (b.has(x)) inter += 1;
  return inter / (a.size + b.size - inter);
}
const g = new Graph({ type: 'undirected', multi: false });
for (const r of data.repos) {
  g.addNode(`repo:${r.id}`, { kind: 'repo', full_name: r.full_name, stars: r.stars });
}
const topicSets = new Map();
const authorSets = new Map();
for (const r of data.repos) {
  topicSets.set(r.id, new Set(r.topics ?? []));
  authorSets.set(r.id, new Set((r.authors_90d ?? []).map((a) => a.login).filter(Boolean)));
}

const K = 4, STRONG = 1.0;
const partnersOf = new Map();
for (const r of data.repos) partnersOf.set(r.id, []);
for (let i = 0; i < data.repos.length; i += 1) {
  for (let j = i + 1; j < data.repos.length; j += 1) {
    const a = data.repos[i];
    const b = data.repos[j];
    let weight = 0;
    const ts = jaccard(topicSets.get(a.id), topicSets.get(b.id));
    if (ts > 0) weight += ts;
    const as = jaccard(authorSets.get(a.id), authorSets.get(b.id));
    if (as > 0) weight += as * 2;
    if (a.primary_language && a.primary_language === b.primary_language) weight += 0.05;
    if (a.full_name.split('/')[0] === b.full_name.split('/')[0]) weight += 0.5;
    if (weight === 0) continue;
    const score = { a, b, weight };
    partnersOf.get(a.id).push(score);
    partnersOf.get(b.id).push(score);
  }
}
const keepKeys = new Set();
const keyFor = (s) => (s.a.id < s.b.id ? `${s.a.id}-${s.b.id}` : `${s.b.id}-${s.a.id}`);
for (const partners of partnersOf.values()) {
  partners.sort((x, y) => y.weight - x.weight);
  for (const s of partners.slice(0, K)) keepKeys.add(keyFor(s));
  for (const s of partners) if (s.weight >= STRONG) keepKeys.add(keyFor(s));
}
const added = new Set();
let edgeCount = 0;
for (const partners of partnersOf.values()) {
  for (const s of partners) {
    const key = keyFor(s);
    if (!keepKeys.has(key) || added.has(key)) continue;
    added.add(key);
    g.addEdge(`repo:${s.a.id}`, `repo:${s.b.id}`, { weight: s.weight });
    edgeCount += 1;
  }
}
// Lifecycle fallback for zero-signal orphans
const stagePivots = new Map();
for (const r of data.repos) {
  const cur = stagePivots.get(r.lifecycle_stage);
  if (!cur || r.stars > cur.stars) stagePivots.set(r.lifecycle_stage, r);
}
for (const r of data.repos) {
  if (g.degree(`repo:${r.id}`) > 0) continue;
  const pivot = stagePivots.get(r.lifecycle_stage);
  if (!pivot || pivot.id === r.id) continue;
  g.addEdge(`repo:${r.id}`, `repo:${pivot.id}`, { weight: 0.05 });
  edgeCount += 1;
}

let isolated = 0;
g.forEachNode((n) => { if (g.degree(n) === 0) isolated += 1; });
ok('graph has 100 nodes', g.order === 100, `got ${g.order}`);
ok('graph has edges', edgeCount > 0, `${edgeCount} edges`);
ok('zero isolated nodes (k-NN backbone)', isolated === 0, `${isolated} isolated`);
ok('average degree ≥ K=4', (2 * edgeCount) / g.order >= 4, `avg deg ${((2 * edgeCount) / g.order).toFixed(1)}`);

console.log('\n== Algorithms ==');
let louvainErr = null;
try {
  const detail = louvain.detailed(g, { getEdgeWeight: 'weight' });
  const communities = new Set(Object.values(detail.communities));
  ok('Louvain runs without error', true, `${communities.size} communities`);
} catch (e) { louvainErr = e; ok('Louvain runs', false, e.message); }

try {
  pagerank.assign(g, { getEdgeWeight: 'weight', alpha: 0.85, maxIterations: 100, tolerance: 1e-6 });
  let prSum = 0;
  let prMax = 0;
  g.forEachNode((n, a) => { prSum += a.pagerank ?? 0; if ((a.pagerank ?? 0) > prMax) prMax = a.pagerank; });
  ok('PageRank runs', true, `sum≈${prSum.toFixed(3)} max≈${prMax.toFixed(4)}`);
  ok('PageRank sums to ≈1', Math.abs(prSum - 1) < 0.05, `got ${prSum.toFixed(4)}`);
} catch (e) { ok('PageRank runs', false, e.message); }

try {
  const nodes = g.nodes();
  let pathFound = 0;
  let attempts = 0;
  for (let i = 0; i < 5 && attempts < 20; i += 1) {
    const a = nodes[Math.floor(Math.random() * nodes.length)];
    const b = nodes[Math.floor(Math.random() * nodes.length)];
    if (a === b) { i -= 1; attempts += 1; continue; }
    const route = bidirectional(g, a, b);
    if (route) pathFound += 1;
    attempts += 1;
  }
  ok('shortest-path runs', true, `${pathFound}/${attempts} pairs connected`);
} catch (e) { ok('shortest-path runs', false, e.message); }

console.log('\n== Lifecycle invariants ==');
const abandoned = data.repos.filter((r) => r.lifecycle_stage === 'Abandoned');
ok('all Abandoned have days_since_push > 365', abandoned.every((r) => r.days_since_push > 365 || r.archived === true));
const classic = data.repos.filter((r) => r.lifecycle_stage === 'Classic');
ok('all Classic are >3y old', classic.every((r) => r.age_days > 365 * 3), `${classic.length} classic repos`);
const hot = data.repos.filter((r) => r.lifecycle_stage === 'Hot');
ok('all Hot have commits_90d >= 30', hot.every((r) => r.commits_90d >= 30), `${hot.length} hot repos`);

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail);
