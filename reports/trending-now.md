# Trending Now — What's Actually Moving in Your Stars

> Derived from **kaiser-data**'s 2,211 starred repos (snapshot `2026-09-21T11:17:33.969Z`), cross-referenced with the repo-similarity graph (2,211 nodes / 7,301 edges, 35 communities).
>
> Generated 2026-09-21 by `scripts/reports/trending_now.py` (regenerate any time — no API cost).

![Biggest star gains (7d)](assets/trending-now-top-tools.svg)

![Repos by movement type](assets/trending-now-categories.svg)


## Executive summary

- **This is the only report here that measures *change* rather than describing a landscape.** Every other report curates a taxonomy and renders it against the current vintage; this one diffs archived snapshots to show what actually moved.
- **Window**: `2026-09-14` → `2026-09-21` (**7 days**), covering the **2,155 repos** present in both snapshots. Long-run comparisons use `2026-06-11` → `2026-09-21` (**102 days**).
- **1,712 repos gained stars** in the recent window, adding **316,725★** between them.
- **56 repos are new to the dataset** since the last refresh — newly starred, so they have no baseline to diff and are listed separately.
- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a lifetime-stars/day proxy (its own source comment calls it "a serviceable proxy"). Everything below is observed snapshot-to-snapshot movement over a known number of days.

## How to read this

| Board | Question it answers | Bias to watch |
|---|---|---|
| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |
| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at 300★ baseline so noise doesn't win. |
| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |
| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |
| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |

## Fastest risers — absolute (2026-09-14 → 2026-09-21, 7d)

Raw star gain over the window. `Stars/day` normalizes for window length so this stays comparable across refreshes of different spacing.

| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |
|---|---|---|---|---|---|---|---|
| 1 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+15,257** | 2179.6 | 18,543 | JavaScript | Rising | active |
| 2 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | **+14,665** | 2095.0 | 38,849 | Go | Hot | very active |
| 3 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | **+8,549** | 1221.3 | 231,895 | TypeScript | Hot | very active |
| 4 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **+6,265** | 895.0 | 264,290 | JavaScript | Hot | very active |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | **+5,888** | 841.1 | 74,151 | TypeScript | Hot | very active |
| 6 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | **+5,787** | 826.7 | 36,687 | C | Hot | very active |
| 7 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+5,716** | 816.6 | 33,726 | Python | Hot | very active |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **+5,592** | 798.9 | 143,416 | JavaScript | Hot | very active |
| 9 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | **+5,282** | 754.6 | 28,330 | Go | Hot | very active |
| 10 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | **+4,639** | 662.7 | 49,529 | Python | Hot | very active |
| 11 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | **+3,767** | 538.1 | 97,960 | JavaScript | Hot | very active |
| 12 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | **+3,467** | 495.3 | 120,040 | Python | Hot | very active |
| 13 | [obra/superpowers](https://github.com/obra/superpowers) | **+3,068** | 438.3 | 289,511 | Shell | Hot | very active |
| 14 | [earendil-works/pi](https://github.com/earendil-works/pi) | **+3,041** | 434.4 | 107,989 | TypeScript | Hot | very active |
| 15 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | **+2,836** | 405.1 | 68,741 | TypeScript | Hot | very active |
| 16 | [trycua/cua](https://github.com/trycua/cua) | **+2,823** | 403.3 | 25,441 | HTML | Hot | very active |
| 17 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **+2,564** | 366.3 | 182,753 | TypeScript | Mature | very active |
| 18 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **+2,507** | 358.1 | 508,412 | — | Mature | active |
| 19 | [Human-Agent-Society/reef](https://github.com/Human-Agent-Society/reef) | **+2,477** | 353.9 | 3,842 | Python | Hot | very active |
| 20 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | **+2,408** | 344.0 | 147,379 | TypeScript | Mature | very active |

## Breakouts — fastest relative growth (≥300★ baseline)

Percent growth over the same 7-day window. The baseline floor keeps small-number noise off the board — a repo going 8★ → 20★ is not a trend.

| # | Repo | Growth | Gain | Stars now | What it is |
|---|---|---|---|---|---|
| 1 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | **+464%** | +15,257 | 18,543 | A coding-agent skill for multi-phase security audits with independently verified, machin… |
| 2 | [Human-Agent-Society/reef](https://github.com/Human-Agent-Society/reef) | **+181%** | +2,477 | 3,842 | Continual learning infra for self-improving agents |
| 3 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | **+61%** | +14,665 | 38,849 | Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code revi… |
| 4 | [NVlabs/SoL-Pi](https://github.com/NVlabs/SoL-Pi) | **+51%** | +939 | 2,765 | SoL-Pi: Scaling Auto-Research Loops for Efficient Agent Harnesses |
| 5 | [jmiao24/Paper2Agent](https://github.com/jmiao24/Paper2Agent) | **+37%** | +861 | 3,214 | Paper2Agent is a multi-agent AI system that automatically transforms research papers int… |
| 6 | [deeplethe/utopia](https://github.com/deeplethe/utopia) | **+30%** | +2,181 | 9,554 | World's first open-source enterprise world model. |
| 7 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | **+23%** | +5,282 | 28,330 | Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomo… |
| 8 | [spotify/portal-ai-plugins](https://github.com/spotify/portal-ai-plugins) | **+23%** | +373 | 2,028 | — |
| 9 | [Anakin-Inc/anakin](https://github.com/Anakin-Inc/anakin) | **+22%** | +796 | 4,403 | Open-source web scraping API. Turn any website into clean markdown or structured JSON. A… |
| 10 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | **+20%** | +5,716 | 33,726 | VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voic… |
| 11 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | **+19%** | +5,787 | 36,687 | Run frontier MoE models on hardware you already own — pure C, zero deps, experts streame… |
| 12 | [lnkiai/m3e-canvas](https://github.com/lnkiai/m3e-canvas) | **+18%** | +1,196 | 7,872 | Sketch Material 3 Expressive screens in the browser and turn them into vibe-coding promp… |
| 13 | [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) | **+18%** | +248 | 1,655 | HarnessRouter Community Edition: the self-hosted, Apache-2.0 edition of the unified inte… |
| 14 | [trailhq/Graft](https://github.com/trailhq/Graft) | **+17%** | +1,299 | 8,888 | Turbocharge Claude Code, Cursor, Codex, Gemini & every coding agent: faster, cheaper, wi… |
| 15 | [NVIDIA/Personal-AI-Router](https://github.com/NVIDIA/Personal-AI-Router) | **+14%** | +175 | 1,449 | Router that virtually distributes inference across connected devices in the home. |
| 16 | [fastino-ai/GLiNER2](https://github.com/fastino-ai/GLiNER2) | **+13%** | +247 | 2,104 | Unified Schema-Based Information Extraction |
| 17 | [nvidia-isaac/video_to_data](https://github.com/nvidia-isaac/video_to_data) | **+13%** | +80 | 703 | Nvidia Isaac Video to Data Pipeline |
| 18 | [trycua/cua](https://github.com/trycua/cua) | **+12%** | +2,823 | 25,441 | Scale computer-use 2.0 with open-source drivers, cross-OS fleets, and benchmarks for tra… |
| 19 | [termio-sh/termio](https://github.com/termio-sh/termio) | **+12%** | +57 | 524 | A terminal-first agentic development environment for agentic coding. Build for CLI/TUI a… |
| 20 | [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | **+12%** | +701 | 6,571 | The secure, validated skill registry for professional AI coding agents. Extend Antigravi… |

## Sustained climbers — long run (2026-06-11 → 2026-09-21, 102d)

Averaged over the full snapshot history, so a single viral week doesn't dominate. Repos high here *and* in the recent board are compounding, not spiking.

| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |
|---|---|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | **635.1** | +64,777 | 289,511 | Shell | 75 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | **555.8** | +56,694 | 247,627 | Python | 75 |
| 3 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | **502.2** | +51,226 | 182,753 | TypeScript | 84 |
| 4 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | **498.6** | +50,856 | 264,290 | JavaScript | 79 |
| 5 | [earendil-works/pi](https://github.com/earendil-works/pi) | **453.0** | +46,211 | 107,989 | TypeScript | 85 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | **415.8** | +42,409 | 153,862 | Shell | 58 |
| 7 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | **403.2** | +41,122 | 481,983 | Python | 65 |
| 8 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | **401.5** | +40,953 | 214,433 | — | 22 |
| 9 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | **398.3** | +40,628 | 43,945 | C | 75 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | **382.6** | +39,023 | 129,461 | Python | 97 |
| 11 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | **380.5** | +38,815 | 124,912 | Python | 85 |
| 12 | [usestrix/strix](https://github.com/usestrix/strix) | **372.5** | +37,997 | 63,943 | Python | 80 |
| 13 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | **351.2** | +35,818 | 209,018 | TypeScript | 88 |
| 14 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | **348.7** | +35,564 | 107,079 | Go | 79 |
| 15 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | **347.5** | +35,442 | 133,921 | Rust | 86 |
| 16 | [openai/codex](https://github.com/openai/codex) | **345.1** | +35,205 | 125,663 | Rust | 74 |
| 17 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | **342.5** | +34,934 | 186,077 | Python | 92 |
| 18 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | **334.4** | +34,113 | 548,542 | Markdown | 41 |
| 19 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | **332.7** | +33,936 | 97,390 | TypeScript | 82 |
| 20 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | **328.7** | +33,531 | 508,412 | — | 54 |

## Emerging themes

The boards above are computed; this section is interpretation. Each theme groups movers that are rising for the same underlying reason.

### Skills as the packaging format for agent behaviour

_The single loudest signal in this dataset. A year ago you configured an agent with a prompt; now behaviour ships as a versioned, installable *skill* bundle — and the repos distributing those bundles are growing faster than the agents that consume them. Note what this implies: the moat is moving from the model to the instruction layer._

- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 264,290★ · +6,265★ in 7d  
  The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** · 143,416★ · +5,592★ in 7d  
  Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
- **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** · 49,529★ · +4,639★ in 7d  
  A skill to stop your coding agent from burying the answer. ADHD-friendly output.
- **[obra/superpowers](https://github.com/obra/superpowers)** · 289,511★ · +3,068★ in 7d  
  An agentic skills framework & software development methodology that works.
- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 129,461★ · +1,965★ in 7d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** · 153,862★ · +1,644★ in 7d  
  A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.
- **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** · 214,433★ · +1,555★ in 7d  
  A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 177,403★ · +1,187★ in 7d  
  Public repository for Agent Skills
- **[garrytan/gstack](https://github.com/garrytan/gstack)** · 133,829★ · +888★ in 7d  
  Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA
- **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** · 54,379★ · +376★ in 7d  
  A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** · 66,157★ · +249★ in 7d  
  from vibe coding to agentic engineering - practice makes claude perfect

### Giving agents a memory of the codebase

_Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and persistent stores an agent can consult instead of re-reading files every session. This is the same insight the graph in this repo is built on, and it is now one of the fastest-moving categories in your stars._

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** · 120,040★ · +3,467★ in 7d  
  Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** · 71,675★ · +902★ in 7d  
  Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local
- **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** · 83,513★ · +871★ in 7d  
  Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
- **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** · 43,945★ · +764★ in 7d  
  High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.
- **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** · 94,376★ · +550★ in 7d  
  Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** · 13,347★ · +492★ in 7d  
  Graph-Native Infrastructure for Context and Accountable AI Systems
- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 27,085★ · +443★ in 7d  
  TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.
- **[repowise-dev/repowise](https://github.com/repowise-dev/repowise)** · 6,759★ · +331★ in 7d  
  Codebase intelligence for AI and humans: code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.
- **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** · 16,686★ · +221★ in 7d  
  OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 30,880★ · +206★ in 7d  
  Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine.
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,557★ · +32★ in 7d  
  Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

### Frontier models on hardware you already own

_The counter-current to everything above: instead of making API calls cheaper, remove them. Big mixture-of-experts models are being squeezed onto consumer machines, and the repos doing it are among the fastest relative movers in the dataset._

- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 36,687★ · +5,787★ in 7d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 129,028★ · +857★ in 7d  
  LLM inference in C/C++
- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 34,632★ · +329★ in 7d  
  AirLLM 70B inference with single 4GB GPU
- **[Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm)** · 3,429★ · +26★ in 7d  
  Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat.
- **[microsoft/foundry-local](https://github.com/microsoft/foundry-local)** · 2,555★ · +7★ in 7d  
  —

### Token economics became a product category

_Context windows got bigger and people started paying for them. These repos exist purely to make agents cheaper to run — compressing tool output, trimming prompts, proxying calls. That a compression layer can add tens of thousands of stars in weeks says the cost pressure is real, not theoretical._

- **[JustVugg/colibri](https://github.com/JustVugg/colibri)** · 36,687★ · +5,787★ in 7d  
  Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
- **[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)** · 107,079★ · +1,603★ in 7d  
  🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.
- **[headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)** · 73,339★ · +1,334★ in 7d  
  Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 81,227★ · +955★ in 7d  
  CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies
- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 55,566★ · +707★ in 7d  
  Use Claude Code, Codex, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly)

### The coding-agent harness field is still splitting, not consolidating

_Terminal coding agents keep multiplying rather than converging on a winner, and a second layer has appeared above them: switchers, meta-harnesses, and orchestrators whose job is to manage the agents themselves._

- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 107,989★ · +3,041★ in 7d  
  AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 147,379★ · +2,408★ in 7d  
  Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 247,627★ · +2,310★ in 7d  
  The agent that grows with you
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 209,018★ · +1,762★ in 7d  
  The open source coding agent.
- **[openai/codex](https://github.com/openai/codex)** · 125,663★ · +1,651★ in 7d  
  Lightweight coding agent that runs in your terminal
- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 50,979★ · +1,193★ in 7d  
  Make humans and AI agents work as one team — open-source and self-hostable.
- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 133,921★ · +1,150★ in 7d  
  A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 88,697★ · +852★ in 7d  
  🙌 OpenHands: AI-Driven Development
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 17,957★ · +730★ in 7d  
  Orchestrate multiple coding agents from desktop and mobile
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 72,973★ · +586★ in 7d  
  🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated
- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** · 81,169★ · +524★ in 7d  
  The open-source app everyone uses to manage agents at work
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 82,794★ · +386★ in 7d  
  An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 19,963★ · +297★ in 7d  
  The most RAM efficient harness
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 69,246★ · +217★ in 7d  
  OmO: Just type "mass ulw" keyword with your prompt. Now you are the master of graph engineering.
- **[vercel/eve](https://github.com/vercel/eve)** · 5,290★ · +183★ in 7d  
  The Open Framework for Building Agents

### Agents are leaving the terminal for specific jobs

_The generalist assistant is being joined by vertical agents pointed at one domain — pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a specific audience rather than on developer-tool hype._

- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 107,884★ · +2,255★ in 7d  
  TradingAgents: Multi-Agents LLM Financial Trading Framework
- **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** · 52,078★ · +2,248★ in 7d  
  Write HTML. Render video. Built for agents.
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 55,333★ · +2,164★ in 7d  
  The open-source AI voice studio. Clone, dictate, create.
- **[usestrix/strix](https://github.com/usestrix/strix)** · 63,943★ · +1,611★ in 7d  
  Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 115,688★ · +1,116★ in 7d  
  Agents that use the browser.
- **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** · 72,302★ · +758★ in 7d  
  Open-source AI job search: scan job portals, evaluate listings into a structured A-H report with a global 1-5 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, Codex, OpenCode, Antigravity…)
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 40,112★ · +537★ in 7d  
  DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/.
- **[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** · 33,764★ · +356★ in 7d  
  "Vibe-Trading: Your Personal Trading Agent"
- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 30,992★ · +257★ in 7d  
  Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai - https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows. Understand How to write meeting minutes
- **[Canner/WrenAI](https://github.com/Canner/WrenAI)** · 17,705★ · +74★ in 7d  
  GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.

### Design and spec as agent-readable artifacts

_If an agent writes the code, the leverage moves upstream to the spec and the design system. These repos turn intent into something an agent can consume directly._

- **[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** · 129,461★ · +1,965★ in 7d  
  An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.
- **[github/spec-kit](https://github.com/github/spec-kit)** · 138,139★ · +1,521★ in 7d  
  💫 Toolkit to help you get started with Spec-Driven Development
- **[nexu-io/open-design](https://github.com/nexu-io/open-design)** · 97,390★ · +1,320★ in 7d  
  🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK.
- **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** · 116,966★ · +1,176★ in 7d  
  A collection of DESIGN.md files analysis by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.

## New entrants — newly starred since the last refresh

These joined the dataset during this window, so they have no baseline to diff. They are what *you* just found interesting, which is its own kind of trend signal.

| Repo | Stars | Lang | Lifecycle | What it is |
|---|---|---|---|---|
| [google/material-design-icons](https://github.com/google/material-design-icons) | 53,998 | — | Mature | Material Design icons by Google (Material Symbols) |
| [oobabooga/textgen](https://github.com/oobabooga/textgen) | 47,696 | Python | Mature | Open-source desktop app for local LLMs. Text, vision, tool-calling, OpenAI/Anthropic… |
| [google/zx](https://github.com/google/zx) | 45,758 | JavaScript | Mature | A tool for writing better scripts |
| [faif/python-patterns](https://github.com/faif/python-patterns) | 42,994 | Python | Classic | A collection of design patterns/idioms in Python |
| [google/styleguide](https://github.com/google/styleguide) | 39,618 | HTML | Mature | Style guides for Google-originated open-source projects |
| [google/googletest](https://github.com/google/googletest) | 39,564 | C++ | Classic | GoogleTest - Google Testing and Mocking Framework |
| [google/leveldb](https://github.com/google/leveldb) | 39,432 | C++ | Declining | LevelDB is a fast key-value storage library written at Google that provides an order… |
| [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) | 29,114 | Python | Hot | Community plugin to control Blender 3D with any LLM of your choice |
| [bendlang/bend](https://github.com/bendlang/bend) | 22,222 | TypeScript | Classic | Bend 2: a fast language that blocks AI mistakes via proof. Install: curl -fsSL https… |
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 13,901 | Python | Declining | i. am. speed. |
| [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | 11,503 | TypeScript | Hot | Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retriev… |
| [huggingface/tokenizers](https://github.com/huggingface/tokenizers) | 11,050 | Rust | Classic | 💥 Fast State-of-the-Art Tokenizers optimized for Research and Production |
| [Companion-Inc/feynman](https://github.com/Companion-Inc/feynman) | 9,724 | TypeScript | Rising | The open source AI research agent. |
| [google/artemis](https://github.com/google/artemis) | 8,558 | Python | Hot | ARTEMIS turns natural-language instructions into reliable Android automation. It aut… |
| [XProger/OpenLara](https://github.com/XProger/OpenLara) | 5,107 | C | Mature | Classic Tomb Raider open-source engine |
| [ansible/molecule](https://github.com/ansible/molecule) | 4,150 | Python | Classic | An ansible-native testing framework for collections, playbooks, and roles with confi… |
| [antonbabenko/pre-commit-terraform](https://github.com/antonbabenko/pre-commit-terraform) | 3,776 | Shell | Classic | pre-commit git hooks to take care of Terraform configurations 🇺🇦 |
| [radixark/miles](https://github.com/radixark/miles) | 2,959 | Python | Hot | Miles is an enterprise-facing reinforcement learning framework for LLM and VLM post-… |
| [google/XNNPACK](https://github.com/google/XNNPACK) | 2,458 | C | Classic | High-efficiency floating-point neural network inference operators for mobile, server… |
| [antonbabenko/terraform-skill](https://github.com/antonbabenko/terraform-skill) | 2,368 | — | Declining | Terraform & OpenTofu Skill for AI Agents - testing, modules, CI/CD, and production p… |
| [cashapp/molecule](https://github.com/cashapp/molecule) | 2,230 | Kotlin | Mature | Build a StateFlow stream using Jetpack Compose |
| [oxigraph/oxigraph](https://github.com/oxigraph/oxigraph) | 1,937 | Rust | Classic | SPARQL graph database |
| [erictli/scratch](https://github.com/erictli/scratch) | 1,579 | TypeScript | Mature | A minimalist, offline-first markdown note-taking app |
| [nickvourd/Supernova](https://github.com/nickvourd/Supernova) | 1,042 | Go | Mature | Shellcode encryptor & obfuscator tool |
| [DTStack/molecule](https://github.com/DTStack/molecule) | 972 | TypeScript | Mature | :rocket: A lightweight Web IDE UI framework. |
| [marlin-codes/Awesome-Hyperbolic-Representation-and-Deep-Learning](https://github.com/marlin-codes/Awesome-Hyperbolic-Representation-and-Deep-Learning) | 615 | — | Mature | Paper list about hyperbolic embedding, hyperbolic models,hyperbolic applications |
| [mizorewww/laya-coreml](https://github.com/mizorewww/laya-coreml) | 577 | Python | Declining | Local Laya typed decisions on Apple Core ML and Neural Engine. Validated ports, ~5 m… |
| [HazyResearch/hyperbolics](https://github.com/HazyResearch/hyperbolics) | 396 | Python | Abandoned | Hyperbolic Embeddings |
| [OpenNMT/Tokenizer](https://github.com/OpenNMT/Tokenizer) | 339 | C++ | Declining | Fast and customizable text tokenization library with BPE and SentencePiece support |
| [AmazonAppDev/react-native-multi-tv-app-sample](https://github.com/AmazonAppDev/react-native-multi-tv-app-sample) | 322 | TypeScript | Mature | 📺🚀 React Native TV app sample for  Android TV, Fire TV (Fire OS and Vega OS), tvOS, … |
| [markburgess/SSTorytime](https://github.com/markburgess/SSTorytime) | 252 | Go | Hot | Semantic Spacetime Story graph database library over postgresql (SSTorytime) |
| [inference-gateway/inference-gateway](https://github.com/inference-gateway/inference-gateway) | 209 | Go | Hot | An open-source, cloud-native, high-performance gateway unifying multiple LLM provide… |
| [runtime-org/runtime](https://github.com/runtime-org/runtime) | 204 | TypeScript | Declining | Deterministic skills-based browser agent |
| [supernova-ws/SuperNova](https://github.com/supernova-ws/SuperNova) | 186 | PHP | Declining | oGame-like browser sci-fi space strategy |
| [koaning/mktestdocs](https://github.com/koaning/mktestdocs) | 161 | Python | Declining | Run pytest against markdown files/docstrings. |
| [gura105/operational-ontology](https://github.com/gura105/operational-ontology) | 145 | TypeScript | Rising | A minimal, readable reference implementation of the Operational Ontology pattern. Pa… |
| [antonbabenko/awesome-terraform-compliance](https://github.com/antonbabenko/awesome-terraform-compliance) | 145 | — | Declining | Awesome Terraform Compliance - tools, frameworks, and resources for implementing com… |
| [CertifaiAI/classifai](https://github.com/CertifaiAI/classifai) | 128 | Java | Abandoned | :fire: One of the most comprehensive open-source data annotation platform. |
| [jsme-editor/jsme-editor.github.io](https://github.com/jsme-editor/jsme-editor.github.io) | 111 | HTML | Abandoned | — |
| [dspinellis/tokenizer](https://github.com/dspinellis/tokenizer) | 67 | C++ | Abandoned | Convert source code into numerical tokens |
| _…and 16 more_ | | | | |

## Cooling off

Deceleration, not decline. These averaged ≥1★/day across the 102-day long window but are now running below 40% of that rate. Most are still gaining — just far more slowly than they were, which is usually the tail of a launch spike rather than a problem.

| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |
|---|---|---|---|---|---|
| [JohnMwendwa/free-ai-resources](https://github.com/JohnMwendwa/free-ai-resources) | 1.2 | -8.3 | **-682%** of prior pace | 1.3y ago | Abandoned |
| [meta-llama/prompt-ops](https://github.com/meta-llama/prompt-ops) | 2.1 | -3.3 | **-155%** of prior pace | 5mo ago | Declining |
| [axios/axios](https://github.com/axios/axios) | 1.3 | -1.1 | **-88%** of prior pace | 5d ago | Classic |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 3.2 | -1.7 | **-53%** of prior pace | 6mo ago | Declining |
| [sentient-agi/ROMA](https://github.com/sentient-agi/ROMA) | 1.1 | -0.1 | **-13%** of prior pace | 7mo ago | Declining |
| [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | 1.2 | -0.1 | **-12%** of prior pace | 2mo ago | Declining |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | 1.6 | -0.1 | **-9%** of prior pace | 2mo ago | Declining |
| [iternal-technologies-partners/blockify-agentic-data-optimization](https://github.com/iternal-technologies-partners/blockify-agentic-data-optimization) | 1.0 | 0.0 | **0%** of prior pace | 5mo ago | Declining |
| [Kuberwastaken/claurst](https://github.com/Kuberwastaken/claurst) | 5.0 | 0.0 | **0%** of prior pace | 19d ago | Hot |
| [Avaiga/taipy](https://github.com/Avaiga/taipy) | 1.9 | 0.0 | **0%** of prior pace | 1mo ago | Mature |
| [Suvink/cut-it-out](https://github.com/Suvink/cut-it-out) | 2.4 | 0.1 | **6%** of prior pace | 9mo ago | Declining |
| [ValueCell-ai/valuecell](https://github.com/ValueCell-ai/valuecell) | 2.1 | 0.1 | **7%** of prior pace | 6mo ago | Declining |
| [openai/openai-cs-agents-demo](https://github.com/openai/openai-cs-agents-demo) | 1.7 | 0.1 | **8%** of prior pace | 9mo ago | Declining |
| [BishopFox/cloudfox](https://github.com/BishopFox/cloudfox) | 1.5 | 0.1 | **9%** of prior pace | 1mo ago | Mature |
| [OpenDCAI/DataFlow](https://github.com/OpenDCAI/DataFlow) | 33.4 | 3.4 | **10%** of prior pace | 1d ago | Mature |

## Graph analysis — where the movement clusters

**Community clustering.** The top 40 risers span **16 of the graph's 35 communities** — the more concentrated they are, the more this looks like one trend rather than broad drift.

- **Community 4** (12): `affaan-m/ECC`, `stablyai/orca`, `DietrichGebert/ponytail`, `ayghri/i-have-adhd`, `addyosmani/agent-skills`, `Graphify-Labs/graphify`, `diegosouzapw/OmniRoute`, `deeplethe/utopia`, `cathrynlavery/diagram-design`, `msitarzewski/agency-agents`, `JuliusBrussee/caveman`, `awesome-selfhosted/awesome-selfhosted`
- **Community 11** (6): `obra/superpowers`, `Human-Agent-Society/reef`, `NousResearch/hermes-agent`, `heygen-com/hyperframes`, `calesthio/OpenMontage`, `usestrix/strix`
- **Community 5** (4): `earendil-works/pi`, `trycua/cua`, `nextlevelbuilder/ui-ux-pro-max-skill`, `herdrdev/herdr`
- **Community 28** (3): `deepseek-ai/deepseek-harness`, `sindresorhus/awesome`, `public-apis/public-apis`
- **Community 10** (2): `JustVugg/colibri`, `openai/codex`
- **Community 2** (2): `debpalash/VoiceStudio`, `jamiepine/voicebox`
- **Community 20** (2): `firecrawl/firecrawl`, `D4Vinci/Scrapling`

**Direct links between risers** (similarity edges where both endpoints are climbing) — co-movement suggests a shared driver:

- `DietrichGebert/ponytail` ⇄ `affaan-m/ECC` (w=0.435) — topics: ai-agents, claude, claude-code, developer-tools
- `addyosmani/agent-skills` ⇄ `cathrynlavery/diagram-design` (w=0.356) — topics: agent-skills, claude-code, codex; authors: dajiaohuang, mvanhorn
- `DietrichGebert/ponytail` ⇄ `JuliusBrussee/caveman` (w=0.292) — topics: claude, claude-code, llm, prompt-engineering; authors: ousamabenyounes
- `D4Vinci/Scrapling` ⇄ `firecrawl/firecrawl` (w=0.258) — topics: crawler, scraping, web-scraper, web-scraping
- `ayghri/i-have-adhd` ⇄ `affaan-m/ECC` (w=0.167) — topics: developer-tools, productivity
- `jamiepine/voicebox` ⇄ `debpalash/VoiceStudio` (w=0.167) — topics: ai, voice-ai, cuda, mlx
- `public-apis/public-apis` ⇄ `sindresorhus/awesome` (w=0.125) — topics: resources, lists
- `cloudflare/security-audit-skill` ⇄ `msitarzewski/agency-agents` (w=0.080) — authors: CooperSheroy

**What the risers are written in** — language mix of the top 40 movers:

- **Python** — 12
- **TypeScript** — 11
- **JavaScript** — 4
- **Go** — 3
- **Rust** — 3
- **Shell** — 2
- **HTML** — 2
- **—** — 2

## Methodology & caveats

- **Source**: `data/snapshots/*.json` diffed against `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Snapshots available**: 2026-06-11, 2026-07-13, 2026-07-19, 2026-07-20, 2026-07-27, 2026-08-07, 2026-08-11, 2026-08-28, 2026-08-29, 2026-08-31, 2026-09-06, 2026-09-07, 2026-09-12, 2026-09-14, 2026-09-21 (15 vintages). `build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.
- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a fixed cadence — consecutive vintages here range from 1 day to several weeks apart. The recent window therefore does not always use the immediately preceding snapshot: it uses the newest one at least 7 days back, because a 1-day window amplifies noise far more than it reveals movement. Per-day normalization keeps the boards comparable across refreshes either way.
- **Star counts are a popularity signal, not a quality one.** A launch post, a conference talk, or a newsletter mention moves stars without anything changing in the code.
- **Only repos present in both snapshots are diffed.** Newly starred repos appear under *New entrants* with no growth figure; unstarred repos silently drop out.
- **The theme layer is hand-written** against the computed boards and does not refresh itself. Re-curate it when the movers change shape.
- Re-run after a fresh `classified.json` to refresh every board.

<sub>Repos tracked: 2,155 · Window: 2026-09-14 → 2026-09-21 (7d) · Snapshot: 2026-09-21T11:17:33.969Z</sub>
