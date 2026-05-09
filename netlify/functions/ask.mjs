// Netlify Function: POST /api/ask
// Body: { question: string, context?: { community?: number, repoName?: string } }
// Env:  ANTHROPIC_API_KEY
//
// Loads graph-context.json (pre-computed by scripts/precompute.mjs) and uses it
// as grounding for the LLM so answers are specific to the user's starred repos.

import Anthropic from '@anthropic-ai/sdk';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

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

  if (!process.env.ANTHROPIC_API_KEY) {
    return new Response(JSON.stringify({ error: 'ANTHROPIC_API_KEY not configured' }), { status: 503, headers: { 'Content-Type': 'application/json' } });
  }

  try {
    const ctx = getContext();
    const msg = await client.messages.create({
      model: 'claude-sonnet-4-6',
      max_tokens: 1024,
      system: buildSystemPrompt(ctx),
      messages: [{ role: 'user', content: question }],
    });

    return new Response(
      JSON.stringify({ answer: msg.content[0].text }),
      { status: 200, headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' } },
    );
  } catch (err) {
    return new Response(JSON.stringify({ error: err.message }), { status: 500, headers: { 'Content-Type': 'application/json' } });
  }
}

export const config = { path: '/api/ask' };
