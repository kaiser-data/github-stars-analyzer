# Graph Report - github-stars-analyzer  (2026-06-29)

## Corpus Check
- 105 files · ~1,951,608 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 901 nodes · 1009 edges · 65 communities (60 shown, 5 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 13 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `429983b7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

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
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]
- [[_COMMUNITY_Community 59|Community 59]]
- [[_COMMUNITY_Community 62|Community 62]]
- [[_COMMUNITY_Community 63|Community 63]]
- [[_COMMUNITY_Community 64|Community 64]]

## God Nodes (most connected - your core abstractions)
1. `useGraph()` - 19 edges
2. `The field guide, by layer` - 15 edges
3. `The field guide, by layer` - 15 edges
4. `scripts` - 13 edges
5. `The AI Engineer's Stack — What's Fundamental, Must-Have, and Trending` - 11 edges
6. `Claude Code Superpowers — Setup Strategies from Your Stars` - 11 edges
7. `By category` - 11 edges
8. `Meeting Transcription & Conversation Analysis — Field Guide` - 11 edges
9. `RAG (Retrieval-Augmented Generation) Tooling — Landscape Report` - 11 edges
10. `Voice AI Agents — Landscape Report` - 11 edges

## Surprising Connections (you probably didn't know these)
- `handler()` --calls--> `buildSystemPrompt()`  [INFERRED]
  netlify/functions/ask.mjs → scripts/lib/ask-prompt.mjs
- `MetricRow()` --calls--> `fmt()`  [INFERRED]
  src/lab/Comparator.jsx → src/lab/ReportsView.jsx
- `fetchAllStarred()` --calls--> `rest()`  [INFERRED]
  scripts/sample.mjs → scripts/lib/github.mjs
- `fetchAllStarred()` --calls--> `logRate()`  [INFERRED]
  scripts/sample.mjs → scripts/lib/github.mjs
- `AllRepos()` --calls--> `useGraph()`  [INFERRED]
  src/lab/AllRepos.jsx → src/lab/GraphProvider.jsx

## Import Cycles
- None detected.

## Communities (65 total, 5 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (42): ALL_STAGES, AllRepos(), Comparator(), findPath(), MetricRow(), GraphContext, GraphProvider(), STAGE_COLOR (+34 more)

### Community 1 - "Community 1"
Cohesion: 0.27
Nodes (15): activity_label(), composite(), days_to_human(), dominated_by(), fmt_int(), mean_rank(), mom(), node_for() (+7 more)

### Community 2 - "Community 2"
Cohesion: 0.10
Nodes (27): clientIp(), config, extractErrorMessage(), getContext(), handler(), jsonResponse(), LLM_BASE_URL, PROVIDER (+19 more)

### Community 3 - "Community 3"
Cohesion: 0.12
Nodes (23): authHeader(), getToken(), graphql(), logRate(), rest(), sleep(), args, failures (+15 more)

### Community 4 - "Community 4"
Cohesion: 0.48
Nodes (5): activity_label(), best_in(), days_to_human(), fmt_int(), node_for()

### Community 5 - "Community 5"
Cohesion: 0.33
Nodes (8): activity_label(), days_to_human(), fmt_int(), mom(), node_for(), Return ('A'|'B'|'=') for which repo wins a metric., row(), winner()

### Community 6 - "Community 6"
Cohesion: 0.48
Nodes (5): fmt(), MD_COMPONENTS, ReportCard(), ReportReader(), ReportsView()

### Community 7 - "Community 7"
Cohesion: 0.50
Nodes (6): activity_label(), approach_of(), comp_table(), days_to_human(), fmt_int(), node_for()

### Community 8 - "Community 8"
Cohesion: 0.22
Nodes (12): args, busFactor(), classified, data, daysAgo(), dist, healthScore(), inArg (+4 more)

### Community 9 - "Community 9"
Cohesion: 0.05
Nodes (38): dependencies, dexie, graphology, graphology-communities-louvain, graphology-metrics, graphology-shortest-path, lucide-react, react (+30 more)

### Community 10 - "Community 10"
Cohesion: 0.53
Nodes (4): activity_label(), days_to_human(), fmt_int(), node_for()

### Community 11 - "Community 11"
Cohesion: 0.53
Nodes (4): activity_label(), days_to_human(), fmt_int(), node_for()

### Community 12 - "Community 12"
Cohesion: 0.53
Nodes (4): activity_label(), days_to_human(), fmt_int(), node_for()

### Community 13 - "Community 13"
Cohesion: 0.53
Nodes (4): activity_label(), days_to_human(), fmt_int(), node_for()

### Community 14 - "Community 14"
Cohesion: 0.53
Nodes (4): activity_label(), days_to_human(), fmt_int(), node_for()

### Community 15 - "Community 15"
Cohesion: 0.53
Nodes (4): activity_label(), days_to_human(), fmt_int(), node_for()

### Community 16 - "Community 16"
Cohesion: 0.53
Nodes (4): activity_label(), days_to_human(), fmt_int(), node_for()

### Community 17 - "Community 17"
Cohesion: 0.60
Nodes (4): fmt_int(), hotness(), life_badge(), mom()

### Community 18 - "Community 18"
Cohesion: 0.70
Nodes (3): fmt_int(), meta_bits(), yn()

### Community 21 - "Community 21"
Cohesion: 0.08
Nodes (23): Agent OS / long-horizon harness, Agent OS / long-horizon harness, AI Agent Orchestration — Landscape Report, Code-first agent frameworks, Code-first agent frameworks, Coding-agent orchestration, Coding-agent orchestration, Comparison by approach (+15 more)

### Community 22 - "Community 22"
Cohesion: 0.06
Nodes (31): authorSets, classified, communities, COMMUNITY_PALETTE, communityContext, communityMeta, __dirname, fgLinks (+23 more)

### Community 27 - "Community 27"
Cohesion: 0.08
Nodes (23): Agent OS / long-horizon harness, Agent OS / long-horizon harness, AI Agent Orchestration — Landscape Report, Code-first agent frameworks, Code-first agent frameworks, Coding-agent orchestration, Coding-agent orchestration, Comparison by approach (+15 more)

### Community 28 - "Community 28"
Cohesion: 0.10
Nodes (20): Adjacent (deliberately not listed here), By layer, Claude Code Superpowers — Setup Strategies from Your Stars, Code-graph / retrieval, Config / setup kit, Executive summary, Graph analysis — how they relate, Harness / coding agent (+12 more)

### Community 29 - "Community 29"
Cohesion: 0.10
Nodes (20): By category, Client / host, Executive summary, Gateway / control plane, Graph analysis — how they relate, Learning / reference, Maintenance & risk signal, Master comparison (+12 more)

### Community 30 - "Community 30"
Cohesion: 0.10
Nodes (20): Adjacent (deliberately not listed here), By layer, Claude Code Superpowers — Setup Strategies from Your Stars, Code-graph / retrieval, Config / setup kit, Executive summary, Graph analysis — how they relate, Harness / coding agent (+12 more)

### Community 31 - "Community 31"
Cohesion: 0.10
Nodes (20): By category, Client / host, Executive summary, Gateway / control plane, Graph analysis — how they relate, Learning / reference, Maintenance & risk signal, Master comparison (+12 more)

### Community 32 - "Community 32"
Cohesion: 0.10
Nodes (19): 🔥 Agentic payments (x402), 🔥 AI × finance / trading, Blockchain Repos You Need to Know — A Field Guide, Caveats, Client libraries (TS/JS), Contract libraries & standards, DeFi protocol references, Dev toolkits (+11 more)

### Community 33 - "Community 33"
Cohesion: 0.10
Nodes (19): 🔥 Agentic payments (x402), 🔥 AI × finance / trading, Blockchain Repos You Need to Know — A Field Guide, Caveats, Client libraries (TS/JS), Contract libraries & standards, DeFi protocol references, Dev toolkits (+11 more)

### Community 34 - "Community 34"
Cohesion: 0.11
Nodes (17): Adjacent (covered elsewhere), Agent framework, Executive summary, Fine-tuning, Graph analysis — how the stack hangs together, Inference runtime, Local vs High-Infra AI Stack — A Deployment-Tier Comparison, Maintenance & risk signal (+9 more)

### Community 35 - "Community 35"
Cohesion: 0.11
Nodes (17): Adjacent (deliberately not listed here), ASR engine / model, By category, Diarization & alignment, Executive summary, Graph analysis — how they relate, Maintenance & risk signal, Master comparison (+9 more)

### Community 36 - "Community 36"
Cohesion: 0.11
Nodes (17): Adjacent (deliberately not listed as voice-AI tools), By category, Executive summary, Graph analysis — how they relate, Maintenance & risk signal, Master comparison, Methodology & caveats, Realtime voice-agent framework (+9 more)

### Community 37 - "Community 37"
Cohesion: 0.11
Nodes (17): Adjacent (covered elsewhere), Agent framework, Executive summary, Fine-tuning, Graph analysis — how the stack hangs together, Inference runtime, Local vs High-Infra AI Stack — A Deployment-Tier Comparison, Maintenance & risk signal (+9 more)

### Community 38 - "Community 38"
Cohesion: 0.11
Nodes (17): Adjacent (deliberately not listed here), ASR engine / model, By category, Diarization & alignment, Executive summary, Graph analysis — how they relate, Maintenance & risk signal, Master comparison (+9 more)

### Community 39 - "Community 39"
Cohesion: 0.11
Nodes (17): Adjacent (deliberately not listed as voice-AI tools), By category, Executive summary, Graph analysis — how they relate, Maintenance & risk signal, Master comparison, Methodology & caveats, Realtime voice-agent framework (+9 more)

### Community 40 - "Community 40"
Cohesion: 0.12
Nodes (16): ⚠️ Adopt with caution, Alternative agent / OS, By category, Core, Desktop / orchestration, Graph analysis — how they relate, Hosting / secure runtime, Master comparison (+8 more)

### Community 41 - "Community 41"
Cohesion: 0.12
Nodes (16): Adjacent (deliberately not listed as RAG tools), By category, Embeddings / rerankers, Executive summary, Graph analysis — how they relate, Ingestion / parsing / chunking, Maintenance & risk signal, Master comparison (+8 more)

### Community 42 - "Community 42"
Cohesion: 0.12
Nodes (16): ⚠️ Adopt with caution, Alternative agent / OS, By category, Core, Desktop / orchestration, Graph analysis — how they relate, Hosting / secure runtime, Master comparison (+8 more)

### Community 43 - "Community 43"
Cohesion: 0.12
Nodes (16): Adjacent (deliberately not listed as RAG tools), By category, Embeddings / rerankers, Executive summary, Graph analysis — how they relate, Ingestion / parsing / chunking, Maintenance & risk signal, Master comparison (+8 more)

### Community 44 - "Community 44"
Cohesion: 0.13
Nodes (15): abandoned, added, authorSets, classic, data, g, hot, jaccard() (+7 more)

### Community 45 - "Community 45"
Cohesion: 0.13
Nodes (14): Benchmark / leaderboard, By category, Evaluation framework, Executive summary, Graph analysis — how they relate, LLM Evaluation Tooling — Landscape Report, Maintenance & risk signal, Master comparison (+6 more)

### Community 46 - "Community 46"
Cohesion: 0.13
Nodes (14): Benchmark / leaderboard, By category, Evaluation framework, Executive summary, Graph analysis — how they relate, LLM Evaluation Tooling — Landscape Report, Maintenance & risk signal, Master comparison (+6 more)

### Community 47 - "Community 47"
Cohesion: 0.14
Nodes (13): By category, Coding-agent memory, Executive summary, General memory layer, Graph analysis — how they relate, Knowledge-graph memory, LLM framework w/ memory, Maintenance & risk signal (+5 more)

### Community 48 - "Community 48"
Cohesion: 0.14
Nodes (13): Deeper analysis, Graph signal: centrality, clustering & the *real* network effect, How the top picks score (component view), Is this verdict robust, or did the weights decide it?, Methodology & caveats, Pareto check: which claws are never the metric-optimal pick?, Pick by what you care about, The one thing the score can't measure: network effect (+5 more)

### Community 49 - "Community 49"
Cohesion: 0.14
Nodes (13): By category, Coding-agent memory, Executive summary, General memory layer, Graph analysis — how they relate, Knowledge-graph memory, LLM framework w/ memory, Maintenance & risk signal (+5 more)

### Community 50 - "Community 50"
Cohesion: 0.14
Nodes (13): Deeper analysis, Graph signal: centrality, clustering & the *real* network effect, How the top picks score (component view), Is this verdict robust, or did the weights decide it?, Methodology & caveats, Pareto check: which claws are never the metric-optimal pick?, Pick by what you care about, The one thing the score can't measure: network effect (+5 more)

### Community 51 - "Community 51"
Cohesion: 0.15
Nodes (12): Agentic payments & settlement, Autonomous trading agents, Caveats, Claws rated for blockchain-fitness, MCP infrastructure (wire any chain in), On-chain data & explorer, Recommended stacks, Security & crypto primitives (+4 more)

### Community 52 - "Community 52"
Cohesion: 0.15
Nodes (12): Architecture, Ask AI setup, Data pipeline, Deploy to Netlify, GitHub Stars Analyzer, License, Project structure, Provider recipes (+4 more)

### Community 53 - "Community 53"
Cohesion: 0.15
Nodes (12): Agentic payments & settlement, Autonomous trading agents, Caveats, Claws rated for blockchain-fitness, MCP infrastructure (wire any chain in), On-chain data & explorer, Recommended stacks, Security & crypto primitives (+4 more)

### Community 54 - "Community 54"
Cohesion: 0.22
Nodes (8): Caveats, Ecosystem & graph signal, Hermes Agent vs OpenClaw — Head-to-Head, Side-by-side (🏆 = leads that metric), The broader field, Verdict, What the numbers say, Which should you use?

### Community 55 - "Community 55"
Cohesion: 0.22
Nodes (8): Caveats, Ecosystem & graph signal, Hermes Agent vs OpenClaw — Head-to-Head, Side-by-side (🏆 = leads that metric), The broader field, Verdict, What the numbers say, Which should you use?

### Community 56 - "Community 56"
Cohesion: 0.22
Nodes (8): Biggest themes worth your attention, 🔴 Empty categories (highest value — you have *nothing* here), 🟠 New round — gaps in uncovered categories (17, live-checked), ✅ Only 1 left, 🟢 Original list — 1 left, Quick-star list (copy/paste), Recommended to Star — Gaps in Your Collection, Secondary picks in covered categories

### Community 57 - "Community 57"
Cohesion: 0.33
Nodes (5): Coverage snapshot, Recommended to Star — Blockchain / DeFi Gaps, 🔴 Tier 1 — can't do serious EVM/DeFi work without these, 🟠 Tier 2 — DeFi protocol references, data & infra (high value for analysis), 🟡 Tier 3 — Solana, ZK & specialized (star if in scope)

### Community 62 - "Community 62"
Cohesion: 0.12
Nodes (15): Adjacent (deliberately not in the core list), Fundamental (13), Graph analysis — how they relate, Maintenance & risk signal, Master comparison, Methodology & caveats, Must-have (20), Projects to build (with the repos) (+7 more)

### Community 63 - "Community 63"
Cohesion: 0.12
Nodes (15): Adjacent (deliberately not in the core list), Fundamental (13), Graph analysis — how they relate, Maintenance & risk signal, Master comparison, Methodology & caveats, Must-have (20), Projects to build (with the repos) (+7 more)

## Knowledge Gaps
- **559 isolated node(s):** `LLM_BASE_URL`, `rateLog`, `PROVIDER_HOSTS`, `PROVIDER`, `config` (+554 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MetricRow()` connect `Community 0` to `Community 6`?**
  _High betweenness centrality (0.001) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `useGraph()` (e.g. with `AllRepos()` and `Comparator()`) actually correct?**
  _`useGraph()` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `LLM_BASE_URL`, `rateLog`, `PROVIDER_HOSTS` to the rest of the system?**
  _562 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.060285563194077206 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.09848484848484848 - nodes in this community are weakly interconnected._
- **Should `Community 3` be split into smaller, more focused modules?**
  _Cohesion score 0.11576354679802955 - nodes in this community are weakly interconnected._
- **Should `Community 9` be split into smaller, more focused modules?**
  _Cohesion score 0.05128205128205128 - nodes in this community are weakly interconnected._