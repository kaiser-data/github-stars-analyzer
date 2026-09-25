# Claude Code Superpowers — Setup Strategies from Your Stars

> Derived from **kaiser-data**'s 2,243 starred repos (snapshot `2026-09-25T10:37:19.717Z`), cross-referenced with the repo-similarity graph (2,243 nodes / 7,393 edges, 35 communities).
>
> Generated 2026-09-25 by `scripts/reports/claude_code_setups.py` (regenerate any time — no API cost).

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

- **59 Claude-Code 'superpower' projects** in your stars (**5,015,783★** combined), spanning 9 setup layers:
  - **Harness / coding agent** (12): `openclaw`, `hermes-agent`, `opencode`, `claude-code`, `codex`, `pi`, `gemini-cli`, `deer-flow`, `ruflo`, `cline`, `goose`, `oh-my-claudecode`
  - **Skills framework** (6): `superpowers`, `ECC`, `skills`, `awesome-claude-skills`, `scientific-agent-skills`, `agents`
  - **Config / setup kit** (11): `andrej-karpathy-skills`, `system-prompts-and-models-of-ai-tools`, `cc-switch`, `gstack`, `claude-code-best-practice`, `awesome-claude-code`, `claude-cookbooks`, `claude-howto`, `claude-code-templates`, `claude-code-system-prompts`, `my-claude-code-setup`
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
| **Harness / coding agent** | The agent loop itself | `openclaw`, `hermes-agent`, `opencode`, `claude-code`, `codex`, `pi` |
| **Skills framework** | On-demand expertise (the modern superpower) | `superpowers`, `ECC`, `skills`, `awesome-claude-skills`, `scientific-agent-skills`, `agents` |
| **Config / setup kit** | Shape behavior up front, cheaply | `andrej-karpathy-skills`, `system-prompts-and-models-of-ai-tools`, `cc-switch`, `gstack`, `claude-code-best-practice`, `awesome-claude-code` |
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
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Harness / coding agent | TypeScript | NOASSERTION | 390,467 (▲286) | Hot | 84 | very active | 0d ago | 10mo | 14 |
| [obra/superpowers](https://github.com/obra/superpowers) | Skills framework | Shell | MIT | 291,377 (▲1,866) | Hot | 75 | very active | 0d ago | 11mo | 6 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Skills framework | JavaScript | MIT | 267,158 (▲2,868) | Hot | 79 | very active | 1d ago | 8mo | 26 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Harness / coding agent | Python | MIT | 248,814 (▲1,187) | Hot | 80 | very active | 0d ago | 1.2y | 11 |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Config / setup kit | — | — | 215,056 (▲623) | Declining | 22 | slowing | 5mo ago | 8mo | 0 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | Harness / coding agent | TypeScript | MIT | 209,940 (▲922) | Hot | 83 | very active | 0d ago | 1.4y | 17 |
| [ollama/ollama](https://github.com/ollama/ollama) | Local runtime | Go | MIT | 181,673 (▲315) | Classic | 83 | very active | 0d ago | 3.3y | 9 |
| [anthropics/skills](https://github.com/anthropics/skills) | Skills framework | Python | — | 178,045 (▲642) | Mature | 50 | active | 1d ago | 1.0y | 5 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Harness / coding agent | TypeScript | — | 148,017 (▲638) | Hot | 79 | very active | 0d ago | 1.6y | 5 |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Config / setup kit | — | GPL-3.0 | 143,855 (▲91) | Mature | 47 | active | 1mo ago | 1.6y | 3 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Config / setup kit | Rust | MIT | 136,676 (▲2,755) | Hot | 81 | very active | 0d ago | 1.1y | 39 |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Config / setup kit | TypeScript | MIT | 134,161 (▲332) | Hot | 58 | very active | 0d ago | 6mo | 5 |
| [openai/codex](https://github.com/openai/codex) | Harness / coding agent | Rust | Apache-2.0 | 126,387 (▲724) | Hot | 94 | very active | 0d ago | 1.5y | 37 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Code-graph / retrieval | Python | Apache-2.0 | 121,287 (▲1,247) | Hot | 81 | very active | 2d ago | 5mo | 15 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness / coding agent | TypeScript | MIT | 109,259 (▲1,270) | Hot | 80 | very active | 0d ago | 1.1y | 10 |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Token-saver / compression | Go | NOASSERTION | 107,770 (▲691) | Hot | 78 | very active | 0d ago | 5mo | 12 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Harness / coding agent | TypeScript | Apache-2.0 | 107,159 (▲53) | Hot | 95 | very active | 0d ago | 1.4y | 18 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP ecosystem | — | MIT | 95,504 (▲127) | Hot | 60 | very active | 2d ago | 1.8y | 32 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Memory / context | TypeScript | Apache-2.0 | 94,658 (▲282) | Hot | 80 | very active | 0d ago | 1.1y | 16 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | MCP ecosystem | TypeScript | NOASSERTION | 90,584 (▲65) | Hot | 90 | very active | 3d ago | 1.8y | 35 |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | Code-graph / retrieval | TypeScript | MIT | 84,129 (▲616) | Hot | 74 | very active | 13d ago | 6mo | 11 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Harness / coding agent | Python | MIT | 82,962 (▲168) | Hot | 87 | very active | 0d ago | 1.4y | 51 |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Token-saver / compression | Rust | Apache-2.0 | 81,687 (▲460) | Hot | 75 | very active | 0d ago | 8mo | 12 |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Skills framework | Python | — | 75,611 (▲188) | Declining | 38 | active | 7d ago | 11mo | 1 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Token-saver / compression | Python | Apache-2.0 | 73,757 (▲418) | Hot | 98 | very active | 0d ago | 8mo | 37 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Harness / coding agent | TypeScript | MIT | 73,238 (▲265) | Hot | 76 | very active | 0d ago | 1.3y | 8 |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | Code-graph / retrieval | C | MIT | 72,059 (▲384) | Hot | 77 | very active | 2d ago | 8mo | 5 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Token-saver / compression | TypeScript | NOASSERTION | 69,395 (▲149) | Hot | 78 | very active | 0d ago | 9mo | 3 |
| [cline/cline](https://github.com/cline/cline) | Harness / coding agent | TypeScript | Apache-2.0 | 69,273 (▲353) | Mature | 78 | very active | 0d ago | 2.2y | 10 |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Config / setup kit | HTML | MIT | 66,321 (▲164) | Rising | 64 | very active | 0d ago | 10mo | 1 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Memory / context | Python | Apache-2.0 | 65,976 (▲219) | Classic | 84 | very active | 0d ago | 3.3y | 28 |
| [upstash/context7](https://github.com/upstash/context7) | MCP ecosystem | TypeScript | MIT | 62,414 (▲148) | Hot | 79 | very active | 1d ago | 1.5y | 10 |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Local runtime | Python | NOASSERTION | 59,598 (▲290) | Classic | 79 | very active | 0d ago | 3.2y | 10 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Memory / context | Python | MIT | 59,268 (▲76) | Hot | 81 | very active | 0d ago | 5mo | 22 |
| [aaif-goose/goose](https://github.com/aaif-goose/goose) | Harness / coding agent | Rust | Apache-2.0 | 54,634 (▲108) | Mature | 99 | very active | 0d ago | 2.1y | 37 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Config / setup kit | Python | NOASSERTION | 54,587 (▲208) | Mature | 60 | very active | 0d ago | 1.4y | 1 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Config / setup kit | Jupyter Notebook | MIT | 52,974 (▲113) | Classic | 61 | very active | 1d ago | 3.1y | 11 |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | Code-graph / retrieval | TypeScript | NOASSERTION | 47,564 (▲82) | Hot | 83 | very active | 0d ago | 1.1y | 26 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Skills framework | Python | MIT | 46,617 (▲745) | Hot | 80 | very active | 4d ago | 11mo | 17 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Code-graph / retrieval | C | MIT | 44,864 (▲919) | Hot | 75 | very active | 1d ago | 7mo | 10 |
| [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | Config / setup kit | Python | MIT | 41,659 (▲48) | Rising | 68 | very active | 5d ago | 10mo | 3 |
| [wshobson/agents](https://github.com/wshobson/agents) | Skills framework | Python | MIT | 39,933 (▲86) | Hot | 66 | very active | 4d ago | 1.2y | 17 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Harness / coding agent | TypeScript | MIT | 39,348 (▲63) | Hot | 85 | very active | 0d ago | 8mo | 10 |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Observability / evals | TypeScript | NOASSERTION | 35,033 (▲150) | Classic | 89 | very active | 0d ago | 3.4y | 21 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Config / setup kit | Python | MIT | 31,758 (▲888) | Hot | 80 | very active | 0d ago | 1.2y | 14 |
| [toon-format/toon](https://github.com/toon-format/toon) | Token-saver / compression | TypeScript | MIT | 25,421 (▲20) | Hot | 78 | very active | 22d ago | 11mo | 4 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Observability / evals | Python | Apache-2.0 | 22,230 (▲51) | Classic | 93 | very active | 0d ago | 3.4y | 22 |
| [memvid/memvid](https://github.com/memvid/memvid) | Memory / context | Rust | Apache-2.0 | 16,554 (▲3) | Declining | 55 | slowing | 2mo ago | 1.3y | 1 |
| [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | Config / setup kit | JavaScript | MIT | 12,764 (▲37) | Rising | 77 | very active | 0d ago | 10mo | 2 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Observability / evals | Python | NOASSERTION | 11,609 (▲48) | Classic | 79 | very active | 0d ago | 3.9y | 17 |
| [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | Token-saver / compression | TypeScript | MIT | 11,228 (▲91) | Hot | 79 | very active | 0d ago | 5mo | 11 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Observability / evals | Python | Apache-2.0 | 7,447 (▲6) | Classic | 70 | active | 1d ago | 3.1y | 7 |
| [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram) | Memory / context | Go | MIT | 6,822 (▲85) | Hot | 79 | very active | 0d ago | 7mo | 10 |
| [MinishLab/semble](https://github.com/MinishLab/semble) | Token-saver / compression | Python | MIT | 6,142 (▲25) | Hot | 73 | very active | 0d ago | 5mo | 5 |
| [campfirein/byterover-cli](https://github.com/campfirein/byterover-cli) | Memory / context | TypeScript | NOASSERTION | 4,964 (▼1) | Declining | 46 | slowing | 3mo ago | 1.3y | 0 |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | Memory / context | JavaScript | Apache-2.0 | 3,696 (▲5) | Declining | 47 | slowing | 2mo ago | 1.2y | 0 |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | Config / setup kit | Python | MIT | 2,644 (▲5) | Mature | 50 | active | 0d ago | 1.2y | 1 |
| [patoles/agent-flow](https://github.com/patoles/agent-flow) | Observability / evals | TypeScript | Apache-2.0 | 1,656 (▲3) | Mature | 46 | slowing | 2mo ago | 6mo | 2 |
| [ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht) | Observability / evals | Go | MIT | 100 (▲1) | Hot | 80 | very active | 1d ago | 1.1y | 5 |

## By layer

### Harness / coding agent

_The loop that reads, plans, edits, and runs. Pick one as your daily driver; keep a second installed to diff behavior and model-shop._

- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · 390,467★ · TypeScript · Hot  
  Cross-platform personal-assistant harness — an 'any OS, any platform' agent runtime.  
  <sub>topics: ai, assistant, own-your-data, personal, crustacean, molty, openclaw</sub>
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 248,814★ · Python · Hot  
  Long-lived 'agent that grows with you' harness — persistent, personalized agent loop.  
  <sub>topics: ai, ai-agent, ai-agents, llm, anthropic, chatgpt, claude, claude-code</sub>
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 209,940★ · TypeScript · Hot  
  Open-source terminal coding agent — a provider-agnostic alternative harness.  
  <sub>topics: —</sub>
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 148,017★ · TypeScript · Hot  
  Claude Code itself — the agentic CLI that lives in your terminal; the baseline every setup here extends.  
  <sub>topics: —</sub>
- **[openai/codex](https://github.com/openai/codex)** · 126,387★ · Rust · Hot  
  OpenAI's lightweight terminal coding agent — useful as a second harness to diff behavior against Claude Code.  
  <sub>topics: —</sub>
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 109,259★ · TypeScript · Hot  
  Unified LLM-API + agent-loop + TUI toolkit — a kit for rolling your own coding agent.  
  <sub>topics: —</sub>
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 107,159★ · TypeScript · Hot  
  Gemini's open-source terminal agent — the third major CLI harness; handy for model-shopping.  
  <sub>topics: gemini, gemini-api, ai, ai-agents, cli, mcp-client, mcp-server</sub>
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 82,962★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and writes — multi-step autonomy.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 73,238★ · TypeScript · Hot  
  Agent meta-harness for Claude — deploys multi-agent swarms with coordination.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server</sub>
- **[cline/cline](https://github.com/cline/cline)** · 69,273★ · TypeScript · Mature  
  Autonomous coding agent as SDK / IDE extension / CLI — strong for in-editor agentic workflows.  
  <sub>topics: —</sub>
- **[aaif-goose/goose](https://github.com/aaif-goose/goose)** · 54,634★ · Rust · Mature  
  Extensible open agent that installs and runs tools, not just suggestions — MCP-native.  
  <sub>topics: mcp, acp, ai, ai-agents</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 39,348★ · TypeScript · Hot  
  Teams-first multi-agent orchestration layer for Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>

### Skills framework

_The biggest 2026 upgrade. Skills load only when triggered, so they add capability without taxing every session — the opposite of a big always-on CLAUDE.md._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 291,377★ · Shell · Hot  
  Agentic skills framework + dev methodology — the headline 'give your agent superpowers' skill collection.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 267,158★ · JavaScript · Hot  
  Agent-harness performance system bundling skills, instincts, and memory into one optimization layer.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[anthropics/skills](https://github.com/anthropics/skills)** · 178,045★ · Python · Mature  
  Anthropic's official Agent Skills repo — canonical examples of the skills format.  
  <sub>topics: agent-skills</sub>
- **[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** · 75,611★ · Python · Declining  
  Curated index of Claude Skills + tooling — the discovery hub for what's worth installing.  
  <sub>topics: claude, claude-code, agent-skills, ai-agents, antigravity, automation, codex, composio</sub>
- **[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)** · 46,617★ · Python · Hot  
  Domain skill pack that turns an agent into a research scientist — example of vertical skills.  
  <sub>topics: ai-scientist, bioinformatics, chemoinformatics, claude, claude-skills, claudecode, clinical-research, computational-biology</sub>
- **[wshobson/agents](https://github.com/wshobson/agents)** · 39,933★ · Python · Hot  
  Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor) — subagents & commands.  
  <sub>topics: anthropic, agent-skills, agentic-ai, ai-agents, cursor, cursor-rules, mcp, multi-agent</sub>

### Config / setup kit

_Turnkey CLAUDE.md / command / hook bundles. Steal a good one, then trim to what you actually use — bloat here is paid on every prompt._

- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 215,056★ · — · Declining  
  A single CLAUDE.md derived from Karpathy's habits — the 'one good config file' approach.  
  <sub>topics: —</sub>
- **[x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)** · 143,855★ · — · Mature  
  Leaked/collected system prompts of major AI coding tools — prompt-engineering reference.  
  <sub>topics: ai, cursor, lovable, system-prompts, v0, cursorai, devin, replit</sub>
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 136,676★ · Rust · Hot  
  Desktop all-in-one for managing Claude Code/Codex/OpenClaw — swap providers & configs fast.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, codex, mcp</sub>
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 134,161★ · TypeScript · Hot  
  Garry Tan's exact Claude Code setup — 23 opinionated tools as a turnkey starting point.  
  <sub>topics: —</sub>
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 66,321★ · HTML · Rising  
  Best-practices collection: vibe-coding → agentic engineering.  
  <sub>topics: claude-ai, claude-code, best-practices, claude, claude-code-best-practices, agentic-engineering, anthropic, claude-code-agents</sub>
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 54,587★ · Python · Mature  
  The awesome-list for Claude Code skills, hooks, slash-commands, and orchestrators.  
  <sub>topics: anthropic, anthropic-claude, awesome, awesome-list, awesome-lists, awesome-resources, claude, claude-code</sub>
- **[anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)** · 52,974★ · Jupyter Notebook · Classic  
  Official recipes/notebooks for effective Claude usage patterns.  
  <sub>topics: —</sub>
- **[luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)** · 41,659★ · Python · Rising  
  Visual, example-driven guide to Claude Code from basics to advanced — the learning path.  
  <sub>topics: claude-code, guide, tutorial</sub>
- **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** · 31,758★ · Python · Hot  
  CLI to configure AND monitor Claude Code — installs commands/agents/hooks and watches usage.  
  <sub>topics: anthropic, anthropic-claude, claude, claude-code</sub>
- **[Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts)** · 12,764★ · JavaScript · Rising  
  Claude Code's full system prompt + 27 builtin tool descriptions — know what you're configuring.  
  <sub>topics: claude-code, claude-code-system-prompts, system-prompts</sub>
- **[centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup)** · 2,644★ · Python · Mature  
  A shared starter CLAUDE.md + memory-bank configuration template you can fork.  
  <sub>topics: claude, claude-ai, claude-code, subagents, claudecode-config, claudecode-hooks, claudecode-subagents</sub>

### Memory / context

_Persist decisions and context across sessions so the agent doesn't re-derive what it already learned. The backend is swappable._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 94,658★ · TypeScript · Hot  
  Persistent context across sessions for every agent — captures work and re-injects it (you run this).  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude, claude-agent-sdk, claude-agents</sub>
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 65,976★ · Python · Classic  
  Universal memory layer for AI agents — the most-adopted general memory backend.  
  <sub>topics: ai, chatgpt, llm, python, rag, long-term-memory, memory, memory-management</sub>
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 59,268★ · Python · Hot  
  Best-benchmarked open-source AI memory system — drop-in long-term memory.  
  <sub>topics: ai, chromadb, llm, mcp, memory, python</sub>
- **[memvid/memvid](https://github.com/memvid/memvid)** · 16,554★ · Rust · Declining  
  Memory layer that replaces RAG pipelines with a compact server — novel storage approach.  
  <sub>topics: ai, context, embedded, faiss, knowledge-base, knowledge-graph, llm, machine-learning</sub>
- **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** · 6,822★ · Go · Hot  
  Agent-agnostic Go binary giving coding agents persistent memory.  
  <sub>topics: —</sub>
- **[campfirein/byterover-cli](https://github.com/campfirein/byterover-cli)** · 4,964★ · TypeScript · Declining  
  Portable memory layer (brv) for autonomous coding agents — agent-agnostic.  
  <sub>topics: agent, llm, mcp, memory, vibe-coding, ai, autonomous-agents, cli</sub>
- **[memodb-io/Acontext](https://github.com/memodb-io/Acontext)** · 3,696★ · JavaScript · Declining  
  Treats Agent Skills as a memory layer — skills-as-memory hybrid.  
  <sub>topics: agent, context-engineering, data-platform, self-learning, agent-development-kit, ai-agent, llm, memory</sub>

### Token-saver / compression

_Measure first (`codeburn`), then compress: leaner code search, output trimming, and a front proxy stack to 60–90% on common loops._

- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 107,770★ · Go · Hot  
  'Why use many token when few token do trick' — a Claude Code skill that aggressively trims tokens.  
  <sub>topics: ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering</sub>
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 81,687★ · Rust · Hot  
  CLI proxy that cuts LLM token consumption 60–90% on common dev commands — sits in front of the agent.  
  <sub>topics: agentic-coding, ai-coding, anthropic, claude-code, cli, command-line-tool, cost-reduction, developer-tools</sub>
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 73,757★ · Python · Hot  
  Compresses tool outputs, logs, files, and RAG chunks before they hit the model's context.  
  <sub>topics: agent, ai, anthropic, compression, context-engineering, context-window, fastapi, langchain</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 69,395★ · TypeScript · Hot  
  omo/lazycodex — a coding agent built for 'tokenmaxxers'; efficiency-first harness.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[toon-format/toon](https://github.com/toon-format/toon)** · 25,421★ · TypeScript · Hot  
  Token-Oriented Object Notation — compact schema-aware encoding to shrink structured payloads.  
  <sub>topics: data-format, llm, serialization, tokenization</sub>
- **[getagentseal/codeburn](https://github.com/getagentseal/codeburn)** · 11,228★ · TypeScript · Hot  
  TUI dashboard showing where your AI coding tokens go — measure before you optimize.  
  <sub>topics: ai-coding, claude-code, cli, codex, cost-tracking, developer-tools, observability, terminal-ui</sub>
- **[MinishLab/semble](https://github.com/MinishLab/semble)** · 6,142★ · Python · Hot  
  Fast, accurate code search for agents using ~98% fewer tokens than reading files.  
  <sub>topics: agents, code-search, embeddings, mcp, mcp-server, model-context-protocol, retrieval</sub>

### Code-graph / retrieval

_Give the agent structure instead of raw files — graphs and indexes answer 'how does X relate to Y' without scanning the repo._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 121,287★ · Python · Hot  
  Coding-assistant skill that turns a repo into a knowledge graph (you use this on this project).  
  <sub>topics: claude-code, graphrag, knowledge-graph, codex, openclaw, skills, antigravity, gemini</sub>
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 84,129★ · TypeScript · Hot  
  Turns any code into an interactive teaching graph — comprehension over impression.  
  <sub>topics: claude-code, claude-skills, understandcode, codex, codex-skills, knowledge-graph, opencode-skills, antigravity-skills</sub>
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 72,059★ · C · Hot  
  Pre-indexed code knowledge graph for Claude Code/Codex/Cursor — structural retrieval.  
  <sub>topics: —</sub>
- **[abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)** · 47,564★ · TypeScript · Hot  
  Zero-server code-intelligence engine — client-side code graph.  
  <sub>topics: —</sub>
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 44,864★ · C · Hot  
  High-performance code-intelligence MCP server — indexes codebases for retrieval.  
  <sub>topics: claude-code, code-analysis, code-intelligence, developer-tools, knowledge-graph, mcp, mcp-server, model-context-protocol</sub>

### MCP ecosystem

_External capabilities via a standard protocol. Each connected server costs context, so connect deliberately — `context7` (live docs) is the highest-ROI default._

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 95,504★ · — · Hot  
  The big community index of MCP servers — discovery for what to connect.  
  <sub>topics: ai, mcp</sub>
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 90,584★ · TypeScript · Hot  
  The official reference MCP servers — the canonical catalog of capabilities to plug in.  
  <sub>topics: —</sub>
- **[upstash/context7](https://github.com/upstash/context7)** · 62,414★ · TypeScript · Hot  
  Up-to-date library docs for LLMs via MCP — kills 'hallucinated API' errors (you have this wired).  
  <sub>topics: llm, mcp, mcp-server, vibe-coding</sub>

### Observability / evals

_You can't optimize what you can't see. Trace runs, watch spend, and score outputs before trusting an autonomous setup._

- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 35,033★ · TypeScript · Classic  
  Open-source LLM engineering platform: traces, evals, metrics, prompts (you trace Claude Code into this).  
  <sub>topics: analytics, llm, llmops, large-language-models, openai, self-hosted, ycombinator, monitoring</sub>
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 22,230★ · Python · Classic  
  Debug/evaluate/monitor LLM apps, RAG, and agents — eval-first observability.  
  <sub>topics: open-source, langchain, openai, playground, prompt-engineering, llama-index, llm, llm-evaluation</sub>
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 11,609★ · Python · Classic  
  AI observability & evaluation — OpenTelemetry-based tracing for agents.  
  <sub>topics: llmops, ai-monitoring, ai-observability, llm-eval, aiengineering, datasets, agents, llms</sub>
- **[traceloop/openllmetry](https://github.com/traceloop/openllmetry)** · 7,447★ · Python · Classic  
  Open-source OpenTelemetry-based observability for LLM apps — standards-based traces.  
  <sub>topics: llmops, observability, open-telemetry, metrics, monitoring, opentelemetry, datascience, ml</sub>
- **[patoles/agent-flow](https://github.com/patoles/agent-flow)** · 1,656★ · TypeScript · Mature  
  Real-time visualization of Claude Code agent orchestration — watch agents think, branch, coordinate.  
  <sub>topics: agent-visualization, ai-agents, claude-code, developer-tools, llm, vscode-extension</sub>
- **[ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht)** · 100★ · Go · Hot  
  Claude Code session lights in the macOS menu bar — at-a-glance session state.  
  <sub>topics: —</sub>

### Local runtime

_Run open models locally or proxy many models behind one endpoint — the cost floor for grunt work and the fallback when the cloud is down._

- **[ollama/ollama](https://github.com/ollama/ollama)** · 181,673★ · Go · Classic  
  Run open models locally with one command — point an agent at it to slash API cost or go offline.  
  <sub>topics: llama, llm, llms, go, golang, ollama, mistral, gemma</sub>
- **[BerriAI/litellm](https://github.com/BerriAI/litellm)** · 59,598★ · Python · Classic  
  OpenAI-compatible proxy/gateway to 100+ LLMs — swap models under any harness from one endpoint.  
  <sub>topics: anthropic, langchain, llm, llmops, openai, ai-gateway, azure-openai, bedrock</sub>

## Graph analysis — how they relate

**Community clustering.** These 59 tools span **20 of the graph's 35 communities** — the Claude-Code ecosystem is spread across agent-framework, memory, retrieval, and observability neighborhoods rather than forming one tidy cluster.

- **Community 6** (9): `aaif-goose/goose`, `NousResearch/hermes-agent`, `obra/superpowers`, `x1xhlol/system-prompts-and-models-of-ai-tools`, `thedotmack/claude-mem`, `mem0ai/mem0`, `MemPalace/mempalace`, `memodb-io/Acontext`, `headroomlabs-ai/headroom`
- **Community 4** (8): `anthropics/claude-code`, `anthropics/skills`, `centminmod/my-claude-code-setup`, `davila7/claude-code-templates`, `luongnv89/claude-howto`, `shanraisshan/claude-code-best-practice`, `Piebald-AI/claude-code-system-prompts`, `anthropics/claude-cookbooks`
- **Community 24** (7): `affaan-m/ECC`, `ComposioHQ/awesome-claude-skills`, `wshobson/agents`, `rtk-ai/rtk`, `Graphify-Labs/graphify`, `DeusData/codebase-memory-mcp`, `patoles/agent-flow`
- **Community 9** (5): `google-gemini/gemini-cli`, `MinishLab/semble`, `modelcontextprotocol/servers`, `punkpeye/awesome-mcp-servers`, `upstash/context7`
- **Community 14** (5): `farion1231/cc-switch`, `hesreallyhim/awesome-claude-code`, `JuliusBrussee/caveman`, `code-yeongyu/oh-my-openagent`, `traceloop/openllmetry`
- **Community 1** (4): `ruvnet/ruflo`, `getagentseal/codeburn`, `Egonex-AI/Understand-Anything`, `BerriAI/litellm`
- **Community 26** (3): `openclaw/openclaw`, `garrytan/gstack`, `campfirein/byterover-cli`
- **Community 13** (3): `Gentleman-Programming/engram`, `abhigyanpatwari/GitNexus`, `ingo-eichhorst/Irrlicht`
- **Community 21** (3): `langfuse/langfuse`, `comet-ml/opik`, `Arize-ai/phoenix`
- **Community 3** (2): `cline/cline`, `earendil-works/pi`

**Centrality (PageRank in the full 2,243-repo graph)** — the most 'hub-like' setup tools in your ecosystem:

- `hesreallyhim/awesome-claude-code` — PageRank 0.0036
- `multica-ai/andrej-karpathy-skills` — PageRank 0.0012
- `shanraisshan/claude-code-best-practice` — PageRank 0.0012
- `affaan-m/ECC` — PageRank 0.0011
- `code-yeongyu/oh-my-openagent` — PageRank 0.0011
- `MemPalace/mempalace` — PageRank 0.0010
- `davila7/claude-code-templates` — PageRank 0.0009
- `comet-ml/opik` — PageRank 0.0009
- `punkpeye/awesome-mcp-servers` — PageRank 0.0008
- `NousResearch/hermes-agent` — PageRank 0.0007

**Direct links between these tools** (top similarity edges where both endpoints are in this report):

- `hesreallyhim/awesome-claude-code` ⇄ `code-yeongyu/oh-my-openagent` (w=0.729) — topics: anthropic, claude; authors: github-actions[bot]
- `anthropics/claude-cookbooks` ⇄ `anthropics/skills` (w=0.633) — authors: cj-ant
- `langfuse/langfuse` ⇄ `comet-ml/opik` (w=0.524) — topics: llm, llmops, openai, open-source
- `aaif-goose/goose` ⇄ `punkpeye/awesome-mcp-servers` (w=0.500) — topics: mcp, ai
- `JuliusBrussee/caveman` ⇄ `davila7/claude-code-templates` (w=0.439) — topics: anthropic, claude, claude-code; authors: claude, github-actions[bot]
- `hesreallyhim/awesome-claude-code` ⇄ `davila7/claude-code-templates` (w=0.403) — topics: anthropic, anthropic-claude, claude, claude-code; authors: github-actions[bot]
- `patoles/agent-flow` ⇄ `affaan-m/ECC` (w=0.400) — topics: ai-agents, claude-code, developer-tools, llm
- `hesreallyhim/awesome-claude-code` ⇄ `traceloop/openllmetry` (w=0.363) — topics: llm; authors: github-actions[bot]
- `wshobson/agents` ⇄ `ComposioHQ/awesome-claude-skills` (w=0.326) — topics: agent-skills, ai-agents, cursor, mcp
- `rtk-ai/rtk` ⇄ `affaan-m/ECC` (w=0.313) — topics: anthropic, claude-code, developer-tools, llm
- `headroomlabs-ai/headroom` ⇄ `MemPalace/mempalace` (w=0.302) — topics: ai, llm, mcp, python; authors: dependabot[bot], sxh313
- `DeusData/codebase-memory-mcp` ⇄ `Graphify-Labs/graphify` (w=0.300) — topics: claude-code, code-analysis, developer-tools, knowledge-graph
- `Graphify-Labs/graphify` ⇄ `ComposioHQ/awesome-claude-skills` (w=0.291) — topics: claude-code, codex, antigravity, ai-agents
- `getagentseal/codeburn` ⇄ `rtk-ai/rtk` (w=0.281) — topics: ai-coding, claude-code, cli, developer-tools; authors: iliaal
- `davila7/claude-code-templates` ⇄ `centminmod/my-claude-code-setup` (w=0.272) — topics: claude, claude-code
- …and 7 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). This ecosystem moves fast and a lot of it is one-person projects — check before wiring one into your daily loop.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| aaif-goose/goose | 99 | Mature | very active | 5 | 14% | 153 |
| headroomlabs-ai/headroom | 98 | Hot | very active | 5 | 22% | 170 |
| google-gemini/gemini-cli | 95 | Hot | very active | 4 | 19% | 639 |
| openai/codex | 94 | Hot | very active | 7 | 16% | 1144 |
| comet-ml/opik | 93 | Classic | very active | 4 | 21% | 597 |
| modelcontextprotocol/servers | 90 | Hot | very active | 4 | 19% | 28 |
| langfuse/langfuse | 89 | Classic | very active | 3 | 23% | 700 |
| bytedance/deer-flow | 87 | Hot | very active | 12 | 6% | 2 |
| Yeachan-Heo/oh-my-claudecode | 85 | Hot | very active | 2 | 43% | 252 |
| openclaw/openclaw | 84 | Hot | very active | 2 | 42% | 247 |
| mem0ai/mem0 | 84 | Classic | very active | 2 | 48% | 414 |
| anomalyco/opencode | 83 | Hot | very active | 2 | 33% | 874 |
| abhigyanpatwari/GitNexus | 83 | Hot | very active | 2 | 46% | 898 |
| ollama/ollama | 83 | Classic | very active | 2 | 32% | 256 |
| farion1231/cc-switch | 81 | Hot | very active | 2 | 42% | 55 |
| MemPalace/mempalace | 81 | Hot | very active | 2 | 47% | 18 |
| Graphify-Labs/graphify | 81 | Hot | very active | 2 | 38% | 213 |
| NousResearch/hermes-agent | 80 | Hot | very active | 2 | 31% | 36 |
| earendil-works/pi | 80 | Hot | very active | 1 | 54% | 263 |
| K-Dense-AI/scientific-agent-skills | 80 | Hot | very active | 1 | 70% | 106 |
| davila7/claude-code-templates | 80 | Hot | very active | 2 | 37% | 21 |
| thedotmack/claude-mem | 80 | Hot | very active | 1 | 78% | 345 |
| ingo-eichhorst/Irrlicht | 80 | Hot | very active | 1 | 90% | 45 |
| anthropics/claude-code | 79 | Hot | very active | 1 | 80% | 227 |
| affaan-m/ECC | 79 | Hot | very active | 1 | 54% | 17 |
| Gentleman-Programming/engram | 79 | Hot | very active | 1 | 78% | 112 |
| getagentseal/codeburn | 79 | Hot | very active | 1 | 62% | 71 |
| upstash/context7 | 79 | Hot | very active | 1 | 57% | 127 |
| Arize-ai/phoenix | 79 | Classic | very active | 1 | 57% | 845 |
| BerriAI/litellm | 79 | Classic | very active | 1 | 80% | 1477 |
| cline/cline | 78 | Mature | very active | 1 | 50% | 431 |
| JuliusBrussee/caveman | 78 | Hot | very active | 1 | 58% | 35 |
| code-yeongyu/oh-my-openagent | 78 | Hot | very active | 1 | 98% | 307 |
| toon-format/toon | 78 | Hot | very active | 1 | 97% | 31 |
| Piebald-AI/claude-code-system-prompts | 77 | Rising | very active | 1 | 99% | 247 |
| colbymchenry/codegraph | 77 | Hot | very active | 1 | 93% | 31 |
| ruvnet/ruflo | 76 | Hot | very active | 1 | 87% | 1654 |
| obra/superpowers | 75 | Hot | very active | 1 | 79% | 13 |
| rtk-ai/rtk | 75 | Hot | very active | 1 | 73% | 357 |
| DeusData/codebase-memory-mcp | 75 | Hot | very active | 1 | 84% | 47 |
| Egonex-AI/Understand-Anything | 74 | Hot | very active | 1 | 80% | 8 |
| MinishLab/semble | 73 | Hot | very active | 1 | 69% | 29 |
| traceloop/openllmetry | 70 | Classic | active | 2 | 33% | 262 |
| luongnv89/claude-howto | 68 | Rising | very active | 1 | 87% | 10 |
| wshobson/agents | 66 | Hot | very active | 2 | 47% | 0 |
| shanraisshan/claude-code-best-practice | 64 | Rising | very active | 1 | 100% | 0 |
| anthropics/claude-cookbooks | 61 | Classic | very active | 2 | 35% | 0 |
| hesreallyhim/awesome-claude-code | 60 | Mature | very active | 1 | 100% | 0 |
| punkpeye/awesome-mcp-servers | 60 | Hot | very active | 1 | 58% | 0 |
| garrytan/gstack | 58 | Hot | very active | 1 | 60% | 0 |
| memvid/memvid | 55 | Declining | slowing | 1 | 100% | 12 |
| anthropics/skills | 50 | Mature | active | 2 | 33% | 0 |
| centminmod/my-claude-code-setup | 50 | Mature | active | 1 | 100% | 0 |
| x1xhlol/system-prompts-and-models-of-ai-tools | 47 | Mature | active | 1 | 65% | 0 |
| memodb-io/Acontext | 47 | Declining | slowing | 0 | 0% | 279 |
| campfirein/byterover-cli | 46 | Declining | slowing | 0 | 0% | 27 |
| patoles/agent-flow | 46 | Mature | slowing | 1 | 71% | 3 |
| ComposioHQ/awesome-claude-skills | 38 | Declining | active | 1 | 100% | 0 |
| multica-ai/andrej-karpathy-skills | 22 | Declining | slowing | 0 | 0% | 0 |

## Adjacent (deliberately not listed here)

- **n8n-io/n8n** (205,912★) — workflow-automation platform — orchestrates agents but isn't a Claude-Code setup layer
- **langgenius/dify** (157,170★) — agentic-workflow platform — covered by the agent-orchestration report
- **langchain-ai/langchain** (147,034★) — agent-engineering library — app framework, not a CC setup tool
- **open-webui/open-webui** (153,123★) — chat UI for local models — a frontend, not an agent setup
- **ultraworkers/claw-code** (195,282★) — art/exhibit harness — not a practical setup layer
- **multica-ai/multica** (51,323★) — managed-agents platform — team product, see agent-orchestration report

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (claude-code / skill / agent harness / mcp / memory / token / observability / code-graph / setup) across name+description+topics, then manual curation into the nine setup layers. General agent *application* frameworks, chat UIs, and broad platforms were routed to adjacent reports or excluded (see above).
- **The three-strategy table is opinionated**, built only from repos in your stars — it is a starting point, not a benchmark. Validate model-tier and token-saver claims against your own `langfuse`/`codeburn` traces.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.

<sub>Tools covered: 59 · Snapshot: 2026-09-25T10:37:19.717Z</sub>
