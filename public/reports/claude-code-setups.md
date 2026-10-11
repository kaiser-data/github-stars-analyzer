# Claude Code Superpowers — Setup Strategies from Your Stars

> Derived from **kaiser-data**'s 2,346 starred repos (snapshot `2026-10-11T13:10:52.436Z`), cross-referenced with the repo-similarity graph (2,346 nodes / 7,792 edges, 42 communities).
>
> Generated 2026-10-11 by `scripts/reports/claude_code_setups.py` (regenerate any time — no API cost).

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

- **61 Claude-Code 'superpower' projects** in your stars (**5,200,735★** combined), spanning 9 setup layers:
  - **Harness / coding agent** (13): `openclaw`, `hermes-agent`, `opencode`, `claude-code`, `codex`, `pi`, `gemini-cli`, `deer-flow`, `learn-claude-code`, `ruflo`, `cline`, `goose`, `oh-my-claudecode`
  - **Skills framework** (7): `superpowers`, `ECC`, `skills`, `awesome-claude-skills`, `scientific-agent-skills`, `agents`, `claude-skills`
  - **Config / setup kit** (11): `andrej-karpathy-skills`, `system-prompts-and-models-of-ai-tools`, `cc-switch`, `gstack`, `claude-code-best-practice`, `awesome-claude-code`, `claude-cookbooks`, `claude-howto`, `claude-code-templates`, `claude-code-system-prompts`, `my-claude-code-setup`
  - **Memory / context** (7): `claude-mem`, `mem0`, `mempalace`, `memvid`, `engram`, `basic-memory`, `Acontext`
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
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Harness / coding agent | TypeScript | MIT | 391,581 | Hot | 79 | very active | 1d ago | 10mo | 20 |
| [obra/superpowers](https://github.com/obra/superpowers) | Skills framework | Shell | MIT | 297,121 | Hot | 74 | very active | 1d ago | 1.0y | 5 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Skills framework | JavaScript | MIT | 276,293 | Hot | 79 | very active | 1d ago | 8mo | 18 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Harness / coding agent | Python | MIT | 252,453 | Hot | 81 | very active | 1d ago | 1.2y | 26 |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Config / setup kit | — | — | 217,948 | Declining | 20 | slowing | 5mo ago | 8mo | 0 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | Harness / coding agent | TypeScript | MIT | 212,497 | Hot | 88 | very active | 1d ago | 1.4y | 21 |
| [ollama/ollama](https://github.com/ollama/ollama) | Local runtime | Go | MIT | 182,613 | Classic | 83 | very active | 1d ago | 3.3y | 15 |
| [anthropics/skills](https://github.com/anthropics/skills) | Skills framework | Python | — | 180,291 | Mature | 51 | active | 2d ago | 1.1y | 5 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Harness / coding agent | TypeScript | — | 150,006 | Hot | 78 | very active | 2d ago | 1.6y | 8 |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Config / setup kit | — | GPL-3.0 | 143,942 | Mature | 42 | slowing | 2mo ago | 1.6y | 1 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Config / setup kit | Rust | MIT | 142,363 | Hot | 77 | very active | 1d ago | 1.2y | 19 |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Config / setup kit | TypeScript | MIT | 135,801 | Hot | 62 | very active | 2d ago | 7mo | 4 |
| [openai/codex](https://github.com/openai/codex) | Harness / coding agent | Rust | Apache-2.0 | 128,516 | Hot | 93 | very active | 1d ago | 1.5y | 42 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Code-graph / retrieval | Python | Apache-2.0 | 125,191 | Hot | 91 | very active | 1d ago | 6mo | 32 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness / coding agent | TypeScript | MIT | 114,040 | Hot | 85 | very active | 1d ago | 1.2y | 8 |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Token-saver / compression | Go | Apache-2.0 | 110,877 | Rising | 79 | very active | 1d ago | 6mo | 2 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Harness / coding agent | TypeScript | Apache-2.0 | 107,275 | Hot | 95 | very active | 1d ago | 1.5y | 13 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Memory / context | TypeScript | Apache-2.0 | 99,136 | Hot | 85 | very active | 2d ago | 1.1y | 8 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP ecosystem | — | MIT | 96,042 | Hot | 60 | very active | 2d ago | 1.9y | 9 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | MCP ecosystem | TypeScript | NOASSERTION | 91,115 | Hot | 89 | very active | 1d ago | 1.9y | 31 |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | Code-graph / retrieval | TypeScript | MIT | 85,824 | Hot | 75 | very active | 1d ago | 7mo | 12 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Harness / coding agent | Python | MIT | 83,646 | Hot | 87 | very active | 1d ago | 1.4y | 45 |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Token-saver / compression | Rust | Apache-2.0 | 82,837 | Hot | 75 | very active | 2d ago | 8mo | 11 |
| [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | Harness / coding agent | Python | MIT | 78,351 | Hot | 59 | very active | 13d ago | 1.3y | 13 |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Skills framework | Python | — | 76,791 | Declining | 37 | active | 23d ago | 11mo | 1 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Token-saver / compression | Python | Apache-2.0 | 74,886 | Hot | 98 | very active | 1d ago | 9mo | 43 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Harness / coding agent | TypeScript | MIT | 74,252 | Hot | 81 | very active | 1d ago | 1.4y | 5 |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | Code-graph / retrieval | C | MIT | 73,659 | Rising | 78 | very active | 1d ago | 8mo | 2 |
| [cline/cline](https://github.com/cline/cline) | Harness / coding agent | TypeScript | Apache-2.0 | 70,110 | Mature | 83 | very active | 1d ago | 2.3y | 19 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Token-saver / compression | TypeScript | NOASSERTION | 69,937 | Hot | 78 | very active | 1d ago | 10mo | 3 |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Config / setup kit | HTML | MIT | 67,340 | Rising | 64 | very active | 1d ago | 11mo | 1 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Memory / context | Python | Apache-2.0 | 66,942 | Classic | 83 | very active | 2d ago | 3.3y | 30 |
| [upstash/context7](https://github.com/upstash/context7) | MCP ecosystem | TypeScript | MIT | 62,855 | Hot | 85 | very active | 1d ago | 1.5y | 13 |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Local runtime | Python | NOASSERTION | 60,879 | Classic | 84 | very active | 1d ago | 3.2y | 20 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Memory / context | Python | MIT | 59,492 | Hot | 76 | very active | 1d ago | 6mo | 12 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Config / setup kit | Python | NOASSERTION | 55,355 | Mature | 61 | very active | 1d ago | 1.5y | 2 |
| [aaif-goose/goose](https://github.com/aaif-goose/goose) | Harness / coding agent | Rust | Apache-2.0 | 55,129 | Mature | 99 | very active | 2d ago | 2.1y | 36 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Config / setup kit | Jupyter Notebook | MIT | 53,326 | Classic | 60 | very active | 1d ago | 3.2y | 8 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Skills framework | Python | MIT | 48,276 | Hot | 79 | very active | 6d ago | 11mo | 17 |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | Code-graph / retrieval | TypeScript | NOASSERTION | 47,825 | Hot | 83 | very active | 1d ago | 1.2y | 20 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Code-graph / retrieval | C | MIT | 46,283 | Rising | 76 | very active | 1d ago | 7mo | 1 |
| [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | Config / setup kit | Python | MIT | 41,789 | Rising | 67 | very active | 11d ago | 11mo | 2 |
| [wshobson/agents](https://github.com/wshobson/agents) | Skills framework | Python | MIT | 40,321 | Hot | 62 | very active | 7d ago | 1.2y | 17 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Harness / coding agent | TypeScript | MIT | 39,763 | Hot | 80 | very active | 3d ago | 9mo | 6 |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Observability / evals | TypeScript | NOASSERTION | 35,600 | Classic | 94 | very active | 1d ago | 3.4y | 19 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Config / setup kit | Python | MIT | 32,530 | Hot | 75 | very active | 1d ago | 1.3y | 6 |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | Skills framework | Python | MIT | 27,998 | Hot | 73 | active | 1mo ago | 11mo | 4 |
| [toon-format/toon](https://github.com/toon-format/toon) | Token-saver / compression | TypeScript | MIT | 25,481 | Hot | 80 | very active | 2d ago | 11mo | 6 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Observability / evals | Python | Apache-2.0 | 22,487 | Classic | 89 | very active | 1d ago | 3.4y | 18 |
| [memvid/memvid](https://github.com/memvid/memvid) | Memory / context | Rust | Apache-2.0 | 16,585 | Declining | 53 | slowing | 2mo ago | 1.4y | 1 |
| [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | Config / setup kit | JavaScript | MIT | 12,872 | Rising | 77 | very active | 2d ago | 10mo | 1 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Observability / evals | Python | NOASSERTION | 11,774 | Classic | 83 | very active | 1d ago | 3.9y | 22 |
| [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | Token-saver / compression | TypeScript | MIT | 11,373 | Hot | 80 | very active | 1d ago | 6mo | 8 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Observability / evals | Python | Apache-2.0 | 7,481 | Classic | 71 | active | 5d ago | 3.1y | 8 |
| [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram) | Memory / context | Go | MIT | 7,121 | Hot | 79 | very active | 1d ago | 7mo | 10 |
| [MinishLab/semble](https://github.com/MinishLab/semble) | Token-saver / compression | Python | MIT | 6,191 | Hot | 73 | very active | 3d ago | 6mo | 5 |
| [basicmachines-co/basic-memory](https://github.com/basicmachines-co/basic-memory) | Memory / context | Python | AGPL-3.0 | 4,129 | Hot | 79 | very active | 1d ago | 1.9y | 5 |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | Memory / context | JavaScript | Apache-2.0 | 3,693 | Declining | 46 | slowing | 2mo ago | 1.2y | 0 |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | Config / setup kit | Python | MIT | 2,659 | Mature | 48 | active | 3d ago | 1.3y | 1 |
| [patoles/agent-flow](https://github.com/patoles/agent-flow) | Observability / evals | TypeScript | Apache-2.0 | 1,692 | Mature | 55 | active | 1d ago | 6mo | 2 |
| [ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht) | Observability / evals | Go | MIT | 100 | Hot | 80 | very active | 1d ago | 1.1y | 4 |

## By layer

### Harness / coding agent

_The loop that reads, plans, edits, and runs. Pick one as your daily driver; keep a second installed to diff behavior and model-shop._

- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · 391,581★ · TypeScript · Hot  
  Cross-platform personal-assistant harness — an 'any OS, any platform' agent runtime.  
  <sub>topics: ai, assistant, own-your-data, personal, crustacean, molty, openclaw</sub>
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 252,453★ · Python · Hot  
  Long-lived 'agent that grows with you' harness — persistent, personalized agent loop.  
  <sub>topics: ai, ai-agent, ai-agents, llm, anthropic, chatgpt, claude, claude-code</sub>
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 212,497★ · TypeScript · Hot  
  Open-source terminal coding agent — a provider-agnostic alternative harness.  
  <sub>topics: —</sub>
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 150,006★ · TypeScript · Hot  
  Claude Code itself — the agentic CLI that lives in your terminal; the baseline every setup here extends.  
  <sub>topics: —</sub>
- **[openai/codex](https://github.com/openai/codex)** · 128,516★ · Rust · Hot  
  OpenAI's lightweight terminal coding agent — useful as a second harness to diff behavior against Claude Code.  
  <sub>topics: —</sub>
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 114,040★ · TypeScript · Hot  
  Unified LLM-API + agent-loop + TUI toolkit — a kit for rolling your own coding agent.  
  <sub>topics: —</sub>
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 107,275★ · TypeScript · Hot  
  Gemini's open-source terminal agent — the third major CLI harness; handy for model-shopping.  
  <sub>topics: gemini, gemini-api, ai, ai-agents, cli, mcp-client, mcp-server</sub>
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 83,646★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and writes — multi-step autonomy.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)** · 78,351★ · Python · Hot  
  Builds a nano Claude Code-like harness from zero — the best teaching walkthrough of how the loop works.  
  <sub>topics: agent, claude-code, teaching, agent-development, ai-agent, claude, educational, llm</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 74,252★ · TypeScript · Hot  
  Agent meta-harness for Claude — deploys multi-agent swarms with coordination.  
  <sub>topics: swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server, multi-agent</sub>
- **[cline/cline](https://github.com/cline/cline)** · 70,110★ · TypeScript · Mature  
  Autonomous coding agent as SDK / IDE extension / CLI — strong for in-editor agentic workflows.  
  <sub>topics: —</sub>
- **[aaif-goose/goose](https://github.com/aaif-goose/goose)** · 55,129★ · Rust · Mature  
  Extensible open agent that installs and runs tools, not just suggestions — MCP-native.  
  <sub>topics: mcp, acp, ai, ai-agents</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 39,763★ · TypeScript · Hot  
  Teams-first multi-agent orchestration layer for Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>

### Skills framework

_The biggest 2026 upgrade. Skills load only when triggered, so they add capability without taxing every session — the opposite of a big always-on CLAUDE.md._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 297,121★ · Shell · Hot  
  Agentic skills framework + dev methodology — the headline 'give your agent superpowers' skill collection.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 276,293★ · JavaScript · Hot  
  Agent-harness performance system bundling skills, instincts, and memory into one optimization layer.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[anthropics/skills](https://github.com/anthropics/skills)** · 180,291★ · Python · Mature  
  Anthropic's official Agent Skills repo — canonical examples of the skills format.  
  <sub>topics: agent-skills</sub>
- **[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** · 76,791★ · Python · Declining  
  Curated index of Claude Skills + tooling — the discovery hub for what's worth installing.  
  <sub>topics: claude, claude-code, agent-skills, ai-agents, antigravity, automation, codex, composio</sub>
- **[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)** · 48,276★ · Python · Hot  
  Domain skill pack that turns an agent into a research scientist — example of vertical skills.  
  <sub>topics: ai-scientist, bioinformatics, chemoinformatics, claude, claude-skills, claudecode, clinical-research, computational-biology</sub>
- **[wshobson/agents](https://github.com/wshobson/agents)** · 40,321★ · Python · Hot  
  Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor) — subagents & commands.  
  <sub>topics: anthropic, agent-skills, agentic-ai, ai-agents, cursor, cursor-rules, mcp, multi-agent</sub>
- **[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)** · 27,998★ · Python · Hot  
  Very large skill/agent/command collection (380+ skills) — browse it for patterns, don't install it wholesale.  
  <sub>topics: agentic-ai, anthropic-claude, claude-ai, claude-code, claude-skills, claude-code-skills, ai-coding-agent, claude-code-plugins</sub>

### Config / setup kit

_Turnkey CLAUDE.md / command / hook bundles. Steal a good one, then trim to what you actually use — bloat here is paid on every prompt._

- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 217,948★ · — · Declining  
  A single CLAUDE.md derived from Karpathy's habits — the 'one good config file' approach.  
  <sub>topics: —</sub>
- **[x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)** · 143,942★ · — · Mature  
  Leaked/collected system prompts of major AI coding tools — prompt-engineering reference.  
  <sub>topics: ai, cursor, lovable, system-prompts, v0, cursorai, devin, replit</sub>
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 142,363★ · Rust · Hot  
  Desktop all-in-one for managing Claude Code/Codex/OpenClaw — swap providers & configs fast.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, codex, mcp</sub>
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 135,801★ · TypeScript · Hot  
  Garry Tan's exact Claude Code setup — 23 opinionated tools as a turnkey starting point.  
  <sub>topics: —</sub>
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 67,340★ · HTML · Rising  
  Best-practices collection: vibe-coding → agentic engineering.  
  <sub>topics: claude-ai, claude-code, best-practices, claude, claude-code-best-practices, agentic-engineering, anthropic, claude-code-agents</sub>
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 55,355★ · Python · Mature  
  The awesome-list for Claude Code skills, hooks, slash-commands, and orchestrators.  
  <sub>topics: anthropic, anthropic-claude, awesome, awesome-list, awesome-lists, awesome-resources, claude, claude-code</sub>
- **[anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)** · 53,326★ · Jupyter Notebook · Classic  
  Official recipes/notebooks for effective Claude usage patterns.  
  <sub>topics: —</sub>
- **[luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)** · 41,789★ · Python · Rising  
  Visual, example-driven guide to Claude Code from basics to advanced — the learning path.  
  <sub>topics: claude-code, guide, tutorial</sub>
- **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** · 32,530★ · Python · Hot  
  CLI to configure AND monitor Claude Code — installs commands/agents/hooks and watches usage.  
  <sub>topics: anthropic, anthropic-claude, claude, claude-code</sub>
- **[Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts)** · 12,872★ · JavaScript · Rising  
  Claude Code's full system prompt + 27 builtin tool descriptions — know what you're configuring.  
  <sub>topics: claude-code, claude-code-system-prompts, system-prompts</sub>
- **[centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup)** · 2,659★ · Python · Mature  
  A shared starter CLAUDE.md + memory-bank configuration template you can fork.  
  <sub>topics: claude, claude-ai, claude-code, subagents, claudecode-config, claudecode-hooks, claudecode-subagents</sub>

### Memory / context

_Persist decisions and context across sessions so the agent doesn't re-derive what it already learned. The backend is swappable._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 99,136★ · TypeScript · Hot  
  Persistent context across sessions for every agent — captures work and re-injects it (you run this).  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude, claude-agent-sdk, claude-agents</sub>
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 66,942★ · Python · Classic  
  Universal memory layer for AI agents — the most-adopted general memory backend.  
  <sub>topics: ai, chatgpt, llm, python, rag, long-term-memory, memory, memory-management</sub>
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 59,492★ · Python · Hot  
  Best-benchmarked open-source AI memory system — drop-in long-term memory.  
  <sub>topics: ai, chromadb, llm, mcp, memory, python</sub>
- **[memvid/memvid](https://github.com/memvid/memvid)** · 16,585★ · Rust · Declining  
  Memory layer that replaces RAG pipelines with a compact server — novel storage approach.  
  <sub>topics: ai, context, embedded, faiss, knowledge-base, knowledge-graph, llm, machine-learning</sub>
- **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** · 7,121★ · Go · Hot  
  Agent-agnostic Go binary giving coding agents persistent memory.  
  <sub>topics: —</sub>
- **[basicmachines-co/basic-memory](https://github.com/basicmachines-co/basic-memory)** · 4,129★ · Python · Hot  
  Local Markdown knowledge base exposed over MCP — the agent reads and writes plain notes you can also edit by hand.  
  <sub>topics: ai, claude, llm, mcp, open-source, python, obsidian, obsidian-md</sub>
- **[memodb-io/Acontext](https://github.com/memodb-io/Acontext)** · 3,693★ · JavaScript · Declining  
  Treats Agent Skills as a memory layer — skills-as-memory hybrid.  
  <sub>topics: agent, context-engineering, data-platform, self-learning, agent-development-kit, ai-agent, llm, memory</sub>

### Token-saver / compression

_Measure first (`codeburn`), then compress: leaner code search, output trimming, and a front proxy stack to 60–90% on common loops._

- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 110,877★ · Go · Rising  
  'Why use many token when few token do trick' — a Claude Code skill that aggressively trims tokens.  
  <sub>topics: ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering</sub>
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 82,837★ · Rust · Hot  
  CLI proxy that cuts LLM token consumption 60–90% on common dev commands — sits in front of the agent.  
  <sub>topics: agentic-coding, ai-coding, anthropic, claude-code, cli, command-line-tool, cost-reduction, developer-tools</sub>
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 74,886★ · Python · Hot  
  Compresses tool outputs, logs, files, and RAG chunks before they hit the model's context.  
  <sub>topics: agent, ai, anthropic, compression, context-engineering, context-window, fastapi, langchain</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 69,937★ · TypeScript · Hot  
  omo/lazycodex — a coding agent built for 'tokenmaxxers'; efficiency-first harness.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[toon-format/toon](https://github.com/toon-format/toon)** · 25,481★ · TypeScript · Hot  
  Token-Oriented Object Notation — compact schema-aware encoding to shrink structured payloads.  
  <sub>topics: data-format, llm, serialization, tokenization</sub>
- **[getagentseal/codeburn](https://github.com/getagentseal/codeburn)** · 11,373★ · TypeScript · Hot  
  TUI dashboard showing where your AI coding tokens go — measure before you optimize.  
  <sub>topics: ai-coding, claude-code, cli, codex, cost-tracking, developer-tools, observability, terminal-ui</sub>
- **[MinishLab/semble](https://github.com/MinishLab/semble)** · 6,191★ · Python · Hot  
  Fast, accurate code search for agents using ~98% fewer tokens than reading files.  
  <sub>topics: agents, code-search, embeddings, mcp, mcp-server, model-context-protocol, retrieval</sub>

### Code-graph / retrieval

_Give the agent structure instead of raw files — graphs and indexes answer 'how does X relate to Y' without scanning the repo._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 125,191★ · Python · Hot  
  Coding-assistant skill that turns a repo into a knowledge graph (you use this on this project).  
  <sub>topics: claude-code, graphrag, knowledge-graph, codex, openclaw, skills, antigravity, gemini</sub>
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 85,824★ · TypeScript · Hot  
  Turns any code into an interactive teaching graph — comprehension over impression.  
  <sub>topics: claude-code, claude-skills, understandcode, codex, codex-skills, knowledge-graph, opencode-skills, antigravity-skills</sub>
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 73,659★ · C · Rising  
  Pre-indexed code knowledge graph for Claude Code/Codex/Cursor — structural retrieval.  
  <sub>topics: —</sub>
- **[abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)** · 47,825★ · TypeScript · Hot  
  Zero-server code-intelligence engine — client-side code graph.  
  <sub>topics: —</sub>
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 46,283★ · C · Rising  
  High-performance code-intelligence MCP server — indexes codebases for retrieval.  
  <sub>topics: claude-code, code-analysis, code-intelligence, developer-tools, knowledge-graph, mcp, mcp-server, model-context-protocol</sub>

### MCP ecosystem

_External capabilities via a standard protocol. Each connected server costs context, so connect deliberately — `context7` (live docs) is the highest-ROI default._

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 96,042★ · — · Hot  
  The big community index of MCP servers — discovery for what to connect.  
  <sub>topics: ai, mcp</sub>
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 91,115★ · TypeScript · Hot  
  The official reference MCP servers — the canonical catalog of capabilities to plug in.  
  <sub>topics: —</sub>
- **[upstash/context7](https://github.com/upstash/context7)** · 62,855★ · TypeScript · Hot  
  Up-to-date library docs for LLMs via MCP — kills 'hallucinated API' errors (you have this wired).  
  <sub>topics: llm, mcp, mcp-server, vibe-coding</sub>

### Observability / evals

_You can't optimize what you can't see. Trace runs, watch spend, and score outputs before trusting an autonomous setup._

- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 35,600★ · TypeScript · Classic  
  Open-source LLM engineering platform: traces, evals, metrics, prompts (you trace Claude Code into this).  
  <sub>topics: analytics, llm, llmops, large-language-models, openai, self-hosted, ycombinator, monitoring</sub>
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 22,487★ · Python · Classic  
  Debug/evaluate/monitor LLM apps, RAG, and agents — eval-first observability.  
  <sub>topics: open-source, langchain, openai, playground, prompt-engineering, llama-index, llm, llm-evaluation</sub>
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 11,774★ · Python · Classic  
  AI observability & evaluation — OpenTelemetry-based tracing for agents.  
  <sub>topics: llmops, ai-monitoring, ai-observability, llm-eval, aiengineering, datasets, agents, llms</sub>
- **[traceloop/openllmetry](https://github.com/traceloop/openllmetry)** · 7,481★ · Python · Classic  
  Open-source OpenTelemetry-based observability for LLM apps — standards-based traces.  
  <sub>topics: llmops, observability, open-telemetry, metrics, monitoring, opentelemetry, datascience, ml</sub>
- **[patoles/agent-flow](https://github.com/patoles/agent-flow)** · 1,692★ · TypeScript · Mature  
  Real-time visualization of Claude Code agent orchestration — watch agents think, branch, coordinate.  
  <sub>topics: agent-visualization, ai-agents, claude-code, developer-tools, llm, vscode-extension</sub>
- **[ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht)** · 100★ · Go · Hot  
  Claude Code session lights in the macOS menu bar — at-a-glance session state.  
  <sub>topics: —</sub>

### Local runtime

_Run open models locally or proxy many models behind one endpoint — the cost floor for grunt work and the fallback when the cloud is down._

- **[ollama/ollama](https://github.com/ollama/ollama)** · 182,613★ · Go · Classic  
  Run open models locally with one command — point an agent at it to slash API cost or go offline.  
  <sub>topics: llama, llm, llms, go, golang, ollama, mistral, gemma</sub>
- **[BerriAI/litellm](https://github.com/BerriAI/litellm)** · 60,879★ · Python · Classic  
  OpenAI-compatible proxy/gateway to 100+ LLMs — swap models under any harness from one endpoint.  
  <sub>topics: anthropic, langchain, llm, llmops, openai, ai-gateway, azure-openai, bedrock</sub>

## Graph analysis — how they relate

**Community clustering.** These 61 tools span **17 of the graph's 42 communities** — the Claude-Code ecosystem is spread across agent-framework, memory, retrieval, and observability neighborhoods rather than forming one tidy cluster.

- **Community 5** (10): `anthropics/claude-code`, `ruvnet/ruflo`, `anthropics/skills`, `centminmod/my-claude-code-setup`, `davila7/claude-code-templates`, `luongnv89/claude-howto`, `shanraisshan/claude-code-best-practice`, `Piebald-AI/claude-code-system-prompts`, `anthropics/claude-cookbooks`, `thedotmack/claude-mem`
- **Community 8** (8): `NousResearch/hermes-agent`, `Yeachan-Heo/oh-my-claudecode`, `K-Dense-AI/scientific-agent-skills`, `multica-ai/andrej-karpathy-skills`, `rtk-ai/rtk`, `code-yeongyu/oh-my-openagent`, `getagentseal/codeburn`, `Egonex-AI/Understand-Anything`
- **Community 3** (8): `affaan-m/ECC`, `ComposioHQ/awesome-claude-skills`, `wshobson/agents`, `farion1231/cc-switch`, `toon-format/toon`, `upstash/context7`, `traceloop/openllmetry`, `patoles/agent-flow`
- **Community 4** (7): `earendil-works/pi`, `garrytan/gstack`, `hesreallyhim/awesome-claude-code`, `JuliusBrussee/caveman`, `Graphify-Labs/graphify`, `colbymchenry/codegraph`, `DeusData/codebase-memory-mcp`
- **Community 20** (5): `google-gemini/gemini-cli`, `aaif-goose/goose`, `MinishLab/semble`, `modelcontextprotocol/servers`, `punkpeye/awesome-mcp-servers`
- **Community 2** (4): `shareAI-lab/learn-claude-code`, `alirezarezvani/claude-skills`, `MemPalace/mempalace`, `basicmachines-co/basic-memory`
- **Community 12** (4): `langfuse/langfuse`, `comet-ml/opik`, `Arize-ai/phoenix`, `BerriAI/litellm`
- **Community 9** (3): `bytedance/deer-flow`, `memodb-io/Acontext`, `headroomlabs-ai/headroom`
- **Community 10** (3): `obra/superpowers`, `mem0ai/mem0`, `Gentleman-Programming/engram`
- **Community 22** (2): `abhigyanpatwari/GitNexus`, `ingo-eichhorst/Irrlicht`

**Centrality (PageRank in the full 2,346-repo graph)** — the most 'hub-like' setup tools in your ecosystem:

- `alirezarezvani/claude-skills` — PageRank 0.0046
- `shareAI-lab/learn-claude-code` — PageRank 0.0039
- `shanraisshan/claude-code-best-practice` — PageRank 0.0017
- `multica-ai/andrej-karpathy-skills` — PageRank 0.0014
- `MemPalace/mempalace` — PageRank 0.0012
- `affaan-m/ECC` — PageRank 0.0012
- `davila7/claude-code-templates` — PageRank 0.0011
- `JuliusBrussee/caveman` — PageRank 0.0010
- `hesreallyhim/awesome-claude-code` — PageRank 0.0009
- `upstash/context7` — PageRank 0.0008

**Direct links between these tools** (top similarity edges where both endpoints are in this report):

- `anthropics/claude-cookbooks` ⇄ `anthropics/skills` (w=0.667) — authors: cj-ant
- `alirezarezvani/claude-skills` ⇄ `shanraisshan/claude-code-best-practice` (w=0.611) — topics: agentic-ai, claude-ai, claude-code, claude-code-skills; authors: claude
- `JuliusBrussee/caveman` ⇄ `davila7/claude-code-templates` (w=0.558) — topics: anthropic, claude, claude-code; authors: github-actions[bot]
- `hesreallyhim/awesome-claude-code` ⇄ `davila7/claude-code-templates` (w=0.546) — topics: anthropic, anthropic-claude, claude, claude-code; authors: github-actions[bot]
- `langfuse/langfuse` ⇄ `comet-ml/opik` (w=0.524) — topics: llm, llmops, openai, open-source
- `shanraisshan/claude-code-best-practice` ⇄ `ruvnet/ruflo` (w=0.511) — topics: claude, agentic-ai, agentic-workflow, ai-agents; authors: claude
- `aaif-goose/goose` ⇄ `punkpeye/awesome-mcp-servers` (w=0.500) — topics: mcp, ai
- `getagentseal/codeburn` ⇄ `rtk-ai/rtk` (w=0.426) — topics: ai-coding, claude-code, cli, developer-tools; authors: dependabot[bot], mvanhorn
- `MemPalace/mempalace` ⇄ `upstash/context7` (w=0.424) — topics: llm, mcp; authors: dependabot[bot], L4XB
- `patoles/agent-flow` ⇄ `affaan-m/ECC` (w=0.400) — topics: ai-agents, claude-code, developer-tools, llm
- `rtk-ai/rtk` ⇄ `affaan-m/ECC` (w=0.384) — topics: anthropic, claude-code, developer-tools, llm; authors: dependabot[bot]
- `NousResearch/hermes-agent` ⇄ `code-yeongyu/oh-my-openagent` (w=0.333) — topics: ai, ai-agents, anthropic, chatgpt
- `shareAI-lab/learn-claude-code` ⇄ `davila7/claude-code-templates` (w=0.328) — topics: claude-code, claude; authors: github-actions[bot]
- `wshobson/agents` ⇄ `ComposioHQ/awesome-claude-skills` (w=0.326) — topics: agent-skills, ai-agents, cursor, mcp
- `shareAI-lab/learn-claude-code` ⇄ `JuliusBrussee/caveman` (w=0.319) — topics: claude-code, claude, llm; authors: github-actions[bot]
- …and 10 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). This ecosystem moves fast and a lot of it is one-person projects — check before wiring one into your daily loop.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| aaif-goose/goose | 99 | Mature | very active | 5 | 17% | 155 |
| headroomlabs-ai/headroom | 98 | Hot | very active | 8 | 16% | 173 |
| google-gemini/gemini-cli | 95 | Hot | very active | 4 | 21% | 656 |
| langfuse/langfuse | 94 | Classic | very active | 4 | 24% | 711 |
| openai/codex | 93 | Hot | very active | 8 | 16% | 1221 |
| Graphify-Labs/graphify | 91 | Hot | very active | 4 | 22% | 230 |
| modelcontextprotocol/servers | 89 | Hot | very active | 4 | 18% | 28 |
| comet-ml/opik | 89 | Classic | very active | 3 | 26% | 613 |
| anomalyco/opencode | 88 | Hot | very active | 3 | 24% | 877 |
| bytedance/deer-flow | 87 | Hot | very active | 9 | 11% | 2 |
| earendil-works/pi | 85 | Hot | very active | 2 | 38% | 272 |
| thedotmack/claude-mem | 85 | Hot | very active | 2 | 48% | 361 |
| upstash/context7 | 85 | Hot | very active | 2 | 33% | 144 |
| BerriAI/litellm | 84 | Classic | very active | 2 | 48% | 1504 |
| cline/cline | 83 | Mature | very active | 2 | 46% | 453 |
| mem0ai/mem0 | 83 | Classic | very active | 2 | 46% | 416 |
| abhigyanpatwari/GitNexus | 83 | Hot | very active | 2 | 42% | 961 |
| Arize-ai/phoenix | 83 | Classic | very active | 2 | 48% | 861 |
| ollama/ollama | 83 | Classic | very active | 2 | 42% | 260 |
| NousResearch/hermes-agent | 81 | Hot | very active | 2 | 28% | 37 |
| ruvnet/ruflo | 81 | Hot | very active | 2 | 44% | 1673 |
| Yeachan-Heo/oh-my-claudecode | 80 | Hot | very active | 1 | 52% | 255 |
| toon-format/toon | 80 | Hot | very active | 1 | 93% | 32 |
| getagentseal/codeburn | 80 | Hot | very active | 1 | 68% | 71 |
| ingo-eichhorst/Irrlicht | 80 | Hot | very active | 1 | 91% | 46 |
| openclaw/openclaw | 79 | Hot | very active | 1 | 67% | 255 |
| affaan-m/ECC | 79 | Hot | very active | 1 | 59% | 19 |
| K-Dense-AI/scientific-agent-skills | 79 | Hot | very active | 1 | 70% | 109 |
| Gentleman-Programming/engram | 79 | Hot | very active | 1 | 76% | 121 |
| basicmachines-co/basic-memory | 79 | Hot | very active | 1 | 90% | 90 |
| JuliusBrussee/caveman | 79 | Rising | very active | 1 | 99% | 47 |
| anthropics/claude-code | 78 | Hot | very active | 1 | 54% | 241 |
| code-yeongyu/oh-my-openagent | 78 | Hot | very active | 1 | 98% | 337 |
| colbymchenry/codegraph | 78 | Rising | very active | 1 | 99% | 33 |
| farion1231/cc-switch | 77 | Hot | very active | 1 | 65% | 63 |
| Piebald-AI/claude-code-system-prompts | 77 | Rising | very active | 1 | 100% | 261 |
| MemPalace/mempalace | 76 | Hot | very active | 1 | 72% | 18 |
| DeusData/codebase-memory-mcp | 76 | Rising | very active | 1 | 100% | 47 |
| davila7/claude-code-templates | 75 | Hot | very active | 1 | 53% | 22 |
| rtk-ai/rtk | 75 | Hot | very active | 1 | 76% | 407 |
| Egonex-AI/Understand-Anything | 75 | Hot | very active | 1 | 85% | 8 |
| obra/superpowers | 74 | Hot | very active | 1 | 91% | 15 |
| alirezarezvani/claude-skills | 73 | Hot | active | 1 | 57% | 6 |
| MinishLab/semble | 73 | Hot | very active | 1 | 75% | 30 |
| traceloop/openllmetry | 71 | Classic | active | 2 | 29% | 263 |
| luongnv89/claude-howto | 67 | Rising | very active | 1 | 90% | 10 |
| shanraisshan/claude-code-best-practice | 64 | Rising | very active | 1 | 100% | 0 |
| wshobson/agents | 62 | Hot | very active | 1 | 53% | 0 |
| garrytan/gstack | 62 | Hot | very active | 1 | 84% | 0 |
| hesreallyhim/awesome-claude-code | 61 | Mature | very active | 1 | 95% | 0 |
| anthropics/claude-cookbooks | 60 | Classic | very active | 2 | 41% | 0 |
| punkpeye/awesome-mcp-servers | 60 | Hot | very active | 1 | 91% | 0 |
| shareAI-lab/learn-claude-code | 59 | Hot | very active | 1 | 71% | 0 |
| patoles/agent-flow | 55 | Mature | active | 1 | 80% | 4 |
| memvid/memvid | 53 | Declining | slowing | 1 | 100% | 12 |
| anthropics/skills | 51 | Mature | active | 2 | 41% | 0 |
| centminmod/my-claude-code-setup | 48 | Mature | active | 1 | 100% | 0 |
| memodb-io/Acontext | 46 | Declining | slowing | 0 | 0% | 279 |
| x1xhlol/system-prompts-and-models-of-ai-tools | 42 | Mature | slowing | 1 | 100% | 0 |
| ComposioHQ/awesome-claude-skills | 37 | Declining | active | 1 | 100% | 0 |
| multica-ai/andrej-karpathy-skills | 20 | Declining | slowing | 0 | 0% | 0 |

## Adjacent (deliberately not listed here)

- **campfirein/byterover-cli** — archived upstream — the portable `brv` memory layer is no longer maintained
- **n8n-io/n8n** (206,900★) — workflow-automation platform — orchestrates agents but isn't a Claude-Code setup layer
- **langgenius/dify** (158,081★) — agentic-workflow platform — covered by the agent-orchestration report
- **langchain-ai/langchain** (147,557★) — agent-engineering library — app framework, not a CC setup tool
- **open-webui/open-webui** (154,191★) — chat UI for local models — a frontend, not an agent setup
- **ultraworkers/claw-code** (194,982★) — art/exhibit harness — not a practical setup layer
- **multica-ai/multica** (52,396★) — managed-agents platform — team product, see agent-orchestration report

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (claude-code / skill / agent harness / mcp / memory / token / observability / code-graph / setup) across name+description+topics, then manual curation into the nine setup layers. General agent *application* frameworks, chat UIs, and broad platforms were routed to adjacent reports or excluded (see above).
- **The three-strategy table is opinionated**, built only from repos in your stars — it is a starting point, not a benchmark. Validate model-tier and token-saver claims against your own `langfuse`/`codeburn` traces.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.

<sub>Tools covered: 61 · Snapshot: 2026-10-11T13:10:52.436Z</sub>
