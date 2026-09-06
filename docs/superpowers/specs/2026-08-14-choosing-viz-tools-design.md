# choosing-viz-tools — design

**Date:** 2026-08-14
**Status:** approved, ready to implement

## Problem

You need to build a visualization or dashboard and want to know which tool to
reach for — chosen from the 1,596 repos you have actually starred, not from a
generic web search. The answer depends on the business or presentation case,
not just on the chart type: the same bar chart wants a different tool for a
board deck than for an analyst's exploration tool.

## Scope

The skill **recommends and justifies**. It picks a tool, names alternates,
surfaces the trade-offs and traps, and stops. It does not scaffold a project or
write chart code.

## Where it lives

Global — `~/.claude/skills/choosing-viz-tools/` — because the work of building a
dashboard happens in other repos. Facts are baked into reference files, so the
skill needs nothing from `github-stars-analyzer` at invoke time.

A generator in this repo (`scripts/build_viz_skill.py`) rewrites those reference
files from `reports/charting-stack.md` + `data/classified.json`. Run it after a
data refresh to un-stale the skill.

## Knowledge base

`reports/charting-stack.md` already contains the hard-won part: hand-curated
`✅ Advantages / ⚠️ Disadvantages / 🎯 Best for` prose for 61 tools across 10
layers, 24 ranked use-cases with evidence, and a licensing-traps section.

**Do not scrape READMEs to rebuild this.** Verified during design: regex over
`readme_text` returns `renderer=svg` for Chart.js (canvas-only), Grafana,
Metabase, Superset and Streamlit — because it matches shields.io badge URLs, not
capability claims. READMEs are badge-heavy and capability-light. The curated
report is the trustworthy source; the live dataset supplies health only.

## Routing dimensions

Five inherited from the report's "six questions", three added:

| Dimension | Values |
|---|---|
| Job | one chart · dashboard · report/deck · exploration · diagram |
| Author | dev in code · analyst in SQL · business user clicking · LLM/agent |
| Surface | browser app · notebook · desktop/native · static site or PDF · mobile |
| Volume | <10k · 10k–1M · >1M / streaming |
| Ops | it's a dependency · it's a platform you run |
| Licence | permissive only · AGPL/open-core fine · commercial budget |
| **Effort** *(new)* | hours · days · weeks (bespoke) |
| **Audience** *(new)* | executive/board · analyst peers · developers · non-technical self-serve · public/press |

Effort and audience carry real weight. "Bar chart of revenue" resolves to
`great-tables` for a board deck, `metabase` for analyst peers, and `d3` for a
public-facing piece — same chart, three tools.

The skill **infers dimensions from the phrasing** and asks only about ones that
are both unknown and decisive. "Board deck" alone implies audience, static
surface, low volume, and hours-not-weeks.

## Maintenance handling

Health is used, never raw. A low `health_score` means opposite things for a
finished library and a dead one, and the dataset cannot tell them apart:

| Label | Rule | Effect |
|---|---|---|
| Active | recent pushes, bus factor ≥2 | none |
| Stable | low commit rate but API-frozen and widely depended on | none; noted as *finished, not dead* |
| Slowing | 90–180d since push, bus 0–1, or Declining | caveat; can still be a first pick |
| Stalled | >180d, Abandoned, or health <20 | **never a first pick**; named as the reason |

Stable-vs-Stalled is a per-tool judgment baked in at authoring time — the single
thing a live-data-only skill would get wrong. `d3` (h40, 75d) is Stable;
`tremor` (3.5k★, 305d) is Stalled.

Verified against the 2026-08-11 vintage: 13 of the 53 ranked picks carry a weak
live signal, including three first picks — `evidence` (174d, bus 0),
`chartjs/Chart.js` (76d), `d3` (75d) — and one Abandoned third pick,
`frappe/charts` (405d, health 5).

`Stalled → never a first pick` is the one place health overrides fit.

## Token budget

Measured on the built artefacts, not estimated. Loading everything each time
costs ~13k tokens; the tiered design costs **~2,050 for a typical case**.

| Tier | Content | Cost |
|---|---|---|
| 1 — always | `SKILL.md`: procedure, 24-job shortlist map, maintenance rule | **1,629** |
| 2 — per pick | `detail.md` via `awk` range, 3 entries | **417** |
| 3 — off-menu | `tools.tsv`, 61 rows × 9 attrs, when no job row matches | **1,182** |
| 4 — on challenge | `evidence.md`, benchmark citations + licence traps | **2,457** |

Typical (tier 1+2) ≈ 2,050. Off-menu (1+2+3) ≈ 3,230. Worst case ≈ 5,700.

Full detail for all 61 tools is 8,056 tokens and is **never** read whole. Extract
by anchor range, not `grep -A<n>` — a fixed context count bleeds into the next
entry when a tool has no licence-trap line:

```
awk '/^## (owner\/repo|owner\/repo2)$/,/^$/' references/detail.md
```

Two earlier estimates in this design were wrong and are corrected above: tier 1
came in at 1,629 rather than ~700 (the job map costs more than the prose it
replaced), and `detail.md` at 8,056 rather than ~4,270 (per-entry metadata
roughly doubles the curated prose). The tiering still pays — 6× rather than the
13× first claimed.

The compression: each of the 24 use-case rows collapses from ~110 words to one
line carrying rank order plus maintenance flags. Reasoning stays in `detail.md`
and arrives only for tools that survive the shortlist.

Deliberate cuts:

- Maintenance labels stored **only where they contradict `health_score`**
  (~16 tools). Silence means unremarkable.
- No `routing.md` — the audience/effort matrices are ~20 lines and live in
  `SKILL.md` rather than costing a second file read.
- No `traps.md` — traps attach to their tool entry in `detail.md`, so they
  arrive with the pick instead of sitting in a file that might not be read.

Accepted trade-off: off-menu cases cost ~2,200 tokens because they read the full
attribute table. Better than bloating every invocation to make the rare case
cheap.

## Files

```
~/.claude/skills/choosing-viz-tools/
  SKILL.md                procedure · 24-job map · maintenance exceptions
  references/
    detail.md             61 × (adv / disadv / best-for / traps), anchored
    tools.tsv             61 × 9 attributes, for off-menu routing
    evidence.md           benchmark citations behind the rankings

github-stars-analyzer/
  scripts/build_viz_skill.py    regenerates the three reference files
```

## Output shape

```
CASE   revenue dashboard · board · 50k rows · Postgres
ROUTED audience: executive   effort: days
       author: analyst/SQL   surface: static + PDF
       volume: 50k (any renderer)   ops: no platform

▶ PICK   evidence-dev/evidence  ★6,838 · MIT
         SQL + markdown → static site, git-reviewable
         MAINTENANCE  Slowing ⚠ — 174d since push, bus 0.
                      Usable, but pin the version.

  ALT    rilldata/rill    ★2,803 · h84 · pushed today
  ALT    metabase         ★48,666 · AGPL · you run it

  TRAP   board decks want PDF — Evidence exports clean,
         Metabase fights you.
  NOT    Recharts/Chart.js — browser-app tools; there's no
         app here, just a deck.
```

Every recommendation states the data vintage, so a stale pick is visibly stale.

## Out of scope

- Scaffolding or writing chart code (recommendation only).
- Tools outside the starred corpus. When the stars genuinely lack a good answer,
  the skill says so rather than promoting a weak local match.
- Live data reads at invoke time — deliberately traded away for portability.
