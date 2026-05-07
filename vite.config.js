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
})
