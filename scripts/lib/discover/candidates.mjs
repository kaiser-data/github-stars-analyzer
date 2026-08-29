// Where candidates come from: GitHub search built out of the report's own
// vocabulary, plus names the model supplies via --extra. Both are unverified
// at this stage — fetch.mjs decides what is real.

const NAME_RE = /^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/;

/** Normalize "--extra a/b, https://github.com/c/d.git" into ['a/b','c/d']. */
export function parseExtra(arg) {
  if (!arg) return [];
  const seen = new Map();
  for (const raw of String(arg).split(',')) {
    let s = raw.trim();
    if (!s) continue;
    s = s.replace(/^https?:\/\/(www\.)?github\.com\//i, '');
    s = s.replace(/\.git$/i, '').replace(/\/+$/, '');
    if (!NAME_RE.test(s)) continue;
    const key = s.toLowerCase();
    if (!seen.has(key)) seen.set(key, s);
  }
  return [...seen.values()];
}

function isoDaysBack(days, now) {
  return new Date(now - days * 24 * 60 * 60 * 1000).toISOString().slice(0, 10);
}

/**
 * One query per report category, plus a broad one from the top vocabulary
 * terms. Category names are what a human already decided the landscape is
 * made of, so they beat anything inferred from the prose.
 */
export function buildQueries(landscape, { minStars = 200, maxStaleDays = 365, now = Date.now() } = {}) {
  const filters = `fork:false archived:false stars:>=${minStars} pushed:>=${isoDaysBack(maxStaleDays, now)}`;
  const queries = [];

  for (const category of Object.keys(landscape.meta?.categories ?? {})) {
    const words = category.toLowerCase().split(/[^a-z0-9+#.]+/).filter((w) => w.length >= 3);
    if (!words.length) continue;
    queries.push({ label: `category: ${category}`, q: `${words.join(' ')} ${filters}` });
  }

  const top = (landscape.vocabulary ?? []).slice(0, 4);
  if (top.length) {
    queries.push({ label: 'vocabulary', q: `${top.join(' OR ')} ${filters}` });
  }

  return queries;
}

/**
 * Which resolved repos make the table.
 *
 * The heuristics — fork, archived, star floor, staleness — exist to keep raw
 * search noise out of the output. A `known-gap` is not search noise: the report
 * named it, so a human already judged it in scope, and the whole posture toward
 * one is "star unless there's a reason not to". Dropping a known-gap here loses
 * it silently — it appears in neither the table nor `unresolved`, so nothing
 * records that it was ever considered. The heuristics therefore apply to `new`
 * candidates only.
 */
export function selectCandidates(resolved, { stateOf, minStars = 200, maxStaleDays = 365 } = {}) {
  return resolved
    .map((r) => ({ ...r, state: stateOf(r.full_name) }))
    .filter((r) => r.state !== 'held')
    .filter(
      (r) =>
        r.state === 'known-gap' ||
        (!r.fork && !r.archived && (r.stars ?? 0) >= minStars && r.days_since_push <= maxStaleDays),
    );
}
