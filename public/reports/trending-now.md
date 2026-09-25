# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 2,243 starred repos (snapshot `2026-09-25T10:37:19.717Z`), cross-referenced with the repo-similarity graph (2,243 nodes / 7,393 edges, 35 communities).
>
> Generated 2026-09-25 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

![Biggest star gains (13d)](assets/trending-now-top-tools.svg)

![Repos by movement type](assets/trending-now-categories.svg)


## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-09-12` → `2026-09-25` (**13 days**), covering the **2,133 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-09-25` (**106 days**).
- **1,790 repos gained stars** in the recent window, adding **812,841★** between them.
- **110 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-09-12 → 2026-09-25, 13d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | **+23,816** | 1832.0 | 51,064 | Python | Hot | very active |
| 2 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | **+22,096** | 1699.7 | 235,536 | TypeScript | Hot | very active |
| 3 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | **+19,059** | 1466.1 | 41,030 | Go | Hot | very active |
| 4 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+18,202** | 1400.2 | 21,428 | JavaScript | Rising | active |
| 5 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+17,310** | 1331.5 | 145,686 | JavaScript | Hot | very active |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **+16,882** | 1298.6 | 267,158 | JavaScript | Hot | very active |
| 7 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+16,115** | 1239.6 | 35,334 | Python | Hot | very active |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | **+15,412** | 1185.5 | 77,810 | TypeScript | Hot | very active |
| 9 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | **+10,715** | 824.2 | 37,594 | C | Hot | very active |
| 10 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | **+10,492** | 807.1 | 42,363 | HTML | Hot | very active |
| 11 | [obra/superpowers](https://github.com/obra/superpowers) | **+9,193** | 707.2 | 291,377 | Shell | Hot | very active |
| 12 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | **+8,751** | 673.2 | 52,973 | TypeScript | Hot | very active |
| 13 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **+8,557** | 658.2 | 186,955 | Python | Hot | very active |
| 14 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | **+8,390** | 645.4 | 29,867 | Go | Hot | very active |
| 15 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | **+8,303** | 638.7 | 70,020 | TypeScript | Hot | very active |
| 16 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **+7,472** | 574.8 | 184,484 | TypeScript | Mature | very active |
| 17 | [earendil-works/pi](https://github.com/earendil-works/pi) | **+7,044** | 541.8 | 109,259 | TypeScript | Hot | very active |
| 18 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **+6,935** | 533.5 | 483,029 | Python | Classic | very active |
| 19 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **+6,760** | 520.0 | 510,178 | — | Mature | active |
| 20 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **+6,665** | 512.7 | 248,814 | Python | Hot | very active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 13-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+564%** | +18,202 | 21,428 | A coding-agent skill for multi-phase security audits with independently verified, machin… |
| 2 | [Human-Agent-Society/reef](https://github.com/Human-Agent-Society/reef) | **+390%** | +4,091 | 5,141 | Continual learning infra for self-improving agents |
| 3 | [deeplethe/utopia](https://github.com/deeplethe/utopia) | **+111%** | +5,348 | 10,164 | World's first open-source enterprise world model. |
| 4 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | **+87%** | +23,816 | 51,064 | A skill to stop your coding agent from burying the answer. ADHD-friendly output. |
| 5 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | **+87%** | +19,059 | 41,030 | Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code revi… |
| 6 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+84%** | +16,115 | 35,334 | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voic… |
| 7 | [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) | **+66%** | +488 | 1,226 | — |
| 8 | [trailhq/Graft](https://github.com/trailhq/Graft) | **+64%** | +3,567 | 9,184 | Turbocharge Claude Code, Cursor, Codex, Gemini & every coding agent: faster, cheaper, wi… |
| 9 | [Anakin-Inc/anakin](https://github.com/Anakin-Inc/anakin) | **+60%** | +1,650 | 4,397 | Open-source web scraping API. Turn any website into clean markdown or structured JSON. A… |
| 10 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | **+52%** | +1,720 | 5,054 | Open source inference engine for the hardware you already own. Profiles your machine, re… |
| 11 | [nateherkai/hyperframes-student-kit](https://github.com/nateherkai/hyperframes-student-kit) | **+51%** | +313 | 923 | Edit videos, reels, and YouTube Shorts with Codex or Claude Code. 14 skills, transcript-… |
| 12 | [spotify/portal-ai-plugins](https://github.com/spotify/portal-ai-plugins) | **+50%** | +750 | 2,265 | — |
| 13 | [jmiao24/Paper2Agent](https://github.com/jmiao24/Paper2Agent) | **+48%** | +1,125 | 3,470 | Paper2Agent is a multi-agent AI system that automatically transforms research papers int… |
| 14 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | **+44%** | +2,548 | 8,372 | Solution for long term memory for agent coding CLIs and to facilitate handoff between di… |
| 15 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | **+41%** | +3,268 | 11,313 | High-performance AI pipeline engine with a C++ core and 50+ Python-extensible nodes. Bui… |
| 16 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | **+40%** | +10,715 | 37,594 | Run frontier MoE models on hardware you already own — pure C, zero deps, experts streame… |
| 17 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | **+39%** | +8,390 | 29,867 | Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomo… |
| 18 | [nvidia-isaac/video_to_data](https://github.com/nvidia-isaac/video_to_data) | **+39%** | +209 | 747 | Nvidia Isaac Video to Data Pipeline |
| 19 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | **+33%** | +10,492 | 42,363 | Editorial diagram design for Claude Code, Codex, and Pi. Self-contained HTML + SVG. No s… |
| 20 | [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | **+32%** | +1,647 | 6,782 | The secure, validated skill registry for professional AI coding agents. Extend Antigravi… |

## Sustained climbers — long run (2026-06-11 → 2026-09-25, 106d)

Averaged over the full snapshot history, so a single viral week doesn't dominate. Repos high here *and* in the recent board are compounding, not spiking.

| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |
|---|---|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | **628.7** | +66,643 | 291,377 | Shell | 75 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **546.0** | +57,881 | 248,814 | Python | 80 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **506.8** | +53,724 | 267,158 | JavaScript | 79 |
| 4 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **499.6** | +52,957 | 184,484 | TypeScript | 84 |
| 5 | [earendil-works/pi](https://github.com/earendil-works/pi) | **447.9** | +47,481 | 109,259 | TypeScript | 80 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **406.8** | +43,117 | 154,570 | Shell | 58 |
| 7 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **397.8** | +42,168 | 483,029 | Python | 65 |
| 8 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **392.2** | +41,576 | 215,056 | — | 22 |
| 9 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | **392.0** | +41,547 | 44,864 | C | 75 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **378.1** | +40,074 | 130,512 | Python | 96 |
| 11 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **372.6** | +39,500 | 125,597 | Python | 85 |
| 12 | [usestrix/strix](https://github.com/usestrix/strix) | **365.7** | +38,761 | 64,707 | Python | 80 |
| 13 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **360.3** | +38,197 | 136,676 | Rust | 81 |
| 14 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **346.6** | +36,740 | 209,940 | TypeScript | 83 |
| 15 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | **342.0** | +36,255 | 107,770 | Go | 78 |
| 16 | [openai/codex](https://github.com/openai/codex) | **339.0** | +35,929 | 126,387 | Rust | 94 |
| 17 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **337.8** | +35,812 | 186,955 | Python | 93 |
| 18 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **333.0** | +35,297 | 510,178 | — | 52 |
| 19 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **330.2** | +35,000 | 549,429 | Markdown | 39 |
| 20 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | **326.2** | +34,576 | 98,030 | TypeScript | 82 |

## Emerging themes

The boards above are computed; this section is interpretation. Each theme groups movers that are rising for the same underlying reason.

### Skills as the packaging format for agent behaviour

_The single loudest signal in this dataset. A year ago you configured an agent with a prompt; now behaviour ships as a versioned, installable *skill* bundle — and the repos distributing those bundles are growing faster than the agents that consume them. Note what this implies: the moat is moving from the model to the instruction layer._

- **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · 51,064★ · +23,816★ in 13d  
  A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 145,686★ · +17,310★ in 13d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 267,158★ · +16,882★ in 13d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 291,377★ · +9,193★ in 13d  
  An agentic skills framework & software development methodology that works.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 130,512★ · +5,161★ in 13d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 215,056★ · +4,595★ in 13d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 154,570★ · +4,271★ in 13d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 178,045★ · +3,367★ in 13d  
  Public repository for Agent Skills
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 134,161★ · +2,550★ in 13d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 54,587★ · +1,012★ in 13d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 66,321★ · +679★ in 13d  
  from vibe coding to agentic engineering - practice makes claude perfect

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 121,287★ · +6,136★ in 13d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 84,129★ · +2,502★ in 13d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 44,864★ · +2,479★ in 13d  
  High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 72,059★ · +2,276★ in 13d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 94,658★ · +1,349★ in 13d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 13,458★ · +1,332★ in 13d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 27,264★ · +1,281★ in 13d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 7,025★ · +679★ in 13d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 16,781★ · +628★ in 13d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 30,973★ · +471★ in 13d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine.
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,567★ · +81★ in 13d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 37,594★ · +10,715★ in 13d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 129,476★ · +2,277★ in 13d  
  LLM inference in C/C++
- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 34,784★ · +1,029★ in 13d  
  AirLLM 70B inference with single 4GB GPU
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,455★ · +97★ in 13d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,564★ · +22★ in 13d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 37,594★ · +10,715★ in 13d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 73,757★ · +4,695★ in 13d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 107,770★ · +3,930★ in 13d  
  🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 81,687★ · +2,697★ in 13d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies
- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 55,909★ · +2,490★ in 13d  
  Use Claude Code, Codex, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly)

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 109,259★ · +7,044★ in 13d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 248,814★ · +6,665★ in 13d  
  The agent that grows with you
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 136,676★ · +5,418★ in 13d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 209,940★ · +5,103★ in 13d  
  The open source coding agent.
- **[openai/codex](https://github.com/openai/codex)** · 126,387★ · +4,547★ in 13d  
  Lightweight coding agent that runs in your terminal
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 148,017★ · +3,807★ in 13d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 83,175★ · +3,097★ in 13d  
  The open-source app everyone uses to manage agents at work
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 89,130★ · +2,829★ in 13d  
  🙌 OpenHands: AI-Driven Development
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 73,238★ · +2,455★ in 13d  
  🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 18,530★ · +2,372★ in 13d  
  Orchestrate multiple coding agents from desktop and mobile
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 51,323★ · +2,308★ in 13d  
  Make humans and AI agents work as one team — open-source and self-hostable.
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 82,962★ · +1,508★ in 13d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 20,118★ · +929★ in 13d  
  The most RAM efficient harness
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 69,395★ · +656★ in 13d  
  OmO: Just type "mass ulw" keyword with your prompt. Now you are the master of graph engineering.
- **[vercel/eve](https://github.com/vercel/eve)** · 5,360★ · +375★ in 13d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 52,973★ · +8,751★ in 13d  
  Write HTML. Render video. Built for agents.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 108,540★ · +5,891★ in 13d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[usestrix/strix](https://github.com/usestrix/strix)** · 64,707★ · +3,907★ in 13d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 116,236★ · +3,776★ in 13d  
  Agents that use the browser.
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 55,653★ · +3,263★ in 13d  
  The open-source AI voice studio. Clone, dictate, create.
- **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** · 72,679★ · +2,405★ in 13d  
  Open-source AI job search: scan job portals, evaluate listings into a structured A-H report with a global 1-5 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, Codex, OpenCode, Antigravity…)
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 40,278★ · +1,424★ in 13d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 34,012★ · +1,345★ in 13d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 31,095★ · +694★ in 13d  
  Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. Understand How to write meeting minutes
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 17,746★ · +239★ in 13d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[github/spec-kit](https://github.com/github/spec-kit)** · 138,825★ · +5,182★ in 13d  
  💫 Toolkit to help you get started with Spec-Driven Development
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 130,512★ · +5,161★ in 13d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 98,030★ · +3,690★ in 13d  
  🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK.
- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 117,818★ · +3,478★ in 13d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [google/material-design-icons](https://github.com/google/material-design-icons) | 54,029 | — | Mature | Material Design icons by Google (Material Symbols) |
| [oobabooga/textgen](https://github.com/oobabooga/textgen) | 47,709 | Python | Mature | Open-source desktop app for local LLMs. Text, vision, tool-calling, OpenAI/Anthropic… |
| [google/zx](https://github.com/google/zx) | 45,773 | JavaScript | Mature | A tool for writing better scripts |
| [reactive-resume/reactive-resume](https://github.com/reactive-resume/reactive-resume) | 43,413 | TypeScript | Classic | A one-of-a-kind resume builder that keeps your privacy in mind. Completely secure, c… |
| [faif/python-patterns](https://github.com/faif/python-patterns) | 43,013 | Python | Classic | A collection of design patterns/idioms in Python |
| [google/styleguide](https://github.com/google/styleguide) | 39,630 | HTML | Mature | Style guides for Google-originated open-source projects |
| [google/googletest](https://github.com/google/googletest) | 39,581 | C++ | Classic | GoogleTest - Google Testing and Mocking Framework |
| [lm-sys/FastChat](https://github.com/lm-sys/FastChat) | 39,551 | Python | Mature | An open platform for training, serving, and evaluating large language models. Releas… |
| [google/leveldb](https://github.com/google/leveldb) | 39,447 | C++ | Declining | LevelDB is a fast key-value storage library written at Google that provides an order… |
| [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | 35,282 | TypeScript | Hot | Your Personal AI Assistant; easy to install, deploy on your own machine or on the cl… |
| [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) | 29,314 | Python | Hot | Community plugin to control Blender 3D with any LLM of your choice |
| [bendlang/bend](https://github.com/bendlang/bend) | 22,677 | TypeScript | Classic | Bend 2: a fast language that blocks AI mistakes via proof. Install: curl -fsSL https… |
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 19,977 | Python | Declining | Fastest and cheapest web agent |
| [NVlabs/instant-ngp](https://github.com/NVlabs/instant-ngp) | 17,559 | Cuda | Declining | Instant neural graphics primitives: lightning fast NeRF and more |
| [coderamp-labs/gitingest](https://github.com/coderamp-labs/gitingest) | 15,623 | Python | Declining | Replace 'hub' with 'ingest' in any GitHub URL to get a prompt-friendly extract of a … |
| [run-llama/liteparse](https://github.com/run-llama/liteparse) | 12,620 | Rust | Rising | A fast, helpful, and open-source document parser |
| [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | 11,573 | TypeScript | Hot | Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retriev… |
| [huggingface/tokenizers](https://github.com/huggingface/tokenizers) | 11,111 | Rust | Classic | 💥 Fast State-of-the-Art Tokenizers optimized for Research and Production |
| [Companion-Inc/feynman](https://github.com/Companion-Inc/feynman) | 9,781 | TypeScript | Rising | The open source AI research agent. |
| [google/artemis](https://github.com/google/artemis) | 9,771 | Python | Hot | ARTEMIS turns natural-language instructions into reliable Android automation. It aut… |
| [NVlabs/Sana](https://github.com/NVlabs/Sana) | 9,144 | Python | Mature | SANA: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformer |
| [apple-aiml-research/ml-sharp](https://github.com/apple-aiml-research/ml-sharp) | 8,918 | Python | Declining | Sharp Monocular View Synthesis in Less Than a Second |
| [katanemo/plano](https://github.com/katanemo/plano) | 7,066 | Rust | Mature | Plano is an AI-native proxy server and data plane for agentic apps. Smart LLM routin… |
| [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | 6,834 | Python | Hot | Jev-like family of decision models built on top of Qwen3.5/3.8 you can train and run… |
| [lm-sys/RouteLLM](https://github.com/lm-sys/RouteLLM) | 5,542 | Python | Abandoned | A framework for serving and evaluating LLM routers - save LLM costs without compromi… |
| [XProger/OpenLara](https://github.com/XProger/OpenLara) | 5,111 | C | Mature | Classic Tomb Raider open-source engine |
| [ApodexAI/FrontierAgent](https://github.com/ApodexAI/FrontierAgent) | 4,599 | Python | Hot | 🧩 FrontierAgent, our agent framework, open-sourced alongside it — native command-lin… |
| [TheoLeeCJ/SemIf-OpenJev](https://github.com/TheoLeeCJ/SemIf-OpenJev) | 4,268 | Python | Rising | Semantic ifs from open models, on a 3090 at home. Independent; not affiliated with J… |
| [ansible/molecule](https://github.com/ansible/molecule) | 4,153 | Python | Classic | An ansible-native testing framework for collections, playbooks, and roles with confi… |
| [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | 4,067 | Python | Hot | The Harness of Harnesses: a trusted, persistent, self-evolving multi-agent ecosystem… |
| [aurelio-labs/semantic-router](https://github.com/aurelio-labs/semantic-router) | 3,923 | Python | Mature | Superfast AI decision making and intelligent processing of multi-modal data. |
| [antonbabenko/pre-commit-terraform](https://github.com/antonbabenko/pre-commit-terraform) | 3,778 | Shell | Classic | pre-commit git hooks to take care of Terraform configurations 🇺🇦 |
| [NVlabs/cuda-oxide](https://github.com/NVlabs/cuda-oxide) | 3,584 | Rust | Hot | cuda-oxide is a Rust-to-CUDA compiler that lets you write (SIMT) GPU kernels in safe… |
| [jordan-gibbs/hyperresearch](https://github.com/jordan-gibbs/hyperresearch) | 3,533 | Python | Hot | Convert Claude Code into the most intelligent Deep Research Agent. Collect, search, … |
| [qdrant/fastembed](https://github.com/qdrant/fastembed) | 3,216 | Python | Classic | Fast, Accurate, Lightweight Python library to make State of the Art Embedding |
| [NVlabs/SoL-Pi](https://github.com/NVlabs/SoL-Pi) | 3,058 | TypeScript | Rising | SoL-Pi: Scaling Auto-Research Loops for Efficient Agent Harnesses |
| [radixark/miles](https://github.com/radixark/miles) | 2,984 | Python | Hot | Miles is an enterprise-facing reinforcement learning framework for LLM and VLM post-… |
| [huggingface/setfit](https://github.com/huggingface/setfit) | 2,823 | Jupyter Notebook | Mature | Efficient few-shot learning with Sentence Transformers |
| [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) | 2,600 | Python | Hot | HarnessRouter Community Edition: the self-hosted, Apache-2.0 edition of the unified … |
| [google/XNNPACK](https://github.com/google/XNNPACK) | 2,460 | C | Classic | High-efficiency floating-point neural network inference operators for mobile, server… |
| _…and 70 more_ | | | | |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 106-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [meta-llama/prompt-ops](https://github.com/meta-llama/prompt-ops) | 2.0 | -1.9 | **-94%** of prior pace | 5mo ago | Declining |
| [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | 1.2 | -0.2 | **-20%** of prior pace | 2mo ago | Declining |
| [Avaiga/taipy](https://github.com/Avaiga/taipy) | 1.8 | -0.2 | **-8%** of prior pace | 1mo ago | Mature |
| [Njengah/claude-code-cheat-sheet](https://github.com/Njengah/claude-code-cheat-sheet) | 1.6 | 0.0 | **0%** of prior pace | 4mo ago | Declining |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 3.2 | 0.2 | **7%** of prior pace | 6mo ago | Declining |
| [Suvink/cut-it-out](https://github.com/Suvink/cut-it-out) | 2.3 | 0.2 | **10%** of prior pace | 9mo ago | Declining |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | 8.8 | 1.2 | **13%** of prior pace | 1mo ago | Rising |
| [winfunc/opcode](https://github.com/winfunc/opcode) | 3.4 | 0.6 | **18%** of prior pace | 7d ago | Declining |
| [Mega4alik/ollm](https://github.com/Mega4alik/ollm) | 1.3 | 0.2 | **18%** of prior pace | 2mo ago | Declining |
| [andrewyng/aisuite](https://github.com/andrewyng/aisuite) | 23.6 | 4.9 | **21%** of prior pace | 6d ago | Mature |
| [sentient-agi/ROMA](https://github.com/sentient-agi/ROMA) | 1.0 | 0.2 | **22%** of prior pace | 7mo ago | Declining |
| [itshover/itshover](https://github.com/itshover/itshover) | 3.9 | 0.9 | **24%** of prior pace | 2mo ago | Rising |
| [guofei9987/blind_watermark](https://github.com/guofei9987/blind_watermark) | 15.0 | 3.6 | **24%** of prior pace | 6mo ago | Declining |
| [microsoft/fara](https://github.com/microsoft/fara) | 6.8 | 1.7 | **25%** of prior pace | 3d ago | Rising |
| [microsoft/magentic-ui](https://github.com/microsoft/magentic-ui) | 1.8 | 0.5 | **26%** of prior pace | 1d ago | Mature |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **18 of the graph's 35 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 1** (6): `stablyai/orca`, `cathrynlavery/diagram-design`, `addyosmani/agent-skills`, `herdrdev/herdr`, `harry0703/MoneyPrinterTurbo`, `rohitg00/ai-engineering-from-scratch`
- **Community 6** (5): `cloudflare/security-audit-skill`, `obra/superpowers`, `NousResearch/hermes-agent`, `headroomlabs-ai/headroom`, `msitarzewski/agency-agents`
- **Community 24** (4): `ayghri/i-have-adhd`, `DietrichGebert/ponytail`, `affaan-m/ECC`, `Graphify-Labs/graphify`
- **Community 8** (3): `alibaba/open-code-review`, `Tencent/WeKnora`, `deeplethe/utopia`
- **Community 17** (3): `public-apis/public-apis`, `sindresorhus/awesome`, `awesome-selfhosted/awesome-selfhosted`
- **Community 5** (2): `debpalash/VoiceStudio`, `JustVugg/colibri`
- **Community 21** (2): `heygen-com/hyperframes`, `diegosouzapw/OmniRoute`
- **Community 7** (2): `microsoft/markitdown`, `TauricResearch/TradingAgents`
- **Community 23** (2): `firecrawl/firecrawl`, `D4Vinci/Scrapling`
- **Community 14** (2): `farion1231/cc-switch`, `nextlevelbuilder/ui-ux-pro-max-skill`
- **Community 9** (2): `github/spec-kit`, `calesthio/OpenMontage`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `addyosmani/agent-skills` ⇄ `cathrynlavery/diagram-design` (w=0.360) — topics: agent-skills, claude-code, codex; authors: dajiaohuang, mvanhorn
- `D4Vinci/Scrapling` ⇄ `firecrawl/firecrawl` (w=0.258) — topics: crawler, scraping, web-scraper, web-scraping
- `calesthio/OpenMontage` ⇄ `headroomlabs-ai/headroom` (w=0.236) — topics: agent, ai, cursor, openai; authors: anupamme
- `alibaba/open-code-review` ⇄ `Tencent/WeKnora` (w=0.201) — topics: agent; authors: dvd233, 58329837+Frank-zhu0404@users.noreply.github.com, po-et
- `rohitg00/ai-engineering-from-scratch` ⇄ `harry0703/MoneyPrinterTurbo` (w=0.189) — topics: llm, python; authors: dajiaohuang
- `ayghri/i-have-adhd` ⇄ `affaan-m/ECC` (w=0.167) — topics: developer-tools, productivity
- `public-apis/public-apis` ⇄ `sindresorhus/awesome` (w=0.125) — topics: resources, lists
- `cloudflare/security-audit-skill` ⇄ `msitarzewski/agency-agents` (w=0.083) — authors: CooperSheroy
- `JustVugg/colibri` ⇄ `debpalash/VoiceStudio` (w=0.069) — authors: kevin9327

**What the risers are written in** — language mix of the top 40 movers:

- **Python** — 16
- **TypeScript** — 7
- **JavaScript** — 4
- **Rust** — 4
- **—** — 3
- **Go** — 2
- **Shell** — 2
- **C** — 1

## Methodology & caveats

- **Source**: `data/snapshots/*.json` diffed against `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-07-27, 2026-08-07, 2026-08-11, 2026-08-28, 2026-08-29, 2026-08-31, 2026-09-06, 2026-09-07, 2026-09-12, 2026-09-25 (14 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. The recent window therefore does not always use the immediately preceding snapshot: it uses the newest one at least 7 days back, because a 1-day window amplifies noise far more than it reveals movement. Per-day normalization keeps the boards comparable across refreshes either way.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 2,133 · Window: 2026-09-12 → 2026-09-25 (13d) · Snapshot: 2026-09-25T10:37:19.717Z</sub>
