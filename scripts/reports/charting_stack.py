#!/usr/bin/env python3
"""
Generate a landscape report on charting and data-visualization tools found in
the starred-repos dataset: web charting libraries, React chart kits, low-level
and high-performance renderers, grammar-of-graphics stacks, Python plotting,
BI/dashboard platforms, data-app frameworks, dashboards-as-code, diagram
generators, and native/desktop plotting.

Unlike the other landscape reports, this one leads with an explicit
advantages / disadvantages / use-case table — that comparison is the point.

Inputs:
  data/classified.json
  public/data/graph.json

Output:
  reports/charting-stack.md   (+ reports/charting-stack.meta.json)

Run: python3 scripts/reports/charting_stack.py
"""
import json
import os
from datetime import datetime, timezone

from lib import fmt_stars, CLASSIFIED, GRAPH, fmt_int, days_to_human, activity_label, make_node_for

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "charting-stack"
TITLE = "Charting & Data-Visualization Tools — Advantages, Disadvantages & Use Cases"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy --------------------------------------------------------
# repo -> (category, blurb, advantages, disadvantages, best_for)
TAXONOMY = {
    # ---------------- Web charting library -----------------------------------
    "apache/echarts": (
        "Web charting library",
        "Apache's batteries-included canvas/SVG charting engine — the widest chart-type "
        "catalogue in open source, with a mature big-data rendering path.",
        "Enormous chart catalogue (incl. sankey, treemap, graph, geo); canvas renderer handles "
        "hundreds of thousands to millions of points; built-in dataZoom/toolbox/theming; strong "
        "i18n and accessibility work; Apache governance.",
        "Large bundle (~1 MB full build) unless you hand-assemble tree-shaken imports; imperative "
        "`setOption` config object is verbose and weakly typed; docs and issues skew Chinese-first; "
        "React/Vue wrappers are third-party.",
        "Dense enterprise dashboards and any chart type the small libraries don't have.",
    ),
    "chartjs/Chart.js": (
        "Web charting library",
        "The default 'just draw me a bar chart' library — canvas-based, tiny API surface, "
        "everywhere in tutorials and CMS plugins.",
        "Trivial learning curve; small (~60 KB, ~14 KB tree-shaken for basic charts); huge plugin "
        "ecosystem; framework-agnostic with well-maintained React/Vue bindings; MIT.",
        "Only ~8 core chart types; performance degrades noticeably past ~10k points; canvas output "
        "isn't selectable/exportable as vector; deep customisation means writing plugins.",
        "Standard business charts (line/bar/pie/doughnut) at typical data volumes.",
    ),
    "plotly/plotly.js": (
        "Web charting library",
        "The JS engine underneath Plotly's Python/R/Julia libraries and Dash — scientific chart "
        "types plus an interaction toolbar you get for free.",
        "40+ chart types including 3D, contour, and statistical plots; zoom/pan/hover/export toolbar "
        "out of the box; identical JSON figure spec across JS/Python/R.",
        "Very heavy bundle (bundles D3 + gl-vis internally); the JSON figure format is verbose; "
        "styling fights you if you want a bespoke look; MIT core but commercial upsell around Dash.",
        "Scientific and engineering charts, and anything already using Plotly in Python/R.",
    ),
    "apexcharts/apexcharts.js": (
        "Web charting library",
        "SVG charting with polished defaults — the pragmatic middle ground between Chart.js's "
        "simplicity and ECharts's breadth.",
        "Attractive out-of-the-box styling and animations; good annotation and mixed-chart support; "
        "official React/Vue/Angular wrappers; MIT.",
        "SVG rendering caps practical dataset size well below canvas libraries; less flexible than "
        "D3 for custom marks; some advanced features are documented only by example.",
        "Product dashboards that must look good with little design work.",
    ),
    "highcharts/highcharts": (
        "Web charting library",
        "The long-running commercial charting suite — extremely complete, with accessibility and "
        "export modules that most open-source libraries lack.",
        "Best-in-class accessibility module (screen-reader sonification, keyboard nav); mature stock/"
        "maps/gantt packages; export server; enterprise support and long-term API stability.",
        "**Not free for commercial use** — proprietary licence with per-developer pricing; large "
        "bundle; the licence alone disqualifies it for many OSS/SaaS teams.",
        "Regulated or accessibility-mandated products with budget for a licence.",
    ),
    "antvis/G2": (
        "Web charting library",
        "AntV's 'concise and progressive visualization grammar' — a grammar-of-graphics layer that "
        "compiles to canvas/SVG, from Ant Group's data-viz team.",
        "Grammar-of-graphics composability without leaving JS; strong statistical transforms; part of "
        "the wider AntV suite (G6 graphs, L7 geo, S2 tables); good animation primitives.",
        "Documentation and community are largely Chinese-language; API churned hard across v4→v5; "
        "smaller Western ecosystem means fewer StackOverflow answers.",
        "Teams that want ggplot-style composition in a TypeScript frontend.",
    ),
    "c3js/c3": (
        "Web charting library",
        "A D3-based reusable chart wrapper — the 2015-era way to get D3 output without writing D3.",
        "Simple declarative config over real D3 output; stable, small, easy to theme with CSS; "
        "still receiving maintenance commits.",
        "Effectively feature-frozen; built on D3 v5-era patterns; limited chart types; the problem it "
        "solved is now solved better by Observable Plot and ECharts.",
        "Legacy codebases already on C3 — not a new-project choice.",
    ),
    "frappe/charts": (
        "Web charting library",
        "Zero-dependency SVG charts, ~14 KB gzipped — the minimalist option, extracted from the "
        "Frappe/ERPNext stack.",
        "Tiny footprint and no dependencies; genuinely pleasant defaults; heatmap (GitHub-contribution "
        "style) built in; MIT.",
        "Small chart catalogue; sparse maintenance; no serious large-dataset story; limited "
        "interactivity beyond tooltips.",
        "Weight-sensitive pages and simple embedded charts.",
    ),
    "observablehq/plot": (
        "Web charting library",
        "Observable's concise layered grammar of graphics for JavaScript — from the authors of D3, "
        "as the answer to 'D3 is too low-level for a scatterplot'.",
        "Extremely terse for exploratory charts; sensible statistical defaults (bins, stacks, "
        "facets); built on and interoperable with D3; ISC licence.",
        "Deliberately exploratory-first — less suited to pixel-exact product charts; interaction model "
        "is thinner than ECharts/Highcharts; smaller plugin ecosystem.",
        "Fast exploratory charts in notebooks and internal tools.",
    ),

    # ---------------- React charting library ---------------------------------
    "recharts/recharts": (
        "React charting library",
        "Charts as React components, composed from D3 primitives — the default answer to "
        "'chart library for React'.",
        "Idiomatic React composition (`<LineChart><XAxis/><Tooltip/>`); declarative and easy to "
        "reason about; responsive container built in; MIT; the most-recommended React default.",
        "SVG-only — struggles well before 10k points; animation and layout bugs surface in complex "
        "compositions; customisation beyond the component props gets awkward fast.",
        "The default choice for typical React dashboards with modest data volumes.",
    ),
    "plouc/nivo": (
        "React charting library",
        "A rich, opinionated set of dataviz React components on top of D3 — with SVG, canvas, and "
        "server-side rendering variants of most charts.",
        "Beautiful defaults and a superb interactive docs/playground; canvas variants for larger "
        "datasets; SSR support; motion via react-spring.",
        "Heavy dependency footprint; each chart family has its own prop vocabulary to learn; theming "
        "is powerful but verbose; bundle size adds up quickly.",
        "Design-led React dashboards where visual polish matters more than bundle size.",
    ),
    "airbnb/visx": (
        "React charting library",
        "Airbnb's *unopinionated* collection of low-level visualization primitives — D3 maths with "
        "React rendering, not a chart library.",
        "You own the DOM and the design entirely; tree-shakes to only what you import; no chart "
        "abstraction to fight; excellent for design-system-native charts.",
        "Not a chart library — you assemble axes, scales, and tooltips yourself; substantially more "
        "code per chart; steeper ramp; you inherit D3's mental model anyway.",
        "Bespoke, design-system-consistent charts in React where control beats speed.",
    ),
    "tremorlabs/tremor": (
        "React charting library",
        "Copy-paste React + Tailwind dashboard components (KPI cards, bars, area charts) built on "
        "Recharts — a dashboard UI kit rather than a charting engine.",
        "Fastest path to a competent-looking dashboard; Tailwind-native; components are copied into "
        "your repo so you can edit them; KPI/stat tiles included, not just charts.",
        "Requires Tailwind; inherits every Recharts performance limit; shifted to a copy-paste model "
        "which complicates upgrades; opinionated visual style is hard to fully escape.",
        "Tailwind/Next.js dashboards that need to look finished this week.",
    ),

    # ---------------- Low-level & high-performance ---------------------------
    "d3/d3": (
        "Low-level / high-performance",
        "Not a chart library — the data-binding, scales, shapes, and layout toolkit that most other "
        "libraries are built on.",
        "Total expressive freedom; the scales/shape/geo/force modules are the reference "
        "implementations; modular (import only `d3-scale` if that's all you need); unmatched "
        "learning material.",
        "Very steep learning curve; you write and maintain everything including axes, legends, and "
        "accessibility; direct DOM manipulation clashes with React's model; slow to ship simple charts.",
        "Custom, one-of-a-kind visualizations — and as a dependency of everything else.",
    ),
    "leeoniya/uPlot": (
        "Low-level / high-performance",
        "A ~50 KB canvas chart for time series, lines, areas, OHLC, and bars — built around one "
        "constraint: render fast.",
        "Renders hundreds of thousands of points in milliseconds; ~50 KB with zero dependencies; "
        "memory-frugal; the benchmark other libraries are measured against.",
        "Deliberately narrow — time-series shapes only, no pie/treemap/geo; terse, low-level API; "
        "minimal built-in interactivity; you build the polish yourself.",
        "Dense time-series panels and anything where render latency is the requirement.",
    ),
    "tradingview/lightweight-charts": (
        "Low-level / high-performance",
        "TradingView's ~45 KB financial charting engine — candlesticks, volume, and crosshairs with "
        "trading-desk-grade interaction.",
        "Purpose-built for financial series: candlestick/OHLC, real-time streaming updates, "
        "professional pan/zoom feel; tiny; Apache-2.0.",
        "Financial charts only — no general chart types; indicator library is not included (that's "
        "the paid Charting Library); attribution notice required.",
        "Trading, crypto, and any price/time chart that must feel native.",
    ),
    "perspective-dev/perspective": (
        "Low-level / high-performance",
        "A C++/WASM streaming analytics engine with a chart+pivot UI — originally built at J.P. "
        "Morgan for real-time trading data.",
        "Handles millions of rows client-side via WASM + Apache Arrow; pivots, filters, and charts "
        "over streaming updates; works in the browser, Jupyter, and as a server.",
        "Heavy, unusual architecture (WASM binary + web components); steep conceptual ramp; overkill "
        "for static datasets; smaller community than mainstream charting.",
        "Real-time, million-row analytical grids that must stay interactive in the browser.",
    ),
    "visgl/deck.gl": (
        "Low-level / high-performance",
        "Uber/vis.gl's WebGL2 layer framework for very large geospatial and scientific datasets.",
        "GPU rendering of millions of points/arcs/hexbins; composable layer model; integrates with "
        "MapLibre/Mapbox/Google Maps; battle-tested at Uber scale.",
        "GPU-only mental model with real memory/driver pitfalls; heavy bundle; overkill for anything "
        "under ~100k features; documentation assumes graphics familiarity.",
        "Large-scale geospatial visualization and GPU-accelerated point clouds.",
    ),
    "keplergl/kepler.gl": (
        "Low-level / high-performance",
        "A ready-made geospatial analysis application built on deck.gl — drag a CSV in and explore "
        "it on a map.",
        "No-code map analysis for large datasets; layer/filter/time-playback UI included; embeddable "
        "as a React component; exports configs as JSON.",
        "Opinionated app, not a library — customisation means forking behaviour; Redux-coupled "
        "embedding is awkward; maintenance has slowed since the Uber era.",
        "Ad-hoc geospatial exploration without building a mapping app.",
    ),

    # ---------------- Grammar of graphics ------------------------------------
    "vega/vega-lite": (
        "Grammar of graphics",
        "A concise JSON grammar for interactive graphics — describe the chart, not the drawing code. "
        "The pragmatic layer over Vega.",
        "Charts are portable JSON, which makes them diffable, generatable, and **the most "
        "LLM-friendly chart format**; sensible defaults infer scales and legends; excellent "
        "faceting/layering; BSD-3.",
        "Escaping the grammar for a bespoke design means dropping to Vega or another library; "
        "rendering performance is modest; error messages on malformed specs are cryptic.",
        "Spec-driven charts, embedded analytics, and charts generated by agents or LLMs.",
    ),
    "vega/vega": (
        "Grammar of graphics",
        "The full visualization grammar Vega-Lite compiles down to — a declarative runtime with "
        "signals, event streams, and custom transforms.",
        "Far more expressive than Vega-Lite (custom interaction, layouts, transforms) while staying "
        "declarative; renders to canvas or SVG; strong academic pedigree (UW IDL).",
        "Verbose specs that get unwieldy fast; steeper than both Vega-Lite and most imperative "
        "libraries; debugging a large spec is genuinely painful.",
        "Custom interactive graphics that must still be declarative and serializable.",
    ),
    "vega/altair": (
        "Grammar of graphics",
        "The Python API over Vega-Lite — statistical charts as method chains on a DataFrame.",
        "Very concise, highly readable chart code; interactive selections and linked brushing come "
        "free; native pandas/Polars support; output is a portable Vega-Lite spec.",
        "Historically awkward with large data (data is embedded in the spec unless you use "
        "`vegafusion`/URLs); customisation ceiling is Vega-Lite's; static export needs extra deps.",
        "Exploratory statistical charts in notebooks, especially with linked interaction.",
    ),
    "has2k1/plotnine": (
        "Grammar of graphics",
        "A faithful port of R's ggplot2 to Python — `+` operator, aesthetics, geoms, facets, the "
        "whole grammar.",
        "If you know ggplot2, you already know it; excellent faceting and statistical layers; "
        "publication-grade static output via matplotlib; consistent, principled API.",
        "Static only — no interactivity; matplotlib backend means matplotlib's speed and styling "
        "constraints; smaller ecosystem than matplotlib/seaborn; slower on large frames.",
        "Publication figures for anyone coming from R/ggplot2.",
    ),
    "JetBrains/lets-plot": (
        "Grammar of graphics",
        "JetBrains's multiplatform grammar-of-graphics library — one ggplot-style API across Python, "
        "Kotlin, and JVM notebooks.",
        "Same grammar from Python and Kotlin/JVM; genuinely good geospatial support; renders in "
        "Jupyter, Datalore, and Kotlin notebooks; actively developed by a funded team.",
        "Much smaller community than ggplot2/matplotlib; Kotlin-first documentation in places; "
        "fewer third-party extensions; another rendering stack to learn.",
        "JVM/Kotlin data teams, and Python users who want ggplot without the R baggage.",
    ),

    # ---------------- Python plotting & dataframe viz -------------------------
    "matplotlib/matplotlib": (
        "Python plotting",
        "The foundation of Python plotting — every other Python viz library either builds on it or "
        "defines itself against it.",
        "Can draw literally anything; the publication standard for scientific figures; vector output "
        "(PDF/SVG/EPS); enormous documentation and 20 years of StackOverflow answers; PSF-style licence.",
        "Two competing APIs (pyplot state machine vs. object-oriented) confuse newcomers; verbose for "
        "anything non-trivial; dated defaults; no real interactivity; slow on large datasets.",
        "Publication figures and any plot that must be exactly right.",
    ),
    "plotly/plotly.py": (
        "Python plotting",
        "Interactive charts from Python, rendering through plotly.js — Plotly Express makes most "
        "charts one line.",
        "Interactivity (hover/zoom/select) for free in notebooks and web; Plotly Express is genuinely "
        "concise; 3D and statistical chart types; the same figure object powers Dash.",
        "Large output payloads bloat notebooks and slow rendering; styling defaults are hard to "
        "override cleanly; the free/enterprise boundary around Dash causes confusion.",
        "Interactive exploration in notebooks, and any chart destined for a Dash app.",
    ),
    "bokeh/bokeh": (
        "Python plotting",
        "Interactive browser visualization from Python with a real server component for streaming "
        "and Python-side callbacks.",
        "Python callbacks can run server-side (no JS required) via `bokeh serve`; strong streaming "
        "and large-data story (with Datashader); composable widgets; BSD-3.",
        "Heavier concepts than Plotly for simple charts; the server model adds deployment burden; "
        "smaller community and slower momentum than Plotly/Altair.",
        "Streaming/live Python dashboards that need server-side callbacks.",
    ),
    "holoviz/holoviews": (
        "Python plotting",
        "Declare *what* the data means and let it render itself — an annotation layer over Bokeh, "
        "matplotlib, and Plotly.",
        "Extremely concise for exploratory work; backend-agnostic (same code → Bokeh or matplotlib); "
        "composes plots with `+` and `*`; pairs with Datashader for billion-point rendering.",
        "Heavy abstraction — debugging means understanding the backend anyway; sparse error messages; "
        "steep conceptual learning curve; small community.",
        "Iterative exploratory analysis where you re-plot constantly.",
    ),
    "holoviz/panel": (
        "Python plotting",
        "HoloViz's app/dashboard framework — the layout and widget layer that turns any Python plot "
        "into an app.",
        "Backend-agnostic: embeds matplotlib, Plotly, Bokeh, Altair, Vega, and DataFrames alike; "
        "works inside notebooks *and* as a served app; mature templating.",
        "Large API surface with several overlapping ways to do things; documentation sprawl; smaller "
        "community than Streamlit; more concepts before the first app runs.",
        "Python dashboards that must mix plotting libraries rather than commit to one.",
    ),
    "Kanaries/pygwalker": (
        "Python plotting",
        "Turns a DataFrame into a drag-and-drop Tableau-style exploration UI with one line in a "
        "notebook.",
        "`pyg.walk(df)` and you have pivot + chart exploration; no chart code at all; works in "
        "Jupyter/Streamlit/Colab; exports the resulting spec.",
        "Exploration tool, not a production chart library; struggles on very large frames without a "
        "compute backend; the free tier nudges toward the commercial Kanaries cloud.",
        "Fast visual EDA on a DataFrame before writing any chart code.",
    ),
    "man-group/dtale": (
        "Python plotting",
        "Man Group's DataFrame inspector — a full web UI for filtering, describing, and charting "
        "pandas objects.",
        "Deep pandas-specific tooling (correlations, missing-value analysis, code export); shows the "
        "pandas code for each operation; runs from notebook, CLI, or Flask.",
        "Purely an inspection/EDA tool; heavy Flask app for what is often a quick look; not embeddable "
        "as a component; pandas-centric.",
        "Interrogating an unfamiliar DataFrame in depth.",
    ),
    "reflex-dev/xy": (
        "Python plotting",
        "Reflex's fast, customizable Python charting library — a young, actively developed entrant "
        "aimed at Reflex apps and beyond.",
        "Very fast rendering; clean modern API; first-class inside Reflex apps; hot development pace "
        "with a funded team behind it.",
        "Young and small — API stability, chart coverage, and ecosystem are all unproven; documentation "
        "is thin; effectively single-vendor.",
        "Reflex apps, and experiments where speed matters more than maturity.",
    ),
    "posit-dev/great-tables": (
        "Python plotting",
        "Not charts — *tables*. Posit's library for publication-quality display tables in Python "
        "(the gt package's Python sibling).",
        "Turns DataFrames into genuinely presentable tables (spanners, footnotes, formatting, "
        "nanoplots); the missing piece in most reporting stacks; Posit maintenance.",
        "Display only — not interactive, not sortable, not a data grid; young API; another dependency "
        "for something teams often hand-roll.",
        "Report and dashboard tables that need to look designed rather than dumped.",
    ),

    # ---------------- BI & dashboard platform --------------------------------
    "grafana/grafana": (
        "BI & dashboard platform",
        "The observability dashboard standard — time-series panels over ~200 data sources, with "
        "alerting as a first-class citizen.",
        "Best-in-class time-series dashboards and alerting; plugs into anything (Prometheus, Loki, "
        "SQL, Elasticsearch, cloud); huge dashboard library; excellent health/activity metrics in "
        "this dataset (see comparison table).",
        "Awkward for non-time-series BI (joins, drill-downs, pivots); dashboard JSON is painful to "
        "review in git without a codegen layer; AGPL core with enterprise features gated; "
        "query-language burden shifts to the data source.",
        "Infrastructure, metrics, and any alert-driven operational dashboard.",
    ),
    "apache/superset": (
        "BI & dashboard platform",
        "Apache's SQL-first BI platform — 40+ visualization types, a semantic layer, and a proper "
        "SQL Lab for technical analysts.",
        "Rich visualization catalogue; genuine multi-tenant BI (roles, row-level security, caching); "
        "warehouse-scale via SQLAlchemy; Apache-2.0 with no feature gating.",
        "Heavy to deploy and operate (Celery, Redis, metadata DB); upgrades are notoriously "
        "involved; the semantic layer is weaker than commercial BI; steeper for business users.",
        "Technical data teams that want warehouse-scale, self-hosted BI.",
    ),
    "metabase/metabase": (
        "BI & dashboard platform",
        "The friendliest open-source BI tool — a question builder that non-SQL users actually use.",
        "Fastest setup of any BI platform here; the notebook/question builder genuinely works for "
        "business users; good embedding story; sane defaults.",
        "Visualization catalogue is comparatively basic; complex analytical modelling hits a ceiling "
        "quickly; the useful embedding/SSO features sit behind the commercial edition (AGPL core).",
        "Self-service BI where adoption by non-technical users is the deciding factor.",
    ),
    "getredash/redash": (
        "BI & dashboard platform",
        "Query-first BI: write SQL, save it, chart it, dashboard it — the simplest mental model of "
        "the BI tools here.",
        "Extremely simple model (query → visualization → dashboard); 50+ data sources; low "
        "operational weight; good for SQL-fluent teams.",
        "Development has been slow since the Databricks acquisition; visualization options are thin; "
        "no semantic layer or modelling; effectively in maintenance mode.",
        "SQL-fluent teams that want dashboards without a BI platform.",
    ),
    "elastic/kibana": (
        "BI & dashboard platform",
        "Elastic's window into Elasticsearch — log exploration, search analytics, and dashboards over "
        "the Elastic stack.",
        "Unmatched for log/search exploration (Discover, Lens, ES\\|QL); tight security/APM/observability "
        "integration; mature alerting and ML jobs.",
        "Only really useful with Elasticsearch behind it; heavy resource footprint; the SSPL/Elastic "
        "licence change still rules it out for some; the UI sprawls across many overlapping apps.",
        "Log-centric troubleshooting in an Elastic-based stack.",
    ),
    "openobserve/openobserve": (
        "BI & dashboard platform",
        "A Rust-based observability platform (logs, metrics, traces, RUM) that positions itself as a "
        "lighter, cheaper Elastic/Grafana-stack replacement.",
        "Claims order-of-magnitude storage savings vs. Elasticsearch; single binary, trivial to run; "
        "logs + metrics + traces + dashboards in one product; very healthy activity in this dataset.",
        "Much younger and smaller ecosystem than Grafana/Kibana; fewer integrations and community "
        "dashboards; open-core with features reserved for the enterprise tier.",
        "Small teams that want an all-in-one observability stack without Elastic's bill.",
    ),
    "evidence-dev/evidence": (
        "BI & dashboard platform",
        "BI as code — write SQL and markdown, get a static interactive data site. Git is the source "
        "of truth, not a dashboard editor.",
        "Dashboards live in version control and review like code; markdown+SQL is fast to author; "
        "static output deploys anywhere; excellent for reproducible reporting.",
        "No point-and-click authoring — non-technical users can't self-serve; static build model "
        "doesn't fit ad-hoc exploration; smaller component library than mature BI tools.",
        "Engineering-led reporting where dashboards should be reviewed like code.",
    ),
    "rilldata/rill": (
        "BI & dashboard platform",
        "A DuckDB-backed BI tool built for speed — dashboards defined as code, with sub-second "
        "exploration and an explicit agent/LLM story.",
        "Genuinely fast exploratory slicing (embedded DuckDB); dashboards-as-YAML; local-first "
        "development loop; deliberately designed to be driven by agents as well as humans.",
        "Young project with a narrower feature set than Superset/Metabase; opinionated metrics-layer "
        "model; open-source core alongside a commercial cloud.",
        "Fast metric exploration for teams comfortable defining dashboards in code.",
    ),
    "Canner/WrenAI": (
        "BI & dashboard platform",
        "Generative BI — a governed text-to-SQL layer that turns natural-language questions into "
        "queries and charts for humans and agents.",
        "Semantic/context layer keeps LLM-generated SQL grounded and governed; answers arrive as "
        "charts, not just tables; MCP-friendly for agent workflows; very active.",
        "Accuracy still depends on modelling discipline — a bad semantic layer produces confidently "
        "wrong charts; requires an LLM provider (cost + data-egress questions); young category.",
        "Letting non-analysts (or agents) ask questions of a governed warehouse.",
    ),
    "ToolJet/ToolJet": (
        "BI & dashboard platform",
        "A low-code internal-tool builder — drag-and-drop apps with charts, tables, and forms wired "
        "to databases and APIs.",
        "Builds full CRUD internal tools, not just read-only dashboards; 50+ connectors; self-hostable; "
        "very healthy maintenance signal.",
        "A low-code app builder first and a charting tool second — visualization options are basic; "
        "vendor lock-in to its app model; complex logic in a visual builder ages badly.",
        "Internal tools that need charts *and* write actions in one place.",
    ),

    # ---------------- Data-app framework -------------------------------------
    "streamlit/streamlit": (
        "Data-app framework",
        "The default way to turn a Python script into a shareable data app — rerun-the-script "
        "execution model, widgets, and charts in a few lines.",
        "Lowest possible friction (a script becomes an app); enormous component ecosystem; free "
        "Community Cloud hosting; renders matplotlib/Plotly/Altair/Vega directly.",
        "The rerun-on-every-interaction model becomes a correctness and performance problem as apps "
        "grow; state management is bolted on; limited layout control; not built for high traffic or "
        "multi-user production.",
        "Internal prototypes and demos that will stay simple.",
    ),
    "gradio-app/gradio": (
        "Data-app framework",
        "Hugging Face's framework for ML model demos — inputs, outputs, and a shareable link in "
        "under ten lines.",
        "Purpose-built for model demos (image/audio/chat components are excellent); instant public "
        "share links; deep Hugging Face Spaces integration; auto-generated REST API.",
        "Charting is an afterthought compared to Streamlit; not designed for traffic or complex "
        "multi-page apps; layout control is limited; app structure gets messy past a few screens.",
        "ML model demos, chat UIs, and Hugging Face Spaces.",
    ),
    "plotly/dash": (
        "Data-app framework",
        "The production-oriented Python dashboard framework — explicit reactive callbacks, Flask "
        "underneath, Plotly figures on top.",
        "Explicit callback graph scales to genuinely complex apps; runs on Flask so it deploys like "
        "any WSGI app; the most 'production' of the Python options; mature enterprise story.",
        "Far more boilerplate than Streamlit; callback chains get hard to reason about; tied to "
        "Plotly for charting; the good enterprise features (auth, scaling) are commercial.",
        "Production Python dashboards that outgrew Streamlit.",
    ),
    "reflex-dev/reflex": (
        "Data-app framework",
        "Pure-Python web apps that compile to a React frontend — full-stack, with routing, auth, and "
        "state in Python.",
        "Real web-app architecture (components, routing, state) without writing JS; compiles to "
        "React/Next.js so the output is a normal SPA; excellent health/activity in this dataset.",
        "Much larger conceptual surface than Streamlit; the Python→React compilation leaks when you "
        "need custom JS; younger ecosystem; debugging spans two runtimes.",
        "Python teams shipping a real web app, not a script with widgets.",
    ),
    "Avaiga/taipy": (
        "Data-app framework",
        "A Python framework with two halves: a GUI layer and a genuine scenario/pipeline orchestration "
        "engine for data and what-if workflows.",
        "Per-user state isolation and an async backend (unlike Streamlit's rerun model); built-in "
        "scenario/pipeline management for what-if analysis; designed for business-facing apps.",
        "More code and more concepts than Streamlit for a simple app; smaller community and component "
        "ecosystem; the orchestration half is wasted if you only want a dashboard.",
        "Business-facing Python apps with scenario/what-if workflows.",
    ),

    # ---------------- Dashboards as code -------------------------------------
    "grafana/grafana-foundation-sdk": (
        "Dashboards as code",
        "Grafana's own typed builders for dashboards and alerts across Go, Java, PHP, Python, and "
        "TypeScript — the official successor to the community codegen tools.",
        "First-party and versioned against Grafana schemas; strong typing catches invalid dashboards "
        "at compile time; multi-language; actively maintained.",
        "Still maturing, with API churn between Grafana versions; more verbose than writing JSON for "
        "simple dashboards; you must track schema versions.",
        "Teams standardising Grafana dashboards as reviewed, typed code.",
    ),
    "deliveryhero/grafyaml": (
        "Dashboards as code",
        "Grafana dashboards defined in YAML instead of JSON — the lightest-weight dashboards-as-code "
        "option here.",
        "YAML is far more reviewable than Grafana's dashboard JSON; minimal tooling; easy to slot "
        "into existing CI; still maintained.",
        "Thin abstraction — you still need to know the underlying JSON model; small community; no "
        "type checking; limited to what the YAML mapping exposes.",
        "Small teams wanting reviewable dashboards without adopting an SDK.",
    ),
    "weaveworks/grafanalib": (
        "Dashboards as code",
        "The original Python library for generating Grafana dashboards — historically the standard "
        "before Grafana shipped its own SDK.",
        "Pythonic dashboard construction with reusable functions; large body of existing examples; "
        "simple to integrate into Python CI.",
        "**Declining in this dataset** — Weaveworks shut down and maintenance has stalled; lags "
        "current Grafana panel schemas; superseded by grafana-foundation-sdk.",
        "Legacy Python dashboard pipelines — migrate new work to the Foundation SDK.",
    ),
    "K-Phoen/grabana": (
        "Dashboards as code",
        "A Go library and DSL for building Grafana dashboards — the Go-ecosystem counterpart to "
        "grafanalib.",
        "Pleasant Go builder API and a YAML DSL; good fit for Go-based platform tooling; supports "
        "alerts as code.",
        "**Reads as abandoned in this snapshot** (no pushes in well over a year); trails current "
        "Grafana schema; the official Go Foundation SDK now covers the same ground.",
        "Existing Go dashboard pipelines only — not a new-project choice.",
    ),

    # ---------------- Diagrams & AI-generated charts -------------------------
    "excalidraw/excalidraw": (
        "Diagrams & AI charts",
        "A virtual whiteboard with a hand-drawn aesthetic — the default tool for sketching "
        "architecture and flow diagrams.",
        "Effortless, genuinely fast sketching; hand-drawn style reads as 'draft' which encourages "
        "iteration; local-first with an open file format; embeddable library; huge adoption.",
        "Not a data-charting tool — no data binding whatsoever; the sketch aesthetic is wrong for "
        "formal documentation; collaboration/storage features push toward Excalidraw+.",
        "Architecture sketches, whiteboarding, and diagrams-in-docs.",
    ),
    "jgraph/drawio-desktop": (
        "Diagrams & AI charts",
        "The offline Electron build of draw.io — the most complete free diagramming application, "
        "with the shape libraries enterprises actually need.",
        "Exhaustive shape libraries (AWS/Azure/GCP/UML/BPMN/network); fully offline and local-file "
        "based; no account required; stable and battle-tested.",
        "Dated Electron UI; XML file format is unpleasant to diff; no data binding — diagrams are "
        "drawn, not generated from data; manual layout work.",
        "Formal architecture, network, and process diagrams that must follow a notation.",
    ),
    "lukilabs/beautiful-mermaid": (
        "Diagrams & AI charts",
        "A polished renderer for Mermaid diagrams — Mermaid's text-to-diagram syntax with far better "
        "typography and theming.",
        "Text-defined diagrams mean git-diffable, LLM-generatable output; substantially better "
        "looking than stock Mermaid; drops into docs pipelines.",
        "Bound to Mermaid's syntax and layout engine (auto-layout is often mediocre); **declining "
        "maintenance signal** in this snapshot; presentation layer only.",
        "Diagrams in docs and READMEs that should look designed.",
    ),
    "hustcc/mcp-mermaid": (
        "Diagrams & AI charts",
        "An MCP server that lets an AI agent generate Mermaid diagrams and charts on demand — "
        "charting as an agent tool.",
        "Gives agents a real diagramming capability over MCP; text-in/diagram-out fits LLMs "
        "perfectly; trivial to wire into Claude Code or any MCP client.",
        "Inherits every Mermaid limitation (layout quality, chart-type range); thin wrapper with "
        "**declining maintenance**; single-maintainer risk.",
        "Letting an agent produce diagrams inside a conversation or doc pipeline.",
    ),

    # ---------------- Native / systems charting ------------------------------
    "ScottPlot/ScottPlot": (
        "Native / systems charting",
        "Interactive plotting for .NET — WinForms, WPF, Avalonia, and console, with a genuinely "
        "simple API.",
        "By far the strongest .NET plotting option; renders millions of points interactively; "
        "supports every major .NET UI framework; MIT; excellent docs and cookbook.",
        ".NET-only; desktop-oriented (no first-class web story); smaller community than the web "
        "libraries; single primary maintainer.",
        "Desktop .NET applications that need real interactive plots.",
    ),
    "AAChartModel/AAChartKit": (
        "Native / systems charting",
        "Declarative charts for iOS/iPadOS/macOS — an Objective-C/Swift wrapper around Highcharts "
        "rendered in a web view.",
        "Highcharts' chart quality inside a native app; declarative, chainable API; broad chart "
        "coverage; long-lived project.",
        "**Wraps Highcharts — inherits its commercial licence for commercial apps**; web-view "
        "rendering costs memory and startup time; slowing maintenance; Swift Charts now covers many "
        "cases natively.",
        "Apple-platform apps needing chart types Swift Charts doesn't cover — check the licence first.",
    ),
    "core-plot/core-plot": (
        "Native / systems charting",
        "The veteran native Core Graphics plotting framework for macOS and iOS — no web view involved.",
        "Genuinely native rendering (no JS bridge); fine-grained drawing control; BSD licence; long "
        "track record.",
        "Dated API from the pre-Swift era; slow maintenance; steep learning curve; largely superseded "
        "by Apple's Swift Charts for new work.",
        "Legacy Apple codebases already using it.",
    ),
    "gonum/plot": (
        "Native / systems charting",
        "Plotting for Go, part of the Gonum numerical stack — generate chart images from a Go "
        "service.",
        "Idiomatic Go with no CGo or browser needed; vector output (SVG/PDF/EPS); integrates with "
        "the Gonum numeric libraries; BSD-3.",
        "Static images only, no interactivity; limited chart types and styling; **low health and "
        "slow maintenance** in this snapshot; API is spartan.",
        "Server-side chart image generation from Go without a JS runtime.",
    ),
    "alandefreitas/matplotplusplus": (
        "Native / systems charting",
        "Matplot++ — a C++17 graphics library with a matplotlib-shaped API for scientific plotting.",
        "Familiar matplotlib-like API from C++; wide chart coverage for a C++ library; multiple "
        "backends and export formats; header-friendly CMake integration.",
        "Depends on gnuplot for rendering in the common setup; heavy build; **low health / slow "
        "maintenance** in this snapshot; small community.",
        "C++ scientific and simulation code that must plot without leaving the process.",
    ),
}

