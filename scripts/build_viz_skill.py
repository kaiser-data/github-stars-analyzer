#!/usr/bin/env python3
"""
Generate the reference files for the global `choosing-viz-tools` skill.

The skill lives outside this repo (~/.claude/skills/choosing-viz-tools) so it
works while you are building a dashboard in some other project. That means its
facts are baked in rather than read live — this script is how they get baked,
and re-baked after a data refresh.

Two inputs, both already trustworthy:

  reports/charting-stack.md  hand-curated capability prose (advantages,
                             disadvantages, best-for) + the ranked use cases
  data/classified.json       live metrics: stars, health, lifecycle, licence

Do NOT try to rebuild the capability prose by scraping readme_text. Verified:
regex over READMEs reports `svg` for Chart.js (canvas-only), Grafana, Metabase
and Superset because it matches shields.io badge URLs, not capability claims.
The curated report is the source of truth for what a tool *does*; the dataset
only says how healthy it is.

Run: python3 scripts/build_viz_skill.py [--skill-dir PATH]
"""
import argparse
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT = os.path.join(ROOT, "reports/charting-stack.md")
CLASSIFIED = os.path.join(ROOT, "data/classified.json")
DEFAULT_SKILL_DIR = os.path.expanduser("~/.claude/skills/choosing-viz-tools")

JOBS_START = "<!-- GENERATED:JOBS -->"
JOBS_END = "<!-- /GENERATED:JOBS -->"

# The report's job labels are written to be read in prose; here they are scanned
# in a lookup table that sits in the always-loaded SKILL.md, so they are worth
# compressing. Keyed by a distinctive fragment of the original label.
JOB_SHORT = {
    "Standard business charts": "standard web charts (line/bar/pie)",
    "React app with minimal": "react app, minimal effort",
    "Dense dashboards": "dense dashboard, >10k points",
    "Fully bespoke": "bespoke / one-of-a-kind",
    "Financial": "financial / trading",
    "geospatial": "geospatial, large scale",
    "Publication-quality": "publication figures (Python)",
    "Exploratory analysis in a notebook": "notebook exploration",
    "Zero-code exploration": "zero-code DataFrame poking",
    "described as data": "spec-driven / LLM-generated",
    "ML model demo": "ML demo UI in an afternoon",
    "survive production": "Python data app, production",
    "Self-service BI": "self-service BI, non-technical",
    "Warehouse-scale": "warehouse-scale BI, data team",
    "reviewed in git": "BI as code, git-reviewed",
    "Infrastructure metrics": "infra metrics & alerting",
    "Log-centric": "log troubleshooting",
    "Natural-language questions": "natural-language → charts",
    "write actions": "internal tool, charts + writes",
    "desktop .NET": "desktop .NET",
    "native iOS": "native iOS / macOS",
    "Go or C++ service": "Go / C++ service, no browser",
    "Presentable tables": "presentable tables, not charts",
    "flow diagrams": "architecture / flow diagrams",
}


def shorten(job):
    for frag, label in JOB_SHORT.items():
        if frag in job:
            return label
    return job.lower()

# --------------------------------------------------------------------------
# Maintenance labels.
#
# health_score alone cannot separate "finished" from "dead" — both look like a
# low commit rate. These overrides carry that judgment, and are the reason the
# skill is worth more than a live query. Only tools whose label would surprise
# you are listed; everything else is derived by RULE below.
#
#   Stable  API-frozen and widely depended on. Low churn means done, not dead.
#   Slowing usable, but pin the version and watch it.
#   Stalled never a first pick. Named as the reason.
# --------------------------------------------------------------------------
OVERRIDE = {
    "d3/d3": ("Stable", "Feature-complete and API-frozen since v7; the reference "
                        "implementation everything else is built on. Low commit "
                        "rate here means finished."),
    "chartjs/Chart.js": ("Stable", "Mature and deliberately small in scope; the "
                                   "plugin ecosystem absorbs most feature demand "
                                   "rather than the core."),
    "matplotlib/matplotlib": ("Stable", "The Python publication standard, under "
                                        "NumFOCUS governance. Slow by design."),
    "c3js/c3": ("Stable", "Effectively feature-frozen. Fine for codebases already "
                          "on it — not a new-project choice."),
    "leeoniya/uPlot": ("Stable", "Deliberately finished: a small, focused "
                                 "time-series renderer. But bus factor 0 — one "
                                 "author, no succession."),
    "gonum/plot": ("Stable", "Low-churn Go plotting under the Gonum umbrella. "
                             "Static output, little surface to break."),
    # Downgrades — these look healthier than they are.
    "core-plot/core-plot": ("Slowing", "Dated API and Apple's own Swift Charts now "
                                       "covers most of its ground natively."),
    "getredash/redash": ("Slowing", "Commits continue, but the project is widely "
                                    "read as being in maintenance mode — feature "
                                    "work has moved elsewhere."),
}

