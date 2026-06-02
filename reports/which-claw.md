# Which Claw Should I Use? — A Decision Report

> Derived from **kaiser-data**'s 1,138 starred repos (snapshot `2026-06-02T21:59:05.644Z`), cross-referenced with the repo-similarity graph.
>
> Generated 2026-06-02 by `scripts/reports/which_claw.py` (regenerate any time — no API cost).

> **Scope.** This ranks the standalone **claws** — agents/runtimes you'd run *as* your assistant. The accessory ecosystem (skills, routers, memory, observability, dashboards) is covered separately in the **OpenClaw Ecosystem** report; those *complement* a claw rather than replace it.

## TL;DR — two honest answers

**On raw metrics, [`zeroclaw-labs/zeroclaw`](https://github.com/zeroclaw-labs/zeroclaw) wins** (composite 0.784): health 98, bus factor 5, very active. If you want the cleanest, most resilient standalone claw and don't care about the surrounding tooling, take it.

**As a pragmatic default, [`openclaw/openclaw`](https://github.com/openclaw/openclaw) (composite 0.747, #2).** The score above *deliberately excludes the ecosystem network effect* — and that's OpenClaw's real edge: every accessory you've already starred (`clawhub`, `ClawRouter`, `clawmetry`, `opik-openclaw`, `openclaw-supermemory`, `NemoClaw`, `moltworker`) targets OpenClaw, not zeroclaw. That's a genuine switching cost in its favour.

- **TypeScript + crypto fit → OpenClaw.** It's TS (so is most of its accessory line), and the ecosystem leans on-chain — e.g. `ClawRouter` does on-chain payments / agent-native settlement. If you live in the TS and crypto world, that's another argument for the hub.
- **Maximum stability/quality →** [`zeroclaw-labs/zeroclaw`](https://github.com/zeroclaw-labs/zeroclaw) (health 98).
- **Running untrusted tools / need isolation →** [`NVIDIA/NemoClaw`](https://github.com/NVIDIA/NemoClaw) — security-hardened runtime.
- **Mostly coding →** [`ultraworkers/claw-code`](https://github.com/ultraworkers/claw-code) is the coding-focused claw.
- **Tiny/edge footprint →** `sipeed/picoclaw` and `nullclaw/nullclaw` (minimal builds).

## The ranking

Composite = 30% health + 20% freshness + 20% momentum + 15% busfactor + 15% adoption. All inputs are precomputed dataset metrics; adoption is log-scaled so a 10× star lead doesn't swamp everything else.

| # | Claw | Type | Score | ★ Stars | Health | Momentum (★/30d) | Last push | Bus factor | Lang |
|---|---|---|---|---|---|---|---|---|---|
| 🥇 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | General assistant | **0.784** | 31,707 | 98 | 21,708 | 0d ago | 5 | Rust |
| 🥈 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | General assistant | **0.747** | 376,269 | 79 | 148,147 | 0d ago | 1 | TypeScript |
| 🥉 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | Coding agent | **0.738** | 193,162 | 58 | 227,992 | 5d ago | 1 | Rust |
| 4 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | General assistant | **0.696** | 29,267 | 90 | 18,540 | 0d ago | 3 | Go |
| 5 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Secure runtime | **0.642** | 20,834 | 73 | 19,728 | 0d ago | 3 | TypeScript |
| 6 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | Secure runtime | **0.614** | 12,393 | 79 | 7,770 | 0d ago | 2 | Rust |
| 7 | [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | Secure runtime | **0.603** | 29,644 | 70 | 18,185 | 2d ago | 2 | TypeScript |
| 8 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | General assistant | **0.567** | 7,653 | 78 | 5,413 | 4d ago | 1 | Zig |
| 9 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | General assistant | **0.553** | 17,706 | 78 | 8,677 | 20d ago | 1 | Rust |

### How the top picks score (component view)

Each column is 0–1 (higher = better); the bar shows the weighted composite.

| Claw | Health | Fresh | Momentum | Bus | Adoption | Composite |
|---|---|---|---|---|---|---|
| zeroclaw-labs/zeroclaw | 0.98 | 1.00 | 0.10 | 1.00 | 0.81 | **0.784** |
| openclaw/openclaw | 0.79 | 1.00 | 0.65 | 0.20 | 1.00 | **0.747** |
| ultraworkers/claw-code | 0.58 | 0.96 | 1.00 | 0.20 | 0.95 | **0.738** |
| sipeed/picoclaw | 0.90 | 1.00 | 0.08 | 0.60 | 0.80 | **0.696** |
| NVIDIA/NemoClaw | 0.73 | 1.00 | 0.09 | 0.60 | 0.77 | **0.642** |

## The one thing the score can't measure: network effect

`zeroclaw-labs/zeroclaw` edges out `openclaw/openclaw` on the composite mostly on **health (98 vs 79)** and **bus factor (5 vs 1)** — both real, both in zeroclaw's favour. But the composite scores each claw *in isolation*. It can't see that:

- Your starred ecosystem is built **around OpenClaw** — `clawhub` (skills), `ClawRouter` (routing, on-chain payments), `clawmetry` / `opik-openclaw` (observability), `openclaw-supermemory` (memory), `NemoClaw` / `moltworker` (hosting). None of that plugs into zeroclaw out of the box.
- OpenClaw is **TypeScript** end-to-end, which matches the rest of that tooling — and the crypto/on-chain bent of the ecosystem (agent-native settlement) is a plus if that's your world.
- zeroclaw is **Rust**: leaner and (per the metrics) cleaner, but you'd be re-building or forgoing the accessory layer.

**Net:** pick `zeroclaw-labs/zeroclaw` if you want a single, self-contained, high-quality claw. Pick `openclaw/openclaw` if you want a *platform* — the ecosystem lock-in is the feature, not the bug.

## Pick by what you care about

| If your priority is… | Use | Why |
|---|---|---|
| **Best on raw metrics** | [`zeroclaw-labs/zeroclaw`](https://github.com/zeroclaw-labs/zeroclaw) | tops the composite (health/resilience/freshness) |
| **Largest ecosystem & accessory support** | [`openclaw/openclaw`](https://github.com/openclaw/openclaw) | the hub every skill/router/memory tool you've starred targets; TS + crypto-friendly |
| **Code quality / least bus-factor risk** | [`zeroclaw-labs/zeroclaw`](https://github.com/zeroclaw-labs/zeroclaw) | highest bus factor (5) — most resilient to a maintainer leaving |
| **Best health score** | [`zeroclaw-labs/zeroclaw`](https://github.com/zeroclaw-labs/zeroclaw) | health 98 — cleanest maintenance signals |
| **Fastest-growing right now** | [`ultraworkers/claw-code`](https://github.com/ultraworkers/claw-code) | ~227,992 est. stars/30d |
| **Security / sandboxed execution** | [`NVIDIA/NemoClaw`](https://github.com/NVIDIA/NemoClaw) | hardened/containerized runtime |
| **Coding agent** | [`ultraworkers/claw-code`](https://github.com/ultraworkers/claw-code) | purpose-built for code |
| **Tiny / edge / self-host cheap** | `sipeed/picoclaw` · `nullclaw/nullclaw` | minimal footprints (Go / Zig) |
| **Most-adopted / most battle-tested** | [`openclaw/openclaw`](https://github.com/openclaw/openclaw) | 376,269★ |

## Watch-outs

- **openclaw/openclaw** — bus factor 1 (single-maintainer risk).
- **ultraworkers/claw-code** — health 58; bus factor 1 (single-maintainer risk).
- **nullclaw/nullclaw** — bus factor 1 (single-maintainer risk).
- **RightNow-AI/openfang** — bus factor 1 (single-maintainer risk).

> Heads-up: `openagen/zeroclaw` (1.9k★, ~79d stale) is an **older, different** project from the healthy **`zeroclaw-labs/zeroclaw`** ranked above — don't confuse them.

## Methodology & caveats

- **Source:** `public/data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Candidate set:** standalone claw agents/runtimes/agent-OSes only. Accessories (skills, routers, memory, observability, dashboards, specialized one-task agents) are excluded by design — see the OpenClaw Ecosystem report for those.
- **Composite weights:** health 30%, freshness 20%, momentum 20%, busfactor 15%, adoption 15%. Adoption is log-scaled. Freshness decays linearly to ~0 by 120 days since last push.
- **Snapshot-bound.** Claws move weekly; momentum especially can flip fast. Re-run after a fresh `npm run refresh`.

<sub>Claws ranked: 9 · Snapshot: 2026-06-02T21:59:05.644Z · regenerate via scripts/reports/which_claw.py</sub>
