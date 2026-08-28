# Repo Discovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Find GitHub repos that belong in an existing landscape report but are absent from the starred collection, rank them with evidence, and star the approved ones.

**Architecture:** One Node CLI, `scripts/discover.mjs`, composed of four small pure-ish modules under `scripts/lib/discover/`. It reads a report's markdown and meta as the landscape definition, crosses the repos it names against the star set to produce a three-state split, generates further candidates from GitHub search plus model recall, verifies everything through the GraphQL API, and scores survivors using the *existing* classifier so they sit on the same scale as the 1,794 repos already held.

**Tech Stack:** Node 24 (ESM, no new dependencies), `scripts/lib/github.mjs` for API access, GitHub GraphQL v4 + search, Python untouched.

**Spec:** `docs/superpowers/specs/2026-08-28-repo-discovery-design.md`

## Global Constraints

- **No new npm dependencies.** Everything uses Node 24 builtins plus the repo's existing `scripts/lib/github.mjs`.
- **Node ESM** (`.mjs`, `import`), matching `sample.mjs` / `ingest.mjs` / `classify.mjs`.
- **Test style follows `scripts/test-graph.mjs`**: a plain script with an `ok(label, cond, detail)` helper, `✓`/`✗` output, and `process.exit(fail > 0 ? 1 : 0)`. No test framework, no new runner.
- **All tests in one file**, `scripts/test-discover.mjs`, extended section by section. Run with `npm run test:discover`.
- **Network is never required by a unit test.** Tasks 1–5 and 8 must pass offline. Only Tasks 6, 7 and 9 make API calls.
- **Repo-name comparison is case-normalized** (`toLowerCase()`) with the original casing preserved for display. Verified 2026-08-28: normalization does not change the `agentic-terminals` split.
- **The user's guardrails say never commit unless explicitly asked.** The commit step in each task is written out ready to run, but ask before running it.
- Paths are relative to `/Users/marty/claude-projects/github-stars-analyzer`.

---

## File Structure

| File | Responsibility |
|---|---|
| `scripts/lib/github.mjs` | *(modify)* add `gh auth token` fallback to `getToken()` |
| `scripts/classify.mjs` | *(modify)* becomes a thin driver over `classify-core.mjs` |
| `scripts/lib/classify-core.mjs` | *(create)* pure lifecycle/health/momentum scoring, extracted verbatim |
| `scripts/lib/discover/landscape.mjs` | *(create)* report md + meta + star set → three-state split and vocabulary |
| `scripts/lib/discover/score.mjs` | *(create)* kind classification and the decomposed fit score |
| `scripts/lib/discover/candidates.mjs` | *(create)* search-query construction and `--extra` parsing |
| `scripts/lib/discover/fetch.mjs` | *(create)* search execution, resolve/enrich, rename detection |
| `scripts/lib/discover/render.mjs` | *(create)* markdown + JSON output |
| `scripts/discover.mjs` | *(create)* CLI wiring |
| `scripts/test-discover.mjs` | *(create)* the whole test suite |
| `~/.claude/skills/discovering-repos-to-star/SKILL.md` | *(create)* the judgement layer |
| `~/.claude/skills/discovering-repos-to-star/references/scoring.md` | *(create)* score internals, not loaded on a normal run |

---

### Task 1: `gh auth token` fallback

The `.env` token returns 401 as of 2026-08-28, and `getToken()` currently throws when `GITHUB_TOKEN` is unset. The `gh` CLI holds a working token with a full 5,000/hour GraphQL budget, so falling back to it makes a dead `.env` a non-event.

**Files:**
- Modify: `scripts/lib/github.mjs:6-10`
- Create: `scripts/test-discover.mjs`
- Modify: `package.json` (add `test:discover` script)

**Interfaces:**
- Consumes: nothing
- Produces: `getToken(): string` — unchanged signature, new fallback behaviour. Throws only when both the env var and `gh` are unavailable.

- [ ] **Step 1: Write the failing test**

Create `scripts/test-discover.mjs`:

```js
// Unit tests for the discovery pipeline. Run: npm run test:discover
// Style matches scripts/test-graph.mjs — no framework, exit code from failures.

let pass = 0;
let fail = 0;
function ok(label, cond, detail = '') {
  if (cond) { console.log(`  ✓ ${label}${detail ? ' — ' + detail : ''}`); pass += 1; }
  else { console.error(`  ✗ ${label}${detail ? ' — ' + detail : ''}`); fail += 1; }
}

console.log('== Task 1: token resolution ==');
{
  const { getToken } = await import('./lib/github.mjs');
  process.env.GITHUB_TOKEN = '  env-token  ';
  ok('env var wins and is trimmed', getToken() === 'env-token');

  delete process.env.GITHUB_TOKEN;
  let fellBack = null;
  try { fellBack = getToken(); } catch { fellBack = null; }
  ok('falls back to gh auth token when env is unset',
     typeof fellBack === 'string' && fellBack.length > 20,
     fellBack ? `${fellBack.length} chars` : 'gh unavailable — install gh or run gh auth login');
}

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail > 0 ? 1 : 0);
```

- [ ] **Step 2: Run it and watch the fallback fail**

```bash
npm run test:discover
```

First add the script to `package.json` under `"scripts"`, next to `"test:graph"`:

```json
    "test:discover": "node scripts/test-discover.mjs",
```

Expected: the first assertion passes; the second fails with `✗ falls back to gh auth token when env is unset`, because `getToken()` throws.

- [ ] **Step 3: Implement the fallback**

Replace `scripts/lib/github.mjs` lines 6–10 with:

```js
import { execFileSync } from 'node:child_process';

let _ghToken;

export function getToken() {
  const t = process.env.GITHUB_TOKEN;
  if (t && t.trim()) return t.trim();

  // Fall back to the gh CLI's own token. A dead or missing .env then costs
  // nothing on a machine where `gh auth login` has been run.
  if (_ghToken === undefined) {
    try {
      _ghToken = execFileSync('gh', ['auth', 'token'], {
        encoding: 'utf8',
        stdio: ['ignore', 'pipe', 'ignore'],
      }).trim() || null;
    } catch {
      _ghToken = null;
    }
  }
  if (_ghToken) return _ghToken;

  throw new Error(
    'No GitHub token. Set GITHUB_TOKEN (node --env-file=.env <script>) or run `gh auth login`.',
  );
}
```

The `import` goes at the top of the file with the other imports; the rest of `github.mjs` is untouched.

- [ ] **Step 4: Run the test again**

```bash
npm run test:discover
```

Expected: `2 passed, 0 failed`.

- [ ] **Step 5: Verify nothing else regressed**

```bash
GITHUB_TOKEN= node -e "import('./scripts/lib/github.mjs').then(m=>console.log('token len', m.getToken().length))"
```

Expected: a length over 20, no throw.

- [ ] **Step 6: Commit** *(ask first)*

```bash
git add scripts/lib/github.mjs scripts/test-discover.mjs package.json
git commit -m "feat: fall back to gh auth token when GITHUB_TOKEN is unset"
```

---

### Task 2: Extract `classify-core.mjs`

Candidates must be scored on the same scale as the dataset, which means running the *same* `lifecycleStage` / `healthScore` code rather than a second implementation. The functions currently live inside `classify.mjs`, a side-effectful script that reads `argv` and writes a file at import time, so they cannot be imported. Extract them verbatim, with `now` threaded as a defaulted parameter so tests can pin time.

**Files:**
- Create: `scripts/lib/classify-core.mjs`
- Modify: `scripts/classify.mjs` (drops to a thin driver)
- Modify: `scripts/test-discover.mjs` (append a section)

