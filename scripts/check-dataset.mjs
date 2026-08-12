// Sanity gate between classify and precompute.
//
// A refresh that silently loses most of the dataset used to sail through the
// rest of the pipeline and get committed — on 2026-08-11 a throttled ingest
// produced 96 repos out of 1,598 and only an unrelated IndexError stopped it
// from reaching production. This compares the freshly classified dataset with
// the most recent snapshot and exits non-zero if it shrank implausibly.
//
// Usage: node scripts/check-dataset.mjs [--max-drop=0.1] [--min-repos=50]
//                                       [--classified=data/classified.json]

import { readFileSync, readdirSync, existsSync } from 'node:fs';
import path from 'node:path';

const args = process.argv.slice(2);
const arg = (name, fallback) => {
  const a = args.find((x) => x.startsWith(`--${name}=`));
  return a ? a.split('=')[1] : fallback;
};

const CLASSIFIED = arg('classified', 'data/classified.json');
const SNAPSHOT_DIR = arg('snapshots', 'data/snapshots');
// Stars come and go, so a small drop is normal; 10% of a ~1,600-repo dataset is
// 160 repos, far more than anyone unstars in a week.
const MAX_DROP = Number(arg('max-drop', 0.1));
const MIN_REPOS = Number(arg('min-repos', 50));

function fail(msg, detail = []) {
  console.error(`✗ Dataset check failed: ${msg}`);
  for (const d of detail) console.error(`  ${d}`);
  console.error('  Refusing to continue — this dataset must not be graphed or committed.');
  process.exit(1);
}

if (!existsSync(CLASSIFIED)) fail(`${CLASSIFIED} does not exist`);

const current = JSON.parse(readFileSync(CLASSIFIED, 'utf8'));
const count = current.repos?.length ?? 0;

if (count < MIN_REPOS) {
  fail(`only ${count} repos in ${CLASSIFIED} (floor is ${MIN_REPOS})`);
}

// Snapshots are named <YYYY-MM-DD>.json, so lexical sort is chronological.
const snapshots = existsSync(SNAPSHOT_DIR)
  ? readdirSync(SNAPSHOT_DIR).filter((f) => f.endsWith('.json')).sort()
  : [];

// The snapshot for this dataset's own vintage is written by a *later* step, but
// re-running the pipeline on unchanged data would otherwise compare against
// itself and mask a drop. Skip any snapshot that shares our generatedAt date.
const currentDate = (current.generatedAt ?? '').slice(0, 10);
const baselineFile = [...snapshots].reverse().find((f) => f.slice(0, 10) !== currentDate);

if (!baselineFile) {
  console.error(`✓ Dataset check: ${count} repos, no earlier snapshot to compare against.`);
  process.exit(0);
}

const baseline = JSON.parse(readFileSync(path.join(SNAPSHOT_DIR, baselineFile), 'utf8'));
const baseCount = Object.keys(baseline.repos ?? {}).length;
const drop = baseCount ? (baseCount - count) / baseCount : 0;

if (drop > MAX_DROP) {
  const present = new Set(current.repos.map((r) => r.full_name));
  const missing = Object.keys(baseline.repos).filter((n) => !present.has(n));
  fail(
    `${count} repos vs ${baseCount} in ${baselineFile} — down ${(drop * 100).toFixed(1)}% ` +
    `(limit ${(MAX_DROP * 100).toFixed(0)}%)`,
    [
      `${missing.length} repos vanished, e.g. ${missing.slice(0, 5).join(', ')}`,
      'Most likely an ingest that was throttled or partially failed, not real unstarring.',
      'Check the ingest log for [rate_limit] / [network] failures before overriding.',
    ],
  );
}

const delta = count - baseCount;
console.error(
  `✓ Dataset check: ${count} repos ` +
  `(${delta >= 0 ? '+' : ''}${delta} vs ${baseCount} in ${baselineFile}).`,
);
