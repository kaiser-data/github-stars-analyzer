import React, { createContext, useContext, useEffect, useMemo, useState } from 'react';
import Graph from 'graphology';
import louvain from 'graphology-communities-louvain';
import pagerank from 'graphology-metrics/centrality/pagerank.js';

const GraphContext = createContext(null);

const STAGE_COLOR = {
  Hot: '#ef4444',
  Rising: '#f59e0b',
  Classic: '#10b981',
  Mature: '#3b82f6',
  Declining: '#a78bfa',
  Abandoned: '#6b7280',
};

function jaccard(setA, setB) {
  if (setA.size === 0 || setB.size === 0) return 0;
  let inter = 0;
  for (const x of setA) if (setB.has(x)) inter += 1;
  return inter / (setA.size + setB.size - inter);
}

function buildGraph(classified, enriched) {
  const enrichmentById = new Map();
  for (const e of enriched ?? []) enrichmentById.set(e.id, e);

  const g = new Graph({ type: 'undirected', multi: false });

  // Nodes: repos
  for (const r of classified.repos) {
    const enrich = enrichmentById.get(r.id) ?? {};
    g.addNode(`repo:${r.id}`, {
      kind: 'repo',
      id: r.id,
      label: r.full_name,
      full_name: r.full_name,
      description: r.description,
      stars: r.stars,
      language: r.primary_language,
      topics: r.topics,
      lifecycle_stage: r.lifecycle_stage,
      health_score: r.health_score,
      bus_factor: r.bus_factor,
      age_days: r.age_days,
      days_since_push: r.days_since_push,
      commits_90d: r.commits_90d,
      unique_authors_90d: r.unique_authors_90d,
      authors_90d: r.authors_90d,
      open_issues: r.open_issues,
      closed_issues: r.closed_issues,
      releases_total: r.releases_total,
      momentum: r.momentum,
      stratum: r.stratum,
      url: r.url,
      readme_text: r.readme_text,
      // Enriched fields (may be undefined)
      one_liner: enrich.one_liner,
      primary_use_case: enrich.primary_use_case,
      audience: enrich.audience,
      category: enrich.category,
      alternatives_mentioned: enrich.alternatives_mentioned,
      key_concepts: enrich.key_concepts,
      maturity_signal: enrich.maturity_signal,
      domain_tags: enrich.domain_tags,
      color: STAGE_COLOR[r.lifecycle_stage] ?? '#6b7280',
      size: 4 + Math.log10(1 + Math.max(0, r.stars)) * 2.5,
    });
  }

  // Compute edges via k-NN backbone: every repo gets edges to its top-K most
  // similar peers regardless of absolute weight. Strong edges (≥STRONG) are
  // always kept on top of that. Guarantees connectivity on sparse samples; weak
  // edges still carry low weight so PageRank/Louvain naturally discount them.
  const K = 4;
  const STRONG = 1.0;

  const repos = classified.repos;
  const topicSets = new Map();
  const authorSets = new Map();
  for (const r of repos) {
    topicSets.set(r.id, new Set(r.topics ?? []));
    const authors = (r.authors_90d ?? []).map((a) => a.login).filter(Boolean);
    authorSets.set(r.id, new Set(authors));
  }

  // Pass 1: O(n²) weight sweep — store only [j_index, weight] tuples.
  // Deferring sharedTopics/sharedAuthors to pass 3 avoids allocating those
  // arrays for all ~530K candidate pairs (only ~4K are kept).
  const pairsOf = repos.map(() => /** @type {[number,number][]} */ ([]));

  for (let i = 0; i < repos.length; i += 1) {
    const a = repos[i];
    const aTopic = topicSets.get(a.id);
    const aAuthor = authorSets.get(a.id);
    for (let j = i + 1; j < repos.length; j += 1) {
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

  // Pass 2: keep top-K per node + every above-STRONG edge (using array indices).
  const keepEdges = new Set(); // "min_i-max_i" index keys
  for (let i = 0; i < repos.length; i += 1) {
    const pairs = pairsOf[i];
    if (!pairs.length) continue;
    pairs.sort((x, y) => y[1] - x[1]);
    for (let k = 0; k < Math.min(K, pairs.length); k += 1) {
      const j = pairs[k][0];
      keepEdges.add(i < j ? `${i}-${j}` : `${j}-${i}`);
    }
    for (const [j, w] of pairs) {
      if (w < STRONG) break; // sorted desc — stop early
      keepEdges.add(i < j ? `${i}-${j}` : `${j}-${i}`);
    }
  }

  // Pass 3: add kept edges — compute shared arrays only for the ~4K survivors.
  let edgeCount = 0;
  for (let i = 0; i < repos.length; i += 1) {
    for (const [j, w] of pairsOf[i]) {
      if (j <= i) continue; // process each pair exactly once from the lower-index side
      if (!keepEdges.has(`${i}-${j}`)) continue;
      const a = repos[i], b = repos[j];
      const aTopic = topicSets.get(a.id), bTopic = topicSets.get(b.id);
      const aAuthor = authorSets.get(a.id), bAuthor = authorSets.get(b.id);
      g.addEdge(`repo:${a.id}`, `repo:${b.id}`, {
        weight: w,
        shared_topics: [...aTopic].filter((t) => bTopic.has(t)),
        shared_authors: [...aAuthor].filter((u) => bAuthor.has(u)),
      });
      edgeCount += 1;
    }
  }

  // Pass 4: fallback for repos with zero signal at all (no topics/authors/lang/owner-overlap).
  // Attach each orphan to the highest-star repo sharing its lifecycle_stage so the graph
  // stays connected and the Louvain communities still have a sensible bucket for them.
  const stagePivots = new Map();
  for (const r of repos) {
    const cur = stagePivots.get(r.lifecycle_stage);
    if (!cur || r.stars > cur.stars) stagePivots.set(r.lifecycle_stage, r);
  }
  for (const r of repos) {
    if (g.degree(`repo:${r.id}`) > 0) continue;
    const pivot = stagePivots.get(r.lifecycle_stage);
    if (!pivot || pivot.id === r.id) continue;
    g.addEdge(`repo:${r.id}`, `repo:${pivot.id}`, {
      weight: 0.05,
      reasons: [{ kind: 'lifecycle_fallback', score: 1, stage: r.lifecycle_stage }],
      shared_topics: [],
      shared_authors: [],
    });
    edgeCount += 1;
  }

  // Louvain community detection on weighted edges
  let communityCount = 0;
  if (edgeCount > 0) {
    const detail = louvain.detailed(g, { getEdgeWeight: 'weight' });
    g.forEachNode((n, attrs) => {
      g.setNodeAttribute(n, 'community', detail.communities[n]);
    });
    communityCount = new Set(Object.values(detail.communities)).size;
  } else {
    g.forEachNode((n) => g.setNodeAttribute(n, 'community', 0));
    communityCount = 1;
  }

  // Per-node degree (used for sizing later)
  g.forEachNode((n) => {
    g.setNodeAttribute(n, 'degree', g.degree(n));
  });

  // PageRank — structural importance, weighted by edge weight
  if (edgeCount > 0) {
    pagerank.assign(g, { getEdgeWeight: 'weight', alpha: 0.85, maxIterations: 100, tolerance: 1e-6 });
    // assigns under attribute name 'pagerank' by default
  } else {
    g.forEachNode((n) => g.setNodeAttribute(n, 'pagerank', 0));
  }

  return { graph: g, stats: { nodeCount: g.order, edgeCount, communityCount } };
}

export function GraphProvider({ children }) {
  const [state, setState] = useState({ status: 'loading', graph: null, stats: null, error: null, hasEnrichment: false });

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        // Try the size-agnostic filename first (latest snapshot), fall back to the
        // committed 100-repo demo dataset.
        let classified = null;
        for (const path of ['/data/classified.json', '/data/classified-100.json']) {
          try {
            const r = await fetch(path);
            if (r.ok) { classified = await r.json(); break; }
          } catch { /* try next */ }
        }
        if (!classified) throw new Error('No classified data found');

        let enriched = null;
        for (const path of ['/data/enriched.json', '/data/enriched-100.json']) {
          try {
            const r = await fetch(path);
            if (r.ok) { enriched = await r.json(); break; }
          } catch { /* enrichment optional */ }
        }

        // Yield to the browser before the O(n²) graph build so the loading
        // state renders before we block the main thread.
        await new Promise((resolve) => setTimeout(resolve, 0));
        if (cancelled) return;

        const { graph, stats } = buildGraph(classified, enriched);
        if (!cancelled) {
          setState({
            status: 'ready',
            graph,
            stats,
            classified,
            enriched,
            hasEnrichment: enriched != null,
            error: null,
          });
        }
      } catch (err) {
        if (!cancelled) setState({ status: 'error', graph: null, error: err.message });
      }
    })();
    return () => { cancelled = true; };
  }, []);

  return <GraphContext.Provider value={state}>{children}</GraphContext.Provider>;
}

export function useGraph() {
  const ctx = useContext(GraphContext);
  if (!ctx) throw new Error('useGraph must be inside GraphProvider');
  return ctx;
}

export { STAGE_COLOR };
