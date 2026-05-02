import React, { useMemo, useState } from 'react';
import { bidirectional } from 'graphology-shortest-path';
import { useGraph, STAGE_COLOR } from './GraphProvider';
import { compareRepos } from './queries';

function findNodeId(graph, fullName) {
  let id = null;
  graph.forEachNode((n, a) => { if (a.kind === 'repo' && a.full_name === fullName) id = n; });
  return id;
}

function pathDetails(graph, path) {
  if (!path || path.length < 2) return [];
  const hops = [];
  for (let i = 0; i < path.length - 1; i += 1) {
    const from = path[i];
    const to = path[i + 1];
    const fromAttrs = graph.getNodeAttributes(from);
    const toAttrs = graph.getNodeAttributes(to);
    const edge = graph.getEdgeAttributes(from, to);
    hops.push({
      from: fromAttrs.full_name,
      to: toAttrs.full_name,
      to_stage: toAttrs.lifecycle_stage,
      weight: edge.weight,
      shared_authors: edge.shared_authors ?? [],
      shared_topics: edge.shared_topics ?? [],
    });
  }
  return hops;
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

export default function Comparator() {
  const { status, graph } = useGraph();
  const repoOptions = useMemo(() => {
    if (status !== 'ready') return [];
    const out = [];
    graph.forEachNode((n, a) => { if (a.kind === 'repo') out.push(a.full_name); });
    return out.sort();
  }, [status, graph]);

  const [a, setA] = useState('');
  const [b, setB] = useState('');
  const result = useMemo(() => {
    if (status !== 'ready' || !a || !b || a === b) return null;
    return compareRepos(graph, a, b);
  }, [status, graph, a, b]);

  const path = useMemo(() => {
    if (status !== 'ready' || !a || !b || a === b) return null;
    const ida = findNodeId(graph, a);
    const idb = findNodeId(graph, b);
    if (!ida || !idb) return null;
    const route = bidirectional(graph, ida, idb);
    if (!route) return { found: false };
    return { found: true, length: route.length - 1, hops: pathDetails(graph, route) };
  }, [status, graph, a, b]);

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
          <MetricRow label="Primary language" a={result.a.language ?? '—'} b={result.b.language ?? '—'} />
          <MetricRow label="Topics" a={(result.a.topics ?? []).join(', ') || '—'} b={(result.b.topics ?? []).join(', ') || '—'} />

          <div className="bg-gray-900 rounded-lg p-4 mt-4">
            <h3 className="text-sm uppercase tracking-wide text-gray-400 mb-2">Relationship</h3>
            <div className="text-sm text-gray-200">
              {result.same_community ? (
                <span className="text-green-400">Same community ({result.a.community})</span>
              ) : (
                <span className="text-gray-400">Different communities ({result.a.community} vs {result.b.community})</span>
              )}
            </div>
            {result.edge ? (
              <>
                <div className="text-sm text-gray-200 mt-2">Direct edge weight: {result.edge.weight.toFixed(2)}</div>
                {result.edge.shared_authors?.length > 0 && (
                  <div className="text-sm text-gray-300 mt-1">
                    Shared authors (last 90d): <span className="text-yellow-300">{result.edge.shared_authors.join(', ')}</span>
                  </div>
                )}
                {result.edge.shared_topics?.length > 0 && (
                  <div className="text-sm text-gray-300 mt-1">
                    Shared topics: <span className="text-cyan-300">{result.edge.shared_topics.join(', ')}</span>
                  </div>
                )}
                {result.edge.reasons?.length > 0 && (
                  <div className="text-xs text-gray-500 mt-2">
                    Reasons: {result.edge.reasons.map((r) => r.kind).join(', ')}
                  </div>
                )}
              </>
            ) : (
              <div className="text-sm text-gray-500 mt-2">No direct edge.</div>
            )}
          </div>

          {path && (
            <div className="bg-gray-900 rounded-lg p-4">
              <h3 className="text-sm uppercase tracking-wide text-gray-400 mb-2">Shortest path through the graph</h3>
              {!path.found && <div className="text-sm text-gray-500">No path — these repos are in disconnected parts of your graph.</div>}
              {path.found && (
                <>
                  <div className="text-sm text-gray-300 mb-3">{path.length} hop{path.length === 1 ? '' : 's'} via shared authors / topics / owners.</div>
                  <ol className="space-y-2">
                    {path.hops.map((hop, i) => (
                      <li key={i} className="bg-gray-800 rounded p-2">
                        <div className="flex items-center gap-2 text-sm">
                          <span className="text-gray-300">{hop.from}</span>
                          <span className="text-gray-500">→</span>
                          <span className="text-blue-400">{hop.to}</span>
                          <span
                            className="px-2 py-0.5 rounded-full text-[10px] font-bold"
                            style={{ backgroundColor: STAGE_COLOR[hop.to_stage], color: '#0a0a0a' }}
                          >{hop.to_stage}</span>
                          <span className="text-xs text-gray-500 ml-auto">w={hop.weight.toFixed(2)}</span>
                        </div>
                        {hop.shared_authors.length > 0 && (
                          <div className="text-xs text-yellow-400 mt-1 truncate">authors: {hop.shared_authors.slice(0, 3).join(', ')}</div>
                        )}
                        {hop.shared_topics.length > 0 && (
                          <div className="text-xs text-cyan-400 mt-1 truncate">topics: {hop.shared_topics.slice(0, 4).join(', ')}</div>
                        )}
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
