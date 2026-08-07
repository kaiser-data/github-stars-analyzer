# Which Claw Should I Use? — A Decision Report

> Derived from **kaiser-data**'s 1,476 starred repos (snapshot `2026-08-07T21:10:17.796Z`), cross-referenced with the repo-similarity graph.
>
> Generated 2026-08-07 by `scripts/reports/which_claw.py` (regenerate any time — no API cost).

> **Scope.** This ranks the standalone **claws** — agents/runtimes you'd run *as* your assistant. "Claw" here is a **role, not a name**: functional claws that aren't literally branded *claw* (Hermes, nanobot, eliza, oh-my-openagent) are ranked alongside the named ones and tagged **†**. The accessory ecosystem (skills, routers, memory, observability, dashboards) is covered separately in the **OpenClaw Ecosystem** report; those *complement* a claw rather than replace it.

## TL;DR — two honest answers

**On raw metrics, [`openclaw/openclaw`](https://github.com/openclaw/openclaw) wins** (composite 0.801): health 84, bus factor 2, very active. And it's **robust** — it stays #1 under 4 of 6 weighting profiles (see the sensitivity analysis), so that's not an artifact of how I weighted the score. If you want the cleanest, most resilient standalone claw and don't care about the surrounding tooling, take it.

**As a pragmatic default, [`openclaw/openclaw`](https://github.com/openclaw/openclaw) (composite 0.801, #1).** The score above *deliberately excludes the ecosystem network effect* — and that's OpenClaw's real edge: every accessory you've already starred (`clawhub`, `ClawRouter`, `clawmetry`, `opik-openclaw`, `openclaw-supermemory`, `NemoClaw`, `moltworker`) targets OpenClaw, not zeroclaw. That's a genuine switching cost in its favour.

- **TypeScript + crypto fit → OpenClaw.** It's TS (so is most of its accessory line), and the ecosystem leans on-chain — e.g. `ClawRouter` does on-chain payments / agent-native settlement. If you live in the TS and crypto world, that's another argument for the hub.
- **Maximum stability/quality →** [`sipeed/picoclaw`](https://github.com/sipeed/picoclaw) (health 85).
- **Running untrusted tools / need isolation →** [`NVIDIA/NemoClaw`](https://github.com/NVIDIA/NemoClaw) — security-hardened runtime.
- **Mostly coding →** [`code-yeongyu/oh-my-openagent`](https://github.com/code-yeongyu/oh-my-openagent) is the coding-focused claw.
- **Tiny/edge footprint →** `sipeed/picoclaw` and `nullclaw/nullclaw` (minimal builds).

## The ranking

Composite = 25% health + 25% adoption + 20% resilience + 15% maturity + 15% momentum. Adoption & momentum are **log-scaled** (so a 10× star lead or a viral spike becomes a *tier*, not a landslide); maturity blends release cadence + age; a **staleness gate** discounts anything >60 days since last push. Freshness is *not* a weighted term — almost every claw was pushed today, so it doesn't discriminate, and health already encodes recency.

`†` = functional claw (same role, not literally named *claw*).

| # | Claw | Type | Score | ★ Stars | Health | Momentum (★/30d) | Last push | Bus factor | Lang |
|---|---|---|---|---|---|---|---|---|---|
| 🥇 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | General assistant | **0.801** | 385,469 (▲1,190) | 84 | 112,731 | 0d ago | 2 | TypeScript |
| 🥈 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) † | General assistant | **0.793** | 227,042 (▲5,921) | 85 | 37,994 | 0d ago | 3 | Python |
| 🥉 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Secure runtime | **0.737** | 22,085 (▲133) | 84 | 11,410 | 0d ago | 5 | TypeScript |
| 4 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | General assistant | **0.710** | 32,526 (▲120) | 83 | 13,899 | 0d ago | 2 | Rust |
| 5 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) † | General assistant | **0.691** | 46,749 (▲466) | 84 | 18,692 | 0d ago | 2 | Python |
| 6 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) † | Coding agent | **0.689** | 67,452 (▲807) | 78 | 20,414 | 0d ago | 1 | TypeScript |
| 7 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | General assistant | **0.676** | 29,833 (▲100) | 85 | 12,136 | 0d ago | 2 | Go |
| 8 | [elizaOS/eliza](https://github.com/elizaOS/eliza) † | General assistant | **0.674** | 18,927 (▲112) | 84 | 1,308 | 0d ago | 2 | TypeScript |
| 9 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | Secure runtime | **0.650** | 12,597 (▲32) | 80 | 5,091 | 0d ago | 2 | Rust |
| 10 | [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | Secure runtime | **0.637** | 30,468 (▲88) | 76 | 12,140 | 1d ago | 2 | TypeScript |
| 11 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | General assistant | **0.602** | 18,083 (▲19) | 71 | 3,310 | 1mo ago | 1 | Rust |
| 12 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | Coding agent | **0.600** | 195,004 (▲74) | 65 | 112,929 | 1d ago | 1 | Rust |
| 13 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | General assistant | **0.578** | 8,009 (▲95) | 77 | 2,235 | 20d ago | 1 | Zig |

**Where's Hermes?** [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent) lands **#2** (composite 0.793) — the **strongest functional claw** and it trails OpenClaw (#1). Health 85, bus factor 3 (vs OpenClaw's 2 — more resilient), 227,042★, very active.
It sits just behind [`openclaw/openclaw`](https://github.com/openclaw/openclaw), which edges it on health (84 vs 85) and resilience (bus 2 vs 3). 
The catch: Hermes carries **none** of the OpenClaw accessory ecosystem and is **Python-first** — so it's the natural pick if you'd rather extend in Python than TypeScript, or value NousResearch's lineage over ecosystem lock-in. See the dedicated **Hermes vs OpenClaw** report for the full head-to-head.

Other functional claws (†): `nanobot` #5, `oh-my-openagent` #6, `eliza` #8.

### How the top picks score (component view)

Each column is 0–1 (higher = better); the bar shows the weighted composite.

| Claw | Health | Adoption | Resilience | Maturity | Momentum | Composite |
|---|---|---|---|---|---|---|
| openclaw/openclaw | 0.84 | 1.00 | 0.40 | 0.74 | 1.00 | **0.801** |
| NousResearch/hermes-agent | 0.85 | 0.96 | 0.60 | 0.56 | 0.91 | **0.793** |
| NVIDIA/NemoClaw | 0.84 | 0.78 | 1.00 | 0.08 | 0.80 | **0.737** |
| zeroclaw-labs/zeroclaw | 0.83 | 0.81 | 0.40 | 0.65 | 0.82 | **0.710** |
| HKUDS/nanobot | 0.84 | 0.84 | 0.40 | 0.43 | 0.85 | **0.691** |

## Deeper analysis

### Is this verdict robust, or did the weights decide it?

A single weight vector is easy to rig. So here's the ranking re-run under **six different priority profiles** — from quality-obsessed to pure-hype. If a claw only wins under one contrived weighting, that's a red flag; if it wins across most, the verdict is real.

| Claw | Balanced (this report) | Equal | Quality-first | Adoption-first | Resilience-first | Hype / trajectory | Mean | Spread |
|---|---|---|---|---|---|---|---|---|
| openclaw | **1** | **1** | 2 | **1** | 3 | **1** | 1.5 | #1–#3 |
| hermes-agent † | 2 | 2 | **1** | 2 | 2 | 3 | 2.0 | #1–#3 |
| zeroclaw | 4 | 3 | 4 | 4 | 4 | 6 | 4.2 | #3–#6 |
| NemoClaw | 3 | 4 | 3 | 8 | **1** | 8 | 4.5 | #1–#8 |
| nanobot † | 5 | 6 | 6 | 5 | 6 | 5 | 5.5 | #5–#6 |
| oh-my-openagent † | 6 | 5 | 8 | 3 | 9 | 4 | 5.8 | #3–#9 |
| picoclaw | 7 | 8 | 7 | 7 | 7 | 7 | 7.2 | #7–#8 |
| eliza † | 8 | 7 | 5 | 10 | 5 | 12 | 7.8 | #5–#12 |
| ironclaw | 9 | 9 | 9 | 11 | 8 | 10 | 9.3 | #8–#11 |
| claw-code | 12 | 12 | 13 | 6 | 13 | 2 | 9.7 | #2–#13 |
| nanoclaw | 10 | 10 | 10 | 9 | 10 | 9 | 9.7 | #9–#10 |
| openfang | 11 | 11 | 11 | 12 | 11 | 11 | 11.2 | #11–#12 |
| nullclaw | 13 | 13 | 12 | 13 | 12 | 13 | 12.7 | #12–#13 |

**Read-out.**
- **`openclaw` is the robust #1** — first under 4 of 6 profiles, mean rank 1.5, never below #3. The top spot is *not* an artifact of the chosen weights.
- **Hermes is the stability champion of the top tier** — mean 2.0, range #1–#3; it never leaves the podium under any weighting. The most *weighting-proof* pick.
- **OpenClaw is polarising** — #1 under adoption/hype profiles but #3 under quality-first. It's a **scale play** (raw stars + momentum), not a **quality play** (its bus-factor-1 sinks it whenever resilience is weighted).
- **`claw-code` is the most volatile** — #2 under one profile, #13 under others. A weighting-dependent gamble, not a safe default.

### Pareto check: which claws are never the metric-optimal pick?

Ignoring fit and weights entirely: a claw is **dominated** if another claw matches or beats it on *every* generic axis (health, stars, bus factor, releases, momentum, freshness) and beats it on at least one. Dominated claws are never the answer **if you only care about generic quality/scale** — but several survive purely on a niche the axes can't see.

**Pareto-optimal (7):** `openclaw`, `hermes-agent`, `NemoClaw`, `nanoclaw`, `openfang`, `claw-code`, `nullclaw`.

**Dominated — only justified by fit, not metrics:**

| Claw | Dominated by | Survives only if you need… |
|---|---|---|
| `zeroclaw` | `openclaw` | a specific niche |
| `nanobot` | `openclaw`, `hermes-agent` | a minimal embeddable Python agent |
| `oh-my-openagent` | `openclaw` | a TS coding harness for big codebases |
| `picoclaw` | `hermes-agent` | a tiny Go edge/SBC binary |
| `eliza` | `openclaw`, `picoclaw`, `hermes-agent`, `nanobot` | autonomous social/web3 swarm bots |
| `ironclaw` | `openclaw`, `zeroclaw` | WASM-sandboxed execution of untrusted code |

> This is the **same lesson as the use-case table, proven from the other direction**: raw metrics would tell you to ignore these — but each holds a job the metrics don't measure. Dominance ≠ uselessness when the dimensions are generic.

### Graph signal: centrality, clustering & the *real* network effect

In the repo-similarity graph (1,138 nodes / 4,785 edges), the claws **don't form one cluster** — they scatter across **9 of 25 communities**. There is no single 'claw' neighbourhood; these are genuinely different projects that happen to share a role.

- **Centrality (PageRank).** Most hub-like claws: `nanobot` (0.0010), `nanoclaw` (0.0009), `openfang` (0.0009). Note PageRank tracks *similarity* connectivity, not quality — a claw is central when many neighbours resemble it.
- **Closest claw pair:** `nullclaw` ⇄ `openclaw` (w=0.38) — near-substitutes. The `zeroclaw` ⇄ `openclaw` edge confirms they compete for the same slot.
- **The honest network-effect caveat.** The similarity graph measures shared topics/authors, **not** 'plugs-into' dependency — so it does *not* by itself prove OpenClaw lock-in. The one direct graph signal that does is **`openclaw` ⇄ `clawhub` (its official skill directory) at w=0.76** — the strongest accessory tie of any claw. The broader lock-in argument below rests on real-world integration, which the graph under-counts, not over-counts.

## Where each claw shines

These claws are **not interchangeable** — they target different jobs. Use this to match a claw to *your* scenario; the score above only ranks general fitness.

| Claw | Type | Lang | Shines at | Skip if… |
|---|---|---|---|---|
| [openclaw](https://github.com/openclaw/openclaw) | General assistant | TypeScript | Your **default daily driver** — own-your-data personal assistant on any OS, with the deepest plugin/skill/router/memory ecosystem to extend in TypeScript. | you're wary of a single-maintainer core (bus 1), or you prefer Python/Rust. |
| [hermes-agent](https://github.com/NousResearch/hermes-agent) † | General assistant | Python | **Python-first builders** who want an agent that *learns/grows over time*, broad model interop, and NousResearch's research lineage. | you want TS or the OpenClaw plug-in ecosystem (it has neither). |
| [NemoClaw](https://github.com/NVIDIA/NemoClaw) | Secure runtime | TypeScript | **Enterprise GPU / managed inference** — run OpenClaw *or* Hermes more securely inside NVIDIA OpenShell. | you're not on NVIDIA infra or want a simple self-host. |
| [zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | General assistant | Rust | **Production self-host where quality matters** — 'deploy anywhere, swap anything' infra, fully autonomous, top health & resilience. The connoisseur's pick. | you depend on OpenClaw's accessory ecosystem or want a TS codebase. |
| [nanobot](https://github.com/HKUDS/nanobot) † | General assistant | Python | **Embedding a lightweight agent into your own tools/chats/workflows** — small Python surface, quick to wire in. | you want a full assistant *platform* or strong maintainer resilience (bus 2). |
| [oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) † | Coding agent | TypeScript | **Serious software engineering on big codebases** — a TUI/IDE 'pickaxe' agent harness for complex SWE and multi-tool orchestration. | you want a general life/personal assistant rather than a coding harness. |
| [picoclaw](https://github.com/sipeed/picoclaw) | General assistant | Go | **Edge / embedded / SBC** deployments — a tiny, fast, single Go binary to automate mundane tasks cheaply, anywhere. | you need a rich plugin ecosystem or heavy multi-agent orchestration. |
| [eliza](https://github.com/elizaOS/eliza) † | General assistant | TypeScript | **Always-on autonomous social agents** — Discord/Telegram/Slack bots, crypto/web3 agents, swarms, on a mature plugin framework. | you want a personal CLI/desktop assistant, not deployed autonomous bots. |
| [ironclaw](https://github.com/nearai/ironclaw) | Secure runtime | Rust | **Privacy/security-first** agent-OS — sandboxed CodeAct via WASM; good when the agent runs untrusted code and isolation matters. | you want plug-and-play or the largest community/ecosystem. |
| [nanoclaw](https://github.com/nanocoai/nanoclaw) | Secure runtime | TypeScript | **Containerized assistant with chat connectors** — WhatsApp/Telegram/Slack/Discord/Gmail, memory + scheduled jobs, on Anthropic's Agents SDK, sandboxed for safety. | you want top health or the full OpenClaw ecosystem. |
| [openfang](https://github.com/RightNow-AI/openfang) | General assistant | Rust | **MCP-native Agent-OS** — pick it if Model Context Protocol tooling is your backbone (Rust). | bus factor 1 + ~20d-stale pushes concern you, or you want TS. |
| [claw-code](https://github.com/ultraworkers/claw-code) | Coding agent | Rust | **Bleeding-edge fast coding agent** (Rust, built on oh-my-codex) — if you chase the newest and tolerate churn. | you need stability — health 58, **0 releases**, very young. Treat as experimental. |
| [nullclaw](https://github.com/nullclaw/nullclaw) | General assistant | Zig | **Absolute minimal footprint** — the fastest/smallest autonomous infra, written in Zig, for the performance-obsessed self-hoster. | you want ecosystem, plugins, or a larger community (7.6k★, bus 1). |

## The one thing the score can't measure: network effect

## Pick by what you care about

| If your priority is… | Use | Why |
|---|---|---|
| **Best on raw metrics** | [`openclaw/openclaw`](https://github.com/openclaw/openclaw) | tops the composite (health/resilience/freshness) |
| **Largest ecosystem & accessory support** | [`openclaw/openclaw`](https://github.com/openclaw/openclaw) | the hub every skill/router/memory tool you've starred targets; TS + crypto-friendly |
| **Code quality / least bus-factor risk** | [`NVIDIA/NemoClaw`](https://github.com/NVIDIA/NemoClaw) | highest bus factor (5) — most resilient to a maintainer leaving |
| **Best health score** | [`sipeed/picoclaw`](https://github.com/sipeed/picoclaw) | health 85 — cleanest maintenance signals |
| **Fastest-growing right now** | [`ultraworkers/claw-code`](https://github.com/ultraworkers/claw-code) | ~112,929 est. stars/30d |
| **Security / sandboxed execution** | [`NVIDIA/NemoClaw`](https://github.com/NVIDIA/NemoClaw) | hardened/containerized runtime |
| **Coding agent** | [`code-yeongyu/oh-my-openagent`](https://github.com/code-yeongyu/oh-my-openagent) | purpose-built for code |
| **Tiny / edge / self-host cheap** | `sipeed/picoclaw` · `nullclaw/nullclaw` | minimal footprints (Go / Zig) |
| **Most-adopted / most battle-tested** | [`openclaw/openclaw`](https://github.com/openclaw/openclaw) | 385,469★ |

## Watch-outs

- **code-yeongyu/oh-my-openagent** — bus factor 1 (single-maintainer risk).
- **RightNow-AI/openfang** — bus factor 1 (single-maintainer risk).
- **ultraworkers/claw-code** — bus factor 1 (single-maintainer risk).
- **nullclaw/nullclaw** — bus factor 1 (single-maintainer risk).

> Heads-up: `openagen/zeroclaw` (1.9k★, ~79d stale) is an **older, different** project from the healthy **`zeroclaw-labs/zeroclaw`** ranked above — don't confuse them.

## Methodology & caveats

- **Source:** `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Candidate set:** standalone claw agents/runtimes/agent-OSes only. Accessories (skills, routers, memory, observability, dashboards, specialized one-task agents) are excluded by design — see the OpenClaw Ecosystem report for those.
- **Composite weights:** health 25%, adoption 25%, resilience 20%, maturity 15%, momentum 15%. Adoption & momentum are log-scaled; maturity = 60% release-cadence + 40% age (age capped at 730d). A staleness gate multiplies the score down (floor 0.6) beyond 60 days since last push. Freshness is deliberately *not* a weighted term (saturated; redundant with health).
- **Why these weights:** this is an *adoption* decision, so battle-testing (adoption) and survivability (resilience, maturity) are weighted as heavily as raw health, and hype (momentum) is capped at 15% and log-scaled — a 2-month-old repo riding a star spike shouldn't outrank a seasoned, multi-maintainer project.
- **Snapshot-bound.** Claws move weekly; momentum especially can flip fast. Re-run after a fresh `npm run refresh`.

<sub>Claws ranked: 13 · Snapshot: 2026-08-07T21:10:17.796Z · regenerate via scripts/reports/which_claw.py</sub>