**Interfaces:**
- Consumes: nothing
- Produces:
  - `daysAgo(iso: string|null, now?: number): number`
  - `busFactor(authors: {login,commits}[]): { count: number, top_share: number }`
  - `lifecycleStage(r: object, now?: number): string`
  - `healthScore(r: object, bf: {count,top_share}, now?: number): number`
  - `momentum(r: object, now?: number): { estimated_stars_30d: number, lifetime_per_day: number }`
  - `classifyRepo(r: object, now?: number): object` — `r` plus `age_days`, `days_since_push`, `bus_factor`, `top_author_share`, `lifecycle_stage`, `health_score`, `momentum`

- [ ] **Step 1: Capture the baseline output before touching anything**

```bash
node scripts/classify.mjs --in=src/data/raw-100.json
cp src/data/classified-100.json /tmp/classify-baseline.json
```

Expected: `Wrote src/data/classified-100.json` on stderr.

- [ ] **Step 2: Write the failing test**

Append to `scripts/test-discover.mjs`, before the final summary lines:

```js
console.log('\n== Task 2: classify-core ==');
{
  const core = await import('./lib/classify-core.mjs');
  const NOW = Date.parse('2026-08-28T00:00:00Z');

  ok('daysAgo is pinned by now', Math.round(core.daysAgo('2026-08-18T00:00:00Z', NOW)) === 10);
  ok('daysAgo of null is Infinity', core.daysAgo(null, NOW) === Infinity);

  const bf = core.busFactor([{ login: 'a', commits: 8 }, { login: 'b', commits: 2 }]);
  ok('busFactor covers 50% with one author', bf.count === 1, `count=${bf.count}`);
  ok('busFactor top_share is 0.8', Math.abs(bf.top_share - 0.8) < 1e-9);

  const archived = { archived: true, created_at: '2020-01-01T00:00:00Z', pushed_at: '2026-08-27T00:00:00Z' };
  ok('archived is Abandoned', core.lifecycleStage(archived, NOW) === 'Abandoned');

  const hot = {
    archived: false,
    created_at: '2025-06-01T00:00:00Z',
    pushed_at: '2026-08-27T00:00:00Z',
    commits_90d: 120,
    unique_authors_90d: 7,
  };
  ok('young + busy + multi-author is Hot', core.lifecycleStage(hot, NOW) === 'Hot');

  const enriched = core.classifyRepo({ ...hot, stars: 900, authors_90d: [{ login: 'a', commits: 120 }] }, NOW);
  ok('classifyRepo adds the dataset fields',
     typeof enriched.health_score === 'number'
     && typeof enriched.lifecycle_stage === 'string'
     && typeof enriched.days_since_push === 'number'
     && typeof enriched.bus_factor === 'number');
  ok('health_score is 0-100', enriched.health_score >= 0 && enriched.health_score <= 100,
     `${enriched.health_score}`);
}
```

- [ ] **Step 3: Run it to verify it fails**

```bash
npm run test:discover
```

Expected: FAIL — `Cannot find module .../scripts/lib/classify-core.mjs`.

- [ ] **Step 4: Create `scripts/lib/classify-core.mjs`**

The bodies below are lifted from `scripts/classify.mjs` unchanged apart from `now` becoming a parameter.

```js
// Deterministic lifecycle + health scoring, extracted from classify.mjs so that
// discover.mjs can score never-starred candidates on exactly the same scale as
// the dataset. No I/O, no argv, no side effects — importable from anywhere.

const DAY = 24 * 60 * 60 * 1000;

export function daysAgo(iso, now = Date.now()) {
  if (!iso) return Infinity;
  return Math.max(0, (now - Date.parse(iso)) / DAY);
}

export function busFactor(authors) {
  // CHAOSS Contributor Absence Factor: smallest set covering 50% of contributions.
  const sorted = [...authors].sort((a, b) => b.commits - a.commits);
  const total = sorted.reduce((s, a) => s + a.commits, 0);
  if (total === 0) return { count: 0, top_share: 0 };
  let acc = 0;
  let count = 0;
  for (const a of sorted) {
    acc += a.commits;
    count += 1;
    if (acc / total >= 0.5) break;
  }
  return { count, top_share: sorted[0].commits / total };
}

export function lifecycleStage(r, now = Date.now()) {
  const ageDays = daysAgo(r.created_at, now);
  const sinceLastPush = daysAgo(r.pushed_at, now);
  const commits90 = r.commits_90d ?? 0;
  const authors90 = r.unique_authors_90d ?? 0;
  const lastRelease = r.releases_recent?.[0]?.published_at;
  const sinceLastRelease = lastRelease ? daysAgo(lastRelease, now) : Infinity;

  if (sinceLastPush > 365 && sinceLastRelease > 540) return 'Abandoned';
  if (r.archived) return 'Abandoned';
  if (ageDays < 365 * 2 && commits90 >= 30 && authors90 >= 3) return 'Hot';
  if (ageDays < 365 && commits90 >= 10) return 'Rising';
  if (ageDays > 365 * 3 && commits90 >= 10 && authors90 >= 2) return 'Classic';
  if (ageDays > 365 * 2 && sinceLastPush < 180) return 'Mature';
  if (sinceLastPush < 365 && commits90 < 5) return 'Declining';
  if (sinceLastPush > 180) return 'Declining';
  return 'Mature';
}

export function healthScore(r, bf, now = Date.now()) {
  // 0–100 combining activity, contributor diversity, release cadence, issue ratio.
  const sinceLastPush = daysAgo(r.pushed_at, now);

  const activity = Math.max(0, 30 - Math.min(30, sinceLastPush / 12));
  const diversity = Math.min(25, bf.count * 5);
  const commitsPerMonth = (r.commits_90d ?? 0) / 3;
  const volume = Math.min(20, Math.log10(1 + commitsPerMonth) * 12);
  const recentReleases = (r.releases_recent ?? [])
    .filter((rel) => daysAgo(rel.published_at, now) < 365).length;
  const releases = Math.min(15, recentReleases * 2);
  const total = (r.open_issues ?? 0) + (r.closed_issues ?? 0);
  const closureRatio = total === 0 ? 0.5 : (r.closed_issues ?? 0) / total;
  const closure = closureRatio * 10;

  return Math.round(activity + diversity + volume + releases + closure);
}

export function momentum(r, now = Date.now()) {
  const stars = r.stars ?? 0;
  const ageDays = Math.max(30, daysAgo(r.created_at, now));
  const sinceLastPush = daysAgo(r.pushed_at, now);
  // Rough estimator: lifetime stars/day weighted by activity. Real momentum needs
  // GraphQL stargazer history per repo (slow). Serviceable proxy.
  const lifetimeRate = stars / ageDays;
  const activityMult = sinceLastPush < 7 ? 2.5 : sinceLastPush < 30 ? 1.6 : sinceLastPush < 90 ? 1.0 : sinceLastPush < 365 ? 0.4 : 0.1;
  const ageMult = ageDays < 365 ? 1 : ageDays < 365 * 2 ? 0.85 : ageDays < 365 * 3 ? 0.7 : 0.5;
  const estimated30d = Math.round(lifetimeRate * 30 * activityMult * ageMult);
  return { estimated_stars_30d: estimated30d, lifetime_per_day: lifetimeRate };
}

export function classifyRepo(r, now = Date.now()) {
  const bf = busFactor(r.authors_90d ?? []);
  return {
    ...r,
    age_days: Math.round(daysAgo(r.created_at, now)),
    days_since_push: Math.round(daysAgo(r.pushed_at, now)),
    bus_factor: bf.count,
    top_author_share: Math.round(bf.top_share * 100) / 100,
    lifecycle_stage: lifecycleStage(r, now),
    health_score: healthScore(r, bf, now),
    momentum: momentum(r, now),
  };
}
```

