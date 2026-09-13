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

# TODO: the three generators' main() functions (stump_base.py, rag_eval_harness.py,
# trading_dashboard.py) are near-identical renderers over their authored constants.
# Extracting a shared renderer here was considered and deliberately deferred —
# narrow scope for this wave — so this stays follow-up debt, not an oversight.


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
