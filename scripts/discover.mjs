#!/usr/bin/env node
// Find repos that belong in a landscape report but are not in the stars.
//
//   node scripts/discover.mjs --report agentic-terminals
//   node scripts/discover.mjs --report rag-tooling --extra a/b,c/d --min-stars 500
//
// Writes reports/<slug>.candidates.md and .json, and prints the table.

import { writeFileSync } from 'node:fs';
import path from 'node:path';

import { loadLandscape, stateFor } from './lib/discover/landscape.mjs';
import { parseExtra, buildQueries, selectCandidates } from './lib/discover/candidates.mjs';
import { resolveRepos, searchRepos } from './lib/discover/fetch.mjs';
import { classifyKind, fitScore } from './lib/discover/score.mjs';
import { renderMarkdown, renderJson } from './lib/discover/render.mjs';

const ROOT = path.resolve(import.meta.dirname, '..');

function arg(name, fallback = undefined) {
  const hit = process.argv.slice(2).find((a) => a.startsWith(`--${name}=`));
  if (hit) return hit.split('=').slice(1).join('=');
  const idx = process.argv.indexOf(`--${name}`);
  if (idx > -1 && process.argv[idx + 1] && !process.argv[idx + 1].startsWith('--')) return process.argv[idx + 1];
  return fallback;
}
const flag = (name) => process.argv.includes(`--${name}`);

const slug = arg('report');
if (!slug) {
  console.error('Usage: node scripts/discover.mjs --report <slug> [--extra a/b,c/d] [--min-stars 200] [--max-stale-days 365] [--limit 40] [--no-search]');
  process.exit(2);
}

const minStars = Number(arg('min-stars', 200));
const maxStaleDays = Number(arg('max-stale-days', 365));
const limit = Number(arg('limit', 40));
const now = Date.now();

const landscape = loadLandscape(slug);
console.error(`Landscape "${slug}": ${landscape.covered.size} repos named, ${landscape.held.length} held, ${landscape.knownGaps.length} known gaps`);

// Known gaps come free — the report already named them, no search required.
const wanted = new Map();
for (const name of landscape.knownGaps) wanted.set(name.toLowerCase(), name);

for (const name of parseExtra(arg('extra'))) {
  if (!landscape.starred.has(name.toLowerCase())) wanted.set(name.toLowerCase(), name);
}

if (!flag('no-search')) {
  const queries = buildQueries(landscape, { minStars, maxStaleDays, now });
  console.error(`Searching with ${queries.length} queries…`);
  const found = await searchRepos(queries);
  for (const f of found) {
    const key = f.full_name.toLowerCase();
    if (!landscape.starred.has(key)) wanted.set(key, f.full_name);
  }
}

console.error(`Resolving ${wanted.size} candidate names…`);
const { resolved, renamed, unresolved } = await resolveRepos([...wanted.values()], { now });

// State is re-checked on the RESOLVED name — a rename can land on something
// already held. selectCandidates then exempts known gaps from the heuristics.
const scored = selectCandidates(resolved, {
  stateOf: (name) => stateFor(name, landscape),
  minStars,
  maxStaleDays,
})
  .map((r) => {
    const kind = classifyKind(r);
    return { ...r, kind, score: fitScore({ ...r, kind }, landscape.vocabulary, { state: r.state }) };
  })
  .sort((a, b) => b.score.total - a.score.total);

// `limit` caps search noise, so it applies to `new` finds only. Letting it
// truncate known gaps would lose them as silently as the filters did.
const candidates = [
  ...scored.filter((r) => r.state === 'known-gap'),
  ...scored.filter((r) => r.state !== 'known-gap').slice(0, limit),
].sort((a, b) => b.score.total - a.score.total);

const result = {
  slug,
  generated: new Date(now).toISOString().slice(0, 10),
  heldCount: landscape.held.length,
  candidates,
  renamed,
  unresolved,
};

const md = renderMarkdown(result);
writeFileSync(path.join(ROOT, `reports/${slug}.candidates.md`), md);
writeFileSync(path.join(ROOT, `reports/${slug}.candidates.json`), JSON.stringify(renderJson(result), null, 2));

console.log(md);
console.error(`\nWrote reports/${slug}.candidates.md and .json`);
