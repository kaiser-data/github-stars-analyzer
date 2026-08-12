// Per-repo bundled GraphQL fetch: README + recent commits + releases + topics + dep manifests.
// Usage: node --env-file=.env scripts/ingest.mjs [--sample src/data/sample-100.json]
// Resumable: caches each repo to src/data/.cache/<id>.json

import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { graphqlWithRetry, logRate, sleep } from './lib/github.mjs';

const args = process.argv.slice(2);
const sampleArg = args.find((a) => a.startsWith('--sample='));
const SAMPLE_PATH = sampleArg ? sampleArg.split('=')[1] : 'src/data/sample-100.json';
const maxAgeArg = args.find((a) => a.startsWith('--max-age='));
const MAX_AGE_DAYS = maxAgeArg ? Number(maxAgeArg.split('=')[1]) : Infinity;
const numArg = (name, fallback) => {
  const a = args.find((x) => x.startsWith(`--${name}=`));
  return a ? Number(a.split('=')[1]) : fallback;
};
const CACHE_DIR = 'src/data/.cache';
const OUT_PATH = SAMPLE_PATH.replace('sample-', 'raw-');
const README_MAX_BYTES = 16_000;
const DAY_MS = 24 * 60 * 60 * 1000;

// Pacing. These queries are heavy (README + 100 commits + four count fields), so
// GitHub's secondary limit — which counts request *cost* per minute, not points —
// trips well before the 5,000/hr primary budget shows any dent. On a CI runner,
// where round-trips are far quicker than from a laptop, 80ms between requests was
// fast enough to get throttled from repo ~86 onward for the rest of the run.
// PACE_MS is a floor that backs off on its own the moment we're throttled.
let paceMs = numArg('pace', 250);
const MAX_PACE_MS = 4000;

// A run that loses more than this fraction of the sample is not a dataset, it's
// an outage. Fail loudly instead of writing a truncated file that later stages
// would happily classify, graph and commit.
const MAX_FAILURE_RATE = numArg('max-failure-rate', 0.1);
// Consecutive retry-exhausted failures before we stop wasting the run entirely.
const ABORT_AFTER_CONSECUTIVE = numArg('abort-after', 25);

mkdirSync(CACHE_DIR, { recursive: true });

const sample = JSON.parse(readFileSync(SAMPLE_PATH, 'utf8'));
console.error(`Ingesting ${sample.repos.length} repos from ${SAMPLE_PATH}`);

const since90 = new Date(Date.now() - 90 * 24 * 60 * 60 * 1000).toISOString();

const QUERY = `
query Repo($owner: String!, $name: String!, $since: GitTimestamp!) {
  repository(owner: $owner, name: $name) {
    nameWithOwner
    description
    homepageUrl
    url
    isArchived
    isFork
    isMirror
    isTemplate
    isInOrganization
    createdAt
    pushedAt
    updatedAt
    diskUsage
    stargazerCount
    forkCount
    watchers { totalCount }
    primaryLanguage { name }
    languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
      totalSize
      edges { size node { name } }
    }
    licenseInfo { name spdxId }
    repositoryTopics(first: 30) { nodes { topic { name } } }
    parent { nameWithOwner }
    owner { login __typename }
    readmeMd: object(expression: "HEAD:README.md") { ... on Blob { text byteSize } }
    readmeRst: object(expression: "HEAD:README.rst") { ... on Blob { text byteSize } }
    readmeTxt: object(expression: "HEAD:README.txt") { ... on Blob { text byteSize } }
    readmeNoExt: object(expression: "HEAD:README") { ... on Blob { text byteSize } }
    readmeMdx: object(expression: "HEAD:README.mdx") { ... on Blob { text byteSize } }
    defaultBranchRef {
      name
      target {
        ... on Commit {
          historySince: history(first: 100, since: $since) {
            totalCount
            nodes {
              committedDate
              author { user { login } email name }
            }
          }
        }
      }
    }
    releases(first: 10, orderBy: {field: CREATED_AT, direction: DESC}) {
      totalCount
      nodes { tagName name publishedAt isPrerelease }
    }
    issues(states: OPEN) { totalCount }
    closedIssues: issues(states: CLOSED) { totalCount }
    openPRs: pullRequests(states: OPEN) { totalCount }
    mergedPRs: pullRequests(states: MERGED) { totalCount }
  }
  rateLimit { remaining limit resetAt cost }
}`;

