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

def make_charts(meta):
    """Render at-a-glance SVGs from a report's meta. Returns md image lines."""
    imgs = []
    top = [t for t in meta.get("top_tools") or [] if t.get("stars")]
    if len(top) >= 3:
        svg = svg_hbar("Top tools by stars", [(t["name"], t["stars"]) for t in top])
        name = f"{meta['slug']}-top-tools.svg"
        with open(os.path.join(ASSETS_DIR, name), "w") as f:
            f.write(svg)
        imgs.append(f"![Top tools by stars](assets/{name})")
    cats = {k: v for k, v in (meta.get("categories") or {}).items() if v}
    if len(cats) >= 3:
        items = sorted(cats.items(), key=lambda x: -x[1])
        svg = svg_hbar("Tools per category", items)
        name = f"{meta['slug']}-categories.svg"
        with open(os.path.join(ASSETS_DIR, name), "w") as f:
            f.write(svg)
        imgs.append(f"![Tools per category](assets/{name})")
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
    run_generators()
    print("Building index…")
    build()
