import React, { useCallback, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { GraphProvider, useGraph } from './GraphProvider';
import MapView from './MapView';
import InsightFeed from './InsightFeed';
import Comparator from './Comparator';
import RepoDetail from './RepoDetail';
import AllRepos from './AllRepos';
import TopicMap from './TopicMap';
import HealthHistogram from './HealthHistogram';

const TABS = [
  { key: 'map', label: 'Map' },
  { key: 'topics', label: 'Topics' },
  { key: 'insights', label: 'Insights' },
  { key: 'all', label: 'Browse' },
  { key: 'compare', label: 'Compare' },
  { key: 'ask', label: 'Ask AI' },
];

function AskView() {
  const { stats } = useGraph();
  const [q, setQ] = useState('');
  const [loading, setLoading] = useState(false);
  const [answer, setAnswer] = useState('');
  const [error, setError] = useState('');
  const [errorCode, setErrorCode] = useState('');
  const [meta, setMeta] = useState(null); // { model, provider }

  const SUGGESTION_GROUPS = [
    {
      label: 'Overview',
      items: [
        'Summarize the major themes across my starred repos.',
        'What are my most influential starred repos by PageRank?',
        'Which communities dominate my stars, and what do they share?',
      ],
    },
    {
      label: 'Communities & topics',
      items: [
        'Which two communities are most similar to each other, and why?',
        'Are there topics that span multiple communities — bridges between clusters?',
        'What technology stack does each major community represent?',
        'Which community looks most "frontier" or experimental right now?',
      ],
    },
    {
      label: 'Lifecycle & risk',
      items: [
        'Which repos are at risk of being abandoned but still get attention?',
        'Which mature projects in my stars are still actively maintained?',
        'Show me rising stars — repos gaining momentum I might be underrating.',
        'Which repos have I starred that look like one-time experiments?',
      ],
    },
    {
      label: 'Hidden gems & gaps',
      items: [
        'Which low-star repos punch above their weight by graph centrality?',
        'What kinds of tools am I underexposed to given the rest of my stars?',
        'Are there obvious duplicates — multiple repos solving the same problem?',
        'Which authors do I follow heavily without realizing it?',
      ],
    },
    {
      label: 'Personal pattern',
      items: [
        'What does my star history say about my interests as a developer?',
        'Where do the developers behind my favorite repos actually work?',
        'If I had to delete half my stars, which clusters would I drop first?',
      ],
    },
  ];

  async function ask(question) {
    setLoading(true); setAnswer(''); setError(''); setErrorCode(''); setMeta(null);
    try {
      const res = await fetch('/api/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question }),
      });
      const data = await res.json();
      if (data.error) {
        setError(data.error);
        setErrorCode(data.code || '');
        if (data.provider) setMeta({ provider: data.provider });
      } else {
        setAnswer(data.answer);
        if (data.model || data.provider) setMeta({ model: data.model, provider: data.provider });
      }
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="max-w-3xl">
      <h2 className="text-xl font-bold text-white mb-1">Ask about your stars</h2>
      <p className="text-gray-400 text-sm mb-5">Questions are answered using the knowledge graph of your {stats?.nodeCount ?? '…'} starred repos — communities, PageRank, lifecycle, connections.</p>

      <div className="flex gap-2 mb-4">
        <input
          value={q}
          onChange={(e) => setQ(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && q.trim() && ask(q)}
          placeholder="Ask anything about your starred repos…"
          className="flex-1 px-4 py-2.5 bg-gray-800 border border-gray-600 rounded-lg text-white placeholder-gray-500 focus:outline-none focus:border-blue-500"
        />
        <button
          onClick={() => q.trim() && ask(q)}
          disabled={loading || !q.trim()}
          className="px-5 py-2.5 bg-blue-600 hover:bg-blue-500 disabled:bg-gray-700 disabled:cursor-not-allowed rounded-lg font-medium text-white transition-colors"
        >{loading ? '…' : 'Ask'}</button>
      </div>

      <div className="space-y-3 mb-6">
        {SUGGESTION_GROUPS.map((group) => (
          <div key={group.label}>
            <div className="text-[11px] uppercase tracking-wider text-gray-500 mb-1.5">{group.label}</div>
            <div className="flex flex-wrap gap-2">
              {group.items.map((s) => (
                <button key={s} onClick={() => { setQ(s); ask(s); }}
                  className="px-3 py-1.5 bg-gray-800 hover:bg-gray-700 border border-gray-700 rounded-full text-xs text-gray-300 transition-colors">
                  {s}
                </button>
              ))}
            </div>
          </div>
        ))}
      </div>

      {error && errorCode === 'billing' && (
        <div className="bg-amber-900/30 border border-amber-600/60 rounded-lg p-4 text-amber-200 text-sm">
          <div className="font-semibold mb-1">{meta?.provider ?? 'LLM provider'} reports a billing or quota issue</div>
          <p>Add credit / upgrade the plan with your provider, then try again. Every other tab works without it.</p>
          <p className="mt-2 text-xs text-amber-300/80 font-mono break-words">{error}</p>
        </div>
      )}
      {error && errorCode === 'no_key' && (
        <div className="bg-amber-900/30 border border-amber-600/60 rounded-lg p-4 text-amber-200 text-sm">
          <div className="font-semibold mb-1">Ask AI is not configured</div>
          <p>Set <code className="bg-amber-950/60 px-1.5 py-0.5 rounded">LLM_API_KEY</code> in your environment (and optionally <code className="bg-amber-950/60 px-1.5 py-0.5 rounded">LLM_BASE_URL</code> / <code className="bg-amber-950/60 px-1.5 py-0.5 rounded">LLM_MODEL</code>) to enable this tab.</p>
        </div>
      )}
      {error && errorCode !== 'billing' && errorCode !== 'no_key' && (
        <div className="bg-red-900/30 border border-red-700 rounded-lg p-4 text-red-300 text-sm">{error}</div>
      )}
      {answer && (
        <div className="bg-gray-800 border border-gray-700 rounded-lg p-5">
          <div className="text-gray-100 text-sm leading-relaxed whitespace-pre-wrap">{answer}</div>
          {(meta?.model || meta?.provider) && (
            <div className="mt-4 pt-3 border-t border-gray-700/60 text-[11px] text-gray-500">
              {meta.model && <span className="font-mono">{meta.model}</span>}
              {meta.model && meta.provider && <span> · </span>}
              {meta.provider && <span>via {meta.provider}</span>}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

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
  const tab = params.get('tab') ?? 'map';
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
      <HealthHistogram />
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
      {tab === 'map' && <MapView onSelectNode={(n) => select(n ? n.full_name : null)} focusedRepoName={selected} />}
      {tab === 'topics' && <TopicMap onSelect={select} />}
      {tab === 'compare' && <Comparator initialA={compareA} initialB={compareB} />}
      {tab === 'ask' && <AskView />}
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
