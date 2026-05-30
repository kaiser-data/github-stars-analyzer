// Shared system prompt for grounding LLM answers in the precomputed
// GitHub-stars knowledge graph context. Used by both the Netlify Function
// (netlify/functions/ask.mjs) at request time and the offline precompute
// script (scripts/precompute-questions.mjs).

export function buildSystemPrompt(ctx) {
  const { summary, communities, most_influential } = ctx;

  const commSummary = communities.slice(0, 12).map(c =>
    `  Community ${c.id} (${c.size} repos, main language: ${c.top_language ?? 'mixed'}): topics [${c.top_topics.slice(0, 5).join(', ')}], top repos: ${c.top_repos.slice(0, 3).join(', ')}`
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
- Top languages: ${summary.top_languages?.slice(0, 5).map(l => `${l.lang} (${l.count})`).join(', ')}

COMMUNITIES (clusters of related repos by shared topics/authors):
${commSummary}

MOST INFLUENTIAL REPOS (by PageRank in the knowledge graph):
${influential}

Use this knowledge graph to give specific, grounded answers about the user's starred repos.
Reference actual repo names, communities, and patterns you observe.
Be concise and insightful — focus on what's non-obvious.
If asked about a specific repo, relate it to its community and neighbors.`;
}

// The 5 "example" questions that get precomputed. One headline question per
// suggestion group in src/lab/LabApp.jsx — gives users an instant first-touch
// answer without burning a live LLM call. Stay in sync with LabApp.jsx pills.
export const EXAMPLE_QUESTIONS = [
  'Summarize the major themes across my starred repos.',
  'Which two communities are most similar to each other, and why?',
  'Which repos are at risk of being abandoned but still get attention?',
  'Which low-star repos punch above their weight by graph centrality?',
  'What does my star history say about my interests as a developer?',
];
