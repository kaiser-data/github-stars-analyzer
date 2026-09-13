import React, { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { MD_COMPONENTS } from './markdownComponents';

// react-markdown + remark-gfm live in this lazy chunk (ReportsView is loaded
// via React.lazy in LabApp), so they stay out of the main bundle.

const fmt = (n) => (typeof n === 'number' ? n.toLocaleString() : n);

function ReportCard({ report, onOpen }) {
  const cats = report.categories || {};
  return (
    <button
      onClick={() => onOpen(report)}
      className="text-left bg-gray-800/60 hover:bg-gray-800 border border-gray-700 hover:border-blue-500 rounded-xl p-5 transition-colors group flex flex-col"
    >
      <div className="flex items-start justify-between gap-2">
        <span className="text-[11px] uppercase tracking-wide text-blue-400 font-medium">
          {report.category}
        </span>
        <span className="text-gray-500 group-hover:text-blue-400 transition-colors">→</span>
      </div>
      <h3 className="text-lg font-semibold text-white mt-1 leading-snug">
        {report.title.split('—')[0].trim()}
      </h3>
      <p className="text-sm text-gray-400 mt-2 flex-1">{report.summary}</p>
      <div className="flex flex-wrap items-baseline gap-3 mt-4 text-sm">
        <span className="text-gray-300">
          <span className="font-semibold text-white">{report.tool_count}</span> tools
        </span>
        <span className="text-gray-300">
          <span className="font-semibold text-amber-300">★ {fmt(report.total_stars)}</span>
        </span>
        {report.created && (
          <span className="text-xs text-gray-500 ml-auto" title={`First published ${report.created}`}>
            {report.created}
          </span>
        )}
      </div>
      {Object.keys(cats).length > 0 && (
        <div className="flex flex-wrap gap-1.5 mt-3">
          {Object.entries(cats).map(([name, count]) => (
            <span key={name} className="text-[11px] bg-gray-900 border border-gray-700 rounded px-2 py-0.5 text-gray-400">
              {name} · {count}
            </span>
          ))}
        </div>
      )}
    </button>
  );
}

function ReportReader({ report, onBack }) {
  const [md, setMd] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    let alive = true;
    setMd(null);
    setError(null);
    fetch(`/reports/${report.file}`)
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.text();
      })
      .then((t) => alive && setMd(t))
      .catch((e) => alive && setError(e.message));
    return () => { alive = false; };
  }, [report.file]);

  return (
    <div>
      <button
        onClick={onBack}
        className="text-sm text-blue-400 hover:underline mb-4 inline-flex items-center gap-1"
      >
        ← All reports
      </button>
      {error && (
        <div className="bg-red-950/40 border border-red-800 rounded-lg p-4 text-red-300 text-sm">
          Couldn’t load this report ({error}).
        </div>
      )}
      {!md && !error && (
        <div className="text-gray-400 text-sm flex items-center gap-3">
          <span className="inline-block w-2 h-2 rounded-full bg-blue-400 animate-pulse" />
          Loading report…
        </div>
      )}
      {md && (
        <article className="max-w-none bg-gray-900/40 border border-gray-800 rounded-xl p-6">
          <ReactMarkdown remarkPlugins={[remarkGfm]} components={MD_COMPONENTS}>
            {md}
          </ReactMarkdown>
        </article>
      )}
    </div>
  );
}

const SORTS = {
  size: { label: 'Biggest', fn: (a, b) => (b.tool_count || 0) - (a.tool_count || 0) },
  created: {
    label: 'Newest',
    fn: (a, b) => String(b.created || b.generated || '').localeCompare(String(a.created || a.generated || '')),
  },
};

export default function ReportsView() {
  const [index, setIndex] = useState(null);
  const [error, setError] = useState(null);
  const [active, setActive] = useState(null);
  const [sort, setSort] = useState('size');

  useEffect(() => {
    let alive = true;
    fetch('/reports/index.json')
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then((d) => alive && setIndex(d))
      .catch((e) => alive && setError(e.message));
    return () => { alive = false; };
  }, []);

  if (active) {
    return <ReportReader report={active} onBack={() => setActive(null)} />;
  }

  if (error) {
    return (
      <div className="bg-amber-950/40 border border-amber-800 rounded-lg p-4 text-amber-200 text-sm">
        No reports found ({error}). Run <code className="bg-amber-950/60 px-1.5 py-0.5 rounded">python3 scripts/reports/build_index.py</code> to generate them.
      </div>
    );
  }

  if (!index) {
    return (
      <div className="text-gray-400 text-sm flex items-center gap-3">
        <span className="inline-block w-2 h-2 rounded-full bg-blue-400 animate-pulse" />
        Loading reports…
      </div>
    );
  }

  return (
    <div>
      <div className="mb-5 flex flex-wrap items-end justify-between gap-3">
        <div>
          <h2 className="text-lg font-semibold text-white">Curated reports</h2>
          <p className="text-sm text-gray-400 mt-1">
            Deep-dives into clusters of these stars, built from the dataset + similarity graph.
            {index.generated && <span className="text-gray-500"> Updated {index.generated}.</span>}
          </p>
        </div>
        <div className="flex items-center gap-1 text-xs bg-gray-800/60 border border-gray-700 rounded-lg p-1">
          {Object.entries(SORTS).map(([key, s]) => (
            <button
              key={key}
              onClick={() => setSort(key)}
              className={`px-2.5 py-1 rounded-md transition-colors ${
                sort === key ? 'bg-gray-700 text-white' : 'text-gray-400 hover:text-gray-200'
              }`}
            >
              {s.label}
            </button>
          ))}
        </div>
      </div>
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {[...index.reports].sort(SORTS[sort].fn).map((r) => (
          <ReportCard key={r.slug} report={r} onOpen={setActive} />
        ))}
      </div>
    </div>
  );
}
