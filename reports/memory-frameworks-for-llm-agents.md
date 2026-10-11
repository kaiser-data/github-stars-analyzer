# Memory Frameworks for LLMs & Agents — Comparative Report

> Derived from **kaiser-data**'s 2,348 starred repos (snapshot `2026-10-11T22:14:20.246Z`), cross-referenced with the repo-similarity graph (2,348 nodes / 7,797 edges, 38 communities).
>
> Generated 2026-10-11 by `scripts/reports/memory_frameworks.py` (regenerate any time — no API cost).

![Top tools by stars](assets/memory-frameworks-for-llm-agents-top-tools.svg)

![Tools per category](assets/memory-frameworks-for-llm-agents-categories.svg)


## Executive summary

- **23 dedicated memory frameworks** identified across your stars, plus **5 storage substrates** (vector/graph DBs) they build on.
- Combined reach: **454,501★**. The space is overwhelmingly **Python** (10/23 projects).
- Four sub-categories emerge: **general memory layers**, **coding-agent/session memory**, **knowledge-graph memory**, and frameworks that **bundle a memory module**.
- The dominant architectural split is **vector-recall vs. knowledge-graph** memory — with a clear trend toward *temporal knowledge graphs* (graphiti) and *local-first* designs (OpenChronicle, ctx, TencentDB-Agent-Memory).

## Master comparison

