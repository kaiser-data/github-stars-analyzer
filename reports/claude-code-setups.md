# Claude Code Superpowers — Setup Strategies from Your Stars

> Derived from **kaiser-data**'s 1,350 starred repos (snapshot `2026-07-20T08:33:57.852Z`), cross-referenced with the repo-similarity graph (1,350 nodes / 4,379 edges, 28 communities).
>
> Generated 2026-07-20 by `scripts/reports/claude_code_setups.py` (regenerate any time — no API cost).

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

- **59 Claude-Code 'superpower' projects** in your stars (**4,530,251★** combined), spanning 9 setup layers:
  - **Harness / coding agent** (12): `openclaw`, `hermes-agent`, `opencode`, `claude-code`, `gemini-cli`, `codex`, `deer-flow`, `pi`, `ruflo`, `cline`, `goose`, `oh-my-claudecode`
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
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Harness / coding agent | TypeScript | NOASSERTION | 383,533 (▲47) | Hot | 79 | very active | 0d ago | 7mo | 17 |
| [obra/superpowers](https://github.com/obra/superpowers) | Skills framework | Shell | MIT | 257,811 (▲280) | Hot | 78 | very active | 0d ago | 9mo | 3 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Skills framework | JavaScript | MIT | 231,351 (▲141) | Hot | 95 | very active | 0d ago | 6mo | 38 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Harness / coding agent | Python | MIT | 217,444 (▲218) | Hot | 85 | very active | 0d ago | 12mo | 33 |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Config / setup kit | — | — | 194,504 (▲158) | Declining | 27 | slowing | 3mo ago | 5mo | 0 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | Harness / coding agent | TypeScript | MIT | 187,641 (▲139) | Hot | 83 | very active | 0d ago | 1.2y | 17 |
| [ollama/ollama](https://github.com/ollama/ollama) | Local runtime | Go | MIT | 176,491 (▲33) | Classic | 88 | very active | 2d ago | 3.1y | 17 |
| [anthropics/skills](https://github.com/anthropics/skills) | Skills framework | Python | — | 162,818 (▲125) | Rising | 45 | active | 3d ago | 10mo | 4 |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | Config / setup kit | — | GPL-3.0 | 142,100 (▲15) | Mature | 51 | very active | 8d ago | 1.4y | 4 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Harness / coding agent | Python | — | 138,390 (▲60) | Hot | 77 | very active | 0d ago | 1.4y | 9 |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Config / setup kit | TypeScript | MIT | 123,056 (▲75) | Hot | 59 | very active | 5d ago | 4mo | 5 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Config / setup kit | Rust | MIT | 119,096 (▲158) | Hot | 76 | very active | 1d ago | 11mo | 25 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Harness / coding agent | TypeScript | Apache-2.0 | 106,079 (▲6) | Hot | 99 | very active | 0d ago | 1.3y | 29 |
| [openai/codex](https://github.com/openai/codex) | Harness / coding agent | Rust | Apache-2.0 | 99,845 (▲173) | Hot | 90 | very active | 0d ago | 1.3y | 35 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Code-graph / retrieval | Python | MIT | 91,816 (▲283) | Hot | 77 | very active | 1d ago | 3mo | 21 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP ecosystem | — | MIT | 90,979 (▲11) | Hot | 64 | very active | 7d ago | 1.6y | 4 |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Token-saver / compression | JavaScript | MIT | 90,950 (▲127) | Hot | 71 | very active | 17d ago | 3mo | 10 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | MCP ecosystem | TypeScript | NOASSERTION | 88,650 (▲11) | Hot | 75 | very active | 10d ago | 1.7y | 14 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Memory / context | JavaScript | Apache-2.0 | 87,912 (▲46) | Rising | 79 | very active | 1d ago | 10mo | 1 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Harness / coding agent | Python | MIT | 77,423 (▲32) | Hot | 84 | very active | 0d ago | 1.2y | 34 |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | Code-graph / retrieval | TypeScript | MIT | 75,253 (▲79) | Hot | 81 | very active | 1d ago | 4mo | 15 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness / coding agent | TypeScript | MIT | 72,998 (▲250) | Hot | 85 | very active | 0d ago | 11mo | 13 |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Token-saver / compression | Rust | Apache-2.0 | 71,938 (▲71) | Hot | 78 | very active | 1d ago | 5mo | 12 |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Skills framework | Python | — | 68,136 (▲30) | Rising | 62 | active | 1mo ago | 9mo | 17 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Token-saver / compression | TypeScript | NOASSERTION | 66,217 (▲44) | Hot | 78 | very active | 0d ago | 7mo | 5 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Harness / coding agent | TypeScript | MIT | 65,237 (▲46) | Hot | 76 | very active | 0d ago | 1.1y | 4 |
| [cline/cline](https://github.com/cline/cline) | Harness / coding agent | TypeScript | Apache-2.0 | 64,821 (▲7) | Mature | 78 | very active | 0d ago | 2.0y | 10 |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Config / setup kit | HTML | MIT | 63,134 (▲31) | Rising | 65 | very active | 0d ago | 8mo | 2 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Memory / context | TypeScript | Apache-2.0 | 61,274 (▲67) | Classic | 89 | very active | 0d ago | 3.1y | 39 |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | Code-graph / retrieval | TypeScript | MIT | 61,028 (▲102) | Hot | 78 | very active | 0d ago | 6mo | 4 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Token-saver / compression | Python | Apache-2.0 | 60,489 (▲208) | Hot | 92 | very active | 0d ago | 6mo | 43 |
| [upstash/context7](https://github.com/upstash/context7) | MCP ecosystem | TypeScript | MIT | 59,460 (▲28) | Hot | 84 | very active | 0d ago | 1.3y | 18 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Memory / context | Python | MIT | 57,493 (▲13) | Hot | 76 | very active | 3d ago | 3mo | 19 |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Local runtime | Python | NOASSERTION | 54,074 (▲48) | Mature | 89 | very active | 0d ago | 3.0y | 9 |
| [aaif-goose/goose](https://github.com/aaif-goose/goose) | Harness / coding agent | Rust | Apache-2.0 | 51,313 (▲18) | Hot | 99 | very active | 0d ago | 1.9y | 42 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Config / setup kit | Python | NOASSERTION | 50,460 (▲39) | Mature | 61 | very active | 0d ago | 1.2y | 2 |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Config / setup kit | Jupyter Notebook | MIT | 49,188 (▲23) | Mature | 72 | very active | 7d ago | 2.9y | 18 |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | Code-graph / retrieval | TypeScript | NOASSERTION | 44,391 (▲23) | Hot | 83 | very active | 0d ago | 11mo | 9 |
| [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | Config / setup kit | Python | MIT | 40,020 (▲27) | Hot | 72 | very active | 2d ago | 8mo | 12 |
| [wshobson/agents](https://github.com/wshobson/agents) | Skills framework | Python | MIT | 38,069 (▲9) | Hot | 65 | very active | 0d ago | 12mo | 20 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Harness / coding agent | TypeScript | MIT | 37,902 (▲5) | Hot | 80 | very active | 1d ago | 6mo | 18 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Code-graph / retrieval | C | MIT | 33,058 (▲109) | Hot | 76 | very active | 0d ago | 4mo | 9 |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Observability / evals | TypeScript | NOASSERTION | 31,458 (▲30) | Classic | 89 | very active | 0d ago | 3.2y | 14 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Skills framework | Python | MIT | 31,257 (▲38) | Hot | 78 | very active | 5d ago | 9mo | 9 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Config / setup kit | Python | MIT | 29,750 (▲16) | Hot | 80 | very active | 0d ago | 1.0y | 18 |
| [toon-format/toon](https://github.com/toon-format/toon) | Token-saver / compression | TypeScript | MIT | 24,929 (▲4) | Hot | 74 | very active | 2d ago | 9mo | 8 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Observability / evals | Python | Apache-2.0 | 20,714 (▲11) | Classic | 94 | very active | 0d ago | 3.2y | 22 |
| [memvid/memvid](https://github.com/memvid/memvid) | Memory / context | Rust | Apache-2.0 | 16,009 (▲4) | Mature | 64 | active | 6d ago | 1.1y | 2 |
| [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | Config / setup kit | JavaScript | MIT | 11,917 (▲7) | Rising | 77 | very active | 1d ago | 8mo | 2 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Observability / evals | Python | NOASSERTION | 10,634 (▲8) | Classic | 79 | very active | 0d ago | 3.7y | 11 |
| [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | Token-saver / compression | TypeScript | MIT | 8,766 (▲10) | Hot | 79 | very active | 0d ago | 3mo | 5 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Observability / evals | Python | Apache-2.0 | 7,312 (▲1) | Mature | 70 | very active | 7d ago | 2.9y | 6 |
| [MinishLab/semble](https://github.com/MinishLab/semble) | Token-saver / compression | Python | MIT | 5,654 (▲4) | Hot | 77 | very active | 3d ago | 3mo | 7 |
| [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram) | Memory / context | Go | MIT | 5,580 (▲6) | Hot | 76 | very active | 12d ago | 5mo | 6 |
| [campfirein/byterover-cli](https://github.com/campfirein/byterover-cli) | Memory / context | TypeScript | NOASSERTION | 4,925 | Hot | 82 | very active | 25d ago | 1.1y | 8 |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | Memory / context | JavaScript | Apache-2.0 | 3,583 (▲1) | Declining | 59 | active | 6d ago | 1.0y | 1 |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | Config / setup kit | Python | MIT | 2,523 (▲1) | Mature | 60 | very active | 2d ago | 1.0y | 1 |
| [patoles/agent-flow](https://github.com/patoles/agent-flow) | Observability / evals | TypeScript | Apache-2.0 | 1,309 (▲5) | Rising | 56 | active | 9d ago | 4mo | 3 |
| [ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht) | Observability / evals | Go | MIT | 89 | Hot | 80 | very active | 1d ago | 10mo | 5 |

## By layer

### Harness / coding agent

_The loop that reads, plans, edits, and runs. Pick one as your daily driver; keep a second installed to diff behavior and model-shop._

- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · 383,533★ · TypeScript · Hot  
  Cross-platform personal-assistant harness — an 'any OS, any platform' agent runtime.  
  <sub>topics: ai, assistant, own-your-data, personal, crustacean, molty, openclaw</sub>
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 217,444★ · Python · Hot  
  Long-lived 'agent that grows with you' harness — persistent, personalized agent loop.  
  <sub>topics: ai, ai-agent, ai-agents, llm, anthropic, chatgpt, claude, claude-code</sub>
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 187,641★ · TypeScript · Hot  
  Open-source terminal coding agent — a provider-agnostic alternative harness.  
  <sub>topics: —</sub>
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 138,390★ · Python · Hot  
  Claude Code itself — the agentic CLI that lives in your terminal; the baseline every setup here extends.  
  <sub>topics: —</sub>
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 106,079★ · TypeScript · Hot  
  Gemini's open-source terminal agent — the third major CLI harness; handy for model-shopping.  
  <sub>topics: gemini, gemini-api, ai, ai-agents, cli, mcp-client, mcp-server</sub>
- **[openai/codex](https://github.com/openai/codex)** · 99,845★ · Rust · Hot  
  OpenAI's lightweight terminal coding agent — useful as a second harness to diff behavior against Claude Code.  
  <sub>topics: —</sub>
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 77,423★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and writes — multi-step autonomy.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 72,998★ · TypeScript · Hot  
  Unified LLM-API + agent-loop + TUI toolkit — a kit for rolling your own coding agent.  
  <sub>topics: —</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 65,237★ · TypeScript · Hot  
  Agent meta-harness for Claude — deploys multi-agent swarms with coordination.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server</sub>
- **[cline/cline](https://github.com/cline/cline)** · 64,821★ · TypeScript · Mature  
  Autonomous coding agent as SDK / IDE extension / CLI — strong for in-editor agentic workflows.  
  <sub>topics: —</sub>
- **[aaif-goose/goose](https://github.com/aaif-goose/goose)** · 51,313★ · Rust · Hot  
  Extensible open agent that installs and runs tools, not just suggestions — MCP-native.  
  <sub>topics: mcp, acp, ai, ai-agents</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 37,902★ · TypeScript · Hot  
  Teams-first multi-agent orchestration layer for Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>

### Skills framework

_The biggest 2026 upgrade. Skills load only when triggered, so they add capability without taxing every session — the opposite of a big always-on CLAUDE.md._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 257,811★ · Shell · Hot  
  Agentic skills framework + dev methodology — the headline 'give your agent superpowers' skill collection.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 231,351★ · JavaScript · Hot  
  Agent-harness performance system bundling skills, instincts, and memory into one optimization layer.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[anthropics/skills](https://github.com/anthropics/skills)** · 162,818★ · Python · Rising  
  Anthropic's official Agent Skills repo — canonical examples of the skills format.  
  <sub>topics: agent-skills</sub>
- **[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** · 68,136★ · Python · Rising  
  Curated index of Claude Skills + tooling — the discovery hub for what's worth installing.  
  <sub>topics: claude, claude-code, agent-skills, ai-agents, antigravity, automation, codex, composio</sub>
- **[wshobson/agents](https://github.com/wshobson/agents)** · 38,069★ · Python · Hot  
  Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor) — subagents & commands.  
  <sub>topics: agents, anthropic, automation, workflows, orchestration, agent-skills, agentic-ai, ai-agents</sub>
- **[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)** · 31,257★ · Python · Hot  
  Domain skill pack that turns an agent into a research scientist — example of vertical skills.  
  <sub>topics: ai-scientist, bioinformatics, chemoinformatics, claude, claude-skills, claudecode, clinical-research, computational-biology</sub>

### Config / setup kit

_Turnkey CLAUDE.md / command / hook bundles. Steal a good one, then trim to what you actually use — bloat here is paid on every prompt._

- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 194,504★ · — · Declining  
  A single CLAUDE.md derived from Karpathy's habits — the 'one good config file' approach.  
  <sub>topics: —</sub>
- **[x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)** · 142,100★ · — · Mature  
  Leaked/collected system prompts of major AI coding tools — prompt-engineering reference.  
  <sub>topics: ai, cursor, lovable, system-prompts, v0, cursorai, devin, replit</sub>
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 123,056★ · TypeScript · Hot  
  Garry Tan's exact Claude Code setup — 23 opinionated tools as a turnkey starting point.  
  <sub>topics: —</sub>
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 119,096★ · Rust · Hot  
  Desktop all-in-one for managing Claude Code/Codex/OpenClaw — swap providers & configs fast.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, typescript, codex</sub>
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 63,134★ · HTML · Rising  
  Best-practices collection: vibe-coding → agentic engineering.  
  <sub>topics: claude-ai, claude-code, best-practices, claude, claude-code-best-practices, agentic-engineering, anthropic, claude-code-agents</sub>
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 50,460★ · Python · Mature  
  The awesome-list for Claude Code skills, hooks, slash-commands, and orchestrators.  
  <sub>topics: anthropic, anthropic-claude, awesome, awesome-list, awesome-lists, awesome-resources, claude, claude-code</sub>
- **[anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)** · 49,188★ · Jupyter Notebook · Mature  
  Official recipes/notebooks for effective Claude usage patterns.  
  <sub>topics: —</sub>
- **[luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)** · 40,020★ · Python · Hot  
  Visual, example-driven guide to Claude Code from basics to advanced — the learning path.  
  <sub>topics: claude-code, guide, tutorial</sub>
- **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** · 29,750★ · Python · Hot  
  CLI to configure AND monitor Claude Code — installs commands/agents/hooks and watches usage.  
  <sub>topics: anthropic, anthropic-claude, claude, claude-code</sub>
- **[Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts)** · 11,917★ · JavaScript · Rising  
  Claude Code's full system prompt + 27 builtin tool descriptions — know what you're configuring.  
  <sub>topics: claude-code, claude-code-system-prompts, system-prompts</sub>
- **[centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup)** · 2,523★ · Python · Mature  
  A shared starter CLAUDE.md + memory-bank configuration template you can fork.  
  <sub>topics: claude, claude-ai, claude-code, subagents, claudecode-config, claudecode-hooks, claudecode-subagents</sub>

### Memory / context

_Persist decisions and context across sessions so the agent doesn't re-derive what it already learned. The backend is swappable._

- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 87,912★ · JavaScript · Rising  
  Persistent context across sessions for every agent — captures work and re-injects it (you run this).  
  <sub>topics: ai, ai-agents, ai-memory, anthropic, artificial-intelligence, claude, claude-agent-sdk, claude-agents</sub>
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 61,274★ · TypeScript · Classic  
  Universal memory layer for AI agents — the most-adopted general memory backend.  
  <sub>topics: ai, chatgpt, llm, python, chatbots, rag, application, long-term-memory</sub>
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 57,493★ · Python · Hot  
  Best-benchmarked open-source AI memory system — drop-in long-term memory.  
  <sub>topics: ai, chromadb, llm, mcp, memory, python</sub>
- **[memvid/memvid](https://github.com/memvid/memvid)** · 16,009★ · Rust · Mature  
  Memory layer that replaces RAG pipelines with a compact server — novel storage approach.  
  <sub>topics: ai, context, embedded, faiss, knowledge-base, knowledge-graph, llm, machine-learning</sub>
- **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** · 5,580★ · Go · Hot  
  Agent-agnostic Go binary giving coding agents persistent memory.  
  <sub>topics: —</sub>
- **[campfirein/byterover-cli](https://github.com/campfirein/byterover-cli)** · 4,925★ · TypeScript · Hot  
  Portable memory layer (brv) for autonomous coding agents — agent-agnostic.  
  <sub>topics: agent, llm, mcp, memory, vibe-coding, ai, autonomous-agents, cli</sub>
- **[memodb-io/Acontext](https://github.com/memodb-io/Acontext)** · 3,583★ · JavaScript · Declining  
  Treats Agent Skills as a memory layer — skills-as-memory hybrid.  
  <sub>topics: agent, context-engineering, data-platform, self-learning, agent-development-kit, ai-agent, llm, memory</sub>

### Token-saver / compression

_Measure first (`codeburn`), then compress: leaner code search, output trimming, and a front proxy stack to 60–90% on common loops._

- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 90,950★ · JavaScript · Hot  
  'Why use many token when few token do trick' — a Claude Code skill that aggressively trims tokens.  
  <sub>topics: ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering</sub>
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 71,938★ · Rust · Hot  
  CLI proxy that cuts LLM token consumption 60–90% on common dev commands — sits in front of the agent.  
  <sub>topics: agentic-coding, ai-coding, anthropic, claude-code, cli, command-line-tool, cost-reduction, developer-tools</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 66,217★ · TypeScript · Hot  
  omo/lazycodex — a coding agent built for 'tokenmaxxers'; efficiency-first harness.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 60,489★ · Python · Hot  
  Compresses tool outputs, logs, files, and RAG chunks before they hit the model's context.  
  <sub>topics: agent, ai, anthropic, compression, context-engineering, context-window, fastapi, langchain</sub>
- **[toon-format/toon](https://github.com/toon-format/toon)** · 24,929★ · TypeScript · Hot  
  Token-Oriented Object Notation — compact schema-aware encoding to shrink structured payloads.  
  <sub>topics: data-format, llm, serialization, tokenization</sub>
- **[getagentseal/codeburn](https://github.com/getagentseal/codeburn)** · 8,766★ · TypeScript · Hot  
  TUI dashboard showing where your AI coding tokens go — measure before you optimize.  
  <sub>topics: ai-coding, claude-code, cli, codex, cost-tracking, developer-tools, observability, terminal-ui</sub>
- **[MinishLab/semble](https://github.com/MinishLab/semble)** · 5,654★ · Python · Hot  
  Fast, accurate code search for agents using ~98% fewer tokens than reading files.  
  <sub>topics: agents, code-search, embeddings, mcp, mcp-server, model-context-protocol, retrieval</sub>

### Code-graph / retrieval

_Give the agent structure instead of raw files — graphs and indexes answer 'how does X relate to Y' without scanning the repo._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 91,816★ · Python · Hot  
  Coding-assistant skill that turns a repo into a knowledge graph (you use this on this project).  
  <sub>topics: claude-code, graphrag, knowledge-graph, codex, openclaw, skills, antigravity, gemini</sub>
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 75,253★ · TypeScript · Hot  
  Turns any code into an interactive teaching graph — comprehension over impression.  
  <sub>topics: claude-code, claude-skills, understandcode, codex, codex-skills, knowledge-graph, opencode-skills, antigravity-skills</sub>
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 61,028★ · TypeScript · Hot  
  Pre-indexed code knowledge graph for Claude Code/Codex/Cursor — structural retrieval.  
  <sub>topics: —</sub>
- **[abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)** · 44,391★ · TypeScript · Hot  
  Zero-server code-intelligence engine — client-side code graph.  
  <sub>topics: —</sub>
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 33,058★ · C · Hot  
  High-performance code-intelligence MCP server — indexes codebases for retrieval.  
  <sub>topics: claude-code, code-analysis, code-intelligence, developer-tools, knowledge-graph, mcp, mcp-server, model-context-protocol</sub>

### MCP ecosystem

_External capabilities via a standard protocol. Each connected server costs context, so connect deliberately — `context7` (live docs) is the highest-ROI default._

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 90,979★ · — · Hot  
  The big community index of MCP servers — discovery for what to connect.  
  <sub>topics: ai, mcp</sub>
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 88,650★ · TypeScript · Hot  
  The official reference MCP servers — the canonical catalog of capabilities to plug in.  
  <sub>topics: —</sub>
- **[upstash/context7](https://github.com/upstash/context7)** · 59,460★ · TypeScript · Hot  
  Up-to-date library docs for LLMs via MCP — kills 'hallucinated API' errors (you have this wired).  
  <sub>topics: llm, mcp, mcp-server, vibe-coding</sub>

### Observability / evals

_You can't optimize what you can't see. Trace runs, watch spend, and score outputs before trusting an autonomous setup._

- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 31,458★ · TypeScript · Classic  
  Open-source LLM engineering platform: traces, evals, metrics, prompts (you trace Claude Code into this).  
  <sub>topics: analytics, llm, llmops, large-language-models, openai, self-hosted, ycombinator, monitoring</sub>
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 20,714★ · Python · Classic  
  Debug/evaluate/monitor LLM apps, RAG, and agents — eval-first observability.  
  <sub>topics: open-source, langchain, openai, playground, prompt-engineering, llama-index, llm, llm-evaluation</sub>
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 10,634★ · Python · Classic  
  AI observability & evaluation — OpenTelemetry-based tracing for agents.  
  <sub>topics: llmops, ai-monitoring, ai-observability, llm-eval, aiengineering, datasets, agents, llms</sub>
- **[traceloop/openllmetry](https://github.com/traceloop/openllmetry)** · 7,312★ · Python · Mature  
  Open-source OpenTelemetry-based observability for LLM apps — standards-based traces.  
  <sub>topics: llmops, observability, open-telemetry, metrics, monitoring, opentelemetry, datascience, ml</sub>
- **[patoles/agent-flow](https://github.com/patoles/agent-flow)** · 1,309★ · TypeScript · Rising  
  Real-time visualization of Claude Code agent orchestration — watch agents think, branch, coordinate.  
  <sub>topics: agent-visualization, ai-agents, claude-code, developer-tools, llm, vscode-extension</sub>
- **[ingo-eichhorst/Irrlicht](https://github.com/ingo-eichhorst/Irrlicht)** · 89★ · Go · Hot  
  Claude Code session lights in the macOS menu bar — at-a-glance session state.  
  <sub>topics: —</sub>

### Local runtime

_Run open models locally or proxy many models behind one endpoint — the cost floor for grunt work and the fallback when the cloud is down._

- **[ollama/ollama](https://github.com/ollama/ollama)** · 176,491★ · Go · Classic  
  Run open models locally with one command — point an agent at it to slash API cost or go offline.  
  <sub>topics: llama, llm, llms, go, golang, ollama, mistral, gemma</sub>
- **[BerriAI/litellm](https://github.com/BerriAI/litellm)** · 54,074★ · Python · Mature  
  OpenAI-compatible proxy/gateway to 100+ LLMs — swap models under any harness from one endpoint.  
  <sub>topics: anthropic, langchain, llm, llmops, openai, ai-gateway, azure-openai, bedrock</sub>

## Graph analysis — how they relate

**Community clustering.** These 59 tools span **17 of the graph's 28 communities** — the Claude-Code ecosystem is spread across agent-framework, memory, retrieval, and observability neighborhoods rather than forming one tidy cluster.

- **Community 1** (16): `anomalyco/opencode`, `cline/cline`, `Yeachan-Heo/oh-my-claudecode`, `affaan-m/ECC`, `ComposioHQ/awesome-claude-skills`, `wshobson/agents`, `garrytan/gstack`, `centminmod/my-claude-code-setup`, `davila7/claude-code-templates`, `thedotmack/claude-mem`, `campfirein/byterover-cli`, `JuliusBrussee/caveman`, `rtk-ai/rtk`, `getagentseal/codeburn`, `DeusData/codebase-memory-mcp`, `patoles/agent-flow`
- **Community 2** (12): `earendil-works/pi`, `ruvnet/ruflo`, `K-Dense-AI/scientific-agent-skills`, `luongnv89/claude-howto`, `hesreallyhim/awesome-claude-code`, `Piebald-AI/claude-code-system-prompts`, `code-yeongyu/oh-my-openagent`, `Graphify-Labs/graphify`, `colbymchenry/codegraph`, `Egonex-AI/Understand-Anything`, `traceloop/openllmetry`, `ingo-eichhorst/Irrlicht`
- **Community 5** (7): `aaif-goose/goose`, `x1xhlol/system-prompts-and-models-of-ai-tools`, `mem0ai/mem0`, `MemPalace/mempalace`, `memodb-io/Acontext`, `headroomlabs-ai/headroom`, `punkpeye/awesome-mcp-servers`
- **Community 11** (4): `anthropics/claude-code`, `anthropics/skills`, `multica-ai/andrej-karpathy-skills`, `anthropics/claude-cookbooks`
- **Community 10** (4): `openclaw/openclaw`, `langfuse/langfuse`, `comet-ml/opik`, `BerriAI/litellm`
- **Community 7** (2): `google-gemini/gemini-cli`, `obra/superpowers`
- **Community 9** (2): `NousResearch/hermes-agent`, `shanraisshan/claude-code-best-practice`
- **Community 22** (2): `toon-format/toon`, `ollama/ollama`
- **Community 18** (2): `MinishLab/semble`, `upstash/context7`

**Centrality (PageRank in the full 1,350-repo graph)** — the most 'hub-like' setup tools in your ecosystem:

- `patoles/agent-flow` — PageRank 0.0027
- `affaan-m/ECC` — PageRank 0.0023
- `hesreallyhim/awesome-claude-code` — PageRank 0.0020
- `MemPalace/mempalace` — PageRank 0.0015
- `punkpeye/awesome-mcp-servers` — PageRank 0.0014
- `davila7/claude-code-templates` — PageRank 0.0014
- `comet-ml/opik` — PageRank 0.0014
- `code-yeongyu/oh-my-openagent` — PageRank 0.0014
- `ComposioHQ/awesome-claude-skills` — PageRank 0.0011
- `bytedance/deer-flow` — PageRank 0.0011

**Direct links between these tools** (top similarity edges where both endpoints are in this report):

- `anthropics/skills` ⇄ `anthropics/claude-code` (w=0.717) — authors: williamqian12
- `anthropics/claude-cookbooks` ⇄ `anthropics/claude-code` (w=0.660) — authors: claude, jportner-ant
- `anthropics/claude-cookbooks` ⇄ `anthropics/skills` (w=0.595) — authors: rlancemartin
- `langfuse/langfuse` ⇄ `comet-ml/opik` (w=0.524) — topics: llm, llmops, openai, open-source
- `aaif-goose/goose` ⇄ `punkpeye/awesome-mcp-servers` (w=0.500) — topics: mcp, ai
- `patoles/agent-flow` ⇄ `affaan-m/ECC` (w=0.400) — topics: ai-agents, claude-code, developer-tools, llm
- `hesreallyhim/awesome-claude-code` ⇄ `davila7/claude-code-templates` (w=0.366) — topics: anthropic, anthropic-claude, claude, claude-code; authors: github-actions[bot]
- `hesreallyhim/awesome-claude-code` ⇄ `traceloop/openllmetry` (w=0.363) — topics: llm; authors: github-actions[bot]
- `JuliusBrussee/caveman` ⇄ `davila7/claude-code-templates` (w=0.347) — topics: anthropic, claude, claude-code; authors: github-actions[bot]
- `JuliusBrussee/caveman` ⇄ `hesreallyhim/awesome-claude-code` (w=0.342) — topics: anthropic, claude, claude-code, llm; authors: github-actions[bot]
- `affaan-m/ECC` ⇄ `davila7/claude-code-templates` (w=0.333) — topics: anthropic, claude, claude-code
- `wshobson/agents` ⇄ `ComposioHQ/awesome-claude-skills` (w=0.326) — topics: automation, agent-skills, ai-agents, cursor
- `rtk-ai/rtk` ⇄ `affaan-m/ECC` (w=0.313) — topics: anthropic, claude-code, developer-tools, llm
- `hesreallyhim/awesome-claude-code` ⇄ `K-Dense-AI/scientific-agent-skills` (w=0.309) — topics: claude, agent-skills; authors: github-actions[bot]
- `NousResearch/hermes-agent` ⇄ `code-yeongyu/oh-my-openagent` (w=0.292) — topics: ai, ai-agents, anthropic, chatgpt
- …and 17 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). This ecosystem moves fast and a lot of it is one-person projects — check before wiring one into your daily loop.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| google-gemini/gemini-cli | 99 | Hot | very active | 5 | 18% | 551 |
| aaif-goose/goose | 99 | Hot | very active | 7 | 12% | 143 |
| affaan-m/ECC | 95 | Hot | very active | 4 | 29% | 14 |
| comet-ml/opik | 94 | Classic | very active | 4 | 24% | 527 |
| headroomlabs-ai/headroom | 92 | Hot | very active | 4 | 22% | 162 |
| openai/codex | 90 | Hot | very active | 4 | 21% | 929 |
| mem0ai/mem0 | 89 | Classic | very active | 3 | 37% | 360 |
| langfuse/langfuse | 89 | Classic | very active | 3 | 30% | 624 |
| BerriAI/litellm | 89 | Mature | very active | 3 | 26% | 1409 |
| ollama/ollama | 88 | Classic | very active | 3 | 22% | 232 |
| NousResearch/hermes-agent | 85 | Hot | very active | 3 | 30% | 21 |
| earendil-works/pi | 85 | Hot | very active | 2 | 40% | 247 |
| bytedance/deer-flow | 84 | Hot | very active | 5 | 20% | 1 |
| upstash/context7 | 84 | Hot | very active | 2 | 39% | 95 |
| anomalyco/opencode | 83 | Hot | very active | 2 | 40% | 841 |
| abhigyanpatwari/GitNexus | 83 | Hot | very active | 2 | 37% | 596 |
| campfirein/byterover-cli | 82 | Hot | very active | 2 | 27% | 27 |
| Egonex-AI/Understand-Anything | 81 | Hot | very active | 2 | 49% | 8 |
| Yeachan-Heo/oh-my-claudecode | 80 | Hot | very active | 1 | 53% | 240 |
| davila7/claude-code-templates | 80 | Hot | very active | 2 | 47% | 19 |
| ingo-eichhorst/Irrlicht | 80 | Hot | very active | 1 | 51% | 38 |
| openclaw/openclaw | 79 | Hot | very active | 1 | 72% | 226 |
| thedotmack/claude-mem | 79 | Rising | very active | 1 | 100% | 297 |
| getagentseal/codeburn | 79 | Hot | very active | 1 | 80% | 45 |
| Arize-ai/phoenix | 79 | Classic | very active | 1 | 68% | 753 |
| cline/cline | 78 | Mature | very active | 1 | 59% | 326 |
| obra/superpowers | 78 | Hot | very active | 1 | 69% | 10 |
| K-Dense-AI/scientific-agent-skills | 78 | Hot | very active | 1 | 78% | 91 |
| rtk-ai/rtk | 78 | Hot | very active | 2 | 35% | 244 |
| code-yeongyu/oh-my-openagent | 78 | Hot | very active | 1 | 93% | 221 |
| colbymchenry/codegraph | 78 | Hot | very active | 1 | 90% | 29 |
| anthropics/claude-code | 77 | Hot | very active | 1 | 84% | 172 |
| Piebald-AI/claude-code-system-prompts | 77 | Rising | very active | 1 | 99% | 190 |
| MinishLab/semble | 77 | Hot | very active | 1 | 65% | 22 |
| Graphify-Labs/graphify | 77 | Hot | very active | 1 | 62% | 166 |
| ruvnet/ruflo | 76 | Hot | very active | 1 | 97% | 1583 |
| farion1231/cc-switch | 76 | Hot | very active | 1 | 70% | 46 |
| MemPalace/mempalace | 76 | Hot | very active | 1 | 53% | 13 |
| Gentleman-Programming/engram | 76 | Hot | very active | 1 | 91% | 97 |
| DeusData/codebase-memory-mcp | 76 | Hot | very active | 1 | 85% | 36 |
| modelcontextprotocol/servers | 75 | Hot | very active | 2 | 41% | 26 |
| toon-format/toon | 74 | Hot | very active | 1 | 84% | 28 |
| luongnv89/claude-howto | 72 | Hot | very active | 1 | 67% | 10 |
| anthropics/claude-cookbooks | 72 | Mature | very active | 4 | 17% | 0 |
| JuliusBrussee/caveman | 71 | Hot | very active | 1 | 78% | 16 |
| traceloop/openllmetry | 70 | Mature | very active | 1 | 75% | 260 |
| wshobson/agents | 65 | Hot | very active | 1 | 57% | 0 |
| shanraisshan/claude-code-best-practice | 65 | Rising | very active | 1 | 96% | 0 |
| memvid/memvid | 64 | Mature | active | 1 | 60% | 12 |
| punkpeye/awesome-mcp-servers | 64 | Hot | very active | 1 | 96% | 0 |
| ComposioHQ/awesome-claude-skills | 62 | Rising | active | 6 | 27% | 0 |
| hesreallyhim/awesome-claude-code | 61 | Mature | very active | 1 | 97% | 0 |
| centminmod/my-claude-code-setup | 60 | Mature | very active | 1 | 100% | 0 |
| garrytan/gstack | 59 | Hot | very active | 1 | 69% | 0 |
| memodb-io/Acontext | 59 | Declining | active | 1 | 100% | 279 |
| patoles/agent-flow | 56 | Rising | active | 1 | 67% | 3 |
| x1xhlol/system-prompts-and-models-of-ai-tools | 51 | Mature | very active | 1 | 57% | 0 |
| anthropics/skills | 45 | Rising | active | 1 | 79% | 0 |
| multica-ai/andrej-karpathy-skills | 27 | Declining | slowing | 0 | 0% | 0 |

## Adjacent (deliberately not listed here)

- **n8n-io/n8n** (197,128★) — workflow-automation platform — orchestrates agents but isn't a Claude-Code setup layer
- **langgenius/dify** (149,431★) — agentic-workflow platform — covered by the agent-orchestration report
- **langchain-ai/langchain** (142,141★) — agent-engineering library — app framework, not a CC setup tool
- **open-webui/open-webui** (146,021★) — chat UI for local models — a frontend, not an agent setup
- **ultraworkers/claw-code** (194,831★) — art/exhibit harness — not a practical setup layer
- **multica-ai/multica** (41,133★) — managed-agents platform — team product, see agent-orchestration report

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (claude-code / skill / agent harness / mcp / memory / token / observability / code-graph / setup) across name+description+topics, then manual curation into the nine setup layers. General agent *application* frameworks, chat UIs, and broad platforms were routed to adjacent reports or excluded (see above).
- **The three-strategy table is opinionated**, built only from repos in your stars — it is a starting point, not a benchmark. Validate model-tier and token-saver claims against your own `langfuse`/`codeburn` traces.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.

<sub>Tools covered: 59 · Snapshot: 2026-07-20T08:33:57.852Z</sub>
