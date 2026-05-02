import React, { useEffect, useMemo, useRef, useState } from 'react';
import Graph from 'graphology';
import louvain from 'graphology-communities-louvain';
import Sigma from 'sigma';
import { useGraph, STAGE_COLOR } from './GraphProvider';

const COMMUNITY_PALETTE = [
  '#a78bfa', '#06b6d4', '#84cc16', '#f97316', '#ec4899',
  '#14b8a6', '#eab308', '#22c55e', '#0ea5e9', '#d946ef',
  '#ef4444', '#f59e0b', '#10b981', '#3b82f6', '#8b5cf6',
];

function buildTopicGraph(repos, minRepoFreq = 2) {
  const topicCounts = new Map();
  const repoTopics = new Map();
  for (const r of repos) {
    const set = new Set((r.topics ?? []).filter(Boolean));
    repoTopics.set(r.id, set);
    for (const t of set) topicCounts.set(t, (topicCounts.get(t) ?? 0) + 1);
  }

  const keep = new Set([...topicCounts.entries()].filter(([, c]) => c >= minRepoFreq).map(([t]) => t));
  const g = new Graph({ type: 'undirected', multi: false });
  for (const t of keep) {
    g.addNode(t, {
      label: t,
      kind: 'topic',
      freq: topicCounts.get(t),
      size: 3 + Math.log10(1 + topicCounts.get(t)) * 5,
    });
  }

  // Co-occurrence edges
  for (const r of repos) {
    const ts = [...repoTopics.get(r.id)].filter((t) => keep.has(t));
    for (let i = 0; i < ts.length; i += 1) {
      for (let j = i + 1; j < ts.length; j += 1) {
        const a = ts[i];
        const b = ts[j];
        if (g.hasEdge(a, b)) {
          g.updateEdgeAttribute(a, b, 'weight', (w) => (w ?? 0) + 1);
        } else {
          g.addEdge(a, b, { weight: 1 });
        }
      }
    }
  }

  // Drop edges with weight < 2 (one co-occurrence is noisy)
  const toDrop = [];
  g.forEachEdge((edge, attrs) => {
    if ((attrs.weight ?? 0) < 2) toDrop.push(edge);
  });
  for (const edge of toDrop) g.dropEdge(edge);

  // Drop isolated topics (no edges) for cleaner viz
  const isolated = [];
  g.forEachNode((n) => { if (g.degree(n) === 0) isolated.push(n); });
  for (const n of isolated) g.dropNode(n);

  if (g.order > 0 && g.size > 0) {
    const detail = louvain.detailed(g, { getEdgeWeight: 'weight' });
    g.forEachNode((n) => g.setNodeAttribute(n, 'community', detail.communities[n]));
  } else {
    g.forEachNode((n) => g.setNodeAttribute(n, 'community', 0));
  }
  return g;
}

