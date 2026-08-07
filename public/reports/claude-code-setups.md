# Claude Code Superpowers — Setup Strategies from Your Stars

> Derived from **kaiser-data**'s 1,476 starred repos (snapshot `2026-08-07T21:10:17.796Z`), cross-referenced with the repo-similarity graph (1,476 nodes / 4,785 edges, 33 communities).
>
> Generated 2026-08-07 by `scripts/reports/claude_code_setups.py` (regenerate any time — no API cost).

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

- **59 Claude-Code 'superpower' projects** in your stars (**4,679,822★** combined), spanning 9 setup layers:
  - **Harness / coding agent** (12): `openclaw`, `hermes-agent`, `opencode`, `claude-code`, `gemini-cli`, `codex`, `pi`, `deer-flow`, `ruflo`, `cline`, `goose`, `oh-my-claudecode`
  - **Skills framework** (6): `superpowers`, `ECC`, `skills`, `awesome-claude-skills`, `agents`, `scientific-agent-skills`
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
| **Harness / coding agent** | The agent loop itself | `openclaw`, `hermes-agent`, `opencode`, `claude-code`, `gemini-cli`, `codex` |
| **Skills framework** | On-demand expertise (the modern superpower) | `superpowers`, `ECC`, `skills`, `awesome-claude-skills`, `agents`, `scientific-agent-skills` |
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
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Harness / coding agent | TypeScript | NOASSERTION | 385,469 (▲1,936) | Hot | 84 | very active | 0d ago | 8mo | 20 |
| [obra/superpowers](https://github.com/obra/superpowers) | Skills framework | Shell | MIT | 268,683 (▲10,872) | Hot | 78 | very active | 0d ago | 10mo | 6 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Skills framework | JavaScript | MIT | 238,551 (▲7,200) | Hot | 85 | very active | 0d ago | 6mo | 29 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Harness / coding agent | Python | MIT | 227,042 (▲9,598) | Hot | 85 | very active | 0d ago | 1.0y | 20 |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Config / setup kit | — | — | 200,508 (▲6,004) | Declining | 26 | slowing | 3mo ago | 6mo | 0 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | Harness / coding agent | TypeScript | MIT | 194,722 (▲7,081) | Hot | 83 | very active | 0d ago | 1.3y | 21 |
| [ollama/ollama](https://github.com/ollama/ollama) | Local runtime | Go | MIT | 178,014 (▲1,523) | Classic | 83 | very active | 0d ago | 3.1y | 12 |
| [anthropics/skills](https://github.com/anthropics/skills) | Skills framework | Python | — | 166,884 (▲4,066) | Rising | 45 | active | 0d ago | 10mo | 4 |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Config / setup kit | — | GPL-3.0 | 142,645 (▲545) | Mature | 52 | very active | 1d ago | 1.4y | 4 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Harness / coding agent | Python | — | 140,599 (▲2,209) | Hot | 76 | very active | 1d ago | 1.5y | 7 |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Config / setup kit | TypeScript | MIT | 126,792 (▲3,736) | Hot | 58 | very active | 0d ago | 4mo | 5 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Config / setup kit | Rust | MIT | 125,449 (▲6,353) | Hot | 77 | very active | 0d ago | 1.0y | 14 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Harness / coding agent | TypeScript | Apache-2.0 | 106,408 (▲329) | Hot | 90 | very active | 0d ago | 1.3y | 15 |
| [openai/codex](https://github.com/openai/codex) | Harness / coding agent | Rust | Apache-2.0 | 104,648 (▲4,803) | Hot | 95 | very active | 0d ago | 1.3y | 43 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Code-graph / retrieval | Python | Apache-2.0 | 103,983 (▲12,167) | Hot | 77 | very active | 1d ago | 4mo | 20 |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Token-saver / compression | JavaScript | MIT | 96,694 (▲5,744) | Hot | 72 | very active | 3d ago | 4mo | 10 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP ecosystem | — | MIT | 91,941 (▲962) | Hot | 64 | very active | 5d ago | 1.7y | 16 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Memory / context | JavaScript | Apache-2.0 | 89,998 (▲2,086) | Hot | 79 | very active | 2d ago | 11mo | 7 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | MCP ecosystem | TypeScript | NOASSERTION | 89,327 (▲677) | Hot | 83 | very active | 2d ago | 1.7y | 15 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness / coding agent | TypeScript | MIT | 85,266 (▲12,268) | Hot | 90 | very active | 0d ago | 12mo | 20 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Harness / coding agent | Python | MIT | 79,512 (▲2,089) | Hot | 84 | very active | 0d ago | 1.3y | 35 |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | Code-graph / retrieval | TypeScript | MIT | 77,872 (▲2,619) | Hot | 80 | very active | 9d ago | 4mo | 15 |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Token-saver / compression | Rust | Apache-2.0 | 75,183 (▲3,245) | Hot | 78 | very active | 0d ago | 6mo | 11 |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Skills framework | Python | — | 72,027 (▲3,891) | Mature | 40 | active | 15d ago | 9mo | 4 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Token-saver / compression | TypeScript | NOASSERTION | 67,452 (▲1,235) | Hot | 78 | very active | 0d ago | 8mo | 5 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Harness / coding agent | TypeScript | MIT | 67,279 (▲2,042) | Hot | 76 | very active | 1d ago | 1.2y | 3 |
| [cline/cline](https://github.com/cline/cline) | Harness / coding agent | TypeScript | Apache-2.0 | 65,830 (▲1,009) | Mature | 79 | very active | 0d ago | 2.1y | 17 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Token-saver / compression | Python | Apache-2.0 | 65,384 (▲4,895) | Hot | 81 | very active | 0d ago | 7mo | 27 |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | Code-graph / retrieval | C | MIT | 65,312 (▲4,284) | Hot | 78 | very active | 0d ago | 6mo | 3 |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Config / setup kit | HTML | MIT | 64,138 (▲1,004) | Rising | 65 | very active | 0d ago | 9mo | 2 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Memory / context | Python | Apache-2.0 | 62,779 (▲1,505) | Classic | 89 | very active | 0d ago | 3.1y | 34 |
| [upstash/context7](https://github.com/upstash/context7) | MCP ecosystem | TypeScript | MIT | 60,396 (▲936) | Hot | 84 | very active | 0d ago | 1.4y | 18 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Memory / context | Python | MIT | 58,192 (▲699) | Hot | 76 | very active | 0d ago | 4mo | 8 |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Local runtime | Python | NOASSERTION | 55,826 (▲1,752) | Classic | 79 | very active | 0d ago | 3.0y | 11 |
| [aaif-goose/goose](https://github.com/aaif-goose/goose) | Harness / coding agent | Rust | Apache-2.0 | 52,523 (▲1,210) | Hot | 99 | very active | 0d ago | 2.0y | 43 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Config / setup kit | Python | NOASSERTION | 51,848 (▲1,388) | Mature | 61 | very active | 0d ago | 1.3y | 2 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Config / setup kit | Jupyter Notebook | MIT | 51,104 (▲1,916) | Mature | 67 | very active | 0d ago | 3.0y | 14 |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | Code-graph / retrieval | TypeScript | NOASSERTION | 45,175 (▲784) | Hot | 83 | very active | 0d ago | 1.0y | 13 |
| [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | Config / setup kit | Python | MIT | 40,902 (▲882) | Hot | 70 | very active | 2d ago | 9mo | 5 |
| [wshobson/agents](https://github.com/wshobson/agents) | Skills framework | Python | MIT | 38,595 (▲526) | Hot | 64 | very active | 3d ago | 1.0y | 20 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Harness / coding agent | TypeScript | MIT | 38,422 (▲520) | Hot | 80 | very active | 1d ago | 7mo | 15 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Code-graph / retrieval | C | MIT | 38,040 (▲4,982) | Hot | 75 | very active | 0d ago | 5mo | 4 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Skills framework | Python | MIT | 32,920 (▲1,663) | Hot | 80 | very active | 0d ago | 9mo | 5 |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Observability / evals | TypeScript | NOASSERTION | 32,708 (▲1,250) | Classic | 89 | very active | 0d ago | 3.2y | 14 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Config / setup kit | Python | MIT | 30,147 (▲397) | Hot | 80 | very active | 0d ago | 1.1y | 15 |
| [toon-format/toon](https://github.com/toon-format/toon) | Token-saver / compression | TypeScript | MIT | 25,107 (▲178) | Hot | 80 | very active | 0d ago | 9mo | 5 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Observability / evals | Python | Apache-2.0 | 21,197 (▲483) | Classic | 94 | very active | 0d ago | 3.2y | 17 |
| [memvid/memvid](https://github.com/memvid/memvid) | Memory / context | Rust | Apache-2.0 | 16,189 (▲180) | Declining | 61 | active | 24d ago | 1.2y | 2 |
| [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | Config / setup kit | JavaScript | MIT | 12,214 (▲297) | Rising | 76 | very active | 0d ago | 8mo | 2 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Observability / evals | Python | NOASSERTION | 10,937 (▲303) | Classic | 79 | very active | 0d ago | 3.7y | 18 |
| [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | Token-saver / compression | TypeScript | MIT | 9,192 (▲426) | Hot | 79 | very active | 3d ago | 3mo | 10 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Observability / evals | Python | Apache-2.0 | 7,360 (▲48) | Mature | 70 | very active | 3d ago | 2.9y | 4 |
| [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram) | Memory / context | Go | MIT | 5,899 (▲319) | Hot | 76 | very active | 8d ago | 5mo | 12 |
| [MinishLab/semble](https://github.com/MinishLab/semble) | Token-saver / compression | Python | MIT | 5,843 (▲189) | Hot | 76 | very active | 2d ago | 4mo | 6 |
| [campfirein/byterover-cli](https://github.com/campfirein/byterover-cli) | Memory / context | TypeScript | NOASSERTION | 4,933 (▲8) | Hot | 80 | active | 1mo ago | 1.1y | 8 |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | Memory / context | JavaScript | Apache-2.0 | 3,662 (▲79) | Declining | 51 | active | 24d ago | 1.1y | 0 |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | Config / setup kit | Python | MIT | 2,551 (▲28) | Mature | 55 | very active | 6d ago | 1.1y | 1 |
| [patoles/agent-flow](https://github.com/patoles/agent-flow) | Observability / evals | TypeScript | Apache-2.0 | 1,457 (▲148) | Mature | 51 | active | 27d ago | 4mo | 2 |
| [ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht) | Observability / evals | Go | MIT | 92 (▲3) | Hot | 85 | very active | 0d ago | 11mo | 3 |

## By layer

### Harness / coding agent

_The loop that reads, plans, edits, and runs. Pick one as your daily driver; keep a second installed to diff behavior and model-shop._

- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · 385,469★ · TypeScript · Hot  
  Cross-platform personal-assistant harness — an 'any OS, any platform' agent runtime.  
  <sub>topics: ai, assistant, own-your-data, personal, crustacean, molty, openclaw</sub>
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 227,042★ · Python · Hot  
  Long-lived 'agent that grows with you' harness — persistent, personalized agent loop.  
  <sub>topics: ai, ai-agent, ai-agents, llm, anthropic, chatgpt, claude, claude-code</sub>
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 194,722★ · TypeScript · Hot  
  Open-source terminal coding agent — a provider-agnostic alternative harness.  
  <sub>topics: —</sub>
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 140,599★ · Python · Hot  
  Claude Code itself — the agentic CLI that lives in your terminal; the baseline every setup here extends.  
  <sub>topics: —</sub>
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 106,408★ · TypeScript · Hot  
  Gemini's open-source terminal agent — the third major CLI harness; handy for model-shopping.  
  <sub>topics: gemini, gemini-api, ai, ai-agents, cli, mcp-client, mcp-server</sub>
- **[openai/codex](https://github.com/openai/codex)** · 104,648★ · Rust · Hot  
  OpenAI's lightweight terminal coding agent — useful as a second harness to diff behavior against Claude Code.  
  <sub>topics: —</sub>
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 85,266★ · TypeScript · Hot  
  Unified LLM-API + agent-loop + TUI toolkit — a kit for rolling your own coding agent.  
  <sub>topics: —</sub>
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 79,512★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and writes — multi-step autonomy.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 67,279★ · TypeScript · Hot  
  Agent meta-harness for Claude — deploys multi-agent swarms with coordination.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server</sub>
- **[cline/cline](https://github.com/cline/cline)** · 65,830★ · TypeScript · Mature  
  Autonomous coding agent as SDK / IDE extension / CLI — strong for in-editor agentic workflows.  
  <sub>topics: —</sub>
- **[aaif-goose/goose](https://github.com/aaif-goose/goose)** · 52,523★ · Rust · Hot  
  Extensible open agent that installs and runs tools, not just suggestions — MCP-native.  
  <sub>topics: mcp, acp, ai, ai-agents</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 38,422★ · TypeScript · Hot  
  Teams-first multi-agent orchestration layer for Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>

### Skills framework

_The biggest 2026 upgrade. Skills load only when triggered, so they add capability without taxing every session — the opposite of a big always-on CLAUDE.md._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 268,683★ · Shell · Hot  
  Agentic skills framework + dev methodology — the headline 'give your agent superpowers' skill collection.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 238,551★ · JavaScript · Hot  
  Agent-harness performance system bundling skills, instincts, and memory into one optimization layer.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[anthropics/skills](https://github.com/anthropics/skills)** · 166,884★ · Python · Rising  
  Anthropic's official Agent Skills repo — canonical examples of the skills format.  
  <sub>topics: agent-skills</sub>
- **[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** · 72,027★ · Python · Mature  
  Curated index of Claude Skills + tooling — the discovery hub for what's worth installing.  
  <sub>topics: claude, claude-code, agent-skills, ai-agents, antigravity, automation, codex, composio</sub>
- **[wshobson/agents](https://github.com/wshobson/agents)** · 38,595★ · Python · Hot  
  Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor) — subagents & commands.  
  <sub>topics: agents, anthropic, automation, workflows, orchestration, agent-skills, agentic-ai, ai-agents</sub>
- **[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)** · 32,920★ · Python · Hot  
  Domain skill pack that turns an agent into a research scientist — example of vertical skills.  
  <sub>topics: ai-scientist, bioinformatics, chemoinformatics, claude, claude-skills, claudecode, clinical-research, computational-biology</sub>

### Config / setup kit

_Turnkey CLAUDE.md / command / hook bundles. Steal a good one, then trim to what you actually use — bloat here is paid on every prompt._

- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 200,508★ · — · Declining  
  A single CLAUDE.md derived from Karpathy's habits — the 'one good config file' approach.  
  <sub>topics: —</sub>
- **[x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)** · 142,645★ · — · Mature  
  Leaked/collected system prompts of major AI coding tools — prompt-engineering reference.  
  <sub>topics: ai, cursor, lovable, system-prompts, v0, cursorai, devin, replit</sub>
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 126,792★ · TypeScript · Hot  
  Garry Tan's exact Claude Code setup — 23 opinionated tools as a turnkey starting point.  
  <sub>topics: —</sub>
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 125,449★ · Rust · Hot  
  Desktop all-in-one for managing Claude Code/Codex/OpenClaw — swap providers & configs fast.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, typescript, codex</sub>
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 64,138★ · HTML · Rising  
  Best-practices collection: vibe-coding → agentic engineering.  
  <sub>topics: claude-ai, claude-code, best-practices, claude, claude-code-best-practices, agentic-engineering, anthropic, claude-code-agents</sub>
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 51,848★ · Python · Mature  
  The awesome-list for Claude Code skills, hooks, slash-commands, and orchestrators.  
  <sub>topics: anthropic, anthropic-claude, awesome, awesome-list, awesome-lists, awesome-resources, claude, claude-code</sub>
- **[anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)** · 51,104★ · Jupyter Notebook · Mature  
  Official recipes/notebooks for effective Claude usage patterns.  
  <sub>topics: —</sub>
- **[luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)** · 40,902★ · Python · Hot  
  Visual, example-driven guide to Claude Code from basics to advanced — the learning path.  
  <sub>topics: claude-code, guide, tutorial</sub>
- **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** · 30,147★ · Python · Hot  
  CLI to configure AND monitor Claude Code — installs commands/agents/hooks and watches usage.  
  <sub>topics: anthropic, anthropic-claude, claude, claude-code</sub>
- **[Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts)** · 12,214★ · JavaScript · Rising  
  Claude Code's full system prompt + 27 builtin tool descriptions — know what you're configuring.  
  <sub>topics: claude-code, claude-code-system-prompts, system-prompts</sub>
- **[centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup)** · 2,551★ · Python · Mature  
  A shared starter CLAUDE.md + memory-bank configuration template you can fork.  
  <sub>topics: claude, claude-ai, claude-code, subagents, claudecode-config, claudecode-hooks, claudecode-subagents</sub>

### Memory / context

_Persist decisions and context across sessions so the agent doesn't re-derive what it already learned. The backend is swappable._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 89,998★ · JavaScript · Hot  
  Persistent context across sessions for every agent — captures work and re-injects it (you run this).  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude, claude-agent-sdk, claude-agents</sub>
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 62,779★ · Python · Classic  
  Universal memory layer for AI agents — the most-adopted general memory backend.  
  <sub>topics: ai, chatgpt, llm, python, chatbots, rag, application, long-term-memory</sub>
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 58,192★ · Python · Hot  
  Best-benchmarked open-source AI memory system — drop-in long-term memory.  
  <sub>topics: ai, chromadb, llm, mcp, memory, python</sub>
- **[memvid/memvid](https://github.com/memvid/memvid)** · 16,189★ · Rust · Declining  
  Memory layer that replaces RAG pipelines with a compact server — novel storage approach.  
  <sub>topics: ai, context, embedded, faiss, knowledge-base, knowledge-graph, llm, machine-learning</sub>
- **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** · 5,899★ · Go · Hot  
  Agent-agnostic Go binary giving coding agents persistent memory.  
  <sub>topics: —</sub>
- **[campfirein/byterover-cli](https://github.com/campfirein/byterover-cli)** · 4,933★ · TypeScript · Hot  
  Portable memory layer (brv) for autonomous coding agents — agent-agnostic.  
  <sub>topics: agent, llm, mcp, memory, vibe-coding, ai, autonomous-agents, cli</sub>
- **[memodb-io/Acontext](https://github.com/memodb-io/Acontext)** · 3,662★ · JavaScript · Declining  
  Treats Agent Skills as a memory layer — skills-as-memory hybrid.  
  <sub>topics: agent, context-engineering, data-platform, self-learning, agent-development-kit, ai-agent, llm, memory</sub>

### Token-saver / compression

_Measure first (`codeburn`), then compress: leaner code search, output trimming, and a front proxy stack to 60–90% on common loops._

- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 96,694★ · JavaScript · Hot  
  'Why use many token when few token do trick' — a Claude Code skill that aggressively trims tokens.  
  <sub>topics: ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering</sub>
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 75,183★ · Rust · Hot  
  CLI proxy that cuts LLM token consumption 60–90% on common dev commands — sits in front of the agent.  
  <sub>topics: agentic-coding, ai-coding, anthropic, claude-code, cli, command-line-tool, cost-reduction, developer-tools</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 67,452★ · TypeScript · Hot  
  omo/lazycodex — a coding agent built for 'tokenmaxxers'; efficiency-first harness.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 65,384★ · Python · Hot  
  Compresses tool outputs, logs, files, and RAG chunks before they hit the model's context.  
  <sub>topics: agent, ai, anthropic, compression, context-engineering, context-window, fastapi, langchain</sub>
- **[toon-format/toon](https://github.com/toon-format/toon)** · 25,107★ · TypeScript · Hot  
  Token-Oriented Object Notation — compact schema-aware encoding to shrink structured payloads.  
  <sub>topics: data-format, llm, serialization, tokenization</sub>
- **[getagentseal/codeburn](https://github.com/getagentseal/codeburn)** · 9,192★ · TypeScript · Hot  
  TUI dashboard showing where your AI coding tokens go — measure before you optimize.  
  <sub>topics: ai-coding, claude-code, cli, codex, cost-tracking, developer-tools, observability, terminal-ui</sub>
- **[MinishLab/semble](https://github.com/MinishLab/semble)** · 5,843★ · Python · Hot  
  Fast, accurate code search for agents using ~98% fewer tokens than reading files.  
  <sub>topics: agents, code-search, embeddings, mcp, mcp-server, model-context-protocol, retrieval</sub>

### Code-graph / retrieval

_Give the agent structure instead of raw files — graphs and indexes answer 'how does X relate to Y' without scanning the repo._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 103,983★ · Python · Hot  
  Coding-assistant skill that turns a repo into a knowledge graph (you use this on this project).  
  <sub>topics: claude-code, graphrag, knowledge-graph, codex, openclaw, skills, antigravity, gemini</sub>
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 77,872★ · TypeScript · Hot  
  Turns any code into an interactive teaching graph — comprehension over impression.  
  <sub>topics: claude-code, claude-skills, understandcode, codex, codex-skills, knowledge-graph, opencode-skills, antigravity-skills</sub>
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 65,312★ · C · Hot  
  Pre-indexed code knowledge graph for Claude Code/Codex/Cursor — structural retrieval.  
  <sub>topics: —</sub>
- **[abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)** · 45,175★ · TypeScript · Hot  
  Zero-server code-intelligence engine — client-side code graph.  
  <sub>topics: —</sub>
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 38,040★ · C · Hot  
  High-performance code-intelligence MCP server — indexes codebases for retrieval.  
  <sub>topics: claude-code, code-analysis, code-intelligence, developer-tools, knowledge-graph, mcp, mcp-server, model-context-protocol</sub>

### MCP ecosystem

_External capabilities via a standard protocol. Each connected server costs context, so connect deliberately — `context7` (live docs) is the highest-ROI default._

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 91,941★ · — · Hot  
  The big community index of MCP servers — discovery for what to connect.  
  <sub>topics: ai, mcp</sub>
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 89,327★ · TypeScript · Hot  
  The official reference MCP servers — the canonical catalog of capabilities to plug in.  
  <sub>topics: —</sub>
- **[upstash/context7](https://github.com/upstash/context7)** · 60,396★ · TypeScript · Hot  
  Up-to-date library docs for LLMs via MCP — kills 'hallucinated API' errors (you have this wired).  
  <sub>topics: llm, mcp, mcp-server, vibe-coding</sub>

### Observability / evals

_You can't optimize what you can't see. Trace runs, watch spend, and score outputs before trusting an autonomous setup._

- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 32,708★ · TypeScript · Classic  
  Open-source LLM engineering platform: traces, evals, metrics, prompts (you trace Claude Code into this).  
  <sub>topics: analytics, llm, llmops, large-language-models, openai, self-hosted, ycombinator, monitoring</sub>
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 21,197★ · Python · Classic  
  Debug/evaluate/monitor LLM apps, RAG, and agents — eval-first observability.  
  <sub>topics: open-source, langchain, openai, playground, prompt-engineering, llama-index, llm, llm-evaluation</sub>
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 10,937★ · Python · Classic  
  AI observability & evaluation — OpenTelemetry-based tracing for agents.  
  <sub>topics: llmops, ai-monitoring, ai-observability, llm-eval, aiengineering, datasets, agents, llms</sub>
- **[traceloop/openllmetry](https://github.com/traceloop/openllmetry)** · 7,360★ · Python · Mature  
  Open-source OpenTelemetry-based observability for LLM apps — standards-based traces.  
  <sub>topics: llmops, observability, open-telemetry, metrics, monitoring, opentelemetry, datascience, ml</sub>
- **[patoles/agent-flow](https://github.com/patoles/agent-flow)** · 1,457★ · TypeScript · Mature  
  Real-time visualization of Claude Code agent orchestration — watch agents think, branch, coordinate.  
  <sub>topics: agent-visualization, ai-agents, claude-code, developer-tools, llm, vscode-extension</sub>
- **[ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht)** · 92★ · Go · Hot  
  Claude Code session lights in the macOS menu bar — at-a-glance session state.  
  <sub>topics: —</sub>

### Local runtime

_Run open models locally or proxy many models behind one endpoint — the cost floor for grunt work and the fallback when the cloud is down._

- **[ollama/ollama](https://github.com/ollama/ollama)** · 178,014★ · Go · Classic  
  Run open models locally with one command — point an agent at it to slash API cost or go offline.  
  <sub>topics: llama, llm, llms, go, golang, ollama, mistral, gemma</sub>
- **[BerriAI/litellm](https://github.com/BerriAI/litellm)** · 55,826★ · Python · Classic  
  OpenAI-compatible proxy/gateway to 100+ LLMs — swap models under any harness from one endpoint.  
  <sub>topics: anthropic, langchain, llm, llmops, openai, ai-gateway, azure-openai, bedrock</sub>

## Graph analysis — how they relate

**Community clustering.** These 59 tools span **14 of the graph's 33 communities** — the Claude-Code ecosystem is spread across agent-framework, memory, retrieval, and observability neighborhoods rather than forming one tidy cluster.

- **Community 0** (18): `anthropics/claude-code`, `earendil-works/pi`, `ruvnet/ruflo`, `anthropics/skills`, `K-Dense-AI/scientific-agent-skills`, `garrytan/gstack`, `centminmod/my-claude-code-setup`, `davila7/claude-code-templates`, `farion1231/cc-switch`, `luongnv89/claude-howto`, `hesreallyhim/awesome-claude-code`, `Piebald-AI/claude-code-system-prompts`, `anthropics/claude-cookbooks`, `rtk-ai/rtk`, `getagentseal/codeburn`, `colbymchenry/codegraph`, `Egonex-AI/Understand-Anything`, `traceloop/openllmetry`
- **Community 9** (9): `NousResearch/hermes-agent`, `Yeachan-Heo/oh-my-claudecode`, `affaan-m/ECC`, `ComposioHQ/awesome-claude-skills`, `wshobson/agents`, `thedotmack/claude-mem`, `JuliusBrussee/caveman`, `code-yeongyu/oh-my-openagent`, `patoles/agent-flow`
- **Community 24** (7): `bytedance/deer-flow`, `mem0ai/mem0`, `headroomlabs-ai/headroom`, `langfuse/langfuse`, `comet-ml/opik`, `Arize-ai/phoenix`, `BerriAI/litellm`
- **Community 3** (5): `aaif-goose/goose`, `x1xhlol/system-prompts-and-models-of-ai-tools`, `MemPalace/mempalace`, `memodb-io/Acontext`, `punkpeye/awesome-mcp-servers`
- **Community 11** (4): `openclaw/openclaw`, `google-gemini/gemini-cli`, `obra/superpowers`, `campfirein/byterover-cli`
- **Community 16** (3): `cline/cline`, `abhigyanpatwari/GitNexus`, `DeusData/codebase-memory-mcp`
- **Community 13** (3): `shanraisshan/claude-code-best-practice`, `toon-format/toon`, `ollama/ollama`
- **Community 22** (3): `MinishLab/semble`, `modelcontextprotocol/servers`, `upstash/context7`
- **Community 8** (2): `Graphify-Labs/graphify`, `ingo-eichhorst/Irrlicht`

**Centrality (PageRank in the full 1,476-repo graph)** — the most 'hub-like' setup tools in your ecosystem:

- `ingo-eichhorst/Irrlicht` — PageRank 0.0020
- `hesreallyhim/awesome-claude-code` — PageRank 0.0020
- `affaan-m/ECC` — PageRank 0.0019
- `punkpeye/awesome-mcp-servers` — PageRank 0.0016
- `davila7/claude-code-templates` — PageRank 0.0013
- `comet-ml/opik` — PageRank 0.0013
- `aaif-goose/goose` — PageRank 0.0010
- `MemPalace/mempalace` — PageRank 0.0010
- `DeusData/codebase-memory-mcp` — PageRank 0.0010
- `upstash/context7` — PageRank 0.0009

**Direct links between these tools** (top similarity edges where both endpoints are in this report):

- `anthropics/claude-cookbooks` ⇄ `anthropics/skills` (w=0.750) — authors: cj-ant, rlancemartin
- `anthropics/skills` ⇄ `anthropics/claude-code` (w=0.750) — authors: williamqian12
- `langfuse/langfuse` ⇄ `comet-ml/opik` (w=0.590) — topics: llm, llmops, openai, open-source; authors: dependabot[bot]
- `aaif-goose/goose` ⇄ `punkpeye/awesome-mcp-servers` (w=0.500) — topics: mcp, ai
- `hesreallyhim/awesome-claude-code` ⇄ `K-Dense-AI/scientific-agent-skills` (w=0.442) — topics: claude, agent-skills; authors: github-actions[bot]
- `patoles/agent-flow` ⇄ `affaan-m/ECC` (w=0.400) — topics: ai-agents, claude-code, developer-tools, llm
- `hesreallyhim/awesome-claude-code` ⇄ `davila7/claude-code-templates` (w=0.386) — topics: anthropic, anthropic-claude, claude, claude-code; authors: github-actions[bot]
- `Arize-ai/phoenix` ⇄ `comet-ml/opik` (w=0.380) — topics: llmops, prompt-engineering, llm-evaluation, openai; authors: dependabot[bot], Anuj7411
- `JuliusBrussee/caveman` ⇄ `davila7/claude-code-templates` (w=0.356) — topics: anthropic, claude, claude-code; authors: github-actions[bot]
- `JuliusBrussee/caveman` ⇄ `hesreallyhim/awesome-claude-code` (w=0.342) — topics: anthropic, claude, claude-code, llm; authors: github-actions[bot]
- `MemPalace/mempalace` ⇄ `punkpeye/awesome-mcp-servers` (w=0.333) — topics: ai, mcp
- `wshobson/agents` ⇄ `ComposioHQ/awesome-claude-skills` (w=0.326) — topics: automation, agent-skills, ai-agents, cursor
- `rtk-ai/rtk` ⇄ `affaan-m/ECC` (w=0.313) — topics: anthropic, claude-code, developer-tools, llm
- `DeusData/codebase-memory-mcp` ⇄ `Graphify-Labs/graphify` (w=0.300) — topics: claude-code, code-analysis, developer-tools, knowledge-graph
- `NousResearch/hermes-agent` ⇄ `code-yeongyu/oh-my-openagent` (w=0.292) — topics: ai, ai-agents, anthropic, chatgpt
- …and 10 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). This ecosystem moves fast and a lot of it is one-person projects — check before wiring one into your daily loop.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| aaif-goose/goose | 99 | Hot | very active | 6 | 13% | 145 |
| openai/codex | 95 | Hot | very active | 7 | 21% | 974 |
| comet-ml/opik | 94 | Classic | very active | 4 | 23% | 543 |
| google-gemini/gemini-cli | 90 | Hot | very active | 3 | 19% | 574 |
| earendil-works/pi | 90 | Hot | very active | 3 | 34% | 254 |
| mem0ai/mem0 | 89 | Classic | very active | 3 | 38% | 379 |
| langfuse/langfuse | 89 | Classic | very active | 3 | 29% | 645 |
| NousResearch/hermes-agent | 85 | Hot | very active | 3 | 24% | 24 |
| affaan-m/ECC | 85 | Hot | very active | 2 | 39% | 15 |
| ingo-eichhorst/Irrlicht | 85 | Hot | very active | 2 | 47% | 38 |
| openclaw/openclaw | 84 | Hot | very active | 2 | 41% | 231 |
| bytedance/deer-flow | 84 | Hot | very active | 7 | 13% | 1 |
| upstash/context7 | 84 | Hot | very active | 2 | 42% | 101 |
| anomalyco/opencode | 83 | Hot | very active | 2 | 44% | 857 |
| abhigyanpatwari/GitNexus | 83 | Hot | very active | 2 | 33% | 718 |
| modelcontextprotocol/servers | 83 | Hot | very active | 3 | 30% | 26 |
| ollama/ollama | 83 | Classic | very active | 2 | 36% | 237 |
| headroomlabs-ai/headroom | 81 | Hot | very active | 2 | 48% | 161 |
| Yeachan-Heo/oh-my-claudecode | 80 | Hot | very active | 1 | 64% | 242 |
| K-Dense-AI/scientific-agent-skills | 80 | Hot | very active | 1 | 92% | 99 |
| davila7/claude-code-templates | 80 | Hot | very active | 2 | 33% | 19 |
| campfirein/byterover-cli | 80 | Hot | active | 2 | 27% | 27 |
| toon-format/toon | 80 | Hot | very active | 1 | 96% | 31 |
| Egonex-AI/Understand-Anything | 80 | Hot | very active | 2 | 47% | 8 |
| cline/cline | 79 | Mature | very active | 1 | 56% | 356 |
| thedotmack/claude-mem | 79 | Hot | very active | 1 | 88% | 304 |
| getagentseal/codeburn | 79 | Hot | very active | 1 | 59% | 48 |
| Arize-ai/phoenix | 79 | Classic | very active | 1 | 57% | 774 |
| BerriAI/litellm | 79 | Classic | very active | 1 | 56% | 1425 |
| obra/superpowers | 78 | Hot | very active | 1 | 82% | 11 |
| rtk-ai/rtk | 78 | Hot | very active | 2 | 48% | 273 |
| code-yeongyu/oh-my-openagent | 78 | Hot | very active | 1 | 82% | 225 |
| colbymchenry/codegraph | 78 | Hot | very active | 1 | 97% | 30 |
| farion1231/cc-switch | 77 | Hot | very active | 1 | 77% | 50 |
| Graphify-Labs/graphify | 77 | Hot | very active | 1 | 53% | 181 |
| anthropics/claude-code | 76 | Hot | very active | 1 | 85% | 181 |
| ruvnet/ruflo | 76 | Hot | very active | 1 | 94% | 1617 |
| Piebald-AI/claude-code-system-prompts | 76 | Rising | very active | 1 | 99% | 199 |
| MemPalace/mempalace | 76 | Hot | very active | 1 | 63% | 13 |
| Gentleman-Programming/engram | 76 | Hot | very active | 1 | 84% | 98 |
| MinishLab/semble | 76 | Hot | very active | 1 | 55% | 25 |
| DeusData/codebase-memory-mcp | 75 | Hot | very active | 1 | 97% | 37 |
| JuliusBrussee/caveman | 72 | Hot | very active | 1 | 78% | 17 |
| luongnv89/claude-howto | 70 | Hot | very active | 1 | 88% | 10 |
| traceloop/openllmetry | 70 | Mature | very active | 1 | 79% | 260 |
| anthropics/claude-cookbooks | 67 | Mature | very active | 3 | 25% | 0 |
| shanraisshan/claude-code-best-practice | 65 | Rising | very active | 1 | 96% | 0 |
| wshobson/agents | 64 | Hot | very active | 1 | 57% | 0 |
| punkpeye/awesome-mcp-servers | 64 | Hot | very active | 1 | 79% | 0 |
| hesreallyhim/awesome-claude-code | 61 | Mature | very active | 1 | 96% | 0 |
| memvid/memvid | 61 | Declining | active | 1 | 50% | 12 |
| garrytan/gstack | 58 | Hot | very active | 1 | 67% | 0 |
| centminmod/my-claude-code-setup | 55 | Mature | very active | 1 | 100% | 0 |
| x1xhlol/system-prompts-and-models-of-ai-tools | 52 | Mature | very active | 1 | 67% | 0 |
| memodb-io/Acontext | 51 | Declining | active | 0 | 0% | 279 |
| patoles/agent-flow | 51 | Mature | active | 1 | 71% | 3 |
| anthropics/skills | 45 | Rising | active | 1 | 77% | 0 |
| ComposioHQ/awesome-claude-skills | 40 | Mature | active | 1 | 50% | 0 |
| multica-ai/andrej-karpathy-skills | 26 | Declining | slowing | 0 | 0% | 0 |

## Adjacent (deliberately not listed here)

- **n8n-io/n8n** (199,728★) — workflow-automation platform — orchestrates agents but isn't a Claude-Code setup layer
- **langgenius/dify** (151,717★) — agentic-workflow platform — covered by the agent-orchestration report
- **langchain-ai/langchain** (143,646★) — agent-engineering library — app framework, not a CC setup tool
- **open-webui/open-webui** (148,174★) — chat UI for local models — a frontend, not an agent setup
- **ultraworkers/claw-code** (195,004★) — art/exhibit harness — not a practical setup layer
- **multica-ai/multica** (44,689★) — managed-agents platform — team product, see agent-orchestration report

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (claude-code / skill / agent harness / mcp / memory / token / observability / code-graph / setup) across name+description+topics, then manual curation into the nine setup layers. General agent *application* frameworks, chat UIs, and broad platforms were routed to adjacent reports or excluded (see above).
- **The three-strategy table is opinionated**, built only from repos in your stars — it is a starting point, not a benchmark. Validate model-tier and token-saver claims against your own `langfuse`/`codeburn` traces.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.

<sub>Tools covered: 59 · Snapshot: 2026-08-07T21:10:17.796Z</sub>
