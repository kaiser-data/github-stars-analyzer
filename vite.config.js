import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// three-forcegraph's animation cycle calls tickFrame() BEFORE _update() processes
// new prop changes. On the very first frame after mount, state.layout is undefined
// (graphData setter hasn't run yet), but state.engineRunning is true → crash.
// This plugin adds a null guard to layoutTick in the pre-bundled three-forcegraph
// chunk so the first frame skips gracefully instead of crashing.
function patchThreeForcegraph() {
  return {
    name: 'patch-three-forcegraph-layout-guard',
    transform(code, id) {
      // Match both the npm source file (prod Rollup) and the dev pre-bundle chunk
      if (!id.includes('three-forcegraph') && !id.includes('chunk-YH5VU6GS')) return;
      if (!code.includes('state.layout[isD3Sim')) return;
      // Source uses single quotes; pre-bundled chunk uses double quotes — handle both
      const patched = code
        .replace("state.layout[isD3Sim ? 'tick' : 'step']()", "state.layout && state.layout[isD3Sim ? 'tick' : 'step']()")
        .replace('state.layout[isD3Sim ? "tick" : "step"]()', 'state.layout && state.layout[isD3Sim ? "tick" : "step"]()');
      if (patched === code) return;
      return { code: patched, map: null };
    },
  };
}

// Heavy 3D / force-graph deps split off LabApp so the initial route can
// stream + parse the React shell first; the 3D chunk loads in parallel.
const THREE_CHUNK = new Set([
  'three',
  'three-spritetext',
  'three-forcegraph',
  'three-render-objects',
  '3d-force-graph',
  'react-force-graph-3d',
  'd3-force-3d',
]);

export default defineConfig({
  plugins: [react(), patchThreeForcegraph()],
  resolve: {
    dedupe: ['three'],
  },
  optimizeDeps: {
    include: [
      'react-force-graph-3d',
      'three',
      'three-spritetext',
      'd3-force-3d',
      'three-forcegraph',
      'three-render-objects',
      '3d-force-graph',
    ],
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (!id.includes('node_modules')) return;
          // Match the package name (the segment after the last "node_modules/",
          // accounting for scoped packages like @foo/bar).
          const m = id.match(/node_modules\/(?:(@[^/]+)\/)?([^/]+)/);
          if (!m) return;
          const pkg = m[1] ? `${m[1]}/${m[2]}` : m[2];
          if (THREE_CHUNK.has(pkg)) return 'three';
        },
      },
    },
  },
})
