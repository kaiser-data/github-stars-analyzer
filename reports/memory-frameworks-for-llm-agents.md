# Memory Frameworks for LLMs & Agents — Comparative Report

> Derived from **kaiser-data**'s 1,121 starred repos (snapshot `2026-06-02T21:41:26.385Z`), cross-referenced with the repo-similarity graph (1,121 nodes / 3,653 edges, 25 communities).
>
> Generated 2026-06-02 by `scripts/reports/memory_frameworks.py` (regenerate any time — no API cost).

## Executive summary

- **21 dedicated memory frameworks** identified across your stars, plus **5 storage substrates** (vector/graph DBs) they build on.
- Combined reach: **348,478★**. The space is overwhelmingly **Python** (11/21 projects).
- Four sub-categories emerge: **general memory layers**, **coding-agent/session memory**, **knowledge-graph memory**, and frameworks that **bundle a memory module**.
- The dominant architectural split is **vector-recall vs. knowledge-graph** memory — with a clear trend toward *temporal knowledge graphs* (graphiti) and *local-first* designs (OpenChronicle, ctx, TencentDB-Agent-Memory).

## Master comparison

Sorted by stars. `Health` and `Momentum` come from the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Project | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Coding-agent memory | TypeScript | Apache-2.0 | 80,248 | Rising | 79 | very active | 4d ago | 9mo | 1 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | General memory layer | Python | Apache-2.0 | 57,427 | Mature | 89 | very active | 0d ago | 3.0y | 24 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | General memory layer | Python | MIT | 53,319 | Hot | 75 | very active | 3d ago | 1mo | 6 |
| [getzep/graphiti](https://github.com/getzep/graphiti) | General memory layer | Python | Apache-2.0 | 26,920 | Hot | 68 | very active | 13d ago | 1.8y | 4 |
| [gastownhall/beads](https://github.com/gastownhall/beads) | Coding-agent memory | Go | MIT | 24,284 | Hot | 84 | very active | 1d ago | 7mo | 14 |
| [letta-ai/letta](https://github.com/letta-ai/letta) | General memory layer | Python | Apache-2.0 | 23,104 | Mature | 83 | very active | 19d ago | 2.6y | 12 |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | General memory layer | Python | Apache-2.0 | 17,642 | Mature | 79 | very active | 0d ago | 2.8y | 6 |
| [memvid/memvid](https://github.com/memvid/memvid) | General memory layer | Rust | Apache-2.0 | 15,607 | Mature | 65 | active | 6d ago | 1.0y | 3 |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | General memory layer | Python | NOASSERTION | 15,169 | Hot | 84 | very active | 0d ago | 10mo | 12 |
| [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | Coding-agent memory | JavaScript | MIT | 13,481 | Hot | 62 | very active | 2d ago | 7mo | 11 |
| [campfirein/byterover-cli](https://github.com/campfirein/byterover-cli) | Coding-agent memory | TypeScript | NOASSERTION | 4,812 | Hot | 84 | very active | 0d ago | 11mo | 8 |
| [plastic-labs/honcho](https://github.com/plastic-labs/honcho) | General memory layer | Python | AGPL-3.0 | 4,677 | Mature | 68 | very active | 0d ago | 2.7y | 24 |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | General memory layer | JavaScript | Apache-2.0 | 3,498 | Hot | 78 | very active | 7d ago | 10mo | 4 |
| [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | General memory layer | Python | MIT | 2,789 | Hot | 54 | very active | 24d ago | 1mo | 9 |
| [trustgraph-ai/trustgraph](https://github.com/trustgraph-ai/trustgraph) | Knowledge-graph memory | Python | Apache-2.0 | 2,130 | Hot | 62 | very active | 0d ago | 1.9y | 11 |
| [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Knowledge-graph memory | Python | MIT | 1,187 | Hot | 79 | very active | 0d ago | 11mo | 5 |
| [shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) | Knowledge-graph memory | JavaScript | MIT | 862 | Declining | 63 | active | 4d ago | 1.5y | 1 |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | General memory layer | TypeScript | — | 781 | Hot | 56 | very active | 8d ago | 4mo | 9 |
| [zmedelis/bosquet](https://github.com/zmedelis/bosquet) | LLM framework w/ memory | Clojure | EPL-1.0 | 372 | Mature | 48 | active | 9d ago | 3.4y | 2 |
| [needle-ai/needle-mcp](https://github.com/needle-ai/needle-mcp) | Knowledge-graph memory | Python | MIT | 100 | Declining | 14 | stale | 10mo ago | 1.5y | 0 |
| [ActiveMemory/ctx](https://github.com/ActiveMemory/ctx) | General memory layer | HTML | NOASSERTION | 69 | Rising | 76 | very active | 0d ago | 4mo | 2 |

## By category

### General memory layer

_Drop-in memory APIs for any agent: store interactions/facts, retrieve relevant context on demand. The crowded, fast-moving core of the space._

- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 57,427★ · Python · Mature  
  Universal, LLM-agnostic memory API; extract+store+retrieve facts across sessions.  
  <sub>topics: ai, chatgpt, llm, python, chatbots, rag, application, long-term-memory</sub>
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 53,319★ · Python · Hot  
  Benchmark-focused open-source memory system.  
  <sub>topics: ai, chromadb, llm, mcp, memory, python</sub>
- **[getzep/graphiti](https://github.com/getzep/graphiti)** · 26,920★ · Python · Hot  
  Temporal knowledge graph engine behind Zep; bi-temporal edges, real-time incremental updates.  
  <sub>topics: agents, graph, llms, rag</sub>
- **[letta-ai/letta](https://github.com/letta-ai/letta)** · 23,104★ · Python · Mature  
  Ex-MemGPT — the project that coined 'agent memory'; self-editing memory + a stateful agent server.  
  <sub>topics: llm, llm-agent, ai, ai-agents</sub>
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 17,642★ · Python · Mature  
  'Memory control plane' — ECL (extract-cognify-load) pipelines into a knowledge graph + vector store.  
  <sub>topics: ai, cognitive-architecture, vector-database, openai, rag, ai-agents, graph-database, ai-memory</sub>
- **[memvid/memvid](https://github.com/memvid/memvid)** · 15,607★ · Rust · Mature  
  Serverless single-file memory layer; replaces RAG pipelines with a portable artifact.  
  <sub>topics: ai, context, embedded, faiss, knowledge-base, knowledge-graph, llm, machine-learning</sub>
- **[MemoriLabs/Memori](https://github.com/MemoriLabs/Memori)** · 15,169★ · Python · Hot  
  Agent-native memory infra; turns execution & conversations into structured recall.  
  <sub>topics: agent, ai, long-short-term-memory, memory, python, rag, aiagent, chatgpt</sub>
- **[plastic-labs/honcho](https://github.com/plastic-labs/honcho)** · 4,677★ · Python · Mature  
  Memory library for stateful agents; user-modeling / theory-of-mind oriented.  
  <sub>topics: ai, llm, memory, personalization, embeddings, rag, agent-memory, ai-agents</sub>
- **[memodb-io/Acontext](https://github.com/memodb-io/Acontext)** · 3,498★ · JavaScript · Hot  
  Treats agent 'skills' as a memory layer.  
  <sub>topics: agent, context-engineering, data-platform, self-learning, agent-development-kit, ai-agent, llm, memory</sub>
- **[Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle)** · 2,789★ · Python · Hot  
  Local-first memory for any tool-capable LLM agent.  
  <sub>topics: —</sub>
- **[supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory)** · 781★ · TypeScript · Hot  
  Long-term memory & recall, packaged for OpenClaw agents.  
  <sub>topics: ai-memory, clawd, clawdbot, memory, moltbot, openai, openclaw</sub>
- **[ActiveMemory/ctx](https://github.com/ActiveMemory/ctx)** · 69★ · HTML · Rising  
  Single-binary, local-first 'convergent' memory for humans + machines.  
  <sub>topics: agent-infrastructure, ai-collaboration, ai-tooling, context-management, developer-tools, documentation, human-in-the-loop, knowledge-management</sub>

### Coding-agent memory

_Memory specialized for coding assistants (Claude Code, Cursor, OpenClaw): persist project context, decisions, and history across sessions._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 80,248★ · TypeScript · Rising  
  Persistent context across sessions; captures everything an agent does and re-injects it.  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude, claude-agent-sdk, claude-agents</sub>
- **[gastownhall/beads](https://github.com/gastownhall/beads)** · 24,284★ · Go · Hot  
  Distributed graph issue-tracker as durable agent memory (Dolt-backed).  
  <sub>topics: agents, claude-code, coding</sub>
- **[andrewyng/context-hub](https://github.com/andrewyng/context-hub)** · 13,481★ · JavaScript · Hot  
  Curated, versioned docs so agents stop hallucinating APIs / forgetting.  
  <sub>topics: —</sub>
- **[campfirein/byterover-cli](https://github.com/campfirein/byterover-cli)** · 4,812★ · TypeScript · Hot  
  Portable memory layer for autonomous coding agents (formerly Cipher).  
  <sub>topics: agent, llm, mcp, memory, vibe-coding, ai, autonomous-agents, cli</sub>

### Knowledge-graph memory

_Memory as a structured graph/ontology rather than a vector blob — better provenance, reasoning, and explainability._

- **[trustgraph-ai/trustgraph](https://github.com/trustgraph-ai/trustgraph)** · 2,130★ · Python · Hot  
  Agent runtime platform powered by context graphs + ontology.  
  <sub>topics: open-source, ai-infra, ai-tools, ontology, agent, graph, rdf, sparql</sub>
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 1,187★ · Python · Hot  
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

- **[zmedelis/bosquet](https://github.com/zmedelis/bosquet)** · 372★ · Clojure · Mature  
  Clojure LLMOps toolkit; prompt composition + agents + LLM memory.  
  <sub>topics: clojure, gpt, prompt-engineering, llmops, ai</sub>

## Graph analysis — how they relate

**Community clustering.** The 21 frameworks fall into **7 of the graph's 25 communities** — meaning memory tooling does *not* form one tight cluster but is spread across the AI-infra landscape (each tends to cluster with its neighbors: vector DBs, agent frameworks, or MCP tooling).

- **Community 5** (5): `mem0ai/mem0`, `MemoriLabs/Memori`, `plastic-labs/honcho`, `memodb-io/Acontext`, `MemPalace/mempalace`
- **Community 7** (4): `letta-ai/letta`, `campfirein/byterover-cli`, `andrewyng/context-hub`, `zmedelis/bosquet`
- **Community 1** (4): `topoteretes/cognee`, `memvid/memvid`, `Einsia/OpenChronicle`, `needle-ai/needle-mcp`
- **Community 15** (3): `ActiveMemory/ctx`, `trustgraph-ai/trustgraph`, `semantica-agi/semantica`
- **Community 18** (2): `getzep/graphiti`, `gastownhall/beads`
- **Community 0** (2): `supermemoryai/openclaw-supermemory`, `shaneholloman/mcp-knowledge-graph`

**Centrality (PageRank in the full 1,071-repo graph).** Higher = more connected to the rest of your starred ecosystem (a proxy for how 'hub-like' the project is):

- `MemPalace/mempalace` — PageRank 0.0023
- `getzep/graphiti` — PageRank 0.0021
- `letta-ai/letta` — PageRank 0.0020
- `ActiveMemory/ctx` — PageRank 0.0019
- `needle-ai/needle-mcp` — PageRank 0.0010
- `plastic-labs/honcho` — PageRank 0.0009
- `campfirein/byterover-cli` — PageRank 0.0009
- `andrewyng/context-hub` — PageRank 0.0008

**Direct links between memory frameworks** (similarity edges where both endpoints are in this report):

- `ActiveMemory/ctx` ⇄ `semantica-agi/semantica` (w=0.387) — topics: context-management, developer-tools; authors: dependabot[bot]
- `MemoriLabs/Memori` ⇄ `mem0ai/mem0` (w=0.370) — topics: ai, memory, python, rag
- `plastic-labs/honcho` ⇄ `mem0ai/mem0` (w=0.358) — topics: ai, llm, memory, rag
- `plastic-labs/honcho` ⇄ `MemoriLabs/Memori` (w=0.350) — topics: ai, llm, memory, rag
- `gastownhall/beads` ⇄ `getzep/graphiti` (w=0.284) — topics: agents; authors: dependabot[bot]
- `MemPalace/mempalace` ⇄ `campfirein/byterover-cli` (w=0.267) — topics: ai, llm, mcp, memory
- `plastic-labs/honcho` ⇄ `topoteretes/cognee` (w=0.262) — topics: ai, rag, ai-agents, ai-memory
- `MemPalace/mempalace` ⇄ `MemoriLabs/Memori` (w=0.240) — topics: ai, llm, memory, python
- `plastic-labs/honcho` ⇄ `thedotmack/claude-mem` (w=0.212) — topics: ai, embeddings, rag, ai-agents
- `trustgraph-ai/trustgraph` ⇄ `topoteretes/cognee` (w=0.161) — topics: open-source, context-engineering, knowledge-graph, graph-database
- `trustgraph-ai/trustgraph` ⇄ `semantica-agi/semantica` (w=0.133) — topics: context-graph, developer-tools, agent-memory

## Maintenance & risk signal

Bus factor = how concentrated commits are in one author (1 = single-maintainer risk). Use alongside lifecycle + activity before adopting.

| Project | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| mem0ai/mem0 | 89 | Mature | very active | 3 | 35% | 331 |
| MemoriLabs/Memori | 84 | Hot | very active | 2 | 36% | 38 |
| campfirein/byterover-cli | 84 | Hot | very active | 2 | 27% | 27 |
| gastownhall/beads | 84 | Hot | very active | 2 | 43% | 91 |
| letta-ai/letta | 83 | Mature | very active | 2 | 30% | 177 |
| topoteretes/cognee | 79 | Mature | very active | 1 | 52% | 115 |
| thedotmack/claude-mem | 79 | Rising | very active | 1 | 100% | 272 |
| semantica-agi/semantica | 79 | Hot | very active | 1 | 81% | 17 |
| memodb-io/Acontext | 78 | Hot | very active | 1 | 74% | 279 |
| ActiveMemory/ctx | 76 | Rising | very active | 1 | 96% | 7 |
| MemPalace/mempalace | 75 | Hot | very active | 1 | 52% | 8 |
| getzep/graphiti | 68 | Hot | very active | 1 | 57% | 195 |
| plastic-labs/honcho | 68 | Mature | very active | 3 | 20% | 0 |
| memvid/memvid | 65 | Mature | active | 1 | 75% | 12 |
| shaneholloman/mcp-knowledge-graph | 63 | Declining | active | 1 | 100% | 8 |
| andrewyng/context-hub | 62 | Hot | very active | 1 | 74% | 1 |
| trustgraph-ai/trustgraph | 62 | Hot | very active | 1 | 73% | 0 |
| supermemoryai/openclaw-supermemory | 56 | Hot | very active | 1 | 52% | 0 |
| Einsia/OpenChronicle | 54 | Hot | very active | 2 | 32% | 0 |
| zmedelis/bosquet | 48 | Mature | active | 1 | 50% | 14 |
| needle-ai/needle-mcp | 14 | Declining | stale | 0 | 0% | 0 |

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
| [redis/redis](https://github.com/redis/redis) | 74,657 | C | In-memory data store; common KV/vector backing for memory layers. |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | 40,189 | C++ | Dense-vector similarity search library; embedding index substrate. |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | 28,190 | Rust | AI-native search/vector DB used as memory storage. |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 9,742 | C++ | Lightweight in-process vector database. |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | 4,497 | C | Fast graph database (GraphBLAS) for graph-shaped memory. |

## Methodology & caveats

- **Source**: `public/data/classified.json` (full metadata) + `public/data/graph.json` (similarity graph). No external calls; fully reproducible.
- **Selection**: keyword scan across name/description/topics/README for memory + LLM/agent signals, then manual curation into the taxonomy in this script. Generic 'memory-efficient' infra (e.g. vLLM) and pure tutorials/awesome-lists were excluded.
- **Metrics** (health, momentum, lifecycle, bus_factor) are precomputed by the analyzer pipeline at snapshot time and may lag GitHub's current state.
- **The market is young**: many of these launched in the last 12 months; star counts and activity shift fast. Re-run this script after a fresh `classified.json` to refresh.

<sub>Frameworks covered: 21 · Snapshot: 2026-06-02T21:41:26.385Z</sub>
