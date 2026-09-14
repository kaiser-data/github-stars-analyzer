# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 2,159 starred repos (snapshot `2026-09-14T11:08:08.535Z`), cross-referenced with the repo-similarity graph (2,159 nodes / 7,086 edges, 37 communities).
>
> Generated 2026-09-14 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

![Biggest star gains (7d)](assets/trending-now-top-tools.svg)

![Repos by movement type](assets/trending-now-categories.svg)


## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-09-07` → `2026-09-14` (**7 days**), covering the **2,082 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-09-14` (**95 days**).
  - The immediately preceding snapshot (`2026-09-12`) is only 2 days before this one — too short to separate signal from noise — so the baseline was widened to the newest snapshot at least 7 days back.
- **1,610 repos gained stars** in the recent window, adding **304,532★** between them.
- **77 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-09-07 → 2026-09-14, 7d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | **+17,366** | 2480.9 | 44,890 | Python | Hot | very active |
| 2 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | **+8,649** | 1235.6 | 223,346 | TypeScript | Hot | very active |
| 3 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+7,789** | 1112.7 | 28,010 | Python | Rising | very active |
| 4 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+7,589** | 1084.1 | 137,824 | JavaScript | Hot | very active |
| 5 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | **+6,551** | 935.9 | 39,546 | HTML | Hot | very active |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **+5,830** | 832.9 | 258,025 | JavaScript | Hot | very active |
| 7 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | **+5,261** | 751.6 | 49,830 | TypeScript | Hot | very active |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | **+5,133** | 733.3 | 68,263 | TypeScript | Hot | very active |
| 9 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **+4,670** | 667.1 | 183,827 | Python | Hot | very active |
| 10 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | **+3,915** | 559.3 | 30,900 | C | Hot | very active |
| 11 | [obra/superpowers](https://github.com/obra/superpowers) | **+3,829** | 547.0 | 286,443 | Shell | Hot | very active |
| 12 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | **+3,688** | 526.9 | 65,905 | TypeScript | Hot | very active |
| 13 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **+3,154** | 450.6 | 479,881 | Python | Classic | very active |
| 14 | [github/spec-kit](https://github.com/github/spec-kit) | **+2,825** | 403.6 | 136,618 | Python | Hot | very active |
| 15 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | **+2,821** | 403.0 | 105,629 | Python | Mature | very active |
| 16 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | **+2,795** | 399.3 | 72,005 | Python | Hot | very active |
| 17 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **+2,753** | 393.3 | 180,189 | TypeScript | Mature | very active |
| 18 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **+2,489** | 355.6 | 245,317 | Python | Hot | very active |
| 19 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | **+2,443** | 349.0 | 58,921 | Python | Hot | very active |
| 20 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | **+2,398** | 342.6 | 38,356 | Rust | Hot | very active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 7-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [NVIDIA/Personal-AI-Router](https://github.com/NVIDIA/Personal-AI-Router) | **+64%** | +496 | 1,274 | Router that virtually distributes inference across connected devices in the home. |
| 2 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | **+63%** | +17,366 | 44,890 | A skill to stop your coding agent from burying the answer. ADHD-friendly output. |
| 3 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+39%** | +7,789 | 28,010 | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voic… |
| 4 | [deeplethe/utopia](https://github.com/deeplethe/utopia) | **+37%** | +1,997 | 7,373 | World's first open-source enterprise world model. |
| 5 | [nateherkai/hyperframes-student-kit](https://github.com/nateherkai/hyperframes-student-kit) | **+32%** | +198 | 811 | Edit videos, reels, and YouTube Shorts with Codex or Claude Code. 14 skills, transcript-… |
| 6 | [trailhq/Graft](https://github.com/trailhq/Graft) | **+30%** | +1,765 | 7,589 | Turbocharge Claude Code, Cursor, Codex, Gemini & every coding agent: faster, cheaper, wi… |
| 7 | [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) | **+30%** | +264 | 1,150 | — |
| 8 | [Anakin-Inc/anakin](https://github.com/Anakin-Inc/anakin) | **+30%** | +827 | 3,607 | Open-source web scraping API. Turn any website into clean markdown or structured JSON. A… |
| 9 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | **+20%** | +6,551 | 39,546 | 38 editorial diagram types for Claude Code, Codex, and Pi. Self-contained HTML + SVG. No… |
| 10 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | **+17%** | +317 | 2,178 | Memory that AI Agents Love! |
| 11 | [Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding) | **+16%** | +222 | 1,574 | WeMM-Embedding is a family of universal multimodal embedding models by the WeChat Vision… |
| 12 | [nateherkai/AIS-OS](https://github.com/nateherkai/AIS-OS) | **+16%** | +190 | 1,371 | AI Operating System starter kit for Claude Code and Codex. Five skills: /onboard, /audit… |
| 13 | [huggingface/Repo2RLEnv](https://github.com/huggingface/Repo2RLEnv) | **+16%** | +82 | 592 | Convert any Repo into an RL Environment |
| 14 | [Jwuthri/Tracely-ai](https://github.com/Jwuthri/Tracely-ai) | **+16%** | +195 | 1,411 | Trace-native CI/CD for AI agents — production failures become regression tests that bloc… |
| 15 | [lucienhuangfu/eLLM](https://github.com/lucienhuangfu/eLLM) | **+15%** | +76 | 590 | eLLM: Run Long-Horizon Inference Faster on CPUs Than on GPUs |
| 16 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | **+15%** | +574 | 4,470 | Open source local inference engine. It runs models on the hardware you already have, whe… |
| 17 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | **+15%** | +3,915 | 30,900 | Run frontier MoE models on hardware you already own — pure C, zero deps, experts streame… |
| 18 | [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | **+14%** | +729 | 5,870 | The secure, validated skill registry for professional AI coding agents. Extend Antigravi… |
| 19 | [MakazhanAlpamys/Soup](https://github.com/MakazhanAlpamys/Soup) | **+14%** | +792 | 6,399 | Fine-tune LLMs from one YAML. Layer streaming trains an 8B model on a 4 GB laptop GPU. |
| 20 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | **+14%** | +815 | 6,744 | Solution for long term memory for agent coding CLIs and to facilitate handoff between di… |

## Sustained climbers — long run (2026-06-11 → 2026-09-14, 95d)

Averaged over the full snapshot history, so a single viral week doesn't dominate. Repos high here *and* in the recent board are compounding, not spiking.

| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |
|---|---|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | **649.6** | +61,709 | 286,443 | Shell | 78 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **572.5** | +54,384 | 245,317 | Python | 75 |
| 3 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **512.2** | +48,662 | 180,189 | TypeScript | 89 |
| 4 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **469.4** | +44,591 | 258,025 | JavaScript | 79 |
| 5 | [earendil-works/pi](https://github.com/earendil-works/pi) | **454.4** | +43,170 | 104,948 | TypeScript | 90 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **429.1** | +40,765 | 152,218 | Shell | 58 |
| 7 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | **419.6** | +39,864 | 43,181 | C | 75 |
| 8 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **414.7** | +39,398 | 212,878 | — | 23 |
| 9 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **410.7** | +39,020 | 479,881 | Python | 70 |
| 10 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **393.4** | +37,377 | 123,474 | Python | 80 |
| 11 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **390.1** | +37,058 | 127,496 | Python | 97 |
| 12 | [usestrix/strix](https://github.com/usestrix/strix) | **383.0** | +36,386 | 62,332 | Python | 80 |
| 13 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **361.0** | +34,292 | 132,771 | Rust | 82 |
| 14 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **358.5** | +34,056 | 207,256 | TypeScript | 88 |
| 15 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | **357.5** | +33,961 | 105,476 | Go | 78 |
| 16 | [openai/codex](https://github.com/openai/codex) | **353.2** | +33,554 | 124,012 | Rust | 94 |
| 17 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **344.3** | +32,711 | 547,140 | Markdown | 47 |
| 18 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **344.0** | +32,684 | 183,827 | Python | 90 |
| 19 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | **343.3** | +32,616 | 96,070 | TypeScript | 82 |
| 20 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **326.6** | +31,024 | 505,905 | — | 55 |

## Emerging themes

The boards above are computed; this section is interpretation. Each theme groups movers that are rising for the same underlying reason.

### Skills as the packaging format for agent behaviour

_The single loudest signal in this dataset. A year ago you configured an agent with a prompt; now behaviour ships as a versioned, installable *skill* bundle — and the repos distributing those bundles are growing faster than the agents that consume them. Note what this implies: the moat is moving from the model to the instruction layer._

- **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · 44,890★ · +17,366★ in 7d  
  A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 137,824★ · +7,589★ in 7d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 258,025★ · +5,830★ in 7d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 286,443★ · +3,829★ in 7d  
  An agentic skills framework & software development methodology that works.
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 212,878★ · +2,121★ in 7d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 127,496★ · +1,841★ in 7d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 152,218★ · +1,614★ in 7d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 176,216★ · +1,264★ in 7d  
  Public repository for Agent Skills
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 132,941★ · +1,095★ in 7d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 54,003★ · +371★ in 7d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 65,908★ · +200★ in 7d  
  from vibe coding to agentic engineering - practice makes claude perfect

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 116,573★ · +1,098★ in 7d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 82,642★ · +927★ in 7d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 70,773★ · +871★ in 7d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 43,181★ · +657★ in 7d  
  High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 12,855★ · +615★ in 7d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 26,642★ · +592★ in 7d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 93,826★ · +451★ in 7d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 16,465★ · +276★ in 7d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 30,674★ · +130★ in 7d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine.
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 6,428★ · +59★ in 7d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,525★ · +28★ in 7d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 30,900★ · +3,915★ in 7d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 128,171★ · +835★ in 7d  
  LLM inference in C/C++
- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 34,303★ · +498★ in 7d  
  AirLLM 70B inference with single 4GB GPU
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,403★ · +45★ in 7d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,548★ · +6★ in 7d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 30,900★ · +3,915★ in 7d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 72,005★ · +2,795★ in 7d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 105,476★ · +1,458★ in 7d  
  🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman
- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 54,859★ · +1,289★ in 7d  
  Use Claude Code, Codex, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly)
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 80,272★ · +1,086★ in 7d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 245,317★ · +2,489★ in 7d  
  The agent that grows with you
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 104,948★ · +2,337★ in 7d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[openai/codex](https://github.com/openai/codex)** · 124,012★ · +1,882★ in 7d  
  Lightweight coding agent that runs in your terminal
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 207,256★ · +1,719★ in 7d  
  The open source coding agent.
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 87,845★ · +1,433★ in 7d  
  🙌 OpenHands: AI-Driven Development
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 132,771★ · +1,292★ in 7d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 72,387★ · +1,212★ in 7d  
  🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 17,227★ · +955★ in 7d  
  Orchestrate multiple coding agents from desktop and mobile
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 82,408★ · +741★ in 7d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 49,786★ · +670★ in 7d  
  Make humans and AI agents work as one team — open-source and self-hostable.
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 144,971★ · +647★ in 7d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 80,645★ · +497★ in 7d  
  The open-source app everyone uses to manage agents at work
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 19,666★ · +406★ in 7d  
  The most RAM efficient harness
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 69,029★ · +256★ in 7d  
  OmO: Just type "mass ulw" keyword with your prompt. Now you are the master of graph engineering.
- **[vercel/eve](https://github.com/vercel/eve)** · 5,107★ · +110★ in 7d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 49,830★ · +5,261★ in 7d  
  Write HTML. Render video. Built for agents.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 105,629★ · +2,821★ in 7d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 114,572★ · +1,720★ in 7d  
  Agents that use the browser.
- **[usestrix/strix](https://github.com/usestrix/strix)** · 62,332★ · +1,314★ in 7d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** · 71,544★ · +1,162★ in 7d  
  Open-source AI job search: scan job portals, evaluate listings into a structured A-H report with a global 1-5 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, Codex, OpenCode, Antigravity…)
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 53,169★ · +700★ in 7d  
  The open-source AI voice studio. Clone, dictate, create.
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 39,575★ · +626★ in 7d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 33,408★ · +502★ in 7d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 30,735★ · +298★ in 7d  
  Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. Understand How to write meeting minutes
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 17,631★ · +110★ in 7d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[github/spec-kit](https://github.com/github/spec-kit)** · 136,618★ · +2,825★ in 7d  
  💫 Toolkit to help you get started with Spec-Driven Development
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 127,496★ · +1,841★ in 7d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 96,070★ · +1,498★ in 7d  
  🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK.
- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 115,790★ · +1,244★ in 7d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [facebook/docusaurus](https://github.com/facebook/docusaurus) | 66,245 | TypeScript | Classic | Easy to maintain open source documentation websites. |
| [reactive-resume/reactive-resume](https://github.com/reactive-resume/reactive-resume) | 42,810 | TypeScript | Classic | A one-of-a-kind resume builder that keeps your privacy in mind. Completely secure, c… |
| [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | 34,920 | Python | Hot | Your Personal AI Assistant; easy to install, deploy on your own machine or on the cl… |
| [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | 28,519 | Python | Hot | Community plugin to control Blender 3D with any LLM of your choice |
| [facebook/zstd](https://github.com/facebook/zstd) | 27,853 | C | Classic | Zstandard - Fast real-time compression algorithm |
| [Tencent/weui](https://github.com/Tencent/weui) | 27,416 | HTML | Declining | A UI library by WeChat official design team, includes the most useful widgets/module… |
| [facebook/lexical](https://github.com/facebook/lexical) | 23,851 | TypeScript | Classic | Lexical is an extensible text editor framework that provides excellent reliability, … |
| [Tencent/ncnn](https://github.com/Tencent/ncnn) | 23,813 | C++ | Classic | ncnn is a high-performance neural network inference framework optimized for the mobi… |
| [facebook/relay](https://github.com/facebook/relay) | 18,962 | Rust | Classic | Relay is a JavaScript framework for building data-driven React applications. |
| [facebook/hhvm](https://github.com/facebook/hhvm) | 18,660 | C++ | Classic | A virtual machine for executing programs written in Hack. |
| [Tencent/tinker](https://github.com/Tencent/tinker) | 17,646 | Java | Mature | Tinker is a hot-fix solution library for Android, it supports dex, library and resou… |
| [NVlabs/instant-ngp](https://github.com/NVlabs/instant-ngp) | 17,548 | Cuda | Declining | Instant neural graphics primitives: lightning fast NeRF and more |
| [OrcaSlicer/OrcaSlicer](https://github.com/OrcaSlicer/OrcaSlicer) | 15,683 | C++ | Classic | G-code generator for 3D printers (Bambu, Prusa, Voron, VzBot, RatRig, Creality, etc.… |
| [coderamp-labs/gitingest](https://github.com/coderamp-labs/gitingest) | 15,458 | Python | Declining | Replace 'hub' with 'ingest' in any GitHub URL to get a prompt-friendly extract of a … |
| [Tencent-Hunyuan/Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) | 14,845 | Python | Declining | High-Resolution 3D Assets Generation with Large Scale Hunyuan3D Diffusion Models. |
| [isl-org/Open3D](https://github.com/isl-org/Open3D) | 13,960 | C++ | Classic | Open3D: A Modern Library for 3D Data Processing |
| [Tencent/omi](https://github.com/Tencent/omi) | 13,265 | TypeScript | Mature | Web Components Framework - Web组件框架 |
| [prusa3d/PrusaSlicer](https://github.com/prusa3d/PrusaSlicer) | 9,335 | C++ | Classic | G-code generator for 3D printers (RepRap, Makerbot, Ultimaker etc.) |
| [NVlabs/Sana](https://github.com/NVlabs/Sana) | 9,076 | Python | Mature | SANA: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformer |
| [apple-aiml-research/ml-sharp](https://github.com/apple-aiml-research/ml-sharp) | 8,889 | Python | Declining | Sharp Monocular View Synthesis in Less Than a Second |
| [lnkiai/m3e-canvas](https://github.com/lnkiai/m3e-canvas) | 6,676 | TypeScript | Hot | Sketch Material 3 Expressive screens in the browser and turn them into vibe-coding p… |
| [wjakob/instant-meshes](https://github.com/wjakob/instant-meshes) | 6,216 | C++ | Abandoned | Interactive field-aligned mesh generator |
| [CadQuery/cadquery](https://github.com/CadQuery/cadquery) | 5,764 | Python | Classic | A python parametric CAD scripting framework based on OCCT |
| [truefoundry/trueforge](https://github.com/truefoundry/trueforge) | 5,423 | TypeScript | Hot | The open-source agent harness - the runtime layer that turns an LLM into a working a… |
| [Tencent/teamai-cli](https://github.com/Tencent/teamai-cli) | 4,477 | TypeScript | Hot | Make Every Team AI Native |
| [GVCLab/PersonaLive](https://github.com/GVCLab/PersonaLive) | 3,742 | Python | Declining | [CVPR 2026] PersonaLive! : Expressive Portrait Image Animation for Live Streaming |
| [mikedh/trimesh](https://github.com/mikedh/trimesh) | 3,678 | Python | Classic | Python library for loading and using triangular meshes. |
| [NVlabs/cuda-oxide](https://github.com/NVlabs/cuda-oxide) | 3,318 | Rust | Hot | cuda-oxide is a Rust-to-CUDA compiler that lets you write (SIMT) GPU kernels in safe… |
| [jordan-gibbs/hyperresearch](https://github.com/jordan-gibbs/hyperresearch) | 3,269 | Python | Hot | Agent-driven research knowledge base. Agents collect, search, and synthesize web res… |
| [qdrant/fastembed](https://github.com/qdrant/fastembed) | 3,201 | Python | Classic | Fast, Accurate, Lightweight Python library to make State of the Art Embedding |
| [brennercruvinel/CCPlugins](https://github.com/brennercruvinel/CCPlugins) | 2,779 | Python | Declining | Best Claude Code framework that actually save time. Built by a dev tired of typing "… |
| [BelfrySCAD/BOSL2](https://github.com/BelfrySCAD/BOSL2) | 2,363 | OpenSCAD | Classic | The Belfry OpenScad Library, v2.0.  An OpenSCAD library of shapes, masks, and manipu… |
| [neka-nat/freecad-mcp](https://github.com/neka-nat/freecad-mcp) | 2,281 | Python | Mature | FreeCAD MCP(Model Context Protocol) server |
| [elalish/manifold](https://github.com/elalish/manifold) | 2,270 | C++ | Classic | Geometry library for topological robustness |
| [NVIDIA-NeMo/Nemotron](https://github.com/NVIDIA-NeMo/Nemotron) | 2,053 | Jupyter Notebook | Hot | Developer Asset Hub for NVIDIA Nemotron — A one-stop resource for training recipes, … |
| [fogleman/sdf](https://github.com/fogleman/sdf) | 2,003 | Python | Abandoned | Simple SDF mesh generation in Python |
| [Ultimaker/CuraEngine](https://github.com/Ultimaker/CuraEngine) | 1,850 | C++ | Classic | Powerful, fast and robust engine for converting 3D models into g-code instructions f… |
| [NVlabs/SoL-Pi](https://github.com/NVlabs/SoL-Pi) | 1,826 | TypeScript | Rising | SoL-Pi: Scaling Auto-Research Loops for Efficient Agent Harnesses |
| [libfive/libfive](https://github.com/libfive/libfive) | 1,662 | C++ | Declining | Infrastructure for solid modeling |
| [spotify/portal-ai-plugins](https://github.com/spotify/portal-ai-plugins) | 1,655 | TypeScript | Mature | — |
| _…and 37 more_ | | | | |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 95-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [axios/axios](https://github.com/axios/axios) | 1.5 | -2.4 | **-165%** of prior pace | 1d ago | Classic |
| [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | 1.3 | -0.3 | **-22%** of prior pace | 2mo ago | Declining |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | 1.1 | -0.1 | **-13%** of prior pace | 18d ago | Declining |
| [meta-llama/prompt-ops](https://github.com/meta-llama/prompt-ops) | 2.5 | -0.3 | **-11%** of prior pace | 4mo ago | Declining |
| [iternal-technologies-partners/blockify-agentic-data-optimization](https://github.com/iternal-technologies-partners/blockify-agentic-data-optimization) | 1.1 | 0.0 | **0%** of prior pace | 4mo ago | Declining |
| [Mega4alik/ollm](https://github.com/Mega4alik/ollm) | 1.4 | 0.0 | **0%** of prior pace | 1mo ago | Declining |
| [reflex-dev/reflex](https://github.com/reflex-dev/reflex) | 4.3 | 0.0 | **0%** of prior pace | 0d ago | Classic |
| [morphik-org/morphik-core](https://github.com/morphik-org/morphik-core) | 1.1 | 0.0 | **0%** of prior pace | 5d ago | Mature |
| [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc) | 4.5 | 0.1 | **3%** of prior pace | 2mo ago | Declining |
| [KalyanKS-NLP/llm-engineer-toolkit](https://github.com/KalyanKS-NLP/llm-engineer-toolkit) | 4.1 | 0.1 | **3%** of prior pace | 5d ago | Mature |
| [russellromney/honker](https://github.com/russellromney/honker) | 2.1 | 0.1 | **7%** of prior pace | 0d ago | Hot |
| [microsoft/BitNet](https://github.com/microsoft/BitNet) | 10.0 | 0.7 | **7%** of prior pace | 1mo ago | Mature |
| [supabase/cli](https://github.com/supabase/cli) | 1.5 | 0.1 | **10%** of prior pace | 0d ago | Classic |
| [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | 7.4 | 0.7 | **10%** of prior pace | 1.0y ago | Declining |
| [itshover/itshover](https://github.com/itshover/itshover) | 4.2 | 0.4 | **10%** of prior pace | 1mo ago | Rising |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **15 of the graph's 37 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 16** (11): `ayghri/i-have-adhd`, `DietrichGebert/ponytail`, `cathrynlavery/diagram-design`, `affaan-m/ECC`, `stablyai/orca`, `JustVugg/colibri`, `diegosouzapw/OmniRoute`, `herdrdev/herdr`, `asgeirtj/system_prompts_leaks`, `nextlevelbuilder/ui-ux-pro-max-skill`, `trailhq/Graft`
- **Community 3** (7): `obra/superpowers`, `headroomlabs-ai/headroom`, `NousResearch/hermes-agent`, `calesthio/OpenMontage`, `browser-use/browser-use`, `Shubhamsaboo/awesome-llm-apps`, `unclecode/crawl4ai`
- **Community 19** (3): `public-apis/public-apis`, `sindresorhus/awesome`, `msitarzewski/agency-agents`
- **Community 8** (3): `firecrawl/firecrawl`, `D4Vinci/Scrapling`, `torvalds/linux`
- **Community 5** (3): `earendil-works/pi`, `mksglu/context-mode`, `rohitg00/ai-engineering-from-scratch`
- **Community 1** (2): `heygen-com/hyperframes`, `anomalyco/opencode`
- **Community 24** (2): `TauricResearch/TradingAgents`, `multica-ai/andrej-karpathy-skills`
- **Community 14** (2): `deeplethe/utopia`, `virgiliojr94/book-to-skill`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `asgeirtj/system_prompts_leaks` ⇄ `NousResearch/hermes-agent` (w=0.375) — topics: ai, anthropic, chatgpt, claude
- `trailhq/Graft` ⇄ `affaan-m/ECC` (w=0.363) — topics: ai-agents, claude-code, developer-tools, llm; authors: dependabot[bot]
- `trailhq/Graft` ⇄ `diegosouzapw/OmniRoute` (w=0.326) — topics: ai-agents, claude-code, mcp, anthropic
- `D4Vinci/Scrapling` ⇄ `firecrawl/firecrawl` (w=0.258) — topics: crawler, scraping, web-scraper, web-scraping
- `asgeirtj/system_prompts_leaks` ⇄ `DietrichGebert/ponytail` (w=0.250) — topics: claude, claude-code, llm, prompt-engineering
- `calesthio/OpenMontage` ⇄ `headroomlabs-ai/headroom` (w=0.244) — topics: agent, ai, cursor, openai; authors: anupamme
- `ayghri/i-have-adhd` ⇄ `affaan-m/ECC` (w=0.219) — topics: developer-tools, productivity; authors: wakqasahmed
- `mksglu/context-mode` ⇄ `nextlevelbuilder/ui-ux-pro-max-skill` (w=0.182) — topics: claude, claude-code, codex, copilot
- `mksglu/context-mode` ⇄ `earendil-works/pi` (w=0.175) — authors: github-actions[bot]
- `public-apis/public-apis` ⇄ `sindresorhus/awesome` (w=0.125) — topics: resources, lists
- `cathrynlavery/diagram-design` ⇄ `msitarzewski/agency-agents` (w=0.080) — authors: Mr-Neutr0n, mvanhorn

**What the risers are written in** — language mix of the top 40 movers:

- **Python** — 17
- **TypeScript** — 9
- **JavaScript** — 3
- **Rust** — 3
- **C** — 2
- **Shell** — 2
- **—** — 2
- **HTML** — 1

## Methodology & caveats

- **Source**: `data/snapshots/*.json` diffed against `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-07-27, 2026-08-07, 2026-08-11, 2026-08-28, 2026-08-29, 2026-08-31, 2026-09-06, 2026-09-07, 2026-09-12, 2026-09-14 (14 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. The recent window therefore does not always use the immediately preceding snapshot: it uses the newest one at least 7 days back, because a 1-day window amplifies noise far more than it reveals movement. Per-day normalization keeps the boards comparable across refreshes either way.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 2,082 · Window: 2026-09-07 → 2026-09-14 (7d) · Snapshot: 2026-09-14T11:08:08.535Z</sub>
