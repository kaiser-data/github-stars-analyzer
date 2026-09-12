# Prompt Library Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn a landscape report into a ready-to-paste build prompt for an LLM, surfaced in a `Prompts` tab and cross-linked from the report that justified it.

**Architecture:** Deterministic Python generators mirroring `scripts/reports/`. Each prompt generator wraps an authored brief in a generated shell — the stack with live repo metrics pulled from `data/classified.json`, plus verify commands. A build step writes `public/prompts/index.json`, copies markdown to `public/prompts/`, and injects a cross-link section into the parent report's markdown. A lazy-loaded React view renders the index and offers a copy-to-clipboard of the brief.

**Tech Stack:** Python 3 (generators, no deps beyond stdlib), pytest 9.0.2 (tests), React 18 + `react-markdown` + `remark-gfm` (app), Vite.

## Global Constraints

- No network calls at generation time. Generators read `data/classified.json` and `reports/*.meta.json` only; output must be reproducible.
- Reuse `scripts/reports/lib.py` for `CLASSIFIED` and `fmt_int` — do not redefine either. `fmt_stars` is deliberately **not** reused in prompt output: it appends a ▲/▼ snapshot trend marker, which is signal in a landscape report and noise in a build prompt whose stack table already carries health and lifecycle. `activity_label` is not needed by prompts.
- Every markdown table row must have the same column count as its header. This is the historic bug source in this repo.
- A `STACK` entry that does not resolve against `classified.json` must print `WARNING missing: [...]` on stdout, surface in the same drift summary as report drift, and render a visible warning banner in the prompt's own markdown. It must **not** fail the build: `build_index.py` deliberately treats curation drift as normal upstream churn (see the comment in its `__main__`), and one stale prompt must not block 27 reports from rebuilding.
- Cross-link injection must run **before** `build()` copies reports to `public/reports/`, or the two diverge.
- The copy button copies the brief only — not the stack table, variants, or verify block.
- Absolute paths in all commands below are relative to the repo root `/Users/marty/claude-projects/github-stars-analyzer`.

---

### Task 1: Prompt library core

**Files:**
- Create: `scripts/prompts/__init__.py` (empty)
- Create: `scripts/prompts/promptlib.py`
- Test: `tests/test_prompt_lib.py`

**Interfaces:**
- Consumes: `scripts/reports/lib.py` → `fmt_int`, `CLASSIFIED` (imported inside `promptlib.py` and re-exported, so generators import both from `promptlib`)
- Produces:
  - `resolve_stack(stack, by_name) -> (resolved, missing)` where `stack` is `[(stage:str, full_name:str)]`, `resolved` is `[(stage:str, full_name:str, repo:dict)]`, `missing` is `[str]`
  - `render_stack_table(resolved) -> list[str]` (markdown lines)
  - `PROMPT_SECTION: str` — the cross-link heading constant
  - `inject_prompt_links(md_path, prompts) -> bool` where `prompts` is `[(title:str, slug:str, summary:str)]`

- [ ] **Step 1: Create the package marker**

```bash
mkdir -p scripts/prompts tests
touch scripts/prompts/__init__.py
```

- [ ] **Step 2: Write the failing tests**

Create `tests/test_prompt_lib.py`:

```python
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts", "prompts"))

from promptlib import PROMPT_SECTION, inject_prompt_links, render_stack_table, resolve_stack  # noqa: E402

REPO_A = {"full_name": "fogleman/sdf", "stars": 2001, "health_score": 4, "lifecycle_stage": "Abandoned"}
REPO_B = {"full_name": "mikedh/trimesh", "stars": 3678, "health_score": 74, "lifecycle_stage": "Classic"}
BY_NAME = {"fogleman/sdf": REPO_A, "mikedh/trimesh": REPO_B}


def test_resolve_stack_returns_repos_in_declared_order():
    stack = [("Author", "fogleman/sdf"), ("Validate", "mikedh/trimesh")]
    resolved, missing = resolve_stack(stack, BY_NAME)
    assert missing == []
    assert [r[0] for r in resolved] == ["Author", "Validate"]
    assert resolved[0][2]["stars"] == 2001


def test_resolve_stack_reports_unresolved_entries():
    stack = [("Author", "fogleman/sdf"), ("Slice", "ghost/nope")]
    resolved, missing = resolve_stack(stack, BY_NAME)
    assert missing == ["ghost/nope"]
    assert len(resolved) == 1


def test_render_stack_table_rows_match_header_column_count():
    resolved, _ = resolve_stack([("Author", "fogleman/sdf"), ("Validate", "mikedh/trimesh")], BY_NAME)
    lines = render_stack_table(resolved)
    header_cols = len(lines[0].strip("|").split("|"))
    for row in lines[2:]:
        assert len(row.strip("|").split("|")) == header_cols


def test_inject_prompt_links_inserts_before_methodology(tmp_path):
    md = tmp_path / "r.md"
    md.write_text("# Title\n\n## Which one?\n\nbody\n\n## Methodology & caveats\n\nnotes\n")
    assert inject_prompt_links(str(md), [("Stump base", "stump-base", "A trophy base.")]) is True
    text = md.read_text()
    assert PROMPT_SECTION in text
    assert text.index(PROMPT_SECTION) < text.index("## Methodology & caveats")


def test_inject_prompt_links_appends_when_no_methodology(tmp_path):
    md = tmp_path / "r.md"
    md.write_text("# Title\n\nbody\n")
    assert inject_prompt_links(str(md), [("Stump base", "stump-base", "A trophy base.")]) is True
    assert PROMPT_SECTION in md.read_text()


def test_inject_prompt_links_is_idempotent(tmp_path):
    md = tmp_path / "r.md"
    md.write_text("# Title\n\nbody\n")
    inject_prompt_links(str(md), [("Stump base", "stump-base", "A trophy base.")])
    assert inject_prompt_links(str(md), [("Stump base", "stump-base", "A trophy base.")]) is False
    assert md.read_text().count(PROMPT_SECTION) == 1


def test_inject_prompt_links_noop_on_empty_list(tmp_path):
    md = tmp_path / "r.md"
    md.write_text("# Title\n\nbody\n")
    assert inject_prompt_links(str(md), []) is False
    assert PROMPT_SECTION not in md.read_text()
```

- [ ] **Step 3: Run the tests to verify they fail**

