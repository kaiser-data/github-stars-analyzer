# Claude Code Superpowers — Setup Strategies from Your Stars

> Derived from **kaiser-data**'s 1,243 starred repos (snapshot `2026-06-11T21:58:33.384Z`), cross-referenced with the repo-similarity graph (1,243 nodes / 4,017 edges, 31 communities).
>
> Generated 2026-06-29 by `scripts/reports/claude_code_setups.py` (regenerate any time — no API cost).

## The big idea

A modern Claude Code setup is **layered**, and the 2026 superpower is *on-demand context*, not a big always-loaded instruction blob. A harness runs the loop; **skills** and config shape behavior only when triggered; **memory** persists context across sessions; **token-savers** compress what the model sees; **code-graph/retrieval** feeds it the right code; **MCP** adds reach; **observability** measures it; **local runtimes** cut cost. Your stars already contain a best-in-class tool for every one of those layers — this report assembles them into three ready-to-run strategies.

## Three setup strategies (built from your stars)

| Layer | 🟢 Token-saver | 🟡 Balanced (recommended) | 🔴 Max-performance |
|---|---|---|---|
| **Harness** | `claude-code` (Sonnet) | `claude-code` (Sonnet→Opus on hard tasks) | `claude-code` (Opus) + `cc-switch` to model-shop |
| **Skills** | `caveman` (trim) + 1–2 essentials | `obra/superpowers` + `anthropics/skills` | `superpowers` + `wshobson/agents` + vertical packs |
| **Config** | one lean `CLAUDE.md` (karpathy-skills) | `claude-code-templates` (configure+monitor) | `gstack` / `centminmod` full kit |
| **Memory** | off / minimal | `claude-mem` (you run this) | `claude-mem` + `mem0` backend |
| **Token-saver** | `rtk` proxy + `semble` search + `headroom` | `semble` for code search; `codeburn` to watch spend | `codeburn` dashboard; spend where it pays |
| **Code-graph** | `graphify` (AST, no API) | `graphify` / `codegraph` | `codegraph` + `codebase-memory-mcp` |
| **MCP** | none global | `context7` (live docs) | `context7` + curated from `awesome-mcp-servers` |
| **Observability** | skip | `langfuse` (you wire this) | `langfuse` + `opik`/`phoenix` evals |
| **Local runtime** | `ollama` for grunt work | `litellm` gateway, escalate to cloud | cloud frontier; `litellm` for fallback |

**One-line verdict:** the *token-saver* and *max-performance* columns share the same backbone — a lean harness, on-demand skills, and a clean context. They differ mainly in *model tier* and *how many measurement/eval layers* you bolt on. The expensive mistake is the same in both: front-loading instructions the model only half-reads.

## Executive summary

- **58 Claude-Code 'superpower' projects** in your stars (**4,132,599★** combined), spanning 9 setup layers:
  - **Harness / coding agent** (12): `openclaw`, `hermes-agent`, `opencode`, `claude-code`, `gemini-cli`, `codex`, `deer-flow`, `cline`, `pi`, `ruflo`, `goose`, `oh-my-claudecode`
  - **Skills framework** (7): `superpowers`, `ECC`, `skills`, `awesome-claude-skills`, `antigravity-awesome-skills`, `agents`, `scientific-agent-skills`
  - **Config / setup kit** (11): `andrej-karpathy-skills`, `system-prompts-and-models-of-ai-tools`, `gstack`, `cc-switch`, `claude-code-best-practice`, `awesome-claude-code`, `claude-cookbooks`, `claude-howto`, `claude-code-templates`, `claude-code-system-prompts`, `my-claude-code-setup`
  - **Memory / context** (7): `claude-mem`, `mem0`, `mempalace`, `memvid`, `byterover-cli`, `engram`, `Acontext`
  - **Token-saver / compression** (7): `caveman`, `oh-my-openagent`, `rtk`, `toon`, `headroom`, `codeburn`, `semble`
  - **Code-graph / retrieval** (5): `graphify`, `Understand-Anything`, `codegraph`, `GitNexus`, `codebase-memory-mcp`
  - **MCP ecosystem** (3): `awesome-mcp-servers`, `servers`, `context7`
  - **Observability / evals** (4): `langfuse`, `opik`, `phoenix`, `openllmetry`
  - **Local runtime** (2): `ollama`, `litellm`
- **Skills are the leverage point.** `obra/superpowers` (the most-starred repo in this whole set) and `anthropics/skills` replace most always-on `CLAUDE.md` prose with on-demand expertise — cheaper *and* sharper.
- **Token-saving is now a stack, not a setting.** A proxy (`rtk`), a leaner code-search (`semble`, ~98% fewer tokens than reading files), output compression (`headroom`), and a spend dashboard (`codeburn`) compose into 60–90% reductions on real dev loops.
- **You already run three layers well** — `claude-mem` (memory), `graphify` (code-graph), and `langfuse` (observability) — plus `context7` over MCP. The gap is a **skills framework** and a deliberate **model-tier policy**.

## The setup, layer by layer

