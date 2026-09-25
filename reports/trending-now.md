# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 2,243 starred repos (snapshot `2026-09-25T10:37:19.717Z`), cross-referenced with the repo-similarity graph (2,243 nodes / 7,393 edges, 35 communities).
>
> Generated 2026-09-25 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

![Biggest star gains (11d)](assets/trending-now-top-tools.svg)

![Repos by movement type](assets/trending-now-categories.svg)


## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-09-14` → `2026-09-25` (**11 days**), covering the **2,154 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-09-25` (**106 days**).
  - The immediately preceding snapshot (`2026-09-21`) is only 4 days before this one — too short to separate signal from noise — so the baseline was widened to the newest snapshot at least 7 days back.
- **1,758 repos gained stars** in the recent window, adding **466,587★** between them.
- **89 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-09-14 → 2026-09-25, 11d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+18,142** | 1649.3 | 21,428 | JavaScript | Rising | active |
| 2 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | **+16,846** | 1531.5 | 41,030 | Go | Hot | very active |
| 3 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | **+12,190** | 1108.2 | 235,536 | TypeScript | Hot | very active |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | **+9,547** | 867.9 | 77,810 | TypeScript | Hot | very active |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **+9,133** | 830.3 | 267,158 | JavaScript | Hot | very active |
| 6 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+7,862** | 714.7 | 145,686 | JavaScript | Hot | very active |
| 7 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+7,324** | 665.8 | 35,334 | Python | Hot | very active |
| 8 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | **+6,819** | 619.9 | 29,867 | Go | Hot | very active |
| 9 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | **+6,694** | 608.5 | 37,594 | C | Hot | very active |
| 10 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | **+6,174** | 561.3 | 51,064 | Python | Hot | very active |
| 11 | [obra/superpowers](https://github.com/obra/superpowers) | **+4,934** | 448.5 | 291,377 | Shell | Hot | very active |
| 12 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | **+4,810** | 437.3 | 28,400 | Python | Hot | very active |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | **+4,757** | 432.5 | 98,950 | JavaScript | Hot | very active |
| 14 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | **+4,714** | 428.5 | 121,287 | Python | Hot | very active |
| 15 | [earendil-works/pi](https://github.com/earendil-works/pi) | **+4,311** | 391.9 | 109,259 | TypeScript | Hot | very active |
| 16 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **+4,295** | 390.5 | 184,484 | TypeScript | Mature | very active |
| 17 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **+4,273** | 388.5 | 510,178 | — | Mature | active |
| 18 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | **+4,115** | 374.1 | 70,020 | TypeScript | Hot | very active |
| 19 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **+3,905** | 355.0 | 136,676 | Rust | Hot | very active |
| 20 | [Human-Agent-Society/reef](https://github.com/Human-Agent-Society/reef) | **+3,776** | 343.3 | 5,141 | Python | Hot | very active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 11-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+552%** | +18,142 | 21,428 | A coding-agent skill for multi-phase security audits with independently verified, machin… |
| 2 | [Human-Agent-Society/reef](https://github.com/Human-Agent-Society/reef) | **+277%** | +3,776 | 5,141 | Continual learning infra for self-improving agents |
| 3 | [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) | **+85%** | +1,193 | 2,600 | HarnessRouter Community Edition: the self-hosted, Apache-2.0 edition of the unified inte… |
| 4 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | **+70%** | +16,846 | 41,030 | Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code revi… |
| 5 | [NVlabs/SoL-Pi](https://github.com/NVlabs/SoL-Pi) | **+67%** | +1,232 | 3,058 | SoL-Pi: Scaling Auto-Research Loops for Efficient Agent Harnesses |
| 6 | [jmiao24/Paper2Agent](https://github.com/jmiao24/Paper2Agent) | **+47%** | +1,117 | 3,470 | Paper2Agent is a multi-agent AI system that automatically transforms research papers int… |
| 7 | [deeplethe/utopia](https://github.com/deeplethe/utopia) | **+38%** | +2,791 | 10,164 | World's first open-source enterprise world model. |
| 8 | [spotify/portal-ai-plugins](https://github.com/spotify/portal-ai-plugins) | **+37%** | +610 | 2,265 | — |
| 9 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | **+34%** | +2,892 | 11,313 | High-performance AI pipeline engine with a C++ core and 50+ Python-extensible nodes. Bui… |
| 10 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | **+30%** | +6,819 | 29,867 | Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomo… |
| 11 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+26%** | +7,324 | 35,334 | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voic… |
| 12 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | **+24%** | +1,628 | 8,372 | Solution for long term memory for agent coding CLIs and to facilitate handoff between di… |
| 13 | [lnkiai/m3e-canvas](https://github.com/lnkiai/m3e-canvas) | **+23%** | +1,518 | 8,194 | Sketch Material 3 Expressive screens in the browser and turn them into vibe-coding promp… |
| 14 | [Anakin-Inc/anakin](https://github.com/Anakin-Inc/anakin) | **+22%** | +790 | 4,397 | Open-source web scraping API. Turn any website into clean markdown or structured JSON. A… |
| 15 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | **+22%** | +6,694 | 37,594 | Run frontier MoE models on hardware you already own — pure C, zero deps, experts streame… |
| 16 | [trailhq/Graft](https://github.com/trailhq/Graft) | **+21%** | +1,595 | 9,184 | Turbocharge Claude Code, Cursor, Codex, Gemini & every coding agent: faster, cheaper, wi… |
| 17 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | **+20%** | +4,810 | 28,400 | Hindsight: Agent Memory That Learns |
| 18 | [nvidia-isaac/video_to_data](https://github.com/nvidia-isaac/video_to_data) | **+20%** | +124 | 747 | Nvidia Isaac Video to Data Pipeline |
| 19 | [NVIDIA/Personal-AI-Router](https://github.com/NVIDIA/Personal-AI-Router) | **+18%** | +225 | 1,499 | Router that virtually distributes inference across connected devices in the home. |
| 20 | [fastino-ai/GLiNER2](https://github.com/fastino-ai/GLiNER2) | **+17%** | +319 | 2,176 | Unified Schema-Based Information Extraction |

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

- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 267,158★ · +9,133★ in 11d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 145,686★ · +7,862★ in 11d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · 51,064★ · +6,174★ in 11d  
  A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 291,377★ · +4,934★ in 11d  
  An agentic skills framework & software development methodology that works.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 130,512★ · +3,016★ in 11d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 154,570★ · +2,352★ in 11d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 215,056★ · +2,178★ in 11d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 178,045★ · +1,829★ in 11d  
  Public repository for Agent Skills
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 134,161★ · +1,220★ in 11d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 54,587★ · +584★ in 11d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 66,321★ · +413★ in 11d  
  from vibe coding to agentic engineering - practice makes claude perfect

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 121,287★ · +4,714★ in 11d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 44,864★ · +1,683★ in 11d  
  High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 84,129★ · +1,487★ in 11d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 72,059★ · +1,286★ in 11d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 94,658★ · +832★ in 11d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 27,264★ · +622★ in 11d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 13,458★ · +603★ in 11d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 7,025★ · +597★ in 11d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 16,781★ · +316★ in 11d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 30,973★ · +299★ in 11d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine.
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,567★ · +42★ in 11d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 37,594★ · +6,694★ in 11d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 129,476★ · +1,305★ in 11d  
  LLM inference in C/C++
- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 34,784★ · +481★ in 11d  
  AirLLM 70B inference with single 4GB GPU
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,455★ · +52★ in 11d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,564★ · +16★ in 11d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 37,594★ · +6,694★ in 11d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 107,770★ · +2,294★ in 11d  
  🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 73,757★ · +1,752★ in 11d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 81,687★ · +1,415★ in 11d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies
- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 55,909★ · +1,050★ in 11d  
  Use Claude Code, Codex, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly)

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 109,259★ · +4,311★ in 11d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 136,676★ · +3,905★ in 11d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 248,814★ · +3,497★ in 11d  
  The agent that grows with you
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 148,017★ · +3,046★ in 11d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 209,940★ · +2,684★ in 11d  
  The open source coding agent.
- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 83,175★ · +2,530★ in 11d  
  The open-source app everyone uses to manage agents at work
- **[openai/codex](https://github.com/openai/codex)** · 126,387★ · +2,375★ in 11d  
  Lightweight coding agent that runs in your terminal
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 51,323★ · +1,537★ in 11d  
  Make humans and AI agents work as one team — open-source and self-hostable.
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 18,530★ · +1,303★ in 11d  
  Orchestrate multiple coding agents from desktop and mobile
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 89,130★ · +1,285★ in 11d  
  🙌 OpenHands: AI-Driven Development
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 73,238★ · +851★ in 11d  
  🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 82,962★ · +554★ in 11d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 20,118★ · +452★ in 11d  
  The most RAM efficient harness
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 69,395★ · +366★ in 11d  
  OmO: Just type "mass ulw" keyword with your prompt. Now you are the master of graph engineering.
- **[vercel/eve](https://github.com/vercel/eve)** · 5,360★ · +253★ in 11d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 52,973★ · +3,143★ in 11d  
  Write HTML. Render video. Built for agents.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 108,540★ · +2,911★ in 11d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 55,653★ · +2,484★ in 11d  
  The open-source AI voice studio. Clone, dictate, create.
- **[usestrix/strix](https://github.com/usestrix/strix)** · 64,707★ · +2,375★ in 11d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 116,236★ · +1,664★ in 11d  
  Agents that use the browser.
- **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** · 72,679★ · +1,135★ in 11d  
  Open-source AI job search: scan job portals, evaluate listings into a structured A-H report with a global 1-5 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, Codex, OpenCode, Antigravity…)
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 40,278★ · +703★ in 11d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 34,012★ · +604★ in 11d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 31,095★ · +360★ in 11d  
  Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. Understand How to write meeting minutes
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 17,746★ · +115★ in 11d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 130,512★ · +3,016★ in 11d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[github/spec-kit](https://github.com/github/spec-kit)** · 138,825★ · +2,207★ in 11d  
  💫 Toolkit to help you get started with Spec-Driven Development
- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 117,818★ · +2,028★ in 11d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 98,030★ · +1,960★ in 11d  
  🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK.

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [google/material-design-icons](https://github.com/google/material-design-icons) | 54,029 | — | Mature | Material Design icons by Google (Material Symbols) |
| [oobabooga/textgen](https://github.com/oobabooga/textgen) | 47,709 | Python | Mature | Open-source desktop app for local LLMs. Text, vision, tool-calling, OpenAI/Anthropic… |
| [google/zx](https://github.com/google/zx) | 45,773 | JavaScript | Mature | A tool for writing better scripts |
| [faif/python-patterns](https://github.com/faif/python-patterns) | 43,013 | Python | Classic | A collection of design patterns/idioms in Python |
| [google/styleguide](https://github.com/google/styleguide) | 39,630 | HTML | Mature | Style guides for Google-originated open-source projects |
| [google/googletest](https://github.com/google/googletest) | 39,581 | C++ | Classic | GoogleTest - Google Testing and Mocking Framework |
| [lm-sys/FastChat](https://github.com/lm-sys/FastChat) | 39,551 | Python | Mature | An open platform for training, serving, and evaluating large language models. Releas… |
| [google/leveldb](https://github.com/google/leveldb) | 39,447 | C++ | Declining | LevelDB is a fast key-value storage library written at Google that provides an order… |
| [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) | 29,314 | Python | Hot | Community plugin to control Blender 3D with any LLM of your choice |
| [bendlang/bend](https://github.com/bendlang/bend) | 22,677 | TypeScript | Classic | Bend 2: a fast language that blocks AI mistakes via proof. Install: curl -fsSL https… |
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 19,977 | Python | Declining | Fastest and cheapest web agent |
| [run-llama/liteparse](https://github.com/run-llama/liteparse) | 12,620 | Rust | Rising | A fast, helpful, and open-source document parser |
| [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | 11,573 | TypeScript | Hot | Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retriev… |
| [huggingface/tokenizers](https://github.com/huggingface/tokenizers) | 11,111 | Rust | Classic | 💥 Fast State-of-the-Art Tokenizers optimized for Research and Production |
| [Companion-Inc/feynman](https://github.com/Companion-Inc/feynman) | 9,781 | TypeScript | Rising | The open source AI research agent. |
| [google/artemis](https://github.com/google/artemis) | 9,771 | Python | Hot | ARTEMIS turns natural-language instructions into reliable Android automation. It aut… |
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
| [radixark/miles](https://github.com/radixark/miles) | 2,984 | Python | Hot | Miles is an enterprise-facing reinforcement learning framework for LLM and VLM post-… |
| [huggingface/setfit](https://github.com/huggingface/setfit) | 2,823 | Jupyter Notebook | Mature | Efficient few-shot learning with Sentence Transformers |
| [google/XNNPACK](https://github.com/google/XNNPACK) | 2,460 | C | Classic | High-efficiency floating-point neural network inference operators for mobile, server… |
| [antonbabenko/terraform-skill](https://github.com/antonbabenko/terraform-skill) | 2,380 | — | Declining | Terraform & OpenTofu Skill for AI Agents - testing, modules, CI/CD, and production p… |
| [cashapp/molecule](https://github.com/cashapp/molecule) | 2,230 | Kotlin | Mature | Build a StateFlow stream using Jetpack Compose |
| [oxigraph/oxigraph](https://github.com/oxigraph/oxigraph) | 1,954 | Rust | Classic | SPARQL graph database |
| [GetStream/stream-chat-android](https://github.com/GetStream/stream-chat-android) | 1,665 | Kotlin | Classic | :speech_balloon: Android Chat SDK ➜ Stream Chat API. UI component libraries for chat… |
| [scikit-learn-contrib/MAPIE](https://github.com/scikit-learn-contrib/MAPIE) | 1,595 | Jupyter Notebook | Classic | A scikit-learn-compatible library for estimating prediction intervals and controllin… |
| [erictli/scratch](https://github.com/erictli/scratch) | 1,582 | TypeScript | Mature | A minimalist, offline-first markdown note-taking app |
| [mizorewww/laya-coreml](https://github.com/mizorewww/laya-coreml) | 1,444 | Python | Mature | Local Laya typed decisions on Apple Core ML and Neural Engine. Validated ports, ~5 m… |
| [GetStream/stream-chat-flutter](https://github.com/GetStream/stream-chat-flutter) | 1,054 | Dart | Classic | Flutter Chat SDK - Build your own chat app experience using Dart, Flutter and the St… |
| [nickvourd/Supernova](https://github.com/nickvourd/Supernova) | 1,042 | Go | Mature | Shellcode encryptor & obfuscator tool |
| [GetStream/stream-chat-swift](https://github.com/GetStream/stream-chat-swift) | 972 | Swift | Classic | 💬 iOS Chat SDK in Swift - Build your own app chat experience for iOS using the offic… |
| [DTStack/molecule](https://github.com/DTStack/molecule) | 972 | TypeScript | Mature | :rocket: A lightweight Web IDE UI framework. |
| _…and 49 more_ | | | | |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 106-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [JohnMwendwa/free-ai-resources](https://github.com/JohnMwendwa/free-ai-resources) | 1.2 | -4.9 | **-407%** of prior pace | 1.3y ago | Abandoned |
| [meta-llama/prompt-ops](https://github.com/meta-llama/prompt-ops) | 2.0 | -2.1 | **-103%** of prior pace | 5mo ago | Declining |
| [Njengah/claude-code-cheat-sheet](https://github.com/Njengah/claude-code-cheat-sheet) | 1.6 | -0.3 | **-17%** of prior pace | 4mo ago | Declining |
| [Avaiga/taipy](https://github.com/Avaiga/taipy) | 1.8 | -0.3 | **-15%** of prior pace | 1mo ago | Mature |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 3.2 | -0.5 | **-14%** of prior pace | 6mo ago | Declining |
| [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | 1.2 | -0.1 | **-8%** of prior pace | 2mo ago | Declining |
| [sentient-agi/ROMA](https://github.com/sentient-agi/ROMA) | 1.0 | 0.0 | **0%** of prior pace | 7mo ago | Declining |
| [Suvink/cut-it-out](https://github.com/Suvink/cut-it-out) | 2.3 | 0.1 | **4%** of prior pace | 9mo ago | Declining |
| [winfunc/opcode](https://github.com/winfunc/opcode) | 3.4 | 0.2 | **5%** of prior pace | 7d ago | Declining |
| [BishopFox/cloudfox](https://github.com/BishopFox/cloudfox) | 1.5 | 0.1 | **6%** of prior pace | 1mo ago | Mature |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | 8.8 | 0.6 | **7%** of prior pace | 1mo ago | Rising |
| [openai/openai-cs-agents-demo](https://github.com/openai/openai-cs-agents-demo) | 1.6 | 0.2 | **11%** of prior pace | 9mo ago | Declining |
| [OpenDCAI/DataFlow](https://github.com/OpenDCAI/DataFlow) | 32.3 | 3.6 | **11%** of prior pace | 5d ago | Mature |
| [jamwithai/production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course) | 19.6 | 2.4 | **12%** of prior pace | 3mo ago | Declining |
| [dagger/container-use](https://github.com/dagger/container-use) | 2.0 | 0.3 | **14%** of prior pace | 4d ago | Mature |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **19 of the graph's 35 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 6** (5): `cloudflare/security-audit-skill`, `obra/superpowers`, `Human-Agent-Society/reef`, `NousResearch/hermes-agent`, `rocketride-org/rocketride-server`
- **Community 1** (4): `stablyai/orca`, `addyosmani/agent-skills`, `cathrynlavery/diagram-design`, `rohitg00/ai-engineering-from-scratch`
- **Community 24** (4): `affaan-m/ECC`, `DietrichGebert/ponytail`, `ayghri/i-have-adhd`, `Graphify-Labs/graphify`
- **Community 8** (3): `alibaba/open-code-review`, `Tencent/WeKnora`, `deeplethe/utopia`
- **Community 17** (3): `sindresorhus/awesome`, `public-apis/public-apis`, `awesome-selfhosted/awesome-selfhosted`
- **Community 14** (3): `farion1231/cc-switch`, `nextlevelbuilder/ui-ux-pro-max-skill`, `paperclipai/paperclip`
- **Community 7** (3): `trycua/cua`, `microsoft/markitdown`, `TauricResearch/TradingAgents`
- **Community 5** (2): `debpalash/VoiceStudio`, `JustVugg/colibri`
- **Community 23** (2): `firecrawl/firecrawl`, `D4Vinci/Scrapling`
- **Community 21** (2): `diegosouzapw/OmniRoute`, `heygen-com/hyperframes`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `addyosmani/agent-skills` ⇄ `cathrynlavery/diagram-design` (w=0.360) — topics: agent-skills, claude-code, codex; authors: dajiaohuang, mvanhorn
- `D4Vinci/Scrapling` ⇄ `firecrawl/firecrawl` (w=0.258) — topics: crawler, scraping, web-scraper, web-scraping
- `alibaba/open-code-review` ⇄ `Tencent/WeKnora` (w=0.201) — topics: agent; authors: dvd233, 58329837+Frank-zhu0404@users.noreply.github.com, po-et
- `ayghri/i-have-adhd` ⇄ `affaan-m/ECC` (w=0.167) — topics: developer-tools, productivity
- `jamiepine/voicebox` ⇄ `debpalash/VoiceStudio` (w=0.167) — topics: ai, voice-ai, cuda, mlx
- `public-apis/public-apis` ⇄ `sindresorhus/awesome` (w=0.125) — topics: resources, lists
- `JustVugg/colibri` ⇄ `debpalash/VoiceStudio` (w=0.069) — authors: kevin9327

**What the risers are written in** — language mix of the top 40 movers:

- **Python** — 14
- **TypeScript** — 11
- **JavaScript** — 4
- **Rust** — 3
- **Go** — 2
- **—** — 2
- **HTML** — 2
- **C** — 1

## Methodology & caveats

- **Source**: `data/snapshots/*.json` diffed against `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-07-27, 2026-08-07, 2026-08-11, 2026-08-28, 2026-08-29, 2026-08-31, 2026-09-06, 2026-09-07, 2026-09-12, 2026-09-14, 2026-09-21, 2026-09-25 (16 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. The recent window therefore does not always use the immediately preceding snapshot: it uses the newest one at least 7 days back, because a 1-day window amplifies noise far more than it reveals movement. Per-day normalization keeps the boards comparable across refreshes either way.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 2,154 · Window: 2026-09-14 → 2026-09-25 (11d) · Snapshot: 2026-09-25T10:37:19.717Z</sub>
