// Unit tests for the discovery pipeline. Run: npm run test:discover
// Style matches scripts/test-graph.mjs — no framework, exit code from failures.

let pass = 0;
let fail = 0;
function ok(label, cond, detail = '') {
  if (cond) { console.log(`  ✓ ${label}${detail ? ' — ' + detail : ''}`); pass += 1; }
  else { console.error(`  ✗ ${label}${detail ? ' — ' + detail : ''}`); fail += 1; }
}

console.log('== Task 1: token resolution ==');
{
  const { getToken } = await import('./lib/github.mjs');
  process.env.GITHUB_TOKEN = '  env-token  ';
  ok('env var wins and is trimmed', getToken() === 'env-token');

  delete process.env.GITHUB_TOKEN;
  let fellBack = null;
  try { fellBack = getToken(); } catch { fellBack = null; }
  ok('falls back to gh auth token when env is unset',
     typeof fellBack === 'string' && fellBack.length > 20,
     fellBack ? `${fellBack.length} chars` : 'gh unavailable — install gh or run gh auth login');
}

console.log('\n== Task 2: classify-core ==');
{
  const core = await import('./lib/classify-core.mjs');
  const NOW = Date.parse('2026-08-28T00:00:00Z');

  ok('daysAgo is pinned by now', Math.round(core.daysAgo('2026-08-18T00:00:00Z', NOW)) === 10);
  ok('daysAgo of null is Infinity', core.daysAgo(null, NOW) === Infinity);

  const bf = core.busFactor([{ login: 'a', commits: 8 }, { login: 'b', commits: 2 }]);
  ok('busFactor covers 50% with one author', bf.count === 1, `count=${bf.count}`);
  ok('busFactor top_share is 0.8', Math.abs(bf.top_share - 0.8) < 1e-9);

  const archived = { archived: true, created_at: '2020-01-01T00:00:00Z', pushed_at: '2026-08-27T00:00:00Z' };
  ok('archived is Abandoned', core.lifecycleStage(archived, NOW) === 'Abandoned');

  const hot = {
    archived: false,
    created_at: '2025-06-01T00:00:00Z',
    pushed_at: '2026-08-27T00:00:00Z',
    commits_90d: 120,
    unique_authors_90d: 7,
  };
  ok('young + busy + multi-author is Hot', core.lifecycleStage(hot, NOW) === 'Hot');

  const enriched = core.classifyRepo({ ...hot, stars: 900, authors_90d: [{ login: 'a', commits: 120 }] }, NOW);
  ok('classifyRepo adds the dataset fields',
     typeof enriched.health_score === 'number'
     && typeof enriched.lifecycle_stage === 'string'
     && typeof enriched.days_since_push === 'number'
     && typeof enriched.bus_factor === 'number');
  ok('health_score is 0-100', enriched.health_score >= 0 && enriched.health_score <= 100,
     `${enriched.health_score}`);
}

console.log('\n== Task 3: landscape ==');
{
  const { coveredRepos, vocabulary, loadLandscape } = await import('./lib/discover/landscape.mjs');

  const md = 'see [tmux](https://github.com/tmux/tmux) and https://github.com/TMUX/tmux'
    + ' and https://github.com/sponsors/someone and https://github.com/foo/bar.git';
  const cov = coveredRepos(md);
  ok('dedupes case variants', cov.size === 2, `${[...cov.values()].join(', ')}`);
  ok('drops non-repo owner paths', ![...cov.keys()].some((k) => k.startsWith('sponsors/')));
  ok('strips a .git suffix', cov.has('foo/bar'));

  const vocab = vocabulary({ title: 'Terminals for Agentic Programming', categories: { 'Terminal emulator': 2, 'Agent runtime / multiplexer': 3 } });
  ok('vocabulary lowercases and splits categories', vocab.includes('terminal') && vocab.includes('multiplexer'));
  ok('vocabulary drops stopwords', !vocab.includes('for') && !vocab.includes('and'));

  const ls = loadLandscape('agentic-terminals');
  // 59 comes from the report markdown and is stable until the report is rewritten.
  // The held/gap split moves as repos get starred, so assert the invariant and
  // print the current vintage rather than pinning yesterday's numbers.
  ok('agentic-terminals links 59 repos', ls.covered.size === 59, `${ls.covered.size}`);
  ok('held + gaps accounts for every covered repo',
     ls.held.length + ls.knownGaps.length === ls.covered.size,
     `${ls.held.length} held + ${ls.knownGaps.length} gaps = ${ls.covered.size}`);
  ok('the two sets are disjoint',
     !ls.held.some((h) => ls.knownGaps.includes(h)));
  ok('every known gap is genuinely unstarred',
     ls.knownGaps.every((g) => !ls.starred.has(g.toLowerCase())));
  ok('every held repo is genuinely starred',
     ls.held.every((h) => ls.starred.has(h.toLowerCase())));
  ok('a held repo is not a gap', !ls.knownGaps.includes('tmux/tmux'));

  const cs = loadLandscape('charting-stack');
  ok('charting-stack links 61 repos', cs.covered.size === 61, `${cs.covered.size}`);
}

