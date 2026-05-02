import React from 'react';
import { useGraph, STAGE_COLOR } from './GraphProvider';

function StageBadge({ stage }) {
  return (
    <span
      className="px-2 py-0.5 rounded-full text-xs font-bold"
      style={{ backgroundColor: STAGE_COLOR[stage] ?? '#6b7280', color: '#0a0a0a' }}
    >
      {stage}
    </span>
  );
}

function HealthBar({ score }) {
  const pct = Math.max(0, Math.min(100, score));
  const color = pct >= 70 ? '#10b981' : pct >= 50 ? '#3b82f6' : pct >= 30 ? '#f59e0b' : '#ef4444';
  return (
    <div className="flex items-center gap-2">
      <div className="flex-1 h-2 bg-gray-700 rounded-full overflow-hidden">
        <div style={{ width: `${pct}%`, backgroundColor: color }} className="h-full" />
      </div>
      <span className="text-xs text-gray-300 w-8 text-right">{score}</span>
    </div>
  );
}

function MetricCell({ label, value }) {
  return (
    <div className="bg-gray-900 rounded-md p-2">
      <div className="text-[10px] uppercase tracking-wider text-gray-500">{label}</div>
      <div className="text-sm font-semibold text-gray-100">{value}</div>
    </div>
  );
}

function findNeighbors(graph, nodeId, limit = 8) {
  if (!graph.hasNode(nodeId)) return [];
  const neighbors = [];
  graph.forEachEdge(nodeId, (edge, attrs, source, target) => {
    const otherId = source === nodeId ? target : source;
    const other = graph.getNodeAttributes(otherId);
    neighbors.push({
      full_name: other.full_name,
      weight: attrs.weight,
      shared_authors: attrs.shared_authors ?? [],
      shared_topics: attrs.shared_topics ?? [],
      lifecycle_stage: other.lifecycle_stage,
      stars: other.stars,
    });
  });
  return neighbors.sort((a, b) => b.weight - a.weight).slice(0, limit);
}

