# Graph Report - github-stars-analyzer  (2026-05-31)

## Corpus Check
- 31 files · ~59,712 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 123 nodes · 124 edges · 9 communities detected
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.8)
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
- [[_COMMUNITY_Community 12|Community 12]]

## God Nodes (most connected - your core abstractions)
1. `useGraph()` - 10 edges
2. `handler()` - 8 edges
3. `daysAgo()` - 4 edges
4. `fetchAllStarred()` - 3 edges
5. `authHeader()` - 3 edges
6. `rest()` - 3 edges
7. `RepoDetail()` - 3 edges
8. `fmt()` - 3 edges
9. `clientIp()` - 2 edges
10. `rateCheck()` - 2 edges

## Surprising Connections (you probably didn't know these)
- `handler()` --calls--> `buildSystemPrompt()`  [INFERRED]
  netlify/functions/ask.mjs → scripts/lib/ask-prompt.mjs
- `TopicMap()` --calls--> `useGraph()`  [INFERRED]
  src/lab/TopicMap.jsx → src/lab/GraphProvider.jsx
- `Comparator()` --calls--> `useGraph()`  [INFERRED]
  src/lab/Comparator.jsx → src/lab/GraphProvider.jsx
- `InsightFeed()` --calls--> `useGraph()`  [INFERRED]
  src/lab/InsightFeed.jsx → src/lab/GraphProvider.jsx
- `MapView()` --calls--> `useGraph()`  [INFERRED]
  src/lab/MapView.jsx → src/lab/GraphProvider.jsx

## Communities

### Community 0 - "Community 0"
Cohesion: 0.12
Nodes (6): AllRepos(), useGraph(), HealthHistogram(), AskView(), StatusBanner(), MapView()

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
Cohesion: 0.25
Nodes (4): Comparator(), MetricRow(), fmt(), ReportCard()

### Community 5 - "Community 5"
Cohesion: 0.53
Nodes (4): daysAgo(), healthScore(), lifecycleStage(), momentum()

### Community 6 - "Community 6"
Cohesion: 0.33
Nodes (1): TopicMap()

### Community 7 - "Community 7"
Cohesion: 0.4
Nodes (2): findNeighbors(), RepoDetail()

### Community 12 - "Community 12"
Cohesion: 0.4
Nodes (1): InsightFeed()

## Knowledge Gaps
- **Thin community `Community 3`** (10 nodes): `activity_label()`, `best_in()`, `days_to_human()`, `fmt_int()`, `node_for()`, `openclaw_ecosystem.py`, `jaccard()`, `keyFor()`, `test-graph.mjs`, `ok()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 6`** (6 nodes): `buildTopicGraph()`, `ControlPanel()`, `ReposByTopic()`, `topicGraphToFG()`, `TopicMap()`, `TopicMap.jsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 7`** (6 nodes): `findNeighbors()`, `HealthBar()`, `MetricCell()`, `RepoDetail()`, `StageBadge()`, `RepoDetail.jsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 12`** (5 nodes): `downloadBlob()`, `InsightFeed()`, `ResultTable()`, `rowsToCsv()`, `InsightFeed.jsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `useGraph()` connect `Community 0` to `Community 4`, `Community 12`, `Community 6`, `Community 7`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._
- **Why does `Comparator()` connect `Community 4` to `Community 0`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **Why does `TopicMap()` connect `Community 6` to `Community 0`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `useGraph()` (e.g. with `TopicMap()` and `MapView()`) actually correct?**
  _`useGraph()` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `fetchAllStarred()` (e.g. with `rest()` and `logRate()`) actually correct?**
  _`fetchAllStarred()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.12 - nodes in this community are weakly interconnected._