# Adjacent but deliberately excluded (kept honest in the report)
ADJACENT = [
    ("prometheus/prometheus", "a time-series *database* and the data source behind most Grafana panels — storage, not charting"),
    ("plausible/analytics", "a fixed-purpose web-analytics product; its dashboard isn't reusable for your own data"),
    ("bluewave-labs/Checkmate", "uptime/infrastructure monitoring with built-in status charts — a monitoring product, not a charting tool"),
    ("voxel51/fiftyone", "visualizes *datasets and model predictions* for computer vision — a data-curation app, not a chart library"),
    ("jessevig/bertviz", "visualizes transformer attention specifically — a model-interpretability tool"),
    ("OpenSpace/OpenSpace", "astrovisualization of space data — scientific rendering, not general charting"),
    ("originalankur/maptoposter", "turns city maps into poster art — cartographic design, not data visualization"),
    ("unhappychoice/gitlogue", "animated replay of git history in the terminal — a novelty visualizer"),
    ("patoles/agent-flow", "real-time visualization of agent orchestration — see the *Agent orchestration* report"),
    ("vivekchand/clawmetry", "agent-runtime observability dashboards — routed to the agent reports"),
    ("williamngan/pts", "creative-coding and generative visuals rather than charts; reads as abandoned in this snapshot"),
    ("GraphiteEditor/Graphite", "a 2D vector graphics editor — design tooling, not data charting"),
    ("mosra/magnum", "C++ graphics middleware used *for* visualization, but a rendering engine at heart"),
    ("deliveryhero/helm-charts", "name collision — Kubernetes Helm charts, nothing to do with data charts"),
    ("ultraworkers/hermes-agent-helm-chart", "same collision: a Helm chart, not a data chart"),
    ("jakevdp/PythonDataScienceHandbook", "a book (notebooks) that teaches matplotlib — learning material, not a tool"),
    ("GeostatsGuy/DataScienceInteractivePython", "teaching notebooks with interactive dashboards — course material"),
]

