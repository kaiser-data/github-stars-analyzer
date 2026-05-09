// Named graph queries — graphology-based, run synchronously over the in-memory graph.
// Each query is a function (graph, opts) => array of result rows.

const STAGE_RANK = { Hot: 6, Rising: 5, Classic: 4, Mature: 3, Declining: 2, Abandoned: 1 };

// nodes is now the pre-computed array from graph.json
function repoNodes(nodes) { return nodes; }

export const QUERIES = {
  whereDevsWork: {
    title: 'Where developers actually work',
    description: 'Top repos by unique authors active in the last 90 days.',
    run: (graph) => {
      return repoNodes(graph)
        .filter((r) => r.unique_authors_90d > 0)
        .sort((a, b) => b.unique_authors_90d - a.unique_authors_90d || b.commits_90d - a.commits_90d)
        .slice(0, 20)
        .map((r) => ({
          full_name: r.full_name,
          authors_90d: r.unique_authors_90d,
          commits_90d: r.commits_90d,
          stage: r.lifecycle_stage,
          stars: r.stars,
        }));
    },
  },

  classicCore: {
    title: 'The classic core of your stars',
    description: 'Old, still healthy, sustained activity — the standards everyone keeps coming back to.',
    run: (graph) => {
      return repoNodes(graph)
        .filter((r) => r.lifecycle_stage === 'Classic')
        .sort((a, b) => b.health_score - a.health_score)
        .slice(0, 15)
        .map((r) => ({
          full_name: r.full_name,
          age_years: (r.age_days / 365).toFixed(1),
          health_score: r.health_score,
          authors_90d: r.unique_authors_90d,
          stars: r.stars,
        }));
    },
  },

  hotRepos: {
    title: 'Hot repos in your stars',
    description: 'Recent, very active, multi-author. These are the ones moving fastest right now.',
    run: (graph) => {
      return repoNodes(graph)
        .filter((r) => r.lifecycle_stage === 'Hot' || r.lifecycle_stage === 'Rising')
        .sort((a, b) => b.commits_90d - a.commits_90d)
        .slice(0, 20)
        .map((r) => ({
          full_name: r.full_name,
          stage: r.lifecycle_stage,
          age_days: r.age_days,
          commits_90d: r.commits_90d,
          authors_90d: r.unique_authors_90d,
          stars: r.stars,
        }));
    },
  },

  busFactorRisks: {
    title: 'Bus-factor risks',
    description: 'Active repos where one person owns the lions share of recent commits.',
    run: (graph) => {
      return repoNodes(graph)
        .filter((r) => r.commits_90d >= 10 && r.bus_factor === 1 && r.lifecycle_stage !== 'Abandoned')
        .sort((a, b) => b.commits_90d - a.commits_90d)
        .slice(0, 15)
        .map((r) => ({
          full_name: r.full_name,
          stage: r.lifecycle_stage,
          commits_90d: r.commits_90d,
          top_author: r.authors_90d?.[0]?.login,
          top_share_pct: Math.round((r.authors_90d?.[0]?.commits / r.commits_90d) * 100),
          stars: r.stars,
        }));
    },
  },

  decliningFormerlyHot: {
    title: 'Declining repos that may need replacing',
    description: 'High stars but cold lately. Candidates to look for modern alternatives.',
    run: (graph) => {
      return repoNodes(graph)
        .filter((r) => (r.lifecycle_stage === 'Declining' || r.lifecycle_stage === 'Abandoned') && r.stars > 1000)
        .sort((a, b) => b.stars - a.stars)
        .slice(0, 15)
        .map((r) => ({
          full_name: r.full_name,
          stage: r.lifecycle_stage,
          days_since_push: r.days_since_push,
          stars: r.stars,
        }));
    },
  },

  hiddenClusterLeaders: {
    title: 'Cluster leaders (PageRank-central in your graph)',
    description: 'Repos most structurally important in your starred network. PageRank weights connections through other influential repos higher than raw degree.',
    run: (graph) => {
      return repoNodes(graph)
        .sort((a, b) => (b.pagerank ?? 0) - (a.pagerank ?? 0))
        .slice(0, 15)
        .map((r) => ({
          full_name: r.full_name,
          pagerank: Number(((r.pagerank ?? 0) * 1000).toFixed(2)),
          degree: graph.degree(`repo:${r.id}`),
          community: r.community,
          stage: r.lifecycle_stage,
          stars: r.stars,
        }));
    },
  },

  ownerHotspots: {
    title: 'Owners with the most repos in your stars',
    description: 'Which orgs/users dominate your starred set.',
    run: (graph) => {
      const counts = new Map();
      for (const r of repoNodes(graph)) {
        const owner = r.full_name.split('/')[0];
        counts.set(owner, (counts.get(owner) ?? 0) + 1);
      }
      return [...counts.entries()]
        .filter(([, c]) => c >= 2)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 15)
        .map(([owner, count]) => ({ owner, count }));
    },
  },

  communityBreakdown: {
    title: 'Communities in your starred graph',
    description: 'Louvain-detected clusters: which themes hold your stars together.',
    run: (graph) => {
      const buckets = new Map();
      for (const r of repoNodes(graph)) {
        const c = r.community ?? 0;
        if (!buckets.has(c)) buckets.set(c, []);
        buckets.get(c).push(r);
      }
      return [...buckets.entries()]
        .map(([id, members]) => {
          const topicCounts = new Map();
          for (const m of members) for (const t of m.topics ?? []) topicCounts.set(t, (topicCounts.get(t) ?? 0) + 1);
          const topTopics = [...topicCounts.entries()]
            .sort((a, b) => b[1] - a[1])
            .slice(0, 5)
            .map(([t]) => t);
          const topMembers = [...members]
            .sort((a, b) => b.stars - a.stars)
            .slice(0, 5)
            .map((m) => m.full_name);
          return {
            community: id,
            size: members.length,
            top_topics: topTopics,
            top_repos: topMembers,
          };
        })
        .sort((a, b) => b.size - a.size);
    },
  },
};

export function compareRepos(nodes, links, fullNameA, fullNameB) {
  const a = nodes.find(n => n.full_name === fullNameA);
  const b = nodes.find(n => n.full_name === fullNameB);
  if (!a || !b) return null;
  const edge = links.find(l => {
    const s = typeof l.source === 'object' ? l.source.id : l.source;
    const t = typeof l.target === 'object' ? l.target.id : l.target;
    return (s === a.id && t === b.id) || (s === b.id && t === a.id);
  }) ?? null;
  return {
    a, b, edge,
    same_community: a.community === b.community,
    diff: {
      stars: a.stars - b.stars,
      health: a.health_score - b.health_score,
      authors_90d: a.unique_authors_90d - b.unique_authors_90d,
      age_days: a.age_days - b.age_days,
      stage_rank_diff: (STAGE_RANK[a.lifecycle_stage] ?? 0) - (STAGE_RANK[b.lifecycle_stage] ?? 0),
    },
  };
}
