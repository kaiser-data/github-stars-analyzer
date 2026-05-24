// Netlify Function: POST /api/ask
// Body: { question: string, context?: { community?: number, repoName?: string } }
// Env:  ZAI_API_KEY  (optional: ZAI_MODEL, defaults to glm-4.6)
//
// Loads graph-context.json (pre-computed by scripts/precompute.mjs) and uses it
// as grounding for the LLM so answers are specific to the user's starred repos.
//
// Z.AI's model API is OpenAI-compatible — we call /chat/completions directly
// with fetch to avoid an extra SDK dependency.

import { readFileSync } from 'node:fs';
import { join } from 'node:path';

// GLM Coding Plan endpoint (subscription-based, OpenAI-compatible). The
// pay-as-you-go /api/paas/v4 path bills against a separate balance and returns
// "insufficient balance" for coding-plan keys. Override via ZAI_BASE_URL.
const ZAI_BASE_URL = process.env.ZAI_BASE_URL || 'https://api.z.ai/api/coding/paas/v4';
const ZAI_MODEL = process.env.ZAI_MODEL || 'glm-4.6';

// Graph context is a static file bundled with the deploy — load once.
let graphContext = null;
function getContext() {
  if (graphContext) return graphContext;
  try {
    // In Netlify Functions, process.cwd() is the site root
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

export default async function handler(req) {
  if (req.method !== 'POST') {
    return new Response('Method not allowed', { status: 405 });
  }

  const { question } = await req.json();
  if (!question?.trim()) {
    return new Response(JSON.stringify({ error: 'question is required' }), { status: 400, headers: { 'Content-Type': 'application/json' } });
  }

  if (!process.env.ZAI_API_KEY) {
    return new Response(JSON.stringify({ error: 'ZAI_API_KEY not configured' }), { status: 503, headers: { 'Content-Type': 'application/json' } });
  }

  try {
    const ctx = getContext();
    const res = await fetch(`${ZAI_BASE_URL}/chat/completions`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.ZAI_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: ZAI_MODEL,
        max_tokens: 1024,
        messages: [
          { role: 'system', content: buildSystemPrompt(ctx) },
          { role: 'user', content: question },
        ],
      }),
    });

    if (!res.ok) {
      const errText = await res.text();
      // Z.AI returns 429 + code "1113" when the account has no balance/resource
      // package — surface that as a clear, actionable billing message.
      let parsed;
      try { parsed = JSON.parse(errText); } catch { /* not JSON */ }
      if (parsed?.error?.code === '1113') {
        return new Response(
          JSON.stringify({
            error: 'Z.AI account has no balance. Add credit or a resource package at https://z.ai/manage-apikey/apikey-list, then try again.',
            code: 'zai_no_balance',
          }),
          { status: 402, headers: { 'Content-Type': 'application/json' } },
        );
      }
      return new Response(
        JSON.stringify({ error: `Z.AI ${res.status}: ${(parsed?.error?.message ?? errText).slice(0, 300)}` }),
        { status: 502, headers: { 'Content-Type': 'application/json' } },
      );
    }

    const data = await res.json();
    const answer = data?.choices?.[0]?.message?.content ?? '';

    return new Response(
      JSON.stringify({ answer, model: ZAI_MODEL }),
      { status: 200, headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' } },
    );
  } catch (err) {
    return new Response(JSON.stringify({ error: err.message }), { status: 500, headers: { 'Content-Type': 'application/json' } });
  }
}

export const config = { path: '/api/ask' };
