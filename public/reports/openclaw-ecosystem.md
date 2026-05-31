# OpenClaw Ecosystem — What to Use Now

> Derived from **kaiser-data**'s 1,071 starred repos (snapshot `2026-05-24T19:57:47.245Z`), cross-referenced with the repo-similarity graph (1,071 nodes / 3,486 edges, 23 communities).
>
> Generated 2026-05-31 by `scripts/reports/openclaw_ecosystem.py` (regenerate any time — no API cost).

> **What is OpenClaw?** A personal AI assistant (🦞, formerly *Clawdbot* / *Moltbot*) that runs on any OS/platform. It has spawned a fast-moving ecosystem of runtimes, skills, routers, memory layers, dashboards, and specialized agents — this report maps the parts in your stars and flags what's worth adopting **now**.

## Recommended stack (use now)

Opinionated picks — filtered for **healthy + actively maintained** (high health score, recent pushes). See the risk table below for what to avoid.

| Layer | Pick | ★ | Health | Why |
|---|---|---|---|---|
| Core assistant | [openclaw/openclaw](https://github.com/openclaw/openclaw) | 374,391 | 84 | The OpenClaw assistant itself — your own personal AI, any OS/platform. Everything else extends this. |
| Secure runtime | [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | 29,351 | 70 | Lightweight OpenClaw alternative that runs in containers for security; WhatsApp/Telegram/Slack connectors. |
| Serverless host | [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | 9,898 | 57 | Run OpenClaw on Cloudflare Workers (serverless edge). |
| Skills directory | [openclaw/clawhub](https://github.com/openclaw/clawhub) | 8,747 | 72 | The official skill directory for OpenClaw. |
| LLM router | [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | 6,505 | 76 | Agent-native LLM router for OpenClaw — 41+ models, <1ms routing, on-chain payments. |
| Memory | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | 4,006 | 67 | Fully-local long-term memory (4-tier pipeline); ships as an OpenClaw plugin. |
| Observability | [vivekchand/clawmetry](https://github.com/vivekchand/clawmetry) | 340 | 78 | Real-time observability dashboard — 'see your agent think' (OpenTelemetry). |
| Desktop hub | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 79,649 | 76 | Cross-platform desktop hub for OpenClaw + Claude Code + Codex + Gemini CLI + Hermes. |

**One-liner:** keep `openclaw/openclaw` as the core; run it via **nanoclaw** (security) or **moltworker** (serverless); add **clawhub** skills, **ClawRouter** routing, and **clawmetry** observability. Want a fresh start? **zeroclaw-labs/zeroclaw** is the highest-health alternative you've starred.

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Project | Category | Lang | ★ Stars | Lifecycle | Health | Activity | Last push | Bus factor |
|---|---|---|---|---|---|---|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Core | TypeScript | 374,391 | Hot | 84 | very active | 0d ago | 2 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Alternative agent / OS | Python | 165,496 | Hot | 79 | very active | 0d ago | 2 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Desktop / orchestration | Rust | 79,649 | Hot | 76 | very active | 0d ago | 1 |
| [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | Desktop / orchestration | TypeScript | 46,219 | Mature | 94 | very active | 0d ago | 4 |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | Alternative agent / OS | Python | 43,074 | Hot | 83 | very active | 0d ago | 2 |
| [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | Alternative agent / OS | Rust | 31,557 | Hot | 93 | very active | 0d ago | 4 |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | Skills / directory | — | 31,175 | Hot | 55 | slowing | 2mo ago | 2 |
| [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | Hosting / secure runtime | TypeScript | 29,351 | Hot | 70 | very active | 1d ago | 2 |
| [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | Desktop / orchestration | TypeScript | 26,383 | Hot | 81 | very active | 0d ago | 2 |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Specialized agent | Python | 24,265 | Hot | 78 | very active | 2d ago | 1 |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Hosting / secure runtime | TypeScript | 20,633 | Hot | 73 | very active | 0d ago | 3 |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | Alternative agent / OS | Rust | 17,632 | Hot | 78 | very active | 10d ago | 1 |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | Specialized agent | Python | 12,600 | Hot | 84 | very active | 2d ago | 2 |
| [nearai/ironclaw](https://github.com/nearai/ironclaw) | Alternative agent / OS | Rust | 12,330 | Hot | 80 | very active | 0d ago | 2 |
| [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | Hosting / secure runtime | TypeScript | 9,898 | Hot | 57 | very active | 16d ago | 1 |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | Skills / directory | TypeScript | 8,747 | Hot | 72 | very active | 0d ago | 1 |
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | Specialized agent | Python | 8,112 | Rising | 41 | slowing | 2mo ago | 1 |
| [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | Routing | TypeScript | 6,505 | Hot | 76 | very active | 1d ago | 1 |
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | Specialized agent | Python | 5,382 | Hot | 57 | very active | 2d ago | 1 |
| [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | Memory | TypeScript | 4,006 | Hot | 67 | very active | 0d ago | 1 |
| [abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control) | Desktop / orchestration | TypeScript | 3,984 | Hot | 56 | active | 1mo ago | 1 |
| [crshdn/mission-control](https://github.com/crshdn/mission-control) | Desktop / orchestration | TypeScript | 2,053 | Hot | 83 | very active | 8d ago | 2 |
| [pinchbench/skill](https://github.com/pinchbench/skill) | Observability | Python | 1,195 | Hot | 79 | very active | 2d ago | 1 |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | Memory | TypeScript | 780 | Hot | 56 | very active | 1d ago | 1 |
| [SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws) | Specialized agent | Python | 669 | Hot | 74 | very active | 2d ago | 1 |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | Observability | TypeScript | 615 | Hot | 78 | very active | 2d ago | 1 |
| [hydro13/tandem-browser](https://github.com/hydro13/tandem-browser) | Specialized agent | TypeScript | 553 | Rising | 75 | very active | 1d ago | 1 |
| [rohitg00/awesome-openclaw](https://github.com/rohitg00/awesome-openclaw) | Skills / directory | Python | 510 | Hot | 57 | very active | 1d ago | 1 |
| [vivekchand/clawmetry](https://github.com/vivekchand/clawmetry) | Observability | Python | 340 | Rising | 78 | very active | 0d ago | 1 |

## By category

### Core

_The assistant everything else plugs into._

- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · 374,391★ · TypeScript · Hot · health 84  
  The OpenClaw assistant itself — your own personal AI, any OS/platform. Everything else extends this.  
  <sub>topics: ai, assistant, own-your-data, personal, crustacean, molty, openclaw</sub>

### Alternative agent / OS

_Standalone agents/agent-OSes you'd pick *instead of* OpenClaw._

- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 165,496★ · Python · Hot · health 79  
  'The agent that grows with you' — large, very active alternative.  
  <sub>topics: ai, ai-agent, ai-agents, llm, anthropic, chatgpt, claude, claude-code</sub>
- **[HKUDS/nanobot](https://github.com/HKUDS/nanobot)** · 43,074★ · Python · Hot · health 83  
  Lightweight open-source agent for tools, chats & workflows.  
  <sub>topics: ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex</sub>
- **[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)** · 31,557★ · Rust · Hot · health 93  
  Fast, small, fully-autonomous assistant infra (Rust); the healthiest alternative in your stars.  
  <sub>topics: agent, agentic, ai, openclaw, infra, ml, os, zeroclaw</sub>
- **[RightNow-AI/openfang](https://github.com/RightNow-AI/openfang)** · 17,632★ · Rust · Hot · health 78  
  Open-source 'Agent Operating System' (Rust), MCP-native.  
  <sub>topics: agent-framework, ai-agents, llm, mcp, open-source, openclaw, operating-system, rust</sub>
- **[nearai/ironclaw](https://github.com/nearai/ironclaw)** · 12,330★ · Rust · Hot · health 80  
  Agent-OS focused on privacy, security & extensibility (Rust/WASM, CodeAct).  
  <sub>topics: codeact, openclaw, rlm, rust, wasm</sub>

### Hosting / secure runtime

_Where & how to run it safely — containers, edge, managed GPU._

- **[nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw)** · 29,351★ · TypeScript · Hot · health 70  
  Lightweight OpenClaw alternative that runs in containers for security; WhatsApp/Telegram/Slack connectors.  
  <sub>topics: ai-agents, ai-assistant, claude-code, claude-skills, openclaw</sub>
- **[NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)** · 20,633★ · TypeScript · Hot · health 73  
  Run OpenClaw more securely inside NVIDIA OpenShell with managed inference.  
  <sub>topics: —</sub>
- **[cloudflare/moltworker](https://github.com/cloudflare/moltworker)** · 9,898★ · TypeScript · Hot · health 57  
  Run OpenClaw on Cloudflare Workers (serverless edge).  
  <sub>topics: ai-agents, cloudflare-workers</sub>

### Skills / directory

_Extend capabilities; find what others have built._

- **[hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)** · 31,175★ · — · Hot · health 55  
  Community collection of OpenClaw use cases (large, but check freshness).  
  <sub>topics: awesome-list, clawdbot, moltbot, openclaw, openclaw-plugin, openclaw-setup, openclaw-skills, usecase</sub>
- **[openclaw/clawhub](https://github.com/openclaw/clawhub)** · 8,747★ · TypeScript · Hot · health 72  
  The official skill directory for OpenClaw.  
  <sub>topics: directory, skill</sub>
- **[rohitg00/awesome-openclaw](https://github.com/rohitg00/awesome-openclaw)** · 510★ · Python · Hot · health 57  
  Curated awesome-list for the OpenClaw ecosystem.  
  <sub>topics: —</sub>

### Routing

_Send each request to the right/cheapest model._

- **[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)** · 6,505★ · TypeScript · Hot · health 76  
  Agent-native LLM router for OpenClaw — 41+ models, <1ms routing, on-chain payments.  
  <sub>topics: ai, ai-agents, anthropic, cost-optimization, deepseek, gemini, llm, llm-router</sub>

### Memory

_Long-term recall across sessions (see also the Memory report)._

- **[Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory)** · 4,006★ · TypeScript · Hot · health 67  
  Fully-local long-term memory (4-tier pipeline); ships as an OpenClaw plugin.  
  <sub>topics: agent, llm, memory, openclaw-plugin, ai-agent, embedding, local-first, long-term-memory</sub>
- **[supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory)** · 780★ · TypeScript · Hot · health 56  
  Long-term memory & recall packaged specifically for OpenClaw agents.  
  <sub>topics: ai-memory, clawd, clawdbot, memory, moltbot, openai, openclaw</sub>

### Observability

_See, measure & benchmark what your agent is doing._

- **[pinchbench/skill](https://github.com/pinchbench/skill)** · 1,195★ · Python · Hot · health 79  
  Benchmarks LLMs as OpenClaw coding agents on real tasks.  
  <sub>topics: —</sub>
- **[comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw)** · 615★ · TypeScript · Hot · health 78  
  Official plugin exporting OpenClaw agent traces (cost/tokens/errors) to Opik.  
  <sub>topics: clawdbot, evaluation, moltbot, observability, openclaw, testing</sub>
- **[vivekchand/clawmetry](https://github.com/vivekchand/clawmetry)** · 340★ · Python · Rising · health 78  
  Real-time observability dashboard — 'see your agent think' (OpenTelemetry).  
  <sub>topics: ai-agent, dashboard, monitoring, observability, openclaw, opentelemetry, python, clawmetry</sub>

### Desktop / orchestration

_GUIs and multi-agent control panels._

- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 79,649★ · Rust · Hot · health 76  
  Cross-platform desktop hub for OpenClaw + Claude Code + Codex + Gemini CLI + Hermes.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, typescript, codex</sub>
- **[CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)** · 46,219★ · TypeScript · Mature · health 94  
  AI productivity studio (300+ assistants) with OpenClaw/skills support; highest health here.  
  <sub>topics: claude-code, ai-agent, skills, codex, vibe-coding, openclaw, deepseek, awesome-skills</sub>
- **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** · 26,383★ · TypeScript · Hot · health 81  
  Free local 24/7 cowork app for OpenClaw, Hermes, Claude Code, Codex & more.  
  <sub>topics: ai, ai-agent, gemini, gemini-cli, llm, chat, chatbot, office</sub>
- **[abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control)** · 3,984★ · TypeScript · Hot · health 56  
  Agent-orchestration dashboard for OpenClaw (assign tasks, coordinate agents).  
  <sub>topics: ai-agents, automation, openclaw, orchestration</sub>
- **[crshdn/mission-control](https://github.com/crshdn/mission-control)** · 2,053★ · TypeScript · Hot · health 83  
  Autonomous Product Engine — agents research, build & ship via OpenClaw.  
  <sub>topics: aiagent, automation, openclaw</sub>

### Specialized agent

_Purpose-built agents on top of OpenClaw (research, tutoring, coding, browser…)._

- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 24,265★ · Python · Hot · health 78  
  Agent-native personalized tutoring.  
  <sub>topics: ai-tutor, deepresearch, interactive-learning, large-language-models, multi-agent-systems, rag, ai-agents, clawdbot</sub>
- **[aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)** · 12,600★ · Python · Hot · health 84  
  Autonomous, self-evolving research: chat an idea → get a paper. 🦞  
  <sub>topics: autonomous-research, citation-verification, llm-agents, multi-agent-debate, openclaw, paper-generation, scientific-discovery, self-evolving</sub>
- **[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)** · 8,112★ · Python · Rising · health 41  
  OpenClaw as an AI coworker (coding focus) — but check freshness.  
  <sub>topics: —</sub>
- **[Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL)** · 5,382★ · Python · Hot · health 57  
  Train any OpenClaw agent simply by talking (RL/skill-learning).  
  <sub>topics: async, memory-systems, open-claw, openclaw-skills, rlhf, sglang, skill-learning, slime</sub>
- **[SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws)** · 669★ · Python · Hot · health 74  
  Fast, production-ready Python-native personal assistant inspired by OpenClaw.  
  <sub>topics: agentic-ai, claude, claude-code, memory, python, skills, openclaw</sub>
- **[hydro13/tandem-browser](https://github.com/hydro13/tandem-browser)** · 553★ · TypeScript · Rising · health 75  
  AI-human symbiotic browser with OpenClaw integration.  
  <sub>topics: ai, browser, chromium, electron, human-ai-collaboration, local-first, openclaw, typescript</sub>

## ⚠️ Adopt with caution

Low health and/or not pushed recently — verify before wiring into anything you rely on:

| Project | Health | Lifecycle | Last push | Note |
|---|---|---|---|---|
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | 41 | Rising | 2mo ago | 82d stale; low health |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 55 | Hot | 2mo ago | 61d stale |
| [abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control) | 56 | Hot | 1mo ago | 48d stale |

> Note: `openagen/zeroclaw` (1.9k★, 70d stale) is a *different, older* project than the healthy **`zeroclaw-labs/zeroclaw`** (h93) recommended above — don't confuse them.

## Graph analysis — how they relate

**Community clustering.** These 29 projects span **11 of the graph's 23 communities** — the OpenClaw ecosystem is spread across agent-infra rather than forming one isolated cluster.

- **Community 10** (9): `HKUDS/nanobot`, `NousResearch/hermes-agent`, `rohitg00/awesome-openclaw`, `BlockRunAI/ClawRouter`, `iOfficeAI/AionUi`, `CherryHQ/cherry-studio`, `HKUDS/DeepTutor`, `HKUDS/ClawWork`, `SafeRL-Lab/cheetahclaws`
- **Community 18** (5): `openclaw/openclaw`, `openclaw/clawhub`, `hesamsheikh/awesome-openclaw-usecases`, `supermemoryai/openclaw-supermemory`, `comet-ml/opik-openclaw`
- **Community 14** (3): `nearai/ironclaw`, `RightNow-AI/openfang`, `farion1231/cc-switch`
- **Community 11** (3): `nanocoai/nanoclaw`, `abhi1693/openclaw-mission-control`, `crshdn/mission-control`
- **Community 0** (2): `zeroclaw-labs/zeroclaw`, `Tencent/TencentDB-Agent-Memory`
- **Community 3** (2): `cloudflare/moltworker`, `hydro13/tandem-browser`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' OpenClaw projects in your ecosystem:

- `vivekchand/clawmetry` — PageRank 0.0040
- `hydro13/tandem-browser` — PageRank 0.0039
- `HKUDS/nanobot` — PageRank 0.0023
- `NVIDIA/NemoClaw` — PageRank 0.0021
- `abhi1693/openclaw-mission-control` — PageRank 0.0017
- `CherryHQ/cherry-studio` — PageRank 0.0014
- `comet-ml/opik-openclaw` — PageRank 0.0014
- `RightNow-AI/openfang` — PageRank 0.0014
- `NousResearch/hermes-agent` — PageRank 0.0012
- `BlockRunAI/ClawRouter` — PageRank 0.0011

**Direct links between OpenClaw projects** (top similarity edges where both endpoints are in this report):

- `HKUDS/nanobot` ⇄ `NousResearch/hermes-agent` (w=0.706) — topics: ai, ai-agent, ai-agents, anthropic; authors: Hinotoi-agent
- `openclaw/clawhub` ⇄ `openclaw/openclaw` (w=0.704) — authors: steipete, Takhoffman
- `HKUDS/nanobot` ⇄ `HKUDS/DeepTutor` (w=0.598) — topics: ai-agents
- `abhi1693/openclaw-mission-control` ⇄ `crshdn/mission-control` (w=0.450) — topics: automation, openclaw
- `comet-ml/opik-openclaw` ⇄ `supermemoryai/openclaw-supermemory` (w=0.350) — topics: clawdbot, moltbot, openclaw
- `abhi1693/openclaw-mission-control` ⇄ `nanocoai/nanoclaw` (w=0.336) — topics: ai-agents, openclaw
- `abhi1693/openclaw-mission-control` ⇄ `RightNow-AI/openfang` (w=0.333) — topics: ai-agents, openclaw; authors: dependabot[bot]
- `comet-ml/opik-openclaw` ⇄ `hydro13/tandem-browser` (w=0.327) — topics: openclaw; authors: dependabot[bot]
- `comet-ml/opik-openclaw` ⇄ `abhi1693/openclaw-mission-control` (w=0.286) — topics: openclaw; authors: dependabot[bot]
- `NousResearch/hermes-agent` ⇄ `iOfficeAI/AionUi` (w=0.286) — topics: ai, ai-agent, llm, claude-code
- `comet-ml/opik-openclaw` ⇄ `hesamsheikh/awesome-openclaw-usecases` (w=0.273) — topics: clawdbot, moltbot, openclaw
- `HKUDS/nanobot` ⇄ `BlockRunAI/ClawRouter` (w=0.261) — topics: ai, ai-agents, anthropic, llm
- `HKUDS/nanobot` ⇄ `nanocoai/nanoclaw` (w=0.257) — topics: ai-agents, claude-code, openclaw; authors: Hinotoi-agent
- `abhi1693/openclaw-mission-control` ⇄ `cloudflare/moltworker` (w=0.250) — topics: ai-agents
- `hesamsheikh/awesome-openclaw-usecases` ⇄ `supermemoryai/openclaw-supermemory` (w=0.250) — topics: clawdbot, moltbot, openclaw
- …and 16 more.

## Methodology & caveats

- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: scan for `openclaw` / `clawd*` / `moltbot` across name/description/topics/README, then manual curation. Repos that merely *mention* OpenClaw in passing (general agent harnesses, awesome-lists, unrelated tools) were excluded; memory/MCP-centric repos are covered in their own reports and only the OpenClaw-specific ones appear here.
- **Metrics** (health, lifecycle, bus_factor, days_since_push) are precomputed at snapshot time. **OpenClaw moves extremely fast** — treat all ages/stars as a May-2026 snapshot and re-verify before adopting.
- Re-run after a fresh `classified.json` to refresh.

<sub>Projects covered: 29 · Snapshot: 2026-05-24T19:57:47.245Z</sub>
