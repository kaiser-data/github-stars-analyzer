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

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
REPORTS_DIR = os.path.join(ROOT, "reports")
PUBLIC_DIR = os.path.join(ROOT, "public/reports")

GENERATORS = [
    "memory_frameworks.py",
    "llm_evaluation.py",
    "rag_tooling.py",
    "mcp_tooling.py",
    "openclaw_ecosystem.py",
]

def run_generators():
    for g in GENERATORS:
        path = os.path.join(HERE, g)
        if not os.path.exists(path):
            print(f"  skip (missing): {g}")
            continue
        print(f"  running {g} …")
        subprocess.run([sys.executable, path], check=True, cwd=ROOT,
                       stdout=subprocess.DEVNULL)

def build():
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    metas = []
    for mp in sorted(glob.glob(os.path.join(REPORTS_DIR, "*.meta.json"))):
        with open(mp) as f:
            meta = json.load(f)
        md_src = os.path.join(REPORTS_DIR, meta["file"])
        if not os.path.exists(md_src):
            print(f"  WARNING: {meta['file']} missing for {meta['slug']}, skipping")
            continue
        shutil.copyfile(md_src, os.path.join(PUBLIC_DIR, meta["file"]))
        metas.append(meta)

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
    print("Regenerating reports…")
    run_generators()
    print("Building index…")
    build()
