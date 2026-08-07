#!/usr/bin/env python3
"""
Generate the "Trending Now" report: what is *actually* gaining stars in the
starred-repos dataset, measured by diffing archived snapshots rather than
estimated from lifetime averages.

Every other report in this pipeline is a static landscape — a curated taxonomy
rendered against the current vintage. This one is about *change*: it is the only
report whose subject is the delta between two data vintages, so its repo set is
computed, not hand-curated.

Note on `momentum` in classified.json: that field is a lifetime-stars/day proxy
(see the comment in scripts/classify.mjs) — it estimates what a repo *probably*
gains. This report uses observed snapshot-to-snapshot deltas instead, so it
reflects what a repo actually gained over a known window.

Inputs:
  data/classified.json
  public/data/graph.json
  data/snapshots/*.json   (needs >= 2 to produce anything)

Output:
  reports/trending-now.md   (+ reports/trending-now.meta.json)

Run: python3 scripts/reports/trending_now.py
"""
import json
import os
from datetime import date, datetime, timezone

from lib import (CLASSIFIED, GRAPH, SNAPSHOT_DIR, activity_label, days_to_human,
                 fmt_int, make_node_for)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "trending-now"
TITLE = "Trending Now — What's Actually Moving in Your Stars"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# How many rows each leaderboard shows.
TOP_N = 20
# Minimum baseline stars before a % move is considered meaningful — without a
# floor, a repo going 12★ → 30★ swamps the relative-growth board.
BREAKOUT_FLOOR = 300
# A repo must gain at least this many stars in the recent window to be a "riser".
RISER_MIN = 1

# ---- Curated theme layer -----------------------------------------------------
# The leaderboards above are computed; this is the interpretation layer. Each
# theme names a trend and lists the repos in this dataset carrying it. Keep the
# repo lists honest — a theme is only listed if its members actually appear in
# the risers table. Re-curate when the shape of the movers changes.
THEMES = [
    (
        "Skills as the packaging format for agent behaviour",
        "The single loudest signal in this dataset. A year ago you configured an agent with a "
        "prompt; now behaviour ships as a versioned, installable *skill* bundle — and the "
        "repos distributing those bundles are growing faster than the agents that consume them. "
        "Note what this implies: the moat is moving from the model to the instruction layer.",
        ["obra/superpowers", "anthropics/skills", "multica-ai/andrej-karpathy-skills",
         "nextlevelbuilder/ui-ux-pro-max-skill", "affaan-m/ECC", "garrytan/gstack",
         "msitarzewski/agency-agents", "hesreallyhim/awesome-claude-code",
         "shanraisshan/claude-code-best-practice", "DietrichGebert/ponytail",
         "ayghri/i-have-adhd"],
    ),
    (
        "Giving agents a memory of the codebase",
        "Retrieval over a codebase is being replaced by *pre-indexed structure* — graphs and "
        "persistent stores an agent can consult instead of re-reading files every session. "
        "This is the same insight the graph in this repo is built on, and it is now one of the "
        "fastest-moving categories in your stars.",
        ["DeusData/codebase-memory-mcp", "colbymchenry/codegraph", "topoteretes/cognee",
         "thedotmack/claude-mem", "Egonex-AI/Understand-Anything", "Graphify-Labs/graphify",
         "zilliztech/claude-context", "langchain-ai/openwiki",
         "TencentCloud/TencentDB-Agent-Memory", "repowise-dev/repowise",
         "semantica-agi/semantica"],
    ),
    (
        "Frontier models on hardware you already own",
        "The counter-current to everything above: instead of making API calls cheaper, remove "
        "them. Big mixture-of-experts models are being squeezed onto consumer machines, and "
        "the repos doing it are among the fastest relative movers in the dataset.",
        ["JustVugg/colibri", "lyogavin/airllm", "ggml-org/llama.cpp",
         "Mesh-LLM/mesh-llm", "microsoft/foundry-local"],
    ),
    (
        "Token economics became a product category",
        "Context windows got bigger and people started paying for them. These repos exist purely "
        "to make agents cheaper to run — compressing tool output, trimming prompts, proxying "
        "calls. That a compression layer can add tens of thousands of stars in weeks says the "
        "cost pressure is real, not theoretical.",
        ["JuliusBrussee/caveman", "headroomlabs-ai/headroom", "rtk-ai/rtk",
         "Alishahryar1/free-claude-code", "JustVugg/colibri"],
    ),
    (
        "The coding-agent harness field is still splitting, not consolidating",
        "Terminal coding agents keep multiplying rather than converging on a winner, and a "
        "second layer has appeared above them: switchers, meta-harnesses, and orchestrators "
        "whose job is to manage the agents themselves.",
        ["anomalyco/opencode", "openai/codex", "earendil-works/pi", "1jehuang/jcode",
         "farion1231/cc-switch", "code-yeongyu/oh-my-openagent", "ruvnet/ruflo",
         "bytedance/deer-flow", "multica-ai/multica", "paperclipai/paperclip",
         "OpenHands/OpenHands", "anthropics/claude-code", "NousResearch/hermes-agent",
         "getpaseo/paseo", "vercel/eve"],
    ),
    (
        "Agents are leaving the terminal for specific jobs",
        "The generalist assistant is being joined by vertical agents pointed at one domain — "
        "pentesting, trading, tutoring, job hunting, video. These grow on usefulness to a "
        "specific audience rather than on developer-tool hype.",
        ["usestrix/strix", "TauricResearch/TradingAgents", "HKUDS/Vibe-Trading",
         "HKUDS/DeepTutor", "santifer/career-ops", "jamiepine/voicebox",
         "heygen-com/hyperframes", "browser-use/browser-use", "Canner/WrenAI",
         "Zackriya-Solutions/meetily"],
    ),
    (
        "Design and spec as agent-readable artifacts",
        "If an agent writes the code, the leverage moves upstream to the spec and the design "
        "system. These repos turn intent into something an agent can consume directly.",
        ["github/spec-kit", "nexu-io/open-design", "VoltAgent/awesome-design-md",
         "nextlevelbuilder/ui-ux-pro-max-skill"],
    ),
]

