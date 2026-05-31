# Token-Savings & Context-Efficiency Tooling

> Derived from **kaiser-data**'s 1,071 starred repos (snapshot `2026-05-24T19:57:47.245Z`), cross-referenced with the repo-similarity graph (1,071 nodes / 3,486 edges, 23 communities).
>
> Generated 2026-05-31 by `scripts/reports/token_savings.py` (regenerate any time — no API cost).

> **Read this first:** these tools cut tokens at *different layers* (codebase reads, tool output, data format, the wire, model weights). They mostly **compose** rather than compete. All **% figures are the projects' own claims** on the May-2026 snapshot — not independently benchmarked here.

## Executive summary

- **15 token-savings tools** in your stars (**311,195★**), split into **8 coding-focused** and **7 general-purpose**.
- **Coding is where the tokens are.** For coding agents the biggest sink is *reading the codebase* — so the highest-leverage tools index/search code (`semble`, `codegraph`) or tame tool output (`context-mode`).
- **The one integration-free win:** `rtk` (a CLI proxy) claims 60–90% with no per-agent setup — the best 'install once' option, and the most-starred (53,585★).
- **General tooling works at the format/data layer** (`toon` compact serialization, `dbhub` efficient DB access) and **composes** with the coding tools above.
- **Measure first:** `codeburn` shows where tokens actually go before you optimize.

## Comparison

### Coding-agent / codebase token savings

