import React from 'react';
import { useGraph, STAGE_COLOR } from './GraphProvider';

const STAGE_ORDER = ['Hot', 'Rising', 'Classic', 'Mature', 'Declining', 'Abandoned'];

export default function HealthHistogram() {
  const { status, nodes = [] } = useGraph();
  if (status !== 'ready') return null;

  const stats = new Map();
  for (const n of nodes) {
    const stage = n.lifecycle_stage;
    if (!stats.has(stage)) stats.set(stage, { count: 0, healthSum: 0 });
    const s = stats.get(stage);
    s.count += 1;
    s.healthSum += n.health_score ?? 0;
  }

  const total = [...stats.values()].reduce((s, v) => s + v.count, 0);
  if (total === 0) return null;

  return (
    <div className="bg-gray-800/50 border border-gray-700 px-4 py-3 rounded-lg mb-4">
      <div className="text-xs uppercase tracking-wider text-gray-500 mb-2">Lifecycle distribution · avg health</div>
      <div className="flex flex-wrap gap-3">
        {STAGE_ORDER.map((stage) => {
          const s = stats.get(stage);
          if (!s) return null;
          const avg = Math.round(s.healthSum / s.count);
          const pct = (s.count / total) * 100;
          return (
            <div key={stage} className="flex items-center gap-2 min-w-[140px]">
              <div className="flex-1">
                <div className="flex items-center justify-between text-xs">
                  <span className="font-bold" style={{ color: STAGE_COLOR[stage] }}>{stage}</span>
                  <span className="text-gray-400">{s.count} · h{avg}</span>
                </div>
                <div className="h-1.5 bg-gray-700 rounded-full mt-1 overflow-hidden">
                  <div style={{ width: `${pct}%`, backgroundColor: STAGE_COLOR[stage] }} className="h-full" />
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