function pickReadme(repo) {
  for (const k of ['readmeMd', 'readmeMdx', 'readmeRst', 'readmeTxt', 'readmeNoExt']) {
    const obj = repo[k];
    if (obj && typeof obj.text === 'string' && obj.text.length > 0) {
      return { source: k, text: obj.text.slice(0, README_MAX_BYTES), byteSize: obj.byteSize };
    }
  }
  return { source: null, text: '', byteSize: 0 };
}

function projectRepo(repo, sampleEntry) {
  const readme = pickReadme(repo);
  const commits = repo.defaultBranchRef?.target?.historySince?.nodes ?? [];
  const totalCommits90d = repo.defaultBranchRef?.target?.historySince?.totalCount ?? 0;
  const authorTallies = new Map();
  for (const c of commits) {
    const login = c.author?.user?.login ?? c.author?.email ?? c.author?.name ?? 'unknown';
    authorTallies.set(login, (authorTallies.get(login) ?? 0) + 1);
  }
  const authors90d = [...authorTallies.entries()]
    .map(([login, commits]) => ({ login, commits }))
    .sort((a, b) => b.commits - a.commits);

  return {
    id: sampleEntry.id,
    full_name: repo.nameWithOwner,
    owner: repo.owner?.login ?? sampleEntry.owner,
    owner_type: repo.owner?.__typename ?? null,
    name: repo.nameWithOwner.split('/')[1],
    description: repo.description ?? '',
    homepage: repo.homepageUrl ?? '',
    url: repo.url,
    archived: repo.isArchived,
    fork: repo.isFork,
    mirror: repo.isMirror,
    template: repo.isTemplate,
    in_org: repo.isInOrganization,
    created_at: repo.createdAt,
    pushed_at: repo.pushedAt,
    updated_at: repo.updatedAt,
    disk_usage_kb: repo.diskUsage ?? null,
    stars: repo.stargazerCount,
    forks: repo.forkCount,
    watchers: repo.watchers?.totalCount ?? 0,
    primary_language: repo.primaryLanguage?.name ?? null,
    languages: (repo.languages?.edges ?? []).map((e) => ({ name: e.node.name, size: e.size })),
    license: repo.licenseInfo?.spdxId ?? null,
    license_name: repo.licenseInfo?.name ?? null,
    topics: (repo.repositoryTopics?.nodes ?? []).map((n) => n.topic.name),
    parent: repo.parent?.nameWithOwner ?? null,
    default_branch: repo.defaultBranchRef?.name ?? null,
    readme_source: readme.source,
    readme_bytes: readme.byteSize,
    readme_text: readme.text,
    commits_90d: totalCommits90d,
    authors_90d: authors90d,
    unique_authors_90d: authors90d.length,
    releases_total: repo.releases?.totalCount ?? 0,
    releases_recent: (repo.releases?.nodes ?? []).map((r) => ({
      tag: r.tagName,
      name: r.name,
      published_at: r.publishedAt,
      prerelease: r.isPrerelease,
    })),
    open_issues: repo.issues?.totalCount ?? 0,
    closed_issues: repo.closedIssues?.totalCount ?? 0,
    open_prs: repo.openPRs?.totalCount ?? 0,
    merged_prs: repo.mergedPRs?.totalCount ?? 0,
    stratum: sampleEntry.stratum,
    fetched_at: new Date().toISOString(),
  };
}

const results = [];
const failures = [];
let lastRateLog = 0;
let staleRefreshed = 0;
let consecutiveFailures = 0;
let throttleEvents = 0;
let aborted = null;

