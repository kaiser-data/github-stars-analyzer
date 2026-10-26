# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 2,415 starred repos (snapshot `2026-10-26T11:46:04.025Z`), cross-referenced with the repo-similarity graph (2,415 nodes / 8,024 edges, 43 communities).
>
> Generated 2026-10-26 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

![Biggest star gains (7d)](assets/trending-now-top-tools.svg)

![Repos by movement type](assets/trending-now-categories.svg)


## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-10-19` → `2026-10-26` (**7 days**), covering the **2,387 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-10-26` (**137 days**).
  - The immediately preceding snapshot (`2026-10-24`) is only 2 days before this one — too short to separate signal from noise — so the baseline was widened to the newest snapshot at least 7 days back.
- **1,811 repos gained stars** in the recent window, adding **415,895★** between them.
- **28 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-10-19 → 2026-10-26, 7d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | **+58,276** | 8325.1 | 387,891 | TypeScript | Hot | very active |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+16,392** | 2341.7 | 47,762 | JavaScript | Declining | active |
| 3 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+11,288** | 1612.6 | 87,868 | Python | Hot | very active |
| 4 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+9,088** | 1298.3 | 176,581 | JavaScript | Hot | very active |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | **+9,023** | 1289.0 | 106,461 | TypeScript | Hot | very active |
| 6 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | **+8,079** | 1154.1 | 262,088 | TypeScript | Hot | very active |
| 7 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | **+6,974** | 996.3 | 135,698 | Python | Hot | very active |
| 8 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **+5,593** | 799.0 | 289,209 | JavaScript | Hot | very active |
| 9 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | **+5,418** | 774.0 | 72,604 | TypeScript | Hot | very active |
| 10 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | **+5,364** | 766.3 | 33,172 | C++ | Rising | very active |
| 11 | [storytold/photocraft](https://github.com/storytold/photocraft) | **+5,133** | 733.3 | 73,095 | Rust | Hot | very active |
| 12 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | **+4,874** | 696.3 | 34,672 | Python | Hot | very active |
| 13 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **+4,597** | 656.7 | 221,732 | TypeScript | Hot | very active |
| 14 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | **+4,517** | 645.3 | 41,843 | TypeScript | Hot | very active |
| 15 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | **+3,997** | 571.0 | 143,114 | Python | Classic | very active |
| 16 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **+3,706** | 529.4 | 524,914 | — | Mature | active |
| 17 | [obra/superpowers](https://github.com/obra/superpowers) | **+3,459** | 494.1 | 305,321 | Shell | Mature | active |
| 18 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | **+3,310** | 472.9 | 19,979 | Rust | Hot | very active |
| 19 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | **+3,243** | 463.3 | 115,250 | Python | Hot | very active |
| 20 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | **+3,233** | 461.9 | 45,185 | Python | Rising | very active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 7-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [Asymptote-Labs/agent-beacon](https://github.com/Asymptote-Labs/agent-beacon) | **+54%** | +999 | 2,841 | The cross-harness, self-improving memory layer for AI agents. Join our community: https:… |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+52%** | +16,392 | 47,762 | A coding-agent skill for multi-phase security audits with independently verified, machin… |
| 3 | [decodingai-magazine/building-a-coding-agent-from-scratch-course](https://github.com/decodingai-magazine/building-a-coding-agent-from-scratch-course) | **+34%** | +226 | 899 | Learn harness engineering by building Claude Code from scratch. Free, open-source course… |
| 4 | [fabio-rovai/open-ontologies](https://github.com/fabio-rovai/open-ontologies) | **+28%** | +302 | 1,390 | Plan, apply and roll back changes to a production ontology, with a blast radius report a… |
| 5 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | **+26%** | +2,823 | 13,642 | Solution for long term memory for agent coding CLIs and to facilitate handoff between di… |
| 6 | [nateherkai/herk-edit-kit](https://github.com/nateherkai/herk-edit-kit) | **+22%** | +394 | 2,222 | Herk Edit Kit by Nate Herk: edit videos, reels, and YouTube Shorts with Codex or Claude … |
| 7 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | **+20%** | +3,310 | 19,979 | OpenShell is the safe, private runtime for autonomous AI agents. |
| 8 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | **+19%** | +5,364 | 33,172 | Qwen3.8-Flash-Next on any consumer hardware: one-click install for Windows / Linux. Stra… |
| 9 | [morluto/rea](https://github.com/morluto/rea) | **+18%** | +58,276 | 387,891 | Reverse engineer anything with agents, from app behavior down to native binaries. |
| 10 | [Graphicle-AI/graphicle](https://github.com/Graphicle-AI/graphicle) | **+18%** | +54 | 361 | Code graph and memory for your coding agents, in one Rust program. For Claude Code, Code… |
| 11 | [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) | **+17%** | +952 | 6,507 | A tiny friend in your Mac's notch and on your iPhone that keeps an eye on your AI coding… |
| 12 | [google/artemis](https://github.com/google/artemis) | **+17%** | +2,155 | 14,904 | ARTEMIS turns natural-language instructions into reliable Android automation. It automat… |
| 13 | [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) | **+17%** | +529 | 3,663 | HarnessRouter Community Edition: the self-hosted, Apache-2.0 edition of the unified inte… |
| 14 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | **+16%** | +4,874 | 34,672 | Independent Auditing of AI Agents. Run by human or the agent itself, to answer the most … |
| 15 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+15%** | +11,288 | 87,868 | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voic… |
| 16 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | **+12%** | +4,517 | 41,843 | 7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behin… |
| 17 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | **+11%** | +1,842 | 17,924 | PdfCraft: An open-source PDF reader and editor written by scratch in pure Rust |
| 18 | [omnara-ai/omnara](https://github.com/omnara-ai/omnara) | **+11%** | +324 | 3,263 | The open-source managed agent platform. A self-hostable alternative to Claude Managed Ag… |
| 19 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | **+9%** | +1,390 | 16,338 | FilmCraft: An open-source, nonlinear video editor written by scratch in pure Rust |
| 20 | [stablyai/orca](https://github.com/stablyai/orca) | **+9%** | +9,023 | 106,461 | Orca is the place for working with a fleet of agents (e.g. Grok Bot, Claude Code). Run a… |

## Sustained climbers — long run (2026-06-11 → 2026-10-26, 137d)

Averaged over the full snapshot history, so a single viral week doesn't dominate. Repos high here *and* in the recent board are compounding, not spiking.

| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |
|---|---|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | **588.2** | +80,587 | 305,321 | Shell | 64 |
| 2 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **553.1** | +75,775 | 289,209 | JavaScript | 84 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **483.9** | +66,293 | 257,226 | Python | 75 |
| 4 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **466.8** | +63,952 | 195,479 | TypeScript | 88 |
| 5 | [earendil-works/pi](https://github.com/earendil-works/pi) | **409.8** | +56,142 | 117,920 | TypeScript | 90 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **384.4** | +52,666 | 164,119 | Shell | 63 |
| 7 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **375.3** | +51,411 | 492,272 | Python | 64 |
| 8 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **369.7** | +50,647 | 224,127 | — | 19 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **367.7** | +50,371 | 148,850 | Rust | 79 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **366.4** | +50,200 | 140,638 | Python | 95 |
| 11 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **365.2** | +50,033 | 524,914 | — | 49 |
| 12 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **358.8** | +49,161 | 135,258 | Python | 80 |
| 13 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **354.2** | +48,532 | 221,732 | TypeScript | 84 |
| 14 | [usestrix/strix](https://github.com/usestrix/strix) | **336.2** | +46,059 | 72,005 | Python | 75 |
| 15 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | **334.2** | +45,791 | 72,604 | TypeScript | 79 |
| 16 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | **322.6** | +44,200 | 47,517 | C | 76 |
| 17 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | **318.6** | +43,647 | 115,162 | Go | 84 |
| 18 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **305.8** | +41,895 | 556,324 | Markdown | 28 |
| 19 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **300.3** | +41,139 | 192,282 | Python | 89 |
| 20 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | **296.4** | +40,601 | 104,055 | TypeScript | 83 |

## Emerging themes

The boards above are computed; this section is interpretation. Each theme groups movers that are rising for the same underlying reason.

### Skills as the packaging format for agent behaviour

_The single loudest signal in this dataset. A year ago you configured an agent with a prompt; now behaviour ships as a versioned, installable *skill* bundle — and the repos distributing those bundles are growing faster than the agents that consume them. Note what this implies: the moat is moving from the model to the instruction layer._

- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 176,581★ · +9,088★ in 7d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 289,209★ · +5,593★ in 7d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 305,321★ · +3,459★ in 7d  
  An agentic skills framework & software development methodology that works.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 140,638★ · +3,199★ in 7d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 224,127★ · +3,042★ in 7d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 164,119★ · +2,697★ in 7d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 183,877★ · +1,759★ in 7d  
  Public repository for Agent Skills
- **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · 58,794★ · +1,020★ in 7d  
  A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 137,775★ · +872★ in 7d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 56,574★ · +581★ in 7d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC (no affiliation). A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 68,133★ · +400★ in 7d  
  from vibe coding to agentic engineering - practice makes claude perfect

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 135,698★ · +6,974★ in 7d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 103,258★ · +1,548★ in 7d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 88,341★ · +1,401★ in 7d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 75,383★ · +963★ in 7d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 47,517★ · +615★ in 7d  
  Local code intelligence for developers and AI agents. Connect code, docs and infrastructure in a persistent graph, with CBM Lens, MCP tools, agent integrations and change-aware test selection.
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 29,966★ · +352★ in 7d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 32,768★ · +238★ in 7d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory with small models for free
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 17,451★ · +184★ in 7d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 14,253★ · +120★ in 7d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 7,918★ · +67★ in 7d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,647★ · +22★ in 7d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 40,711★ · +1,300★ in 7d  
  AirLLM 2.8T LLM inference with single 4GB GPU
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 43,975★ · +1,165★ in 7d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 132,400★ · +719★ in 7d  
  LLM inference in C/C++
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,555★ · +30★ in 7d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,599★ · +7★ in 7d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 77,872★ · +1,913★ in 7d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 63,596★ · +1,853★ in 7d  
  Use Claude Code, Codex, Antigravity, VSCode, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly)
- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 115,162★ · +1,593★ in 7d  
  🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 43,975★ · +1,165★ in 7d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 84,595★ · +662★ in 7d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 221,732★ · +4,597★ in 7d  
  The open source coding agent.
- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 107,479★ · +3,066★ in 7d  
  The open-source app everyone uses to manage agents at work
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 148,850★ · +2,659★ in 7d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 79,392★ · +2,564★ in 7d  
  🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 257,226★ · +2,124★ in 7d  
  The agent that grows with you
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 117,920★ · +1,596★ in 7d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[openai/codex](https://github.com/openai/codex)** · 130,982★ · +1,103★ in 7d  
  Lightweight coding agent that runs in your terminal
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 153,420★ · +1,077★ in 7d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 22,080★ · +696★ in 7d  
  Orchestrate multiple coding agents from desktop and mobile
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 53,841★ · +646★ in 7d  
  Make humans and AI agents work as one team — open-source and self-hostable.
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 91,884★ · +632★ in 7d  
  🙌 OpenHands: AI-Driven Development
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 84,439★ · +319★ in 7d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 21,214★ · +189★ in 7d  
  High performance coding agent harness written in Rust, built for heavy multi-agent dev workflows
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 70,345★ · +164★ in 7d  
  OmO: Just type "mass ulw" keyword with your prompt. Now you are the master of graph engineering.
- **[vercel/eve](https://github.com/vercel/eve)** · 5,679★ · +64★ in 7d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 72,604★ · +5,418★ in 7d  
  Write HTML. Render video. Built for agents.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 115,250★ · +3,243★ in 7d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[usestrix/strix](https://github.com/usestrix/strix)** · 72,005★ · +2,197★ in 7d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** · 77,432★ · +1,858★ in 7d  
  Open-source AI job search agent and job finder: scan job boards, score each job 1-5 against your CV before you apply, tailor an ATS-friendly resume and cover letter, get interview prep and a job application tracker. It helps you fill in each application; you press Submit. Runs locally in your AI coding CLI (Claude Code, Codex, OpenCode and more).
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 43,203★ · +1,480★ in 7d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 36,716★ · +834★ in 7d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 119,178★ · +706★ in 7d  
  Open-source Python library for AI browser agents, plus Browser Use Cloud: stealth browsers and a hosted agent API.
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 58,573★ · +588★ in 7d  
  The open-source AI voice studio. Clone, dictate, create.
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 32,177★ · +251★ in 7d  
  Privacy first AI meeting note taker. Download Free and open source granola, otter ai, fireflies alternative. Parakeet / Whisper live transcription, on-device speaker diarization, built on Rust. 100% local processing. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker & Assistant for macOS & Windows
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 17,976★ · +75★ in 7d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 140,638★ · +3,199★ in 7d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 104,055★ · +1,672★ in 7d  
  The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create motion, prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.
- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 123,604★ · +1,396★ in 7d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.
- **[github/spec-kit](https://github.com/github/spec-kit)** · 142,957★ · +1,075★ in 7d  
  💫 Toolkit to help you get started with SDD or any other process!

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 102,721 | JavaScript | Hot | Agent skills that give coding agents taste: art direction, reference images and a br… |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 88,385 | Rust | Hot | The design language that makes your AI harness better at design. |
| [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | 81,297 | TypeScript | Hot | Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,4… |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 73,018 | TypeScript | Hot | Spec-driven development (SDD) for AI coding assistants. |
| [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | 66,005 | Python | Hot | The job search that runs on your machine. AI job application framework built on Clau… |
| [motiondivision/motion](https://github.com/motiondivision/motion) | 34,540 | TypeScript | Classic | A modern animation library for React and JavaScript |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | 33,097 | Python | Hot | Open source repository of plugins primarily intended for knowledge workers to use in… |
| [kitao/pyxel](https://github.com/kitao/pyxel) | 18,459 | Rust | Mature | A retro game engine for Python |
| [ParadevAI/Paradev](https://github.com/ParadevAI/Paradev) | 15,566 | TypeScript | Hot | Superset is an agentic IDE to orchestrate 100+ coding agents in parallel. Run any ag… |
| [google/ax](https://github.com/google/ax) | 14,097 | Go | Hot | Agent Executor (AX) is Google's open agentic orchestration runtime |
| [idosal/git-mcp](https://github.com/idosal/git-mcp) | 8,491 | TypeScript | Declining | Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server … |
| [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | 7,437 | Python | Hot | PaperBanana: Automating Academic Illustration For AI Scientists |
| [Zipstack/unstract](https://github.com/Zipstack/unstract) | 7,299 | Python | Mature | LLM-Driven Extraction of Unstructured Data — Built for API Deployments & ETL Pipelin… |
| [mutonby/openshorts](https://github.com/mutonby/openshorts) | 7,103 | Python | Hot | Open source AI clip generator: turns long videos into viral 9:16 shorts with AI mome… |
| [Zuhaitz-dev/zenc-lang](https://github.com/Zuhaitz-dev/zenc-lang) | 4,320 | C | Rising | Write like a high-level language, run like C. |
| [openenv/OpenEnv](https://github.com/openenv/OpenEnv) | 2,780 | Python | Hot | An interface library for RL post training with environments. |
| [XHToken/Spark-X2.6](https://github.com/XHToken/Spark-X2.6) | 850 | — | Rising | Spark-x2.6 open model series. Pushing the Limits of Agentic Capabilities in On-Devic… |
| [addyosmani/clarity](https://github.com/addyosmani/clarity) | 317 | JavaScript | Hot | Clarity - an Agent skill for clearer writing |
| [MotleyAI/slayer](https://github.com/MotleyAI/slayer) | 313 | Python | Rising | An embeddable, expressive semantic layer for AI agents and humans |
| [facebookresearch/swe-sweep](https://github.com/facebookresearch/swe-sweep) | 196 | Python | Declining | How many bugs can LMs find & fix in large codebases? |
| [superlinked/synty](https://github.com/superlinked/synty) | 12 | Rust | Mature | Local-first memory for you and your coding agents. Every session and PR, searchable;… |
| [rnckp/awesome-ai-switzerland](https://github.com/rnckp/awesome-ai-switzerland) | 12 | Python | Rising | A curated list of Apertus models, datasets, tools, research, and community projects … |
| [douzog/How-to-Build-Your-Own-Neural-Network](https://github.com/douzog/How-to-Build-Your-Own-Neural-Network) | 4 | HTML | Mature | — |
| [superlinked/terraform-azure-sie](https://github.com/superlinked/terraform-azure-sie) | 3 | HCL | Rising | Terraform module for deploying SIE on Azure AKS |
| [superlinked/terraform-aws-sie](https://github.com/superlinked/terraform-aws-sie) | 3 | HCL | Rising | Terraform module for deploying SIE on Amazon EKS |
| [superlinked/naky](https://github.com/superlinked/naky) | 2 | Rust | Mature | Convert AV1 screen recordings into compact ScreenEvents for reasoning models. |
| [skkim7821/site-guard-ai](https://github.com/skkim7821/site-guard-ai) | 2 | TypeScript | Declining | — |
| [prakash-aryan/parlamentsthemen](https://github.com/prakash-aryan/parlamentsthemen) | 1 | Python | Mature | Topic classification for Swiss parliamentary affairs with Apertus |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 137-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [meta-llama/prompt-ops](https://github.com/meta-llama/prompt-ops) | 1.5 | -1.7 | **-113%** of prior pace | 6mo ago | Declining |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 2.2 | -1.7 | **-77%** of prior pace | 7mo ago | Declining |
| [deeplethe/forkd](https://github.com/deeplethe/forkd) | 5.4 | -3.0 | **-56%** of prior pace | 0d ago | Rising |
| [hexabot-ai/Hexabot](https://github.com/hexabot-ai/Hexabot) | 1.3 | -0.7 | **-55%** of prior pace | 1mo ago | Mature |
| [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | 5.2 | -1.1 | **-22%** of prior pace | 11d ago | Declining |
| [bigskysoftware/htmx](https://github.com/bigskysoftware/htmx) | 10.1 | -0.9 | **-8%** of prior pace | 4d ago | Classic |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | 13.7 | -1.1 | **-8%** of prior pace | 23d ago | Mature |
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | 2.6 | -0.1 | **-5%** of prior pace | 7mo ago | Declining |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | 43.4 | -0.7 | **-2%** of prior pace | 0d ago | Classic |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | 6.9 | 0.0 | **0%** of prior pace | 2mo ago | Mature |
| [ethereum/go-ethereum](https://github.com/ethereum/go-ethereum) | 2.1 | 0.0 | **0%** of prior pace | 0d ago | Classic |
| [russellromney/honker](https://github.com/russellromney/honker) | 1.6 | 0.0 | **0%** of prior pace | 0d ago | Hot |
| [Suvink/cut-it-out](https://github.com/Suvink/cut-it-out) | 1.9 | 0.0 | **0%** of prior pace | 10mo ago | Declining |
| [Njengah/claude-code-cheat-sheet](https://github.com/Njengah/claude-code-cheat-sheet) | 1.3 | 0.0 | **0%** of prior pace | 5mo ago | Declining |
| [langchain-ai/agentevals](https://github.com/langchain-ai/agentevals) | 1.0 | 0.0 | **0%** of prior pace | 3mo ago | Declining |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **23 of the graph's 43 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 2** (10): `morluto/rea`, `DietrichGebert/ponytail`, `Graphify-Labs/graphify`, `affaan-m/ECC`, `nextlevelbuilder/ui-ux-pro-max-skill`, `cathrynlavery/diagram-design`, `paperclipai/paperclip`, `akitaonrails/ai-memory`, `msitarzewski/agency-agents`, `addyosmani/agent-skills`
- **Community 21** (2): `cloudflare/security-audit-skill`, `deepseek-ai/deepseek-harness`
- **Community 3** (2): `stablyai/orca`, `awesome-selfhosted/awesome-selfhosted`
- **Community 35** (2): `ifixai-ai/iFixAi`, `HKUDS/CLI-Anything`
- **Community 0** (2): `anomalyco/opencode`, `luongnv89/claude-howto`
- **Community 11** (2): `tashfeenahmed/freellmapi`, `ruvnet/ruflo`
- **Community 29** (2): `obra/superpowers`, `supabase/supabase`
- **Community 9** (2): `rohitg00/ai-engineering-from-scratch`, `farion1231/cc-switch`
- **Community 8** (2): `calesthio/OpenMontage`, `harry0703/MoneyPrinterTurbo`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `addyosmani/agent-skills` ⇄ `cathrynlavery/diagram-design` (w=0.333) — topics: agent-skills, claude-code, codex; authors: rudycelekli
- `morluto/rea` ⇄ `deepseek-ai/deepseek-harness` (w=0.250) — topics: ai-agents, dsh-plugin, cordis, dsh
- `calesthio/OpenMontage` ⇄ `harry0703/MoneyPrinterTurbo` (w=0.232) — topics: ffmpeg, python, text-to-speech; authors: rudycelekli, ac1982
- `tashfeenahmed/freellmapi` ⇄ `ruvnet/ruflo` (w=0.119) — authors: kevin9327

**What the risers are written in** — language mix of the top 40 movers:

- **Python** — 14
- **TypeScript** — 11
- **JavaScript** — 4
- **Rust** — 4
- **—** — 3
- **Shell** — 2
- **C++** — 1
- **HTML** — 1

## Methodology & caveats

- **Source**: `data/snapshots/*.json` diffed against `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-07-27, 2026-08-07, 2026-08-11, 2026-08-28, 2026-08-29, 2026-08-31, 2026-09-06, 2026-09-07, 2026-09-12, 2026-09-14, 2026-09-21, 2026-09-25, 2026-09-28, 2026-09-29, 2026-10-05, 2026-10-10, 2026-10-11, 2026-10-19, 2026-10-24, 2026-10-26 (24 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. The recent window therefore does not always use the immediately preceding snapshot: it uses the newest one at least 7 days back, because a 1-day window amplifies noise far more than it reveals movement. Per-day normalization keeps the boards comparable across refreshes either way.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 2,387 · Window: 2026-10-19 → 2026-10-26 (7d) · Snapshot: 2026-10-26T11:46:04.025Z</sub>