# Derived when a tool is not in OVERRIDE. Ordered — first match wins.
def rule_label(r):
    push = r.get("days_since_push") or 0
    if r["lifecycle_stage"] == "Abandoned" or push > 180 or r["health_score"] < 20:
        return "Stalled", f"{push}d since push, health {r['health_score']}."
    if push > 90 or r["lifecycle_stage"] == "Declining" or (r.get("bus_factor") or 0) == 0:
        return "Slowing", (f"{push}d since push, bus factor "
                           f"{r.get('bus_factor')}.")
    return "Active", ""


# Licence traps, from the report's Licensing traps section. Attached to the
# tool entry so they arrive with the pick rather than in a file nobody reads.
TRAP = {
    "highcharts/highcharts": "**Proprietary for commercial use** — per-developer "
                             "paid licence, not an open-source dependency.",
    "AAChartModel/AAChartKit": "**Wraps Highcharts** and inherits its commercial "
                               "licence. The most commonly missed trap here.",
    "grafana/grafana": "AGPL open-core: self-hosting is free, but SSO and "
                       "fine-grained permissions are enterprise-only.",
    "metabase/metabase": "AGPL open-core: SSO, permissions and some embedding "
                         "features are enterprise-only.",
    "elastic/kibana": "Elastic Licence / SSPL — not OSI-approved, and rejected "
                      "outright by some corporate policies.",
}


def load():
    with open(REPORT) as f:
        md = f.read()
    with open(CLASSIFIED) as f:
        cl = json.load(f)
    by_full = {r["full_name"]: r for r in cl["repos"]}
    by_short = {}
    for r in cl["repos"]:
        by_short.setdefault(r["name"].lower(), r)
    return md, by_full, by_short


def parse_capabilities(md):
    """[(full_name, layer, advantages, disadvantages, best_for)] from the report."""
    sec = md.split("## Advantages, disadvantages & use cases")[1] \
            .split("\n## Use-case rankings")[0]
    layer, out = None, []
    for line in sec.splitlines():
        if line.startswith("### "):
            layer = line[4:].strip()
        elif line.startswith("| **["):
            cells = [c.strip() for c in line.split("|")]
            m = re.search(r"\*\*\[([\w\-./]+)\]", cells[1])
            if m:
                out.append((m.group(1), layer, cells[3], cells[4], cells[5]))
    return out


def parse_jobs(md, by_full, by_short, labels):
    """[(job, [full_name, ...])] from the ranked use-case table."""
    sec = md.split("## Use-case rankings")[1].split("\n## Master comparison")[0]
    jobs = []
    for line in sec.splitlines():
        if not line.startswith("|") or "---" in line or "Use case" in line:
            continue
        cells = [c.strip() for c in line.split("|")]
        job = re.sub(r"\*\*", "", cells[1]).strip()
        picks = []
        for cell in cells[2:5]:
            m = re.search(r"`([\w\-./]+)`", cell)
            if not m:
                continue
            name = m.group(1)
            r = by_full.get(name) or by_short.get(name.split("/")[-1].lower())
            if r:
                picks.append(r["full_name"])
        if job and picks:
            jobs.append((job, picks))
    return jobs


def short(full_name):
    """Display name — unambiguous but not repo-path verbose."""
    owner, name = full_name.split("/")
    return name if name.lower() not in ("plot", "charts", "xy") else full_name


def write_detail(path, caps, by_full, labels):
    lines = [
        "# Tool detail",
        "",
        "One anchored entry per tool. **Never read this file whole** (~4,300 "
        "tokens) — pull only the tools on your shortlist:",
        "",
        "```",
        "grep -A6 '^## owner/repo' references/detail.md",
        "```",
        "",
    ]
    for full, layer, adv, dis, best in sorted(caps, key=lambda c: c[0].lower()):
        r = by_full[full]
        label, why = labels[full]
        lic = r.get("license") or "no licence file"
        lines.append(f"## {full}")
        lines.append(
            f"{layer} · {r['stars']:,}★ · {r.get('primary_language') or '—'} · {lic} "
            f"· **{label}**{(' — ' + why) if why else ''}"
        )
        lines.append(f"- ✅ {adv}")
        lines.append(f"- ⚠️ {dis}")
        lines.append(f"- 🎯 {best}")
        if full in TRAP:
            lines.append(f"- 🚩 {TRAP[full]}")
        lines.append("")
    with open(path, "w") as f:
        f.write("\n".join(lines))
    return len(caps)


