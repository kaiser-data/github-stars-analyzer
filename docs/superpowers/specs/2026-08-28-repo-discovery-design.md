# Repo discovery — design

**Date:** 2026-08-28
**Status:** approved, not yet implemented

Find GitHub repos that belong in an existing landscape report but are absent
from the starred collection, rank them, and star the ones that survive review.

---

## Problem

The collection holds 1,794 starred repos and 28 hand-curated landscape reports
over them. A report's taxonomy can only name repos that are already starred, so
every report is bounded by what was starred *before* it was written. Two reports
have already run into this by hand:

- `agentic-terminals` — a gap analysis checked 45 candidate terminal apps by
  exact `owner/name`, confirmed all 45 absent, and read their metrics from the
  GitHub API manually.
- `jetson-inference-engines` — supplemented missing engines with live API data
  rather than dataset rows.

Both were one-off manual sweeps. This design makes that sweep repeatable.

## Scope

In: finding candidates for a report topic, ranking them, starring approved ones.

Out: writing report prose, editing report `TAXONOMY` dicts, changing the weekly
refresh pipeline. Taxonomy prose stays hand-written — it is the part of a report
that carries actual judgement.

## Decisions

| Question | Decision |
|---|---|
| What makes a repo "relevant"? | Report-gap driven: it belongs in a landscape a report already covers |
| Where do candidates come from? | GitHub search **and** model recall, both verified through the API |
| How far does it go? | Ranked shortlist → user approves → it stars → user re-runs refresh |
| How is it built? | A script does the mechanical half; a thin skill carries the judgement half |
| Language | Node, not Python — see below |

**Why Node.** Discovery is data acquisition, not reporting. `scripts/lib/github.mjs`
already carries typed failure classification, retry-with-backoff and request
pacing, all added after the 2026-08-12 secondary-rate-limit incident that
silently truncated the dataset 1,596 → 96. Reimplementing that in Python to
match `scripts/reports/` would mean re-learning it. `discover.mjs` sits beside
`sample.mjs` and `ingest.mjs`; the report generators stay Python.

---

## Architecture

Single entry point:

```
node scripts/discover.mjs --report <slug> \
     [--extra owner/repo,owner/repo] \
     [--min-stars 200] [--max-stale-days 365] [--limit 40]
```

### Data flow

1. **Load the landscape.**
   - `reports/<slug>.md` → *covered set*: every `github.com/owner/repo` link in
     the markdown. Uniform across all 28 reports regardless of generator shape
     (measured: 59 links for `agentic-terminals`, 61 for `charting-stack`).
   - `reports/<slug>.meta.json` → `title`, `summary`, and `categories` keys.
     The category names are the search vocabulary.
   - `data/classified.json` → *star set*, the 1,794 repos already held.

2. **Generate candidates**, union of two sources:
   - **Search** — one GitHub search query per category name, plus keyword
     queries derived from title and summary. Every query carries
     `fork:false archived:false stars:>=<min> pushed:>=<date>`.
   - **Model recall** — names passed via `--extra`, supplied by the skill from
     what the model knows belongs in the landscape. This is where well-branded
     tools that keyword search ranks badly enter.

3. **Resolve, then classify against three states.** Resolution comes *before*
   diffing — see Renames.

   A report's markdown links every repo it *names*, including ones it names as
   absent. `agentic-terminals` links 59 repos, of which only 14 are starred.
   So "covered" is not a drop filter — crossing it with the star set gives
   three states, and only the first is uninteresting:

   | Covered by report | In star set | State | Action |
   |---|---|---|---|
   | yes | yes | held | drop |
   | yes | **no** | **`known-gap`** | **surface first** |
   | no | no | `new` | surface |

   `known-gap` candidates rank above `new` ones by default: the report author
   already judged them in-scope and wrote them down, so the only open question
   is whether to star them. On `agentic-terminals` this state is exactly the
   45 repos its gap analysis enumerated.

   (`covered: no, starred: yes` also exists — a starred repo the report omits.
   That is a *report* gap rather than a *collection* gap, out of scope here.)

4. **Verify and enrich.** One GraphQL call per surviving candidate: stars,
   `created_at`, `pushed_at`, licence, primary language, topics, description,
   90-day commits, 90-day unique authors. An `--extra` name that fails to
   resolve is emitted as **unresolved**, never silently dropped — that is the
   hallucination check, and it must be visible.

5. **Score, rank, emit** → `reports/<slug>.candidates.md` and
   `reports/<slug>.candidates.json`, plus the table on stdout.

### Token resolution

`GITHUB_TOKEN` from the environment, falling back to `gh auth token`. The `.env`
token was found dead (HTTP 401) on 2026-08-28, which is also why every scheduled
CI refresh since 2026-08-03 failed at the token gate. The fallback makes a dead
`.env` a non-event for local runs.

---

## Scoring

### Health: reuse the existing classifier

`lifecycleStage()` and `healthScore()` move out of `scripts/classify.mjs` into
`scripts/lib/classify-core.mjs`, imported by both `classify.mjs` and
`discover.mjs`. Behaviour is unchanged; `classify.mjs` keeps producing
byte-identical output.