# Task-ranked picks: (task, [(repo, note) …up to 3], evidence)
TASK_RANKINGS = [
    ("Standard business charts in a web app (line/bar/pie)",
     [("chartjs/Chart.js", "smallest sane default, trivial API"),
      ("apexcharts/apexcharts.js", "better-looking defaults, still simple"),
      ("frappe/charts", "~14 KB when weight is the constraint")],
     "Chart.js is ~60 KB (≈14 KB tree-shaken for basic charts) and covers the common types; reach further only when it fails you."),
    ("Charts in a React app with minimal effort",
     [("recharts/recharts", "the idiomatic React default"),
      ("plouc/nivo", "nicer defaults, canvas variants available"),
      ("tremorlabs/tremor", "whole dashboard UI, not just charts")],
     "Consensus 2026 guidance: Recharts as the practical React default; switch to canvas-based libs when volume bites."),
    ("Dense dashboards / 10k+ points in the browser",
     [("apache/echarts", "canvas renderer, millions of points"),
      ("leeoniya/uPlot", "~50 KB, fastest time-series render"),
      ("perspective-dev/perspective", "WASM engine for millions of streaming rows")],
     "Chart.js and SVG libraries (Recharts, ApexCharts) degrade noticeably above ~10k points; ECharts is documented at 10M+."),
    ("Fully bespoke, one-of-a-kind visualization",
     [("d3/d3", "total control, the reference implementation"),
      ("airbnb/visx", "D3 maths with React rendering"),
      ("antvis/G2", "grammar-based composition in TS")],
     "D3 is a toolkit, not a chart library — budget for building axes, legends, and accessibility yourself."),
    ("Financial / trading charts",
     [("tradingview/lightweight-charts", "purpose-built, ~45 KB, streaming"),
      ("highcharts/highcharts", "Highstock package, commercial licence"),
      ("apache/echarts", "candlestick support, free")],
     "Lightweight-charts gives trading-desk interaction feel; indicators are in TradingView's paid Charting Library, not this one."),
    ("Large-scale geospatial visualization",
     [("visgl/deck.gl", "GPU layers, millions of features"),
      ("keplergl/kepler.gl", "ready-made app on top of deck.gl"),
      ("apache/echarts", "adequate for modest geo overlays")],
     "deck.gl is the library; kepler.gl is the app — pick by whether you're building or exploring."),
    ("Publication-quality static figures (Python)",
     [("matplotlib/matplotlib", "the publication standard, vector output"),
      ("has2k1/plotnine", "ggplot2 grammar, matplotlib backend"),
      ("JetBrains/lets-plot", "grammar + good geospatial")],
     "Journals expect vector PDF/EPS; all three deliver it. Choose by API taste, not capability."),
    ("Exploratory analysis in a notebook",
     [("plotly/plotly.py", "Plotly Express, one-line interactive charts"),
      ("vega/altair", "concise grammar with linked selections"),
      ("holoviz/holoviews", "re-plot repeatedly with minimal code")],
     "Altair embeds data in the spec — use vegafusion or URL data for large frames."),
    ("Zero-code exploration of a DataFrame",
     [("Kanaries/pygwalker", "Tableau-style drag-and-drop in one line"),
      ("man-group/dtale", "deep pandas inspection + code export"),
      ("holoviz/panel", "when it needs to become an app")],
     "EDA tools, not production charting — expect to rewrite the final chart properly."),
    ("Charts described as data (spec-driven / LLM-generated)",
     [("vega/vega-lite", "portable JSON spec, the LLM-friendly format"),
      ("vega/vega", "when Vega-Lite's ceiling is reached"),
      ("hustcc/mcp-mermaid", "agent-callable diagram/chart tool over MCP")],
     "Vega-Lite specs are diffable JSON, which makes them the most reliable target for model-generated charts."),
    ("ML model demo with a UI in an afternoon",
     [("gradio-app/gradio", "purpose-built for model demos + Spaces"),
      ("streamlit/streamlit", "more general, better charting"),
      ("plotly/dash", "if it will outlive the demo")],
     "Gradio's image/audio/chat components are why it wins here; its charting is weaker than Streamlit's."),
    ("Python data app that must survive production",
     [("plotly/dash", "explicit callbacks, Flask deployment"),
      ("reflex-dev/reflex", "compiles to React, real app architecture"),
      ("Avaiga/taipy", "per-user state + scenario orchestration")],
     "Streamlit's rerun-everything model is the documented pain point at scale; all three fix it differently."),
    ("Self-service BI for non-technical users",
     [("metabase/metabase", "easiest adoption, question builder"),
      ("apache/superset", "richer viz, heavier to run"),
      ("getredash/redash", "simplest if everyone writes SQL")],
     "2026 comparisons converge on Metabase for usability, Superset for depth — Redash is effectively in maintenance mode."),
    ("Warehouse-scale BI for a technical data team",
     [("apache/superset", "40+ viz types, RLS, caching"),
      ("rilldata/rill", "DuckDB speed, dashboards as code"),
      ("Canner/WrenAI", "governed text-to-SQL on top")],
     "Superset is the deepest self-hosted option; budget real operational effort for Celery/Redis/upgrades."),
    ("Dashboards reviewed in git (BI as code)",
     [("evidence-dev/evidence", "SQL + markdown → static data site"),
      ("rilldata/rill", "dashboards as YAML, local-first"),
      ("grafana/grafana-foundation-sdk", "typed Grafana dashboards in 5 languages")],
     "All three trade point-and-click authoring for reviewability — non-technical self-service is the cost."),
    ("Infrastructure metrics & alerting",
     [("grafana/grafana", "the standard; ~200 data sources"),
      ("openobserve/openobserve", "single binary, logs+metrics+traces"),
      ("elastic/kibana", "if the data already lives in Elastic")],
     "Grafana remains the leading choice for live metrics and alert-driven dashboards."),
    ("Log-centric troubleshooting",
     [("elastic/kibana", "Discover/Lens/ES\\|QL over Elasticsearch"),
      ("openobserve/openobserve", "much cheaper storage, younger"),
      ("grafana/grafana", "via Loki, if already on Grafana")],
     "Kibana is strongest when logs and search are central — and only really useful with Elastic behind it."),
    ("Natural-language questions → charts (for people or agents)",
     [("Canner/WrenAI", "governed semantic layer over text-to-SQL"),
      ("rilldata/rill", "explicitly designed for agent-driven BI"),
      ("metabase/metabase", "safest fallback: a guided question builder")],
     "The failure mode is confidently wrong SQL — the semantic layer, not the model, is what makes this safe."),
    ("Internal tool with charts *and* write actions",
     [("ToolJet/ToolJet", "low-code CRUD + charts + 50 connectors"),
      ("reflex-dev/reflex", "code-first alternative, full control"),
      ("Avaiga/taipy", "when scenarios/what-if are involved")],
     "Dashboards are read-only; if users must also edit data, a BI tool is the wrong shape."),
    ("Charts in a desktop .NET application",
     [("ScottPlot/ScottPlot", "the clear .NET winner, millions of points"),
      (None, ""), (None, "")],
     "No serious open-source competition in .NET desktop plotting; ScottPlot supports WinForms/WPF/Avalonia."),
    ("Charts in a native iOS / macOS app",
     [("AAChartModel/AAChartKit", "broad chart coverage — check the Highcharts licence"),
      ("core-plot/core-plot", "truly native Core Graphics, dated API"),
      (None, "")],
     "Apple's own Swift Charts now covers most common cases natively — reach for these only for chart types it lacks."),
    ("Charts from a Go or C++ service (no browser)",
     [("gonum/plot", "Go, vector output, no CGo"),
      ("alandefreitas/matplotplusplus", "C++17, matplotlib-shaped API"),
      (None, "")],
     "Both are static-image generators with low maintenance signal in this snapshot — vendor or pin them."),
    ("Presentable tables (not charts) in a report",
     [("posit-dev/great-tables", "publication-quality display tables in Python"),
      (None, ""), (None, "")],
     "Frequently the actual requirement behind 'make me a chart' — a table that reads well beats a weak chart."),
    ("Architecture & flow diagrams (not data charts)",
     [("excalidraw/excalidraw", "fastest sketching, hand-drawn feel"),
      ("jgraph/drawio-desktop", "formal notations, exhaustive shape libraries"),
      ("lukilabs/beautiful-mermaid", "text-defined, git-diffable diagrams")],
     "Diagrams are drawn, not data-bound — a different job from every other row in this table."),
]