Run: `python3 -m pytest tests/test_prompt_lib.py -v`
Expected: FAIL — `ModuleNotFoundError` or `ImportError: cannot import name 'resolve_stack'`

- [ ] **Step 4: Write the implementation**

Create `scripts/prompts/promptlib.py`:

```python
"""Shared helpers for prompt generators.

Named promptlib, not lib, because scripts/reports/lib.py already claims `lib`
and both directories land on sys.path during a full build. That rename is what
lets this module import the reports lib by its own name, below.

Mirrors scripts/reports/lib.py in spirit: pure functions over already-loaded
data, no I/O beyond the one injection helper, no network.
"""

import os
import sys

# scripts/reports/lib.py owns CLASSIFIED and fmt_int; reuse them rather than
# forking. Path insert is done here so the import works regardless of which
# generator imported this module first.
_REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports")
if _REPORTS_DIR not in sys.path:
    sys.path.insert(0, _REPORTS_DIR)

from lib import CLASSIFIED, fmt_int  # noqa: E402,F401  (re-exported for generators)

PROMPT_SECTION = "## Build something with this stack"


def resolve_stack(stack, by_name):
    """Resolve [(stage, full_name)] against the classified dataset.

    Returns (resolved, missing). A repo that has left the dataset — archived
    upstream and dropped by sample.mjs, unstarred, or renamed — lands in
    `missing` so the generator can warn and the build can fail loudly, rather
    than a prompt quietly recommending a dead tool.
    """
    resolved = []
    missing = []
    for stage, full_name in stack:
        repo = by_name.get(full_name)
        if repo is None:
            missing.append(full_name)
        else:
            resolved.append((stage, full_name, repo))
    return resolved, missing


def render_stack_table(resolved):
    """Markdown table of the stack, carrying each tool's current metrics.

    The metrics are inline on purpose: a reader should be able to judge a low
    health score themselves. In geometry and algorithm libraries it usually
    means *finished*, not dead.
    """
    lines = [
        "| Stage | Tool | Stars | Health | Lifecycle |",
        "|---|---|---|---|---|",
    ]
    for stage, full_name, repo in resolved:
        lines.append(
            "| {stage} | [`{name}`](https://github.com/{name}) | {stars} | {health} | {lc} |".format(
                stage=stage,
                name=full_name,
                stars=fmt_int(repo.get("stars", 0)),
                health=repo.get("health_score", "—"),
                lc=repo.get("lifecycle_stage", "—"),
            )
        )
    return lines


def inject_prompt_links(md_path, prompts):
    """Add a cross-link section to a parent report's markdown.

    Follows the inject_charts pattern in build_index.py: guard on the marker
    already being present, and rely on reports being regenerated from scratch
    each build so the injection is idempotent per run.

    Returns True when it wrote, False when it was a no-op.
    """
    if not prompts:
        return False
    with open(md_path) as f:
        lines = f.read().split("\n")
    if any(line.startswith(PROMPT_SECTION) for line in lines):
        return False

    block = [
        PROMPT_SECTION,
        "",
        "Ready-to-paste build prompts generated from this report's stack — the tools "
        "above, wired into a brief an LLM can act on.",
        "",
    ]
    for title, slug, summary in prompts:
        block.append(f"- **{title}** — {summary}  ")
        block.append(f"  <sub>`prompts/{slug}.md`</sub>")
    block.append("")

    idx = next(
        (i for i, line in enumerate(lines) if line.startswith("## Methodology")),
        len(lines),
    )
    lines[idx:idx] = block
    with open(md_path, "w") as f:
        f.write("\n".join(lines))
    return True
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `python3 -m pytest tests/test_prompt_lib.py -v`
Expected: PASS — 7 passed

- [ ] **Step 6: Commit**

```bash
git add scripts/prompts/__init__.py scripts/prompts/promptlib.py tests/test_prompt_lib.py
git commit -m "feat: prompt library core — stack resolution and cross-link injection"
```

---

### Task 2: The stump-base generator

**Files:**
- Create: `scripts/prompts/stump_base.py`
- Delete: `prompt-tree-stump.md`
- Test: `tests/test_prompt_outputs.py`

**Interfaces:**
- Consumes: `promptlib.resolve_stack`, `promptlib.render_stack_table`, `promptlib.CLASSIFIED` (re-exported from `scripts/reports/lib.py`)
- Produces: `prompts/stump-base.md`, `prompts/stump-base.meta.json`. Meta schema all later tasks depend on:
  `{slug, title, file, report, summary, stack: [{stage, name, stars, health, lifecycle}], brief, generated, generator}`

- [ ] **Step 1: Write the failing test**

Create `tests/test_prompt_outputs.py`:

```python
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED_META_KEYS = {
    "slug", "title", "file", "report", "summary", "stack", "brief", "generated", "generator",
}


