// Shared GitHub API helpers. Run with: node --env-file=.env <script>

const GITHUB_API = 'https://api.github.com';
const GRAPHQL_API = 'https://api.github.com/graphql';

export function getToken() {
  const t = process.env.GITHUB_TOKEN;
  if (!t) throw new Error('GITHUB_TOKEN missing. Run with: node --env-file=.env <script>');
  return t.trim();
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

export async function graphql(query, variables = {}, { token = getToken() } = {}) {
  const res = await fetch(GRAPHQL_API, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: authHeader(token),
    },
    body: JSON.stringify({ query, variables }),
  });
  const json = await res.json();
  if (json.errors) {
    const msg = json.errors.map((e) => e.message).join('; ');
    const err = new Error(`GraphQL: ${msg}`);
    err.errors = json.errors;
    err.partial = json.data;
    throw err;
  }
  return { data: json.data, headers: res.headers };
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