# ---- Load --------------------------------------------------------------------
with open(CLASSIFIED) as f:
    cl = json.load(f)
with open(GRAPH) as f:
    gr = json.load(f)

by_name = {r["full_name"]: r for r in cl["repos"]}
nodes_by_id = {n["id"]: n for n in gr["nodes"]}
name_to_nodeid = {n["full_name"]: n["id"] for n in gr["nodes"]}
node_for = make_node_for(nodes_by_id, name_to_nodeid)

snap_files = sorted(f for f in os.listdir(SNAPSHOT_DIR) if f.endswith(".json"))
if len(snap_files) < 2:
    raise SystemExit("trending-now needs >= 2 snapshots in data/snapshots/ — skipping")

snaps = {}
for f in snap_files:
    with open(os.path.join(SNAPSHOT_DIR, f)) as fh:
        snaps[f[:-5]] = json.load(fh)

dates = list(snaps.keys())
NEWEST, PREV, OLDEST = dates[-1], dates[-2], dates[0]


def days_between(a, b):
    ya, ma, da = map(int, a.split("-"))
    yb, mb, db = map(int, b.split("-"))
    return (date(yb, mb, db) - date(ya, ma, da)).days


def deltas(a, b):
    """[(name, gain, per_day, now, then)] for repos present in both snapshots."""
    n = max(days_between(a, b), 1)
    ra, rb = snaps[a]["repos"], snaps[b]["repos"]
    rows = []
    for name, cur in rb.items():
        old = ra.get(name)
        if not old or old.get("stars") is None or cur.get("stars") is None:
            continue
        gain = cur["stars"] - old["stars"]
        rows.append((name, gain, gain / n, cur["stars"], old["stars"]))
    return rows


