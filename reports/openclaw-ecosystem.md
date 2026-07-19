# OpenClaw Ecosystem — What to Use Now

> Derived from **kaiser-data**'s 1,327 starred repos (snapshot `2026-07-13T08:42:30.177Z`), cross-referenced with the repo-similarity graph (1,327 nodes / 4,302 edges, 26 communities).
>
> Generated 2026-07-19 by `scripts/reports/openclaw_ecosystem.py` (regenerate any time — no API cost).

![Top tools by stars](assets/openclaw-ecosystem-top-tools.svg)

![Tools per category](assets/openclaw-ecosystem-categories.svg)


> **What is OpenClaw?** A personal AI assistant (🦞, formerly *Clawdbot* / *Moltbot*) that runs on any OS/platform. It has spawned a fast-moving ecosystem of runtimes, skills, routers, memory layers, dashboards, and specialized agents — this report maps the parts in your stars and flags what's worth adopting **now**.

## Recommended stack (use now)

Opinionated picks — filtered for **healthy + actively maintained** (high health score, recent pushes). See the risk table below for what to avoid.

| Layer | Pick | ★ | Health | Why |
|---|---|---|---|---|
| Core assistant | [openclaw/openclaw](https://github.com/openclaw/openclaw) | 382,751 (▲4,536) | 79 | The OpenClaw assistant itself — your own personal AI, any OS/platform. Everything else extends this. |
| Secure runtime | [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | 30,215 (▲406) | 69 | Lightweight OpenClaw alternative that runs in containers for security; WhatsApp/Telegram/Slack connectors. |
| Serverless host | [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | 9,916 (▲7) | 30 | Run OpenClaw on Cloudflare Workers (serverless edge). |
| Skills directory | [openclaw/clawhub](https://github.com/openclaw/clawhub) | 9,141 (▲213) | 80 | The official skill directory for OpenClaw. |
| LLM router | [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | 6,652 (▲91) | 77 | Agent-native LLM router for OpenClaw — 41+ models, <1ms routing, on-chain payments. |
| Observability | [vivekchand/clawmetry](https://github.com/vivekchand/clawmetry) | 387 (▲15) | 79 | Real-time observability dashboard — 'see your agent think' (OpenTelemetry). |
| Desktop hub | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 116,545 (▲18,066) | 76 | Cross-platform desktop hub for OpenClaw + Claude Code + Codex + Gemini CLI + Hermes. |

**One-liner:** keep `openclaw/openclaw` as the core; run it via **nanoclaw** (security) or **moltworker** (serverless); add **clawhub** skills, **ClawRouter** routing, and **clawmetry** observability. Want a fresh start? **zeroclaw-labs/zeroclaw** is the highest-health alternative you've starred.

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Project | Category | Lang | ★ Stars | Lifecycle | Health | Activity | Last push | Bus factor |
|---|---|---|---|---|---|---|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Core | TypeScript | 382,751 (▲4,536) | Hot | 79 | very active | 0d ago | 1 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Alternative agent / OS | Python | 213,952 (▲23,019) | Hot | 79 | very active | 0d ago | 2 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Desktop / orchestration | Rust | 116,545 (▲18,066) | Hot | 76 | very active | 1d ago | 1 |
| [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | Desktop / orchestration | TypeScript | 48,494 (▲1,274) | Mature | 89 | very active | 0d ago | 3 |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | Alternative agent / OS | Python | 45,327 (▲1,259) | Hot | 78 | very active | 0d ago | 1 |
| [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | Alternative agent / OS | Rust | 32,241 (▲360) | Hot | 99 | very active | 1d ago | 5 |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | Skills / directory | — | 31,497 (▲159) | Declining | 26 | slowing | 3mo ago | 0 |
| [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | Hosting / secure runtime | TypeScript | 30,215 (▲406) | Hot | 69 | very active | 0d ago | 1 |
| [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | Desktop / orchestration | TypeScript | 29,941 (▲1,870) | Hot | 81 | very active | 0d ago | 2 |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Specialized agent | Python | 25,527 (▲819) | Hot | 78 | very active | 4d ago | 1 |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Hosting / secure runtime | TypeScript | 21,759 (▲627) | Hot | 74 | very active | 0d ago | 3 |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | Alternative agent / OS | Rust | 18,001 (▲192) | Hot | 78 | very active | 11d ago | 1 |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | Specialized agent | Python | 13,782 (▲422) | Hot | 79 | very active | 0d ago | 2 |
| [nearai/ironclaw](https://github.com/nearai/ironclaw) | Alternative agent / OS | Rust | 12,519 (▲77) | Hot | 80 | very active | 0d ago | 2 |
| [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | Hosting / secure runtime | TypeScript | 9,916 (▲7) | Declining | 30 | slowing | 2mo ago | 0 |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | Skills / directory | TypeScript | 9,141 (▲213) | Hot | 80 | very active | 0d ago | 1 |
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | Specialized agent | Python | 8,228 (▲26) | Declining | 22 | slowing | 4mo ago | 0 |
| [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | Routing | TypeScript | 6,652 (▲91) | Hot | 77 | very active | 1d ago | 1 |
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | Specialized agent | Python | 5,563 (▲77) | Hot | 49 | active | 1mo ago | 1 |
| [abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control) | Desktop / orchestration | TypeScript | 4,094 (▲53) | Declining | 27 | slowing | 3mo ago | 0 |
| [crshdn/mission-control](https://github.com/crshdn/mission-control) | Desktop / orchestration | TypeScript | 2,098 (▲22) | Rising | 71 | very active | 6d ago | 1 |
| [pinchbench/skill](https://github.com/pinchbench/skill) | Observability | Python | 1,275 (▲48) | Hot | 78 | very active | 11d ago | 1 |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | Memory | TypeScript | 788 (▼3) | Hot | 58 | very active | 22d ago | 2 |
| [SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws) | Specialized agent | Python | 757 (▲36) | Hot | 76 | very active | 2d ago | 1 |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | Observability | TypeScript | 670 (▲50) | Hot | 72 | very active | 7d ago | 1 |
| [hydro13/tandem-browser](https://github.com/hydro13/tandem-browser) | Specialized agent | TypeScript | 565 (▲11) | Rising | 74 | very active | 3d ago | 1 |
| [rohitg00/awesome-openclaw](https://github.com/rohitg00/awesome-openclaw) | Skills / directory | Python | 554 (▲36) | Hot | 54 | active | 1mo ago | 1 |
| [vivekchand/clawmetry](https://github.com/vivekchand/clawmetry) | Observability | Python | 387 (▲15) | Rising | 79 | very active | 0d ago | 1 |

## By category

### Core

_The assistant everything else plugs into._

- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · 382,751★ · TypeScript · Hot · health 79  
  The OpenClaw assistant itself — your own personal AI, any OS/platform. Everything else extends this.  
  <sub>topics: ai, assistant, own-your-data, personal, crustacean, molty, openclaw</sub>

### Alternative agent / OS

_Standalone agents/agent-OSes you'd pick *instead of* OpenClaw._

- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 213,952★ · Python · Hot · health 79  
  'The agent that grows with you' — large, very active alternative.  
  <sub>topics: ai, ai-agent, ai-agents, llm, anthropic, chatgpt, claude, claude-code</sub>
- **[HKUDS/nanobot](https://github.com/HKUDS/nanobot)** · 45,327★ · Python · Hot · health 78  
  Lightweight open-source agent for tools, chats & workflows.  
  <sub>topics: ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex</sub>
- **[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)** · 32,241★ · Rust · Hot · health 99  
  Fast, small, fully-autonomous assistant infra (Rust); the healthiest alternative in your stars.  
  <sub>topics: agent, agentic, ai, openclaw, infra, ml, os, zeroclaw</sub>
- **[RightNow-AI/openfang](https://github.com/RightNow-AI/openfang)** · 18,001★ · Rust · Hot · health 78  
  Open-source 'Agent Operating System' (Rust), MCP-native.  
  <sub>topics: agent-framework, ai-agents, llm, mcp, open-source, openclaw, operating-system, rust</sub>
- **[nearai/ironclaw](https://github.com/nearai/ironclaw)** · 12,519★ · Rust · Hot · health 80  
  Agent-OS focused on privacy, security & extensibility (Rust/WASM, CodeAct).  
  <sub>topics: codeact, openclaw, rlm, rust, wasm</sub>

### Hosting / secure runtime

_Where & how to run it safely — containers, edge, managed GPU._

- **[nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw)** · 30,215★ · TypeScript · Hot · health 69  
  Lightweight OpenClaw alternative that runs in containers for security; WhatsApp/Telegram/Slack connectors.  
  <sub>topics: ai-agents, ai-assistant, claude-code, claude-skills, openclaw</sub>
- **[NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)** · 21,759★ · TypeScript · Hot · health 74  
  Run OpenClaw more securely inside NVIDIA OpenShell with managed inference.  
  <sub>topics: ai-agents, nvidia, openclaw, openshell, sandboxing, typescript, hermes</sub>
- **[cloudflare/moltworker](https://github.com/cloudflare/moltworker)** · 9,916★ · TypeScript · Declining · health 30  
  Run OpenClaw on Cloudflare Workers (serverless edge).  
  <sub>topics: ai-agents, cloudflare-workers</sub>

### Skills / directory

_Extend capabilities; find what others have built._

- **[hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)** · 31,497★ · — · Declining · health 26  
  Community collection of OpenClaw use cases (large, but check freshness).  
  <sub>topics: awesome-list, clawdbot, moltbot, openclaw, openclaw-plugin, openclaw-setup, openclaw-skills, usecase</sub>
- **[openclaw/clawhub](https://github.com/openclaw/clawhub)** · 9,141★ · TypeScript · Hot · health 80  
  The official skill directory for OpenClaw.  
  <sub>topics: directory, skill</sub>
- **[rohitg00/awesome-openclaw](https://github.com/rohitg00/awesome-openclaw)** · 554★ · Python · Hot · health 54  
  Curated awesome-list for the OpenClaw ecosystem.  
  <sub>topics: —</sub>

### Routing

_Send each request to the right/cheapest model._

- **[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)** · 6,652★ · TypeScript · Hot · health 77  
  Agent-native LLM router for OpenClaw — 41+ models, <1ms routing, on-chain payments.  
  <sub>topics: ai, ai-agents, anthropic, cost-optimization, deepseek, gemini, llm, llm-router</sub>

### Memory

_Long-term recall across sessions (see also the Memory report)._

- **[supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory)** · 788★ · TypeScript · Hot · health 58  
  Long-term memory & recall packaged specifically for OpenClaw agents.  
  <sub>topics: ai-memory, clawd, clawdbot, memory, moltbot, openai, openclaw</sub>

### Observability

_See, measure & benchmark what your agent is doing._

- **[pinchbench/skill](https://github.com/pinchbench/skill)** · 1,275★ · Python · Hot · health 78  
  Benchmarks LLMs as OpenClaw coding agents on real tasks.  
  <sub>topics: —</sub>
- **[comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw)** · 670★ · TypeScript · Hot · health 72  
  Official plugin exporting OpenClaw agent traces (cost/tokens/errors) to Opik.  
  <sub>topics: clawdbot, evaluation, moltbot, observability, openclaw, testing</sub>
- **[vivekchand/clawmetry](https://github.com/vivekchand/clawmetry)** · 387★ · Python · Rising · health 79  
  Real-time observability dashboard — 'see your agent think' (OpenTelemetry).  
  <sub>topics: ai-agent, dashboard, monitoring, observability, openclaw, opentelemetry, python, clawmetry</sub>

### Desktop / orchestration

_GUIs and multi-agent control panels._

- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 116,545★ · Rust · Hot · health 76  
  Cross-platform desktop hub for OpenClaw + Claude Code + Codex + Gemini CLI + Hermes.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, typescript, codex</sub>
- **[CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)** · 48,494★ · TypeScript · Mature · health 89  
  AI productivity studio (300+ assistants) with OpenClaw/skills support; highest health here.  
  <sub>topics: claude-code, ai-agent, skills, codex, vibe-coding, openclaw, deepseek, awesome-skills</sub>
- **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** · 29,941★ · TypeScript · Hot · health 81  
  Free local 24/7 cowork app for OpenClaw, Hermes, Claude Code, Codex & more.  
  <sub>topics: ai, ai-agent, gemini, gemini-cli, llm, chat, chatbot, office</sub>
- **[abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control)** · 4,094★ · TypeScript · Declining · health 27  
  Agent-orchestration dashboard for OpenClaw (assign tasks, coordinate agents).  
  <sub>topics: ai-agents, automation, openclaw, orchestration</sub>
- **[crshdn/mission-control](https://github.com/crshdn/mission-control)** · 2,098★ · TypeScript · Rising · health 71  
  Autonomous Product Engine — agents research, build & ship via OpenClaw.  
  <sub>topics: aiagent, automation, openclaw</sub>

### Specialized agent

_Purpose-built agents on top of OpenClaw (research, tutoring, coding, browser…)._

- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 25,527★ · Python · Hot · health 78  
  Agent-native personalized tutoring.  
  <sub>topics: ai-tutor, deepresearch, interactive-learning, large-language-models, multi-agent-systems, rag, ai-agents, clawdbot</sub>
- **[aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)** · 13,782★ · Python · Hot · health 79  
  Autonomous, self-evolving research: chat an idea → get a paper. 🦞  
  <sub>topics: autonomous-research, citation-verification, llm-agents, multi-agent-debate, openclaw, paper-generation, scientific-discovery, self-evolving</sub>
- **[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)** · 8,228★ · Python · Declining · health 22  
  OpenClaw as an AI coworker (coding focus) — but check freshness.  
  <sub>topics: —</sub>
- **[Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL)** · 5,563★ · Python · Hot · health 49  
  Train any OpenClaw agent simply by talking (RL/skill-learning).  
  <sub>topics: async, memory-systems, open-claw, openclaw-skills, rlhf, sglang, skill-learning, slime</sub>
- **[SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws)** · 757★ · Python · Hot · health 76  
  Fast, production-ready Python-native personal assistant inspired by OpenClaw.  
  <sub>topics: agentic-ai, claude, claude-code, memory, python, skills, openclaw</sub>
- **[hydro13/tandem-browser](https://github.com/hydro13/tandem-browser)** · 565★ · TypeScript · Rising · health 74  
  AI-human symbiotic browser with OpenClaw integration.  
  <sub>topics: ai, browser, chromium, electron, human-ai-collaboration, local-first, openclaw, typescript</sub>

## ⚠️ Adopt with caution

Low health and/or not pushed recently — verify before wiring into anything you rely on:

| Project | Health | Lifecycle | Last push | Note |
|---|---|---|---|---|
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | 22 | Declining | 4mo ago | 132d stale; low health; declining |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 26 | Declining | 3mo ago | 111d stale; low health; declining |
| [abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control) | 27 | Declining | 3mo ago | 97d stale; low health; declining |
| [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | 30 | Declining | 2mo ago | 65d stale; low health; declining |
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | 49 | Hot | 1mo ago | 51d stale; low health |

> Note: `openagen/zeroclaw` (1.9k★, 70d stale) is a *different, older* project than the healthy **`zeroclaw-labs/zeroclaw`** (h93) recommended above — don't confuse them.

## Graph analysis — how they relate

**Community clustering.** These 28 projects span **9 of the graph's 26 communities** — the OpenClaw ecosystem is spread across agent-infra rather than forming one isolated cluster.

- **Community 18** (11): `openclaw/openclaw`, `HKUDS/nanobot`, `NousResearch/hermes-agent`, `openclaw/clawhub`, `hesamsheikh/awesome-openclaw-usecases`, `BlockRunAI/ClawRouter`, `supermemoryai/openclaw-supermemory`, `comet-ml/opik-openclaw`, `iOfficeAI/AionUi`, `HKUDS/DeepTutor`, `HKUDS/ClawWork`
- **Community 16** (4): `nanocoai/nanoclaw`, `vivekchand/clawmetry`, `CherryHQ/cherry-studio`, `SafeRL-Lab/cheetahclaws`
- **Community 2** (3): `nearai/ironclaw`, `RightNow-AI/openfang`, `farion1231/cc-switch`
- **Community 12** (3): `NVIDIA/NemoClaw`, `abhi1693/openclaw-mission-control`, `crshdn/mission-control`
- **Community 0** (2): `zeroclaw-labs/zeroclaw`, `pinchbench/skill`
- **Community 10** (2): `Gen-Verse/OpenClaw-RL`, `hydro13/tandem-browser`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' OpenClaw projects in your ecosystem:

- `hydro13/tandem-browser` — PageRank 0.0019
- `vivekchand/clawmetry` — PageRank 0.0016
- `NVIDIA/NemoClaw` — PageRank 0.0016
- `RightNow-AI/openfang` — PageRank 0.0015
- `HKUDS/nanobot` — PageRank 0.0013
- `comet-ml/opik-openclaw` — PageRank 0.0011
- `openclaw/openclaw` — PageRank 0.0010
- `CherryHQ/cherry-studio` — PageRank 0.0010
- `nanocoai/nanoclaw` — PageRank 0.0009
- `NousResearch/hermes-agent` — PageRank 0.0008

**Direct links between OpenClaw projects** (top similarity edges where both endpoints are in this report):

- `openclaw/clawhub` ⇄ `openclaw/openclaw` (w=0.903) — authors: vincentkoc, steipete, fuller-stack-dev
- `HKUDS/nanobot` ⇄ `NousResearch/hermes-agent` (w=0.661) — topics: ai, ai-agent, ai-agents, anthropic
- `HKUDS/nanobot` ⇄ `HKUDS/DeepTutor` (w=0.598) — topics: ai-agents
- `abhi1693/openclaw-mission-control` ⇄ `crshdn/mission-control` (w=0.450) — topics: automation, openclaw
- `comet-ml/opik-openclaw` ⇄ `hydro13/tandem-browser` (w=0.413) — topics: openclaw; authors: dependabot[bot]
- `comet-ml/opik-openclaw` ⇄ `supermemoryai/openclaw-supermemory` (w=0.350) — topics: clawdbot, moltbot, openclaw
- `abhi1693/openclaw-mission-control` ⇄ `nanocoai/nanoclaw` (w=0.336) — topics: ai-agents, openclaw
- `CherryHQ/cherry-studio` ⇄ `nanocoai/nanoclaw` (w=0.309) — topics: claude-code, openclaw; authors: github-actions[bot]
- `NousResearch/hermes-agent` ⇄ `iOfficeAI/AionUi` (w=0.286) — topics: ai, ai-agent, llm, claude-code
- `comet-ml/opik-openclaw` ⇄ `hesamsheikh/awesome-openclaw-usecases` (w=0.273) — topics: clawdbot, moltbot, openclaw
- `NVIDIA/NemoClaw` ⇄ `abhi1693/openclaw-mission-control` (w=0.272) — topics: ai-agents, openclaw
- `comet-ml/opik-openclaw` ⇄ `openclaw/openclaw` (w=0.267) — topics: openclaw; authors: vincentkoc
- `BlockRunAI/ClawRouter` ⇄ `openclaw/openclaw` (w=0.263) — topics: ai, openclaw; authors: steipete
- `HKUDS/nanobot` ⇄ `BlockRunAI/ClawRouter` (w=0.261) — topics: ai, ai-agents, anthropic, llm
- `abhi1693/openclaw-mission-control` ⇄ `cloudflare/moltworker` (w=0.250) — topics: ai-agents
- …and 14 more.

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: scan for `openclaw` / `clawd*` / `moltbot` across name/description/topics/README, then manual curation. Repos that merely *mention* OpenClaw in passing (general agent harnesses, awesome-lists, unrelated tools) were excluded; memory/MCP-centric repos are covered in their own reports and only the OpenClaw-specific ones appear here.
- **Metrics** (health, lifecycle, bus_factor, days_since_push) are precomputed at snapshot time. **OpenClaw moves extremely fast** — treat all ages/stars as a May-2026 snapshot and re-verify before adopting.
- Re-run after a fresh `classified.json` to refresh.

<sub>Projects covered: 28 · Snapshot: 2026-07-13T08:42:30.177Z</sub>
