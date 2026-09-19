# Scoring review: 24/7 VPS claw convenience ranking

**Evidence basis, stated once:** I was asked to answer without tools, so I have not opened a single repo, README, unit file, or Docker sample. Everything in your rationale column is taken as given. My findings are therefore about *rubric application, internal consistency, and the formula* — places where your own stated evidence contradicts your own stated scale. Where I bring outside recollection, I mark it and flag it for verification. I invent no docs.

---

## 1. Verdict

**Revise.** Not reject — the axis choice is sane, the exclusion list is principled, and the top cluster is roughly right. But three of the eight scores contradict evidence you wrote yourself in the same row, and the ranking's headline result (the 9.0/9.0 tie broken by hand) is an artifact of one of those contradictions rather than a real dead heat.

The three structural problems:

1. **ZeroClaw Ops=10 is unsupportable on your own rubric.** Your Ops-10 definition requires "sane loopback defaults." Your ZeroClaw rationale says "Docker sample binds public." A runtime cannot score full marks on a scale one of whose four named terms it fails. This is the single largest error in the table and it is self-evident from the row alone.
2. **The Fit rubric was written around the #1 entry.** "Named 24/7 assistant with channels, memory, a daemon — not a coding TUI, not a swarm-only framework" is a description of OpenClaw with the negations aimed at the excluded set. A 10 awarded against a rubric shaped by the winner carries no information.
3. **An unstated criterion ("treasury-grade", "finance operator agent") is doing scoring work in rows 4 and 7 but appears nowhere in the job definition or either axis.** Either promote it to the rubric and rescore all eight against it, or strike it. Applied selectively, it produces the ElizaOS/PicoClaw inversion below.

Fixing #1 alone dissolves the tie and makes the tie-break note unnecessary.

---

## 2. Score-by-score

### OpenClaw 2.0 — Fit 10 / Ops 8
**Fit: keep 10, but label it.** It's the anchor, not a measurement. Everything else is scored as a distance from OpenClaw, which is legitimate as a method but means "Fit 10" should be read as "defines the scale." If you want the axis to be informative, decompose Fit into four named sub-criteria (persistent identity, channel breadth, durable memory, supervised daemon), score each 0–2.5, and let OpenClaw land where it lands.

**Ops: drop to 7.5.** Your own ding is "≥6 GB for source builds" — the highest RAM floor in the table — yet you gave NanoClaw a 6 for a *4 GB* floor. The ranking penalizes less RAM more. Separate build RAM from steady-state RAM and apply it consistently; if the Docker path runs fine in 2 GB, say so and the 8 survives.

**Flag, low confidence, verify before using:** I recall public reporting in early 2026 about internet-exposed Clawdbot/Moltbot-lineage instances reachable without authentication. If that is accurate and 2.0 did not change the default posture, you have dinged ZeroClaw for a public-bind sample while giving a pass to a project with a *field history* of the same failure. That asymmetry, not the RAM, is the real threat to Ops 8. I cannot confirm this from here.

### ZeroClaw — Fit 8 / Ops 10
**Fit: keep 8.** "Thinner skill/channel graph" is a fit deficiency, correctly located and correctly sized relative to a 10 anchor.

**Ops: drop to 8.5.** As above — a public-binding default sample fails a named term of the Ops-10 definition. 8.5 credits the genuinely strong parts (`service install`, distroless GHCR, VPS named as system-scope) while refusing full marks to a runtime that ships an insecure sample. If the sample is in the README rather than a compose file people actually `docker compose up`, 9.0 is arguable; 10 is not.

### Hermes Agent — Fit 9 / Ops 8
**Fit: bump to 9.5.** Your rationale states Hermes does "the same job as OpenClaw: gateway, channels, memory, skills, linger" — that is the Fit-10 rubric enumerated, item for item. A one-point gap against an identical capability list needs a named missing capability. You don't name one. Either name it (channel count? maturity? single-maintainer?) or close the gap. I'd close it to 0.5 to reflect a plausible maturity/breadth edge for OpenClaw that you haven't yet documented.

**Ops: keep 8.** "Ops ding matches OpenClaw (Python+Node, not a 4 MB binary)" is consistent — and if you drop OpenClaw's Ops to 7.5 on the RAM point, Hermes should *not* follow, because a curl installer with linger is a lighter first-day path than a 6 GB source build. Keeping Hermes at 8 while OpenClaw moves to 7.5 is the consistent outcome, not a favor.

