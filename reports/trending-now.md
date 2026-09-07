# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 2,087 starred repos (snapshot `2026-09-07T10:42:15.216Z`), cross-referenced with the repo-similarity graph (2,087 nodes / 6,821 edges, 38 communities).
>
> Generated 2026-09-07 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

![Biggest star gains (7d)](assets/trending-now-top-tools.svg)

![Repos by movement type](assets/trending-now-categories.svg)


## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-08-31` → `2026-09-07` (**7 days**), covering the **1,895 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-09-07` (**88 days**).
  - The immediately preceding snapshot (`2026-09-06`) is only 1 day before this one — too short to separate signal from noise — so the baseline was widened to the newest snapshot at least 7 days back.
- **1,494 repos gained stars** in the recent window, adding **270,465★** between them.
- **192 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-08-31 → 2026-09-07, 7d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+12,391** | 1770.1 | 130,235 | JavaScript | Hot | very active |
| 2 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | **+8,865** | 1266.4 | 214,697 | TypeScript | Hot | very active |
| 3 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+7,795** | 1113.6 | 20,221 | Python | Rising | very active |
| 4 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **+7,257** | 1036.7 | 252,195 | JavaScript | Hot | very active |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | **+5,186** | 740.9 | 63,130 | TypeScript | Hot | very active |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **+4,079** | 582.7 | 242,828 | Python | Hot | very active |
| 7 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | **+4,022** | 574.6 | 32,995 | HTML | Hot | very active |
| 8 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | **+3,248** | 464.0 | 62,217 | TypeScript | Hot | very active |
| 9 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **+3,193** | 456.1 | 476,727 | Python | Classic | very active |
| 10 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | **+3,141** | 448.7 | 43,480 | Python | Hot | very active |
| 11 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **+2,818** | 402.6 | 205,537 | TypeScript | Hot | very active |
| 12 | [earendil-works/pi](https://github.com/earendil-works/pi) | **+2,802** | 400.3 | 102,611 | TypeScript | Hot | very active |
| 13 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **+2,798** | 399.7 | 177,436 | TypeScript | Mature | very active |
| 14 | [obra/superpowers](https://github.com/obra/superpowers) | **+2,729** | 389.9 | 282,614 | Shell | Hot | very active |
| 15 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | **+2,629** | 375.6 | 115,475 | Python | Hot | very active |
| 16 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | **+2,611** | 373.0 | 114,546 | — | Declining | active |
| 17 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | **+2,599** | 371.3 | 35,576 | Python | Mature | very active |
| 18 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | **+2,311** | 330.1 | 41,136 | Python | Hot | very active |
| 19 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **+2,285** | 326.4 | 121,257 | Python | Mature | very active |
| 20 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **+2,272** | 324.6 | 125,655 | Python | Hot | very active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 7-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+63%** | +7,795 | 20,221 | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voic… |
| 2 | [MakazhanAlpamys/Soup](https://github.com/MakazhanAlpamys/Soup) | **+38%** | +1,533 | 5,607 | Fine-tune LLMs from one YAML. Layer streaming trains an 8B model on a 4 GB laptop GPU. |
| 3 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | **+23%** | +820 | 4,394 | Open-source AI coworkers that each get a computer of their own: a browser, files and too… |
| 4 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | **+17%** | +840 | 5,681 | A general-purpose AIGC video engine: script to finished film in one pipeline — dramas, a… |
| 5 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | **+15%** | +1,553 | 11,926 | FreeToken brings datacenter-scale model serving to your desktop. Run massive models loca… |
| 6 | [nvidia-isaac/video_to_data](https://github.com/nvidia-isaac/video_to_data) | **+15%** | +70 | 549 | Nvidia Isaac Video to Data Pipeline |
| 7 | [apache/maka](https://github.com/apache/maka) | **+14%** | +601 | 4,873 | Apache Maka (Incubating) is a high-performance agent workspace that keeps a complete rec… |
| 8 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | **+14%** | +4,022 | 32,995 | 38 editorial diagram types for Claude Code, Codex, and Pi. Self-contained HTML + SVG. No… |
| 9 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | **+14%** | +581 | 4,832 | A single archive of public exploit PoCs and vulnerability research writeups. At the time… |
| 10 | [gridex/gridex](https://github.com/gridex/gridex) | **+13%** | +172 | 1,458 | A native macOS / windows / Linux database IDE built with Swift and AppKit. Connect to Po… |
| 11 | [termio-sh/termio](https://github.com/termio-sh/termio) | **+13%** | +48 | 413 | A terminal-first agentic development environment for agentic coding. Build for CLI/TUI a… |
| 12 | [decodingai-magazine/building-a-coding-agent-from-scratch-course](https://github.com/decodingai-magazine/building-a-coding-agent-from-scratch-course) | **+13%** | +42 | 368 | From agent user to agent builder: build a Claude Code-style coding agent from scratch in… |
| 13 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | **+13%** | +735 | 6,531 | A local multi-agent harness that works with your existing Claude Code, Codex subscriptio… |
| 14 | [superlinked/sie](https://github.com/superlinked/sie) | **+13%** | +361 | 3,224 | Open-source inference server and production cluster for all the models your agent needs. |
| 15 | [trailhq/Graft](https://github.com/trailhq/Graft) | **+12%** | +628 | 5,824 | Turbocharge Claude Code, Cursor, Codex, Gemini & every coding agent: faster, cheaper, wi… |
| 16 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | **+12%** | +638 | 5,929 | Solution for long term memory for agent coding CLIs and to facilitate handoff between di… |
| 17 | [Anakin-Inc/anakin](https://github.com/Anakin-Inc/anakin) | **+11%** | +286 | 2,780 | Open-source web scraping API. Turn any website into clean markdown or structured JSON. A… |
| 18 | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | **+11%** | +1,119 | 10,880 | Free, local tool to track AI coding token usage and cost across 37 tools and agents (Cla… |
| 19 | [bhimrazy/receipt-ocr](https://github.com/bhimrazy/receipt-ocr) | **+11%** | +70 | 688 | An efficient OCR engine for receipt image processing. |
| 20 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | **+11%** | +836 | 8,408 | High-performance AI pipeline engine with a C++ core and 50+ Python-extensible nodes. Bui… |

## Sustained climbers — long run (2026-06-11 → 2026-09-07, 88d)

Averaged over the full snapshot history, so a single viral week doesn't dominate. Repos high here *and* in the recent board are compounding, not spiking.

| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |
|---|---|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | **657.7** | +57,880 | 282,614 | Shell | 78 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **589.7** | +51,895 | 242,828 | Python | 80 |
| 3 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **521.7** | +45,909 | 177,436 | TypeScript | 84 |
| 4 | [earendil-works/pi](https://github.com/earendil-works/pi) | **464.0** | +40,833 | 102,611 | TypeScript | 90 |
| 5 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | **445.5** | +39,207 | 42,524 | C | 75 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **444.9** | +39,151 | 150,604 | Shell | 58 |
| 7 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **440.5** | +38,761 | 252,195 | JavaScript | 79 |
| 8 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **423.6** | +37,277 | 210,757 | — | 23 |
| 9 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **407.6** | +35,866 | 476,727 | Python | 64 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **400.2** | +35,217 | 125,655 | Python | 97 |
| 11 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **399.5** | +35,160 | 121,257 | Python | 80 |
| 12 | [usestrix/strix](https://github.com/usestrix/strix) | **398.5** | +35,072 | 61,018 | Python | 75 |
| 13 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **375.0** | +33,000 | 131,479 | Rust | 82 |
| 14 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | **369.4** | +32,503 | 104,018 | Go | 79 |
| 15 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **367.5** | +32,337 | 205,537 | TypeScript | 88 |
| 16 | [openai/codex](https://github.com/openai/codex) | **359.9** | +31,672 | 122,130 | Rust | 84 |
| 17 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **355.5** | +31,287 | 545,716 | Markdown | 48 |
| 18 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | **353.6** | +31,118 | 94,572 | TypeScript | 87 |
| 19 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **328.9** | +28,939 | 503,820 | — | 55 |
| 20 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **318.3** | +28,014 | 179,157 | Python | 88 |

## Emerging themes

The boards above are computed; this section is interpretation. Each theme groups movers that are rising for the same underlying reason.

### Skills as the packaging format for agent behaviour

_The single loudest signal in this dataset. A year ago you configured an agent with a prompt; now behaviour ships as a versioned, installable *skill* bundle — and the repos distributing those bundles are growing faster than the agents that consume them. Note what this implies: the moat is moving from the model to the instruction layer._

- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 130,235★ · +12,391★ in 7d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 252,195★ · +7,257★ in 7d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 282,614★ · +2,729★ in 7d  
  An agentic skills framework & software development methodology that works.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 125,655★ · +2,272★ in 7d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 174,952★ · +2,218★ in 7d  
  Public repository for Agent Skills
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 210,757★ · +1,732★ in 7d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · 27,524★ · +1,585★ in 7d  
  A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 150,604★ · +1,425★ in 7d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 131,846★ · +1,305★ in 7d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 53,632★ · +360★ in 7d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 65,708★ · +291★ in 7d  
  from vibe coding to agentic engineering - practice makes claude perfect

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 115,475★ · +2,629★ in 7d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 42,524★ · +1,109★ in 7d  
  High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 69,902★ · +1,102★ in 7d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 12,240★ · +764★ in 7d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 26,050★ · +687★ in 7d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 93,375★ · +661★ in 7d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 81,715★ · +561★ in 7d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 16,189★ · +294★ in 7d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 30,544★ · +177★ in 7d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine.
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 6,369★ · +94★ in 7d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,497★ · +41★ in 7d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 127,336★ · +863★ in 7d  
  LLM inference in C/C++
- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 33,805★ · +516★ in 7d  
  AirLLM 70B inference with single 4GB GPU
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 26,985★ · +484★ in 7d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,358★ · +17★ in 7d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,542★ · +9★ in 7d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 104,018★ · +2,049★ in 7d  
  🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman
- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 53,570★ · +1,442★ in 7d  
  Use Claude Code, Codex, Pi, and OpenCode and more for free (1.3B+ free tokens) from your terminal, app, IDE, or phone like OpenClaw (voice supported + ToS friendly)
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 79,186★ · +1,171★ in 7d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 69,210★ · +1,052★ in 7d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 26,985★ · +484★ in 7d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 242,828★ · +4,079★ in 7d  
  The agent that grows with you
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 205,537★ · +2,818★ in 7d  
  The open source coding agent.
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 102,611★ · +2,802★ in 7d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[openai/codex](https://github.com/openai/codex)** · 122,130★ · +1,778★ in 7d  
  Lightweight coding agent that runs in your terminal
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 71,175★ · +1,252★ in 7d  
  🌊 The original agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 131,479★ · +1,139★ in 7d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 144,324★ · +786★ in 7d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 49,116★ · +739★ in 7d  
  Make humans and AI agents work as one team — open-source and self-hostable.
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 86,412★ · +674★ in 7d  
  🙌 OpenHands: AI-Driven Development
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 16,272★ · +669★ in 7d  
  Orchestrate multiple coding agents from desktop and mobile
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 81,667★ · +499★ in 7d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 80,148★ · +412★ in 7d  
  The open-source app everyone uses to manage agents at work
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 19,260★ · +396★ in 7d  
  The most RAM efficient harness
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 68,773★ · +226★ in 7d  
  OmO: Drop your tokens. Ultrawork. Done.
- **[vercel/eve](https://github.com/vercel/eve)** · 4,997★ · +115★ in 7d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[usestrix/strix](https://github.com/usestrix/strix)** · 61,018★ · +1,397★ in 7d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 44,569★ · +1,274★ in 7d  
  Write HTML. Render video. Built for agents.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 112,852★ · +1,038★ in 7d  
  🌐 Make websites accessible for AI agents. Automate tasks online with ease.
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 38,949★ · +945★ in 7d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 102,808★ · +863★ in 7d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 32,906★ · +754★ in 7d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 52,469★ · +538★ in 7d  
  The open-source AI voice studio. Clone, dictate, create.
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 30,437★ · +299★ in 7d  
  Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. Understand How to write meeting minutes
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 17,521★ · +91★ in 7d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.
- **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** · 70,382★ · new to the dataset  
  Open-source AI job search: scan job portals, evaluate listings into a structured A-H report with a global 1-5 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, Codex, OpenCode, Antigravity…)

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 114,546★ · +2,611★ in 7d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 125,655★ · +2,272★ in 7d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 94,572★ · +1,615★ in 7d  
  🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK.
- **[github/spec-kit](https://github.com/github/spec-kit)** · 133,793★ · +1,359★ in 7d  
  💫 Toolkit to help you get started with Spec-Driven Development

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | 70,382 | JavaScript | Hot | Open-source AI job search: scan job portals, evaluate listings into a structured A-H… |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | 64,306 | JavaScript | Mature | Extracted system prompts from Anthropic - Claude Fable 5.1, Opus 5, Claude Design, C… |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 52,693 | Python | Hot | Learn it. Build it. Ship it for others. |
| [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | 49,113 | — | Mature | LEAKED SYSTEM PROMPTS FOR CHATGPT, CLAUDE, GEMINI, GROK, PERPLEXITY, CURSOR, LOVABLE… |
| [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent) | 46,801 | Python | Classic | Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, … |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 46,703 | Python | Hot | Academic Research Skills for Claude Code: research → write → review → revise → final… |
| [Hmbown/Codewhale](https://github.com/Hmbown/Codewhale) | 40,916 | Rust | Hot | Open-source coding agent for your terminal, built in Rust and on a journey of contin… |
| [TencentARC/GFPGAN](https://github.com/TencentARC/GFPGAN) | 37,673 | Python | Abandoned | GFPGAN aims at developing Practical Algorithms for Real-world Face Restoration. |
| [ItzCrazyKns/Vane](https://github.com/ItzCrazyKns/Vane) | 36,661 | TypeScript | Mature | Vane is an AI-powered answering engine. |
| [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 32,331 | Python | Hot | 817 structured cybersecurity skills for AI agents · Mapped to 6 frameworks: MITRE AT… |
| [dmlc/xgboost](https://github.com/dmlc/xgboost) | 28,740 | C++ | Classic | Scalable, Portable and Distributed Gradient Boosting (GBDT, GBRT or GBM) Library,  f… |
| [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | 28,052 | JavaScript | Declining | An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Ro… |
| [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | 26,306 | Rust | Hot | The headless browser for AI agents and web scraping |
| [pytorch/examples](https://github.com/pytorch/examples) | 24,033 | Python | Abandoned | A set of examples around pytorch in Vision, Text, Reinforcement Learning, etc. |
| [akfamily/akshare](https://github.com/akfamily/akshare) | 22,455 | Python | Classic | AKShare is an elegant and simple financial data interface library for Python, built … |
| [Atlas-OS/Atlas](https://github.com/Atlas-OS/Atlas) | 21,469 | Batchfile | Mature | 🚀 An open and lightweight modification to Windows, designed to optimize performance,… |
| [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools) | 17,205 | Rust | Hot | 🚀 通用 AI IDE 账号管理工具：支持 Antigravity / Codex / GitHub Copilot / Windsurf / Kiro / Curso… |
| [tradecatlabs/vibe-coding-cn](https://github.com/tradecatlabs/vibe-coding-cn) | 16,109 | Python | Rising | Vibe Coding 从入门到精通教程｜AI 结对编程工作流｜Prompt、Skill、Workflow、上下文管理、codex实战指南 |
| [davisking/dlib](https://github.com/davisking/dlib) | 14,438 | C++ | Mature | A toolkit for making real world machine learning and data analysis applications in C… |
| [spotify/annoy](https://github.com/spotify/annoy) | 14,294 | C++ | Declining | Approximate Nearest Neighbors in C++/Python optimized for memory usage and loading/s… |
| [paperswithbacktest/awesome-systematic-trading](https://github.com/paperswithbacktest/awesome-systematic-trading) | 14,169 | Python | Classic | A curated list of awesome libraries, packages, strategies, books, blogs, tutorials f… |
| [YouMind-OpenLab/awesome-nano-banana-pro-prompts](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts) | 13,377 | TypeScript | Rising | 🍌 World's largest Nano Banana Pro prompt library — 10,000+ curated prompts with prev… |
| [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | 13,123 | Python | Hot | Independent Auditing of AI Agents. Run by human or the agent itself, to answer the m… |
| [NVIDIA/cutlass](https://github.com/NVIDIA/cutlass) | 10,391 | C++ | Classic | CUDA Templates and Python DSLs for High-Performance Linear Algebra |
| [ZeroLu/awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) | 10,294 | — | Rising | 🚀 An awesome list of curated Nano Banana pro prompts and examples. Your go-to resour… |
| [fossasia/visdom](https://github.com/fossasia/visdom) | 10,289 | Python | Classic | Tool for real-time visualization, monitoring and collaborative analysis of AI/ML exp… |
| [TencentARC/PhotoMaker](https://github.com/TencentARC/PhotoMaker) | 10,090 | Jupyter Notebook | Abandoned | PhotoMaker [CVPR 2024] |
| [OpenMined/PySyft](https://github.com/OpenMined/PySyft) | 10,027 | Python | Classic | Perform data science on data that remains in someone else's server |
| [friuns2/BlackFriday-GPTs-Prompts](https://github.com/friuns2/BlackFriday-GPTs-Prompts) | 9,730 | — | Mature | List of free GPTs that doesn't require plus subscription |
| [ghostfolio/ghostfolio](https://github.com/ghostfolio/ghostfolio) | 9,256 | TypeScript | Classic | Open Source Wealth Management Software. Angular + NestJS + Prisma + Nx + TypeScript … |
| [advaitpaliwal/feynman](https://github.com/advaitpaliwal/feynman) | 8,894 | TypeScript | Rising | The open source AI research agent. |
| [JerBouma/FinanceDatabase](https://github.com/JerBouma/FinanceDatabase) | 8,807 | Python | Classic | This is a database of 300.000+ symbols containing Equities, ETFs, Funds, Indices, Cu… |
| [rockbenben/ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut) | 8,739 | TypeScript | Classic | Stop writing prompts from scratch — a searchable prompt library for ChatGPT, Claude,… |
| [ariga/atlas](https://github.com/ariga/atlas) | 8,707 | Go | Mature | Declarative schema migrations with schema-as-code workflows |
| [timercrack/trader](https://github.com/timercrack/trader) | 8,440 | C | Declining | 期货自动交易 |
| [jamez-bondos/awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images) | 8,140 | JavaScript | Abandoned | Awesome curated collection of images and prompts generated by GPT-4o and gpt-image-1… |
| [bombshell-dev/clack](https://github.com/bombshell-dev/clack) | 8,044 | TypeScript | Classic | Effortlessly build beautiful command-line apps |
| [enquirer/enquirer](https://github.com/enquirer/enquirer) | 7,951 | JavaScript | Abandoned | Stylish, intuitive and user-friendly prompts. Used by eslint, webpack, yarn, pm2, pn… |
| [evidentlyai/evidently](https://github.com/evidentlyai/evidently) | 7,897 | Jupyter Notebook | Mature | Evidently is ​​an open-source ML and LLM observability framework. Evaluate, test, an… |
| [OpenWhispr/openwhispr](https://github.com/OpenWhispr/openwhispr) | 7,694 | JavaScript | Hot | Voice-to-text dictation app with local (Nvidia Parakeet/Whisper) and cloud models (B… |
| _…and 152 more_ | | | | |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 88-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [DevAgentForge/Open-Claude-Cowork](https://github.com/DevAgentForge/Open-Claude-Cowork) | 1.0 | -0.4 | **-42%** of prior pace | 5mo ago | Declining |
| [OpenZeppelin/openzeppelin-contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) | 1.1 | -0.4 | **-40%** of prior pace | 0d ago | Classic |
| [Avaiga/taipy](https://github.com/Avaiga/taipy) | 2.2 | -0.7 | **-32%** of prior pace | 28d ago | Mature |
| [TurixAI/TuriX-CUA](https://github.com/TurixAI/TuriX-CUA) | 1.1 | -0.3 | **-26%** of prior pace | 1mo ago | Declining |
| [morphik-org/morphik-core](https://github.com/morphik-org/morphik-core) | 1.1 | -0.3 | **-25%** of prior pace | 3d ago | Mature |
| [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | 7.9 | -1.1 | **-14%** of prior pace | 1.0y ago | Declining |
| [ValueCell-ai/valuecell](https://github.com/ValueCell-ai/valuecell) | 2.4 | -0.3 | **-12%** of prior pace | 6mo ago | Declining |
| [Memento-Teams/Memento](https://github.com/Memento-Teams/Memento) | 1.3 | 0.0 | **0%** of prior pace | 11mo ago | Declining |
| [stevesolun/ctx](https://github.com/stevesolun/ctx) | 1.1 | 0.0 | **0%** of prior pace | 7d ago | Hot |
| [russellromney/honker](https://github.com/russellromney/honker) | 2.2 | 0.0 | **0%** of prior pace | 0d ago | Hot |
| [arman-bd/guppylm](https://github.com/arman-bd/guppylm) | 2.4 | 0.1 | **6%** of prior pace | 4mo ago | Declining |
| [openai/openai-cs-agents-demo](https://github.com/openai/openai-cs-agents-demo) | 1.9 | 0.1 | **8%** of prior pace | 8mo ago | Declining |
| [FareedKhan-dev/all-rl-algorithms](https://github.com/FareedKhan-dev/all-rl-algorithms) | 3.5 | 0.3 | **8%** of prior pace | 1.0y ago | Abandoned |
| [lochie/web-haptics](https://github.com/lochie/web-haptics) | 1.5 | 0.1 | **10%** of prior pace | 5d ago | Declining |
| [microsoft/fara](https://github.com/microsoft/fara) | 8.0 | 0.9 | **11%** of prior pace | 1mo ago | Rising |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **17 of the graph's 38 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 3** (11): `DietrichGebert/ponytail`, `affaan-m/ECC`, `NousResearch/hermes-agent`, `diegosouzapw/OmniRoute`, `firecrawl/firecrawl`, `Graphify-Labs/graphify`, `VoltAgent/awesome-design-md`, `nextlevelbuilder/ui-ux-pro-max-skill`, `ayghri/i-have-adhd`, `guillaumemeyer/watermarks-remover`, `D4Vinci/Scrapling`
- **Community 12** (5): `stablyai/orca`, `cathrynlavery/diagram-design`, `herdrdev/herdr`, `addyosmani/agent-skills`, `nexu-io/open-design`
- **Community 13** (4): `deepseek-ai/deepseek-harness`, `public-apis/public-apis`, `sindresorhus/awesome`, `codecrafters-io/build-your-own-x`
- **Community 22** (3): `obra/superpowers`, `MadsLorentzen/ai-job-search`, `harry0703/MoneyPrinterTurbo`
- **Community 15** (2): `K-Dense-AI/scientific-agent-skills`, `JuliusBrussee/caveman`
- **Community 0** (2): `anomalyco/opencode`, `earendil-works/pi`
- **Community 21** (2): `sgl-project/sglang`, `FlashML-org/FreeToken`
- **Community 6** (2): `anthropics/skills`, `donnemartin/system-design-primer`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `FlashML-org/FreeToken` ⇄ `sgl-project/sglang` (w=0.350) — topics: glm, inference, minimax, moe
- `addyosmani/agent-skills` ⇄ `cathrynlavery/diagram-design` (w=0.318) — topics: agent-skills, claude-code, codex; authors: NgoQuocViet2001
- `D4Vinci/Scrapling` ⇄ `firecrawl/firecrawl` (w=0.258) — topics: crawler, scraping, web-scraper, web-scraping
- `ayghri/i-have-adhd` ⇄ `affaan-m/ECC` (w=0.221) — topics: developer-tools, productivity; authors: Souptik96
- `MadsLorentzen/ai-job-search` ⇄ `NousResearch/hermes-agent` (w=0.186) — topics: ai, ai-agents, claude-code
- `public-apis/public-apis` ⇄ `sindresorhus/awesome` (w=0.166) — topics: resources, lists; authors: AkashGowdaNC
- `deepseek-ai/deepseek-harness` ⇄ `nexu-io/open-design` (w=0.141) — topics: dsh, dsh-plugin
- `tashfeenahmed/freellmapi` ⇄ `MadsLorentzen/ai-job-search` (w=0.056) — authors: shahidbeig-a11y

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
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-07-27, 2026-08-07, 2026-08-11, 2026-08-28, 2026-08-29, 2026-08-31, 2026-09-06, 2026-09-07 (12 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. The recent window therefore does not always use the immediately preceding snapshot: it uses the newest one at least 7 days back, because a 1-day window amplifies noise far more than it reveals movement. Per-day normalization keeps the boards comparable across refreshes either way.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 1,895 · Window: 2026-08-31 → 2026-09-07 (7d) · Snapshot: 2026-09-07T10:42:15.216Z</sub>
