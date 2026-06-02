# Graph Report - github-stars-analyzer  (2026-06-02)

## Corpus Check
- 33 files · ~71,306 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 139 nodes · 140 edges · 10 communities detected
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.8)
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
- [[_COMMUNITY_Community 13|Community 13]]

## God Nodes (most connected - your core abstractions)
1. `useGraph()` - 10 edges
2. `handler()` - 8 edges
3. `daysAgo()` - 4 edges
4. `fetchAllStarred()` - 3 edges
5. `authHeader()` - 3 edges
6. `rest()` - 3 edges
7. `comp_table()` - 3 edges
8. `RepoDetail()` - 3 edges
9. `fmt()` - 3 edges
10. `clientIp()` - 2 edges

## Surprising Connections (you probably didn't know these)
- `handler()` --calls--> `buildSystemPrompt()`  [INFERRED]
  netlify/functions/ask.mjs → scripts/lib/ask-prompt.mjs
- `Comparator()` --calls--> `useGraph()`  [INFERRED]
  src/lab/Comparator.jsx → src/lab/GraphProvider.jsx
- `InsightFeed()` --calls--> `useGraph()`  [INFERRED]
  src/lab/InsightFeed.jsx → src/lab/GraphProvider.jsx
- `TopicMap()` --calls--> `useGraph()`  [INFERRED]
  src/lab/TopicMap.jsx → src/lab/GraphProvider.jsx
- `MapView()` --calls--> `useGraph()`  [INFERRED]
  src/lab/MapView.jsx → src/lab/GraphProvider.jsx

## Communities

### Community 0 - "Community 0"
Cohesion: 0.09
Nodes (7): AllRepos(), useGraph(), HealthHistogram(), AskView(), StatusBanner(), MapView(), TopicMap()

### Community 1 - "Community 1"
Cohesion: 0.22
Nodes (8): clientIp(), extractErrorMessage(), getContext(), handler(), jsonResponse(), rateCheck(), streamCompletion(), buildSystemPrompt()

### Community 2 - "Community 2"
Cohesion: 0.22
Nodes (7): authHeader(), graphql(), logRate(), rest(), pickReadme(), projectRepo(), fetchAllStarred()

### Community 3 - "Community 3"
Cohesion: 0.2
Nodes (2): best_in(), ok()

### Community 4 - "Community 4"
Cohesion: 0.22
Nodes (2): Return ('A'|'B'|'=') for which repo wins a metric., winner()

### Community 5 - "Community 5"
Cohesion: 0.25
Nodes (4): Comparator(), MetricRow(), fmt(), ReportCard()

### Community 6 - "Community 6"
Cohesion: 0.38
Nodes (3): activity_label(), comp_table(), fmt_int()

### Community 7 - "Community 7"
Cohesion: 0.53
Nodes (4): daysAgo(), healthScore(), lifecycleStage(), momentum()

### Community 8 - "Community 8"
Cohesion: 0.4
Nodes (2): findNeighbors(), RepoDetail()

### Community 13 - "Community 13"
Cohesion: 0.4
Nodes (1): InsightFeed()

## Knowledge Gaps
- **1 isolated node(s):** `Return ('A'|'B'|'=') for which repo wins a metric.`
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 3`** (10 nodes): `activity_label()`, `best_in()`, `days_to_human()`, `fmt_int()`, `node_for()`, `openclaw_ecosystem.py`, `jaccard()`, `keyFor()`, `test-graph.mjs`, `ok()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 4`** (9 nodes): `activity_label()`, `days_to_human()`, `fmt_int()`, `mom()`, `node_for()`, `Return ('A'|'B'|'=') for which repo wins a metric.`, `row()`, `winner()`, `hermes_vs_openclaw.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 8`** (6 nodes): `findNeighbors()`, `HealthBar()`, `MetricCell()`, `RepoDetail()`, `StageBadge()`, `RepoDetail.jsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (5 nodes): `downloadBlob()`, `InsightFeed()`, `ResultTable()`, `rowsToCsv()`, `InsightFeed.jsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `useGraph()` connect `Community 0` to `Community 8`, `Community 13`, `Community 5`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Why does `Comparator()` connect `Community 5` to `Community 0`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `useGraph()` (e.g. with `TopicMap()` and `MapView()`) actually correct?**
  _`useGraph()` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `fetchAllStarred()` (e.g. with `rest()` and `logRate()`) actually correct?**
  _`fetchAllStarred()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Return ('A'|'B'|'=') for which repo wins a metric.` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.09 - nodes in this community are weakly interconnected._