- [ ] **Step 5: Run the test to verify it passes**

```bash
npm run test:discover
```

Expected: `9 passed, 0 failed`.

- [ ] **Step 6: Rewrite `scripts/classify.mjs` as a thin driver**

Replace the entire file with:

```js
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
```

Note one deliberate behaviour change: the original called `Date.now()` once at module load and used it for every repo, and so does this. Passing `now` explicitly preserves that.

- [ ] **Step 7: Prove the output is unchanged**

```bash
node scripts/classify.mjs --in=src/data/raw-100.json
node -e "
const a=require('/tmp/classify-baseline.json'), b=require('./src/data/classified-100.json');
delete a.generatedAt; delete b.generatedAt;
const same = JSON.stringify(a) === JSON.stringify(b);
console.log(same ? 'IDENTICAL' : 'DIFFERS');
process.exit(same ? 0 : 1);
"
```

Expected: `IDENTICAL`, exit 0. If it differs, the extraction changed behaviour — diff the two files rather than proceeding.

- [ ] **Step 8: Commit** *(ask first)*

```bash
git add scripts/lib/classify-core.mjs scripts/classify.mjs scripts/test-discover.mjs
git commit -m "refactor: extract lifecycle/health scoring into lib/classify-core.mjs"
```

---

### Task 3: Landscape loading and the three-state split

A report's markdown links every repo it *names*, including ones it names as missing. `agentic-terminals` links 59 repos: 14 starred, 45 not. Those 45 are the report's own gap analysis — the highest-value candidates, already judged in-scope by a human. Treating "covered" as a drop filter would discard exactly them.

**Files:**
- Create: `scripts/lib/discover/landscape.mjs`
- Modify: `scripts/test-discover.mjs` (append a section)

**Interfaces:**
- Consumes: nothing
- Produces:
  - `coveredRepos(markdown: string): Map<string, string>` — lowercase name → display name
  - `vocabulary(meta: object): string[]` — lowercase search terms from category names and title
  - `loadLandscape(slug: string, opts?: {root?: string}): { slug, meta, starred: Set<string>, covered: Map<string,string>, vocabulary: string[], held: string[], knownGaps: string[] }` — `held` and `knownGaps` hold display names, sorted

- [ ] **Step 1: Write the failing test**

Append to `scripts/test-discover.mjs`, before the summary:

```js
console.log('\n== Task 3: landscape ==');
{
  const { coveredRepos, vocabulary, loadLandscape } = await import('./lib/discover/landscape.mjs');

  const md = 'see [tmux](https://github.com/tmux/tmux) and https://github.com/TMUX/tmux'
    + ' and https://github.com/sponsors/someone and https://github.com/foo/bar.git';
  const cov = coveredRepos(md);
  ok('dedupes case variants', cov.size === 2, `${[...cov.values()].join(', ')}`);
  ok('drops non-repo owner paths', ![...cov.keys()].some((k) => k.startsWith('sponsors/')));
  ok('strips a .git suffix', cov.has('foo/bar'));

  const vocab = vocabulary({ title: 'Terminals for Agentic Programming', categories: { 'Terminal emulator': 2, 'Agent runtime / multiplexer': 3 } });
  ok('vocabulary lowercases and splits categories', vocab.includes('terminal') && vocab.includes('multiplexer'));
  ok('vocabulary drops stopwords', !vocab.includes('for') && !vocab.includes('and'));

  const ls = loadLandscape('agentic-terminals');
  ok('agentic-terminals links 59 repos', ls.covered.size === 59, `${ls.covered.size}`);
  ok('14 are held', ls.held.length === 14, `${ls.held.length}`);
  ok('45 are known gaps', ls.knownGaps.length === 45, `${ls.knownGaps.length}`);
  ok('a known gap is a real one', ls.knownGaps.includes('alacritty/alacritty'));
  ok('a held repo is not a gap', !ls.knownGaps.includes('tmux/tmux'));

  const cs = loadLandscape('charting-stack');
  ok('charting-stack links 61 repos', cs.covered.size === 61, `${cs.covered.size}`);
}
```

- [ ] **Step 2: Run it to verify it fails**

```bash
npm run test:discover
```

Expected: FAIL — `Cannot find module .../scripts/lib/discover/landscape.mjs`.

- [ ] **Step 3: Create `scripts/lib/discover/landscape.mjs`**

```js
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
```

- [ ] **Step 4: Run the test to verify it passes**

```bash
npm run test:discover
```

Expected: `20 passed, 0 failed`. If the 59/14/45 assertions fail, the dataset has been refreshed since 2026-08-28 and some of the 45 are now starred — update the expected numbers from the actual split rather than changing the extraction.

- [ ] **Step 5: Commit** *(ask first)*

```bash
git add scripts/lib/discover/landscape.mjs scripts/test-discover.mjs
git commit -m "feat: landscape loader with held/known-gap/new three-state split"
```

---

### Task 4: Kind classification and the fit score

Ranking must be explainable, so the score is decomposed and every component is printed. Awesome-lists are demoted rather than dropped — `rothgar/awesome-tuis` is legitimately part of the agentic-terminals set.

**Files:**
- Create: `scripts/lib/discover/score.mjs`
- Modify: `scripts/test-discover.mjs` (append a section)

**Interfaces:**
- Consumes: `classifyRepo` output shape from Task 2 (`health_score`, `days_since_push`)
- Produces:
  - `classifyKind(repo: object): 'tool'|'list'|'tutorial'|'spec/doc'`
  - `relevance(repo: object, vocabulary: string[]): number` — 0..1
  - `standing(stars: number): number` — 0..1
  - `recency(daysSincePush: number): number` — 0..1
  - `fitScore(repo: object, vocabulary: string[], opts: {state: string}): { parts: {relevance,standing,health,recency}, kind_multiplier: number, total: number }` — `total` is 0..100

- [ ] **Step 1: Write the failing test**

Append to `scripts/test-discover.mjs`, before the summary:

```js
console.log('\n== Task 4: scoring ==');
{
  const { classifyKind, standing, recency, fitScore } = await import('./lib/discover/score.mjs');

  ok('awesome list with low churn is a list',
     classifyKind({ full_name: 'rothgar/awesome-tuis', description: 'List of projects that provide terminal user interfaces', commits_90d: 2 }) === 'list');
  ok('an active tool is a tool',
     classifyKind({ full_name: 'tmux/tmux', description: 'tmux source code', commits_90d: 90 }) === 'tool');
  ok('a course is a tutorial',
     classifyKind({ full_name: 'x/llm-course', description: 'Course to get into Large Language Models', commits_90d: 5 }) === 'tutorial');
  ok('a busy repo named awesome-* is still a tool',
     classifyKind({ full_name: 'x/awesome-engine', description: 'awesome rendering engine', commits_90d: 400 }) === 'tool');

  ok('standing is monotonic in stars', standing(50000) > standing(3000) && standing(3000) > standing(100));
  ok('standing is capped at 1', standing(5_000_000) <= 1);
  ok('recency is 1 for a fresh push', recency(5) === 1);
  ok('recency is 0 past a year', recency(400) === 0);
  ok('recency decays in between', recency(200) > 0 && recency(200) < 1);

  const base = { full_name: 'a/b', description: 'terminal multiplexer', topics: ['terminal'], stars: 5000, health_score: 70, days_since_push: 10, commits_90d: 50 };
  const vocab = ['terminal', 'multiplexer', 'agent'];
  const asNew = fitScore({ ...base, kind: 'tool' }, vocab, { state: 'new' });
  const asGap = fitScore({ ...base, kind: 'tool' }, vocab, { state: 'known-gap' });
  ok('known-gap outranks an identical new repo', asGap.total > asNew.total, `${asGap.total} > ${asNew.total}`);
  ok('score exposes its components',
     ['relevance', 'standing', 'health', 'recency'].every((k) => typeof asNew.parts[k] === 'number'));
  ok('total stays within 0-100', asGap.total <= 100 && asNew.total >= 0);

  const asList = fitScore({ ...base, kind: 'list' }, vocab, { state: 'new' });
  ok('a list ranks below an identical tool', asList.total < asNew.total, `${asList.total} < ${asNew.total}`);

  const offTopic = fitScore({ ...base, kind: 'tool', description: 'json parser', topics: [] }, vocab, { state: 'new' });
  ok('off-theme scores lower than on-theme', offTopic.total < asNew.total);
}
```