### PicoClaw — Fit 6 / Ops 9
**Fit: keep 6, but on different grounds.** "Too thin for treasury-grade assistant" imports a criterion the job spec doesn't contain. On the stated rubric the question is only: named identity, channels, memory, daemon — yes or no, how many. A single Go binary with easy systemd almost certainly clears "daemon" and probably "named identity," and is thin on memory/skills. That reasoning lands at 6 too, so the number survives; the justification should be replaced so it doesn't leak an unscored axis into one row.

**Ops: keep 9.** One static binary + systemd is the reference case. I'd reserve 10 for a runtime that also documents upgrade-in-place and has no insecure sample.

### NanoClaw — Fit 7 / Ops 6
**Ops: bump to 7.** Two problems with 6. First, a 4 GB floor is cheap — that's a ~€4/mo Hetzner CX22 — and it is *lower* than the 6 GB you forgave in the #1 row. Second, "Claude-tied" is vendor lock-in, which is a fit/portability property, and you have already priced it in the Fit=7. Counting it again in Ops is double-charging. Per-agent Docker isolation plus linger is a 7 ops story with a real RAM tax, not a 6.

**Fit: keep 7.** Defensible — per-agent isolation implies a real supervised runtime, model lock caps it below the assistants above.

### IronClaw — Fit 6 / Ops 7
**Keep both.** No internal contradiction. But note what this row exposes: WASM sandboxing of untrusted tool code is a *security* property, and your formula has no security axis, so its entire value is being expressed as "convenient when untrusted tool code is the point" — a sentence with nowhere to land numerically. That's a formula defect (§3), not a scoring error.

### ElizaOS — Fit 5 / Ops 6
**Fit: bump to 7.** This is the clearest inversion in the table. On your *stated* rubric — named persistent agent, channels, memory, daemon — ElizaOS has a broader channel and memory surface than PicoClaw, which you scored 6. Your stated reason for the 5 ("public social/web3 bots, not a finance operator agent") is the unstated finance criterion again, and it's a statement about *what people typically deploy it for*, not about whether it satisfies the four rubric terms. If finance-operator suitability matters — and for a treasury context it obviously does — make it an axis and let ElizaOS lose points there honestly, in a column where OpenClaw and Hermes also get graded.

**Ops: keep 6.** Docker/Coolify/PM2 documented is real but PM2 as a named path is a mark against a systemd-or-Docker job spec.

### Nanobot — Fit 4 / Ops 5
**Ops: drop to 4.** Your Ops-10 definition leads with "official systemd/Docker path." Your rationale says "you write the daemon." That's a zero on the first and heaviest term of the axis; `pip install` ease cannot carry it back to the midpoint. 4 credits the easy install and the headless-friendliness of a library.

**Fit: keep 4.** "Library, not the org identity" is the right call and correctly placed on Fit.

**No evidence available to me on:** Hermes Agent, ZeroClaw, PicoClaw, NanoClaw, IronClaw as named here — I cannot confirm their install paths, RAM floors, or bind defaults, and I have not tried. Every judgment above is conditional on your rationale text being accurate.

---

## 3. Formula

**50/50 fit+ops is directionally right and structurally incomplete.** It measures *choosing* and *installing*. The job is "24/7" — the expensive part is month nine, and nothing in the current formula sees month nine.

Two specific failures of the 50/50 model as applied:

- **It has no floor.** ZeroClaw's public-bind sample is a security defect that got averaged into a 10 and then into a 9.0 total. Averaging is the wrong operator for disqualifying defects.
- **It cannot represent day-2 cost.** A 4 MB static binary and a Node source build with a fast-moving dep tree can score identically on "official Docker path documented," and then diverge enormously the first time you run an unattended upgrade.

**What I would actually use:**

```
Total = 0.45 × Fit + 0.35 × Day-1 ops + 0.20 × Day-2 survivability
```
…with a hard gate: **any runtime whose shipped default or sample exposes a secrets-bearing process beyond loopback is capped at Ops 7 until that is fixed**, regardless of how good the rest of the ops story is.

**Day-2 survivability (0–10)** = upgrade-in-place path + behavior on crash/OOM/reboot + whether a silent death is observable + breaking-change cadence + bus factor. It's a fifth of the weight because on a 24/7 box it is roughly a fifth of the pain, and it's the axis where "one static binary" earns its keep beyond the install-day 9 you already gave PicoClaw.

If you want the minimal change instead: **keep 50/50 and add only the gate.** The gate alone fixes the tie and is one sentence of rubric. I'd take the three-axis version because it's the one that stops PicoClaw and ZeroClaw being undervalued for the thing that actually makes them pleasant to run for a year.

---

## 4. Blind spots

Ranked by how likely each is to change the ordering:

