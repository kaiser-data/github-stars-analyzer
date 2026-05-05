import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  // Pre-bundle d3-force-3d and three-forcegraph so Vite's dev server doesn't
  // mis-resolve their hybrid CJS/ESM exports — without this, react-force-graph-3d's
  // simulation tick crashes with "Cannot read properties of undefined (reading 'tick')".
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
