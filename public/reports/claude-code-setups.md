# Claude Code Superpowers — Setup Strategies from Your Stars

> Derived from **kaiser-data**'s 1,900 starred repos (snapshot `2026-08-31T12:10:08.018Z`), cross-referenced with the repo-similarity graph (1,900 nodes / 6,181 edges, 37 communities).
>
> Generated 2026-08-31 by `scripts/reports/claude_code_setups.py` (regenerate any time — no API cost).

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

- **59 Claude-Code 'superpower' projects** in your stars (**4,847,787★** combined), spanning 9 setup layers:
  - **Harness / coding agent** (12): `openclaw`, `hermes-agent`, `opencode`, `claude-code`, `codex`, `gemini-cli`, `pi`, `deer-flow`, `ruflo`, `cline`, `goose`, `oh-my-claudecode`
  - **Skills framework** (6): `superpowers`, `ECC`, `skills`, `awesome-claude-skills`, `scientific-agent-skills`, `agents`
  - **Config / setup kit** (11): `andrej-karpathy-skills`, `system-prompts-and-models-of-ai-tools`, `gstack`, `cc-switch`, `claude-code-best-practice`, `awesome-claude-code`, `claude-cookbooks`, `claude-howto`, `claude-code-templates`, `claude-code-system-prompts`, `my-claude-code-setup`
  - **Memory / context** (7): `claude-mem`, `mem0`, `mempalace`, `memvid`, `engram`, `byterover-cli`, `Acontext`
  - **Token-saver / compression** (7): `caveman`, `rtk`, `oh-my-openagent`, `headroom`, `toon`, `codeburn`, `semble`
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
| **Token-saver / compression** | Shrink what the model has to read | `caveman`, `rtk`, `oh-my-openagent`, `headroom`, `toon`, `codeburn` |
| **Code-graph / retrieval** | Feed the *right* code, not all of it | `graphify`, `Understand-Anything`, `codegraph`, `GitNexus`, `codebase-memory-mcp` |
| **MCP ecosystem** | External reach (docs, tools, data) | `awesome-mcp-servers`, `servers`, `context7` |
| **Observability / evals** | Measure cost & quality | `langfuse`, `opik`, `phoenix`, `openllmetry`, `agent-flow`, `Irrlicht` |
| **Local runtime** | Cut cost / go offline | `ollama`, `litellm` |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Layer | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Harness / coding agent | TypeScript | NOASSERTION | 388,189 (▲343) | Hot | 79 | very active | 0d ago | 9mo | 19 |
| [obra/superpowers](https://github.com/obra/superpowers) | Skills framework | Shell | MIT | 279,885 (▲1,224) | Hot | 78 | very active | 2d ago | 10mo | 6 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Skills framework | JavaScript | MIT | 244,938 (▲1,173) | Hot | 79 | very active | 0d ago | 7mo | 19 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Harness / coding agent | Python | MIT | 238,749 (▲1,411) | Hot | 80 | very active | 0d ago | 1.1y | 27 |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Config / setup kit | — | — | 209,025 (▲934) | Declining | 24 | slowing | 4mo ago | 7mo | 0 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | Harness / coding agent | TypeScript | MIT | 202,719 (▲747) | Hot | 83 | very active | 0d ago | 1.3y | 15 |
| [ollama/ollama](https://github.com/ollama/ollama) | Local runtime | Go | MIT | 179,825 (▲237) | Classic | 83 | very active | 2d ago | 3.2y | 9 |
| [anthropics/skills](https://github.com/anthropics/skills) | Skills framework | Python | — | 172,734 (▲651) | Rising | 50 | active | 10d ago | 11mo | 5 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Harness / coding agent | Python | — | 143,538 (▲336) | Hot | 76 | very active | 3d ago | 1.5y | 6 |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Config / setup kit | — | GPL-3.0 | 143,254 (▲68) | Mature | 50 | very active | 20d ago | 1.5y | 4 |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Config / setup kit | TypeScript | MIT | 130,541 (▲478) | Hot | 58 | very active | 0d ago | 5mo | 5 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Config / setup kit | Rust | MIT | 130,340 (▲579) | Hot | 77 | very active | 0d ago | 1.1y | 14 |
| [openai/codex](https://github.com/openai/codex) | Harness / coding agent | Rust | Apache-2.0 | 120,352 (▲1,145) | Hot | 94 | very active | 0d ago | 1.4y | 38 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Code-graph / retrieval | Python | Apache-2.0 | 112,846 (▲1,235) | Hot | 86 | very active | 1d ago | 5mo | 25 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Harness / coding agent | TypeScript | Apache-2.0 | 106,751 (▲32) | Hot | 90 | very active | 0d ago | 1.4y | 13 |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Token-saver / compression | Go | NOASSERTION | 101,969 (▲529) | Hot | 78 | very active | 2d ago | 4mo | 11 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness / coding agent | TypeScript | MIT | 99,809 (▲1,498) | Hot | 85 | very active | 0d ago | 1.1y | 13 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP ecosystem | — | MIT | 93,560 (▲665) | Mature | 65 | very active | 2d ago | 1.8y | 1 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Memory / context | JavaScript | Apache-2.0 | 92,714 (▲434) | Hot | 80 | very active | 0d ago | 1.0y | 3 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | MCP ecosystem | TypeScript | NOASSERTION | 89,985 (▲70) | Hot | 84 | very active | 1d ago | 1.8y | 24 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Harness / coding agent | Python | MIT | 81,168 (▲150) | Hot | 84 | very active | 0d ago | 1.3y | 51 |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | Code-graph / retrieval | TypeScript | MIT | 81,154 (▲381) | Hot | 80 | very active | 5d ago | 5mo | 16 |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Token-saver / compression | Rust | Apache-2.0 | 78,015 (▲380) | Hot | 78 | very active | 0d ago | 7mo | 9 |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Skills framework | Python | — | 74,118 (▲506) | Declining | 37 | active | 21d ago | 10mo | 1 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Harness / coding agent | TypeScript | MIT | 69,923 (▲355) | Hot | 76 | very active | 0d ago | 1.2y | 7 |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | Code-graph / retrieval | C | MIT | 68,800 (▲414) | Hot | 77 | very active | 5d ago | 7mo | 5 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Token-saver / compression | TypeScript | NOASSERTION | 68,547 (▲98) | Hot | 78 | very active | 0d ago | 9mo | 4 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Token-saver / compression | Python | Apache-2.0 | 68,158 (▲328) | Hot | 82 | very active | 0d ago | 7mo | 14 |
| [cline/cline](https://github.com/cline/cline) | Harness / coding agent | TypeScript | Apache-2.0 | 67,216 (▲198) | Mature | 78 | very active | 0d ago | 2.2y | 12 |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Config / setup kit | HTML | MIT | 65,417 (▲155) | Rising | 64 | very active | 0d ago | 10mo | 1 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Memory / context | Python | Apache-2.0 | 64,420 (▲217) | Classic | 79 | very active | 0d ago | 3.2y | 25 |
| [upstash/context7](https://github.com/upstash/context7) | MCP ecosystem | TypeScript | MIT | 61,439 (▲130) | Hot | 79 | very active | 0d ago | 1.4y | 12 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Memory / context | Python | MIT | 58,747 (▲62) | Hot | 76 | very active | 0d ago | 4mo | 10 |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Local runtime | Python | NOASSERTION | 57,662 (▲237) | Classic | 84 | very active | 0d ago | 3.1y | 8 |
| [aaif-goose/goose](https://github.com/aaif-goose/goose) | Harness / coding agent | Rust | Apache-2.0 | 53,732 (▲150) | Mature | 89 | very active | 0d ago | 2.0y | 29 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Config / setup kit | Python | NOASSERTION | 53,272 (▲175) | Mature | 60 | very active | 0d ago | 1.4y | 1 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Config / setup kit | Jupyter Notebook | MIT | 52,313 (▲102) | Classic | 66 | very active | 3d ago | 3.0y | 11 |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | Code-graph / retrieval | TypeScript | NOASSERTION | 46,725 (▲769) | Hot | 83 | very active | 0d ago | 1.1y | 20 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Code-graph / retrieval | C | MIT | 41,415 (▲514) | Hot | 75 | very active | 0d ago | 6mo | 7 |
| [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | Config / setup kit | Python | MIT | 41,278 (▲57) | Rising | 68 | very active | 5d ago | 9mo | 3 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Skills framework | Python | MIT | 40,339 (▲5,020) | Hot | 79 | very active | 0d ago | 10mo | 8 |
| [wshobson/agents](https://github.com/wshobson/agents) | Skills framework | Python | MIT | 39,292 (▲91) | Hot | 64 | very active | 0d ago | 1.1y | 16 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Harness / coding agent | TypeScript | MIT | 38,913 (▲85) | Hot | 80 | very active | 0d ago | 7mo | 4 |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Observability / evals | TypeScript | NOASSERTION | 33,971 (▲151) | Classic | 89 | very active | 0d ago | 3.3y | 13 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Config / setup kit | Python | MIT | 30,466 (▲40) | Hot | 80 | very active | 0d ago | 1.2y | 21 |
| [toon-format/toon](https://github.com/toon-format/toon) | Token-saver / compression | TypeScript | MIT | 25,281 (▲14) | Hot | 80 | very active | 0d ago | 10mo | 5 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Observability / evals | Python | Apache-2.0 | 21,710 (▲68) | Classic | 93 | very active | 0d ago | 3.3y | 26 |
| [memvid/memvid](https://github.com/memvid/memvid) | Memory / context | Rust | Apache-2.0 | 16,455 (▼1) | Declining | 57 | active | 1mo ago | 1.3y | 1 |
| [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | Config / setup kit | JavaScript | MIT | 12,526 (▲51) | Hot | 77 | very active | 3d ago | 9mo | 3 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Observability / evals | Python | NOASSERTION | 11,261 (▲43) | Classic | 84 | very active | 0d ago | 3.8y | 21 |
| [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | Token-saver / compression | TypeScript | MIT | 9,761 (▲70) | Hot | 79 | very active | 0d ago | 4mo | 5 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Observability / evals | Python | Apache-2.0 | 7,410 (▲6) | Mature | 65 | active | 21d ago | 3.0y | 4 |
| [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram) | Memory / context | Go | MIT | 6,242 (▲44) | Rising | 77 | very active | 0d ago | 6mo | 2 |
| [MinishLab/semble](https://github.com/MinishLab/semble) | Token-saver / compression | Python | MIT | 5,970 (▲6) | Hot | 73 | very active | 5d ago | 4mo | 7 |
| [campfirein/byterover-cli](https://github.com/campfirein/byterover-cli) | Memory / context | TypeScript | NOASSERTION | 4,954 (▲4) | Declining | 56 | slowing | 2mo ago | 1.2y | 1 |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | Memory / context | JavaScript | Apache-2.0 | 3,678 (▲2) | Declining | 49 | active | 1mo ago | 1.1y | 0 |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | Config / setup kit | Python | MIT | 2,611 (▲4) | Mature | 51 | very active | 1mo ago | 1.1y | 1 |
| [patoles/agent-flow](https://github.com/patoles/agent-flow) | Observability / evals | TypeScript | Apache-2.0 | 1,610 (▲3) | Mature | 49 | active | 1mo ago | 5mo | 2 |
| [ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht) | Observability / evals | Go | MIT | 95 | Hot | 80 | very active | 1d ago | 12mo | 4 |

## By layer

### Harness / coding agent

_The loop that reads, plans, edits, and runs. Pick one as your daily driver; keep a second installed to diff behavior and model-shop._

- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · 388,189★ · TypeScript · Hot  
  Cross-platform personal-assistant harness — an 'any OS, any platform' agent runtime.  
  <sub>topics: ai, assistant, own-your-data, personal, crustacean, molty, openclaw</sub>
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 238,749★ · Python · Hot  
  Long-lived 'agent that grows with you' harness — persistent, personalized agent loop.  
  <sub>topics: ai, ai-agent, ai-agents, llm, anthropic, chatgpt, claude, claude-code</sub>
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 202,719★ · TypeScript · Hot  
  Open-source terminal coding agent — a provider-agnostic alternative harness.  
  <sub>topics: —</sub>
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 143,538★ · Python · Hot  
  Claude Code itself — the agentic CLI that lives in your terminal; the baseline every setup here extends.  
  <sub>topics: —</sub>
- **[openai/codex](https://github.com/openai/codex)** · 120,352★ · Rust · Hot  
  OpenAI's lightweight terminal coding agent — useful as a second harness to diff behavior against Claude Code.  
  <sub>topics: —</sub>
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 106,751★ · TypeScript · Hot  
  Gemini's open-source terminal agent — the third major CLI harness; handy for model-shopping.  
  <sub>topics: gemini, gemini-api, ai, ai-agents, cli, mcp-client, mcp-server</sub>
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 99,809★ · TypeScript · Hot  
  Unified LLM-API + agent-loop + TUI toolkit — a kit for rolling your own coding agent.  
  <sub>topics: —</sub>
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 81,168★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and writes — multi-step autonomy.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 69,923★ · TypeScript · Hot  
  Agent meta-harness for Claude — deploys multi-agent swarms with coordination.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server</sub>
- **[cline/cline](https://github.com/cline/cline)** · 67,216★ · TypeScript · Mature  
  Autonomous coding agent as SDK / IDE extension / CLI — strong for in-editor agentic workflows.  
  <sub>topics: —</sub>
- **[aaif-goose/goose](https://github.com/aaif-goose/goose)** · 53,732★ · Rust · Mature  
  Extensible open agent that installs and runs tools, not just suggestions — MCP-native.  
  <sub>topics: mcp, acp, ai, ai-agents</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 38,913★ · TypeScript · Hot  
  Teams-first multi-agent orchestration layer for Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>

### Skills framework

_The biggest 2026 upgrade. Skills load only when triggered, so they add capability without taxing every session — the opposite of a big always-on CLAUDE.md._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 279,885★ · Shell · Hot  
  Agentic skills framework + dev methodology — the headline 'give your agent superpowers' skill collection.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 244,938★ · JavaScript · Hot  
  Agent-harness performance system bundling skills, instincts, and memory into one optimization layer.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[anthropics/skills](https://github.com/anthropics/skills)** · 172,734★ · Python · Rising  
  Anthropic's official Agent Skills repo — canonical examples of the skills format.  
  <sub>topics: agent-skills</sub>
- **[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** · 74,118★ · Python · Declining  
  Curated index of Claude Skills + tooling — the discovery hub for what's worth installing.  
  <sub>topics: claude, claude-code, agent-skills, ai-agents, antigravity, automation, codex, composio</sub>
- **[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)** · 40,339★ · Python · Hot  
  Domain skill pack that turns an agent into a research scientist — example of vertical skills.  
  <sub>topics: ai-scientist, bioinformatics, chemoinformatics, claude, claude-skills, claudecode, clinical-research, computational-biology</sub>
- **[wshobson/agents](https://github.com/wshobson/agents)** · 39,292★ · Python · Hot  
  Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor) — subagents & commands.  
  <sub>topics: agents, anthropic, agent-skills, agentic-ai, ai-agents, cursor, cursor-rules, mcp</sub>

### Config / setup kit

_Turnkey CLAUDE.md / command / hook bundles. Steal a good one, then trim to what you actually use — bloat here is paid on every prompt._

- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 209,025★ · — · Declining  
  A single CLAUDE.md derived from Karpathy's habits — the 'one good config file' approach.  
  <sub>topics: —</sub>
- **[x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)** · 143,254★ · — · Mature  
  Leaked/collected system prompts of major AI coding tools — prompt-engineering reference.  
  <sub>topics: ai, cursor, lovable, system-prompts, v0, cursorai, devin, replit</sub>
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 130,541★ · TypeScript · Hot  
  Garry Tan's exact Claude Code setup — 23 opinionated tools as a turnkey starting point.  
  <sub>topics: —</sub>
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 130,340★ · Rust · Hot  
  Desktop all-in-one for managing Claude Code/Codex/OpenClaw — swap providers & configs fast.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, codex, mcp</sub>
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 65,417★ · HTML · Rising  
  Best-practices collection: vibe-coding → agentic engineering.  
  <sub>topics: claude-ai, claude-code, best-practices, claude, claude-code-best-practices, agentic-engineering, anthropic, claude-code-agents</sub>
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 53,272★ · Python · Mature  
  The awesome-list for Claude Code skills, hooks, slash-commands, and orchestrators.  
  <sub>topics: anthropic, anthropic-claude, awesome, awesome-list, awesome-lists, awesome-resources, claude, claude-code</sub>
- **[anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)** · 52,313★ · Jupyter Notebook · Classic  
  Official recipes/notebooks for effective Claude usage patterns.  
  <sub>topics: —</sub>
- **[luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)** · 41,278★ · Python · Rising  
  Visual, example-driven guide to Claude Code from basics to advanced — the learning path.  
  <sub>topics: claude-code, guide, tutorial</sub>
- **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** · 30,466★ · Python · Hot  
  CLI to configure AND monitor Claude Code — installs commands/agents/hooks and watches usage.  
  <sub>topics: anthropic, anthropic-claude, claude, claude-code</sub>
- **[Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts)** · 12,526★ · JavaScript · Hot  
  Claude Code's full system prompt + 27 builtin tool descriptions — know what you're configuring.  
  <sub>topics: claude-code, claude-code-system-prompts, system-prompts</sub>
- **[centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup)** · 2,611★ · Python · Mature  
  A shared starter CLAUDE.md + memory-bank configuration template you can fork.  
  <sub>topics: claude, claude-ai, claude-code, subagents, claudecode-config, claudecode-hooks, claudecode-subagents</sub>

### Memory / context

_Persist decisions and context across sessions so the agent doesn't re-derive what it already learned. The backend is swappable._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 92,714★ · JavaScript · Hot  
  Persistent context across sessions for every agent — captures work and re-injects it (you run this).  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude, claude-agent-sdk, claude-agents</sub>
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 64,420★ · Python · Classic  
  Universal memory layer for AI agents — the most-adopted general memory backend.  
  <sub>topics: ai, chatgpt, llm, python, chatbots, rag, application, long-term-memory</sub>
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 58,747★ · Python · Hot  
  Best-benchmarked open-source AI memory system — drop-in long-term memory.  
  <sub>topics: ai, chromadb, llm, mcp, memory, python</sub>
- **[memvid/memvid](https://github.com/memvid/memvid)** · 16,455★ · Rust · Declining  
  Memory layer that replaces RAG pipelines with a compact server — novel storage approach.  
  <sub>topics: ai, context, embedded, faiss, knowledge-base, knowledge-graph, llm, machine-learning</sub>
- **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** · 6,242★ · Go · Rising  
  Agent-agnostic Go binary giving coding agents persistent memory.  
  <sub>topics: —</sub>
- **[campfirein/byterover-cli](https://github.com/campfirein/byterover-cli)** · 4,954★ · TypeScript · Declining  
  Portable memory layer (brv) for autonomous coding agents — agent-agnostic.  
  <sub>topics: agent, llm, mcp, memory, vibe-coding, ai, autonomous-agents, cli</sub>
- **[memodb-io/Acontext](https://github.com/memodb-io/Acontext)** · 3,678★ · JavaScript · Declining  
  Treats Agent Skills as a memory layer — skills-as-memory hybrid.  
  <sub>topics: agent, context-engineering, data-platform, self-learning, agent-development-kit, ai-agent, llm, memory</sub>

### Token-saver / compression

_Measure first (`codeburn`), then compress: leaner code search, output trimming, and a front proxy stack to 60–90% on common loops._

- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 101,969★ · Go · Hot  
  'Why use many token when few token do trick' — a Claude Code skill that aggressively trims tokens.  
  <sub>topics: ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering</sub>
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 78,015★ · Rust · Hot  
  CLI proxy that cuts LLM token consumption 60–90% on common dev commands — sits in front of the agent.  
  <sub>topics: agentic-coding, ai-coding, anthropic, claude-code, cli, command-line-tool, cost-reduction, developer-tools</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 68,547★ · TypeScript · Hot  
  omo/lazycodex — a coding agent built for 'tokenmaxxers'; efficiency-first harness.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 68,158★ · Python · Hot  
  Compresses tool outputs, logs, files, and RAG chunks before they hit the model's context.  
  <sub>topics: agent, ai, anthropic, compression, context-engineering, context-window, fastapi, langchain</sub>
- **[toon-format/toon](https://github.com/toon-format/toon)** · 25,281★ · TypeScript · Hot  
  Token-Oriented Object Notation — compact schema-aware encoding to shrink structured payloads.  
  <sub>topics: data-format, llm, serialization, tokenization</sub>
- **[getagentseal/codeburn](https://github.com/getagentseal/codeburn)** · 9,761★ · TypeScript · Hot  
  TUI dashboard showing where your AI coding tokens go — measure before you optimize.  
  <sub>topics: ai-coding, claude-code, cli, codex, cost-tracking, developer-tools, observability, terminal-ui</sub>
- **[MinishLab/semble](https://github.com/MinishLab/semble)** · 5,970★ · Python · Hot  
  Fast, accurate code search for agents using ~98% fewer tokens than reading files.  
  <sub>topics: agents, code-search, embeddings, mcp, mcp-server, model-context-protocol, retrieval</sub>

### Code-graph / retrieval

_Give the agent structure instead of raw files — graphs and indexes answer 'how does X relate to Y' without scanning the repo._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 112,846★ · Python · Hot  
  Coding-assistant skill that turns a repo into a knowledge graph (you use this on this project).  
  <sub>topics: claude-code, graphrag, knowledge-graph, codex, openclaw, skills, antigravity, gemini</sub>
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 81,154★ · TypeScript · Hot  
  Turns any code into an interactive teaching graph — comprehension over impression.  
  <sub>topics: claude-code, claude-skills, understandcode, codex, codex-skills, knowledge-graph, opencode-skills, antigravity-skills</sub>
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 68,800★ · C · Hot  
  Pre-indexed code knowledge graph for Claude Code/Codex/Cursor — structural retrieval.  
  <sub>topics: —</sub>
- **[abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)** · 46,725★ · TypeScript · Hot  
  Zero-server code-intelligence engine — client-side code graph.  
  <sub>topics: —</sub>
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 41,415★ · C · Hot  
  High-performance code-intelligence MCP server — indexes codebases for retrieval.  
  <sub>topics: claude-code, code-analysis, code-intelligence, developer-tools, knowledge-graph, mcp, mcp-server, model-context-protocol</sub>

### MCP ecosystem

_External capabilities via a standard protocol. Each connected server costs context, so connect deliberately — `context7` (live docs) is the highest-ROI default._

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 93,560★ · — · Mature  
  The big community index of MCP servers — discovery for what to connect.  
  <sub>topics: ai, mcp</sub>
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 89,985★ · TypeScript · Hot  
  The official reference MCP servers — the canonical catalog of capabilities to plug in.  
  <sub>topics: —</sub>
- **[upstash/context7](https://github.com/upstash/context7)** · 61,439★ · TypeScript · Hot  
  Up-to-date library docs for LLMs via MCP — kills 'hallucinated API' errors (you have this wired).  
  <sub>topics: llm, mcp, mcp-server, vibe-coding</sub>

### Observability / evals

_You can't optimize what you can't see. Trace runs, watch spend, and score outputs before trusting an autonomous setup._

- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 33,971★ · TypeScript · Classic  
  Open-source LLM engineering platform: traces, evals, metrics, prompts (you trace Claude Code into this).  
  <sub>topics: analytics, llm, llmops, large-language-models, openai, self-hosted, ycombinator, monitoring</sub>
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 21,710★ · Python · Classic  
  Debug/evaluate/monitor LLM apps, RAG, and agents — eval-first observability.  
  <sub>topics: open-source, langchain, openai, playground, prompt-engineering, llama-index, llm, llm-evaluation</sub>
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 11,261★ · Python · Classic  
  AI observability & evaluation — OpenTelemetry-based tracing for agents.  
  <sub>topics: llmops, ai-monitoring, ai-observability, llm-eval, aiengineering, datasets, agents, llms</sub>
- **[traceloop/openllmetry](https://github.com/traceloop/openllmetry)** · 7,410★ · Python · Mature  
  Open-source OpenTelemetry-based observability for LLM apps — standards-based traces.  
  <sub>topics: llmops, observability, open-telemetry, metrics, monitoring, opentelemetry, datascience, ml</sub>
- **[patoles/agent-flow](https://github.com/patoles/agent-flow)** · 1,610★ · TypeScript · Mature  
  Real-time visualization of Claude Code agent orchestration — watch agents think, branch, coordinate.  
  <sub>topics: agent-visualization, ai-agents, claude-code, developer-tools, llm, vscode-extension</sub>
- **[ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht)** · 95★ · Go · Hot  
  Claude Code session lights in the macOS menu bar — at-a-glance session state.  
  <sub>topics: —</sub>

### Local runtime

_Run open models locally or proxy many models behind one endpoint — the cost floor for grunt work and the fallback when the cloud is down._

- **[ollama/ollama](https://github.com/ollama/ollama)** · 179,825★ · Go · Classic  
  Run open models locally with one command — point an agent at it to slash API cost or go offline.  
  <sub>topics: llama, llm, llms, go, golang, ollama, mistral, gemma</sub>
- **[BerriAI/litellm](https://github.com/BerriAI/litellm)** · 57,662★ · Python · Classic  
  OpenAI-compatible proxy/gateway to 100+ LLMs — swap models under any harness from one endpoint.  
  <sub>topics: anthropic, langchain, llm, llmops, openai, ai-gateway, azure-openai, bedrock</sub>

## Graph analysis — how they relate

**Community clustering.** These 59 tools span **17 of the graph's 37 communities** — the Claude-Code ecosystem is spread across agent-framework, memory, retrieval, and observability neighborhoods rather than forming one tidy cluster.

- **Community 7** (8): `NousResearch/hermes-agent`, `obra/superpowers`, `centminmod/my-claude-code-setup`, `davila7/claude-code-templates`, `mem0ai/mem0`, `MemPalace/mempalace`, `memodb-io/Acontext`, `headroomlabs-ai/headroom`
- **Community 15** (8): `affaan-m/ECC`, `ComposioHQ/awesome-claude-skills`, `wshobson/agents`, `rtk-ai/rtk`, `code-yeongyu/oh-my-openagent`, `Graphify-Labs/graphify`, `DeusData/codebase-memory-mcp`, `patoles/agent-flow`
- **Community 2** (7): `earendil-works/pi`, `K-Dense-AI/scientific-agent-skills`, `farion1231/cc-switch`, `hesreallyhim/awesome-claude-code`, `JuliusBrussee/caveman`, `colbymchenry/codegraph`, `traceloop/openllmetry`
- **Community 18** (6): `google-gemini/gemini-cli`, `aaif-goose/goose`, `MinishLab/semble`, `modelcontextprotocol/servers`, `punkpeye/awesome-mcp-servers`, `upstash/context7`
- **Community 24** (5): `anthropics/claude-code`, `anthropics/skills`, `luongnv89/claude-howto`, `Piebald-AI/claude-code-system-prompts`, `anthropics/claude-cookbooks`
- **Community 9** (5): `ruvnet/ruflo`, `Gentleman-Programming/engram`, `getagentseal/codeburn`, `abhigyanpatwari/GitNexus`, `ingo-eichhorst/Irrlicht`
- **Community 1** (4): `anomalyco/opencode`, `Yeachan-Heo/oh-my-claudecode`, `x1xhlol/system-prompts-and-models-of-ai-tools`, `Egonex-AI/Understand-Anything`
- **Community 19** (4): `langfuse/langfuse`, `comet-ml/opik`, `Arize-ai/phoenix`, `BerriAI/litellm`
- **Community 10** (2): `openclaw/openclaw`, `garrytan/gstack`
- **Community 13** (2): `bytedance/deer-flow`, `ollama/ollama`
- **Community 21** (2): `shanraisshan/claude-code-best-practice`, `thedotmack/claude-mem`

**Centrality (PageRank in the full 1,900-repo graph)** — the most 'hub-like' setup tools in your ecosystem:

- `hesreallyhim/awesome-claude-code` — PageRank 0.0055
- `affaan-m/ECC` — PageRank 0.0016
- `shanraisshan/claude-code-best-practice` — PageRank 0.0014
- `MemPalace/mempalace` — PageRank 0.0013
- `wshobson/agents` — PageRank 0.0012
- `multica-ai/andrej-karpathy-skills` — PageRank 0.0011
- `comet-ml/opik` — PageRank 0.0010
- `davila7/claude-code-templates` — PageRank 0.0009
- `punkpeye/awesome-mcp-servers` — PageRank 0.0009
- `anthropics/skills` — PageRank 0.0008

**Direct links between these tools** (top similarity edges where both endpoints are in this report):

- `shanraisshan/claude-code-best-practice` ⇄ `thedotmack/claude-mem` (w=0.810) — topics: claude-code, claude, anthropic, ai; authors: claude
- `anthropics/skills` ⇄ `anthropics/claude-code` (w=0.750) — authors: williamqian12
- `anthropics/claude-cookbooks` ⇄ `anthropics/skills` (w=0.633) — authors: cj-ant
- `hesreallyhim/awesome-claude-code` ⇄ `traceloop/openllmetry` (w=0.578) — topics: llm; authors: github-actions[bot]
- `langfuse/langfuse` ⇄ `comet-ml/opik` (w=0.524) — topics: llm, llmops, openai, open-source
- `aaif-goose/goose` ⇄ `punkpeye/awesome-mcp-servers` (w=0.500) — topics: mcp, ai
- `patoles/agent-flow` ⇄ `affaan-m/ECC` (w=0.400) — topics: ai-agents, claude-code, developer-tools, llm
- `colbymchenry/codegraph` ⇄ `hesreallyhim/awesome-claude-code` (w=0.400) — authors: github-actions[bot]
- `wshobson/agents` ⇄ `ComposioHQ/awesome-claude-skills` (w=0.371) — topics: agent-skills, ai-agents, cursor, mcp
- `hesreallyhim/awesome-claude-code` ⇄ `K-Dense-AI/scientific-agent-skills` (w=0.359) — topics: claude, agent-skills; authors: github-actions[bot]
- `hesreallyhim/awesome-claude-code` ⇄ `davila7/claude-code-templates` (w=0.356) — topics: anthropic, anthropic-claude, claude, claude-code; authors: github-actions[bot]
- `JuliusBrussee/caveman` ⇄ `MemPalace/mempalace` (w=0.353) — topics: ai, llm; authors: SomSamantray, AmirF194
- `JuliusBrussee/caveman` ⇄ `hesreallyhim/awesome-claude-code` (w=0.342) — topics: anthropic, claude, claude-code, llm; authors: github-actions[bot]
- `JuliusBrussee/caveman` ⇄ `davila7/claude-code-templates` (w=0.337) — topics: anthropic, claude, claude-code; authors: github-actions[bot]
- `NousResearch/hermes-agent` ⇄ `code-yeongyu/oh-my-openagent` (w=0.333) — topics: ai, ai-agents, anthropic, chatgpt
- …and 11 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). This ecosystem moves fast and a lot of it is one-person projects — check before wiring one into your daily loop.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| openai/codex | 94 | Hot | very active | 7 | 21% | 1040 |
| comet-ml/opik | 93 | Classic | very active | 4 | 17% | 563 |
| google-gemini/gemini-cli | 90 | Hot | very active | 3 | 19% | 606 |
| aaif-goose/goose | 89 | Mature | very active | 3 | 32% | 148 |
| langfuse/langfuse | 89 | Classic | very active | 3 | 23% | 669 |
| Graphify-Labs/graphify | 86 | Hot | very active | 3 | 32% | 199 |
| earendil-works/pi | 85 | Hot | very active | 2 | 33% | 257 |
| bytedance/deer-flow | 84 | Hot | very active | 12 | 8% | 1 |
| modelcontextprotocol/servers | 84 | Hot | very active | 3 | 27% | 27 |
| Arize-ai/phoenix | 84 | Classic | very active | 2 | 44% | 796 |
| BerriAI/litellm | 84 | Classic | very active | 2 | 39% | 1449 |
| anomalyco/opencode | 83 | Hot | very active | 2 | 32% | 867 |
| abhigyanpatwari/GitNexus | 83 | Hot | very active | 2 | 35% | 787 |
| ollama/ollama | 83 | Classic | very active | 2 | 35% | 249 |
| headroomlabs-ai/headroom | 82 | Hot | very active | 2 | 46% | 169 |
| NousResearch/hermes-agent | 80 | Hot | very active | 2 | 42% | 30 |
| Yeachan-Heo/oh-my-claudecode | 80 | Hot | very active | 1 | 82% | 248 |
| davila7/claude-code-templates | 80 | Hot | very active | 2 | 31% | 19 |
| thedotmack/claude-mem | 80 | Hot | very active | 1 | 98% | 313 |
| toon-format/toon | 80 | Hot | very active | 1 | 96% | 31 |
| Egonex-AI/Understand-Anything | 80 | Hot | very active | 2 | 48% | 8 |
| ingo-eichhorst/Irrlicht | 80 | Hot | very active | 1 | 94% | 41 |
| openclaw/openclaw | 79 | Hot | very active | 1 | 70% | 237 |
| affaan-m/ECC | 79 | Hot | very active | 1 | 58% | 16 |
| K-Dense-AI/scientific-agent-skills | 79 | Hot | very active | 1 | 86% | 102 |
| mem0ai/mem0 | 79 | Classic | very active | 1 | 53% | 393 |
| getagentseal/codeburn | 79 | Hot | very active | 1 | 77% | 63 |
| upstash/context7 | 79 | Hot | very active | 1 | 53% | 109 |
| cline/cline | 78 | Mature | very active | 1 | 65% | 398 |
| obra/superpowers | 78 | Hot | very active | 1 | 82% | 12 |
| JuliusBrussee/caveman | 78 | Hot | very active | 1 | 77% | 29 |
| rtk-ai/rtk | 78 | Hot | very active | 2 | 35% | 297 |
| code-yeongyu/oh-my-openagent | 78 | Hot | very active | 1 | 76% | 254 |
| farion1231/cc-switch | 77 | Hot | very active | 1 | 52% | 52 |
| Piebald-AI/claude-code-system-prompts | 77 | Hot | very active | 1 | 98% | 223 |
| Gentleman-Programming/engram | 77 | Rising | very active | 1 | 87% | 99 |
| colbymchenry/codegraph | 77 | Hot | very active | 1 | 83% | 31 |
| anthropics/claude-code | 76 | Hot | very active | 1 | 89% | 203 |
| ruvnet/ruflo | 76 | Hot | very active | 1 | 76% | 1637 |
| MemPalace/mempalace | 76 | Hot | very active | 1 | 61% | 17 |
| DeusData/codebase-memory-mcp | 75 | Hot | very active | 1 | 89% | 46 |
| MinishLab/semble | 73 | Hot | very active | 1 | 56% | 26 |
| luongnv89/claude-howto | 68 | Rising | very active | 1 | 88% | 10 |
| anthropics/claude-cookbooks | 66 | Classic | very active | 3 | 31% | 0 |
| punkpeye/awesome-mcp-servers | 65 | Mature | very active | 1 | 100% | 0 |
| traceloop/openllmetry | 65 | Mature | active | 1 | 61% | 262 |
| wshobson/agents | 64 | Hot | very active | 1 | 61% | 0 |
| shanraisshan/claude-code-best-practice | 64 | Rising | very active | 1 | 100% | 0 |
| hesreallyhim/awesome-claude-code | 60 | Mature | very active | 1 | 100% | 0 |
| garrytan/gstack | 58 | Hot | very active | 1 | 59% | 0 |
| memvid/memvid | 57 | Declining | active | 1 | 100% | 12 |
| campfirein/byterover-cli | 56 | Declining | slowing | 1 | 100% | 27 |
| centminmod/my-claude-code-setup | 51 | Mature | very active | 1 | 100% | 0 |
| anthropics/skills | 50 | Rising | active | 2 | 47% | 0 |
| x1xhlol/system-prompts-and-models-of-ai-tools | 50 | Mature | very active | 1 | 62% | 0 |
| memodb-io/Acontext | 49 | Declining | active | 0 | 0% | 279 |
| patoles/agent-flow | 49 | Mature | active | 1 | 71% | 3 |
| ComposioHQ/awesome-claude-skills | 37 | Declining | active | 1 | 100% | 0 |
| multica-ai/andrej-karpathy-skills | 24 | Declining | slowing | 0 | 0% | 0 |

## Adjacent (deliberately not listed here)

- **n8n-io/n8n** (202,943★) — workflow-automation platform — orchestrates agents but isn't a Claude-Code setup layer
- **langgenius/dify** (153,989★) — agentic-workflow platform — covered by the agent-orchestration report
- **langchain-ai/langchain** (145,332★) — agent-engineering library — app framework, not a CC setup tool
- **open-webui/open-webui** (150,483★) — chat UI for local models — a frontend, not an agent setup
- **ultraworkers/claw-code** (195,161★) — art/exhibit harness — not a practical setup layer
- **multica-ai/multica** (48,377★) — managed-agents platform — team product, see agent-orchestration report

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (claude-code / skill / agent harness / mcp / memory / token / observability / code-graph / setup) across name+description+topics, then manual curation into the nine setup layers. General agent *application* frameworks, chat UIs, and broad platforms were routed to adjacent reports or excluded (see above).
- **The three-strategy table is opinionated**, built only from repos in your stars — it is a starting point, not a benchmark. Validate model-tier and token-saver claims against your own `langfuse`/`codeburn` traces.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.

<sub>Tools covered: 59 · Snapshot: 2026-08-31T12:10:08.018Z</sub>
