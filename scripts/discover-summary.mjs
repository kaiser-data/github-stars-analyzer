#!/usr/bin/env node
// Consolidate every reports/*.candidates.json into one cross-report shortlist.
//
//   node scripts/discover-summary.mjs [--min-fit 75] [--min-health 55] [--top 40]
//
// A repo that surfaces for several reports is ranked once, carrying the list of
// landscapes that wanted it — that overlap is itself a relevance signal.

import { readdirSync, readFileSync, writeFileSync } from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '..');
const REPORTS = path.join(ROOT, 'reports');

function arg(name, fallback) {
  const hit = process.argv.slice(2).find((a) => a.startsWith(`--${name}=`));
  if (hit) return Number(hit.split('=')[1]);
  const i = process.argv.indexOf(`--${name}`);
  return i > -1 && process.argv[i + 1] ? Number(process.argv[i + 1]) : fallback;
}

const minFit = arg('min-fit', 75);
const minHealth = arg('min-health', 55);
const top = arg('top', 40);

const byRepo = new Map();
let files = 0;

for (const f of readdirSync(REPORTS).filter((f) => f.endsWith('.candidates.json'))) {
  files += 1;
  const d = JSON.parse(readFileSync(path.join(REPORTS, f), 'utf8'));
  for (const c of d.candidates) {
    const key = c.full_name.toLowerCase();
    const prev = byRepo.get(key);
    const entry = prev ?? { ...c, reports: [], best_fit: 0 };
    entry.reports.push({ slug: d.slug, state: c.state, fit: c.score.total });
    entry.best_fit = Math.max(entry.best_fit, c.score.total);
    // Keep the highest-relevance rendering of the repo.
    if (!prev || c.score.parts.relevance > entry.score.parts.relevance) {
      Object.assign(entry, { ...c, reports: entry.reports, best_fit: entry.best_fit });
    }
    byRepo.set(key, entry);
  }
}

const ranked = [...byRepo.values()]
  .filter((c) => c.best_fit >= minFit && (c.health_score ?? 0) >= minHealth)
  .sort((a, b) => (b.reports.length - a.reports.length) || (b.best_fit - a.best_fit))
  .slice(0, top);

const lines = [];
lines.push(`# Cross-report candidate shortlist`);
lines.push('');
lines.push(`${byRepo.size} distinct repos across ${files} reports; `
  + `${ranked.length} shown at fit >= ${minFit} and health >= ${minHealth}.`);
lines.push('');
lines.push('Repos wanted by more than one report rank first — that overlap is a relevance signal in itself.');
lines.push('');
lines.push('| Repo | Wanted by | ★ | Lang | Stage | Health | Pushed | Fit | What it is |');
lines.push('|---|---|---|---|---|---|---|---|---|');
for (const c of ranked) {
  const where = c.reports.map((r) => `${r.slug}${r.state === 'known-gap' ? '*' : ''}`).join(', ');
  lines.push('| ' + [
    `[${c.full_name}](https://github.com/${c.full_name})`,
    where,
    (c.stars ?? 0).toLocaleString('en-US'),
    c.primary_language ?? '—',
    c.lifecycle_stage,
    c.health_score,
    `${c.days_since_push}d`,
    `**${c.best_fit}**`,
    String(c.description ?? '').replace(/\|/g, '\\|').slice(0, 90),
  ].join(' | ') + ' |');
}
lines.push('');
lines.push('`*` marks a repo the report itself named as missing.');
lines.push('');

const out = lines.join('\n');
writeFileSync(path.join(REPORTS, 'ALL.candidates.md'), out);
console.log(out);
console.error(`\nWrote reports/ALL.candidates.md — ${byRepo.size} distinct repos from ${files} reports`);
