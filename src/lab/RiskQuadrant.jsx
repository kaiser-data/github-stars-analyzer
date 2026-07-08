import React, { useMemo, useRef, useState } from 'react';
import { useGraph, STAGE_COLOR } from './GraphProvider';

// Risk quadrant: repo health (x) vs star momentum (y, log), dot size = stars,
// color = lifecycle stage. The actionable read is the left edge: big dots with
// low health are popular projects you may depend on that look fragile.

const W = 960;
const H = 560;
const M = { top: 24, right: 24, bottom: 46, left: 64 };
const HEALTH_RISK = 40; // below this we call a repo "at risk"

const fmt = (n) => (typeof n === 'number' ? n.toLocaleString() : '—');

function yTickLabel(v) {
  if (v >= 1000) return `${v / 1000}k`;
  return String(v);
}

export default function RiskQuadrant({ onSelect }) {
  const { status, nodes } = useGraph();
  const [hidden, setHidden] = useState(new Set()); // lifecycle stages toggled off
  const [hover, setHover] = useState(null); // { node, x, y } in wrapper coords
  const wrapRef = useRef(null);

  const model = useMemo(() => {
    if (status !== 'ready' || !nodes) return null;
    const pts = nodes.filter((n) => n.health_score != null);
    const maxStars = Math.max(...pts.map((n) => n.stars || 0), 1);
    const yMax = Math.log10(1 + Math.max(...pts.map((n) => n.momentum?.estimated_stars_30d || 0), 10));
    const plotW = W - M.left - M.right;
    const plotH = H - M.top - M.bottom;
    const sx = (h) => M.left + (h / 100) * plotW;
    const sy = (m) => M.top + plotH - (Math.log10(1 + m) / yMax) * plotH;
    const sr = (s) => 3.5 + 13 * Math.sqrt((s || 0) / maxStars);
    const dots = pts
      .map((n) => ({
        n,
        x: sx(n.health_score),
        y: sy(n.momentum?.estimated_stars_30d || 0),
        r: sr(n.stars),
      }))
      // big dots first so small ones stay on top and hoverable
      .sort((a, b) => b.r - a.r);
    const yTicks = [0, 10, 100, 1000, 10000, 100000]
      .filter((v) => Math.log10(1 + v) <= yMax + 0.001)
      .map((v) => ({ v, y: sy(v) }));
    const xTicks = [0, 20, 40, 60, 80, 100].map((v) => ({ v, x: sx(v) }));
    const counts = {};
    for (const p of pts) counts[p.lifecycle_stage] = (counts[p.lifecycle_stage] || 0) + 1;
    const atRisk = pts
      .filter((n) => n.health_score < HEALTH_RISK)
      .sort((a, b) => (b.stars || 0) - (a.stars || 0))
      .slice(0, 8);
    return { dots, yTicks, xTicks, counts, atRisk, sx, plotH };
  }, [status, nodes]);

  if (!model) {
    return <div className="bg-gray-800/40 border border-gray-700 rounded-lg p-6 text-gray-400 text-sm">Loading risk view…</div>;
  }

  const toggleStage = (stage) => {
    setHidden((prev) => {
      const next = new Set(prev);
      next.has(stage) ? next.delete(stage) : next.add(stage);
      return next;
    });
  };

  const showTip = (e, n) => {
    const box = wrapRef.current?.getBoundingClientRect();
    if (!box) return;
    setHover({ n, x: e.clientX - box.left, y: e.clientY - box.top });
  };

  const riskX = model.sx(HEALTH_RISK);

  return (
    <div>
      <div className="mb-3">
        <h2 className="text-xl font-bold text-white">Risk quadrant</h2>
        <p className="text-gray-400 text-sm">
          Health score vs. star momentum (log). Dot size = stars, color = lifecycle stage.
          Big dots left of the line are popular projects with weak health signals — check before you depend on them.
        </p>
      </div>

      {/* legend: color identifies the stage; toggling filters without repainting */}
      <div className="flex flex-wrap gap-2 mb-3 text-xs">
        {Object.entries(STAGE_COLOR).map(([stage, color]) => (
          <button
            key={stage}
            onClick={() => toggleStage(stage)}
            className={`flex items-center gap-1.5 px-2.5 py-1 rounded-full border transition-colors ${
              hidden.has(stage)
                ? 'border-gray-700 text-gray-600 bg-gray-900/40'
                : 'border-gray-600 text-gray-200 bg-gray-800'
            }`}
          >
            <span className="w-2.5 h-2.5 rounded-full" style={{ background: hidden.has(stage) ? '#4b5563' : color }} />
            {stage} <span className="text-gray-500">{model.counts[stage] || 0}</span>
          </button>
        ))}
        {hidden.size > 0 && (
          <button onClick={() => setHidden(new Set())} className="px-2.5 py-1 text-blue-400 hover:text-blue-300 underline">
            show all
          </button>
        )}
      </div>

      <div ref={wrapRef} className="relative bg-gray-800/40 border border-gray-700 rounded-lg overflow-hidden">
        <svg viewBox={`0 0 ${W} ${H}`} className="w-full block" role="img" aria-label="Scatter of repo health vs momentum">
          {/* at-risk zone */}
          <rect x={M.left} y={M.top} width={riskX - M.left} height={model.plotH} fill="#ef4444" opacity="0.05" />
          <line x1={riskX} y1={M.top} x2={riskX} y2={M.top + model.plotH} stroke="#ef4444" strokeOpacity="0.35" strokeDasharray="4 4" />
          <text x={riskX - 8} y={M.top + 16} textAnchor="end" fill="#f87171" fontSize="11">
            ⚠ health &lt; {HEALTH_RISK}
          </text>

          {/* recessive grid + axes */}
          {model.yTicks.map(({ v, y }) => (
            <g key={`y${v}`}>
              <line x1={M.left} y1={y} x2={W - M.right} y2={y} stroke="#374151" strokeOpacity="0.4" />
              <text x={M.left - 8} y={y + 3.5} textAnchor="end" fill="#9ca3af" fontSize="11">{yTickLabel(v)}</text>
            </g>
          ))}
          {model.xTicks.map(({ v, x }) => (
            <text key={`x${v}`} x={x} y={H - M.bottom + 18} textAnchor="middle" fill="#9ca3af" fontSize="11">{v}</text>
          ))}
          <text x={M.left + (W - M.left - M.right) / 2} y={H - 8} textAnchor="middle" fill="#6b7280" fontSize="11.5">
            Health score →
          </text>
          <text x={16} y={M.top + model.plotH / 2} textAnchor="middle" fill="#6b7280" fontSize="11.5"
            transform={`rotate(-90 16 ${M.top + model.plotH / 2})`}>
            Momentum (est. +stars / 30d) →
          </text>

          {/* dots */}
          {model.dots.map(({ n, x, y, r }) =>
            hidden.has(n.lifecycle_stage) ? null : (
              <circle
                key={n.id}
                cx={x}
                cy={y}
                r={r}
                fill={STAGE_COLOR[n.lifecycle_stage] || '#6b7280'}
                fillOpacity="0.75"
                stroke="#111827"
                strokeWidth="1"
                className="cursor-pointer"
                onMouseEnter={(e) => showTip(e, n)}
                onMouseMove={(e) => showTip(e, n)}
                onMouseLeave={() => setHover(null)}
                onClick={() => onSelect?.(n.full_name)}
              />
            )
          )}
        </svg>

        {hover && (
          <div
            className="absolute z-10 pointer-events-none bg-gray-900 border border-gray-600 rounded-lg px-3 py-2 text-xs shadow-xl"
            style={{
              left: Math.min(hover.x + 14, (wrapRef.current?.clientWidth ?? W) - 230),
              top: Math.max(hover.y - 10, 4),
              width: 220,
            }}
          >
            <div className="font-semibold text-white truncate">{hover.n.full_name}</div>
            <div className="text-gray-400 mt-1 space-y-0.5">
              <div>
                <span className="inline-block w-2 h-2 rounded-full mr-1.5" style={{ background: STAGE_COLOR[hover.n.lifecycle_stage] }} />
                {hover.n.lifecycle_stage} · health <span className="text-gray-200">{hover.n.health_score}</span>
              </div>
              <div>★ {fmt(hover.n.stars)} · +{fmt(hover.n.momentum?.estimated_stars_30d || 0)}/30d</div>
              <div>last push {fmt(hover.n.days_since_push)}d ago</div>
            </div>
          </div>
        )}
      </div>

      {/* the actionable list: the danger quadrant, spelled out */}
      {model.atRisk.length > 0 && (
        <div className="mt-4">
          <h3 className="text-sm font-semibold text-gray-200 mb-2">Popular but fragile — most-starred repos with health &lt; {HEALTH_RISK}</h3>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-2">
            {model.atRisk.map((n) => (
              <button
                key={n.id}
                onClick={() => onSelect?.(n.full_name)}
                className="text-left bg-gray-800/60 hover:bg-gray-800 border border-gray-700 hover:border-red-500/60 rounded-lg px-3 py-2 transition-colors"
              >
                <div className="text-sm text-white truncate">{n.full_name}</div>
                <div className="text-xs text-gray-400 mt-0.5">
                  ★ {fmt(n.stars)} · health <span className="text-red-400">{n.health_score}</span> · push {fmt(n.days_since_push)}d ago
                </div>
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
