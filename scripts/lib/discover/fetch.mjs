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
      const { data } = await graphqlWithRetry(REPO_FIELDS_QUERY, { owner, name: repoName, since });
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
      const { data } = await graphqlWithRetry(SEARCH_QUERY, { q, first: perQuery });
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
