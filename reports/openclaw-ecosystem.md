# OpenClaw Ecosystem — What to Use Now

> Derived from **kaiser-data**'s 2,243 starred repos (snapshot `2026-09-25T10:37:19.717Z`), cross-referenced with the repo-similarity graph (2,243 nodes / 7,393 edges, 35 communities).
>
> Generated 2026-09-25 by `scripts/reports/openclaw_ecosystem.py` (regenerate any time — no API cost).

![Top tools by stars](assets/openclaw-ecosystem-top-tools.svg)

![Tools per category](assets/openclaw-ecosystem-categories.svg)


> **What is OpenClaw?** A personal AI assistant (🦞, formerly *Clawdbot* / *Moltbot*) that runs on any OS/platform. It has spawned a fast-moving ecosystem of runtimes, skills, routers, memory layers, dashboards, and specialized agents — this report maps the parts in your stars and flags what's worth adopting **now**.

## Recommended stack (use now)

Opinionated picks — filtered for **healthy + actively maintained** (high health score, recent pushes). See the risk table below for what to avoid.

| Layer | Pick | ★ | Health | Why |
|---|---|---|---|---|
| Core assistant | [openclaw/openclaw](https://github.com/openclaw/openclaw) | 390,467 (▲286) | 84 | The OpenClaw assistant itself — your own personal AI, any OS/platform. Everything else extends this. |
| Secure runtime | [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | 30,846 (▲35) | 76 | Lightweight OpenClaw alternative that runs in containers for security; WhatsApp/Telegram/Slack connectors. |
| Serverless host | [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | 9,958 (▼3) | 24 | Run OpenClaw on Cloudflare Workers (serverless edge). |
| Skills directory | [openclaw/clawhub](https://github.com/openclaw/clawhub) | 9,453 (▲17) | 80 | The official skill directory for OpenClaw. |
| LLM router | [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | 6,614 (▲3) | 80 | Agent-native LLM router for OpenClaw — 41+ models, <1ms routing, on-chain payments. |
| Memory | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | 27,264 (▲179) | 84 | Fully-local long-term memory (4-tier pipeline); ships as an OpenClaw plugin. |
| Observability | [vivekchand/clawmetry](https://github.com/vivekchand/clawmetry) | 420 (▲1) | 80 | Real-time observability dashboard — 'see your agent think' (OpenTelemetry). |
| Desktop hub | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 136,676 (▲2,755) | 81 | Cross-platform desktop hub for OpenClaw + Claude Code + Codex + Gemini CLI + Hermes. |

**One-liner:** keep `openclaw/openclaw` as the core; run it via **nanoclaw** (security) or **moltworker** (serverless); add **clawhub** skills, **ClawRouter** routing, and **clawmetry** observability. Want a fresh start? **zeroclaw-labs/zeroclaw** is the highest-health alternative you've starred.

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Project | Category | Lang | ★ Stars | Lifecycle | Health | Activity | Last push | Bus factor |
|---|---|---|---|---|---|---|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Core | TypeScript | 390,467 (▲286) | Hot | 84 | very active | 0d ago | 2 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Alternative agent / OS | Python | 248,814 (▲1,187) | Hot | 80 | very active | 0d ago | 2 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Desktop / orchestration | Rust | 136,676 (▲2,755) | Hot | 81 | very active | 0d ago | 2 |
| [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | Desktop / orchestration | TypeScript | 52,139 (▲90) | Mature | 94 | very active | 0d ago | 4 |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | Alternative agent / OS | Python | 48,561 (▲116) | Hot | 84 | very active | 0d ago | 2 |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Specialized agent | Python | 40,278 (▲166) | Rising | 78 | very active | 1d ago | 1 |
| [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | Desktop / orchestration | TypeScript | 33,113 (▲106) | Hot | 79 | very active | 16d ago | 2 |
| [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | Alternative agent / OS | Rust | 32,878 (▲29) | Hot | 83 | very active | 0d ago | 2 |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | Skills / directory | — | 31,676 (▲7) | Declining | 20 | stale | 6mo ago | 0 |
| [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | Hosting / secure runtime | TypeScript | 30,846 (▲35) | Hot | 76 | very active | 1d ago | 1 |
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | Memory | TypeScript | 27,264 (▲179) | Hot | 84 | very active | 1d ago | 4 |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Hosting / secure runtime | TypeScript | 22,538 (▲34) | Hot | 74 | very active | 0d ago | 3 |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | Alternative agent / OS | Rust | 18,210 (▲1) | Declining | 47 | slowing | 2mo ago | 0 |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | Specialized agent | Python | 14,527 (▲43) | Hot | 69 | active | 1mo ago | 1 |
| [nearai/ironclaw](https://github.com/nearai/ironclaw) | Alternative agent / OS | Rust | 12,632 (▲6) | Hot | 80 | very active | 0d ago | 2 |
| [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | Hosting / secure runtime | TypeScript | 9,958 (▼3) | Declining | 24 | slowing | 4mo ago | 0 |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | Skills / directory | TypeScript | 9,453 (▲17) | Hot | 80 | very active | 0d ago | 1 |
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | Specialized agent | Python | 8,555 (▲5) | Declining | 16 | stale | 6mo ago | 0 |
| [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | Routing | TypeScript | 6,614 (▲3) | Hot | 80 | very active | 0d ago | 1 |
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | Specialized agent | Python | 5,699 (▲5) | Declining | 21 | slowing | 4mo ago | 0 |
| [crshdn/mission-control](https://github.com/crshdn/mission-control) | Desktop / orchestration | TypeScript | 2,143 (▲3) | Declining | 59 | active | 9d ago | 1 |
| [pinchbench/skill](https://github.com/pinchbench/skill) | Observability | Python | 1,350 (▲1) | Declining | 47 | slowing | 2mo ago | 0 |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | Memory | TypeScript | 795 | Mature | 47 | active | 8d ago | 1 |
| [SAIL-Research-Lab/cheetahclaws](https://github.com/SAIL-Research-Lab/cheetahclaws) | Specialized agent | Python | 780 | Hot | 73 | very active | 5d ago | 1 |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | Observability | TypeScript | 724 (▼1) | Declining | 60 | active | 10d ago | 1 |
| [hydro13/tandem-browser](https://github.com/hydro13/tandem-browser) | Specialized agent | TypeScript | 611 | Rising | 68 | very active | 6d ago | 1 |
| [rohitg00/awesome-openclaw](https://github.com/rohitg00/awesome-openclaw) | Skills / directory | Python | 562 (▼1) | Declining | 23 | slowing | 3mo ago | 0 |
| [vivekchand/clawmetry](https://github.com/vivekchand/clawmetry) | Observability | Python | 420 (▲1) | Hot | 80 | very active | 0d ago | 1 |

## By category

### Core

_The assistant everything else plugs into._

- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · 390,467★ · TypeScript · Hot · health 84  
  The OpenClaw assistant itself — your own personal AI, any OS/platform. Everything else extends this.  
  <sub>topics: ai, assistant, own-your-data, personal, crustacean, molty, openclaw</sub>

### Alternative agent / OS

_Standalone agents/agent-OSes you'd pick *instead of* OpenClaw._

- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 248,814★ · Python · Hot · health 80  
  'The agent that grows with you' — large, very active alternative.  
  <sub>topics: ai, ai-agent, ai-agents, llm, anthropic, chatgpt, claude, claude-code</sub>
- **[HKUDS/nanobot](https://github.com/HKUDS/nanobot)** · 48,561★ · Python · Hot · health 84  
  Lightweight open-source agent for tools, chats & workflows.  
  <sub>topics: ai-agent, ai-agents, openclaw, agent-framework, chatbot, chatops, discord-bot, llm-agents</sub>
- **[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)** · 32,878★ · Rust · Hot · health 83  
  Fast, small, fully-autonomous assistant infra (Rust); the healthiest alternative in your stars.  
  <sub>topics: agent, agentic, ai, openclaw, infra, ml, os, zeroclaw</sub>
- **[RightNow-AI/openfang](https://github.com/RightNow-AI/openfang)** · 18,210★ · Rust · Declining · health 47  
  Open-source 'Agent Operating System' (Rust), MCP-native.  
  <sub>topics: agent-framework, ai-agents, llm, mcp, open-source, openclaw, operating-system, rust</sub>
- **[nearai/ironclaw](https://github.com/nearai/ironclaw)** · 12,632★ · Rust · Hot · health 80  
  Agent-OS focused on privacy, security & extensibility (Rust/WASM, CodeAct).  
  <sub>topics: codeact, openclaw, rlm, rust, wasm</sub>

### Hosting / secure runtime

_Where & how to run it safely — containers, edge, managed GPU._

- **[nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw)** · 30,846★ · TypeScript · Hot · health 76  
  Lightweight OpenClaw alternative that runs in containers for security; WhatsApp/Telegram/Slack connectors.  
  <sub>topics: ai-agents, ai-assistant, claude-code, claude-skills, openclaw</sub>
- **[NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)** · 22,538★ · TypeScript · Hot · health 74  
  Run OpenClaw more securely inside NVIDIA OpenShell with managed inference.  
  <sub>topics: ai-agents, nvidia, openclaw, openshell, sandboxing, typescript, hermes, deep-agents</sub>
- **[cloudflare/moltworker](https://github.com/cloudflare/moltworker)** · 9,958★ · TypeScript · Declining · health 24  
  Run OpenClaw on Cloudflare Workers (serverless edge).  
  <sub>topics: ai-agents, cloudflare-workers</sub>

### Skills / directory

_Extend capabilities; find what others have built._

- **[hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)** · 31,676★ · — · Declining · health 20  
  Community collection of OpenClaw use cases (large, but check freshness).  
  <sub>topics: awesome-list, clawdbot, moltbot, openclaw, openclaw-plugin, openclaw-setup, openclaw-skills, usecase</sub>
- **[openclaw/clawhub](https://github.com/openclaw/clawhub)** · 9,453★ · TypeScript · Hot · health 80  
  The official skill directory for OpenClaw.  
  <sub>topics: directory, skill</sub>
- **[rohitg00/awesome-openclaw](https://github.com/rohitg00/awesome-openclaw)** · 562★ · Python · Declining · health 23  
  Curated awesome-list for the OpenClaw ecosystem.  
  <sub>topics: —</sub>

### Routing

_Send each request to the right/cheapest model._

- **[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)** · 6,614★ · TypeScript · Hot · health 80  
  Agent-native LLM router for OpenClaw — 41+ models, <1ms routing, on-chain payments.  
  <sub>topics: ai, ai-agents, anthropic, cost-optimization, deepseek, gemini, llm, llm-router</sub>

### Memory

_Long-term recall across sessions (see also the Memory report)._

- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 27,264★ · TypeScript · Hot · health 84  
  Fully-local long-term memory (4-tier pipeline); ships as an OpenClaw plugin.  
  <sub>topics: agent, llm, memory, openclaw-plugin, ai-agent, embedding, local-first, long-term-memory</sub>
- **[supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory)** · 795★ · TypeScript · Mature · health 47  
  Long-term memory & recall packaged specifically for OpenClaw agents.  
  <sub>topics: ai-memory, clawd, clawdbot, memory, moltbot, openai, openclaw</sub>

### Observability

_See, measure & benchmark what your agent is doing._

- **[pinchbench/skill](https://github.com/pinchbench/skill)** · 1,350★ · Python · Declining · health 47  
  Benchmarks LLMs as OpenClaw coding agents on real tasks.  
  <sub>topics: —</sub>
- **[comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw)** · 724★ · TypeScript · Declining · health 60  
  Official plugin exporting OpenClaw agent traces (cost/tokens/errors) to Opik.  
  <sub>topics: clawdbot, evaluation, moltbot, observability, openclaw, testing, ai-agents, llm-observability</sub>
- **[vivekchand/clawmetry](https://github.com/vivekchand/clawmetry)** · 420★ · Python · Hot · health 80  
  Real-time observability dashboard — 'see your agent think' (OpenTelemetry).  
  <sub>topics: ai-agent, monitoring, observability, openclaw, opentelemetry, python, clawmetry, agent-monitoring</sub>

### Desktop / orchestration

_GUIs and multi-agent control panels._

- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 136,676★ · Rust · Hot · health 81  
  Cross-platform desktop hub for OpenClaw + Claude Code + Codex + Gemini CLI + Hermes.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, codex, mcp</sub>
- **[CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)** · 52,139★ · TypeScript · Mature · health 94  
  AI productivity studio (300+ assistants) with OpenClaw/skills support; highest health here.  
  <sub>topics: claude-code, ai-agent, skills, codex, vibe-coding, deepseek, hermes-agent, agent-skills</sub>
- **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** · 33,113★ · TypeScript · Hot · health 79  
  Free local 24/7 cowork app for OpenClaw, Hermes, Claude Code, Codex & more.  
  <sub>topics: ai, ai-agent, gemini, gemini-cli, llm, chat, chatbot, office</sub>
- **[crshdn/mission-control](https://github.com/crshdn/mission-control)** · 2,143★ · TypeScript · Declining · health 59  
  Autonomous Product Engine — agents research, build & ship via OpenClaw.  
  <sub>topics: aiagent, automation, openclaw</sub>

### Specialized agent

_Purpose-built agents on top of OpenClaw (research, tutoring, coding, browser…)._

- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 40,278★ · Python · Rising · health 78  
  Agent-native personalized tutoring.  
  <sub>topics: ai-tutor, deepresearch, interactive-learning, multi-agent-systems, rag, ai-agents, cli-tool, clawbot</sub>
- **[aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)** · 14,527★ · Python · Hot · health 69  
  Autonomous, self-evolving research: chat an idea → get a paper. 🦞  
  <sub>topics: autonomous-research, citation-verification, llm-agents, multi-agent-debate, openclaw, paper-generation, scientific-discovery, self-evolving</sub>
- **[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)** · 8,555★ · Python · Declining · health 16  
  OpenClaw as an AI coworker (coding focus) — but check freshness.  
  <sub>topics: —</sub>
- **[Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL)** · 5,699★ · Python · Declining · health 21  
  Train any OpenClaw agent simply by talking (RL/skill-learning).  
  <sub>topics: async, memory-systems, open-claw, openclaw-skills, rlhf, sglang, skill-learning, slime</sub>
- **[SAIL-Research-Lab/cheetahclaws](https://github.com/SAIL-Research-Lab/cheetahclaws)** · 780★ · Python · Hot · health 73  
  Fast, production-ready Python-native personal assistant inspired by OpenClaw.  
  <sub>topics: agentic-ai, claude, claude-code, memory, python, skills, openclaw</sub>
- **[hydro13/tandem-browser](https://github.com/hydro13/tandem-browser)** · 611★ · TypeScript · Rising · health 68  
  AI-human symbiotic browser with OpenClaw integration.  
  <sub>topics: ai, browser, chromium, electron, human-ai-collaboration, local-first, openclaw, typescript</sub>

## ⚠️ Adopt with caution

Low health and/or not pushed recently — verify before wiring into anything you rely on:

| Project | Health | Lifecycle | Last push | Note |
|---|---|---|---|---|
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | 16 | Declining | 6mo ago | 206d stale; low health; declining |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 20 | Declining | 6mo ago | 185d stale; low health; declining |
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | 21 | Declining | 4mo ago | 125d stale; low health; declining |
| [rohitg00/awesome-openclaw](https://github.com/rohitg00/awesome-openclaw) | 23 | Declining | 3mo ago | 105d stale; low health; declining |
| [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | 24 | Declining | 4mo ago | 139d stale; low health; declining |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | 47 | Declining | 2mo ago | 85d stale; low health; declining |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | 47 | Mature | 8d ago | low health |
| [pinchbench/skill](https://github.com/pinchbench/skill) | 47 | Declining | 2mo ago | 85d stale; low health; declining |
| [crshdn/mission-control](https://github.com/crshdn/mission-control) | 59 | Declining | 9d ago | declining |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | 60 | Declining | 10d ago | declining |

> Note: `openagen/zeroclaw` (1.9k★, 70d stale) is a *different, older* project than the healthy **`zeroclaw-labs/zeroclaw`** (h93) recommended above — don't confuse them.

## Graph analysis — how they relate

**Community clustering.** These 28 projects span **14 of the graph's 35 communities** — the OpenClaw ecosystem is spread across agent-infra rather than forming one isolated cluster.

- **Community 6** (5): `zeroclaw-labs/zeroclaw`, `NousResearch/hermes-agent`, `cloudflare/moltworker`, `BlockRunAI/ClawRouter`, `TencentCloud/TencentDB-Agent-Memory`
- **Community 1** (4): `rohitg00/awesome-openclaw`, `iOfficeAI/AionUi`, `CherryHQ/cherry-studio`, `hydro13/tandem-browser`
- **Community 15** (3): `HKUDS/nanobot`, `HKUDS/DeepTutor`, `HKUDS/ClawWork`
- **Community 21** (3): `hesamsheikh/awesome-openclaw-usecases`, `supermemoryai/openclaw-supermemory`, `comet-ml/opik-openclaw`
- **Community 26** (2): `openclaw/openclaw`, `openclaw/clawhub`
- **Community 11** (2): `RightNow-AI/openfang`, `NVIDIA/NemoClaw`
- **Community 3** (2): `nanocoai/nanoclaw`, `crshdn/mission-control`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' OpenClaw projects in your ecosystem:

- `vivekchand/clawmetry` — PageRank 0.0010
- `NousResearch/hermes-agent` — PageRank 0.0007
- `openclaw/openclaw` — PageRank 0.0006
- `cloudflare/moltworker` — PageRank 0.0006
- `CherryHQ/cherry-studio` — PageRank 0.0006
- `RightNow-AI/openfang` — PageRank 0.0006
- `HKUDS/DeepTutor` — PageRank 0.0006
- `HKUDS/nanobot` — PageRank 0.0006
- `supermemoryai/openclaw-supermemory` — PageRank 0.0005
- `nanocoai/nanoclaw` — PageRank 0.0005

**Direct links between OpenClaw projects** (top similarity edges where both endpoints are in this report):

- `openclaw/clawhub` ⇄ `openclaw/openclaw` (w=1.150) — authors: Patrick-Erichsen, SebTardif, vincentkoc
- `HKUDS/nanobot` ⇄ `HKUDS/DeepTutor` (w=0.586) — topics: ai-agents
- `comet-ml/opik-openclaw` ⇄ `supermemoryai/openclaw-supermemory` (w=0.281) — topics: clawdbot, moltbot, openclaw
- `hesamsheikh/awesome-openclaw-usecases` ⇄ `supermemoryai/openclaw-supermemory` (w=0.250) — topics: clawdbot, moltbot, openclaw
- `hydro13/tandem-browser` ⇄ `iOfficeAI/AionUi` (w=0.235) — topics: ai, openclaw, claude-code, codex
- `NVIDIA/NemoClaw` ⇄ `nanocoai/nanoclaw` (w=0.232) — topics: ai-agents, openclaw
- `RightNow-AI/openfang` ⇄ `nearai/ironclaw` (w=0.232) — topics: openclaw, rust
- `farion1231/cc-switch` ⇄ `RightNow-AI/openfang` (w=0.217) — topics: open-source, rust, mcp, openclaw
- `comet-ml/opik-openclaw` ⇄ `nanocoai/nanoclaw` (w=0.217) — topics: openclaw, ai-agents
- `comet-ml/opik-openclaw` ⇄ `hesamsheikh/awesome-openclaw-usecases` (w=0.214) — topics: clawdbot, moltbot, openclaw
- `nearai/ironclaw` ⇄ `nanocoai/nanoclaw` (w=0.206) — topics: openclaw; authors: linhongyu510
- `crshdn/mission-control` ⇄ `nanocoai/nanoclaw` (w=0.193) — topics: openclaw
- `farion1231/cc-switch` ⇄ `iOfficeAI/AionUi` (w=0.176) — topics: claude-code, codex, opencode, skills
- `crshdn/mission-control` ⇄ `supermemoryai/openclaw-supermemory` (w=0.161) — topics: openclaw
- `crshdn/mission-control` ⇄ `openclaw/openclaw` (w=0.161) — topics: openclaw

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

<sub>Projects covered: 28 · Snapshot: 2026-09-25T10:37:19.717Z</sub>
