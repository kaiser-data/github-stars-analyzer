# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 2,408 starred repos (snapshot `2026-10-24T18:18:45.023Z`), cross-referenced with the repo-similarity graph (2,408 nodes / 7,966 edges, 39 communities).
>
> Generated 2026-10-24 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

![Biggest star gains (13d)](assets/trending-now-top-tools.svg)

![Repos by movement type](assets/trending-now-categories.svg)


## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-10-11` → `2026-10-24` (**13 days**), covering the **2,349 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-10-24` (**135 days**).
  - The immediately preceding snapshot (`2026-10-19`) is only 5 days before this one — too short to separate signal from noise — so the baseline was widened to the newest snapshot at least 7 days back.
- **1,880 repos gained stars** in the recent window, adding **1,026,669★** between them.
- **59 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-10-11 → 2026-10-24, 13d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | **+313,732** | 24133.2 | 377,090 | TypeScript | Hot | very active |
| 2 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+27,671** | 2128.5 | 84,573 | Python | Hot | very active |
| 3 | [storytold/photocraft](https://github.com/storytold/photocraft) | **+27,352** | 2104.0 | 72,284 | Rust | Hot | very active |
| 4 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+16,497** | 1269.0 | 43,764 | JavaScript | Declining | active |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | **+15,726** | 1209.7 | 104,720 | TypeScript | Hot | very active |
| 6 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+15,184** | 1168.0 | 175,374 | JavaScript | Hot | very active |
| 7 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | **+13,507** | 1039.0 | 260,346 | TypeScript | Hot | very active |
| 8 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | **+12,061** | 927.8 | 60,635 | HTML | Hot | very active |
| 9 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **+11,594** | 891.8 | 287,887 | JavaScript | Hot | very active |
| 10 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | **+11,159** | 858.4 | 71,330 | TypeScript | Hot | very active |
| 11 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | **+10,584** | 814.2 | 33,950 | Python | Hot | very active |
| 12 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | **+9,106** | 700.5 | 134,297 | Python | Hot | very active |
| 13 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | **+8,876** | 682.8 | 17,593 | Rust | Hot | very active |
| 14 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **+8,513** | 654.8 | 221,010 | TypeScript | Hot | very active |
| 15 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | **+8,010** | 616.2 | 40,802 | TypeScript | Hot | very active |
| 16 | [obra/superpowers](https://github.com/obra/superpowers) | **+7,441** | 572.4 | 304,562 | Shell | Mature | active |
| 17 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | **+7,331** | 563.9 | 106,853 | TypeScript | Hot | very active |
| 18 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **+6,957** | 535.2 | 524,048 | — | Mature | active |
| 19 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | **+6,700** | 515.4 | 44,313 | Python | Hot | very active |
| 20 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | **+6,697** | 515.2 | 16,031 | Rust | Hot | very active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 13-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | **+495%** | +313,732 | 377,090 | Reverse engineer anything with agents, from app behavior down to native binaries. |
| 2 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | **+102%** | +8,876 | 17,593 | PdfCraft: An open-source PDF reader and editor written by scratch in pure Rust |
| 3 | [storytold/artcraft-services](https://github.com/storytold/artcraft-services) | **+87%** | +602 | 1,293 | backend, web frontend, etc. |
| 4 | [storytold/artcraftx](https://github.com/storytold/artcraftx) | **+83%** | +463 | 1,023 | ArtCraft-X |
| 5 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | **+72%** | +6,697 | 16,031 | FilmCraft: An open-source, nonlinear video editor written by scratch in pure Rust |
| 6 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | **+71%** | +6,016 | 14,517 | LightCraft: An open-source non-destructive photo editor written by scratch in pure Rust |
| 7 | [storytold/photocraft](https://github.com/storytold/photocraft) | **+61%** | +27,352 | 72,284 | PhotoCraft: An open-source, photo editor written by scratch in pure Rust |
| 8 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+61%** | +16,497 | 43,764 | A coding-agent skill for multi-phase security audits with independently verified, machin… |
| 9 | [Asymptote-Labs/agent-beacon](https://github.com/Asymptote-Labs/agent-beacon) | **+51%** | +933 | 2,746 | The cross-harness, self-improving memory layer for AI agents. Join our community: https:… |
| 10 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+49%** | +27,671 | 84,573 | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voic… |
| 11 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | **+45%** | +10,584 | 33,950 | Independent Auditing of AI Agents. Run by human or the agent itself, to answer the most … |
| 12 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | **+45%** | +4,111 | 13,213 | Solution for long term memory for agent coding CLIs and to facilitate handoff between di… |
| 13 | [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) | **+33%** | +1,589 | 6,346 | A tiny friend in your Mac's notch and on your iPhone that keeps an eye on your AI coding… |
| 14 | [fabio-rovai/open-ontologies](https://github.com/fabio-rovai/open-ontologies) | **+31%** | +313 | 1,333 | Plan, apply and roll back changes to a production ontology, with a blast radius report a… |
| 15 | [strands-labs/strands-decider](https://github.com/strands-labs/strands-decider) | **+27%** | +151 | 703 | A small, fast decision model, or system one model, for agentic workflows. Pick between o… |
| 16 | [google/artemis](https://github.com/google/artemis) | **+27%** | +3,048 | 14,335 | ARTEMIS turns natural-language instructions into reliable Android automation. It automat… |
| 17 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | **+25%** | +12,061 | 60,635 | Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, … |
| 18 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | **+24%** | +8,010 | 40,802 | 7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behin… |
| 19 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | **+23%** | +6,004 | 32,107 | Context window optimization for AI coding agents. Sandboxes tool output (98% reduction),… |
| 20 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | **+23%** | +3,605 | 19,283 | OpenShell is the safe, private runtime for autonomous AI agents. |

## Sustained climbers — long run (2026-06-11 → 2026-10-24, 135d)

Averaged over the full snapshot history, so a single viral week doesn't dominate. Repos high here *and* in the recent board are compounding, not spiking.

| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |
|---|---|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | **591.3** | +79,828 | 304,562 | Shell | 64 |
| 2 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **551.5** | +74,453 | 287,887 | JavaScript | 78 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **487.5** | +65,810 | 256,743 | Python | 75 |
| 4 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **469.6** | +63,398 | 194,925 | TypeScript | 83 |
| 5 | [earendil-works/pi](https://github.com/earendil-works/pi) | **413.4** | +55,803 | 117,581 | TypeScript | 90 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **386.8** | +52,214 | 163,667 | Shell | 63 |
| 7 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **377.6** | +50,982 | 491,843 | Python | 64 |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **369.1** | +49,823 | 148,302 | Rust | 79 |
| 9 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **368.8** | +49,792 | 223,272 | — | 19 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **366.0** | +49,409 | 139,847 | Python | 96 |
| 11 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **364.2** | +49,167 | 524,048 | — | 49 |
| 12 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **360.9** | +48,718 | 134,815 | Python | 80 |
| 13 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **354.1** | +47,810 | 221,010 | TypeScript | 89 |
| 14 | [usestrix/strix](https://github.com/usestrix/strix) | **338.3** | +45,675 | 71,621 | Python | 75 |
| 15 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | **329.8** | +44,517 | 71,330 | TypeScript | 83 |
| 16 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | **326.5** | +44,080 | 47,397 | C | 76 |
| 17 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | **320.5** | +43,265 | 114,780 | Go | 79 |
| 18 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **307.6** | +41,524 | 555,953 | Markdown | 29 |
| 19 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **302.3** | +40,804 | 191,947 | Python | 89 |
| 20 | [openai/codex](https://github.com/openai/codex) | **298.8** | +40,333 | 130,791 | Rust | 93 |

## Emerging themes

The boards above are computed; this section is interpretation. Each theme groups movers that are rising for the same underlying reason.

### Skills as the packaging format for agent behaviour

_The single loudest signal in this dataset. A year ago you configured an agent with a prompt; now behaviour ships as a versioned, installable *skill* bundle — and the repos distributing those bundles are growing faster than the agents that consume them. Note what this implies: the moat is moving from the model to the instruction layer._

- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 175,374★ · +15,184★ in 13d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 287,887★ · +11,594★ in 13d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 304,562★ · +7,441★ in 13d  
  An agentic skills framework & software development methodology that works.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 139,847★ · +5,436★ in 13d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 223,272★ · +5,324★ in 13d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 163,667★ · +5,008★ in 13d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 183,465★ · +3,174★ in 13d  
  Public repository for Agent Skills
- **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · 58,576★ · +2,329★ in 13d  
  A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 137,492★ · +1,691★ in 13d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 56,418★ · +1,063★ in 13d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC (no affiliation). A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 67,966★ · +626★ in 13d  
  from vibe coding to agentic engineering - practice makes claude perfect

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 134,297★ · +9,106★ in 13d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 102,756★ · +3,620★ in 13d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 88,047★ · +2,223★ in 13d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 29,888★ · +2,001★ in 13d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 75,207★ · +1,548★ in 13d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 47,397★ · +1,114★ in 13d  
  Local code intelligence for developers and AI agents. Connect code, docs and infrastructure in a persistent graph, with CBM Lens, MCP tools, agent integrations and change-aware test selection.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 32,718★ · +770★ in 13d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory with small models for free
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 7,894★ · +465★ in 13d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 17,376★ · +315★ in 13d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 14,214★ · +313★ in 13d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,644★ · +47★ in 13d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 40,547★ · +4,917★ in 13d  
  AirLLM 2.8T LLM inference with single 4GB GPU
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 43,699★ · +2,761★ in 13d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 132,228★ · +1,494★ in 13d  
  LLM inference in C/C++
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,551★ · +59★ in 13d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,596★ · +18★ in 13d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 63,072★ · +5,811★ in 13d  
  Use Claude Code, Codex, VSCode, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly)
- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 114,780★ · +3,903★ in 13d  
  🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 77,711★ · +2,825★ in 13d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 43,699★ · +2,761★ in 13d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 84,451★ · +1,614★ in 13d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 221,010★ · +8,513★ in 13d  
  The open source coding agent.
- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 106,853★ · +7,331★ in 13d  
  The open-source app everyone uses to manage agents at work
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 148,302★ · +5,939★ in 13d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 78,966★ · +4,714★ in 13d  
  🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 256,743★ · +4,290★ in 13d  
  The agent that grows with you
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 117,581★ · +3,541★ in 13d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 153,265★ · +3,259★ in 13d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[openai/codex](https://github.com/openai/codex)** · 130,791★ · +2,275★ in 13d  
  Lightweight coding agent that runs in your terminal
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 21,873★ · +1,497★ in 13d  
  Orchestrate multiple coding agents from desktop and mobile
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 53,711★ · +1,315★ in 13d  
  Make humans and AI agents work as one team — open-source and self-hostable.
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 91,733★ · +1,250★ in 13d  
  🙌 OpenHands: AI-Driven Development
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 21,183★ · +805★ in 13d  
  High performance coding agent harness written in Rust, built for heavy multi-agent dev workflows
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 84,378★ · +732★ in 13d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 70,309★ · +372★ in 13d  
  OmO: Just type "mass ulw" keyword with your prompt. Now you are the master of graph engineering.
- **[vercel/eve](https://github.com/vercel/eve)** · 5,666★ · +153★ in 13d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 71,330★ · +11,159★ in 13d  
  Write HTML. Render video. Built for agents.
- **[usestrix/strix](https://github.com/usestrix/strix)** · 71,621★ · +3,912★ in 13d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 113,591★ · +3,120★ in 13d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** · 76,978★ · +3,025★ in 13d  
  Open-source AI job search agent and job finder: scan job boards, score each job 1-5 against your CV before you apply, tailor an ATS-friendly resume and cover letter, get interview prep and a job application tracker. It helps you fill in each application; you press Submit. Runs locally in your AI coding CLI (Claude Code, Codex, OpenCode and more).
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 58,448★ · +1,655★ in 13d  
  The open-source AI voice studio. Clone, dictate, create.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 119,047★ · +1,523★ in 13d  
  Open-source Python library for AI browser agents, plus Browser Use Cloud: stealth browsers and a hosted agent API.
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 42,514★ · +1,433★ in 13d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 36,515★ · +1,395★ in 13d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 32,119★ · +539★ in 13d  
  Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. Understand How to write meeting minutes
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 17,961★ · +126★ in 13d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 139,847★ · +5,436★ in 13d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 103,734★ · +3,383★ in 13d  
  The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create motion, prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.
- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 123,307★ · +3,170★ in 13d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.
- **[github/spec-kit](https://github.com/github/spec-kit)** · 142,703★ · +2,022★ in 13d  
  💫 Toolkit to help you get started with SDD or any other process!

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [lobehub/lobehub](https://github.com/lobehub/lobehub) | 83,466 | TypeScript | Classic | 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations … |
| [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | 80,670 | TypeScript | Hot | Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,4… |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 72,893 | TypeScript | Hot | Spec-driven development (SDD) for AI coding assistants. |
| [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | 64,480 | Python | Hot | The job search that runs on your machine. AI job application framework built on Clau… |
| [Niko1221/Strata](https://github.com/Niko1221/Strata) | 31,795 | C++ | Rising | Qwen3.8-Flash-Next on any consumer hardware: one-click install for Windows / Linux. … |
| [serengil/deepface](https://github.com/serengil/deepface) | 23,595 | Python | Classic | A Lightweight Face Recognition and Facial Attribute Analysis (Age, Gender, Emotion a… |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | 20,944 | TypeScript | Hot | LLM Wiki is a cross-platform desktop application that turns your documents into an o… |
| [kitao/pyxel](https://github.com/kitao/pyxel) | 18,449 | Rust | Mature | A retro game engine for Python |
| [web-infra-dev/midscene](https://github.com/web-infra-dev/midscene) | 15,380 | TypeScript | Mature | See interfaces like a human. E2E testing in natural language. |
| [naklecha/llama3-from-scratch](https://github.com/naklecha/llama3-from-scratch) | 15,205 | Jupyter Notebook | Abandoned | llama3 implementation one matrix multiplication at a time |
| [tester-army/e2e](https://github.com/tester-army/e2e) | 11,833 | TypeScript | Hot | Next generation e2e testing framework for web and mobile apps. |
| [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code) | 10,717 | TypeScript | Hot | Turbocharge Claude Code, Cursor, Codex, Gemini & every coding agent: faster, cheaper… |
| [baptisteArno/typebot.io](https://github.com/baptisteArno/typebot.io) | 10,577 | TypeScript | Classic | 💬 Typebot is a powerful chatbot builder that you can self-host. |
| [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | 7,422 | Python | Hot | PaperBanana: Automating Academic Illustration For AI Scientists |
| [Zipstack/unstract](https://github.com/Zipstack/unstract) | 7,296 | Python | Mature | LLM-Driven Extraction of Unstructured Data — Built for API Deployments & ETL Pipelin… |
| [mutonby/openshorts](https://github.com/mutonby/openshorts) | 7,050 | Python | Hot | Open source AI clip generator: turns long videos into viral 9:16 shorts with AI mome… |
| [stefanprodan/podinfo](https://github.com/stefanprodan/podinfo) | 6,024 | Go | Classic | Go microservice template for Kubernetes |
| [antiwork/shortest](https://github.com/antiwork/shortest) | 5,696 | TypeScript | Mature | QA via natural language AI tests |
| [callstack/agent-device](https://github.com/callstack/agent-device) | 5,130 | TypeScript | Hot | Mobile app automation and verification for AI coding agents. CLI, MCP server, and ty… |
| [TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli) | 4,955 | TypeScript | Hot | Official TestSprite CLI — AI-powered automated testing from your terminal |
| [Zuhaitz-dev/zenc-lang](https://github.com/Zuhaitz-dev/zenc-lang) | 4,317 | C | Rising | Write like a high-level language, run like C. |
| [hardkoded/puppeteer-sharp](https://github.com/hardkoded/puppeteer-sharp) | 3,931 | C# | Classic | Headless Chrome .NET API |
| [Contrastive-LM/CLM](https://github.com/Contrastive-LM/CLM) | 3,115 | Python | Mature | Contrastive Language Models (CLMs) are a new class of System One model trained with … |
| [symfony/panther](https://github.com/symfony/panther) | 3,070 | PHP | Mature | A browser testing and web crawling library for PHP and Symfony |
| [openenv/OpenEnv](https://github.com/openenv/OpenEnv) | 2,766 | Python | Hot | An interface library for RL post training with environments. |
| [Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki) | 2,593 | Python | Declining | Agent Skills-compatible LLM wiki for Claude Code, Cursor, and Codex. Build a Karpath… |
| [mike4192/spotMicro](https://github.com/mike4192/spotMicro) | 2,160 | C++ | Abandoned | Spot Micro Quadruped Project |
| [nateherkai/herk-edit-kit](https://github.com/nateherkai/herk-edit-kit) | 2,118 | HTML | Rising | Herk Edit Kit by Nate Herk: edit videos, reels, and YouTube Shorts with Codex or Cla… |
| [HelixDB/helix-foundry](https://github.com/HelixDB/helix-foundry) | 1,659 | TypeScript | Hot | Your company's data, connected into one ontology, on your own computer. A local-firs… |
| [nvk/llm-wiki](https://github.com/nvk/llm-wiki) | 1,458 | Python | Hot | LLM-compiled knowledge bases for any AI agent. Parallel multi-agent research, thesis… |
| [XHToken/Spark-X2.6](https://github.com/XHToken/Spark-X2.6) | 842 | — | Rising | Spark-x2.6 open model series. Pushing the Limits of Agentic Capabilities in On-Devic… |
| [mozilla-ai/otari](https://github.com/mozilla-ai/otari) | 735 | Python | Hot | Open-source, OpenAI-compatible LLM gateway you run yourself. One endpoint for 40+ pr… |
| [ibrahimqureshae/mdflux](https://github.com/ibrahimqureshae/mdflux) | 570 | Python | Mature | Turn any document into clean, AI-ready Markdown. Local-first desktop app: reads scan… |
| [nebius/soperator](https://github.com/nebius/soperator) | 453 | Go | Mature | Run Slurm in Kubernetes |
| [zengyh1900/3D-Human-Body-Shape](https://github.com/zengyh1900/3D-Human-Body-Shape) | 397 | Python | Abandoned | [ICIMCS'2017] Official Code for 3D Human Body Reshaping with Anthropometric Modeling |
| [Graphicle-AI/graphicle](https://github.com/Graphicle-AI/graphicle) | 352 | Rust | Rising | Code graph and memory for your coding agents, in one Rust program. For Claude Code, … |
| [nebius/token-factory-cookbook](https://github.com/nebius/token-factory-cookbook) | 309 | Jupyter Notebook | Hot | — |
| [NandhaKishorM/vegaml](https://github.com/NandhaKishorM/vegaml) | 283 | Python | Hot | Typed decisions from a frozen language model and a small physics engine: calibrated … |
| [facebookresearch/swe-sweep](https://github.com/facebookresearch/swe-sweep) | 190 | Python | Declining | How many bugs can LMs find & fix in large codebases? |
| [JNavas2/Archive-Page](https://github.com/JNavas2/Archive-Page) | 184 | JavaScript | Mature | Browser extension to archive webpages in Archive Today |
| _…and 19 more_ | | | | |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 135-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [axios/axios](https://github.com/axios/axios) | 1.7 | -2.7 | **-155%** of prior pace | 1d ago | Classic |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 2.3 | -1.5 | **-67%** of prior pace | 7mo ago | Declining |
| [meta-llama/prompt-ops](https://github.com/meta-llama/prompt-ops) | 1.5 | -0.7 | **-45%** of prior pace | 6mo ago | Declining |
| [deeplethe/forkd](https://github.com/deeplethe/forkd) | 5.4 | -2.0 | **-37%** of prior pace | 0d ago | Hot |
| [hashicorp/consul](https://github.com/hashicorp/consul) | 1.2 | -0.4 | **-32%** of prior pace | 0d ago | Classic |
| [libgdx/libgdx](https://github.com/libgdx/libgdx) | 2.5 | -0.2 | **-9%** of prior pace | 10d ago | Classic |
| [hexabot-ai/Hexabot](https://github.com/hexabot-ai/Hexabot) | 1.3 | -0.1 | **-6%** of prior pace | 1mo ago | Mature |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | 13.9 | -0.5 | **-3%** of prior pace | 22d ago | Mature |
| [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) | 3.9 | 0.1 | **2%** of prior pace | 1.2y ago | Abandoned |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | 7.0 | 0.2 | **2%** of prior pace | 1mo ago | Mature |
| [Suvink/cut-it-out](https://github.com/Suvink/cut-it-out) | 1.9 | 0.1 | **4%** of prior pace | 10mo ago | Declining |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | 3.0 | 0.2 | **5%** of prior pace | 3mo ago | Declining |
| [https-deeplearning-ai/deeplearning-ai](https://github.com/https-deeplearning-ai/deeplearning-ai) | 1.2 | 0.1 | **6%** of prior pace | 4mo ago | Declining |
| [SuperClaude-Org/SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) | 4.8 | 0.3 | **6%** of prior pace | 27d ago | Declining |
| [microsoft/fara](https://github.com/microsoft/fara) | 5.6 | 0.4 | **7%** of prior pace | 1mo ago | Declining |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **16 of the graph's 39 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 2** (7): `morluto/rea`, `cathrynlavery/diagram-design`, `heygen-com/hyperframes`, `ifixai-ai/iFixAi`, `Graphify-Labs/graphify`, `addyosmani/agent-skills`, `msitarzewski/agency-agents`
- **Community 5** (5): `paperclipai/paperclip`, `rohitg00/ai-engineering-from-scratch`, `K-Dense-AI/scientific-agent-skills`, `mksglu/context-mode`, `nextlevelbuilder/ui-ux-pro-max-skill`
- **Community 21** (4): `storytold/photocraft`, `storytold/pdfcraft`, `storytold/filmcraft`, `storytold/lightcraft`
- **Community 0** (4): `anomalyco/opencode`, `Alishahryar1/free-claude-code`, `calesthio/OpenMontage`, `harry0703/MoneyPrinterTurbo`
- **Community 16** (3): `DietrichGebert/ponytail`, `affaan-m/ECC`, `firecrawl/firecrawl`
- **Community 36** (3): `deepseek-ai/deepseek-harness`, `sindresorhus/awesome`, `awesome-selfhosted/awesome-selfhosted`
- **Community 23** (3): `tashfeenahmed/freellmapi`, `vectorize-io/hindsight`, `ruvnet/ruflo`
- **Community 3** (2): `debpalash/VoiceStudio`, `farion1231/cc-switch`
- **Community 6** (2): `stablyai/orca`, `anthropics/claude-plugins-official`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `storytold/filmcraft` ⇄ `storytold/lightcraft` (w=1.185) — topics: art, rust; authors: dylanmtaylor, aiongg, Silvertree2010
- `storytold/filmcraft` ⇄ `storytold/pdfcraft` (w=1.172) — topics: rust; authors: dylanmtaylor, aiongg, dotCooCoo
- `storytold/filmcraft` ⇄ `storytold/photocraft` (w=1.030) — topics: art, rust; authors: dylanmtaylor, aiongg, Silvertree2010
- `rohitg00/ai-engineering-from-scratch` ⇄ `mksglu/context-mode` (w=1.026) — topics: mcp; authors: github-actions[bot]
- `storytold/photocraft` ⇄ `storytold/lightcraft` (w=0.993) — topics: art, rust; authors: dylanmtaylor, aiongg, echelon
- `storytold/pdfcraft` ⇄ `storytold/lightcraft` (w=0.991) — topics: rust; authors: aiongg, dylanmtaylor, echelon
- `storytold/pdfcraft` ⇄ `storytold/photocraft` (w=0.882) — topics: rust; authors: aiongg, dylanmtaylor, PerchAnton
- `paperclipai/paperclip` ⇄ `mksglu/context-mode` (w=0.526) — topics: claude-code, codex, mcp, openclaw; authors: github-actions[bot]
- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `addyosmani/agent-skills` ⇄ `cathrynlavery/diagram-design` (w=0.337) — topics: agent-skills, claude-code, codex; authors: rudycelekli
- `morluto/rea` ⇄ `deepseek-ai/deepseek-harness` (w=0.250) — topics: ai-agents, dsh-plugin, cordis, dsh
- `calesthio/OpenMontage` ⇄ `harry0703/MoneyPrinterTurbo` (w=0.232) — topics: ffmpeg, python, text-to-speech; authors: rudycelekli, ac1982
- …and 3 more.

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
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-07-27, 2026-08-07, 2026-08-11, 2026-08-28, 2026-08-29, 2026-08-31, 2026-09-06, 2026-09-07, 2026-09-12, 2026-09-14, 2026-09-21, 2026-09-25, 2026-09-28, 2026-09-29, 2026-10-05, 2026-10-10, 2026-10-11, 2026-10-19, 2026-10-24 (23 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. The recent window therefore does not always use the immediately preceding snapshot: it uses the newest one at least 7 days back, because a 1-day window amplifies noise far more than it reveals movement. Per-day normalization keeps the boards comparable across refreshes either way.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 2,349 · Window: 2026-10-11 → 2026-10-24 (13d) · Snapshot: 2026-10-24T18:18:45.023Z</sub>
