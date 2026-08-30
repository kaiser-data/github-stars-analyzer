#!/usr/bin/env python3
"""
Build the reports index consumed by the web app's Reports tab.

- Regenerates every report (runs each generator) so meta + markdown are fresh.
- Copies reports/<slug>.md into public/reports/<slug>.md (served as static assets).
- Aggregates reports/*.meta.json into public/reports/index.json.

Run: python3 scripts/reports/build_index.py
"""
import glob
import json
import os
import shutil
import subprocess
import sys

from lib import svg_hbar

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
REPORTS_DIR = os.path.join(ROOT, "reports")
ASSETS_DIR = os.path.join(REPORTS_DIR, "assets")
PUBLIC_DIR = os.path.join(ROOT, "public/reports")

GENERATORS = [
    "memory_frameworks.py",
    "agent_memory.py",
    "llm_evaluation.py",
    "rag_tooling.py",
    "mcp_tooling.py",
    "openclaw_ecosystem.py",
    "token_savings.py",
    "agent_orchestration.py",
    "hermes_vs_openclaw.py",
    "which_claw.py",
    "blockchain_claws.py",
    "blockchain_essentials.py",
    "voice_agents.py",
    "local_vs_infra_stack.py",
    "meeting_transcription.py",
    "claude_code_setups.py",
    "ai_engineer_stack.py",
    "notebooklm_stack.py",
    "agent_harnesses.py",
    "document_extraction.py",
    "ai_coding_tuis.py",
    "agentic_terminals.py",
    "jetson_inference.py",
    "finetuning_stack.py",
    "trending_now.py",
    "charting_stack.py",
]

def run_generators():
    """Run every generator, then report the ones that failed and the ones that drifted.

    A single crashing generator used to abort the whole build, leaving the other
    22 reports stale. Now each one is isolated: the rest still regenerate and the
    index is still rebuilt, but the failures are collected and re-raised at the
    end so a broken generator can never pass silently.

    Generators also print `WARNING …` on stdout when a curated `TAXONOMY` key is
    no longer in the dataset — a repo renamed upstream, archived (and so dropped
    by sample.mjs), or unstarred. That detection has always worked; this runner
    sent its stdout to DEVNULL, so every warning was discarded by the only thing
    that ever runs the generators. Six entries drifted unnoticed that way. The
    warnings are surfaced per-generator now and summarised by the caller.

    Returns (failed, drift) where drift is [(generator, warning line), …].
    """
    failed = []
    drift = []
    for g in GENERATORS:
        path = os.path.join(HERE, g)
        if not os.path.exists(path):
            print(f"  skip (missing): {g}")
            continue
        print(f"  running {g} …")
        proc = subprocess.run([sys.executable, path], cwd=ROOT,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              text=True)
        if proc.returncode != 0:
            tail = (proc.stderr or "").strip().splitlines()[-3:]
            print(f"  ✗ FAILED: {g} (exit {proc.returncode})")
            for line in tail:
                print(f"      {line}")
            failed.append(g)
            continue
        for line in (proc.stdout or "").splitlines():
            line = line.strip()
            if line.startswith("WARNING"):
                print(f"  ⚠ {g}: {line}")
                drift.append((g, line))
    return failed, drift

def created_date(md_file):
    """First git commit date (YYYY-MM-DD) of a report's markdown.

    `generated` is bumped on every rebuild; `created` stays fixed at the date
    the report first entered the repo. Returns None for untracked (brand-new)
    reports — the caller falls back to today's `generated`.
    """
    try:
        out = subprocess.run(
            ["git", "log", "--follow", "--diff-filter=A", "--format=%ad",
             "--date=short", "--", f"reports/{md_file}"],
            capture_output=True, text=True, cwd=ROOT, check=True,
        ).stdout.split()
        return out[-1] if out else None
    except (subprocess.CalledProcessError, OSError):
        return None


