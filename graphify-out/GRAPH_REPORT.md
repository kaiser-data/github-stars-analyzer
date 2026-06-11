# Graph Report - github-stars-analyzer  (2026-06-12)

## Corpus Check
- 39 files · ~124,217 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 179 nodes · 184 edges · 12 communities detected
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]

## God Nodes (most connected - your core abstractions)
1. `useGraph()` - 10 edges
2. `handler()` - 8 edges
3. `daysAgo()` - 4 edges
4. `staleness_factor()` - 4 edges
5. `score_components()` - 4 edges
6. `fetchAllStarred()` - 3 edges
7. `authHeader()` - 3 edges
8. `rest()` - 3 edges
9. `mom()` - 3 edges
10. `composite()` - 3 edges

## Surprising Connections (you probably didn't know these)
- `handler()` --calls--> `buildSystemPrompt()`  [INFERRED]
  netlify/functions/ask.mjs → scripts/lib/ask-prompt.mjs
- `Comparator()` --calls--> `useGraph()`  [INFERRED]
  src/lab/Comparator.jsx → src/lab/GraphProvider.jsx
- `TopicMap()` --calls--> `useGraph()`  [INFERRED]
  src/lab/TopicMap.jsx → src/lab/GraphProvider.jsx
- `MapView()` --calls--> `useGraph()`  [INFERRED]
  src/lab/MapView.jsx → src/lab/GraphProvider.jsx
- `RepoDetail()` --calls--> `useGraph()`  [INFERRED]
  src/lab/RepoDetail.jsx → src/lab/GraphProvider.jsx

## Communities

### Community 0 - "Community 0"
Cohesion: 0.07
Nodes (8): AllRepos(), useGraph(), HealthHistogram(), InsightFeed(), AskView(), StatusBanner(), MapView(), TopicMap()

### Community 1 - "Community 1"
Cohesion: 0.19
Nodes (10): composite(), dominated_by(), mean_rank(), mom(), pvec(), rank_of(), Multiplicative gate: 1.0 up to 60d since push, decaying to a 0.6 floor.     Fres, score_components() (+2 more)

### Community 2 - "Community 2"
Cohesion: 0.22
Nodes (8): clientIp(), extractErrorMessage(), getContext(), handler(), jsonResponse(), rateCheck(), streamCompletion(), buildSystemPrompt()

### Community 3 - "Community 3"
Cohesion: 0.22
Nodes (7): authHeader(), graphql(), logRate(), rest(), pickReadme(), projectRepo(), fetchAllStarred()

### Community 4 - "Community 4"
Cohesion: 0.2
Nodes (2): best_in(), ok()

### Community 5 - "Community 5"
Cohesion: 0.22
Nodes (2): Return ('A'|'B'|'=') for which repo wins a metric., winner()

### Community 6 - "Community 6"
Cohesion: 0.25
Nodes (4): Comparator(), MetricRow(), fmt(), ReportCard()

### Community 7 - "Community 7"
Cohesion: 0.38
Nodes (3): activity_label(), comp_table(), fmt_int()

### Community 8 - "Community 8"
Cohesion: 0.53
Nodes (4): daysAgo(), healthScore(), lifecycleStage(), momentum()

### Community 9 - "Community 9"
Cohesion: 0.4
Nodes (2): findNeighbors(), RepoDetail()

### Community 17 - "Community 17"
Cohesion: 0.5
Nodes (2): hotness(), mom()

### Community 18 - "Community 18"
Cohesion: 0.67
Nodes (2): fmt_int(), meta_bits()

## Knowledge Gaps
- **2 isolated node(s):** `Return ('A'|'B'|'=') for which repo wins a metric.`, `Multiplicative gate: 1.0 up to 60d since push, decaying to a 0.6 floor.     Fres`
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 4`** (10 nodes): `activity_label()`, `best_in()`, `days_to_human()`, `fmt_int()`, `node_for()`, `openclaw_ecosystem.py`, `jaccard()`, `keyFor()`, `test-graph.mjs`, `ok()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 5`** (9 nodes): `activity_label()`, `days_to_human()`, `fmt_int()`, `mom()`, `node_for()`, `Return ('A'|'B'|'=') for which repo wins a metric.`, `row()`, `winner()`, `hermes_vs_openclaw.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 9`** (6 nodes): `findNeighbors()`, `HealthBar()`, `MetricCell()`, `RepoDetail()`, `StageBadge()`, `RepoDetail.jsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 17`** (5 nodes): `fmt_int()`, `hotness()`, `life_badge()`, `mom()`, `blockchain_essentials.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 18`** (4 nodes): `fmt_int()`, `meta_bits()`, `yn()`, `blockchain_claws.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `useGraph()` connect `Community 0` to `Community 9`, `Community 6`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Why does `Comparator()` connect `Community 6` to `Community 0`?**
  _High betweenness centrality (0.017) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `useGraph()` (e.g. with `TopicMap()` and `MapView()`) actually correct?**
  _`useGraph()` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Return ('A'|'B'|'=') for which repo wins a metric.`, `Multiplicative gate: 1.0 up to 60d since push, decaying to a 0.6 floor.     Fres` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.07 - nodes in this community are weakly interconnected._