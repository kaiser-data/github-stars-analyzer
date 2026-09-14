# OpenClaw Ecosystem — What to Use Now

> Derived from **kaiser-data**'s 2,159 starred repos (snapshot `2026-09-14T11:08:08.535Z`), cross-referenced with the repo-similarity graph (2,159 nodes / 7,086 edges, 37 communities).
>
> Generated 2026-09-14 by `scripts/reports/openclaw_ecosystem.py` (regenerate any time — no API cost).

![Top tools by stars](assets/openclaw-ecosystem-top-tools.svg)

![Tools per category](assets/openclaw-ecosystem-categories.svg)


> **What is OpenClaw?** A personal AI assistant (🦞, formerly *Clawdbot* / *Moltbot*) that runs on any OS/platform. It has spawned a fast-moving ecosystem of runtimes, skills, routers, memory layers, dashboards, and specialized agents — this report maps the parts in your stars and flags what's worth adopting **now**.

## Recommended stack (use now)

Opinionated picks — filtered for **healthy + actively maintained** (high health score, recent pushes). See the risk table below for what to avoid.

| Layer | Pick | ★ | Health | Why |
|---|---|---|---|---|
| Core assistant | [openclaw/openclaw](https://github.com/openclaw/openclaw) | 389,649 (▲653) | 84 | The OpenClaw assistant itself — your own personal AI, any OS/platform. Everything else extends this. |
| Secure runtime | [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | 30,763 (▲55) | 80 | Lightweight OpenClaw alternative that runs in containers for security; WhatsApp/Telegram/Slack connectors. |
| Serverless host | [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | 9,956 (▼2) | 25 | Run OpenClaw on Cloudflare Workers (serverless edge). |
| Skills directory | [openclaw/clawhub](https://github.com/openclaw/clawhub) | 9,419 (▲26) | 80 | The official skill directory for OpenClaw. |
| LLM router | [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | 6,597 (▲16) | 80 | Agent-native LLM router for OpenClaw — 41+ models, <1ms routing, on-chain payments. |
| Memory | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | 26,642 (▲659) | 77 | Fully-local long-term memory (4-tier pipeline); ships as an OpenClaw plugin. |
| Observability | [vivekchand/clawmetry](https://github.com/vivekchand/clawmetry) | 415 (▲9) | 80 | Real-time observability dashboard — 'see your agent think' (OpenTelemetry). |
| Desktop hub | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 132,771 (▲1,513) | 82 | Cross-platform desktop hub for OpenClaw + Claude Code + Codex + Gemini CLI + Hermes. |

**One-liner:** keep `openclaw/openclaw` as the core; run it via **nanoclaw** (security) or **moltworker** (serverless); add **clawhub** skills, **ClawRouter** routing, and **clawmetry** observability. Want a fresh start? **zeroclaw-labs/zeroclaw** is the highest-health alternative you've starred.

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Project | Category | Lang | ★ Stars | Lifecycle | Health | Activity | Last push | Bus factor |
|---|---|---|---|---|---|---|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | Core | TypeScript | 389,649 (▲653) | Hot | 84 | very active | 0d ago | 2 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Alternative agent / OS | Python | 245,317 (▲3,168) | Hot | 75 | very active | 0d ago | 1 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Desktop / orchestration | Rust | 132,771 (▲1,513) | Hot | 82 | very active | 0d ago | 2 |
| [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | Desktop / orchestration | TypeScript | 51,780 (▲279) | Mature | 99 | very active | 0d ago | 5 |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | Alternative agent / OS | Python | 48,143 (▲404) | Hot | 84 | very active | 0d ago | 2 |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Specialized agent | Python | 39,575 (▲721) | Hot | 78 | very active | 0d ago | 1 |
| [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | Desktop / orchestration | TypeScript | 32,806 (▲201) | Hot | 80 | very active | 5d ago | 2 |
| [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | Alternative agent / OS | Rust | 32,801 (▲67) | Hot | 88 | very active | 0d ago | 3 |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | Skills / directory | — | 31,681 (▲8) | Declining | 21 | slowing | 5mo ago | 0 |
| [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | Hosting / secure runtime | TypeScript | 30,763 (▲55) | Hot | 80 | very active | 0d ago | 2 |
| [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | Memory | TypeScript | 26,642 (▲659) | Hot | 77 | very active | 3d ago | 3 |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Hosting / secure runtime | TypeScript | 22,452 (▲72) | Hot | 74 | very active | 0d ago | 3 |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | Alternative agent / OS | Rust | 18,180 (▲17) | Declining | 48 | slowing | 2mo ago | 0 |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | Specialized agent | Python | 14,418 (▲74) | Hot | 70 | very active | 26d ago | 1 |
| [nearai/ironclaw](https://github.com/nearai/ironclaw) | Alternative agent / OS | Rust | 12,620 (▲13) | Hot | 80 | very active | 1d ago | 2 |
| [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | Hosting / secure runtime | TypeScript | 9,956 (▼2) | Declining | 25 | slowing | 4mo ago | 0 |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | Skills / directory | TypeScript | 9,419 (▲26) | Hot | 80 | very active | 0d ago | 1 |
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | Specialized agent | Python | 8,544 (▲6) | Declining | 17 | stale | 6mo ago | 0 |
| [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | Routing | TypeScript | 6,597 (▲16) | Hot | 80 | very active | 0d ago | 1 |
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | Specialized agent | Python | 5,677 (▲9) | Declining | 22 | slowing | 3mo ago | 0 |
| [crshdn/mission-control](https://github.com/crshdn/mission-control) | Desktop / orchestration | TypeScript | 2,136 (▼2) | Declining | 54 | slowing | 2mo ago | 1 |
| [pinchbench/skill](https://github.com/pinchbench/skill) | Observability | Python | 1,344 (▲6) | Declining | 48 | slowing | 2mo ago | 0 |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | Memory | TypeScript | 798 (▼1) | Mature | 47 | active | 5d ago | 1 |
| [SAIL-Research-Lab/cheetahclaws](https://github.com/SAIL-Research-Lab/cheetahclaws) | Specialized agent | Python | 775 (▲4) | Hot | 74 | very active | 2d ago | 1 |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | Observability | TypeScript | 724 (▼1) | Declining | 58 | active | 18d ago | 1 |
| [hydro13/tandem-browser](https://github.com/hydro13/tandem-browser) | Specialized agent | TypeScript | 606 (▲1) | Rising | 68 | very active | 1d ago | 1 |
| [rohitg00/awesome-openclaw](https://github.com/rohitg00/awesome-openclaw) | Skills / directory | Python | 562 (▲1) | Declining | 24 | slowing | 3mo ago | 0 |
| [vivekchand/clawmetry](https://github.com/vivekchand/clawmetry) | Observability | Python | 415 (▲9) | Hot | 80 | very active | 0d ago | 1 |

## By category

### Core

_The assistant everything else plugs into._

- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** · 389,649★ · TypeScript · Hot · health 84  
  The OpenClaw assistant itself — your own personal AI, any OS/platform. Everything else extends this.  
  <sub>topics: ai, assistant, own-your-data, personal, crustacean, molty, openclaw</sub>

### Alternative agent / OS

_Standalone agents/agent-OSes you'd pick *instead of* OpenClaw._

- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** · 245,317★ · Python · Hot · health 75  
  'The agent that grows with you' — large, very active alternative.  
  <sub>topics: ai, ai-agent, ai-agents, llm, anthropic, chatgpt, claude, claude-code</sub>
- **[HKUDS/nanobot](https://github.com/HKUDS/nanobot)** · 48,143★ · Python · Hot · health 84  
  Lightweight open-source agent for tools, chats & workflows.  
  <sub>topics: ai-agent, ai-agents, openclaw, agent-framework, chatbot, chatops, discord-bot, llm-agents</sub>
- **[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)** · 32,801★ · Rust · Hot · health 88  
  Fast, small, fully-autonomous assistant infra (Rust); the healthiest alternative in your stars.  
  <sub>topics: agent, agentic, ai, openclaw, infra, ml, os, zeroclaw</sub>
- **[RightNow-AI/openfang](https://github.com/RightNow-AI/openfang)** · 18,180★ · Rust · Declining · health 48  
  Open-source 'Agent Operating System' (Rust), MCP-native.  
  <sub>topics: agent-framework, ai-agents, llm, mcp, open-source, openclaw, operating-system, rust</sub>
- **[nearai/ironclaw](https://github.com/nearai/ironclaw)** · 12,620★ · Rust · Hot · health 80  
  Agent-OS focused on privacy, security & extensibility (Rust/WASM, CodeAct).  
  <sub>topics: codeact, openclaw, rlm, rust, wasm</sub>

### Hosting / secure runtime

_Where & how to run it safely — containers, edge, managed GPU._

- **[nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw)** · 30,763★ · TypeScript · Hot · health 80  
  Lightweight OpenClaw alternative that runs in containers for security; WhatsApp/Telegram/Slack connectors.  
  <sub>topics: ai-agents, ai-assistant, claude-code, claude-skills, openclaw</sub>
- **[NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)** · 22,452★ · TypeScript · Hot · health 74  
  Run OpenClaw more securely inside NVIDIA OpenShell with managed inference.  
  <sub>topics: ai-agents, nvidia, openclaw, openshell, sandboxing, typescript, hermes, deep-agents</sub>
- **[cloudflare/moltworker](https://github.com/cloudflare/moltworker)** · 9,956★ · TypeScript · Declining · health 25  
  Run OpenClaw on Cloudflare Workers (serverless edge).  
  <sub>topics: ai-agents, cloudflare-workers</sub>

### Skills / directory

_Extend capabilities; find what others have built._

- **[hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)** · 31,681★ · — · Declining · health 21  
  Community collection of OpenClaw use cases (large, but check freshness).  
  <sub>topics: awesome-list, clawdbot, moltbot, openclaw, openclaw-plugin, openclaw-setup, openclaw-skills, usecase</sub>
- **[openclaw/clawhub](https://github.com/openclaw/clawhub)** · 9,419★ · TypeScript · Hot · health 80  
  The official skill directory for OpenClaw.  
  <sub>topics: directory, skill</sub>
- **[rohitg00/awesome-openclaw](https://github.com/rohitg00/awesome-openclaw)** · 562★ · Python · Declining · health 24  
  Curated awesome-list for the OpenClaw ecosystem.  
  <sub>topics: —</sub>

### Routing

_Send each request to the right/cheapest model._

- **[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)** · 6,597★ · TypeScript · Hot · health 80  
  Agent-native LLM router for OpenClaw — 41+ models, <1ms routing, on-chain payments.  
  <sub>topics: ai, ai-agents, anthropic, cost-optimization, deepseek, gemini, llm, llm-router</sub>

### Memory

_Long-term recall across sessions (see also the Memory report)._

- **[TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** · 26,642★ · TypeScript · Hot · health 77  
  Fully-local long-term memory (4-tier pipeline); ships as an OpenClaw plugin.  
  <sub>topics: agent, llm, memory, openclaw-plugin, ai-agent, embedding, local-first, long-term-memory</sub>
- **[supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory)** · 798★ · TypeScript · Mature · health 47  
  Long-term memory & recall packaged specifically for OpenClaw agents.  
  <sub>topics: ai-memory, clawd, clawdbot, memory, moltbot, openai, openclaw</sub>

### Observability

_See, measure & benchmark what your agent is doing._

- **[pinchbench/skill](https://github.com/pinchbench/skill)** · 1,344★ · Python · Declining · health 48  
  Benchmarks LLMs as OpenClaw coding agents on real tasks.  
  <sub>topics: —</sub>
- **[comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw)** · 724★ · TypeScript · Declining · health 58  
  Official plugin exporting OpenClaw agent traces (cost/tokens/errors) to Opik.  
  <sub>topics: clawdbot, evaluation, moltbot, observability, openclaw, testing, ai-agents, llm-observability</sub>
- **[vivekchand/clawmetry](https://github.com/vivekchand/clawmetry)** · 415★ · Python · Hot · health 80  
  Real-time observability dashboard — 'see your agent think' (OpenTelemetry).  
  <sub>topics: ai-agent, monitoring, observability, openclaw, opentelemetry, python, clawmetry, agent-monitoring</sub>

### Desktop / orchestration

_GUIs and multi-agent control panels._

- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 132,771★ · Rust · Hot · health 82  
  Cross-platform desktop hub for OpenClaw + Claude Code + Codex + Gemini CLI + Hermes.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, codex, mcp</sub>
- **[CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)** · 51,780★ · TypeScript · Mature · health 99  
  AI productivity studio (300+ assistants) with OpenClaw/skills support; highest health here.  
  <sub>topics: claude-code, ai-agent, skills, codex, vibe-coding, deepseek, hermes-agent, agent-skills</sub>
- **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** · 32,806★ · TypeScript · Hot · health 80  
  Free local 24/7 cowork app for OpenClaw, Hermes, Claude Code, Codex & more.  
  <sub>topics: ai, ai-agent, gemini, gemini-cli, llm, chat, chatbot, office</sub>
- **[crshdn/mission-control](https://github.com/crshdn/mission-control)** · 2,136★ · TypeScript · Declining · health 54  
  Autonomous Product Engine — agents research, build & ship via OpenClaw.  
  <sub>topics: aiagent, automation, openclaw</sub>

### Specialized agent

_Purpose-built agents on top of OpenClaw (research, tutoring, coding, browser…)._

- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 39,575★ · Python · Hot · health 78  
  Agent-native personalized tutoring.  
  <sub>topics: ai-tutor, deepresearch, interactive-learning, large-language-models, multi-agent-systems, rag, ai-agents, clawdbot</sub>
- **[aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)** · 14,418★ · Python · Hot · health 70  
  Autonomous, self-evolving research: chat an idea → get a paper. 🦞  
  <sub>topics: autonomous-research, citation-verification, llm-agents, multi-agent-debate, openclaw, paper-generation, scientific-discovery, self-evolving</sub>
- **[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)** · 8,544★ · Python · Declining · health 17  
  OpenClaw as an AI coworker (coding focus) — but check freshness.  
  <sub>topics: —</sub>
- **[Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL)** · 5,677★ · Python · Declining · health 22  
  Train any OpenClaw agent simply by talking (RL/skill-learning).  
  <sub>topics: async, memory-systems, open-claw, openclaw-skills, rlhf, sglang, skill-learning, slime</sub>
- **[SAIL-Research-Lab/cheetahclaws](https://github.com/SAIL-Research-Lab/cheetahclaws)** · 775★ · Python · Hot · health 74  
  Fast, production-ready Python-native personal assistant inspired by OpenClaw.  
  <sub>topics: agentic-ai, claude, claude-code, memory, python, skills, openclaw</sub>
- **[hydro13/tandem-browser](https://github.com/hydro13/tandem-browser)** · 606★ · TypeScript · Rising · health 68  
  AI-human symbiotic browser with OpenClaw integration.  
  <sub>topics: ai, browser, chromium, electron, human-ai-collaboration, local-first, openclaw, typescript</sub>

## ⚠️ Adopt with caution

Low health and/or not pushed recently — verify before wiring into anything you rely on:

| Project | Health | Lifecycle | Last push | Note |
|---|---|---|---|---|
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | 17 | Declining | 6mo ago | 195d stale; low health; declining |
| [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | 21 | Declining | 5mo ago | 174d stale; low health; declining |
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | 22 | Declining | 3mo ago | 114d stale; low health; declining |
| [rohitg00/awesome-openclaw](https://github.com/rohitg00/awesome-openclaw) | 24 | Declining | 3mo ago | 94d stale; low health; declining |
| [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | 25 | Declining | 4mo ago | 128d stale; low health; declining |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | 47 | Mature | 5d ago | low health |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | 48 | Declining | 2mo ago | 74d stale; low health; declining |
| [pinchbench/skill](https://github.com/pinchbench/skill) | 48 | Declining | 2mo ago | 74d stale; low health; declining |
| [crshdn/mission-control](https://github.com/crshdn/mission-control) | 54 | Declining | 2mo ago | 69d stale; declining |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | 58 | Declining | 18d ago | declining |

> Note: `openagen/zeroclaw` (1.9k★, 70d stale) is a *different, older* project than the healthy **`zeroclaw-labs/zeroclaw`** (h93) recommended above — don't confuse them.

## Graph analysis — how they relate

**Community clustering.** These 28 projects span **12 of the graph's 37 communities** — the OpenClaw ecosystem is spread across agent-infra rather than forming one isolated cluster.

- **Community 3** (4): `zeroclaw-labs/zeroclaw`, `NousResearch/hermes-agent`, `TencentCloud/TencentDB-Agent-Memory`, `aiming-lab/AutoResearchClaw`
- **Community 16** (4): `BlockRunAI/ClawRouter`, `iOfficeAI/AionUi`, `CherryHQ/cherry-studio`, `hydro13/tandem-browser`
- **Community 11** (3): `HKUDS/nanobot`, `HKUDS/DeepTutor`, `HKUDS/ClawWork`
- **Community 14** (3): `nanocoai/nanoclaw`, `crshdn/mission-control`, `SAIL-Research-Lab/cheetahclaws`
- **Community 25** (3): `hesamsheikh/awesome-openclaw-usecases`, `supermemoryai/openclaw-supermemory`, `comet-ml/opik-openclaw`
- **Community 29** (2): `openclaw/openclaw`, `openclaw/clawhub`
- **Community 2** (2): `RightNow-AI/openfang`, `NVIDIA/NemoClaw`
- **Community 19** (2): `cloudflare/moltworker`, `vivekchand/clawmetry`
- **Community 5** (2): `rohitg00/awesome-openclaw`, `farion1231/cc-switch`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' OpenClaw projects in your ecosystem:

- `vivekchand/clawmetry` — PageRank 0.0026
- `NousResearch/hermes-agent` — PageRank 0.0007
- `openclaw/openclaw` — PageRank 0.0007
- `cloudflare/moltworker` — PageRank 0.0007
- `HKUDS/nanobot` — PageRank 0.0006
- `supermemoryai/openclaw-supermemory` — PageRank 0.0005
- `CherryHQ/cherry-studio` — PageRank 0.0005
- `RightNow-AI/openfang` — PageRank 0.0005
- `HKUDS/DeepTutor` — PageRank 0.0005
- `NVIDIA/NemoClaw` — PageRank 0.0005

**Direct links between OpenClaw projects** (top similarity edges where both endpoints are in this report):

- `openclaw/clawhub` ⇄ `openclaw/openclaw` (w=1.021) — authors: steipete, vincentkoc, vyctorbrzezowski
- `HKUDS/nanobot` ⇄ `HKUDS/DeepTutor` (w=0.586) — topics: ai-agents
- `comet-ml/opik-openclaw` ⇄ `supermemoryai/openclaw-supermemory` (w=0.281) — topics: clawdbot, moltbot, openclaw
- `hesamsheikh/awesome-openclaw-usecases` ⇄ `supermemoryai/openclaw-supermemory` (w=0.250) — topics: clawdbot, moltbot, openclaw
- `hydro13/tandem-browser` ⇄ `iOfficeAI/AionUi` (w=0.235) — topics: ai, openclaw, claude-code, codex
- `NVIDIA/NemoClaw` ⇄ `nanocoai/nanoclaw` (w=0.232) — topics: ai-agents, openclaw
- `RightNow-AI/openfang` ⇄ `nearai/ironclaw` (w=0.232) — topics: openclaw, rust
- `farion1231/cc-switch` ⇄ `RightNow-AI/openfang` (w=0.217) — topics: open-source, rust, mcp, openclaw
- `comet-ml/opik-openclaw` ⇄ `nanocoai/nanoclaw` (w=0.217) — topics: openclaw, ai-agents
- `comet-ml/opik-openclaw` ⇄ `hesamsheikh/awesome-openclaw-usecases` (w=0.214) — topics: clawdbot, moltbot, openclaw
- `farion1231/cc-switch` ⇄ `CherryHQ/cherry-studio` (w=0.194) — topics: claude-code, codex, skills, hermes-agent; authors: fszcd
- `crshdn/mission-control` ⇄ `nanocoai/nanoclaw` (w=0.193) — topics: openclaw
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

<sub>Projects covered: 28 · Snapshot: 2026-09-14T11:08:08.535Z</sub>