| Tool | ★ | Health | Activity | Mechanism | Claimed saving |
|---|---|---|---|---|---|
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 64,286 | 74 | very active | Prompt-style skill | ~65% |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | 53,585 | 78 | very active | Wire-level proxy | 60–90% on dev cmds |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 21,684 | 76 | very active | Code index/graph | ~70% |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | 15,558 | 80 | very active | Tool-output sandbox | 98% on tool output |
| [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | 6,995 | 79 | very active | Measurement / observability | — (measures) |
| [MinishLab/semble](https://github.com/MinishLab/semble) | 4,109 | 76 | very active | Semantic code search | ~98% vs grep+read |
| [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | 2,169 | 48 | slowing | Code understanding | qualitative |
| [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx) | 2,146 | 79 | very active | Context layer | qualitative |

### General / other token savings

| Tool | ★ | Health | Activity | Mechanism | Claimed saving |
|---|---|---|---|---|---|
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 77,829 | 79 | very active | Session compression | qualitative |
| [toon-format/toon](https://github.com/toon-format/toon) | 24,362 | 74 | very active | Compact data format | ~30–50% on structured data |
| [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) | 23,165 | 21 | slowing | Optical context compression | research |
| [davidkimai/Context-Engineering](https://github.com/davidkimai/Context-Engineering) | 9,007 | 38 | slowing | Methodology / guide | — (educational) |
| [vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor) | 3,280 | 84 | very active | Model weight compression | n/a (inference, not prompt) |
| [bytebase/dbhub](https://github.com/bytebase/dbhub) | 2,824 | 57 | active | Token-efficient DB access | qualitative |
| [iternal-technologies-partners/blockify-agentic-data-optimization](https://github.com/iternal-technologies-partners/blockify-agentic-data-optimization) | 196 | 41 | active | Data optimization (RAG) | qualitative |

## Details

### Coding

_Token savings aimed at coding agents (Claude Code, Codex, Cursor, OpenCode, Hermes) and codebase context — the largest token sink for most users._

- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 64,286★ · JavaScript · Hot · health 74 · _Prompt-style skill_ · **~65%**  
  Claude Code skill that trims tokens by emitting terse 'caveman' output — cheap to try, trades readability.  
  <sub>topics: ai, anthropic, caveman, claude, claude-code, llm</sub>
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 53,585★ · Rust · Hot · health 78 · _Wire-level proxy_ · **60–90% on dev cmds**  
  CLI proxy that intercepts common dev commands; integration-free 'install once, save everywhere'.  
  <sub>topics: agentic-coding, ai-coding, anthropic, claude-code, cli, command-line-tool</sub>
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 21,684★ · TypeScript · Hot · health 76 · _Code index/graph_ · **~70%**  
  Pre-indexed code knowledge graph for Claude Code/Codex/Cursor/OpenCode/Hermes — query instead of read.  
  <sub>topics: —</sub>
- **[mksglu/context-mode](https://github.com/mksglu/context-mode)** · 15,558★ · TypeScript · Hot · health 80 · _Tool-output sandbox_ · **98% on tool output**  
  Sandboxes/truncates tool output in the context window; 15 platforms.  
  <sub>topics: claude, claude-code, claude-code-plugins, mcp, skills, codex</sub>
- **[getagentseal/codeburn](https://github.com/getagentseal/codeburn)** · 6,995★ · TypeScript · Hot · health 79 · _Measurement / observability_ · **— (measures)**  
  TUI dashboard showing where your Claude Code/Codex/Cursor tokens go. Measure before you optimize.  
  <sub>topics: ai-coding, claude-code, cli, codex, cost-tracking, developer-tools</sub>
- **[MinishLab/semble](https://github.com/MinishLab/semble)** · 4,109★ · Python · Hot · health 76 · _Semantic code search_ · **~98% vs grep+read**  
  Fast, accurate code search for agents — replaces the grep+read pattern that dominates coding context.  
  <sub>topics: agents, code-search, embeddings, mcp, mcp-server, model-context-protocol</sub>
- **[HKUDS/FastCode](https://github.com/HKUDS/FastCode)** · 2,169★ · Python · Rising · health 48 · _Code understanding_ · **qualitative**  
  Accelerates/streamlines code understanding — but low health and stale; verify first.  
  <sub>topics: —</sub>
- **[yvgude/lean-ctx](https://github.com/yvgude/lean-ctx)** · 2,146★ · Rust · Hot · health 79 · _Context layer_ · **qualitative**  
  Cognitive context layer: 51+ MCP tools, multiple read modes, surgical reads (also in the MCP report).  
  <sub>topics: ai, cursor, llm, mcp, rust, token-optimization</sub>

### General

_Token / context savings that aren't coding-specific: data formats, DB access, session compression, model-weight & research approaches._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 77,829★ · TypeScript · Rising · health 79 · _Session compression_ · **qualitative**  
  Compresses & persists session context across runs (also in the Memory report).  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude</sub>
- **[toon-format/toon](https://github.com/toon-format/toon)** · 24,362★ · TypeScript · Hot · health 74 · _Compact data format_ · **~30–50% on structured data**  
  Token-Oriented Object Notation — schema-aware, human-readable replacement for JSON in prompts.  
  <sub>topics: data-format, llm, serialization, tokenization</sub>
- **[deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)** · 23,165★ · Python · Declining · health 21 · _Optical context compression_ · **research**  
  'Contexts Optical Compression' — renders context to images to fit more in window; low health & stale.  
  <sub>topics: —</sub>
- **[davidkimai/Context-Engineering](https://github.com/davidkimai/Context-Engineering)** · 9,007★ · Python · Declining · health 38 · _Methodology / guide_ · **— (educational)**  
  A guide to filling the context window with just the right info — concepts, not a tool; stale.  
  <sub>topics: —</sub>
- **[vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor)** · 3,280★ · Python · Hot · health 84 · _Model weight compression_ · **n/a (inference, not prompt)**  
  Compresses model *weights* for cheaper inference — different layer than prompt-token savings; included for contrast.  
  <sub>topics: compression, quantization</sub>
- **[bytebase/dbhub](https://github.com/bytebase/dbhub)** · 2,824★ · TypeScript · Hot · health 57 · _Token-efficient DB access_ · **qualitative**  
  Zero-dependency, token-efficient database MCP server (Postgres/MySQL/SQL Server/…).  
  <sub>topics: ai, anthropic, claude, database, mcp, mcp-server</sub>
- **[iternal-technologies-partners/blockify-agentic-data-optimization](https://github.com/iternal-technologies-partners/blockify-agentic-data-optimization)** · 196★ · Python · Declining · health 41 · _Data optimization (RAG)_ · **qualitative**  
  Replaces naive chunking with dense 'blocks' for enterprise RAG; declining/low health.  
  <sub>topics: —</sub>

## How to stack them

Because they hit different layers, a strong setup combines several:

| Your token sink | Reach for | Layer |
|---|---|---|
| Reading source code | `MinishLab/semble` or `colbymchenry/codegraph` | retrieval |
| Noisy tool / command output | `mksglu/context-mode` | tool output |
| Everything, no integration | `rtk-ai/rtk` | wire (proxy) |
| Structured data in prompts | `toon-format/toon` | format |
| Database queries | `bytebase/dbhub` | data access |
| Long multi-session work | `thedotmack/claude-mem` | session memory |
| Don't know yet | `getagentseal/codeburn` | measurement |

## Recommendations

**For coding agents (most people):**
1. `rtk-ai/rtk` — best general, integration-free reduction (60–90%, 53,585★, health 78).
2. `MinishLab/semble` (sharpest claim) or `colbymchenry/codegraph` (most adopted) — kill the read-the-codebase cost.
3. `mksglu/context-mode` — pair on top to tame tool output.

**General add-ons:**
- `toon-format/toon` if you feed structured data into prompts (format-level, composes with everything).
- `getagentseal/codeburn` first if you want evidence on where to focus.

## ⚠️ Adopt with caution

Low health and/or stale — verify before relying on:

| Tool | Scope | Health | Lifecycle | Last push |
|---|---|---|---|---|
| [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) | General | 21 | Declining | 3mo ago |
| [davidkimai/Context-Engineering](https://github.com/davidkimai/Context-Engineering) | General | 38 | Declining | 2mo ago |
| [iternal-technologies-partners/blockify-agentic-data-optimization](https://github.com/iternal-technologies-partners/blockify-agentic-data-optimization) | General | 41 | Declining | 1mo ago |
| [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | Coding | 48 | Rising | 2mo ago |

## Graph analysis — how they relate

**Community clustering.** These 15 tools span **9 of the graph's 23 communities** — token-savings is a cross-cutting concern, not a single cluster.

- **Community 10** (3): `getagentseal/codeburn`, `HKUDS/FastCode`, `thedotmack/claude-mem`
- **Community 0** (2): `rtk-ai/rtk`, `colbymchenry/codegraph`
- **Community 6** (2): `mksglu/context-mode`, `JuliusBrussee/caveman`
- **Community 15** (2): `toon-format/toon`, `vllm-project/llm-compressor`
- **Community 5** (2): `iternal-technologies-partners/blockify-agentic-data-optimization`, `davidkimai/Context-Engineering`

**Centrality (PageRank in the full 1,071-repo graph):**

- `colbymchenry/codegraph` — PageRank 0.0025
- `HKUDS/FastCode` — PageRank 0.0017
- `yvgude/lean-ctx` — PageRank 0.0015
- `mksglu/context-mode` — PageRank 0.0014
- `vllm-project/llm-compressor` — PageRank 0.0010
- `rtk-ai/rtk` — PageRank 0.0009
- `deepseek-ai/DeepSeek-OCR` — PageRank 0.0009
- `JuliusBrussee/caveman` — PageRank 0.0008

**Direct links between these tools** (similarity edges where both endpoints are in this report):

- `yvgude/lean-ctx` ⇄ `rtk-ai/rtk` (w=0.368) — topics: llm, rust, token-optimization, agentic-coding
- `getagentseal/codeburn` ⇄ `rtk-ai/rtk` (w=0.211) — topics: ai-coding, claude-code, cli, developer-tools
- `colbymchenry/codegraph` ⇄ `mksglu/context-mode` (w=0.111) — authors: Baijack-star

## Methodology & caveats

- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: scan for token / context-window / compression signals (and explicit `NN% fewer/less` claims) across name/description/topics/README, then manual curation into Coding vs General and by mechanism.
- **% savings are vendor-claimed**, measured on the projects' own workloads — not verified here. Real savings depend heavily on *your* usage pattern.
- **Metrics** (health, lifecycle, days_since_push) are precomputed at snapshot time and may lag GitHub. Re-run after a fresh `classified.json` to refresh.

<sub>Tools covered: 15 (8 coding / 7 general) · Snapshot: 2026-05-24T19:57:47.245Z</sub>
