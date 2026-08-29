# Token-Savings & Context-Efficiency Tooling

> Derived from **kaiser-data**'s 1,859 starred repos (snapshot `2026-08-29T23:54:34.573Z`), cross-referenced with the repo-similarity graph (1,859 nodes / 6,070 edges, 37 communities).
>
> Generated 2026-08-29 by `scripts/reports/token_savings.py` (regenerate any time — no API cost).

![Top tools by stars](assets/token-savings-top-tools.svg)

![Tools per category](assets/token-savings-categories.svg)


> **Read this first:** the right token-saver depends on **what you're spending tokens on** — reading code, generating structured output, retrieving documents, or carrying long-session memory. So this report is organized **by workload**, not by tool type. Tools at different layers mostly **compose** rather than compete. All **% figures are the projects' own claims** on the May-2026 snapshot — not independently benchmarked here.

## Executive summary

- **15 token-savings tools** in your stars (**447,359★**), organized by workload:
  - **Coding agents & codebases** (8): `caveman`, `rtk`, `codegraph`, `context-mode`, `codeburn`, `semble`, `lean-ctx`, `FastCode`
  - **Generation & structured prompting** (1): `toon`
  - **Retrieval, RAG & documents** (3): `DeepSeek-OCR`, `dbhub`, `blockify-agentic-data-optimization`
  - **Long-running agents & memory** (1): `claude-mem`
  - **Model & inference level** (1): `llm-compressor`
  - **Methodology / cross-cutting** (1): `Context-Engineering`
- **Your collection skews hard to coding** — 8 of 15 tools. The big coding sink is *reading the codebase*, so the highest-leverage picks index/search code (`semble`, `codegraph`) or tame tool output (`context-mode`).
- **Different workload, different layer:** generation savings live in the *prompt/format* (`toon`); retrieval savings in *what you fetch* (`dbhub`, `blockify`); long agents in *session memory* (`claude-mem`); and model-level compression (`llm-compressor`) is a separate concern entirely (cheaper inference, not fewer prompt tokens).
- **The one integration-free win:** `rtk` (a CLI proxy) claims 60–90% with no per-agent setup — and it's the most-starred here (77,635★).
- **Measure first:** `codeburn` shows where tokens actually go before you optimize.

## Comparison by workload

### Coding agents & codebases