- [ ] **Step 2: Run it to verify it fails**

```bash
npm run test:discover
```

Expected: FAIL — `Cannot find module .../scripts/lib/discover/score.mjs`.

- [ ] **Step 3: Create `scripts/lib/discover/score.mjs`**

```js
// Kind classification and the fit score. Health comes from the dataset's own
// classifier (lib/classify-core.mjs); everything here is about *relevance to
// this report*, which health cannot express.

const LIST_RE = /\b(awesome|curated|collection of|list of|resources)\b/i;
const TUTORIAL_RE = /\b(tutorial|course|examples?|learning|book|roadmap|interview|cheat ?sheet|handbook|workshop)\b/i;
const DOC_RE = /\b(specification|rfc|documentation|whitepaper|proposal)\b/i;

// Curation-shaped repos with real commit churn are usually tools that merely
// sound like lists, so activity is part of the test rather than the name alone.
const CURATION_CHURN_CEILING = 30;

export function classifyKind(repo) {
  const hay = `${repo.full_name ?? ''} ${repo.description ?? ''}`;
  const commits = repo.commits_90d ?? 0;
  if (LIST_RE.test(hay) && commits < CURATION_CHURN_CEILING) return 'list';
  if (TUTORIAL_RE.test(hay)) return 'tutorial';
  if (DOC_RE.test(hay) && commits < CURATION_CHURN_CEILING) return 'spec/doc';
  return 'tool';
}

const KIND_MULTIPLIER = { tool: 1.0, 'spec/doc': 0.75, list: 0.6, tutorial: 0.45 };

/** Share of the report's vocabulary the repo's own text hits, saturating at 4 terms. */
export function relevance(repo, vocabulary) {
  if (!vocabulary?.length) return 0;
  const hay = `${repo.description ?? ''} ${(repo.topics ?? []).join(' ')} ${repo.full_name ?? ''}`.toLowerCase();
  let hits = 0;
  for (const term of vocabulary) if (hay.includes(term)) hits += 1;
  return Math.min(1, hits / Math.min(4, vocabulary.length));
}

/** Log-scaled so a 200k-star list cannot outrank a 3k-star tool on size alone. */
export function standing(stars) {
  return Math.min(1, Math.log10(1 + Math.max(0, stars ?? 0)) / 5);
}

export function recency(daysSincePush) {
  if (!Number.isFinite(daysSincePush)) return 0;
  if (daysSincePush <= 30) return 1;
  if (daysSincePush >= 365) return 0;
  return 1 - (daysSincePush - 30) / 335;
}

const WEIGHTS = { relevance: 0.35, standing: 0.20, health: 0.25, recency: 0.20 };

// The report author already judged a known-gap repo in-scope and wrote it down;
// the only open question is whether to star it. That is worth a head start.
const KNOWN_GAP_BONUS = 0.15;

export function fitScore(repo, vocabulary, { state = 'new' } = {}) {
  const parts = {
    relevance: relevance(repo, vocabulary),
    standing: standing(repo.stars),
    health: Math.min(1, Math.max(0, (repo.health_score ?? 0) / 100)),
    recency: recency(repo.days_since_push),
  };
  const base = Object.entries(WEIGHTS).reduce((s, [k, w]) => s + w * parts[k], 0);
  const kindMultiplier = KIND_MULTIPLIER[repo.kind] ?? 1;
  const bonus = state === 'known-gap' ? KNOWN_GAP_BONUS : 0;
  return {
    parts,
    kind_multiplier: kindMultiplier,
    total: Math.round(Math.min(1, base * kindMultiplier + bonus) * 100),
  };
}
```

- [ ] **Step 4: Run the test to verify it passes**

```bash
npm run test:discover
```

Expected: `34 passed, 0 failed`.

- [ ] **Step 5: Commit** *(ask first)*

```bash
git add scripts/lib/discover/score.mjs scripts/test-discover.mjs
git commit -m "feat: kind classification and decomposed fit score"
```

---

### Task 5: Candidate generation

Two sources: GitHub search queries built from the report's own vocabulary, and names supplied by the model via `--extra`. This task builds and parses them; Task 6 executes them.

**Files:**
- Create: `scripts/lib/discover/candidates.mjs`
- Modify: `scripts/test-discover.mjs` (append a section)

**Interfaces:**
- Consumes: `vocabulary` from Task 3
- Produces:
  - `parseExtra(arg: string|undefined): string[]` — normalized `owner/repo` names, deduped
  - `buildQueries(landscape: object, opts: {minStars: number, maxStaleDays: number, now?: number}): {label: string, q: string}[]`

- [ ] **Step 1: Write the failing test**

Append to `scripts/test-discover.mjs`, before the summary:

```js
console.log('\n== Task 5: candidate generation ==');
{
  const { parseExtra, buildQueries } = await import('./lib/discover/candidates.mjs');

  ok('parses a comma list', JSON.stringify(parseExtra('a/b, c/d')) === JSON.stringify(['a/b', 'c/d']));
  ok('strips a github url', parseExtra('https://github.com/a/b')[0] === 'a/b');
  ok('strips a trailing .git and slash', parseExtra('a/b.git, c/d/')[0] === 'a/b' && parseExtra('a/b.git, c/d/')[1] === 'c/d');
  ok('dedupes case-insensitively', parseExtra('A/B, a/b').length === 1);
  ok('drops malformed entries', parseExtra('a/b, nope, /x, y/').length === 1);
  ok('empty input is an empty list', parseExtra(undefined).length === 0);

  const ls = {
    meta: { title: 'Terminals for Agentic Programming', categories: { 'Terminal emulator': 2, 'Agent runtime / multiplexer': 3 } },
    vocabulary: ['terminal', 'emulator', 'agent', 'runtime', 'multiplexer'],
  };
  const qs = buildQueries(ls, { minStars: 200, maxStaleDays: 365, now: Date.parse('2026-08-28T00:00:00Z') });
  ok('builds at least one query per category', qs.length >= 2, `${qs.length} queries`);
  ok('every query filters forks and archives', qs.every((q) => q.q.includes('fork:false') && q.q.includes('archived:false')));
  ok('every query carries the star floor', qs.every((q) => q.q.includes('stars:>=200')));
  ok('every query carries a pushed floor', qs.every((q) => /pushed:>=\d{4}-\d{2}-\d{2}/.test(q.q)));
  ok('pushed floor is maxStaleDays back', qs[0].q.includes('pushed:>=2025-08-28'));
  ok('queries are labelled', qs.every((q) => typeof q.label === 'string' && q.label.length > 0));
}
```