console.log('\n== Task 4: scoring ==');
{
  const { classifyKind, standing, recency, fitScore } = await import('./lib/discover/score.mjs');

  ok('awesome list with low churn is a list',
     classifyKind({ full_name: 'rothgar/awesome-tuis', description: 'List of projects that provide terminal user interfaces', commits_90d: 2 }) === 'list');
  ok('an active tool is a tool',
     classifyKind({ full_name: 'tmux/tmux', description: 'tmux source code', commits_90d: 90 }) === 'tool');
  ok('a course is a tutorial',
     classifyKind({ full_name: 'x/llm-course', description: 'Course to get into Large Language Models', commits_90d: 5 }) === 'tutorial');
  ok('a busy repo named awesome-* is still a tool',
     classifyKind({ full_name: 'x/awesome-engine', description: 'awesome rendering engine', commits_90d: 400 }) === 'tool');

  ok('standing is monotonic in stars', standing(50000) > standing(3000) && standing(3000) > standing(100));
  ok('standing is capped at 1', standing(5000000) <= 1);
  ok('recency is 1 for a fresh push', recency(5) === 1);
  ok('recency is 0 past a year', recency(400) === 0);
  ok('recency decays in between', recency(200) > 0 && recency(200) < 1);

  const base = { full_name: 'a/b', description: 'terminal multiplexer', topics: ['terminal'], stars: 5000, health_score: 70, days_since_push: 10, commits_90d: 50 };
  const vocab = ['terminal', 'multiplexer', 'agent'];
  const asNew = fitScore({ ...base, kind: 'tool' }, vocab, { state: 'new' });
  const asGap = fitScore({ ...base, kind: 'tool' }, vocab, { state: 'known-gap' });
  ok('known-gap outranks an identical new repo', asGap.total > asNew.total, `${asGap.total} > ${asNew.total}`);
  ok('score exposes its components',
     ['relevance', 'standing', 'health', 'recency'].every((k) => typeof asNew.parts[k] === 'number'));
  ok('total stays within 0-100', asGap.total <= 100 && asNew.total >= 0);

  const asList = fitScore({ ...base, kind: 'list' }, vocab, { state: 'new' });
  ok('a list ranks below an identical tool', asList.total < asNew.total, `${asList.total} < ${asNew.total}`);

  const offTopic = fitScore({ ...base, kind: 'tool', description: 'json parser', topics: [] }, vocab, { state: 'new' });
  ok('off-theme scores lower than on-theme', offTopic.total < asNew.total);
}

console.log('\n== Task 5: candidate generation ==');
{
  const { parseExtra, buildQueries } = await import('./lib/discover/candidates.mjs');

  ok('parses a comma list', JSON.stringify(parseExtra('a/b, c/d')) === JSON.stringify(['a/b', 'c/d']));
  ok('strips a github url', parseExtra('https://github.com/a/b')[0] === 'a/b');
  ok('strips a trailing .git and slash', parseExtra('a/b.git, c/d/')[0] === 'a/b' && parseExtra('a/b.git, c/d/')[1] === 'c/d');
  ok('dedupes case-insensitively', parseExtra('A/B, a/b').length === 1);
  ok('drops malformed entries', parseExtra('a/b, nope, /x, y/').length === 1);
  ok('empty input is an empty list', parseExtra(undefined).length === 0);

  const ls = {
    meta: { title: 'Terminals for Agentic Programming', categories: { 'Terminal emulator': 2, 'Agent runtime / multiplexer': 3 } },
    vocabulary: ['terminal', 'emulator', 'agent', 'runtime', 'multiplexer'],
  };
  const qs = buildQueries(ls, { minStars: 200, maxStaleDays: 365, now: Date.parse('2026-08-28T00:00:00Z') });
  ok('builds at least one query per category', qs.length >= 2, `${qs.length} queries`);
  ok('every query filters forks and archives', qs.every((q) => q.q.includes('fork:false') && q.q.includes('archived:false')));
  ok('every query carries the star floor', qs.every((q) => q.q.includes('stars:>=200')));
  ok('every query carries a pushed floor', qs.every((q) => /pushed:>=\d{4}-\d{2}-\d{2}/.test(q.q)));
  ok('pushed floor is maxStaleDays back', qs[0].q.includes('pushed:>=2025-08-28'));
  ok('queries are labelled', qs.every((q) => typeof q.label === 'string' && q.label.length > 0));
}

