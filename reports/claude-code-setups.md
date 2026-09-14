# Claude Code Superpowers — Setup Strategies from Your Stars

> Derived from **kaiser-data**'s 2,159 starred repos (snapshot `2026-09-14T11:08:08.535Z`), cross-referenced with the repo-similarity graph (2,159 nodes / 7,086 edges, 37 communities).
>
> Generated 2026-09-14 by `scripts/reports/claude_code_setups.py` (regenerate any time — no API cost).

![Top tools by stars](assets/claude-code-setups-top-tools.svg)

![Tools per category](assets/claude-code-setups-categories.svg)


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

- **59 Claude-Code 'superpower' projects** in your stars (**4,945,337★** combined), spanning 9 setup layers:
  - **Harness / coding agent** (12): `openclaw`, `hermes-agent`, `opencode`, `claude-code`, `codex`, `gemini-cli`, `pi`, `deer-flow`, `ruflo`, `cline`, `goose`, `oh-my-claudecode`
  - **Skills framework** (6): `superpowers`, `ECC`, `skills`, `awesome-claude-skills`, `scientific-agent-skills`, `agents`
  - **Config / setup kit** (11): `andrej-karpathy-skills`, `system-prompts-and-models-of-ai-tools`, `gstack`, `cc-switch`, `claude-code-best-practice`, `awesome-claude-code`, `claude-cookbooks`, `claude-howto`, `claude-code-templates`, `claude-code-system-prompts`, `my-claude-code-setup`
  - **Memory / context** (7): `claude-mem`, `mem0`, `mempalace`, `memvid`, `engram`, `byterover-cli`, `Acontext`
  - **Token-saver / compression** (7): `caveman`, `rtk`, `headroom`, `oh-my-openagent`, `toon`, `codeburn`, `semble`
  - **Code-graph / retrieval** (5): `graphify`, `Understand-Anything`, `codegraph`, `GitNexus`, `codebase-memory-mcp`
  - **MCP ecosystem** (3): `awesome-mcp-servers`, `servers`, `context7`
  - **Observability / evals** (6): `langfuse`, `opik`, `phoenix`, `openllmetry`, `agent-flow`, `Irrlicht`
  - **Local runtime** (2): `ollama`, `litellm`
- **Skills are the leverage point.** `obra/superpowers` (the most-starred repo in this whole set) and `anthropics/skills` replace most always-on `CLAUDE.md` prose with on-demand expertise — cheaper *and* sharper.
- **Token-saving is now a stack, not a setting.** A proxy (`rtk`), a leaner code-search (`semble`, ~98% fewer tokens than reading files), output compression (`headroom`), and a spend dashboard (`codeburn`) compose into 60–90% reductions on real dev loops.
- **You already run three layers well** — `claude-mem` (memory), `graphify` (code-graph), and `langfuse` (observability) — plus `context7` over MCP. The gap is a **skills framework** and a deliberate **model-tier policy**.

## The setup, layer by layer

