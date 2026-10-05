# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 2,304 starred repos (snapshot `2026-10-05T13:01:39.533Z`), cross-referenced with the repo-similarity graph (2,304 nodes / 7,632 edges, 40 communities).
>
> Generated 2026-10-05 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

![Biggest star gains (7d)](assets/trending-now-top-tools.svg)

![Repos by movement type](assets/trending-now-categories.svg)


## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-09-28` → `2026-10-05` (**7 days**), covering the **2,248 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-10-05` (**116 days**).
  - The immediately preceding snapshot (`2026-09-29`) is only 6 days before this one — too short to separate signal from noise — so the baseline was widened to the newest snapshot at least 7 days back.
- **1,647 repos gained stars** in the recent window, adding **255,348★** between them.
- **56 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-09-28 → 2026-10-05, 7d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+11,755** | 1679.3 | 53,440 | Python | Rising | very active |
| 2 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+8,341** | 1191.6 | 155,543 | JavaScript | Hot | very active |
| 3 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | **+6,216** | 888.0 | 45,723 | Python | Hot | very active |
| 4 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | **+5,823** | 831.9 | 97,398 | TypeScript | Hot | very active |
| 5 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | **+5,354** | 764.9 | 243,747 | TypeScript | Hot | very active |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | **+5,207** | 743.9 | 85,423 | TypeScript | Hot | very active |
| 7 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **+4,632** | 661.7 | 273,296 | JavaScript | Hot | very active |
| 8 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | **+4,542** | 648.9 | 20,832 | Python | Hot | very active |
| 9 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | **+4,277** | 611.0 | 64,301 | Python | Hot | very active |
| 10 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | **+3,582** | 511.7 | 30,830 | Python | Hot | very active |
| 11 | [t8y2/dbx](https://github.com/t8y2/dbx) | **+3,273** | 467.6 | 24,672 | Rust | Hot | very active |
| 12 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | **+3,255** | 465.0 | 57,028 | TypeScript | Hot | very active |
| 13 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **+3,163** | 451.9 | 514,926 | — | Mature | active |
| 14 | [obra/superpowers](https://github.com/obra/superpowers) | **+3,104** | 443.4 | 295,458 | Shell | Hot | very active |
| 15 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **+3,015** | 430.7 | 188,761 | TypeScript | Mature | very active |
| 16 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | **+2,776** | 396.6 | 38,669 | Python | Hot | very active |
| 17 | [earendil-works/pi](https://github.com/earendil-works/pi) | **+2,604** | 372.0 | 112,592 | TypeScript | Hot | very active |
| 18 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | **+2,248** | 321.1 | 73,162 | TypeScript | Hot | very active |
| 19 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **+2,198** | 314.0 | 486,169 | Python | Classic | very active |
| 20 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **+2,186** | 312.3 | 140,188 | Rust | Hot | very active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 7-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [docker/skills](https://github.com/docker/skills) | **+40%** | +150 | 527 | A collection of Docker skills for AI coding agents to help them build, test, debug, and … |
| 2 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+28%** | +11,755 | 53,440 | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voic… |
| 3 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | **+28%** | +4,542 | 20,832 | Independent Auditing of AI Agents. Run by human or the agent itself, to answer the most … |
| 4 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | **+21%** | +909 | 5,184 | The Harness of Harnesses • built for RSI: a trusted, persistent, self-evolving multi-age… |
| 5 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | **+20%** | +1,071 | 6,396 | Open source inference engine for agents that optimizes itself for your exact hardware. C… |
| 6 | [decodingai-magazine/building-a-coding-agent-from-scratch-course](https://github.com/decodingai-magazine/building-a-coding-agent-from-scratch-course) | **+17%** | +85 | 571 | Free harness engineering open-source course. Build a Claude Code clone from scratch: 8 a… |
| 7 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | **+16%** | +6,216 | 45,723 | Hindsight: Agent Memory That Learns |
| 8 | [t8y2/dbx](https://github.com/t8y2/dbx) | **+15%** | +3,273 | 24,672 | 25 MB lightweight cross-platform database client for 100+ databases, including MySQL, Po… |
| 9 | [gridex/gridex](https://github.com/gridex/gridex) | **+14%** | +218 | 1,740 | A native macOS / windows / Linux database IDE built with Swift and AppKit. Connect to Po… |
| 10 | [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | **+14%** | +875 | 7,199 | A super fast Graph Database uses GraphBLAS under the hood for its sparse adjacency matri… |
| 11 | [NarratorAI-Studio/narrator-ai-cli-skill](https://github.com/NarratorAI-Studio/narrator-ai-cli-skill) | **+13%** | +353 | 3,024 | AI 解说大师 — Agent skill；封装 narrator-ai-cli 供 Claude/Codex 等工具调用 |
| 12 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | **+13%** | +3,582 | 30,830 | Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions ov… |
| 13 | [tile-ai/tilelang](https://github.com/tile-ai/tilelang) | **+12%** | +910 | 8,401 | Domain-specific language designed to streamline the development of high-performance GPU/… |
| 14 | [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | **+12%** | +916 | 8,469 | Jev-like family of decision models built on top of Qwen3.5/3.8 you can train and run on … |
| 15 | [Kruszoneq/macUSB](https://github.com/Kruszoneq/macUSB) | **+11%** | +320 | 3,142 | The all-in-one bootable USB creator for Mac |
| 16 | [nateherkai/hyperframes-student-kit](https://github.com/nateherkai/hyperframes-student-kit) | **+11%** | +115 | 1,179 | Edit videos, reels, and YouTube Shorts with Codex or Claude Code. 14 skills, transcript-… |
| 17 | [Zefan-Cai/Open-Jev](https://github.com/Zefan-Cai/Open-Jev) | **+11%** | +38 | 391 | — |
| 18 | [MakazhanAlpamys/Soup](https://github.com/MakazhanAlpamys/Soup) | **+10%** | +711 | 8,155 | Fine-tune LLMs from one YAML. Layer streaming trains an 8B model on a 4 GB laptop GPU. |
| 19 | [ApodexAI/FrontierAgent](https://github.com/ApodexAI/FrontierAgent) | **+9%** | +442 | 5,109 | 🧩 FrontierAgent, our agent framework, open-sourced alongside it — native command-line TU… |
| 20 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+9%** | +2,043 | 24,580 | A coding-agent skill for multi-phase security audits with independently verified, machin… |

## Sustained climbers — long run (2026-06-11 → 2026-10-05, 116d)

Averaged over the full snapshot history, so a single viral week doesn't dominate. Repos high here *and* in the recent board are compounding, not spiking.

| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |
|---|---|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | **609.7** | +70,724 | 295,458 | Shell | 73 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **520.5** | +60,376 | 251,309 | Python | 86 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **516.1** | +59,862 | 273,296 | JavaScript | 79 |
| 4 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **493.4** | +57,234 | 188,761 | TypeScript | 84 |
| 5 | [earendil-works/pi](https://github.com/earendil-works/pi) | **438.1** | +50,814 | 112,592 | TypeScript | 80 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **392.2** | +45,501 | 156,954 | Shell | 61 |
| 7 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **390.6** | +45,308 | 486,169 | Python | 65 |
| 8 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **374.9** | +43,487 | 216,967 | — | 21 |
| 9 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **368.2** | +42,714 | 133,152 | Python | 95 |
| 10 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | **366.3** | +42,486 | 45,803 | C | 76 |
| 11 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **365.9** | +42,448 | 128,545 | Python | 80 |
| 12 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **359.6** | +41,709 | 140,188 | Rust | 76 |
| 13 | [usestrix/strix](https://github.com/usestrix/strix) | **350.3** | +40,632 | 66,578 | Python | 75 |
| 14 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **345.2** | +40,045 | 514,926 | — | 50 |
| 15 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **332.9** | +38,616 | 211,816 | TypeScript | 88 |
| 16 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | **331.0** | +38,399 | 109,914 | Go | 79 |
| 17 | [openai/codex](https://github.com/openai/codex) | **322.8** | +37,442 | 127,900 | Rust | 84 |
| 18 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **322.5** | +37,412 | 188,555 | Python | 94 |
| 19 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **320.7** | +37,206 | 551,635 | Markdown | 38 |
| 20 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | **310.7** | +36,040 | 99,494 | TypeScript | 82 |

## Emerging themes

The boards above are computed; this section is interpretation. Each theme groups movers that are rising for the same underlying reason.

### Skills as the packaging format for agent behaviour

_The single loudest signal in this dataset. A year ago you configured an agent with a prompt; now behaviour ships as a versioned, installable *skill* bundle — and the repos distributing those bundles are growing faster than the agents that consume them. Note what this implies: the moat is moving from the model to the instruction layer._

- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 155,543★ · +8,341★ in 7d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 273,296★ · +4,632★ in 7d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 295,458★ · +3,104★ in 7d  
  An agentic skills framework & software development methodology that works.
- **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · 53,788★ · +2,042★ in 7d  
  A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 133,152★ · +2,004★ in 7d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 156,954★ · +1,949★ in 7d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 216,967★ · +1,336★ in 7d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 179,723★ · +983★ in 7d  
  Public repository for Agent Skills
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 135,288★ · +914★ in 7d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 67,107★ · +622★ in 7d  
  from vibe coding to agentic engineering - practice makes claude perfect
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 55,088★ · +352★ in 7d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 123,925★ · +1,923★ in 7d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 96,379★ · +1,560★ in 7d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 73,238★ · +991★ in 7d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 85,316★ · +876★ in 7d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 45,803★ · +567★ in 7d  
  High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 27,692★ · +293★ in 7d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 31,377★ · +267★ in 7d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory with small models for free
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 16,971★ · +142★ in 7d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 13,651★ · +130★ in 7d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 7,153★ · +78★ in 7d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,585★ · +11★ in 7d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 39,667★ · +1,606★ in 7d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 130,358★ · +600★ in 7d  
  LLM inference in C/C++
- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 35,403★ · +258★ in 7d  
  AirLLM 70B inference with single 4GB GPU
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,483★ · +20★ in 7d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,574★ · +4★ in 7d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 109,914★ · +1,774★ in 7d  
  🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 39,667★ · +1,606★ in 7d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 56,692★ · +601★ in 7d  
  Use Claude Code, Codex, VSCode, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly)
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 82,410★ · +533★ in 7d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 74,440★ · +444★ in 7d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 97,398★ · +5,823★ in 7d  
  The open-source app everyone uses to manage agents at work
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 112,592★ · +2,604★ in 7d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 140,188★ · +2,186★ in 7d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 251,309★ · +1,640★ in 7d  
  The agent that grows with you
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 211,816★ · +1,281★ in 7d  
  The open source coding agent.
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 149,465★ · +1,032★ in 7d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[openai/codex](https://github.com/openai/codex)** · 127,900★ · +995★ in 7d  
  Lightweight coding agent that runs in your terminal
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 19,571★ · +735★ in 7d  
  Orchestrate multiple coding agents from desktop and mobile
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 90,020★ · +654★ in 7d  
  🙌 OpenHands: AI-Driven Development
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 73,892★ · +471★ in 7d  
  🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 51,978★ · +441★ in 7d  
  Make humans and AI agents work as one team — open-source and self-hostable.
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 83,401★ · +262★ in 7d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 69,807★ · +190★ in 7d  
  OmO: Just type "mass ulw" keyword with your prompt. Now you are the master of graph engineering.
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 20,302★ · +118★ in 7d  
  High performance coding agent harness written in rust
- **[vercel/eve](https://github.com/vercel/eve)** · 5,457★ · +65★ in 7d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 57,028★ · +3,255★ in 7d  
  Write HTML. Render video. Built for agents.
- **[usestrix/strix](https://github.com/usestrix/strix)** · 66,578★ · +1,265★ in 7d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 109,824★ · +833★ in 7d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 117,167★ · +586★ in 7d  
  Agents that use the browser.
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 34,754★ · +557★ in 7d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** · 73,512★ · +547★ in 7d  
  Open-source AI job search agent and job finder: scan job boards, score each job 1-5 against your CV before you apply, tailor an ATS-friendly resume and cover letter, get interview prep and a job application tracker. It helps you fill in each application; you press Submit. Runs locally in your AI coding CLI (Claude Code, Codex, OpenCode and more).
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 56,404★ · +512★ in 7d  
  The open-source AI voice studio. Clone, dictate, create.
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 40,810★ · +401★ in 7d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 31,447★ · +252★ in 7d  
  Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. Understand How to write meeting minutes
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 17,798★ · +33★ in 7d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 133,152★ · +2,004★ in 7d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 119,617★ · +1,124★ in 7d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 99,494★ · +1,056★ in 7d  
  🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK.
- **[github/spec-kit](https://github.com/github/spec-kit)** · 140,186★ · +966★ in 7d  
  💫 Toolkit to help you get started with SDD or any other process!

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [openbq-org/OpenBB](https://github.com/openbq-org/OpenBB) | 73,856 | Python | Mature | Open Data Platform for analysts, quants and AI agents. |
| [codewhale-hq/Codewhale](https://github.com/codewhale-hq/Codewhale) | 41,048 | Rust | Hot | Open-source coding agent for your terminal, built in Rust and on a journey of contin… |
| [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | 40,641 | Rust | Rising | OpenHuman is the fastest, cheapest, most efficient open-source agent harness. Writte… |
| [Infisical/infisical](https://github.com/Infisical/infisical) | 29,613 | TypeScript | Classic | Infisical is the open-source platform for secrets, certificates, and privileged acce… |
| [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | 14,936 | Rust | Hot | OpenShell is the safe, private runtime for autonomous AI agents. |
| [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | 12,770 | Go | Hot | Run and supervise teams of coding agents from planning to merge. Any harness (Claude… |
| [IBM/sarama](https://github.com/IBM/sarama) | 12,522 | Go | Classic | Sarama is a Go library for Apache Kafka. |
| [IBM/plex](https://github.com/IBM/plex) | 11,672 | CSS | Mature | The package of IBM’s typeface, IBM Plex. |
| [microsoft/fast](https://github.com/microsoft/fast) | 9,674 | TypeScript | Classic | The adaptive interface system for modern web experiences. |
| [Open-Shell/Open-Shell-Menu](https://github.com/Open-Shell/Open-Shell-Menu) | 9,364 | C++ | Classic | Classic Shell Reborn. |
| [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin) | 8,451 | TypeScript | Hot | an open-source alternative to the dots, bots and muses of the world, run an office o… |
| [supabase/realtime](https://github.com/supabase/realtime) | 7,650 | Elixir | Classic | Broadcast, Presence, and Postgres Changes via WebSockets |
| [microsoft/aspire](https://github.com/microsoft/aspire) | 6,340 | C# | Classic | Aspire is the tool for code-first, extensible, observable dev and deploy. |
| [supabase/supabase-js](https://github.com/supabase/supabase-js) | 4,574 | TypeScript | Classic | An isomorphic Javascript client for Supabase. Query your Supabase database, subscrib… |
| [cs341-illinois/coursebook](https://github.com/cs341-illinois/coursebook) | 3,719 | TeX | Classic | Open Source Introductory Systems Programming Textbook for the University of Illinois |
| [NVIDIA/cuda-rust](https://github.com/NVIDIA/cuda-rust) | 3,657 | Rust | Hot | cuda-oxide is a Rust-to-CUDA compiler that lets you write (SIMT) GPU kernels in safe… |
| [MIT-LCP/mimic-code](https://github.com/MIT-LCP/mimic-code) | 3,399 | Jupyter Notebook | Classic | MIMIC Code Repository: Code shared by the research community for the MIMIC family of… |
| [rtr7/router7](https://github.com/rtr7/router7) | 2,772 | Go | Mature | router7 is a small home internet router completely written in Go. It is implemented … |
| [supabase/auth](https://github.com/supabase/auth) | 2,574 | Go | Classic | A JWT based API for managing users and issuing JWT tokens |
| [IBM/AssetOpsBench](https://github.com/IBM/AssetOpsBench) | 2,328 | Python | Hot | AssetOpsBench - Industry 4.0: A unified benchmark and framework for building, orches… |
| [littledivy/mimic](https://github.com/littledivy/mimic) | 2,318 | Python | Rising | Intercept any app, then call it from Python like a library |
| [dzhng/jevgrep](https://github.com/dzhng/jevgrep) | 2,276 | TypeScript | Hot | Find code by asking what it does. A CLI for coding agents that uses Jev to discover … |
| [garywill/linux-router](https://github.com/garywill/linux-router) | 2,057 | Shell | Mature | Set Linux as router in one command. Support Internet sharing, redsocks, Wifi hotspot… |
| [IBM/fp-go](https://github.com/IBM/fp-go) | 2,030 | Go | Classic | Functional programming library for Go 1.24+, inspired by fp-ts. Uses generic type al… |
| [IBM/mcp-cli](https://github.com/IBM/mcp-cli) | 2,025 | Python | Mature | — |
| [microsoft/waza](https://github.com/microsoft/waza) | 1,396 | Go | Hot | CLI / Framework for Agent Skills - create, test, measure and improve skill quality a… |
| [petergyang/human-review](https://github.com/petergyang/human-review) | 1,361 | JavaScript | Hot | A visual tool to edit HTML and Markdown files, leave comments like a Google Doc, and… |
| [google-research/rrsi](https://github.com/google-research/rrsi) | 1,251 | Python | Declining | — |
| [microsoft/testfx](https://github.com/microsoft/testfx) | 1,047 | C# | Classic | This repository holds the source code of Microsoft.Testing.Platform (MTP), a lightwe… |
| [getsentry/toolkit](https://github.com/getsentry/toolkit) | 912 | TypeScript | Hot | Agentic tooling for Sentry |
| [realZachi/pg-jev](https://github.com/realZachi/pg-jev) | 896 | Shell | Rising | Ask your Postgres tables questions in plain language. A PostgreSQL extension powered… |
| [angel291592/Intent-Router](https://github.com/angel291592/Intent-Router) | 839 | Python | Rising | Intent compiler for AI agents — converges vague requests into typed IntentSpec contr… |
| [XHToken/Spark-X2.5](https://github.com/XHToken/Spark-X2.5) | 632 | — | Mature | Spark-x2.5 open model series. Pushing the Limits of Agentic Capabilities in On-Devic… |
| [AbdelStark/awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev) | 562 | HTML | Hot | Awesome Jev: a source-backed field guide to TypeSafe's System One model, with SDKs, … |
| [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) | 506 | — | Hot | A curated, source-backed list of projects built with Jev, TypeSafe AI's System One m… |
| [arjunmann73/Data-Analytics-Projects](https://github.com/arjunmann73/Data-Analytics-Projects) | 451 | Jupyter Notebook | Abandoned | :mag_right: Data analysis with real world data sets using Python :mag: |
| [strands-labs/strands-decider](https://github.com/strands-labs/strands-decider) | 358 | Python | Rising | A small, fast decision model, or system one model, for agentic workflows. Pick betwe… |
| [0xethanq/astra-quant-agent](https://github.com/0xethanq/astra-quant-agent) | 345 | Python | Rising | 结合多大模型分析与确定性代码风控的自主量化交易系统 ｜ Autonomous crypto trading system with multi-LLM analysis… |
| [yologdev/yoagent](https://github.com/yologdev/yoagent) | 310 | Rust | Hot | The agent loop for Rust — stream from 7 LLM protocols, run tools, loop until done. |
| [dbarrosop/sir](https://github.com/dbarrosop/sir) | 218 | CSS | Abandoned | SDN Internet Router |
| _…and 16 more_ | | | | |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 116-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [suno-ai/bark](https://github.com/suno-ai/bark) | 1.0 | -1.1 | **-114%** of prior pace | 2.1y ago | Abandoned |
| [ValueCell-ai/valuecell](https://github.com/ValueCell-ai/valuecell) | 1.9 | -1.7 | **-89%** of prior pace | 7mo ago | Declining |
| [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | 13.6 | -10.0 | **-74%** of prior pace | 1mo ago | Mature |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 2.9 | -1.1 | **-39%** of prior pace | 6mo ago | Declining |
| [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | 3.6 | -1.3 | **-36%** of prior pace | 4mo ago | Declining |
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | 3.0 | -1.0 | **-34%** of prior pace | 7mo ago | Declining |
| [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | 3.6 | -0.9 | **-24%** of prior pace | 0d ago | Hot |
| [OAI/OpenAPI-Specification](https://github.com/OAI/OpenAPI-Specification) | 1.9 | -0.4 | **-23%** of prior pace | 1d ago | Classic |
| [microsoft/magentic-ui](https://github.com/microsoft/magentic-ui) | 1.6 | -0.3 | **-18%** of prior pace | 12d ago | Mature |
| [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | 1.0 | -0.1 | **-14%** of prior pace | 3mo ago | Declining |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | 3.4 | -0.4 | **-13%** of prior pace | 3mo ago | Declining |
| [HKUDS/AutoAgent](https://github.com/HKUDS/AutoAgent) | 3.7 | -0.4 | **-12%** of prior pace | 11mo ago | Declining |
| [OpenDCAI/DataFlow](https://github.com/OpenDCAI/DataFlow) | 29.4 | -3.1 | **-11%** of prior pace | 7d ago | Mature |
| [google-coral/coralnpu](https://github.com/google-coral/coralnpu) | 1.8 | -0.1 | **-8%** of prior pace | 3d ago | Hot |
| [meta-llama/prompt-ops](https://github.com/meta-llama/prompt-ops) | 1.9 | -0.1 | **-8%** of prior pace | 5mo ago | Declining |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **15 of the graph's 40 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 0** (13): `DietrichGebert/ponytail`, `vectorize-io/hindsight`, `affaan-m/ECC`, `ifixai-ai/iFixAi`, `firecrawl/firecrawl`, `VectifyAI/PageIndex`, `diegosouzapw/OmniRoute`, `ayghri/i-have-adhd`, `harry0703/MoneyPrinterTurbo`, `msitarzewski/agency-agents`, `NousResearch/hermes-agent`, `thedotmack/claude-mem`, `D4Vinci/Scrapling`
- **Community 5** (5): `stablyai/orca`, `rohitg00/ai-engineering-from-scratch`, `sindresorhus/awesome`, `public-apis/public-apis`, `addyosmani/agent-skills`
- **Community 7** (4): `paperclipai/paperclip`, `NandhaKishorM/laya`, `OpenCut-app/OpenCut`, `tashfeenahmed/freellmapi`
- **Community 6** (4): `farion1231/cc-switch`, `Graphify-Labs/graphify`, `JuliusBrussee/caveman`, `awesome-selfhosted/awesome-selfhosted`
- **Community 21** (3): `cloudflare/security-audit-skill`, `calesthio/OpenMontage`, `rocketride-org/rocketride-server`
- **Community 13** (2): `earendil-works/pi`, `nextlevelbuilder/ui-ux-pro-max-skill`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `vectorize-io/hindsight` ⇄ `harry0703/MoneyPrinterTurbo` (w=0.300) — authors: rudycelekli, FenjuFu
- `ifixai-ai/iFixAi` ⇄ `harry0703/MoneyPrinterTurbo` (w=0.280) — topics: python; authors: rudycelekli, Thibaultjaigu
- `vectorize-io/hindsight` ⇄ `thedotmack/claude-mem` (w=0.254) — topics: ai-memory; authors: rudycelekli, FenjuFu
- `ayghri/i-have-adhd` ⇄ `thedotmack/claude-mem` (w=0.201) — topics: claude-code-plugin, claude-skills; authors: wakqasahmed, FenjuFu
- `vectorize-io/hindsight` ⇄ `msitarzewski/agency-agents` (w=0.200) — authors: rudycelekli
- `ayghri/i-have-adhd` ⇄ `affaan-m/ECC` (w=0.167) — topics: developer-tools, productivity
- `msitarzewski/agency-agents` ⇄ `harry0703/MoneyPrinterTurbo` (w=0.167) — authors: rudycelekli
- `public-apis/public-apis` ⇄ `sindresorhus/awesome` (w=0.125) — topics: resources, lists

**What the risers are written in** — language mix of the top 40 movers:

- **Python** — 16
- **TypeScript** — 10
- **JavaScript** — 4
- **Rust** — 3
- **—** — 2
- **Shell** — 2
- **Go** — 2
- **C** — 1

## Methodology & caveats

- **Source**: `data/snapshots/*.json` diffed against `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-07-27, 2026-08-07, 2026-08-11, 2026-08-28, 2026-08-29, 2026-08-31, 2026-09-06, 2026-09-07, 2026-09-12, 2026-09-14, 2026-09-21, 2026-09-25, 2026-09-28, 2026-09-29, 2026-10-05 (19 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. The recent window therefore does not always use the immediately preceding snapshot: it uses the newest one at least 7 days back, because a 1-day window amplifies noise far more than it reveals movement. Per-day normalization keeps the boards comparable across refreshes either way.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 2,248 · Window: 2026-09-28 → 2026-10-05 (7d) · Snapshot: 2026-10-05T13:01:39.533Z</sub>
