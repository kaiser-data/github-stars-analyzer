import React, { useEffect, useRef, useState } from 'react';
import Sigma from 'sigma';
import { useGraph } from './GraphProvider';

// Deterministic palette for community colors (overrides per-stage color in map view).
const COMMUNITY_PALETTE = [
  '#ef4444', '#f59e0b', '#10b981', '#3b82f6', '#a78bfa',
  '#ec4899', '#06b6d4', '#84cc16', '#f97316', '#8b5cf6',
  '#14b8a6', '#eab308', '#22c55e', '#0ea5e9', '#d946ef',
];

function forceLayout(graph, iterations = 100) {
  // Simple Fruchterman-Reingold-ish layout; good enough for ~100 nodes.
  const nodes = graph.nodes();
  const k = 1.0;
  const positions = {};
  for (const n of nodes) {
    positions[n] = {
      x: (Math.random() - 0.5) * 10,
      y: (Math.random() - 0.5) * 10,
      vx: 0,
      vy: 0,
    };
  }

  for (let it = 0; it < iterations; it += 1) {
    const temperature = 1.0 * (1 - it / iterations);
    // Repulsive forces
    for (let i = 0; i < nodes.length; i += 1) {
      for (let j = i + 1; j < nodes.length; j += 1) {
        const a = positions[nodes[i]];
        const b = positions[nodes[j]];
        const dx = a.x - b.x;
        const dy = a.y - b.y;
        const dist = Math.sqrt(dx * dx + dy * dy) + 0.01;
        const repel = (k * k) / dist;
        a.vx += (dx / dist) * repel;
        a.vy += (dy / dist) * repel;
        b.vx -= (dx / dist) * repel;
        b.vy -= (dy / dist) * repel;
      }
    }
    // Attractive forces along edges
    graph.forEachEdge((edge, attrs, source, target) => {
      const a = positions[source];
      const b = positions[target];
      const dx = a.x - b.x;
      const dy = a.y - b.y;
      const dist = Math.sqrt(dx * dx + dy * dy) + 0.01;
      const w = attrs.weight ?? 1;
      const attract = (dist * dist) / k * Math.min(2, w);
      a.vx -= (dx / dist) * attract;
      a.vy -= (dy / dist) * attract;
      b.vx += (dx / dist) * attract;
      b.vy += (dy / dist) * attract;
    });
    // Apply velocity capped by temperature
    for (const n of nodes) {
      const p = positions[n];
      const v = Math.sqrt(p.vx * p.vx + p.vy * p.vy) + 0.001;
      const move = Math.min(v, temperature * 5);
      p.x += (p.vx / v) * move;
      p.y += (p.vy / v) * move;
      p.vx = 0;
      p.vy = 0;
    }
  }
  return positions;
}

export default function MapView({ onSelectNode }) {
  const containerRef = useRef(null);
  const sigmaRef = useRef(null);
  const { status, graph, stats, error } = useGraph();
  const [hovered, setHovered] = useState(null);

  useEffect(() => {
    if (status !== 'ready' || !graph || !containerRef.current) return;

    const positions = forceLayout(graph, 200);
    graph.forEachNode((n, a) => {
      const community = a.community ?? 0;
      graph.mergeNodeAttributes(n, {
        x: positions[n].x,
        y: positions[n].y,
        size: a.size ?? 5,
        color: COMMUNITY_PALETTE[community % COMMUNITY_PALETTE.length],
        label: a.full_name,
      });
    });
    graph.forEachEdge((edge, a) => {
      graph.mergeEdgeAttributes(edge, {
        size: 0.3 + Math.min(2, (a.weight ?? 0) * 0.5),
        color: 'rgba(148,163,184,0.25)',
      });
    });

    const renderer = new Sigma(graph, containerRef.current, {
      labelDensity: 0.07,
      labelRenderedSizeThreshold: 8,
      labelColor: { color: '#e5e7eb' },
      defaultEdgeColor: 'rgba(148,163,184,0.25)',
      renderEdgeLabels: false,
    });

    renderer.on('enterNode', ({ node }) => {
      setHovered(graph.getNodeAttributes(node));
    });
    renderer.on('leaveNode', () => setHovered(null));
    renderer.on('clickNode', ({ node }) => {
      if (onSelectNode) onSelectNode(graph.getNodeAttributes(node));
    });

    sigmaRef.current = renderer;
    return () => {
      renderer.kill();
      sigmaRef.current = null;
    };
  }, [status, graph, onSelectNode]);

  if (status === 'loading') return <div className="text-gray-400 p-6">Loading graph…</div>;
  if (status === 'error') return <div className="text-red-400 p-6">Failed: {error}</div>;

  return (
    <div className="relative">
      <div className="absolute top-3 left-3 z-10 bg-gray-900/80 border border-gray-700 rounded-lg px-3 py-2 text-xs text-gray-300">
        <div>{stats.nodeCount} repos · {stats.edgeCount} edges · {stats.communityCount} communities</div>
        <div className="text-gray-500 mt-1">Color = community · Size = stars · Hover for detail</div>
      </div>
      {hovered && (
        <div className="absolute top-3 right-3 z-10 bg-gray-900/95 border border-gray-700 rounded-lg p-4 text-sm text-gray-100 max-w-md">
          <div className="font-bold text-blue-400">{hovered.full_name}</div>
          <div className="text-xs text-gray-400 mt-1">{hovered.description?.slice(0, 200)}</div>
          {hovered.one_liner && <div className="text-gray-200 mt-2 italic">{hovered.one_liner}</div>}
          <div className="flex gap-3 mt-3 text-xs">
            <span className="px-2 py-0.5 rounded bg-gray-700">{hovered.lifecycle_stage}</span>
            <span>★ {hovered.stars?.toLocaleString()}</span>
            <span>health {hovered.health_score}</span>
            <span>authors90 {hovered.unique_authors_90d}</span>
          </div>
        </div>
      )}
      <div ref={containerRef} style={{ width: '100%', height: '70vh', background: '#111827', borderRadius: 12 }} />
    </div>
  );
}
