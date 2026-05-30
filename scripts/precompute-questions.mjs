#!/usr/bin/env node
// scripts/precompute-questions.mjs
// Generate cached answers for the 5 example questions so the Ask AI tab can
// show instant responses for the headliner pills without burning a live LLM
// call. Reuses the same system prompt as the runtime function.
//
// Usage:  node --env-file=.env scripts/precompute-questions.mjs
// Env:    LLM_API_KEY (or ZAI_API_KEY)
//         LLM_BASE_URL (default: Z.AI coding plan endpoint)
//         LLM_MODEL    (default: glm-4.6)
//         LLM_MAX_TOKENS (default: 2048)
//
// Writes: public/data/questions.json
//   {
//     generated_at: ISO timestamp,
//     model: string, provider: string,
//     items: [{ question, answer }]
//   }

import { readFileSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildSystemPrompt, EXAMPLE_QUESTIONS } from './lib/ask-prompt.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');

const LLM_API_KEY  = process.env.LLM_API_KEY  || process.env.ZAI_API_KEY;
const LLM_BASE_URL = (process.env.LLM_BASE_URL || process.env.ZAI_BASE_URL || 'https://api.z.ai/api/coding/paas/v4').replace(/\/+$/, '');
const LLM_MODEL    = process.env.LLM_MODEL    || process.env.ZAI_MODEL || 'glm-4.6';
const LLM_MAX_TOKENS = Number(process.env.LLM_MAX_TOKENS) || 2048;

if (!LLM_API_KEY) {
  console.error('LLM_API_KEY (or ZAI_API_KEY) is not set. Add it to .env and retry.');
  process.exit(1);
}

const providerOf = (url) => {
  try { return new URL(url).host; } catch { return 'unknown'; }
};
const PROVIDER = providerOf(LLM_BASE_URL);

const ctxPath = join(ROOT, 'public/data/graph-context.json');
const ctx = JSON.parse(readFileSync(ctxPath, 'utf8'));
const system = buildSystemPrompt(ctx);

async function ask(question) {
  const res = await fetch(`${LLM_BASE_URL}/chat/completions`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${LLM_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: LLM_MODEL,
      max_tokens: LLM_MAX_TOKENS,
      messages: [
        { role: 'system', content: system },
        { role: 'user', content: question },
      ],
    }),
  });
  if (!res.ok) {
    const body = await res.text().catch(() => '');
    throw new Error(`HTTP ${res.status}: ${body.slice(0, 300)}`);
  }
  const data = await res.json();
  const answer = data?.choices?.[0]?.message?.content?.trim();
  if (!answer) throw new Error(`empty answer (response: ${JSON.stringify(data).slice(0, 200)})`);
  return answer;
}

console.log(`Precomputing ${EXAMPLE_QUESTIONS.length} example Q&As using ${LLM_MODEL} via ${PROVIDER}…\n`);

const items = [];
for (const [i, question] of EXAMPLE_QUESTIONS.entries()) {
  process.stdout.write(`[${i + 1}/${EXAMPLE_QUESTIONS.length}] ${question}\n  → `);
  const t0 = Date.now();
  try {
    const answer = await ask(question);
    const ms = Date.now() - t0;
    process.stdout.write(`${answer.length} chars in ${(ms / 1000).toFixed(1)}s\n\n`);
    items.push({ question, answer });
  } catch (err) {
    process.stdout.write(`FAILED — ${err.message}\n\n`);
    items.push({ question, answer: null, error: err.message });
  }
}

const out = {
  generated_at: new Date().toISOString(),
  model: LLM_MODEL,
  provider: PROVIDER,
  graph_repos: ctx.summary?.total_repos ?? null,
  items,
};

const outPath = join(ROOT, 'public/data/questions.json');
writeFileSync(outPath, JSON.stringify(out, null, 2));
const ok = items.filter(i => i.answer).length;
console.log(`Wrote ${outPath} (${ok}/${items.length} succeeded)`);
