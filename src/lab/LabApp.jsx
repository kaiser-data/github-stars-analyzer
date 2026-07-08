import React, { Suspense, lazy, useCallback, useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { GraphProvider, useGraph } from './GraphProvider';
import InsightFeed from './InsightFeed';
import Comparator from './Comparator';
import RepoDetail from './RepoDetail';
import AllRepos from './AllRepos';
import HealthHistogram from './HealthHistogram';
import RiskQuadrant from './RiskQuadrant';

// Lazy: both pull in react-force-graph-3d + three (~1.36 MB chunk).
// Loaded only when the user actually opens the Map or Topics tab.
const MapView = lazy(() => import('./MapView'));
const TopicMap = lazy(() => import('./TopicMap'));
// Lazy: pulls in react-markdown + remark-gfm; only loaded on the Reports tab.
const ReportsView = lazy(() => import('./ReportsView'));

function GraphTabFallback({ label = 'graph' }) {
  return (
    <div className="bg-gray-800/40 border border-gray-700 rounded-lg p-6 text-gray-400 text-sm flex items-center gap-3">
      <span className="inline-block w-2 h-2 rounded-full bg-blue-400 animate-pulse" />
      Loading 3D {label}…
    </div>
  );
}

function TabFallback({ label = 'content' }) {
  return (
    <div className="bg-gray-800/40 border border-gray-700 rounded-lg p-6 text-gray-400 text-sm flex items-center gap-3">
      <span className="inline-block w-2 h-2 rounded-full bg-blue-400 animate-pulse" />
      Loading {label}…
    </div>
  );
}

const TABS = [
  { key: 'map', label: 'Map' },
  { key: 'topics', label: 'Topics' },
  { key: 'insights', label: 'Insights' },
  { key: 'risk', label: 'Risk' },
  { key: 'all', label: 'Browse' },
  { key: 'compare', label: 'Compare' },
  { key: 'reports', label: 'Reports' },
  { key: 'ask', label: 'Ask AI' },
];

function AskView() {
  const { stats } = useGraph();
  const [q, setQ] = useState('');
  const [loading, setLoading] = useState(false);
  const [answer, setAnswer] = useState('');
  const [error, setError] = useState('');
  const [errorCode, setErrorCode] = useState('');
  const [meta, setMeta] = useState(null); // { model, provider, cached, generated_at }
  // Map<question, {answer, model, provider, generated_at}> from /data/questions.json
  const [cache, setCache] = useState(null);

  useEffect(() => {
    let aborted = false;
    fetch('/data/questions.json')
      .then((r) => (r.ok ? r.json() : null))
      .then((data) => {
        if (aborted || !data?.items) return;
        const m = new Map();
        for (const it of data.items) {
          if (it.answer) m.set(it.question, {
            answer: it.answer,
            model: data.model,
            provider: data.provider,
            generated_at: data.generated_at,
          });
        }
        setCache(m);
      })
      .catch(() => { /* cache is optional */ });
    return () => { aborted = true; };
  }, []);

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

  // Show a precomputed answer instantly if we have one; otherwise hit /api/ask.
  function askMaybeCached(question) {
    const hit = cache?.get(question);
    if (hit) {
      setAnswer(hit.answer);
      setError(''); setErrorCode('');
      setMeta({ model: hit.model, provider: hit.provider, cached: true, generated_at: hit.generated_at });
      setLoading(false);
      return;
    }
    return ask(question);
  }

  async function ask(question) {
    setLoading(true); setAnswer(''); setError(''); setErrorCode(''); setMeta(null);
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 90_000);
    try {
      const res = await fetch('/api/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question }),
        signal: controller.signal,
      });

      const contentType = res.headers.get('content-type') || '';

      // Streaming success path: Server-Sent Events of answer tokens.
      if (contentType.includes('text/event-stream')) {
        setMeta({
          model: res.headers.get('x-llm-model') || undefined,
          provider: res.headers.get('x-llm-provider') || undefined,
        });
        const reader = res.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';
        let acc = '';
        let streamErr = null;
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          buffer += decoder.decode(value, { stream: true });
          let sep;
          while ((sep = buffer.indexOf('\n\n')) !== -1) {
            const frame = buffer.slice(0, sep);
            buffer = buffer.slice(sep + 2);
            for (const line of frame.split('\n')) {
              if (!line.startsWith('data:')) continue; // ignore `:` heartbeats
              const payload = line.slice(5).trim();
              if (!payload) continue;
              let json;
              try { json = JSON.parse(payload); } catch { continue; }
              if (json.v) { acc += json.v; setAnswer(acc); }
              else if (json.error) { streamErr = json.error; }
            }
          }
        }
        if (streamErr && !acc) { setError(streamErr); setErrorCode('stream_error'); }
        return;
      }

      // Non-stream path: JSON error (no key, billing, upstream, etc.).
      let data;
      try {
        data = await res.json();
      } catch {
        setError(`Server returned an unexpected response (HTTP ${res.status}). The model may have taken too long — try a shorter question.`);
        setErrorCode('bad_response');
        return;
      }
      if (data.error) {
        setError(data.error);
        setErrorCode(data.code || '');
        if (data.provider) setMeta({ provider: data.provider });
      } else if (data.answer) {
        setAnswer(data.answer);
        if (data.model || data.provider) setMeta({ model: data.model, provider: data.provider });
      }
    } catch (e) {
      if (e.name === 'AbortError') {
        setError('The request timed out. Try a shorter or more specific question.');
        setErrorCode('timeout');
      } else {
        setError(e.message);
      }
    } finally {
      clearTimeout(timeout);
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
          onKeyDown={(e) => e.key === 'Enter' && q.trim() && askMaybeCached(q)}
          placeholder="Ask anything about your starred repos…"
          className="flex-1 px-4 py-2.5 bg-gray-800 border border-gray-600 rounded-lg text-white placeholder-gray-500 focus:outline-none focus:border-blue-500"
        />
        <button
          onClick={() => q.trim() && askMaybeCached(q)}
          disabled={loading || !q.trim()}
          className="px-5 py-2.5 bg-blue-600 hover:bg-blue-500 disabled:bg-gray-700 disabled:cursor-not-allowed rounded-lg font-medium text-white transition-colors"
        >{loading ? '…' : 'Ask'}</button>
      </div>

      <div className="space-y-3 mb-6">
        {SUGGESTION_GROUPS.map((group) => (
          <div key={group.label}>
            <div className="text-[11px] uppercase tracking-wider text-gray-500 mb-1.5">{group.label}</div>
            <div className="flex flex-wrap gap-2">
              {group.items.map((s) => {
                const isCached = cache?.has(s);
                return (
                  <button key={s} onClick={() => { setQ(s); askMaybeCached(s); }}
                    title={isCached ? 'Instant answer — precomputed' : undefined}
                    className={`px-3 py-1.5 border rounded-full text-xs transition-colors ${
                      isCached
                        ? 'bg-blue-900/30 hover:bg-blue-900/50 border-blue-700/60 text-blue-200'
                        : 'bg-gray-800 hover:bg-gray-700 border-gray-700 text-gray-300'
                    }`}>
                    {isCached && <span className="mr-1 text-blue-400">✦</span>}{s}
                  </button>
                );
              })}
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
      {loading && !answer && !error && (
        <div className="bg-gray-800 border border-gray-700 rounded-lg p-5 text-gray-400 text-sm flex items-center gap-2">
          <span className="inline-block w-2 h-2 rounded-full bg-blue-400 animate-pulse" />
          {meta?.provider ? `${meta.provider} is thinking…` : 'Thinking…'}
        </div>
      )}
      {answer && (
        <div className="bg-gray-800 border border-gray-700 rounded-lg p-5">
          <div className="text-gray-100 text-sm leading-relaxed whitespace-pre-wrap">{answer}{loading && <span className="inline-block w-1.5 h-4 ml-0.5 -mb-0.5 bg-blue-400 animate-pulse" />}</div>
          {!loading && (meta?.model || meta?.provider || meta?.cached) && (
            <div className="mt-4 pt-3 border-t border-gray-700/60 text-[11px] text-gray-500 flex items-center gap-2 flex-wrap">
              {meta.cached && (
                <span className="text-blue-400">✦ instant · cached {meta.generated_at ? new Date(meta.generated_at).toLocaleDateString() : ''}</span>
              )}
              {meta.cached && (meta.model || meta.provider) && <span>·</span>}
              {meta.model && <span className="font-mono">{meta.model}</span>}
              {meta.model && meta.provider && <span>·</span>}
              {meta.provider && <span>via {meta.provider}</span>}
              {meta.cached && (
                <button onClick={() => q && ask(q)}
                  className="ml-auto text-blue-400 hover:text-blue-300 underline">
                  ask fresh
                </button>
              )}
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
      {tab === 'risk' && <RiskQuadrant onSelect={select} />}
      {tab === 'all' && <AllRepos onSelect={select} />}
      {tab === 'map' && (
        <Suspense fallback={<GraphTabFallback label="map" />}>
          <MapView onSelectNode={(n) => select(n ? n.full_name : null)} focusedRepoName={selected} />
        </Suspense>
      )}
      {tab === 'topics' && (
        <Suspense fallback={<GraphTabFallback label="topic graph" />}>
          <TopicMap onSelect={select} />
        </Suspense>
      )}
      {tab === 'compare' && <Comparator initialA={compareA} initialB={compareB} />}
      {tab === 'reports' && (
        <Suspense fallback={<TabFallback label="reports" />}>
          <ReportsView />
        </Suspense>
      )}
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
