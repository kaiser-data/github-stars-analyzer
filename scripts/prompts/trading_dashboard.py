#!/usr/bin/env python3
"""Prompt: a single-file OHLC trading dashboard, built with the charting-stack.

Run: python3 scripts/prompts/trading_dashboard.py
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

SLUG = "trading-dashboard"
TITLE = "OHLC trading dashboard"
REPORT = "charting-stack"
SUMMARY = ("A single-file OHLC dashboard with a linked volume subplot and moving-average "
           "overlay, built to avoid the two classic trading-chart bugs: interpolated "
           "market-closed gaps and hue-only direction encoding.")

STACK = [
    ("Chart", "apache/echarts"),
    ("Data", "Kanaries/pygwalker"),
    ("App", "Avaiga/taipy"),
]

WHY = ("Financial charts fail in ways that are easy to miss in a demo and expensive to miss "
       "in front of a trader: a line quietly drawn across a weekend implies trading that "
       "never happened, and a candle whose only up/down signal is red-vs-green is unreadable "
       "to a meaningful share of viewers. This prompt makes both failure modes explicit "
       "requirements rather than things to notice later.")

INPUTS = None

BRIEF = """You are writing Python that builds a single-file, single-process trading
dashboard for OHLC (open/high/low/close) price data. Output one script, nothing else.

**Deliverable:** a dashboard rendering candlestick OHLC data with a volume subplot below
it and a moving-average overlay on the price panel. It must run as one file with one
command — no separate build step, no external services beyond the packages imported.

**Shared x-axis, linked zoom and pan.** The price panel and the volume panel share one
time axis. Zooming or panning on either panel must move the other in lock-step — a
trader reading volume against price at the same instant, not two independently-scrolling
charts that happen to sit on the same page. Wire this through the charting library's own
axis-linking mechanism rather than reimplementing it by hand with callbacks.

**Tooltips must show every series at the hovered timestamp, not one series.** Hovering
anywhere on the time axis shows open, high, low, close, volume, and the moving-average
value together in one tooltip, aligned to that single x position. A tooltip that shows
only whichever series happens to be under the cursor forces the reader to hover multiple
times to compare values that belong together.

**Handle market-closed gaps correctly — do not interpolate across them.** Do not treat
the time axis as a continuous calendar. Weekends, exchange holidays, and any other
session with no trades must produce a visible gap or a compressed skip in the axis, never
a straight line drawn between the last tick before the closure and the first tick after
it. A line through a closed market implies price movement that did not happen and is
data the source never recorded — it is a lie about the data. Build the x-axis from the
list of actual trading timestamps present in the data (a category axis, or an explicit
skip-list of closed dates) rather than from a uniform time interval that assumes every
day traded.

**Direction must survive red-green colour blindness — do not encode it with hue alone.**
Up/down candles must be distinguishable by a second, non-colour channel: use filled vs.
hollow (or outlined) candle bodies as the primary encoding, with colour as a secondary
reinforcement only. Roughly 8% of men have red-green colour vision deficiency and cannot
reliably read a chart where the only signal is red-vs-green hue; a shape or fill
difference remains legible to them. Apply this same fill/hollow rule consistently in
both the candle body and any legend swatches — never introduce a legend that is itself
hue-only after the chart body got the fix.

**Build, naming each tool where it is used:**

1. **Data** — use `Kanaries/pygwalker` to load and reshape the raw OHLC+volume rows
   (from CSV or an in-memory dataframe) into the tidy per-timestamp structure the chart
   layer consumes, including the trading-timestamp list used for the gap handling above.
2. **Chart** — use `apache/echarts` (via its Python binding) to render the candlestick
   price panel, the linked volume bar panel, and the moving-average line overlay, with
   the shared/linked x-axis (`axisPointer` link group or equivalent) and the combined
   tooltip wired at this layer.
3. **App** — use `Avaiga/taipy` to host the chart in a single-process web app: one
   Python entry point, a page containing the chart component, and a `taipy.Gui(...).run()`
   call that is the only thing needed to view it locally.

Compute the moving average (state the window, e.g. `MA_WINDOW = 20`, as a constant) over
the same trading-timestamp list as the price series, so the overlay has no points on
closed-market gaps either.

Keep styling minimal: a light and dark variant of the colour pair is fine, but the
fill/hollow distinction must be present in both."""

VARIANTS = [
    ("Multiple symbols", "Add a symbol selector that swaps the whole dataset and re-renders "
                         "all three panels without losing the current zoom range."),
    ("Bollinger bands", "Add a second overlay band (rolling mean ± k·rolling std) as a "
                        "shaded region on the price panel, computed over the same "
                        "trading-timestamp list as the moving average."),
    ("Intraday", "Switch the time axis from daily bars to intraday bars and extend the "
                "gap handling to skip overnight and lunch-break closures, not just "
                "weekends and holidays."),
]

VERIFY = [
    ("run it", "python3 trading_dashboard.py --csv sample_ohlc.csv"),
    ("check for interpolated gaps", """python3 -c "
import pandas as pd
df = pd.read_csv('sample_ohlc.csv', parse_dates=['date'])
gaps = df['date'].diff().dt.days
print('max gap (days):', gaps.max())
print('weekend-sized gaps present:', (gaps >= 3).any())
\""""),
    ("look at it", "open http://localhost:5000  # taipy's default GUI port"),
]

CLOSING = """If the chart draws a diagonal line across every weekend, the x-axis is a
continuous time scale rather than the trading-timestamp category axis the brief asks for —
fix it at the axis definition, not by hiding the line with styling.

Check the candle-direction encoding with a colour-blindness simulator (or just convert a
screenshot to grayscale) before calling this done. If up and down candles become
indistinguishable in grayscale, the fill/hollow channel did not actually get wired in and
the chart is still hue-only underneath."""


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
    L.append("Metrics are live from the dataset. A low health score in charting libraries "
             "usually means *finished*, not dead — see the parent report's maintenance section.")
    L.append("")
    if INPUTS:
        L.append("## Measure these first")
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
