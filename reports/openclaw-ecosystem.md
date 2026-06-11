# OpenClaw Ecosystem — What to Use Now

> Derived from **kaiser-data**'s 1,243 starred repos (snapshot `2026-06-11T21:58:33.384Z`), cross-referenced with the repo-similarity graph (1,243 nodes / 4,017 edges, 31 communities).
>
> Generated 2026-06-11 by `scripts/reports/openclaw_ecosystem.py` (regenerate any time — no API cost).

> **What is OpenClaw?** A personal AI assistant (🦞, formerly *Clawdbot* / *Moltbot*) that runs on any OS/platform. It has spawned a fast-moving ecosystem of runtimes, skills, routers, memory layers, dashboards, and specialized agents — this report maps the parts in your stars and flags what's worth adopting **now**.

## Recommended stack (use now)

Opinionated picks — filtered for **healthy + actively maintained** (high health score, recent pushes). See the risk table below for what to avoid.

| Layer | Pick | ★ | Health | Why |
|---|---|---|---|---|
| Core assistant | [openclaw/openclaw](https://github.com/openclaw/openclaw) | 378,215 | 84 | The OpenClaw assistant itself — your own personal AI, any OS/platform. Everything else extends this. |
| Secure runtime | [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | 29,809 | 65 | Lightweight OpenClaw alternative that runs in containers for security; WhatsApp/Telegram/Slack connectors. |
| Serverless host | [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | 9,909 | 56 | Run OpenClaw on Cloudflare Workers (serverless edge). |
| Skills directory | [openclaw/clawhub](https://github.com/openclaw/clawhub) | 8,928 | 79 | The official skill directory for OpenClaw. |
| LLM router | [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | 6,561 | 77 | Agent-native LLM router for OpenClaw — 41+ models, <1ms routing, on-chain payments. |
| Observability | [vivekchand/clawmetry](https://github.com/vivekchand/clawmetry) | 372 | 78 | Real-time observability dashboard — 'see your agent think' (OpenTelemetry). |
| Desktop hub | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 98,479 | 77 | Cross-platform desktop hub for OpenClaw + Claude Code + Codex + Gemini CLI + Hermes. |

**One-liner:** keep `openclaw/openclaw` as the core; run it via **nanoclaw** (security) or **moltworker** (serverless); add **clawhub** skills, **ClawRouter** routing, and **clawmetry** observability. Want a fresh start? **zeroclaw-labs/zeroclaw** is the highest-health alternative you've starred.

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Project | Category | Lang | ★ Stars | Lifecycle | Health | Activity | Last push | Bus factor |
|---|---|---|---|---|---|---|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Core | TypeScript | 378,215 | Hot | 84 | very active | 0d ago | 2 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Alternative agent / OS | Python | 190,933 | Hot | 79 | very active | 0d ago | 2 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Desktop / orchestration | Rust | 98,479 | Hot | 77 | very active | 0d ago | 1 |
| [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | Desktop / orchestration | TypeScript | 47,220 | Mature | 84 | very active | 0d ago | 2 |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | Alternative agent / OS | Python | 44,068 | Hot | 83 | very active | 0d ago | 2 |
| [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | Alternative agent / OS | Rust | 31,881 | Hot | 84 | very active | 0d ago | 2 |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | Skills / directory | — | 31,338 | Rising | 47 | slowing | 2mo ago | 2 |
| [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | Hosting / secure runtime | TypeScript | 29,809 | Hot | 65 | very active | 0d ago | 1 |
| [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | Desktop / orchestration | TypeScript | 28,071 | Hot | 81 | very active | 0d ago | 2 |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Specialized agent | Python | 24,708 | Hot | 79 | very active | 0d ago | 1 |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Hosting / secure runtime | TypeScript | 21,132 | Hot | 69 | very active | 0d ago | 2 |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | Alternative agent / OS | Rust | 17,809 | Hot | 77 | very active | 29d ago | 1 |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | Specialized agent | Python | 13,360 | Hot | 83 | very active | 8d ago | 2 |
| [nearai/ironclaw](https://github.com/nearai/ironclaw) | Alternative agent / OS | Rust | 12,442 | Hot | 80 | very active | 0d ago | 2 |
| [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | Hosting / secure runtime | TypeScript | 9,909 | Hot | 56 | active | 1mo ago | 1 |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | Skills / directory | TypeScript | 8,928 | Hot | 79 | very active | 0d ago | 1 |
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | Specialized agent | Python | 8,202 | Declining | 25 | slowing | 3mo ago | 0 |
| [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | Routing | TypeScript | 6,561 | Hot | 77 | very active | 0d ago | 1 |
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | Specialized agent | Python | 5,486 | Hot | 56 | very active | 20d ago | 1 |
| [abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control) | Desktop / orchestration | TypeScript | 4,041 | Rising | 50 | slowing | 2mo ago | 2 |
| [crshdn/mission-control](https://github.com/crshdn/mission-control) | Desktop / orchestration | TypeScript | 2,076 | Hot | 80 | very active | 26d ago | 2 |
| [pinchbench/skill](https://github.com/pinchbench/skill) | Observability | Python | 1,227 | Hot | 78 | very active | 9d ago | 1 |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | Memory | TypeScript | 791 | Hot | 61 | very active | 2d ago | 2 |
| [SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws) | Specialized agent | Python | 721 | Hot | 75 | very active | 5d ago | 1 |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | Observability | TypeScript | 620 | Hot | 72 | very active | 4d ago | 1 |
| [hydro13/tandem-browser](https://github.com/hydro13/tandem-browser) | Specialized agent | TypeScript | 554 | Rising | 74 | very active | 13d ago | 1 |
| [rohitg00/awesome-openclaw](https://github.com/rohitg00/awesome-openclaw) | Skills / directory | Python | 518 | Hot | 57 | very active | 1d ago | 1 |
| [vivekchand/clawmetry](https://github.com/vivekchand/clawmetry) | Observability | Python | 372 | Hot | 78 | very active | 0d ago | 1 |

## By category

### Core

_The assistant everything else plugs into._

- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · 378,215★ · TypeScript · Hot · health 84  
  The OpenClaw assistant itself — your own personal AI, any OS/platform. Everything else extends this.  
  <sub>topics: ai, assistant, own-your-data, personal, crustacean, molty, openclaw</sub>

### Alternative agent / OS

_Standalone agents/agent-OSes you'd pick *instead of* OpenClaw._

- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 190,933★ · Python · Hot · health 79  
  'The agent that grows with you' — large, very active alternative.  
  <sub>topics: ai, ai-agent, ai-agents, llm, anthropic, chatgpt, claude, claude-code</sub>
- **[HKUDS/nanobot](https://github.com/HKUDS/nanobot)** · 44,068★ · Python · Hot · health 83  
  Lightweight open-source agent for tools, chats & workflows.  
  <sub>topics: ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex</sub>
- **[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)** · 31,881★ · Rust · Hot · health 84  
  Fast, small, fully-autonomous assistant infra (Rust); the healthiest alternative in your stars.  
  <sub>topics: agent, agentic, ai, openclaw, infra, ml, os, zeroclaw</sub>
- **[RightNow-AI/openfang](https://github.com/RightNow-AI/openfang)** · 17,809★ · Rust · Hot · health 77  
  Open-source 'Agent Operating System' (Rust), MCP-native.  
  <sub>topics: agent-framework, ai-agents, llm, mcp, open-source, openclaw, operating-system, rust</sub>
- **[nearai/ironclaw](https://github.com/nearai/ironclaw)** · 12,442★ · Rust · Hot · health 80  
  Agent-OS focused on privacy, security & extensibility (Rust/WASM, CodeAct).  
  <sub>topics: codeact, openclaw, rlm, rust, wasm</sub>

### Hosting / secure runtime

_Where & how to run it safely — containers, edge, managed GPU._

- **[nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw)** · 29,809★ · TypeScript · Hot · health 65  
  Lightweight OpenClaw alternative that runs in containers for security; WhatsApp/Telegram/Slack connectors.  
  <sub>topics: ai-agents, ai-assistant, claude-code, claude-skills, openclaw</sub>
- **[NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)** · 21,132★ · TypeScript · Hot · health 69  
  Run OpenClaw more securely inside NVIDIA OpenShell with managed inference.  
  <sub>topics: ai-agents, nvidia, openclaw, openshell, sandboxing, typescript</sub>
- **[cloudflare/moltworker](https://github.com/cloudflare/moltworker)** · 9,909★ · TypeScript · Hot · health 56  
  Run OpenClaw on Cloudflare Workers (serverless edge).  
  <sub>topics: ai-agents, cloudflare-workers</sub>

### Skills / directory

_Extend capabilities; find what others have built._

- **[hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)** · 31,338★ · — · Rising · health 47  
  Community collection of OpenClaw use cases (large, but check freshness).  
  <sub>topics: awesome-list, clawdbot, moltbot, openclaw, openclaw-plugin, openclaw-setup, openclaw-skills, usecase</sub>
- **[openclaw/clawhub](https://github.com/openclaw/clawhub)** · 8,928★ · TypeScript · Hot · health 79  
  The official skill directory for OpenClaw.  
  <sub>topics: directory, skill</sub>
- **[rohitg00/awesome-openclaw](https://github.com/rohitg00/awesome-openclaw)** · 518★ · Python · Hot · health 57  
  Curated awesome-list for the OpenClaw ecosystem.  
  <sub>topics: —</sub>

### Routing

_Send each request to the right/cheapest model._

- **[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)** · 6,561★ · TypeScript · Hot · health 77  
  Agent-native LLM router for OpenClaw — 41+ models, <1ms routing, on-chain payments.  
  <sub>topics: ai, ai-agents, anthropic, cost-optimization, deepseek, gemini, llm, llm-router</sub>

### Memory

_Long-term recall across sessions (see also the Memory report)._

- **[supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory)** · 791★ · TypeScript · Hot · health 61  
  Long-term memory & recall packaged specifically for OpenClaw agents.  
  <sub>topics: ai-memory, clawd, clawdbot, memory, moltbot, openai, openclaw</sub>

### Observability

_See, measure & benchmark what your agent is doing._

- **[pinchbench/skill](https://github.com/pinchbench/skill)** · 1,227★ · Python · Hot · health 78  
  Benchmarks LLMs as OpenClaw coding agents on real tasks.  
  <sub>topics: —</sub>
- **[comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw)** · 620★ · TypeScript · Hot · health 72  
  Official plugin exporting OpenClaw agent traces (cost/tokens/errors) to Opik.  
  <sub>topics: clawdbot, evaluation, moltbot, observability, openclaw, testing</sub>
- **[vivekchand/clawmetry](https://github.com/vivekchand/clawmetry)** · 372★ · Python · Hot · health 78  
  Real-time observability dashboard — 'see your agent think' (OpenTelemetry).  
  <sub>topics: ai-agent, dashboard, monitoring, observability, openclaw, opentelemetry, python, clawmetry</sub>

### Desktop / orchestration

_GUIs and multi-agent control panels._

- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 98,479★ · Rust · Hot · health 77  
  Cross-platform desktop hub for OpenClaw + Claude Code + Codex + Gemini CLI + Hermes.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, typescript, codex</sub>
- **[CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)** · 47,220★ · TypeScript · Mature · health 84  
  AI productivity studio (300+ assistants) with OpenClaw/skills support; highest health here.  
  <sub>topics: claude-code, ai-agent, skills, codex, vibe-coding, openclaw, deepseek, awesome-skills</sub>
- **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** · 28,071★ · TypeScript · Hot · health 81  
  Free local 24/7 cowork app for OpenClaw, Hermes, Claude Code, Codex & more.  
  <sub>topics: ai, ai-agent, gemini, gemini-cli, llm, chat, chatbot, office</sub>
- **[abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control)** · 4,041★ · TypeScript · Rising · health 50  
  Agent-orchestration dashboard for OpenClaw (assign tasks, coordinate agents).  
  <sub>topics: ai-agents, automation, openclaw, orchestration</sub>
- **[crshdn/mission-control](https://github.com/crshdn/mission-control)** · 2,076★ · TypeScript · Hot · health 80  
  Autonomous Product Engine — agents research, build & ship via OpenClaw.  
  <sub>topics: aiagent, automation, openclaw</sub>

### Specialized agent

_Purpose-built agents on top of OpenClaw (research, tutoring, coding, browser…)._

- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 24,708★ · Python · Hot · health 79  
  Agent-native personalized tutoring.  
  <sub>topics: ai-tutor, deepresearch, interactive-learning, large-language-models, multi-agent-systems, rag, ai-agents, clawdbot</sub>
- **[aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)** · 13,360★ · Python · Hot · health 83  
  Autonomous, self-evolving research: chat an idea → get a paper. 🦞  
  <sub>topics: autonomous-research, citation-verification, llm-agents, multi-agent-debate, openclaw, paper-generation, scientific-discovery, self-evolving</sub>
- **[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)** · 8,202★ · Python · Declining · health 25  
  OpenClaw as an AI coworker (coding focus) — but check freshness.  
  <sub>topics: —</sub>
- **[Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL)** · 5,486★ · Python · Hot · health 56  
  Train any OpenClaw agent simply by talking (RL/skill-learning).  
  <sub>topics: async, memory-systems, open-claw, openclaw-skills, rlhf, sglang, skill-learning, slime</sub>
- **[SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws)** · 721★ · Python · Hot · health 75  
  Fast, production-ready Python-native personal assistant inspired by OpenClaw.  
  <sub>topics: agentic-ai, claude, claude-code, memory, python, skills, openclaw</sub>
- **[hydro13/tandem-browser](https://github.com/hydro13/tandem-browser)** · 554★ · TypeScript · Rising · health 74  
  AI-human symbiotic browser with OpenClaw integration.  
  <sub>topics: ai, browser, chromium, electron, human-ai-collaboration, local-first, openclaw, typescript</sub>

## ⚠️ Adopt with caution

Low health and/or not pushed recently — verify before wiring into anything you rely on:

| Project | Health | Lifecycle | Last push | Note |
|---|---|---|---|---|
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | 25 | Declining | 3mo ago | 100d stale; low health; declining |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 47 | Rising | 2mo ago | 79d stale; low health |
| [abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control) | 50 | Rising | 2mo ago | 66d stale |

> Note: `openagen/zeroclaw` (1.9k★, 70d stale) is a *different, older* project than the healthy **`zeroclaw-labs/zeroclaw`** (h93) recommended above — don't confuse them.

## Graph analysis — how they relate

**Community clustering.** These 28 projects span **10 of the graph's 31 communities** — the OpenClaw ecosystem is spread across agent-infra rather than forming one isolated cluster.

- **Community 18** (6): `HKUDS/nanobot`, `NousResearch/hermes-agent`, `BlockRunAI/ClawRouter`, `iOfficeAI/AionUi`, `HKUDS/DeepTutor`, `HKUDS/ClawWork`
- **Community 8** (5): `openclaw/openclaw`, `openclaw/clawhub`, `abhi1693/openclaw-mission-control`, `crshdn/mission-control`, `hydro13/tandem-browser`
- **Community 11** (5): `nanocoai/nanoclaw`, `cloudflare/moltworker`, `hesamsheikh/awesome-openclaw-usecases`, `farion1231/cc-switch`, `CherryHQ/cherry-studio`
- **Community 19** (2): `zeroclaw-labs/zeroclaw`, `rohitg00/awesome-openclaw`
- **Community 5** (2): `nearai/ironclaw`, `RightNow-AI/openfang`
- **Community 20** (2): `supermemoryai/openclaw-supermemory`, `comet-ml/opik-openclaw`
- **Community 22** (2): `vivekchand/clawmetry`, `Gen-Verse/OpenClaw-RL`
- **Community 7** (2): `aiming-lab/AutoResearchClaw`, `SafeRL-Lab/cheetahclaws`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' OpenClaw projects in your ecosystem:

- `vivekchand/clawmetry` — PageRank 0.0032
- `hydro13/tandem-browser` — PageRank 0.0023
- `HKUDS/nanobot` — PageRank 0.0018
- `RightNow-AI/openfang` — PageRank 0.0017
- `NVIDIA/NemoClaw` — PageRank 0.0016
- `abhi1693/openclaw-mission-control` — PageRank 0.0015
- `CherryHQ/cherry-studio` — PageRank 0.0013
- `NousResearch/hermes-agent` — PageRank 0.0010
- `comet-ml/opik-openclaw` — PageRank 0.0010
- `nanocoai/nanoclaw` — PageRank 0.0009

**Direct links between OpenClaw projects** (top similarity edges where both endpoints are in this report):

- `openclaw/clawhub` ⇄ `openclaw/openclaw` (w=0.755) — authors: Patrick-Erichsen, clawsweeper[bot], steipete
- `HKUDS/nanobot` ⇄ `NousResearch/hermes-agent` (w=0.661) — topics: ai, ai-agent, ai-agents, anthropic
- `HKUDS/nanobot` ⇄ `HKUDS/DeepTutor` (w=0.598) — topics: ai-agents
- `HKUDS/nanobot` ⇄ `HKUDS/ClawWork` (w=0.550)
- `hydro13/tandem-browser` ⇄ `abhi1693/openclaw-mission-control` (w=0.474) — topics: openclaw; authors: dependabot[bot]
- `abhi1693/openclaw-mission-control` ⇄ `crshdn/mission-control` (w=0.450) — topics: automation, openclaw
- `comet-ml/opik-openclaw` ⇄ `vivekchand/clawmetry` (w=0.367) — topics: observability, openclaw; authors: dependabot[bot]
- `abhi1693/openclaw-mission-control` ⇄ `RightNow-AI/openfang` (w=0.367) — topics: ai-agents, openclaw; authors: dependabot[bot]
- `comet-ml/opik-openclaw` ⇄ `supermemoryai/openclaw-supermemory` (w=0.350) — topics: clawdbot, moltbot, openclaw
- `comet-ml/opik-openclaw` ⇄ `hydro13/tandem-browser` (w=0.349) — topics: openclaw; authors: dependabot[bot]
- `abhi1693/openclaw-mission-control` ⇄ `nanocoai/nanoclaw` (w=0.336) — topics: ai-agents, openclaw
- `vivekchand/clawmetry` ⇄ `CherryHQ/cherry-studio` (w=0.325) — topics: ai-agent, openclaw; authors: github-actions[bot], dependabot[bot]
- `comet-ml/opik-openclaw` ⇄ `openclaw/clawhub` (w=0.300) — authors: vincentkoc, dependabot[bot]
- `NousResearch/hermes-agent` ⇄ `iOfficeAI/AionUi` (w=0.286) — topics: ai, ai-agent, llm, claude-code
- `CherryHQ/cherry-studio` ⇄ `nanocoai/nanoclaw` (w=0.284) — topics: claude-code, openclaw; authors: github-actions[bot]
- …and 17 more.

## Methodology & caveats

- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: scan for `openclaw` / `clawd*` / `moltbot` across name/description/topics/README, then manual curation. Repos that merely *mention* OpenClaw in passing (general agent harnesses, awesome-lists, unrelated tools) were excluded; memory/MCP-centric repos are covered in their own reports and only the OpenClaw-specific ones appear here.
- **Metrics** (health, lifecycle, bus_factor, days_since_push) are precomputed at snapshot time. **OpenClaw moves extremely fast** — treat all ages/stars as a May-2026 snapshot and re-verify before adopting.
- Re-run after a fresh `classified.json` to refresh.

<sub>Projects covered: 28 · Snapshot: 2026-06-11T21:58:33.384Z</sub>
