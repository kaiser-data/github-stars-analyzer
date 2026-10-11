#!/usr/bin/env python3
"""
Assemble the Astrolab landing-page mockups into self-contained HTML files.

  src/shared.css   one stylesheet, inlined into every page
  src/*.html       page bodies with {{TOKENS}}
  ../../..         repo data: data/classified.json, data/snapshots/, public/data/graph.json,
                   docs/screenshots/*.jpg

Every number on the pages is computed here from the repo data, so re-running after a
data refresh updates the mockups. Prices, product names and the package name are
placeholders and are marked as such on the pages.

Run: python3 docs/mockups/landing/build.py
"""
import base64
import json
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "src")

PAGES = {
    "index.html": ("Astrolab", "brass", None),
    "picker.html": ("Astrolab Picker", "brass", "picker"),
    "atlas.html": ("Astrolab Atlas", "atlas", "atlas"),
    "almanac.html": ("Astrolab Almanac", "almanac", "almanac"),
    "survey.html": ("Astrolab Survey", "survey", "survey"),
}
NAV = [
    ("picker", "picker.html", "Picker", "brass"),
    ("atlas", "atlas.html", "Atlas", "atlas"),
    ("almanac", "almanac.html", "Almanac", "almanac"),
    ("survey", "survey.html", "Survey", "survey"),
]
LOGO = (
    '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true">'
    '<circle cx="16" cy="17" r="12"/><circle cx="16" cy="17" r="7.5"/>'
    '<path d="M16 2v3M6 27l20-20" stroke-linecap="round"/><circle cx="16" cy="17" r="1.6" fill="currentColor"/></svg>'
)


def load(path):
    with open(os.path.join(ROOT, path)) as f:
        return json.load(f)


def fmt(n):
    return f"{n:,}"


