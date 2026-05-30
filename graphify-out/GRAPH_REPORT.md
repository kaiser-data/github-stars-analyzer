# Graph Report - github-stars-analyzer  (2026-05-30)

## Corpus Check
- 24 files · ~20,812 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 88 nodes · 93 edges · 7 communities detected
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 12 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]

## God Nodes (most connected - your core abstractions)
1. `useGraph()` - 10 edges
2. `handler()` - 8 edges
3. `daysAgo()` - 4 edges
4. `fetchAllStarred()` - 3 edges
5. `authHeader()` - 3 edges
6. `rest()` - 3 edges
7. `RepoDetail()` - 3 edges
8. `clientIp()` - 2 edges
9. `rateCheck()` - 2 edges
10. `getContext()` - 2 edges

## Surprising Connections (you probably didn't know these)
- `handler()` --calls--> `buildSystemPrompt()`  [INFERRED]
  netlify/functions/ask.mjs → scripts/lib/ask-prompt.mjs
- `TopicMap()` --calls--> `useGraph()`  [INFERRED]
  src/lab/TopicMap.jsx → src/lab/GraphProvider.jsx
- `InsightFeed()` --calls--> `useGraph()`  [INFERRED]
  src/lab/InsightFeed.jsx → src/lab/GraphProvider.jsx
- `MapView()` --calls--> `useGraph()`  [INFERRED]
  src/lab/MapView.jsx → src/lab/GraphProvider.jsx
- `RepoDetail()` --calls--> `useGraph()`  [INFERRED]
  src/lab/RepoDetail.jsx → src/lab/GraphProvider.jsx

## Communities

### Community 0 - "Community 0"
Cohesion: 0.11
Nodes (7): AllRepos(), Comparator(), useGraph(), HealthHistogram(), AskView(), StatusBanner(), MapView()

### Community 1 - "Community 1"
Cohesion: 0.22
Nodes (8): clientIp(), extractErrorMessage(), getContext(), handler(), jsonResponse(), rateCheck(), streamCompletion(), buildSystemPrompt()

### Community 2 - "Community 2"
Cohesion: 0.22
Nodes (7): authHeader(), graphql(), logRate(), rest(), pickReadme(), projectRepo(), fetchAllStarred()

### Community 3 - "Community 3"
Cohesion: 0.53
Nodes (4): daysAgo(), healthScore(), lifecycleStage(), momentum()

### Community 4 - "Community 4"
Cohesion: 0.33
Nodes (1): TopicMap()

### Community 5 - "Community 5"
Cohesion: 0.4
Nodes (2): findNeighbors(), RepoDetail()

### Community 6 - "Community 6"
Cohesion: 0.4
Nodes (1): InsightFeed()

## Knowledge Gaps
- **Thin community `Community 4`** (6 nodes): `buildTopicGraph()`, `ControlPanel()`, `ReposByTopic()`, `topicGraphToFG()`, `TopicMap()`, `TopicMap.jsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 5`** (6 nodes): `findNeighbors()`, `HealthBar()`, `MetricCell()`, `RepoDetail()`, `StageBadge()`, `RepoDetail.jsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 6`** (5 nodes): `downloadBlob()`, `InsightFeed()`, `ResultTable()`, `rowsToCsv()`, `InsightFeed.jsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `useGraph()` connect `Community 0` to `Community 4`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.151) - this node is a cross-community bridge._
- **Why does `TopicMap()` connect `Community 4` to `Community 0`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Why does `RepoDetail()` connect `Community 5` to `Community 0`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `useGraph()` (e.g. with `TopicMap()` and `MapView()`) actually correct?**
  _`useGraph()` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `fetchAllStarred()` (e.g. with `rest()` and `logRate()`) actually correct?**
  _`fetchAllStarred()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.11 - nodes in this community are weakly interconnected._