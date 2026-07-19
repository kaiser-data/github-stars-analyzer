# Memory Frameworks for LLMs & Agents — Comparative Report

> Derived from **kaiser-data**'s 1,341 starred repos (snapshot `2026-07-19T22:39:07.967Z`), cross-referenced with the repo-similarity graph (1,341 nodes / 4,341 edges, 28 communities).
>
> Generated 2026-07-19 by `scripts/reports/memory_frameworks.py` (regenerate any time — no API cost).

![Top tools by stars](assets/memory-frameworks-for-llm-agents-top-tools.svg)

![Tools per category](assets/memory-frameworks-for-llm-agents-categories.svg)


## Executive summary

- **22 dedicated memory frameworks** identified across your stars, plus **5 storage substrates** (vector/graph DBs) they build on.
- Combined reach: **391,153★**. The space is overwhelmingly **Python** (10/22 projects).
- Four sub-categories emerge: **general memory layers**, **coding-agent/session memory**, **knowledge-graph memory**, and frameworks that **bundle a memory module**.
- The dominant architectural split is **vector-recall vs. knowledge-graph** memory — with a clear trend toward *temporal knowledge graphs* (graphiti) and *local-first* designs (OpenChronicle, ctx, TencentDB-Agent-Memory).

## Master comparison