def img(name):
    with open(os.path.join(ROOT, "docs/screenshots", name), "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()


def pill(stage):
    cls = {"Declining": "bad", "Abandoned": "bad", "Hot": "acc", "Rising": "acc"}.get(stage, "good")
    return f'<span class="pill {cls}">{stage}</span>'


def nav(active):
    cur = ' aria-current="page"'
    items = "".join(
        f'<li><a href="{href}" style="--c:var(--{c})"{cur if key == active else ""}>'
        f'<span class="dot"></span>{label}</a></li>'
        for key, href, label, c in NAV
    )
    return (
        f'<nav class="nav"><div class="frame"><a class="brand" href="index.html">{LOGO}Astrolab</a>'
        f"<ul>{items}</ul></div></nav>"
    )


FOOTER = (
    '<footer><div class="frame">'
    '<a class="brand" href="index.html">' + LOGO + "Astrolab</a>"
    '<div class="row"><a href="picker.html">Picker</a><a href="atlas.html">Atlas</a>'
    '<a href="almanac.html">Almanac</a><a href="survey.html">Survey</a>'
    '<a href="index.html#trust">Trust policy</a><a href="index.html#method">Method</a></div>'
    '<p class="small">Mockup built {built} from the github-stars-analyzer dataset (snapshot {snap}). '
    "Product names, prices and the package name are placeholders. Every repo figure is real.</p>"
    "</div></footer>"
)


def compute():
    cls = load("data/classified.json")
    repos = cls["repos"]
    by_name = {r["full_name"]: r for r in repos}
    snaps = sorted(os.listdir(os.path.join(ROOT, "data/snapshots")))
    latest = load(f"data/snapshots/{snaps[-1]}")["repos"]
    # Compare against the snapshot closest to 4 weeks earlier.
    prev_name = snaps[-1]
    for s in reversed(snaps[:-1]):
        prev_name = s
        if (int(snaps[-1][5:7]) * 31 + int(snaps[-1][8:10])) - (int(s[5:7]) * 31 + int(s[8:10])) >= 28:
            break
    prev = load(f"data/snapshots/{prev_name}")["repos"]

    settings = []
    for k, v in latest.items():
        a = prev.get(k)
        if a and v["lifecycle_stage"] in ("Declining", "Abandoned") and a["lifecycle_stage"] not in ("Declining", "Abandoned"):
            settings.append((v["stars"], k, a["lifecycle_stage"], v["lifecycle_stage"], a["health_score"], v["health_score"], v["days_since_push"]))
    settings.sort(reverse=True)
    risings = sorted(
        ((v["stars"] - prev[k]["stars"], k, v["stars"], v["lifecycle_stage"]) for k, v in latest.items() if k in prev),
        reverse=True,
    )

    g = load("public/data/graph.json")
    pts = []
    for n in g["nodes"]:
        try:
            pts.append([
                round(float(n["x"])), round(float(n["y"])), round(float(n["z"])),
                int(float(n["stars"])), n["lifecycle_stage"][0], n["full_name"],
            ])
        except (KeyError, ValueError, TypeError):
            continue

    memory = []
    t = open(os.path.join(ROOT, "reports/agent-memory.md")).read()
    sec = t[t.index("## Maintenance & risk"):t.index("**Slowing")]
    for line in sec.splitlines():
        if line.startswith("| `"):
            c = [x.strip() for x in line.split("|")[1:-1]]
            memory.append({"name": c[0].strip("`"), "cat": c[1], "health": int(c[2]), "stage": c[3],
                           "push": c[5], "bus": int(c[6]), "top": c[7]})

    reports = [f for f in os.listdir(os.path.join(ROOT, "reports")) if f.endswith(".meta.json")]
    stages = {}
    for r in repos:
        stages[r["lifecycle_stage"]] = stages.get(r["lifecycle_stage"], 0) + 1
    return dict(
        repos=repos, by_name=by_name, snaps=snaps, prev_name=prev_name, settings=settings,
        risings=risings, pts=pts, memory=memory, n_reports=len(reports), stages=stages,
        n_comm=g["stats"]["communityCount"],
    )


def tokens(d):
    repos, by = d["repos"], d["by_name"]
    dying = d["stages"].get("Declining", 0) + d["stages"].get("Abandoned", 0)
    snap_latest, snap_prev = d["snaps"][-1][:-5], d["prev_name"][:-5]

    def r(name, key):
        return by[name][key] if name in by else "—"

    settings_rows = "".join(
        f'<tr><td><span class="repo">{k}</span></td><td class="num">{fmt(st)}</td>'
        f'<td>{a} → {pill(b)}</td><td class="num">{ha} → {hb}</td><td class="num">{dp} d</td></tr>'
        for st, k, a, b, ha, hb, dp in d["settings"][:8]
    )
    risings_rows = "".join(
        f'<tr><td><span class="repo">{k}</span></td><td class="num">+{fmt(gain)}</td>'
        f'<td class="num">{fmt(st)}</td><td>{pill(stage)}</td></tr>'
        for gain, k, st, stage in d["risings"][:8]
    )
    mem = d["memory"]
    mem_counts = {}
    for m in mem:
        mem_counts[m["stage"]] = mem_counts.get(m["stage"], 0) + 1
    order = ["Rising", "Hot", "Mature", "Classic", "Declining", "Abandoned"]
    colors = {"Rising": "var(--brass)", "Hot": "var(--warn)", "Mature": "var(--atlas)", "Classic": "var(--good)",
              "Declining": "var(--almanac)", "Abandoned": "var(--bad)"}
    bar = "".join(
        f'<div style="flex:{mem_counts[s]};background:{colors[s]}" title="{s}: {mem_counts[s]}"></div>'
        for s in order if mem_counts.get(s)
    )
    legend = "".join(
        f'<span><i style="background:{colors[s]}"></i>{s} <b>{mem_counts[s]}</b></span>'
        for s in order if mem_counts.get(s)
    )
    single = [m for m in mem if m["bus"] <= 1]
    risk_rows = "".join(
        f'<tr><td><span class="repo">{m["name"]}</span></td><td>{m["cat"]}</td><td class="num">{m["health"]}</td>'
        f'<td>{pill(m["stage"])}</td><td class="num">{m["push"]}</td><td class="num">{m["top"]}</td></tr>'
        for m in sorted(mem, key=lambda m: m["health"])[:6]
    )

    def card(name):
        x = by.get(name, {})
        return {"health": x.get("health_score", "—"), "stage": x.get("lifecycle_stage", "—"),
                "stars": fmt(x["stars"]) if x else "—", "bus": x.get("bus_factor", "—"),
                "push": x.get("days_since_push", "—")}

    picks = {n: card(n) for n in ["topoteretes/cognee", "qdrant/qdrant", "getzep/graphiti", "mem0ai/mem0",
                                  "memvid/memvid", "shaneholloman/mcp-knowledge-graph"]}

    import datetime
    t = {
        "N_REPOS": fmt(len(repos)),
        "N_DYING": fmt(dying),
        "PCT_DYING": str(round(100 * dying / len(repos))),
        "N_REPORTS": str(d["n_reports"]),
        "N_SNAPS": str(len(d["snaps"])),
        "N_COMM": str(d["n_comm"]),
        "FIRST_SNAP": d["snaps"][0][:-5],
        "SNAP": snap_latest,
        "SNAP_PREV": snap_prev,
        "N_SETTINGS": str(len(d["settings"])),
        "SETTINGS_ROWS": settings_rows,
        "RISINGS_ROWS": risings_rows,
        "MEM_N": str(len(mem)),
        "MEM_BAR": bar,
        "MEM_LEGEND": legend,
        "MEM_SINGLE": str(len(single)),
        "MEM_RISK_ROWS": risk_rows,
        "STARS_JSON": json.dumps(d["pts"], separators=(",", ":")),
        "BUILT": datetime.date.today().isoformat(),
    }
    for n, c in picks.items():
        key = n.split("/")[1].upper().replace("-", "_")
        for f, v in c.items():
            t[f"{key}_{f.upper()}"] = str(v)
    for f in ["01-map.jpg", "04-risk.jpg", "07-reports.jpg", "06-compare.jpg"]:
        t["IMG_" + f.split("-")[0]] = img(f)
    return t


def main():
    d = compute()
    t = tokens(d)
    css = open(os.path.join(SRC, "shared.css")).read()
    for out, (title, accent, active) in PAGES.items():
        body = open(os.path.join(SRC, out)).read()
        body = body.replace("{{NAV}}", nav(active)).replace(
            "{{FOOTER}}", FOOTER.format(built=t["BUILT"], snap=t["SNAP"]))
        body = re.sub(r"\{\{([A-Z0-9_]+)\}\}", lambda m: t.get(m.group(1), m.group(0)), body)
        left = re.findall(r"\{\{[A-Z0-9_]+\}\}", body)
        if left:
            raise SystemExit(f"{out}: unresolved tokens {sorted(set(left))}")
        html = (
            "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
            f"<title>{title}</title>\n<style>\n{css}\n:root {{ --accent: var(--{accent}); }}\n</style>\n</head>\n"
            f"<body>\n{body}\n</body>\n</html>\n"
        )
        with open(os.path.join(HERE, out), "w") as f:
            f.write(html)
        print(f"wrote {out} ({len(html) // 1024} KB)")


if __name__ == "__main__":
    main()