export default function RepoDetail({ repoFullName, onClose }) {
  const { graph } = useGraph();
  if (!repoFullName) return null;

  let nodeId = null;
  let attrs = null;
  graph.forEachNode((n, a) => {
    if (a.kind === 'repo' && a.full_name === repoFullName) {
      nodeId = n;
      attrs = a;
    }
  });
  if (!attrs) return null;

  const neighbors = findNeighbors(graph, nodeId);
  const topAuthors = (attrs.authors_90d ?? []).slice(0, 5);
  const recentRelease = attrs.releases_total > 0 ? `${attrs.releases_total} releases` : 'no releases';
  const readmeExcerpt = (attrs.readme_text ?? '').slice(0, 1200);

  return (
    <div className="fixed inset-y-0 right-0 w-full md:w-[600px] bg-gray-900 border-l border-gray-700 shadow-2xl overflow-y-auto z-50">
      <div className="sticky top-0 bg-gray-900 border-b border-gray-800 p-4 flex items-start justify-between gap-3">
        <div className="min-w-0 flex-1">
          <div className="flex items-center gap-2 flex-wrap">
            <a
              href={attrs.url || `https://github.com/${attrs.full_name}`}
              target="_blank"
              rel="noopener noreferrer"
              className="text-xl font-bold text-blue-400 hover:text-blue-300 break-all"
            >
              {attrs.full_name}
            </a>
            <StageBadge stage={attrs.lifecycle_stage} />
          </div>
          <div className="text-sm text-gray-400 mt-1 line-clamp-2">{attrs.description}</div>
          {attrs.one_liner && <div className="text-sm text-gray-200 mt-2 italic">{attrs.one_liner}</div>}
        </div>
        <button onClick={onClose} className="text-gray-400 hover:text-white text-2xl leading-none">×</button>
      </div>

      <div className="p-4 space-y-5">
        <div>
          <div className="text-xs uppercase tracking-wider text-gray-500 mb-1">Health</div>
          <HealthBar score={attrs.health_score} />
        </div>

        <div className="grid grid-cols-3 gap-2">
          <MetricCell label="Stars" value={attrs.stars?.toLocaleString()} />
          <MetricCell label="Age" value={`${Math.round(attrs.age_days / 365 * 10) / 10}y`} />
          <MetricCell label="Last push" value={`${attrs.days_since_push}d ago`} />
          <MetricCell label="Commits 90d" value={attrs.commits_90d?.toLocaleString()} />
          <MetricCell label="Authors 90d" value={attrs.unique_authors_90d} />
          <MetricCell label="Bus factor" value={attrs.bus_factor} />
          <MetricCell label="Open issues" value={attrs.open_issues?.toLocaleString()} />
          <MetricCell label="Closed issues" value={attrs.closed_issues?.toLocaleString()} />
          <MetricCell label="Releases" value={attrs.releases_total} />
        </div>

        {attrs.language && (
          <div>
            <div className="text-xs uppercase tracking-wider text-gray-500 mb-1">Primary language</div>
            <div className="text-gray-200 text-sm">{attrs.language}</div>
          </div>
        )}

        {attrs.topics?.length > 0 && (
          <div>
            <div className="text-xs uppercase tracking-wider text-gray-500 mb-1">Topics</div>
            <div className="flex flex-wrap gap-1">
              {attrs.topics.map((t) => (
                <span key={t} className="px-2 py-0.5 bg-blue-900/40 border border-blue-700/40 rounded text-xs text-blue-200">{t}</span>
              ))}
            </div>
          </div>
        )}

        {(attrs.category || attrs.audience || attrs.domain_tags) && (
          <div className="bg-gray-800 rounded-lg p-3 space-y-2">
            <div className="text-xs uppercase tracking-wider text-gray-500">Enriched</div>
            {attrs.category && (
              <div className="text-sm"><span className="text-gray-400">Category: </span><span className="text-gray-100">{attrs.category}</span></div>
            )}
            {attrs.primary_use_case && (
              <div className="text-sm text-gray-300">{attrs.primary_use_case}</div>
            )}
            {attrs.audience?.length > 0 && (
              <div className="flex flex-wrap gap-1">
                {attrs.audience.map((a) => <span key={a} className="px-2 py-0.5 bg-purple-900/40 border border-purple-700/40 rounded text-xs text-purple-200">{a}</span>)}
              </div>
            )}
            {attrs.domain_tags?.length > 0 && (
              <div className="flex flex-wrap gap-1">
                {attrs.domain_tags.map((d) => <span key={d} className="px-2 py-0.5 bg-cyan-900/40 border border-cyan-700/40 rounded text-xs text-cyan-200">{d}</span>)}
              </div>
            )}
            {attrs.alternatives_mentioned?.length > 0 && (
              <div className="text-xs text-gray-400">Alternatives mentioned in README: <span className="text-gray-200">{attrs.alternatives_mentioned.join(', ')}</span></div>
            )}
            {attrs.key_concepts?.length > 0 && (
              <div className="text-xs text-gray-400">Concepts: <span className="text-gray-200">{attrs.key_concepts.join(' · ')}</span></div>
            )}
          </div>
        )}

        {topAuthors.length > 0 && (
          <div>
            <div className="text-xs uppercase tracking-wider text-gray-500 mb-1">Top contributors (last 90d)</div>
            <div className="space-y-1">
              {topAuthors.map((a) => (
                <div key={a.login} className="flex items-center justify-between text-sm">
                  <a
                    href={`https://github.com/${a.login}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-gray-200 hover:text-blue-300"
                  >{a.login}</a>
                  <span className="text-gray-500">{a.commits} commits</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {neighbors.length > 0 && (
          <div>
            <div className="text-xs uppercase tracking-wider text-gray-500 mb-1">Connected repos in your stars</div>
            <div className="space-y-2">
              {neighbors.map((n) => (
                <div key={n.full_name} className="bg-gray-800 rounded p-2">
                  <div className="flex items-center justify-between gap-2">
                    <span className="text-sm text-blue-300 truncate">{n.full_name}</span>
                    <StageBadge stage={n.lifecycle_stage} />
                  </div>
                  <div className="text-xs text-gray-500 mt-1">
                    weight {n.weight.toFixed(2)}
                    {n.shared_authors.length > 0 && ` · ${n.shared_authors.length} shared author${n.shared_authors.length === 1 ? '' : 's'}`}
                    {n.shared_topics.length > 0 && ` · ${n.shared_topics.length} shared topic${n.shared_topics.length === 1 ? '' : 's'}`}
                  </div>
                  {n.shared_authors.length > 0 && (
                    <div className="text-xs text-yellow-400 mt-1 truncate">{n.shared_authors.slice(0, 3).join(', ')}</div>
                  )}
                  {n.shared_topics.length > 0 && (
                    <div className="text-xs text-cyan-400 mt-1 truncate">{n.shared_topics.slice(0, 4).join(', ')}</div>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}

        {readmeExcerpt && (
          <div>
            <div className="text-xs uppercase tracking-wider text-gray-500 mb-1">README excerpt</div>
            <pre className="bg-gray-950 rounded p-3 text-xs text-gray-300 whitespace-pre-wrap font-mono overflow-x-auto">
              {readmeExcerpt}
              {(attrs.readme_text ?? '').length > 1200 ? '\n…' : ''}
            </pre>
          </div>
        )}
      </div>
    </div>
  );
}