| Tool | ★ | Health | Activity | Mechanism | Claimed saving |
|---|---|---|---|---|---|
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 101,440 | 75 | very active | Prompt-style skill | ~65% |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | 77,635 | 78 | very active | Wire-level proxy | 60–90% on dev cmds |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 68,386 | 77 | very active | Code index/graph | ~70% |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | 20,195 | 78 | very active | Tool-output sandbox | 98% on tool output |
| [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | 9,691 | 79 | very active | Measurement / observability | — (measures) |
| [MinishLab/semble](https://github.com/MinishLab/semble) | 5,964 | 73 | very active | Semantic code search | ~98% vs grep+read |
| [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx) | 3,662 | 80 | very active | Context layer | qualitative |
| [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | 2,292 | 40 | active | Code understanding | qualitative |

### Generation & structured prompting

| Tool | ★ | Health | Activity | Mechanism | Claimed saving |
|---|---|---|---|---|---|
| [toon-format/toon](https://github.com/toon-format/toon) | 25,267 | 79 | very active | Compact data format | ~30–50% on structured data |

### Retrieval, RAG & documents

| Tool | ★ | Health | Activity | Mechanism | Claimed saving |
|---|---|---|---|---|---|
| [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) | 23,855 | 13 | stale | Optical context compression | research |
| [bytebase/dbhub](https://github.com/bytebase/dbhub) | 3,417 | 76 | very active | Token-efficient DB access | qualitative |
| [iternal-technologies-partners/blockify-agentic-data-optimization](https://github.com/iternal-technologies-partners/blockify-agentic-data-optimization) | 313 | 24 | slowing | Data optimization (RAG) | qualitative |

### Long-running agents & memory

| Tool | ★ | Health | Activity | Mechanism | Claimed saving |
|---|---|---|---|---|---|
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 92,280 | 79 | very active | Session compression | qualitative |

### Model & inference level

| Tool | ★ | Health | Activity | Mechanism | Claimed saving |
|---|---|---|---|---|---|
| [vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor) | 3,734 | 89 | very active | Model weight compression | n/a (inference, not prompt) |

### Methodology / cross-cutting

| Tool | ★ | Health | Activity | Mechanism | Claimed saving |
|---|---|---|---|---|---|
| [jasontang-ai/Context-Engineering](https://github.com/jasontang-ai/Context-Engineering) | 9,228 | 23 | stale | Methodology / guide | — (educational) |

## Details

### Coding agents & codebases

_Claude Code, Codex, Cursor, OpenCode, Hermes — the biggest token sink for most users, dominated by reading/searching source and tool output._

- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 101,440★ · Go · Hot · health 75 · _Prompt-style skill_ · **~65%**  
  Claude Code skill that trims tokens by emitting terse 'caveman' output — cheap to try, trades readability.  
  <sub>topics: ai, anthropic, caveman, claude, claude-code, llm</sub>
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 77,635★ · Rust · Hot · health 78 · _Wire-level proxy_ · **60–90% on dev cmds**  
  CLI proxy that intercepts common dev commands; integration-free 'install once, save everywhere'.  
  <sub>topics: agentic-coding, ai-coding, anthropic, claude-code, cli, command-line-tool</sub>
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 68,386★ · C · Hot · health 77 · _Code index/graph_ · **~70%**  
  Pre-indexed code knowledge graph for Claude Code/Codex/Cursor/OpenCode/Hermes — query instead of read.  
  <sub>topics: —</sub>
- **[mksglu/context-mode](https://github.com/mksglu/context-mode)** · 20,195★ · TypeScript · Rising · health 78 · _Tool-output sandbox_ · **98% on tool output**  
  Sandboxes/truncates tool output in the context window; 15 platforms.  
  <sub>topics: claude, claude-code, claude-code-plugins, mcp, skills, codex</sub>
- **[getagentseal/codeburn](https://github.com/getagentseal/codeburn)** · 9,691★ · TypeScript · Hot · health 79 · _Measurement / observability_ · **— (measures)**  
  TUI dashboard showing where your Claude Code/Codex/Cursor tokens go. Measure before you optimize.  
  <sub>topics: ai-coding, claude-code, cli, codex, cost-tracking, developer-tools</sub>
- **[MinishLab/semble](https://github.com/MinishLab/semble)** · 5,964★ · Python · Hot · health 73 · _Semantic code search_ · **~98% vs grep+read**  
  Fast, accurate code search for agents — replaces the grep+read pattern that dominates coding context.  
  <sub>topics: agents, code-search, embeddings, mcp, mcp-server, model-context-protocol</sub>
- **[yvgude/lean-ctx](https://github.com/yvgude/lean-ctx)** · 3,662★ · Rust · Rising · health 80 · _Context layer_ · **qualitative**  
  Cognitive context layer: 51+ MCP tools, multiple read modes, surgical reads (also in the MCP report).  
  <sub>topics: ai, cursor, llm, mcp, rust, token-optimization</sub>
- **[HKUDS/FastCode](https://github.com/HKUDS/FastCode)** · 2,292★ · Python · Declining · health 40 · _Code understanding_ · **qualitative**  
  Accelerates/streamlines code understanding — but low health and stale; verify first.  
  <sub>topics: —</sub>

### Generation & structured prompting

_When you feed data into prompts or ask for structured output — savings come from a tighter serialization format._

- **[toon-format/toon](https://github.com/toon-format/toon)** · 25,267★ · TypeScript · Hot · health 79 · _Compact data format_ · **~30–50% on structured data**  
  Token-Oriented Object Notation — schema-aware, human-readable replacement for JSON when you feed data into prompts or ask for structured output. Cross-cutting, but lives at the generation/prompt layer.  
  <sub>topics: data-format, llm, serialization, tokenization</sub>

### Retrieval, RAG & documents

_When tokens go to fetched context — keep what you retrieve small and dense._

- **[deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)** · 23,855★ · Python · Declining · health 13 · _Optical context compression_ · **research**  
  'Contexts Optical Compression' — renders document context to images to fit more in window; low health & stale.  
  <sub>topics: —</sub>
- **[bytebase/dbhub](https://github.com/bytebase/dbhub)** · 3,417★ · TypeScript · Hot · health 76 · _Token-efficient DB access_ · **qualitative**  
  Zero-dependency, token-efficient database MCP server (Postgres/MySQL/SQL Server/…) — keeps query results lean.  
  <sub>topics: ai, anthropic, claude, database, mcp, mcp-server</sub>
- **[iternal-technologies-partners/blockify-agentic-data-optimization](https://github.com/iternal-technologies-partners/blockify-agentic-data-optimization)** · 313★ · Python · Declining · health 24 · _Data optimization (RAG)_ · **qualitative**  
  Replaces naive chunking with dense 'blocks' so retrieved context is smaller; declining/low health.  
  <sub>topics: —</sub>

### Long-running agents & memory

_Multi-session work where re-sending history is the cost — compress and persist instead._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 92,280★ · JavaScript · Rising · health 79 · _Session compression_ · **qualitative**  
  Compresses & persists session context across runs so long projects don't re-pay for history (also in the Memory report).  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude</sub>

### Model & inference level

_A different layer: shrink the *model* for cheaper inference (doesn't reduce your prompt tokens)._

- **[vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor)** · 3,734★ · Python · Mature · health 89 · _Model weight compression_ · **n/a (inference, not prompt)**  
  Compresses model *weights* for cheaper/faster inference — a different layer than prompt-token savings; included for contrast.  
  <sub>topics: compression, quantization</sub>

### Methodology / cross-cutting

_Principles that apply across every workload above._

- **[jasontang-ai/Context-Engineering](https://github.com/jasontang-ai/Context-Engineering)** · 9,228★ · Python · Declining · health 23 · _Methodology / guide_ · **— (educational)**  
  A guide to filling the context window with just the right info — concepts that apply to every workload above; stale.  
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
1. `rtk-ai/rtk` — best general, integration-free reduction (60–90%, 77,635★, health 78).
2. `MinishLab/semble` (sharpest claim) or `colbymchenry/codegraph` (most adopted) — kill the read-the-codebase cost.
3. `mksglu/context-mode` — pair on top to tame tool output.

**General add-ons:**
- `toon-format/toon` if you feed structured data into prompts (format-level, composes with everything).
- `getagentseal/codeburn` first if you want evidence on where to focus.

## ⚠️ Adopt with caution

Low health and/or stale — verify before relying on:

| Tool | Workload | Health | Lifecycle | Last push |
|---|---|---|---|---|
| [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) | Retrieval, RAG & documents | 13 | Declining | 7mo ago |
| [jasontang-ai/Context-Engineering](https://github.com/jasontang-ai/Context-Engineering) | Methodology / cross-cutting | 23 | Declining | 6mo ago |
| [iternal-technologies-partners/blockify-agentic-data-optimization](https://github.com/iternal-technologies-partners/blockify-agentic-data-optimization) | Retrieval, RAG & documents | 24 | Declining | 4mo ago |
| [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | Coding agents & codebases | 40 | Declining | 1mo ago |

## Graph analysis — how they relate

**Community clustering.** These 15 tools span **10 of the graph's 37 communities** — token-savings is a cross-cutting concern, not a single cluster.

- **Community 12** (3): `rtk-ai/rtk`, `yvgude/lean-ctx`, `thedotmack/claude-mem`
- **Community 9** (3): `colbymchenry/codegraph`, `mksglu/context-mode`, `JuliusBrussee/caveman`
- **Community 1** (2): `iternal-technologies-partners/blockify-agentic-data-optimization`, `jasontang-ai/Context-Engineering`

**Centrality (PageRank in the full 1,071-repo graph):**

- `mksglu/context-mode` — PageRank 0.0057
- `JuliusBrussee/caveman` — PageRank 0.0009
- `vllm-project/llm-compressor` — PageRank 0.0006
- `deepseek-ai/DeepSeek-OCR` — PageRank 0.0005
- `bytebase/dbhub` — PageRank 0.0004
- `rtk-ai/rtk` — PageRank 0.0004
- `HKUDS/FastCode` — PageRank 0.0004
- `yvgude/lean-ctx` — PageRank 0.0004

**Direct links between these tools** (similarity edges where both endpoints are in this report):

- `JuliusBrussee/caveman` ⇄ `mksglu/context-mode` (w=0.738) — topics: claude, claude-code; authors: github-actions[bot]
- `colbymchenry/codegraph` ⇄ `mksglu/context-mode` (w=0.400) — authors: github-actions[bot]
- `yvgude/lean-ctx` ⇄ `rtk-ai/rtk` (w=0.330) — topics: llm, rust, token-optimization, agentic-coding

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: scan for token / context-window / compression signals (and explicit `NN% fewer/less` claims) across name/description/topics/README, then manual curation into Coding vs General and by mechanism.
- **% savings are vendor-claimed**, measured on the projects' own workloads — not verified here. Real savings depend heavily on *your* usage pattern.
- **Metrics** (health, lifecycle, days_since_push) are precomputed at snapshot time and may lag GitHub. Re-run after a fresh `classified.json` to refresh.

<sub>Tools covered: 15 across 6 workloads · Snapshot: 2026-08-29T23:54:34.573Z</sub>
