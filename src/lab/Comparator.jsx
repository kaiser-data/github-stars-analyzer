import React, { useMemo, useState } from 'react';
import { useGraph } from './GraphProvider';
import { compareRepos } from './queries';

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
                <div className="text-sm text-gray-200 mt-2">Edge weight: {result.edge.weight.toFixed(2)}</div>
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
              <div className="text-sm text-gray-500 mt-2">No direct edge — these repos share no significant signal.</div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
