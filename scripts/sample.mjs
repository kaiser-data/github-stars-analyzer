// Stratified sample of starred repos: 40 top-by-stars + 30 most-recent + 30 random middle.
// Usage: node --env-file=.env scripts/sample.mjs <username> [--total 100]

import { writeFileSync, mkdirSync } from 'node:fs';
import { rest, logRate } from './lib/github.mjs';

const args = process.argv.slice(2);
const username = args.find((a) => !a.startsWith('--')) ?? 'kaiser-data';
const totalArg = args.find((a) => a.startsWith('--total='));
const ALL = args.includes('--all');
const TOTAL = ALL ? Infinity : (totalArg ? Number(totalArg.split('=')[1]) : 100);
const TOP_BY_STARS = ALL ? 0 : Math.round(TOTAL * 0.4);
const RECENT = ALL ? 0 : Math.round(TOTAL * 0.3);
const RANDOM_MIDDLE = ALL ? 0 : TOTAL - TOP_BY_STARS - RECENT;

if (ALL) console.error(`Sampling ALL non-archived stars from ${username}`);
else console.error(`Sampling ${TOTAL} stars from ${username} (top=${TOP_BY_STARS}, recent=${RECENT}, random=${RANDOM_MIDDLE})`);

async function fetchAllStarred() {
  const all = [];
  let page = 1;
  while (true) {
    const path = `/users/${username}/starred?per_page=100&page=${page}`;
    const { data, headers } = await rest(path, {
      accept: 'application/vnd.github.star+json', // include starred_at
    });
    if (data.length === 0) break;
    for (const item of data) {
      // With star+json the shape is {starred_at, repo: {...}}
      const repo = item.repo ?? item;
      all.push({
        id: repo.id,
        full_name: repo.full_name,
        owner: repo.owner.login,
        name: repo.name,
        stargazers_count: repo.stargazers_count,
        starred_at: item.starred_at ?? null,
        archived: repo.archived,
      });
    }
    logRate(headers, `page ${page}`);
    if (data.length < 100) break;
    page += 1;
    if (page > 50) {
      console.error('  hit safety cap of 50 pages (5000 stars), stopping');
      break;
    }
  }
  return all;
}

function pickStratified(all) {
  // Filter out archived to keep the spike clean.
  const candidates = all.filter((r) => !r.archived);
  if (ALL) return candidates.map((r) => ({ ...r, stratum: 'all' }));
  if (candidates.length <= TOTAL) return candidates;

  const byStars = [...candidates].sort((a, b) => b.stargazers_count - a.stargazers_count);
  const byRecent = [...candidates].sort((a, b) => {
    const da = a.starred_at ? Date.parse(a.starred_at) : 0;
    const db = b.starred_at ? Date.parse(b.starred_at) : 0;
    return db - da;
  });

  const picked = new Map();
  for (const r of byStars.slice(0, TOP_BY_STARS)) picked.set(r.id, { ...r, stratum: 'top-stars' });
  for (const r of byRecent) {
    if (picked.size >= TOP_BY_STARS + RECENT) break;
    if (!picked.has(r.id)) picked.set(r.id, { ...r, stratum: 'recent' });
  }

  // Random middle: shuffle remaining and take RANDOM_MIDDLE
  const remaining = candidates.filter((r) => !picked.has(r.id));
  for (let i = remaining.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [remaining[i], remaining[j]] = [remaining[j], remaining[i]];
  }
  for (const r of remaining.slice(0, RANDOM_MIDDLE)) {
    picked.set(r.id, { ...r, stratum: 'random-middle' });
  }
  return [...picked.values()];
}

const all = await fetchAllStarred();
console.error(`Fetched ${all.length} total stars`);
const sample = pickStratified(all);
console.error(`Stratified sample: ${sample.length}`);
const counts = sample.reduce((acc, r) => ((acc[r.stratum] = (acc[r.stratum] ?? 0) + 1), acc), {});
console.error(`  by stratum: ${JSON.stringify(counts)}`);

mkdirSync('src/data', { recursive: true });
const out = ALL ? `src/data/sample-all.json` : `src/data/sample-${TOTAL}.json`;
writeFileSync(out, JSON.stringify({ username, total: sample.length, generatedAt: new Date().toISOString(), repos: sample }, null, 2));
console.error(`Wrote ${out}`);
