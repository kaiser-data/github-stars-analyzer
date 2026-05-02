import React, { useCallback } from 'react';
import { useSearchParams } from 'react-router-dom';
import { GraphProvider, useGraph } from './GraphProvider';
import MapView from './MapView';
import InsightFeed from './InsightFeed';
import Comparator from './Comparator';
import RepoDetail from './RepoDetail';
import AllRepos from './AllRepos';
import TopicMap from './TopicMap';

const TABS = [
  { key: 'insights', label: 'Insights' },
  { key: 'all', label: 'Browse' },
  { key: 'map', label: 'Map' },
  { key: 'topics', label: 'Topics' },
  { key: 'compare', label: 'Compare' },
];

function StatusBanner() {
  const { status, stats, hasEnrichment, error } = useGraph();
  if (status === 'loading') {
    return <div className="bg-blue-900/30 border border-blue-500/50 text-blue-200 px-4 py-2 rounded-lg text-sm mb-4">Loading classified data and building graph…</div>;
  }
  if (status === 'error') {
    return <div className="bg-red-900/30 border border-red-500/50 text-red-200 px-4 py-2 rounded-lg text-sm mb-4">Error: {error}</div>;
  }
  return (
    <div className="bg-gray-800/50 border border-gray-700 px-4 py-2 rounded-lg text-sm mb-4 flex items-center justify-between">
      <span className="text-gray-300">
        Graph ready: <strong className="text-white">{stats.nodeCount}</strong> repos · <strong className="text-white">{stats.edgeCount}</strong> edges · <strong className="text-white">{stats.communityCount}</strong> communities
      </span>
      <span className="text-xs">
        {hasEnrichment ? (
          <span className="text-green-400">+ enriched (LLM summaries available)</span>
        ) : (
          <span className="text-yellow-400">no enriched-100.json yet — runs without LLM data</span>
        )}
      </span>
    </div>
  );
}

function LabContent() {
  const [params, setParams] = useSearchParams();
  const tab = params.get('tab') ?? 'insights';
  const selected = params.get('repo');
  const compareA = params.get('a');
  const compareB = params.get('b');

  const setTab = useCallback((next) => {
    setParams((prev) => {
      const p = new URLSearchParams(prev);
      p.set('tab', next);
      return p;
    });
  }, [setParams]);

  const select = useCallback((fullName) => {
    setParams((prev) => {
      const p = new URLSearchParams(prev);
      if (fullName) p.set('repo', fullName); else p.delete('repo');
      return p;
    });
  }, [setParams]);

  const closeDetail = useCallback(() => select(null), [select]);

  const goCompare = useCallback((a, b) => {
    setParams((prev) => {
      const p = new URLSearchParams(prev);
      p.set('tab', 'compare');
      if (a) p.set('a', a);
      if (b) p.set('b', b);
      p.delete('repo');
      return p;
    });
  }, [setParams]);

  return (
    <div>
      <StatusBanner />
      <div className="flex flex-wrap gap-2 mb-5">
        {TABS.map((t) => (
          <button
            key={t.key}
            onClick={() => setTab(t.key)}
            className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
              tab === t.key ? 'bg-blue-600 text-white' : 'bg-gray-800 text-gray-300 hover:bg-gray-700'
            }`}
          >
            {t.label}
          </button>
        ))}
      </div>
      {tab === 'insights' && <InsightFeed onSelect={select} />}
      {tab === 'all' && <AllRepos onSelect={select} />}
      {tab === 'map' && <MapView onSelectNode={(n) => select(n.full_name)} />}
      {tab === 'topics' && <TopicMap onSelect={select} />}
      {tab === 'compare' && <Comparator initialA={compareA} initialB={compareB} />}
      {selected && <RepoDetail repoFullName={selected} onClose={closeDetail} onCompareWith={goCompare} />}
    </div>
  );
}

export default function LabApp() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-gray-800 text-white py-6 px-4">
      <div className="max-w-[1920px] mx-auto">
        <div className="mb-6">
          <h1 className="text-3xl font-bold">Stars Lab</h1>
          <p className="text-gray-400 text-sm">Knowledge graph view of your starred repos — relationships, communities, lifecycle.</p>
        </div>
        <GraphProvider>
          <LabContent />
        </GraphProvider>
      </div>
    </div>
  );
}
