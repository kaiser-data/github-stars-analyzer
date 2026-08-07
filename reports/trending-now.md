# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 1,476 starred repos (snapshot `2026-08-07T21:10:17.796Z`), cross-referenced with the repo-similarity graph (1,476 nodes / 4,785 edges, 33 communities).
>
> Generated 2026-08-07 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-07-20` → `2026-08-07` (**18 days**), covering the **1,340 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-08-07` (**57 days**).
- **1,127 repos gained stars** in the recent window, adding **566,155★** between them.
- **136 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-07-20 → 2026-08-07, 18d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [earendil-works/pi](https://github.com/earendil-works/pi) | **+12,268** | 681.6 | 85,266 | TypeScript | Hot | very active |
| 2 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | **+12,167** | 675.9 | 103,983 | Python | Hot | very active |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+11,912** | 661.8 | 98,197 | JavaScript | Hot | very active |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | **+10,872** | 604.0 | 268,683 | Shell | Hot | very active |
| 5 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | **+10,672** | 592.9 | 63,137 | Jupyter Notebook | Classic | very active |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **+9,598** | 533.2 | 227,042 | Python | Hot | very active |
| 7 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **+9,571** | 531.7 | 162,852 | TypeScript | Mature | very active |
| 8 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **+8,324** | 462.4 | 537,480 | Markdown | Mature | active |
| 9 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | **+8,301** | 461.2 | 17,450 | TypeScript | Mature | active |
| 10 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | **+7,219** | 401.1 | 16,337 | Rust | Rising | very active |
| 11 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **+7,200** | 400.0 | 238,551 | JavaScript | Hot | very active |
| 12 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **+7,081** | 393.4 | 194,722 | TypeScript | Hot | very active |
| 13 | [usestrix/strix](https://github.com/usestrix/strix) | **+6,867** | 381.5 | 49,624 | Python | Hot | very active |
| 14 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | **+6,574** | 365.2 | 23,168 | C | Hot | very active |
| 15 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **+6,553** | 364.1 | 493,398 | — | Mature | active |
| 16 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | **+6,533** | 362.9 | 131,309 | Python | Mature | very active |
| 17 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **+6,522** | 362.3 | 114,470 | Python | Hot | very active |
| 18 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **+6,353** | 352.9 | 125,449 | Rust | Hot | very active |
| 19 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | **+6,130** | 340.6 | 29,885 | Jupyter Notebook | Mature | very active |
| 20 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | **+6,018** | 334.3 | 49,694 | TypeScript | Hot | very active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 18-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | **+91%** | +8,301 | 17,450 | TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations,… |
| 2 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | **+79%** | +7,219 | 16,337 | The most RAM efficient harness |
| 3 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | **+66%** | +3,244 | 8,153 | Open-source vacuum robot cleaner |
| 4 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | **+62%** | +878 | 2,294 | Graph-Native Infrastructure for Context and Accountable AI Systems |
| 5 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | **+47%** | +1,406 | 4,425 | Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, … |
| 6 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | **+40%** | +6,574 | 23,168 | Run frontier MoE models on hardware you already own — pure C, zero deps, experts streame… |
| 7 | [hi-godot/godot-ai](https://github.com/hi-godot/godot-ai) | **+38%** | +409 | 1,488 | Production-grade MCP server and AI tools for the Godot engine. A Snap to install. Totall… |
| 8 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | **+35%** | +2,426 | 9,337 | The end of web parsing. The beginning of scalable pixel-native search. link: https://pix… |
| 9 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | **+28%** | +1,047 | 4,847 | Codebase intelligence for AI and humans: code health scores, auto-generated docs, git an… |
| 10 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | **+26%** | +6,130 | 29,885 | AirLLM 70B inference with single 4GB GPU |
| 11 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | **+20%** | +10,672 | 63,137 | 12 Weeks, 24 Lessons, AI for All! |
| 12 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | **+19%** | +4,798 | 30,230 | "Vibe-Trading: Your Personal Trading Agent" |
| 13 | [Kruszoneq/macUSB](https://github.com/Kruszoneq/macUSB) | **+18%** | +356 | 2,340 | The all-in-one bootable USB creator for Mac |
| 14 | [superlinked/sie](https://github.com/superlinked/sie) | **+17%** | +391 | 2,668 | Open-source inference server and production cluster for all the models your agent needs. |
| 15 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | **+17%** | +4,801 | 32,938 | DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/. |
| 16 | [earendil-works/pi](https://github.com/earendil-works/pi) | **+17%** | +12,268 | 85,266 | AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI |
| 17 | [usestrix/strix](https://github.com/usestrix/strix) | **+16%** | +6,867 | 49,624 | Open-source AI penetration testing tool to find and fix your app’s vulnerabilities. |
| 18 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | **+16%** | +1,749 | 12,640 | Orchestrate multiple coding agents from desktop and mobile |
| 19 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | **+16%** | +1,978 | 14,515 | OpenWiki is a CLI that writes and maintains agent documentation for your codebase. |
| 20 | [malisper/pgrust](https://github.com/malisper/pgrust) | **+15%** | +547 | 4,112 | Postgres rewritten in Rust, now faster than Postgres and Clickhouse |

## Sustained climbers — long run (2026-06-11 → 2026-08-07, 57d)

Averaged over the full snapshot history, so a single viral week doesn't dominate. Repos high here *and* in the recent board are compounding, not spiking.

| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |
|---|---|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | **771.0** | +43,949 | 268,683 | Shell | 78 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **633.5** | +36,109 | 227,042 | Python | 85 |
| 3 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | **609.2** | +34,723 | 38,040 | C | 75 |
| 4 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **549.6** | +31,325 | 162,852 | TypeScript | 99 |
| 5 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **484.9** | +27,639 | 139,092 | Shell | 65 |
| 6 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **474.2** | +27,028 | 200,508 | — | 26 |
| 7 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **473.2** | +26,970 | 125,449 | Rust | 77 |
| 8 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | **441.7** | +25,179 | 96,694 | JavaScript | 72 |
| 9 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **440.6** | +25,117 | 238,551 | JavaScript | 85 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **421.6** | +24,032 | 114,470 | Python | 94 |
| 11 | [usestrix/strix](https://github.com/usestrix/strix) | **415.4** | +23,678 | 49,624 | Python | 76 |
| 12 | [earendil-works/pi](https://github.com/earendil-works/pi) | **412.1** | +23,488 | 85,266 | TypeScript | 90 |
| 13 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **404.4** | +23,051 | 537,480 | Markdown | 50 |
| 14 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **377.6** | +21,522 | 194,722 | TypeScript | 83 |
| 15 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **369.5** | +21,064 | 172,207 | Python | 61 |
| 16 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | **367.1** | +20,927 | 84,381 | TypeScript | 87 |
| 17 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | **360.1** | +20,527 | 77,872 | TypeScript | 80 |
| 18 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | **349.5** | +19,920 | 49,694 | TypeScript | 87 |
| 19 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **324.9** | +18,517 | 493,398 | — | 52 |
| 20 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | **313.9** | +17,890 | 65,312 | C | 78 |

## Emerging themes

The boards above are computed; this section is interpretation. Each theme groups movers that are rising for the same underlying reason.

### Skills as the packaging format for agent behaviour

_The single loudest signal in this dataset. A year ago you configured an agent with a prompt; now behaviour ships as a versioned, installable *skill* bundle — and the repos distributing those bundles are growing faster than the agents that consume them. Note what this implies: the moat is moving from the model to the instruction layer._

- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 98,197★ · +11,912★ in 18d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 268,683★ · +10,872★ in 18d  
  An agentic skills framework & software development methodology that works.
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 238,551★ · +7,200★ in 18d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 114,470★ · +6,522★ in 18d  
  An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 200,508★ · +6,004★ in 18d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 139,092★ · +4,851★ in 18d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 166,884★ · +4,066★ in 18d  
  Public repository for Agent Skills
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 126,792★ · +3,736★ in 18d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 51,848★ · +1,388★ in 18d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 64,138★ · +1,004★ in 18d  
  from vibe coding to agentic engineering - practice makes claude perfect

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 103,983★ · +12,167★ in 18d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 17,450★ · +8,301★ in 18d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 38,040★ · +4,982★ in 18d  
  High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 65,312★ · +4,284★ in 18d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 77,872★ · +2,619★ in 18d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 89,998★ · +2,086★ in 18d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 14,515★ · +1,978★ in 18d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 29,847★ · +1,296★ in 18d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine.
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 4,847★ · +1,047★ in 18d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 2,294★ · +878★ in 18d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,307★ · +142★ in 18d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 23,168★ · +6,574★ in 18d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 29,885★ · +6,130★ in 18d  
  AirLLM 70B inference with single 4GB GPU
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 123,011★ · +2,005★ in 18d  
  LLM inference in C/C++
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,072★ · +354★ in 18d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,495★ · +59★ in 18d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 23,168★ · +6,574★ in 18d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 96,694★ · +5,744★ in 18d  
  🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 65,384★ · +4,895★ in 18d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 44,770★ · +3,703★ in 18d  
  Use Claude Code, Codex and Pi for free from your terminal, app, IDE, or phone like OpenClaw (voice supported)
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 75,183★ · +3,245★ in 18d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 85,266★ · +12,268★ in 18d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 227,042★ · +9,598★ in 18d  
  The agent that grows with you
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 16,337★ · +7,219★ in 18d  
  The most RAM efficient harness
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 194,722★ · +7,081★ in 18d  
  The open source coding agent.
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 125,449★ · +6,353★ in 18d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **[openai/codex](https://github.com/openai/codex)** · 104,648★ · +4,803★ in 18d  
  Lightweight coding agent that runs in your terminal
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 44,689★ · +3,556★ in 18d  
  Assign issues to Claude Code, Codex, Cursor, and 17 more coding agents like teammates — open-source and self-hostable.
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 140,599★ · +2,209★ in 18d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 79,512★ · +2,089★ in 18d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 67,279★ · +2,042★ in 18d  
  🌊 The original agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 83,392★ · +2,029★ in 18d  
  🙌 OpenHands: AI-Driven Development
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 12,640★ · +1,749★ in 18d  
  Orchestrate multiple coding agents from desktop and mobile
- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 75,827★ · +1,587★ in 18d  
  The open-source app everyone uses to manage agents at work
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 67,452★ · +1,235★ in 18d  
  omo/lazycodex: The coding agent for tokenmaxxers;the one and only agent harness for complex codebases. For your Codex, for your OpenCode
- **[vercel/eve](https://github.com/vercel/eve)** · 4,450★ · +559★ in 18d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[usestrix/strix](https://github.com/usestrix/strix)** · 49,624★ · +6,867★ in 18d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 49,694★ · +6,018★ in 18d  
  The open-source AI voice studio. Clone, dictate, create.
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 32,938★ · +4,801★ in 18d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 30,230★ · +4,798★ in 18d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 39,941★ · +3,607★ in 18d  
  Write HTML. Render video. Built for agents.
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 28,439★ · +2,762★ in 18d  
  Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. Understand How to write meeting minutes
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 108,197★ · +2,552★ in 18d  
  🌐 Make websites accessible for AI agents. Automate tasks online with ease.
- **[santifer/career-ops](https://github.com/santifer/career-ops)** · 63,159★ · +2,511★ in 18d  
  Open-source AI job search: scan job portals, evaluate listings with a structured A-F rubric into a 1.0-5.0 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, Codex, OpenCode, Antigravity…)
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 96,073★ · +2,327★ in 18d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 17,179★ · +821★ in 18d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 114,470★ · +6,522★ in 18d  
  An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 84,381★ · +4,547★ in 18d  
  🎨 The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / Gemini / OpenCode / Qwen & 20+ CLIs via BYOK.
- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 107,184★ · +3,937★ in 18d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.
- **[github/spec-kit](https://github.com/github/spec-kit)** · 125,772★ · +3,264★ in 18d  
  💫 Toolkit to help you get started with Spec-Driven Development

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | 81,508 | TypeScript | Hot | The open-source CapCut alternative |
| [SimplifyJobs/Summer2027-Internships](https://github.com/SimplifyJobs/Summer2027-Internships) | 46,073 | Python | Classic | Summer 2026 software engineering, data science, AI, quant, product management, and h… |
| [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 45,875 | Python | Hot | World's first open-source, agentic video production system. 12 production pipelines,… |
| [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 42,447 | TypeScript | Hot | Never stop coding. Free MIT AI gateway: one endpoint, 290+ providers (90+ free), 500… |
| [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | 31,504 | JavaScript | Declining | Use Codex from Claude Code to review code or delegate tasks. |
| [openai/openai-python](https://github.com/openai/openai-python) | 31,317 | Python | Classic | The official Python library for the OpenAI API |
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | 30,684 | TypeScript | Hot | The job search that runs on your machine. AI job application framework built on Clau… |
| [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | 29,340 | Python | Hot | Local-first code intelligence graph for MCP and CLI. Builds a persistent map of your… |
| [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | 29,186 | Python | Mature | Python scraper based on AI |
| [herdrdev/herdr](https://github.com/herdrdev/herdr) | 25,579 | Rust | Hot | the runtime your coding agents live on |
| [block/buzz](https://github.com/block/buzz) | 24,879 | Rust | Hot | A hive mind communication platform |
| [krayin/laravel-crm](https://github.com/krayin/laravel-crm) | 23,643 | PHP | Classic | Krayin CRM is Free & Open Source CRM Built with Laravel for Customer, Lead, and Sale… |
| [snarktank/ralph](https://github.com/snarktank/ralph) | 21,406 | TypeScript | Declining | Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are co… |
| [chidiwilliams/buzz](https://github.com/chidiwilliams/buzz) | 20,832 | Python | Classic | Buzz transcribes and translates audio offline on your personal computer. Powered by … |
| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 19,502 | Go | Hot | Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an auto… |
| [openai/tiktoken](https://github.com/openai/tiktoken) | 18,939 | Python | Mature | tiktoken is a fast BPE tokeniser for use with OpenAI's models. |
| [react/yoga](https://github.com/react/yoga) | 18,859 | C++ | Classic | Yoga is an embeddable layout engine targeting web standards. |
| [square/picasso](https://github.com/square/picasso) | 18,815 | Kotlin | Abandoned | A powerful image downloading and caching library for Android |
| [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | 18,105 | Python | Hot | A skill to stop your coding agent from burying the answer. ADHD-friendly output. |
| [gnachman/iTerm2](https://github.com/gnachman/iTerm2) | 17,912 | Objective-C | Classic | iTerm2 is a terminal emulator for Mac OS X that does amazing things. |
| [danielmiessler/LifeOS](https://github.com/danielmiessler/LifeOS) | 17,239 | TypeScript | Hot | ⛰️A General Hill-climbing AI harness that helps you move from Current State to Ideal… |
| [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) | 14,767 | TypeScript | Classic | The Open Context Layer for Data and AI ,  OpenMetadata is the open platform for buil… |
| [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | 14,418 | Python | Mature | Give Claude the ability to watch any video. /watch downloads, extracts frames, trans… |
| [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | 14,326 | Python | Mature | TensorRT LLM provides users with an easy-to-use Python API to define Large Language … |
| [github-linguist/linguist](https://github.com/github-linguist/linguist) | 13,623 | Ruby | Classic | Language Savant. If your repository's language is being reported incorrectly, send u… |
| [huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech) | 11,564 | Python | Mature | Build local voice agents with open-source models |
| [NVIDIA/cosmos](https://github.com/NVIDIA/cosmos) | 11,410 | Jupyter Notebook | Hot | NVIDIA Cosmos is an open platform of world models, datasets, and tools that enables … |
| [openai/openai-node](https://github.com/openai/openai-node) | 11,100 | TypeScript | Classic | Official JavaScript / TypeScript library for the OpenAI API |
| [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | 10,465 | Python | Declining | Native and Compact Structured Latents for 3D Generation |
| [bluewave-labs/Checkmate](https://github.com/bluewave-labs/Checkmate) | 10,430 | TypeScript | Mature | Checkmate is an open-source, self-hosted tool designed to track and monitor server h… |
| [pymupdf/PyMuPDF](https://github.com/pymupdf/PyMuPDF) | 10,424 | Python | Classic | PyMuPDF is a high performance Python library for data extraction, analysis, conversi… |
| [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | 10,174 | Python | Hot | Build your own AI SRE agents. The open source toolkit for the AI era. |
| [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | 10,161 | Python | Hot | Rebuild the object in a reference image as a code-only, procedural, quality-gated, a… |
| [openscad/openscad](https://github.com/openscad/openscad) | 9,901 | C++ | Classic | OpenSCAD - The Programmers Solid 3D CAD Modeller |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | 9,714 | Python | Hot | The Open-Source Elevenlabs alternative AI Voice Clone, Dub, Dictate, Transcribe, Aud… |
| [utkarshdalal/GameNative](https://github.com/utkarshdalal/GameNative) | 9,583 | Kotlin | Hot | Native PC gaming with Steam, Epic, GOG and Amazon integrations on Android |
| [anchore/syft](https://github.com/anchore/syft) | 9,366 | Go | Classic | CLI tool and library for generating a Software Bill of Materials from container imag… |
| [studio-dots-ai/dots.ocr](https://github.com/studio-dots-ai/dots.ocr) | 9,059 | Python | Declining | Multilingual Document Layout Parsing in a Single Vision-Language Model |
| [QwenAudio/SenseVoice](https://github.com/QwenAudio/SenseVoice) | 9,032 | C | Mature | Open-source SenseVoiceSmall model for Mandarin, Cantonese, English, Japanese, and Ko… |
| [Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) | 8,852 | Go | Hot | Agent IDE that enables you to manage fleets of coding agents. It comes with an agent… |
| _…and 96 more_ | | | | |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 57-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [arman-bd/guppylm](https://github.com/arman-bd/guppylm) | 1.4 | 0.1 | **4%** of prior pace | 3mo ago | Declining |
| [https-deeplearning-ai/deeplearning-ai](https://github.com/https-deeplearning-ai/deeplearning-ai) | 2.5 | 0.2 | **7%** of prior pace | 1mo ago | Rising |
| [deeplethe/forkd](https://github.com/deeplethe/forkd) | 9.9 | 1.2 | **12%** of prior pace | 5d ago | Hot |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 98.7 | 13.2 | **13%** of prior pace | 0d ago | Hot |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | 15.3 | 2.3 | **15%** of prior pace | 1mo ago | Rising |
| [openai/openai-cs-agents-demo](https://github.com/openai/openai-cs-agents-demo) | 2.6 | 0.5 | **19%** of prior pace | 7mo ago | Declining |
| [StarTrail-org/LEANN](https://github.com/StarTrail-org/LEANN) | 15.2 | 3.6 | **23%** of prior pace | 7d ago | Hot |
| [hashicorp/consul](https://github.com/hashicorp/consul) | 1.6 | 0.4 | **24%** of prior pace | 0d ago | Classic |
| [allenai/olmocr](https://github.com/allenai/olmocr) | 33.2 | 8.3 | **25%** of prior pace | 4mo ago | Declining |
| [jujumilk3/leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts) | 4.5 | 1.3 | **28%** of prior pace | 1mo ago | Mature |
| [campfirein/byterover-cli](https://github.com/campfirein/byterover-cli) | 1.6 | 0.4 | **28%** of prior pace | 1mo ago | Hot |
| [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | 37.7 | 10.8 | **29%** of prior pace | 15d ago | Rising |
| [itshover/itshover](https://github.com/itshover/itshover) | 5.8 | 1.7 | **29%** of prior pace | 15d ago | Rising |
| [FareedKhan-dev/all-rl-algorithms](https://github.com/FareedKhan-dev/all-rl-algorithms) | 4.8 | 1.4 | **30%** of prior pace | 11mo ago | Declining |
| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | 126.3 | 38.2 | **30%** of prior pace | 1d ago | Hot |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **15 of the graph's 33 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 0** (7): `earendil-works/pi`, `1jehuang/jcode`, `nextlevelbuilder/ui-ux-pro-max-skill`, `farion1231/cc-switch`, `nexu-io/open-design`, `colbymchenry/codegraph`, `anthropics/skills`
- **Community 9** (5): `DietrichGebert/ponytail`, `NousResearch/hermes-agent`, `affaan-m/ECC`, `JuliusBrussee/caveman`, `ComposioHQ/awesome-claude-skills`
- **Community 4** (5): `codecrafters-io/build-your-own-x`, `sindresorhus/awesome`, `jamiepine/voicebox`, `DigitalPlatDev/FreeDomain`, `awesome-selfhosted/awesome-selfhosted`
- **Community 3** (4): `firecrawl/firecrawl`, `TencentCloud/TencentDB-Agent-Memory`, `Shubhamsaboo/awesome-llm-apps`, `harry0703/MoneyPrinterTurbo`
- **Community 11** (3): `obra/superpowers`, `msitarzewski/agency-agents`, `VoltAgent/awesome-design-md`
- **Community 20** (3): `openai/codex`, `yt-dlp/yt-dlp`, `unclecode/crawl4ai`
- **Community 10** (2): `microsoft/AI-For-Beginners`, `microsoft/markitdown`
- **Community 23** (2): `usestrix/strix`, `donnemartin/system-design-primer`
- **Community 13** (2): `JustVugg/colibri`, `lyogavin/airllm`
- **Community 1** (2): `HKUDS/DeepTutor`, `HKUDS/Vibe-Trading`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `HKUDS/Vibe-Trading` ⇄ `HKUDS/DeepTutor` (w=0.597) — authors: santhreal
- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `DietrichGebert/ponytail` ⇄ `JuliusBrussee/caveman` (w=0.341) — topics: claude, claude-code, llm, prompt-engineering; authors: ousamabenyounes
- `DeusData/codebase-memory-mcp` ⇄ `Graphify-Labs/graphify` (w=0.300) — topics: claude-code, code-analysis, developer-tools, knowledge-graph
- `Graphify-Labs/graphify` ⇄ `ComposioHQ/awesome-claude-skills` (w=0.291) — topics: claude-code, codex, antigravity, ai-agents
- `NousResearch/hermes-agent` ⇄ `affaan-m/ECC` (w=0.263) — topics: ai-agents, llm, anthropic, claude
- `awesome-selfhosted/awesome-selfhosted` ⇄ `sindresorhus/awesome` (w=0.182) — topics: awesome, awesome-list
- `nextlevelbuilder/ui-ux-pro-max-skill` ⇄ `ComposioHQ/awesome-claude-skills` (w=0.175) — topics: antigravity, claude, claude-code, codex
- `DigitalPlatDev/FreeDomain` ⇄ `codecrafters-io/build-your-own-x` (w=0.083) — topics: free
- `JustVugg/colibri` ⇄ `DeusData/codebase-memory-mcp` (w=0.050)

**What the risers are written in** — language mix of the top 40 movers:

- **Python** — 15
- **TypeScript** — 6
- **—** — 5
- **JavaScript** — 3
- **Rust** — 3
- **C** — 3
- **Shell** — 2
- **Jupyter Notebook** — 2

## Methodology & caveats

- **Source**: `data/snapshots/*.json` diffed against `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-08-07 (5 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. Per-day normalization makes the boards comparable, but a 1-day window amplifies noise, so treat short-window figures as directional.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 1,340 · Window: 2026-07-20 → 2026-08-07 (18d) · Snapshot: 2026-08-07T21:10:17.796Z</sub>