| Layer | What it buys you | Your starred picks |
|---|---|---|
| **Harness / coding agent** | The agent loop itself | `openclaw`, `hermes-agent`, `opencode`, `claude-code`, `gemini-cli`, `codex` |
| **Skills framework** | On-demand expertise (the modern superpower) | `superpowers`, `ECC`, `skills`, `awesome-claude-skills`, `antigravity-awesome-skills`, `agents` |
| **Config / setup kit** | Shape behavior up front, cheaply | `andrej-karpathy-skills`, `system-prompts-and-models-of-ai-tools`, `gstack`, `cc-switch`, `claude-code-best-practice`, `awesome-claude-code` |
| **Memory / context** | Persist context across sessions | `claude-mem`, `mem0`, `mempalace`, `memvid`, `byterover-cli`, `engram` |
| **Token-saver / compression** | Shrink what the model has to read | `caveman`, `oh-my-openagent`, `rtk`, `toon`, `headroom`, `codeburn` |
| **Code-graph / retrieval** | Feed the *right* code, not all of it | `graphify`, `Understand-Anything`, `codegraph`, `GitNexus`, `codebase-memory-mcp` |
| **MCP ecosystem** | External reach (docs, tools, data) | `awesome-mcp-servers`, `servers`, `context7` |
| **Observability / evals** | Measure cost & quality | `langfuse`, `opik`, `phoenix`, `openllmetry` |
| **Local runtime** | Cut cost / go offline | `ollama`, `litellm` |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Layer | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Harness / coding agent | TypeScript | NOASSERTION | 378,215 | Hot | 84 | very active | 0d ago | 6mo | 33 |
| [obra/superpowers](https://github.com/obra/superpowers) | Skills framework | Shell | MIT | 224,734 | Hot | 71 | very active | 0d ago | 8mo | 9 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Skills framework | JavaScript | MIT | 213,434 | Hot | 100 | very active | 0d ago | 4mo | 44 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Harness / coding agent | Python | MIT | 190,933 | Hot | 79 | very active | 0d ago | 10mo | 22 |
| [ollama/ollama](https://github.com/ollama/ollama) | Local runtime | Go | MIT | 173,893 | Mature | 88 | very active | 0d ago | 3.0y | 12 |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Config / setup kit | — | — | 173,480 | Mature | 42 | active | 1mo ago | 4mo | 3 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | Harness / coding agent | TypeScript | MIT | 173,200 | Hot | 87 | very active | 0d ago | 1.1y | 21 |
| [anthropics/skills](https://github.com/anthropics/skills) | Skills framework | Python | — | 149,487 | Rising | 46 | active | 2d ago | 8mo | 6 |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Config / setup kit | — | GPL-3.0 | 139,839 | Mature | 50 | active | 3d ago | 1.3y | 2 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Harness / coding agent | Python | — | 131,796 | Hot | 77 | very active | 1d ago | 1.3y | 11 |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Config / setup kit | TypeScript | MIT | 109,211 | Rising | 60 | very active | 1d ago | 3mo | 1 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Harness / coding agent | TypeScript | Apache-2.0 | 105,171 | Hot | 99 | very active | 0d ago | 1.2y | 40 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Config / setup kit | Rust | MIT | 98,479 | Hot | 77 | very active | 0d ago | 10mo | 38 |
| [openai/codex](https://github.com/openai/codex) | Harness / coding agent | Rust | Apache-2.0 | 90,458 | Hot | 96 | very active | 0d ago | 1.2y | 32 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP ecosystem | — | MIT | 88,887 | Hot | 65 | very active | 0d ago | 1.5y | 7 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | MCP ecosystem | TypeScript | NOASSERTION | 87,070 | Hot | 85 | very active | 4d ago | 1.6y | 17 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Memory / context | JavaScript | Apache-2.0 | 81,818 | Hot | 80 | very active | 0d ago | 9mo | 18 |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Token-saver / compression | JavaScript | MIT | 71,515 | Hot | 72 | very active | 22d ago | 2mo | 13 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Harness / coding agent | Python | MIT | 70,988 | Hot | 81 | very active | 0d ago | 1.1y | 27 |
| [safishamsi/graphify](https://github.com/safishamsi/graphify) | Code-graph / retrieval | Python | MIT | 65,604 | Hot | 78 | very active | 0d ago | 2mo | 12 |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Skills framework | Python | — | 64,193 | Rising | 65 | very active | 21d ago | 7mo | 17 |
| [cline/cline](https://github.com/cline/cline) | Harness / coding agent | TypeScript | Apache-2.0 | 63,059 | Hot | 79 | very active | 0d ago | 1.9y | 14 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Token-saver / compression | TypeScript | NOASSERTION | 61,925 | Hot | 78 | very active | 0d ago | 6mo | 3 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness / coding agent | TypeScript | MIT | 61,778 | Hot | 80 | very active | 0d ago | 10mo | 14 |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Token-saver / compression | Rust | Apache-2.0 | 61,471 | Hot | 73 | very active | 2d ago | 4mo | 12 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Harness / coding agent | TypeScript | MIT | 58,993 | Hot | 77 | very active | 0d ago | 1.0y | 8 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Memory / context | Python | Apache-2.0 | 58,361 | Mature | 94 | very active | 0d ago | 3.0y | 30 |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Config / setup kit | HTML | MIT | 57,446 | Rising | 65 | very active | 0d ago | 7mo | 2 |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | Code-graph / retrieval | TypeScript | MIT | 57,345 | Hot | 75 | very active | 1d ago | 2mo | 20 |
| [upstash/context7](https://github.com/upstash/context7) | MCP ecosystem | TypeScript | MIT | 57,189 | Hot | 85 | very active | 0d ago | 1.2y | 15 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Memory / context | Python | MIT | 55,384 | Hot | 76 | very active | 1d ago | 2mo | 14 |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Local runtime | Python | NOASSERTION | 50,082 | Mature | 89 | very active | 0d ago | 2.9y | 10 |
| [aaif-goose/goose](https://github.com/aaif-goose/goose) | Harness / coding agent | Rust | Apache-2.0 | 48,887 | Hot | 94 | very active | 0d ago | 1.8y | 32 |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | Code-graph / retrieval | TypeScript | MIT | 47,422 | Hot | 78 | very active | 0d ago | 4mo | 9 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Config / setup kit | Python | NOASSERTION | 46,209 | Mature | 58 | active | 1mo ago | 1.1y | 2 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Config / setup kit | Jupyter Notebook | MIT | 45,305 | Mature | 75 | very active | 2d ago | 2.8y | 19 |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | Code-graph / retrieval | TypeScript | NOASSERTION | 41,960 | Hot | 82 | very active | 0d ago | 10mo | 18 |
| [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | Skills framework | Python | MIT | 40,386 | Hot | 85 | very active | 1d ago | 4mo | 20 |
| [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | Config / setup kit | Python | MIT | 36,870 | Hot | 76 | very active | 2d ago | 7mo | 19 |
| [wshobson/agents](https://github.com/wshobson/agents) | Skills framework | Python | MIT | 36,637 | Hot | 69 | very active | 4d ago | 10mo | 14 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Harness / coding agent | TypeScript | MIT | 36,221 | Hot | 80 | very active | 0d ago | 5mo | 8 |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Observability / evals | TypeScript | NOASSERTION | 28,929 | Classic | 89 | very active | 0d ago | 3.1y | 18 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Skills framework | Python | MIT | 27,973 | Hot | 79 | very active | 0d ago | 7mo | 12 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Config / setup kit | Python | MIT | 27,960 | Hot | 80 | very active | 1d ago | 11mo | 15 |
| [toon-format/toon](https://github.com/toon-format/toon) | Token-saver / compression | TypeScript | MIT | 24,534 | Hot | 71 | very active | 20d ago | 7mo | 6 |
| [chopratejas/headroom](https://github.com/chopratejas/headroom) | Token-saver / compression | Python | Apache-2.0 | 23,068 | Hot | 95 | very active | 0d ago | 5mo | 35 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Observability / evals | Python | Apache-2.0 | 19,579 | Classic | 99 | very active | 0d ago | 3.1y | 21 |
| [memvid/memvid](https://github.com/memvid/memvid) | Memory / context | Rust | Apache-2.0 | 15,642 | Mature | 64 | active | 15d ago | 1.0y | 3 |
| [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | Config / setup kit | JavaScript | MIT | 10,952 | Rising | 77 | very active | 0d ago | 6mo | 1 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Observability / evals | Python | NOASSERTION | 10,100 | Classic | 84 | very active | 0d ago | 3.6y | 15 |
| [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | Token-saver / compression | TypeScript | MIT | 7,879 | Hot | 79 | very active | 0d ago | 1mo | 13 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Observability / evals | Python | Apache-2.0 | 7,190 | Mature | 84 | very active | 1d ago | 2.8y | 15 |
| [MinishLab/semble](https://github.com/MinishLab/semble) | Token-saver / compression | Python | MIT | 5,070 | Hot | 77 | very active | 7d ago | 2mo | 5 |
| [campfirein/byterover-cli](https://github.com/campfirein/byterover-cli) | Memory / context | TypeScript | NOASSERTION | 4,844 | Hot | 84 | very active | 8d ago | 11mo | 8 |
| [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram) | Memory / context | Go | MIT | 4,292 | Hot | 77 | very active | 13d ago | 3mo | 3 |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | Memory / context | JavaScript | Apache-2.0 | 3,524 | Hot | 78 | very active | 2d ago | 11mo | 4 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Code-graph / retrieval | C | MIT | 3,317 | Rising | 78 | very active | 0d ago | 3mo | 2 |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | Config / setup kit | Python | MIT | 2,411 | Rising | 58 | very active | 1d ago | 11mo | 1 |

## By layer

### Harness / coding agent

_The loop that reads, plans, edits, and runs. Pick one as your daily driver; keep a second installed to diff behavior and model-shop._

- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · 378,215★ · TypeScript · Hot  
  Cross-platform personal-assistant harness — an 'any OS, any platform' agent runtime.  
  <sub>topics: ai, assistant, own-your-data, personal, crustacean, molty, openclaw</sub>
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 190,933★ · Python · Hot  
  Long-lived 'agent that grows with you' harness — persistent, personalized agent loop.  
  <sub>topics: ai, ai-agent, ai-agents, llm, anthropic, chatgpt, claude, claude-code</sub>
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 173,200★ · TypeScript · Hot  
  Open-source terminal coding agent — a provider-agnostic alternative harness.  
  <sub>topics: —</sub>
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 131,796★ · Python · Hot  
  Claude Code itself — the agentic CLI that lives in your terminal; the baseline every setup here extends.  
  <sub>topics: —</sub>
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 105,171★ · TypeScript · Hot  
  Gemini's open-source terminal agent — the third major CLI harness; handy for model-shopping.  
  <sub>topics: gemini, gemini-api, ai, ai-agents, cli, mcp-client, mcp-server</sub>
- **[openai/codex](https://github.com/openai/codex)** · 90,458★ · Rust · Hot  
  OpenAI's lightweight terminal coding agent — useful as a second harness to diff behavior against Claude Code.  
  <sub>topics: —</sub>
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 70,988★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and writes — multi-step autonomy.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[cline/cline](https://github.com/cline/cline)** · 63,059★ · TypeScript · Hot  
  Autonomous coding agent as SDK / IDE extension / CLI — strong for in-editor agentic workflows.  
  <sub>topics: —</sub>
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 61,778★ · TypeScript · Hot  
  Unified LLM-API + agent-loop + TUI toolkit — a kit for rolling your own coding agent.  
  <sub>topics: —</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 58,993★ · TypeScript · Hot  
  Agent meta-harness for Claude — deploys multi-agent swarms with coordination.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-rag, agentic-workflow, autonomous-agents, codex</sub>
- **[aaif-goose/goose](https://github.com/aaif-goose/goose)** · 48,887★ · Rust · Hot  
  Extensible open agent that installs and runs tools, not just suggestions — MCP-native.  
  <sub>topics: mcp, acp, ai, ai-agents</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 36,221★ · TypeScript · Hot  
  Teams-first multi-agent orchestration layer for Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>

### Skills framework

_The biggest 2026 upgrade. Skills load only when triggered, so they add capability without taxing every session — the opposite of a big always-on CLAUDE.md._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 224,734★ · Shell · Hot  
  Agentic skills framework + dev methodology — the headline 'give your agent superpowers' skill collection.  
  <sub>topics: —</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 213,434★ · JavaScript · Hot  
  Agent-harness performance system bundling skills, instincts, and memory into one optimization layer.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[anthropics/skills](https://github.com/anthropics/skills)** · 149,487★ · Python · Rising  
  Anthropic's official Agent Skills repo — canonical examples of the skills format.  
  <sub>topics: agent-skills</sub>
- **[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** · 64,193★ · Python · Rising  
  Curated index of Claude Skills + tooling — the discovery hub for what's worth installing.  
  <sub>topics: claude, claude-code, agent-skills, ai-agents, antigravity, automation, codex, composio</sub>
- **[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)** · 40,386★ · Python · Hot  
  Installable library of 1,500+ agentic skills across Claude Code/Cursor/etc.  
  <sub>topics: agentic-skills, ai-agents, antigravity, claude-code, mcp, ai-workflows, codex-cli, developer-tools</sub>
- **[wshobson/agents](https://github.com/wshobson/agents)** · 36,637★ · Python · Hot  
  Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor) — subagents & commands.  
  <sub>topics: agents, anthropic, automation, workflows, orchestration, agent-skills, agentic-ai, ai-agents</sub>
- **[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)** · 27,973★ · Python · Hot  
  Domain skill pack that turns an agent into a research scientist — example of vertical skills.  
  <sub>topics: ai-scientist, bioinformatics, chemoinformatics, claude, claude-skills, claudecode, clinical-research, computational-biology</sub>

### Config / setup kit

_Turnkey CLAUDE.md / command / hook bundles. Steal a good one, then trim to what you actually use — bloat here is paid on every prompt._

- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 173,480★ · — · Mature  
  A single CLAUDE.md derived from Karpathy's habits — the 'one good config file' approach.  
  <sub>topics: —</sub>
- **[x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)** · 139,839★ · — · Mature  
  Leaked/collected system prompts of major AI coding tools — prompt-engineering reference.  
  <sub>topics: ai, cursor, lovable, system-prompts, v0, cursorai, devin, replit</sub>
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 109,211★ · TypeScript · Rising  
  Garry Tan's exact Claude Code setup — 23 opinionated tools as a turnkey starting point.  
  <sub>topics: —</sub>
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 98,479★ · Rust · Hot  
  Desktop all-in-one for managing Claude Code/Codex/OpenClaw — swap providers & configs fast.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, typescript, codex</sub>
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 57,446★ · HTML · Rising  
  Best-practices collection: vibe-coding → agentic engineering.  
  <sub>topics: claude-ai, claude-code, best-practices, claude, claude-code-best-practices, agentic-engineering, anthropic, claude-code-agents</sub>
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 46,209★ · Python · Mature  
  The awesome-list for Claude Code skills, hooks, slash-commands, and orchestrators.  
  <sub>topics: anthropic, anthropic-claude, awesome, awesome-list, awesome-lists, awesome-resources, claude, claude-code</sub>
- **[anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)** · 45,305★ · Jupyter Notebook · Mature  
  Official recipes/notebooks for effective Claude usage patterns.  
  <sub>topics: —</sub>
- **[luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)** · 36,870★ · Python · Hot  
  Visual, example-driven guide to Claude Code from basics to advanced — the learning path.  
  <sub>topics: claude-code, guide, tutorial</sub>
- **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** · 27,960★ · Python · Hot  
  CLI to configure AND monitor Claude Code — installs commands/agents/hooks and watches usage.  
  <sub>topics: anthropic, anthropic-claude, claude, claude-code</sub>
- **[Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts)** · 10,952★ · JavaScript · Rising  
  Claude Code's full system prompt + 27 builtin tool descriptions — know what you're configuring.  
  <sub>topics: claude-code, claude-code-system-prompts, system-prompts</sub>
- **[centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup)** · 2,411★ · Python · Rising  
  A shared starter CLAUDE.md + memory-bank configuration template you can fork.  
  <sub>topics: claude, claude-ai, claude-code, subagents, claudecode-config, claudecode-hooks, claudecode-subagents</sub>

### Memory / context

_Persist decisions and context across sessions so the agent doesn't re-derive what it already learned. The backend is swappable._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 81,818★ · JavaScript · Hot  
  Persistent context across sessions for every agent — captures work and re-injects it (you run this).  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude, claude-agent-sdk, claude-agents</sub>
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 58,361★ · Python · Mature  
  Universal memory layer for AI agents — the most-adopted general memory backend.  
  <sub>topics: ai, chatgpt, llm, python, chatbots, rag, application, long-term-memory</sub>
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 55,384★ · Python · Hot  
  Best-benchmarked open-source AI memory system — drop-in long-term memory.  
  <sub>topics: ai, chromadb, llm, mcp, memory, python</sub>
- **[memvid/memvid](https://github.com/memvid/memvid)** · 15,642★ · Rust · Mature  
  Memory layer that replaces RAG pipelines with a compact server — novel storage approach.  
  <sub>topics: ai, context, embedded, faiss, knowledge-base, knowledge-graph, llm, machine-learning</sub>
- **[campfirein/byterover-cli](https://github.com/campfirein/byterover-cli)** · 4,844★ · TypeScript · Hot  
  Portable memory layer (brv) for autonomous coding agents — agent-agnostic.  
  <sub>topics: agent, llm, mcp, memory, vibe-coding, ai, autonomous-agents, cli</sub>
- **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** · 4,292★ · Go · Hot  
  Agent-agnostic Go binary giving coding agents persistent memory.  
  <sub>topics: —</sub>
- **[memodb-io/Acontext](https://github.com/memodb-io/Acontext)** · 3,524★ · JavaScript · Hot  
  Treats Agent Skills as a memory layer — skills-as-memory hybrid.  
  <sub>topics: agent, context-engineering, data-platform, self-learning, agent-development-kit, ai-agent, llm, memory</sub>

### Token-saver / compression

_Measure first (`codeburn`), then compress: leaner code search, output trimming, and a front proxy stack to 60–90% on common loops._

- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 71,515★ · JavaScript · Hot  
  'Why use many token when few token do trick' — a Claude Code skill that aggressively trims tokens.  
  <sub>topics: ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 61,925★ · TypeScript · Hot  
  omo/lazycodex — a coding agent built for 'tokenmaxxers'; efficiency-first harness.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 61,471★ · Rust · Hot  
  CLI proxy that cuts LLM token consumption 60–90% on common dev commands — sits in front of the agent.  
  <sub>topics: agentic-coding, ai-coding, anthropic, claude-code, cli, command-line-tool, cost-reduction, developer-tools</sub>
- **[toon-format/toon](https://github.com/toon-format/toon)** · 24,534★ · TypeScript · Hot  
  Token-Oriented Object Notation — compact schema-aware encoding to shrink structured payloads.  
  <sub>topics: data-format, llm, serialization, tokenization</sub>
- **[chopratejas/headroom](https://github.com/chopratejas/headroom)** · 23,068★ · Python · Hot  
  Compresses tool outputs, logs, files, and RAG chunks before they hit the model's context.  
  <sub>topics: agent, ai, anthropic, compression, context-engineering, context-window, fastapi, langchain</sub>
- **[getagentseal/codeburn](https://github.com/getagentseal/codeburn)** · 7,879★ · TypeScript · Hot  
  TUI dashboard showing where your AI coding tokens go — measure before you optimize.  
  <sub>topics: ai-coding, claude-code, cli, codex, cost-tracking, developer-tools, observability, terminal-ui</sub>
- **[MinishLab/semble](https://github.com/MinishLab/semble)** · 5,070★ · Python · Hot  
  Fast, accurate code search for agents using ~98% fewer tokens than reading files.  
  <sub>topics: agents, code-search, embeddings, mcp, mcp-server, model-context-protocol, retrieval</sub>

### Code-graph / retrieval

_Give the agent structure instead of raw files — graphs and indexes answer 'how does X relate to Y' without scanning the repo._

- **[safishamsi/graphify](https://github.com/safishamsi/graphify)** · 65,604★ · Python · Hot  
  Coding-assistant skill that turns a repo into a knowledge graph (you use this on this project).  
  <sub>topics: claude-code, graphrag, knowledge-graph, codex, openclaw, skills, antigravity, gemini</sub>
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 57,345★ · TypeScript · Hot  
  Turns any code into an interactive teaching graph — comprehension over impression.  
  <sub>topics: claude-code, claude-skills, understandcode, codex, codex-skills, knowledge-graph, opencode-skills, antigravity-skills</sub>
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 47,422★ · TypeScript · Hot  
  Pre-indexed code knowledge graph for Claude Code/Codex/Cursor — structural retrieval.  
  <sub>topics: —</sub>
- **[abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)** · 41,960★ · TypeScript · Hot  
  Zero-server code-intelligence engine — client-side code graph.  
  <sub>topics: —</sub>
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 3,317★ · C · Rising  
  High-performance code-intelligence MCP server — indexes codebases for retrieval.  
  <sub>topics: claude-code, code-analysis, code-intelligence, developer-tools, knowledge-graph, mcp, mcp-server, model-context-protocol</sub>

### MCP ecosystem

_External capabilities via a standard protocol. Each connected server costs context, so connect deliberately — `context7` (live docs) is the highest-ROI default._

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 88,887★ · — · Hot  
  The big community index of MCP servers — discovery for what to connect.  
  <sub>topics: ai, mcp</sub>
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 87,070★ · TypeScript · Hot  
  The official reference MCP servers — the canonical catalog of capabilities to plug in.  
  <sub>topics: —</sub>
- **[upstash/context7](https://github.com/upstash/context7)** · 57,189★ · TypeScript · Hot  
  Up-to-date library docs for LLMs via MCP — kills 'hallucinated API' errors (you have this wired).  
  <sub>topics: llm, mcp, mcp-server, vibe-coding</sub>

### Observability / evals

_You can't optimize what you can't see. Trace runs, watch spend, and score outputs before trusting an autonomous setup._

- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 28,929★ · TypeScript · Classic  
  Open-source LLM engineering platform: traces, evals, metrics, prompts (you trace Claude Code into this).  
  <sub>topics: analytics, llm, llmops, large-language-models, openai, self-hosted, ycombinator, monitoring</sub>
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 19,579★ · Python · Classic  
  Debug/evaluate/monitor LLM apps, RAG, and agents — eval-first observability.  
  <sub>topics: open-source, langchain, openai, playground, prompt-engineering, llama-index, llm, llm-evaluation</sub>
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 10,100★ · Python · Classic  
  AI observability & evaluation — OpenTelemetry-based tracing for agents.  
  <sub>topics: llmops, ai-monitoring, ai-observability, llm-eval, aiengineering, datasets, agents, llms</sub>
- **[traceloop/openllmetry](https://github.com/traceloop/openllmetry)** · 7,190★ · Python · Mature  
  Open-source OpenTelemetry-based observability for LLM apps — standards-based traces.  
  <sub>topics: llmops, observability, open-telemetry, metrics, monitoring, opentelemetry, datascience, ml</sub>

### Local runtime

_Run open models locally or proxy many models behind one endpoint — the cost floor for grunt work and the fallback when the cloud is down._

- **[ollama/ollama](https://github.com/ollama/ollama)** · 173,893★ · Go · Mature  
  Run open models locally with one command — point an agent at it to slash API cost or go offline.  
  <sub>topics: llama, llm, llms, go, golang, ollama, mistral, gemma</sub>
- **[BerriAI/litellm](https://github.com/BerriAI/litellm)** · 50,082★ · Python · Mature  
  OpenAI-compatible proxy/gateway to 100+ LLMs — swap models under any harness from one endpoint.  
  <sub>topics: anthropic, langchain, llm, llmops, openai, ai-gateway, azure-openai, bedrock</sub>

## Graph analysis — how they relate

**Community clustering.** These 58 tools span **17 of the graph's 31 communities** — the Claude-Code ecosystem is spread across agent-framework, memory, retrieval, and observability neighborhoods rather than forming one tidy cluster.

- **Community 18** (15): `NousResearch/hermes-agent`, `Yeachan-Heo/oh-my-claudecode`, `affaan-m/ECC`, `ComposioHQ/awesome-claude-skills`, `sickn33/antigravity-awesome-skills`, `wshobson/agents`, `multica-ai/andrej-karpathy-skills`, `centminmod/my-claude-code-setup`, `davila7/claude-code-templates`, `luongnv89/claude-howto`, `Piebald-AI/claude-code-system-prompts`, `thedotmack/claude-mem`, `JuliusBrussee/caveman`, `rtk-ai/rtk`, `getagentseal/codeburn`
- **Community 11** (8): `earendil-works/pi`, `K-Dense-AI/scientific-agent-skills`, `farion1231/cc-switch`, `hesreallyhim/awesome-claude-code`, `code-yeongyu/oh-my-openagent`, `safishamsi/graphify`, `colbymchenry/codegraph`, `Egonex-AI/Understand-Anything`
- **Community 8** (5): `openclaw/openclaw`, `cline/cline`, `ruvnet/ruflo`, `abhigyanpatwari/GitNexus`, `DeusData/codebase-memory-mcp`
- **Community 1** (5): `google-gemini/gemini-cli`, `aaif-goose/goose`, `x1xhlol/system-prompts-and-models-of-ai-tools`, `MemPalace/mempalace`, `punkpeye/awesome-mcp-servers`
- **Community 14** (4): `anthropics/claude-code`, `anthropics/skills`, `anthropics/claude-cookbooks`, `Gentleman-Programming/engram`
- **Community 7** (4): `bytedance/deer-flow`, `mem0ai/mem0`, `memodb-io/Acontext`, `chopratejas/headroom`
- **Community 20** (4): `langfuse/langfuse`, `comet-ml/opik`, `Arize-ai/phoenix`, `BerriAI/litellm`
- **Community 2** (2): `anomalyco/opencode`, `garrytan/gstack`
- **Community 3** (2): `shanraisshan/claude-code-best-practice`, `memvid/memvid`
- **Community 10** (2): `MinishLab/semble`, `upstash/context7`

**Centrality (PageRank in the full 1,243-repo graph)** — the most 'hub-like' setup tools in your ecosystem:

- `hesreallyhim/awesome-claude-code` — PageRank 0.0036
- `DeusData/codebase-memory-mcp` — PageRank 0.0025
- `code-yeongyu/oh-my-openagent` — PageRank 0.0022
- `affaan-m/ECC` — PageRank 0.0018
- `davila7/claude-code-templates` — PageRank 0.0017
- `comet-ml/opik` — PageRank 0.0015
- `anthropics/claude-code` — PageRank 0.0014
- `punkpeye/awesome-mcp-servers` — PageRank 0.0013
- `MemPalace/mempalace` — PageRank 0.0012
- `anthropics/skills` — PageRank 0.0012

**Direct links between these tools** (top similarity edges where both endpoints are in this report):

- `anthropics/claude-cookbooks` ⇄ `anthropics/claude-code` (w=0.643) — authors: claude, jportner-ant
- `anthropics/claude-cookbooks` ⇄ `anthropics/skills` (w=0.583) — authors: rlancemartin
- `anthropics/skills` ⇄ `anthropics/claude-code` (w=0.550)
- `langfuse/langfuse` ⇄ `comet-ml/opik` (w=0.524) — topics: llm, llmops, openai, open-source
- `aaif-goose/goose` ⇄ `punkpeye/awesome-mcp-servers` (w=0.500) — topics: mcp, ai
- `hesreallyhim/awesome-claude-code` ⇄ `davila7/claude-code-templates` (w=0.386) — topics: anthropic, anthropic-claude, claude, claude-code; authors: github-actions[bot]
- `affaan-m/ECC` ⇄ `davila7/claude-code-templates` (w=0.368) — topics: anthropic, claude, claude-code; authors: dependabot[bot]
- `JuliusBrussee/caveman` ⇄ `davila7/claude-code-templates` (w=0.347) — topics: anthropic, claude, claude-code; authors: github-actions[bot]
- `JuliusBrussee/caveman` ⇄ `affaan-m/ECC` (w=0.336) — topics: anthropic, claude, claude-code, llm
- `MemPalace/mempalace` ⇄ `punkpeye/awesome-mcp-servers` (w=0.333) — topics: ai, mcp
- `wshobson/agents` ⇄ `ComposioHQ/awesome-claude-skills` (w=0.326) — topics: automation, agent-skills, ai-agents, cursor
- `sickn33/antigravity-awesome-skills` ⇄ `ComposioHQ/awesome-claude-skills` (w=0.326) — topics: ai-agents, antigravity, claude-code, mcp
- `Arize-ai/phoenix` ⇄ `comet-ml/opik` (w=0.315) — topics: llmops, prompt-engineering, llm-evaluation, openai; authors: dependabot[bot]
- `rtk-ai/rtk` ⇄ `affaan-m/ECC` (w=0.313) — topics: anthropic, claude-code, developer-tools, llm
- `DeusData/codebase-memory-mcp` ⇄ `wshobson/agents` (w=0.310) — topics: claude-code, developer-tools, mcp, cursor; authors: dependabot[bot]
- …and 20 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). This ecosystem moves fast and a lot of it is one-person projects — check before wiring one into your daily loop.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| affaan-m/ECC | 100 | Hot | very active | 5 | 26% | 14 |
| google-gemini/gemini-cli | 99 | Hot | very active | 7 | 12% | 522 |
| comet-ml/opik | 99 | Classic | very active | 5 | 25% | 482 |
| openai/codex | 96 | Hot | very active | 5 | 17% | 830 |
| chopratejas/headroom | 95 | Hot | very active | 6 | 12% | 154 |
| aaif-goose/goose | 94 | Hot | very active | 4 | 21% | 137 |
| mem0ai/mem0 | 94 | Mature | very active | 4 | 30% | 335 |
| langfuse/langfuse | 89 | Classic | very active | 3 | 21% | 575 |
| BerriAI/litellm | 89 | Mature | very active | 3 | 19% | 1356 |
| ollama/ollama | 88 | Mature | very active | 3 | 32% | 223 |
| anomalyco/opencode | 87 | Hot | very active | 3 | 29% | 820 |
| sickn33/antigravity-awesome-skills | 85 | Hot | very active | 2 | 41% | 137 |
| modelcontextprotocol/servers | 85 | Hot | very active | 4 | 24% | 24 |
| upstash/context7 | 85 | Hot | very active | 2 | 36% | 86 |
| openclaw/openclaw | 84 | Hot | very active | 2 | 46% | 204 |
| campfirein/byterover-cli | 84 | Hot | very active | 2 | 27% | 27 |
| Arize-ai/phoenix | 84 | Classic | very active | 2 | 41% | 715 |
| traceloop/openllmetry | 84 | Mature | very active | 3 | 23% | 258 |
| abhigyanpatwari/GitNexus | 82 | Hot | very active | 2 | 43% | 452 |
| bytedance/deer-flow | 81 | Hot | very active | 5 | 16% | 0 |
| earendil-works/pi | 80 | Hot | very active | 1 | 53% | 228 |
| Yeachan-Heo/oh-my-claudecode | 80 | Hot | very active | 1 | 64% | 232 |
| davila7/claude-code-templates | 80 | Hot | very active | 2 | 45% | 19 |
| thedotmack/claude-mem | 80 | Hot | very active | 1 | 74% | 281 |
| cline/cline | 79 | Hot | very active | 1 | 52% | 288 |
| NousResearch/hermes-agent | 79 | Hot | very active | 2 | 37% | 17 |
| K-Dense-AI/scientific-agent-skills | 79 | Hot | very active | 1 | 71% | 86 |
| getagentseal/codeburn | 79 | Hot | very active | 1 | 86% | 35 |
| memodb-io/Acontext | 78 | Hot | very active | 1 | 74% | 279 |
| code-yeongyu/oh-my-openagent | 78 | Hot | very active | 1 | 90% | 198 |
| safishamsi/graphify | 78 | Hot | very active | 1 | 89% | 132 |
| colbymchenry/codegraph | 78 | Hot | very active | 1 | 88% | 15 |
| DeusData/codebase-memory-mcp | 78 | Rising | very active | 1 | 98% | 34 |
| anthropics/claude-code | 77 | Hot | very active | 1 | 84% | 138 |
| ruvnet/ruflo | 77 | Hot | very active | 1 | 92% | 1529 |
| farion1231/cc-switch | 77 | Hot | very active | 1 | 57% | 42 |
| Piebald-AI/claude-code-system-prompts | 77 | Rising | very active | 1 | 100% | 155 |
| Gentleman-Programming/engram | 77 | Hot | very active | 1 | 95% | 89 |
| MinishLab/semble | 77 | Hot | very active | 1 | 65% | 16 |
| luongnv89/claude-howto | 76 | Hot | very active | 1 | 53% | 10 |
| MemPalace/mempalace | 76 | Hot | very active | 1 | 66% | 10 |
| anthropics/claude-cookbooks | 75 | Mature | very active | 4 | 19% | 0 |
| Egonex-AI/Understand-Anything | 75 | Hot | very active | 1 | 55% | 7 |
| rtk-ai/rtk | 73 | Hot | very active | 1 | 59% | 207 |
| JuliusBrussee/caveman | 72 | Hot | very active | 1 | 75% | 14 |
| obra/superpowers | 71 | Hot | very active | 1 | 59% | 5 |
| toon-format/toon | 71 | Hot | very active | 1 | 86% | 27 |
| wshobson/agents | 69 | Hot | very active | 2 | 36% | 0 |
| ComposioHQ/awesome-claude-skills | 65 | Rising | very active | 6 | 27% | 0 |
| shanraisshan/claude-code-best-practice | 65 | Rising | very active | 1 | 94% | 0 |
| punkpeye/awesome-mcp-servers | 65 | Hot | very active | 1 | 86% | 0 |
| memvid/memvid | 64 | Mature | active | 1 | 75% | 12 |
| garrytan/gstack | 60 | Rising | very active | 1 | 100% | 0 |
| centminmod/my-claude-code-setup | 58 | Rising | very active | 1 | 100% | 0 |
| hesreallyhim/awesome-claude-code | 58 | Mature | active | 1 | 98% | 0 |
| x1xhlol/system-prompts-and-models-of-ai-tools | 50 | Mature | active | 1 | 79% | 0 |
| anthropics/skills | 46 | Rising | active | 1 | 56% | 0 |
| multica-ai/andrej-karpathy-skills | 42 | Mature | active | 1 | 57% | 0 |

## Adjacent (deliberately not listed here)

- **n8n-io/n8n** (192,095★) — workflow-automation platform — orchestrates agents but isn't a Claude-Code setup layer
- **langgenius/dify** (144,875★) — agentic-workflow platform — covered by the agent-orchestration report
- **langchain-ai/langchain** (139,060★) — agent-engineering library — app framework, not a CC setup tool
- **open-webui/open-webui** (141,111★) — chat UI for local models — a frontend, not an agent setup
- **ultraworkers/claw-code** (193,637★) — art/exhibit harness — not a practical setup layer
- **multica-ai/multica** (36,287★) — managed-agents platform — team product, see agent-orchestration report

## Methodology & caveats

- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (claude-code / skill / agent harness / mcp / memory / token / observability / code-graph / setup) across name+description+topics, then manual curation into the nine setup layers. General agent *application* frameworks, chat UIs, and broad platforms were routed to adjacent reports or excluded (see above).
- **The three-strategy table is opinionated**, built only from repos in your stars — it is a starting point, not a benchmark. Validate model-tier and token-saver claims against your own `langfuse`/`codeburn` traces.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.

<sub>Tools covered: 58 · Snapshot: 2026-06-11T21:58:33.384Z</sub>
