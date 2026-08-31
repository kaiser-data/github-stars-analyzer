# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 1,900 starred repos (snapshot `2026-08-31T12:10:08.018Z`), cross-referenced with the repo-similarity graph (1,900 nodes / 6,181 edges, 37 communities).
>
> Generated 2026-08-31 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

![Biggest star gains (20d)](assets/trending-now-top-tools.svg)

![Repos by movement type](assets/trending-now-categories.svg)


## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-08-11` → `2026-08-31` (**20 days**), covering the **1,584 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-08-31` (**81 days**).
  - The immediately preceding snapshot (`2026-08-29`) is only 2 days before this one — too short to separate signal from noise — so the baseline was widened to the newest snapshot at least 7 days back.
- **1,358 repos gained stars** in the recent window, adding **839,980★** between them.
- **316 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-08-11 → 2026-08-31, 20d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+19,647** | 982.4 | 117,844 | JavaScript | Hot | very active |
| 2 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **+18,586** | 929.3 | 473,534 | Python | Classic | very active |
| 3 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **+16,885** | 844.2 | 118,972 | Python | Mature | very active |
| 4 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | **+16,522** | 826.1 | 58,969 | TypeScript | Hot | very active |
| 5 | [openai/codex](https://github.com/openai/codex) | **+15,704** | 785.2 | 120,352 | Rust | Hot | very active |
| 6 | [earendil-works/pi](https://github.com/earendil-works/pi) | **+14,543** | 727.1 | 99,809 | TypeScript | Hot | very active |
| 7 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | **+13,141** | 657.0 | 19,350 | TypeScript | Hot | very active |
| 8 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **+11,786** | 589.3 | 174,638 | TypeScript | Mature | very active |
| 9 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **+11,707** | 585.4 | 238,749 | Python | Hot | very active |
| 10 | [obra/superpowers](https://github.com/obra/superpowers) | **+11,202** | 560.1 | 279,885 | Shell | Hot | very active |
| 11 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **+10,087** | 504.4 | 149,179 | Shell | Hot | very active |
| 12 | [usestrix/strix](https://github.com/usestrix/strix) | **+9,997** | 499.9 | 59,621 | Python | Hot | very active |
| 13 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | **+9,182** | 459.1 | 11,476 | Python | Hot | very active |
| 14 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | **+8,973** | 448.6 | 54,848 | Python | Hot | very active |
| 15 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **+8,913** | 445.6 | 123,383 | Python | Hot | very active |
| 16 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | **+8,863** | 443.1 | 112,846 | Python | Hot | very active |
| 17 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | **+8,576** | 428.8 | 92,957 | — | Hot | very active |
| 18 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **+8,517** | 425.9 | 209,025 | — | Declining | slowing |
| 19 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | **+8,316** | 415.8 | 33,895 | Rust | Hot | very active |
| 20 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **+8,190** | 409.5 | 501,588 | — | Mature | active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 20-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [MakazhanAlpamys/Soup](https://github.com/MakazhanAlpamys/Soup) | **+934%** | +3,680 | 4,074 | Fine-tune LLMs from one YAML. Layer streaming trains an 8B model on a 4 GB laptop GPU. |
| 2 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | **+400%** | +9,182 | 11,476 | Graph-Native Infrastructure for Context and Accountable AI Systems |
| 3 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | **+212%** | +13,141 | 19,350 | A self-improving RLM agent for coding workflows and long-running autonomous tasks. |
| 4 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | **+166%** | +6,141 | 9,836 | 14MB foundation model for tiny devices; phones, wearables, smart home, and robots. |
| 5 | [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) | **+114%** | +3,665 | 6,885 | A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB of RAM. P… |
| 6 | [vitali87/code-graph-rag](https://github.com/vitali87/code-graph-rag) | **+91%** | +2,329 | 4,890 | The ultimate RAG for your monorepo. Query, understand, and edit multi-language codebases… |
| 7 | [Prism-Shadow/penguin-harness](https://github.com/Prism-Shadow/penguin-harness) | **+88%** | +861 | 1,840 | 🐧 Harness for RSI. Let AI Build AI. Multi-Agent Auto-Dev Platform. Everything is Transpa… |
| 8 | [Anakin-Inc/anakin](https://github.com/Anakin-Inc/anakin) | **+67%** | +997 | 2,494 | Open-source web scraping API. Turn any website into clean markdown or structured JSON. A… |
| 9 | [cloudflare/computer](https://github.com/cloudflare/computer) | **+60%** | +3,327 | 8,850 | Give your agent a computer 👾 |
| 10 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | **+45%** | +7,913 | 25,363 | TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations,… |
| 11 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | **+44%** | +4,495 | 14,656 | Rebuild the object in a reference image as a code-only, procedural, quality-gated, anima… |
| 12 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | **+43%** | +7,834 | 25,939 | A skill to stop your coding agent from burying the answer. ADHD-friendly output. |
| 13 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | **+41%** | +162 | 555 | Light, fluffy, and always free - Local Azure Emulator |
| 14 | [bjarneo/cliamp](https://github.com/bjarneo/cliamp) | **+40%** | +1,122 | 3,895 | cliamp - Terminal music player inspired by winamp |
| 15 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | **+39%** | +16,522 | 58,969 | Never stop coding. Free MIT AI gateway: one endpoint, 350 providers (90+ free), 1200+ mo… |
| 16 | [hi-godot/godot-ai](https://github.com/hi-godot/godot-ai) | **+37%** | +551 | 2,039 | Production-grade MCP server and AI tools for the Godot engine. A Snap to install. Totall… |
| 17 | [zzet/gortex](https://github.com/zzet/gortex) | **+36%** | +404 | 1,511 | High-performance code-intelligence engine for AI agents and IDE, supports 257 languages,… |
| 18 | [sophiamyang/finger-frame-effect-ai](https://github.com/sophiamyang/finger-frame-effect-ai) | **+35%** | +259 | 989 | — |
| 19 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | **+34%** | +7,037 | 27,470 | Turn any technical book PDF into a Claude Code skill — ready to study, reference, and us… |
| 20 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | **+33%** | +8,316 | 33,895 | the runtime your coding agents live on |

## Sustained climbers — long run (2026-06-11 → 2026-08-31, 81d)

Averaged over the full snapshot history, so a single viral week doesn't dominate. Repos high here *and* in the recent board are compounding, not spiking.

| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |
|---|---|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | **680.9** | +55,151 | 279,885 | Shell | 78 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **590.3** | +47,816 | 238,749 | Python | 80 |
| 3 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **532.2** | +43,111 | 174,638 | TypeScript | 89 |
| 4 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | **470.3** | +38,098 | 41,415 | C | 75 |
| 5 | [earendil-works/pi](https://github.com/earendil-works/pi) | **469.5** | +38,031 | 99,809 | TypeScript | 85 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **465.8** | +37,726 | 149,179 | Shell | 64 |
| 7 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **438.8** | +35,545 | 209,025 | — | 24 |
| 8 | [usestrix/strix](https://github.com/usestrix/strix) | **415.7** | +33,675 | 59,621 | Python | 81 |
| 9 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **406.7** | +32,945 | 123,383 | Python | 96 |
| 10 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **405.9** | +32,875 | 118,972 | Python | 85 |
| 11 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **403.4** | +32,673 | 473,534 | Python | 65 |
| 12 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **393.3** | +31,861 | 130,340 | Rust | 77 |
| 13 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **388.9** | +31,504 | 244,938 | JavaScript | 79 |
| 14 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | **376.0** | +30,454 | 101,969 | Go | 78 |
| 15 | [openai/codex](https://github.com/openai/codex) | **369.1** | +29,894 | 120,352 | Rust | 94 |
| 16 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **367.7** | +29,783 | 544,212 | Markdown | 48 |
| 17 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **364.4** | +29,519 | 202,719 | TypeScript | 83 |
| 18 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | **364.2** | +29,503 | 92,957 | — | 82 |
| 19 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **329.7** | +26,707 | 501,588 | — | 60 |
| 20 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **323.0** | +26,166 | 177,309 | Python | 63 |

## Emerging themes

The boards above are computed; this section is interpretation. Each theme groups movers that are rising for the same underlying reason.

### Skills as the packaging format for agent behaviour

_The single loudest signal in this dataset. A year ago you configured an agent with a prompt; now behaviour ships as a versioned, installable *skill* bundle — and the repos distributing those bundles are growing faster than the agents that consume them. Note what this implies: the moat is moving from the model to the instruction layer._

- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 117,844★ · +19,647★ in 20d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 279,885★ · +11,202★ in 20d  
  An agentic skills framework & software development methodology that works.
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 149,179★ · +10,087★ in 20d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 123,383★ · +8,913★ in 20d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 209,025★ · +8,517★ in 20d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · 25,939★ · +7,834★ in 20d  
  A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 244,938★ · +6,387★ in 20d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 172,734★ · +5,850★ in 20d  
  Public repository for Agent Skills
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 130,541★ · +3,749★ in 20d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 53,272★ · +1,424★ in 20d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 65,417★ · +1,279★ in 20d  
  from vibe coding to agentic engineering - practice makes claude perfect

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 11,476★ · +9,182★ in 20d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 112,846★ · +8,863★ in 20d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 25,363★ · +7,913★ in 20d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 68,800★ · +3,488★ in 20d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 41,415★ · +3,375★ in 20d  
  High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 81,154★ · +3,282★ in 20d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 92,714★ · +2,716★ in 20d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 6,275★ · +1,428★ in 20d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 15,895★ · +1,380★ in 20d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 30,367★ · +520★ in 20d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine.
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,456★ · +149★ in 20d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 126,473★ · +3,462★ in 20d  
  LLM inference in C/C++
- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 33,289★ · +3,404★ in 20d  
  AirLLM 70B inference with single 4GB GPU
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 26,501★ · +3,333★ in 20d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,341★ · +269★ in 20d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,533★ · +38★ in 20d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 52,128★ · +7,358★ in 20d  
  Use Claude Code, Codex, Pi, and OpenCode and more for free (1.3B+ free tokens) from your terminal, app, IDE, or phone like OpenClaw (voice supported + ToS friendly)
- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 101,969★ · +5,275★ in 20d  
  🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 26,501★ · +3,333★ in 20d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 78,015★ · +2,832★ in 20d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 68,158★ · +2,774★ in 20d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[openai/codex](https://github.com/openai/codex)** · 120,352★ · +15,704★ in 20d  
  Lightweight coding agent that runs in your terminal
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 99,809★ · +14,543★ in 20d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 238,749★ · +11,707★ in 20d  
  The agent that grows with you
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 202,719★ · +7,997★ in 20d  
  The open source coding agent.
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 130,340★ · +4,891★ in 20d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 79,736★ · +3,909★ in 20d  
  The open-source app everyone uses to manage agents at work
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 48,377★ · +3,688★ in 20d  
  Make humans and AI agents work as one team — open-source and self-hostable.
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 15,603★ · +2,963★ in 20d  
  Orchestrate multiple coding agents from desktop and mobile
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 143,538★ · +2,939★ in 20d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 69,923★ · +2,644★ in 20d  
  🌊 The original agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 18,864★ · +2,527★ in 20d  
  The most RAM efficient harness
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 85,738★ · +2,346★ in 20d  
  🙌 OpenHands: AI-Driven Development
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 81,168★ · +1,656★ in 20d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 68,547★ · +1,095★ in 20d  
  omo/lazycodex: The coding agent for tokenmaxxers;the one and only agent harness for complex codebases. For your Codex, for your OpenCode
- **[vercel/eve](https://github.com/vercel/eve)** · 4,882★ · +432★ in 20d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[usestrix/strix](https://github.com/usestrix/strix)** · 59,621★ · +9,997★ in 20d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[santifer/career-ops](https://github.com/santifer/career-ops)** · 69,537★ · +6,378★ in 20d  
  Open-source AI job search: scan job portals, evaluate listings into a structured A-H report with a global 1-5 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, Codex, OpenCode, Antigravity…)
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 101,945★ · +5,872★ in 20d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 38,004★ · +5,066★ in 20d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 111,814★ · +3,617★ in 20d  
  🌐 Make websites accessible for AI agents. Automate tasks online with ease.
- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 43,295★ · +3,354★ in 20d  
  Write HTML. Render video. Built for agents.
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 51,931★ · +2,237★ in 20d  
  The open-source AI voice studio. Clone, dictate, create.
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 32,152★ · +1,922★ in 20d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 30,138★ · +1,699★ in 20d  
  Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. Understand How to write meeting minutes
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 17,430★ · +251★ in 20d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 123,383★ · +8,913★ in 20d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 92,957★ · +8,576★ in 20d  
  🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK.
- **[github/spec-kit](https://github.com/github/spec-kit)** · 132,434★ · +6,662★ in 20d  
  💫 Toolkit to help you get started with Spec-Driven Development
- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 111,935★ · +4,751★ in 20d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 205,832 | TypeScript | Hot | DeepSeek Harness: Everything is a Plugin. |
| [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 189,468 | Shell | Classic | 🙃   A delightful community-driven (with 2,500+ contributors) framework for managing … |
| [microsoft/terminal](https://github.com/microsoft/terminal) | 104,753 | C++ | Classic | The new Windows Terminal and the original Windows console host, all in the same plac… |
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 94,985 | Python | Declining | AI agents running research on single-GPU nanochat training automatically |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 91,042 | JavaScript | Hot | Production-grade engineering skills for AI coding agents. |
| [junegunn/fzf](https://github.com/junegunn/fzf) | 82,740 | Go | Classic | :cherry_blossom: A command-line fuzzy finder |
| [Eugeny/tabby](https://github.com/Eugeny/tabby) | 74,247 | TypeScript | Classic | A terminal for a more modern age |
| [alacritty/alacritty](https://github.com/alacritty/alacritty) | 65,569 | Rust | Mature | A cross-platform, OpenGL terminal emulator. |
| [warpdotdev/warp](https://github.com/warpdotdev/warp) | 64,674 | Rust | Classic | Warp is an agentic development environment, born out of the terminal. |
| [tldr-pages/tldr](https://github.com/tldr-pages/tldr) | 63,539 | Markdown | Classic | Collaborative cheatsheets for console commands 📚. |
| [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | 60,506 | Zig | Classic | 👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses pl… |
| [sharkdp/bat](https://github.com/sharkdp/bat) | 60,315 | Rust | Classic | A cat(1) clone with wings. |
| [termux/termux-app](https://github.com/termux/termux-app) | 60,071 | Java | Mature | Termux - a terminal emulator application for Android OS extendible by variety of pac… |
| [starship/starship](https://github.com/starship/starship) | 59,685 | Rust | Classic | ☄🌌️  The minimal, blazing-fast, and infinitely customizable prompt for any shell! |
| [stablyai/orca](https://github.com/stablyai/orca) | 57,944 | TypeScript | Hot | Orca is the ADE for working with a fleet of parallel agents. Run any coding agent wi… |
| [Textualize/rich](https://github.com/Textualize/rich) | 57,289 | Python | Mature | Rich is a Python library for rich text and beautiful formatting in the terminal. |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 50,248 | TypeScript | Hot | Chrome DevTools for coding agents |
| [vercel/hyper](https://github.com/vercel/hyper) | 44,711 | TypeScript | Mature | A terminal built on web technologies |
| [sharkdp/fd](https://github.com/sharkdp/fd) | 44,258 | Rust | Classic | A simple, fast and user-friendly alternative to 'find' |
| [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | 43,923 | Jupyter Notebook | Mature | This is a repo with links to everything you'd ever want to learn about data engineer… |
| [sxyazi/yazi](https://github.com/sxyazi/yazi) | 41,827 | Rust | Classic | 💥 Blazing fast terminal file manager written in Rust, based on async I/O. |
| [chubin/cheat.sh](https://github.com/chubin/cheat.sh) | 41,709 | Python | Declining | the only cheat sheet you need |
| [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | 40,876 | Rust | Hot | Open-source coding agent for your terminal, built in Rust and on a journey of contin… |
| [appsmithorg/appsmith](https://github.com/appsmithorg/appsmith) | 40,788 | TypeScript | Classic | Platform to build admin panels, internal tools, and dashboards. Integrates with 25+ … |
| [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | 40,543 | Python | Classic | A community-maintained Python framework for creating mathematical animations. |
| [nushell/nushell](https://github.com/nushell/nushell) | 40,382 | Rust | Classic | A new type of shell |
| [ajeetdsouza/zoxide](https://github.com/ajeetdsouza/zoxide) | 39,082 | Rust | Classic | A smarter cd command. Supports all major shells. |
| [httpie/cli](https://github.com/httpie/cli) | 38,472 | Python | Abandoned | 🥧 HTTPie CLI  — modern, user-friendly command-line HTTP client for the API era. JSON… |
| [Textualize/textual](https://github.com/Textualize/textual) | 37,102 | Python | Classic | The lean application framework for Python.  Build sophisticated user interfaces with… |
| [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | 35,284 | Go | Hot | DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache st… |
| [zellij-org/zellij](https://github.com/zellij-org/zellij) | 35,209 | Rust | Classic | A terminal workspace with batteries included |
| [kovidgoyal/kitty](https://github.com/kovidgoyal/kitty) | 34,703 | Python | Classic | If you live in the terminal, kitty is made for you! Cross-platform, fast, feature-ri… |
| [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | 34,602 | Python | Hot | Self-evolving Context Database for AI Agents. Unify Agent Memory, Knowledge RAG and … |
| [fish-shell/fish-shell](https://github.com/fish-shell/fish-shell) | 34,102 | Rust | Classic | The user-friendly command line shell. |
| [microsoft/WSL](https://github.com/microsoft/WSL) | 33,578 | C++ | Classic | Windows Subsystem for Linux |
| [nicolargo/glances](https://github.com/nicolargo/glances) | 33,486 | Python | Classic | Glances an Eye on your system. A top/htop alternative for GNU/Linux, BSD, macOS and … |
| [ibraheemdev/modern-unix](https://github.com/ibraheemdev/modern-unix) | 33,022 | — | Abandoned | A collection of modern/faster/saner alternatives to common unix commands. |
| [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | 32,452 | Rust | Rising | Algorithm powering the For You feed on X |
| [kingToolbox/WindTerm](https://github.com/kingToolbox/WindTerm) | 32,103 | C | Declining | A professional cross-platform SSH/Sftp/Shell/Telnet/Tmux/Serial terminal. |
| [jumpserver/jumpserver](https://github.com/jumpserver/jumpserver) | 31,479 | Python | Classic | JumpServer is an open-source Privileged Access Management (PAM) platform that provid… |
| _…and 276 more_ | | | | |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 81-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [HeartMuLa/heartlib](https://github.com/HeartMuLa/heartlib) | 1.2 | -2.5 | **-209%** of prior pace | 4mo ago | Declining |
| [axios/axios](https://github.com/axios/axios) | 1.5 | -1.8 | **-123%** of prior pace | 3d ago | Classic |
| [iternal-technologies-partners/blockify-agentic-data-optimization](https://github.com/iternal-technologies-partners/blockify-agentic-data-optimization) | 1.3 | -0.1 | **-8%** of prior pace | 4mo ago | Declining |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 4.1 | -0.1 | **-2%** of prior pace | 5mo ago | Declining |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 71.2 | 7.0 | **10%** of prior pace | 1d ago | Hot |
| [nearai/ironclaw](https://github.com/nearai/ironclaw) | 2.0 | 0.2 | **13%** of prior pace | 0d ago | Hot |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | 11.2 | 1.9 | **17%** of prior pace | 5d ago | Rising |
| [Suvink/cut-it-out](https://github.com/Suvink/cut-it-out) | 3.0 | 0.5 | **17%** of prior pace | 8mo ago | Declining |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 155.2 | 26.0 | **17%** of prior pace | 0d ago | Classic |
| [https-deeplearning-ai/deeplearning-ai](https://github.com/https-deeplearning-ai/deeplearning-ai) | 1.9 | 0.3 | **19%** of prior pace | 2mo ago | Mature |
| [microsoft/fara](https://github.com/microsoft/fara) | 8.6 | 1.7 | **20%** of prior pace | 1mo ago | Rising |
| [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | 28.0 | 5.8 | **21%** of prior pace | 1mo ago | Declining |
| [i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework) | 1.2 | 0.3 | **26%** of prior pace | 3d ago | Mature |
| [allenai/olmocr](https://github.com/allenai/olmocr) | 25.0 | 6.5 | **26%** of prior pace | 5mo ago | Declining |
| [andrewyng/aisuite](https://github.com/andrewyng/aisuite) | 29.7 | 8.0 | **27%** of prior pace | 18d ago | Mature |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **18 of the graph's 37 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 15** (6): `DietrichGebert/ponytail`, `diegosouzapw/OmniRoute`, `nextlevelbuilder/ui-ux-pro-max-skill`, `Graphify-Labs/graphify`, `ayghri/i-have-adhd`, `affaan-m/ECC`
- **Community 2** (5): `earendil-works/pi`, `TencentCloud/TencentDB-Agent-Memory`, `K-Dense-AI/scientific-agent-skills`, `santifer/career-ops`, `JuliusBrussee/caveman`
- **Community 0** (4): `public-apis/public-apis`, `sindresorhus/awesome`, `codecrafters-io/build-your-own-x`, `DigitalPlatDev/FreeDomain`
- **Community 7** (4): `harry0703/MoneyPrinterTurbo`, `NousResearch/hermes-agent`, `obra/superpowers`, `MadsLorentzen/ai-job-search`
- **Community 1** (4): `msitarzewski/agency-agents`, `nexu-io/open-design`, `herdrdev/herdr`, `anomalyco/opencode`
- **Community 19** (2): `usestrix/strix`, `block/buzz`
- **Community 16** (2): `semantica-agi/semantica`, `virgiliojr94/book-to-skill`
- **Community 18** (2): `calesthio/OpenMontage`, `github/spec-kit`
- **Community 9** (2): `Alishahryar1/free-claude-code`, `OpenCut-app/OpenCut`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `NousResearch/hermes-agent` ⇄ `affaan-m/ECC` (w=0.313) — topics: ai-agents, llm, anthropic, claude
- `MadsLorentzen/ai-job-search` ⇄ `santifer/career-ops` (w=0.280) — topics: ai, career, claude-code, job-application
- `calesthio/OpenMontage` ⇄ `unslothai/unsloth` (w=0.269) — topics: agent, ai, image-generation, openai
- `ayghri/i-have-adhd` ⇄ `affaan-m/ECC` (w=0.218) — topics: developer-tools, productivity; authors: Souptik96
- `JuliusBrussee/caveman` ⇄ `santifer/career-ops` (w=0.190) — topics: ai, anthropic, claude, claude-code; authors: github-actions[bot]
- `MadsLorentzen/ai-job-search` ⇄ `NousResearch/hermes-agent` (w=0.186) — topics: ai, ai-agents, claude-code
- `public-apis/public-apis` ⇄ `sindresorhus/awesome` (w=0.168) — topics: resources, lists; authors: morning-verlu
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
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-07-27, 2026-08-07, 2026-08-11, 2026-08-28, 2026-08-29, 2026-08-31 (10 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. The recent window therefore does not always use the immediately preceding snapshot: it uses the newest one at least 7 days back, because a 1-day window amplifies noise far more than it reveals movement. Per-day normalization keeps the boards comparable across refreshes either way.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 1,584 · Window: 2026-08-11 → 2026-08-31 (20d) · Snapshot: 2026-08-31T12:10:08.018Z</sub>
