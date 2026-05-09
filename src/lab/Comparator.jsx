import React, { useMemo, useState } from 'react';
import { useGraph, STAGE_COLOR } from './GraphProvider';
import { compareRepos } from './queries';

function findPath(nodes, links, fullNameA, fullNameB) {
  const nodeA = nodes.find(n => n.full_name === fullNameA);
  const nodeB = nodes.find(n => n.full_name === fullNameB);
  if (!nodeA || !nodeB) return null;

  // BFS over adjacency
  const adj = new Map();
  for (const l of links) {
    const s = typeof l.source === 'object' ? l.source.id : l.source;
    const t = typeof l.target === 'object' ? l.target.id : l.target;
    if (!adj.has(s)) adj.set(s, []);
    if (!adj.has(t)) adj.set(t, []);
    adj.get(s).push({ id: t, link: l });
    adj.get(t).push({ id: s, link: l });
  }

  const queue = [[nodeA.id]];
  const visited = new Set([nodeA.id]);
  while (queue.length) {
    const path = queue.shift();
    const cur = path[path.length - 1];
    if (cur === nodeB.id) {
      // Reconstruct hops
      const nodeById = new Map(nodes.map(n => [n.id, n]));
      const hops = [];
      for (let i = 0; i < path.length - 1; i++) {
        const from = nodeById.get(path[i]);
        const to = nodeById.get(path[i + 1]);
        const link = adj.get(path[i])?.find(e => e.id === path[i + 1])?.link ?? {};
        hops.push({ from: from?.full_name, to: to?.full_name, to_stage: to?.lifecycle_stage, weight: link.weight ?? 0, shared_authors: link.shared_authors ?? [], shared_topics: link.shared_topics ?? [] });
      }
      return { found: true, length: hops.length, hops };
    }
    for (const { id } of adj.get(cur) ?? []) {
      if (!visited.has(id)) { visited.add(id); queue.push([...path, id]); }
    }
  }
  return { found: false };
}

function MetricRow({ label, a, b, fmt = (x) => x }) {
  return (
    <div className="grid grid-cols-3 gap-3 py-2 border-b border-gray-800">
      <div className="text-gray-400 text-sm">{label}</div>
      <div className="text-gray-100 text-sm">{fmt(a)}</div>
      <div className="text-gray-100 text-sm">{fmt(b)}</div>
    </div>
  );
}

