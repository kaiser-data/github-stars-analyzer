# Scoring review: 24/7 VPS claw convenience ranking (Codex, gpt-6-astra)

Second independent review, run 2026-09-21 after the 09-19 attempt hit a usage
limit. Unlike the Claude review, this reviewer had web access and cites the
docs it checked.

## 1. Verdict

**Revise.** The ranking overvalues implementation language, mixes build requirements with runtime requirements, and understates several products’ assistant capabilities. “Treasury-grade” and “finance operator” also introduce requirements absent from the stated job.

**OpenClaw Fit=10 is defensible only under your narrow definition of 10:** it matches the product category, not proven flawless autonomy or organizational governance. Under that definition, Hermes deserves the same score. I found no evidence supporting an exclusive OpenClaw lead.

These are provisional assessments of current official documentation and selected source files, **not uptime or RAM benchmarks**. Pin releases before treating this as a reproducible ranking.

## 2. Score-by-score

- **OpenClaw — keep Fit 10; bump Ops 8→8.5 (+0.5).** Its official VPS guide explicitly supports a shared company agent within one trust boundary and recommends loopback access; the Docker documentation identifies 6 GB as a **local source-build** requirement avoided by prebuilt images. ([VPS guide](https://docs.openclaw.ai/vps), [Docker](https://docs.openclaw.ai/install/docker))  
  The 10 does not establish separation between mutually untrusted colleagues, and “Node” alone is not an operational defect.

- **ZeroClaw — bump Fit 8→9 (+1); drop Ops 10→8 (−2).** Official documentation describes channels, memory, cron and resumable procedures, but its minimum Docker example publishes the gateway on all host interfaces with pairing disabled, including unauthenticated configuration and memory endpoints. ([Capabilities](https://github.com/zeroclaw-labs/zeroclaw), [Container defaults](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/setup/container.md))  
  This directly contradicts your Ops=10 criterion; the separately documented loopback Compose configuration mitigates it.

- **Hermes — bump Fit 9→10 (+1); bump Ops 8→8.5 (+0.5).** It documents persistent memory, personality, unattended scheduling and messaging, plus systemd user/system services and Docker requirements of 1 GB minimum, with more recommended for browser work. ([Capabilities](https://github.com/NousResearch/hermes-agent), [Services](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/), [Docker](https://hermes-agent.nousresearch.com/docs/user-guide/docker))  
  Neither Python+Node nor having a TUI establishes a disadvantage for this job.

- **PicoClaw — bump Fit 6→8.5 (+2.5); drop Ops 9→8 (−1).** Its documentation includes persistent memory, scheduling, numerous messaging channels and Docker Compose, while explicitly warning against production deployment before v1.0. ([Official README](https://github.com/sipeed/picoclaw))  
  “Too thin for treasury” does not justify Fit=6; the project’s own readiness warning does justify withholding a near-perfect operations score.

- **NanoClaw — bump Fit 7→9 (+2); bump Ops 6→7 (+1).** It documents named assistants, per-agent memory and scheduled tasks, ships systemd setup with restart and linger handling, and specifies a 4 GB machine requirement. ([Capabilities](https://github.com/nanocoai/nanoclaw), [Service implementation](https://github.com/nanocoai/nanoclaw/blob/main/setup/service.ts), [Requirements](https://docs.nanoclaw.dev/quickstart))  
  Six undervalues its actual service support; Docker, credential tooling and customization through code still create operating friction. The documented 4 GB requirement is not a measured steady-state footprint.

- **IronClaw — bump Fit 6→8.5 (+2.5); keep Ops 7.** Its official README documents identity files, persistent memory, channels, routines, heartbeat execution and onboarding that installs a background service, although channel activation requires its WebUI. ([Official README](https://github.com/nearai/ironclaw))  
  It is more than an untrusted-tool sandbox; I lack comparable runtime-memory and unattended-recovery evidence to increase Ops.

- **ElizaOS — bump Fit 5→7 (+2); keep Ops 6 provisionally.** Its official documentation covers character identity, memory, runtime lifecycle and recurring background tasks, while its server configuration documents authentication as unset by default. ([Documentation index](https://docs.elizaos.ai/llms.txt), [Server defaults](https://docs.elizaos.ai/projects/environment-variables))  
  Social/web3 positioning is not disqualifying, but assembling an assistant from framework components earns less convenience credit; I could not verify the claimed Docker/Coolify/PM2 deployment coverage sufficiently to raise Ops.

- **Nanobot — bump Fit 4→9 (+5); bump Ops 5→8 (+3).** The official project documents long-term memory, channels, scheduled automation and a persistent gateway, with Docker deployment and `gateway install-service --manager systemd` plus logout-survival instructions. ([Capabilities](https://github.com/HKUDS/nanobot), [Deployment](https://github.com/HKUDS/nanobot/blob/main/docs/deployment.md))  
  “Library; you write the daemon” is contradicted by the current documentation.

## 3. Formula

**Keep 50/50.** The evidence and axis definitions need repair more than the weights.

Define **Fit** as coverage of the actual assistant workflows and required channels. Define **Ops** as installation, safe defaults, resource consumption, supervision, recovery, updates and restoration. Count each concern once.

Require the chosen channel and logout/reboot survival as eligibility conditions: a tiny binary cannot compensate for failing either. Exclude migration costs throughout. Treat differences below roughly 0.5 total points as unresolved without operational testing.

## 4. Blind spots

- **Security defaults:** distinguish container-internal listening from host-port publication; evaluate authentication, sender authorization, tool isolation and secret access separately. Encryption with a colocated key does not protect against a compromised service account.
- **RAM reality:** measure the whole deployment during idle, concurrent conversations, browser work and updates. Binary size, source-build RAM and runtime RSS answer different questions.
- **Channel reliability:** test reconnects, token expiry, duplicate delivery, queued messages and recovery after reboot or network loss. A running daemon does not prove a working channel.
- **Updater pain:** assess pinned releases, dependency changes, database migrations, rollback and preservation of customizations. This is ongoing operations, not excluded migration cost.
- **Bus factor:** examine active maintainers, release ownership, security-response history and adapter maintenance. I have not established comparative evidence here.
- **Unattended behavior:** check stuck-task recovery, spending limits, approval handling and useful failure notifications. “Has cron” proves scheduling exists, not that delegated work completes.
- **Organization semantics:** clarify shared trusted assistant versus separate users with permissions and private memories; those are materially different jobs.

## 5. Revised table

Totals retain your formula; equal scores remain tied.

| Rank | Claw | Fit | Ops | Total |
|---|---|---:|---:|---:|
| =1 | OpenClaw | 10 | 8.5 | 9.25 |
| =1 | Hermes Agent | 10 | 8.5 | 9.25 |
| =3 | ZeroClaw | 9 | 8 | 8.50 |
| =3 | Nanobot | 9 | 8 | 8.50 |
| 5 | PicoClaw | 8.5 | 8 | 8.25 |
| 6 | NanoClaw | 9 | 7 | 8.00 |
| 7 | IronClaw | 8.5 | 7 | 7.75 |
| 8 | ElizaOS | 7 | 6 | 6.50 |
