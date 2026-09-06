# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 2,022 starred repos (snapshot `2026-09-06T08:24:34.321Z`), cross-referenced with the repo-similarity graph (2,022 nodes / 6,605 edges, 38 communities).
>
> Generated 2026-09-06 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

![Biggest star gains (8d)](assets/trending-now-top-tools.svg)

![Repos by movement type](assets/trending-now-categories.svg)


## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-08-29` → `2026-09-06` (**8 days**), covering the **1,854 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-09-06` (**87 days**).
  - The immediately preceding snapshot (`2026-08-31`) is only 6 days before this one — too short to separate signal from noise — so the baseline was widened to the newest snapshot at least 7 days back.
- **1,505 repos gained stars** in the recent window, adding **353,780★** between them.
- **168 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-08-29 → 2026-09-06, 8d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+14,327** | 1790.9 | 128,376 | JavaScript | Hot | very active |
| 2 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | **+13,237** | 1654.6 | 213,440 | TypeScript | Hot | very active |
| 3 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | **+7,753** | 969.1 | 43,072 | Python | Hot | very active |
| 4 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+7,356** | 919.5 | 19,219 | Python | Hot | very active |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | **+7,120** | 890.0 | 62,398 | TypeScript | Hot | very active |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **+6,511** | 813.9 | 250,276 | JavaScript | Hot | very active |
| 7 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **+4,811** | 601.4 | 242,149 | Python | Hot | very active |
| 8 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | **+4,737** | 592.1 | 61,717 | TypeScript | Hot | very active |
| 9 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **+4,367** | 545.9 | 476,094 | Python | Classic | very active |
| 10 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | **+3,932** | 491.5 | 56,299 | Python | Hot | very active |
| 11 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | **+3,916** | 489.5 | 31,871 | HTML | Hot | very active |
| 12 | [earendil-works/pi](https://github.com/earendil-works/pi) | **+3,904** | 488.0 | 102,215 | TypeScript | Hot | very active |
| 13 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **+3,770** | 471.2 | 177,012 | TypeScript | Mature | very active |
| 14 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | **+3,688** | 461.0 | 40,955 | Python | Hot | very active |
| 15 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | **+3,540** | 442.5 | 115,151 | Python | Hot | very active |
| 16 | [obra/superpowers](https://github.com/obra/superpowers) | **+3,523** | 440.4 | 282,184 | Shell | Hot | very active |
| 17 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **+3,465** | 433.1 | 120,911 | Python | Mature | very active |
| 18 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | **+3,447** | 430.9 | 114,340 | — | Declining | active |
| 19 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | **+3,404** | 425.5 | 24,470 | TypeScript | Hot | very active |
| 20 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **+3,340** | 417.5 | 125,351 | Python | Hot | very active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 8-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [MakazhanAlpamys/Soup](https://github.com/MakazhanAlpamys/Soup) | **+63%** | +2,104 | 5,447 | Fine-tune LLMs from one YAML. Layer streaming trains an 8B model on a 4 GB laptop GPU. |
| 2 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+62%** | +7,356 | 19,219 | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voic… |
| 3 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | **+36%** | +1,148 | 4,332 | Open-source AI coworkers that each get a computer of their own: a browser, files and too… |
| 4 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | **+32%** | +2,856 | 11,794 | FreeToken brings datacenter-scale model serving to your desktop. Run massive models loca… |
| 5 | [apache/maka](https://github.com/apache/maka) | **+27%** | +1,031 | 4,797 | Apache Maka (Incubating) is a high-performance agent workspace that keeps a complete rec… |
| 6 | [termio-sh/termio](https://github.com/termio-sh/termio) | **+24%** | +80 | 408 | A terminal-first agentic development environment for agentic coding. Build for CLI/TUI a… |
| 7 | [meta-llama/prompt-ops](https://github.com/meta-llama/prompt-ops) | **+24%** | +208 | 1,061 | An open-source tool for LLM prompt optimization. |
| 8 | [nvidia-isaac/video_to_data](https://github.com/nvidia-isaac/video_to_data) | **+23%** | +102 | 538 | Nvidia Isaac Video to Data Pipeline |
| 9 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | **+22%** | +7,753 | 43,072 | Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by… |
| 10 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | **+21%** | +949 | 5,418 | A general-purpose AIGC video engine: script to finished film in one pipeline — dramas, a… |
| 11 | [decodingai-magazine/building-a-coding-agent-from-scratch-course](https://github.com/decodingai-magazine/building-a-coding-agent-from-scratch-course) | **+19%** | +58 | 358 | From agent user to agent builder: build a Claude Code-style coding agent from scratch in… |
| 12 | [Anakin-Inc/anakin](https://github.com/Anakin-Inc/anakin) | **+19%** | +438 | 2,747 | Open-source web scraping API. Turn any website into clean markdown or structured JSON. A… |
| 13 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | **+17%** | +832 | 5,824 | Solution for long term memory for agent coding CLIs and to facilitate handoff between di… |
| 14 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | **+16%** | +3,404 | 24,470 | 7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behin… |
| 15 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | **+14%** | +3,916 | 31,871 | 38 editorial diagram types for Claude Code, Codex, and Pi. Self-contained HTML + SVG. No… |
| 16 | [superlinked/sie](https://github.com/superlinked/sie) | **+13%** | +379 | 3,216 | Open-source inference server and production cluster for all the models your agent needs. |
| 17 | [stablyai/orca](https://github.com/stablyai/orca) | **+13%** | +7,120 | 62,398 | Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with y… |
| 18 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+13%** | +14,327 | 128,376 | Makes your AI agent think like the laziest senior dev in the room. The best code is the … |
| 19 | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | **+12%** | +1,171 | 10,862 | Free, local tool to track AI coding token usage and cost across 37 tools and agents (Cla… |
| 20 | [trailhq/Graft](https://github.com/trailhq/Graft) | **+12%** | +605 | 5,617 | Turbocharge Claude Code, Cursor, Codex, Gemini & every coding agent: faster, cheaper, wi… |

## Sustained climbers — long run (2026-06-11 → 2026-09-06, 87d)

Averaged over the full snapshot history, so a single viral week doesn't dominate. Repos high here *and* in the recent board are compounding, not spiking.

| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |
|---|---|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | **660.3** | +57,450 | 282,184 | Shell | 79 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **588.7** | +51,216 | 242,149 | Python | 75 |
| 3 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **522.8** | +45,485 | 177,012 | TypeScript | 84 |
| 4 | [earendil-works/pi](https://github.com/earendil-works/pi) | **464.8** | +40,437 | 102,215 | TypeScript | 85 |
| 5 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | **449.1** | +39,068 | 42,385 | C | 75 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **446.5** | +38,846 | 150,299 | Shell | 58 |
| 7 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **425.1** | +36,981 | 210,461 | — | 23 |
| 8 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **423.5** | +36,842 | 250,276 | JavaScript | 79 |
| 9 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **405.0** | +35,233 | 476,094 | Python | 65 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **401.3** | +34,913 | 125,351 | Python | 97 |
| 11 | [usestrix/strix](https://github.com/usestrix/strix) | **400.6** | +34,854 | 60,800 | Python | 75 |
| 12 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **400.2** | +34,814 | 120,911 | Python | 80 |
| 13 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **376.8** | +32,779 | 131,258 | Rust | 77 |
| 14 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | **371.6** | +32,325 | 103,840 | Go | 78 |
| 15 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **363.6** | +31,637 | 204,837 | TypeScript | 88 |
| 16 | [openai/codex](https://github.com/openai/codex) | **360.7** | +31,382 | 121,840 | Rust | 89 |
| 17 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **357.0** | +31,057 | 545,486 | Markdown | 48 |
| 18 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | **355.0** | +30,886 | 94,340 | TypeScript | 87 |
| 19 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **328.0** | +28,537 | 503,418 | — | 55 |
| 20 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **313.3** | +27,255 | 178,398 | Python | 87 |

## Emerging themes

The boards above are computed; this section is interpretation. Each theme groups movers that are rising for the same underlying reason.

### Skills as the packaging format for agent behaviour

_The single loudest signal in this dataset. A year ago you configured an agent with a prompt; now behaviour ships as a versioned, installable *skill* bundle — and the repos distributing those bundles are growing faster than the agents that consume them. Note what this implies: the moat is moving from the model to the instruction layer._

- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 128,376★ · +14,327★ in 8d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 250,276★ · +6,511★ in 8d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 282,184★ · +3,523★ in 8d  
  An agentic skills framework & software development methodology that works.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 125,351★ · +3,340★ in 8d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 174,678★ · +2,595★ in 8d  
  Public repository for Agent Skills
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 210,461★ · +2,370★ in 8d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · 27,248★ · +2,263★ in 8d  
  A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 150,299★ · +1,817★ in 8d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 131,611★ · +1,548★ in 8d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 53,575★ · +478★ in 8d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 65,642★ · +380★ in 8d  
  from vibe coding to agentic engineering - practice makes claude perfect

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 115,151★ · +3,540★ in 8d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 42,385★ · +1,484★ in 8d  
  High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 69,783★ · +1,397★ in 8d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 25,983★ · +1,111★ in 8d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 12,126★ · +1,083★ in 8d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 93,309★ · +1,029★ in 8d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 81,627★ · +854★ in 8d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 16,153★ · +391★ in 8d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 30,502★ · +203★ in 8d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine.
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 6,346★ · +100★ in 8d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,486★ · +36★ in 8d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 127,199★ · +1,230★ in 8d  
  LLM inference in C/C++
- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 33,755★ · +1,062★ in 8d  
  AirLLM 70B inference with single 4GB GPU
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 26,879★ · +570★ in 8d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,358★ · +50★ in 8d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,542★ · +14★ in 8d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 53,419★ · +2,563★ in 8d  
  Use Claude Code, Codex, Pi, and OpenCode and more for free (1.3B+ free tokens) from your terminal, app, IDE, or phone like OpenClaw (voice supported + ToS friendly)
- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 103,840★ · +2,400★ in 8d  
  🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 78,990★ · +1,355★ in 8d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 69,062★ · +1,232★ in 8d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 26,879★ · +570★ in 8d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 242,149★ · +4,811★ in 8d  
  The agent that grows with you
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 102,215★ · +3,904★ in 8d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 204,837★ · +2,865★ in 8d  
  The open source coding agent.
- **[openai/codex](https://github.com/openai/codex)** · 121,840★ · +2,633★ in 8d  
  Lightweight coding agent that runs in your terminal
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 131,258★ · +1,497★ in 8d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 70,783★ · +1,215★ in 8d  
  🌊 The original agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 144,210★ · +1,008★ in 8d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 49,015★ · +999★ in 8d  
  Make humans and AI agents work as one team — open-source and self-hostable.
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 86,301★ · +985★ in 8d  
  🙌 OpenHands: AI-Driven Development
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 16,158★ · +894★ in 8d  
  Orchestrate multiple coding agents from desktop and mobile
- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 80,078★ · +564★ in 8d  
  The open-source app everyone uses to manage agents at work
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 19,189★ · +481★ in 8d  
  The most RAM efficient harness
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 81,454★ · +436★ in 8d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 68,739★ · +290★ in 8d  
  OmO: Drop your tokens. Ultrawork. Done.
- **[vercel/eve](https://github.com/vercel/eve)** · 4,985★ · +147★ in 8d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[usestrix/strix](https://github.com/usestrix/strix)** · 60,800★ · +1,928★ in 8d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 102,649★ · +1,414★ in 8d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 44,222★ · +1,342★ in 8d  
  Write HTML. Render video. Built for agents.
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 38,854★ · +1,137★ in 8d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 112,460★ · +1,005★ in 8d  
  🌐 Make websites accessible for AI agents. Automate tasks online with ease.
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 32,667★ · +770★ in 8d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 52,390★ · +740★ in 8d  
  The open-source AI voice studio. Clone, dictate, create.
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 30,401★ · +424★ in 8d  
  Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. Understand How to write meeting minutes
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 17,507★ · +98★ in 8d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.
- **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** · 70,274★ · new to the dataset  
  Open-source AI job search: scan job portals, evaluate listings into a structured A-H report with a global 1-5 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, Codex, OpenCode, Antigravity…)

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 114,340★ · +3,447★ in 8d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 125,351★ · +3,340★ in 8d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 94,340★ · +2,275★ in 8d  
  🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK.
- **[github/spec-kit](https://github.com/github/spec-kit)** · 133,643★ · +1,742★ in 8d  
  💫 Toolkit to help you get started with Spec-Driven Development

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | 70,274 | JavaScript | Hot | Open-source AI job search: scan job portals, evaluate listings into a structured A-H… |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 64,247 | JavaScript | Mature | Extracted system prompts from Anthropic - Claude Fable 5.1, Opus 5, Claude Design, C… |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 52,516 | Python | Hot | Learn it. Build it. Ship it for others. |
| [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | 49,048 | — | Mature | LEAKED SYSTEM PROMPTS FOR CHATGPT, CLAUDE, GEMINI, GROK, PERPLEXITY, CURSOR, LOVABLE… |
| [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent) | 46,787 | Python | Classic | Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, … |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 46,458 | Python | Hot | Academic Research Skills for Claude Code: research → write → review → revise → final… |
| [Hmbown/Codewhale](https://github.com/Hmbown/Codewhale) | 40,913 | Rust | Hot | Open-source coding agent for your terminal, built in Rust and on a journey of contin… |
| [TencentARC/GFPGAN](https://github.com/TencentARC/GFPGAN) | 37,668 | Python | Abandoned | GFPGAN aims at developing Practical Algorithms for Real-world Face Restoration. |
| [ItzCrazyKns/Vane](https://github.com/ItzCrazyKns/Vane) | 36,650 | TypeScript | Mature | Vane is an AI-powered answering engine. |
| [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | 32,740 | Rust | Rising | Algorithm powering the For You feed on X |
| [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 32,263 | Python | Hot | 817 structured cybersecurity skills for AI agents · Mapped to 6 frameworks: MITRE AT… |
| [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | 30,079 | C# | Hot | OfficeCLI is the first and best Office suite  purpose-built for AI agents to read, e… |
| [dmlc/xgboost](https://github.com/dmlc/xgboost) | 28,738 | C++ | Classic | Scalable, Portable and Distributed Gradient Boosting (GBDT, GBRT or GBM) Library,  f… |
| [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | 25,977 | Rust | Hot | The headless browser for AI agents and web scraping |
| [pytorch/examples](https://github.com/pytorch/examples) | 24,034 | Python | Abandoned | A set of examples around pytorch in Vision, Text, Reinforcement Learning, etc. |
| [mikeroyal/Self-Hosting-Guide](https://github.com/mikeroyal/Self-Hosting-Guide) | 22,723 | Dockerfile | Abandoned | Self-Hosting Guide. Learn all about  locally hosting (on premises & private web serv… |
| [palantir/blueprint](https://github.com/palantir/blueprint) | 22,033 | TypeScript | Classic | A React-based UI toolkit for the web |
| [t8y2/dbx](https://github.com/t8y2/dbx) | 18,102 | Rust | Hot | 20 MB lightweight cross-platform database client for 90+ databases, including MySQL,… |
| [tradecatlabs/vibe-coding-cn](https://github.com/tradecatlabs/vibe-coding-cn) | 16,097 | Python | Rising | Vibe Coding 从入门到精通教程｜AI 结对编程工作流｜Prompt、Skill、Workflow、上下文管理、codex实战指南 |
| [duixcom/Duix-Avatar](https://github.com/duixcom/Duix-Avatar) | 15,038 | C | Declining | 🚀 Truly open-source AI avatar(digital human) toolkit for offline video generation an… |
| [davisking/dlib](https://github.com/davisking/dlib) | 14,438 | C++ | Mature | A toolkit for making real world machine learning and data analysis applications in C… |
| [spotify/annoy](https://github.com/spotify/annoy) | 14,293 | C++ | Declining | Approximate Nearest Neighbors in C++/Python optimized for memory usage and loading/s… |
| [YouMind-OpenLab/awesome-nano-banana-pro-prompts](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts) | 13,373 | TypeScript | Rising | 🍌 World's largest Nano Banana Pro prompt library — 10,000+ curated prompts with prev… |
| [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | 13,008 | Python | Hot | Independent Auditing of AI Agents. Run by human or the agent itself, to answer the m… |
| [ZeroLu/awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) | 10,291 | — | Rising | 🚀 An awesome list of curated Nano Banana pro prompts and examples. Your go-to resour… |
| [fossasia/visdom](https://github.com/fossasia/visdom) | 10,289 | Python | Classic | Tool for real-time visualization, monitoring and collaborative analysis of AI/ML exp… |
| [TencentARC/PhotoMaker](https://github.com/TencentARC/PhotoMaker) | 10,087 | Jupyter Notebook | Abandoned | PhotoMaker [CVPR 2024] |
| [OpenMined/PySyft](https://github.com/OpenMined/PySyft) | 10,026 | Python | Classic | Perform data science on data that remains in someone else's server |
| [friuns2/BlackFriday-GPTs-Prompts](https://github.com/friuns2/BlackFriday-GPTs-Prompts) | 9,725 | — | Mature | List of free GPTs that doesn't require plus subscription |
| [sparkle-project/Sparkle](https://github.com/sparkle-project/Sparkle) | 9,648 | Objective-C | Classic | A software update framework for macOS |
| [advaitpaliwal/feynman](https://github.com/advaitpaliwal/feynman) | 8,871 | TypeScript | Rising | The open source AI research agent. |
| [rockbenben/ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut) | 8,738 | TypeScript | Classic | Stop writing prompts from scratch — a searchable prompt library for ChatGPT, Claude,… |
| [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | 8,561 | TypeScript | Hot | Open Source Global Intelligence Platform - Real-Time OSINT Dashboard - A Palantir Al… |
| [jamez-bondos/awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images) | 8,139 | JavaScript | Abandoned | Awesome curated collection of images and prompts generated by GPT-4o and gpt-image-1… |
| [bombshell-dev/clack](https://github.com/bombshell-dev/clack) | 8,042 | TypeScript | Classic | Effortlessly build beautiful command-line apps |
| [enquirer/enquirer](https://github.com/enquirer/enquirer) | 7,951 | JavaScript | Abandoned | Stylish, intuitive and user-friendly prompts. Used by eslint, webpack, yarn, pm2, pn… |
| [evidentlyai/evidently](https://github.com/evidentlyai/evidently) | 7,893 | Jupyter Notebook | Mature | Evidently is ​​an open-source ML and LLM observability framework. Evaluate, test, an… |
| [h2oai/h2o-3](https://github.com/h2oai/h2o-3) | 7,500 | Jupyter Notebook | Classic | H2O is an Open Source, Distributed, Fast & Scalable Machine Learning Platform: Deep … |
| [NVIDIA/warp](https://github.com/NVIDIA/warp) | 7,080 | Python | Classic | A Python framework for GPU-accelerated simulation, robotics, and machine learning. |
| [OpenWhispr/openwhispr](https://github.com/OpenWhispr/openwhispr) | 6,996 | JavaScript | Hot | Voice-to-text dictation app with local (Nvidia Parakeet/Whisper) and cloud models (B… |
| _…and 128 more_ | | | | |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 87-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [OpenZeppelin/openzeppelin-contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) | 1.1 | -0.6 | **-58%** of prior pace | 1d ago | Classic |
| [TurixAI/TuriX-CUA](https://github.com/TurixAI/TuriX-CUA) | 1.1 | -0.5 | **-45%** of prior pace | 1mo ago | Mature |
| [DevAgentForge/Open-Claude-Cowork](https://github.com/DevAgentForge/Open-Claude-Cowork) | 1.0 | -0.4 | **-36%** of prior pace | 5mo ago | Declining |
| [ValueCell-ai/valuecell](https://github.com/ValueCell-ai/valuecell) | 2.5 | -0.1 | **-5%** of prior pace | 6mo ago | Declining |
| [iternal-technologies-partners/blockify-agentic-data-optimization](https://github.com/iternal-technologies-partners/blockify-agentic-data-optimization) | 1.2 | 0.0 | **0%** of prior pace | 4mo ago | Declining |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | 1.2 | 0.0 | **0%** of prior pace | 9d ago | Declining |
| [Avaiga/taipy](https://github.com/Avaiga/taipy) | 2.3 | 0.0 | **0%** of prior pace | 27d ago | Mature |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 3.9 | 0.1 | **3%** of prior pace | 5mo ago | Declining |
| [russellromney/honker](https://github.com/russellromney/honker) | 2.2 | 0.1 | **6%** of prior pace | 1d ago | Hot |
| [hexabot-ai/Hexabot](https://github.com/hexabot-ai/Hexabot) | 2.7 | 0.2 | **9%** of prior pace | 13d ago | Mature |
| [gamosoft/NoteDiscovery](https://github.com/gamosoft/NoteDiscovery) | 2.7 | 0.2 | **9%** of prior pace | 1d ago | Hot |
| [Memento-Teams/Memento](https://github.com/Memento-Teams/Memento) | 1.3 | 0.1 | **10%** of prior pace | 11mo ago | Declining |
| [morphik-org/morphik-core](https://github.com/morphik-org/morphik-core) | 1.2 | 0.1 | **11%** of prior pace | 2d ago | Mature |
| [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | 26.3 | 3.5 | **13%** of prior pace | 1mo ago | Declining |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 146.1 | 25.4 | **17%** of prior pace | 0d ago | Classic |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **16 of the graph's 38 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 16** (12): `DietrichGebert/ponytail`, `stablyai/orca`, `affaan-m/ECC`, `diegosouzapw/OmniRoute`, `cathrynlavery/diagram-design`, `Graphify-Labs/graphify`, `VoltAgent/awesome-design-md`, `nextlevelbuilder/ui-ux-pro-max-skill`, `herdrdev/herdr`, `nexu-io/open-design`, `ayghri/i-have-adhd`, `addyosmani/agent-skills`
- **Community 4** (5): `deepseek-ai/deepseek-harness`, `public-apis/public-apis`, `sindresorhus/awesome`, `multica-ai/andrej-karpathy-skills`, `codecrafters-io/build-your-own-x`
- **Community 17** (5): `debpalash/VoiceStudio`, `MadsLorentzen/ai-job-search`, `obra/superpowers`, `harry0703/MoneyPrinterTurbo`, `tashfeenahmed/freellmapi`
- **Community 10** (2): `K-Dense-AI/scientific-agent-skills`, `JuliusBrussee/caveman`
- **Community 23** (2): `NousResearch/hermes-agent`, `guillaumemeyer/watermarks-remover`
- **Community 13** (2): `calesthio/OpenMontage`, `firecrawl/firecrawl`
- **Community 6** (2): `openai/codex`, `unclecode/crawl4ai`
- **Community 22** (2): `anthropics/skills`, `usestrix/strix`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `addyosmani/agent-skills` ⇄ `cathrynlavery/diagram-design` (w=0.375) — topics: agent-skills, claude-code, codex; authors: mvanhorn, NgoQuocViet2001
- `FlashML-org/FreeToken` ⇄ `sgl-project/sglang` (w=0.350) — topics: glm, inference, minimax, moe
- `ayghri/i-have-adhd` ⇄ `affaan-m/ECC` (w=0.221) — topics: developer-tools, productivity; authors: Souptik96
- `MadsLorentzen/ai-job-search` ⇄ `NousResearch/hermes-agent` (w=0.186) — topics: ai, ai-agents, claude-code
- `public-apis/public-apis` ⇄ `sindresorhus/awesome` (w=0.166) — topics: resources, lists; authors: AkashGowdaNC
- `ayghri/i-have-adhd` ⇄ `DietrichGebert/ponytail` (w=0.143) — topics: claude-code-plugin, developer-tools
- `deepseek-ai/deepseek-harness` ⇄ `nexu-io/open-design` (w=0.141) — topics: dsh, dsh-plugin
- `tashfeenahmed/freellmapi` ⇄ `MadsLorentzen/ai-job-search` (w=0.054) — authors: shahidbeig-a11y

**What the risers are written in** — language mix of the top 40 movers:

- **Python** — 19
- **TypeScript** — 8
- **JavaScript** — 3
- **—** — 3
- **Rust** — 2
- **HTML** — 1
- **Shell** — 1
- **Go** — 1

## Methodology & caveats

- **Source**: `data/snapshots/*.json` diffed against `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-07-27, 2026-08-07, 2026-08-11, 2026-08-28, 2026-08-29, 2026-08-31, 2026-09-06 (11 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. The recent window therefore does not always use the immediately preceding snapshot: it uses the newest one at least 7 days back, because a 1-day window amplifies noise far more than it reveals movement. Per-day normalization keeps the boards comparable across refreshes either way.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 1,854 · Window: 2026-08-29 → 2026-09-06 (8d) · Snapshot: 2026-09-06T08:24:34.321Z</sub>