def make_charts(meta):
    """Render at-a-glance SVGs from a report's meta. Returns md image lines.

    Chart titles and the top-chart series default to the star-ranked landscape
    framing every taxonomy report uses. A report whose subject isn't "biggest
    tools" (e.g. trending-now, which ranks by star *gain*) can override them
    with `chart_top_title` / `chart_top_series` / `chart_cat_title`.
    """
    imgs = []
    series = ([(s["name"], s["value"]) for s in meta.get("chart_top_series") or []]
              or [(t["name"], t["stars"]) for t in meta.get("top_tools") or []
                  if t.get("stars")])
    top_title = meta.get("chart_top_title") or "Top tools by stars"
    if len(series) >= 3:
        svg = svg_hbar(top_title, series)
        name = f"{meta['slug']}-top-tools.svg"
        with open(os.path.join(ASSETS_DIR, name), "w") as f:
            f.write(svg)
        imgs.append(f"![{top_title}](assets/{name})")
    cats = {k: v for k, v in (meta.get("categories") or {}).items() if v}
    cat_title = meta.get("chart_cat_title") or "Tools per category"
    if len(cats) >= 3:
        items = sorted(cats.items(), key=lambda x: -x[1])
        svg = svg_hbar(cat_title, items)
        name = f"{meta['slug']}-categories.svg"
        with open(os.path.join(ASSETS_DIR, name), "w") as f:
            f.write(svg)
        imgs.append(f"![{cat_title}](assets/{name})")
    return imgs


def inject_charts(md_path, imgs):
    """Insert chart images after the intro blockquote of a generated report."""
    with open(md_path) as f:
        lines = f.read().split("\n")
    if not imgs or any("](assets/" in l for l in lines):
        return
    # skip the H1, then the first blockquote block; insert after its blank line
    i = 0
    while i < len(lines) and not lines[i].startswith(">"):
        i += 1
    while i < len(lines) and lines[i].startswith(">"):
        i += 1
    block = [""] + [x for img in imgs for x in (img, "")]
    lines[i:i] = block
    with open(md_path, "w") as f:
        f.write("\n".join(lines))


def build():
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    os.makedirs(ASSETS_DIR, exist_ok=True)
    metas = []
    for mp in sorted(glob.glob(os.path.join(REPORTS_DIR, "*.meta.json"))):
        with open(mp) as f:
            meta = json.load(f)
        md_src = os.path.join(REPORTS_DIR, meta["file"])
        if not os.path.exists(md_src):
            print(f"  WARNING: {meta['file']} missing for {meta['slug']}, skipping")
            continue
        # Stable creation date (first commit) alongside the rolling `generated`;
        # persisted into the sidecar so the app can sort by it.
        meta["created"] = created_date(meta["file"]) or meta.get("created") or meta["generated"]
        with open(mp, "w") as f:
            json.dump(meta, f, indent=2)
        inject_charts(md_src, make_charts(meta))
        shutil.copyfile(md_src, os.path.join(PUBLIC_DIR, meta["file"]))
        metas.append(meta)

    # charts referenced by the markdown live in assets/ next to it
    if os.path.isdir(ASSETS_DIR):
        shutil.copytree(ASSETS_DIR, os.path.join(PUBLIC_DIR, "assets"),
                        dirs_exist_ok=True)

    # Sort by tool_count desc so the biggest landscapes lead.
    metas.sort(key=lambda m: -m.get("tool_count", 0))
    index = {
        "generated": metas[0]["generated"] if metas else None,
        "count": len(metas),
        "reports": metas,
    }
    with open(os.path.join(PUBLIC_DIR, "index.json"), "w") as f:
        json.dump(index, f, indent=2)
    print(f"Wrote public/reports/index.json ({len(metas)} reports) "
          f"+ {len(metas)} markdown files")

if __name__ == "__main__":
    print("Snapshotting dataset…")
    subprocess.run([sys.executable, os.path.join(HERE, "snapshot.py")],
                   check=True, cwd=ROOT)
    print("Regenerating reports…")
    failed, drift = run_generators()
    print("Building index…")
    build()
    if drift:
        # Not fatal: a curated repo going archived or renamed is normal upstream
        # churn, not a broken build. It does need a human to re-point or retire
        # the entry, so it gets its own summary rather than one line lost among
        # 26 generator logs.
        print(f"\n⚠ {len(drift)} curation drift warning(s):")
        for g, line in drift:
            print(f"    {g}: {line}")
        print("  Drift runs both ways — a curated entry that left the dataset "
              "(renamed, archived, unstarred), or a gap-table entry that has since "
              "been starred and now needs promoting into TAXONOMY.")
        print("  See docs/HANDOFF-2026-08-28.md §3 on renames.")
    if failed:
        raise SystemExit(
            f"\n✗ {len(failed)} generator(s) failed: {', '.join(failed)}\n"
            "  The other reports and the index were still rebuilt."
        )