def run_generator(name):
    proc = subprocess.run(
        [sys.executable, os.path.join(ROOT, "scripts", "prompts", name)],
        cwd=ROOT, capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stderr
    return proc.stdout


def table_columns_match(md_text):
    lines = md_text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        is_sep = (
            i + 1 < len(lines)
            and lines[i + 1].startswith("|")
            and set(lines[i + 1].replace("|", "").replace(" ", "")) <= {"-", ":"}
            and lines[i + 1].replace("|", "").strip() != ""
        )
        if line.startswith("|") and is_sep:
            n = len(line.strip("|").split("|"))
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                if len(lines[i].strip("|").split("|")) != n:
                    return False
                i += 1
        else:
            i += 1
    return True


def test_stump_base_generates_without_drift():
    out = run_generator("stump_base.py")
    assert "WARNING missing:" not in out
    assert "stack: " in out


def test_stump_base_meta_has_required_keys_and_nonempty_brief():
    run_generator("stump_base.py")
    with open(os.path.join(ROOT, "prompts", "stump-base.meta.json")) as f:
        meta = json.load(f)
    assert REQUIRED_META_KEYS <= set(meta)
    assert meta["report"] == "3d-printing-stack"
    assert len(meta["brief"].strip()) > 500
    assert len(meta["stack"]) >= 3


def test_stump_base_markdown_tables_are_well_formed():
    run_generator("stump_base.py")
    with open(os.path.join(ROOT, "prompts", "stump-base.md")) as f:
        assert table_columns_match(f.read())
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m pytest tests/test_prompt_outputs.py -v`
Expected: FAIL — generator file does not exist, `returncode != 0`

- [ ] **Step 3: Write the generator**

Create `scripts/prompts/stump_base.py`. Copy `BRIEF`, `INPUTS`, `VARIANTS` and `VERIFY` content verbatim from the existing `prompt-tree-stump.md` at the repo root — the wording is already reviewed, only its packaging changes.

```python
#!/usr/bin/env python3
"""Prompt: a tree-stump base for a Pokal, built with the 3d-printing-stack.

Run: python3 scripts/prompts/stump_base.py
"""
import json
import os
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts", "reports"))

from promptlib import CLASSIFIED, render_stack_table, resolve_stack  # noqa: E402

SLUG = "stump-base"
TITLE = "Tree-stump base for a Pokal"
REPORT = "3d-printing-stack"
SUMMARY = ("A naturalistic tree-stump plinth for an existing trophy, sized entirely from "
           "measurements of the trophy it carries.")

STACK = [
    ("Author", "fogleman/sdf"),
    ("See", "f3d-app/f3d"),
    ("Validate", "mikedh/trimesh"),
    ("Slice", "OrcaSlicer/OrcaSlicer"),
]

WHY = ("A stump base is the textbook case for the implicit/SDF route: the form is organic "
       "and irregular (where code-CAD is painful), it needs no support (it is its own flat "
       "base), and SDF output is watertight by construction — so the repair layer never runs.")

INPUTS = [
    ("MOUNT_DIA", "The trophy's spigot, rod or foot where it meets the base", "Sets the socket"),
    ("MOUNT_DEPTH", "How far that spigot can sink in", "Sets socket depth"),
    ("MOUNT_TYPE", "Threaded rod / plain spigot / flat foot", "Decides socket vs. through-hole"),
    ("TROPHY_HEIGHT", "Full height of the trophy alone", "Drives footprint — tall needs wide"),
    ("TROPHY_MASS", "Weigh it", "Decides whether ballast is needed"),
    ("TROPHY_COG", "Roughly how high its mass sits", "Tall, top-heavy cups need more base"),
    ("PLATE_W, PLATE_H", "The engraving plate, if there is one", "Sizes the flat facet"),
]

BRIEF = """You are writing Python that generates a 3D-printable model using the `sdf` library
(`fogleman/sdf`). Output a single script, nothing else. Units are millimetres.

**Model: a naturalistic tree stump that serves as the base of a trophy (Pokal).**
It is not a standalone ornament — it carries an existing trophy, and every dimension is
derived from that trophy rather than chosen.

Begin the script with an input block holding only *measured* values: `MOUNT_DIA`,
`MOUNT_DEPTH`, `MOUNT_TYPE`, `TROPHY_HEIGHT`, `TROPHY_MASS`, `TROPHY_COG`, and optionally
`PLATE_W` / `PLATE_H`. I will fill these in. Everything else must be **computed** from
them, each derived value a named constant with a one-line comment explaining the rule.

Derive the proportions with these rules:

- **Footprint** scales with trophy height and how high its mass sits — a tall or top-heavy
  cup needs a wider stump. Size it so the whole assembly does not tip until it is leaned
  well past any angle a display shelf would see, and state the resulting tip angle in a comment.
- **Stump height** is a visual proportion of the trophy, not a fixed number: tall enough to
  read as a plinth, short enough that the cup stays the subject.
- **Taper** narrows from base to cut face; the cut face must be comfortably wider than
  `MOUNT_DIA` so the socket is not cutting into the rim.

Build these features, in this order:

1. **Trunk body** — a tapered vertical solid with a non-circular cross-section. Modulate
   the radius by angle, and let that irregularity change with height so no two cross-sections
   match. It must read as a real stump, not a noisy cylinder.
2. **Root flare** — the lower portion swells into five or six uneven buttress roots,
   unequally spaced and of differing sizes, blended into the trunk with a smooth union
   (`k=` roughly 4–6) so there is no seam. Roots widen the footprint, so account for them
   in the stability calculation rather than treating them as decoration.
3. **Bark** — vertical ridges over the full height, irregular in spacing and depth, broken
   by a second finer noise so they do not look striped. Relief must be at least 0.8 mm
   peak-to-valley or it will not survive 0.2 mm layers.
4. **Cut face** — flat, level, perpendicular to Z, with a slightly ragged outer edge where
   the bark meets it. Cut concentric growth rings into it, irregularly spaced and off-centre,
   0.6 mm wide and 0.4 mm deep, with two or three fine radial cracks. **Keep the rings clear
   of the socket** — they should read as wood around the mount, not run into it.
5. **Mount socket**, centred on the cut face, according to `MOUNT_TYPE`:
   - *plain spigot* — a blind socket, `MOUNT_DIA` plus 0.3 mm diametral clearance, depth
     `MOUNT_DEPTH` plus 1 mm so it seats on the shoulder and not the floor.
   - *threaded rod* — a through-hole with the same clearance, opening into a hex or
     cylindrical recess in the underside deep enough to take a nut and washer.
   - *flat foot* — a shallow register recess matching the foot outline with 0.3 mm clearance,
     so the trophy locates instead of sliding.
6. **Nameplate facet** — if `PLATE_W` is set, flatten one area of the bark into a smooth
   planar facet a little larger than the plate, tilted slightly upward toward a viewer.
   It must be genuinely flat so the plate sits without rocking, and must not cut so deep
   that it breaks into the interior.
7. **Ballast cavity** — if `TROPHY_MASS` is large enough to matter, hollow the interior
   from the underside into a cavity for sand or steel shot, leaving walls of at least 3 mm
   and keeping the cavity clear of the socket and the nameplate facet. Ballast is far more
   effective than infill for stability because it sits low. If it is not needed, say so in
   a comment and skip it.
8. **Underside** — perfectly flat at z=0, guaranteed by intersecting with a half-space,
   with a shallow recess inset from the edge to take a felt pad.

**Hard printability constraints — these override aesthetics:**

- Nothing may overhang more than 45° from vertical. The root flare is the risk: keep its
  underside sloping outward and down to the base, never undercutting.
- Minimum wall and minimum feature 0.8 mm. No knife edges.
- One connected solid, no floating geometry.
- Print orientation is cut-face-up, as modelled — do not design anything that assumes supports.
- Mesh fine enough to resolve 0.4 mm detail: pass `step=0.25` to `save()`.

Expose every noise seed and ridge parameter as a named constant so the shape can be
re-rolled without touching the body of the code.

Save to `stump_base.stl`. After saving, print the bounding box, the volume, the computed
footprint and the tip angle, so I can check the derivation before printing."""

VARIANTS = [
    ("Multiple places", "Make the cut face a stepped tier with sockets at different heights "
                        "for first, second and third place."),
    ("Broken stump", "Replace the sawn top with a splintered break, the socket set into the "
                     "one intact area. Keep every splinter above 45° from horizontal."),
    ("Integrated plate", "Instead of a facet for a metal plate, emboss the engraving text "
                         "directly, raised 0.6 mm on a flat panel, and expose the text as a constant."),
]

VERIFY = [
    ("generate", "python3 stump_base.py"),
    ("assert on the geometry", """python3 -c "
import trimesh; m = trimesh.load('stump_base.stl')
print('watertight:', m.is_watertight)
print('winding ok :', m.is_winding_consistent)
print('euler      :', m.euler_number)
print('volume cm3 :', round(m.volume/1000, 1))
print('centre of mass:', m.center_mass.round(1))
\""""),
    ("look at it", "f3d stump_base.stl --output=view.png --camera-direction=-1,-1,0.4"),
    ("will it slice", "orca-slicer --export-3mf out.3mf --detect-overhang-wall=1 stump_base.stl"),
]

CLOSING = """`is_watertight` should be `True` first try. If not, the SDF has disjoint components —
usually a root lobe that floated free. Raise the smooth-union `k` rather than reaching for a
repair tool; fixing it at the source keeps the guarantee that made this route worth choosing.

**Test the socket before printing the whole thing.** Slice a 10 mm tall disc containing just
the socket and print that first — a clearance that is wrong costs minutes there and hours on
the full base. FDM shrinkage varies enough between filaments that 0.3 mm is a starting point,
not an answer.

Then show the render and the trimesh numbers back to the model and iterate. That loop, not
the first generation, is where the shape gets good."""


def main():
    with open(CLASSIFIED) as f:
        cl = json.load(f)
    by_name = {r["full_name"]: r for r in cl["repos"]}
    resolved, missing = resolve_stack(STACK, by_name)

    out_md = os.path.join(ROOT, f"prompts/{SLUG}.md")
    out_meta = os.path.join(ROOT, f"prompts/{SLUG}.meta.json")
    os.makedirs(os.path.join(ROOT, "prompts"), exist_ok=True)

    L = []
    L.append(f"# {TITLE}")
    L.append("")
    if missing:
        # Drift is non-fatal at the build level, so the prompt itself has to say
        # so — otherwise a reader pastes a prompt naming a tool that is gone.
        L.append(f"> ⚠ **{len(missing)} tool(s) in this stack no longer resolve in the dataset:** "
                 + ", ".join(f"`{m}`" for m in missing)
                 + ". They were archived, renamed or unstarred. Re-point them in "
                 + f"`scripts/prompts/{os.path.basename(__file__)}` before relying on this prompt.")
        L.append("")
    L.append(f"> Built from the **{REPORT}** report, against {cl['total']:,} starred repos "
             f"(snapshot `{cl.get('generatedAt','')}`). Regenerate any time — no API cost.")
    L.append("")
    L.append(WHY)
    L.append("")
    L.append("## The stack this uses")
    L.append("")
    L.extend(render_stack_table(resolved))
    L.append("")
    L.append("Metrics are live from the dataset. A low health score in geometry libraries "
             "usually means *finished*, not dead — see the parent report's maintenance section.")
    L.append("")
    if INPUTS:
        L.append("## Measure these first")
        L.append("")
        L.append("No dimensions appear in the prompt on purpose. This part carries a trophy "
                 "that already exists, so every size is derived from it.")
        L.append("")
        L.append("| Input | What to measure | Why it drives the shape |")
        L.append("|---|---|---|")
        for name, what, why in INPUTS:
            L.append(f"| `{name}` | {what} | {why} |")
        L.append("")
    L.append("## The prompt")
    L.append("")
    for line in BRIEF.split("\n"):
        L.append(f"> {line}" if line else ">")
    L.append("")
    L.append("## Variants")
    L.append("")
    L.append("Append one of these:")
    L.append("")
    for label, text in VARIANTS:
        L.append(f"- **{label}** — \"{text}\"")
    L.append("")
    L.append("## Verify before you print")
    L.append("")
    for comment, cmd in VERIFY:
        L.append(f"```bash")
        L.append(f"# {comment}")
        L.append(cmd)
        L.append("```")
        L.append("")
    L.append(CLOSING)
    L.append("")
    L.append(f"<sub>Generated by `scripts/prompts/{os.path.basename(__file__)}` · "
             f"parent report: `{REPORT}`</sub>")

    with open(out_md, "w") as f:
        f.write("\n".join(L) + "\n")

    meta = {
        "slug": SLUG,
        "title": TITLE,
        "file": f"{SLUG}.md",
        "report": REPORT,
        "summary": SUMMARY,
        "stack": [
            {"stage": s, "name": n, "stars": r.get("stars"),
             "health": r.get("health_score"), "lifecycle": r.get("lifecycle_stage")}
            for s, n, r in resolved
        ],
        "brief": BRIEF,
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "generator": f"scripts/prompts/{os.path.basename(__file__)}",
    }
    with open(out_meta, "w") as f:
        json.dump(meta, f, indent=2)

    print(f"Wrote {out_md}")
    print(f"Wrote {out_meta}")
    print(f"  stack: {len(resolved)} / {len(STACK)} resolved")
    if missing:
        print("  WARNING missing:", missing)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `python3 -m pytest tests/test_prompt_outputs.py -v`
Expected: PASS — 3 passed

- [ ] **Step 5: Remove the superseded draft**

```bash
git rm --cached prompt-tree-stump.md 2>/dev/null || true
rm -f prompt-tree-stump.md
```

- [ ] **Step 6: Commit**

```bash
git add scripts/prompts/stump_base.py prompts/stump-base.md prompts/stump-base.meta.json tests/test_prompt_outputs.py
git add -u
git commit -m "feat: stump-base prompt generated from the 3d-printing-stack report"
```

---

### Task 3: The prompt build step

**Files:**
- Create: `scripts/prompts/build_prompts.py`
- Test: `tests/test_build_prompts.py`

**Interfaces:**
- Consumes: `promptlib.inject_prompt_links`, `prompts/*.meta.json` from Task 2
- Produces:
  - `run_prompt_generators() -> list[tuple[str, str]]` — returns drift as `[(generator, warning_line)]`, matching `build_index.run_generators()`'s second return value so the two concatenate; raises `RuntimeError` only if a generator exits non-zero
  - `inject_cross_links() -> int` — number of reports modified
  - `build_prompts_index() -> int` — number of prompts indexed
  - `public/prompts/index.json` with shape `{generated, count, prompts: [meta, …]}`

- [ ] **Step 1: Write the failing test**

Create `tests/test_build_prompts.py`:

```python
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts", "prompts"))


def run_build():
    proc = subprocess.run(
        [sys.executable, os.path.join(ROOT, "scripts", "prompts", "build_prompts.py")],
        cwd=ROOT, capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    return proc.stdout


def test_build_writes_public_index_with_briefs():
    run_build()
    with open(os.path.join(ROOT, "public", "prompts", "index.json")) as f:
        index = json.load(f)
    assert index["count"] >= 1
    assert index["count"] == len(index["prompts"])
    for p in index["prompts"]:
        assert p["brief"].strip()
        assert p["report"]


def test_build_copies_markdown_to_public():
    run_build()
    with open(os.path.join(ROOT, "public", "prompts", "index.json")) as f:
        index = json.load(f)
    for p in index["prompts"]:
        assert os.path.exists(os.path.join(ROOT, "public", "prompts", p["file"]))


def test_cross_link_appears_once_after_two_consecutive_runs():
    from promptlib import PROMPT_SECTION
    run_build()
    run_build()
    with open(os.path.join(ROOT, "reports", "3d-printing-stack.md")) as f:
        text = f.read()
    assert text.count(PROMPT_SECTION) == 1
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m pytest tests/test_build_prompts.py -v`
Expected: FAIL — `build_prompts.py` does not exist, `returncode != 0`

- [ ] **Step 3: Write the build step**

Create `scripts/prompts/build_prompts.py`:

```python
#!/usr/bin/env python3
"""Run every prompt generator, index the results, cross-link the parent reports.

Ordering matters: inject_cross_links() edits reports/*.md, and build_index.py's
build() copies those files to public/reports/ in the same loop that injects
charts. So cross-linking must happen BEFORE that copy, or the public copy and
the repo copy silently diverge.

Run: python3 scripts/prompts/build_prompts.py
"""
import glob
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

from promptlib import inject_prompt_links  # noqa: E402

PROMPTS_DIR = os.path.join(ROOT, "prompts")
PUBLIC_DIR = os.path.join(ROOT, "public", "prompts")
REPORTS_DIR = os.path.join(ROOT, "reports")

GENERATORS = [
    "stump_base.py",
]


def run_prompt_generators():
    """Run each generator; collect drift, raise only on hard failure.

    Returns drift as [(generator, warning_line), …] — the same shape
    build_index.run_generators() returns, so the two lists concatenate.
    """
    drift = []
    failures = []
    print("Running prompt generators…")
    for g in GENERATORS:
        path = os.path.join(HERE, g)
        if not os.path.exists(path):
            print(f"  skip (missing): {g}")
            continue
        print(f"  running {g} …")
        proc = subprocess.run([sys.executable, path], cwd=ROOT,
                              capture_output=True, text=True)
        for line in proc.stdout.split("\n"):
            if "WARNING" in line:
                drift.append((g, line.strip()))
                print(f"  ⚠ {g}: {line.strip()}")
        if proc.returncode != 0:
            failures.append((g, proc.stderr.strip()))
            print(f"  ✗ {g} failed")
    if failures:
        raise RuntimeError("prompt generators failed: " + ", ".join(f[0] for f in failures))
    return drift


def load_metas():
    metas = []
    for mp in sorted(glob.glob(os.path.join(PROMPTS_DIR, "*.meta.json"))):
        with open(mp) as f:
            metas.append(json.load(f))
    return metas


def inject_cross_links():
    """Add a prompts section to each parent report. Returns reports modified."""
    by_report = {}
    for meta in load_metas():
        by_report.setdefault(meta["report"], []).append(
            (meta["title"], meta["slug"], meta["summary"])
        )
    modified = 0
    for report_slug, prompts in sorted(by_report.items()):
        md_path = os.path.join(REPORTS_DIR, f"{report_slug}.md")
        if not os.path.exists(md_path):
            print(f"  WARNING: parent report missing for prompts: {report_slug}")
            continue
        if inject_prompt_links(md_path, sorted(prompts)):
            modified += 1
    print(f"  cross-linked {modified} report(s)")
    return modified


def build_prompts_index():
    """Copy prompt markdown to public/ and write the index."""
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    metas = load_metas()
    for meta in metas:
        src = os.path.join(PROMPTS_DIR, meta["file"])
        if os.path.exists(src):
            shutil.copyfile(src, os.path.join(PUBLIC_DIR, meta["file"]))
    metas.sort(key=lambda m: m["slug"])
    index = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "count": len(metas),
        "prompts": metas,
    }
    with open(os.path.join(PUBLIC_DIR, "index.json"), "w") as f:
        json.dump(index, f, indent=2)
    print(f"Wrote public/prompts/index.json ({len(metas)} prompts) + {len(metas)} markdown files")
    return len(metas)


if __name__ == "__main__":
    drift = run_prompt_generators()
    inject_cross_links()
    build_prompts_index()
    if drift:
        # Non-fatal, matching build_index.py's treatment of report drift: a repo
        # going archived upstream is churn, not a broken build. The prompt's own
        # markdown carries a visible banner so a reader cannot miss it.
        print(f"\n⚠ {len(drift)} prompt drift warning(s):")
        for g, line in drift:
            print(f"    {g}: {line}")
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `python3 -m pytest tests/test_build_prompts.py -v`
Expected: PASS — 3 passed

- [ ] **Step 5: Verify the cross-link landed in the real report**

Run: `grep -A4 "Build something with this stack" reports/3d-printing-stack.md`
Expected: the heading, the intro line, and a bullet for **Tree-stump base for a Pokal**

- [ ] **Step 6: Commit**

```bash
git add scripts/prompts/build_prompts.py tests/test_build_prompts.py public/prompts reports/3d-printing-stack.md
git commit -m "feat: prompt build step — index, public copy, report cross-links"
```

---

### Task 4: Wire prompts into the main build

**Files:**
- Modify: `scripts/reports/build_index.py` (the `if __name__ == "__main__":` block at the end)
- Modify: `package.json` (scripts section)

**Interfaces:**
- Consumes: `build_prompts.run_prompt_generators`, `inject_cross_links`, `build_prompts_index` from Task 3
- Produces: a single `python3 scripts/reports/build_index.py` run that produces reports, prompts, cross-links and both indexes in the correct order

- [ ] **Step 1: Read the current entry point**

Run: `tail -20 scripts/reports/build_index.py`
Expected: a `run_generators()` call followed by `build()` inside `if __name__ == "__main__":`

- [ ] **Step 2: Write the failing test**

Append to `tests/test_build_prompts.py`:

```python
def test_full_build_leaves_public_report_and_repo_report_identical():
    """The cross-link must reach public/reports/, not just reports/."""
    proc = subprocess.run(
        [sys.executable, os.path.join(ROOT, "scripts", "reports", "build_index.py")],
        cwd=ROOT, capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    with open(os.path.join(ROOT, "reports", "3d-printing-stack.md")) as f:
        repo_copy = f.read()
    with open(os.path.join(ROOT, "public", "reports", "3d-printing-stack.md")) as f:
        public_copy = f.read()
    assert repo_copy == public_copy
    from promptlib import PROMPT_SECTION
    assert PROMPT_SECTION in public_copy
```

- [ ] **Step 3: Run the test to verify it fails**

Run: `python3 -m pytest tests/test_build_prompts.py::test_full_build_leaves_public_report_and_repo_report_identical -v`
Expected: FAIL — `PROMPT_SECTION in public_copy` is False, because `build_index.py` regenerates reports from scratch and never re-injects

- [ ] **Step 4: Change the entry point**

`run_generators()` returns `(failed, drift)` where `drift` is `[(generator, line)]`.
Keep that contract and keep drift non-fatal. Insert four lines into the existing
`if __name__ == "__main__":` block — do not rewrite the parts that already work.

After the `from lib import …` line near the top of the file, add:

```python
sys.path.insert(0, os.path.join(ROOT, "scripts", "prompts"))
from build_prompts import build_prompts_index, inject_cross_links, run_prompt_generators  # noqa: E402
```

Then, inside `if __name__ == "__main__":`, change these three lines:

```python
    failed, drift = run_generators()
    print("Building index…")
    build()
```

to:

```python
    failed, drift = run_generators()

    # Prompt generators run between the report generators and build(). build()
    # injects charts and copies each report to public/reports/ in the SAME loop,
    # so cross-links must be written before it runs or the public copy silently
    # diverges from the repo copy.
    print("Regenerating prompts…")
    drift += run_prompt_generators()
    inject_cross_links()

    print("Building index…")
    build()
    build_prompts_index()
```

Everything below — the `if drift:` summary and the `if failed:` raise — stays exactly
as it is. Prompt drift now flows into the same summary as report drift, which is the
intended behaviour.

- [ ] **Step 5: Run the test to verify it passes**

Run: `python3 -m pytest tests/test_build_prompts.py -v`
Expected: PASS — 4 passed

- [ ] **Step 6: Add an npm script**

In `package.json`, add to `scripts`:

```json
"test:prompts": "python3 -m pytest tests/ -q"
```

- [ ] **Step 7: Verify the whole pipeline is clean**

Run: `python3 scripts/reports/build_index.py 2>&1 | tail -20 && npm run test:prompts`
Expected: `Wrote public/reports/index.json (27 reports)`, `Wrote public/prompts/index.json (1 prompts)`, no `WARNING`, all pytest tests pass

- [ ] **Step 8: Commit**

```bash
git add scripts/reports/build_index.py package.json tests/test_build_prompts.py
git add reports public/reports public/prompts
git commit -m "feat: run prompt generators inside the main build, before the public copy"
```

---

### Task 5: Two more prompts, from two other reports

**Files:**
- Create: `scripts/prompts/rag_eval_harness.py`
- Create: `scripts/prompts/trading_dashboard.py`
- Modify: `scripts/prompts/build_prompts.py:GENERATORS`
- Test: `tests/test_prompt_outputs.py` (extend)

**Interfaces:**
- Consumes: same `promptlib.resolve_stack` / `promptlib.render_stack_table` contract as Task 2
- Produces: `prompts/rag-eval-harness.*`, `prompts/trading-dashboard.*` with the identical meta schema

- [ ] **Step 1: Confirm the stacks resolve before writing briefs**

Run:
```bash
python3 -c "
import json
d=json.load(open('data/classified.json')); n={r['full_name'] for r in d['repos']}
for c in ['deepset-ai/haystack','qdrant/qdrant','huggingface/sentence-transformers','KRLabsOrg/LettuceDetect','run-llama/llama_index']:
    print(('OK  ' if c in n else 'MISS'), c)
"
```
Expected: every candidate prints `OK`. Replace any `MISS` with a repo that is in `reports/rag-tooling.md`'s taxonomy before continuing — a `MISS` here becomes a build failure later.

- [ ] **Step 2: Repeat the check for the charting stack**

Run:
```bash
python3 -c "
import json
d=json.load(open('data/classified.json')); n={r['full_name'] for r in d['repos']}
import re
md=open('reports/charting-stack.md').read()
for c in sorted(set(re.findall(r'\[([\w.-]+/[\w.-]+)\]\(https://github', md)))[:12]:
    print(('OK  ' if c in n else 'MISS'), c)
"
```
Expected: a list of charting repos with `OK`. Pick four for the stack, one per stage.

- [ ] **Step 3: Write the failing tests**

Append to `tests/test_prompt_outputs.py`:

```python
import pytest


@pytest.mark.parametrize("gen,slug,report", [
    ("rag_eval_harness.py", "rag-eval-harness", "rag-tooling"),
    ("trading_dashboard.py", "trading-dashboard", "charting-stack"),
])
def test_additional_prompts_generate_cleanly(gen, slug, report):
    out = run_generator(gen)
    assert "WARNING missing:" not in out
    with open(os.path.join(ROOT, "prompts", f"{slug}.meta.json")) as f:
        meta = json.load(f)
    assert REQUIRED_META_KEYS <= set(meta)
    assert meta["report"] == report
    assert len(meta["brief"].strip()) > 500
    with open(os.path.join(ROOT, "prompts", f"{slug}.md")) as f:
        assert table_columns_match(f.read())


def test_rag_prompt_has_no_inputs_table():
    """INPUTS=None must render no 'Measure these first' section."""
    run_generator("rag_eval_harness.py")
    with open(os.path.join(ROOT, "prompts", "rag-eval-harness.md")) as f:
        assert "Measure these first" not in f.read()
```

- [ ] **Step 4: Run to verify they fail**

Run: `python3 -m pytest tests/test_prompt_outputs.py -v`
Expected: FAIL — the two new generators do not exist

- [ ] **Step 5: Write `rag_eval_harness.py`**

Copy `scripts/prompts/stump_base.py` as the template and change: `SLUG = "rag-eval-harness"`,
`REPORT = "rag-tooling"`, `INPUTS = None`, and the `STACK` to the four repos confirmed in
Step 1 (stages: `Retrieve`, `Index`, `Embed`, `Judge`).

Guard the inputs block so `INPUTS = None` renders nothing — the `if INPUTS:` in the
Task 2 template already does this; keep it.

`BRIEF` is authored prose, not code — write it against this acceptance checklist, and
verify each line is present before committing:

- [ ] States the deliverable: a retrieval-evaluation harness that loads a document set,
      builds an index, runs a fixed question set, and writes per-question results to CSV.
- [ ] **Separates retrieval quality from generation quality explicitly** — recall@k and
      MRR are retrieval, faithfulness and answer-correctness are generation. Conflating
      them is the standard failure of home-made RAG evals and the brief must forbid
      reporting a single blended score.
- [ ] Requires a fixed random seed, stated as a constant.
- [ ] Requires a `--baseline` flag that runs retrieval with embeddings disabled (keyword
      only), so every score has a floor to be read against. A number with no baseline is
      not a result.
- [ ] Requires the question set to live in a separate file, not inline in the script.
- [ ] Names each tool from `STACK` at the step where it is used.

`VERIFY` should run the harness on a tiny corpus, assert the CSV has one row per
question, and re-run with `--baseline` to confirm the scores drop.

- [ ] **Step 6: Write `trading_dashboard.py`**

Same template. `SLUG = "trading-dashboard"`, `REPORT = "charting-stack"`, `INPUTS = None`,
`STACK` from Step 2 (stages: `Chart`, `Data`, `Layout`, `Serve`).

`BRIEF` is authored prose. Acceptance checklist:

- [ ] States the deliverable: a single-file dashboard rendering OHLC data with a volume
      subplot and a moving average overlay.
- [ ] Requires a shared x-axis across panels, with zoom/pan linked between them.
- [ ] Requires tooltips to show every series at the hovered timestamp, not one series.
- [ ] **Requires correct market-closed gap handling** — no interpolation across weekends
      or holidays. A line drawn through a closed market is a lie about the data.
- [ ] **Requires direction to survive red-green colour blindness** — encode up/down with
      a second channel (fill vs. hollow candles, or shape), not hue alone. This is the
      specific trap in financial charts and roughly 8% of men cannot read the default.
- [ ] Names each tool from `STACK` at the step where it is used.

- [ ] **Step 7: Register both generators**

In `scripts/prompts/build_prompts.py`, extend `GENERATORS`:

```python
GENERATORS = [
    "stump_base.py",
    "rag_eval_harness.py",
    "trading_dashboard.py",
]
```

- [ ] **Step 8: Run the tests to verify they pass**

Run: `python3 -m pytest tests/ -v`
Expected: PASS — all tests pass, including `test_rag_prompt_has_no_inputs_table`

- [ ] **Step 9: Verify all three cross-link correctly**

Run:
```bash
python3 scripts/reports/build_index.py 2>&1 | tail -8
for r in 3d-printing-stack rag-tooling charting-stack; do
  printf "%-22s " "$r"; grep -c "Build something with this stack" reports/$r.md
done
```
Expected: `Wrote public/prompts/index.json (3 prompts)`, and each report prints `1`

- [ ] **Step 10: Commit**

```bash
git add scripts/prompts/ prompts/ public/prompts/ tests/ reports/ public/reports/
git commit -m "feat: add rag-eval-harness and trading-dashboard prompts"
```

---

### Task 6: Extract shared markdown components

**Files:**
- Create: `src/lab/markdownComponents.js`
- Modify: `src/lab/ReportsView.jsx:1-48` (remove the inline `MD_COMPONENTS`, import instead)

**Interfaces:**
- Produces: `export const MD_COMPONENTS` — the react-markdown component map, imported by `ReportsView` and (Task 7) `PromptsView`

- [ ] **Step 1: Create the shared module**

Create `src/lab/markdownComponents.js` containing the exact `MD_COMPONENTS` object
currently in `src/lab/ReportsView.jsx` lines 11–48, unchanged, with `import React from 'react';`
at the top and `export const MD_COMPONENTS = { … };`.

The `img` renderer rewrites `assets/…` to `/reports/assets/…`. Keep that as-is —
prompt markdown has no images, so it is harmless there.

- [ ] **Step 2: Replace the inline copy in ReportsView**

In `src/lab/ReportsView.jsx`, delete the `const MD_COMPONENTS = { … };` block and its
preceding comment, and add to the imports:

```javascript
import { MD_COMPONENTS } from './markdownComponents';
```

- [ ] **Step 3: Verify the build and the Reports tab still work**

Run: `npm run build`
Expected: build succeeds with no unresolved-import errors

- [ ] **Step 4: Commit**

```bash
git add src/lab/markdownComponents.js src/lab/ReportsView.jsx
git commit -m "refactor: extract MD_COMPONENTS so both report and prompt views share it"
```

---

### Task 7: The Prompts tab

**Files:**
- Create: `src/lab/PromptsView.jsx`
- Modify: `src/lab/LabApp.jsx:36-45` (TABS), `:16` (lazy imports), `:399-404` (tab render block)

**Interfaces:**
- Consumes: `markdownComponents.MD_COMPONENTS` (Task 6); `public/prompts/index.json` (Task 3)

- [ ] **Step 1: Write the view**

Create `src/lab/PromptsView.jsx`:

```jsx
import React, { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { MD_COMPONENTS } from './markdownComponents';

function CopyBriefButton({ brief }) {
  const [state, setState] = useState('idle');

  const copy = async () => {
    try {
      await navigator.clipboard.writeText(brief);
      setState('copied');
    } catch {
      setState('failed');
    }
    setTimeout(() => setState('idle'), 2000);
  };

  const label = { idle: 'Copy prompt', copied: 'Copied', failed: 'Press ⌘C' }[state];

  return (
    <button
      onClick={copy}
      className="text-sm bg-blue-600 hover:bg-blue-500 text-white rounded-lg px-4 py-2 transition-colors"
    >
      {label}
    </button>
  );
}

function PromptCard({ prompt, onOpen }) {
  return (
    <button
      onClick={() => onOpen(prompt)}
      className="text-left bg-gray-800/60 hover:bg-gray-800 border border-gray-700 hover:border-blue-500 rounded-xl p-5 transition-colors group flex flex-col"
    >
      <div className="flex items-start justify-between gap-2">
        <span className="text-[11px] uppercase tracking-wide text-blue-400 font-medium">
          {prompt.report}
        </span>
        <span className="text-gray-500 group-hover:text-blue-400 transition-colors">→</span>
      </div>
      <h3 className="text-lg font-semibold text-white mt-1 leading-snug">{prompt.title}</h3>
      <p className="text-sm text-gray-400 mt-2 flex-1">{prompt.summary}</p>
      <div className="flex flex-wrap gap-1.5 mt-4">
        {prompt.stack.map((s) => (
          <span
            key={s.name}
            className="text-[11px] bg-gray-900 border border-gray-700 rounded px-2 py-0.5 text-gray-400"
            title={`${s.stage} · ${s.lifecycle}`}
          >
            {s.name.split('/')[1]}
          </span>
        ))}
      </div>
    </button>
  );
}

function PromptReader({ prompt, onBack }) {
  const [md, setMd] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    let alive = true;
    setMd(null);
    setError(null);
    fetch(`/prompts/${prompt.file}`)
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.text();
      })
      .then((t) => alive && setMd(t))
      .catch((e) => alive && setError(e.message));
    return () => { alive = false; };
  }, [prompt.file]);

  return (
    <div>
      <div className="flex items-center justify-between gap-4 mb-4">
        <button onClick={onBack} className="text-sm text-blue-400 hover:underline inline-flex items-center gap-1">
          ← All prompts
        </button>
        <CopyBriefButton brief={prompt.brief} />
      </div>
      {error && (
        <div className="bg-red-950/40 border border-red-800 rounded-lg p-4 text-red-300 text-sm">
          Couldn’t load this prompt ({error}).
        </div>
      )}
      {!md && !error && (
        <div className="text-gray-400 text-sm flex items-center gap-3">
          <span className="inline-block w-2 h-2 rounded-full bg-blue-400 animate-pulse" />
          Loading prompt…
        </div>
      )}
      {md && (
        <article className="max-w-none bg-gray-900/40 border border-gray-800 rounded-xl p-6">
          <ReactMarkdown remarkPlugins={[remarkGfm]} components={MD_COMPONENTS}>
            {md}
          </ReactMarkdown>
        </article>
      )}
    </div>
  );
}

