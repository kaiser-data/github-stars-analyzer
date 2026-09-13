import React from 'react';

// react-markdown component overrides shared by ReportsView and PromptsView, so
// generated reports and prompts render with one consistent look.
export const MD_COMPONENTS = {
  h1: (p) => <h1 className="text-2xl font-bold text-white mt-6 mb-3" {...p} />,
  h2: (p) => <h2 className="text-xl font-semibold text-white mt-7 mb-3 pb-1 border-b border-gray-700" {...p} />,
  h3: (p) => <h3 className="text-lg font-semibold text-blue-300 mt-5 mb-2" {...p} />,
  p: (p) => <p className="text-gray-300 leading-relaxed my-3" {...p} />,
  a: (p) => <a className="text-blue-400 hover:underline" target="_blank" rel="noreferrer" {...p} />,
  // report markdown references its charts relative to itself (assets/…); the
  // app serves them from /reports/assets/
  img: ({ src, ...p }) => (
    <img
      src={src?.startsWith('assets/') ? `/reports/${src}` : src}
      className="my-4 rounded-lg max-w-full"
      loading="lazy"
      {...p}
    />
  ),
  ul: (p) => <ul className="list-disc pl-6 my-3 space-y-1 text-gray-300" {...p} />,
  ol: (p) => <ol className="list-decimal pl-6 my-3 space-y-1 text-gray-300" {...p} />,
  li: (p) => <li className="leading-relaxed" {...p} />,
  blockquote: (p) => (
    <blockquote className="border-l-4 border-gray-600 pl-4 my-4 text-gray-400 text-sm" {...p} />
  ),
  // react-markdown v10 dropped the `inline` prop: style inline `code` here and
  // fenced blocks via `pre` below.
  code: (p) => <code className="bg-gray-800 text-amber-300 px-1.5 py-0.5 rounded text-[0.85em]" {...p} />,
  pre: (p) => (
    <pre className="bg-gray-900 border border-gray-700 rounded-lg p-3 my-3 overflow-x-auto text-sm text-gray-200" {...p} />
  ),
  table: (p) => (
    <div className="overflow-x-auto my-4 rounded-lg border border-gray-700">
      <table className="w-full text-sm border-collapse" {...p} />
    </div>
  ),
  thead: (p) => <thead className="bg-gray-800" {...p} />,
  th: (p) => <th className="text-left font-semibold text-gray-200 px-3 py-2 border-b border-gray-700 whitespace-nowrap" {...p} />,
  td: (p) => <td className="px-3 py-2 border-b border-gray-800 text-gray-300 align-top" {...p} />,
  hr: () => <hr className="border-gray-700 my-6" />,
};
