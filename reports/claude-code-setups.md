# Claude Code Superpowers — Setup Strategies from Your Stars

> Derived from **kaiser-data**'s 2,304 starred repos (snapshot `2026-10-05T13:01:39.533Z`), cross-referenced with the repo-similarity graph (2,304 nodes / 7,632 edges, 40 communities).
>
> Generated 2026-10-05 by `scripts/reports/claude_code_setups.py` (regenerate any time — no API cost).

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

- **58 Claude-Code 'superpower' projects** in your stars (**5,063,673★** combined), spanning 9 setup layers:
  - **Harness / coding agent** (12): `openclaw`, `hermes-agent`, `opencode`, `claude-code`, `codex`, `pi`, `gemini-cli`, `deer-flow`, `ruflo`, `cline`, `goose`, `oh-my-claudecode`
  - **Skills framework** (6): `superpowers`, `ECC`, `skills`, `awesome-claude-skills`, `scientific-agent-skills`, `agents`
  - **Config / setup kit** (11): `andrej-karpathy-skills`, `system-prompts-and-models-of-ai-tools`, `cc-switch`, `gstack`, `claude-code-best-practice`, `awesome-claude-code`, `claude-cookbooks`, `claude-howto`, `claude-code-templates`, `claude-code-system-prompts`, `my-claude-code-setup`
  - **Memory / context** (6): `claude-mem`, `mem0`, `mempalace`, `memvid`, `engram`, `Acontext`
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
| **Memory / context** | Persist context across sessions | `claude-mem`, `mem0`, `mempalace`, `memvid`, `engram`, `Acontext` |
| **Token-saver / compression** | Shrink what the model has to read | `caveman`, `rtk`, `headroom`, `oh-my-openagent`, `toon`, `codeburn` |
| **Code-graph / retrieval** | Feed the *right* code, not all of it | `graphify`, `Understand-Anything`, `codegraph`, `GitNexus`, `codebase-memory-mcp` |
| **MCP ecosystem** | External reach (docs, tools, data) | `awesome-mcp-servers`, `servers`, `context7` |
| **Observability / evals** | Measure cost & quality | `langfuse`, `opik`, `phoenix`, `openllmetry`, `agent-flow`, `Irrlicht` |
| **Local runtime** | Cut cost / go offline | `ollama`, `litellm` |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Layer | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Harness / coding agent | TypeScript | MIT | 391,416 (▲949) | Hot | 79 | very active | 0d ago | 10mo | 12 |
| [obra/superpowers](https://github.com/obra/superpowers) | Skills framework | Shell | MIT | 295,458 (▲4,081) | Hot | 73 | very active | 8d ago | 12mo | 5 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Skills framework | JavaScript | MIT | 273,296 (▲6,138) | Hot | 79 | very active | 0d ago | 8mo | 5 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Harness / coding agent | Python | MIT | 251,309 (▲2,495) | Hot | 86 | very active | 0d ago | 1.2y | 24 |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Config / setup kit | — | — | 216,967 (▲1,911) | Declining | 21 | slowing | 5mo ago | 8mo | 0 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | Harness / coding agent | TypeScript | MIT | 211,816 (▲1,876) | Hot | 88 | very active | 0d ago | 1.4y | 16 |
| [ollama/ollama](https://github.com/ollama/ollama) | Local runtime | Go | MIT | 182,220 (▲547) | Classic | 83 | very active | 1d ago | 3.3y | 8 |
| [anthropics/skills](https://github.com/anthropics/skills) | Skills framework | Python | — | 179,723 (▲1,678) | Mature | 50 | active | 2d ago | 1.0y | 5 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Harness / coding agent | TypeScript | — | 149,465 (▲1,448) | Hot | 79 | very active | 0d ago | 1.6y | 7 |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Config / setup kit | — | GPL-3.0 | 144,026 (▲171) | Mature | 43 | active | 1mo ago | 1.6y | 1 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Config / setup kit | Rust | MIT | 140,188 (▲3,512) | Hot | 76 | very active | 0d ago | 1.2y | 5 |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Config / setup kit | TypeScript | MIT | 135,288 (▲1,127) | Hot | 61 | very active | 0d ago | 6mo | 5 |
| [openai/codex](https://github.com/openai/codex) | Harness / coding agent | Rust | Apache-2.0 | 127,900 (▲1,513) | Hot | 84 | very active | 0d ago | 1.5y | 30 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Code-graph / retrieval | Python | Apache-2.0 | 123,925 (▲2,638) | Hot | 96 | very active | 1d ago | 6mo | 29 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness / coding agent | TypeScript | MIT | 112,592 (▲3,333) | Hot | 80 | very active | 0d ago | 1.2y | 14 |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Token-saver / compression | Go | Apache-2.0 | 109,914 (▲2,144) | Hot | 79 | very active | 0d ago | 6mo | 8 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Harness / coding agent | TypeScript | Apache-2.0 | 107,232 (▲73) | Hot | 95 | very active | 0d ago | 1.5y | 14 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Memory / context | TypeScript | Apache-2.0 | 96,379 (▲1,721) | Hot | 80 | very active | 0d ago | 1.1y | 13 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP ecosystem | — | MIT | 95,829 (▲325) | Hot | 59 | very active | 8d ago | 1.8y | 31 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | MCP ecosystem | TypeScript | NOASSERTION | 91,012 (▲428) | Hot | 94 | very active | 0d ago | 1.9y | 31 |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | Code-graph / retrieval | TypeScript | MIT | 85,316 (▲1,187) | Hot | 75 | very active | 3d ago | 6mo | 12 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Harness / coding agent | Python | MIT | 83,401 (▲439) | Hot | 87 | very active | 0d ago | 1.4y | 37 |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Token-saver / compression | Rust | Apache-2.0 | 82,410 (▲723) | Hot | 75 | very active | 0d ago | 8mo | 12 |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Skills framework | Python | — | 76,523 (▲912) | Declining | 37 | active | 17d ago | 11mo | 1 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Token-saver / compression | Python | Apache-2.0 | 74,440 (▲683) | Hot | 98 | very active | 0d ago | 9mo | 46 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Harness / coding agent | TypeScript | MIT | 73,892 (▲654) | Mature | 76 | very active | 0d ago | 1.3y | 1 |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | Code-graph / retrieval | C | MIT | 73,238 (▲1,179) | Rising | 78 | very active | 2d ago | 8mo | 2 |
| [cline/cline](https://github.com/cline/cline) | Harness / coding agent | TypeScript | Apache-2.0 | 69,871 (▲598) | Mature | 83 | very active | 0d ago | 2.2y | 11 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Token-saver / compression | TypeScript | NOASSERTION | 69,807 (▲412) | Hot | 78 | very active | 0d ago | 10mo | 6 |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Config / setup kit | HTML | MIT | 67,107 (▲786) | Rising | 64 | very active | 0d ago | 11mo | 1 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Memory / context | Python | Apache-2.0 | 66,590 (▲614) | Classic | 83 | very active | 0d ago | 3.3y | 28 |
| [upstash/context7](https://github.com/upstash/context7) | MCP ecosystem | TypeScript | MIT | 62,701 (▲287) | Hot | 79 | very active | 0d ago | 1.5y | 8 |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Local runtime | Python | NOASSERTION | 60,147 (▲549) | Classic | 79 | very active | 0d ago | 3.2y | 12 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Memory / context | Python | MIT | 59,413 (▲145) | Hot | 81 | very active | 2d ago | 6mo | 22 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Config / setup kit | Python | NOASSERTION | 55,088 (▲501) | Mature | 60 | very active | 0d ago | 1.5y | 1 |
| [aaif-goose/goose](https://github.com/aaif-goose/goose) | Harness / coding agent | Rust | Apache-2.0 | 54,950 (▲316) | Mature | 99 | very active | 0d ago | 2.1y | 42 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Config / setup kit | Jupyter Notebook | MIT | 53,205 (▲231) | Classic | 60 | very active | 7d ago | 3.1y | 9 |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | Code-graph / retrieval | TypeScript | NOASSERTION | 47,729 (▲165) | Hot | 83 | very active | 0d ago | 1.2y | 20 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Skills framework | Python | MIT | 47,651 (▲1,034) | Hot | 80 | very active | 0d ago | 11mo | 17 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Code-graph / retrieval | C | MIT | 45,803 (▲939) | Rising | 76 | very active | 0d ago | 7mo | 1 |
| [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | Config / setup kit | Python | MIT | 41,748 (▲89) | Rising | 68 | very active | 5d ago | 11mo | 2 |
| [wshobson/agents](https://github.com/wshobson/agents) | Skills framework | Python | MIT | 40,208 (▲275) | Hot | 63 | very active | 0d ago | 1.2y | 21 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Harness / coding agent | TypeScript | MIT | 39,585 (▲237) | Hot | 85 | very active | 0d ago | 8mo | 7 |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Observability / evals | TypeScript | NOASSERTION | 35,396 (▲363) | Classic | 94 | very active | 0d ago | 3.4y | 21 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Config / setup kit | Python | MIT | 32,384 (▲626) | Hot | 75 | very active | 0d ago | 1.3y | 5 |
| [toon-format/toon](https://github.com/toon-format/toon) | Token-saver / compression | TypeScript | MIT | 25,453 (▲32) | Hot | 80 | very active | 0d ago | 11mo | 5 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Observability / evals | Python | Apache-2.0 | 22,385 (▲155) | Classic | 94 | very active | 0d ago | 3.4y | 24 |
| [memvid/memvid](https://github.com/memvid/memvid) | Memory / context | Rust | Apache-2.0 | 16,573 (▲19) | Declining | 54 | slowing | 2mo ago | 1.4y | 1 |
| [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | Config / setup kit | JavaScript | MIT | 12,832 (▲68) | Rising | 77 | very active | 2d ago | 10mo | 2 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Observability / evals | Python | NOASSERTION | 11,713 (▲104) | Classic | 83 | very active | 1d ago | 3.9y | 21 |
| [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | Token-saver / compression | TypeScript | MIT | 11,341 (▲113) | Hot | 84 | very active | 0d ago | 5mo | 14 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Observability / evals | Python | Apache-2.0 | 7,469 (▲22) | Classic | 70 | active | 1d ago | 3.1y | 8 |
| [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram) | Memory / context | Go | MIT | 7,041 (▲219) | Hot | 79 | very active | 1d ago | 7mo | 8 |
| [MinishLab/semble](https://github.com/MinishLab/semble) | Token-saver / compression | Python | MIT | 6,184 (▲42) | Hot | 73 | very active | 0d ago | 6mo | 5 |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | Memory / context | JavaScript | Apache-2.0 | 3,697 (▲1) | Declining | 46 | slowing | 2mo ago | 1.2y | 0 |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | Config / setup kit | Python | MIT | 2,653 (▲9) | Mature | 49 | active | 8d ago | 1.2y | 1 |
| [patoles/agent-flow](https://github.com/patoles/agent-flow) | Observability / evals | TypeScript | Apache-2.0 | 1,674 (▲18) | Mature | 44 | slowing | 2mo ago | 6mo | 2 |
| [ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht) | Observability / evals | Go | MIT | 100 | Hot | 80 | very active | 1d ago | 1.1y | 4 |

## By layer

### Harness / coding agent

_The loop that reads, plans, edits, and runs. Pick one as your daily driver; keep a second installed to diff behavior and model-shop._

- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · 391,416★ · TypeScript · Hot  
  Cross-platform personal-assistant harness — an 'any OS, any platform' agent runtime.  
  <sub>topics: ai, assistant, own-your-data, personal, crustacean, molty, openclaw</sub>
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 251,309★ · Python · Hot  
  Long-lived 'agent that grows with you' harness — persistent, personalized agent loop.  
  <sub>topics: ai, ai-agent, ai-agents, llm, anthropic, chatgpt, claude, claude-code</sub>
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 211,816★ · TypeScript · Hot  
  Open-source terminal coding agent — a provider-agnostic alternative harness.  
  <sub>topics: —</sub>
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 149,465★ · TypeScript · Hot  
  Claude Code itself — the agentic CLI that lives in your terminal; the baseline every setup here extends.  
  <sub>topics: —</sub>
- **[openai/codex](https://github.com/openai/codex)** · 127,900★ · Rust · Hot  
  OpenAI's lightweight terminal coding agent — useful as a second harness to diff behavior against Claude Code.  
  <sub>topics: —</sub>
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 112,592★ · TypeScript · Hot  
  Unified LLM-API + agent-loop + TUI toolkit — a kit for rolling your own coding agent.  
  <sub>topics: —</sub>
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 107,232★ · TypeScript · Hot  
  Gemini's open-source terminal agent — the third major CLI harness; handy for model-shopping.  
  <sub>topics: gemini, gemini-api, ai, ai-agents, cli, mcp-client, mcp-server</sub>
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 83,401★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and writes — multi-step autonomy.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 73,892★ · TypeScript · Mature  
  Agent meta-harness for Claude — deploys multi-agent swarms with coordination.  
  <sub>topics: swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server, multi-agent</sub>
- **[cline/cline](https://github.com/cline/cline)** · 69,871★ · TypeScript · Mature  
  Autonomous coding agent as SDK / IDE extension / CLI — strong for in-editor agentic workflows.  
  <sub>topics: —</sub>
- **[aaif-goose/goose](https://github.com/aaif-goose/goose)** · 54,950★ · Rust · Mature  
  Extensible open agent that installs and runs tools, not just suggestions — MCP-native.  
  <sub>topics: mcp, acp, ai, ai-agents</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 39,585★ · TypeScript · Hot  
  Teams-first multi-agent orchestration layer for Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>

### Skills framework

_The biggest 2026 upgrade. Skills load only when triggered, so they add capability without taxing every session — the opposite of a big always-on CLAUDE.md._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 295,458★ · Shell · Hot  
  Agentic skills framework + dev methodology — the headline 'give your agent superpowers' skill collection.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 273,296★ · JavaScript · Hot  
  Agent-harness performance system bundling skills, instincts, and memory into one optimization layer.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[anthropics/skills](https://github.com/anthropics/skills)** · 179,723★ · Python · Mature  
  Anthropic's official Agent Skills repo — canonical examples of the skills format.  
  <sub>topics: agent-skills</sub>
- **[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** · 76,523★ · Python · Declining  
  Curated index of Claude Skills + tooling — the discovery hub for what's worth installing.  
  <sub>topics: claude, claude-code, agent-skills, ai-agents, antigravity, automation, codex, composio</sub>
- **[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)** · 47,651★ · Python · Hot  
  Domain skill pack that turns an agent into a research scientist — example of vertical skills.  
  <sub>topics: ai-scientist, bioinformatics, chemoinformatics, claude, claude-skills, claudecode, clinical-research, computational-biology</sub>
- **[wshobson/agents](https://github.com/wshobson/agents)** · 40,208★ · Python · Hot  
  Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor) — subagents & commands.  
  <sub>topics: anthropic, agent-skills, agentic-ai, ai-agents, cursor, cursor-rules, mcp, multi-agent</sub>

### Config / setup kit

_Turnkey CLAUDE.md / command / hook bundles. Steal a good one, then trim to what you actually use — bloat here is paid on every prompt._

- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 216,967★ · — · Declining  
  A single CLAUDE.md derived from Karpathy's habits — the 'one good config file' approach.  
  <sub>topics: —</sub>
- **[x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)** · 144,026★ · — · Mature  
  Leaked/collected system prompts of major AI coding tools — prompt-engineering reference.  
  <sub>topics: ai, cursor, lovable, system-prompts, v0, cursorai, devin, replit</sub>
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 140,188★ · Rust · Hot  
  Desktop all-in-one for managing Claude Code/Codex/OpenClaw — swap providers & configs fast.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, codex, mcp</sub>
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 135,288★ · TypeScript · Hot  
  Garry Tan's exact Claude Code setup — 23 opinionated tools as a turnkey starting point.  
  <sub>topics: —</sub>
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 67,107★ · HTML · Rising  
  Best-practices collection: vibe-coding → agentic engineering.  
  <sub>topics: claude-ai, claude-code, best-practices, claude, claude-code-best-practices, agentic-engineering, anthropic, claude-code-agents</sub>
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 55,088★ · Python · Mature  
  The awesome-list for Claude Code skills, hooks, slash-commands, and orchestrators.  
  <sub>topics: anthropic, anthropic-claude, awesome, awesome-list, awesome-lists, awesome-resources, claude, claude-code</sub>
- **[anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)** · 53,205★ · Jupyter Notebook · Classic  
  Official recipes/notebooks for effective Claude usage patterns.  
  <sub>topics: —</sub>
- **[luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)** · 41,748★ · Python · Rising  
  Visual, example-driven guide to Claude Code from basics to advanced — the learning path.  
  <sub>topics: claude-code, guide, tutorial</sub>
- **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** · 32,384★ · Python · Hot  
  CLI to configure AND monitor Claude Code — installs commands/agents/hooks and watches usage.  
  <sub>topics: anthropic, anthropic-claude, claude, claude-code</sub>
- **[Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts)** · 12,832★ · JavaScript · Rising  
  Claude Code's full system prompt + 27 builtin tool descriptions — know what you're configuring.  
  <sub>topics: claude-code, claude-code-system-prompts, system-prompts</sub>
- **[centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup)** · 2,653★ · Python · Mature  
  A shared starter CLAUDE.md + memory-bank configuration template you can fork.  
  <sub>topics: claude, claude-ai, claude-code, subagents, claudecode-config, claudecode-hooks, claudecode-subagents</sub>

### Memory / context

_Persist decisions and context across sessions so the agent doesn't re-derive what it already learned. The backend is swappable._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 96,379★ · TypeScript · Hot  
  Persistent context across sessions for every agent — captures work and re-injects it (you run this).  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude, claude-agent-sdk, claude-agents</sub>
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 66,590★ · Python · Classic  
  Universal memory layer for AI agents — the most-adopted general memory backend.  
  <sub>topics: ai, chatgpt, llm, python, rag, long-term-memory, memory, memory-management</sub>
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 59,413★ · Python · Hot  
  Best-benchmarked open-source AI memory system — drop-in long-term memory.  
  <sub>topics: ai, chromadb, llm, mcp, memory, python</sub>
- **[memvid/memvid](https://github.com/memvid/memvid)** · 16,573★ · Rust · Declining  
  Memory layer that replaces RAG pipelines with a compact server — novel storage approach.  
  <sub>topics: ai, context, embedded, faiss, knowledge-base, knowledge-graph, llm, machine-learning</sub>
- **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** · 7,041★ · Go · Hot  
  Agent-agnostic Go binary giving coding agents persistent memory.  
  <sub>topics: —</sub>
- **[memodb-io/Acontext](https://github.com/memodb-io/Acontext)** · 3,697★ · JavaScript · Declining  
  Treats Agent Skills as a memory layer — skills-as-memory hybrid.  
  <sub>topics: agent, context-engineering, data-platform, self-learning, agent-development-kit, ai-agent, llm, memory</sub>

### Token-saver / compression

_Measure first (`codeburn`), then compress: leaner code search, output trimming, and a front proxy stack to 60–90% on common loops._

- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 109,914★ · Go · Hot  
  'Why use many token when few token do trick' — a Claude Code skill that aggressively trims tokens.  
  <sub>topics: ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering</sub>
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 82,410★ · Rust · Hot  
  CLI proxy that cuts LLM token consumption 60–90% on common dev commands — sits in front of the agent.  
  <sub>topics: agentic-coding, ai-coding, anthropic, claude-code, cli, command-line-tool, cost-reduction, developer-tools</sub>
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 74,440★ · Python · Hot  
  Compresses tool outputs, logs, files, and RAG chunks before they hit the model's context.  
  <sub>topics: agent, ai, anthropic, compression, context-engineering, context-window, fastapi, langchain</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 69,807★ · TypeScript · Hot  
  omo/lazycodex — a coding agent built for 'tokenmaxxers'; efficiency-first harness.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[toon-format/toon](https://github.com/toon-format/toon)** · 25,453★ · TypeScript · Hot  
  Token-Oriented Object Notation — compact schema-aware encoding to shrink structured payloads.  
  <sub>topics: data-format, llm, serialization, tokenization</sub>
- **[getagentseal/codeburn](https://github.com/getagentseal/codeburn)** · 11,341★ · TypeScript · Hot  
  TUI dashboard showing where your AI coding tokens go — measure before you optimize.  
  <sub>topics: ai-coding, claude-code, cli, codex, cost-tracking, developer-tools, observability, terminal-ui</sub>
- **[MinishLab/semble](https://github.com/MinishLab/semble)** · 6,184★ · Python · Hot  
  Fast, accurate code search for agents using ~98% fewer tokens than reading files.  
  <sub>topics: agents, code-search, embeddings, mcp, mcp-server, model-context-protocol, retrieval</sub>

### Code-graph / retrieval

_Give the agent structure instead of raw files — graphs and indexes answer 'how does X relate to Y' without scanning the repo._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 123,925★ · Python · Hot  
  Coding-assistant skill that turns a repo into a knowledge graph (you use this on this project).  
  <sub>topics: claude-code, graphrag, knowledge-graph, codex, openclaw, skills, antigravity, gemini</sub>
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 85,316★ · TypeScript · Hot  
  Turns any code into an interactive teaching graph — comprehension over impression.  
  <sub>topics: claude-code, claude-skills, understandcode, codex, codex-skills, knowledge-graph, opencode-skills, antigravity-skills</sub>
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 73,238★ · C · Rising  
  Pre-indexed code knowledge graph for Claude Code/Codex/Cursor — structural retrieval.  
  <sub>topics: —</sub>
- **[abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)** · 47,729★ · TypeScript · Hot  
  Zero-server code-intelligence engine — client-side code graph.  
  <sub>topics: —</sub>
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 45,803★ · C · Rising  
  High-performance code-intelligence MCP server — indexes codebases for retrieval.  
  <sub>topics: claude-code, code-analysis, code-intelligence, developer-tools, knowledge-graph, mcp, mcp-server, model-context-protocol</sub>

### MCP ecosystem

_External capabilities via a standard protocol. Each connected server costs context, so connect deliberately — `context7` (live docs) is the highest-ROI default._

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 95,829★ · — · Hot  
  The big community index of MCP servers — discovery for what to connect.  
  <sub>topics: ai, mcp</sub>
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 91,012★ · TypeScript · Hot  
  The official reference MCP servers — the canonical catalog of capabilities to plug in.  
  <sub>topics: —</sub>
- **[upstash/context7](https://github.com/upstash/context7)** · 62,701★ · TypeScript · Hot  
  Up-to-date library docs for LLMs via MCP — kills 'hallucinated API' errors (you have this wired).  
  <sub>topics: llm, mcp, mcp-server, vibe-coding</sub>

### Observability / evals

_You can't optimize what you can't see. Trace runs, watch spend, and score outputs before trusting an autonomous setup._

- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 35,396★ · TypeScript · Classic  
  Open-source LLM engineering platform: traces, evals, metrics, prompts (you trace Claude Code into this).  
  <sub>topics: analytics, llm, llmops, large-language-models, openai, self-hosted, ycombinator, monitoring</sub>
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 22,385★ · Python · Classic  
  Debug/evaluate/monitor LLM apps, RAG, and agents — eval-first observability.  
  <sub>topics: open-source, langchain, openai, playground, prompt-engineering, llama-index, llm, llm-evaluation</sub>
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 11,713★ · Python · Classic  
  AI observability & evaluation — OpenTelemetry-based tracing for agents.  
  <sub>topics: llmops, ai-monitoring, ai-observability, llm-eval, aiengineering, datasets, agents, llms</sub>
- **[traceloop/openllmetry](https://github.com/traceloop/openllmetry)** · 7,469★ · Python · Classic  
  Open-source OpenTelemetry-based observability for LLM apps — standards-based traces.  
  <sub>topics: llmops, observability, open-telemetry, metrics, monitoring, opentelemetry, datascience, ml</sub>
- **[patoles/agent-flow](https://github.com/patoles/agent-flow)** · 1,674★ · TypeScript · Mature  
  Real-time visualization of Claude Code agent orchestration — watch agents think, branch, coordinate.  
  <sub>topics: agent-visualization, ai-agents, claude-code, developer-tools, llm, vscode-extension</sub>
- **[ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht)** · 100★ · Go · Hot  
  Claude Code session lights in the macOS menu bar — at-a-glance session state.  
  <sub>topics: —</sub>

### Local runtime

_Run open models locally or proxy many models behind one endpoint — the cost floor for grunt work and the fallback when the cloud is down._

- **[ollama/ollama](https://github.com/ollama/ollama)** · 182,220★ · Go · Classic  
  Run open models locally with one command — point an agent at it to slash API cost or go offline.  
  <sub>topics: llama, llm, llms, go, golang, ollama, mistral, gemma</sub>
- **[BerriAI/litellm](https://github.com/BerriAI/litellm)** · 60,147★ · Python · Classic  
  OpenAI-compatible proxy/gateway to 100+ LLMs — swap models under any harness from one endpoint.  
  <sub>topics: anthropic, langchain, llm, llmops, openai, ai-gateway, azure-openai, bedrock</sub>

## Graph analysis — how they relate

**Community clustering.** These 58 tools span **14 of the graph's 40 communities** — the Claude-Code ecosystem is spread across agent-framework, memory, retrieval, and observability neighborhoods rather than forming one tidy cluster.

- **Community 0** (11): `NousResearch/hermes-agent`, `affaan-m/ECC`, `thedotmack/claude-mem`, `mem0ai/mem0`, `MemPalace/mempalace`, `memvid/memvid`, `Gentleman-Programming/engram`, `memodb-io/Acontext`, `toon-format/toon`, `headroomlabs-ai/headroom`, `patoles/agent-flow`
- **Community 6** (8): `multica-ai/andrej-karpathy-skills`, `centminmod/my-claude-code-setup`, `davila7/claude-code-templates`, `farion1231/cc-switch`, `JuliusBrussee/caveman`, `rtk-ai/rtk`, `Graphify-Labs/graphify`, `DeusData/codebase-memory-mcp`
- **Community 21** (7): `anomalyco/opencode`, `google-gemini/gemini-cli`, `aaif-goose/goose`, `MinishLab/semble`, `modelcontextprotocol/servers`, `punkpeye/awesome-mcp-servers`, `upstash/context7`
- **Community 5** (7): `ruvnet/ruflo`, `ComposioHQ/awesome-claude-skills`, `wshobson/agents`, `K-Dense-AI/scientific-agent-skills`, `x1xhlol/system-prompts-and-models-of-ai-tools`, `code-yeongyu/oh-my-openagent`, `Egonex-AI/Understand-Anything`
- **Community 26** (6): `anthropics/claude-code`, `anthropics/skills`, `luongnv89/claude-howto`, `shanraisshan/claude-code-best-practice`, `Piebald-AI/claude-code-system-prompts`, `anthropics/claude-cookbooks`
- **Community 13** (4): `earendil-works/pi`, `hesreallyhim/awesome-claude-code`, `colbymchenry/codegraph`, `traceloop/openllmetry`
- **Community 17** (4): `langfuse/langfuse`, `comet-ml/opik`, `Arize-ai/phoenix`, `BerriAI/litellm`
- **Community 7** (3): `getagentseal/codeburn`, `abhigyanpatwari/GitNexus`, `ingo-eichhorst/Irrlicht`
- **Community 12** (2): `openclaw/openclaw`, `garrytan/gstack`
- **Community 4** (2): `cline/cline`, `obra/superpowers`

**Centrality (PageRank in the full 2,304-repo graph)** — the most 'hub-like' setup tools in your ecosystem:

- `hesreallyhim/awesome-claude-code` — PageRank 0.0029
- `multica-ai/andrej-karpathy-skills` — PageRank 0.0012
- `davila7/claude-code-templates` — PageRank 0.0011
- `affaan-m/ECC` — PageRank 0.0011
- `shanraisshan/claude-code-best-practice` — PageRank 0.0009
- `MemPalace/mempalace` — PageRank 0.0009
- `comet-ml/opik` — PageRank 0.0008
- `code-yeongyu/oh-my-openagent` — PageRank 0.0008
- `punkpeye/awesome-mcp-servers` — PageRank 0.0008
- `JuliusBrussee/caveman` — PageRank 0.0006

**Direct links between these tools** (top similarity edges where both endpoints are in this report):

- `colbymchenry/codegraph` ⇄ `hesreallyhim/awesome-claude-code` (w=1.000) — authors: github-actions[bot]
- `hesreallyhim/awesome-claude-code` ⇄ `davila7/claude-code-templates` (w=0.661) — topics: anthropic, anthropic-claude, claude, claude-code; authors: github-actions[bot]
- `anthropics/claude-cookbooks` ⇄ `anthropics/skills` (w=0.654) — authors: cj-ant
- `JuliusBrussee/caveman` ⇄ `davila7/claude-code-templates` (w=0.636) — topics: anthropic, claude, claude-code; authors: claude, github-actions[bot]
- `langfuse/langfuse` ⇄ `comet-ml/opik` (w=0.569) — topics: llm, llmops, openai, open-source; authors: dependabot[bot]
- `aaif-goose/goose` ⇄ `punkpeye/awesome-mcp-servers` (w=0.500) — topics: mcp, ai
- `patoles/agent-flow` ⇄ `affaan-m/ECC` (w=0.400) — topics: ai-agents, claude-code, developer-tools, llm
- `hesreallyhim/awesome-claude-code` ⇄ `traceloop/openllmetry` (w=0.328) — topics: llm; authors: github-actions[bot]
- `wshobson/agents` ⇄ `ComposioHQ/awesome-claude-skills` (w=0.326) — topics: agent-skills, ai-agents, cursor, mcp
- `DeusData/codebase-memory-mcp` ⇄ `Graphify-Labs/graphify` (w=0.290) — topics: claude-code, code-analysis, developer-tools, knowledge-graph
- `davila7/claude-code-templates` ⇄ `centminmod/my-claude-code-setup` (w=0.272) — topics: claude, claude-code
- `Arize-ai/phoenix` ⇄ `comet-ml/opik` (w=0.258) — topics: llmops, prompt-engineering, llm-evaluation, openai
- `hesreallyhim/awesome-claude-code` ⇄ `K-Dense-AI/scientific-agent-skills` (w=0.226) — topics: claude, agent-skills; authors: github-actions[bot]
- `luongnv89/claude-howto` ⇄ `davila7/claude-code-templates` (w=0.217) — topics: claude-code
- `BerriAI/litellm` ⇄ `comet-ml/opik` (w=0.210) — topics: langchain, llm, llmops, openai
- …and 1 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). This ecosystem moves fast and a lot of it is one-person projects — check before wiring one into your daily loop.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| aaif-goose/goose | 99 | Mature | very active | 7 | 10% | 154 |
| headroomlabs-ai/headroom | 98 | Hot | very active | 6 | 17% | 172 |
| Graphify-Labs/graphify | 96 | Hot | very active | 5 | 19% | 222 |
| google-gemini/gemini-cli | 95 | Hot | very active | 4 | 19% | 649 |
| modelcontextprotocol/servers | 94 | Hot | very active | 5 | 18% | 28 |
| langfuse/langfuse | 94 | Classic | very active | 4 | 16% | 705 |
| comet-ml/opik | 94 | Classic | very active | 4 | 14% | 606 |
| anomalyco/opencode | 88 | Hot | very active | 3 | 26% | 876 |
| bytedance/deer-flow | 87 | Hot | very active | 8 | 14% | 2 |
| NousResearch/hermes-agent | 86 | Hot | very active | 3 | 38% | 36 |
| Yeachan-Heo/oh-my-claudecode | 85 | Hot | very active | 2 | 48% | 254 |
| openai/codex | 84 | Hot | very active | 3 | 29% | 1204 |
| getagentseal/codeburn | 84 | Hot | very active | 2 | 45% | 71 |
| cline/cline | 83 | Mature | very active | 2 | 44% | 446 |
| mem0ai/mem0 | 83 | Classic | very active | 2 | 45% | 416 |
| abhigyanpatwari/GitNexus | 83 | Hot | very active | 2 | 35% | 941 |
| Arize-ai/phoenix | 83 | Classic | very active | 2 | 41% | 855 |
| ollama/ollama | 83 | Classic | very active | 2 | 28% | 258 |
| MemPalace/mempalace | 81 | Hot | very active | 2 | 47% | 18 |
| earendil-works/pi | 80 | Hot | very active | 1 | 51% | 270 |
| K-Dense-AI/scientific-agent-skills | 80 | Hot | very active | 1 | 70% | 109 |
| thedotmack/claude-mem | 80 | Hot | very active | 1 | 70% | 354 |
| toon-format/toon | 80 | Hot | very active | 1 | 96% | 31 |
| ingo-eichhorst/Irrlicht | 80 | Hot | very active | 1 | 91% | 46 |
| anthropics/claude-code | 79 | Hot | very active | 1 | 65% | 234 |
| openclaw/openclaw | 79 | Hot | very active | 1 | 84% | 252 |
| affaan-m/ECC | 79 | Hot | very active | 1 | 93% | 19 |
| Gentleman-Programming/engram | 79 | Hot | very active | 1 | 78% | 115 |
| JuliusBrussee/caveman | 79 | Hot | very active | 1 | 55% | 44 |
| upstash/context7 | 79 | Hot | very active | 1 | 53% | 128 |
| BerriAI/litellm | 79 | Classic | very active | 1 | 66% | 1491 |
| code-yeongyu/oh-my-openagent | 78 | Hot | very active | 1 | 82% | 329 |
| colbymchenry/codegraph | 78 | Rising | very active | 1 | 99% | 33 |
| Piebald-AI/claude-code-system-prompts | 77 | Rising | very active | 1 | 99% | 254 |
| ruvnet/ruflo | 76 | Mature | very active | 1 | 100% | 1664 |
| farion1231/cc-switch | 76 | Hot | very active | 1 | 85% | 57 |
| DeusData/codebase-memory-mcp | 76 | Rising | very active | 1 | 100% | 47 |
| davila7/claude-code-templates | 75 | Hot | very active | 1 | 53% | 21 |
| rtk-ai/rtk | 75 | Hot | very active | 1 | 58% | 390 |
| Egonex-AI/Understand-Anything | 75 | Hot | very active | 1 | 81% | 8 |
| obra/superpowers | 73 | Hot | very active | 1 | 91% | 14 |
| MinishLab/semble | 73 | Hot | very active | 1 | 70% | 30 |
| traceloop/openllmetry | 70 | Classic | active | 2 | 31% | 263 |
| luongnv89/claude-howto | 68 | Rising | very active | 1 | 91% | 10 |
| shanraisshan/claude-code-best-practice | 64 | Rising | very active | 1 | 100% | 0 |
| wshobson/agents | 63 | Hot | very active | 1 | 52% | 0 |
| garrytan/gstack | 61 | Hot | very active | 1 | 68% | 0 |
| hesreallyhim/awesome-claude-code | 60 | Mature | very active | 1 | 100% | 0 |
| anthropics/claude-cookbooks | 60 | Classic | very active | 2 | 37% | 0 |
| punkpeye/awesome-mcp-servers | 59 | Hot | very active | 1 | 59% | 0 |
| memvid/memvid | 54 | Declining | slowing | 1 | 100% | 12 |
| anthropics/skills | 50 | Mature | active | 2 | 36% | 0 |
| centminmod/my-claude-code-setup | 49 | Mature | active | 1 | 100% | 0 |
| memodb-io/Acontext | 46 | Declining | slowing | 0 | 0% | 279 |
| patoles/agent-flow | 44 | Mature | slowing | 1 | 60% | 3 |
| x1xhlol/system-prompts-and-models-of-ai-tools | 43 | Mature | active | 1 | 100% | 0 |
| ComposioHQ/awesome-claude-skills | 37 | Declining | active | 1 | 100% | 0 |
| multica-ai/andrej-karpathy-skills | 21 | Declining | slowing | 0 | 0% | 0 |

## Adjacent (deliberately not listed here)

- **n8n-io/n8n** (206,698★) — workflow-automation platform — orchestrates agents but isn't a Claude-Code setup layer
- **langgenius/dify** (157,871★) — agentic-workflow platform — covered by the agent-orchestration report
- **langchain-ai/langchain** (147,462★) — agent-engineering library — app framework, not a CC setup tool
- **open-webui/open-webui** (153,984★) — chat UI for local models — a frontend, not an agent setup
- **ultraworkers/claw-code** (195,212★) — art/exhibit harness — not a practical setup layer
- **multica-ai/multica** (51,978★) — managed-agents platform — team product, see agent-orchestration report

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (claude-code / skill / agent harness / mcp / memory / token / observability / code-graph / setup) across name+description+topics, then manual curation into the nine setup layers. General agent *application* frameworks, chat UIs, and broad platforms were routed to adjacent reports or excluded (see above).
- **The three-strategy table is opinionated**, built only from repos in your stars — it is a starting point, not a benchmark. Validate model-tier and token-saver claims against your own `langfuse`/`codeburn` traces.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.

<sub>Tools covered: 58 · Snapshot: 2026-10-05T13:01:39.533Z</sub>
