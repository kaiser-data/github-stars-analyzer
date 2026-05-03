import React, { useEffect, useRef, useState } from 'react';
import Sigma from 'sigma';
import forceAtlas2 from 'graphology-layout-forceatlas2';
import randomLayout from 'graphology-layout/random';
import { useGraph } from './GraphProvider';

// Deterministic palette for community colors (overrides per-stage color in map view).
const COMMUNITY_PALETTE = [
  '#ef4444', '#f59e0b', '#10b981', '#3b82f6', '#a78bfa',
  '#ec4899', '#06b6d4', '#84cc16', '#f97316', '#8b5cf6',
  '#14b8a6', '#eab308', '#22c55e', '#0ea5e9', '#d946ef',
];

function applyLayout(graph) {
  // ForceAtlas2 with Barnes-Hut: O(n log n) per iteration vs O(n²) for naive FR.
  // Same family of algorithms (cluster-revealing force-directed); FA2 is what
  // Gephi uses as default. Result quality is at least as good, often clearer.
  randomLayout.assign(graph, { scale: 100 });
  forceAtlas2.assign(graph, {
    iterations: 200,
    settings: {
      barnesHutOptimize: true,
      barnesHutTheta: 0.6,
      gravity: 1,
      scalingRatio: 10,
      strongGravityMode: false,
      slowDown: 5,
      adjustSizes: false,
      edgeWeightInfluence: 1,
    },
    getEdgeWeight: 'weight',
  });
}

export default function MapView({ onSelectNode, focusedRepoName }) {
  const containerRef = useRef(null);
  const sigmaRef = useRef(null);
  const focusRef = useRef(null); // stays in sync with reducers without re-init
  const { status, graph, stats, error } = useGraph();
  const [hovered, setHovered] = useState(null);
  const [focused, setFocused] = useState(null);

  // External focus driven by URL param — when prop changes, find the node
  // and apply focus without re-creating the sigma instance.
  useEffect(() => {
    if (status !== 'ready' || !graph || !sigmaRef.current) return;
    if (!focusedRepoName) {
      if (focusRef.current) {
        focusRef.current = null;
        setFocused(null);
        sigmaRef.current.refresh();
      }
      return;
    }
    let nodeId = null;
    graph.forEachNode((n, a) => { if (a.kind === 'repo' && a.full_name === focusedRepoName) nodeId = n; });
    if (nodeId && nodeId !== focusRef.current?.id) {
      focusRef.current = { id: nodeId, neighbors: new Set(graph.neighbors(nodeId)) };
      setFocused(focusedRepoName);
      sigmaRef.current.refresh();
    }
  }, [focusedRepoName, status, graph]);

  useEffect(() => {
    if (status !== 'ready' || !graph || !containerRef.current) return;

    applyLayout(graph);
    graph.forEachNode((n, a) => {
      const community = a.community ?? 0;
      graph.mergeNodeAttributes(n, {
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
      nodeReducer: (node, data) => {
        const focus = focusRef.current;
        if (!focus) return data;
        if (node === focus.id) return { ...data, zIndex: 2, size: data.size * 1.4 };
        if (focus.neighbors.has(node)) return { ...data, zIndex: 1 };
        return { ...data, color: '#374151', label: '', size: data.size * 0.6 };
      },
      edgeReducer: (edge, data) => {
        const focus = focusRef.current;
        if (!focus) return data;
        const ext = graph.extremities(edge);
        const incident = ext[0] === focus.id || ext[1] === focus.id;
        if (incident) return { ...data, color: 'rgba(96,165,250,0.7)', size: data.size * 1.5 };
        return { ...data, hidden: true };
      },
    });

    renderer.on('enterNode', ({ node }) => {
      setHovered(graph.getNodeAttributes(node));
    });
    renderer.on('leaveNode', () => setHovered(null));
    renderer.on('clickNode', ({ node }) => {
      const neighbors = new Set(graph.neighbors(node));
      focusRef.current = { id: node, neighbors };
      setFocused(graph.getNodeAttributes(node).full_name);
      renderer.refresh();
      if (onSelectNode) onSelectNode(graph.getNodeAttributes(node));
    });
    renderer.on('clickStage', () => {
      focusRef.current = null;
      setFocused(null);
      renderer.refresh();
      if (onSelectNode) onSelectNode(null);
    });

    sigmaRef.current = renderer;
    return () => {
      renderer.kill();
      sigmaRef.current = null;
      focusRef.current = null;
    };
  }, [status, graph, onSelectNode]);

  if (status === 'loading') return <div className="text-gray-400 p-6">Loading graph…</div>;
  if (status === 'error') return <div className="text-red-400 p-6">Failed: {error}</div>;

  return (
    <div className="relative">
      <div className="absolute top-3 left-3 z-10 bg-gray-900/80 border border-gray-700 rounded-lg px-3 py-2 text-xs text-gray-300">
        <div>{stats.nodeCount} repos · {stats.edgeCount} edges · {stats.communityCount} communities</div>
        <div className="text-gray-500 mt-1">Color = community · Size = stars · Click to focus, click background to clear</div>
        {focused && (
          <div className="mt-1 text-blue-300">Focused: {focused}</div>
        )}
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