export default function PromptsView() {
  const [index, setIndex] = useState(null);
  const [error, setError] = useState(null);
  const [open, setOpen] = useState(null);

  useEffect(() => {
    let alive = true;
    fetch('/prompts/index.json')
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then((j) => alive && setIndex(j))
      .catch((e) => alive && setError(e.message));
    return () => { alive = false; };
  }, []);

  if (error) {
    return (
      <div className="bg-red-950/40 border border-red-800 rounded-lg p-4 text-red-300 text-sm">
        Couldn’t load prompts ({error}). Run <code>python3 scripts/reports/build_index.py</code>.
      </div>
    );
  }
  if (!index) return <div className="text-gray-400 text-sm">Loading prompts…</div>;
  if (open) return <PromptReader prompt={open} onBack={() => setOpen(null)} />;

  return (
    <div>
      <p className="text-sm text-gray-400 mb-5 max-w-2xl">
        Build prompts generated from the landscape reports. Each one names the tools its
        parent report selected, with their current metrics, so a prompt that recommends a
        dead tool fails the build instead of failing you.
      </p>
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {index.prompts.map((p) => (
          <PromptCard key={p.slug} prompt={p} onOpen={setOpen} />
        ))}
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Register the lazy import**

In `src/lab/LabApp.jsx`, beside the existing `ReportsView` lazy import (line ~16):

```javascript
const PromptsView = lazy(() => import('./PromptsView'));
```

- [ ] **Step 3: Add the tab**

In the `TABS` array, insert after the `reports` entry:

```javascript
  { key: 'prompts', label: 'Prompts' },
```

- [ ] **Step 4: Render it**

Beside the existing `{tab === 'reports' && …}` block:

```jsx
      {tab === 'prompts' && (
        <Suspense fallback={<TabFallback label="prompts" />}>
          <PromptsView />
        </Suspense>
      )}
```

- [ ] **Step 5: Build and check**

Run: `npm run build`
Expected: build succeeds

- [ ] **Step 6: Verify in the running app**

Run: `npm run dev`
Then open `http://localhost:5173/?tab=prompts` and confirm: three cards render; clicking
one opens the markdown; **Copy prompt** changes to **Copied**; pasting into a text editor
yields the brief text starting `You are writing Python that generates a 3D-printable model`
and containing no `| Stage | Tool |` table.

- [ ] **Step 7: Commit**

```bash
git add src/lab/PromptsView.jsx src/lab/LabApp.jsx
git commit -m "feat: Prompts tab with copy-to-clipboard"
```

---

## Done criteria

- `python3 scripts/reports/build_index.py` completes with no `WARNING` lines and writes both `public/reports/index.json` (27 reports) and `public/prompts/index.json` (3 prompts).
- `npm run test:prompts` passes.
- `npm run build` succeeds.
- Each of the three parent reports contains exactly one `## Build something with this stack` section, and `reports/<slug>.md` is byte-identical to `public/reports/<slug>.md`.
- The `Prompts` tab lists three prompts; the copy button places only the brief on the clipboard.
