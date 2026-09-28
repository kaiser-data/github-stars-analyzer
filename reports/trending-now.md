# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 2,259 starred repos (snapshot `2026-09-28T12:23:49.424Z`), cross-referenced with the repo-similarity graph (2,259 nodes / 7,430 edges, 38 communities).
>
> Generated 2026-09-28 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

![Biggest star gains (7d)](assets/trending-now-top-tools.svg)

![Repos by movement type](assets/trending-now-categories.svg)


## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-09-21` → `2026-09-28` (**7 days**), covering the **2,208 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-09-28` (**109 days**).
  - The immediately preceding snapshot (`2026-09-25`) is only 3 days before this one — too short to separate signal from noise — so the baseline was widened to the newest snapshot at least 7 days back.
- **1,692 repos gained stars** in the recent window, adding **289,696★** between them.
- **51 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-09-21 → 2026-09-28, 7d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | **+15,340** | 2191.4 | 39,507 | Python | Hot | very active |
| 2 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | **+10,406** | 1486.6 | 91,575 | TypeScript | Hot | very active |
| 3 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | **+8,031** | 1147.3 | 16,558 | Python | Hot | very active |
| 4 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+7,959** | 1137.0 | 41,685 | Python | Rising | very active |
| 5 | [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | **+7,108** | 1015.4 | 21,009 | Python | Declining | active |
| 6 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | **+6,498** | 928.3 | 238,393 | TypeScript | Hot | very active |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | **+6,065** | 866.4 | 80,216 | TypeScript | Hot | very active |
| 8 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | **+4,901** | 700.1 | 60,024 | Python | Hot | very active |
| 9 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **+4,374** | 624.9 | 268,664 | JavaScript | Hot | very active |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **+4,081** | 583.0 | 138,002 | Rust | Hot | very active |
| 11 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+3,994** | 570.6 | 22,537 | JavaScript | Rising | active |
| 12 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+3,786** | 540.9 | 147,202 | JavaScript | Hot | very active |
| 13 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **+3,351** | 478.7 | 511,763 | — | Mature | active |
| 14 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | **+3,275** | 467.9 | 42,124 | Go | Hot | very active |
| 15 | [Human-Agent-Society/reef](https://github.com/Human-Agent-Society/reef) | **+3,021** | 431.6 | 6,863 | Python | Hot | very active |
| 16 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **+2,993** | 427.6 | 185,746 | TypeScript | Mature | very active |
| 17 | [obra/superpowers](https://github.com/obra/superpowers) | **+2,843** | 406.1 | 292,354 | Shell | Hot | very active |
| 18 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | **+2,492** | 356.0 | 30,822 | Go | Hot | very active |
| 19 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | **+2,217** | 316.7 | 51,746 | Python | Hot | very active |
| 20 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | **+2,173** | 310.4 | 70,914 | TypeScript | Hot | very active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 7-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [mizorewww/laya-coreml](https://github.com/mizorewww/laya-coreml) | **+162%** | +937 | 1,514 | Local Laya typed decisions on Apple Core ML and Neural Engine. Validated ports, ~5 ms sh… |
| 2 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | **+94%** | +8,031 | 16,558 | High-performance AI pipeline engine with a C++ core and 50+ Python-extensible nodes. Bui… |
| 3 | [Human-Agent-Society/reef](https://github.com/Human-Agent-Society/reef) | **+79%** | +3,021 | 6,863 | Infrastructure for continually self‑improving agents |
| 4 | [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) | **+65%** | +1,072 | 2,727 | HarnessRouter Community Edition: the self-hosted, Apache-2.0 edition of the unified inte… |
| 5 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | **+63%** | +15,340 | 39,507 | Hindsight: Agent Memory That Learns |
| 6 | [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | **+51%** | +7,108 | 21,009 | Fastest and cheapest web agent |
| 7 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+24%** | +7,959 | 41,685 | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voic… |
| 8 | [google/artemis](https://github.com/google/artemis) | **+23%** | +1,977 | 10,535 | ARTEMIS turns natural-language instructions into reliable Android automation. It automat… |
| 9 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+22%** | +3,994 | 22,537 | A coding-agent skill for multi-phase security audits with independently verified, machin… |
| 10 | [nateherkai/hyperframes-student-kit](https://github.com/nateherkai/hyperframes-student-kit) | **+20%** | +174 | 1,064 | Edit videos, reels, and YouTube Shorts with Codex or Claude Code. 14 skills, transcript-… |
| 11 | [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) | **+19%** | +1,310 | 8,102 | Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android, Emulator… |
| 12 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | **+15%** | +1,133 | 8,510 | Solution for long term memory for agent coding CLIs and to facilitate handoff between di… |
| 13 | [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | **+15%** | +1,119 | 8,505 | Build an agent harness and control it end-to-end. Open-source SDK for production AI agen… |
| 14 | [NVlabs/SoL-Pi](https://github.com/NVlabs/SoL-Pi) | **+14%** | +395 | 3,160 | SoL-Pi: Scaling Auto-Research Loops for Efficient Agent Harnesses |
| 15 | [aws/context-ontology-accelerator](https://github.com/aws/context-ontology-accelerator) | **+14%** | +105 | 876 | An open-source, ontology-based semantic context accelerator that enables AI agents to ma… |
| 16 | [spotify/portal-ai-plugins](https://github.com/spotify/portal-ai-plugins) | **+13%** | +273 | 2,301 | — |
| 17 | [zzet/gortex](https://github.com/zzet/gortex) | **+13%** | +213 | 1,798 | High-performance code-intelligence engine for AI agents and IDE, supports 257 languages,… |
| 18 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | **+13%** | +10,406 | 91,575 | The open-source app everyone uses to manage agents at work |
| 19 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | **+13%** | +594 | 5,325 | Open source inference engine for the hardware you already own. Profiles your machine, re… |
| 20 | [nvidia-isaac/video_to_data](https://github.com/nvidia-isaac/video_to_data) | **+11%** | +79 | 782 | Nvidia Isaac Video to Data Pipeline |

## Sustained climbers — long run (2026-06-11 → 2026-09-28, 109d)

Averaged over the full snapshot history, so a single viral week doesn't dominate. Repos high here *and* in the recent board are compounding, not spiking.

| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |
|---|---|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | **620.4** | +67,620 | 292,354 | Shell | 75 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **538.9** | +58,736 | 249,669 | Python | 81 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **506.7** | +55,230 | 268,664 | JavaScript | 79 |
| 4 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **497.4** | +54,219 | 185,746 | TypeScript | 84 |
| 5 | [earendil-works/pi](https://github.com/earendil-works/pi) | **442.3** | +48,210 | 109,988 | TypeScript | 85 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **399.6** | +43,552 | 155,005 | Shell | 58 |
| 7 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **395.5** | +43,110 | 483,971 | Python | 65 |
| 8 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **386.7** | +42,151 | 215,631 | — | 22 |
| 9 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | **384.6** | +41,919 | 45,236 | C | 76 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **373.5** | +40,710 | 131,148 | Python | 96 |
| 11 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **371.0** | +40,439 | 126,536 | Python | 85 |
| 12 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **362.6** | +39,523 | 138,002 | Rust | 76 |
| 13 | [usestrix/strix](https://github.com/usestrix/strix) | **361.2** | +39,367 | 65,313 | Python | 80 |
| 14 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **342.5** | +37,335 | 210,535 | TypeScript | 83 |
| 15 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **338.4** | +36,882 | 511,763 | — | 52 |
| 16 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | **336.0** | +36,625 | 108,140 | Go | 78 |
| 17 | [openai/codex](https://github.com/openai/codex) | **334.4** | +36,447 | 126,905 | Rust | 84 |
| 18 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **332.6** | +36,258 | 187,401 | Python | 93 |
| 19 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **329.1** | +35,871 | 550,300 | Markdown | 38 |
| 20 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | **321.0** | +34,984 | 98,438 | TypeScript | 82 |

## Emerging themes

The boards above are computed; this section is interpretation. Each theme groups movers that are rising for the same underlying reason.

### Skills as the packaging format for agent behaviour

_The single loudest signal in this dataset. A year ago you configured an agent with a prompt; now behaviour ships as a versioned, installable *skill* bundle — and the repos distributing those bundles are growing faster than the agents that consume them. Note what this implies: the moat is moving from the model to the instruction layer._

- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 268,664★ · +4,374★ in 7d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 147,202★ · +3,786★ in 7d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 292,354★ · +2,843★ in 7d  
  An agentic skills framework & software development methodology that works.
- **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · 51,746★ · +2,217★ in 7d  
  A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 131,148★ · +1,687★ in 7d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 178,740★ · +1,337★ in 7d  
  Public repository for Agent Skills
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 215,631★ · +1,198★ in 7d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 155,005★ · +1,143★ in 7d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 134,374★ · +545★ in 7d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 54,736★ · +357★ in 7d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 66,485★ · +328★ in 7d  
  from vibe coding to agentic engineering - practice makes claude perfect

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 122,002★ · +1,962★ in 7d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 45,236★ · +1,291★ in 7d  
  High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 84,440★ · +927★ in 7d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 72,247★ · +572★ in 7d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 94,819★ · +443★ in 7d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 7,075★ · +316★ in 7d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 27,399★ · +314★ in 7d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 31,110★ · +230★ in 7d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory with small models for free
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 13,521★ · +174★ in 7d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 16,829★ · +143★ in 7d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,574★ · +17★ in 7d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 38,061★ · +1,374★ in 7d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 129,758★ · +730★ in 7d  
  LLM inference in C/C++
- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 35,145★ · +513★ in 7d  
  AirLLM 70B inference with single 4GB GPU
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,463★ · +34★ in 7d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,570★ · +15★ in 7d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 38,061★ · +1,374★ in 7d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 108,140★ · +1,061★ in 7d  
  🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 73,996★ · +657★ in 7d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 81,877★ · +650★ in 7d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies
- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 56,091★ · +525★ in 7d  
  Use Claude Code, Codex, VSCode, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly)

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 91,575★ · +10,406★ in 7d  
  The open-source app everyone uses to manage agents at work
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 138,002★ · +4,081★ in 7d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 249,669★ · +2,042★ in 7d  
  The agent that grows with you
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 109,988★ · +1,999★ in 7d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 210,535★ · +1,517★ in 7d  
  The open source coding agent.
- **[openai/codex](https://github.com/openai/codex)** · 126,905★ · +1,242★ in 7d  
  Lightweight coding agent that runs in your terminal
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 148,433★ · +1,054★ in 7d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 18,836★ · +879★ in 7d  
  Orchestrate multiple coding agents from desktop and mobile
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 89,366★ · +669★ in 7d  
  🙌 OpenHands: AI-Driven Development
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 51,537★ · +558★ in 7d  
  Make humans and AI agents work as one team — open-source and self-hostable.
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 73,421★ · +448★ in 7d  
  🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 69,617★ · +371★ in 7d  
  OmO: Just type "mass ulw" keyword with your prompt. Now you are the master of graph engineering.
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 83,139★ · +345★ in 7d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 20,184★ · +221★ in 7d  
  The most RAM efficient harness
- **[vercel/eve](https://github.com/vercel/eve)** · 5,392★ · +102★ in 7d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 53,773★ · +1,695★ in 7d  
  Write HTML. Render video. Built for agents.
- **[usestrix/strix](https://github.com/usestrix/strix)** · 65,313★ · +1,370★ in 7d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 108,991★ · +1,107★ in 7d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 116,581★ · +893★ in 7d  
  Agents that use the browser.
- **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** · 72,965★ · +663★ in 7d  
  Open-source AI job search: scan job portals, evaluate listings into a structured A-H report with a global 1-5 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, Codex, OpenCode, Antigravity…)
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 55,892★ · +559★ in 7d  
  The open-source AI voice studio. Clone, dictate, create.
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 34,197★ · +433★ in 7d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 40,409★ · +297★ in 7d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 31,195★ · +203★ in 7d  
  Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. Understand How to write meeting minutes
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 17,765★ · +60★ in 7d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 131,148★ · +1,687★ in 7d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 118,493★ · +1,527★ in 7d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.
- **[github/spec-kit](https://github.com/github/spec-kit)** · 139,220★ · +1,081★ in 7d  
  💫 Toolkit to help you get started with SDD or any other process!
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 98,438★ · +1,048★ in 7d  
  🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK.

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [omacom/omarchy](https://github.com/omacom/omarchy) | 43,461 | Shell | Hot | Beautiful, Modern & Opinionated Linux |
| [lm-sys/FastChat](https://github.com/lm-sys/FastChat) | 39,550 | Python | Mature | An open platform for training, serving, and evaluating large language models. Releas… |
| [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 27,248 | Python | Rising | Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decision… |
| [run-llama/liteparse](https://github.com/run-llama/liteparse) | 12,689 | Rust | Rising | A fast, helpful, and open-source document parser |
| [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | 7,553 | Python | Hot | Jev-like family of decision models built on top of Qwen3.5/3.8 you can train and run… |
| [katanemo/plano](https://github.com/katanemo/plano) | 7,068 | Rust | Mature | Plano is an AI-native proxy server and data plane for agentic apps. Smart LLM routin… |
| [lm-sys/RouteLLM](https://github.com/lm-sys/RouteLLM) | 5,553 | Python | Abandoned | A framework for serving and evaluating LLM routers - save LLM costs without compromi… |
| [ApodexAI/FrontierAgent](https://github.com/ApodexAI/FrontierAgent) | 4,667 | Python | Hot | 🧩 FrontierAgent, our agent framework, open-sourced alongside it — native command-lin… |
| [TheoLeeCJ/SemIf-OpenJev](https://github.com/TheoLeeCJ/SemIf-OpenJev) | 4,488 | Python | Rising | Semantic ifs from open models, on a 3090 at home. Independent; not affiliated with J… |
| [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | 4,275 | Python | Hot | The Harness of Harnesses • built for RSI: a trusted, persistent, self-evolving multi… |
| [aurelio-labs/semantic-router](https://github.com/aurelio-labs/semantic-router) | 3,929 | Python | Mature | Superfast AI decision making and intelligent processing of multi-modal data. |
| [huggingface/setfit](https://github.com/huggingface/setfit) | 2,823 | Jupyter Notebook | Mature | Efficient few-shot learning with Sentence Transformers |
| [microsoft/Ontology-Playground](https://github.com/microsoft/Ontology-Playground) | 2,795 | TypeScript | Hot | Free, open-source web app for learning about ontologies and Microsoft Fabric IQ. Exp… |
| [inferstep/ATLAS](https://github.com/inferstep/ATLAS) | 2,096 | Python | Rising | Adaptive Test-time Learning and Autonomous Specialization |
| [omacom/omarchy-mac](https://github.com/omacom/omarchy-mac) | 1,856 | Shell | Hot | Opinionated Arch/Hyprland Setup for Apple Silicon Macs M1/M2 |
| [GetStream/stream-chat-android](https://github.com/GetStream/stream-chat-android) | 1,666 | Kotlin | Classic | :speech_balloon: Android Chat SDK ➜ Stream Chat API. UI component libraries for chat… |
| [scikit-learn-contrib/MAPIE](https://github.com/scikit-learn-contrib/MAPIE) | 1,596 | Jupyter Notebook | Classic | A scikit-learn-compatible library for estimating prediction intervals and controllin… |
| [goodroot/hyprwhspr](https://github.com/goodroot/hyprwhspr) | 1,222 | Python | Hot | Native speech-to-text for Linux - Fast, accurate, private, and hackable system-wide … |
| [GetStream/stream-chat-flutter](https://github.com/GetStream/stream-chat-flutter) | 1,055 | Dart | Classic | Flutter Chat SDK - Build your own chat app experience using Dart, Flutter and the St… |
| [GetStream/stream-chat-swift](https://github.com/GetStream/stream-chat-swift) | 972 | Swift | Classic | 💬 iOS Chat SDK in Swift - Build your own app chat experience for iOS using the offic… |
| [ontio/ontology](https://github.com/ontio/ontology) | 905 | Go | Mature | Official Go implementation of the Ontology protocol. https://dev-docs.ont.io/#/ |
| [GetStream/stream-chat-react](https://github.com/GetStream/stream-chat-react) | 845 | TypeScript | Classic | React Chat SDK ➜ Stream Chat 💬 |
| [ozekik/awesome-ontology](https://github.com/ozekik/awesome-ontology) | 711 | — | Mature | A curated list of ontology things |
| [YennNing/Awesome-Code-as-Agent-Harness-Papers](https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers) | 710 | — | Declining | A curated list of papers and resources based on the survey "Code as Agent Harness" |
| [Knowledgator/GLiClass](https://github.com/Knowledgator/GLiClass) | 541 | Python | Mature | Generalist and Lightweight Model for Text Classification |
| [naw103/foremerge](https://github.com/naw103/foremerge) | 515 | Rust | Rising | Catch intent conflicts before code conflicts. The open-source coordination protocol … |
| [anistark/feluda](https://github.com/anistark/feluda) | 478 | Rust | Hot | Detect license usage restrictions in your project! |
| [run-llama/llama-agents](https://github.com/run-llama/llama-agents) | 453 | Python | Hot | Llama Agents + Workflows are an event-driven, async-first, step-based way to control… |
| [docker/skills](https://github.com/docker/skills) | 377 | Python | Hot | A collection of Docker skills for AI coding agents to help them build, test, debug, … |
| [Zefan-Cai/Open-Jev](https://github.com/Zefan-Cai/Open-Jev) | 353 | Python | Hot | — |
| [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) | 332 | Python | Rising | Jev-compatible API endpoint based on open models (prefill-only) |
| [ibm-granite/granite-guardian](https://github.com/ibm-granite/granite-guardian) | 180 | Jupyter Notebook | Mature | The Granite Guardian models are designed to detect risks in prompts and responses. |
| [OpenEnergyPlatform/ontology](https://github.com/OpenEnergyPlatform/ontology) | 168 | Python | Classic | Repository for the Open Energy Ontology (OEO) |
| [daseinlabs/open-jev](https://github.com/daseinlabs/open-jev) | 117 | Python | Rising | Open Jev implementation with custom finetuning |
| [tattle-made/feluda](https://github.com/tattle-made/feluda) | 97 | Python | Mature | A configurable engine for analysing multi-lingual and multi-modal content. |
| [NVIDIA-Medtech/NV-Reason-CXR](https://github.com/NVIDIA-Medtech/NV-Reason-CXR) | 86 | Python | Declining | 🩻 NV-Reason-CXR-3B is a specialized vision-language model designed for medical reaso… |
| [apartresearch/interpretability-starter](https://github.com/apartresearch/interpretability-starter) | 82 | — | Abandoned | 🧠 Starter templates for doing interpretability research |
| [run-llama/llama-parse-py](https://github.com/run-llama/llama-parse-py) | 63 | Python | Hot | Python SDK for OCR and document parsing in the cloud with LlamaParse |
| [ontology-tools/py-horned-owl](https://github.com/ontology-tools/py-horned-owl) | 30 | Rust | Classic | A library for Web Ontology Language in Python created using a bridge from horned-owl… |
| [FrancoisChastel/jev-code](https://github.com/FrancoisChastel/jev-code) | 27 | TypeScript | Rising | Jev, TypeSafe's System One classifier, as a tool inside Claude Code, Codex, Pi, and … |
| _…and 11 more_ | | | | |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 109-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | 1.1 | -0.4 | **-39%** of prior pace | 2mo ago | Declining |
| [lllyasviel/FramePack](https://github.com/lllyasviel/FramePack) | 2.3 | -0.7 | **-31%** of prior pace | 11mo ago | Declining |
| [Njengah/claude-code-cheat-sheet](https://github.com/Njengah/claude-code-cheat-sheet) | 1.6 | -0.4 | **-27%** of prior pace | 4mo ago | Declining |
| [microsoft/magentic-ui](https://github.com/microsoft/magentic-ui) | 1.7 | -0.3 | **-16%** of prior pace | 5d ago | Mature |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | 3.7 | -0.1 | **-4%** of prior pace | 2mo ago | Declining |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | 8.6 | 0.0 | **0%** of prior pace | 1mo ago | Rising |
| [dagger/container-use](https://github.com/dagger/container-use) | 2.0 | 0.0 | **0%** of prior pace | 7d ago | Mature |
| [Avaiga/taipy](https://github.com/Avaiga/taipy) | 1.8 | 0.0 | **0%** of prior pace | 1mo ago | Mature |
| [meta-llama/prompt-ops](https://github.com/meta-llama/prompt-ops) | 2.0 | 0.0 | **0%** of prior pace | 5mo ago | Declining |
| [cursor/cursor](https://github.com/cursor/cursor) | 2.8 | 0.0 | **0%** of prior pace | 4mo ago | Mature |
| [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | 15.1 | 0.4 | **3%** of prior pace | 1mo ago | Mature |
| [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | 6.0 | 0.3 | **5%** of prior pace | 4d ago | Hot |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 57.3 | 5.3 | **9%** of prior pace | 0d ago | Hot |
| [OpenDCAI/DataFlow](https://github.com/OpenDCAI/DataFlow) | 31.5 | 3.0 | **10%** of prior pace | 0d ago | Mature |
| [algorithmicsuperintelligence/optillm](https://github.com/algorithmicsuperintelligence/optillm) | 1.5 | 0.1 | **10%** of prior pace | 0d ago | Mature |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **16 of the graph's 38 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 15** (9): `rocketride-org/rocketride-server`, `browser-use/jev-ultrafast`, `Human-Agent-Society/reef`, `obra/superpowers`, `diegosouzapw/OmniRoute`, `NousResearch/hermes-agent`, `heygen-com/hyperframes`, `VoltAgent/awesome-design-md`, `block/buzz`
- **Community 5** (6): `affaan-m/ECC`, `cloudflare/security-audit-skill`, `DietrichGebert/ponytail`, `ayghri/i-have-adhd`, `Graphify-Labs/graphify`, `awesome-selfhosted/awesome-selfhosted`
- **Community 33** (4): `deepseek-ai/deepseek-harness`, `sindresorhus/awesome`, `public-apis/public-apis`, `codecrafters-io/build-your-own-x`
- **Community 20** (3): `paperclipai/paperclip`, `nextlevelbuilder/ui-ux-pro-max-skill`, `juspay/hyperswitch`
- **Community 0** (3): `stablyai/orca`, `rohitg00/ai-engineering-from-scratch`, `addyosmani/agent-skills`
- **Community 7** (3): `alibaba/open-code-review`, `Tencent/WeKnora`, `harry0703/MoneyPrinterTurbo`
- **Community 25** (2): `firecrawl/firecrawl`, `D4Vinci/Scrapling`
- **Community 19** (2): `google/artemis`, `JustVugg/colibri`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `D4Vinci/Scrapling` ⇄ `firecrawl/firecrawl` (w=0.258) — topics: crawler, scraping, web-scraper, web-scraping
- `rohitg00/ai-engineering-from-scratch` ⇄ `harry0703/MoneyPrinterTurbo` (w=0.203) — topics: llm, python; authors: dajiaohuang
- `alibaba/open-code-review` ⇄ `Tencent/WeKnora` (w=0.175) — topics: agent; authors: dvd233, 58329837+Frank-zhu0404@users.noreply.github.com, po-et
- `ayghri/i-have-adhd` ⇄ `affaan-m/ECC` (w=0.167) — topics: developer-tools, productivity
- `ayghri/i-have-adhd` ⇄ `DietrichGebert/ponytail` (w=0.143) — topics: claude-code-plugin, developer-tools
- `public-apis/public-apis` ⇄ `sindresorhus/awesome` (w=0.125) — topics: resources, lists

**What the risers are written in** — language mix of the top 40 movers:

- **Python** — 16
- **TypeScript** — 9
- **JavaScript** — 4
- **Rust** — 3
- **—** — 3
- **Go** — 2
- **Shell** — 1
- **Markdown** — 1

## Methodology & caveats

- **Source**: `data/snapshots/*.json` diffed against `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-07-27, 2026-08-07, 2026-08-11, 2026-08-28, 2026-08-29, 2026-08-31, 2026-09-06, 2026-09-07, 2026-09-12, 2026-09-14, 2026-09-21, 2026-09-25, 2026-09-28 (17 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. The recent window therefore does not always use the immediately preceding snapshot: it uses the newest one at least 7 days back, because a 1-day window amplifies noise far more than it reveals movement. Per-day normalization keeps the boards comparable across refreshes either way.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 2,208 · Window: 2026-09-21 → 2026-09-28 (7d) · Snapshot: 2026-09-28T12:23:49.424Z</sub>
