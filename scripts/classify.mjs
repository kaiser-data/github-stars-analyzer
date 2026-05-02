// Deterministic lifecycle + health classifier (no LLM).
// Usage: node scripts/classify.mjs [--in src/data/raw-100.json]

import { readFileSync, writeFileSync } from 'node:fs';

const args = process.argv.slice(2);
const inArg = args.find((a) => a.startsWith('--in='));
const IN = inArg ? inArg.split('=')[1] : 'src/data/raw-100.json';
const OUT = IN.replace('raw-', 'classified-');

const data = JSON.parse(readFileSync(IN, 'utf8'));
const now = Date.now();
const DAY = 24 * 60 * 60 * 1000;

function daysAgo(iso) {
  if (!iso) return Infinity;
  return Math.max(0, (now - Date.parse(iso)) / DAY);
}

function busFactor(authors) {
  // CHAOSS Contributor Absence Factor: smallest set covering 50% of contributions.
  const sorted = [...authors].sort((a, b) => b.commits - a.commits);
  const total = sorted.reduce((s, a) => s + a.commits, 0);
  if (total === 0) return { count: 0, top_share: 0 };
  let acc = 0;
  let count = 0;
  for (const a of sorted) {
    acc += a.commits;
    count += 1;
    if (acc / total >= 0.5) break;
  }
  return { count, top_share: sorted[0].commits / total };
}

function lifecycleStage(r) {
  const ageDays = daysAgo(r.created_at);
  const sinceLastPush = daysAgo(r.pushed_at);
  const commits90 = r.commits_90d ?? 0;
  const authors90 = r.unique_authors_90d ?? 0;
  const lastRelease = r.releases_recent?.[0]?.published_at;
  const sinceLastRelease = lastRelease ? daysAgo(lastRelease) : Infinity;

  // Hard signals
  if (sinceLastPush > 365 && sinceLastRelease > 540) return 'Abandoned';
  if (r.archived) return 'Abandoned';

  // Hot: young + active + multi-author
  if (ageDays < 365 * 2 && commits90 >= 30 && authors90 >= 3) return 'Hot';

  // Rising: very young + accelerating activity
  if (ageDays < 365 && commits90 >= 10) return 'Rising';

  // Classic: old + still healthy + sustained activity
  if (ageDays > 365 * 3 && commits90 >= 10 && authors90 >= 2) return 'Classic';

  // Mature: old, low but non-zero activity, stable
  if (ageDays > 365 * 2 && sinceLastPush < 180) return 'Mature';

  // Declining: was active, dropping off
  if (sinceLastPush < 365 && commits90 < 5) return 'Declining';

  // Default fallback for genuinely quiet
  if (sinceLastPush > 180) return 'Declining';
  return 'Mature';
}

function healthScore(r, bf) {
  // 0–100 score combining activity, contributor diversity, release cadence, issue ratio.
  const sinceLastPush = daysAgo(r.pushed_at);
  const ageDays = Math.max(1, daysAgo(r.created_at));

  // Activity recency (0–30): full credit if pushed in last 30d, decays over a year
  const activity = Math.max(0, 30 - Math.min(30, sinceLastPush / 12));

  // Author diversity (0–25): more bus-factor count = more diversity
  const diversity = Math.min(25, bf.count * 5);

  // Commit volume relative to age (0–20)
  const commitsPerMonth = (r.commits_90d ?? 0) / 3;
  const volume = Math.min(20, Math.log10(1 + commitsPerMonth) * 12);

  // Release cadence (0–15)
  const recentReleases = (r.releases_recent ?? []).filter((rel) => daysAgo(rel.published_at) < 365).length;
  const releases = Math.min(15, recentReleases * 2);

  // Issue closure ratio (0–10)
  const total = (r.open_issues ?? 0) + (r.closed_issues ?? 0);
  const closureRatio = total === 0 ? 0.5 : (r.closed_issues ?? 0) / total;
  const closure = closureRatio * 10;

  return Math.round(activity + diversity + volume + releases + closure);
}

function momentum(r) {
  const stars = r.stars ?? 0;
  const ageDays = Math.max(30, daysAgo(r.created_at));
  const sinceLastPush = daysAgo(r.pushed_at);
  // Rough estimator: lifetime stars/day weighted by activity. The real momentum needs
  // GraphQL stargazer history per repo (slow). This is a serviceable proxy for now.
  const lifetimeRate = stars / ageDays;
  const activityMult = sinceLastPush < 7 ? 2.5 : sinceLastPush < 30 ? 1.6 : sinceLastPush < 90 ? 1.0 : sinceLastPush < 365 ? 0.4 : 0.1;
  const ageMult = ageDays < 365 ? 1 : ageDays < 365 * 2 ? 0.85 : ageDays < 365 * 3 ? 0.7 : 0.5;
  const estimated30d = Math.round(lifetimeRate * 30 * activityMult * ageMult);
  return { estimated_stars_30d: estimated30d, lifetime_per_day: lifetimeRate };
}

const classified = data.repos.map((r) => {
  const bf = busFactor(r.authors_90d ?? []);
  const stage = lifecycleStage(r);
  const score = healthScore(r, bf);
  const m = momentum(r);
  const ageDays = Math.round(daysAgo(r.created_at));
  const sinceLastPush = Math.round(daysAgo(r.pushed_at));
  return {
    ...r,
    age_days: ageDays,
    days_since_push: sinceLastPush,
    bus_factor: bf.count,
    top_author_share: Math.round(bf.top_share * 100) / 100,
    lifecycle_stage: stage,
    health_score: score,
    momentum: m,
  };
});

const dist = classified.reduce((acc, r) => ((acc[r.lifecycle_stage] = (acc[r.lifecycle_stage] ?? 0) + 1), acc), {});
console.error('Lifecycle distribution:', dist);
console.error('Avg health score:', Math.round(classified.reduce((s, r) => s + r.health_score, 0) / classified.length));

writeFileSync(OUT, JSON.stringify({
  ...data,
  generatedAt: new Date().toISOString(),
  distribution: dist,
  repos: classified,
}, null, 2));
console.error(`Wrote ${OUT}`);
