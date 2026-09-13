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
    "rag_eval_harness.py",
    "trading_dashboard.py",
]


def run_prompt_generators():
    """Run each generator; collect drift and failures, raise on neither.

    Returns (drift, failed) — drift as [(generator, warning_line), …] and
    failed as [generator, …] — the same shapes build_index.run_generators()
    returns, so the two lists concatenate in the caller.

    A single crashing generator must not abort the run: this function is
    called before inject_cross_links() and build() in build_index.py's
    __main__, and raising here used to skip both — leaving reports/*.md
    rewritten (cross-links stripped) but public/reports/ never updated, on
    top of whatever the crash itself broke. Failures are collected and left
    for the caller to surface once the rest of the build has completed,
    mirroring run_generators()'s own isolation contract.
    """
    drift = []
    failed = []
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
            line = line.strip()
            if line.startswith("WARNING"):
                drift.append((g, line))
                print(f"  ⚠ {g}: {line}")
        if proc.returncode != 0:
            tail = (proc.stderr or "").strip().splitlines()[-3:]
            print(f"  ✗ FAILED: {g} (exit {proc.returncode})")
            for line in tail:
                print(f"      {line}")
            failed.append(g)
    return drift, failed


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
    kept = []
    for meta in load_metas():
        src = os.path.join(PROMPTS_DIR, meta["file"])
        if not os.path.exists(src):
            print(f"  WARNING: {meta['file']} missing for {meta['slug']}, skipping")
            continue
        shutil.copyfile(src, os.path.join(PUBLIC_DIR, meta["file"]))
        kept.append(meta)
    metas = kept
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
    drift, failed = run_prompt_generators()
    inject_cross_links()
    build_prompts_index()
    if drift:
        # Non-fatal, matching build_index.py's treatment of report drift: a repo
        # going archived upstream is churn, not a broken build. The prompt's own
        # markdown carries a visible banner so a reader cannot miss it.
        print(f"\n⚠ {len(drift)} prompt drift warning(s):")
        for g, line in drift:
            print(f"    {g}: {line}")
    if failed:
        raise SystemExit(
            f"\n✗ {len(failed)} prompt generator(s) failed: {', '.join(failed)}\n"
            "  The other prompts and the index were still rebuilt."
        )