# ---- Load --------------------------------------------------------------------
with open(CLASSIFIED) as f:
    cl = json.load(f)
with open(GRAPH) as f:
    gr = json.load(f)

by_name = {r["full_name"]: r for r in cl["repos"]}
nodes_by_id = {n["id"]: n for n in gr["nodes"]}
name_to_nodeid = {n["full_name"]: n["id"] for n in gr["nodes"]}

sel_names = list(TAXONOMY.keys())
sel_node_ids = {name_to_nodeid[n] for n in sel_names if n in name_to_nodeid}
inter_edges = [e for e in gr["links"]
               if e["source"] in sel_node_ids and e["target"] in sel_node_ids]

node_for = make_node_for(nodes_by_id, name_to_nodeid)

# Bare repo names are ambiguous here — two `…/plot` repos, and a bare `charts`
# means nothing in a report about charts. Fall back to owner/name in those cases.
_GENERIC = {"plot", "plots", "chart", "charts", "analytics"}
_tail_counts = {}
for _n in sel_names:
    _tail_counts[_n.split("/")[-1]] = _tail_counts.get(_n.split("/")[-1], 0) + 1


def short(name):
    tail = name.split("/")[-1]
    if _tail_counts.get(tail, 0) > 1 or tail.lower() in _GENERIC:
        return name
    return tail


