import React, { useMemo, useState } from 'react';
import { useGraph, STAGE_COLOR } from './GraphProvider';

const ALL_STAGES = ['Hot', 'Rising', 'Classic', 'Mature', 'Declining', 'Abandoned'];

export default function AllRepos({ onSelect }) {
  const { status, graph } = useGraph();
  const [q, setQ] = useState('');
  const [stages, setStages] = useState(new Set(ALL_STAGES));
  const [sortKey, setSortKey] = useState('stars');

  const repos = useMemo(() => {
    if (status !== 'ready') return [];
    const out = [];
    graph.forEachNode((n, a) => { if (a.kind === 'repo') out.push(a); });
    return out;
  }, [status, graph]);

  const filtered = useMemo(() => {
    const ql = q.trim().toLowerCase();
    let list = repos.filter((r) => stages.has(r.lifecycle_stage));
    if (ql) {
      list = list.filter((r) => {
        const haystack = [
          r.full_name,
          r.description,
          (r.topics ?? []).join(' '),
          r.one_liner,
          (r.audience ?? []).join(' '),
          (r.domain_tags ?? []).join(' '),
          (r.key_concepts ?? []).join(' '),
        ].filter(Boolean).join(' ').toLowerCase();
        return haystack.includes(ql);
      });
    }
    list.sort((a, b) => {
      switch (sortKey) {
        case 'health': return b.health_score - a.health_score;
        case 'authors90': return b.unique_authors_90d - a.unique_authors_90d;
        case 'commits90': return b.commits_90d - a.commits_90d;
        case 'age': return a.age_days - b.age_days;
        case 'pushed': return a.days_since_push - b.days_since_push;
        case 'pagerank': return (b.pagerank ?? 0) - (a.pagerank ?? 0);
        case 'stars':
        default: return b.stars - a.stars;
      }
    });
    return list;
  }, [repos, q, stages, sortKey]);

  const toggleStage = (s) => {
    setStages((prev) => {
      const next = new Set(prev);
      if (next.has(s)) next.delete(s); else next.add(s);
      return next;
    });
  };

  if (status !== 'ready') return <div className="text-gray-400 p-4">Waiting for graph…</div>;

  return (
    <div className="bg-gray-800 rounded-lg p-5">
      <div className="flex flex-wrap items-center gap-3 mb-4">
        <input
          value={q}
          onChange={(e) => setQ(e.target.value)}
          placeholder="Search names, descriptions, topics, concepts…"
          className="flex-1 min-w-[260px] px-3 py-2 bg-gray-900 text-white rounded-lg border border-gray-700 focus:outline-none focus:border-blue-500"
        />
        <select
          value={sortKey}
          onChange={(e) => setSortKey(e.target.value)}
          className="px-3 py-2 bg-gray-900 text-white rounded-lg border border-gray-700"
        >
          <option value="stars">Sort: stars</option>
          <option value="pagerank">Sort: PageRank (graph-central)</option>
          <option value="health">Sort: health score</option>
          <option value="authors90">Sort: authors 90d</option>
          <option value="commits90">Sort: commits 90d</option>
          <option value="age">Sort: youngest first</option>
          <option value="pushed">Sort: most recently pushed</option>
        </select>
      </div>

      <div className="flex flex-wrap gap-2 mb-4">
        {ALL_STAGES.map((s) => {
          const active = stages.has(s);
          return (
            <button
              key={s}
              onClick={() => toggleStage(s)}
              className={`px-3 py-1 rounded-full text-xs font-bold border transition-opacity ${active ? '' : 'opacity-40'}`}
              style={{
                backgroundColor: active ? STAGE_COLOR[s] : 'transparent',
                borderColor: STAGE_COLOR[s],
                color: active ? '#0a0a0a' : STAGE_COLOR[s],
              }}
            >
              {s}
            </button>
          );
        })}
        <button
          onClick={() => setStages(new Set(ALL_STAGES))}
          className="px-3 py-1 rounded-full text-xs text-gray-400 hover:text-white"
        >
          all
        </button>
      </div>

      <div className="text-xs text-gray-400 mb-3">
        {filtered.length} of {repos.length} repos · click any to open detail
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3 max-h-[60vh] overflow-y-auto pr-2">
        {filtered.map((r) => (
          <button
            key={r.id}
            onClick={() => onSelect && onSelect(r.full_name)}
            className="text-left bg-gray-900 hover:bg-gray-700 transition-colors rounded-lg p-3 border border-gray-700"
          >
            <div className="flex items-center justify-between gap-2">
              <span className="text-blue-400 font-semibold truncate">{r.full_name}</span>
              <span
                className="px-2 py-0.5 rounded-full text-[10px] font-bold flex-shrink-0"
                style={{ backgroundColor: STAGE_COLOR[r.lifecycle_stage], color: '#0a0a0a' }}
              >{r.lifecycle_stage}</span>
            </div>
            <div className="text-xs text-gray-400 mt-1 line-clamp-2">{r.one_liner ?? r.description}</div>
            <div className="flex flex-wrap gap-3 mt-2 text-xs text-gray-500">
              <span>★ {r.stars?.toLocaleString()}</span>
              <span>health {r.health_score}</span>
              <span>a90 {r.unique_authors_90d}</span>
              <span>c90 {r.commits_90d}</span>
              {r.language && <span className="text-gray-400">{r.language}</span>}
            </div>
          </button>
        ))}
      </div>
    </div>
  );
}