- [ ] **Step 2: Run it to verify it fails**

```bash
npm run test:discover
```

Expected: FAIL — `Cannot find module .../scripts/lib/discover/candidates.mjs`.

- [ ] **Step 3: Create `scripts/lib/discover/candidates.mjs`**

```js
// Where candidates come from: GitHub search built out of the report's own
// vocabulary, plus names the model supplies via --extra. Both are unverified
// at this stage — fetch.mjs decides what is real.

const NAME_RE = /^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/;

/** Normalize "--extra a/b, https://github.com/c/d.git" into ['a/b','c/d']. */
export function parseExtra(arg) {
  if (!arg) return [];
  const seen = new Map();
  for (const raw of String(arg).split(',')) {
    let s = raw.trim();
    if (!s) continue;
    s = s.replace(/^https?:\/\/(www\.)?github\.com\//i, '');
    s = s.replace(/\.git$/i, '').replace(/\/+$/, '');
    if (!NAME_RE.test(s)) continue;
    const key = s.toLowerCase();
    if (!seen.has(key)) seen.set(key, s);
  }
  return [...seen.values()];
}

function isoDaysBack(days, now) {
  return new Date(now - days * 24 * 60 * 60 * 1000).toISOString().slice(0, 10);
}

/**
 * One query per report category, plus a broad one from the top vocabulary
 * terms. Category names are what a human already decided the landscape is
 * made of, so they beat anything inferred from the prose.
 */
export function buildQueries(landscape, { minStars = 200, maxStaleDays = 365, now = Date.now() } = {}) {
  const filters = `fork:false archived:false stars:>=${minStars} pushed:>=${isoDaysBack(maxStaleDays, now)}`;
  const queries = [];

  for (const category of Object.keys(landscape.meta?.categories ?? {})) {
    const words = category.toLowerCase().split(/[^a-z0-9+#.]+/).filter((w) => w.length >= 3);
    if (!words.length) continue;
    queries.push({ label: `category: ${category}`, q: `${words.join(' ')} ${filters}` });
  }

  const top = (landscape.vocabulary ?? []).slice(0, 4);
  if (top.length) {
    queries.push({ label: 'vocabulary', q: `${top.join(' OR ')} ${filters}` });
  }

  return queries;
}
```

- [ ] **Step 4: Run the test to verify it passes**

```bash
npm run test:discover
```

Expected: `46 passed, 0 failed`.

- [ ] **Step 5: Commit** *(ask first)*

```bash
git add scripts/lib/discover/candidates.mjs scripts/test-discover.mjs
git commit -m "feat: candidate query construction and --extra parsing"
```

---

### Task 6: Fetch, resolve and enrich

The first task that touches the network. Two responsibilities: run search queries, and resolve each candidate name to its canonical repo with the fields `classify-core` needs.

Renames are the correctness risk. The GraphQL API silently follows them — a query for `pvolok/mprocs` returns `nameWithOwner: "pvolok/dekit"`. The set-diff must run on the **returned** name, or a repo you already star reappears every week under its old one. The `agentic-terminals` gap analysis hit this three times.

**Files:**
- Create: `scripts/lib/discover/fetch.mjs`
- Modify: `scripts/test-discover.mjs` (append a network-gated section)

**Interfaces:**
- Consumes: `graphqlWithRetry`, `sleep` from `scripts/lib/github.mjs`; `classifyRepo` from Task 2
- Produces:
  - `REPO_FIELDS_QUERY: string` — the GraphQL document
  - `projectCandidate(repo: object): object` — GraphQL node → the field shape `classifyRepo` expects
  - `resolveRepos(names: string[], opts?): Promise<{ resolved: object[], renamed: {from,to}[], unresolved: string[] }>`
  - `searchRepos(queries: {label,q}[], opts?): Promise<{ full_name: string, via: string }[]>`

- [ ] **Step 1: Write the failing test**

Append to `scripts/test-discover.mjs`, before the summary. It is network-gated so the offline suite still passes:

```js
console.log('\n== Task 6: fetch (network) ==');
{
  const { projectCandidate, resolveRepos, searchRepos } = await import('./lib/discover/fetch.mjs');

  const node = {
    nameWithOwner: 'a/b', description: 'd', createdAt: '2024-01-01T00:00:00Z',
    pushedAt: '2026-08-01T00:00:00Z', stargazerCount: 12, forkCount: 3,
    isArchived: false, isFork: false, isMirror: false,
    primaryLanguage: { name: 'Rust' }, licenseInfo: { spdxId: 'MIT' },
    repositoryTopics: { nodes: [{ topic: { name: 'cli' } }] },
    defaultBranchRef: { target: { historySince: { totalCount: 7, nodes: [{ author: { user: { login: 'u' } } }] } } },
    releases: { totalCount: 1, nodes: [{ tagName: 'v1', publishedAt: '2026-07-01T00:00:00Z' }] },
    issues: { totalCount: 2 }, closedIssues: { totalCount: 8 },
  };
  const p = projectCandidate(node);
  ok('projectCandidate maps to dataset field names',
     p.full_name === 'a/b' && p.stars === 12 && p.commits_90d === 7
     && p.license === 'MIT' && p.topics[0] === 'cli' && p.unique_authors_90d === 1);

  let token = true;
  try { (await import('./lib/github.mjs')).getToken(); } catch { token = false; }
  if (!token) {
    console.log('  … skipped: no GitHub token available');
  } else {
    const r = await resolveRepos(['tmux/tmux', 'pvolok/mprocs', 'this-owner-does-not-exist-xyz/nope']);
    ok('resolves a live repo', r.resolved.some((x) => x.full_name === 'tmux/tmux'));
    ok('reports an unresolvable name', r.unresolved.includes('this-owner-does-not-exist-xyz/nope'));
    ok('detects a rename', r.renamed.some((x) => x.from === 'pvolok/mprocs' && x.to !== 'pvolok/mprocs'),
       JSON.stringify(r.renamed));
    ok('resolved rows carry health fields',
       r.resolved.every((x) => typeof x.health_score === 'number' && typeof x.lifecycle_stage === 'string'));

    const found = await searchRepos([{ label: 'test', q: 'terminal multiplexer fork:false archived:false stars:>=5000' }], { perQuery: 5 });
    ok('search returns candidates', found.length > 0, `${found.length}`);
    ok('search rows carry their origin', found.every((x) => typeof x.via === 'string'));
  }
}
```

- [ ] **Step 2: Run it to verify it fails**

```bash
npm run test:discover
```

Expected: FAIL — `Cannot find module .../scripts/lib/discover/fetch.mjs`.

- [ ] **Step 3: Create `scripts/lib/discover/fetch.mjs`**