export default function Comparator({ initialA, initialB }) {
  const { status, nodes = [], links = [] } = useGraph();
  const repoOptions = useMemo(() => (status === 'ready' ? nodes.map(n => n.full_name).sort() : []), [status, nodes]);

  const [a, setA] = useState(initialA ?? '');
  const [b, setB] = useState(initialB ?? '');
  React.useEffect(() => { if (initialA) setA(initialA); }, [initialA]);
  React.useEffect(() => { if (initialB) setB(initialB); }, [initialB]);

  const result = useMemo(() => {
    if (status !== 'ready' || !a || !b || a === b) return null;
    return compareRepos(nodes, links, a, b);
  }, [status, nodes, links, a, b]);

  const path = useMemo(() => {
    if (status !== 'ready' || !a || !b || a === b) return null;
    return findPath(nodes, links, a, b);
  }, [status, nodes, links, a, b]);

  if (status !== 'ready') return null;

  return (
    <div className="bg-gray-800 rounded-lg p-5">
      <h2 className="text-xl font-bold text-white mb-3">Compare two repos</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mb-5">
        <select value={a} onChange={(e) => setA(e.target.value)} className="px-3 py-2 bg-gray-700 text-white rounded-lg border border-gray-600">
          <option value="">Select first repo…</option>
          {repoOptions.map((n) => <option key={n} value={n}>{n}</option>)}
        </select>
        <select value={b} onChange={(e) => setB(e.target.value)} className="px-3 py-2 bg-gray-700 text-white rounded-lg border border-gray-600">
          <option value="">Select second repo…</option>
          {repoOptions.map((n) => <option key={n} value={n}>{n}</option>)}
        </select>
      </div>
      {!result && <div className="text-gray-500 text-sm">Pick two different repos to compare.</div>}
      {result && (
        <div className="space-y-4">
          <div className="grid grid-cols-3 gap-3 pb-2 border-b border-gray-700">
            <div className="text-gray-400 text-xs uppercase tracking-wide">Metric</div>
            <div className="text-blue-400 font-bold">{result.a.full_name}</div>
            <div className="text-blue-400 font-bold">{result.b.full_name}</div>
          </div>
          <MetricRow label="Stars" a={result.a.stars} b={result.b.stars} fmt={(x) => x?.toLocaleString()} />
          <MetricRow label="Lifecycle" a={result.a.lifecycle_stage} b={result.b.lifecycle_stage} />
          <MetricRow label="Health score" a={result.a.health_score} b={result.b.health_score} />
          <MetricRow label="Age (days)" a={result.a.age_days} b={result.b.age_days} fmt={(x) => x?.toLocaleString()} />
          <MetricRow label="Days since push" a={result.a.days_since_push} b={result.b.days_since_push} />
          <MetricRow label="Commits last 90d" a={result.a.commits_90d} b={result.b.commits_90d} />
          <MetricRow label="Authors last 90d" a={result.a.unique_authors_90d} b={result.b.unique_authors_90d} />
          <MetricRow label="Bus factor" a={result.a.bus_factor} b={result.b.bus_factor} />
          <MetricRow label="Primary language" a={result.a.primary_language ?? '—'} b={result.b.primary_language ?? '—'} />
          <MetricRow label="Topics" a={(result.a.topics ?? []).join(', ') || '—'} b={(result.b.topics ?? []).join(', ') || '—'} />
          <div className="bg-gray-900 rounded-lg p-4 mt-4">
            <h3 className="text-sm uppercase tracking-wide text-gray-400 mb-2">Relationship</h3>
            <div className="text-sm text-gray-200">
              {result.same_community ? <span className="text-green-400">Same community ({result.a.community})</span> : <span className="text-gray-400">Different communities ({result.a.community} vs {result.b.community})</span>}
            </div>
            {result.edge ? (
              <>
                <div className="text-sm text-gray-200 mt-2">Direct edge weight: {result.edge.weight.toFixed(2)}</div>
                {result.edge.shared_topics?.length > 0 && <div className="text-sm text-gray-300 mt-1">Shared topics: <span className="text-cyan-300">{result.edge.shared_topics.join(', ')}</span></div>}
                {result.edge.shared_authors?.length > 0 && <div className="text-sm text-gray-300 mt-1">Shared authors: <span className="text-yellow-300">{result.edge.shared_authors.join(', ')}</span></div>}
              </>
            ) : <div className="text-sm text-gray-500 mt-2">No direct edge.</div>}
          </div>
          {path && (
            <div className="bg-gray-900 rounded-lg p-4">
              <h3 className="text-sm uppercase tracking-wide text-gray-400 mb-2">Shortest path through the graph</h3>
              {!path.found && <div className="text-sm text-gray-500">No path found.</div>}
              {path.found && (
                <>
                  <div className="text-sm text-gray-300 mb-3">{path.length} hop{path.length === 1 ? '' : 's'}</div>
                  <ol className="space-y-2">
                    {path.hops.map((hop, i) => (
                      <li key={i} className="bg-gray-800 rounded p-2">
                        <div className="flex items-center gap-2 text-sm">
                          <span className="text-gray-300">{hop.from}</span>
                          <span className="text-gray-500">→</span>
                          <span className="text-blue-400">{hop.to}</span>
                          <span className="px-2 py-0.5 rounded-full text-[10px] font-bold" style={{ backgroundColor: STAGE_COLOR[hop.to_stage], color: '#0a0a0a' }}>{hop.to_stage}</span>
                          <span className="text-xs text-gray-500 ml-auto">w={hop.weight.toFixed(2)}</span>
                        </div>
                        {hop.shared_topics.length > 0 && <div className="text-xs text-cyan-400 mt-1">topics: {hop.shared_topics.slice(0, 4).join(', ')}</div>}
                      </li>
                    ))}
                  </ol>
                </>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
