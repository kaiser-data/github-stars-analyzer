#!/usr/bin/env python3
"""
Render a generated report's markdown into a standalone, self-contained HTML page.

The markdown in reports/ stays the source of truth; this is a presentation layer
over it, so a data refresh regenerates the page for free. Everything is inlined
(CSS + the chart SVGs) so the file works offline and survives a strict CSP.

Only the markdown subset the generators actually emit is supported: headings,
blockquote intro, tables, list items, images, and inline bold/code/links.

Run: python3 scripts/reports/render_html.py charting-stack --title "Chartography"
"""
import argparse
import html
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Lifecycle / activity values get rendered as state pills rather than bare text —
# the master tables are scanned, not read, so state should register at a glance.
STATE_CLASS = {
    "Hot": "s-hot", "Rising": "s-hot",
    "Classic": "s-good", "Mature": "s-good",
    "very active": "s-good", "active": "s-good",
    "Declining": "s-warn", "slowing": "s-warn",
    "Abandoned": "s-crit", "stale": "s-crit",
    "unknown": "s-mute",
}

# Split a table row on unescaped pipes only — "ES\|QL" must stay one cell.
CELL_SPLIT = re.compile(r"(?<!\\)\|")


def inline_md(s):
    """Inline markdown → HTML. Code spans are protected from other rules."""
    spans = []

    def stash(m):
        spans.append(m.group(1))
        return f"\x00{len(spans) - 1}\x00"

    s = re.sub(r"`([^`]+)`", stash, s)
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
               lambda m: f'<a href="{html.escape(m.group(2), quote=True)}" '
                         f'target="_blank" rel="noopener">{m.group(1)}</a>', s)
    # Bold before italic, and non-greedy — bold spans may contain *nested* italics.
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    s = re.sub(r"(?<!\w)_([^_]+)_(?!\w)", r"<em>\1</em>", s)
    s = s.replace("\\|", "|")
    s = re.sub(r"\x00(\d+)\x00",
               lambda m: f"<code>{html.escape(spans[int(m.group(1))], quote=False)}</code>", s)
    return s


def cell(text):
    """A table cell, with bare state words promoted to pills."""
    t = text.strip()
    cls = STATE_CLASS.get(t)
    if cls:
        return f'<td><span class="pill {cls}">{html.escape(t)}</span></td>'
    return f"<td>{inline_md(t)}</td>"


def read_svg(path):
    """Inline an SVG file, stripped of its XML prolog."""
    with open(path, encoding="utf-8") as f:
        svg = f.read()
    return re.sub(r"^<\?xml[^>]*\?>\s*", "", svg.strip())


def convert(md, slug):
    out = []
    lines = md.split("\n")
    i = 0
    intro = []
    in_list = False

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    while i < len(lines):
        ln = lines[i]

        # Chart images → inline SVG (external refs are blocked by the CSP)
        m = re.match(r"!\[([^\]]*)\]\((assets/[^)]+)\)", ln.strip())
        if m:
            close_list()
            p = os.path.join(ROOT, "reports", m.group(2))
            if os.path.exists(p):
                out.append(f'<figure class="chart">{read_svg(p)}</figure>')
            i += 1
            continue

        if ln.startswith("> "):
            intro.append(ln[2:].strip())
            i += 1
            continue
        if ln.strip() == ">":
            intro.append("")
            i += 1
            continue

        # Tables
        if ln.startswith("|") and i + 1 < len(lines) and re.fullmatch(
                r"\|(\s*-{3,}\s*\|)+", lines[i + 1].strip()):
            close_list()
            heads = [c for c in CELL_SPLIT.split(ln)[1:-1]]
            out.append('<div class="tw"><table><thead><tr>'
                       + "".join(f"<th>{inline_md(h.strip())}</th>" for h in heads)
                       + "</tr></thead><tbody>")
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                cells = CELL_SPLIT.split(lines[j])[1:-1]
                out.append("<tr>" + "".join(cell(c) for c in cells) + "</tr>")
                j += 1
            out.append("</tbody></table></div>")
            i = j
            continue

        if ln.startswith("### "):
            close_list()
            out.append(f"<h3>{inline_md(ln[4:])}</h3>")
        elif ln.startswith("## "):
            close_list()
            out.append(f"<h2>{inline_md(ln[3:])}</h2>")
        elif ln.startswith("# "):
            pass  # the title lives in the hero
        elif re.match(r"^\s*- ", ln):
            depth = (len(ln) - len(ln.lstrip())) // 2
            if not in_list:
                out.append("<ul>")
                in_list = True
            item = inline_md(re.sub(r"^\s*- ", "", ln).rstrip())
            out.append(f'<li class="d{min(depth, 2)}">{item}</li>')
        elif ln.strip().startswith("<sub>"):
            close_list()
            out.append(f'<p class="fine">{inline_md(re.sub(r"</?sub>", "", ln.strip()))}</p>')
        elif ln.strip() == "":
            close_list()
        else:
            close_list()
            out.append(f"<p>{inline_md(ln)}</p>")
        i += 1

    close_list()
    return "\n".join(out), inline_md(" ".join(x for x in intro if x))


