// Per-repo bundled GraphQL fetch: README + recent commits + releases + topics + dep manifests.
// Usage: node --env-file=.env scripts/ingest.mjs [--sample src/data/sample-100.json]
// Resumable: caches each repo to src/data/.cache/<id>.json

import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { graphql, logRate, sleep } from './lib/github.mjs';

const args = process.argv.slice(2);
const sampleArg = args.find((a) => a.startsWith('--sample='));
const SAMPLE_PATH = sampleArg ? sampleArg.split('=')[1] : 'src/data/sample-100.json';
const CACHE_DIR = 'src/data/.cache';
const README_MAX_BYTES = 16_000;

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

for (let i = 0; i < sample.repos.length; i += 1) {
  const entry = sample.repos[i];
  const cachePath = `${CACHE_DIR}/${entry.id}.json`;
  const prefix = `[${i + 1}/${sample.repos.length}] ${entry.full_name}`;

  if (existsSync(cachePath)) {
    results.push(JSON.parse(readFileSync(cachePath, 'utf8')));
    if (i % 20 === 0) console.error(`${prefix} (cached)`);
    continue;
  }

  try {
    const { data, headers } = await graphql(QUERY, {
      owner: entry.owner,
      name: entry.name,
      since: since90,
    });
    if (!data?.repository) throw new Error('repository not returned (private/deleted/renamed?)');
    const projected = projectRepo(data.repository, entry);
    writeFileSync(cachePath, JSON.stringify(projected, null, 2));
    results.push(projected);
    const remaining = data.rateLimit?.remaining;
    const cost = data.rateLimit?.cost;
    console.error(`${prefix} ✓ commits90=${projected.commits_90d} authors90=${projected.unique_authors_90d} stars=${projected.stars} (cost=${cost} remaining=${remaining})`);
    if (Date.now() - lastRateLog > 30000) {
      logRate(headers, 'snapshot');
      lastRateLog = Date.now();
    }
    await sleep(80);
  } catch (err) {
    console.error(`${prefix} ✗ ${err.message}`);
    failures.push({ ...entry, error: err.message });
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
    await sleep(200);
  }
}

const out = SAMPLE_PATH.replace('sample-', 'raw-');
writeFileSync(out, JSON.stringify({
  username: sample.username,
  total: results.length,
  failures: failures.length,
  generatedAt: new Date().toISOString(),
  repos: results,
}, null, 2));
console.error(`Wrote ${out} (${results.length} repos, ${failures.length} failures)`);
if (failures.length) {
  console.error('Failures:');
  for (const f of failures) console.error(`  ${f.full_name}: ${f.error}`);
}