| Layer | What it buys you | Your starred picks |
|---|---|---|
| **Harness / coding agent** | The agent loop itself | `openclaw`, `hermes-agent`, `opencode`, `claude-code`, `codex`, `gemini-cli` |
| **Skills framework** | On-demand expertise (the modern superpower) | `superpowers`, `ECC`, `skills`, `awesome-claude-skills`, `scientific-agent-skills`, `agents` |
| **Config / setup kit** | Shape behavior up front, cheaply | `andrej-karpathy-skills`, `system-prompts-and-models-of-ai-tools`, `gstack`, `cc-switch`, `claude-code-best-practice`, `awesome-claude-code` |
| **Memory / context** | Persist context across sessions | `claude-mem`, `mem0`, `mempalace`, `memvid`, `engram`, `byterover-cli` |
| **Token-saver / compression** | Shrink what the model has to read | `caveman`, `rtk`, `headroom`, `oh-my-openagent`, `toon`, `codeburn` |
| **Code-graph / retrieval** | Feed the *right* code, not all of it | `graphify`, `Understand-Anything`, `codegraph`, `GitNexus`, `codebase-memory-mcp` |
| **MCP ecosystem** | External reach (docs, tools, data) | `awesome-mcp-servers`, `servers`, `context7` |
| **Observability / evals** | Measure cost & quality | `langfuse`, `opik`, `phoenix`, `openllmetry`, `agent-flow`, `Irrlicht` |
| **Local runtime** | Cut cost / go offline | `ollama`, `litellm` |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Layer | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Harness / coding agent | TypeScript | NOASSERTION | 389,649 (▲653) | Hot | 84 | very active | 0d ago | 9mo | 14 |
| [obra/superpowers](https://github.com/obra/superpowers) | Skills framework | Shell | MIT | 286,443 (▲4,259) | Hot | 78 | very active | 2d ago | 11mo | 6 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Skills framework | JavaScript | MIT | 258,025 (▲7,749) | Hot | 79 | very active | 0d ago | 7mo | 18 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Harness / coding agent | Python | MIT | 245,317 (▲3,168) | Hot | 75 | very active | 0d ago | 1.1y | 16 |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Config / setup kit | — | — | 212,878 (▲2,417) | Declining | 23 | slowing | 4mo ago | 7mo | 0 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | Harness / coding agent | TypeScript | MIT | 207,256 (▲2,419) | Hot | 88 | very active | 0d ago | 1.4y | 23 |
| [ollama/ollama](https://github.com/ollama/ollama) | Local runtime | Go | MIT | 180,877 (▲611) | Classic | 83 | very active | 0d ago | 3.2y | 10 |
| [anthropics/skills](https://github.com/anthropics/skills) | Skills framework | Python | — | 176,216 (▲1,538) | Rising | 50 | active | 4d ago | 11mo | 5 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Harness / coding agent | Python | — | 144,971 (▲761) | Hot | 79 | very active | 0d ago | 1.6y | 4 |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Config / setup kit | — | GPL-3.0 | 143,608 (▲219) | Mature | 48 | active | 1mo ago | 1.5y | 3 |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Config / setup kit | TypeScript | MIT | 132,941 (▲1,330) | Hot | 57 | very active | 3d ago | 6mo | 5 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Config / setup kit | Rust | MIT | 132,771 (▲1,513) | Hot | 82 | very active | 0d ago | 1.1y | 37 |
| [openai/codex](https://github.com/openai/codex) | Harness / coding agent | Rust | Apache-2.0 | 124,012 (▲2,172) | Hot | 94 | very active | 0d ago | 1.4y | 35 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Code-graph / retrieval | Python | Apache-2.0 | 116,573 (▲1,422) | Hot | 86 | very active | 2d ago | 5mo | 25 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Harness / coding agent | TypeScript | Apache-2.0 | 106,969 (▲143) | Hot | 90 | very active | 0d ago | 1.4y | 17 |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Token-saver / compression | Go | NOASSERTION | 105,476 (▲1,636) | Hot | 78 | very active | 0d ago | 5mo | 8 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness / coding agent | TypeScript | MIT | 104,948 (▲2,733) | Hot | 90 | very active | 0d ago | 1.1y | 16 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP ecosystem | — | MIT | 94,952 (▲581) | Hot | 65 | very active | 1d ago | 1.8y | 23 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Memory / context | TypeScript | Apache-2.0 | 93,826 (▲517) | Hot | 80 | very active | 1d ago | 1.0y | 19 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | MCP ecosystem | TypeScript | NOASSERTION | 90,309 (▲204) | Hot | 89 | very active | 11d ago | 1.8y | 35 |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | Code-graph / retrieval | TypeScript | MIT | 82,642 (▲1,015) | Hot | 75 | very active | 2d ago | 6mo | 11 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Harness / coding agent | Python | MIT | 82,408 (▲954) | Hot | 84 | very active | 0d ago | 1.4y | 44 |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Token-saver / compression | Rust | Apache-2.0 | 80,272 (▲1,282) | Hot | 80 | very active | 0d ago | 7mo | 6 |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Skills framework | Python | — | 74,998 (▲436) | Declining | 36 | active | 1mo ago | 11mo | 1 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Harness / coding agent | TypeScript | MIT | 72,387 (▲1,604) | Hot | 76 | very active | 0d ago | 1.3y | 5 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Token-saver / compression | Python | Apache-2.0 | 72,005 (▲2,943) | Hot | 87 | very active | 1d ago | 8mo | 29 |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | Code-graph / retrieval | C | MIT | 70,773 (▲990) | Hot | 78 | very active | 0d ago | 7mo | 4 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Token-saver / compression | TypeScript | NOASSERTION | 69,029 (▲290) | Rising | 78 | very active | 0d ago | 9mo | 1 |
| [cline/cline](https://github.com/cline/cline) | Harness / coding agent | TypeScript | Apache-2.0 | 67,967 (▲420) | Mature | 78 | very active | 0d ago | 2.2y | 11 |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Config / setup kit | HTML | MIT | 65,908 (▲266) | Rising | 64 | very active | 0d ago | 10mo | 1 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Memory / context | Python | Apache-2.0 | 65,265 (▲502) | Classic | 79 | very active | 0d ago | 3.2y | 24 |
| [upstash/context7](https://github.com/upstash/context7) | MCP ecosystem | TypeScript | MIT | 61,983 (▲301) | Hot | 78 | very active | 3d ago | 1.5y | 13 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Memory / context | Python | MIT | 59,043 (▲178) | Hot | 76 | very active | 0d ago | 5mo | 23 |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Local runtime | Python | NOASSERTION | 58,685 (▲551) | Classic | 84 | very active | 0d ago | 3.1y | 9 |
| [aaif-goose/goose](https://github.com/aaif-goose/goose) | Harness / coding agent | Rust | Apache-2.0 | 54,246 (▲293) | Mature | 89 | very active | 0d ago | 2.1y | 27 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Config / setup kit | Python | NOASSERTION | 54,003 (▲428) | Mature | 60 | very active | 0d ago | 1.4y | 2 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Config / setup kit | Jupyter Notebook | MIT | 52,670 (▲214) | Classic | 60 | very active | 11d ago | 3.1y | 9 |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | Code-graph / retrieval | TypeScript | NOASSERTION | 47,322 (▲259) | Hot | 88 | very active | 0d ago | 1.1y | 24 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Skills framework | Python | MIT | 44,846 (▲1,774) | Hot | 80 | very active | 0d ago | 11mo | 17 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Code-graph / retrieval | C | MIT | 43,181 (▲796) | Hot | 75 | very active | 0d ago | 6mo | 3 |
| [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | Config / setup kit | Python | MIT | 41,467 (▲94) | Rising | 68 | very active | 8d ago | 10mo | 3 |
| [wshobson/agents](https://github.com/wshobson/agents) | Skills framework | Python | MIT | 39,640 (▲190) | Hot | 64 | very active | 0d ago | 1.1y | 17 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Harness / coding agent | TypeScript | MIT | 39,149 (▲119) | Hot | 80 | very active | 0d ago | 8mo | 8 |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Observability / evals | TypeScript | NOASSERTION | 34,579 (▲336) | Classic | 89 | very active | 0d ago | 3.3y | 15 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Config / setup kit | Python | MIT | 30,724 (▲178) | Hot | 80 | very active | 0d ago | 1.2y | 17 |
| [toon-format/toon](https://github.com/toon-format/toon) | Token-saver / compression | TypeScript | MIT | 25,369 (▲44) | Hot | 79 | very active | 11d ago | 10mo | 4 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Observability / evals | Python | Apache-2.0 | 22,010 (▲187) | Classic | 88 | very active | 0d ago | 3.4y | 20 |
| [memvid/memvid](https://github.com/memvid/memvid) | Memory / context | Rust | Apache-2.0 | 16,539 (▲50) | Declining | 56 | slowing | 2mo ago | 1.3y | 1 |
| [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | Config / setup kit | JavaScript | MIT | 12,666 (▲81) | Rising | 77 | very active | 2d ago | 10mo | 2 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Observability / evals | Python | NOASSERTION | 11,452 (▲110) | Classic | 84 | very active | 1d ago | 3.8y | 14 |
| [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | Token-saver / compression | TypeScript | MIT | 10,998 (▲136) | Rising | 79 | very active | 0d ago | 5mo | 2 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Observability / evals | Python | Apache-2.0 | 7,427 (▲14) | Classic | 64 | active | 1mo ago | 3.0y | 4 |
| [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram) | Memory / context | Go | MIT | 6,579 (▲234) | Hot | 79 | very active | 0d ago | 7mo | 5 |
| [MinishLab/semble](https://github.com/MinishLab/semble) | Token-saver / compression | Python | MIT | 6,068 (▲64) | Hot | 73 | very active | 2d ago | 5mo | 6 |
| [campfirein/byterover-cli](https://github.com/campfirein/byterover-cli) | Memory / context | TypeScript | NOASSERTION | 4,957 (▲1) | Declining | 54 | slowing | 2mo ago | 1.2y | 1 |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | Memory / context | JavaScript | Apache-2.0 | 3,692 (▲8) | Declining | 48 | slowing | 2mo ago | 1.2y | 0 |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | Config / setup kit | Python | MIT | 2,633 (▲9) | Mature | 49 | active | 12d ago | 1.2y | 1 |
| [patoles/agent-flow](https://github.com/patoles/agent-flow) | Observability / evals | TypeScript | Apache-2.0 | 1,639 (▲14) | Mature | 47 | slowing | 2mo ago | 5mo | 2 |
| [ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht) | Observability / evals | Go | MIT | 99 (▲2) | Hot | 80 | very active | 0d ago | 1.0y | 5 |

## By layer

### Harness / coding agent

_The loop that reads, plans, edits, and runs. Pick one as your daily driver; keep a second installed to diff behavior and model-shop._

- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · 389,649★ · TypeScript · Hot  
  Cross-platform personal-assistant harness — an 'any OS, any platform' agent runtime.  
  <sub>topics: ai, assistant, own-your-data, personal, crustacean, molty, openclaw</sub>
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 245,317★ · Python · Hot  
  Long-lived 'agent that grows with you' harness — persistent, personalized agent loop.  
  <sub>topics: ai, ai-agent, ai-agents, llm, anthropic, chatgpt, claude, claude-code</sub>
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 207,256★ · TypeScript · Hot  
  Open-source terminal coding agent — a provider-agnostic alternative harness.  
  <sub>topics: —</sub>
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 144,971★ · Python · Hot  
  Claude Code itself — the agentic CLI that lives in your terminal; the baseline every setup here extends.  
  <sub>topics: —</sub>
- **[openai/codex](https://github.com/openai/codex)** · 124,012★ · Rust · Hot  
  OpenAI's lightweight terminal coding agent — useful as a second harness to diff behavior against Claude Code.  
  <sub>topics: —</sub>
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 106,969★ · TypeScript · Hot  
  Gemini's open-source terminal agent — the third major CLI harness; handy for model-shopping.  
  <sub>topics: gemini, gemini-api, ai, ai-agents, cli, mcp-client, mcp-server</sub>
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 104,948★ · TypeScript · Hot  
  Unified LLM-API + agent-loop + TUI toolkit — a kit for rolling your own coding agent.  
  <sub>topics: —</sub>
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 82,408★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and writes — multi-step autonomy.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 72,387★ · TypeScript · Hot  
  Agent meta-harness for Claude — deploys multi-agent swarms with coordination.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server</sub>
- **[cline/cline](https://github.com/cline/cline)** · 67,967★ · TypeScript · Mature  
  Autonomous coding agent as SDK / IDE extension / CLI — strong for in-editor agentic workflows.  
  <sub>topics: —</sub>
- **[aaif-goose/goose](https://github.com/aaif-goose/goose)** · 54,246★ · Rust · Mature  
  Extensible open agent that installs and runs tools, not just suggestions — MCP-native.  
  <sub>topics: mcp, acp, ai, ai-agents</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 39,149★ · TypeScript · Hot  
  Teams-first multi-agent orchestration layer for Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>

### Skills framework

_The biggest 2026 upgrade. Skills load only when triggered, so they add capability without taxing every session — the opposite of a big always-on CLAUDE.md._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 286,443★ · Shell · Hot  
  Agentic skills framework + dev methodology — the headline 'give your agent superpowers' skill collection.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 258,025★ · JavaScript · Hot  
  Agent-harness performance system bundling skills, instincts, and memory into one optimization layer.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[anthropics/skills](https://github.com/anthropics/skills)** · 176,216★ · Python · Rising  
  Anthropic's official Agent Skills repo — canonical examples of the skills format.  
  <sub>topics: agent-skills</sub>
- **[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** · 74,998★ · Python · Declining  
  Curated index of Claude Skills + tooling — the discovery hub for what's worth installing.  
  <sub>topics: claude, claude-code, agent-skills, ai-agents, antigravity, automation, codex, composio</sub>
- **[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)** · 44,846★ · Python · Hot  
  Domain skill pack that turns an agent into a research scientist — example of vertical skills.  
  <sub>topics: ai-scientist, bioinformatics, chemoinformatics, claude, claude-skills, claudecode, clinical-research, computational-biology</sub>
- **[wshobson/agents](https://github.com/wshobson/agents)** · 39,640★ · Python · Hot  
  Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor) — subagents & commands.  
  <sub>topics: anthropic, agent-skills, agentic-ai, ai-agents, cursor, cursor-rules, mcp, multi-agent</sub>

### Config / setup kit

_Turnkey CLAUDE.md / command / hook bundles. Steal a good one, then trim to what you actually use — bloat here is paid on every prompt._

- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 212,878★ · — · Declining  
  A single CLAUDE.md derived from Karpathy's habits — the 'one good config file' approach.  
  <sub>topics: —</sub>
- **[x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)** · 143,608★ · — · Mature  
  Leaked/collected system prompts of major AI coding tools — prompt-engineering reference.  
  <sub>topics: ai, cursor, lovable, system-prompts, v0, cursorai, devin, replit</sub>
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 132,941★ · TypeScript · Hot  
  Garry Tan's exact Claude Code setup — 23 opinionated tools as a turnkey starting point.  
  <sub>topics: —</sub>
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 132,771★ · Rust · Hot  
  Desktop all-in-one for managing Claude Code/Codex/OpenClaw — swap providers & configs fast.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, codex, mcp</sub>
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 65,908★ · HTML · Rising  
  Best-practices collection: vibe-coding → agentic engineering.  
  <sub>topics: claude-ai, claude-code, best-practices, claude, claude-code-best-practices, agentic-engineering, anthropic, claude-code-agents</sub>
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 54,003★ · Python · Mature  
  The awesome-list for Claude Code skills, hooks, slash-commands, and orchestrators.  
  <sub>topics: anthropic, anthropic-claude, awesome, awesome-list, awesome-lists, awesome-resources, claude, claude-code</sub>
- **[anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)** · 52,670★ · Jupyter Notebook · Classic  
  Official recipes/notebooks for effective Claude usage patterns.  
  <sub>topics: —</sub>
- **[luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)** · 41,467★ · Python · Rising  
  Visual, example-driven guide to Claude Code from basics to advanced — the learning path.  
  <sub>topics: claude-code, guide, tutorial</sub>
- **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** · 30,724★ · Python · Hot  
  CLI to configure AND monitor Claude Code — installs commands/agents/hooks and watches usage.  
  <sub>topics: anthropic, anthropic-claude, claude, claude-code</sub>
- **[Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts)** · 12,666★ · JavaScript · Rising  
  Claude Code's full system prompt + 27 builtin tool descriptions — know what you're configuring.  
  <sub>topics: claude-code, claude-code-system-prompts, system-prompts</sub>
- **[centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup)** · 2,633★ · Python · Mature  
  A shared starter CLAUDE.md + memory-bank configuration template you can fork.  
  <sub>topics: claude, claude-ai, claude-code, subagents, claudecode-config, claudecode-hooks, claudecode-subagents</sub>

### Memory / context

_Persist decisions and context across sessions so the agent doesn't re-derive what it already learned. The backend is swappable._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 93,826★ · TypeScript · Hot  
  Persistent context across sessions for every agent — captures work and re-injects it (you run this).  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude, claude-agent-sdk, claude-agents</sub>
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 65,265★ · Python · Classic  
  Universal memory layer for AI agents — the most-adopted general memory backend.  
  <sub>topics: ai, chatgpt, llm, python, rag, long-term-memory, memory, memory-management</sub>
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 59,043★ · Python · Hot  
  Best-benchmarked open-source AI memory system — drop-in long-term memory.  
  <sub>topics: ai, chromadb, llm, mcp, memory, python</sub>
- **[memvid/memvid](https://github.com/memvid/memvid)** · 16,539★ · Rust · Declining  
  Memory layer that replaces RAG pipelines with a compact server — novel storage approach.  
  <sub>topics: ai, context, embedded, faiss, knowledge-base, knowledge-graph, llm, machine-learning</sub>
- **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** · 6,579★ · Go · Hot  
  Agent-agnostic Go binary giving coding agents persistent memory.  
  <sub>topics: —</sub>
- **[campfirein/byterover-cli](https://github.com/campfirein/byterover-cli)** · 4,957★ · TypeScript · Declining  
  Portable memory layer (brv) for autonomous coding agents — agent-agnostic.  
  <sub>topics: agent, llm, mcp, memory, vibe-coding, ai, autonomous-agents, cli</sub>
- **[memodb-io/Acontext](https://github.com/memodb-io/Acontext)** · 3,692★ · JavaScript · Declining  
  Treats Agent Skills as a memory layer — skills-as-memory hybrid.  
  <sub>topics: agent, context-engineering, data-platform, self-learning, agent-development-kit, ai-agent, llm, memory</sub>

### Token-saver / compression

_Measure first (`codeburn`), then compress: leaner code search, output trimming, and a front proxy stack to 60–90% on common loops._

- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 105,476★ · Go · Hot  
  'Why use many token when few token do trick' — a Claude Code skill that aggressively trims tokens.  
  <sub>topics: ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering</sub>
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 80,272★ · Rust · Hot  
  CLI proxy that cuts LLM token consumption 60–90% on common dev commands — sits in front of the agent.  
  <sub>topics: agentic-coding, ai-coding, anthropic, claude-code, cli, command-line-tool, cost-reduction, developer-tools</sub>
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 72,005★ · Python · Hot  
  Compresses tool outputs, logs, files, and RAG chunks before they hit the model's context.  
  <sub>topics: agent, ai, anthropic, compression, context-engineering, context-window, fastapi, langchain</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 69,029★ · TypeScript · Rising  
  omo/lazycodex — a coding agent built for 'tokenmaxxers'; efficiency-first harness.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[toon-format/toon](https://github.com/toon-format/toon)** · 25,369★ · TypeScript · Hot  
  Token-Oriented Object Notation — compact schema-aware encoding to shrink structured payloads.  
  <sub>topics: data-format, llm, serialization, tokenization</sub>
- **[getagentseal/codeburn](https://github.com/getagentseal/codeburn)** · 10,998★ · TypeScript · Rising  
  TUI dashboard showing where your AI coding tokens go — measure before you optimize.  
  <sub>topics: ai-coding, claude-code, cli, codex, cost-tracking, developer-tools, observability, terminal-ui</sub>
- **[MinishLab/semble](https://github.com/MinishLab/semble)** · 6,068★ · Python · Hot  
  Fast, accurate code search for agents using ~98% fewer tokens than reading files.  
  <sub>topics: agents, code-search, embeddings, mcp, mcp-server, model-context-protocol, retrieval</sub>

### Code-graph / retrieval

_Give the agent structure instead of raw files — graphs and indexes answer 'how does X relate to Y' without scanning the repo._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 116,573★ · Python · Hot  
  Coding-assistant skill that turns a repo into a knowledge graph (you use this on this project).  
  <sub>topics: claude-code, graphrag, knowledge-graph, codex, openclaw, skills, antigravity, gemini</sub>
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 82,642★ · TypeScript · Hot  
  Turns any code into an interactive teaching graph — comprehension over impression.  
  <sub>topics: claude-code, claude-skills, understandcode, codex, codex-skills, knowledge-graph, opencode-skills, antigravity-skills</sub>
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 70,773★ · C · Hot  
  Pre-indexed code knowledge graph for Claude Code/Codex/Cursor — structural retrieval.  
  <sub>topics: —</sub>
- **[abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)** · 47,322★ · TypeScript · Hot  
  Zero-server code-intelligence engine — client-side code graph.  
  <sub>topics: —</sub>
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 43,181★ · C · Hot  
  High-performance code-intelligence MCP server — indexes codebases for retrieval.  
  <sub>topics: claude-code, code-analysis, code-intelligence, developer-tools, knowledge-graph, mcp, mcp-server, model-context-protocol</sub>

### MCP ecosystem

_External capabilities via a standard protocol. Each connected server costs context, so connect deliberately — `context7` (live docs) is the highest-ROI default._

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 94,952★ · — · Hot  
  The big community index of MCP servers — discovery for what to connect.  
  <sub>topics: ai, mcp</sub>
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 90,309★ · TypeScript · Hot  
  The official reference MCP servers — the canonical catalog of capabilities to plug in.  
  <sub>topics: —</sub>
- **[upstash/context7](https://github.com/upstash/context7)** · 61,983★ · TypeScript · Hot  
  Up-to-date library docs for LLMs via MCP — kills 'hallucinated API' errors (you have this wired).  
  <sub>topics: llm, mcp, mcp-server, vibe-coding</sub>

### Observability / evals

_You can't optimize what you can't see. Trace runs, watch spend, and score outputs before trusting an autonomous setup._

- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 34,579★ · TypeScript · Classic  
  Open-source LLM engineering platform: traces, evals, metrics, prompts (you trace Claude Code into this).  
  <sub>topics: analytics, llm, llmops, large-language-models, openai, self-hosted, ycombinator, monitoring</sub>
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 22,010★ · Python · Classic  
  Debug/evaluate/monitor LLM apps, RAG, and agents — eval-first observability.  
  <sub>topics: open-source, langchain, openai, playground, prompt-engineering, llama-index, llm, llm-evaluation</sub>
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 11,452★ · Python · Classic  
  AI observability & evaluation — OpenTelemetry-based tracing for agents.  
  <sub>topics: llmops, ai-monitoring, ai-observability, llm-eval, aiengineering, datasets, agents, llms</sub>
- **[traceloop/openllmetry](https://github.com/traceloop/openllmetry)** · 7,427★ · Python · Classic  
  Open-source OpenTelemetry-based observability for LLM apps — standards-based traces.  
  <sub>topics: llmops, observability, open-telemetry, metrics, monitoring, opentelemetry, datascience, ml</sub>
- **[patoles/agent-flow](https://github.com/patoles/agent-flow)** · 1,639★ · TypeScript · Mature  
  Real-time visualization of Claude Code agent orchestration — watch agents think, branch, coordinate.  
  <sub>topics: agent-visualization, ai-agents, claude-code, developer-tools, llm, vscode-extension</sub>
- **[ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht)** · 99★ · Go · Hot  
  Claude Code session lights in the macOS menu bar — at-a-glance session state.  
  <sub>topics: —</sub>

### Local runtime

_Run open models locally or proxy many models behind one endpoint — the cost floor for grunt work and the fallback when the cloud is down._

- **[ollama/ollama](https://github.com/ollama/ollama)** · 180,877★ · Go · Classic  
  Run open models locally with one command — point an agent at it to slash API cost or go offline.  
  <sub>topics: llama, llm, llms, go, golang, ollama, mistral, gemma</sub>
- **[BerriAI/litellm](https://github.com/BerriAI/litellm)** · 58,685★ · Python · Classic  
  OpenAI-compatible proxy/gateway to 100+ LLMs — swap models under any harness from one endpoint.  
  <sub>topics: anthropic, langchain, llm, llmops, openai, ai-gateway, azure-openai, bedrock</sub>

## Graph analysis — how they relate

**Community clustering.** These 59 tools span **17 of the graph's 37 communities** — the Claude-Code ecosystem is spread across agent-framework, memory, retrieval, and observability neighborhoods rather than forming one tidy cluster.

- **Community 16** (12): `ruvnet/ruflo`, `Yeachan-Heo/oh-my-claudecode`, `affaan-m/ECC`, `ComposioHQ/awesome-claude-skills`, `x1xhlol/system-prompts-and-models-of-ai-tools`, `thedotmack/claude-mem`, `rtk-ai/rtk`, `code-yeongyu/oh-my-openagent`, `Graphify-Labs/graphify`, `Egonex-AI/Understand-Anything`, `DeusData/codebase-memory-mcp`, `patoles/agent-flow`
- **Community 3** (11): `google-gemini/gemini-cli`, `aaif-goose/goose`, `NousResearch/hermes-agent`, `obra/superpowers`, `centminmod/my-claude-code-setup`, `davila7/claude-code-templates`, `luongnv89/claude-howto`, `MemPalace/mempalace`, `memodb-io/Acontext`, `headroomlabs-ai/headroom`, `punkpeye/awesome-mcp-servers`
- **Community 12** (5): `anthropics/claude-code`, `anthropics/skills`, `shanraisshan/claude-code-best-practice`, `anthropics/claude-cookbooks`, `abhigyanpatwari/GitNexus`
- **Community 5** (5): `earendil-works/pi`, `farion1231/cc-switch`, `hesreallyhim/awesome-claude-code`, `JuliusBrussee/caveman`, `traceloop/openllmetry`
- **Community 25** (4): `langfuse/langfuse`, `comet-ml/opik`, `Arize-ai/phoenix`, `BerriAI/litellm`
- **Community 29** (3): `openclaw/openclaw`, `garrytan/gstack`, `campfirein/byterover-cli`
- **Community 1** (3): `anomalyco/opencode`, `cline/cline`, `MinishLab/semble`
- **Community 10** (3): `K-Dense-AI/scientific-agent-skills`, `getagentseal/codeburn`, `ingo-eichhorst/Irrlicht`
- **Community 23** (2): `bytedance/deer-flow`, `ollama/ollama`
- **Community 24** (2): `multica-ai/andrej-karpathy-skills`, `toon-format/toon`
- **Community 14** (2): `mem0ai/mem0`, `memvid/memvid`
- **Community 26** (2): `modelcontextprotocol/servers`, `upstash/context7`

**Centrality (PageRank in the full 2,159-repo graph)** — the most 'hub-like' setup tools in your ecosystem:

- `affaan-m/ECC` — PageRank 0.0015
- `shanraisshan/claude-code-best-practice` — PageRank 0.0015
- `multica-ai/andrej-karpathy-skills` — PageRank 0.0012
- `hesreallyhim/awesome-claude-code` — PageRank 0.0011
- `davila7/claude-code-templates` — PageRank 0.0009
- `punkpeye/awesome-mcp-servers` — PageRank 0.0008
- `MemPalace/mempalace` — PageRank 0.0007
- `NousResearch/hermes-agent` — PageRank 0.0007
- `comet-ml/opik` — PageRank 0.0007
- `openclaw/openclaw` — PageRank 0.0007

**Direct links between these tools** (top similarity edges where both endpoints are in this report):

- `anthropics/skills` ⇄ `anthropics/claude-code` (w=0.800) — authors: williamqian12
- `anthropics/claude-cookbooks` ⇄ `anthropics/skills` (w=0.654) — authors: cj-ant
- `langfuse/langfuse` ⇄ `comet-ml/opik` (w=0.524) — topics: llm, llmops, openai, open-source
- `aaif-goose/goose` ⇄ `punkpeye/awesome-mcp-servers` (w=0.500) — topics: mcp, ai
- `patoles/agent-flow` ⇄ `affaan-m/ECC` (w=0.400) — topics: ai-agents, claude-code, developer-tools, llm
- `JuliusBrussee/caveman` ⇄ `hesreallyhim/awesome-claude-code` (w=0.382) — topics: anthropic, claude, claude-code, llm; authors: github-actions[bot]
- `hesreallyhim/awesome-claude-code` ⇄ `davila7/claude-code-templates` (w=0.372) — topics: anthropic, anthropic-claude, claude, claude-code; authors: github-actions[bot]
- `JuliusBrussee/caveman` ⇄ `davila7/claude-code-templates` (w=0.356) — topics: anthropic, claude, claude-code; authors: github-actions[bot]
- `NousResearch/hermes-agent` ⇄ `code-yeongyu/oh-my-openagent` (w=0.333) — topics: ai, ai-agents, anthropic, chatgpt
- `affaan-m/ECC` ⇄ `davila7/claude-code-templates` (w=0.333) — topics: anthropic, claude, claude-code
- `wshobson/agents` ⇄ `ComposioHQ/awesome-claude-skills` (w=0.326) — topics: agent-skills, ai-agents, cursor, mcp
- `rtk-ai/rtk` ⇄ `affaan-m/ECC` (w=0.313) — topics: anthropic, claude-code, developer-tools, llm
- `DeusData/codebase-memory-mcp` ⇄ `Graphify-Labs/graphify` (w=0.300) — topics: claude-code, code-analysis, developer-tools, knowledge-graph
- `Graphify-Labs/graphify` ⇄ `ComposioHQ/awesome-claude-skills` (w=0.291) — topics: claude-code, codex, antigravity, ai-agents
- `Arize-ai/phoenix` ⇄ `JuliusBrussee/caveman` (w=0.283) — topics: prompt-engineering, anthropic; authors: github-actions[bot], AmirF194
- …and 7 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). This ecosystem moves fast and a lot of it is one-person projects — check before wiring one into your daily loop.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| openai/codex | 94 | Hot | very active | 7 | 20% | 1076 |
| google-gemini/gemini-cli | 90 | Hot | very active | 3 | 20% | 623 |
| earendil-works/pi | 90 | Hot | very active | 3 | 27% | 259 |
| aaif-goose/goose | 89 | Mature | very active | 3 | 24% | 150 |
| modelcontextprotocol/servers | 89 | Hot | very active | 4 | 21% | 28 |
| langfuse/langfuse | 89 | Classic | very active | 3 | 26% | 681 |
| anomalyco/opencode | 88 | Hot | very active | 3 | 30% | 872 |
| abhigyanpatwari/GitNexus | 88 | Hot | very active | 3 | 27% | 865 |
| comet-ml/opik | 88 | Classic | very active | 3 | 34% | 577 |
| headroomlabs-ai/headroom | 87 | Hot | very active | 3 | 29% | 169 |
| Graphify-Labs/graphify | 86 | Hot | very active | 3 | 23% | 207 |
| openclaw/openclaw | 84 | Hot | very active | 2 | 40% | 243 |
| bytedance/deer-flow | 84 | Hot | very active | 8 | 12% | 1 |
| Arize-ai/phoenix | 84 | Classic | very active | 2 | 45% | 829 |
| BerriAI/litellm | 84 | Classic | very active | 2 | 30% | 1461 |
| ollama/ollama | 83 | Classic | very active | 2 | 27% | 251 |
| farion1231/cc-switch | 82 | Hot | very active | 2 | 46% | 54 |
| Yeachan-Heo/oh-my-claudecode | 80 | Hot | very active | 1 | 62% | 251 |
| K-Dense-AI/scientific-agent-skills | 80 | Hot | very active | 1 | 71% | 106 |
| davila7/claude-code-templates | 80 | Hot | very active | 2 | 35% | 20 |
| thedotmack/claude-mem | 80 | Hot | very active | 1 | 68% | 344 |
| rtk-ai/rtk | 80 | Hot | very active | 2 | 43% | 344 |
| ingo-eichhorst/Irrlicht | 80 | Hot | very active | 1 | 93% | 43 |
| anthropics/claude-code | 79 | Hot | very active | 1 | 62% | 216 |
| affaan-m/ECC | 79 | Hot | very active | 1 | 58% | 17 |
| mem0ai/mem0 | 79 | Classic | very active | 1 | 55% | 399 |
| Gentleman-Programming/engram | 79 | Hot | very active | 1 | 79% | 108 |
| toon-format/toon | 79 | Hot | very active | 1 | 97% | 31 |
| getagentseal/codeburn | 79 | Rising | very active | 1 | 64% | 67 |
| cline/cline | 78 | Mature | very active | 1 | 53% | 411 |
| obra/superpowers | 78 | Hot | very active | 1 | 82% | 12 |
| JuliusBrussee/caveman | 78 | Hot | very active | 1 | 72% | 33 |
| code-yeongyu/oh-my-openagent | 78 | Rising | very active | 1 | 100% | 281 |
| colbymchenry/codegraph | 78 | Hot | very active | 1 | 95% | 31 |
| upstash/context7 | 78 | Hot | very active | 1 | 57% | 122 |
| Piebald-AI/claude-code-system-prompts | 77 | Rising | very active | 1 | 99% | 236 |
| ruvnet/ruflo | 76 | Hot | very active | 1 | 90% | 1645 |
| MemPalace/mempalace | 76 | Hot | very active | 1 | 52% | 17 |
| NousResearch/hermes-agent | 75 | Hot | very active | 1 | 80% | 33 |
| Egonex-AI/Understand-Anything | 75 | Hot | very active | 1 | 80% | 8 |
| DeusData/codebase-memory-mcp | 75 | Hot | very active | 1 | 93% | 46 |
| MinishLab/semble | 73 | Hot | very active | 1 | 65% | 28 |
| luongnv89/claude-howto | 68 | Rising | very active | 1 | 88% | 10 |
| punkpeye/awesome-mcp-servers | 65 | Hot | very active | 1 | 64% | 0 |
| wshobson/agents | 64 | Hot | very active | 1 | 64% | 0 |
| shanraisshan/claude-code-best-practice | 64 | Rising | very active | 1 | 100% | 0 |
| traceloop/openllmetry | 64 | Classic | active | 1 | 56% | 262 |
| hesreallyhim/awesome-claude-code | 60 | Mature | very active | 1 | 97% | 0 |
| anthropics/claude-cookbooks | 60 | Classic | very active | 2 | 30% | 0 |
| garrytan/gstack | 57 | Hot | very active | 1 | 55% | 0 |
| memvid/memvid | 56 | Declining | slowing | 1 | 100% | 12 |
| campfirein/byterover-cli | 54 | Declining | slowing | 1 | 100% | 27 |
| anthropics/skills | 50 | Rising | active | 2 | 36% | 0 |
| centminmod/my-claude-code-setup | 49 | Mature | active | 1 | 100% | 0 |
| x1xhlol/system-prompts-and-models-of-ai-tools | 48 | Mature | active | 1 | 65% | 0 |
| memodb-io/Acontext | 48 | Declining | slowing | 0 | 0% | 279 |
| patoles/agent-flow | 47 | Mature | slowing | 1 | 71% | 3 |
| ComposioHQ/awesome-claude-skills | 36 | Declining | active | 1 | 100% | 0 |
| multica-ai/andrej-karpathy-skills | 23 | Declining | slowing | 0 | 0% | 0 |

## Adjacent (deliberately not listed here)

- **n8n-io/n8n** (204,240★) — workflow-automation platform — orchestrates agents but isn't a Claude-Code setup layer
- **langgenius/dify** (155,674★) — agentic-workflow platform — covered by the agent-orchestration report
- **langchain-ai/langchain** (146,288★) — agent-engineering library — app framework, not a CC setup tool
- **open-webui/open-webui** (151,961★) — chat UI for local models — a frontend, not an agent setup
- **ultraworkers/claw-code** (195,222★) — art/exhibit harness — not a practical setup layer
- **multica-ai/multica** (49,786★) — managed-agents platform — team product, see agent-orchestration report

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (claude-code / skill / agent harness / mcp / memory / token / observability / code-graph / setup) across name+description+topics, then manual curation into the nine setup layers. General agent *application* frameworks, chat UIs, and broad platforms were routed to adjacent reports or excluded (see above).
- **The three-strategy table is opinionated**, built only from repos in your stars — it is a starting point, not a benchmark. Validate model-tier and token-saver claims against your own `langfuse`/`codeburn` traces.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.

<sub>Tools covered: 59 · Snapshot: 2026-09-14T11:08:08.535Z</sub>