ORDER = [
    "Web charting library",
    "React charting library",
    "Low-level / high-performance",
    "Grammar of graphics",
    "Python plotting",
    "BI & dashboard platform",
    "Data-app framework",
    "Dashboards as code",
    "Diagrams & AI charts",
    "Native / systems charting",
]

# ---- Build -------------------------------------------------------------------
gen = cl.get("generatedAt", "")
user = cl.get("username", "")
lines = []
A = lines.append

A(f"# {TITLE}")
A("")
A(f"> Derived from **{user}**'s {fmt_int(cl['total'])} starred repos "
  f"(snapshot `{gen}`), cross-referenced with the repo-similarity graph "
  f"({fmt_int(len(gr['nodes']))} nodes / {fmt_int(len(gr['links']))} edges, "
  f"{len(gr['communities'])} communities). The advantages/disadvantages column is "
  f"editorial judgement grounded in the dataset's own health metrics plus external "
  f"comparisons — see Methodology.")
A(">")
A(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/charting_stack.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} charting and visualization tools** in your stars "
  f"(**{fmt_int(total_stars)}★** combined), grouped into {len([c for c in ORDER if cats.get(c)])} layers:")
for c in ORDER:
    if cats.get(c):
        A(f"  - **{c}** ({len(cats[c])}): "
          + ", ".join(f"`{short(x)}`" for x in sorted(cats[c], key=lambda x: -by_name[x]['stars'])))