CSS = """
:root{
  --ground:#f7f8fa; --panel:#ffffff; --rule:#dde2ea; --hair:#e9edf3;
  --ink:#12161c; --ink-2:#4a5462; --ink-3:#727c8b;
  --accent:#2a78d6; --accent-soft:#e8f0fb;
  --good:#1a7f4b; --good-bg:#e6f4ec;
  --warn:#8a5a00; --warn-bg:#fbf0da;
  --crit:#a52f2f; --crit-bg:#fbe9e9;
  --hot:#1f5fa8; --hot-bg:#e4eefb;
  --display:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
  --body:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#0e1116; --panel:#161b22; --rule:#2b333e; --hair:#222a34;
    --ink:#eef2f7; --ink-2:#b3bdca; --ink-3:#8592a2;
    --accent:#3987e5; --accent-soft:#16283f;
    --good:#5fd39a; --good-bg:#13291f;
    --warn:#e0b25f; --warn-bg:#2c2416;
    --crit:#f08b8b; --crit-bg:#2e1a1a;
    --hot:#7fb2f0; --hot-bg:#152438;
  }
}
:root[data-theme="dark"]{
  --ground:#0e1116; --panel:#161b22; --rule:#2b333e; --hair:#222a34;
  --ink:#eef2f7; --ink-2:#b3bdca; --ink-3:#8592a2;
  --accent:#3987e5; --accent-soft:#16283f;
  --good:#5fd39a; --good-bg:#13291f;
  --warn:#e0b25f; --warn-bg:#2c2416;
  --crit:#f08b8b; --crit-bg:#2e1a1a;
  --hot:#7fb2f0; --hot-bg:#152438;
}
*{box-sizing:border-box}
body{
  margin:0; background:var(--ground); color:var(--ink);
  font-family:var(--body); font-size:16px; line-height:1.65;
  /* graph-paper ground: the subject's own material */
  background-image:linear-gradient(var(--hair) 1px,transparent 1px),
                   linear-gradient(90deg,var(--hair) 1px,transparent 1px);
  background-size:28px 28px;
}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px 96px}
header.hero{padding:72px 0 40px;border-bottom:2px solid var(--ink);margin-bottom:8px}
.eyebrow{
  font-family:var(--mono);font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--accent);margin:0 0 18px
}
h1{
  font-family:var(--display);font-weight:600;line-height:1.04;
  font-size:clamp(2.9rem,7vw,5.1rem);letter-spacing:-.022em;
  margin:0 0 6px;text-wrap:balance
}
.sub{
  font-family:var(--display);font-style:italic;color:var(--ink-2);
  font-size:clamp(1.05rem,2.2vw,1.4rem);margin:0 0 28px;max-width:62ch
}
.intro{color:var(--ink-2);font-size:14.5px;max-width:78ch;margin:0}
.intro code{font-size:12.5px}
.stats{display:flex;flex-wrap:wrap;gap:10px 40px;margin:30px 0 0;padding:0;list-style:none}
.stats div{display:flex;flex-direction:column}
.stats b{
  font-family:var(--display);font-size:1.9rem;font-weight:600;
  font-variant-numeric:tabular-nums;line-height:1.1
}
.stats span{
  font-family:var(--mono);font-size:10.5px;letter-spacing:.11em;
  text-transform:uppercase;color:var(--ink-3)
}
h2{
  font-family:var(--display);font-weight:600;font-size:clamp(1.5rem,3vw,2.05rem);
  letter-spacing:-.014em;margin:64px 0 4px;padding-top:16px;
  border-top:1px solid var(--rule);position:relative;text-wrap:balance
}
/* tick mark on the section axis — a plotting device, not decoration */
h2::before{content:"";position:absolute;top:-1px;left:0;width:52px;height:3px;background:var(--accent)}
h3{
  font-family:var(--body);font-weight:650;font-size:.85rem;letter-spacing:.1em;
  text-transform:uppercase;color:var(--accent);margin:40px 0 10px
}
p{margin:0 0 14px;max-width:82ch}
ul{margin:0 0 16px;padding:0;list-style:none;max-width:84ch}
li{position:relative;padding-left:18px;margin-bottom:7px;color:var(--ink-2)}
li::before{content:"";position:absolute;left:2px;top:.68em;width:6px;height:1.5px;background:var(--accent)}
li.d1{margin-left:22px;font-size:14.6px}
li.d2{margin-left:44px;font-size:14.2px}
li strong,p strong{color:var(--ink);font-weight:640}
a{color:var(--accent);text-decoration:none;border-bottom:1px solid transparent}
a:hover{border-bottom-color:var(--accent)}
a:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:2px}
code{
  font-family:var(--mono);font-size:.855em;background:var(--accent-soft);
  color:var(--ink);padding:.1em .34em;border-radius:3px
}
.tw{
  overflow-x:auto;margin:0 0 26px;border:1px solid var(--rule);border-radius:6px;
  background:var(--panel)
}
table{border-collapse:collapse;width:100%;font-size:13.4px;min-width:640px}
thead th{
  position:sticky;top:0;z-index:1;background:var(--panel);
  text-align:left;vertical-align:bottom;padding:11px 13px;
  font-family:var(--mono);font-size:10.5px;letter-spacing:.075em;text-transform:uppercase;
  color:var(--ink-3);border-bottom:1.5px solid var(--ink);white-space:nowrap
}
tbody td{
  padding:11px 13px;border-bottom:1px solid var(--hair);
  vertical-align:top;color:var(--ink-2);font-variant-numeric:tabular-nums
}
tbody tr:last-child td{border-bottom:0}
tbody tr:hover td{background:var(--accent-soft)}
td strong{color:var(--ink)}
td:first-child{min-width:150px}
.pill{
  display:inline-block;padding:2px 8px;border-radius:11px;
  font-family:var(--mono);font-size:10.5px;letter-spacing:.045em;white-space:nowrap
}
.s-good{background:var(--good-bg);color:var(--good)}
.s-warn{background:var(--warn-bg);color:var(--warn)}
.s-crit{background:var(--crit-bg);color:var(--crit)}
.s-hot{background:var(--hot-bg);color:var(--hot)}
.s-mute{background:var(--hair);color:var(--ink-3)}
.chart{
  margin:22px 0 30px;padding:16px;background:var(--panel);
  border:1px solid var(--rule);border-radius:6px;overflow-x:auto
}
.chart svg{max-width:100%;height:auto;display:block}
.fine{
  font-family:var(--mono);font-size:11.5px;color:var(--ink-3);
  margin-top:36px;padding-top:14px;border-top:1px solid var(--rule)
}
@media (max-width:640px){
  header.hero{padding:44px 0 30px}
  .wrap{padding:0 16px 64px}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--title", default=None, help="display title (defaults to the h1)")
    ap.add_argument("--tagline", default="")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    md_path = os.path.join(ROOT, "reports", f"{a.slug}.md")
    with open(md_path, encoding="utf-8") as f:
        md = f.read()

    h1 = next((x[2:].strip() for x in md.split("\n") if x.startswith("# ")), a.slug)
    title = a.title or h1
    body, intro = convert(md, a.slug)

    import json
    meta_path = os.path.join(ROOT, "reports", f"{a.slug}.meta.json")
    meta = json.load(open(meta_path, encoding="utf-8")) if os.path.exists(meta_path) else {}
    tools = meta.get("tool_count", "")
    stars = f"{meta.get('total_stars', 0):,}" if meta.get("total_stars") else ""
    layers = len([v for v in (meta.get("categories") or {}).values() if v])
    snap = (meta.get("snapshot") or "")[:10]

    stats = ""
    if tools:
        stats = (f'<div class="stats">'
                 f'<div><b>{tools}</b><span>tools compared</span></div>'
                 f'<div><b>{stars}</b><span>combined stars</span></div>'
                 f'<div><b>{layers}</b><span>layers</span></div>'
                 f'<div><b>{snap}</b><span>data vintage</span></div>'
                 f'</div>')

    out = f"""<title>{html.escape(title)}</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>{CSS}</style>
<div class="wrap">
<header class="hero">
  <p class="eyebrow">Landscape report · github-stars-analyzer</p>
  <h1>{html.escape(title)}</h1>
  <p class="sub">{html.escape(a.tagline or h1)}</p>
  <p class="intro">{intro}</p>
  {stats}
</header>
{body}
</div>
"""
    dest = a.out or os.path.join(ROOT, "reports", f"{a.slug}.html")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"Wrote {dest}  ({len(out):,} bytes)")


if __name__ == "__main__":
    main()
