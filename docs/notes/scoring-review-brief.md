# Scoring review request

You are an independent reviewer. Do not edit files. Do not agree by default.
Review the convenience scoring below for the job:

**Job:** a named autonomous 24/7 org assistant on a generic Linux VPS
(systemd or Docker, messaging channels stay up after SSH logout, secrets on disk).

**Out of scope for the score:** migration/rewrite cost from OpenClaw to Hermes
or anyone else. Score the runtime as if you were choosing a 24/7 VPS claw on
product merit.

**Formula now:** Total = 0.50 × Job fit + 0.50 × VPS ops. Each axis 0–10.

**Job fit 10:** named 24/7 assistant with channels, memory, a daemon — not a
coding TUI, not a swarm-only framework.

**VPS ops 10:** official systemd/Docker path, headless docs, sane loopback
defaults, RAM you can rent cheaply.

## Current scores

| Rank | Claw | Fit | Ops | Total | Author rationale |
|---|---|---|---|---|---|
| 1 | OpenClaw 2.0 (TS, Node) | 10 | 8 | 9.0 | Full assistant + first-class VPS docs (Hetzner Docker, Ansible+Tailscale, loopback). Ding: Node, ≥6 GB for source builds. |
| 2 | ZeroClaw (Rust) | 8 | 10 | 9.0 | `zeroclaw service install`, distroless GHCR, docs name VPS as system-scope. Thinner skill/channel graph. Docker sample binds public — ding if shipped as-is. |
| 3 | Hermes Agent (Python) | 9 | 8 | 8.5 | Same job as OpenClaw: gateway, channels, memory, skills, linger. Install one curl. Ops ding matches OpenClaw (Python+Node, not a 4 MB binary). |
| 4 | PicoClaw (Go) | 6 | 9 | 7.5 | One binary, easy systemd. Too thin for treasury-grade assistant. |
| 5 | NanoClaw (TS, Anthropic SDK) | 7 | 6 | 6.5 | Per-agent Docker isolation. 4 GB floor, linger, Claude-tied. |
| 6 | IronClaw (Rust, WASM) | 6 | 7 | 6.5 | Installer + systemd. Convenient when untrusted tool code is the point. |
| 7 | ElizaOS (TS) | 5 | 6 | 5.5 | Docker/Coolify/PM2 documented. Public social/web3 bots, not a finance operator agent. |
| 8 | Nanobot (Python) | 4 | 5 | 4.5 | pip/uv easy; you write the daemon. Library, not the org identity. |

Tie-break: OpenClaw #1 over ZeroClaw on job fit despite equal totals.

Excluded from ranking: NemoClaw (NVIDIA OpenShell), coding harnesses
(oh-my-openagent, claw-code), stale claws (openfang, nullclaw), Moltworker
(Cloudflare), Claude Cowork, ChatGPT Work (vendor clouds, not a VPS process).

## What to return

Write a review with these sections only:

1. **Verdict** — accept, revise, or reject the ranking.
2. **Score-by-score** — for each of the 8, say keep / bump / drop and by how
   much (integer or .5). Give one sentence of evidence. If you lack evidence,
   say so; do not invent docs.
3. **Formula** — is 50/50 fit+ops the right convenience model? Propose a
   better one only if you would actually use it.
4. **Blind spots** — missing axes (security defaults, RAM reality, channel
   reliability, updater pain, bus factor).
5. **Revised table** — your own Fit / Ops / Total if you disagree.

Be specific. Challenge OpenClaw Fit=10, ZeroClaw Ops=10, Hermes Fit=9 vs
OpenClaw Fit=10, PicoClaw Fit=6, NanoClaw Ops=6. Do not rubber-stamp.
