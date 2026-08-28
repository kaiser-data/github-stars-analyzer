// A "landscape" is one report: the repos it names, which of those are already
// starred, and the vocabulary to search GitHub with.

import { readFileSync } from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '../../..');

const REPO_LINK = /github\.com\/([A-Za-z0-9_.-]+)\/([A-Za-z0-9_.-]+)/g;

// github.com paths whose first segment is not an owner.
const NON_REPO_OWNERS = new Set([
  'sponsors', 'topics', 'features', 'about', 'settings', 'orgs', 'users',
  'marketplace', 'collections', 'trending', 'search', 'login', 'pricing',
  'apps', 'notifications', 'explore', 'readme',
]);

const STOP = new Set([
  'the', 'and', 'for', 'with', 'from', 'into', 'over', 'per', 'via',
  'what', 'which', 'how', 'why', 'when', 'this', 'that', 'are', 'not',
]);

/** Every repo the markdown names, as lowercase key → display name. */
export function coveredRepos(markdown) {
  const out = new Map();
  for (const m of markdown.matchAll(REPO_LINK)) {
    const owner = m[1];
    const name = m[2].replace(/\.git$/, '');
    if (NON_REPO_OWNERS.has(owner.toLowerCase())) continue;
    if (!name || name === '.' || name === '..') continue;
    const display = `${owner}/${name}`;
    const key = display.toLowerCase();
    if (!out.has(key)) out.set(key, display);
  }
  return out;
}

/** Search terms drawn from the report's own category names and title. */
export function vocabulary(meta) {
  const terms = new Set();
  const sources = [...Object.keys(meta.categories ?? {}), meta.title ?? ''];
  for (const s of sources) {
    for (const w of String(s).toLowerCase().split(/[^a-z0-9+#.]+/)) {
      if (w.length >= 3 && !STOP.has(w)) terms.add(w);
    }
  }
  return [...terms];
}

export function loadLandscape(slug, { root = ROOT } = {}) {
  const md = readFileSync(path.join(root, `reports/${slug}.md`), 'utf8');
  const meta = JSON.parse(readFileSync(path.join(root, `reports/${slug}.meta.json`), 'utf8'));
  const classified = JSON.parse(readFileSync(path.join(root, 'data/classified.json'), 'utf8'));

  const starred = new Set(classified.repos.map((r) => r.full_name.toLowerCase()));
  const covered = coveredRepos(md);

  const held = [];
  const knownGaps = [];
  for (const [key, display] of covered) {
    (starred.has(key) ? held : knownGaps).push(display);
  }
  held.sort();
  knownGaps.sort();

  return { slug, meta, starred, covered, vocabulary: vocabulary(meta), held, knownGaps };
}

/** Which of the three states a resolved name falls into. */
export function stateFor(fullName, { starred, covered }) {
  const key = fullName.toLowerCase();
  if (starred.has(key)) return 'held';
  return covered.has(key) ? 'known-gap' : 'new';
}
