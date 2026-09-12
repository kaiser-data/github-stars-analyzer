# Prompt library — design

**Date:** 2026-09-12
**Status:** approved, not yet implemented

Turn a landscape report into a ready-to-paste build prompt for an LLM, so the
starred collection produces something usable rather than only something readable.

---

## Problem

The pipeline currently ends at a report. A report tells you *which* tools to use;
it does not get you to a built thing. The gap between "here are the seven tools
that make a printable model" and an actual STL is a prompt that nobody has written
— and writing it well requires knowing the stack, the verification loop, and the
constraints a model will not infer.

That prompt is derivable from the report, but not mechanically: the stack, the
tool metrics and the verify commands come from data, while the creative brief
("a tree stump base for a trophy") cannot. A hand-written prompt file solves it
once and then rots — it keeps naming `fogleman/sdf` after the repo is archived,
with nothing to catch it.

This is also the repo's strongest demo. The arc **stars → report → prompt → artifact**
is the whole argument for curating stars at all, and only the last two links are missing.

## Scope

**In:** a prompt generator format, a build step, an index, a `Prompts` tab, a
cross-link from each parent report, and three prompts drawn from three unrelated
reports.

**Out:** generating briefs automatically; running the prompts; storing outputs;
prompt versioning or history; any change to how reports themselves are curated.

## Decisions

1. **Hybrid generation.** Each prompt is a Python generator, like a report. It
   pulls the stack and tool metrics from data and wraps them around an authored
   brief. Rejected: pure hand-authored markdown (goes stale silently, demos
   nothing about the pipeline) and fully generated prompts (the brief is the
   part that makes a prompt useful, and it cannot be derived from repo metadata —
   "Use fogleman/sdf to accomplish: Sculptural piece that must print" is not a prompt).

2. **Three prompts in v1, from three different reports.** One reads as a bespoke
   page; five written in a sitting will be uneven, and the weakest sets the
   impression. Three from unrelated domains proves the machinery is not
   3D-printing-specific.

3. **A sibling `Prompts` tab, plus a cross-link on the parent report.** The tab
   makes prompts discoverable; the cross-link makes the stars→report→prompt arc
   visible without narration. A section inside reports alone would bury them
   three clicks deep.

4. **Reuse `scripts/reports/lib.py`, do not fork it.** `fmt_stars`,
   `activity_label`, `fmt_int` and `CLASSIFIED` are needed identically.

5. **The copy button copies the brief only** — not the stack line, the verify
   block or the variants. What lands in the model's context should be the prompt
   and nothing else; the surrounding material is for the human deciding whether
   to use it.

## Architecture

```
data/classified.json      ─┐
reports/<slug>.meta.json  ─┴→ scripts/prompts/<name>.py → prompts/<name>.md
                                                          prompts/<name>.meta.json
                                                        → scripts/prompts/build_prompts.py
                                                          → public/prompts/index.json
                                                          → copies to public/prompts/
                                                          → injects cross-link into
                                                            reports/<parent>.md
```

Deliberately the same shape as `scripts/reports/`: a `GENERATORS` list, one
generator per artifact, a meta sidecar, an index the app reads, no API calls,
fully reproducible.

### The generator contract

Every prompt generator declares:

| Field | Type | Source |
|---|---|---|
| `SLUG`, `TITLE` | str | authored |
| `REPORT` | str | parent report slug; must exist in `reports/` |
| `STACK` | `[(stage, full_name), …]` | repos, resolved against `classified.json` |
| `BRIEF` | str | **authored** — the prompt body |
| `INPUTS` | `[(name, what, why)]` or `None` | authored; optional measured-inputs table |
| `VERIFY` | `[(comment, command)]` | authored, tool names interpolated from `STACK` |
| `VARIANTS` | `[(label, text)]` | authored |

Rendered order: title → parent-report provenance line → live stack table →
optional inputs table → the brief → variants → verify block → methodology.

### Drift detection

`STACK` entries are resolved against `classified.json`. An entry that no longer
resolves — archived upstream and dropped by `sample.mjs`, unstarred, or renamed —
makes the generator print `WARNING missing: [...]` on stdout, exactly as report
`TAXONOMY` drift already does, and `build_prompts.py` collects those and re-raises
at the end. This is the mechanism that keeps a prompt from recommending a dead tool.

Each resolved entry additionally renders its current metrics inline
(`fogleman/sdf · 2,001★ · Abandoned`), so a reader sees the evidence and can judge
a low health score themselves. Prompts inherit the report's caveat that in
geometry and algorithm libraries, low health frequently means *finished*.

### Cross-link injection

`build_prompts.py` appends a `## Build something with this stack` section to each
parent report's markdown, listing its prompts. It follows the existing
`inject_charts` pattern in `build_index.py`: guard on a marker already being
present, and rely on the report being regenerated from scratch each build so the
injection is idempotent per run.

Placement: immediately before `## Methodology & caveats` when present, otherwise
appended. Ordering constraint — **`build_prompts.py` must run after the report
generators**, since it edits their output. It is invoked at the end of
`build_index.py`'s `build()`, after `inject_charts`.

## App

- `src/lab/PromptsView.jsx` — lazy-loaded like `ReportsView`; card grid → detail.
- `src/lab/markdownComponents.js` — `MD_COMPONENTS` extracted from `ReportsView.jsx`
  (currently 40 lines inline) and imported by both views. This is the only
  refactor in scope.
- `LabApp.jsx` — new `prompts` tab key, `React.lazy` import, `Suspense` fallback,
  entry in the tab list.
- Copy button uses `navigator.clipboard.writeText` on the brief text, carried in
  the prompt's meta sidecar as a `brief` field so the view need not parse markdown
  to find it. Falls back to selecting the text when the clipboard API is unavailable.

## The three prompts

| Slug | Parent report | Exercises |
|---|---|---|
| `stump-base` | `3d-printing-stack` | measured `INPUTS`; ported verbatim from the existing draft |
| `rag-eval-harness` | `rag-tooling` | `INPUTS = None`; a different domain entirely |
| `trading-dashboard` | `charting-stack` | visual output; overlaps the `choosing-viz-tools` skill |

`prompt-tree-stump.md` at the repo root is deleted; its brief moves verbatim into
`scripts/prompts/stump_base.py`.

## Validation

- Each generator prints `stack: N / N resolved` with no `WARNING missing:` line.
- Markdown table column counts match their headers in all three outputs — the
  historic bug source in this repo.
- `public/prompts/index.json` contains three entries with non-empty `brief` fields.
- Each parent report contains exactly one `## Build something with this stack`
  section after a full `build_index.py` run, and still exactly one after a second
  consecutive run.
- A deliberately broken `STACK` entry (nonexistent repo) fails the build loudly.
- `npm run build` succeeds; the `Prompts` tab renders; the copy button places the
  brief and only the brief on the clipboard.

## Out of scope

- Generating briefs from `TASK_RANKINGS`. Tried in design and rejected: the output
  is generic to the point of uselessness.
- Prompt outputs, run history, or any execution. The repo analyses stars; it does
  not run models.
- Backfilling prompts across all 27 reports. Three is the proof; breadth is a
  later decision once the format has survived contact with use.