```js
// The only module that talks to GitHub. Search finds names; resolve turns a
// name into a canonical, enriched, classified repo — or says why it could not.

import { graphqlWithRetry, sleep } from '../github.mjs';
import { classifyRepo } from '../classify-core.mjs';

// Pace floor matching ingest.mjs. The 2026-08-12 incident was caused by request
// *rate*, not budget, so discovery holds the same line.
const PACE_MS = 250;

export const REPO_FIELDS_QUERY = `
query Cand($owner: String!, $name: String!, $since: GitTimestamp!) {
  repository(owner: $owner, name: $name) {
    nameWithOwner
    description
    url
    homepageUrl
    isArchived
    isFork
    isMirror
    createdAt
    pushedAt
    stargazerCount
    forkCount
    primaryLanguage { name }
    licenseInfo { spdxId name }
    repositoryTopics(first: 20) { nodes { topic { name } } }
    defaultBranchRef {
      target {
        ... on Commit {
          historySince: history(first: 100, since: $since) {
            totalCount
            nodes { author { user { login } email name } }
          }
        }
      }
    }
    releases(first: 5, orderBy: {field: CREATED_AT, direction: DESC}) {
      totalCount
      nodes { tagName publishedAt }
    }
    issues(states: OPEN) { totalCount }
    closedIssues: issues(states: CLOSED) { totalCount }
  }
  rateLimit { remaining limit resetAt cost }
}`;

const SEARCH_QUERY = `
query Search($q: String!, $first: Int!) {
  search(query: $q, type: REPOSITORY, first: $first) {
    nodes { ... on Repository { nameWithOwner } }
  }
  rateLimit { remaining limit resetAt cost }
}`;

/** GraphQL node → the field names classify-core and the dataset already use. */
export function projectCandidate(repo) {
  const commits = repo.defaultBranchRef?.target?.historySince?.nodes ?? [];
  const tallies = new Map();
  for (const c of commits) {
    const login = c.author?.user?.login ?? c.author?.email ?? c.author?.name ?? 'unknown';
    tallies.set(login, (tallies.get(login) ?? 0) + 1);
  }
  const authors90d = [...tallies.entries()]
    .map(([login, n]) => ({ login, commits: n }))
    .sort((a, b) => b.commits - a.commits);

  return {
    full_name: repo.nameWithOwner,
    description: repo.description ?? '',
    url: repo.url,
    homepage: repo.homepageUrl ?? '',
    archived: repo.isArchived,
    fork: repo.isFork,
    mirror: repo.isMirror,
    created_at: repo.createdAt,
    pushed_at: repo.pushedAt,
    stars: repo.stargazerCount,
    forks: repo.forkCount,
    primary_language: repo.primaryLanguage?.name ?? null,
    license: repo.licenseInfo?.spdxId ?? null,
    license_name: repo.licenseInfo?.name ?? null,
    topics: (repo.repositoryTopics?.nodes ?? []).map((n) => n.topic.name),
    commits_90d: repo.defaultBranchRef?.target?.historySince?.totalCount ?? 0,
    authors_90d: authors90d,
    unique_authors_90d: authors90d.length,
    releases_total: repo.releases?.totalCount ?? 0,
    releases_recent: (repo.releases?.nodes ?? []).map((r) => ({ tag: r.tagName, published_at: r.publishedAt })),
    open_issues: repo.issues?.totalCount ?? 0,
    closed_issues: repo.closedIssues?.totalCount ?? 0,
  };
}

/**
 * Resolve names to canonical repos. The API follows renames silently, so the
 * returned nameWithOwner — not the queried name — is what callers must diff on.
 */
export async function resolveRepos(names, { now = Date.now(), pace = PACE_MS } = {}) {
  const since = new Date(now - 90 * 24 * 60 * 60 * 1000).toISOString();
  const resolved = [];
  const renamed = [];
  const unresolved = [];

  for (const name of names) {
    const [owner, repoName] = name.split('/');
    try {
      const data = await graphqlWithRetry(REPO_FIELDS_QUERY, { owner, name: repoName, since });
      const node = data?.repository;
      if (!node) { unresolved.push(name); continue; }
      if (node.nameWithOwner.toLowerCase() !== name.toLowerCase()) {
        renamed.push({ from: name, to: node.nameWithOwner });
      }
      resolved.push(classifyRepo(projectCandidate(node), now));
    } catch (err) {
      unresolved.push(name);
      console.error(`  ! ${name}: ${err.message}`);
    }
    await sleep(pace);
  }

  return { resolved, renamed, unresolved };
}

/** Run each query, returning names with the query that produced them. */
export async function searchRepos(queries, { perQuery = 25, pace = PACE_MS } = {}) {
  const seen = new Map();
  for (const { label, q } of queries) {
    try {
      const data = await graphqlWithRetry(SEARCH_QUERY, { q, first: perQuery });
      for (const n of data?.search?.nodes ?? []) {
        if (!n?.nameWithOwner) continue;
        const key = n.nameWithOwner.toLowerCase();
        if (!seen.has(key)) seen.set(key, { full_name: n.nameWithOwner, via: label });
      }
    } catch (err) {
      console.error(`  ! search "${label}": ${err.message}`);
    }
    await sleep(pace);
  }
  return [...seen.values()];
}
```

- [ ] **Step 4: Run the test to verify it passes**

```bash
export GITHUB_TOKEN=$(gh auth token)
npm run test:discover
```

Expected: `53 passed, 0 failed`. The rename assertion depends on `pvolok/mprocs` still redirecting — if that repo is deleted outright it lands in `unresolved` instead, in which case substitute another known rename and note it in the test.

- [ ] **Step 5: Commit** *(ask first)*

```bash
git add scripts/lib/discover/fetch.mjs scripts/test-discover.mjs
git commit -m "feat: candidate resolution with rename detection and search"
```

---

### Task 7: Rendering and the CLI

**Files:**
- Create: `scripts/lib/discover/render.mjs`
- Create: `scripts/discover.mjs`
- Modify: `package.json` (add `discover` script)
- Modify: `scripts/test-discover.mjs` (append a section)

**Interfaces:**
- Consumes: everything above
- Produces:
  - `renderMarkdown(result: object): string`
  - `renderJson(result: object): object`
  - CLI: `node scripts/discover.mjs --report <slug> [--extra …] [--min-stars 200] [--max-stale-days 365] [--limit 40] [--no-search]`

- [ ] **Step 1: Write the failing test**

Append to `scripts/test-discover.mjs`, before the summary:

```js
console.log('\n== Task 7: render ==');
{
  const { renderMarkdown } = await import('./lib/discover/render.mjs');
  const md = renderMarkdown({
    slug: 'demo',
    generated: '2026-08-28',
    heldCount: 14,
    candidates: [
      { full_name: 'a/b', state: 'known-gap', kind: 'tool', stars: 1200, license: 'MIT',
        primary_language: 'Rust', lifecycle_stage: 'Hot', health_score: 71, days_since_push: 3,
        bus_factor: 3, description: 'a thing', score: { total: 88, parts: { relevance: 1, standing: 0.6, health: 0.71, recency: 1 }, kind_multiplier: 1 } },
    ],
    renamed: [{ from: 'x/old', to: 'x/new' }],
    unresolved: ['q/nope'],
  });
  ok('markdown names the report', md.includes('demo'));
  ok('markdown shows the candidate', md.includes('a/b'));
  ok('markdown shows the state', md.includes('known-gap'));
  ok('markdown surfaces renames', md.includes('x/old') && md.includes('x/new'));
  ok('markdown surfaces unresolved names', md.includes('q/nope'));
  ok('markdown escapes table pipes', !md.split('\n').some((l) => l.startsWith('|') && l.split('|').length > 14));
}
```

- [ ] **Step 2: Run it to verify it fails**

```bash
npm run test:discover
```

Expected: FAIL — `Cannot find module .../scripts/lib/discover/render.mjs`.

- [ ] **Step 3: Create `scripts/lib/discover/render.mjs`**

