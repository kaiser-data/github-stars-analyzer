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

  // Compute edges: SHARED_TOPIC, SHARED_AUTHOR, SHARED_LANGUAGE
  // Stored as one undirected edge per pair with composite weight + reasons.
  const repos = classified.repos;
  const topicSets = new Map();
  const authorSets = new Map();
  for (const r of repos) {
    topicSets.set(r.id, new Set(r.topics ?? []));
    const authors = (r.authors_90d ?? []).map((a) => a.login).filter(Boolean);
    authorSets.set(r.id, new Set(authors));
  }

  let edgeCount = 0;
  for (let i = 0; i < repos.length; i += 1) {
    for (let j = i + 1; j < repos.length; j += 1) {
      const a = repos[i];
      const b = repos[j];
      const reasons = [];
      let weight = 0;

      const topicSim = jaccard(topicSets.get(a.id), topicSets.get(b.id));
      if (topicSim > 0.15) {
        weight += topicSim * 1.0;
        reasons.push({ kind: 'topic', score: topicSim });
      }

      const authorSim = jaccard(authorSets.get(a.id), authorSets.get(b.id));
      if (authorSim > 0) {
        weight += authorSim * 2.0; // shared contributors weigh more
        reasons.push({ kind: 'author', score: authorSim });
      }

      if (a.primary_language && a.primary_language === b.primary_language) {
        weight += 0.05;
        reasons.push({ kind: 'language', score: 1, language: a.primary_language });
      }

      if (a.owner === b.owner) {
        weight += 0.5;
        reasons.push({ kind: 'owner', score: 1, owner: a.owner });
      }

      if (weight > 0.18) {
        g.addEdge(`repo:${a.id}`, `repo:${b.id}`, {
          weight,
          reasons,
          shared_topics: [...topicSets.get(a.id)].filter((t) => topicSets.get(b.id).has(t)),
          shared_authors: [...authorSets.get(a.id)].filter((u) => authorSets.get(b.id).has(u)),
        });
        edgeCount += 1;
      }
    }
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
        const classifiedRes = await fetch('/data/classified-100.json');
        if (!classifiedRes.ok) throw new Error(`classified-100.json: ${classifiedRes.status}`);
        const classified = await classifiedRes.json();

        let enriched = null;
        try {
          const r = await fetch('/data/enriched-100.json');
          if (r.ok) enriched = await r.json();
        } catch { /* enrichment optional */ }

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
