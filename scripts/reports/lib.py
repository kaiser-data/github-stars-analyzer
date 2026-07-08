"""
Shared helpers for the report generators in scripts/reports/.

Every generator reads the same two inputs and formats repo metrics the same
way — this module is the single home for that logic. Generators import it as
a sibling module (`from lib import …`), which works because build_index.py
runs each generator as a standalone script (sys.path[0] = this directory).
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLASSIFIED = os.path.join(ROOT, "data/classified.json")
GRAPH = os.path.join(ROOT, "public/data/graph.json")
SNAPSHOT_DIR = os.path.join(ROOT, "data/snapshots")

# Per-repo fields archived by snapshot.py for trend comparisons.
SNAPSHOT_FIELDS = [
    "stars", "forks", "open_issues", "health_score", "lifecycle_stage",
    "days_since_push", "archived", "commits_90d", "unique_authors_90d",
]


def load_data():
    """Return (classified, graph) dicts — the two inputs every report uses."""
    with open(CLASSIFIED) as f:
        cl = json.load(f)
    with open(GRAPH) as f:
        gr = json.load(f)
    return cl, gr


def make_node_for(nodes_by_id, name_to_nodeid):
    """Build the node_for(full_name) lookup used in graph-analysis sections."""
    def node_for(name):
        nid = name_to_nodeid.get(name)
        return nodes_by_id.get(nid) if nid else None
    return node_for


def fmt_int(n):
    try:
        return f"{int(n):,}"
    except Exception:
        return str(n)


_BASELINE = "unloaded"


def baseline_snapshot():
    """The snapshot to diff against: second-newest in data/snapshots/.

    build_index.py snapshots the current data vintage before generators run,
    so the newest snapshot always mirrors classified.json itself and the one
    before it is the previous refresh. Returns (date, {full_name: fields}) or
    (None, {}) when there is no history yet.
    """
    global _BASELINE
    if _BASELINE == "unloaded":
        try:
            files = sorted(f for f in os.listdir(SNAPSHOT_DIR) if f.endswith(".json"))
        except FileNotFoundError:
            files = []
        if len(files) >= 2:
            with open(os.path.join(SNAPSHOT_DIR, files[-2])) as f:
                snap = json.load(f)
            _BASELINE = (snap["date"], snap["repos"])
        else:
            _BASELINE = (None, {})
    return _BASELINE


def star_delta(r):
    """(delta, baseline_date) vs the previous snapshot, or None if no history."""
    date, base = baseline_snapshot()
    prev = base.get(r["full_name"])
    if prev is None or prev.get("stars") is None:
        return None
    return r["stars"] - prev["stars"], date


def fmt_stars(r):
    """Star count with a trend marker when snapshot history exists.

    e.g. "12,345 (▲210)" — used in master-comparison tables; falls back to
    plain fmt_int before the second snapshot lands.
    """
    s = fmt_int(r["stars"])
    sd = star_delta(r)
    if sd and sd[0]:
        d, _ = sd
        s += f" ({'▲' if d > 0 else '▼'}{fmt_int(abs(d))})"
    return s


def _esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg_hbar(title, items, width=680):
    """Dependency-free horizontal bar chart as an SVG string.

    items: [(label, numeric value)] — single series, direct-labeled, so no
    legend/axis. Colors adapt to light/dark via a media query inside the SVG,
    which applies even when the file is loaded through <img> (GitHub included).
    Hues are the dataviz reference palette (validated: slot-1 blue both modes).
    """
    pad, title_h, bar_h, gap, label_w, value_w = 14, 40, 18, 9, 244, 78
    n = len(items)
    height = title_h + n * (bar_h + gap) - gap + pad
    bar_max = width - label_w - value_w - pad
    vmax = max((v for _, v in items), default=0) or 1

    def bar(x, y, w, h, r=4):
        if w <= r:  # too short to round — plain sliver
            return f'<rect x="{x}" y="{y}" width="{max(w, 1):.1f}" height="{h}" class="bar"/>'
        return (f'<path d="M{x},{y} h{w - r:.1f} q{r},0 {r},{r} v{h - 2 * r} '
                f'q0,{r} -{r},{r} h-{w - r:.1f} z" class="bar"/>')

    rows = []
    y = title_h
    for label, v in items:
        lbl = label if len(label) <= 32 else label[:31] + "…"
        w = bar_max * v / vmax
        cy = y + bar_h / 2
        rows.append(f'<text x="{label_w - 8}" y="{cy:.1f}" class="lbl" text-anchor="end" '
                    f'dominant-baseline="central">{_esc(lbl)}</text>')
        rows.append(bar(label_w, y, w, bar_h))
        rows.append(f'<text x="{label_w + w + 6:.1f}" y="{cy:.1f}" class="val" '
                    f'dominant-baseline="central">{fmt_int(v)}</text>')
        y += bar_h + gap

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{_esc(title)}">
<style>
text{{font-family:system-ui,-apple-system,'Segoe UI',sans-serif}}
.srf{{fill:#fcfcfb;stroke:#e4e4e0}}.ttl{{fill:#0b0b0b;font-size:13.5px;font-weight:600}}
.lbl{{fill:#52514e;font-size:11.5px}}.val{{fill:#0b0b0b;font-size:11.5px;font-weight:600}}
.bar{{fill:#2a78d6}}
@media(prefers-color-scheme:dark){{
.srf{{fill:#1a1a19;stroke:#33332f}}.ttl{{fill:#ffffff}}
.lbl{{fill:#c3c2b7}}.val{{fill:#ffffff}}.bar{{fill:#3987e5}}
}}
</style>
<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="8" class="srf"/>
<text x="{pad}" y="25" class="ttl">{_esc(title)}</text>
{chr(10).join(rows)}
</svg>'''


def newly_archived(r):
    """True if the repo is archived now but wasn't in the baseline snapshot."""
    _, base = baseline_snapshot()
    prev = base.get(r["full_name"])
    return bool(r.get("archived")) and prev is not None and not prev.get("archived")


def days_to_human(d):
    if d is None:
        return "?"
    d = int(d)
    if d < 30:
        return f"{d}d"
    if d < 365:
        return f"{d//30}mo"
    return f"{d/365:.1f}y"


def activity_label(r):
    dsp = r.get("days_since_push")
    c90 = r.get("commits_90d") or 0
    if dsp is None:
        return "unknown"
    if dsp <= 30 and c90 >= 20:
        return "very active"
    if dsp <= 60:
        return "active"
    if dsp <= 180:
        return "slowing"
    return "stale"
