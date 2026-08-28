// Deterministic lifecycle + health classifier (no LLM).
// Usage: node scripts/classify.mjs [--in src/data/raw-100.json]
// Scoring lives in lib/classify-core.mjs so discover.mjs can reuse it.

import { readFileSync, writeFileSync } from 'node:fs';
import { classifyRepo } from './lib/classify-core.mjs';

const args = process.argv.slice(2);
const inArg = args.find((a) => a.startsWith('--in='));
const IN = inArg ? inArg.split('=')[1] : 'src/data/raw-100.json';
const OUT = IN.replace('raw-', 'classified-');

const data = JSON.parse(readFileSync(IN, 'utf8'));
const now = Date.now();

const classified = data.repos.map((r) => classifyRepo(r, now));

const dist = classified.reduce((acc, r) => ((acc[r.lifecycle_stage] = (acc[r.lifecycle_stage] ?? 0) + 1), acc), {});
console.error('Lifecycle distribution:', dist);
console.error('Avg health score:', Math.round(classified.reduce((s, r) => s + r.health_score, 0) / classified.length));

writeFileSync(OUT, JSON.stringify({
  ...data,
  generatedAt: new Date().toISOString(),
  distribution: dist,
  repos: classified,
}, null, 2));
console.error(`Wrote ${OUT}`);
