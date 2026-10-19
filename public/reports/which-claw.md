# Which Claw Should I Use? — A Decision Report

> Derived from **kaiser-data**'s 2,398 starred repos (snapshot `2026-10-19T11:27:31.266Z`), cross-referenced with the repo-similarity graph.
>
> Generated 2026-10-19 by `scripts/reports/which_claw.py` (regenerate any time — no API cost).

![Top tools by stars](assets/which-claw-top-tools.svg)

![Tools per category](assets/which-claw-categories.svg)


> **Scope.** This ranks the standalone **claws** — agents/runtimes you'd run *as* your assistant. "Claw" here is a **role, not a name**: functional claws that aren't literally branded *claw* (Hermes, nanobot, eliza, oh-my-openagent) are ranked alongside the named ones and tagged **†**. The accessory ecosystem (skills, routers, memory, observability, dashboards) is covered separately in the **OpenClaw Ecosystem** report; those *complement* a claw rather than replace it.

## TL;DR — two honest answers

**On raw metrics, [`zeroclaw-labs/zeroclaw`](https://github.com/zeroclaw-labs/zeroclaw) wins** (composite 0.841): health 88, bus factor 3, very active. And it's **robust** — it stays #1 under 4 of 6 weighting profiles (see the sensitivity analysis), so that's not an artifact of how I weighted the score. If you want the cleanest, most resilient standalone claw and don't care about the surrounding tooling, take it.

**As a pragmatic default, [`openclaw/openclaw`](https://github.com/openclaw/openclaw) (composite 0.777, #2).** The score above *deliberately excludes the ecosystem network effect* — and that's OpenClaw's real edge: every accessory you've already starred (`clawhub`, `ClawRouter`, `clawmetry`, `opik-openclaw`, `openclaw-supermemory`, `NemoClaw`, `moltworker`) targets OpenClaw, not zeroclaw. That's a genuine switching cost in its favour.

- **TypeScript + crypto fit → OpenClaw.** It's TS (so is most of its accessory line), and the ecosystem leans on-chain — e.g. `ClawRouter` does on-chain payments / agent-native settlement. If you live in the TS and crypto world, that's another argument for the hub.
- **Maximum stability/quality →** [`zeroclaw-labs/zeroclaw`](https://github.com/zeroclaw-labs/zeroclaw) (health 88).
- **Running untrusted tools / need isolation →** [`nearai/ironclaw`](https://github.com/nearai/ironclaw) — security-hardened runtime.
- **Mostly coding →** [`ultraworkers/claw-code`](https://github.com/ultraworkers/claw-code) is the coding-focused claw.
- **Tiny/edge footprint →** `sipeed/picoclaw` and `nullclaw/nullclaw` (minimal builds).

## The ranking

Composite = 25% health + 25% adoption + 20% resilience + 15% maturity + 15% momentum. Adoption & momentum are **log-scaled** (so a 10× star lead or a viral spike becomes a *tier*, not a landslide); maturity blends release cadence + age; a **staleness gate** discounts anything >60 days since last push. Freshness is *not* a weighted term — almost every claw was pushed today, so it doesn't discriminate, and health already encodes recency.

`†` = functional claw (same role, not literally named *claw*).

| # | Claw | Type | Score | ★ Stars | Health | Momentum (★/30d) | Last push | Bus factor | Lang |
|---|---|---|---|---|---|---|---|---|---|
| 🥇 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | General assistant | **0.841** | 32,998 (▲49) | 88 | 9,975 | 0d ago | 3 | Rust |
| 🥈 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | General assistant | **0.777** | 392,443 (▲862) | 79 | 89,449 | 0d ago | 1 | TypeScript |
| 🥉 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | Coding agent | **0.761** | 194,908 (▼74) | 80 | 72,330 | 0d ago | 2 | Rust |
| 4 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) † | General assistant | **0.747** | 49,173 (▲249) | 84 | 14,175 | 0d ago | 2 | Python |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) † | General assistant | **0.729** | 255,102 (▲2,649) | 75 | 35,857 | 0d ago | 1 | Python |
| 6 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) † | Coding agent | **0.722** | 70,181 (▲244) | 78 | 16,428 | 0d ago | 1 | TypeScript |
| 7 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | Secure runtime | **0.706** | 12,663 (▲16) | 80 | 3,678 | 1d ago | 2 | Rust |
| 8 | [elizaOS/eliza](https://github.com/elizaOS/eliza) † | General assistant | **0.657** | 19,622 (▲56) | 80 | 1,238 | 0d ago | 1 | TypeScript |
| 9 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Secure runtime | **0.652** | 22,768 (▲70) | 71 | 7,841 | 0d ago | 2 | TypeScript |
| 10 | [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | Secure runtime | **0.639** | 30,969 (▲58) | 77 | 8,905 | 0d ago | 1 | TypeScript |
| 11 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | General assistant | **0.609** | 30,085 (▲67) | 63 | 8,781 | 4d ago | 1 | Go |
| 12 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | General assistant | **0.592** | 8,131 (▲20) | 72 | 1,596 | 11d ago | 1 | Zig |
| 13 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | General assistant | **0.385** | 18,210 (▼7) | 45 | 924 | 3mo ago | 0 | Rust |

**Where's Hermes?** [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent) lands **#5** (composite 0.729) — the **strongest functional claw** and it trails OpenClaw (#2). Health 75, bus factor 1 (vs OpenClaw's 1 — more resilient), 255,102★, very active.
It sits just behind [`HKUDS/nanobot`](https://github.com/HKUDS/nanobot), which edges it on health (84 vs 75) and resilience (bus 2 vs 1). 
The catch: Hermes carries **none** of the OpenClaw accessory ecosystem and is **Python-first** — so it's the natural pick if you'd rather extend in Python than TypeScript, or value NousResearch's lineage over ecosystem lock-in. See the dedicated **Hermes vs OpenClaw** report for the full head-to-head.

Other functional claws (†): `nanobot` #4, `oh-my-openagent` #6, `eliza` #8.

### How the top picks score (component view)

Each column is 0–1 (higher = better); the bar shows the weighted composite.

| Claw | Health | Adoption | Resilience | Maturity | Momentum | Composite |
|---|---|---|---|---|---|---|
| zeroclaw-labs/zeroclaw | 0.88 | 0.81 | 1.00 | 0.65 | 0.81 | **0.841** |
| openclaw/openclaw | 0.79 | 1.00 | 0.33 | 0.75 | 1.00 | **0.777** |
| ultraworkers/claw-code | 0.80 | 0.95 | 0.67 | 0.29 | 0.98 | **0.761** |
| HKUDS/nanobot | 0.84 | 0.84 | 0.67 | 0.46 | 0.84 | **0.747** |
| NousResearch/hermes-agent | 0.75 | 0.97 | 0.33 | 0.63 | 0.92 | **0.729** |

## Deeper analysis

### Is this verdict robust, or did the weights decide it?

A single weight vector is easy to rig. So here's the ranking re-run under **six different priority profiles** — from quality-obsessed to pure-hype. If a claw only wins under one contrived weighting, that's a red flag; if it wins across most, the verdict is real.

| Claw | Balanced (this report) | Equal | Quality-first | Adoption-first | Resilience-first | Hype / trajectory | Mean | Spread |
|---|---|---|---|---|---|---|---|---|
| zeroclaw | **1** | **1** | **1** | 4 | **1** | 6 | 2.3 | #1–#6 |
| openclaw | 2 | 2 | 4 | **1** | 5 | **1** | 2.5 | #1–#5 |
| claw-code | 3 | 3 | 5 | 3 | 4 | 2 | 3.3 | #2–#5 |
| nanobot † | 4 | 4 | 2 | 6 | 2 | 5 | 3.8 | #2–#6 |
| hermes-agent † | 5 | 6 | 7 | 2 | 8 | 3 | 5.2 | #2–#8 |
| oh-my-openagent † | 6 | 5 | 6 | 5 | 6 | 4 | 5.3 | #4–#6 |
| ironclaw | 7 | 7 | 3 | 8 | 3 | 10 | 6.3 | #3–#10 |
| NemoClaw | 9 | 9 | 9 | 11 | 7 | 8 | 8.8 | #7–#11 |
| eliza † | 8 | 8 | 8 | 9 | 9 | 11 | 8.8 | #8–#11 |
| nanoclaw | 10 | 10 | 10 | 7 | 10 | 7 | 9.0 | #7–#10 |
| picoclaw | 11 | 11 | 12 | 10 | 12 | 9 | 10.8 | #9–#12 |
| nullclaw | 12 | 12 | 11 | 12 | 11 | 12 | 11.7 | #11–#12 |
| openfang | 13 | 13 | 13 | 13 | 13 | 13 | 13.0 | #13–#13 |

**Read-out.**
- **`zeroclaw` is the robust #1** — first under 4 of 6 profiles, mean rank 2.3, never below #6. The top spot is *not* an artifact of the chosen weights.
- **Hermes is the stability champion of the top tier** — mean 5.2, range #2–#8; it never leaves the podium under any weighting. The most *weighting-proof* pick.
- **OpenClaw is polarising** — #1 under adoption/hype profiles but #5 under quality-first. It's a **scale play** (raw stars + momentum), not a **quality play** (its bus-factor-1 sinks it whenever resilience is weighted).
- **`ironclaw` is the most volatile** — #3 under one profile, #10 under others. A weighting-dependent gamble, not a safe default.

### Pareto check: which claws are never the metric-optimal pick?

Ignoring fit and weights entirely: a claw is **dominated** if another claw matches or beats it on *every* generic axis (health, stars, bus factor, releases, momentum, freshness) and beats it on at least one. Dominated claws are never the answer **if you only care about generic quality/scale** — but several survive purely on a niche the axes can't see.

**Pareto-optimal (8):** `zeroclaw`, `openclaw`, `claw-code`, `nanobot`, `oh-my-openagent`, `ironclaw`, `picoclaw`, `openfang`.

**Dominated — only justified by fit, not metrics:**

| Claw | Dominated by | Survives only if you need… |
|---|---|---|
| `hermes-agent` | `openclaw` | a specific niche |
| `eliza` | `zeroclaw`, `nanobot` | autonomous social/web3 swarm bots |
| `NemoClaw` | `claw-code`, `zeroclaw`, `nanobot` | managed inference on NVIDIA infra |
| `nanoclaw` | `openclaw`, `zeroclaw`, `nanobot`, `oh-my-openagent` | containerised chat-app connectors |
| `nullclaw` | `ironclaw` | the absolute smallest (Zig) footprint |

> This is the **same lesson as the use-case table, proven from the other direction**: raw metrics would tell you to ignore these — but each holds a job the metrics don't measure. Dominance ≠ uselessness when the dimensions are generic.

### Graph signal: centrality, clustering & the *real* network effect

In the repo-similarity graph (1,138 nodes / 8,025 edges), the claws **don't form one cluster** — they scatter across **8 of 25 communities**. There is no single 'claw' neighbourhood; these are genuinely different projects that happen to share a role.

- **Centrality (PageRank).** Most hub-like claws: `hermes-agent` (0.0007), `nanobot` (0.0006), `openclaw` (0.0006). Note PageRank tracks *similarity* connectivity, not quality — a claw is central when many neighbours resemble it.
- **Closest claw pair:** `nullclaw` ⇄ `openclaw` (w=0.38) — near-substitutes. The `zeroclaw` ⇄ `openclaw` edge confirms they compete for the same slot.
- **The honest network-effect caveat.** The similarity graph measures shared topics/authors, **not** 'plugs-into' dependency — so it does *not* by itself prove OpenClaw lock-in. The one direct graph signal that does is **`openclaw` ⇄ `clawhub` (its official skill directory) at w=1.35** — the strongest accessory tie of any claw. The broader lock-in argument below rests on real-world integration, which the graph under-counts, not over-counts.

## Where each claw shines

These claws are **not interchangeable** — they target different jobs. Use this to match a claw to *your* scenario; the score above only ranks general fitness.

| Claw | Type | Lang | Shines at | Skip if… |
|---|---|---|---|---|
| [zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | General assistant | Rust | **Production self-host where quality matters** — 'deploy anywhere, swap anything' infra, fully autonomous, top health & resilience. The connoisseur's pick. | you depend on OpenClaw's accessory ecosystem or want a TS codebase. |
| [openclaw](https://github.com/openclaw/openclaw) | General assistant | TypeScript | Your **default daily driver** — own-your-data personal assistant on any OS, with the deepest plugin/skill/router/memory ecosystem to extend in TypeScript. | you're wary of a single-maintainer core (bus 1), or you prefer Python/Rust. |
| [claw-code](https://github.com/ultraworkers/claw-code) | Coding agent | Rust | **Bleeding-edge fast coding agent** (Rust, built on oh-my-codex) — if you chase the newest and tolerate churn. | you need stability — health 58, **0 releases**, very young. Treat as experimental. |
| [nanobot](https://github.com/HKUDS/nanobot) † | General assistant | Python | **Embedding a lightweight agent into your own tools/chats/workflows** — small Python surface, quick to wire in. | you want a full assistant *platform* or strong maintainer resilience (bus 2). |
| [hermes-agent](https://github.com/NousResearch/hermes-agent) † | General assistant | Python | **Python-first builders** who want an agent that *learns/grows over time*, broad model interop, and NousResearch's research lineage. | you want TS or the OpenClaw plug-in ecosystem (it has neither). |
| [oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) † | Coding agent | TypeScript | **Serious software engineering on big codebases** — a TUI/IDE 'pickaxe' agent harness for complex SWE and multi-tool orchestration. | you want a general life/personal assistant rather than a coding harness. |
| [ironclaw](https://github.com/nearai/ironclaw) | Secure runtime | Rust | **Privacy/security-first** agent-OS — sandboxed CodeAct via WASM; good when the agent runs untrusted code and isolation matters. | you want plug-and-play or the largest community/ecosystem. |
| [eliza](https://github.com/elizaOS/eliza) † | General assistant | TypeScript | **Always-on autonomous social agents** — Discord/Telegram/Slack bots, crypto/web3 agents, swarms, on a mature plugin framework. | you want a personal CLI/desktop assistant, not deployed autonomous bots. |
| [NemoClaw](https://github.com/NVIDIA/NemoClaw) | Secure runtime | TypeScript | **Enterprise GPU / managed inference** — run OpenClaw *or* Hermes more securely inside NVIDIA OpenShell. | you're not on NVIDIA infra or want a simple self-host. |
| [nanoclaw](https://github.com/nanocoai/nanoclaw) | Secure runtime | TypeScript | **Containerized assistant with chat connectors** — WhatsApp/Telegram/Slack/Discord/Gmail, memory + scheduled jobs, on Anthropic's Agents SDK, sandboxed for safety. | you want top health or the full OpenClaw ecosystem. |
| [picoclaw](https://github.com/sipeed/picoclaw) | General assistant | Go | **Edge / embedded / SBC** deployments — a tiny, fast, single Go binary to automate mundane tasks cheaply, anywhere. | you need a rich plugin ecosystem or heavy multi-agent orchestration. |
| [nullclaw](https://github.com/nullclaw/nullclaw) | General assistant | Zig | **Absolute minimal footprint** — the fastest/smallest autonomous infra, written in Zig, for the performance-obsessed self-hoster. | you want ecosystem, plugins, or a larger community (7.6k★, bus 1). |
| [openfang](https://github.com/RightNow-AI/openfang) | General assistant | Rust | **MCP-native Agent-OS** — pick it if Model Context Protocol tooling is your backbone (Rust). | bus factor 1 + ~20d-stale pushes concern you, or you want TS. |

## The one thing the score can't measure: network effect

`zeroclaw-labs/zeroclaw` edges out `openclaw/openclaw` on the composite mostly on **health (88 vs 79)** and **bus factor (3 vs 1)** — both real, both in zeroclaw's favour. But the composite scores each claw *in isolation*. It can't see that:

- Your starred ecosystem is built **around OpenClaw** — `clawhub` (skills, the strongest single graph edge at w=1.35), `ClawRouter` (routing, on-chain payments), `clawmetry` / `opik-openclaw` (observability), `openclaw-supermemory` (memory), `NemoClaw` / `moltworker` (hosting). None of that plugs into zeroclaw out of the box. (The graph under-counts this — it sees topic/author similarity, not 'plugs-into' integration — so treat the real lock-in as *stronger* than the edges suggest.)
- OpenClaw is **TypeScript** end-to-end, which matches the rest of that tooling — and the crypto/on-chain bent of the ecosystem (agent-native settlement) is a plus if that's your world.
- zeroclaw is **Rust**: leaner and (per the metrics) cleaner, but you'd be re-building or forgoing the accessory layer.

**Net:** pick `zeroclaw-labs/zeroclaw` if you want a single, self-contained, high-quality claw. Pick `openclaw/openclaw` if you want a *platform* — the ecosystem lock-in is the feature, not the bug.

## Pick by what you care about

| If your priority is… | Use | Why |
|---|---|---|
| **Best on raw metrics** | [`zeroclaw-labs/zeroclaw`](https://github.com/zeroclaw-labs/zeroclaw) | tops the composite (health/resilience/freshness) |
| **Largest ecosystem & accessory support** | [`openclaw/openclaw`](https://github.com/openclaw/openclaw) | the hub every skill/router/memory tool you've starred targets; TS + crypto-friendly |
| **Code quality / least bus-factor risk** | [`zeroclaw-labs/zeroclaw`](https://github.com/zeroclaw-labs/zeroclaw) | highest bus factor (3) — most resilient to a maintainer leaving |
| **Best health score** | [`zeroclaw-labs/zeroclaw`](https://github.com/zeroclaw-labs/zeroclaw) | health 88 — cleanest maintenance signals |
| **Fastest-growing right now** | [`openclaw/openclaw`](https://github.com/openclaw/openclaw) | ~89,449 est. stars/30d |
| **Security / sandboxed execution** | [`nearai/ironclaw`](https://github.com/nearai/ironclaw) | hardened/containerized runtime |
| **Coding agent** | [`ultraworkers/claw-code`](https://github.com/ultraworkers/claw-code) | purpose-built for code |
| **Tiny / edge / self-host cheap** | `sipeed/picoclaw` · `nullclaw/nullclaw` | minimal footprints (Go / Zig) |
| **Most-adopted / most battle-tested** | [`openclaw/openclaw`](https://github.com/openclaw/openclaw) | 392,443★ |

## Watch-outs

- **openclaw/openclaw** — bus factor 1 (single-maintainer risk).
- **NousResearch/hermes-agent** — bus factor 1 (single-maintainer risk).
- **code-yeongyu/oh-my-openagent** — bus factor 1 (single-maintainer risk).
- **elizaOS/eliza** — bus factor 1 (single-maintainer risk).
- **nanocoai/nanoclaw** — bus factor 1 (single-maintainer risk).
- **sipeed/picoclaw** — bus factor 1 (single-maintainer risk).
- **nullclaw/nullclaw** — bus factor 1 (single-maintainer risk).
- **RightNow-AI/openfang** — health 45; 109d since last push; bus factor 0 (single-maintainer risk).

> Heads-up: `openagen/zeroclaw` (1.9k★, ~79d stale) is an **older, different** project from the healthy **`zeroclaw-labs/zeroclaw`** ranked above — don't confuse them.

## Methodology & caveats

- **Source:** `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Candidate set:** standalone claw agents/runtimes/agent-OSes only. Accessories (skills, routers, memory, observability, dashboards, specialized one-task agents) are excluded by design — see the OpenClaw Ecosystem report for those.
- **Composite weights:** health 25%, adoption 25%, resilience 20%, maturity 15%, momentum 15%. Adoption & momentum are log-scaled; maturity = 60% release-cadence + 40% age (age capped at 730d). A staleness gate multiplies the score down (floor 0.6) beyond 60 days since last push. Freshness is deliberately *not* a weighted term (saturated; redundant with health).
- **Why these weights:** this is an *adoption* decision, so battle-testing (adoption) and survivability (resilience, maturity) are weighted as heavily as raw health, and hype (momentum) is capped at 15% and log-scaled — a 2-month-old repo riding a star spike shouldn't outrank a seasoned, multi-maintainer project.
- **Snapshot-bound.** Claws move weekly; momentum especially can flip fast. Re-run after a fresh `npm run refresh`.

<sub>Claws ranked: 13 · Snapshot: 2026-10-19T11:27:31.266Z · regenerate via scripts/reports/which_claw.py</sub>
