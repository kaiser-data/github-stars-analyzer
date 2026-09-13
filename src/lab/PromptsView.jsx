import React, { useEffect, useRef, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { MD_COMPONENTS } from './markdownComponents';

function CopyBriefButton({ brief }) {
  const [state, setState] = useState('idle');
  const taRef = useRef(null);

  // Selects the brief into an offscreen textarea so the fallback label is
  // actually true: there is something selected to press Ctrl/Cmd+C on.
  const selectFallback = () => {
    const ta = taRef.current;
    if (!ta) return;
    ta.value = brief;
    ta.focus();
    ta.select();
    ta.setSelectionRange(0, brief.length);
  };

  const copy = async () => {
    // navigator.clipboard is undefined on non-secure origins (e.g. a
    // `vite --host` LAN preview over plain http), so this button must not
    // assume it exists.
    if (navigator.clipboard?.writeText) {
      try {
        await navigator.clipboard.writeText(brief);
        setState('copied');
        setTimeout(() => setState('idle'), 2000);
        return;
      } catch {
        // fall through to the selection fallback below
      }
    }
    selectFallback();
    setState('selected');
    setTimeout(() => setState('idle'), 2000);
  };

  const label = {
    idle: 'Copy prompt',
    copied: 'Copied',
    selected: 'Selected — press Ctrl/Cmd+C',
  }[state];

  return (
    <>
      <button
        onClick={copy}
        className="text-sm bg-blue-600 hover:bg-blue-500 text-white rounded-lg px-4 py-2 transition-colors"
      >
        {label}
      </button>
      <textarea
        ref={taRef}
        readOnly
        tabIndex={-1}
        aria-hidden="true"
        style={{ position: 'fixed', top: 0, left: '-9999px', width: 1, height: 1, opacity: 0 }}
      />
    </>
  );
}

function PromptCard({ prompt, onOpen }) {
  return (
    <button
      onClick={() => onOpen(prompt)}
      className="text-left bg-gray-800/60 hover:bg-gray-800 border border-gray-700 hover:border-blue-500 rounded-xl p-5 transition-colors group flex flex-col"
    >
      <div className="flex items-start justify-between gap-2">
        <span className="text-[11px] uppercase tracking-wide text-blue-400 font-medium">
          {prompt.report}
        </span>
        <span className="text-gray-500 group-hover:text-blue-400 transition-colors">→</span>
      </div>
      <h3 className="text-lg font-semibold text-white mt-1 leading-snug">{prompt.title}</h3>
      <p className="text-sm text-gray-400 mt-2 flex-1">{prompt.summary}</p>
      <div className="flex flex-wrap gap-1.5 mt-4">
        {prompt.stack.map((s) => (
          <span
            key={s.name}
            className="text-[11px] bg-gray-900 border border-gray-700 rounded px-2 py-0.5 text-gray-400"
            title={`${s.stage} · ${s.lifecycle}`}
          >
            {s.name.split('/')[1]}
          </span>
        ))}
      </div>
    </button>
  );
}

function PromptReader({ prompt, onBack }) {
  const [md, setMd] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    let alive = true;
    setMd(null);
    setError(null);
    fetch(`/prompts/${prompt.file}`)
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.text();
      })
      .then((t) => alive && setMd(t))
      .catch((e) => alive && setError(e.message));
    return () => { alive = false; };
  }, [prompt.file]);

  return (
    <div>
      <div className="flex items-center justify-between gap-4 mb-4">
        <button onClick={onBack} className="text-sm text-blue-400 hover:underline inline-flex items-center gap-1">
          ← All prompts
        </button>
        <CopyBriefButton brief={prompt.brief} />
      </div>
      {error && (
        <div className="bg-red-950/40 border border-red-800 rounded-lg p-4 text-red-300 text-sm">
          Couldn’t load this prompt ({error}).
        </div>
      )}
      {!md && !error && (
        <div className="text-gray-400 text-sm flex items-center gap-3">
          <span className="inline-block w-2 h-2 rounded-full bg-blue-400 animate-pulse" />
          Loading prompt…
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

export default function PromptsView() {
  const [index, setIndex] = useState(null);
  const [error, setError] = useState(null);
  const [open, setOpen] = useState(null);

  useEffect(() => {
    let alive = true;
    fetch('/prompts/index.json')
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then((j) => alive && setIndex(j))
      .catch((e) => alive && setError(e.message));
    return () => { alive = false; };
  }, []);

  if (error) {
    return (
      <div className="bg-amber-950/40 border border-amber-800 rounded-lg p-4 text-amber-200 text-sm">
        No prompts found ({error}). Run <code className="bg-amber-950/60 px-1.5 py-0.5 rounded">python3 scripts/reports/build_index.py</code> to generate them.
      </div>
    );
  }
  if (!index) return <div className="text-gray-400 text-sm">Loading prompts…</div>;
  if (open) return <PromptReader prompt={open} onBack={() => setOpen(null)} />;

  return (
    <div>
      <p className="text-sm text-gray-400 mb-5 max-w-2xl">
        Build prompts generated from the landscape reports. Each one names the tools its
        parent report selected, with their current stars, health and lifecycle stage
        alongside it, so you can judge a low score for yourself instead of trusting a
        stale recommendation — and if a tool has since left the dataset, the prompt
        carries a visible warning saying so.
      </p>
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {index.prompts.map((p) => (
          <PromptCard key={p.slug} prompt={p} onOpen={setOpen} />
        ))}
      </div>
    </div>
  );
}