RECENT_DAYS = max(days_between(PREV, NEWEST), 1)
LONG_DAYS = max(days_between(OLDEST, NEWEST), 1)


def days_word(n):
    return f"{n} day" if n == 1 else f"{n} days"
recent = deltas(PREV, NEWEST)
longrun = deltas(OLDEST, NEWEST)

risers = sorted([r for r in recent if r[1] >= RISER_MIN], key=lambda x: -x[1])
breakouts = sorted(
    [(n, g, pd, cur, then, g / then) for n, g, pd, cur, then in recent
     if then >= BREAKOUT_FLOOR and g > 0],
    key=lambda x: -x[5],
)
sustained = sorted(longrun, key=lambda x: -x[2])

prev_names = set(snaps[PREV]["repos"])
entrants = sorted(
    [n for n in by_name if n not in prev_names],
    key=lambda n: -(by_name[n].get("stars") or 0),
)

newly_archived_now = [
    name for name, cur in snaps[NEWEST]["repos"].items()
    if cur.get("archived") and (snaps[PREV]["repos"].get(name) or {}).get("archived") is False
]

# Repos that were climbing over the long window but have decelerated since.
# Testing for zero recent gain is useless on a multi-week window — almost
# everything ticks up a little — so compare *rates*: a repo is cooling when its
# recent stars/day falls well below its long-run stars/day.
COOLING_RATIO = 0.4
COOLING_MIN_RATE = 1.0
recent_by_name = {n: g for n, g, _, _, _ in recent}
recent_rate = {n: pd for n, _g, pd, _c, _t in recent}
cooling = sorted(
    [(n, long_pd, recent_rate[n], recent_rate[n] / long_pd)
     for n, _g, long_pd, _c, _t in longrun
     if long_pd >= COOLING_MIN_RATE and n in recent_rate
     and recent_rate[n] < long_pd * COOLING_RATIO],
    key=lambda x: x[3],
)


def row_meta(name):
    """(lang, lifecycle, activity, url, description) for a repo, safely."""
    r = by_name.get(name) or {}
    return (
        r.get("primary_language") or "—",
        r.get("lifecycle_stage") or "—",
        activity_label(r) if r else "unknown",
        r.get("url") or f"https://github.com/{name}",
        (r.get("description") or "").strip(),
    )


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
  f"{len(gr['communities'])} communities).")
