# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 2,585 starred repos (snapshot `2026-11-01T12:41:55.392Z`), cross-referenced with the repo-similarity graph (2,585 nodes / 8,670 edges, 45 communities).
>
> Generated 2026-11-01 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

![Biggest star gains (8d)](assets/trending-now-top-tools.svg)

![Repos by movement type](assets/trending-now-categories.svg)


## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-10-24` → `2026-11-01` (**8 days**), covering the **2,395 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-11-01` (**143 days**).
  - The immediately preceding snapshot (`2026-10-26`) is only 6 days before this one — too short to separate signal from noise — so the baseline was widened to the newest snapshot at least 7 days back.
- **1,857 repos gained stars** in the recent window, adding **438,765★** between them.
- **190 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-10-24 → 2026-11-01, 8d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | **+39,896** | 4987.0 | 416,986 | TypeScript | Hot | very active |
| 2 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+12,766** | 1595.8 | 97,339 | Python | Rising | very active |
| 3 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+12,096** | 1512.0 | 55,860 | JavaScript | Declining | active |
| 4 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | **+10,812** | 1351.5 | 53,326 | Python | Rising | very active |
| 5 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | **+8,059** | 1007.4 | 42,009 | Python | Hot | very active |
| 6 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | **+7,584** | 948.0 | 267,930 | TypeScript | Hot | very active |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | **+7,350** | 918.8 | 112,070 | TypeScript | Hot | very active |
| 8 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **+6,514** | 814.2 | 294,401 | JavaScript | Hot | very active |
| 9 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+6,431** | 803.9 | 181,805 | JavaScript | Hot | very active |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | **+5,984** | 748.0 | 140,281 | Python | Hot | very active |
| 11 | [obra/superpowers](https://github.com/obra/superpowers) | **+5,778** | 722.2 | 310,340 | Shell | Mature | active |
| 12 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | **+5,743** | 717.9 | 108,499 | TypeScript | Hot | very active |
| 13 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | **+5,692** | 711.5 | 119,283 | Python | Mature | very active |
| 14 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | **+5,554** | 694.2 | 37,349 | C++ | Rising | very active |
| 15 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | **+5,484** | 685.5 | 76,814 | TypeScript | Hot | very active |
| 16 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | **+4,613** | 576.6 | 45,415 | TypeScript | Hot | very active |
| 17 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **+4,466** | 558.2 | 227,738 | — | Declining | stale |
| 18 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **+4,203** | 525.4 | 528,251 | — | Mature | active |
| 19 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | **+4,097** | 512.1 | 68,577 | Python | Hot | very active |
| 20 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **+3,774** | 471.8 | 143,621 | Python | Hot | very active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 8-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [fabio-rovai/open-ontologies](https://github.com/fabio-rovai/open-ontologies) | **+99%** | +1,324 | 2,657 | Plan, apply and roll back changes to a production ontology, with a blast radius report a… |
| 2 | [decodingai-magazine/building-a-coding-agent-from-scratch-course](https://github.com/decodingai-magazine/building-a-coding-agent-from-scratch-course) | **+49%** | +361 | 1,092 | Learn harness engineering by building Claude Code from scratch. Free, open-source course… |
| 3 | [Graphicle-AI/graphicle](https://github.com/Graphicle-AI/graphicle) | **+38%** | +133 | 485 | Code graph and memory for your coding agents, in one Rust program. For Claude Code, Code… |
| 4 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | **+31%** | +2,190 | 9,226 | Open-source AI coworkers that each get a computer of their own: a browser, files and too… |
| 5 | [termio-sh/termio](https://github.com/termio-sh/termio) | **+29%** | +170 | 752 | A terminal-first agentic development environment for agentic coding. Build for CLI/TUI a… |
| 6 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+28%** | +12,096 | 55,860 | A coding-agent skill for multi-phase security audits with independently verified, machin… |
| 7 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | **+25%** | +10,812 | 53,326 | DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/. |
| 8 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | **+24%** | +8,059 | 42,009 | Independent Auditing of AI Agents. Run by human or the agent itself, to answer the most … |
| 9 | [HelixDB/helix-foundry](https://github.com/HelixDB/helix-foundry) | **+18%** | +296 | 1,955 | Connect your company's data, let an agent draft an ontology over it, and load it into He… |
| 10 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | **+17%** | +5,554 | 37,349 | Qwen3.8-Flash-Next on any consumer hardware: one-click install for Windows / Linux. Stra… |
| 11 | [nateherkai/herk-edit-kit](https://github.com/nateherkai/herk-edit-kit) | **+17%** | +356 | 2,474 | Herk Edit Kit by Nate Herk: edit videos, reels, and YouTube Shorts with Codex or Claude … |
| 12 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+15%** | +12,766 | 97,339 | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voic… |
| 13 | [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) | **+13%** | +450 | 3,811 | HarnessRouter Community Edition: the self-hosted, Apache-2.0 edition of the unified inte… |
| 14 | [cporter202/agentic-ai-apis](https://github.com/cporter202/agentic-ai-apis) | **+13%** | +86 | 746 | The ultimate collection of APIs for building autonomous AI agents — 2,036 production-rea… |
| 15 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | **+12%** | +2,541 | 23,774 | Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, securi… |
| 16 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | **+12%** | +1,561 | 14,774 | Solution for long term memory for agent coding CLIs and to facilitate handoff between di… |
| 17 | [google/artemis](https://github.com/google/artemis) | **+12%** | +1,662 | 15,997 | ARTEMIS turns natural-language instructions into reliable Android automation. It automat… |
| 18 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | **+11%** | +4,613 | 45,415 | 7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behin… |
| 19 | [morluto/rea](https://github.com/morluto/rea) | **+11%** | +39,896 | 416,986 | Reverse engineer anything with agents, from app behavior down to native binaries. |
| 20 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | **+9%** | +2,282 | 28,367 | Huashu Design 3.0 · 在 agent 里打一句话，拿回能交付的设计：网页 / App 原型 / 可编辑 PPTX / 动画 / 信息图 · 六个候选挑三个方向… |

## Sustained climbers — long run (2026-06-11 → 2026-11-01, 143d)

Averaged over the full snapshot history, so a single viral week doesn't dominate. Repos high here *and* in the recent board are compounding, not spiking.

| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |
|---|---|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | **598.6** | +85,606 | 310,340 | Shell | 64 |
| 2 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **566.2** | +80,967 | 294,401 | JavaScript | 79 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **478.4** | +68,417 | 259,350 | Python | 75 |
| 4 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **461.6** | +66,010 | 197,537 | TypeScript | 86 |
| 5 | [earendil-works/pi](https://github.com/earendil-works/pi) | **402.1** | +57,497 | 119,275 | TypeScript | 80 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **380.0** | +54,333 | 165,786 | Shell | 63 |
| 7 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **379.4** | +54,258 | 227,738 | — | 19 |
| 8 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **373.2** | +53,370 | 528,251 | — | 48 |
| 9 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **371.9** | +53,183 | 143,621 | Python | 95 |
| 10 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **371.7** | +53,149 | 494,010 | Python | 64 |
| 11 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **365.7** | +52,300 | 150,779 | Rust | 79 |
| 12 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **356.4** | +50,964 | 137,061 | Python | 85 |
| 13 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **353.3** | +50,517 | 223,717 | TypeScript | 84 |
| 14 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | **349.7** | +50,001 | 76,814 | TypeScript | 79 |
| 15 | [usestrix/strix](https://github.com/usestrix/strix) | **330.2** | +47,215 | 73,161 | Python | 75 |
| 16 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | **315.3** | +45,091 | 116,606 | Go | 84 |
| 17 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | **312.0** | +44,616 | 47,933 | C | 76 |
| 18 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **304.8** | +43,582 | 558,011 | Markdown | 28 |
| 19 | [openai/codex](https://github.com/openai/codex) | **295.1** | +42,199 | 132,657 | Rust | 93 |
| 20 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **295.0** | +42,185 | 193,328 | Python | 89 |

## Emerging themes

The boards above are computed; this section is interpretation. Each theme groups movers that are rising for the same underlying reason.

### Skills as the packaging format for agent behaviour

_The single loudest signal in this dataset. A year ago you configured an agent with a prompt; now behaviour ships as a versioned, installable *skill* bundle — and the repos distributing those bundles are growing faster than the agents that consume them. Note what this implies: the moat is moving from the model to the instruction layer._

- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 294,401★ · +6,514★ in 8d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 181,805★ · +6,431★ in 8d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 310,340★ · +5,778★ in 8d  
  An agentic skills framework & software development methodology that works.
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 227,738★ · +4,466★ in 8d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 143,621★ · +3,774★ in 8d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 186,105★ · +2,640★ in 8d  
  Public repository for Agent Skills
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 165,786★ · +2,119★ in 8d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · 59,640★ · +1,064★ in 8d  
  A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 138,527★ · +1,035★ in 8d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 57,014★ · +596★ in 8d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC (no affiliation). A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 68,398★ · +432★ in 8d  
  from vibe coding to agentic engineering - practice makes claude perfect

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 140,281★ · +5,984★ in 8d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 108,499★ · +5,743★ in 8d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 89,518★ · +1,471★ in 8d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 76,111★ · +904★ in 8d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 47,933★ · +536★ in 8d  
  Local code intelligence for developers and AI agents. Connect code, docs and infrastructure in a persistent graph, with CBM Lens, MCP tools, agent integrations and change-aware test selection.
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 30,312★ · +424★ in 8d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 17,652★ · +276★ in 8d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 32,974★ · +256★ in 8d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory with small models for free
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 8,080★ · +186★ in 8d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 14,367★ · +153★ in 8d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,664★ · +20★ in 8d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 45,468★ · +1,769★ in 8d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 41,464★ · +917★ in 8d  
  AirLLM 2.8T LLM inference with single 4GB GPU
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 133,039★ · +811★ in 8d  
  LLM inference in C/C++
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,730★ · +179★ in 8d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,604★ · +8★ in 8d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 65,583★ · +2,511★ in 8d  
  Use Claude Code, Codex, Antigravity, VSCode, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly)
- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 116,606★ · +1,826★ in 8d  
  🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.
- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 45,468★ · +1,769★ in 8d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 78,507★ · +796★ in 8d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 85,180★ · +729★ in 8d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 109,699★ · +2,846★ in 8d  
  The open-source app everyone uses to manage agents at work
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 223,717★ · +2,707★ in 8d  
  The open source coding agent.
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 259,350★ · +2,607★ in 8d  
  The agent that grows with you
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 150,779★ · +2,477★ in 8d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode,DeepSeek Harness and more. Only official website: ccswitch.io
- **[openai/codex](https://github.com/openai/codex)** · 132,657★ · +1,866★ in 8d  
  Lightweight coding agent that runs in your terminal
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 119,275★ · +1,694★ in 8d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 80,472★ · +1,506★ in 8d  
  🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 154,131★ · +866★ in 8d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 22,684★ · +811★ in 8d  
  Orchestrate multiple coding agents from desktop and mobile
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 54,489★ · +778★ in 8d  
  Make humans and AI agents work as one team — open-source and self-hostable.
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 92,408★ · +675★ in 8d  
  🙌 OpenHands: AI-Driven Development
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 84,817★ · +439★ in 8d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 70,569★ · +260★ in 8d  
  OmO: Just type "mass ulw" keyword with your prompt. Now you are the master of graph engineering.
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 21,383★ · +200★ in 8d  
  High performance coding agent harness written in Rust, built for heavy multi-agent dev workflows
- **[vercel/eve](https://github.com/vercel/eve)** · 5,756★ · +90★ in 8d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 53,326★ · +10,812★ in 8d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 119,283★ · +5,692★ in 8d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 76,814★ · +5,484★ in 8d  
  Write HTML. Render video. Built for agents.
- **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** · 79,148★ · +2,170★ in 8d  
  Open-source AI job search agent and job finder: scan job boards, score each job 1-5 against your CV before you apply, tailor an ATS-friendly resume and cover letter, get interview prep and an application tracker. It helps you fill in each application; you press Submit. Runs locally in Codex, OpenCode and other AI CLIs, or as a Claude Code plugin.
- **[usestrix/strix](https://github.com/usestrix/strix)** · 73,161★ · +1,540★ in 8d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 37,338★ · +823★ in 8d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 59,172★ · +724★ in 8d  
  The open-source AI voice studio. Clone, dictate, create.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 119,728★ · +681★ in 8d  
  Open-source Python library for AI browser agents, plus Browser Use Cloud: stealth browsers and a hosted agent API.
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 32,357★ · +238★ in 8d  
  Privacy first AI meeting note taker. Download Free and open source granola, otter ai, fireflies alternative. Parakeet / Whisper live transcription, on-device speaker diarization, built on Rust. 100% local processing. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker & Assistant for macOS & Windows
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 18,029★ · +68★ in 8d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 143,621★ · +3,774★ in 8d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[github/spec-kit](https://github.com/github/spec-kit)** · 144,677★ · +1,974★ in 8d  
  💫 Toolkit to help you get started with SDD or any other process!
- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 124,981★ · +1,674★ in 8d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 105,260★ · +1,526★ in 8d  
  The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create motion, prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [react/react](https://github.com/react/react) | 252,064 | JavaScript | Classic | The library for web and native user interfaces. |
| [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms) | 196,713 | JavaScript | Mature | 📝 Algorithms and data structures implemented in JavaScript with explanations and lin… |
| [twbs/bootstrap](https://github.com/twbs/bootstrap) | 174,971 | MDX | Classic | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobi… |
| [vercel/next.js](https://github.com/vercel/next.js) | 143,466 | JavaScript | Classic | The React Framework |
| [denoland/deno](https://github.com/denoland/deno) | 108,782 | Rust | Classic | A modern runtime for JavaScript and TypeScript. |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 107,387 | JavaScript | Hot | Agent skills that give coding agents taste: art direction, reference images and a br… |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 98,795 | Rust | Hot | The design vocabulary for your coding agent. Steer with polish and bolder, review wi… |
| [sveltejs/svelte](https://github.com/sveltejs/svelte) | 88,516 | JavaScript | Classic | web development for the rest of us |
| [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) | 80,957 | Python | Mature | Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) |
| [nektos/act](https://github.com/nektos/act) | 72,510 | Go | Classic | Run your GitHub Actions locally 🚀 |
| [meta/docusaurus](https://github.com/meta/docusaurus) | 66,622 | TypeScript | Classic | Easy to maintain open source documentation websites. |
| [git/git](https://github.com/git/git) | 64,104 | C | Classic | Git Source Code Mirror - This is a publish-only repository but pull requests can be … |
| [TryGhost/Ghost](https://github.com/TryGhost/Ghost) | 55,649 | TypeScript | Classic | Independent technology for modern publishing, memberships, subscriptions and newslet… |
| [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | 55,085 | Python | Mature | Open-Source Frontier Voice AI |
| [wagoodman/dive](https://github.com/wagoodman/dive) | 54,686 | Go | Mature | A tool for exploring each layer in a docker image |
| [dockur/windows](https://github.com/dockur/windows) | 53,980 | Shell | Mature | Windows inside a Docker container. |
| [cypress-io/cypress](https://github.com/cypress-io/cypress) | 51,019 | TypeScript | Classic | Fast, easy and reliable testing for anything that runs in a browser. |
| [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | 48,415 | Python | Hot | Debloat any Android or Google TV over Wi-Fi and get an Apple TV-style home. |
| [moment/moment](https://github.com/moment/moment) | 47,885 | JavaScript | Classic | Parse, validate, manipulate, and display dates in javascript. |
| [helix-editor/helix](https://github.com/helix-editor/helix) | 46,760 | Rust | Mature | A post-modern modal text editor. |
| [ziglang/zig](https://github.com/ziglang/zig) | 43,257 | Zig | Declining | Moved to Codeberg |
| [trpc/trpc](https://github.com/trpc/trpc) | 40,758 | TypeScript | Classic | 🧙‍♀️  Move Fast and Break Nothing. End-to-end typesafe APIs made easy. |
| [vlang/v](https://github.com/vlang/v) | 38,080 | V | Classic | Simple, fast, safe, compiled language for developing maintainable software. Compiles… |
| [p-e-w/heretic](https://github.com/p-e-w/heretic) | 37,339 | Python | Hot | Training-free language model modification: Remove censorship, suppress slop, reduce … |
| [lerna/lerna](https://github.com/lerna/lerna) | 36,041 | TypeScript | Classic | Lerna is a fast, modern build system for managing and publishing multiple JavaScript… |
| [sahat/hackathon-starter](https://github.com/sahat/hackathon-starter) | 35,259 | JavaScript | Classic | A boilerplate for Node.js web applications |
| [huggingface/diffusers](https://github.com/huggingface/diffusers) | 34,843 | Python | Classic | 🤗 Diffusers: State-of-the-art diffusion models for image, video, and audio generatio… |
| [motiondivision/motion](https://github.com/motiondivision/motion) | 34,755 | TypeScript | Classic | A modern animation library for React and JavaScript |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | 34,286 | Python | Hot | Open source repository of plugins primarily intended for knowledge workers to use in… |
| [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | 33,519 | Python | Classic | SOTA Open Source TTS |
| [influxdata/influxdb](https://github.com/influxdata/influxdb) | 31,793 | Rust | Mature | Scalable datastore for metrics, events, and real-time analytics |
| [ReactiveX/rxjs](https://github.com/ReactiveX/rxjs) | 31,714 | TypeScript | Mature | A reactive programming library for JavaScript |
| [openssl/openssl](https://github.com/openssl/openssl) | 31,148 | C | Classic | General purpose TLS and crypto library |
| [sampotts/plyr](https://github.com/sampotts/plyr) | 29,995 | JavaScript | Classic | Deprecated in favour of Video.js 10; security updates only. Simple HTML5, YouTube an… |
| [meta/zstd](https://github.com/meta/zstd) | 28,144 | C | Classic | Zstandard - Fast real-time compression algorithm |
| [squidfunk/mkdocs-material](https://github.com/squidfunk/mkdocs-material) | 27,598 | Python | Classic | Documentation that simply works |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | 27,587 | — | Rising | PM Skills Marketplace: 100+ agentic skills, commands, and plugins — from discovery t… |
| [typesense/typesense](https://github.com/typesense/typesense) | 27,073 | C++ | Classic | Open Source alternative to Algolia + Pinecone and an Easier-to-Use alternative to El… |
| [simple-icons/simple-icons](https://github.com/simple-icons/simple-icons) | 26,117 | JavaScript | Classic | SVG icons for popular brands |
| [dubinc/dub.link](https://github.com/dubinc/dub.link) | 25,069 | TypeScript | Classic | The modern link attribution platform. Loved by world-class engineering teams at Twil… |
| _…and 150 more_ | | | | |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 143-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | 9.5 | -9.2 | **-98%** of prior pace | 4d ago | Hot |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 2.1 | -1.4 | **-66%** of prior pace | 7mo ago | Declining |
| [axios/axios](https://github.com/axios/axios) | 1.6 | -0.2 | **-15%** of prior pace | 4d ago | Classic |
| [AndyMik90/Aperant](https://github.com/AndyMik90/Aperant) | 1.7 | -0.1 | **-7%** of prior pace | 4mo ago | Declining |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | 6.6 | 0.1 | **2%** of prior pace | 2mo ago | Mature |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | 41.7 | 1.4 | **3%** of prior pace | 0d ago | Classic |
| [guofei9987/blind_watermark](https://github.com/guofei9987/blind_watermark) | 11.4 | 0.5 | **4%** of prior pace | 7mo ago | Declining |
| [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | 5.0 | 0.2 | **5%** of prior pace | 2d ago | Declining |
| [python/cpython](https://github.com/python/cpython) | 32.2 | 1.8 | **5%** of prior pace | 0d ago | Classic |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 44.7 | 2.9 | **6%** of prior pace | 0d ago | Hot |
| [allenai/olmocr](https://github.com/allenai/olmocr) | 17.0 | 1.4 | **8%** of prior pace | 7mo ago | Declining |
| [andrewyng/aisuite](https://github.com/andrewyng/aisuite) | 17.9 | 1.6 | **9%** of prior pace | 1mo ago | Mature |
| [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | 44.7 | 4.1 | **9%** of prior pace | 25d ago | Rising |
| [illuin-tech/colpali](https://github.com/illuin-tech/colpali) | 1.2 | 0.1 | **10%** of prior pace | 1mo ago | Mature |
| [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | 27.1 | 3.0 | **11%** of prior pace | 2d ago | Hot |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **18 of the graph's 45 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 13** (5): `morluto/rea`, `tashfeenahmed/freellmapi`, `vectorize-io/hindsight`, `remotion-dev/remotion`, `Alishahryar1/free-claude-code`
- **Community 5** (5): `cloudflare/security-audit-skill`, `stablyai/orca`, `thedotmack/claude-mem`, `yt-dlp/yt-dlp`, `awesome-selfhosted/awesome-selfhosted`
- **Community 4** (5): `ifixai-ai/iFixAi`, `heygen-com/hyperframes`, `nextlevelbuilder/ui-ux-pro-max-skill`, `cheaper-inference/OmniRoute`, `NousResearch/hermes-agent`
- **Community 30** (5): `affaan-m/ECC`, `DietrichGebert/ponytail`, `ai-job-search-dev/ai-job-search`, `lightpanda-io/browser`, `firecrawl/firecrawl`
- **Community 15** (4): `deepseek-ai/deepseek-harness`, `sindresorhus/awesome`, `cathrynlavery/diagram-design`, `alchaincyf/huashu-design`
- **Community 11** (3): `rohitg00/ai-engineering-from-scratch`, `paperclipai/paperclip`, `anomalyco/opencode`
- **Community 7** (2): `multica-ai/andrej-karpathy-skills`, `gitroomhq/postiz-app`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `ifixai-ai/iFixAi` ⇄ `alchaincyf/huashu-design` (w=0.286) — authors: dajiaohuang, Aliciawque
- `morluto/rea` ⇄ `rohitg00/ai-engineering-from-scratch` (w=0.282) — topics: mcp, rea, python, typescript; authors: rohitg00
- `morluto/rea` ⇄ `heygen-com/hyperframes` (w=0.217) — topics: mcp, claude-code, typescript, ai

**What the risers are written in** — language mix of the top 40 movers:

- **Python** — 15
- **TypeScript** — 12
- **JavaScript** — 3
- **—** — 3
- **Rust** — 2
- **HTML** — 2
- **Shell** — 1
- **C++** — 1

## Methodology & caveats

- **Source**: `data/snapshots/*.json` diffed against `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-07-27, 2026-08-07, 2026-08-11, 2026-08-28, 2026-08-29, 2026-08-31, 2026-09-06, 2026-09-07, 2026-09-12, 2026-09-14, 2026-09-21, 2026-09-25, 2026-09-28, 2026-09-29, 2026-10-05, 2026-10-10, 2026-10-11, 2026-10-19, 2026-10-24, 2026-10-26, 2026-11-01 (25 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. The recent window therefore does not always use the immediately preceding snapshot: it uses the newest one at least 7 days back, because a 1-day window amplifies noise far more than it reveals movement. Per-day normalization keeps the boards comparable across refreshes either way.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 2,395 · Window: 2026-10-24 → 2026-11-01 (8d) · Snapshot: 2026-11-01T12:41:55.392Z</sub>
