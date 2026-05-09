import React, { createContext, useContext, useEffect, useState } from 'react';

const GraphContext = createContext(null);

export const STAGE_COLOR = {
  Hot: '#ef4444', Rising: '#f59e0b', Classic: '#10b981',
  Mature: '#3b82f6', Declining: '#a78bfa', Abandoned: '#6b7280',
};

export function GraphProvider({ children }) {
  const [state, setState] = useState({ status: 'loading', graph: null, stats: null, error: null });

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        // graph.json is pre-computed by scripts/precompute.mjs — nodes already have
        // community assignments, PageRank, and force-simulation positions baked in.
        const r = await fetch('/data/graph.json');
        if (!r.ok) throw new Error(`graph.json not found (${r.status}) — run npm run precompute`);
        const { nodes, links, stats, communities, computed_at } = await r.json();

        if (!cancelled) {
          setState({ status: 'ready', nodes, links, stats, communities, computed_at, error: null });
        }
      } catch (err) {
        if (!cancelled) setState({ status: 'error', error: err.message });
      }
    })();
    return () => { cancelled = true; };
  }, []);

  return <GraphContext.Provider value={state}>{children}</GraphContext.Provider>;
}

export function useGraph() {
  const ctx = useContext(GraphContext);
  if (!ctx) throw new Error('useGraph must be inside GraphProvider');
  return ctx;
}
