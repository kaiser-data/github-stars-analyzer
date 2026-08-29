# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 1,857 starred repos (snapshot `2026-08-29T15:31:31.780Z`), cross-referenced with the repo-similarity graph (1,857 nodes / 6,041 edges, 37 communities).
>
> Generated 2026-08-29 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

![Biggest star gains (18d)](assets/trending-now-top-tools.svg)

![Repos by movement type](assets/trending-now-categories.svg)


## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-08-11` → `2026-08-29` (**18 days**), covering the **1,584 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-08-29` (**79 days**).
  - The immediately preceding snapshot (`2026-08-28`) is only 1 day before this one — too short to separate signal from noise — so the baseline was widened to the newest snapshot at least 7 days back.
- **1,356 repos gained stars** in the recent window, adding **782,590★** between them.
- **273 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-08-11 → 2026-08-29, 18d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+17,910** | 995.0 | 116,107 | JavaScript | Hot | very active |
| 2 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **+17,705** | 983.6 | 472,653 | Python | Classic | very active |
| 3 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **+16,293** | 905.2 | 118,380 | Python | Mature | very active |
| 4 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | **+15,447** | 858.2 | 57,894 | TypeScript | Hot | very active |
| 5 | [openai/codex](https://github.com/openai/codex) | **+15,098** | 838.8 | 119,746 | Rust | Hot | very active |
| 6 | [earendil-works/pi](https://github.com/earendil-works/pi) | **+13,739** | 763.3 | 99,005 | TypeScript | Hot | very active |
| 7 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | **+12,800** | 711.1 | 19,009 | TypeScript | Hot | very active |
| 8 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **+11,037** | 613.2 | 173,889 | TypeScript | Mature | very active |
| 9 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **+10,956** | 608.7 | 237,998 | Python | Hot | very active |
| 10 | [obra/superpowers](https://github.com/obra/superpowers) | **+10,588** | 588.2 | 279,271 | Shell | Hot | very active |
| 11 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **+9,674** | 537.4 | 148,766 | Shell | Hot | very active |
| 12 | [usestrix/strix](https://github.com/usestrix/strix) | **+9,613** | 534.1 | 59,237 | Python | Hot | very active |
| 13 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | **+8,914** | 495.2 | 11,208 | Python | Hot | very active |
| 14 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **+8,339** | 463.3 | 122,809 | Python | Hot | very active |
| 15 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | **+8,208** | 456.0 | 112,191 | Python | Hot | very active |
| 16 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | **+8,178** | 454.3 | 92,559 | — | Hot | very active |
| 17 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **+8,062** | 447.9 | 208,570 | — | Declining | slowing |
| 18 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | **+7,922** | 440.1 | 53,797 | Python | Hot | very active |
| 19 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | **+7,751** | 430.6 | 33,330 | Rust | Hot | very active |
| 20 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | **+7,676** | 426.4 | 25,126 | TypeScript | Rising | very active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 18-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [MakazhanAlpamys/Soup](https://github.com/MakazhanAlpamys/Soup) | **+798%** | +3,144 | 3,538 | Fine-tune LLMs from one YAML. Layer streaming trains an 8B model on a 4 GB laptop GPU. |
| 2 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | **+389%** | +8,914 | 11,208 | Graph-Native Infrastructure for Context and Accountable AI Systems |
| 3 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | **+206%** | +12,800 | 19,009 | A self-improving RLM agent for coding workflows and long-running autonomous tasks. |
| 4 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | **+161%** | +5,944 | 9,639 | 14MB foundation model for tiny devices; phones, wearables, smart home, and robots. |
| 5 | [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) | **+108%** | +3,493 | 6,713 | A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB of RAM. P… |
| 6 | [vitali87/code-graph-rag](https://github.com/vitali87/code-graph-rag) | **+89%** | +2,283 | 4,844 | The ultimate RAG for your monorepo. Query, understand, and edit multi-language codebases… |
| 7 | [Prism-Shadow/penguin-harness](https://github.com/Prism-Shadow/penguin-harness) | **+85%** | +837 | 1,816 | 🐧 Harness for RSI. Let AI Build AI. Multi-Agent Auto-Dev Platform. Everything is Transpa… |
| 8 | [cloudflare/computer](https://github.com/cloudflare/computer) | **+60%** | +3,294 | 8,817 | Give your agent a computer 👾 |
| 9 | [Anakin-Inc/anakin](https://github.com/Anakin-Inc/anakin) | **+58%** | +873 | 2,370 | Open-source web scraping API. Turn any website into clean markdown or structured JSON. A… |
| 10 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | **+44%** | +7,676 | 25,126 | TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations,… |
| 11 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | **+42%** | +4,265 | 14,426 | Rebuild the object in a reference image as a code-only, procedural, quality-gated, anima… |
| 12 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | **+41%** | +7,388 | 25,493 | A skill to stop your coding agent from burying the answer. ADHD-friendly output. |
| 13 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | **+40%** | +158 | 551 | Light, fluffy, and always free - Local Azure Emulator |
| 14 | [bjarneo/cliamp](https://github.com/bjarneo/cliamp) | **+38%** | +1,066 | 3,839 | cliamp - Terminal music player inspired by winamp |
| 15 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | **+36%** | +15,447 | 57,894 | Never stop coding. Free MIT AI gateway: one endpoint, 350 providers (90+ free), 1200+ mo… |
| 16 | [zzet/gortex](https://github.com/zzet/gortex) | **+36%** | +395 | 1,502 | High-performance code-intelligence engine for AI agents and IDE, supports 257 languages,… |
| 17 | [sophiamyang/finger-frame-effect-ai](https://github.com/sophiamyang/finger-frame-effect-ai) | **+35%** | +252 | 982 | — |
| 18 | [hi-godot/godot-ai](https://github.com/hi-godot/godot-ai) | **+34%** | +508 | 1,996 | Production-grade MCP server and AI tools for the Godot engine. A Snap to install. Totall… |
| 19 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | **+32%** | +6,487 | 26,920 | Turn any technical book PDF into a Claude Code skill — ready to study, reference, and us… |
| 20 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | **+30%** | +7,751 | 33,330 | the runtime your coding agents live on |

## Sustained climbers — long run (2026-06-11 → 2026-08-29, 79d)

Averaged over the full snapshot history, so a single viral week doesn't dominate. Repos high here *and* in the recent board are compounding, not spiking.

| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |
|---|---|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | **690.3** | +54,537 | 279,271 | Shell | 79 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **595.8** | +47,065 | 237,998 | Python | 85 |
| 3 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **536.2** | +42,362 | 173,889 | TypeScript | 89 |
| 4 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | **477.9** | +37,751 | 41,068 | C | 75 |
| 5 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **472.3** | +37,313 | 148,766 | Shell | 65 |
| 6 | [earendil-works/pi](https://github.com/earendil-works/pi) | **471.2** | +37,227 | 99,005 | TypeScript | 85 |
| 7 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **444.2** | +35,090 | 208,570 | — | 24 |
| 8 | [usestrix/strix](https://github.com/usestrix/strix) | **421.4** | +33,291 | 59,237 | Python | 81 |
| 9 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **409.8** | +32,371 | 122,809 | Python | 95 |
| 10 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **408.6** | +32,283 | 118,380 | Python | 85 |
| 11 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **402.4** | +31,792 | 472,653 | Python | 64 |
| 12 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **399.8** | +31,583 | 130,062 | Rust | 77 |
| 13 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **388.1** | +30,660 | 244,094 | JavaScript | 79 |
| 14 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | **382.3** | +30,201 | 101,716 | Go | 75 |
| 15 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **372.4** | +29,418 | 543,847 | Markdown | 48 |
| 16 | [openai/codex](https://github.com/openai/codex) | **370.7** | +29,288 | 119,746 | Rust | 94 |
| 17 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **368.6** | +29,117 | 202,317 | TypeScript | 83 |
| 18 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | **368.4** | +29,105 | 92,559 | — | 82 |
| 19 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **331.2** | +26,166 | 501,047 | — | 60 |
| 20 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **327.0** | +25,836 | 176,979 | Python | 64 |

## Emerging themes

The boards above are computed; this section is interpretation. Each theme groups movers that are rising for the same underlying reason.

### Skills as the packaging format for agent behaviour

_The single loudest signal in this dataset. A year ago you configured an agent with a prompt; now behaviour ships as a versioned, installable *skill* bundle — and the repos distributing those bundles are growing faster than the agents that consume them. Note what this implies: the moat is moving from the model to the instruction layer._

- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 116,107★ · +17,910★ in 18d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 279,271★ · +10,588★ in 18d  
  An agentic skills framework & software development methodology that works.
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 148,766★ · +9,674★ in 18d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 122,809★ · +8,339★ in 18d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 208,570★ · +8,062★ in 18d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · 25,493★ · +7,388★ in 18d  
  A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 244,094★ · +5,543★ in 18d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 172,418★ · +5,534★ in 18d  
  Public repository for Agent Skills
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 130,302★ · +3,510★ in 18d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 53,168★ · +1,320★ in 18d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 65,337★ · +1,199★ in 18d  
  from vibe coding to agentic engineering - practice makes claude perfect

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 11,208★ · +8,914★ in 18d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 112,191★ · +8,208★ in 18d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 25,126★ · +7,676★ in 18d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 68,579★ · +3,267★ in 18d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 80,959★ · +3,087★ in 18d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 41,068★ · +3,028★ in 18d  
  High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 92,556★ · +2,558★ in 18d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 6,268★ · +1,421★ in 18d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 15,806★ · +1,291★ in 18d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 30,335★ · +488★ in 18d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine.
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,455★ · +148★ in 18d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 26,397★ · +3,229★ in 18d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 126,203★ · +3,192★ in 18d  
  LLM inference in C/C++
- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 33,035★ · +3,150★ in 18d  
  AirLLM 70B inference with single 4GB GPU
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,324★ · +252★ in 18d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,531★ · +36★ in 18d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 51,335★ · +6,565★ in 18d  
  Use Claude Code, Codex, Pi, and OpenCode and more for free (1.3B+ free tokens) from your terminal, app, IDE, or phone like OpenClaw (voice supported + ToS friendly)
- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 101,716★ · +5,022★ in 18d  
  🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 26,397★ · +3,229★ in 18d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 77,794★ · +2,611★ in 18d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 67,983★ · +2,599★ in 18d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[openai/codex](https://github.com/openai/codex)** · 119,746★ · +15,098★ in 18d  
  Lightweight coding agent that runs in your terminal
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 99,005★ · +13,739★ in 18d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 237,998★ · +10,956★ in 18d  
  The agent that grows with you
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 202,317★ · +7,595★ in 18d  
  The open source coding agent.
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 130,062★ · +4,613★ in 18d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 79,620★ · +3,793★ in 18d  
  The open-source app everyone uses to manage agents at work
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 48,215★ · +3,526★ in 18d  
  Make humans and AI agents work as one team — open-source and self-hostable.
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 143,373★ · +2,774★ in 18d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 15,411★ · +2,771★ in 18d  
  Orchestrate multiple coding agents from desktop and mobile
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 18,775★ · +2,438★ in 18d  
  The most RAM efficient harness
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 69,703★ · +2,424★ in 18d  
  🌊 The original agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 85,544★ · +2,152★ in 18d  
  🙌 OpenHands: AI-Driven Development
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 81,091★ · +1,579★ in 18d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 68,499★ · +1,047★ in 18d  
  omo/lazycodex: The coding agent for tokenmaxxers;the one and only agent harness for complex codebases. For your Codex, for your OpenCode
- **[vercel/eve](https://github.com/vercel/eve)** · 4,864★ · +414★ in 18d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[usestrix/strix](https://github.com/usestrix/strix)** · 59,237★ · +9,613★ in 18d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[santifer/career-ops](https://github.com/santifer/career-ops)** · 69,185★ · +6,026★ in 18d  
  Open-source AI job search: scan job portals, evaluate listings into a structured A-H report with a global 1-5 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, Codex, OpenCode, Antigravity…)
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 101,667★ · +5,594★ in 18d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 37,839★ · +4,901★ in 18d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 111,637★ · +3,440★ in 18d  
  🌐 Make websites accessible for AI agents. Automate tasks online with ease.
- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 43,042★ · +3,101★ in 18d  
  Write HTML. Render video. Built for agents.
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 51,775★ · +2,081★ in 18d  
  The open-source AI voice studio. Clone, dictate, create.
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 32,026★ · +1,796★ in 18d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 30,046★ · +1,607★ in 18d  
  Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. Understand How to write meeting minutes
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 17,422★ · +243★ in 18d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 122,809★ · +8,339★ in 18d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 92,559★ · +8,178★ in 18d  
  🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK.
- **[github/spec-kit](https://github.com/github/spec-kit)** · 132,136★ · +6,364★ in 18d  
  💫 Toolkit to help you get started with Spec-Driven Development
- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 111,200★ · +4,016★ in 18d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 203,007 | TypeScript | Hot | DeepSeek Harness: Everything is a Plugin. |
| [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 189,439 | Shell | Classic | 🙃   A delightful community-driven (with 2,500+ contributors) framework for managing … |
| [microsoft/terminal](https://github.com/microsoft/terminal) | 104,724 | C++ | Classic | The new Windows Terminal and the original Windows console host, all in the same plac… |
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 94,894 | Python | Declining | AI agents running research on single-GPU nanochat training automatically |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 90,628 | JavaScript | Hot | Production-grade engineering skills for AI coding agents. |
| [junegunn/fzf](https://github.com/junegunn/fzf) | 82,712 | Go | Classic | :cherry_blossom: A command-line fuzzy finder |
| [Eugeny/tabby](https://github.com/Eugeny/tabby) | 74,218 | TypeScript | Classic | A terminal for a more modern age |
| [alacritty/alacritty](https://github.com/alacritty/alacritty) | 65,550 | Rust | Mature | A cross-platform, OpenGL terminal emulator. |
| [warpdotdev/warp](https://github.com/warpdotdev/warp) | 64,628 | Rust | Classic | Warp is an agentic development environment, born out of the terminal. |
| [tldr-pages/tldr](https://github.com/tldr-pages/tldr) | 63,522 | Markdown | Classic | Collaborative cheatsheets for console commands 📚. |
| [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | 60,417 | Zig | Classic | 👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses pl… |
| [sharkdp/bat](https://github.com/sharkdp/bat) | 60,296 | Rust | Classic | A cat(1) clone with wings. |
| [termux/termux-app](https://github.com/termux/termux-app) | 59,962 | Java | Mature | Termux - a terminal emulator application for Android OS extendible by variety of pac… |
| [starship/starship](https://github.com/starship/starship) | 59,647 | Rust | Classic | ☄🌌️  The minimal, blazing-fast, and infinitely customizable prompt for any shell! |
| [Textualize/rich](https://github.com/Textualize/rich) | 57,271 | Python | Mature | Rich is a Python library for rich text and beautiful formatting in the terminal. |
| [stablyai/orca](https://github.com/stablyai/orca) | 56,609 | TypeScript | Hot | Orca is the ADE for working with a fleet of parallel agents. Run any coding agent wi… |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 50,091 | TypeScript | Hot | Chrome DevTools for coding agents |
| [vercel/hyper](https://github.com/vercel/hyper) | 44,709 | TypeScript | Mature | A terminal built on web technologies |
| [sharkdp/fd](https://github.com/sharkdp/fd) | 44,241 | Rust | Classic | A simple, fast and user-friendly alternative to 'find' |
| [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | 43,900 | Jupyter Notebook | Mature | This is a repo with links to everything you'd ever want to learn about data engineer… |
| [sxyazi/yazi](https://github.com/sxyazi/yazi) | 41,779 | Rust | Classic | 💥 Blazing fast terminal file manager written in Rust, based on async I/O. |
| [chubin/cheat.sh](https://github.com/chubin/cheat.sh) | 41,701 | Python | Declining | the only cheat sheet you need |
| [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | 40,865 | Rust | Hot | Open-source coding agent for your terminal, built in Rust and on a journey of contin… |
| [appsmithorg/appsmith](https://github.com/appsmithorg/appsmith) | 40,780 | TypeScript | Classic | Platform to build admin panels, internal tools, and dashboards. Integrates with 25+ … |
| [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | 40,512 | Python | Classic | A community-maintained Python framework for creating mathematical animations. |
| [nushell/nushell](https://github.com/nushell/nushell) | 40,366 | Rust | Classic | A new type of shell |
| [ajeetdsouza/zoxide](https://github.com/ajeetdsouza/zoxide) | 39,013 | Rust | Classic | A smarter cd command. Supports all major shells. |
| [httpie/cli](https://github.com/httpie/cli) | 38,465 | Python | Abandoned | 🥧 HTTPie CLI  — modern, user-friendly command-line HTTP client for the API era. JSON… |
| [Textualize/textual](https://github.com/Textualize/textual) | 37,080 | Python | Classic | The lean application framework for Python.  Build sophisticated user interfaces with… |
| [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | 35,240 | Go | Hot | DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache st… |
| [zellij-org/zellij](https://github.com/zellij-org/zellij) | 35,171 | Rust | Classic | A terminal workspace with batteries included |
| [kovidgoyal/kitty](https://github.com/kovidgoyal/kitty) | 34,669 | Python | Classic | If you live in the terminal, kitty is made for you! Cross-platform, fast, feature-ri… |
| [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | 34,236 | Python | Hot | Self-evolving Context Database for AI Agents. Unify Agent Memory, Knowledge RAG and … |
| [fish-shell/fish-shell](https://github.com/fish-shell/fish-shell) | 34,085 | Rust | Classic | The user-friendly command line shell. |
| [microsoft/WSL](https://github.com/microsoft/WSL) | 33,559 | C++ | Classic | Windows Subsystem for Linux |
| [nicolargo/glances](https://github.com/nicolargo/glances) | 33,467 | Python | Classic | Glances an Eye on your system. A top/htop alternative for GNU/Linux, BSD, macOS and … |
| [ibraheemdev/modern-unix](https://github.com/ibraheemdev/modern-unix) | 33,022 | — | Abandoned | A collection of modern/faster/saner alternatives to common unix commands. |
| [kingToolbox/WindTerm](https://github.com/kingToolbox/WindTerm) | 32,093 | C | Declining | A professional cross-platform SSH/Sftp/Shell/Telnet/Tmux/Serial terminal. |
| [jumpserver/jumpserver](https://github.com/jumpserver/jumpserver) | 31,470 | Python | Classic | JumpServer is an open-source Privileged Access Management (PAM) platform that provid… |
| [atuinsh/atuin](https://github.com/atuinsh/atuin) | 31,457 | Rust | Classic | ✨ Making your shell magical |
| _…and 233 more_ | | | | |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 79-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [HeartMuLa/heartlib](https://github.com/HeartMuLa/heartlib) | 1.2 | -3.0 | **-247%** of prior pace | 4mo ago | Declining |
| [axios/axios](https://github.com/axios/axios) | 1.5 | -2.1 | **-138%** of prior pace | 1d ago | Classic |
| [iternal-technologies-partners/blockify-agentic-data-optimization](https://github.com/iternal-technologies-partners/blockify-agentic-data-optimization) | 1.3 | -0.1 | **-4%** of prior pace | 4mo ago | Declining |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 4.2 | -0.1 | **-1%** of prior pace | 5mo ago | Declining |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 72.9 | 7.3 | **10%** of prior pace | 1d ago | Hot |
| [Suvink/cut-it-out](https://github.com/Suvink/cut-it-out) | 3.0 | 0.4 | **13%** of prior pace | 8mo ago | Declining |
| [nearai/ironclaw](https://github.com/nearai/ironclaw) | 2.0 | 0.3 | **14%** of prior pace | 0d ago | Hot |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | 11.4 | 1.8 | **16%** of prior pace | 3d ago | Rising |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 158.8 | 27.1 | **17%** of prior pace | 0d ago | Classic |
| [microsoft/fara](https://github.com/microsoft/fara) | 8.8 | 1.8 | **20%** of prior pace | 1mo ago | Rising |
| [https-deeplearning-ai/deeplearning-ai](https://github.com/https-deeplearning-ai/deeplearning-ai) | 1.9 | 0.4 | **20%** of prior pace | 2mo ago | Rising |
| [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | 28.6 | 6.1 | **21%** of prior pace | 1mo ago | Declining |
| [winfunc/opcode](https://github.com/winfunc/opcode) | 4.3 | 1.1 | **25%** of prior pace | 10mo ago | Declining |
| [andrewyng/aisuite](https://github.com/andrewyng/aisuite) | 30.3 | 8.1 | **27%** of prior pace | 16d ago | Mature |
| [allenai/olmocr](https://github.com/allenai/olmocr) | 25.5 | 6.8 | **27%** of prior pace | 5mo ago | Declining |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **17 of the graph's 37 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 11** (9): `DietrichGebert/ponytail`, `diegosouzapw/OmniRoute`, `msitarzewski/agency-agents`, `nextlevelbuilder/ui-ux-pro-max-skill`, `Graphify-Labs/graphify`, `nexu-io/open-design`, `herdrdev/herdr`, `ayghri/i-have-adhd`, `affaan-m/ECC`
- **Community 24** (5): `public-apis/public-apis`, `usestrix/strix`, `sindresorhus/awesome`, `codecrafters-io/build-your-own-x`, `DigitalPlatDev/FreeDomain`
- **Community 9** (5): `NousResearch/hermes-agent`, `obra/superpowers`, `TencentCloud/TencentDB-Agent-Memory`, `MadsLorentzen/ai-job-search`, `unslothai/unsloth`
- **Community 12** (3): `harry0703/MoneyPrinterTurbo`, `calesthio/OpenMontage`, `github/spec-kit`
- **Community 8** (3): `earendil-works/pi`, `santifer/career-ops`, `JuliusBrussee/caveman`
- **Community 23** (2): `firecrawl/firecrawl`, `TauricResearch/TradingAgents`
- **Community 7** (2): `semantica-agi/semantica`, `virgiliojr94/book-to-skill`
- **Community 3** (2): `Alishahryar1/free-claude-code`, `OpenCut-app/OpenCut`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `NousResearch/hermes-agent` ⇄ `affaan-m/ECC` (w=0.313) — topics: ai-agents, llm, anthropic, claude
- `MadsLorentzen/ai-job-search` ⇄ `santifer/career-ops` (w=0.280) — topics: ai, career, claude-code, job-application
- `calesthio/OpenMontage` ⇄ `unslothai/unsloth` (w=0.269) — topics: agent, ai, image-generation, openai
- `calesthio/OpenMontage` ⇄ `harry0703/MoneyPrinterTurbo` (w=0.203) — topics: ffmpeg, python, text-to-speech; authors: octo-patch
- `JuliusBrussee/caveman` ⇄ `santifer/career-ops` (w=0.192) — topics: ai, anthropic, claude, claude-code; authors: github-actions[bot]
- `MadsLorentzen/ai-job-search` ⇄ `NousResearch/hermes-agent` (w=0.186) — topics: ai, ai-agents, claude-code
- `ayghri/i-have-adhd` ⇄ `affaan-m/ECC` (w=0.167) — topics: developer-tools, productivity
- `public-apis/public-apis` ⇄ `sindresorhus/awesome` (w=0.167) — topics: resources, lists; authors: morning-verlu
- `ayghri/i-have-adhd` ⇄ `DietrichGebert/ponytail` (w=0.143) — topics: claude-code-plugin, developer-tools
- `DigitalPlatDev/FreeDomain` ⇄ `codecrafters-io/build-your-own-x` (w=0.100) — topics: free

**What the risers are written in** — language mix of the top 40 movers:

- **Python** — 19
- **TypeScript** — 7
- **JavaScript** — 3
- **Rust** — 3
- **—** — 3
- **Shell** — 2
- **Markdown** — 2
- **Go** — 1

## Methodology & caveats

- **Source**: `data/snapshots/*.json` diffed against `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-07-27, 2026-08-07, 2026-08-11, 2026-08-28, 2026-08-29 (9 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. The recent window therefore does not always use the immediately preceding snapshot: it uses the newest one at least 7 days back, because a 1-day window amplifies noise far more than it reveals movement. Per-day normalization keeps the boards comparable across refreshes either way.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 1,584 · Window: 2026-08-11 → 2026-08-29 (18d) · Snapshot: 2026-08-29T15:31:31.780Z</sub>
