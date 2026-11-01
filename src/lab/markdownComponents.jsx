import React from 'react';

// react-markdown component overrides shared by ReportsView, PromptsView and Ask AI, so
// generated reports, prompts and answers render with one consistent, editorial look:
// serif headings, prose held to a readable measure, tables allowed full width.
const PROSE = 'max-w-[72ch]';

export const MD_COMPONENTS = {
  h1: (p) => <h1 className="font-display text-3xl md:text-4xl text-white mt-2 mb-4 leading-tight" {...p} />,
  h2: (p) => (
    <h2 className="font-display text-2xl text-white mt-10 mb-3 pb-2 border-b border-blue-400/25" {...p} />
  ),
  h3: (p) => <h3 className="font-display text-xl italic text-blue-300 mt-7 mb-2" {...p} />,
  h4: (p) => <h4 className="font-mono text-[11px] tracking-[0.25em] uppercase text-blue-400 mt-6 mb-2" {...p} />,
  p: (p) => <p className={`${PROSE} text-gray-300 leading-[1.75] my-3`} {...p} />,
  a: (p) => (
    <a className="text-blue-300 underline decoration-blue-400/40 underline-offset-2 hover:decoration-blue-300"
       target="_blank" rel="noreferrer" {...p} />
  ),
  strong: (p) => <strong className="text-white font-semibold" {...p} />,
  // report markdown references its charts relative to itself (assets/…); the
  // app serves them from /reports/assets/
  img: ({ src, ...p }) => (
    <img
      src={src?.startsWith('assets/') ? `/reports/${src}` : src}
      className="my-6 rounded-xl max-w-full border border-gray-700"
      loading="lazy"
      {...p}
    />
  ),
  ul: (p) => <ul className={`${PROSE} list-disc marker:text-blue-400 pl-6 my-3 space-y-1.5 text-gray-300`} {...p} />,
  ol: (p) => <ol className={`${PROSE} list-decimal marker:text-blue-400 pl-6 my-3 space-y-1.5 text-gray-300`} {...p} />,
  li: (p) => <li className="leading-[1.7]" {...p} />,
  blockquote: (p) => (
    // reports use blockquotes for provenance notes ("Derived from…"), so keep them quiet
    <blockquote className={`${PROSE} border-l-2 border-blue-400/60 bg-gray-900/50 rounded-r-lg pl-4 pr-3 py-1 my-5 text-sm text-gray-400 [&_p]:text-gray-400 [&_p]:my-2`} {...p} />
  ),
  // react-markdown v10 dropped the `inline` prop: style inline `code` here and
  // fenced blocks via `pre` below.
  code: (p) => <code className="bg-gray-800 text-blue-200 px-1.5 py-0.5 rounded text-[0.85em]" {...p} />,
  pre: (p) => (
    <pre className="bg-gray-950 border border-gray-700 rounded-xl p-4 my-4 overflow-x-auto text-sm text-gray-200" {...p} />
  ),
  table: (p) => (
    <div className="overflow-x-auto my-6 rounded-xl border border-gray-700 bg-gray-950/60">
      <table className="w-full text-sm border-collapse" {...p} />
    </div>
  ),
  thead: (p) => <thead className="bg-gray-800/80" {...p} />,
  th: (p) => (
    <th className="text-left font-mono text-[11px] tracking-[0.12em] uppercase text-blue-300 px-3 py-2.5 border-b border-gray-700 whitespace-nowrap" {...p} />
  ),
  tr: (p) => <tr className="hover:bg-gray-800/40 transition-colors" {...p} />,
  td: (p) => <td className="px-3 py-2 border-b border-gray-800 text-gray-300 align-top" {...p} />,
  hr: () => <hr className="border-gray-700 my-8" />,
};