Sorted by stars. `Health` and `Momentum` come from the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Project | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Coding-agent memory | JavaScript | Apache-2.0 | 87,866 (▲854) | Rising | 79 | very active | 1d ago | 10mo | 1 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | General memory layer | TypeScript | Apache-2.0 | 61,207 (▲501) | Classic | 89 | very active | 0d ago | 3.1y | 38 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | General memory layer | Python | MIT | 57,480 (▲212) | Hot | 76 | very active | 2d ago | 3mo | 19 |
| [getzep/graphiti](https://github.com/getzep/graphiti) | General memory layer | Python | Apache-2.0 | 28,921 (▲263) | Hot | 76 | very active | 2d ago | 1.9y | 10 |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | General memory layer | Python | Apache-2.0 | 28,491 (▲787) | Mature | 77 | very active | 0d ago | 2.9y | 10 |
| [gastownhall/beads](https://github.com/gastownhall/beads) | Coding-agent memory | Go | MIT | 25,435 (▲173) | Hot | 83 | very active | 0d ago | 9mo | 8 |
| [letta-ai/letta](https://github.com/letta-ai/letta) | General memory layer | Python | Apache-2.0 | 23,868 (▲102) | Mature | 63 | active | 16d ago | 2.8y | 2 |
| [memvid/memvid](https://github.com/memvid/memvid) | General memory layer | Rust | Apache-2.0 | 16,005 (▲255) | Mature | 64 | active | 5d ago | 1.1y | 2 |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | General memory layer | Python | NOASSERTION | 15,628 (▲51) | Hot | 81 | active | 1mo ago | 12mo | 13 |
| [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | Coding-agent memory | JavaScript | MIT | 13,807 (▲29) | Hot | 55 | active | 1mo ago | 8mo | 8 |
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | General memory layer | TypeScript | NOASSERTION | 9,126 (▲408) | Hot | 80 | very active | 0d ago | 3mo | 21 |
| [plastic-labs/honcho](https://github.com/plastic-labs/honcho) | General memory layer | Python | AGPL-3.0 | 6,059 (▲125) | Mature | 73 | very active | 2d ago | 2.9y | 26 |
| [campfirein/byterover-cli](https://github.com/campfirein/byterover-cli) | Coding-agent memory | TypeScript | NOASSERTION | 4,925 (▲9) | Hot | 82 | very active | 24d ago | 1.1y | 8 |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | General memory layer | JavaScript | Apache-2.0 | 3,582 (▲7) | Declining | 59 | active | 5d ago | 1.0y | 1 |
| [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | General memory layer | Python | MIT | 2,798 (▲3) | Hot | 50 | slowing | 2mo ago | 2mo | 9 |
| [trustgraph-ai/trustgraph](https://github.com/trustgraph-ai/trustgraph) | Knowledge-graph memory | Python | Apache-2.0 | 2,328 (▲46) | Mature | 63 | very active | 3d ago | 2.0y | 9 |
| [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Knowledge-graph memory | Python | MIT | 1,415 (▲12) | Hot | 80 | very active | 0d ago | 1.1y | 4 |
| [shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) | Knowledge-graph memory | JavaScript | MIT | 877 (▲2) | Declining | 59 | active | 1mo ago | 1.6y | 1 |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | General memory layer | TypeScript | — | 791 (▲3) | Rising | 60 | very active | 29d ago | 5mo | 7 |
| [zmedelis/bosquet](https://github.com/zmedelis/bosquet) | LLM framework w/ memory | Clojure | EPL-1.0 | 375 | Mature | 44 | active | 1mo ago | 3.5y | 2 |
| [needle-ai/needle-mcp](https://github.com/needle-ai/needle-mcp) | Knowledge-graph memory | Python | MIT | 99 | Declining | 10 | stale | 11mo ago | 1.6y | 0 |
| [ActiveMemory/ctx](https://github.com/ActiveMemory/ctx) | General memory layer | HTML | NOASSERTION | 70 | Hot | 76 | very active | 0d ago | 6mo | 4 |

## By category

### General memory layer

_Drop-in memory APIs for any agent: store interactions/facts, retrieve relevant context on demand. The crowded, fast-moving core of the space._

- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 61,207★ · TypeScript · Classic  
  Universal, LLM-agnostic memory API; extract+store+retrieve facts across sessions.  
  <sub>topics: ai, chatgpt, llm, python, chatbots, rag, application, long-term-memory</sub>
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 57,480★ · Python · Hot  
  Benchmark-focused open-source memory system.  
  <sub>topics: ai, chromadb, llm, mcp, memory, python</sub>
- **[getzep/graphiti](https://github.com/getzep/graphiti)** · 28,921★ · Python · Hot  
  Temporal knowledge graph engine behind Zep; bi-temporal edges, real-time incremental updates.  
  <sub>topics: agents, graph, llms, rag</sub>
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 28,491★ · Python · Mature  
  'Memory control plane' — ECL (extract-cognify-load) pipelines into a knowledge graph + vector store.  
  <sub>topics: ai, cognitive-architecture, vector-database, ai-agents, graph-database, ai-memory, cognitive-memory, knowledge</sub>
- **[letta-ai/letta](https://github.com/letta-ai/letta)** · 23,868★ · Python · Mature  
  Ex-MemGPT — the project that coined 'agent memory'; self-editing memory + a stateful agent server.  
  <sub>topics: llm, llm-agent, ai, ai-agents</sub>
- **[memvid/memvid](https://github.com/memvid/memvid)** · 16,005★ · Rust · Mature  
  Serverless single-file memory layer; replaces RAG pipelines with a portable artifact.  
  <sub>topics: ai, context, embedded, faiss, knowledge-base, knowledge-graph, llm, machine-learning</sub>
- **[MemoriLabs/Memori](https://github.com/MemoriLabs/Memori)** · 15,628★ · Python · Hot  
  Agent-native memory infra; turns execution & conversations into structured recall.  
  <sub>topics: agent, ai, long-short-term-memory, memory, python, rag, state-management, memory-management</sub>
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 9,126★ · TypeScript · Hot  
  Fully-local long-term memory via a 4-tier progressive pipeline.  
  <sub>topics: agent, llm, memory, openclaw-plugin, ai-agent, embedding, local-first, long-term-memory</sub>
- **[plastic-labs/honcho](https://github.com/plastic-labs/honcho)** · 6,059★ · Python · Mature  
  Memory library for stateful agents; user-modeling / theory-of-mind oriented.  
  <sub>topics: ai, llm, memory, personalization, embeddings, rag, agent-memory, ai-agents</sub>
- **[memodb-io/Acontext](https://github.com/memodb-io/Acontext)** · 3,582★ · JavaScript · Declining  
  Treats agent 'skills' as a memory layer.  
  <sub>topics: agent, context-engineering, data-platform, self-learning, agent-development-kit, ai-agent, llm, memory</sub>
- **[Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle)** · 2,798★ · Python · Hot  
  Local-first memory for any tool-capable LLM agent.  
  <sub>topics: —</sub>
- **[supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory)** · 791★ · TypeScript · Rising  
  Long-term memory & recall, packaged for OpenClaw agents.  
  <sub>topics: ai-memory, clawd, clawdbot, memory, moltbot, openai, openclaw</sub>
- **[ActiveMemory/ctx](https://github.com/ActiveMemory/ctx)** · 70★ · HTML · Hot  
  Single-binary, local-first 'convergent' memory for humans + machines.  
  <sub>topics: agent-infrastructure, ai-collaboration, ai-tooling, context-management, developer-tools, documentation, human-in-the-loop, knowledge-management</sub>

### Coding-agent memory

_Memory specialized for coding assistants (Claude Code, Cursor, OpenClaw): persist project context, decisions, and history across sessions._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 87,866★ · JavaScript · Rising  
  Persistent context across sessions; captures everything an agent does and re-injects it.  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude, claude-agent-sdk, claude-agents</sub>
- **[gastownhall/beads](https://github.com/gastownhall/beads)** · 25,435★ · Go · Hot  
  Distributed graph issue-tracker as durable agent memory (Dolt-backed).  
  <sub>topics: agents, claude-code, coding</sub>
- **[andrewyng/context-hub](https://github.com/andrewyng/context-hub)** · 13,807★ · JavaScript · Hot  
  Curated, versioned docs so agents stop hallucinating APIs / forgetting.  
  <sub>topics: —</sub>
- **[campfirein/byterover-cli](https://github.com/campfirein/byterover-cli)** · 4,925★ · TypeScript · Hot  
  Portable memory layer for autonomous coding agents (formerly Cipher).  
  <sub>topics: agent, llm, mcp, memory, vibe-coding, ai, autonomous-agents, cli</sub>

### Knowledge-graph memory

_Memory as a structured graph/ontology rather than a vector blob — better provenance, reasoning, and explainability._

- **[trustgraph-ai/trustgraph](https://github.com/trustgraph-ai/trustgraph)** · 2,328★ · Python · Mature  
  Agent runtime platform powered by context graphs + ontology.  
  <sub>topics: open-source, ontology, agent, graph, rdf, sparql, context, knowledge-graph</sub>
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 1,415★ · Python · Hot  
  AI-native KG framework: semantic retrieval, ontology reasoning, provenance.  
  <sub>topics: ai, ai-governance, artificial-intelligence, context-engineering, context-graphs, decision-intelligence, explainable-ai, generative-ai</sub>
- **[shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** · 877★ · JavaScript · Declining  
  MCP server giving Claude persistent memory via a local knowledge graph.  
  <sub>topics: ai-memory, claude-ai, knowledge-graph, mcp, memory-server, typescript</sub>
- **[needle-ai/needle-mcp](https://github.com/needle-ai/needle-mcp)** · 99★ · Python · Declining  
  MCP server: long-term memory for LLMs via managed RAG.  
  <sub>topics: ai, mcp, modelcontextprotocol, rag, semantic-search</sub>

### LLM framework w/ memory

_Broader LLMOps toolkits that ship memory as one module._

- **[zmedelis/bosquet](https://github.com/zmedelis/bosquet)** · 375★ · Clojure · Mature  
  Clojure LLMOps toolkit; prompt composition + agents + LLM memory.  
  <sub>topics: clojure, gpt, prompt-engineering, llmops, ai</sub>

## Graph analysis — how they relate

**Community clustering.** The 22 frameworks fall into **8 of the graph's 28 communities** — meaning memory tooling does *not* form one tight cluster but is spread across the AI-infra landscape (each tends to cluster with its neighbors: vector DBs, agent frameworks, or MCP tooling).

- **Community 9** (10): `mem0ai/mem0`, `letta-ai/letta`, `MemoriLabs/Memori`, `plastic-labs/honcho`, `TencentCloud/TencentDB-Agent-Memory`, `memodb-io/Acontext`, `MemPalace/mempalace`, `Einsia/OpenChronicle`, `andrewyng/context-hub`, `zmedelis/bosquet`
- **Community 16** (4): `topoteretes/cognee`, `ActiveMemory/ctx`, `trustgraph-ai/trustgraph`, `semantica-agi/semantica`
- **Community 2** (2): `thedotmack/claude-mem`, `campfirein/byterover-cli`
- **Community 1** (2): `shaneholloman/mcp-knowledge-graph`, `needle-ai/needle-mcp`

**Centrality (PageRank in the full 1,071-repo graph).** Higher = more connected to the rest of your starred ecosystem (a proxy for how 'hub-like' the project is):

- `letta-ai/letta` — PageRank 0.0018
- `MemPalace/mempalace` — PageRank 0.0015
- `getzep/graphiti` — PageRank 0.0012
- `semantica-agi/semantica` — PageRank 0.0011
- `plastic-labs/honcho` — PageRank 0.0009
- `MemoriLabs/Memori` — PageRank 0.0008
- `gastownhall/beads` — PageRank 0.0008
- `needle-ai/needle-mcp` — PageRank 0.0008

**Direct links between memory frameworks** (similarity edges where both endpoints are in this report):

- `plastic-labs/honcho` ⇄ `MemoriLabs/Memori` (w=0.360) — topics: ai, llm, memory, rag
- `plastic-labs/honcho` ⇄ `mem0ai/mem0` (w=0.308) — topics: ai, llm, memory, rag
- `MemoriLabs/Memori` ⇄ `mem0ai/mem0` (w=0.280) — topics: ai, memory, python, rag
- `MemPalace/mempalace` ⇄ `campfirein/byterover-cli` (w=0.267) — topics: ai, llm, mcp, memory
- `plastic-labs/honcho` ⇄ `topoteretes/cognee` (w=0.232) — topics: ai, agent-memory, ai-agents, ai-memory
- `plastic-labs/honcho` ⇄ `thedotmack/claude-mem` (w=0.212) — topics: ai, embeddings, rag, ai-agents
- `TencentCloud/TencentDB-Agent-Memory` ⇄ `campfirein/byterover-cli` (w=0.208) — topics: agent, llm, memory
- `trustgraph-ai/trustgraph` ⇄ `topoteretes/cognee` (w=0.202) — topics: open-source, knowledge-graph, agent-memory, graph-database
- `TencentCloud/TencentDB-Agent-Memory` ⇄ `memodb-io/Acontext` (w=0.200) — topics: agent, llm, memory, ai-agent
- `trustgraph-ai/trustgraph` ⇄ `semantica-agi/semantica` (w=0.197) — topics: ontology, knowledge-graph, agent-memory, explainable-ai
- `semantica-agi/semantica` ⇄ `topoteretes/cognee` (w=0.197) — topics: ai, context-engineering, graph-rag, knowledge-graph
- `Einsia/OpenChronicle` ⇄ `MemoriLabs/Memori` (w=0.145) — authors: Chen17-sq

## Maintenance & risk signal

Bus factor = how concentrated commits are in one author (1 = single-maintainer risk). Use alongside lifecycle + activity before adopting.

| Project | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| mem0ai/mem0 | 89 | Classic | very active | 3 | 38% | 360 |
| gastownhall/beads | 83 | Hot | very active | 2 | 38% | 93 |
| campfirein/byterover-cli | 82 | Hot | very active | 2 | 27% | 27 |
| MemoriLabs/Memori | 81 | Hot | active | 2 | 41% | 38 |
| TencentCloud/TencentDB-Agent-Memory | 80 | Hot | very active | 2 | 40% | 9 |
| semantica-agi/semantica | 80 | Hot | very active | 1 | 62% | 18 |
| thedotmack/claude-mem | 79 | Rising | very active | 1 | 100% | 297 |
| topoteretes/cognee | 77 | Mature | very active | 1 | 61% | 127 |
| getzep/graphiti | 76 | Hot | very active | 2 | 27% | 196 |
| MemPalace/mempalace | 76 | Hot | very active | 1 | 53% | 13 |
| ActiveMemory/ctx | 76 | Hot | very active | 1 | 83% | 7 |
| plastic-labs/honcho | 73 | Mature | very active | 4 | 20% | 0 |
| memvid/memvid | 64 | Mature | active | 1 | 60% | 12 |
| letta-ai/letta | 63 | Mature | active | 1 | 75% | 177 |
| trustgraph-ai/trustgraph | 63 | Mature | very active | 1 | 64% | 0 |
| supermemoryai/openclaw-supermemory | 60 | Rising | very active | 3 | 22% | 0 |
| memodb-io/Acontext | 59 | Declining | active | 1 | 100% | 279 |
| shaneholloman/mcp-knowledge-graph | 59 | Declining | active | 1 | 100% | 8 |
| andrewyng/context-hub | 55 | Hot | active | 1 | 88% | 1 |
| Einsia/OpenChronicle | 50 | Hot | slowing | 2 | 32% | 0 |
| zmedelis/bosquet | 44 | Mature | active | 1 | 50% | 14 |
| needle-ai/needle-mcp | 10 | Declining | stale | 0 | 0% | 0 |

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
| [redis/redis](https://github.com/redis/redis) | 75,591 (▲154) | C | In-memory data store; common KV/vector backing for memory layers. |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | 40,541 (▲41) | C++ | Dense-vector similarity search library; embedding index substrate. |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | 28,828 (▲51) | Rust | AI-native search/vector DB used as memory storage. |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 15,144 (▲309) | C++ | Lightweight in-process vector database. |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | 4,803 (▲46) | C | Fast graph database (GraphBLAS) for graph-shaped memory. |

## Methodology & caveats

- **Source**: `data/classified.json` (full metadata) + `public/data/graph.json` (similarity graph). No external calls; fully reproducible.
- **Selection**: keyword scan across name/description/topics/README for memory + LLM/agent signals, then manual curation into the taxonomy in this script. Generic 'memory-efficient' infra (e.g. vLLM) and pure tutorials/awesome-lists were excluded.
- **Metrics** (health, momentum, lifecycle, bus_factor) are precomputed by the analyzer pipeline at snapshot time and may lag GitHub's current state.
- **The market is young**: many of these launched in the last 12 months; star counts and activity shift fast. Re-run this script after a fresh `classified.json` to refresh.

<sub>Frameworks covered: 22 · Snapshot: 2026-07-19T22:39:07.967Z</sub>