console.log('\n== Task 6: fetch (network) ==');
{
  const { projectCandidate, resolveRepos, searchRepos } = await import('./lib/discover/fetch.mjs');

  const node = {
    nameWithOwner: 'a/b', description: 'd', createdAt: '2024-01-01T00:00:00Z',
    pushedAt: '2026-08-01T00:00:00Z', stargazerCount: 12, forkCount: 3,
    isArchived: false, isFork: false, isMirror: false,
    primaryLanguage: { name: 'Rust' }, licenseInfo: { spdxId: 'MIT' },
    repositoryTopics: { nodes: [{ topic: { name: 'cli' } }] },
    defaultBranchRef: { target: { historySince: { totalCount: 7, nodes: [{ author: { user: { login: 'u' } } }] } } },
    releases: { totalCount: 1, nodes: [{ tagName: 'v1', publishedAt: '2026-07-01T00:00:00Z' }] },
    issues: { totalCount: 2 }, closedIssues: { totalCount: 8 },
  };
  const p = projectCandidate(node);
  ok('projectCandidate maps to dataset field names',
     p.full_name === 'a/b' && p.stars === 12 && p.commits_90d === 7
     && p.license === 'MIT' && p.topics[0] === 'cli' && p.unique_authors_90d === 1);

  let token = true;
  try { (await import('./lib/github.mjs')).getToken(); } catch { token = false; }
  if (!token) {
    console.log('  … skipped: no GitHub token available');
  } else {
    const r = await resolveRepos(['tmux/tmux', 'pvolok/mprocs', 'this-owner-does-not-exist-xyz/nope']);
    ok('resolves a live repo', r.resolved.some((x) => x.full_name === 'tmux/tmux'));
    ok('reports an unresolvable name', r.unresolved.includes('this-owner-does-not-exist-xyz/nope'));
    ok('detects a rename', r.renamed.some((x) => x.from === 'pvolok/mprocs' && x.to !== 'pvolok/mprocs'),
       JSON.stringify(r.renamed));
    ok('resolved rows carry health fields',
       r.resolved.length > 0
       && r.resolved.every((x) => typeof x.health_score === 'number' && typeof x.lifecycle_stage === 'string'),
       `${r.resolved.length} resolved`);

    const found = await searchRepos([{ label: 'test', q: 'terminal multiplexer fork:false archived:false stars:>=5000' }], { perQuery: 5 });
    ok('search returns candidates', found.length > 0, `${found.length}`);
    ok('search rows carry their origin', found.every((x) => typeof x.via === 'string'));
  }
}

console.log('\n== Task 7: render ==');
{
  const { renderMarkdown } = await import('./lib/discover/render.mjs');
  const md = renderMarkdown({
    slug: 'demo',
    generated: '2026-08-28',
    heldCount: 14,
    candidates: [
      { full_name: 'a/b', state: 'known-gap', kind: 'tool', stars: 1200, license: 'MIT',
        primary_language: 'Rust', lifecycle_stage: 'Hot', health_score: 71, days_since_push: 3,
        bus_factor: 3, description: 'a thing', score: { total: 88, parts: { relevance: 1, standing: 0.6, health: 0.71, recency: 1 }, kind_multiplier: 1 } },
    ],
    renamed: [{ from: 'x/old', to: 'x/new' }],
    unresolved: ['q/nope'],
  });
  ok('markdown names the report', md.includes('demo'));
  ok('markdown shows the candidate', md.includes('a/b'));
  ok('markdown shows the state', md.includes('known-gap'));
  ok('markdown surfaces renames', md.includes('x/old') && md.includes('x/new'));
  ok('markdown surfaces unresolved names', md.includes('q/nope'));
  ok('markdown escapes table pipes', !md.split('\n').some((l) => l.startsWith('|') && l.split('|').length > 16));
}

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail > 0 ? 1 : 0);
