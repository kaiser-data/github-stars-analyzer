// Kind classification and the fit score. Health comes from the dataset's own
// classifier (lib/classify-core.mjs); everything here is about *relevance to
// this report*, which health cannot express.

const LIST_RE = /\b(awesome|curated|collection of|list of|resources)\b/i;
const TUTORIAL_RE = /\b(tutorial|course|examples?|learning|book|roadmap|interview|cheat ?sheet|handbook|workshop)\b/i;
const DOC_RE = /\b(specification|rfc|documentation|whitepaper|proposal)\b/i;

// Curation-shaped repos with real commit churn are usually tools that merely
// sound like lists, so activity is part of the test rather than the name alone.
const CURATION_CHURN_CEILING = 30;

export function classifyKind(repo) {
  const hay = `${repo.full_name ?? ''} ${repo.description ?? ''}`;
  const commits = repo.commits_90d ?? 0;
  if (LIST_RE.test(hay) && commits < CURATION_CHURN_CEILING) return 'list';
  if (TUTORIAL_RE.test(hay)) return 'tutorial';
  if (DOC_RE.test(hay) && commits < CURATION_CHURN_CEILING) return 'spec/doc';
  return 'tool';
}

const KIND_MULTIPLIER = { tool: 1.0, 'spec/doc': 0.75, list: 0.6, tutorial: 0.45 };

/** Share of the report's vocabulary the repo's own text hits, saturating at 4 terms. */
export function relevance(repo, vocabulary) {
  if (!vocabulary?.length) return 0;
  const hay = `${repo.description ?? ''} ${(repo.topics ?? []).join(' ')} ${repo.full_name ?? ''}`.toLowerCase();
  let hits = 0;
  for (const term of vocabulary) if (hay.includes(term)) hits += 1;
  return Math.min(1, hits / Math.min(4, vocabulary.length));
}

/** Log-scaled so a 200k-star list cannot outrank a 3k-star tool on size alone. */
export function standing(stars) {
  return Math.min(1, Math.log10(1 + Math.max(0, stars ?? 0)) / 5);
}

export function recency(daysSincePush) {
  if (!Number.isFinite(daysSincePush)) return 0;
  if (daysSincePush <= 30) return 1;
  if (daysSincePush >= 365) return 0;
  return 1 - (daysSincePush - 30) / 335;
}

const WEIGHTS = { relevance: 0.35, standing: 0.20, health: 0.25, recency: 0.20 };

// The report author already judged a known-gap repo in-scope and wrote it down;
// the only open question is whether to star it. That is worth a head start.
const KNOWN_GAP_BONUS = 0.15;

export function fitScore(repo, vocabulary, { state = 'new' } = {}) {
  const parts = {
    relevance: relevance(repo, vocabulary),
    standing: standing(repo.stars),
    health: Math.min(1, Math.max(0, (repo.health_score ?? 0) / 100)),
    recency: recency(repo.days_since_push),
  };
  const base = Object.entries(WEIGHTS).reduce((s, [k, w]) => s + w * parts[k], 0);
  const kindMultiplier = KIND_MULTIPLIER[repo.kind] ?? 1;
  const bonus = state === 'known-gap' ? KNOWN_GAP_BONUS : 0;
  return {
    parts,
    kind_multiplier: kindMultiplier,
    total: Math.round(Math.min(1, base * kindMultiplier + bonus) * 100),
  };
}
