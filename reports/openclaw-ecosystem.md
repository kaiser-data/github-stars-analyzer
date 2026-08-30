# OpenClaw Ecosystem — What to Use Now

> Derived from **kaiser-data**'s 1,859 starred repos (snapshot `2026-08-29T23:54:34.573Z`), cross-referenced with the repo-similarity graph (1,859 nodes / 6,070 edges, 37 communities).
>
> Generated 2026-08-30 by `scripts/reports/openclaw_ecosystem.py` (regenerate any time — no API cost).

![Top tools by stars](assets/openclaw-ecosystem-top-tools.svg)

![Tools per category](assets/openclaw-ecosystem-categories.svg)


> **What is OpenClaw?** A personal AI assistant (🦞, formerly *Clawdbot* / *Moltbot*) that runs on any OS/platform. It has spawned a fast-moving ecosystem of runtimes, skills, routers, memory layers, dashboards, and specialized agents — this report maps the parts in your stars and flags what's worth adopting **now**.

## Recommended stack (use now)

Opinionated picks — filtered for **healthy + actively maintained** (high health score, recent pushes). See the risk table below for what to avoid.

| Layer | Pick | ★ | Health | Why |
|---|---|---|---|---|
| Core assistant | [openclaw/openclaw](https://github.com/openclaw/openclaw) | 387,846 | 79 | The OpenClaw assistant itself — your own personal AI, any OS/platform. Everything else extends this. |
| Secure runtime | [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | 30,626 | 80 | Lightweight OpenClaw alternative that runs in containers for security; WhatsApp/Telegram/Slack connectors. |
| Serverless host | [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | 9,957 | 26 | Run OpenClaw on Cloudflare Workers (serverless edge). |
| Skills directory | [openclaw/clawhub](https://github.com/openclaw/clawhub) | 9,359 | 85 | The official skill directory for OpenClaw. |
| LLM router | [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | 6,573 | 78 | Agent-native LLM router for OpenClaw — 41+ models, <1ms routing, on-chain payments. |
| Memory | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | 24,872 | 71 | Fully-local long-term memory (4-tier pipeline); ships as an OpenClaw plugin. |
| Observability | [vivekchand/clawmetry](https://github.com/vivekchand/clawmetry) | 401 | 79 | Real-time observability dashboard — 'see your agent think' (OpenTelemetry). |
| Desktop hub | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 129,761 | 76 | Cross-platform desktop hub for OpenClaw + Claude Code + Codex + Gemini CLI + Hermes. |

**One-liner:** keep `openclaw/openclaw` as the core; run it via **nanoclaw** (security) or **moltworker** (serverless); add **clawhub** skills, **ClawRouter** routing, and **clawmetry** observability. Want a fresh start? **zeroclaw-labs/zeroclaw** is the highest-health alternative you've starred.

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Project | Category | Lang | ★ Stars | Lifecycle | Health | Activity | Last push | Bus factor |
|---|---|---|---|---|---|---|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Core | TypeScript | 387,846 | Hot | 79 | very active | 2d ago | 1 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Alternative agent / OS | Python | 237,338 | Hot | 85 | very active | 2d ago | 3 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Desktop / orchestration | Rust | 129,761 | Hot | 76 | very active | 2d ago | 1 |
| [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | Desktop / orchestration | TypeScript | 51,155 | Mature | 94 | very active | 2d ago | 4 |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | Alternative agent / OS | Python | 47,471 | Hot | 78 | very active | 2d ago | 1 |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Specialized agent | Python | 37,717 | Hot | 78 | very active | 2d ago | 1 |
| [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | Alternative agent / OS | Rust | 32,667 | Hot | 88 | very active | 3d ago | 3 |
| [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | Desktop / orchestration | TypeScript | 32,345 | Hot | 80 | very active | 3d ago | 2 |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | Skills / directory | — | 31,672 | Declining | 22 | slowing | 5mo ago | 0 |
| [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | Hosting / secure runtime | TypeScript | 30,626 | Hot | 80 | very active | 2d ago | 2 |
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | Memory | TypeScript | 24,872 | Rising | 71 | very active | 3d ago | 2 |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Hosting / secure runtime | TypeScript | 22,296 | Hot | 74 | very active | 2d ago | 3 |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | Alternative agent / OS | Rust | 18,139 | Declining | 49 | active | 1mo ago | 0 |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | Specialized agent | Python | 14,263 | Hot | 72 | very active | 11d ago | 1 |
| [nearai/ironclaw](https://github.com/nearai/ironclaw) | Alternative agent / OS | Rust | 12,603 | Hot | 80 | very active | 2d ago | 2 |
| [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | Hosting / secure runtime | TypeScript | 9,957 | Declining | 26 | slowing | 3mo ago | 0 |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | Skills / directory | TypeScript | 9,359 | Hot | 85 | very active | 2d ago | 2 |
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | Specialized agent | Python | 8,525 | Declining | 18 | slowing | 5mo ago | 0 |
| [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | Routing | TypeScript | 6,573 | Hot | 78 | very active | 4d ago | 1 |
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | Specialized agent | Python | 5,657 | Declining | 24 | slowing | 3mo ago | 0 |
| [crshdn/mission-control](https://github.com/crshdn/mission-control) | Desktop / orchestration | TypeScript | 2,135 | Declining | 56 | active | 1mo ago | 1 |
| [pinchbench/skill](https://github.com/pinchbench/skill) | Observability | Python | 1,327 | Declining | 49 | active | 1mo ago | 0 |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | Memory | TypeScript | 798 | Mature | 48 | slowing | 2mo ago | 2 |
| [SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws) | Specialized agent | Python | 768 | Hot | 76 | very active | 3d ago | 1 |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | Observability | TypeScript | 725 | Declining | 59 | active | 2d ago | 1 |
| [hydro13/tandem-browser](https://github.com/hydro13/tandem-browser) | Specialized agent | TypeScript | 594 | Rising | 70 | very active | 13d ago | 1 |
| [rohitg00/awesome-openclaw](https://github.com/rohitg00/awesome-openclaw) | Skills / directory | Python | 561 | Rising | 40 | slowing | 2mo ago | 1 |
| [vivekchand/clawmetry](https://github.com/vivekchand/clawmetry) | Observability | Python | 401 | Rising | 79 | very active | 2d ago | 1 |

## By category

### Core

_The assistant everything else plugs into._

- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · 387,846★ · TypeScript · Hot · health 79  
  The OpenClaw assistant itself — your own personal AI, any OS/platform. Everything else extends this.  
  <sub>topics: ai, assistant, own-your-data, personal, crustacean, molty, openclaw</sub>

### Alternative agent / OS

_Standalone agents/agent-OSes you'd pick *instead of* OpenClaw._

- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 237,338★ · Python · Hot · health 85  
  'The agent that grows with you' — large, very active alternative.  
  <sub>topics: ai, ai-agent, ai-agents, llm, anthropic, chatgpt, claude, claude-code</sub>
- **[HKUDS/nanobot](https://github.com/HKUDS/nanobot)** · 47,471★ · Python · Hot · health 78  
  Lightweight open-source agent for tools, chats & workflows.  
  <sub>topics: ai-agent, ai-agents, openclaw, agent-framework, chatbot, chatops, discord-bot, llm-agents</sub>
- **[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)** · 32,667★ · Rust · Hot · health 88  
  Fast, small, fully-autonomous assistant infra (Rust); the healthiest alternative in your stars.  
  <sub>topics: agent, agentic, ai, openclaw, infra, ml, os, zeroclaw</sub>
- **[RightNow-AI/openfang](https://github.com/RightNow-AI/openfang)** · 18,139★ · Rust · Declining · health 49  
  Open-source 'Agent Operating System' (Rust), MCP-native.  
  <sub>topics: agent-framework, ai-agents, llm, mcp, open-source, openclaw, operating-system, rust</sub>
- **[nearai/ironclaw](https://github.com/nearai/ironclaw)** · 12,603★ · Rust · Hot · health 80  
  Agent-OS focused on privacy, security & extensibility (Rust/WASM, CodeAct).  
  <sub>topics: codeact, openclaw, rlm, rust, wasm</sub>

### Hosting / secure runtime

_Where & how to run it safely — containers, edge, managed GPU._

- **[nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw)** · 30,626★ · TypeScript · Hot · health 80  
  Lightweight OpenClaw alternative that runs in containers for security; WhatsApp/Telegram/Slack connectors.  
  <sub>topics: ai-agents, ai-assistant, claude-code, claude-skills, openclaw</sub>
- **[NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)** · 22,296★ · TypeScript · Hot · health 74  
  Run OpenClaw more securely inside NVIDIA OpenShell with managed inference.  
  <sub>topics: ai-agents, nvidia, openclaw, openshell, sandboxing, typescript, hermes</sub>
- **[cloudflare/moltworker](https://github.com/cloudflare/moltworker)** · 9,957★ · TypeScript · Declining · health 26  
  Run OpenClaw on Cloudflare Workers (serverless edge).  
  <sub>topics: ai-agents, cloudflare-workers</sub>

### Skills / directory

_Extend capabilities; find what others have built._

- **[hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)** · 31,672★ · — · Declining · health 22  
  Community collection of OpenClaw use cases (large, but check freshness).  
  <sub>topics: awesome-list, clawdbot, moltbot, openclaw, openclaw-plugin, openclaw-setup, openclaw-skills, usecase</sub>
- **[openclaw/clawhub](https://github.com/openclaw/clawhub)** · 9,359★ · TypeScript · Hot · health 85  
  The official skill directory for OpenClaw.  
  <sub>topics: directory, skill</sub>
- **[rohitg00/awesome-openclaw](https://github.com/rohitg00/awesome-openclaw)** · 561★ · Python · Rising · health 40  
  Curated awesome-list for the OpenClaw ecosystem.  
  <sub>topics: —</sub>

### Routing

_Send each request to the right/cheapest model._

- **[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)** · 6,573★ · TypeScript · Hot · health 78  
  Agent-native LLM router for OpenClaw — 41+ models, <1ms routing, on-chain payments.  
  <sub>topics: ai, ai-agents, anthropic, cost-optimization, deepseek, gemini, llm, llm-router</sub>

### Memory

_Long-term recall across sessions (see also the Memory report)._

- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 24,872★ · TypeScript · Rising · health 71  
  Fully-local long-term memory (4-tier pipeline); ships as an OpenClaw plugin.  
  <sub>topics: agent, llm, memory, openclaw-plugin, ai-agent, embedding, local-first, long-term-memory</sub>
- **[supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory)** · 798★ · TypeScript · Mature · health 48  
  Long-term memory & recall packaged specifically for OpenClaw agents.  
  <sub>topics: ai-memory, clawd, clawdbot, memory, moltbot, openai, openclaw</sub>

### Observability

_See, measure & benchmark what your agent is doing._

- **[pinchbench/skill](https://github.com/pinchbench/skill)** · 1,327★ · Python · Declining · health 49  
  Benchmarks LLMs as OpenClaw coding agents on real tasks.  
  <sub>topics: —</sub>
- **[comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw)** · 725★ · TypeScript · Declining · health 59  
  Official plugin exporting OpenClaw agent traces (cost/tokens/errors) to Opik.  
  <sub>topics: clawdbot, evaluation, moltbot, observability, openclaw, testing, ai-agents, llm-observability</sub>
- **[vivekchand/clawmetry](https://github.com/vivekchand/clawmetry)** · 401★ · Python · Rising · health 79  
  Real-time observability dashboard — 'see your agent think' (OpenTelemetry).  
  <sub>topics: ai-agent, monitoring, observability, openclaw, opentelemetry, python, clawmetry, agent-monitoring</sub>

### Desktop / orchestration

_GUIs and multi-agent control panels._

- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 129,761★ · Rust · Hot · health 76  
  Cross-platform desktop hub for OpenClaw + Claude Code + Codex + Gemini CLI + Hermes.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, codex, mcp</sub>
- **[CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)** · 51,155★ · TypeScript · Mature · health 94  
  AI productivity studio (300+ assistants) with OpenClaw/skills support; highest health here.  
  <sub>topics: claude-code, ai-agent, skills, codex, vibe-coding, deepseek, hermes-agent, agent-skills</sub>
- **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** · 32,345★ · TypeScript · Hot · health 80  
  Free local 24/7 cowork app for OpenClaw, Hermes, Claude Code, Codex & more.  
  <sub>topics: ai, ai-agent, gemini, gemini-cli, llm, chat, chatbot, office</sub>
- **[crshdn/mission-control](https://github.com/crshdn/mission-control)** · 2,135★ · TypeScript · Declining · health 56  
  Autonomous Product Engine — agents research, build & ship via OpenClaw.  
  <sub>topics: aiagent, automation, openclaw</sub>

### Specialized agent

_Purpose-built agents on top of OpenClaw (research, tutoring, coding, browser…)._

- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 37,717★ · Python · Hot · health 78  
  Agent-native personalized tutoring.  
  <sub>topics: ai-tutor, deepresearch, interactive-learning, large-language-models, multi-agent-systems, rag, ai-agents, clawdbot</sub>
- **[aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)** · 14,263★ · Python · Hot · health 72  
  Autonomous, self-evolving research: chat an idea → get a paper. 🦞  
  <sub>topics: autonomous-research, citation-verification, llm-agents, multi-agent-debate, openclaw, paper-generation, scientific-discovery, self-evolving</sub>
- **[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)** · 8,525★ · Python · Declining · health 18  
  OpenClaw as an AI coworker (coding focus) — but check freshness.  
  <sub>topics: —</sub>
- **[Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL)** · 5,657★ · Python · Declining · health 24  
  Train any OpenClaw agent simply by talking (RL/skill-learning).  
  <sub>topics: async, memory-systems, open-claw, openclaw-skills, rlhf, sglang, skill-learning, slime</sub>
- **[SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws)** · 768★ · Python · Hot · health 76  
  Fast, production-ready Python-native personal assistant inspired by OpenClaw.  
  <sub>topics: agentic-ai, claude, claude-code, memory, python, skills, openclaw</sub>
- **[hydro13/tandem-browser](https://github.com/hydro13/tandem-browser)** · 594★ · TypeScript · Rising · health 70  
  AI-human symbiotic browser with OpenClaw integration.  
  <sub>topics: ai, browser, chromium, electron, human-ai-collaboration, local-first, openclaw, typescript</sub>

## ⚠️ Adopt with caution

Low health and/or not pushed recently — verify before wiring into anything you rely on:

| Project | Health | Lifecycle | Last push | Note |
|---|---|---|---|---|
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | 18 | Declining | 5mo ago | 179d stale; low health; declining |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 22 | Declining | 5mo ago | 158d stale; low health; declining |
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | 24 | Declining | 3mo ago | 99d stale; low health; declining |
| [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | 26 | Declining | 3mo ago | 113d stale; low health; declining |
| [rohitg00/awesome-openclaw](https://github.com/rohitg00/awesome-openclaw) | 40 | Rising | 2mo ago | 79d stale; low health |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | 48 | Mature | 2mo ago | 70d stale; low health |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | 49 | Declining | 1mo ago | 59d stale; low health; declining |
| [pinchbench/skill](https://github.com/pinchbench/skill) | 49 | Declining | 1mo ago | 59d stale; low health; declining |
| [crshdn/mission-control](https://github.com/crshdn/mission-control) | 56 | Declining | 1mo ago | 54d stale; declining |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | 59 | Declining | 2d ago | declining |

> Note: `openagen/zeroclaw` (1.9k★, 70d stale) is a *different, older* project than the healthy **`zeroclaw-labs/zeroclaw`** (h93) recommended above — don't confuse them.

## Graph analysis — how they relate

**Community clustering.** These 28 projects span **14 of the graph's 37 communities** — the OpenClaw ecosystem is spread across agent-infra rather than forming one isolated cluster.

- **Community 19** (4): `zeroclaw-labs/zeroclaw`, `NousResearch/hermes-agent`, `BlockRunAI/ClawRouter`, `aiming-lab/AutoResearchClaw`
- **Community 9** (4): `nanocoai/nanoclaw`, `vivekchand/clawmetry`, `farion1231/cc-switch`, `iOfficeAI/AionUi`
- **Community 14** (4): `hesamsheikh/awesome-openclaw-usecases`, `supermemoryai/openclaw-supermemory`, `comet-ml/opik-openclaw`, `crshdn/mission-control`
- **Community 15** (3): `HKUDS/nanobot`, `HKUDS/DeepTutor`, `HKUDS/ClawWork`
- **Community 24** (2): `openclaw/openclaw`, `openclaw/clawhub`
- **Community 6** (2): `RightNow-AI/openfang`, `NVIDIA/NemoClaw`
- **Community 12** (2): `rohitg00/awesome-openclaw`, `CherryHQ/cherry-studio`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' OpenClaw projects in your ecosystem:

- `hydro13/tandem-browser` — PageRank 0.0018
- `vivekchand/clawmetry` — PageRank 0.0011
- `supermemoryai/openclaw-supermemory` — PageRank 0.0008
- `cloudflare/moltworker` — PageRank 0.0008
- `NousResearch/hermes-agent` — PageRank 0.0008
- `CherryHQ/cherry-studio` — PageRank 0.0007
- `openclaw/openclaw` — PageRank 0.0007
- `RightNow-AI/openfang` — PageRank 0.0007
- `HKUDS/nanobot` — PageRank 0.0006
- `nanocoai/nanoclaw` — PageRank 0.0005

**Direct links between OpenClaw projects** (top similarity edges where both endpoints are in this report):

- `openclaw/clawhub` ⇄ `openclaw/openclaw` (w=0.858) — authors: Patrick-Erichsen, vincentkoc, vyctorbrzezowski
- `HKUDS/nanobot` ⇄ `HKUDS/DeepTutor` (w=0.586) — topics: ai-agents
- `comet-ml/opik-openclaw` ⇄ `supermemoryai/openclaw-supermemory` (w=0.281) — topics: clawdbot, moltbot, openclaw
- `hesamsheikh/awesome-openclaw-usecases` ⇄ `supermemoryai/openclaw-supermemory` (w=0.250) — topics: clawdbot, moltbot, openclaw
- `hydro13/tandem-browser` ⇄ `iOfficeAI/AionUi` (w=0.235) — topics: ai, openclaw, claude-code, codex
- `RightNow-AI/openfang` ⇄ `nearai/ironclaw` (w=0.232) — topics: openclaw, rust
- `NousResearch/hermes-agent` ⇄ `iOfficeAI/AionUi` (w=0.222) — topics: ai, ai-agent, llm, claude-code
- `farion1231/cc-switch` ⇄ `RightNow-AI/openfang` (w=0.217) — topics: open-source, rust, mcp, openclaw
- `comet-ml/opik-openclaw` ⇄ `nanocoai/nanoclaw` (w=0.217) — topics: openclaw, ai-agents
- `comet-ml/opik-openclaw` ⇄ `hesamsheikh/awesome-openclaw-usecases` (w=0.214) — topics: clawdbot, moltbot, openclaw
- `iOfficeAI/AionUi` ⇄ `CherryHQ/cherry-studio` (w=0.210) — topics: ai-agent, claude-code, codex, skills
- `crshdn/mission-control` ⇄ `nanocoai/nanoclaw` (w=0.193) — topics: openclaw
- `farion1231/cc-switch` ⇄ `iOfficeAI/AionUi` (w=0.176) — topics: claude-code, codex, opencode, skills
- `hydro13/tandem-browser` ⇄ `openclaw/clawhub` (w=0.175) — authors: dependabot[bot]
- `NVIDIA/NemoClaw` ⇄ `crshdn/mission-control` (w=0.161) — topics: openclaw
- …and 1 more.

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: scan for `openclaw` / `clawd*` / `moltbot` across name/description/topics/README, then manual curation. Repos that merely *mention* OpenClaw in passing (general agent harnesses, awesome-lists, unrelated tools) were excluded; memory/MCP-centric repos are covered in their own reports and only the OpenClaw-specific ones appear here.
- **Metrics** (health, lifecycle, bus_factor, days_since_push) are precomputed at snapshot time. **OpenClaw moves extremely fast** — treat all ages/stars as a May-2026 snapshot and re-verify before adopting.
- Re-run after a fresh `classified.json` to refresh.

### Retired from the scored set

Archived upstream, so they no longer appear in this report's tables — `sample.mjs` excludes archived repos. Metrics are frozen at the date shown and are not refreshed.

| Project | Category | Why it left | Metrics as of |
|---|---|---|---|
| [`abhi1693/openclaw-mission-control`](https://github.com/abhi1693/openclaw-mission-control) | Desktop / orchestration | Archived upstream; last in the dataset 2026-07-27. Agent-orchestration dashboard for OpenClaw (assign tasks, coordinate agents). | 2026-07-27 |

<sub>Projects covered: 28 · Snapshot: 2026-08-29T23:54:34.573Z</sub>
