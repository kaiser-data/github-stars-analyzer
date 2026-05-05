import React, { useEffect, useMemo, useRef, useState } from 'react';
import ForceGraph3D from 'react-force-graph-3d';
import * as THREE from 'three';
import SpriteText from 'three-spritetext';
import { useGraph } from './GraphProvider';

const COMMUNITY_PALETTE = [
  '#ef4444', '#f59e0b', '#10b981', '#3b82f6', '#a78bfa',
  '#ec4899', '#06b6d4', '#84cc16', '#f97316', '#8b5cf6',
  '#14b8a6', '#eab308', '#22c55e', '#0ea5e9', '#d946ef',
];

function graphologyToFG(graph) {
  const nodes = [];
  const links = [];
  graph.forEachNode((id, attrs) => {
    if (attrs.kind !== 'repo') return;
    nodes.push({
      id,
      full_name: attrs.full_name,
      community: attrs.community ?? 0,
      lifecycle_stage: attrs.lifecycle_stage,
      stars: attrs.stars ?? 0,
      health_score: attrs.health_score ?? 0,
      unique_authors_90d: attrs.unique_authors_90d ?? 0,
      description: attrs.description,
      one_liner: attrs.one_liner,
      pagerank: attrs.pagerank ?? 0,
      val: 1 + Math.log10(1 + (attrs.stars ?? 0)) * 1.4 + (attrs.pagerank ?? 0) * 50,
    });
  });
  graph.forEachEdge((edge, attrs, source, target) => {
    links.push({
      source, target,
      weight: attrs.weight ?? 1,
      shared_authors: attrs.shared_authors ?? [],
      shared_topics: attrs.shared_topics ?? [],
    });
  });
  return { nodes, links };
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
    <div className="absolute top-3 right-3 z-10 bg-gray-900/90 backdrop-blur border border-gray-700 rounded-lg p-3 text-xs text-gray-200 shadow-xl w-[260px]">
      <button
        onClick={onRecenter}
        className="w-full mb-2 px-3 py-1.5 bg-blue-600 hover:bg-blue-500 rounded text-white font-medium"
      >Recenter view</button>
      <div className="text-[10px] uppercase tracking-wider text-gray-500 mb-2">Layout</div>
      <Row label="Spread"><input type="range" min={-300} max={-30} step={5} value={settings.charge} onChange={(e) => upd('charge', Number(e.target.value))} className="w-full" /></Row>
      <Row label="Link length"><input type="range" min={20} max={300} step={5} value={settings.linkDistance} onChange={(e) => upd('linkDistance', Number(e.target.value))} className="w-full" /></Row>
      <div className="text-[10px] uppercase tracking-wider text-gray-500 mt-3 mb-1">Display</div>
      <Row label="Label density">
        <input type="range" min={1} max={12} step={0.5} value={settings.labelDensity}
          onChange={(e) => upd('labelDensity', Number(e.target.value))} className="w-full" />
      </Row>
      <Row label="Labels always"><input type="checkbox" checked={settings.alwaysLabels} onChange={(e) => upd('alwaysLabels', e.target.checked)} /></Row>
      <Row label="Drag nodes"><input type="checkbox" checked={settings.drag} onChange={(e) => upd('drag', e.target.checked)} /></Row>
      <Row label="Auto-rotate"><input type="checkbox" checked={settings.autoRotate} onChange={(e) => upd('autoRotate', e.target.checked)} /></Row>
      <div className="text-[10px] text-gray-500 mt-3 leading-snug">Left-drag: orbit · Right-drag: pan · Scroll: zoom · Click node: focus</div>
    </div>
  );
}