def write_tsv(path, caps, by_full, labels):
    """Off-menu routing table. Read only when no job row matches."""
    head = ("tool\tlayer\tlang\tlicence\tstars\tmaint\thealth\tpush_days\tbus")
    rows = [head]
    for full, layer, *_ in sorted(caps, key=lambda c: -by_full[c[0]]["stars"]):
        r = by_full[full]
        rows.append("\t".join([
            full, layer, r.get("primary_language") or "-",
            r.get("license") or "none", str(r["stars"]), labels[full][0],
            str(r["health_score"]), str(r.get("days_since_push")),
            str(r.get("bus_factor")),
        ]))
    with open(path, "w") as f:
        f.write("\n".join(rows) + "\n")
    return len(rows) - 1


def write_evidence(md, path):
    """Benchmark citations + licence traps. Read only when a pick is challenged."""
    ranks = md.split("## Use-case rankings")[1].split("\n## Master comparison")[0]
    traps = md.split("## Licensing traps")[1].split("\n## ")[0]
    spot = md.split("## Spotlight:")[1].split("\n## ")[0]
    with open(path, "w") as f:
        f.write("# Evidence\n\nWhy the rankings are ordered the way they are. "
                "Read only when a pick is challenged or the case is unusual.\n\n"
                "## Ranked use cases, with evidence\n" + ranks +
                "\n## Licensing traps\n" + traps +
                "\n## Spotlight:" + spot)


def write_jobs_block(skill_md, jobs, labels):
    """Rewrite the generated job map inside the hand-written SKILL.md."""
    flag = {"Stalled": "✗", "Slowing": "~", "Stable": "=", "Active": ""}
    lines = [JOBS_START, "```"]
    rows = [(shorten(job), picks) for job, picks in jobs]
    width = max(len(j) for j, _ in rows)
    for job, picks in rows:
        rendered = [short(p) + flag[labels[p][0]] for p in picks]
        lines.append(f"{job:<{width}}  {' > '.join(rendered)}")
    lines.append("```")
    lines.append("")
    lines.append("`✗` Stalled — never a first pick.  `~` Slowing — usable, pin it.  "
                 "`=` Stable — finished, not dead.")
    lines.append(JOBS_END)
    block = "\n".join(lines)

    with open(skill_md) as f:
        src = f.read()
    if JOBS_START not in src:
        raise SystemExit(f"{skill_md} is missing the {JOBS_START} marker")
    out = re.sub(re.escape(JOBS_START) + r".*?" + re.escape(JOBS_END),
                 lambda _: block, src, flags=re.S)
    with open(skill_md, "w") as f:
        f.write(out)
    return len(jobs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill-dir", default=DEFAULT_SKILL_DIR)
    args = ap.parse_args()

    md, by_full, by_short = load()
    caps = parse_capabilities(md)

    labels = {}
    for full, *_ in caps:
        labels[full] = OVERRIDE.get(full) or rule_label(by_full[full])

    jobs = parse_jobs(md, by_full, by_short, labels)

    refs = os.path.join(args.skill_dir, "references")
    os.makedirs(refs, exist_ok=True)

    n_detail = write_detail(os.path.join(refs, "detail.md"), caps, by_full, labels)
    n_tsv = write_tsv(os.path.join(refs, "tools.tsv"), caps, by_full, labels)
    write_evidence(md, os.path.join(refs, "evidence.md"))
    n_jobs = write_jobs_block(os.path.join(args.skill_dir, "SKILL.md"), jobs, labels)

    counts = {}
    for label, _ in labels.values():
        counts[label] = counts.get(label, 0) + 1
    print(f"tools: {n_detail}   jobs: {n_jobs}   tsv rows: {n_tsv}")
    print("maintenance: " + "  ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    stalled = sorted(f for f, (label, _) in labels.items() if label == "Stalled")
    print("stalled (never a first pick): " + ", ".join(short(s) for s in stalled))
    for size, name in sorted(
        ((os.path.getsize(os.path.join(refs, n)), n) for n in os.listdir(refs)),
        reverse=True,
    ):
        print(f"  {name:<14} {size:>7,} bytes  ~{size // 4:,} tokens")


if __name__ == "__main__":
    main()
