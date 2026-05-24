// Netlify Function: POST /api/ask
// Body: { question: string, context?: { community?: number, repoName?: string } }
//
// Provider-agnostic LLM caller. Talks to any OpenAI-compatible chat-completions
// endpoint (Z.AI, OpenAI, Groq, Together, DeepSeek, Mistral, OpenRouter,
// Ollama/vLLM, …). Configured by three env vars:
//
//   LLM_API_KEY   — bearer token (required)
//   LLM_BASE_URL  — endpoint root, e.g. https://api.openai.com/v1
//   LLM_MODEL     — model id, e.g. gpt-4o-mini
//
// Defaults target the Z.AI GLM Coding Plan. Legacy ZAI_* env vars are honored
// as fallbacks for backward compatibility.

import { readFileSync } from 'node:fs';
import { join } from 'node:path';

const LLM_API_KEY  = process.env.LLM_API_KEY  || process.env.ZAI_API_KEY;
const LLM_BASE_URL = (process.env.LLM_BASE_URL || process.env.ZAI_BASE_URL || 'https://api.z.ai/api/coding/paas/v4').replace(/\/+$/, '');
const LLM_MODEL    = process.env.LLM_MODEL    || process.env.ZAI_MODEL || 'glm-4.6';

// Map a base URL host to a friendly provider label (display only).
const PROVIDER_HOSTS = [
  [/(^|\.)z\.ai$/i,             'Z.AI'],
  [/(^|\.)openai\.com$/i,        'OpenAI'],
  [/(^|\.)anthropic\.com$/i,     'Anthropic'],
  [/(^|\.)groq\.com$/i,          'Groq'],
  [/(^|\.)together\.(ai|xyz)$/i, 'Together'],
  [/(^|\.)openrouter\.ai$/i,     'OpenRouter'],
  [/(^|\.)deepseek\.com$/i,      'DeepSeek'],
  [/(^|\.)mistral\.ai$/i,        'Mistral'],
  [/(^|\.)fireworks\.ai$/i,      'Fireworks'],
  [/(^|\.)perplexity\.ai$/i,     'Perplexity'],
  [/^(localhost|127\.0\.0\.1)/i, 'Local'],
];
function providerLabel(baseUrl) {
  try {
    const host = new URL(baseUrl).host;
    for (const [re, name] of PROVIDER_HOSTS) if (re.test(host)) return name;
    return host;
  } catch { return 'LLM'; }
}
const PROVIDER = providerLabel(LLM_BASE_URL);

// Generic billing / quota / credit indicators across providers.
const BILLING_RE = /(insufficient\s+(balance|credit|funds|quota)|no\s+(balance|credit|funds|quota|resource)|quota\s+exceeded|out\s+of\s+(credit|quota|funds)|payment\s+required|please\s+recharge|billing|credit.*deplet|account.*suspend)/i;

// Graph context is a static file bundled with the deploy — load once.
let graphContext = null;
function getContext() {
  if (graphContext) return graphContext;
  try {
    const raw = readFileSync(join(process.cwd(), 'public/data/graph-context.json'), 'utf8');
    graphContext = JSON.parse(raw);
  } catch {
    graphContext = { summary: { total_repos: 0 }, communities: [], most_influential: [] };
  }
  return graphContext;
}

function buildSystemPrompt(ctx) {
  const { summary, communities, most_influential } = ctx;

  const commSummary = communities.slice(0, 12).map(c =>
    `  Community ${c.id} (${c.size} repos, main language: ${c.top_language ?? 'mixed'}): topics [${c.top_topics.slice(0,5).join(', ')}], top repos: ${c.top_repos.slice(0,3).join(', ')}`
  ).join('\n');

  const influential = most_influential.slice(0, 15).map(r =>
    `  ${r.full_name} (★${r.stars?.toLocaleString()}, ${r.lifecycle_stage}, community ${r.community})`
  ).join('\n');

  return `You are an expert analyst of a developer's GitHub starred repositories.
You have access to a pre-computed knowledge graph of their ${summary.total_repos} starred repos.

GRAPH OVERVIEW:
- Total repos: ${summary.total_repos}
- Communities detected: ${communities.length}
- Lifecycle distribution: ${JSON.stringify(summary.lifecycle_distribution)}
- Top languages: ${summary.top_languages?.slice(0,5).map(l => `${l.lang} (${l.count})`).join(', ')}

COMMUNITIES (clusters of related repos by shared topics/authors):
${commSummary}

MOST INFLUENTIAL REPOS (by PageRank in the knowledge graph):
${influential}

Use this knowledge graph to give specific, grounded answers about the user's starred repos.
Reference actual repo names, communities, and patterns you observe.
Be concise and insightful — focus on what's non-obvious.
If asked about a specific repo, relate it to its community and neighbors.`;
}

// Extract a human-readable message from a (possibly JSON) error body.
function extractErrorMessage(raw) {
  try {
    const j = JSON.parse(raw);
    return j?.error?.message
      ?? j?.error?.error?.message
      ?? j?.message
      ?? j?.detail
      ?? (typeof j?.error === 'string' ? j.error : null)
      ?? raw;
  } catch {
    return raw;
  }
}

function jsonResponse(body, status = 200, extraHeaders = {}) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', ...extraHeaders },
  });
}

export default async function handler(req) {
  if (req.method !== 'POST') return new Response('Method not allowed', { status: 405 });

  const { question } = await req.json();
  if (!question?.trim()) {
    return jsonResponse({ error: 'question is required' }, 400);
  }

  if (!LLM_API_KEY) {
    return jsonResponse({ error: 'LLM_API_KEY (or ZAI_API_KEY) not configured', code: 'no_key' }, 503);
  }

  try {
    const ctx = getContext();
    const res = await fetch(`${LLM_BASE_URL}/chat/completions`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${LLM_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: LLM_MODEL,
        max_tokens: 1024,
        messages: [
          { role: 'system', content: buildSystemPrompt(ctx) },
          { role: 'user', content: question },
        ],
      }),
    });

    if (!res.ok) {
      const raw = await res.text();
      const msg = extractErrorMessage(raw).slice(0, 400);
      // Treat 402/403 + matching keyword, or 429 + billing keyword, as a
      // billing/quota issue rather than rate-limiting.
      const isBilling = res.status === 402
        || (res.status === 403 && BILLING_RE.test(msg))
        || (res.status === 429 && BILLING_RE.test(msg))
        || (res.status === 400 && BILLING_RE.test(msg));
      if (isBilling) {
        return jsonResponse({
          error: `${PROVIDER} reports a billing/quota issue: ${msg}`,
          code: 'billing',
          provider: PROVIDER,
        }, 402);
      }
      return jsonResponse({
        error: `${PROVIDER} ${res.status}: ${msg}`,
        code: 'upstream_error',
        provider: PROVIDER,
      }, 502);
    }

    const data = await res.json();
    const answer = data?.choices?.[0]?.message?.content ?? '';

    return jsonResponse({ answer, model: LLM_MODEL, provider: PROVIDER });
  } catch (err) {
    return jsonResponse({ error: err.message, code: 'fetch_error', provider: PROVIDER }, 500);
  }
}

export const config = { path: '/api/ask' };