```js
// Output. The score is always shown decomposed — a total alone gives the
// reader nothing to overrule.

function cell(s) {
  return String(s ?? '').replace(/\|/g, '\\|').replace(/\n/g, ' ');
}

function pct(n) {
  return `${Math.round((n ?? 0) * 100)}`;
}

export function renderMarkdown(result) {
  const { slug, generated, heldCount, candidates, renamed, unresolved } = result;
  const gaps = candidates.filter((c) => c.state === 'known-gap');
  const fresh = candidates.filter((c) => c.state === 'new');

  const lines = [];
  lines.push(`# Candidates for \`${slug}\``);
  lines.push('');
  lines.push(`Generated ${generated}. ${heldCount} repos in this landscape are already starred; `
    + `${gaps.length} are named by the report but unstarred (\`known-gap\`), and ${fresh.length} are new finds.`);
  lines.push('');
  lines.push('`known-gap` means the report already judged it in-scope — the only open question is whether to star it.');
  lines.push('');
  lines.push('| # | Repo | State | Kind | ★ | Lang | Licence | Stage | Health | Pushed | Bus | Fit | rel/std/hlt/rec | What it is |');
  lines.push('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|');

  candidates.forEach((c, i) => {
    const p = c.score.parts;
    lines.push('| ' + [
      i + 1,
      `[${cell(c.full_name)}](https://github.com/${c.full_name})`,
      c.state,
      c.kind,
      (c.stars ?? 0).toLocaleString('en-US'),
      cell(c.primary_language ?? '—'),
      cell(c.license ?? 'none'),
      c.lifecycle_stage,
      c.health_score,
      `${c.days_since_push}d`,
      c.bus_factor,
      `**${c.score.total}**`,
      `${pct(p.relevance)}/${pct(p.standing)}/${pct(p.health)}/${pct(p.recency)}`,
      cell((c.description ?? '').slice(0, 110)),
    ].join(' | ') + ' |');
  });

  if (renamed.length) {
    lines.push('', '## Renames followed', '');
    lines.push('The API resolved these to a different name. The set-diff used the resolved one.', '');
    for (const r of renamed) lines.push(`- \`${r.from}\` → \`${r.to}\``);
  }

  if (unresolved.length) {
    lines.push('', '## Unresolved', '');
    lines.push('Names that did not resolve to a repo. A name supplied via `--extra` landing here '
      + 'means it was misremembered, not that the repo is obscure.', '');
    for (const u of unresolved) lines.push(`- \`${u}\``);
  }

  lines.push('');
  return lines.join('\n');
}

export function renderJson(result) {
  return {
    slug: result.slug,
    generated: result.generated,
    held_count: result.heldCount,
    counts: {
      known_gap: result.candidates.filter((c) => c.state === 'known-gap').length,
      new: result.candidates.filter((c) => c.state === 'new').length,
      renamed: result.renamed.length,
      unresolved: result.unresolved.length,
    },
    candidates: result.candidates,
    renamed: result.renamed,
    unresolved: result.unresolved,
  };
}
```

- [ ] **Step 4: Run the render test to verify it passes**

```bash
npm run test:discover
```

Expected: `59 passed, 0 failed`.

- [ ] **Step 5: Create `scripts/discover.mjs`**

```js
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
import { parseExtra, buildQueries } from './lib/discover/candidates.mjs';
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

const candidates = resolved
  // Re-check against the star set on the RESOLVED name — a rename can land on
  // something already held.
  .filter((r) => stateFor(r.full_name, landscape) !== 'held')
  .filter((r) => !r.fork && !r.archived)
  .filter((r) => (r.stars ?? 0) >= minStars)
  .filter((r) => r.days_since_push <= maxStaleDays)
  .map((r) => {
    const kind = classifyKind(r);
    const state = stateFor(r.full_name, landscape);
    return { ...r, kind, state, score: fitScore({ ...r, kind }, landscape.vocabulary, { state }) };
  })
  .sort((a, b) => b.score.total - a.score.total)
  .slice(0, limit);

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
```

Add to `package.json` scripts:

```json
    "discover": "node scripts/discover.mjs",
```

- [ ] **Step 6: Run it end to end, search disabled first**

```bash
export GITHUB_TOKEN=$(gh auth token)
node scripts/discover.mjs --report agentic-terminals --no-search --limit 60
```

Expected: `45 known gaps` on the landscape line, a ranked table, and non-zero renames (the mprocs/crystal cases). Repos that fail the star floor or staleness filter drop out, so the table is shorter than 45 — that is correct behaviour, not a bug.

- [ ] **Step 7: Run it with search on**

```bash
node scripts/discover.mjs --report agentic-terminals --limit 40
```

Expected: additional `new`-state rows above and below the known gaps, sorted by fit.

- [ ] **Step 8: Commit** *(ask first)*

```bash
git add scripts/lib/discover/render.mjs scripts/discover.mjs scripts/test-discover.mjs package.json
git commit -m "feat: discover CLI with candidate table output"
```

---

### Task 8: The `discovering-repos-to-star` skill

The script cannot decide whether a candidate belongs in *this* report rather than a neighbouring one, whether a low health score means finished or dead, or whether a list is worth starring. That is the skill's job.

**Files:**
- Create: `~/.claude/skills/discovering-repos-to-star/SKILL.md`
- Create: `~/.claude/skills/discovering-repos-to-star/references/scoring.md`

**Interfaces:**
- Consumes: the CLI from Task 7
- Produces: no code

- [ ] **Step 1: Write `SKILL.md`**

```markdown
---
name: discovering-repos-to-star
description: Use when looking for GitHub repos that belong in a github-stars-analyzer landscape report but are missing from the starred collection — "what's missing from the RAG report", "find new repos worth starring", "anything new in agent memory since August", "should I be starring anything for X". Produces a ranked candidate table and stars the approved ones.
---

# Discovering repos to star

Find repos that belong in a landscape report but are absent from the stars,
rank them with evidence, and star the ones that survive review.

**Core principle: the report defines the landscape, the script does the
mechanics, you make the call.** Scoring can rank a candidate; it cannot decide
whether it belongs in *this* report.

## Precondition

```bash
ls reports/<slug>.md
```

**No report → no discovery.** The whole premise is a landscape to find gaps in.
Build the report first with the `star-reports` skill.

## Run it

```bash
export GITHUB_TOKEN=$(gh auth token)   # .env may be stale
node scripts/discover.mjs --report <slug>
```

Useful flags: `--extra a/b,c/d` (see below), `--no-search` (known gaps only, no
API search), `--min-stars 500`, `--max-stale-days 180`, `--limit 40`.

**Always pass `--extra`.** Before running, name the tools you know belong in
this landscape and are not in the table — search ranks well-branded projects
badly, and this is the one input only a model can supply. Wrong guesses are
harmless: they land in the **Unresolved** section rather than the table.

## Read the output

Three states, and they mean different things:

| State | Meaning | Default posture |
|---|---|---|
| `known-gap` | the report names it, you don't star it | star unless there's a reason not to — a human already judged it in-scope |
| `new` | neither named nor starred | judge it on the merits |
| *(held)* | already starred | never shown |

The **Fit** column is a total; `rel/std/hlt/rec` beside it is that total
decomposed into relevance, standing, health, recency (0–100 each). Overrule the
total whenever the components tell a different story — a 40 with `rel=100` is a
better find than a 70 with `rel=25`.

Check the **Renames** and **Unresolved** sections every run. A rename that
resolves to something you already star is why a candidate vanished; an
unresolved `--extra` name means you misremembered it.

## What the script deliberately does not decide

- **Does it belong in *this* report, or a neighbouring one?** Vocabulary overlap
  is not topical judgement. A vector database scores well against half the
  reports in the suite.
- **Is a low health score "finished" or "dead"?** An API-frozen library that
  everything depends on looks identical to an abandoned one. Read the repo.