export default function MapView({ onSelectNode, focusedRepoName }) {
  const fgRef = useRef(null);
  const containerRef = useRef(null);
  const { status, graph, stats, error } = useGraph();
  const [hovered, setHovered] = useState(null);
  const [size, setSize] = useState({ w: 1200, h: 720 });
  const [highlightLinks, setHighlightLinks] = useState(new Set());
  const [highlightNodes, setHighlightNodes] = useState(new Set());
  const [settings, setSettings] = useState({
    charge: -120, linkDistance: 60, alwaysLabels: false, drag: false, autoRotate: false,
    labelDensity: 5, // val threshold — lower = more labels visible
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

  const data = useMemo(() => {
    if (status !== 'ready' || !graph) return { nodes: [], links: [] };
    return graphologyToFG(graph);
  }, [status, graph]);

  useEffect(() => {
    if (!fgRef.current) return;
    const fg = fgRef.current;
    if (fg.d3Force) {
      const charge = fg.d3Force('charge');
      if (charge) charge.strength(settings.charge);
      const link = fg.d3Force('link');
      if (link) link.distance(settings.linkDistance);
      fg.d3ReheatSimulation?.();
    }
  }, [settings.charge, settings.linkDistance, data]);

  // Re-run nodeThreeObject when label settings change (forces label refresh)
  useEffect(() => {
    if (fgRef.current?.refresh) fgRef.current.refresh();
  }, [settings.labelDensity, settings.alwaysLabels, highlightNodes]);

  const recenter = () => {
    if (fgRef.current?.zoomToFit) fgRef.current.zoomToFit(800, 80);
  };

  useEffect(() => {
    if (!fgRef.current || data.nodes.length === 0) return;
    const ts = [
      setTimeout(() => recenter(), 500),
      setTimeout(() => recenter(), 2000),
      setTimeout(() => recenter(), 4000),
    ];
    return () => ts.forEach(clearTimeout);
  }, [data]);

  useEffect(() => {
    if (!fgRef.current) return;
    const controls = fgRef.current.controls?.();
    if (!controls) return;
    controls.autoRotate = settings.autoRotate;
    controls.autoRotateSpeed = 0.8;
  }, [settings.autoRotate, data]);

  useEffect(() => {
    if (!fgRef.current) return;
    if (!focusedRepoName) {
      setHighlightLinks(new Set());
      setHighlightNodes(new Set());
      return;
    }
    const node = data.nodes.find((n) => n.full_name === focusedRepoName);
    if (!node) return;
    const neighbors = new Set();
    const links = new Set();
    for (const l of data.links) {
      const sId = typeof l.source === 'object' ? l.source.id : l.source;
      const tId = typeof l.target === 'object' ? l.target.id : l.target;
      if (sId === node.id) { neighbors.add(tId); links.add(l); }
      else if (tId === node.id) { neighbors.add(sId); links.add(l); }
    }
    neighbors.add(node.id);
    setHighlightNodes(neighbors);
    setHighlightLinks(links);
    if (node.x != null && fgRef.current.cameraPosition) {
      const dist = 140;
      const distRatio = 1 + dist / Math.hypot(node.x, node.y, node.z);
      fgRef.current.cameraPosition(
        { x: node.x * distRatio, y: node.y * distRatio, z: node.z * distRatio },
        node, 1000,
      );
    }
  }, [focusedRepoName, data]);

  if (status === 'loading') return <div className="text-gray-400 p-6">Loading graph…</div>;
  if (status === 'error') return <div className="text-red-400 p-6">Failed: {error}</div>;

  const nodeThreeObject = (node) => {
    const showLabel = settings.alwaysLabels || node.val >= settings.labelDensity;
    const isHighlight = highlightNodes.size === 0 || highlightNodes.has(node.id);
    if (!showLabel || !isHighlight) return new THREE.Object3D();
    const [owner, repoName] = node.full_name.split('/');
    const truncated = (repoName ?? node.full_name).length > 22
      ? (repoName ?? node.full_name).slice(0, 22) + '…'
      : (repoName ?? node.full_name);

    const r = Math.cbrt(node.val) * 1.6;
    const group = new THREE.Group();

    // Primary label: repo name (big, bright)
    const primary = new SpriteText(truncated);
    primary.color = '#f1f5f9';
    primary.backgroundColor = 'rgba(15,23,42,0.85)';
    primary.padding = 3;
    primary.borderRadius = 4;
    primary.textHeight = 5;
    primary.position.set(0, r + 5, 0);
    group.add(primary);

    // Secondary label: owner (small, dim) — only for hubs and only if owner adds info
    if (owner && (node.val > 10 || settings.alwaysLabels)) {
      const ownerLabel = new SpriteText(owner);
      ownerLabel.color = '#94a3b8';
      ownerLabel.backgroundColor = 'rgba(15,23,42,0.6)';
      ownerLabel.padding = 2;
      ownerLabel.borderRadius = 3;
      ownerLabel.textHeight = 2.5;
      ownerLabel.position.set(0, r + 9.5, 0);
      group.add(ownerLabel);
    }
    return group;
  };

  return (
    <div className="relative">
      <div className="absolute top-3 left-3 z-10 bg-gray-900/85 backdrop-blur border border-gray-700 rounded-lg px-3 py-2 text-xs text-gray-300 shadow-xl">
        <div>{stats.nodeCount} repos · {stats.edgeCount} edges · {stats.communityCount} communities</div>
        <div className="text-gray-500 mt-1">Color = community · Size = stars + PageRank</div>
        {focusedRepoName && <div className="mt-1 text-blue-300">Focused: {focusedRepoName}</div>}
      </div>
      <ControlPanel settings={settings} setSettings={setSettings} onRecenter={recenter} />
      {hovered && (
        <div className="absolute bottom-3 left-3 z-10 bg-gray-900/95 backdrop-blur border border-gray-700 rounded-lg p-4 text-sm text-gray-100 max-w-md shadow-xl pointer-events-none">
          <div className="font-bold text-blue-400">{hovered.full_name}</div>
          <div className="text-xs text-gray-400 mt-1">{hovered.description?.slice(0, 200)}</div>
          {hovered.one_liner && <div className="text-gray-200 mt-2 italic">{hovered.one_liner}</div>}
          <div className="flex flex-wrap gap-3 mt-3 text-xs">
            <span className="px-2 py-0.5 rounded bg-gray-700">{hovered.lifecycle_stage}</span>
            <span>★ {hovered.stars?.toLocaleString()}</span>
            <span>health {hovered.health_score}</span>
            <span>authors90 {hovered.unique_authors_90d}</span>
          </div>
        </div>
      )}
      <div ref={containerRef} style={{ width: '100%', height: '78vh', background: 'radial-gradient(circle at 30% 20%, #1e293b 0%, #020617 70%)', borderRadius: 12, overflow: 'hidden' }}>
        <ForceGraph3D
          ref={fgRef}
          width={size.w}
          height={size.h}
          graphData={data}
          backgroundColor="rgba(0,0,0,0)"
          showNavInfo={false}
          nodeRelSize={6}
          nodeVal={(n) => n.val}
          nodeLabel=""
          nodeColor={(n) => {
            const isHighlight = highlightNodes.size === 0 || highlightNodes.has(n.id);
            if (!isHighlight) return 'rgba(75,85,99,0.3)';
            return COMMUNITY_PALETTE[n.community % COMMUNITY_PALETTE.length];
          }}
          nodeOpacity={0.95}
          nodeThreeObject={nodeThreeObject}
          nodeThreeObjectExtend={true}
          linkColor={(l) => {
            if (highlightLinks.size > 0) return highlightLinks.has(l) ? 'rgba(96,165,250,0.9)' : 'rgba(75,85,99,0.04)';
            return 'rgba(148,163,184,0.16)';
          }}
          linkWidth={(l) => 0.3 + Math.min(2, l.weight * 0.5)}
          linkOpacity={0.5}
          linkDirectionalParticles={(l) => (highlightLinks.has(l) ? 3 : 0)}
          linkDirectionalParticleSpeed={0.005}
          linkDirectionalParticleColor={() => 'rgba(96,165,250,1)'}
          linkDirectionalParticleWidth={2.5}
          d3AlphaDecay={0.02}
          d3VelocityDecay={0.35}
          cooldownTicks={150}
          warmupTicks={50}
          enableNodeDrag={settings.drag}
          onNodeClick={(node) => onSelectNode && onSelectNode({ full_name: node.full_name })}
          onBackgroundClick={() => onSelectNode && onSelectNode(null)}
          onNodeHover={(node) => setHovered(node || null)}
        />
      </div>
    </div>
  );
}
