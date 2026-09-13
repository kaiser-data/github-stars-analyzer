# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 2,140 starred repos (snapshot `2026-09-12T16:25:05.965Z`), cross-referenced with the repo-similarity graph (2,140 nodes / 7,036 edges, 41 communities).
>
> Generated 2026-09-13 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

![Biggest star gains (12d)](assets/trending-now-top-tools.svg)

![Repos by movement type](assets/trending-now-categories.svg)


## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-08-31` → `2026-09-12` (**12 days**), covering the **1,894 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-09-12` (**93 days**).
  - The immediately preceding snapshot (`2026-09-07`) is only 5 days before this one — too short to separate signal from noise — so the baseline was widened to the newest snapshot at least 7 days back.
- **1,483 repos gained stars** in the recent window, adding **226,272★** between them.
- **246 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-08-31 → 2026-09-12, 12d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+10,532** | 877.7 | 128,376 | JavaScript | Hot | very active |
| 2 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | **+7,608** | 634.0 | 213,440 | TypeScript | Hot | very active |
| 3 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+6,793** | 566.1 | 19,219 | Python | Hot | very active |
| 4 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **+5,338** | 444.8 | 250,276 | JavaScript | Hot | very active |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | **+4,454** | 371.2 | 62,398 | TypeScript | Hot | very active |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **+3,400** | 283.3 | 242,149 | Python | Hot | very active |
| 7 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | **+2,898** | 241.5 | 31,871 | HTML | Hot | very active |
| 8 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | **+2,748** | 229.0 | 61,717 | TypeScript | Hot | very active |
| 9 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | **+2,733** | 227.8 | 43,072 | Python | Hot | very active |
| 10 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **+2,560** | 213.3 | 476,094 | Python | Classic | very active |
| 11 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | **+2,542** | 211.8 | 35,519 | Python | Mature | very active |
| 12 | [earendil-works/pi](https://github.com/earendil-works/pi) | **+2,406** | 200.5 | 102,215 | TypeScript | Hot | very active |
| 13 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | **+2,405** | 200.4 | 114,340 | — | Declining | active |
| 14 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **+2,374** | 197.8 | 177,012 | TypeScript | Mature | very active |
| 15 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | **+2,305** | 192.1 | 115,151 | Python | Hot | very active |
| 16 | [obra/superpowers](https://github.com/obra/superpowers) | **+2,299** | 191.6 | 282,184 | Shell | Hot | very active |
| 17 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | **+2,130** | 177.5 | 40,955 | Python | Hot | very active |
| 18 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **+2,118** | 176.5 | 204,837 | TypeScript | Hot | very active |
| 19 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **+1,968** | 164.0 | 125,351 | Python | Hot | very active |
| 20 | [anthropics/skills](https://github.com/anthropics/skills) | **+1,944** | 162.0 | 174,678 | Python | Rising | active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 12-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+55%** | +6,793 | 19,219 | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voic… |
| 2 | [MakazhanAlpamys/Soup](https://github.com/MakazhanAlpamys/Soup) | **+34%** | +1,373 | 5,447 | Fine-tune LLMs from one YAML. Layer streaming trains an 8B model on a 4 GB laptop GPU. |
| 3 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | **+21%** | +758 | 4,332 | Open-source AI coworkers that each get a computer of their own: a browser, files and too… |
| 4 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | **+14%** | +1,421 | 11,794 | FreeToken brings datacenter-scale model serving to your desktop. Run massive models loca… |
| 5 | [gridex/gridex](https://github.com/gridex/gridex) | **+13%** | +167 | 1,453 | A native macOS / windows / Linux database IDE built with Swift and AppKit. Connect to Po… |
| 6 | [superlinked/sie](https://github.com/superlinked/sie) | **+12%** | +353 | 3,216 | Open-source inference server and production cluster for all the models your agent needs. |
| 7 | [nvidia-isaac/video_to_data](https://github.com/nvidia-isaac/video_to_data) | **+12%** | +59 | 538 | Nvidia Isaac Video to Data Pipeline |
| 8 | [apache/maka](https://github.com/apache/maka) | **+12%** | +525 | 4,797 | Apache Maka (Incubating) is a high-performance agent workspace that keeps a complete rec… |
| 9 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | **+12%** | +577 | 5,418 | A general-purpose AIGC video engine: script to finished film in one pipeline — dramas, a… |
| 10 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | **+12%** | +504 | 4,755 | A single archive of public exploit PoCs and vulnerability research writeups. At the time… |
| 11 | [termio-sh/termio](https://github.com/termio-sh/termio) | **+12%** | +43 | 408 | A terminal-first agentic development environment for agentic coding. Build for CLI/TUI a… |
| 12 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | **+12%** | +668 | 6,464 | A local multi-agent harness that works with your existing Claude Code, Codex subscriptio… |
| 13 | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | **+11%** | +1,101 | 10,862 | Free, local tool to track AI coding token usage and cost across 37 tools and agents (Cla… |
| 14 | [jangles-byte/Pythia](https://github.com/jangles-byte/Pythia) | **+11%** | +103 | 1,061 | One local API call gives your agent the entire live state of the planet — every major wo… |
| 15 | [bhimrazy/receipt-ocr](https://github.com/bhimrazy/receipt-ocr) | **+11%** | +66 | 684 | An efficient OCR engine for receipt image processing. |
| 16 | [Anakin-Inc/anakin](https://github.com/Anakin-Inc/anakin) | **+10%** | +253 | 2,747 | Open-source web scraping API. Turn any website into clean markdown or structured JSON. A… |
| 17 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | **+10%** | +533 | 5,824 | Solution for long term memory for agent coding CLIs and to facilitate handoff between di… |
| 18 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | **+10%** | +2,898 | 31,871 | 38 editorial diagram types for Claude Code, Codex, and Pi. Self-contained HTML + SVG. No… |
| 19 | [decodingai-magazine/building-a-coding-agent-from-scratch-course](https://github.com/decodingai-magazine/building-a-coding-agent-from-scratch-course) | **+10%** | +32 | 358 | From agent user to agent builder: build a Claude Code-style coding agent from scratch in… |
| 20 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+9%** | +10,532 | 128,376 | Makes your AI agent think like the laziest senior dev in the room. The best code is the … |

## Sustained climbers — long run (2026-06-11 → 2026-09-12, 93d)

Averaged over the full snapshot history, so a single viral week doesn't dominate. Repos high here *and* in the recent board are compounding, not spiking.

| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |
|---|---|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | **617.7** | +57,450 | 282,184 | Shell | 78 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **550.7** | +51,216 | 242,149 | Python | 74 |
| 3 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **489.1** | +45,485 | 177,012 | TypeScript | 84 |
| 4 | [earendil-works/pi](https://github.com/earendil-works/pi) | **434.8** | +40,437 | 102,215 | TypeScript | 84 |
| 5 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | **420.1** | +39,068 | 42,385 | C | 75 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **417.7** | +38,846 | 150,299 | Shell | 58 |
| 7 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **397.6** | +36,981 | 210,461 | — | 23 |
| 8 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **396.2** | +36,842 | 250,276 | JavaScript | 79 |
| 9 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **378.8** | +35,233 | 476,094 | Python | 64 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **375.4** | +34,913 | 125,351 | Python | 96 |
| 11 | [usestrix/strix](https://github.com/usestrix/strix) | **374.8** | +34,854 | 60,800 | Python | 75 |
| 12 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **374.3** | +34,814 | 120,911 | Python | 79 |
| 13 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **352.5** | +32,779 | 131,258 | Rust | 76 |
| 14 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | **347.6** | +32,325 | 103,840 | Go | 78 |
| 15 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **340.2** | +31,637 | 204,837 | TypeScript | 88 |
| 16 | [openai/codex](https://github.com/openai/codex) | **337.4** | +31,382 | 121,840 | Rust | 89 |
| 17 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **333.9** | +31,057 | 545,486 | Markdown | 47 |
| 18 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | **332.1** | +30,886 | 94,340 | TypeScript | 87 |
| 19 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **306.8** | +28,537 | 503,418 | — | 55 |
| 20 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **293.1** | +27,255 | 178,398 | Python | 87 |

## Emerging themes

The boards above are computed; this section is interpretation. Each theme groups movers that are rising for the same underlying reason.

### Skills as the packaging format for agent behaviour

_The single loudest signal in this dataset. A year ago you configured an agent with a prompt; now behaviour ships as a versioned, installable *skill* bundle — and the repos distributing those bundles are growing faster than the agents that consume them. Note what this implies: the moat is moving from the model to the instruction layer._

- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 128,376★ · +10,532★ in 12d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 250,276★ · +5,338★ in 12d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 282,184★ · +2,299★ in 12d  
  An agentic skills framework & software development methodology that works.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 125,351★ · +1,968★ in 12d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 174,678★ · +1,944★ in 12d  
  Public repository for Agent Skills
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 210,461★ · +1,436★ in 12d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · 27,248★ · +1,309★ in 12d  
  A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 150,299★ · +1,120★ in 12d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 131,611★ · +1,070★ in 12d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 53,575★ · +303★ in 12d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 65,642★ · +225★ in 12d  
  from vibe coding to agentic engineering - practice makes claude perfect

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 115,151★ · +2,305★ in 12d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 69,783★ · +983★ in 12d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 42,385★ · +970★ in 12d  
  High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 12,126★ · +650★ in 12d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 25,983★ · +620★ in 12d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 93,309★ · +595★ in 12d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 81,627★ · +473★ in 12d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 16,153★ · +258★ in 12d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 30,502★ · +135★ in 12d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine.
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 6,346★ · +71★ in 12d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,486★ · +30★ in 12d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 127,199★ · +726★ in 12d  
  LLM inference in C/C++
- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 33,755★ · +466★ in 12d  
  AirLLM 70B inference with single 4GB GPU
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 26,879★ · +378★ in 12d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,358★ · +17★ in 12d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,542★ · +9★ in 12d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 103,840★ · +1,871★ in 12d  
  🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman
- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 53,419★ · +1,291★ in 12d  
  Use Claude Code, Codex, Pi, and OpenCode and more for free (1.3B+ free tokens) from your terminal, app, IDE, or phone like OpenClaw (voice supported + ToS friendly)
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 78,990★ · +975★ in 12d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 69,062★ · +904★ in 12d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 26,879★ · +378★ in 12d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 242,149★ · +3,400★ in 12d  
  The agent that grows with you
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 102,215★ · +2,406★ in 12d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 204,837★ · +2,118★ in 12d  
  The open source coding agent.
- **[openai/codex](https://github.com/openai/codex)** · 121,840★ · +1,488★ in 12d  
  Lightweight coding agent that runs in your terminal
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 131,258★ · +918★ in 12d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 70,783★ · +860★ in 12d  
  🌊 The original agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 144,210★ · +672★ in 12d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 49,015★ · +638★ in 12d  
  Make humans and AI agents work as one team — open-source and self-hostable.
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 86,301★ · +563★ in 12d  
  🙌 OpenHands: AI-Driven Development
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 16,158★ · +555★ in 12d  
  Orchestrate multiple coding agents from desktop and mobile
- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 80,078★ · +342★ in 12d  
  The open-source app everyone uses to manage agents at work
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 19,189★ · +325★ in 12d  
  The most RAM efficient harness
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 81,454★ · +286★ in 12d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 68,739★ · +192★ in 12d  
  OmO: Drop your tokens. Ultrawork. Done.
- **[vercel/eve](https://github.com/vercel/eve)** · 4,985★ · +103★ in 12d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[usestrix/strix](https://github.com/usestrix/strix)** · 60,800★ · +1,179★ in 12d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 44,222★ · +927★ in 12d  
  Write HTML. Render video. Built for agents.
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 38,854★ · +850★ in 12d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 102,649★ · +704★ in 12d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 112,460★ · +646★ in 12d  
  🌐 Make websites accessible for AI agents. Automate tasks online with ease.
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 32,667★ · +515★ in 12d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 52,390★ · +459★ in 12d  
  The open-source AI voice studio. Clone, dictate, create.
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 30,401★ · +263★ in 12d  
  Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. Understand How to write meeting minutes
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 17,507★ · +77★ in 12d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.
- **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** · 70,274★ · new to the dataset  
  Open-source AI job search: scan job portals, evaluate listings into a structured A-H report with a global 1-5 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, Codex, OpenCode, Antigravity…)

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 114,340★ · +2,405★ in 12d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 125,351★ · +1,968★ in 12d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 94,340★ · +1,383★ in 12d  
  🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK.
- **[github/spec-kit](https://github.com/github/spec-kit)** · 133,643★ · +1,209★ in 12d  
  💫 Toolkit to help you get started with Spec-Driven Development

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | 70,274 | JavaScript | Hot | Open-source AI job search: scan job portals, evaluate listings into a structured A-H… |
| [facebook/docusaurus](https://github.com/facebook/docusaurus) | 66,236 | TypeScript | Classic | Easy to maintain open source documentation websites. |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 64,247 | JavaScript | Mature | Extracted system prompts from Anthropic - Claude Fable 5.1, Opus 5, Claude Design, C… |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 52,516 | Python | Hot | Learn it. Build it. Ship it for others. |
| [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | 49,048 | — | Mature | LEAKED SYSTEM PROMPTS FOR CHATGPT, CLAUDE, GEMINI, GROK, PERPLEXITY, CURSOR, LOVABLE… |
| [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent) | 46,787 | Python | Classic | Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, … |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 46,458 | Python | Hot | Academic Research Skills for Claude Code: research → write → review → revise → final… |
| [Hmbown/Codewhale](https://github.com/Hmbown/Codewhale) | 40,913 | Rust | Hot | Open-source coding agent for your terminal, built in Rust and on a journey of contin… |
| [TencentARC/GFPGAN](https://github.com/TencentARC/GFPGAN) | 37,668 | Python | Abandoned | GFPGAN aims at developing Practical Algorithms for Real-world Face Restoration. |
| [ItzCrazyKns/Vane](https://github.com/ItzCrazyKns/Vane) | 36,650 | TypeScript | Mature | Vane is an AI-powered answering engine. |
| [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 32,263 | Python | Hot | 817 structured cybersecurity skills for AI agents · Mapped to 6 frameworks: MITRE AT… |
| [dmlc/xgboost](https://github.com/dmlc/xgboost) | 28,738 | C++ | Classic | Scalable, Portable and Distributed Gradient Boosting (GBDT, GBRT or GBM) Library,  f… |
| [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | 28,331 | Python | Hot | Community plugin to control Blender 3D with any LLM of your choice |
| [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | 28,064 | JavaScript | Declining | An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Ro… |
| [facebook/zstd](https://github.com/facebook/zstd) | 27,840 | C | Classic | Zstandard - Fast real-time compression algorithm |
| [Tencent/weui](https://github.com/Tencent/weui) | 27,415 | HTML | Declining | A UI library by WeChat official design team, includes the most useful widgets/module… |
| [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | 25,977 | Rust | Hot | The headless browser for AI agents and web scraping |
| [pytorch/examples](https://github.com/pytorch/examples) | 24,034 | Python | Abandoned | A set of examples around pytorch in Vision, Text, Reinforcement Learning, etc. |
| [facebook/lexical](https://github.com/facebook/lexical) | 23,847 | TypeScript | Classic | Lexical is an extensible text editor framework that provides excellent reliability, … |
| [Tencent/ncnn](https://github.com/Tencent/ncnn) | 23,806 | C++ | Classic | ncnn is a high-performance neural network inference framework optimized for the mobi… |
| [akfamily/akshare](https://github.com/akfamily/akshare) | 22,543 | Python | Classic | AKShare is an elegant and simple financial data interface library for Python, built … |
| [Atlas-OS/Atlas](https://github.com/Atlas-OS/Atlas) | 21,507 | Batchfile | Mature | 🚀 An open and lightweight modification to Windows, designed to optimize performance,… |
| [facebook/relay](https://github.com/facebook/relay) | 18,962 | Rust | Classic | Relay is a JavaScript framework for building data-driven React applications. |
| [facebook/hhvm](https://github.com/facebook/hhvm) | 18,661 | C++ | Classic | A virtual machine for executing programs written in Hack. |
| [Tencent/tinker](https://github.com/Tencent/tinker) | 17,646 | Java | Mature | Tinker is a hot-fix solution library for Android, it supports dex, library and resou… |
| [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools) | 17,544 | Rust | Hot | 🚀 通用 AI IDE 账号管理工具：支持 Antigravity / Codex / GitHub Copilot / Windsurf / Kiro / Curso… |
| [tradecatlabs/vibe-coding-cn](https://github.com/tradecatlabs/vibe-coding-cn) | 16,097 | Python | Rising | Vibe Coding 从入门到精通教程｜AI 结对编程工作流｜Prompt、Skill、Workflow、上下文管理、codex实战指南 |
| [OrcaSlicer/OrcaSlicer](https://github.com/OrcaSlicer/OrcaSlicer) | 15,676 | C++ | Classic | G-code generator for 3D printers (Bambu, Prusa, Voron, VzBot, RatRig, Creality, etc.… |
| [Tencent-Hunyuan/Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) | 14,822 | Python | Declining | High-Resolution 3D Assets Generation with Large Scale Hunyuan3D Diffusion Models. |
| [davisking/dlib](https://github.com/davisking/dlib) | 14,438 | C++ | Mature | A toolkit for making real world machine learning and data analysis applications in C… |
| [spotify/annoy](https://github.com/spotify/annoy) | 14,293 | C++ | Declining | Approximate Nearest Neighbors in C++/Python optimized for memory usage and loading/s… |
| [paperswithbacktest/awesome-systematic-trading](https://github.com/paperswithbacktest/awesome-systematic-trading) | 14,251 | Python | Classic | A curated list of awesome libraries, packages, strategies, books, blogs, tutorials f… |
| [isl-org/Open3D](https://github.com/isl-org/Open3D) | 13,956 | C++ | Classic | Open3D: A Modern Library for 3D Data Processing |
| [YouMind-OpenLab/awesome-nano-banana-pro-prompts](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts) | 13,373 | TypeScript | Rising | 🍌 World's largest Nano Banana Pro prompt library — 10,000+ curated prompts with prev… |
| [Tencent/omi](https://github.com/Tencent/omi) | 13,264 | TypeScript | Mature | Web Components Framework - Web组件框架 |
| [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | 13,008 | Python | Hot | Independent Auditing of AI Agents. Run by human or the agent itself, to answer the m… |
| [NVIDIA/cutlass](https://github.com/NVIDIA/cutlass) | 10,419 | C++ | Classic | CUDA Templates and Python DSLs for High-Performance Linear Algebra |
| [ZeroLu/awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) | 10,291 | — | Rising | 🚀 An awesome list of curated Nano Banana pro prompts and examples. Your go-to resour… |
| [fossasia/visdom](https://github.com/fossasia/visdom) | 10,289 | Python | Classic | Tool for real-time visualization, monitoring and collaborative analysis of AI/ML exp… |
| [TencentARC/PhotoMaker](https://github.com/TencentARC/PhotoMaker) | 10,087 | Jupyter Notebook | Abandoned | PhotoMaker [CVPR 2024] |
| _…and 206 more_ | | | | |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 93-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [OpenZeppelin/openzeppelin-contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) | 1.0 | -0.3 | **-33%** of prior pace | 8d ago | Classic |
| [TurixAI/TuriX-CUA](https://github.com/TurixAI/TuriX-CUA) | 1.0 | -0.2 | **-24%** of prior pace | 1mo ago | Mature |
| [Avaiga/taipy](https://github.com/Avaiga/taipy) | 2.1 | -0.3 | **-16%** of prior pace | 1mo ago | Mature |
| [morphik-org/morphik-core](https://github.com/morphik-org/morphik-core) | 1.1 | -0.2 | **-15%** of prior pace | 8d ago | Mature |
| [suno-ai/bark](https://github.com/suno-ai/bark) | 1.2 | -0.1 | **-7%** of prior pace | 2.1y ago | Abandoned |
| [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | 7.5 | -0.5 | **-7%** of prior pace | 1.0y ago | Declining |
| [russellromney/honker](https://github.com/russellromney/honker) | 2.1 | -0.1 | **-4%** of prior pace | 8d ago | Hot |
| [ValueCell-ai/valuecell](https://github.com/ValueCell-ai/valuecell) | 2.3 | -0.1 | **-4%** of prior pace | 6mo ago | Declining |
| [stevesolun/ctx](https://github.com/stevesolun/ctx) | 1.1 | 0.0 | **0%** of prior pace | 12d ago | Hot |
| [TanStack/form](https://github.com/TanStack/form) | 1.2 | 0.0 | **0%** of prior pace | 7d ago | Classic |
| [FareedKhan-dev/all-rl-algorithms](https://github.com/FareedKhan-dev/all-rl-algorithms) | 3.3 | 0.1 | **3%** of prior pace | 1.0y ago | Abandoned |
| [gamosoft/NoteDiscovery](https://github.com/gamosoft/NoteDiscovery) | 2.5 | 0.1 | **3%** of prior pace | 7d ago | Hot |
| [arman-bd/guppylm](https://github.com/arman-bd/guppylm) | 2.2 | 0.1 | **4%** of prior pace | 5mo ago | Declining |
| [openai/openai-cs-agents-demo](https://github.com/openai/openai-cs-agents-demo) | 1.8 | 0.1 | **5%** of prior pace | 8mo ago | Declining |
| [PostgREST/postgrest](https://github.com/PostgREST/postgrest) | 4.6 | 0.2 | **5%** of prior pace | 7d ago | Classic |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **16 of the graph's 41 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 13** (13): `DietrichGebert/ponytail`, `affaan-m/ECC`, `stablyai/orca`, `NousResearch/hermes-agent`, `cathrynlavery/diagram-design`, `diegosouzapw/OmniRoute`, `VoltAgent/awesome-design-md`, `Graphify-Labs/graphify`, `nextlevelbuilder/ui-ux-pro-max-skill`, `herdrdev/herdr`, `addyosmani/agent-skills`, `nexu-io/open-design`, `ayghri/i-have-adhd`
- **Community 30** (4): `deepseek-ai/deepseek-harness`, `public-apis/public-apis`, `sindresorhus/awesome`, `codecrafters-io/build-your-own-x`
- **Community 4** (3): `debpalash/VoiceStudio`, `K-Dense-AI/scientific-agent-skills`, `JuliusBrussee/caveman`
- **Community 5** (3): `firecrawl/firecrawl`, `harry0703/MoneyPrinterTurbo`, `guillaumemeyer/watermarks-remover`
- **Community 20** (3): `obra/superpowers`, `MadsLorentzen/ai-job-search`, `tashfeenahmed/freellmapi`
- **Community 26** (2): `sgl-project/sglang`, `FlashML-org/FreeToken`
- **Community 21** (2): `anthropics/skills`, `donnemartin/system-design-primer`
- **Community 9** (2): `Alishahryar1/free-claude-code`, `virgiliojr94/book-to-skill`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `addyosmani/agent-skills` ⇄ `cathrynlavery/diagram-design` (w=0.375) — topics: agent-skills, claude-code, codex; authors: mvanhorn, NgoQuocViet2001
- `FlashML-org/FreeToken` ⇄ `sgl-project/sglang` (w=0.350) — topics: glm, inference, minimax, moe
- `ayghri/i-have-adhd` ⇄ `affaan-m/ECC` (w=0.221) — topics: developer-tools, productivity; authors: Souptik96
- `MadsLorentzen/ai-job-search` ⇄ `NousResearch/hermes-agent` (w=0.186) — topics: ai, ai-agents, claude-code
- `public-apis/public-apis` ⇄ `sindresorhus/awesome` (w=0.166) — topics: resources, lists; authors: AkashGowdaNC
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
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-07-27, 2026-08-07, 2026-08-11, 2026-08-28, 2026-08-29, 2026-08-31, 2026-09-06, 2026-09-07, 2026-09-12 (13 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. The recent window therefore does not always use the immediately preceding snapshot: it uses the newest one at least 7 days back, because a 1-day window amplifies noise far more than it reveals movement. Per-day normalization keeps the boards comparable across refreshes either way.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 1,894 · Window: 2026-08-31 → 2026-09-12 (12d) · Snapshot: 2026-09-12T16:25:05.965Z</sub>