- **Is a high-star repo a real tool or a rehosted mirror?** `KDE/konsole` is a
  read-only mirror whose star count understates adoption; the reverse also
  happens.
- **Is a `list` worth starring on its own merits?** Some are (`awesome-tuis` is
  legitimately in the terminals set); most are not.

## Star the approved ones

Present the shortlist and **wait for explicit approval**. Starring writes to the
user's account — never do it on your own judgement, and never star the whole
table because it ranked well.

```bash
gh api --method PUT /user/starred/<owner>/<repo>
```

Then tell the user to pull them into the dataset:

```bash
export GITHUB_TOKEN=$(gh auth token) && npm run refresh
```

New repos do not appear in any report until that runs, and the report's own
`TAXONOMY` still needs the hand-written entry — that prose is deliberately not
generated.

## Scoring internals

See `references/scoring.md` — only needed when tuning weights or filters.
```

- [ ] **Step 2: Write `references/scoring.md`**

```markdown
# Scoring internals

Only needed when tuning. A normal run does not require this file.

## Fit score

`total = min(1, (0.35·relevance + 0.20·standing + 0.25·health + 0.20·recency) × kind_multiplier + gap_bonus) × 100`

| Term | Definition |
|---|---|
| `relevance` | share of the report's vocabulary hit by description + topics + name, saturating at 4 terms |
| `standing` | `log10(1 + stars) / 5`, capped at 1 — 100k stars ≈ 1.0 |
| `health` | `health_score / 100` from `lib/classify-core.mjs`, the dataset's own classifier |
| `recency` | 1 up to 30 days since push, linear to 0 at 365 |
| `kind_multiplier` | tool 1.0 · spec/doc 0.75 · list 0.6 · tutorial 0.45 |
| `gap_bonus` | +0.15 for `known-gap` |

Health is deliberately the dataset's own formula, not a second one, so a
candidate's 71 means the same thing as a starred repo's 71.

## Vocabulary

Drawn from the report's `meta.json` `categories` keys plus its title, lowercased,
split on non-alphanumerics, words under 3 characters and stopwords dropped.
Category names are used because a human already decided those are what the
landscape is made of.

## Kind classification

Regex over `full_name + description`:

- `list` — `awesome|curated|collection of|list of|resources`, **and** under 30
  commits in 90 days. The churn test matters: a busy repo that merely sounds
  like a list is a tool.
- `tutorial` — `tutorial|course|examples|learning|book|roadmap|interview|cheatsheet|handbook|workshop`
- `spec/doc` — `specification|rfc|documentation|whitepaper|proposal`, under 30 commits
- `tool` — everything else

Kinds demote, they never drop. Dropping lists would have removed
`rothgar/awesome-tuis` from the terminals landscape, where it belongs.

## Hard filters

Applied after resolution, before scoring: forks, archived repos, `stars < --min-stars`
(default 200), `days_since_push > --max-stale-days` (default 365).

## Renames

The GraphQL API follows renames silently. All set-diffing happens on the
**resolved** `nameWithOwner`, never the queried name. Without this, a repo
starred under its new name resurfaces every run under its old one. Known cases
from the agentic-terminals gap analysis: `pvolok/mprocs` → `pvolok/dekit`,
`stravu/crystal` → `nimbalyst/nimbalyst`.

## Pacing

250 ms between API calls, matching `ingest.mjs`. The 2026-08-12 dataset
truncation was caused by request *rate* tripping GitHub's secondary limit, not
by budget exhaustion. Do not lower this.
```

- [ ] **Step 3: Verify the skill loads**

```bash
ls -la ~/.claude/skills/discovering-repos-to-star/
head -4 ~/.claude/skills/discovering-repos-to-star/SKILL.md
```

Expected: both files present; frontmatter shows `name` and `description`.

- [ ] **Step 4: Commit** *(ask first — and note the skill lives outside this repo)*

The skill files are in `~/.claude/skills/`, not in the repo, so there is nothing to commit here unless you choose to vendor a copy under `docs/`.

---

### Task 9: End-to-end validation

**Files:**
- Modify: none (this task only runs things)

- [ ] **Step 1: Full offline suite**

```bash
unset GITHUB_TOKEN
npm run test:discover
```

Expected: every non-network assertion passes; the network section prints `… skipped: no GitHub token available`.

- [ ] **Step 2: Full suite with network**

```bash
export GITHUB_TOKEN=$(gh auth token)
npm run test:discover
```

Expected: `0 failed`.

- [ ] **Step 3: Ground truth — the known-gap count must be exact**

```bash
node -e "
import('./scripts/lib/discover/landscape.mjs').then(({loadLandscape}) => {
  const ls = loadLandscape('agentic-terminals');
  console.log('covered', ls.covered.size, 'held', ls.held.length, 'gaps', ls.knownGaps.length);
  process.exit(ls.covered.size === 59 && ls.held.length === 14 && ls.knownGaps.length === 45 ? 0 : 1);
});
"
```

Expected: `covered 59 held 14 gaps 45`, exit 0. This is the report's own stated split ("14 present, 45 missing") reproduced mechanically, and it needs no network.

- [ ] **Step 4: Confirm the graph test still passes**

```bash
npm run test:graph
```

Expected: unchanged from before this work — `classify-core.mjs` must not have moved any numbers.

- [ ] **Step 5: Run discovery on a second, unrelated report**

```bash
node scripts/discover.mjs --report rag-tooling --limit 25
```

Expected: it completes without error on a report that has no gap analysis, proving the loader is not shaped around `agentic-terminals`. Read the top 10 rows and judge whether they are on-theme — this is the recall check that cannot be asserted.

- [ ] **Step 6: Commit any fixes** *(ask first)*

```bash
git add -A
git commit -m "test: end-to-end validation of the discovery pipeline"
```

---

## Self-Review

**Spec coverage:**

| Spec requirement | Task |
|---|---|
| Node, reusing `github.mjs` | 6 |
| `gh auth token` fallback | 1 |
| Report md → covered set | 3 |
| meta.json → vocabulary | 3 |
| Three-state split, `known-gap` surfaced | 3, 7 |
| Search + `--extra` candidate sources | 5, 7 |
| Verify via GraphQL, unresolved reported | 6 |
| Rename resolution before diffing | 6, 7 |
| `classify-core` extraction, same health scale | 2 |
| Decomposed fit score, components displayed | 4, 7 |
| Kind labels demote, never drop | 4 |
| Hard filters minimal and stated | 7 |
| Skill with tiered references | 8 |
| Approval-gated starring | 8 |
| Exactly-45 ground truth | 9 |
| Unit checks (59/61, kind, unresolved, byte-identical) | 2, 3, 4, 6 |

No gaps.

**Placeholder scan:** none — every code step carries complete code, every command carries expected output.

**Type consistency:** `loadLandscape` returns `covered` as a `Map` and `starred` as a `Set` of lowercase keys; `stateFor` consumes exactly that shape and is called in Task 7 with the landscape object itself. `classifyKind` is called before `fitScore` in `discover.mjs` so `repo.kind` is populated when the multiplier is read. `projectCandidate` emits the field names `classifyRepo` reads (`created_at`, `pushed_at`, `commits_90d`, `authors_90d`, `releases_recent`, `open_issues`, `closed_issues`) — checked against `classify-core.mjs` in Task 2.

**One deliberate deviation from the spec:** the spec's step 3 said a candidate is dropped if it is in the covered set. Task 3 implements the corrected three-state model instead, and the spec has been updated to match.