This matters because it puts a candidate's `health_score` on the same scale as
the 1,794 repos already held. "Is this better maintained than what the report
already covers" becomes a direct comparison instead of a judgement call.

This is one of two changes the work makes to existing code. The other is
`getToken()` in `scripts/lib/github.mjs`, which currently throws when
`GITHUB_TOKEN` is unset and gains the `gh auth token` fallback described above.
Nothing else is touched.

### Fit: a separate, decomposed score

Ranked by a blend, but **every component is displayed** — a total alone gives
the reader nothing to overrule.

| Component | Source | Purpose |
|---|---|---|
| `relevance` | vocabulary overlap of topics + description against the report's category names and title terms | keeps fast-rising but off-theme repos out |
| `standing` | log-scaled stars | a 200k-star list must not outrank a 3k-star tool |
| `health` | reused `health_score` | same scale as the dataset |
| `recency` | `days_since_push`, age | a landscape report cares about what is alive |

### Kind labels, not hard drops

The classic false positive is the awesome-list — but `rothgar/awesome-tuis` is
legitimately in the `agentic-terminals` set, so dropping lists would be wrong.
Each candidate gets a `kind`:

- `tool` — default
- `list` — name/description matches `awesome|curated|collection of|resources`
  and 90-day commits are low
- `tutorial` — matches `tutorial|course|examples|learn|book|roadmap|interview`
- `spec/doc` — specification or documentation repos

`list` and `tutorial` rank below `tool` rather than being removed.

Hard filters stay minimal and are stated in the output: forks, archived, below
`--min-stars`, unpushed for longer than `--max-stale-days`.

---

## Renames are a correctness requirement

The GitHub API silently follows renames, so a query for `owner/old-name` returns
the repo under `owner/new-name`. If the set-diff runs on the *queried* name, a
repo already starred under its new name reappears on every sweep as a fresh
"missing" candidate.

The `agentic-terminals` gap analysis hit exactly this, three times:

- `pvolok/mprocs` → `pvolok/dekit`
- `stravu/crystal` → `nimbalyst/nimbalyst`
- `KDE/konsole` — a read-only mirror whose star count understates adoption

**Requirement:** resolve every candidate to its canonical `full_name` before
diffing, and report the redirect in the output when one occurs. Mirrors are
flagged, not dropped.

---

## The skill

Name: `discovering-repos-to-star`.

Triggers on: "what's missing from report X", "find new repos for the stars",
"anything new in agent memory since August", "should I be starring anything for
the RAG report".

**Precondition:** `reports/<slug>.md` must exist. No report, no discovery — the
whole premise is a landscape to find gaps in. Point the user at the
`star-reports` skill instead.

### Tiering

- `SKILL.md` — when to use, precondition, run recipe, how to supply `--extra`
  from model recall, how to read the table, the judgement the script
  deliberately does not make, the approval and star steps.
- `references/scoring.md` — score internals, filter tuning, kind patterns.
  Not loaded on a normal run.

### The judgement layer

Things the script cannot decide and the skill must ask the model to weigh:

- Does this candidate actually belong in *this* report, or a different one?
- Is a low health score "finished" or "dead"? (the distinction
  `building-repo-picker-skills` already documents)
- Is a high-star repo a genuine tool or a rehosted mirror?
- Is a `list` worth starring on its own merits?

### Starring

Gated. The skill presents the shortlist; only on explicit user approval does it
run `gh api --method PUT /user/starred/{owner}/{repo}` per approved repo, then
instructs the user to re-run `npm run refresh` to pull the new repos into the
dataset. Starring writes to the user's account and is never done on model
judgement alone.

---

## Validation

**Ground truth already in the repo, and it is exact.** The `agentic-terminals`
gap analysis checked 45 candidates by exact name on 2026-08-23 and confirmed all
absent. Measured 2026-08-28: that report links 59 repos, 14 starred and 45 not —
matching its own stated "14 present, 45 missing".

So the `known-gap` set is not a fuzzy target. Running discovery against
`agentic-terminals` must emit **exactly 45** `known-gap` candidates, requiring
zero network calls to compute. Any drift is a bug in link extraction or the
set-diff, and it is caught offline.

Recall on the `new` state stays a judgement call — there is no ground truth for
"repos nobody has named yet" — so it is assessed by reading the output, not
asserted in a test.

**Deterministic unit checks:**

| Check | Expectation |
|---|---|
| Markdown link extraction | 59 unique repos for `agentic-terminals`, 61 for `charting-stack` |
| Three-state split | `agentic-terminals` → 14 held, 45 `known-gap` |
| Set-diff | runs on resolved names; a starred repo queried by its old name does not surface |
| Kind classification | `rothgar/awesome-tuis` → `list`, `tmux/tmux` → `tool` |
| Unresolved `--extra` | reported, not dropped |
| `classify-core` extraction | `classify.mjs` output identical before and after the refactor, `generatedAt` excluded |

---

## Out of scope

- Editing report `TAXONOMY` dicts or report prose.
- Wiring discovery into `npm run refresh`. It is judgement-heavy work; on a cron
  it produces a weekly list nobody reads, and it would put GitHub search quota
  into the critical path of a refresh that has failed every run since
  2026-08-03.
- Discovering topics no report covers yet. That is a different skill with a
  different premise.