Sorted by stars. `Health` and `Momentum` come from the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Project | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Coding-agent memory | TypeScript | Apache-2.0 | 99,136 | Hot | 85 | very active | 2d ago | 1.1y | 8 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | General memory layer | Python | Apache-2.0 | 66,942 | Classic | 83 | very active | 3d ago | 3.3y | 30 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | General memory layer | Python | MIT | 59,492 | Hot | 76 | very active | 2d ago | 6mo | 12 |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | General memory layer | Python | Apache-2.0 | 31,948 | Classic | 77 | very active | 2d ago | 3.2y | 9 |
| [getzep/graphiti](https://github.com/getzep/graphiti) | General memory layer | Python | Apache-2.0 | 31,613 | Mature | 76 | very active | 1d ago | 2.2y | 21 |
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | General memory layer | TypeScript | NOASSERTION | 27,887 | Hot | 84 | very active | 2d ago | 6mo | 25 |
| [gastownhall/beads](https://github.com/gastownhall/beads) | Coding-agent memory | Go | MIT | 27,780 | Hot | 76 | very active | 1d ago | 1.0y | 7 |
| [letta-ai/letta](https://github.com/letta-ai/letta) | General memory layer | — | Apache-2.0 | 25,095 | Mature | 64 | active | 1mo ago | 3.0y | 2 |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | General memory layer | Python | NOASSERTION | 17,148 | Mature | 63 | active | 9d ago | 1.2y | 1 |
| [memvid/memvid](https://github.com/memvid/memvid) | General memory layer | Rust | Apache-2.0 | 16,585 | Declining | 53 | slowing | 2mo ago | 1.4y | 1 |
| [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | Coding-agent memory | JavaScript | MIT | 13,973 | Declining | 26 | slowing | 4mo ago | 11mo | 0 |
| [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Knowledge-graph memory | Python | MIT | 13,901 | Hot | 89 | very active | 1d ago | 1.3y | 24 |
| [plastic-labs/honcho](https://github.com/plastic-labs/honcho) | General memory layer | Python | AGPL-3.0 | 7,554 | Classic | 70 | very active | 2d ago | 3.1y | 19 |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | General memory layer | JavaScript | Apache-2.0 | 3,693 | Declining | 46 | slowing | 2mo ago | 1.2y | 0 |
| [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | General memory layer | Python | MIT | 2,816 | Declining | 19 | slowing | 5mo ago | 5mo | 0 |
| [trustgraph-ai/trustgraph](https://github.com/trustgraph-ai/trustgraph) | Knowledge-graph memory | Python | Apache-2.0 | 2,790 | Mature | 63 | very active | 4d ago | 2.3y | 9 |
| [MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent) | General memory layer | TypeScript | MIT | 2,088 | Hot | 82 | very active | 2d ago | 2mo | 10 |
| [Asymptote-Labs/agent-beacon](https://github.com/Asymptote-Labs/agent-beacon) | Coding-agent memory | Go | MIT | 1,813 | Rising | 80 | very active | 0d ago | 5mo | 2 |
| [shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) | Knowledge-graph memory | JavaScript | MIT | 888 | Declining | 39 | slowing | 4mo ago | 1.8y | 0 |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | General memory layer | TypeScript | — | 796 | Rising | 49 | active | 2d ago | 8mo | 2 |
| [zmedelis/bosquet](https://github.com/zmedelis/bosquet) | LLM framework w/ memory | Clojure | EPL-1.0 | 381 | Mature | 49 | active | 12d ago | 3.8y | 2 |
| [needle-ai/needle-mcp](https://github.com/needle-ai/needle-mcp) | Knowledge-graph memory | Python | MIT | 103 | Abandoned | 10 | stale | 1.2y ago | 1.8y | 0 |
| [ActiveMemory/ctx](https://github.com/ActiveMemory/ctx) | General memory layer | HTML | NOASSERTION | 79 | Hot | 77 | very active | 6d ago | 8mo | 6 |

## By category

### General memory layer

_Drop-in memory APIs for any agent: store interactions/facts, retrieve relevant context on demand. The crowded, fast-moving core of the space._

- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 66,942★ · Python · Classic  
  Universal, LLM-agnostic memory API; extract+store+retrieve facts across sessions.  
  <sub>topics: ai, chatgpt, llm, python, rag, long-term-memory, memory, memory-management</sub>
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 59,492★ · Python · Hot  
  Benchmark-focused open-source memory system.  
  <sub>topics: ai, chromadb, llm, mcp, memory, python</sub>
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 31,948★ · Python · Classic  
  'Memory control plane' — ECL (extract-cognify-load) pipelines into a knowledge graph + vector store.  
  <sub>topics: ai, cognitive-architecture, vector-database, ai-agents, graph-database, ai-memory, cognitive-memory, knowledge</sub>
- **[getzep/graphiti](https://github.com/getzep/graphiti)** · 31,613★ · Python · Mature  
  Temporal knowledge graph engine behind Zep; bi-temporal edges, real-time incremental updates.  
  <sub>topics: agents, graph, llms, rag</sub>
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 27,887★ · TypeScript · Hot  
  Fully-local long-term memory via a 4-tier progressive pipeline.  
  <sub>topics: agent, llm, memory, openclaw-plugin, ai-agent, embedding, local-first, long-term-memory</sub>
- **[letta-ai/letta](https://github.com/letta-ai/letta)** · 25,095★ · — · Mature  
  Ex-MemGPT — the project that coined 'agent memory'; self-editing memory + a stateful agent server.  
  <sub>topics: llm, llm-agent, ai, ai-agents</sub>
- **[MemoriLabs/Memori](https://github.com/MemoriLabs/Memori)** · 17,148★ · Python · Mature  
  Agent-native memory infra; turns execution & conversations into structured recall.  
  <sub>topics: agent, ai, long-short-term-memory, memory, python, rag, state-management, memory-management</sub>
- **[memvid/memvid](https://github.com/memvid/memvid)** · 16,585★ · Rust · Declining  
  Serverless single-file memory layer; replaces RAG pipelines with a portable artifact.  
  <sub>topics: ai, context, embedded, faiss, knowledge-base, knowledge-graph, llm, machine-learning</sub>
- **[plastic-labs/honcho](https://github.com/plastic-labs/honcho)** · 7,554★ · Python · Classic  
  Memory library for stateful agents; user-modeling / theory-of-mind oriented.  
  <sub>topics: ai, llm, memory, agent-memory, ai-agents, ai-memory, context-engineering, continual-learning</sub>
- **[memodb-io/Acontext](https://github.com/memodb-io/Acontext)** · 3,693★ · JavaScript · Declining  
  Treats agent 'skills' as a memory layer.  
  <sub>topics: agent, context-engineering, data-platform, self-learning, agent-development-kit, ai-agent, llm, memory</sub>
- **[Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle)** · 2,816★ · Python · Declining  
  Local-first memory for any tool-capable LLM agent.  
  <sub>topics: —</sub>
- **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** · 2,088★ · TypeScript · Hot  
  Personal agent and local memory hub from the MemOS team — one shared memory any AI client can read.  
  <sub>topics: agent, ai-agents, memory, agentic-ai, llm, long-term-memory, personal-ai, chatgpt</sub>
- **[supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory)** · 796★ · TypeScript · Rising  
  Long-term memory & recall, packaged for OpenClaw agents.  
  <sub>topics: ai-memory, clawd, clawdbot, memory, moltbot, openai, openclaw</sub>
- **[ActiveMemory/ctx](https://github.com/ActiveMemory/ctx)** · 79★ · HTML · Hot  
  Single-binary, local-first 'convergent' memory for humans + machines.  
  <sub>topics: agent-infrastructure, ai-collaboration, ai-tooling, context-management, developer-tools, documentation, human-in-the-loop, knowledge-management</sub>

### Coding-agent memory

_Memory specialized for coding assistants (Claude Code, Cursor, OpenClaw): persist project context, decisions, and history across sessions._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 99,136★ · TypeScript · Hot  
  Persistent context across sessions; captures everything an agent does and re-injects it.  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude, claude-agent-sdk, claude-agents</sub>
- **[gastownhall/beads](https://github.com/gastownhall/beads)** · 27,780★ · Go · Hot  
  Distributed graph issue-tracker as durable agent memory (Dolt-backed).  
  <sub>topics: agents, claude-code, coding</sub>
- **[andrewyng/context-hub](https://github.com/andrewyng/context-hub)** · 13,973★ · JavaScript · Declining  
  Curated, versioned docs so agents stop hallucinating APIs / forgetting.  
  <sub>topics: —</sub>
- **[Asymptote-Labs/agent-beacon](https://github.com/Asymptote-Labs/agent-beacon)** · 1,813★ · Go · Rising  
  Cross-harness, self-improving memory layer — one memory shared by Claude Code, Codex and other agents.  
  <sub>topics: security-tools, agent-ai-cli, agent-security, mobile-device-management, security-information-and-event-management, security, ci, cloud</sub>

### Knowledge-graph memory

_Memory as a structured graph/ontology rather than a vector blob — better provenance, reasoning, and explainability._

- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 13,901★ · Python · Hot  
  AI-native KG framework: semantic retrieval, ontology reasoning, provenance.  
  <sub>topics: ai, ai-governance, artificial-intelligence, context-engineering, context-graphs, decision-intelligence, explainable-ai, generative-ai</sub>
- **[trustgraph-ai/trustgraph](https://github.com/trustgraph-ai/trustgraph)** · 2,790★ · Python · Mature  
  Agent runtime platform powered by context graphs + ontology.  
  <sub>topics: open-source, ontology, agent, graph, rdf, knowledge-graph, owl, explainable-ai</sub>
- **[shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** · 888★ · JavaScript · Declining  
  MCP server giving Claude persistent memory via a local knowledge graph.  
  <sub>topics: ai-memory, claude-ai, knowledge-graph, mcp, memory-server, typescript</sub>
- **[needle-ai/needle-mcp](https://github.com/needle-ai/needle-mcp)** · 103★ · Python · Abandoned  
  MCP server: long-term memory for LLMs via managed RAG.  
  <sub>topics: ai, mcp, modelcontextprotocol, rag, semantic-search</sub>

### LLM framework w/ memory

_Broader LLMOps toolkits that ship memory as one module._

- **[zmedelis/bosquet](https://github.com/zmedelis/bosquet)** · 381★ · Clojure · Mature  
  Clojure LLMOps toolkit; prompt composition + agents + LLM memory.  
  <sub>topics: clojure, gpt, prompt-engineering, llmops, ai</sub>

## Graph analysis — how they relate

**Community clustering.** The 23 frameworks fall into **9 of the graph's 38 communities** — meaning memory tooling does *not* form one tight cluster but is spread across the AI-infra landscape (each tends to cluster with its neighbors: vector DBs, agent frameworks, or MCP tooling).

- **Community 8** (10): `mem0ai/mem0`, `letta-ai/letta`, `topoteretes/cognee`, `getzep/graphiti`, `MemoriLabs/Memori`, `plastic-labs/honcho`, `TencentCloud/TencentDB-Agent-Memory`, `MemPalace/mempalace`, `gastownhall/beads`, `needle-ai/needle-mcp`
- **Community 16** (3): `memvid/memvid`, `trustgraph-ai/trustgraph`, `semantica-agi/semantica`
- **Community 10** (2): `supermemoryai/openclaw-supermemory`, `zmedelis/bosquet`
- **Community 0** (2): `Einsia/OpenChronicle`, `andrewyng/context-hub`
- **Community 5** (2): `thedotmack/claude-mem`, `Asymptote-Labs/agent-beacon`

**Centrality (PageRank in the full 1,071-repo graph).** Higher = more connected to the rest of your starred ecosystem (a proxy for how 'hub-like' the project is):

- `MemTensor/memmy-agent` — PageRank 0.0018
- `Asymptote-Labs/agent-beacon` — PageRank 0.0012
- `MemPalace/mempalace` — PageRank 0.0012
- `letta-ai/letta` — PageRank 0.0006
- `mem0ai/mem0` — PageRank 0.0005
- `plastic-labs/honcho` — PageRank 0.0005
- `needle-ai/needle-mcp` — PageRank 0.0005
- `getzep/graphiti` — PageRank 0.0004

**Direct links between memory frameworks** (similarity edges where both endpoints are in this report):

- `MemoriLabs/Memori` ⇄ `mem0ai/mem0` (w=0.330) — topics: ai, memory, python, rag
- `MemPalace/mempalace` ⇄ `semantica-agi/semantica` (w=0.298) — topics: ai, llm, python; authors: dependabot[bot], AmirF194
- `MemPalace/mempalace` ⇄ `plastic-labs/honcho` (w=0.281) — topics: ai, llm, memory
- `TencentCloud/TencentDB-Agent-Memory` ⇄ `memodb-io/Acontext` (w=0.200) — topics: agent, llm, memory, ai-agent

## Maintenance & risk signal

Bus factor = how concentrated commits are in one author (1 = single-maintainer risk). Use alongside lifecycle + activity before adopting.

| Project | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| semantica-agi/semantica | 89 | Hot | very active | 3 | 18% | 24 |
| thedotmack/claude-mem | 85 | Hot | very active | 2 | 48% | 361 |
| TencentCloud/TencentDB-Agent-Memory | 84 | Hot | very active | 4 | 20% | 20 |
| mem0ai/mem0 | 83 | Classic | very active | 2 | 46% | 416 |
| MemTensor/memmy-agent | 82 | Hot | very active | 2 | 30% | 21 |
| Asymptote-Labs/agent-beacon | 80 | Rising | very active | 1 | 91% | 149 |
| topoteretes/cognee | 77 | Classic | very active | 1 | 86% | 152 |
| ActiveMemory/ctx | 77 | Hot | very active | 1 | 80% | 7 |
| getzep/graphiti | 76 | Mature | very active | 1 | 55% | 200 |
| MemPalace/mempalace | 76 | Hot | very active | 1 | 72% | 18 |
| gastownhall/beads | 76 | Hot | very active | 1 | 62% | 105 |
| plastic-labs/honcho | 70 | Classic | very active | 2 | 29% | 2 |
| letta-ai/letta | 64 | Mature | active | 1 | 57% | 177 |
| MemoriLabs/Memori | 63 | Mature | active | 1 | 100% | 38 |
| trustgraph-ai/trustgraph | 63 | Mature | very active | 1 | 65% | 1 |
| memvid/memvid | 53 | Declining | slowing | 1 | 100% | 12 |
| supermemoryai/openclaw-supermemory | 49 | Rising | active | 1 | 70% | 0 |
| zmedelis/bosquet | 49 | Mature | active | 1 | 67% | 14 |
| memodb-io/Acontext | 46 | Declining | slowing | 0 | 0% | 279 |
| shaneholloman/mcp-knowledge-graph | 39 | Declining | slowing | 0 | 0% | 8 |
| andrewyng/context-hub | 26 | Declining | slowing | 0 | 0% | 1 |
| Einsia/OpenChronicle | 19 | Declining | slowing | 0 | 0% | 0 |
| needle-ai/needle-mcp | 10 | Abandoned | stale | 0 | 0% | 0 |

## Which one should you use?

| If you want… | Start with | Why |
|---|---|---|
| A batteries-included, widely-adopted memory API | `mem0ai/mem0` | Largest mindshare among dedicated layers; LLM-agnostic; well-documented. |
| Temporal / relationship-aware memory (knowledge graph) | `getzep/graphiti` | Bi-temporal KG with real-time incremental updates; strongest graph design. |
| A full 'memory control plane' with pipelines | `topoteretes/cognee` | ECL pipelines + graph + vector; more framework than library. |
| Memory for a coding agent (Claude Code/Cursor) | `thedotmack/claude-mem` | Purpose-built session persistence; by far the most-starred in this niche. |
| Local-first / no-cloud memory | `Einsia/OpenChronicle` or `TencentCloud/TencentDB-Agent-Memory` | Both emphasize fully-local long-term memory. |
| Provenance / explainable, ontology-driven memory | `trustgraph-ai/trustgraph` / `semantica-agi/semantica` | Context graphs with reasoning + full provenance. |
| Drop-in via MCP (no SDK lock-in) | `shaneholloman/mcp-knowledge-graph` / `needle-ai/needle-mcp` | Expose memory to any MCP-capable client. |

## Memory substrate (storage layer)

Not memory *frameworks*, but the databases these layers typically sit on. Several are also in your stars:

| Store | ★ Stars | Lang | Role |
|---|---|---|---|
| [redis/redis](https://github.com/redis/redis) | 76,695 | C | In-memory data store; common KV/vector backing for memory layers. |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | 41,124 | C++ | Dense-vector similarity search library; embedding index substrate. |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | 29,472 | Rust | AI-native search/vector DB used as memory storage. |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 16,092 | C++ | Lightweight in-process vector database. |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | 8,671 | Rust | Fast graph database (GraphBLAS) for graph-shaped memory. |

## Methodology & caveats

- **Source**: `data/classified.json` (full metadata) + `public/data/graph.json` (similarity graph). No external calls; fully reproducible.
- **Selection**: keyword scan across name/description/topics/README for memory + LLM/agent signals, then manual curation into the taxonomy in this script. Generic 'memory-efficient' infra (e.g. vLLM) and pure tutorials/awesome-lists were excluded.
- **Metrics** (health, momentum, lifecycle, bus_factor) are precomputed by the analyzer pipeline at snapshot time and may lag GitHub's current state.
- **The market is young**: many of these launched in the last 12 months; star counts and activity shift fast. Re-run this script after a fresh `classified.json` to refresh.

<sub>Frameworks covered: 23 · Snapshot: 2026-10-11T22:14:20.246Z</sub>
