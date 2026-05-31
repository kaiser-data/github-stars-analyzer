# Memory Frameworks for LLMs & Agents — Comparative Report

> Derived from **kaiser-data**'s 1,071 starred repos (snapshot `2026-05-24T19:57:47.245Z`), cross-referenced with the repo-similarity graph (1,071 nodes / 3,486 edges, 23 communities).
>
> Generated 2026-05-30 by `scripts/reports/memory_frameworks.py` (regenerate any time — no API cost).

## Executive summary

- **21 dedicated memory frameworks** identified across your stars, plus **5 storage substrates** (vector/graph DBs) they build on.
- Combined reach: **323,585★**. The space is overwhelmingly **Python** (10/21 projects).
- Four sub-categories emerge: **general memory layers**, **coding-agent/session memory**, **knowledge-graph memory**, and frameworks that **bundle a memory module**.
- The dominant architectural split is **vector-recall vs. knowledge-graph** memory — with a clear trend toward *temporal knowledge graphs* (graphiti) and *local-first* designs (OpenChronicle, ctx, TencentDB-Agent-Memory).

## Master comparison

Sorted by stars. `Health` and `Momentum` come from the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Project | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Coding-agent memory | TypeScript | Apache-2.0 | 77,829 | Rising | 79 | very active | 3d ago | 8mo | 1 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | General memory layer | Python | Apache-2.0 | 56,594 | Mature | 94 | very active | 0d ago | 2.9y | 32 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | General memory layer | Python | MIT | 52,767 | Hot | 76 | very active | 0d ago | 1mo | 10 |
| [getzep/graphiti](https://github.com/getzep/graphiti) | General memory layer | Python | Apache-2.0 | 26,478 | Hot | 70 | very active | 4d ago | 1.8y | 4 |
| [gastownhall/beads](https://github.com/gastownhall/beads) | Coding-agent memory | Go | MIT | 24,064 | Hot | 84 | very active | 0d ago | 7mo | 8 |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | General memory layer | Python | Apache-2.0 | 17,491 | Mature | 79 | very active | 0d ago | 2.8y | 8 |
| [memvid/memvid](https://github.com/memvid/memvid) | General memory layer | Rust | Apache-2.0 | 15,559 | Mature | 63 | active | 18d ago | 12mo | 3 |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | General memory layer | Python | NOASSERTION | 14,889 | Hot | 84 | very active | 1d ago | 10mo | 11 |
| [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | Coding-agent memory | JavaScript | MIT | 13,344 | Hot | 65 | very active | 0d ago | 6mo | 24 |
| [campfirein/byterover-cli](https://github.com/campfirein/byterover-cli) | Coding-agent memory | TypeScript | NOASSERTION | 4,786 | Hot | 84 | very active | 0d ago | 11mo | 11 |
| [plastic-labs/honcho](https://github.com/plastic-labs/honcho) | General memory layer | Python | AGPL-3.0 | 4,173 | Mature | 68 | very active | 2d ago | 2.7y | 25 |
| [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | General memory layer | TypeScript | NOASSERTION | 4,006 | Hot | 67 | very active | 0d ago | 1mo | 7 |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | General memory layer | JavaScript | Apache-2.0 | 3,388 | Hot | 78 | very active | 5d ago | 10mo | 4 |
| [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | General memory layer | Python | MIT | 2,757 | Hot | 53 | very active | 15d ago | 1mo | 9 |
| [trustgraph-ai/trustgraph](https://github.com/trustgraph-ai/trustgraph) | Knowledge-graph memory | Python | Apache-2.0 | 2,111 | Hot | 62 | very active | 3d ago | 1.9y | 13 |
| [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Knowledge-graph memory | Python | MIT | 1,170 | Hot | 79 | very active | 0d ago | 11mo | 4 |
| [shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) | Knowledge-graph memory | JavaScript | MIT | 862 | Declining | 41 | slowing | 5mo ago | 1.5y | 0 |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | General memory layer | TypeScript | — | 780 | Hot | 56 | very active | 1d ago | 3mo | 9 |
| [zmedelis/bosquet](https://github.com/zmedelis/bosquet) | LLM framework w/ memory | Clojure | EPL-1.0 | 371 | Mature | 30 | slowing | 4mo ago | 3.4y | 0 |
| [needle-ai/needle-mcp](https://github.com/needle-ai/needle-mcp) | Knowledge-graph memory | Python | MIT | 100 | Declining | 15 | stale | 10mo ago | 1.4y | 0 |
| [ActiveMemory/ctx](https://github.com/ActiveMemory/ctx) | General memory layer | HTML | NOASSERTION | 66 | Hot | 75 | very active | 1d ago | 4mo | 3 |

## By category

### General memory layer

_Drop-in memory APIs for any agent: store interactions/facts, retrieve relevant context on demand. The crowded, fast-moving core of the space._

- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 56,594★ · Python · Mature  
  Universal, LLM-agnostic memory API; extract+store+retrieve facts across sessions.  
  <sub>topics: ai, chatgpt, llm, python, chatbots, rag, application, long-term-memory</sub>
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 52,767★ · Python · Hot  
  Benchmark-focused open-source memory system.  
  <sub>topics: ai, chromadb, llm, mcp, memory, python</sub>
- **[getzep/graphiti](https://github.com/getzep/graphiti)** · 26,478★ · Python · Hot  
  Temporal knowledge graph engine behind Zep; bi-temporal edges, real-time incremental updates.  
  <sub>topics: agents, graph, llms, rag</sub>
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 17,491★ · Python · Mature  
  'Memory control plane' — ECL (extract-cognify-load) pipelines into a knowledge graph + vector store.  
  <sub>topics: ai, cognitive-architecture, vector-database, openai, rag, ai-agents, graph-database, ai-memory</sub>
- **[memvid/memvid](https://github.com/memvid/memvid)** · 15,559★ · Rust · Mature  
  Serverless single-file memory layer; replaces RAG pipelines with a portable artifact.  
  <sub>topics: ai, context, embedded, faiss, knowledge-base, knowledge-graph, llm, machine-learning</sub>
- **[MemoriLabs/Memori](https://github.com/MemoriLabs/Memori)** · 14,889★ · Python · Hot  
  Agent-native memory infra; turns execution & conversations into structured recall.  
  <sub>topics: agent, ai, long-short-term-memory, memory, python, rag, aiagent, chatgpt</sub>
- **[plastic-labs/honcho](https://github.com/plastic-labs/honcho)** · 4,173★ · Python · Mature  
  Memory library for stateful agents; user-modeling / theory-of-mind oriented.  
  <sub>topics: ai, llm, memory, personalization, embeddings, rag, agent-memory, ai-agents</sub>
- **[Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory)** · 4,006★ · TypeScript · Hot  
  Fully-local long-term memory via a 4-tier progressive pipeline.  
  <sub>topics: agent, llm, memory, openclaw-plugin, ai-agent, embedding, local-first, long-term-memory</sub>
- **[memodb-io/Acontext](https://github.com/memodb-io/Acontext)** · 3,388★ · JavaScript · Hot  
  Treats agent 'skills' as a memory layer.  
  <sub>topics: agent, context-engineering, data-platform, self-learning, agent-development-kit, ai-agent, llm, memory</sub>
- **[Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle)** · 2,757★ · Python · Hot  
  Local-first memory for any tool-capable LLM agent.  
  <sub>topics: —</sub>
- **[supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory)** · 780★ · TypeScript · Hot  
  Long-term memory & recall, packaged for OpenClaw agents.  
  <sub>topics: ai-memory, clawd, clawdbot, memory, moltbot, openai, openclaw</sub>
- **[ActiveMemory/ctx](https://github.com/ActiveMemory/ctx)** · 66★ · HTML · Hot  
  Single-binary, local-first 'convergent' memory for humans + machines.  
  <sub>topics: agent-infrastructure, ai-collaboration, ai-tooling, context-management, developer-tools, documentation, human-in-the-loop, knowledge-management</sub>

### Coding-agent memory

_Memory specialized for coding assistants (Claude Code, Cursor, OpenClaw): persist project context, decisions, and history across sessions._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 77,829★ · TypeScript · Rising  
  Persistent context across sessions; captures everything an agent does and re-injects it.  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude, claude-agent-sdk, claude-agents</sub>
- **[gastownhall/beads](https://github.com/gastownhall/beads)** · 24,064★ · Go · Hot  
  Distributed graph issue-tracker as durable agent memory (Dolt-backed).  
  <sub>topics: agents, claude-code, coding</sub>
- **[andrewyng/context-hub](https://github.com/andrewyng/context-hub)** · 13,344★ · JavaScript · Hot  
  Curated, versioned docs so agents stop hallucinating APIs / forgetting.  
  <sub>topics: —</sub>
- **[campfirein/byterover-cli](https://github.com/campfirein/byterover-cli)** · 4,786★ · TypeScript · Hot  
  Portable memory layer for autonomous coding agents (formerly Cipher).  
  <sub>topics: agent, llm, mcp, memory, vibe-coding, ai, autonomous-agents, cli</sub>

### Knowledge-graph memory

_Memory as a structured graph/ontology rather than a vector blob — better provenance, reasoning, and explainability._

- **[trustgraph-ai/trustgraph](https://github.com/trustgraph-ai/trustgraph)** · 2,111★ · Python · Hot  
  Agent runtime platform powered by context graphs + ontology.  
  <sub>topics: open-source, ai-infra, ai-tools, ontology, agent, graph, rdf, sparql</sub>
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 1,170★ · Python · Hot  
  AI-native KG framework: semantic retrieval, ontology reasoning, provenance.  
  <sub>topics: ai-agents, graphrag, knowledge-engineering, rag, semantic-layer, agentic-ai, semantic-web, context-management</sub>
- **[shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** · 862★ · JavaScript · Declining  
  MCP server giving Claude persistent memory via a local knowledge graph.  
  <sub>topics: ai-memory, claude-ai, knowledge-graph, mcp, memory-server, typescript</sub>
- **[needle-ai/needle-mcp](https://github.com/needle-ai/needle-mcp)** · 100★ · Python · Declining  
  MCP server: long-term memory for LLMs via managed RAG.  
  <sub>topics: ai, mcp, modelcontextprotocol, rag, semantic-search</sub>

### LLM framework w/ memory

_Broader LLMOps toolkits that ship memory as one module._

- **[zmedelis/bosquet](https://github.com/zmedelis/bosquet)** · 371★ · Clojure · Mature  
  Clojure LLMOps toolkit; prompt composition + agents + LLM memory.  
  <sub>topics: clojure, gpt, prompt-engineering, llmops, ai</sub>

## Graph analysis — how they relate

**Community clustering.** The 21 frameworks fall into **6 of the graph's 23 communities** — meaning memory tooling does *not* form one tight cluster but is spread across the AI-infra landscape (each tends to cluster with its neighbors: vector DBs, agent frameworks, or MCP tooling).

- **Community 12** (12): `mem0ai/mem0`, `topoteretes/cognee`, `MemoriLabs/Memori`, `memvid/memvid`, `plastic-labs/honcho`, `memodb-io/Acontext`, `MemPalace/mempalace`, `trustgraph-ai/trustgraph`, `semantica-agi/semantica`, `shaneholloman/mcp-knowledge-graph`, `needle-ai/needle-mcp`, `zmedelis/bosquet`
- **Community 3** (2): `getzep/graphiti`, `ActiveMemory/ctx`
- **Community 0** (2): `Tencent/TencentDB-Agent-Memory`, `campfirein/byterover-cli`
- **Community 5** (2): `Einsia/OpenChronicle`, `andrewyng/context-hub`
- **Community 10** (2): `thedotmack/claude-mem`, `gastownhall/beads`

**Centrality (PageRank in the full 1,071-repo graph).** Higher = more connected to the rest of your starred ecosystem (a proxy for how 'hub-like' the project is):

- `MemPalace/mempalace` — PageRank 0.0021
- `getzep/graphiti` — PageRank 0.0020
- `campfirein/byterover-cli` — PageRank 0.0010
- `needle-ai/needle-mcp` — PageRank 0.0010
- `ActiveMemory/ctx` — PageRank 0.0010
- `plastic-labs/honcho` — PageRank 0.0009
- `andrewyng/context-hub` — PageRank 0.0008
- `mem0ai/mem0` — PageRank 0.0007

**Direct links between memory frameworks** (similarity edges where both endpoints are in this report):

- `MemoriLabs/Memori` ⇄ `mem0ai/mem0` (w=0.370) — topics: ai, memory, python, rag
- `plastic-labs/honcho` ⇄ `mem0ai/mem0` (w=0.358) — topics: ai, llm, memory, rag
- `plastic-labs/honcho` ⇄ `MemoriLabs/Memori` (w=0.350) — topics: ai, llm, memory, rag
- `MemPalace/mempalace` ⇄ `campfirein/byterover-cli` (w=0.267) — topics: ai, llm, mcp, memory
- `plastic-labs/honcho` ⇄ `topoteretes/cognee` (w=0.262) — topics: ai, rag, ai-agents, ai-memory
- `MemPalace/mempalace` ⇄ `MemoriLabs/Memori` (w=0.240) — topics: ai, llm, memory, python
- `plastic-labs/honcho` ⇄ `thedotmack/claude-mem` (w=0.212) — topics: ai, embeddings, rag, ai-agents
- `Tencent/TencentDB-Agent-Memory` ⇄ `campfirein/byterover-cli` (w=0.208) — topics: agent, llm, memory
- `Tencent/TencentDB-Agent-Memory` ⇄ `memodb-io/Acontext` (w=0.200) — topics: agent, llm, memory, ai-agent
- `trustgraph-ai/trustgraph` ⇄ `semantica-agi/semantica` (w=0.164) — topics: context-graph, ontology-engineering, developer-tools, agent-memory
- `trustgraph-ai/trustgraph` ⇄ `topoteretes/cognee` (w=0.161) — topics: open-source, context-engineering, knowledge-graph, graph-database

## Maintenance & risk signal

Bus factor = how concentrated commits are in one author (1 = single-maintainer risk). Use alongside lifecycle + activity before adopting.

| Project | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| mem0ai/mem0 | 94 | Mature | very active | 4 | 27% | 321 |
| MemoriLabs/Memori | 84 | Hot | very active | 2 | 36% | 36 |
| campfirein/byterover-cli | 84 | Hot | very active | 2 | 34% | 25 |
| gastownhall/beads | 84 | Hot | very active | 2 | 38% | 90 |
| topoteretes/cognee | 79 | Mature | very active | 1 | 58% | 113 |
| thedotmack/claude-mem | 79 | Rising | very active | 1 | 100% | 271 |
| semantica-agi/semantica | 79 | Hot | very active | 1 | 91% | 17 |
| memodb-io/Acontext | 78 | Hot | very active | 1 | 74% | 279 |
| MemPalace/mempalace | 76 | Hot | very active | 1 | 54% | 8 |
| ActiveMemory/ctx | 75 | Hot | very active | 1 | 68% | 7 |
| getzep/graphiti | 70 | Hot | very active | 1 | 62% | 195 |
| plastic-labs/honcho | 68 | Mature | very active | 3 | 22% | 0 |
| Tencent/TencentDB-Agent-Memory | 67 | Hot | very active | 1 | 64% | 5 |
| andrewyng/context-hub | 65 | Hot | very active | 2 | 47% | 1 |
| memvid/memvid | 63 | Mature | active | 1 | 71% | 11 |
| trustgraph-ai/trustgraph | 62 | Hot | very active | 1 | 70% | 0 |
| supermemoryai/openclaw-supermemory | 56 | Hot | very active | 1 | 54% | 0 |
| Einsia/OpenChronicle | 53 | Hot | very active | 2 | 32% | 0 |
| shaneholloman/mcp-knowledge-graph | 41 | Declining | slowing | 0 | 0% | 8 |
| zmedelis/bosquet | 30 | Mature | slowing | 0 | 0% | 14 |
| needle-ai/needle-mcp | 15 | Declining | stale | 0 | 0% | 0 |

## Which one should you use?

| If you want… | Start with | Why |
|---|---|---|
| A batteries-included, widely-adopted memory API | `mem0ai/mem0` | Largest mindshare among dedicated layers; LLM-agnostic; well-documented. |
| Temporal / relationship-aware memory (knowledge graph) | `getzep/graphiti` | Bi-temporal KG with real-time incremental updates; strongest graph design. |
| A full 'memory control plane' with pipelines | `topoteretes/cognee` | ECL pipelines + graph + vector; more framework than library. |
| Memory for a coding agent (Claude Code/Cursor) | `thedotmack/claude-mem` | Purpose-built session persistence; by far the most-starred in this niche. |
| Local-first / no-cloud memory | `Einsia/OpenChronicle` or `Tencent/TencentDB-Agent-Memory` | Both emphasize fully-local long-term memory. |
| Provenance / explainable, ontology-driven memory | `trustgraph-ai/trustgraph` / `semantica-agi/semantica` | Context graphs with reasoning + full provenance. |
| Drop-in via MCP (no SDK lock-in) | `shaneholloman/mcp-knowledge-graph` / `needle-ai/needle-mcp` | Expose memory to any MCP-capable client. |

## Memory substrate (storage layer)

Not memory *frameworks*, but the databases these layers typically sit on. Several are also in your stars:

| Store | ★ Stars | Lang | Role |
|---|---|---|---|
| [redis/redis](https://github.com/redis/redis) | 74,518 | C | In-memory data store; common KV/vector backing for memory layers. |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | 40,116 | C++ | Dense-vector similarity search library; embedding index substrate. |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | 28,084 | Rust | AI-native search/vector DB used as memory storage. |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 9,685 | C++ | Lightweight in-process vector database. |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | 4,456 | C | Fast graph database (GraphBLAS) for graph-shaped memory. |

## Methodology & caveats

- **Source**: `public/data/classified.json` (full metadata) + `public/data/graph.json` (similarity graph). No external calls; fully reproducible.
- **Selection**: keyword scan across name/description/topics/README for memory + LLM/agent signals, then manual curation into the taxonomy in this script. Generic 'memory-efficient' infra (e.g. vLLM) and pure tutorials/awesome-lists were excluded.
- **Metrics** (health, momentum, lifecycle, bus_factor) are precomputed by the analyzer pipeline at snapshot time and may lag GitHub's current state.
- **The market is young**: many of these launched in the last 12 months; star counts and activity shift fast. Re-run this script after a fresh `classified.json` to refresh.

<sub>Frameworks covered: 21 · Snapshot: 2026-05-24T19:57:47.245Z</sub>