function forceLayout(graph, iterations = 200) {
  const nodes = graph.nodes();
  const k = 1.0;
  const positions = {};
  for (const n of nodes) {
    positions[n] = { x: (Math.random() - 0.5) * 12, y: (Math.random() - 0.5) * 12, vx: 0, vy: 0 };
  }
  for (let it = 0; it < iterations; it += 1) {
    const temperature = 1.0 * (1 - it / iterations);
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
    graph.forEachEdge((edge, attrs, source, target) => {
      const a = positions[source];
      const b = positions[target];
      const dx = a.x - b.x;
      const dy = a.y - b.y;
      const dist = Math.sqrt(dx * dx + dy * dy) + 0.01;
      const w = attrs.weight ?? 1;
      const attract = (dist * dist) / k * Math.min(3, w);
      a.vx -= (dx / dist) * attract;
      a.vy -= (dy / dist) * attract;
      b.vx += (dx / dist) * attract;
      b.vy += (dy / dist) * attract;
    });
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

function ReposByTopic({ topic, repos, onSelect }) {
  if (!topic) return null;
  const matching = repos.filter((r) => (r.topics ?? []).includes(topic));
  const stageCounts = matching.reduce((acc, r) => ((acc[r.lifecycle_stage] = (acc[r.lifecycle_stage] ?? 0) + 1), acc), {});
  return (
    <div className="bg-gray-800 rounded-lg p-4 border border-gray-700">
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-lg font-bold text-cyan-300">#{topic}</h3>
        <span className="text-xs text-gray-400">{matching.length} repo{matching.length === 1 ? '' : 's'}</span>
      </div>
      <div className="flex flex-wrap gap-2 mb-3">
        {Object.entries(stageCounts).map(([stage, n]) => (
          <span
            key={stage}
            className="px-2 py-0.5 rounded-full text-[10px] font-bold"
            style={{ backgroundColor: STAGE_COLOR[stage], color: '#0a0a0a' }}
          >{stage} {n}</span>
        ))}
      </div>
      <div className="space-y-1 max-h-[40vh] overflow-y-auto pr-1">
        {matching
          .sort((a, b) => b.stars - a.stars)
          .map((r) => (
            <button
              key={r.id}
              onClick={() => onSelect(r.full_name)}
              className="w-full text-left px-2 py-1.5 rounded hover:bg-gray-700 text-sm flex items-center justify-between gap-2"
            >
              <span className="text-blue-300 truncate">{r.full_name}</span>
              <span className="text-xs text-gray-500 flex-shrink-0">★ {r.stars?.toLocaleString()}</span>
            </button>
          ))}
      </div>
    </div>
  );
}

export default function TopicMap({ onSelect }) {
  const containerRef = useRef(null);
  const sigmaRef = useRef(null);
  const focusRef = useRef(null);
  const { status, classified } = useGraph();
  const [hovered, setHovered] = useState(null);
  const [selected, setSelected] = useState(null);
  const [minFreq, setMinFreq] = useState(2);

  const topicGraph = useMemo(() => {
    if (status !== 'ready' || !classified) return null;
    return buildTopicGraph(classified.repos, minFreq);
  }, [status, classified, minFreq]);

  useEffect(() => {
    if (!topicGraph || !containerRef.current || topicGraph.order === 0) {
      if (sigmaRef.current) {
        sigmaRef.current.kill();
        sigmaRef.current = null;
      }
      return;
    }

    const positions = forceLayout(topicGraph, 250);
    topicGraph.forEachNode((n, a) => {
      topicGraph.mergeNodeAttributes(n, {
        x: positions[n].x,
        y: positions[n].y,
        size: a.size,
        color: COMMUNITY_PALETTE[(a.community ?? 0) % COMMUNITY_PALETTE.length],
      });
    });
    topicGraph.forEachEdge((edge, a) => {
      topicGraph.mergeEdgeAttributes(edge, {
        size: 0.3 + Math.min(2.5, (a.weight ?? 1) * 0.4),
        color: 'rgba(148,163,184,0.2)',
      });
    });

    const renderer = new Sigma(topicGraph, containerRef.current, {
      labelDensity: 0.1,
      labelRenderedSizeThreshold: 6,
      labelColor: { color: '#e5e7eb' },
      defaultEdgeColor: 'rgba(148,163,184,0.2)',
      nodeReducer: (node, data) => {
        const focus = focusRef.current;
        if (!focus) return data;
        if (node === focus.id) return { ...data, zIndex: 2, size: data.size * 1.4 };
        if (focus.neighbors.has(node)) return { ...data, zIndex: 1 };
        return { ...data, color: '#374151', label: '', size: data.size * 0.5 };
      },
      edgeReducer: (edge, data) => {
        const focus = focusRef.current;
        if (!focus) return data;
        const ext = topicGraph.extremities(edge);
        const incident = ext[0] === focus.id || ext[1] === focus.id;
        if (incident) return { ...data, color: 'rgba(34,211,238,0.6)', size: data.size * 1.5 };
        return { ...data, hidden: true };
      },
    });

    renderer.on('enterNode', ({ node }) => setHovered(topicGraph.getNodeAttributes(node)));
    renderer.on('leaveNode', () => setHovered(null));
    renderer.on('clickNode', ({ node }) => {
      const neighbors = new Set(topicGraph.neighbors(node));
      focusRef.current = { id: node, neighbors };
      setSelected(node);
      renderer.refresh();
    });
    renderer.on('clickStage', () => {
      focusRef.current = null;
      setSelected(null);
      renderer.refresh();
    });

    sigmaRef.current = renderer;
    return () => {
      renderer.kill();
      sigmaRef.current = null;
      focusRef.current = null;
    };
  }, [topicGraph]);

  if (status !== 'ready') return <div className="text-gray-400 p-4">Waiting for graph…</div>;
  const stats = topicGraph
    ? { topics: topicGraph.order, edges: topicGraph.size }
    : { topics: 0, edges: 0 };

  return (
    <div className="grid grid-cols-1 lg:grid-cols-4 gap-4">
      <div className="lg:col-span-3">
        <div className="relative">
          <div className="absolute top-3 left-3 z-10 bg-gray-900/80 border border-gray-700 rounded-lg px-3 py-2 text-xs text-gray-300">
            <div>{stats.topics} topics · {stats.edges} co-occurrences</div>
            <div className="text-gray-500 mt-1">Edge weight = repos sharing both topics. Click to focus.</div>
            <div className="mt-2">
              <label className="text-gray-500">Min repos per topic: </label>
              <input
                type="number"
                min={2}
                max={10}
                value={minFreq}
                onChange={(e) => setMinFreq(Math.max(2, Math.min(10, Number(e.target.value) || 2)))}
                className="w-12 bg-gray-800 border border-gray-700 rounded px-1 text-gray-200"
              />
            </div>
          </div>
          {hovered && !selected && (
            <div className="absolute top-3 right-3 z-10 bg-gray-900/95 border border-gray-700 rounded-lg p-3 text-sm text-gray-100">
              <div className="font-bold text-cyan-300">#{hovered.label}</div>
              <div className="text-xs text-gray-400 mt-1">{hovered.freq} repos</div>
            </div>
          )}
          {topicGraph && topicGraph.order === 0 ? (
            <div className="bg-gray-900 rounded-lg p-12 text-center text-gray-500">
              No topics meet the minimum frequency. Lower the threshold.
            </div>
          ) : (
            <div ref={containerRef} style={{ width: '100%', height: '70vh', background: '#111827', borderRadius: 12 }} />
          )}
        </div>
      </div>
      <div className="lg:col-span-1">
        {selected ? (
          <ReposByTopic topic={selected} repos={classified.repos} onSelect={onSelect} />
        ) : (
          <div className="bg-gray-800 rounded-lg p-4 border border-gray-700 text-sm text-gray-400">
            Click a topic to see repos using it. Bigger nodes = more repos. Edges = topics that appear together.
          </div>
        )}
      </div>
    </div>
  );
}