A("- **There is no 'best chart app' — there are six different questions.** *Who "
  "writes the chart* (developer / analyst / business user / agent), *where it renders* "
  "(browser / notebook / desktop / static site), *how much data* (hundreds / millions), "
  "*how bespoke* (library defaults / pixel-exact), *who operates it* (a dependency vs. "
  "a platform to run), and *what licence* you can live with. Every row in the "
  "advantages/disadvantages table below is really one of those trade-offs.")
A("- The single most common mistake this landscape produces: **picking an SVG "
  "library for a canvas-sized problem**. Recharts, ApexCharts, and Chart.js degrade "
  "noticeably past ~10k points; ECharts, uPlot, Perspective, and deck.gl exist "
  "precisely for what lies beyond that line.")
A("- **Licence is a real constraint, not a footnote.** `highcharts` is proprietary "
  "for commercial use — and `AAChartKit` inherits that licence by wrapping it. "
  "`grafana`, `metabase`, and `superset` differ sharply in what they gate behind an "
  "enterprise edition.")
A("- The dashboards-as-code corner is consolidating: `grafanalib` is **declining** and "
  "`grabana` reads as **abandoned** in this snapshot, both superseded by Grafana's "
  "first-party `grafana-foundation-sdk`.")
A("- New in this landscape: **charts as an agent output**. `vega-lite`'s JSON specs, "
  "`mcp-mermaid`'s MCP tool, and `WrenAI`/`rill`'s explicit agent framing all point the "
  "same way — the chart is becoming something a model emits, not something a human draws.")
