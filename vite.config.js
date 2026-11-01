import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { readFileSync, writeFileSync, existsSync } from 'node:fs'
import { resolve } from 'node:path'

// The one place the public URL lives. Switching to a custom domain means
// changing this (or setting SITE_URL in the build env) and redeploying.
const SITE_URL = (process.env.SITE_URL || 'https://star-astrolab.vercel.app').replace(/\/+$/, '')
const APP_TABS = ['map', 'topics', 'insights', 'risk', 'all', 'compare', 'reports', 'prompts', 'ask']

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

// The default route (/lab?tab=map) needs the three chunk, but it must not sit
// on the critical path: modulepreload lets the browser fetch it in parallel
// without blocking first paint. Injected here because the hash changes per build.
function preloadThreeChunk() {
  return {
    name: 'preload-three-chunk',
    transformIndexHtml: {
      order: 'post',
      handler(html, ctx) {
        if (!ctx.bundle) return html;
        const three = Object.keys(ctx.bundle).find((k) => /^assets\/three-.*\.js$/.test(k));
        if (!three) return html;
        // Preload the ~1.35 MB 3D chunk only when the page opens on a 3D tab (map is the
        // default). Reports, Ask, Risk… no longer pay for it up front; the chunk still
        // loads lazily if the user switches to Map later.
        const snippet =
          `<script>(function(){var t=new URLSearchParams(location.search).get('tab');` +
          `if(!t||t==='map'||t==='topics'){var l=document.createElement('link');` +
          `l.rel='modulepreload';l.crossOrigin='';l.href='/${three}';document.head.appendChild(l);}})();</script>`;
        return html.replace('</head>', `  ${snippet}\n  </head>`);
      },
    },
  };
}

// Inline the (small, Tailwind-purged) stylesheet into the HTML so first paint
// doesn't wait on a second request, and preload the Latin Geist face so text
// renders in the final font without a swap. Both names carry build hashes.
function inlineCriticalCss() {
  return {
    name: 'inline-critical-css',
    enforce: 'post',
    transformIndexHtml: {
      order: 'post',
      handler(html, ctx) {
        if (!ctx.bundle) return html;
        let out = html;
        for (const [file, chunk] of Object.entries(ctx.bundle)) {
          if (chunk.type !== 'asset' || !/^assets\/index-.*\.css$/.test(file)) continue;
          const link = new RegExp(`<link rel="stylesheet"[^>]*href="/${file.replace(/[.]/g, '\\.')}"[^>]*>`);
          if (link.test(out)) out = out.replace(link, () => `<style>${chunk.source}</style>`);
        }
        const font = Object.keys(ctx.bundle).find((k) => /geist-latin-wght-normal.*\.woff2$/.test(k));
        if (font) {
          out = out.replace(
            '</head>',
            `  <link rel="preload" href="/${font}" as="font" type="font/woff2" crossorigin>\n  </head>`
          );
        }
        return out;
      },
    },
  };
}

// Fills %SITE_URL%, %DESCRIPTION% and the corpus counts (%NODES%, %REPORTS%…)
// from the committed data, so the landing page and meta tags never go stale
// after the weekly refresh. index.html is transformed in the pipeline; the
// files copied verbatim from public/ are rewritten in dist after the bundle.
// Writes sitemap.xml too.
function siteMeta() {
  const fmt = (n) => Number(n).toLocaleString('en-US')
  const vars = () => {
    const graph = JSON.parse(readFileSync(resolve('public/data/graph.json'), 'utf8'))
    const index = JSON.parse(readFileSync(resolve('public/reports/index.json'), 'utf8'))
    const nodes = graph.stats?.nodeCount ?? graph.nodes.length
    return {
      SITE_URL,
      NODES: fmt(nodes),
      EDGES: fmt(graph.stats?.edgeCount ?? graph.links.length),
      COMMUNITIES: fmt(graph.stats?.communityCount ?? Object.keys(graph.communities).length),
      REPORTS: fmt(index.reports.length),
      REPORT_CATEGORIES: fmt(new Set(index.reports.map((r) => r.category)).size),
      DESCRIPTION: `${fmt(nodes)} starred GitHub repositories as a navigable 3D knowledge graph, `
        + `with lifecycle and risk scoring, ${index.reports.length} curated landscape reports, and natural-language search.`,
    }
  }
  const fill = (text, v) => text.replace(/%([A-Z_]+)%/g, (m, k) => (k in v ? v[k] : m))
  let outDir = 'dist'
  return {
    name: 'site-meta',
    configResolved(config) { outDir = config.build.outDir },
    transformIndexHtml: { order: 'pre', handler: (html) => fill(html, vars()) },
    closeBundle() {
      const v = vars()
      for (const file of ['landing.html', 'robots.txt']) {
        const p = resolve(outDir, file)
        if (existsSync(p)) writeFileSync(p, fill(readFileSync(p, 'utf8'), v))
      }
      const urls = [`${SITE_URL}/`, ...APP_TABS.map((t) => `${SITE_URL}/lab?tab=${t}`)]
      writeFileSync(resolve(outDir, 'sitemap.xml'),
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + urls.map((u) => `  <url><loc>${u.replace(/&/g, '&amp;')}</loc></url>`).join('\n')
        + '\n</urlset>\n')
    },
  }
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

// React runtime + router in their own chunk. Without this, Rollup colocates
// react-dom inside the three chunk (every other chunk imports React from it),
// which forces all 1.3MB of three.js onto the critical path of every page.
const REACT_CHUNK = new Set([
  'react',
  'react-dom',
  'scheduler',
  'react-router',
  'react-router-dom',
]);

export default defineConfig({
  plugins: [react(), patchThreeForcegraph(), preloadThreeChunk(), inlineCriticalCss(), siteMeta()],
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
          if (REACT_CHUNK.has(pkg)) return 'react';
        },
      },
    },
  },
})