A(">")
A(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/trending_now.py` (regenerate any time — no API cost).")
A("")

total_gain = sum(g for _, g, _, _, _ in recent if g > 0)

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **This is the only report here that measures *change* rather than describing a landscape.** "
  f"Every other report curates a taxonomy and renders it against the current vintage; this one "
  f"diffs archived snapshots to show what actually moved.")
A(f"- **Window**: `{PREV}` → `{NEWEST}` (**{days_word(RECENT_DAYS)}**), covering the "
  f"**{fmt_int(len(recent))} repos** present in both snapshots. Long-run comparisons use "
  f"`{OLDEST}` → `{NEWEST}` (**{days_word(LONG_DAYS)}**).")
A(f"- **{fmt_int(len([r for r in recent if r[1] > 0]))} repos gained stars** in the recent window, "
  f"adding **{fmt_int(total_gain)}★** between them.")
if entrants:
    A(f"- **{len(entrants)} repos are new to the dataset** since the last refresh — newly starred, "
      f"so they have no baseline to diff and are listed separately.")
if newly_archived_now:
    A(f"- **{len(newly_archived_now)} repos were archived** during this window — see *Cooling off*.")
A(f"- **Measured, not estimated.** `classified.json` carries a `momentum` field, but it is a "
  f"lifetime-stars/day proxy (its own source comment calls it \"a serviceable proxy\"). "
  f"Everything below is observed snapshot-to-snapshot movement over a known number of days.")
A("")

# --- Reading guide
A("## How to read this")
A("")
A("| Board | Question it answers | Bias to watch |")
A("|---|---|---|")
A("| **Fastest risers** | What gained the most stars outright? | Favours repos that are already huge — a 1% move on 100k stars beats a doubling at 500. |")
A("| **Breakouts** | What grew fastest *relative to its size*? | Favours small repos; floored at "
  f"{fmt_int(BREAKOUT_FLOOR)}★ baseline so noise doesn't win. |")
A("| **Sustained climbers** | What has compounded over the long window? | Smooths out one-off spikes (a HN front page, a launch). |")
A("| **New entrants** | What did you just start following? | Not growth at all — these have no baseline. |")
A("| **Cooling off** | What is still growing, but much slower than it was? | Deceleration usually means a launch spike ending, not a project dying. |")
A("")

# --- Fastest risers (absolute)
A(f"## Fastest risers — absolute ({PREV} → {NEWEST}, {RECENT_DAYS}d)")
A("")
A("Raw star gain over the window. `Stars/day` normalizes for window length so this "
  "stays comparable across refreshes of different spacing.")
A("")
A("| # | Repo | Gain | Stars/day | Stars now | Lang | Lifecycle | Activity |")
A("|" + "---|" * 8)
for i, (name, gain, per_day, cur, _then) in enumerate(risers[:TOP_N], 1):
    lang, lc, act, url, _d = row_meta(name)
    A(f"| {i} | [{name}]({url}) | **+{fmt_int(gain)}** | {per_day:.1f} | {fmt_int(cur)} | "
      f"{lang} | {lc} | {act} |")
if not risers:
    A("| — | _No star gains recorded in this window._ | | | | | | |")
A("")

# --- Breakouts (relative)
A(f"## Breakouts — fastest relative growth (≥{fmt_int(BREAKOUT_FLOOR)}★ baseline)")
A("")
A(f"Percent growth over the same {RECENT_DAYS}-day window. The baseline floor keeps "
  "small-number noise off the board — a repo going 8★ → 20★ is not a trend.")
A("")
A("| # | Repo | Growth | Gain | Stars now | What it is |")
A("|" + "---|" * 6)
for i, (name, gain, _pd, cur, then, pct) in enumerate(breakouts[:TOP_N], 1):
    _lang, _lc, _act, url, desc = row_meta(name)
    desc = (desc[:88] + "…") if len(desc) > 88 else (desc or "—")
    A(f"| {i} | [{name}]({url}) | **+{pct:.0%}** | +{fmt_int(gain)} | {fmt_int(cur)} | {desc} |")
if not breakouts:
    A("| — | _No repos cleared the baseline floor with positive growth._ | | | | |")
A("")

# --- Sustained climbers
A(f"## Sustained climbers — long run ({OLDEST} → {NEWEST}, {LONG_DAYS}d)")
A("")
A("Averaged over the full snapshot history, so a single viral week doesn't dominate. "
  "Repos high here *and* in the recent board are compounding, not spiking.")
A("")
A("| # | Repo | Stars/day | Total gain | Stars now | Lang | Health |")
A("|" + "---|" * 7)
for i, (name, gain, per_day, cur, _then) in enumerate(sustained[:TOP_N], 1):
    lang, _lc, _act, url, _d = row_meta(name)
    r = by_name.get(name) or {}
    hs = r.get("health_score")
    A(f"| {i} | [{name}]({url}) | **{per_day:.1f}** | +{fmt_int(gain)} | {fmt_int(cur)} | "
      f"{lang} | {hs if hs is not None else '—'} |")
A("")

# --- Themes
A("## Emerging themes")
A("")
A("The boards above are computed; this section is interpretation. Each theme groups movers "
  "that are rising for the same underlying reason.")
A("")
for theme, blurb, members in THEMES:
    present_members = [m for m in members if m in by_name]
    if not present_members:
        continue
    A(f"### {theme}")
    A("")
    A(f"_{blurb}_")
    A("")
    for m in sorted(present_members, key=lambda x: -(recent_by_name.get(x, 0))):
        r = by_name[m]
        g = recent_by_name.get(m)
        mv = f"+{fmt_int(g)}★ in {RECENT_DAYS}d" if g else "new to the dataset"
        A(f"- **[{m}]({r['url']})** · {fmt_int(r['stars'])}★ · {mv}  ")
        A(f"  {(r.get('description') or '—').strip()}")
    A("")

# --- New entrants
A("## New entrants — newly starred since the last refresh")
A("")
A("These joined the dataset during this window, so they have no baseline to diff. "
  "They are what *you* just found interesting, which is its own kind of trend signal.")
A("")
if entrants:
    A("| Repo | Stars | Lang | Lifecycle | What it is |")
    A("|" + "---|" * 5)
    for name in entrants[:40]:
        r = by_name[name]
        lang, lc, _act, url, desc = row_meta(name)
        desc = (desc[:84] + "…") if len(desc) > 84 else (desc or "—")
        A(f"| [{name}]({url}) | {fmt_int(r['stars'])} | {lang} | {lc} | {desc} |")
    if len(entrants) > 40:
        A(f"| _…and {len(entrants) - 40} more_ | | | | |")
else:
    A("- _No new repos since the last refresh._")
A("")

# --- Cooling
A("## Cooling off")
A("")
A(f"Deceleration, not decline. These averaged ≥{COOLING_MIN_RATE:.0f}★/day across the "
  f"{LONG_DAYS}-day long window but are now running below "
  f"{COOLING_RATIO:.0%} of that rate. Most are still gaining — just far more slowly than "
  f"they were, which is usually the tail of a launch spike rather than a problem.")
A("")
if cooling:
    A("| Repo | Long-run ★/day | Recent ★/day | Now at | Last push | Lifecycle |")
    A("|" + "---|" * 6)
    for name, long_pd, rec_pd, ratio in cooling[:15]:
        r = by_name.get(name) or {}
        _lang, lc, _act, url, _d = row_meta(name)
        A(f"| [{name}]({url}) | {long_pd:.1f} | {rec_pd:.1f} | **{ratio:.0%}** of prior pace | "
          f"{days_to_human(r.get('days_since_push'))} ago | {lc} |")
else:
    A("- _Nothing that was climbing has decelerated meaningfully in this window._")
A("")
if newly_archived_now:
    A(f"**Archived during this window** ({len(newly_archived_now)}): "
      + ", ".join(f"`{n}`" for n in sorted(newly_archived_now)))
    A("")

# --- Graph analysis
A("## Graph analysis — where the movement clusters")
A("")
top_names = [n for n, *_ in risers[:40]]
comm = {}
for n in top_names:
    nd = node_for(n)
    if nd is not None:
        comm.setdefault(nd.get("community"), []).append(n)
A(f"**Community clustering.** The top {len(top_names)} risers span "
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities** — the more "
  f"concentrated they are, the more this looks like one trend rather than broad drift.")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 2:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in names))
A("")

sel_ids = {name_to_nodeid[n] for n in top_names if n in name_to_nodeid}
inter = [l for l in gr["links"] if l["source"] in sel_ids and l["target"] in sel_ids]
A("**Direct links between risers** (similarity edges where both endpoints are climbing) — "
  "co-movement suggests a shared driver:")
A("")
if inter:
    id_to_name = {v: k for k, v in name_to_nodeid.items()}
    for e in sorted(inter, key=lambda x: -x["weight"])[:12]:
        a = id_to_name.get(e["source"], e["source"])
        b = id_to_name.get(e["target"], e["target"])
        why = []
        if e.get("shared_topics"):
            why.append("topics: " + ", ".join(e["shared_topics"][:4]))
        if e.get("shared_authors"):
            why.append("authors: " + ", ".join(e["shared_authors"][:3]))
        A(f"- `{a}` ⇄ `{b}` (w={e['weight']:.3f})" + (f" — {'; '.join(why)}" if why else ""))
    if len(inter) > 12:
        A(f"- …and {len(inter) - 12} more.")
else:
    A("- _No direct similarity edges among the top risers — the movement is spread across "
      "unrelated projects rather than one cluster._")
A("")

# --- Language / topic mix
A("**What the risers are written in** — language mix of the top "
  f"{len(top_names)} movers:")
A("")
langs = {}
for n in top_names:
    lg = (by_name.get(n) or {}).get("primary_language") or "—"
    langs[lg] = langs.get(lg, 0) + 1
for lg, c in sorted(langs.items(), key=lambda x: -x[1])[:8]:
    A(f"- **{lg}** — {c}")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A(f"- **Source**: `data/snapshots/*.json` diffed against `data/classified.json` + "
  f"`public/data/graph.json`. No external calls; fully reproducible.")
A(f"- **Snapshots available**: {', '.join(dates)} ({len(dates)} vintages). "
  f"`build_index.py` archives one per refresh, keyed by the dataset's `generatedAt` date.")
A(f"- **Windows are uneven.** Snapshots are taken when the data is refreshed, not on a "
  f"fixed cadence — consecutive vintages here range from 1 day to several weeks apart. "
  f"Per-day normalization makes the boards comparable, but a 1-day window amplifies noise, "
  f"so treat short-window figures as directional.")
A("- **Star counts are a popularity signal, not a quality one.** A launch post, a "
  "conference talk, or a newsletter mention moves stars without anything changing in the code.")
A("- **Only repos present in both snapshots are diffed.** Newly starred repos appear under "
  "*New entrants* with no growth figure; unstarred repos silently drop out.")
A("- **The theme layer is hand-written** against the computed boards and does not refresh "
  "itself. Re-curate it when the movers change shape.")
A("- Re-run after a fresh `classified.json` to refresh every board.")
A("")
A(f"<sub>Repos tracked: {fmt_int(len(recent))} · Window: {PREV} → {NEWEST} ({RECENT_DAYS}d) · "
  f"Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta -------------------------------------------------------------
# `tool_count` / `total_stars` drive the index card and its sort order, and every
# other report defines them as "repos covered" and "their combined stars". Match
# that here — counting all 700-odd repos that ticked up would both misread on the
# card and rocket this report to the top of the size-sorted index.
featured = list(dict.fromkeys(
    [n for n, *_ in risers[:TOP_N]]
    + [b[0] for b in breakouts[:TOP_N]]
    + [n for n, *_ in sustained[:TOP_N]]
    + entrants
    + [c[0] for c in cooling[:15]]
))
featured = [n for n in featured if n in by_name]
featured_stars = sum(by_name[n]["stars"] for n in featured)

top_tools = [{"name": n, "stars": by_name[n]["stars"]}
             for n, *_ in risers[:5] if n in by_name]
categories = {
    "Risers": len([r for r in recent if r[1] > 0]),
    "Breakouts": len(breakouts),
    "New entrants": len(entrants),
    "Cooling": len(cooling),
}
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / Trends",
    "summary": (f"Measured star momentum across {len(dates)} data vintages: the "
                f"{RECENT_DAYS}-day movers, relative breakouts, sustained climbers, "
                f"{len(entrants)} new entrants, and what has gone flat."),
    "tool_count": len(featured),
    "total_stars": featured_stars,
    "categories": categories,
    "top_tools": top_tools,
    # Absolute stars would make this chart a popularity ranking; the report is
    # about movement, so plot the gain instead.
    "chart_top_series": [{"name": n, "value": g} for n, g, *_ in risers[:8]],
    "chart_top_title": f"Biggest star gains ({RECENT_DAYS}d)",
    "chart_cat_title": "Repos by movement type",
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/trending_now.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  window: {PREV} -> {NEWEST} ({RECENT_DAYS}d)")
print(f"  risers: {len(risers)} · breakouts: {len(breakouts)} · "
      f"entrants: {len(entrants)} · cooling: {len(cooling)}")
themed = [m for _t, _b, ms in THEMES for m in ms]
missing = [m for m in themed if m not in by_name]
if missing:
    print("  WARNING missing:", missing)
