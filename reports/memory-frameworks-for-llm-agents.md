# Memory Frameworks for LLMs & Agents — Comparative Report

> Derived from **kaiser-data**'s 2,243 starred repos (snapshot `2026-09-25T10:37:19.717Z`), cross-referenced with the repo-similarity graph (2,243 nodes / 7,393 edges, 35 communities).
>
> Generated 2026-09-25 by `scripts/reports/memory_frameworks.py` (regenerate any time — no API cost).

![Top tools by stars](assets/memory-frameworks-for-llm-agents-top-tools.svg)

![Tools per category](assets/memory-frameworks-for-llm-agents-categories.svg)


## Executive summary

- **22 dedicated memory frameworks** identified across your stars, plus **5 storage substrates** (vector/graph DBs) they build on.
- Combined reach: **446,307★**. The space is overwhelmingly **Python** (10/22 projects).
- Four sub-categories emerge: **general memory layers**, **coding-agent/session memory**, **knowledge-graph memory**, and frameworks that **bundle a memory module**.
- The dominant architectural split is **vector-recall vs. knowledge-graph** memory — with a clear trend toward *temporal knowledge graphs* (graphiti) and *local-first* designs (OpenChronicle, ctx, TencentDB-Agent-Memory).

## Master comparison

Sorted by stars. `Health` and `Momentum` come from the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Project | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Coding-agent memory | TypeScript | Apache-2.0 | 94,658 (▲282) | Hot | 80 | very active | 0d ago | 1.1y | 16 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | General memory layer | Python | Apache-2.0 | 65,976 (▲219) | Classic | 84 | very active | 0d ago | 3.3y | 28 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | General memory layer | Python | MIT | 59,268 (▲76) | Hot | 81 | very active | 0d ago | 5mo | 22 |
| [getzep/graphiti](https://github.com/getzep/graphiti) | General memory layer | Python | Apache-2.0 | 31,149 (▲102) | Mature | 74 | very active | 0d ago | 2.1y | 27 |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | General memory layer | Python | Apache-2.0 | 30,973 (▲93) | Classic | 83 | very active | 0d ago | 3.1y | 10 |
| [gastownhall/beads](https://github.com/gastownhall/beads) | Coding-agent memory | Go | MIT | 27,410 (▲78) | Hot | 77 | very active | 0d ago | 11mo | 17 |
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | General memory layer | TypeScript | NOASSERTION | 27,264 (▲179) | Hot | 84 | very active | 1d ago | 5mo | 22 |
| [letta-ai/letta](https://github.com/letta-ai/letta) | General memory layer | — | Apache-2.0 | 24,877 (▲55) | Mature | 66 | active | 15d ago | 3.0y | 2 |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | General memory layer | Python | NOASSERTION | 16,929 (▲54) | Mature | 63 | active | 7d ago | 1.2y | 1 |
| [memvid/memvid](https://github.com/memvid/memvid) | General memory layer | Rust | Apache-2.0 | 16,554 (▲3) | Declining | 55 | slowing | 2mo ago | 1.3y | 1 |
| [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | Coding-agent memory | JavaScript | MIT | 13,983 (▲3) | Declining | 27 | slowing | 3mo ago | 11mo | 0 |
| [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Knowledge-graph memory | Python | MIT | 13,458 (▲111) | Hot | 99 | very active | 0d ago | 1.3y | 33 |
| [plastic-labs/honcho](https://github.com/plastic-labs/honcho) | General memory layer | Python | AGPL-3.0 | 7,333 (▲52) | Classic | 68 | very active | 1d ago | 3.0y | 13 |
| [campfirein/byterover-cli](https://github.com/campfirein/byterover-cli) | Coding-agent memory | TypeScript | NOASSERTION | 4,964 (▼1) | Declining | 46 | slowing | 3mo ago | 1.3y | 0 |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | General memory layer | JavaScript | Apache-2.0 | 3,696 (▲5) | Declining | 47 | slowing | 2mo ago | 1.2y | 0 |
| [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | General memory layer | Python | MIT | 2,820 (▲2) | Declining | 21 | slowing | 4mo ago | 5mo | 0 |
| [trustgraph-ai/trustgraph](https://github.com/trustgraph-ai/trustgraph) | Knowledge-graph memory | Python | Apache-2.0 | 2,749 (▲13) | Mature | 65 | very active | 1d ago | 2.2y | 11 |
| [shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) | Knowledge-graph memory | JavaScript | MIT | 890 (▲1) | Declining | 41 | slowing | 3mo ago | 1.8y | 0 |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | General memory layer | TypeScript | — | 795 | Mature | 47 | active | 8d ago | 8mo | 2 |
| [zmedelis/bosquet](https://github.com/zmedelis/bosquet) | LLM framework w/ memory | Clojure | EPL-1.0 | 380 | Mature | 31 | slowing | 4mo ago | 3.7y | 0 |
| [needle-ai/needle-mcp](https://github.com/needle-ai/needle-mcp) | Knowledge-graph memory | Python | MIT | 103 | Abandoned | 10 | stale | 1.2y ago | 1.8y | 0 |
| [ActiveMemory/ctx](https://github.com/ActiveMemory/ctx) | General memory layer | HTML | NOASSERTION | 78 | Hot | 77 | very active | 2d ago | 8mo | 6 |

## By category

### General memory layer

_Drop-in memory APIs for any agent: store interactions/facts, retrieve relevant context on demand. The crowded, fast-moving core of the space._

- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 65,976★ · Python · Classic  
  Universal, LLM-agnostic memory API; extract+store+retrieve facts across sessions.  
  <sub>topics: ai, chatgpt, llm, python, rag, long-term-memory, memory, memory-management</sub>
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 59,268★ · Python · Hot  
  Benchmark-focused open-source memory system.  
  <sub>topics: ai, chromadb, llm, mcp, memory, python</sub>
- **[getzep/graphiti](https://github.com/getzep/graphiti)** · 31,149★ · Python · Mature  
  Temporal knowledge graph engine behind Zep; bi-temporal edges, real-time incremental updates.  
  <sub>topics: agents, graph, llms, rag</sub>
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 30,973★ · Python · Classic  
  'Memory control plane' — ECL (extract-cognify-load) pipelines into a knowledge graph + vector store.  
  <sub>topics: ai, cognitive-architecture, vector-database, ai-agents, graph-database, ai-memory, cognitive-memory, knowledge</sub>
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 27,264★ · TypeScript · Hot  
  Fully-local long-term memory via a 4-tier progressive pipeline.  
  <sub>topics: agent, llm, memory, openclaw-plugin, ai-agent, embedding, local-first, long-term-memory</sub>
- **[letta-ai/letta](https://github.com/letta-ai/letta)** · 24,877★ · — · Mature  
  Ex-MemGPT — the project that coined 'agent memory'; self-editing memory + a stateful agent server.  
  <sub>topics: llm, llm-agent, ai, ai-agents</sub>
- **[MemoriLabs/Memori](https://github.com/MemoriLabs/Memori)** · 16,929★ · Python · Mature  
  Agent-native memory infra; turns execution & conversations into structured recall.  
  <sub>topics: agent, ai, long-short-term-memory, memory, python, rag, state-management, memory-management</sub>
- **[memvid/memvid](https://github.com/memvid/memvid)** · 16,554★ · Rust · Declining  
  Serverless single-file memory layer; replaces RAG pipelines with a portable artifact.  
  <sub>topics: ai, context, embedded, faiss, knowledge-base, knowledge-graph, llm, machine-learning</sub>
- **[plastic-labs/honcho](https://github.com/plastic-labs/honcho)** · 7,333★ · Python · Classic  
  Memory library for stateful agents; user-modeling / theory-of-mind oriented.  
  <sub>topics: ai, llm, memory, agent-memory, ai-agents, ai-memory, context-engineering, continual-learning</sub>
- **[memodb-io/Acontext](https://github.com/memodb-io/Acontext)** · 3,696★ · JavaScript · Declining  
  Treats agent 'skills' as a memory layer.  
  <sub>topics: agent, context-engineering, data-platform, self-learning, agent-development-kit, ai-agent, llm, memory</sub>
- **[Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle)** · 2,820★ · Python · Declining  
  Local-first memory for any tool-capable LLM agent.  
  <sub>topics: —</sub>
- **[supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory)** · 795★ · TypeScript · Mature  
  Long-term memory & recall, packaged for OpenClaw agents.  
  <sub>topics: ai-memory, clawd, clawdbot, memory, moltbot, openai, openclaw</sub>
- **[ActiveMemory/ctx](https://github.com/ActiveMemory/ctx)** · 78★ · HTML · Hot  
  Single-binary, local-first 'convergent' memory for humans + machines.  
  <sub>topics: agent-infrastructure, ai-collaboration, ai-tooling, context-management, developer-tools, documentation, human-in-the-loop, knowledge-management</sub>

### Coding-agent memory

_Memory specialized for coding assistants (Claude Code, Cursor, OpenClaw): persist project context, decisions, and history across sessions._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 94,658★ · TypeScript · Hot  
  Persistent context across sessions; captures everything an agent does and re-injects it.  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude, claude-agent-sdk, claude-agents</sub>
- **[gastownhall/beads](https://github.com/gastownhall/beads)** · 27,410★ · Go · Hot  
  Distributed graph issue-tracker as durable agent memory (Dolt-backed).  
  <sub>topics: agents, claude-code, coding</sub>
- **[andrewyng/context-hub](https://github.com/andrewyng/context-hub)** · 13,983★ · JavaScript · Declining  
  Curated, versioned docs so agents stop hallucinating APIs / forgetting.  
  <sub>topics: —</sub>
- **[campfirein/byterover-cli](https://github.com/campfirein/byterover-cli)** · 4,964★ · TypeScript · Declining  
  Portable memory layer for autonomous coding agents (formerly Cipher).  
  <sub>topics: agent, llm, mcp, memory, vibe-coding, ai, autonomous-agents, cli</sub>

### Knowledge-graph memory

_Memory as a structured graph/ontology rather than a vector blob — better provenance, reasoning, and explainability._

- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 13,458★ · Python · Hot  
  AI-native KG framework: semantic retrieval, ontology reasoning, provenance.  
  <sub>topics: ai, ai-governance, artificial-intelligence, context-engineering, context-graphs, decision-intelligence, explainable-ai, generative-ai</sub>
- **[trustgraph-ai/trustgraph](https://github.com/trustgraph-ai/trustgraph)** · 2,749★ · Python · Mature  
  Agent runtime platform powered by context graphs + ontology.  
  <sub>topics: open-source, ontology, agent, graph, rdf, knowledge-graph, owl, explainable-ai</sub>
- **[shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** · 890★ · JavaScript · Declining  
  MCP server giving Claude persistent memory via a local knowledge graph.  
  <sub>topics: ai-memory, claude-ai, knowledge-graph, mcp, memory-server, typescript</sub>
- **[needle-ai/needle-mcp](https://github.com/needle-ai/needle-mcp)** · 103★ · Python · Abandoned  
  MCP server: long-term memory for LLMs via managed RAG.  
  <sub>topics: ai, mcp, modelcontextprotocol, rag, semantic-search</sub>

### LLM framework w/ memory

_Broader LLMOps toolkits that ship memory as one module._

- **[zmedelis/bosquet](https://github.com/zmedelis/bosquet)** · 380★ · Clojure · Mature  
  Clojure LLMOps toolkit; prompt composition + agents + LLM memory.  
  <sub>topics: clojure, gpt, prompt-engineering, llmops, ai</sub>

## Graph analysis — how they relate

**Community clustering.** The 22 frameworks fall into **8 of the graph's 35 communities** — meaning memory tooling does *not* form one tight cluster but is spread across the AI-infra landscape (each tends to cluster with its neighbors: vector DBs, agent frameworks, or MCP tooling).

- **Community 6** (12): `mem0ai/mem0`, `letta-ai/letta`, `topoteretes/cognee`, `getzep/graphiti`, `MemoriLabs/Memori`, `plastic-labs/honcho`, `TencentCloud/TencentDB-Agent-Memory`, `memodb-io/Acontext`, `MemPalace/mempalace`, `thedotmack/claude-mem`, `andrewyng/context-hub`, `zmedelis/bosquet`
- **Community 8** (2): `memvid/memvid`, `semantica-agi/semantica`
- **Community 13** (2): `ActiveMemory/ctx`, `trustgraph-ai/trustgraph`
- **Community 9** (2): `shaneholloman/mcp-knowledge-graph`, `needle-ai/needle-mcp`

**Centrality (PageRank in the full 1,071-repo graph).** Higher = more connected to the rest of your starred ecosystem (a proxy for how 'hub-like' the project is):

- `MemPalace/mempalace` — PageRank 0.0010
- `letta-ai/letta` — PageRank 0.0007
- `plastic-labs/honcho` — PageRank 0.0006
- `mem0ai/mem0` — PageRank 0.0005
- `supermemoryai/openclaw-supermemory` — PageRank 0.0005
- `gastownhall/beads` — PageRank 0.0005
- `getzep/graphiti` — PageRank 0.0004
- `topoteretes/cognee` — PageRank 0.0004

**Direct links between memory frameworks** (similarity edges where both endpoints are in this report):

- `MemoriLabs/Memori` ⇄ `mem0ai/mem0` (w=0.330) — topics: ai, memory, python, rag
- `MemPalace/mempalace` ⇄ `plastic-labs/honcho` (w=0.281) — topics: ai, llm, memory
- `plastic-labs/honcho` ⇄ `topoteretes/cognee` (w=0.258) — topics: ai, agent-memory, ai-agents, ai-memory
- `TencentCloud/TencentDB-Agent-Memory` ⇄ `memodb-io/Acontext` (w=0.200) — topics: agent, llm, memory, ai-agent

## Maintenance & risk signal

Bus factor = how concentrated commits are in one author (1 = single-maintainer risk). Use alongside lifecycle + activity before adopting.

| Project | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| semantica-agi/semantica | 99 | Hot | very active | 5 | 25% | 24 |
| mem0ai/mem0 | 84 | Classic | very active | 2 | 48% | 414 |
| TencentCloud/TencentDB-Agent-Memory | 84 | Hot | very active | 4 | 19% | 19 |
| topoteretes/cognee | 83 | Classic | very active | 2 | 42% | 150 |
| MemPalace/mempalace | 81 | Hot | very active | 2 | 47% | 18 |
| thedotmack/claude-mem | 80 | Hot | very active | 1 | 78% | 345 |
| ActiveMemory/ctx | 77 | Hot | very active | 1 | 72% | 7 |
| gastownhall/beads | 77 | Hot | very active | 1 | 51% | 101 |
| getzep/graphiti | 74 | Mature | very active | 1 | 55% | 200 |
| plastic-labs/honcho | 68 | Classic | very active | 2 | 27% | 1 |
| letta-ai/letta | 66 | Mature | active | 1 | 50% | 177 |
| trustgraph-ai/trustgraph | 65 | Mature | very active | 1 | 65% | 1 |
| MemoriLabs/Memori | 63 | Mature | active | 1 | 100% | 38 |
| memvid/memvid | 55 | Declining | slowing | 1 | 100% | 12 |
| memodb-io/Acontext | 47 | Declining | slowing | 0 | 0% | 279 |
| supermemoryai/openclaw-supermemory | 47 | Mature | active | 1 | 57% | 0 |
| campfirein/byterover-cli | 46 | Declining | slowing | 0 | 0% | 27 |
| shaneholloman/mcp-knowledge-graph | 41 | Declining | slowing | 0 | 0% | 8 |
| zmedelis/bosquet | 31 | Mature | slowing | 0 | 0% | 14 |
| andrewyng/context-hub | 27 | Declining | slowing | 0 | 0% | 1 |
| Einsia/OpenChronicle | 21 | Declining | slowing | 0 | 0% | 0 |
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
| [redis/redis](https://github.com/redis/redis) | 76,469 (▲36) | C | In-memory data store; common KV/vector backing for memory layers. |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | 40,978 (▲30) | C++ | Dense-vector similarity search library; embedding index substrate. |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | 29,370 (▲22) | Rust | AI-native search/vector DB used as memory storage. |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 16,004 (▲22) | C++ | Lightweight in-process vector database. |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | 6,296 (▲68) | Rust | Fast graph database (GraphBLAS) for graph-shaped memory. |

## Methodology & caveats

- **Source**: `data/classified.json` (full metadata) + `public/data/graph.json` (similarity graph). No external calls; fully reproducible.
- **Selection**: keyword scan across name/description/topics/README for memory + LLM/agent signals, then manual curation into the taxonomy in this script. Generic 'memory-efficient' infra (e.g. vLLM) and pure tutorials/awesome-lists were excluded.
- **Metrics** (health, momentum, lifecycle, bus_factor) are precomputed by the analyzer pipeline at snapshot time and may lag GitHub's current state.
- **The market is young**: many of these launched in the last 12 months; star counts and activity shift fast. Re-run this script after a fresh `classified.json` to refresh.

<sub>Frameworks covered: 22 · Snapshot: 2026-09-25T10:37:19.717Z</sub>