A("")

# --- Decision anatomy
A("## Choosing: the six questions")
A("")
A("| Question | If the answer is… | Look at |")
A("|---|---|---|")
A("| **Who authors the chart?** | a developer, in code | charting libraries (ECharts, Recharts, D3) |")
A("| | an analyst, in SQL | Superset, Redash, Evidence, Rill |")
A("| | a business user, clicking | Metabase, ToolJet |")
A("| | an LLM / agent | Vega-Lite specs, mcp-mermaid, WrenAI |")
A("| **Where does it render?** | browser app | web + React charting libraries |")
A("| | notebook | Plotly.py, Altair, HoloViews, PyGWalker |")
A("| | desktop / native | ScottPlot, AAChartKit, Core Plot |")
A("| | a static site / PDF | Evidence, matplotlib, plotnine |")
A("| **How much data?** | < 10k points | any SVG library |")
A("| | 10k–1M | ECharts, uPlot, ScottPlot |")
A("| | > 1M / streaming | Perspective, deck.gl, Datashader-backed HoloViews |")
A("| **How bespoke?** | library defaults are fine | Chart.js, Recharts, ApexCharts |")
A("| | must match a design system | visx, D3, G2 |")
A("| **Who operates it?** | it's a dependency | every library here |")
A("| | it's a platform you run | Grafana, Superset, Metabase, Kibana |")
A("| **Licence tolerance?** | permissive only | avoid Highcharts (and AAChartKit) |")
A("| | AGPL/open-core acceptable | Grafana, Metabase |")
A("")

# --- The core table: advantages / disadvantages / use cases
A("## Advantages, disadvantages & use cases")
A("")
A("The core of this report. Grouped by layer, sorted by stars within each layer.")
A("")
for cat in ORDER:
    members = cats.get(cat) or []
    if not members:
        continue
    A(f"### {cat}")
    A("")
    A("| Tool | ★ | ✅ Advantages | ⚠️ Disadvantages | 🎯 Best for |")
    A("|" + "---|" * 5)
    for n in sorted(members, key=lambda x: -by_name[x]["stars"]):
        r = by_name[n]
        _, _, pros, cons, best = TAXONOMY[n]
        A(f"| **[{n}]({r['url']})** | {fmt_stars(r)} | {pros} | {cons} | {best} |")
    A("")

# --- Task rankings
A("## Use-case rankings — which tool for which job")
A("")
A("Ranked picks per job. Dataset metrics say who is *healthy*; the notes and evidence "
  "column say who is *right for the job*.")
A("")
A("| Use case | 🥇 First pick | 🥈 Second | 🥉 Third | Evidence / note |")
A("|" + "---|" * 5)
for task, picks, evidence in TASK_RANKINGS:
    cells = []
    for entry in picks:
        repo, note = entry
        if repo is None:
            cells.append("—")
        else:
            cells.append(f"`{short(repo)}` — {note}" if note else f"`{short(repo)}`")
    while len(cells) < 3:
        cells.append("—")
    A(f"| **{task}** | {cells[0]} | {cells[1]} | {cells[2]} | {evidence} |")
A("")

# --- Master comparison
A("## Master comparison — dataset metrics")
A("")
A("Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits.")
A("")
A("| Tool | Layer | Lang | License | ★ Stars | Lifecycle | Health | "
  "Activity | Last push | Age | Contrib(90d) |")
A("|" + "---|" * 11)
for n in sorted(present, key=lambda x: -by_name[x]["stars"]):
    r = by_name[n]
    A("| [{name}]({url}) | {cat} | {lang} | {lic} | {stars} | {lc} | {hs} | "
      "{act} | {push} | {age} | {auth} |".format(
        name=n, url=r["url"], cat=TAXONOMY[n][0],
        lang=r.get("primary_language") or "—",
        lic=(r.get("license") or "—"),
        stars=fmt_stars(r),
        lc=r.get("lifecycle_stage") or "—",
        hs=r.get("health_score") if r.get("health_score") is not None else "—",
        act=activity_label(r),
        push=days_to_human(r.get("days_since_push")) + " ago",
        age=days_to_human(r.get("age_days")),
        auth=r.get("unique_authors_90d") if r.get("unique_authors_90d") is not None else "—",
    ))
A("")

# --- Category deep dives
A("## By layer")
A("")
cat_blurb = {
    "Web charting library": "General-purpose JS/TS chart engines. The choice here is mostly "
        "bundle size vs. chart-type breadth vs. how many points you need to draw.",
    "React charting library": "Charts as React components. Convenience scales inversely with "
        "control — and all of them inherit SVG's data-volume ceiling unless noted.",
    "Low-level / high-performance": "Toolkits and renderers rather than chart libraries: "
        "maximum control (D3, visx) or maximum throughput (uPlot, Perspective, deck.gl).",
    "Grammar of graphics": "Describe the chart declaratively and let the library draw it. "
        "The most portable, diffable, and LLM-generatable way to specify a chart.",
    "Python plotting": "The notebook and scientific-computing side: static publication figures, "
        "interactive exploration, and zero-code DataFrame inspection.",
    "BI & dashboard platform": "Products you deploy and operate, not dependencies you import. "
        "Differ by audience (business vs. technical) and by data shape (metrics vs. warehouse vs. logs).",
    "Data-app framework": "Turn Python into a UI. The axis that matters is how far each one "
        "scales past a prototype.",
    "Dashboards as code": "Generate Grafana dashboards from typed code or YAML so they can be "
        "reviewed and versioned. Consolidating fast around Grafana's first-party SDK.",
    "Diagrams & AI charts": "Drawn diagrams rather than data-bound charts — plus the text-defined "
        "formats that agents can generate.",
    "Native / systems charting": "Plotting inside desktop and systems applications, where a "
        "browser runtime isn't available or isn't wanted.",
}
for cat in ORDER:
    members = cats.get(cat) or []
    if not members:
        continue
    A(f"### {cat}")
    A("")
    A(f"_{cat_blurb[cat]}_")
    A("")
    for n in sorted(members, key=lambda x: -by_name[x]["stars"]):
        r = by_name[n]
        topics = ", ".join((r.get("topics") or [])[:8]) or "—"
        A(f"- **[{n}]({r['url']})** · {fmt_int(r['stars'])}★ · {r.get('primary_language') or '—'} · "
          f"{r.get('lifecycle_stage','—')}  ")
        A(f"  {TAXONOMY[n][1]}  ")
        A(f"  <sub>topics: {topics}</sub>")
    A("")

