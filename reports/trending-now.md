# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 2,398 starred repos (snapshot `2026-10-19T11:27:31.266Z`), cross-referenced with the repo-similarity graph (2,398 nodes / 8,025 edges, 39 communities).
>
> Generated 2026-10-19 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

![Biggest star gains (8d)](assets/trending-now-top-tools.svg)

![Repos by movement type](assets/trending-now-categories.svg)


## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-10-11` → `2026-10-19` (**8 days**), covering the **2,358 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-10-19` (**130 days**).
- **1,840 repos gained stars** in the recent window, adding **722,456★** between them.
- **40 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-10-11 → 2026-10-19, 8d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | **+266,257** | 33282.1 | 329,615 | TypeScript | Hot | very active |
| 2 | [storytold/photocraft](https://github.com/storytold/photocraft) | **+23,030** | 2878.8 | 67,962 | Rust | Hot | very active |
| 3 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+19,678** | 2459.8 | 76,580 | Python | Hot | very active |
| 4 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | **+9,545** | 1193.1 | 55,081 | Python | Hot | very active |
| 5 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | **+9,502** | 1187.8 | 58,076 | HTML | Hot | very active |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | **+8,444** | 1055.5 | 97,438 | TypeScript | Hot | very active |
| 7 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | **+7,365** | 920.6 | 16,082 | Rust | Hot | very active |
| 8 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **+7,323** | 915.4 | 283,616 | JavaScript | Hot | very active |
| 9 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+7,303** | 912.9 | 167,493 | JavaScript | Hot | very active |
| 10 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | **+7,170** | 896.2 | 254,009 | TypeScript | Hot | very active |
| 11 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | **+7,015** | 876.9 | 67,186 | TypeScript | Hot | very active |
| 12 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | **+6,432** | 804.0 | 29,798 | Python | Hot | very active |
| 13 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | **+5,614** | 701.8 | 14,948 | Rust | Hot | very active |
| 14 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | **+5,423** | 677.9 | 43,036 | Python | Rising | very active |
| 15 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | **+5,276** | 659.5 | 13,777 | Rust | Hot | very active |
| 16 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | **+4,891** | 611.4 | 104,413 | TypeScript | Hot | very active |
| 17 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | **+4,811** | 601.4 | 30,914 | TypeScript | Rising | very active |
| 18 | [obra/superpowers](https://github.com/obra/superpowers) | **+4,741** | 592.6 | 301,862 | Shell | Hot | very active |
| 19 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | **+4,706** | 588.2 | 71,235 | Python | Hot | very active |
| 20 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **+4,638** | 579.8 | 217,135 | TypeScript | Hot | very active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 8-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | **+420%** | +266,257 | 329,615 | Reverse engineer anything with agents, from app behavior down to native binaries. |
| 2 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | **+84%** | +7,365 | 16,082 | PdfCraft: An open-source PDF reader and editor written by scratch in pure Rust |
| 3 | [storytold/artcraft-services](https://github.com/storytold/artcraft-services) | **+77%** | +531 | 1,222 | backend, web frontend, etc. |
| 4 | [storytold/artcraftx](https://github.com/storytold/artcraftx) | **+70%** | +393 | 953 | ArtCraft-X |
| 5 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | **+62%** | +5,276 | 13,777 | LightCraft: An open-source non-destructive photo editor written by scratch in pure Rust |
| 6 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | **+60%** | +5,614 | 14,948 | FilmCraft: An open-source, nonlinear video editor written by scratch in pure Rust |
| 7 | [storytold/photocraft](https://github.com/storytold/photocraft) | **+51%** | +23,030 | 67,962 | PhotoCraft: An open-source, photo editor written by scratch in pure Rust |
| 8 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+35%** | +19,678 | 76,580 | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voic… |
| 9 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | **+28%** | +6,432 | 29,798 | Independent Auditing of AI Agents. Run by human or the agent itself, to answer the most … |
| 10 | [strands-labs/strands-decider](https://github.com/strands-labs/strands-decider) | **+21%** | +118 | 670 | A small, fast decision model, or system one model, for agentic workflows. Pick between o… |
| 11 | [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | **+21%** | +1,826 | 10,497 | A super fast Graph Database uses GraphBLAS under the hood for its sparse adjacency matri… |
| 12 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | **+21%** | +9,545 | 55,081 | The job search that runs on your machine. AI job application framework built on Claude C… |
| 13 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | **+20%** | +9,502 | 58,076 | Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, … |
| 14 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | **+19%** | +1,717 | 10,819 | Solution for long term memory for agent coding CLIs and to facilitate handoff between di… |
| 15 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | **+18%** | +4,811 | 30,914 | Context window optimization for AI coding agents. Sandboxes tool output (98% reduction),… |
| 16 | [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) | **+17%** | +798 | 5,555 | A tiny friend in your Mac's notch and on your iPhone that keeps an eye on your AI coding… |
| 17 | [Prism-Shadow/penguin-harness](https://github.com/Prism-Shadow/penguin-harness) | **+15%** | +381 | 2,855 | 🐧 Unified and Stable RSI Platform |
| 18 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+15%** | +4,103 | 31,370 | A coding-agent skill for multi-phase security audits with independently verified, machin… |
| 19 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | **+14%** | +5,423 | 43,036 | Official, Anthropic-managed directory of high quality Claude Code Plugins. |
| 20 | [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | **+14%** | +243 | 1,979 | — |

## Sustained climbers — long run (2026-06-11 → 2026-10-19, 130d)

Averaged over the full snapshot history, so a single viral week doesn't dominate. Repos high here *and* in the recent board are compounding, not spiking.

| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |
|---|---|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | **593.3** | +77,128 | 301,862 | Shell | 73 |
| 2 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **539.9** | +70,182 | 283,616 | JavaScript | 79 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **493.6** | +64,169 | 255,102 | Python | 75 |
| 4 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **472.3** | +61,403 | 192,930 | TypeScript | 83 |
| 5 | [earendil-works/pi](https://github.com/earendil-works/pi) | **419.6** | +54,546 | 116,324 | TypeScript | 85 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **384.4** | +49,969 | 161,422 | Shell | 61 |
| 7 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **380.3** | +49,435 | 490,296 | Python | 64 |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **367.0** | +47,712 | 146,191 | Rust | 78 |
| 9 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **366.2** | +47,605 | 221,085 | — | 20 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **361.5** | +47,001 | 137,439 | Python | 95 |
| 11 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **360.8** | +46,907 | 133,004 | Python | 80 |
| 12 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **356.4** | +46,327 | 521,208 | — | 49 |
| 13 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **338.0** | +43,935 | 217,135 | TypeScript | 89 |
| 14 | [usestrix/strix](https://github.com/usestrix/strix) | **337.4** | +43,862 | 69,808 | Python | 75 |
| 15 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | **335.3** | +43,585 | 46,902 | C | 76 |
| 16 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | **323.5** | +42,054 | 113,569 | Go | 79 |
| 17 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | **310.6** | +40,373 | 67,186 | TypeScript | 78 |
| 18 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **308.1** | +40,052 | 554,481 | Markdown | 29 |
| 19 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **306.8** | +39,884 | 191,027 | Python | 93 |
| 20 | [openai/codex](https://github.com/openai/codex) | **303.2** | +39,421 | 129,879 | Rust | 94 |

## Emerging themes

The boards above are computed; this section is interpretation. Each theme groups movers that are rising for the same underlying reason.

### Skills as the packaging format for agent behaviour

_The single loudest signal in this dataset. A year ago you configured an agent with a prompt; now behaviour ships as a versioned, installable *skill* bundle — and the repos distributing those bundles are growing faster than the agents that consume them. Note what this implies: the moat is moving from the model to the instruction layer._

- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 283,616★ · +7,323★ in 8d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 167,493★ · +7,303★ in 8d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 301,862★ · +4,741★ in 8d  
  An agentic skills framework & software development methodology that works.
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 221,085★ · +3,137★ in 8d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 137,439★ · +3,028★ in 8d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 161,422★ · +2,763★ in 8d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 182,118★ · +1,827★ in 8d  
  Public repository for Agent Skills
- **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · 57,774★ · +1,527★ in 8d  
  A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 136,903★ · +1,102★ in 8d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 55,993★ · +638★ in 8d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC (no affiliation). A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 67,733★ · +393★ in 8d  
  from vibe coding to agentic engineering - practice makes claude perfect

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 128,724★ · +3,533★ in 8d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 101,710★ · +2,574★ in 8d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 29,614★ · +1,727★ in 8d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 86,940★ · +1,116★ in 8d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 74,420★ · +761★ in 8d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 46,902★ · +619★ in 8d  
  High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 162 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 32,530★ · +582★ in 8d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory with small models for free
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 7,851★ · +422★ in 8d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 14,133★ · +232★ in 8d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 17,267★ · +206★ in 8d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,625★ · +28★ in 8d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 39,411★ · +3,781★ in 8d  
  AirLLM 2.8T LLM inference with single 4GB GPU
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 42,810★ · +1,872★ in 8d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 131,681★ · +947★ in 8d  
  LLM inference in C/C++
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,525★ · +33★ in 8d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,592★ · +14★ in 8d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 61,743★ · +4,482★ in 8d  
  Use Claude Code, Codex, VSCode, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly)
- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 113,569★ · +2,692★ in 8d  
  🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 42,810★ · +1,872★ in 8d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 83,933★ · +1,096★ in 8d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 75,959★ · +1,073★ in 8d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 104,413★ · +4,891★ in 8d  
  The open-source app everyone uses to manage agents at work
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 217,135★ · +4,638★ in 8d  
  The open source coding agent.
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 146,191★ · +3,828★ in 8d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 255,102★ · +2,649★ in 8d  
  The agent that grows with you
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 76,828★ · +2,576★ in 8d  
  🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 152,343★ · +2,337★ in 8d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 116,324★ · +2,284★ in 8d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[openai/codex](https://github.com/openai/codex)** · 129,879★ · +1,363★ in 8d  
  Lightweight coding agent that runs in your terminal
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 21,384★ · +1,008★ in 8d  
  Orchestrate multiple coding agents from desktop and mobile
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 53,195★ · +799★ in 8d  
  Make humans and AI agents work as one team — open-source and self-hostable.
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 91,252★ · +769★ in 8d  
  🙌 OpenHands: AI-Driven Development
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 21,025★ · +647★ in 8d  
  High performance coding agent harness written in Rust, built for heavy multi-agent dev workflows
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 84,120★ · +474★ in 8d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 70,181★ · +244★ in 8d  
  OmO: Just type "mass ulw" keyword with your prompt. Now you are the master of graph engineering.
- **[vercel/eve](https://github.com/vercel/eve)** · 5,615★ · +102★ in 8d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 67,186★ · +7,015★ in 8d  
  Write HTML. Render video. Built for agents.
- **[usestrix/strix](https://github.com/usestrix/strix)** · 69,808★ · +2,099★ in 8d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** · 75,574★ · +1,621★ in 8d  
  Open-source AI job search agent and job finder: scan job boards, score each job 1-5 against your CV before you apply, tailor an ATS-friendly resume and cover letter, get interview prep and a job application tracker. It helps you fill in each application; you press Submit. Runs locally in your AI coding CLI (Claude Code, Codex, OpenCode and more).
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 112,007★ · +1,536★ in 8d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 57,985★ · +1,192★ in 8d  
  The open-source AI voice studio. Clone, dictate, create.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 118,472★ · +948★ in 8d  
  Open-source Python library for AI browser agents, plus Browser Use Cloud: stealth browsers and a hosted agent API.
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 35,882★ · +762★ in 8d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 41,723★ · +642★ in 8d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 31,926★ · +346★ in 8d  
  Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. Understand How to write meeting minutes
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 17,901★ · +66★ in 8d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 137,439★ · +3,028★ in 8d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 122,208★ · +2,071★ in 8d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 102,383★ · +2,032★ in 8d  
  The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create motion, prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.
- **[github/spec-kit](https://github.com/github/spec-kit)** · 141,882★ · +1,201★ in 8d  
  💫 Toolkit to help you get started with SDD or any other process!

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [lobehub/lobehub](https://github.com/lobehub/lobehub) | 83,319 | TypeScript | Classic | 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations … |
| [Niko1221/Strata](https://github.com/Niko1221/Strata) | 27,808 | C++ | Hot | Qwen3.8-Flash-Next on any consumer hardware: one-click install for Windows / Linux. … |
| [serengil/deepface](https://github.com/serengil/deepface) | 23,570 | Python | Classic | A Lightweight Face Recognition and Facial Attribute Analysis (Age, Gender, Emotion a… |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 20,778 | TypeScript | Hot | LLM Wiki is a cross-platform desktop application that turns your documents into an o… |
| [web-infra-dev/midscene](https://github.com/web-infra-dev/midscene) | 15,321 | TypeScript | Mature | See interfaces like a human. E2E testing in natural language. |
| [naklecha/llama3-from-scratch](https://github.com/naklecha/llama3-from-scratch) | 15,205 | Jupyter Notebook | Abandoned | llama3 implementation one matrix multiplication at a time |
| [tester-army/e2e](https://github.com/tester-army/e2e) | 11,302 | TypeScript | Hot | Next generation e2e testing framework for web and mobile apps. |
| [baptisteArno/typebot.io](https://github.com/baptisteArno/typebot.io) | 10,556 | TypeScript | Classic | 💬 Typebot is a powerful chatbot builder that you can self-host. |
| [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code) | 10,426 | TypeScript | Hot | Turbocharge Claude Code, Cursor, Codex, Gemini & every coding agent: faster, cheaper… |
| [stefanprodan/podinfo](https://github.com/stefanprodan/podinfo) | 6,022 | Go | Classic | Go microservice template for Kubernetes |
| [antiwork/shortest](https://github.com/antiwork/shortest) | 5,691 | TypeScript | Mature | QA via natural language AI tests |
| [callstack/agent-device](https://github.com/callstack/agent-device) | 5,074 | TypeScript | Hot | Mobile app automation and verification for AI coding agents. CLI, MCP server, and ty… |
| [TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli) | 4,782 | TypeScript | Hot | Official TestSprite CLI — AI-powered automated testing from your terminal |
| [hardkoded/puppeteer-sharp](https://github.com/hardkoded/puppeteer-sharp) | 3,928 | C# | Classic | Headless Chrome .NET API |
| [Contrastive-LM/CLM](https://github.com/Contrastive-LM/CLM) | 3,072 | Python | Mature | Contrastive Language Models (CLMs) are a new class of System One model trained with … |
| [symfony/panther](https://github.com/symfony/panther) | 3,069 | PHP | Mature | A browser testing and web crawling library for PHP and Symfony |
| [Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki) | 2,529 | Python | Rising | Agent Skills-compatible LLM wiki for Claude Code, Cursor, and Codex. Build a Karpath… |
| [mike4192/spotMicro](https://github.com/mike4192/spotMicro) | 2,156 | C++ | Abandoned | Spot Micro Quadruped Project |
| [nateherkai/herk-edit-kit](https://github.com/nateherkai/herk-edit-kit) | 1,828 | HTML | Rising | Herk Edit Kit by Nate Herk: edit videos, reels, and YouTube Shorts with Codex or Cla… |
| [HelixDB/helix-foundry](https://github.com/HelixDB/helix-foundry) | 1,616 | TypeScript | Hot | Your company's data, connected into one ontology, on your own computer. A local-firs… |
| [nvk/llm-wiki](https://github.com/nvk/llm-wiki) | 1,435 | Python | Hot | LLM-compiled knowledge bases for any AI agent. Parallel multi-agent research, thesis… |
| [mozilla-ai/otari](https://github.com/mozilla-ai/otari) | 681 | Python | Hot | Open-source, OpenAI-compatible LLM gateway you run yourself. One endpoint for 40+ pr… |
| [ibrahimqureshae/mdflux](https://github.com/ibrahimqureshae/mdflux) | 567 | Python | Mature | Turn any document into clean, AI-ready Markdown. Local-first desktop app: reads scan… |
| [nebius/soperator](https://github.com/nebius/soperator) | 451 | Go | Mature | Run Slurm in Kubernetes |
| [zengyh1900/3D-Human-Body-Shape](https://github.com/zengyh1900/3D-Human-Body-Shape) | 397 | Python | Abandoned | [ICIMCS'2017] Official Code for 3D Human Body Reshaping with Anthropometric Modeling |
| [Graphicle-AI/graphicle](https://github.com/Graphicle-AI/graphicle) | 307 | Rust | Rising | Code graph and memory for your coding agents, in one Rust program. For Claude Code, … |
| [NandhaKishorM/vegaml](https://github.com/NandhaKishorM/vegaml) | 274 | Python | Hot | Typed decisions from a frozen language model and a small physics engine: calibrated … |
| [nebius/token-factory-cookbook](https://github.com/nebius/token-factory-cookbook) | 270 | Jupyter Notebook | Hot | — |
| [JNavas2/Archive-Page](https://github.com/JNavas2/Archive-Page) | 183 | JavaScript | Mature | Browser extension to archive webpages in Archive Today |
| [nebius/kvax](https://github.com/nebius/kvax) | 177 | Python | Declining | A FlashAttention implementation for JAX with support for efficient document mask com… |
| [vinilana/jev-eval-agent](https://github.com/vinilana/jev-eval-agent) | 109 | HTML | Rising | — |
| [btahir/reelbird](https://github.com/btahir/reelbird) | 40 | Swift | Rising | Free, open-source screen recorder for macOS. A share link the moment you stop, then … |
| [tuvovan/RFDNet-ImageSuperResolution](https://github.com/tuvovan/RFDNet-ImageSuperResolution) | 37 | Python | Abandoned | Keras Implementation of the paper Residual Feature Distillation Network for Lightwei… |
| [google-parfait/dpsynth](https://github.com/google-parfait/dpsynth) | 33 | Python | Hot | — |
| [eth-cscs/cscs-key](https://github.com/eth-cscs/cscs-key) | 11 | Rust | Rising | — |
| [AstraBert/statembed](https://github.com/AstraBert/statembed) | 11 | Rust | Rising | Fast, lightweight static text embeddings for Rust and Python |
| [kaiser-data/free-llm-proxy-router](https://github.com/kaiser-data/free-llm-proxy-router) | 10 | Go | Mature | One small Go binary that turns every free LLM tier (Groq, Gemini, OpenRouter, Cerebr… |
| [GlebBerjoskin/gtc_berlin_workshop](https://github.com/GlebBerjoskin/gtc_berlin_workshop) | 8 | Python | Mature | — |
| [tschechlovdev/watch-party-building-ai-agents](https://github.com/tschechlovdev/watch-party-building-ai-agents) | 4 | Python | Rising | Watch Party: Building AI Agents – Todo App Demo (FastAPI + React) |
| [kaiser-data/github-stars-analyzer](https://github.com/kaiser-data/github-stars-analyzer) | 2 | HTML | Mature | — |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 130-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [axios/axios](https://github.com/axios/axios) | 1.7 | -5.8 | **-334%** of prior pace | 0d ago | Classic |
| [libgdx/libgdx](https://github.com/libgdx/libgdx) | 2.4 | -2.5 | **-103%** of prior pace | 5d ago | Classic |
| [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | 9.8 | -9.2 | **-95%** of prior pace | 0d ago | Hot |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 2.4 | -1.8 | **-72%** of prior pace | 6mo ago | Declining |
| [hashicorp/consul](https://github.com/hashicorp/consul) | 1.2 | -0.6 | **-51%** of prior pace | 0d ago | Classic |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | 3.1 | -0.9 | **-28%** of prior pace | 3mo ago | Declining |
| [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) | 4.0 | -0.8 | **-19%** of prior pace | 1.2y ago | Abandoned |
| [deeplethe/forkd](https://github.com/deeplethe/forkd) | 5.8 | -0.8 | **-13%** of prior pace | 1mo ago | Hot |
| [NVIDIA/NeMo-Agent-Toolkit](https://github.com/NVIDIA/NeMo-Agent-Toolkit) | 2.0 | -0.2 | **-13%** of prior pace | 1d ago | Hot |
| [SuperClaude-Org/SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) | 4.9 | -0.5 | **-10%** of prior pace | 22d ago | Declining |
| [AndyMik90/Aperant](https://github.com/AndyMik90/Aperant) | 1.8 | -0.1 | **-7%** of prior pace | 4mo ago | Declining |
| [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | 3.2 | 0.0 | **0%** of prior pace | 4mo ago | Declining |
| [lochie/web-haptics](https://github.com/lochie/web-haptics) | 1.3 | 0.0 | **0%** of prior pace | 1mo ago | Declining |
| [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | 6.1 | 0.0 | **0%** of prior pace | 3d ago | Classic |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | 14.5 | 0.1 | **1%** of prior pace | 16d ago | Mature |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **14 of the graph's 39 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 3** (12): `debpalash/VoiceStudio`, `cathrynlavery/diagram-design`, `affaan-m/ECC`, `DietrichGebert/ponytail`, `heygen-com/hyperframes`, `ifixai-ai/iFixAi`, `rohitg00/ai-engineering-from-scratch`, `addyosmani/agent-skills`, `Graphify-Labs/graphify`, `diegosouzapw/OmniRoute`, `nextlevelbuilder/ui-ux-pro-max-skill`, `msitarzewski/agency-agents`
- **Community 2** (4): `morluto/rea`, `anthropics/claude-plugins-official`, `mksglu/context-mode`, `K-Dense-AI/scientific-agent-skills`
- **Community 19** (4): `storytold/photocraft`, `storytold/pdfcraft`, `storytold/filmcraft`, `storytold/lightcraft`
- **Community 13** (3): `stablyai/orca`, `cloudflare/security-audit-skill`, `awesome-selfhosted/awesome-selfhosted`
- **Community 36** (3): `deepseek-ai/deepseek-harness`, `sindresorhus/awesome`, `public-apis/public-apis`
- **Community 11** (3): `calesthio/OpenMontage`, `harry0703/MoneyPrinterTurbo`, `firecrawl/firecrawl`
- **Community 15** (2): `MadsLorentzen/ai-job-search`, `obra/superpowers`
- **Community 32** (2): `anomalyco/opencode`, `HKUDS/CLI-Anything`
- **Community 4** (2): `tashfeenahmed/freellmapi`, `Alishahryar1/free-claude-code`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `storytold/filmcraft` ⇄ `storytold/photocraft` (w=1.176) — topics: art, rust; authors: echelon, marcoarnulfo, Ni-zav
- `anthropics/claude-plugins-official` ⇄ `mksglu/context-mode` (w=1.150) — topics: claude-code, mcp, skills; authors: github-actions[bot]
- `storytold/photocraft` ⇄ `storytold/lightcraft` (w=1.110) — topics: art, rust; authors: aiongg, skylartaylor, Silvertree2010
- `storytold/filmcraft` ⇄ `storytold/lightcraft` (w=1.066) — topics: art, rust; authors: echelon, marcoarnulfo, Silvertree2010
- `storytold/filmcraft` ⇄ `storytold/pdfcraft` (w=0.947) — topics: rust; authors: echelon, marcoarnulfo, Silvertree2010
- `storytold/pdfcraft` ⇄ `storytold/lightcraft` (w=0.947) — topics: rust; authors: skylartaylor, Silvertree2010, aiongg
- `storytold/pdfcraft` ⇄ `storytold/photocraft` (w=0.896) — topics: rust; authors: skylartaylor, Silvertree2010, aiongg
- `ifixai-ai/iFixAi` ⇄ `rohitg00/ai-engineering-from-scratch` (w=0.503) — topics: ai, python; authors: ALANDVO, github-actions[bot]
- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `morluto/rea` ⇄ `mksglu/context-mode` (w=0.417) — topics: mcp, claude-code, codex; authors: github-actions[bot]
- `addyosmani/agent-skills` ⇄ `cathrynlavery/diagram-design` (w=0.353) — topics: agent-skills, claude-code, codex; authors: rudycelekli
- `morluto/rea` ⇄ `paperclipai/paperclip` (w=0.310) — topics: ai-agents, mcp, agent-skills, claude-code; authors: github-actions[bot]
- …and 9 more.

**What the risers are written in** — language mix of the top 40 movers:

- **Python** — 14
- **TypeScript** — 10
- **Rust** — 5
- **JavaScript** — 4
- **—** — 3
- **Shell** — 2
- **HTML** — 1
- **Jupyter Notebook** — 1

## Methodology & caveats

- **Source**: `data/snapshots/*.json` diffed against `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-07-27, 2026-08-07, 2026-08-11, 2026-08-28, 2026-08-29, 2026-08-31, 2026-09-06, 2026-09-07, 2026-09-12, 2026-09-14, 2026-09-21, 2026-09-25, 2026-09-28, 2026-09-29, 2026-10-05, 2026-10-10, 2026-10-11, 2026-10-19 (22 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. The recent window therefore does not always use the immediately preceding snapshot: it uses the newest one at least 7 days back, because a 1-day window amplifies noise far more than it reveals movement. Per-day normalization keeps the boards comparable across refreshes either way.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 2,358 · Window: 2026-10-11 → 2026-10-19 (8d) · Snapshot: 2026-10-19T11:27:31.266Z</sub>
