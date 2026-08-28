// Shared GitHub API helpers. Run with: node --env-file=.env <script>

import { execFileSync } from 'node:child_process';

const GITHUB_API = 'https://api.github.com';
const GRAPHQL_API = 'https://api.github.com/graphql';

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

function authHeader(token) {
  return token.startsWith('github_pat_') || token.startsWith('ghp_')
    ? `Bearer ${token}`
    : `token ${token}`;
}

export async function rest(path, { token = getToken(), accept = 'application/vnd.github+json' } = {}) {
  const url = path.startsWith('http') ? path : `${GITHUB_API}${path}`;
  const res = await fetch(url, {
    headers: {
      Accept: accept,
      Authorization: authHeader(token),
      'X-GitHub-Api-Version': '2022-11-28',
    },
  });
  if (!res.ok) {
    const body = await res.text().catch(() => '');
    throw new Error(`REST ${res.status} ${res.statusText} ${url}\n${body.slice(0, 400)}`);
  }
  return { data: await res.json(), headers: res.headers };
}

// Every failure mode gets a `kind` so callers can tell a genuinely missing repo
// from a throttled or flaky one. Without this the two are indistinguishable and
// a throttled run looks like 1,500 deleted repos.
//   'not_found'  — repo is private/deleted/renamed. Permanent; skip it.
//   'rate_limit' — primary or secondary limit. Retryable after a wait.
//   'network'    — DNS/TCP/TLS failure ("fetch failed"). Retryable.
//   'http'       — other non-2xx. Not retried unless 5xx.
//   'graphql'    — 200 with an `errors` array we don't recognise.
export class GitHubError extends Error {
  constructor(message, { kind, status = null, retryAfter = null, cause } = {}) {
    super(message, cause ? { cause } : undefined);
    this.name = 'GitHubError';
    this.kind = kind;
    this.status = status;
    this.retryAfter = retryAfter; // seconds until it's worth trying again, or null
  }
}

// Seconds to wait, preferring GitHub's own advice over our guesswork.
function retryAfterSeconds(headers) {
  const ra = Number(headers.get('retry-after'));
  if (Number.isFinite(ra) && ra > 0) return ra;
  const remaining = Number(headers.get('x-ratelimit-remaining'));
  const reset = Number(headers.get('x-ratelimit-reset'));
  if (remaining === 0 && Number.isFinite(reset)) {
    return Math.max(1, Math.ceil(reset - Date.now() / 1000));
  }
  return null;
}

export function rateSummary(headers) {
  const remaining = headers.get('x-ratelimit-remaining');
  if (remaining == null) return 'rate n/a';
  const reset = Number(headers.get('x-ratelimit-reset'));
  const resetIn = Number.isFinite(reset)
    ? ` resets in ${Math.max(0, Math.round((reset - Date.now() / 1000) / 60))}m`
    : '';
  return `rate ${remaining}/${headers.get('x-ratelimit-limit')}${resetIn}`;
}

export async function graphql(query, variables = {}, { token = getToken() } = {}) {
  let res;
  try {
    res = await fetch(GRAPHQL_API, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: authHeader(token),
      },
      body: JSON.stringify({ query, variables }),
    });
  } catch (cause) {
    throw new GitHubError(`network: ${cause.message}`, { kind: 'network', cause });
  }

  // Read as text first: throttle and gateway responses are not always JSON, and
  // res.json() on those throws a SyntaxError that hides the real status.
  const body = await res.text().catch(() => '');
  let json = null;
  try {
    json = body ? JSON.parse(body) : null;
  } catch {
    /* handled below via res.ok / missing data */
  }

  if (!res.ok) {
    // A tripped secondary rate limit answers 403/429 with a bare {message},
    // no `errors` key — which used to fall through as "repository not returned".
    const msg = json?.message || body.slice(0, 200) || res.statusText;
    const throttled = res.status === 403 || res.status === 429;
    throw new GitHubError(`HTTP ${res.status}: ${msg} [${rateSummary(res.headers)}]`, {
      kind: throttled ? 'rate_limit' : 'http',
      status: res.status,
      retryAfter: retryAfterSeconds(res.headers),
    });
  }

  if (json?.errors) {
    const msg = json.errors.map((e) => e.message).join('; ');
    const types = json.errors.map((e) => e.type);
    const kind = types.includes('RATE_LIMITED')
      ? 'rate_limit'
      : types.includes('NOT_FOUND')
        ? 'not_found'
        : 'graphql';
    const err = new GitHubError(`GraphQL: ${msg}`, {
      kind,
      status: res.status,
      retryAfter: retryAfterSeconds(res.headers),
    });
    err.errors = json.errors;
    err.partial = json.data;
    throw err;
  }

  if (!json || typeof json !== 'object') {
    throw new GitHubError(`HTTP ${res.status} with unparseable body: ${body.slice(0, 200)}`, {
      kind: 'http',
      status: res.status,
    });
  }

  return { data: json.data, headers: res.headers };
}

// Retries the transient kinds with backoff, honouring Retry-After when GitHub
// sends one. Permanent failures (not_found, 4xx that isn't a limit) throw at once.
export async function graphqlWithRetry(query, variables = {}, opts = {}) {
  const {
    retries = 4,
    baseDelayMs = 2000,
    maxDelayMs = 120_000,
    onRetry,
    ...rest
  } = opts;

  for (let attempt = 0; ; attempt += 1) {
    try {
      return await graphql(query, variables, rest);
    } catch (err) {
      const retryable =
        err.kind === 'rate_limit' || err.kind === 'network' || err.status >= 500;
      if (!retryable || attempt >= retries) throw err;
      const waitMs =
        err.retryAfter != null
          ? Math.min(err.retryAfter * 1000, maxDelayMs)
          : Math.min(baseDelayMs * 2 ** attempt, maxDelayMs);
      onRetry?.({ attempt: attempt + 1, retries, waitMs, error: err });
      await sleep(waitMs);
    }
  }
}

export function logRate(headers, label = '') {
  const remaining = headers.get('x-ratelimit-remaining');
  const limit = headers.get('x-ratelimit-limit');
  const reset = headers.get('x-ratelimit-reset');
  if (remaining != null) {
    const resetIn = reset ? Math.max(0, Math.round(reset * 1000 - Date.now()) / 1000) : null;
    console.error(`  rate ${label}: ${remaining}/${limit}${resetIn != null ? ` (resets in ${Math.round(resetIn / 60)}m)` : ''}`);
  }
}

export function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}