1. **Channel reliability.** The #1 cause of a 24/7 assistant being dead on a Tuesday is not the VPS — it's a WhatsApp/Telegram/iMessage bridge that got re-auth'd, rate-limited, or banned. Nothing in Fit or Ops distinguishes "has a Telegram plugin" from "reconnects cleanly after a 3 a.m. session invalidation." For this job that gap is larger than the entire Rust-vs-Node question.
2. **Security defaults, as an axis rather than a footnote.** The job says *secrets on disk*. So: env file vs. OS keyring vs. sops/age? Is the gateway authenticated or does loopback-only *substitute* for auth (fatal the moment someone adds a reverse proxy)? Is there per-channel authz — the job says "org assistant," so who besides you can make it act? None of this is visible in a single "Ops" number, and IronClaw's WASM sandbox currently has nowhere to score.
3. **RAM reality.** Your numbers mix three different quantities — build RAM, idle RAM, and RAM under load — and it's already produced the OpenClaw-6GB-vs-NanoClaw-4GB inconsistency. Also unaddressed: do any of these run inference locally, or are they all API clients? If all API clients, RAM barely separates them and Ops is really about process supervision, not memory. If any expects a local model, its floor is 10× everything else here.
4. **Updater pain.** Unattended `apt upgrade`, a Node major bump, a Python minor bump, a breaking config schema change. Single-binary-with-a-`self-update` and "git pull && rebuild" are different products.
5. **Bus factor and cadence.** Six of these eight read as young projects. A one-maintainer runtime that ships breaking changes weekly is a worse 24/7 bet than a slower project with a worse installer — and the current formula rewards the installer.
6. **State durability.** Where does memory live, can you back it up while running, and does a restore actually restore the assistant's identity? For an org assistant this is the difference between a service and a toy.
7. **Silent-failure observability.** Does it log usefully, expose health, and can you alert on it dying? systemd `Restart=always` hides a crash loop rather than reporting it.
8. **Methodological:** with two axes at 0.5 granularity you will keep generating ties, and the tie-break is doing real ranking work. State it as a standing rule ("fit wins ties") rather than a per-row note.

---

## 5. Revised table

Both columns use my revised Fit/Ops. Day-2 is assigned on **structural** grounds only — static binary ⇒ low upgrade pain, large dep tree ⇒ higher, vendor-API coupling ⇒ exposed to upstream breakage — not on any documentation I have read. Treat that column as a hypothesis to verify, not a finding.

| Rank | Claw | Fit | Ops | Day-2 | **Total (0.45/0.35/0.20)** | Total (50/50) | Change vs. yours |
|---|---|---|---|---|---|---|---|
| 1 | OpenClaw 2.0 | 10 | 7.5 | 6.5 | **8.43** | 8.75 | Ops −0.5 (build RAM, applied consistently) |
| 2 | Hermes Agent | 9.5 | 8 | 7 | **8.48** | 8.75 | Fit +0.5 — **moves to #2** |
| 3 | ZeroClaw | 8 | 8.5 | 8.5 | **8.28** | 8.25 | Ops −1.5 (gate: public-bind sample) |
| 4 | PicoClaw | 6 | 9 | 8.5 | **7.55** | 7.5 | Same number, different reason |
| 5 | NanoClaw | 7 | 7 | 6 | **6.80** | 7.0 | Ops +1 (RAM consistency, no double-count) |
| 6 | ElizaOS | 7 | 6 | 5.5 | **6.35** | 6.5 | Fit +2 — **passes IronClaw on 50/50** |
| 7 | IronClaw | 6 | 7 | 6.5 | **6.45** | 6.5 | Unchanged |
| 8 | Nanobot | 4 | 4 | 5 | **4.60** | 4.0 | Ops −1 (no daemon path = fails axis term 1) |

Under the three-axis formula, Hermes edges OpenClaw by 0.05 — which is noise, and the honest reading is **OpenClaw and Hermes are tied at the top**, with ZeroClaw a genuine third rather than a co-first. Under 50/50 with corrected scores, OpenClaw and Hermes tie at 8.75 and ZeroClaw sits clearly third.

The three changes that actually matter, in order: **ZeroClaw is not an Ops 10 while its sample binds public**; **Hermes is not a point behind OpenClaw on a capability list you described as identical**; **ElizaOS is not a Fit 5 on a rubric that never mentions finance**. The rest is bookkeeping.

**Two things to verify before publishing** — both could move the top of the table and neither is checkable from here: whether OpenClaw 2.0's default posture still exposes an unauthenticated gateway (the ZeroClaw ding must be applied symmetrically if so), and whether ZeroClaw's public bind is a copy-paste compose file or a README illustration. The second determines whether its Ops is 8.5 or 9.
