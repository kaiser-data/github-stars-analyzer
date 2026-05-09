import React, { useEffect, useMemo, useRef, useState } from 'react';
import { forceManyBody, forceLink } from 'd3-force-3d';
import Graph from 'graphology';
import louvain from 'graphology-communities-louvain';
import ForceGraph3D from 'react-force-graph-3d';
import * as THREE from 'three';
import SpriteText from 'three-spritetext';
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
  for (const t of keep) g.addNode(t, { kind: 'topic', freq: topicCounts.get(t) });
  for (const r of repos) {
    const ts = [...repoTopics.get(r.id)].filter((t) => keep.has(t));
    for (let i = 0; i < ts.length; i += 1) {
      for (let j = i + 1; j < ts.length; j += 1) {
        const a = ts[i], b = ts[j];
        if (g.hasEdge(a, b)) g.updateEdgeAttribute(a, b, 'weight', (w) => (w ?? 0) + 1);
        else g.addEdge(a, b, { weight: 1 });
      }
    }
  }
  const toDrop = [];
  g.forEachEdge((edge, attrs) => { if ((attrs.weight ?? 0) < 2) toDrop.push(edge); });
  for (const edge of toDrop) g.dropEdge(edge);
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

function topicGraphToFG(g) {
  const nodes = [];
  const links = [];
  g.forEachNode((id, attrs) => {
    nodes.push({
      id,
      label: id,
      community: attrs.community ?? 0,
      freq: attrs.freq,
      val: 1 + Math.log10(1 + attrs.freq) * 3,
    });
  });
  g.forEachEdge((edge, attrs, source, target) => {
    links.push({ source, target, weight: attrs.weight ?? 1 });
  });
  return { nodes, links };
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
          <span key={stage} className="px-2 py-0.5 rounded-full text-[10px] font-bold" style={{ backgroundColor: STAGE_COLOR[stage], color: '#0a0a0a' }}>{stage} {n}</span>
        ))}
      </div>
      <div className="space-y-1 max-h-[40vh] overflow-y-auto pr-1">
        {matching.sort((a, b) => b.stars - a.stars).map((r) => (
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

function ControlPanel({ settings, setSettings, onRecenter }) {
  const upd = (k, v) => setSettings((s) => ({ ...s, [k]: v }));
  const Row = ({ label, children }) => (
    <div className="grid grid-cols-3 items-center gap-2 py-1">
      <span className="text-[11px] text-gray-400 col-span-1">{label}</span>
      <div className="col-span-2">{children}</div>
    </div>
  );
  return (
    <div className="absolute top-3 right-3 z-10 bg-gray-900/90 backdrop-blur border border-gray-700 rounded-lg p-3 text-xs text-gray-200 shadow-xl w-[240px]">
      <button
        onClick={onRecenter}
        className="w-full mb-2 px-3 py-1.5 bg-blue-600 hover:bg-blue-500 rounded text-white font-medium"
      >Recenter view</button>
      <div className="text-[10px] uppercase tracking-wider text-gray-500 mb-2">Layout</div>
      <Row label="Repulsion"><input type="range" min={-300} max={-30} step={5} value={settings.charge} onChange={(e) => upd('charge', Number(e.target.value))} className="w-full" /></Row>
      <Row label="Link length"><input type="range" min={20} max={200} step={5} value={settings.linkDistance} onChange={(e) => upd('linkDistance', Number(e.target.value))} className="w-full" /></Row>
      <div className="text-[10px] uppercase tracking-wider text-gray-500 mt-3 mb-1">Display</div>
      <Row label="Label density">
        <input type="range" min={1} max={10} step={0.5} value={settings.labelDensity}
          onChange={(e) => upd('labelDensity', Number(e.target.value))} className="w-full" />
      </Row>
      <Row label="Labels always"><input type="checkbox" checked={settings.alwaysLabels} onChange={(e) => upd('alwaysLabels', e.target.checked)} /></Row>
      <Row label="Drag nodes"><input type="checkbox" checked={settings.drag} onChange={(e) => upd('drag', e.target.checked)} /></Row>
      <Row label="Auto-rotate"><input type="checkbox" checked={settings.autoRotate} onChange={(e) => upd('autoRotate', e.target.checked)} /></Row>
      <div className="text-[10px] text-gray-500 mt-3 leading-snug">Left-drag: orbit · Right-drag: pan · Scroll: zoom</div>
    </div>
  );
}

export default function TopicMap({ onSelect }) {
  const containerRef = useRef(null);
  const fgRef = useRef(null);
  const { status, nodes: classified } = useGraph();
  const [hovered, setHovered] = useState(null);
  const [selected, setSelected] = useState(null);
  const [minFreq, setMinFreq] = useState(2);
  const [size, setSize] = useState({ w: 1000, h: 720 });
  const [highlight, setHighlight] = useState({ nodes: new Set(), links: new Set() });
  const [settings, setSettings] = useState({
    charge: -100, linkDistance: 50, alwaysLabels: false, drag: false, autoRotate: false,
    labelDensity: 4,
  });

  useEffect(() => {
    if (!containerRef.current) return;
    const ro = new ResizeObserver((entries) => {
      const cr = entries[0].contentRect;
      setSize({ w: Math.max(400, cr.width), h: Math.max(400, cr.height) });
    });
    ro.observe(containerRef.current);
    return () => ro.disconnect();
  }, []);

  const topicGraph = useMemo(() => {
    if (status !== 'ready' || !classified) return null;
    return buildTopicGraph(classified ?? [], minFreq);
  }, [status, classified, minFreq]);

  const fgData = useMemo(() => topicGraph ? topicGraphToFG(topicGraph) : { nodes: [], links: [] }, [topicGraph]);

  useEffect(() => {
    if (!fgRef.current) return;
    fgRef.current.d3Force('charge')?.strength(settings.charge);
    fgRef.current.d3Force('link')?.distance(settings.linkDistance);
    fgRef.current.d3ReheatSimulation?.();
  }, [settings.charge, settings.linkDistance, fgData]);

  const recenter = () => {
    if (fgRef.current?.zoomToFit) fgRef.current.zoomToFit(800, 60);
  };

  useEffect(() => {
    if (!fgRef.current || fgData.nodes.length === 0) return;
    const ts = [
      setTimeout(() => recenter(), 200),
      setTimeout(() => recenter(), 1500),
      setTimeout(() => recenter(), 3500),
    ];
    return () => ts.forEach(clearTimeout);
  }, [fgData]);

  useEffect(() => {
    if (!fgRef.current) return;
    const controls = fgRef.current.controls?.();
    if (!controls) return;
    controls.autoRotate = settings.autoRotate;
    controls.autoRotateSpeed = 0.8;
  }, [settings.autoRotate, fgData]);

  useEffect(() => {
    if (fgRef.current?.refresh) fgRef.current.refresh();
  }, [settings.labelDensity, settings.alwaysLabels, highlight]);

  useEffect(() => {
    if (!selected) {
      setHighlight({ nodes: new Set(), links: new Set() });
      return;
    }
    const nodes = new Set([selected]);
    const links = new Set();
    for (const l of fgData.links) {
      const sId = typeof l.source === 'object' ? l.source.id : l.source;
      const tId = typeof l.target === 'object' ? l.target.id : l.target;
      if (sId === selected) { nodes.add(tId); links.add(l); }
      else if (tId === selected) { nodes.add(sId); links.add(l); }
    }
    setHighlight({ nodes, links });
  }, [selected, fgData]);

  const materialCache = new Map();
  const getMaterial = (color, dim) => {
    const key = `${color}-${dim ? 1 : 0}`;
    if (!materialCache.has(key)) {
      materialCache.set(key, new THREE.MeshLambertMaterial({
        color, transparent: true, opacity: dim ? 0.18 : 0.95,
        emissive: color, emissiveIntensity: dim ? 0.05 : 0.4,
      }));
    }
    return materialCache.get(key);
  };

  const nodeThreeObject = (node) => {
    const showLabel = settings.alwaysLabels || node.val >= settings.labelDensity;
    const isHighlight = highlight.nodes.size === 0 || highlight.nodes.has(node.id);
    if (!showLabel || !isHighlight) return new THREE.Object3D();
    const sprite = new SpriteText(node.label);
    sprite.color = '#f1f5f9';
    sprite.backgroundColor = 'rgba(15,23,42,0.85)';
    sprite.padding = 3;
    sprite.borderRadius = 4;
    sprite.textHeight = 5;
    sprite.position.set(0, Math.cbrt(node.val) * 1.6 + 5, 0);
    return sprite;
  };

  if (status !== 'ready') return <div className="text-gray-400 p-4">Waiting for graph…</div>;
  const stats = topicGraph ? { topics: topicGraph.order, edges: topicGraph.size } : { topics: 0, edges: 0 };

  return (
    <div className="grid grid-cols-1 lg:grid-cols-4 gap-4">
      <div className="lg:col-span-3">
        <div className="relative">
          <div className="absolute top-3 left-3 z-10 bg-gray-900/85 backdrop-blur border border-gray-700 rounded-lg px-3 py-2 text-xs text-gray-300 shadow-xl">
            <div>{stats.topics} topics · {stats.edges} co-occurrences</div>
            <div className="text-gray-500 mt-1">Edge weight = repos sharing both topics</div>
            <div className="mt-2">
              <label className="text-gray-500">Min repos per topic: </label>
              <input type="number" min={2} max={10} value={minFreq}
                onChange={(e) => setMinFreq(Math.max(2, Math.min(10, Number(e.target.value) || 2)))}
                className="w-12 bg-gray-800 border border-gray-700 rounded px-1 text-gray-200" />
            </div>
          </div>
          <ControlPanel settings={settings} setSettings={setSettings} onRecenter={recenter} />
          {hovered && !selected && (
            <div className="absolute bottom-3 left-3 z-10 bg-gray-900/95 backdrop-blur border border-gray-700 rounded-lg p-3 text-sm text-gray-100 pointer-events-none shadow-xl">
              <div className="font-bold text-cyan-300">#{hovered.label}</div>
              <div className="text-xs text-gray-400 mt-1">{hovered.freq} repos</div>
            </div>
          )}
          <div ref={containerRef} style={{ width: '100%', height: '78vh', background: 'radial-gradient(circle at 70% 30%, #1e293b 0%, #020617 70%)', borderRadius: 12, overflow: 'hidden' }}>
            {topicGraph && topicGraph.order === 0 ? (
              <div className="p-12 text-center text-gray-500">No topics meet the minimum frequency. Lower the threshold.</div>
            ) : (
              <ForceGraph3D
                ref={fgRef}
                width={size.w}
                height={size.h}
                graphData={fgData}
                backgroundColor="rgba(0,0,0,0)"
                showNavInfo={false}
                nodeRelSize={6}
                nodeVal={(n) => n.val}
                nodeLabel=""
                nodeColor={(n) => {
                  if (highlight.nodes.size > 0 && !highlight.nodes.has(n.id)) return 'rgba(75,85,99,0.3)';
                  return COMMUNITY_PALETTE[n.community % COMMUNITY_PALETTE.length];
                }}
                nodeOpacity={0.95}
                nodeThreeObject={nodeThreeObject}
                nodeThreeObjectExtend={true}
                linkColor={(l) => {
                  if (highlight.links.size > 0) return highlight.links.has(l) ? 'rgba(34,211,238,0.85)' : 'rgba(75,85,99,0.04)';
                  return 'rgba(148,163,184,0.16)';
                }}
                linkWidth={(l) => 0.3 + Math.min(2, l.weight * 0.4)}
                linkOpacity={0.5}
                linkDirectionalParticles={(l) => (highlight.links.has(l) ? 3 : 0)}
                linkDirectionalParticleSpeed={0.006}
                linkDirectionalParticleColor={() => 'rgba(34,211,238,1)'}
                linkDirectionalParticleWidth={2.5}
                d3AlphaDecay={0.025}
                d3VelocityDecay={0.4}
                cooldownTicks={100}
                warmupTicks={20}
                enableNodeDrag={settings.drag}
                onNodeClick={(n) => setSelected(n.id === selected ? null : n.id)}
                onBackgroundClick={() => setSelected(null)}
                onNodeHover={(n) => setHovered(n || null)}
              />
            )}
          </div>
        </div>
      </div>
      <div className="lg:col-span-1">
        {selected ? (
          <ReposByTopic topic={selected} repos={classified ?? []} onSelect={onSelect} />
        ) : (
          <div className="bg-gray-800 rounded-lg p-4 border border-gray-700 text-sm text-gray-400">
            Click a topic to see repos using it. Bigger nodes = more repos. Edges = topics that appear together.
          </div>
        )}
      </div>
    </div>
  );
}
