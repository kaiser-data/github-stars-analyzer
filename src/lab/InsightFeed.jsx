import React, { useMemo, useState } from 'react';
import { useGraph } from './GraphProvider';
import { QUERIES } from './queries';

function ResultTable({ rows, onSelect }) {
  if (!rows || rows.length === 0) {
    return <div className="text-gray-500 text-sm">No results.</div>;
  }
  const headers = Object.keys(rows[0]);
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="text-gray-400 border-b border-gray-700">
            {headers.map((h) => (
              <th key={h} className="text-left py-2 pr-4 font-medium">{h}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, i) => {
            const fullName = typeof row.full_name === 'string' ? row.full_name : null;
            return (
              <tr
                key={i}
                className={`border-b border-gray-800 hover:bg-gray-800/50 ${fullName && onSelect ? 'cursor-pointer' : ''}`}
                onClick={() => fullName && onSelect && onSelect(fullName)}
              >
                {headers.map((h) => {
                  const v = row[h];
                  let display = v;
                  if (Array.isArray(v)) display = v.join(', ');
                  else if (typeof v === 'number') display = v.toLocaleString();
                  return (
                    <td key={h} className="py-2 pr-4 text-gray-200">
                      {h === 'full_name' && typeof v === 'string' ? (
                        <span className="text-blue-400 hover:text-blue-300">{v}</span>
                      ) : display}
                    </td>
                  );
                })}
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export default function InsightFeed({ onSelect }) {
  const { status, graph } = useGraph();
  const [activeKey, setActiveKey] = useState('whereDevsWork');

  const result = useMemo(() => {
    if (status !== 'ready') return null;
    const q = QUERIES[activeKey];
    if (!q) return null;
    return q.run(graph);
  }, [status, graph, activeKey]);

  if (status !== 'ready') return <div className="text-gray-400 p-4">Waiting for graph…</div>;

  return (
    <div className="grid grid-cols-1 lg:grid-cols-4 gap-4">
      <div className="lg:col-span-1">
        <h3 className="text-sm font-bold text-gray-300 mb-3 uppercase tracking-wide">Insights</h3>
        <div className="flex flex-col gap-1">
          {Object.entries(QUERIES).map(([key, q]) => (
            <button
              key={key}
              onClick={() => setActiveKey(key)}
              className={`text-left px-3 py-2 rounded-lg text-sm transition-colors ${
                activeKey === key ? 'bg-blue-600 text-white' : 'bg-gray-800 text-gray-300 hover:bg-gray-700'
              }`}
            >
              {q.title}
            </button>
          ))}
        </div>
      </div>
      <div className="lg:col-span-3 bg-gray-800 rounded-lg p-5">
        <h2 className="text-xl font-bold text-white">{QUERIES[activeKey].title}</h2>
        <p className="text-sm text-gray-400 mt-1 mb-4">{QUERIES[activeKey].description}</p>
        <ResultTable rows={result} onSelect={onSelect} />
        <div className="text-xs text-gray-500 mt-3">Click a row with a repo name to open detail panel.</div>
      </div>
    </div>
  );
}
