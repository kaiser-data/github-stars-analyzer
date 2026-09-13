# OHLC trading dashboard

> Built from the **charting-stack** report, against 2,140 starred repos (snapshot `2026-09-12T16:25:05.965Z`). Regenerate any time — no API cost.

Financial charts fail in ways that are easy to miss in a demo and expensive to miss in front of a trader: a line quietly drawn across a weekend implies trading that never happened, and a candle whose only up/down signal is red-vs-green is unreadable to a meaningful share of viewers. This prompt makes both failure modes explicit requirements rather than things to notice later.

## The stack this uses

| Stage | Tool | Stars | Health | Lifecycle |
|---|---|---|---|---|
| Chart | [`tradingview/lightweight-charts`](https://github.com/tradingview/lightweight-charts) | 17,186 | 72 | Classic |
| App | [`streamlit/streamlit`](https://github.com/streamlit/streamlit) | 45,699 | 83 | Classic |

Metrics are live from the dataset.

## The prompt

> You are writing Python that builds a single-file, single-process trading
> dashboard for OHLC (open/high/low/close) price data. Output one script, nothing else.
>
> **Deliverable:** a dashboard rendering candlestick OHLC data with a volume subplot below
> it and a moving-average overlay on the price panel. It must run as one file with one
> command — no separate build step, no external services beyond the packages imported.
>
> **Shared x-axis, linked zoom and pan.** The price panel and the volume panel share one
> time axis. Zooming or panning on either panel must move the other in lock-step — a
> trader reading volume against price at the same instant, not two independently-scrolling
> charts that happen to sit on the same page. Wire this through the charting library's own
> axis-linking mechanism rather than reimplementing it by hand with callbacks.
>
> **Tooltips must show every series at the hovered timestamp, not one series.** Hovering
> anywhere on the time axis shows open, high, low, close, volume, and the moving-average
> value together in one tooltip, aligned to that single x position. A tooltip that shows
> only whichever series happens to be under the cursor forces the reader to hover multiple
> times to compare values that belong together.
>
> **Handle market-closed gaps correctly — do not interpolate across them.** Do not treat
> the time axis as a continuous calendar. Weekends, exchange holidays, and any other
> session with no trades must produce a visible gap or a compressed skip in the axis, never
> a straight line drawn between the last tick before the closure and the first tick after
> it. A line through a closed market implies price movement that did not happen and is
> data the source never recorded — it is a lie about the data. Build the x-axis from the
> list of actual trading timestamps present in the data (a category axis, or an explicit
> skip-list of closed dates) rather than from a uniform time interval that assumes every
> day traded.
>
> **Direction must survive red-green colour blindness — do not encode it with hue alone.**
> Up/down candles must be distinguishable by a second, non-colour channel: use filled vs.
> hollow (or outlined) candle bodies as the primary encoding, with colour as a secondary
> reinforcement only. Roughly 8% of men have red-green colour vision deficiency and cannot
> reliably read a chart where the only signal is red-vs-green hue; a shape or fill
> difference remains legible to them. Apply this same fill/hollow rule consistently in
> both the candle body and any legend swatches — never introduce a legend that is itself
> hue-only after the chart body got the fix.
>
> **Build, naming each tool where it is used:**
>
> 1. **Chart** — use `tradingview/lightweight-charts` to render the candlestick price
>    panel, the linked volume histogram pane, and the moving-average line overlay.
>    Lightweight Charts' own multi-pane API (a candlestick series and a histogram series
>    on a linked pane, plus a line series for the overlay, all on one chart instance)
>    gives you the shared/linked x-axis and the combined crosshair tooltip natively —
>    this is the one job the library is purpose-built for, so do not reach for a second
>    charting library to get panel-linking it already does for free. Lightweight Charts
>    is a JavaScript library with no official Python binding: write the chart-construction
>    code in plain JavaScript against its UMD bundle, loaded via a `<script>` tag in the
>    page the app step serves. Do not route it through an unofficial Python wrapper that
>    is not part of this stack.
> 2. **App** — use `streamlit/streamlit` to host the page as a single-process app: read
>    the OHLC+volume CSV, reshape it into the JSON structure the chart script consumes
>    (including the trading-timestamp list used for the gap handling above and the
>    moving-average series), and hand the assembled HTML/JS as one string to
>    `st.components.v1.html(...)`. One `streamlit run trading_dashboard.py` is the only
>    command needed to view it locally.
>
> Compute the moving average (state the window, e.g. `MA_WINDOW = 20`, as a constant) over
> the same trading-timestamp list as the price series, so the overlay has no points on
> closed-market gaps either.
>
> Keep styling minimal: a light and dark variant of the colour pair is fine, but the
> fill/hollow distinction must be present in both.

## Variants

Append one of these:

- **Multiple symbols** — "Add a symbol selector that swaps the whole dataset and re-renders all three panels without losing the current zoom range."
- **Bollinger bands** — "Add a second overlay band (rolling mean ± k·rolling std) as a shaded region on the price panel, computed over the same trading-timestamp list as the moving average."
- **Intraday** — "Switch the time axis from daily bars to intraday bars and extend the gap handling to skip overnight and lunch-break closures, not just weekends and holidays."

## Verify before you ship it

```bash
# run it
streamlit run trading_dashboard.py -- --csv sample_ohlc.csv
```

```bash
# check for interpolated gaps
python3 -c "
import pandas as pd
df = pd.read_csv('sample_ohlc.csv', parse_dates=['date'])
gaps = df['date'].diff().dt.days
print('max gap (days):', gaps.max())
print('weekend-sized gaps present:', (gaps >= 3).any())
"
```

```bash
# look at it
open http://localhost:8501  # streamlit's default port
```

If the chart draws a diagonal line across every weekend, the x-axis is a
continuous time scale rather than the trading-timestamp category axis the brief asks for —
fix it at the axis definition, not by hiding the line with styling.

Check the candle-direction encoding with a colour-blindness simulator (or just convert a
screenshot to grayscale) before calling this done. If up and down candles become
indistinguishable in grayscale, the fill/hollow channel did not actually get wired in and
the chart is still hue-only underneath.

<sub>Generated by `scripts/prompts/trading_dashboard.py` · parent report: `charting-stack`</sub>