# --- Spotlight
A("## Spotlight: the SVG/canvas line, and why most chart choices go wrong")
A("")
A("Almost every 'our dashboard got slow' story in this landscape is the same story: "
  "an SVG-based library asked to draw more marks than the DOM can carry.")
A("")
A("- **SVG libraries** (`Recharts`, `ApexCharts`, `nivo`'s SVG variants, `frappe/charts`, "
  "`c3`) create one DOM node per mark. That is wonderful for styling, CSS transitions, and "
  "accessibility — and it falls over somewhere between 5k and 10k points.")
A("- **Canvas libraries** (`Chart.js`, `ECharts`, `uPlot`, `nivo`'s canvas variants, "
  "`ScottPlot`) draw pixels. You lose per-element CSS and easy hit-testing; you gain one to "
  "two orders of magnitude of headroom. `ECharts` documents rendering at 10M+ points.")
A("- **GPU/WASM** (`deck.gl`, `perspective`) move the work off the main thread entirely. "
  "This is the only tier that survives millions of *streaming* rows, and it costs real "
  "architectural complexity.")
A("")
A("The practical rule: **decide the data volume before the library.** Retrofitting "
  "a canvas renderer into a component tree built around SVG charts is close to a rewrite. "
  "The second rule: **downsample before you upgrade** — `uPlot`-class performance on "
  "aggregated data usually beats GPU rendering on raw data, and it's far less code.")
A("")

# --- Graph analysis
A("## Graph analysis — how they relate")
A("")
comm = {}
for n in present:
    nd = node_for(n)
    if nd is not None:
        comm.setdefault(nd.get("community"), []).append(n)
A(f"**Community clustering.** These {len(present)} tools span "
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities** — a wide spread, "
  f"because charting cuts across the frontend, Python-data, and observability clusters "
  f"rather than forming one of its own.")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 2:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in names))
A("")

ranked = sorted(
    [(node_for(n).get("pagerank", 0) if node_for(n) else 0, n) for n in present],
    key=lambda x: -x[0],
)
A(f"**Centrality (PageRank in the full {fmt_int(len(gr['nodes']))}-repo graph)** — "
  "most 'hub-like' visualization tools in your ecosystem:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between charting tools** (top similarity edges where both "
  "endpoints are in this report):")
A("")
if inter_edges:
    id_to_name = {v: k for k, v in name_to_nodeid.items()}
    shown = sorted(inter_edges, key=lambda x: -x["weight"])[:15]
    for e in shown:
        a = id_to_name.get(e["source"], e["source"])
        b = id_to_name.get(e["target"], e["target"])
        why = []
        if e.get("shared_topics"):
            why.append("topics: " + ", ".join(e["shared_topics"][:4]))
        if e.get("shared_authors"):
            why.append("authors: " + ", ".join(e["shared_authors"][:3]))
        A(f"- `{a}` ⇄ `{b}` (w={e['weight']:.3f})" + (f" — {'; '.join(why)}" if why else ""))
    if len(inter_edges) > 15:
        A(f"- …and {len(inter_edges) - 15} more.")
else:
    A("- _None._")
A("")

# --- Maintenance / risk
A("## Maintenance & risk signal")
A("")
A("Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle "
  "+ activity before adopting.")
A("")
A("| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |")
A("|---|---|---|---|---|---|---|")
for n in sorted(present, key=lambda x: -(by_name[x].get("health_score") or 0)):
    r = by_name[n]
    tas = r.get("top_author_share")
    A("| {n} | {h} | {lc} | {act} | {bf} | {tas} | {rel} |".format(
        n=n, h=r.get("health_score", "—"), lc=r.get("lifecycle_stage", "—"),
        act=activity_label(r), bf=r.get("bus_factor", "—"),
        tas=f"{tas:.0%}" if isinstance(tas, (int, float)) else "—",
        rel=r.get("releases_total", "—")))
A("")
A("Watch items: `grafanalib` is **declining** (Weaveworks is gone) and `grabana` reads "
  "as **abandoned** — migrate Grafana codegen to `grafana-foundation-sdk`. `c3` is "
  "effectively feature-frozen; `Observable Plot` or `ECharts` covers new work. "
  "`core-plot`, `gonum/plot`, and `matplotplusplus` all show low health and slow "
  "maintenance — pin or vendor them. `beautiful-mermaid` and `mcp-mermaid` are declining "
  "single-maintainer projects; the underlying Mermaid syntax is the durable part, not "
  "these wrappers. `redash` is effectively in maintenance mode post-acquisition.")
A("")

# --- Licensing
A("## Licensing traps")
A("")
A("The one dimension that silently disqualifies an otherwise-correct choice:")
A("")
A("- **`highcharts` is proprietary for commercial use.** It is genuinely excellent — "
  "especially its accessibility module — but it is a per-developer paid licence, not "
  "an open-source dependency.")
A("- **`AAChartKit` wraps Highcharts**, and therefore inherits that licence for "
  "commercial apps. This is the most commonly missed trap in the table above.")
A("- **`grafana` (AGPL) and `metabase` (AGPL)** are open-core: self-hosting is free, but "
  "SSO, fine-grained permissions, and some embedding features are enterprise-only.")
A("- **`kibana`** is under the Elastic Licence / SSPL, which is not OSI-approved and is "
  "rejected by some corporate policies outright.")
A("- **`apache/echarts` and `apache/superset`** are Apache-2.0 with no feature gating — "
  "the safest picks in their respective rows if licensing is the binding constraint.")
A("")

# --- Adjacent
A("## Adjacent (deliberately not listed as charting tools)")
A("")
for name, why in ADJACENT:
    r = by_name.get(name)
    star = f" ({fmt_int(r['stars'])}★)" if r else ""
    A(f"- **{name}**{star} — {why}")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `data/classified.json` + `public/data/graph.json` for all repo "
  "metrics and graph structure. No API calls at generation time; fully reproducible.")
A("- **Selection**: keyword scan (chart / plot / visuali[sz] / dashboard / graphing / BI / "
  "diagram) over `full_name + description + topics`, then manual curation into layers. "
  "Domain-specific visualizers (model interpretability, geospatial art, agent "
  "observability) and rendering engines were routed to the adjacent list.")
A("- **Name collisions were checked**: `deliveryhero/helm-charts` and "
  "`ultraworkers/hermes-agent-helm-chart` are Kubernetes Helm charts, not data charts, "
  "and are excluded.")
A("- **Advantages/disadvantages are editorial**, not measured. They combine the dataset's "
  "own health/lifecycle/activity signals (which *are* measured) with external "
  "comparisons gathered 2026-08 covering JS charting libraries "
  "(bundle sizes, data-volume ceilings), BI platforms (Grafana/Kibana/Metabase/Superset), "
  "and Python data-app frameworks (Streamlit/Gradio/Reflex/Taipy). Bundle-size and "
  "performance figures are point-in-time and version-dependent — verify against the "
  "version you are pinning.")
A("- **Licence fields** come from the snapshot's GitHub metadata and can be wrong for "
  "dual-licensed projects. `highcharts` in particular is not usable commercially under "
  "an open-source licence regardless of what the repo metadata says. Verify before shipping.")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and "
  "may lag GitHub's current state.")
A("- Re-run after a fresh `classified.json` to refresh stars/activity; the editorial "
  "columns are frozen text and need manual review when major versions land.")
A("")
A(f"<sub>Tools covered: {len(present)} · Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta (consumed by build_index.py) --------------------------------
top = sorted(present, key=lambda x: -by_name[x]["stars"])[:5]
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / Apps",
    "summary": (f"{len(present)} charting and data-visualization tools "
                f"({fmt_int(total_stars)}★) compared head-to-head on advantages, "
                "disadvantages, and use cases: web and React chart libraries, "
                "high-performance renderers, grammar-of-graphics stacks, Python "
                "plotting, BI platforms, data-app frameworks, dashboards-as-code, "
                "and native/desktop plotting."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in ORDER},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/charting_stack.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