for (let i = 0; i < sample.repos.length; i += 1) {
  const entry = sample.repos[i];
  const cachePath = `${CACHE_DIR}/${entry.id}.json`;
  const prefix = `[${i + 1}/${sample.repos.length}] ${entry.full_name}`;

  if (existsSync(cachePath)) {
    const cached = JSON.parse(readFileSync(cachePath, 'utf8'));
    const ageDays = cached.fetched_at
      ? (Date.now() - Date.parse(cached.fetched_at)) / DAY_MS
      : Infinity;
    if (ageDays < MAX_AGE_DAYS) {
      results.push(cached);
      if (i % 50 === 0) console.error(`${prefix} (cached, age=${ageDays.toFixed(1)}d)`);
      continue;
    }
    // Stale → fall through and refetch. The new fetch will overwrite the cache file.
    staleRefreshed += 1;
    console.error(`${prefix} (stale, ${ageDays.toFixed(1)}d > ${MAX_AGE_DAYS}d, refetching)`);
  }

  try {
    const { data, headers } = await graphqlWithRetry(QUERY, {
      owner: entry.owner,
      name: entry.name,
      since: since90,
    }, {
      onRetry: ({ attempt, retries, waitMs, error }) => {
        if (error.kind === 'rate_limit') throttleEvents += 1;
        console.error(
          `${prefix} ⟳ ${error.kind} (${attempt}/${retries}), waiting ${Math.round(waitMs / 1000)}s — ${error.message}`,
        );
        // Throttling means our pace is wrong, not just this request. Slow the
        // whole run down so we stop earning penalties on every subsequent repo.
        if (error.kind === 'rate_limit') paceMs = Math.min(paceMs * 2, MAX_PACE_MS);
      },
    });
    if (!data?.repository) throw new Error('repository not returned (private/deleted/renamed?)');
    const projected = projectRepo(data.repository, entry);
    writeFileSync(cachePath, JSON.stringify(projected, null, 2));
    results.push(projected);
    consecutiveFailures = 0;
    const remaining = data.rateLimit?.remaining;
    const cost = data.rateLimit?.cost;
    console.error(`${prefix} ✓ commits90=${projected.commits_90d} authors90=${projected.unique_authors_90d} stars=${projected.stars} (cost=${cost} remaining=${remaining})`);
    if (Date.now() - lastRateLog > 30000) {
      logRate(headers, 'snapshot');
      lastRateLog = Date.now();
    }
    await sleep(paceMs);
  } catch (err) {
    const kind = err.kind ?? 'unknown';
    console.error(`${prefix} ✗ [${kind}] ${err.message}`);
    failures.push({ ...entry, error: err.message, kind });
    consecutiveFailures += 1;
    // Still try to recover partial data if GraphQL returned partial
    if (err.partial?.repository) {
      try {
        const projected = projectRepo(err.partial.repository, entry);
        projected._partial = true;
        projected._error = err.message;
        writeFileSync(cachePath, JSON.stringify(projected, null, 2));
        results.push(projected);
      } catch {}
    }
    if (consecutiveFailures >= ABORT_AFTER_CONSECUTIVE) {
      aborted = `${consecutiveFailures} consecutive failures at repo ${i + 1}/${sample.repos.length}`;
      console.error(`\n✗ Aborting ingest: ${aborted}.`);
      console.error('  Nothing downstream should run on a dataset this incomplete.');
      break;
    }
    await sleep(Math.max(200, paceMs));
  }
}

const byKind = failures.reduce((acc, f) => ((acc[f.kind] = (acc[f.kind] ?? 0) + 1), acc), {});
if (failures.length) {
  console.error('\nFailures by kind:', byKind);
  console.error('Failures:');
  for (const f of failures) console.error(`  ${f.full_name}: [${f.kind}] ${f.error}`);
}

// Refuse to write a truncated dataset. `npm run refresh` chains with `&&`, so a
// non-zero exit here stops classify/precompute and leaves the previous good
// raw-*.json in place. Per-repo work isn't lost — the cache keeps every success.
const attempted = failures.length + results.length;
const failureRate = attempted ? failures.length / attempted : 0;
if (aborted || failureRate > MAX_FAILURE_RATE) {
  console.error(
    `\n✗ Ingest failed: ${failures.length}/${attempted} lookups failed ` +
    `(${(failureRate * 100).toFixed(1)}%, limit ${(MAX_FAILURE_RATE * 100).toFixed(0)}%).` +
    (aborted ? ` Aborted early: ${aborted}.` : ''),
  );
  if (throttleEvents) {
    console.error(
      `  ${throttleEvents} rate-limit retries — GitHub was throttling. Re-run to resume ` +
      `from cache, or lower the pace with --pace=<ms> (current ${paceMs}ms).`,
    );
  }
  console.error(`  ${OUT_PATH} left untouched; downstream stages will not run.`);
  process.exit(1);
}

writeFileSync(OUT_PATH, JSON.stringify({
  username: sample.username,
  total: results.length,
  failures: failures.length,
  failuresByKind: byKind,
  generatedAt: new Date().toISOString(),
  repos: results,
}, null, 2));
console.error(`Wrote ${OUT_PATH} (${results.length} repos, ${staleRefreshed} refreshed, ${failures.length} failures)`);
