// Shared daily + weekly spend cap for /api/ask.
//
// Serverless instances share no memory, so the running total lives in Redis
// (Upstash REST API via fetch, no client library). Amounts are integer
// micro-dollars so INCRBY stays exact.
//
// Flow: reserve the worst case (prompt estimate + max_tokens) before calling
// the model, refuse if that would cross either cap, then settle to the real
// usage once the stream ends. Reserving first means concurrent requests can't
// overshoot the cap together.
//
// Env:
//   BUDGET_DAILY_USD, BUDGET_WEEKLY_USD   caps (default 1 and 5; 0 disables one)
//   LLM_PRICE_IN_PER_M, LLM_PRICE_OUT_PER_M  USD per 1M tokens (defaults are
//                                            deliberately high so a missing
//                                            price over-counts, never under)
//   KV_REST_API_URL + KV_REST_API_TOKEN    (Vercel's Upstash integration), or
//   UPSTASH_REDIS_REST_URL + UPSTASH_REDIS_REST_TOKEN
//
// Fails closed: with a cap set but no reachable store, every request is refused.

const num = (v, d) => (v === undefined || v === '' || !Number.isFinite(Number(v)) ? d : Number(v));

export const DAILY_USD = num(process.env.BUDGET_DAILY_USD, 1);
export const WEEKLY_USD = num(process.env.BUDGET_WEEKLY_USD, 5);
const PRICE_IN = num(process.env.LLM_PRICE_IN_PER_M, 1);
const PRICE_OUT = num(process.env.LLM_PRICE_OUT_PER_M, 3);

const REDIS_URL = (process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL || '').replace(/\/+$/, '');
const REDIS_TOKEN = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN || '';

const MICRO = 1_000_000;
const enabled = DAILY_USD > 0 || WEEKLY_USD > 0;

// Rough token count for text we send; ~4 chars per token, rounded up.
export const estimateTokens = (text) => Math.ceil((text?.length || 0) / 4);

export const costMicros = (inTok, outTok) =>
  Math.ceil(((inTok * PRICE_IN) + (outTok * PRICE_OUT)) * MICRO / 1_000_000);

function periodKeys(now = new Date()) {
  const day = now.toISOString().slice(0, 10);
  // Week = Monday-start UTC week, keyed by its Monday.
  const monday = new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate()));
  monday.setUTCDate(monday.getUTCDate() - ((monday.getUTCDay() + 6) % 7));
  return {
    day: `ask:spend:day:${day}`,
    week: `ask:spend:week:${monday.toISOString().slice(0, 10)}`,
  };
}

async function redis(commands) {
  const res = await fetch(`${REDIS_URL}/pipeline`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${REDIS_TOKEN}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(commands),
  });
  if (!res.ok) throw new Error(`spend store ${res.status}`);
  const out = await res.json();
  const err = out.find((r) => r.error);
  if (err) throw new Error(`spend store: ${err.error}`);
  return out.map((r) => r.result);
}

async function add(keys, micros) {
  const [day, , week] = await redis([
    ['INCRBY', keys.day, micros], ['EXPIRE', keys.day, 2 * 86400],
    ['INCRBY', keys.week, micros], ['EXPIRE', keys.week, 8 * 86400],
  ]);
  return { day: Number(day), week: Number(week) };
}

const usd = (micros) => `$${(micros / MICRO).toFixed(2)}`;

// Returns { ok: true, settle(inTok, outTok) } or { ok: false, status, body }.
export async function reserve(inTokEstimate, maxOutTokens) {
  if (!enabled) return { ok: true, settle: async () => {} };
  if (!REDIS_URL || !REDIS_TOKEN) {
    return {
      ok: false, status: 503,
      body: { error: 'Spend cap is on but no spend store is configured (KV_REST_API_URL / KV_REST_API_TOKEN).', code: 'budget_store' },
    };
  }
  const keys = periodKeys();
  const held = costMicros(inTokEstimate, maxOutTokens);
  let totals;
  try {
    totals = await add(keys, held);
  } catch (err) {
    return { ok: false, status: 503, body: { error: `Spend store unavailable: ${err.message}`, code: 'budget_store' } };
  }
  const overDay = DAILY_USD > 0 && totals.day > DAILY_USD * MICRO;
  const overWeek = WEEKLY_USD > 0 && totals.week > WEEKLY_USD * MICRO;
  if (overDay || overWeek) {
    await add(keys, -held).catch(() => {});
    const which = overDay ? `daily budget (${usd(DAILY_USD * MICRO)})` : `weekly budget (${usd(WEEKLY_USD * MICRO)})`;
    return {
      ok: false, status: 429,
      body: {
        error: `Ask AI has used its ${which}. It resets ${overDay ? 'at 00:00 UTC' : 'on Monday 00:00 UTC'}.`,
        code: 'budget',
      },
    };
  }
  let settled = false;
  return {
    ok: true,
    // Swap the worst-case hold for the real cost. Called once; later calls no-op.
    async settle(inTok, outTok) {
      if (settled) return;
      settled = true;
      const delta = costMicros(inTok, outTok) - held;
      if (delta !== 0) await add(keys, delta).catch(() => {});
    },
  };
}
