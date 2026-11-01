# Claude Code Superpowers — Setup Strategies from Your Stars

> Derived from **kaiser-data**'s 2,585 starred repos (snapshot `2026-11-01T12:41:55.392Z`), cross-referenced with the repo-similarity graph (2,585 nodes / 8,670 edges, 45 communities).
>
> Generated 2026-11-01 by `scripts/reports/claude_code_setups.py` (regenerate any time — no API cost).

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

- **60 Claude-Code 'superpower' projects** in your stars (**5,381,279★** combined), spanning 9 setup layers:
  - **Harness / coding agent** (13): `openclaw`, `hermes-agent`, `opencode`, `claude-code`, `codex`, `pi`, `gemini-cli`, `deer-flow`, `ruflo`, `learn-claude-code`, `cline`, `goose`, `oh-my-claudecode`
  - **Skills framework** (7): `superpowers`, `ECC`, `skills`, `awesome-claude-skills`, `scientific-agent-skills`, `agents`, `claude-skills`
  - **Config / setup kit** (11): `andrej-karpathy-skills`, `cc-switch`, `system-prompts-and-models-of-ai-tools`, `gstack`, `claude-code-best-practice`, `awesome-claude-code`, `claude-cookbooks`, `claude-howto`, `claude-code-templates`, `claude-code-system-prompts`, `my-claude-code-setup`
  - **Memory / context** (6): `claude-mem`, `mem0`, `mempalace`, `memvid`, `engram`, `basic-memory`
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
| **Config / setup kit** | Shape behavior up front, cheaply | `andrej-karpathy-skills`, `cc-switch`, `system-prompts-and-models-of-ai-tools`, `gstack`, `claude-code-best-practice`, `awesome-claude-code` |
| **Memory / context** | Persist context across sessions | `claude-mem`, `mem0`, `mempalace`, `memvid`, `engram`, `basic-memory` |
| **Token-saver / compression** | Shrink what the model has to read | `caveman`, `rtk`, `headroom`, `oh-my-openagent`, `toon`, `codeburn` |
| **Code-graph / retrieval** | Feed the *right* code, not all of it | `graphify`, `Understand-Anything`, `codegraph`, `GitNexus`, `codebase-memory-mcp` |
| **MCP ecosystem** | External reach (docs, tools, data) | `awesome-mcp-servers`, `servers`, `context7` |
| **Observability / evals** | Measure cost & quality | `langfuse`, `opik`, `phoenix`, `openllmetry`, `agent-flow`, `Irrlicht` |
| **Local runtime** | Cut cost / go offline | `ollama`, `litellm` |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Layer | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Harness / coding agent | TypeScript | MIT | 393,610 (▲495) | Hot | 84 | very active | 0d ago | 11mo | 17 |
| [obra/superpowers](https://github.com/obra/superpowers) | Skills framework | Shell | MIT | 310,340 (▲5,019) | Mature | 64 | active | 3d ago | 1.1y | 1 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Skills framework | JavaScript | MIT | 294,401 (▲5,192) | Hot | 79 | very active | 2d ago | 9mo | 4 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Harness / coding agent | Python | MIT | 259,350 (▲2,124) | Hot | 75 | very active | 0d ago | 1.3y | 7 |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Config / setup kit | — | — | 227,738 (▲3,611) | Declining | 19 | stale | 6mo ago | 9mo | 0 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | Harness / coding agent | TypeScript | MIT | 223,717 (▲1,985) | Hot | 84 | very active | 0d ago | 1.5y | 12 |
| [anthropics/skills](https://github.com/anthropics/skills) | Skills framework | Python | — | 186,105 (▲2,228) | Mature | 50 | active | 4d ago | 1.1y | 5 |
| [ollama/ollama](https://github.com/ollama/ollama) | Local runtime | Go | MIT | 185,540 (▲711) | Classic | 83 | very active | 1d ago | 3.4y | 12 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Harness / coding agent | TypeScript | — | 154,131 (▲711) | Hot | 78 | very active | 1d ago | 1.7y | 9 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Config / setup kit | Rust | MIT | 150,779 (▲1,929) | Hot | 79 | very active | 1d ago | 1.2y | 24 |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Config / setup kit | — | GPL-3.0 | 144,400 (▲135) | Mature | 45 | active | 20d ago | 1.7y | 2 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Code-graph / retrieval | Python | Apache-2.0 | 140,281 (▲4,583) | Hot | 87 | very active | 0d ago | 7mo | 21 |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Config / setup kit | TypeScript | MIT | 138,527 (▲752) | Rising | 68 | very active | 0d ago | 7mo | 1 |
| [openai/codex](https://github.com/openai/codex) | Harness / coding agent | Rust | Apache-2.0 | 132,657 (▲1,675) | Hot | 93 | very active | 2d ago | 1.6y | 38 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness / coding agent | TypeScript | MIT | 119,275 (▲1,355) | Hot | 80 | very active | 0d ago | 1.2y | 9 |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Token-saver / compression | Go | Apache-2.0 | 116,606 (▲1,444) | Hot | 84 | very active | 0d ago | 7mo | 18 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Harness / coding agent | TypeScript | Apache-2.0 | 108,646 (▲248) | Hot | 100 | very active | 0d ago | 1.5y | 16 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Memory / context | TypeScript | Apache-2.0 | 108,499 (▲5,241) | Hot | 90 | very active | 0d ago | 1.2y | 25 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP ecosystem | — | MIT | 97,152 (▲268) | Mature | 59 | very active | 9d ago | 1.9y | 2 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | MCP ecosystem | TypeScript | NOASSERTION | 91,730 (▲155) | Mature | 80 | very active | 3d ago | 2.0y | 2 |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | Code-graph / retrieval | TypeScript | MIT | 89,518 (▲1,177) | Hot | 73 | very active | 6d ago | 7mo | 13 |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Token-saver / compression | Rust | Apache-2.0 | 85,180 (▲585) | Hot | 75 | very active | 0d ago | 9mo | 15 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Harness / coding agent | Python | MIT | 84,817 (▲378) | Hot | 87 | very active | 0d ago | 1.5y | 47 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Harness / coding agent | TypeScript | MIT | 80,472 (▲1,080) | Hot | 77 | very active | 0d ago | 1.4y | 13 |
| [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | Harness / coding agent | Python | MIT | 79,661 (▲412) | Hot | 59 | very active | 5d ago | 1.3y | 23 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Token-saver / compression | Python | Apache-2.0 | 78,507 (▲635) | Hot | 98 | very active | 0d ago | 9mo | 39 |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Skills framework | Python | — | 78,482 (▲508) | Declining | 27 | active | 1mo ago | 1.0y | 0 |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | Code-graph / retrieval | TypeScript | MIT | 76,111 (▲728) | Hot | 78 | very active | 0d ago | 9mo | 8 |
| [cline/cline](https://github.com/cline/cline) | Harness / coding agent | TypeScript | Apache-2.0 | 71,150 (▲286) | Mature | 78 | very active | 1d ago | 2.3y | 14 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Token-saver / compression | TypeScript | NOASSERTION | 70,569 (▲224) | Rising | 77 | very active | 0d ago | 11mo | 1 |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Config / setup kit | HTML | MIT | 68,398 (▲265) | Mature | 64 | very active | 0d ago | 1.0y | 1 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Memory / context | Python | Apache-2.0 | 68,212 (▲373) | Classic | 83 | very active | 2d ago | 3.4y | 29 |
| [upstash/context7](https://github.com/upstash/context7) | MCP ecosystem | TypeScript | MIT | 64,036 (▲329) | Hot | 85 | very active | 0d ago | 1.6y | 12 |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Local runtime | Python | NOASSERTION | 62,484 (▲429) | Classic | 99 | very active | 0d ago | 3.3y | 27 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Memory / context | Python | MIT | 60,213 (▲469) | Hot | 76 | very active | 1d ago | 7mo | 22 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Config / setup kit | Python | NOASSERTION | 57,014 (▲440) | Mature | 61 | very active | 0d ago | 1.5y | 1 |
| [aaif-goose/goose](https://github.com/aaif-goose/goose) | Harness / coding agent | Rust | Apache-2.0 | 56,067 (▲331) | Mature | 99 | very active | 1d ago | 2.2y | 38 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Skills framework | Python | MIT | 55,606 (▲915) | Hot | 77 | very active | 6d ago | 1.0y | 17 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Config / setup kit | Jupyter Notebook | MIT | 54,027 (▲240) | Classic | 59 | very active | 3d ago | 3.2y | 8 |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | Code-graph / retrieval | TypeScript | NOASSERTION | 48,163 (▲119) | Hot | 83 | very active | 0d ago | 1.2y | 14 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Code-graph / retrieval | C | MIT | 47,933 (▲416) | Hot | 76 | very active | 0d ago | 8mo | 4 |
| [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | Config / setup kit | Python | MIT | 46,324 (▲1,139) | Rising | 68 | very active | 4d ago | 11mo | 4 |
| [wshobson/agents](https://github.com/wshobson/agents) | Skills framework | Python | MIT | 42,069 (▲329) | Hot | 63 | very active | 2d ago | 1.3y | 21 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Harness / coding agent | TypeScript | MIT | 40,477 (▲197) | Hot | 80 | very active | 0d ago | 9mo | 7 |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Observability / evals | TypeScript | NOASSERTION | 36,823 (▲311) | Classic | 94 | very active | 0d ago | 3.5y | 19 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Config / setup kit | Python | MIT | 33,028 (▲117) | Hot | 72 | very active | 0d ago | 1.3y | 4 |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | Skills framework | Python | MIT | 29,100 (▲357) | Hot | 80 | very active | 1d ago | 1.0y | 4 |
| [toon-format/toon](https://github.com/toon-format/toon) | Token-saver / compression | TypeScript | MIT | 25,591 (▲28) | Hot | 76 | very active | 0d ago | 1.0y | 3 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Observability / evals | Python | Apache-2.0 | 23,081 (▲149) | Classic | 89 | very active | 0d ago | 3.5y | 24 |
| [memvid/memvid](https://github.com/memvid/memvid) | Memory / context | Rust | Apache-2.0 | 17,329 (▲719) | Declining | 44 | slowing | 3mo ago | 1.4y | 0 |
| [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | Config / setup kit | JavaScript | MIT | 13,056 (▲55) | Rising | 77 | very active | 1d ago | 11mo | 1 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Observability / evals | Python | NOASSERTION | 12,090 (▲83) | Classic | 84 | very active | 0d ago | 4.0y | 17 |
| [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | Token-saver / compression | TypeScript | MIT | 11,635 (▲55) | Hot | 79 | very active | 0d ago | 6mo | 9 |
| [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram) | Memory / context | Go | MIT | 7,723 (▲106) | Hot | 79 | very active | 0d ago | 8mo | 6 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Observability / evals | Python | Apache-2.0 | 7,515 (▲7) | Classic | 72 | very active | 13d ago | 3.2y | 10 |
| [MinishLab/semble](https://github.com/MinishLab/semble) | Token-saver / compression | Python | MIT | 6,340 (▲42) | Hot | 73 | very active | 3d ago | 6mo | 5 |
| [basicmachines-co/basic-memory](https://github.com/basicmachines-co/basic-memory) | Memory / context | Python | AGPL-3.0 | 4,432 (▲75) | Hot | 79 | very active | 0d ago | 1.9y | 4 |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | Config / setup kit | Python | MIT | 2,706 (▲25) | Mature | 46 | active | 24d ago | 1.3y | 1 |
| [patoles/agent-flow](https://github.com/patoles/agent-flow) | Observability / evals | TypeScript | Apache-2.0 | 1,755 (▲13) | Rising | 62 | active | 3d ago | 7mo | 4 |
| [ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht) | Observability / evals | Go | MIT | 101 | Hot | 80 | very active | 0d ago | 1.2y | 4 |

## By layer

### Harness / coding agent

_The loop that reads, plans, edits, and runs. Pick one as your daily driver; keep a second installed to diff behavior and model-shop._

- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · 393,610★ · TypeScript · Hot  
  Cross-platform personal-assistant harness — an 'any OS, any platform' agent runtime.  
  <sub>topics: ai, assistant, own-your-data, personal, crustacean, molty, openclaw</sub>
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 259,350★ · Python · Hot  
  Long-lived 'agent that grows with you' harness — persistent, personalized agent loop.  
  <sub>topics: ai, ai-agent, ai-agents, llm, anthropic, chatgpt, claude, claude-code</sub>
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 223,717★ · TypeScript · Hot  
  Open-source terminal coding agent — a provider-agnostic alternative harness.  
  <sub>topics: —</sub>
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 154,131★ · TypeScript · Hot  
  Claude Code itself — the agentic CLI that lives in your terminal; the baseline every setup here extends.  
  <sub>topics: —</sub>
- **[openai/codex](https://github.com/openai/codex)** · 132,657★ · Rust · Hot  
  OpenAI's lightweight terminal coding agent — useful as a second harness to diff behavior against Claude Code.  
  <sub>topics: —</sub>
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 119,275★ · TypeScript · Hot  
  Unified LLM-API + agent-loop + TUI toolkit — a kit for rolling your own coding agent.  
  <sub>topics: —</sub>
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 108,646★ · TypeScript · Hot  
  Gemini's open-source terminal agent — the third major CLI harness; handy for model-shopping.  
  <sub>topics: gemini, gemini-api, ai, ai-agents, cli, mcp-client, mcp-server</sub>
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 84,817★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and writes — multi-step autonomy.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 80,472★ · TypeScript · Hot  
  Agent meta-harness for Claude — deploys multi-agent swarms with coordination.  
  <sub>topics: swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server, multi-agent</sub>
- **[shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)** · 79,661★ · Python · Hot  
  Builds a nano Claude Code-like harness from zero — the best teaching walkthrough of how the loop works.  
  <sub>topics: agent, claude-code, teaching, agent-development, ai-agent, claude, educational, llm</sub>
- **[cline/cline](https://github.com/cline/cline)** · 71,150★ · TypeScript · Mature  
  Autonomous coding agent as SDK / IDE extension / CLI — strong for in-editor agentic workflows.  
  <sub>topics: —</sub>
- **[aaif-goose/goose](https://github.com/aaif-goose/goose)** · 56,067★ · Rust · Mature  
  Extensible open agent that installs and runs tools, not just suggestions — MCP-native.  
  <sub>topics: mcp, acp, ai, ai-agents</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 40,477★ · TypeScript · Hot  
  Teams-first multi-agent orchestration layer for Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>

### Skills framework

_The biggest 2026 upgrade. Skills load only when triggered, so they add capability without taxing every session — the opposite of a big always-on CLAUDE.md._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 310,340★ · Shell · Mature  
  Agentic skills framework + dev methodology — the headline 'give your agent superpowers' skill collection.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 294,401★ · JavaScript · Hot  
  Agent-harness performance system bundling skills, instincts, and memory into one optimization layer.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[anthropics/skills](https://github.com/anthropics/skills)** · 186,105★ · Python · Mature  
  Anthropic's official Agent Skills repo — canonical examples of the skills format.  
  <sub>topics: agent-skills</sub>
- **[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** · 78,482★ · Python · Declining  
  Curated index of Claude Skills + tooling — the discovery hub for what's worth installing.  
  <sub>topics: claude, claude-code, agent-skills, ai-agents, antigravity, automation, codex, composio</sub>
- **[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)** · 55,606★ · Python · Hot  
  Domain skill pack that turns an agent into a research scientist — example of vertical skills.  
  <sub>topics: ai-scientist, bioinformatics, chemoinformatics, claude, claude-skills, claudecode, clinical-research, computational-biology</sub>
- **[wshobson/agents](https://github.com/wshobson/agents)** · 42,069★ · Python · Hot  
  Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor) — subagents & commands.  
  <sub>topics: anthropic, agent-skills, agentic-ai, ai-agents, cursor, cursor-rules, mcp, multi-agent</sub>
- **[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)** · 29,100★ · Python · Hot  
  Very large skill/agent/command collection (380+ skills) — browse it for patterns, don't install it wholesale.  
  <sub>topics: agentic-ai, anthropic-claude, claude-ai, claude-code, claude-skills, claude-code-skills, ai-coding-agent, claude-code-plugins</sub>

### Config / setup kit

_Turnkey CLAUDE.md / command / hook bundles. Steal a good one, then trim to what you actually use — bloat here is paid on every prompt._

- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 227,738★ · — · Declining  
  A single CLAUDE.md derived from Karpathy's habits — the 'one good config file' approach.  
  <sub>topics: —</sub>
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 150,779★ · Rust · Hot  
  Desktop all-in-one for managing Claude Code/Codex/OpenClaw — swap providers & configs fast.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, codex, mcp</sub>
- **[x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)** · 144,400★ · — · Mature  
  Leaked/collected system prompts of major AI coding tools — prompt-engineering reference.  
  <sub>topics: ai, cursor, lovable, system-prompts, v0, cursorai, devin, replit</sub>
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 138,527★ · TypeScript · Rising  
  Garry Tan's exact Claude Code setup — 23 opinionated tools as a turnkey starting point.  
  <sub>topics: —</sub>
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 68,398★ · HTML · Mature  
  Best-practices collection: vibe-coding → agentic engineering.  
  <sub>topics: claude-ai, claude-code, best-practices, claude, claude-code-best-practices, agentic-engineering, anthropic, claude-code-agents</sub>
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 57,014★ · Python · Mature  
  The awesome-list for Claude Code skills, hooks, slash-commands, and orchestrators.  
  <sub>topics: anthropic, anthropic-claude, awesome, awesome-list, awesome-lists, awesome-resources, claude, claude-code</sub>
- **[anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)** · 54,027★ · Jupyter Notebook · Classic  
  Official recipes/notebooks for effective Claude usage patterns.  
  <sub>topics: —</sub>
- **[luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)** · 46,324★ · Python · Rising  
  Visual, example-driven guide to Claude Code from basics to advanced — the learning path.  
  <sub>topics: claude-code, guide, tutorial</sub>
- **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** · 33,028★ · Python · Hot  
  CLI to configure AND monitor Claude Code — installs commands/agents/hooks and watches usage.  
  <sub>topics: anthropic, anthropic-claude, claude, claude-code</sub>
- **[Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts)** · 13,056★ · JavaScript · Rising  
  Claude Code's full system prompt + 27 builtin tool descriptions — know what you're configuring.  
  <sub>topics: claude-code, claude-code-system-prompts, system-prompts</sub>
- **[centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup)** · 2,706★ · Python · Mature  
  A shared starter CLAUDE.md + memory-bank configuration template you can fork.  
  <sub>topics: claude, claude-ai, claude-code, subagents, claudecode-config, claudecode-hooks, claudecode-subagents</sub>

### Memory / context

_Persist decisions and context across sessions so the agent doesn't re-derive what it already learned. The backend is swappable._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 108,499★ · TypeScript · Hot  
  Persistent context across sessions for every agent — captures work and re-injects it (you run this).  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude, claude-agent-sdk, claude-agents</sub>
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 68,212★ · Python · Classic  
  Universal memory layer for AI agents — the most-adopted general memory backend.  
  <sub>topics: ai, chatgpt, llm, python, rag, long-term-memory, memory, memory-management</sub>
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 60,213★ · Python · Hot  
  Best-benchmarked open-source AI memory system — drop-in long-term memory.  
  <sub>topics: ai, chromadb, llm, mcp, memory, python</sub>
- **[memvid/memvid](https://github.com/memvid/memvid)** · 17,329★ · Rust · Declining  
  Memory layer that replaces RAG pipelines with a compact server — novel storage approach.  
  <sub>topics: ai, context, embedded, faiss, knowledge-base, knowledge-graph, llm, machine-learning</sub>
- **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** · 7,723★ · Go · Hot  
  Agent-agnostic Go binary giving coding agents persistent memory.  
  <sub>topics: —</sub>
- **[basicmachines-co/basic-memory](https://github.com/basicmachines-co/basic-memory)** · 4,432★ · Python · Hot  
  Local Markdown knowledge base exposed over MCP — the agent reads and writes plain notes you can also edit by hand.  
  <sub>topics: ai, claude, llm, mcp, open-source, python, obsidian, obsidian-md</sub>

### Token-saver / compression

_Measure first (`codeburn`), then compress: leaner code search, output trimming, and a front proxy stack to 60–90% on common loops._

- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 116,606★ · Go · Hot  
  'Why use many token when few token do trick' — a Claude Code skill that aggressively trims tokens.  
  <sub>topics: ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering</sub>
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 85,180★ · Rust · Hot  
  CLI proxy that cuts LLM token consumption 60–90% on common dev commands — sits in front of the agent.  
  <sub>topics: agentic-coding, ai-coding, anthropic, claude-code, cli, command-line-tool, cost-reduction, developer-tools</sub>
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 78,507★ · Python · Hot  
  Compresses tool outputs, logs, files, and RAG chunks before they hit the model's context.  
  <sub>topics: agent, ai, anthropic, compression, context-engineering, context-window, fastapi, langchain</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 70,569★ · TypeScript · Rising  
  omo/lazycodex — a coding agent built for 'tokenmaxxers'; efficiency-first harness.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[toon-format/toon](https://github.com/toon-format/toon)** · 25,591★ · TypeScript · Hot  
  Token-Oriented Object Notation — compact schema-aware encoding to shrink structured payloads.  
  <sub>topics: data-format, llm, serialization, tokenization</sub>
- **[getagentseal/codeburn](https://github.com/getagentseal/codeburn)** · 11,635★ · TypeScript · Hot  
  TUI dashboard showing where your AI coding tokens go — measure before you optimize.  
  <sub>topics: ai-coding, claude-code, cli, codex, cost-tracking, developer-tools, observability, terminal-ui</sub>
- **[MinishLab/semble](https://github.com/MinishLab/semble)** · 6,340★ · Python · Hot  
  Fast, accurate code search for agents using ~98% fewer tokens than reading files.  
  <sub>topics: agents, code-search, embeddings, mcp, mcp-server, model-context-protocol, retrieval</sub>

### Code-graph / retrieval

_Give the agent structure instead of raw files — graphs and indexes answer 'how does X relate to Y' without scanning the repo._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 140,281★ · Python · Hot  
  Coding-assistant skill that turns a repo into a knowledge graph (you use this on this project).  
  <sub>topics: claude-code, graphrag, knowledge-graph, codex, openclaw, skills, antigravity, gemini</sub>
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 89,518★ · TypeScript · Hot  
  Turns any code into an interactive teaching graph — comprehension over impression.  
  <sub>topics: claude-code, claude-skills, understandcode, codex, codex-skills, knowledge-graph, opencode-skills, antigravity-skills</sub>
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 76,111★ · TypeScript · Hot  
  Pre-indexed code knowledge graph for Claude Code/Codex/Cursor — structural retrieval.  
  <sub>topics: —</sub>
- **[abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)** · 48,163★ · TypeScript · Hot  
  Zero-server code-intelligence engine — client-side code graph.  
  <sub>topics: —</sub>
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 47,933★ · C · Hot  
  High-performance code-intelligence MCP server — indexes codebases for retrieval.  
  <sub>topics: claude-code, code-analysis, code-intelligence, developer-tools, knowledge-graph, mcp, mcp-server, model-context-protocol</sub>

### MCP ecosystem

_External capabilities via a standard protocol. Each connected server costs context, so connect deliberately — `context7` (live docs) is the highest-ROI default._

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 97,152★ · — · Mature  
  The big community index of MCP servers — discovery for what to connect.  
  <sub>topics: ai, mcp</sub>
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 91,730★ · TypeScript · Mature  
  The official reference MCP servers — the canonical catalog of capabilities to plug in.  
  <sub>topics: —</sub>
- **[upstash/context7](https://github.com/upstash/context7)** · 64,036★ · TypeScript · Hot  
  Up-to-date library docs for LLMs via MCP — kills 'hallucinated API' errors (you have this wired).  
  <sub>topics: llm, mcp, mcp-server, vibe-coding</sub>

### Observability / evals

_You can't optimize what you can't see. Trace runs, watch spend, and score outputs before trusting an autonomous setup._

- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 36,823★ · TypeScript · Classic  
  Open-source LLM engineering platform: traces, evals, metrics, prompts (you trace Claude Code into this).  
  <sub>topics: analytics, llm, llmops, large-language-models, openai, self-hosted, ycombinator, monitoring</sub>
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 23,081★ · Python · Classic  
  Debug/evaluate/monitor LLM apps, RAG, and agents — eval-first observability.  
  <sub>topics: open-source, langchain, openai, playground, prompt-engineering, llama-index, llm, llm-evaluation</sub>
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 12,090★ · Python · Classic  
  AI observability & evaluation — OpenTelemetry-based tracing for agents.  
  <sub>topics: llmops, ai-monitoring, ai-observability, llm-eval, aiengineering, datasets, agents, llms</sub>
- **[traceloop/openllmetry](https://github.com/traceloop/openllmetry)** · 7,515★ · Python · Classic  
  Open-source OpenTelemetry-based observability for LLM apps — standards-based traces.  
  <sub>topics: llmops, observability, open-telemetry, metrics, monitoring, opentelemetry, datascience, ml</sub>
- **[patoles/agent-flow](https://github.com/patoles/agent-flow)** · 1,755★ · TypeScript · Rising  
  Real-time visualization of Claude Code agent orchestration — watch agents think, branch, coordinate.  
  <sub>topics: agent-visualization, ai-agents, claude-code, developer-tools, llm, vscode-extension</sub>
- **[ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht)** · 101★ · Go · Hot  
  Claude Code session lights in the macOS menu bar — at-a-glance session state.  
  <sub>topics: —</sub>

### Local runtime

_Run open models locally or proxy many models behind one endpoint — the cost floor for grunt work and the fallback when the cloud is down._

- **[ollama/ollama](https://github.com/ollama/ollama)** · 185,540★ · Go · Classic  
  Run open models locally with one command — point an agent at it to slash API cost or go offline.  
  <sub>topics: llama, llm, llms, go, golang, ollama, mistral, gemma</sub>
- **[BerriAI/litellm](https://github.com/BerriAI/litellm)** · 62,484★ · Python · Classic  
  OpenAI-compatible proxy/gateway to 100+ LLMs — swap models under any harness from one endpoint.  
  <sub>topics: anthropic, langchain, llm, llmops, openai, ai-gateway, azure-openai, bedrock</sub>

## Graph analysis — how they relate

**Community clustering.** These 60 tools span **21 of the graph's 45 communities** — the Claude-Code ecosystem is spread across agent-framework, memory, retrieval, and observability neighborhoods rather than forming one tidy cluster.

- **Community 4** (9): `aaif-goose/goose`, `NousResearch/hermes-agent`, `shareAI-lab/learn-claude-code`, `mem0ai/mem0`, `MemPalace/mempalace`, `basicmachines-co/basic-memory`, `code-yeongyu/oh-my-openagent`, `toon-format/toon`, `headroomlabs-ai/headroom`
- **Community 11** (8): `anomalyco/opencode`, `K-Dense-AI/scientific-agent-skills`, `centminmod/my-claude-code-setup`, `davila7/claude-code-templates`, `hesreallyhim/awesome-claude-code`, `JuliusBrussee/caveman`, `modelcontextprotocol/servers`, `traceloop/openllmetry`
- **Community 17** (7): `anthropics/claude-code`, `anthropics/skills`, `alirezarezvani/claude-skills`, `luongnv89/claude-howto`, `shanraisshan/claude-code-best-practice`, `Piebald-AI/claude-code-system-prompts`, `anthropics/claude-cookbooks`
- **Community 5** (5): `ruvnet/ruflo`, `Yeachan-Heo/oh-my-claudecode`, `thedotmack/claude-mem`, `Gentleman-Programming/engram`, `getagentseal/codeburn`
- **Community 22** (5): `x1xhlol/system-prompts-and-models-of-ai-tools`, `langfuse/langfuse`, `comet-ml/opik`, `Arize-ai/phoenix`, `BerriAI/litellm`
- **Community 13** (4): `rtk-ai/rtk`, `abhigyanpatwari/GitNexus`, `DeusData/codebase-memory-mcp`, `ingo-eichhorst/Irrlicht`
- **Community 15** (3): `ComposioHQ/awesome-claude-skills`, `wshobson/agents`, `Egonex-AI/Understand-Anything`
- **Community 31** (2): `openclaw/openclaw`, `garrytan/gstack`
- **Community 7** (2): `cline/cline`, `multica-ai/andrej-karpathy-skills`
- **Community 1** (2): `earendil-works/pi`, `punkpeye/awesome-mcp-servers`
- **Community 30** (2): `affaan-m/ECC`, `patoles/agent-flow`
- **Community 16** (2): `MinishLab/semble`, `upstash/context7`

**Centrality (PageRank in the full 2,585-repo graph)** — the most 'hub-like' setup tools in your ecosystem:

- `hesreallyhim/awesome-claude-code` — PageRank 0.0036
- `punkpeye/awesome-mcp-servers` — PageRank 0.0018
- `affaan-m/ECC` — PageRank 0.0014
- `multica-ai/andrej-karpathy-skills` — PageRank 0.0013
- `shanraisshan/claude-code-best-practice` — PageRank 0.0012
- `davila7/claude-code-templates` — PageRank 0.0008
- `MemPalace/mempalace` — PageRank 0.0008
- `NousResearch/hermes-agent` — PageRank 0.0007
- `modelcontextprotocol/servers` — PageRank 0.0007
- `langfuse/langfuse` — PageRank 0.0005

**Direct links between these tools** (top similarity edges where both endpoints are in this report):

- `modelcontextprotocol/servers` ⇄ `hesreallyhim/awesome-claude-code` (w=1.000) — authors: github-actions[bot]
- `hesreallyhim/awesome-claude-code` ⇄ `davila7/claude-code-templates` (w=0.761) — topics: anthropic, anthropic-claude, claude, claude-code; authors: github-actions[bot]
- `anthropics/claude-cookbooks` ⇄ `anthropics/skills` (w=0.667) — authors: cj-ant
- `alirezarezvani/claude-skills` ⇄ `shanraisshan/claude-code-best-practice` (w=0.611) — topics: agentic-ai, claude-ai, claude-code, claude-code-skills; authors: claude
- `langfuse/langfuse` ⇄ `comet-ml/opik` (w=0.524) — topics: llm, llmops, openai, open-source
- `aaif-goose/goose` ⇄ `punkpeye/awesome-mcp-servers` (w=0.500) — topics: mcp, ai
- `rtk-ai/rtk` ⇄ `affaan-m/ECC` (w=0.424) — topics: anthropic, claude-code, developer-tools, llm; authors: dependabot[bot]
- `patoles/agent-flow` ⇄ `affaan-m/ECC` (w=0.400) — topics: ai-agents, claude-code, developer-tools, llm
- `DeusData/codebase-memory-mcp` ⇄ `Graphify-Labs/graphify` (w=0.374) — topics: claude-code, code-analysis, developer-tools, knowledge-graph; authors: divakantpandey
- `JuliusBrussee/caveman` ⇄ `davila7/claude-code-templates` (w=0.368) — topics: anthropic, claude, claude-code; authors: github-actions[bot]
- `NousResearch/hermes-agent` ⇄ `code-yeongyu/oh-my-openagent` (w=0.333) — topics: ai, ai-agents, anthropic, chatgpt
- `wshobson/agents` ⇄ `ComposioHQ/awesome-claude-skills` (w=0.326) — topics: agent-skills, ai-agents, cursor, mcp
- `headroomlabs-ai/headroom` ⇄ `JuliusBrussee/caveman` (w=0.323) — topics: ai, anthropic, llm, claude-code; authors: danieldutu, Yi-111-a
- `Arize-ai/phoenix` ⇄ `comet-ml/opik` (w=0.308) — topics: llmops, prompt-engineering, llm-evaluation, openai; authors: pcbeingused333
- `Arize-ai/phoenix` ⇄ `BerriAI/litellm` (w=0.288) — topics: llmops, anthropic, openai, langchain; authors: pcbeingused333, dependabot[bot]
- …and 12 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). This ecosystem moves fast and a lot of it is one-person projects — check before wiring one into your daily loop.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| google-gemini/gemini-cli | 100 | Hot | very active | 5 | 14% | 680 |
| aaif-goose/goose | 99 | Mature | very active | 5 | 20% | 158 |
| BerriAI/litellm | 99 | Classic | very active | 7 | 10% | 1543 |
| headroomlabs-ai/headroom | 98 | Hot | very active | 5 | 22% | 175 |
| langfuse/langfuse | 94 | Classic | very active | 4 | 22% | 731 |
| openai/codex | 93 | Hot | very active | 8 | 11% | 1257 |
| thedotmack/claude-mem | 90 | Hot | very active | 3 | 35% | 382 |
| comet-ml/opik | 89 | Classic | very active | 3 | 26% | 653 |
| bytedance/deer-flow | 87 | Hot | very active | 10 | 11% | 2 |
| Graphify-Labs/graphify | 87 | Hot | very active | 3 | 23% | 246 |
| upstash/context7 | 85 | Hot | very active | 2 | 39% | 163 |
| openclaw/openclaw | 84 | Hot | very active | 2 | 39% | 277 |
| anomalyco/opencode | 84 | Hot | very active | 2 | 41% | 892 |
| JuliusBrussee/caveman | 84 | Hot | very active | 2 | 35% | 52 |
| Arize-ai/phoenix | 84 | Classic | very active | 2 | 34% | 893 |
| mem0ai/mem0 | 83 | Classic | very active | 2 | 43% | 416 |
| abhigyanpatwari/GitNexus | 83 | Hot | very active | 2 | 47% | 1052 |
| ollama/ollama | 83 | Classic | very active | 2 | 38% | 271 |
| earendil-works/pi | 80 | Hot | very active | 1 | 63% | 275 |
| Yeachan-Heo/oh-my-claudecode | 80 | Hot | very active | 1 | 87% | 282 |
| alirezarezvani/claude-skills | 80 | Hot | very active | 1 | 61% | 13 |
| modelcontextprotocol/servers | 80 | Mature | very active | 1 | 98% | 32 |
| ingo-eichhorst/Irrlicht | 80 | Hot | very active | 1 | 83% | 47 |
| affaan-m/ECC | 79 | Hot | very active | 1 | 96% | 19 |
| farion1231/cc-switch | 79 | Hot | very active | 1 | 61% | 79 |
| Gentleman-Programming/engram | 79 | Hot | very active | 1 | 91% | 127 |
| basicmachines-co/basic-memory | 79 | Hot | very active | 1 | 87% | 93 |
| getagentseal/codeburn | 79 | Hot | very active | 1 | 79% | 80 |
| anthropics/claude-code | 78 | Hot | very active | 1 | 59% | 257 |
| cline/cline | 78 | Mature | very active | 1 | 52% | 468 |
| colbymchenry/codegraph | 78 | Hot | very active | 1 | 78% | 33 |
| ruvnet/ruflo | 77 | Hot | very active | 1 | 56% | 1727 |
| K-Dense-AI/scientific-agent-skills | 77 | Hot | very active | 1 | 67% | 109 |
| Piebald-AI/claude-code-system-prompts | 77 | Rising | very active | 1 | 100% | 278 |
| code-yeongyu/oh-my-openagent | 77 | Rising | very active | 1 | 100% | 356 |
| MemPalace/mempalace | 76 | Hot | very active | 1 | 70% | 19 |
| toon-format/toon | 76 | Hot | very active | 1 | 93% | 32 |
| DeusData/codebase-memory-mcp | 76 | Hot | very active | 1 | 96% | 49 |
| NousResearch/hermes-agent | 75 | Hot | very active | 1 | 51% | 44 |
| rtk-ai/rtk | 75 | Hot | very active | 1 | 53% | 453 |
| MinishLab/semble | 73 | Hot | very active | 1 | 82% | 32 |
| Egonex-AI/Understand-Anything | 73 | Hot | very active | 1 | 86% | 8 |
| davila7/claude-code-templates | 72 | Hot | very active | 1 | 54% | 22 |
| traceloop/openllmetry | 72 | Classic | very active | 2 | 35% | 263 |
| garrytan/gstack | 68 | Rising | very active | 1 | 100% | 2 |
| luongnv89/claude-howto | 68 | Rising | very active | 1 | 84% | 10 |
| obra/superpowers | 64 | Mature | active | 1 | 100% | 16 |
| shanraisshan/claude-code-best-practice | 64 | Mature | very active | 1 | 100% | 0 |
| wshobson/agents | 63 | Hot | very active | 1 | 51% | 0 |
| patoles/agent-flow | 62 | Rising | active | 1 | 70% | 6 |
| hesreallyhim/awesome-claude-code | 61 | Mature | very active | 1 | 100% | 0 |
| shareAI-lab/learn-claude-code | 59 | Hot | very active | 1 | 64% | 0 |
| anthropics/claude-cookbooks | 59 | Classic | very active | 2 | 37% | 0 |
| punkpeye/awesome-mcp-servers | 59 | Mature | very active | 1 | 99% | 0 |
| anthropics/skills | 50 | Mature | active | 2 | 47% | 0 |
| centminmod/my-claude-code-setup | 46 | Mature | active | 1 | 100% | 0 |
| x1xhlol/system-prompts-and-models-of-ai-tools | 45 | Mature | active | 1 | 86% | 0 |
| memvid/memvid | 44 | Declining | slowing | 0 | 0% | 12 |
| ComposioHQ/awesome-claude-skills | 27 | Declining | active | 0 | 0% | 0 |
| multica-ai/andrej-karpathy-skills | 19 | Declining | stale | 0 | 0% | 0 |

## Adjacent (deliberately not listed here)

- **campfirein/byterover-cli** — archived upstream — the portable `brv` memory layer is no longer maintained
- **memodb-io/Acontext** — archived upstream (2026-10) — the skills-as-memory hybrid is no longer maintained
- **n8n-io/n8n** (209,256★) — workflow-automation platform — orchestrates agents but isn't a Claude-Code setup layer
- **langgenius/dify** (160,150★) — agentic-workflow platform — covered by the agent-orchestration report
- **langchain-ai/langchain** (148,809★) — agent-engineering library — app framework, not a CC setup tool
- **open-webui/open-webui** (157,449★) — chat UI for local models — a frontend, not an agent setup
- **ultraworkers/claw-code** (194,992★) — art/exhibit harness — not a practical setup layer
- **multica-ai/multica** (54,489★) — managed-agents platform — team product, see agent-orchestration report

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (claude-code / skill / agent harness / mcp / memory / token / observability / code-graph / setup) across name+description+topics, then manual curation into the nine setup layers. General agent *application* frameworks, chat UIs, and broad platforms were routed to adjacent reports or excluded (see above).
- **The three-strategy table is opinionated**, built only from repos in your stars — it is a starting point, not a benchmark. Validate model-tier and token-saver claims against your own `langfuse`/`codeburn` traces.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.

<sub>Tools covered: 60 · Snapshot: 2026-11-01T12:41:55.392Z</sub>
