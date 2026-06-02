#!/usr/bin/env python3
"""
Head-to-head report: NousResearch/hermes-agent vs openclaw/openclaw, placed
within the broader field of personal-AI-assistant / agent-harness projects in
the starred-repos dataset.

Inputs:
  public/data/classified.json
  public/data/graph.json

Output:
  reports/hermes-vs-openclaw.md   (+ reports/hermes-vs-openclaw.meta.json)

Run: python3 scripts/reports/hermes_vs_openclaw.py
"""
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLASSIFIED = os.path.join(ROOT, "public/data/classified.json")
GRAPH = os.path.join(ROOT, "public/data/graph.json")
SLUG = "hermes-vs-openclaw"
TITLE = "Hermes Agent vs OpenClaw — Head-to-Head"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

A_REPO = "openclaw/openclaw"
B_REPO = "NousResearch/hermes-agent"

# Broader field of personal-assistant / agent-harness contenders for context.
FIELD = [
    "openclaw/openclaw",
    "NousResearch/hermes-agent",
    "bytedance/deer-flow",
    "code-yeongyu/oh-my-openagent",
    "zeroclaw-labs/zeroclaw",
    "elizaOS/eliza",
    "nanocoai/nanoclaw",
    "nearai/ironclaw",
    "HKUDS/nanobot",
    "RightNow-AI/openfang",
]

# ---- Load --------------------------------------------------------------------
with open(CLASSIFIED) as f:
    cl = json.load(f)
with open(GRAPH) as f:
    gr = json.load(f)

by_name = {r["full_name"]: r for r in cl["repos"]}
nodes_by_id = {n["id"]: n for n in gr["nodes"]}
name_to_nodeid = {n["full_name"]: n["id"] for n in gr["nodes"]}

def node_for(name):
    nid = name_to_nodeid.get(name)
    return nodes_by_id.get(nid) if nid else None

# ---- Helpers -----------------------------------------------------------------
def fmt_int(n):
    try:
        return f"{int(n):,}"
    except Exception:
        return str(n)

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

def mom(r):
    m = r.get("momentum") or {}
    return m.get("estimated_stars_30d")

def winner(a_val, b_val, higher_better=True):
    """Return ('A'|'B'|'=') for which repo wins a metric."""
    if a_val is None or b_val is None:
        return "="
    if a_val == b_val:
        return "="
    if higher_better:
        return "A" if a_val > b_val else "B"
    return "A" if a_val < b_val else "B"

# ---- Build -------------------------------------------------------------------
gen = cl.get("generatedAt", "")
user = cl.get("username", "")
A_ = by_name[A_REPO]
B_ = by_name[B_REPO]
lines = []
P = lines.append

P(f"# {TITLE}")
P("")
P(f"> Derived from **{user}**'s {fmt_int(cl['total'])} starred repos "
  f"(snapshot `{gen}`), cross-referenced with the repo-similarity graph.")
P(">")
P(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/hermes_vs_openclaw.py` (regenerate any time — no API cost).")
P("")
P(f"**[{A_REPO}]({A_['url']})** — 🦞 _{(A_.get('description') or '').strip()}_  ")
P(f"**[{B_REPO}]({B_['url']})** — ☤ _{(B_.get('description') or '').strip()}_")
P("")

# --- Verdict up top
a_stars, b_stars = A_["stars"], B_["stars"]
P("## Verdict")
P("")
P(f"**Default to OpenClaw.** It leads on adoption ({fmt_int(a_stars)}★ vs "
  f"{fmt_int(b_stars)}★), velocity, release cadence and health, and it's the hub the rest "
  f"of your starred ecosystem plugs into. **Choose Hermes** if you want a Python-first, "
  f"NousResearch-backed single agent that 'grows with you', or a broader contributor base.")
P("")

# --- Side-by-side metric table with winners
def row(label, a_disp, b_disp, w):
    aw = " 🏆" if w == "A" else ""
    bw = " 🏆" if w == "B" else ""
    P(f"| {label} | {a_disp}{aw} | {b_disp}{bw} |")

P("## Side-by-side (🏆 = leads that metric)")
P("")
P(f"| Metric | 🦞 OpenClaw | ☤ Hermes Agent |")
P("|---|---|---|")
row("Stars", fmt_int(a_stars), fmt_int(b_stars), winner(a_stars, b_stars))
row("Health score", A_.get("health_score"), B_.get("health_score"),
    winner(A_.get("health_score"), B_.get("health_score")))
row("Momentum (est. ★/30d)", fmt_int(mom(A_)), fmt_int(mom(B_)), winner(mom(A_), mom(B_)))
row("Language", A_.get("primary_language") or "—", B_.get("primary_language") or "—", "=")
row("License", A_.get("license") or "—", B_.get("license") or "—", "=")
row("Lifecycle", A_.get("lifecycle_stage") or "—", B_.get("lifecycle_stage") or "—", "=")
row("Age", days_to_human(A_.get("age_days")), days_to_human(B_.get("age_days")),
    "=")
row("Last push", days_to_human(A_.get("days_since_push")) + " ago",
    days_to_human(B_.get("days_since_push")) + " ago", "=")
row("Commits (90d)", fmt_int(A_.get("commits_90d")), fmt_int(B_.get("commits_90d")),
    winner(A_.get("commits_90d"), B_.get("commits_90d")))
row("Contributors (90d)", A_.get("unique_authors_90d"), B_.get("unique_authors_90d"),
    winner(A_.get("unique_authors_90d"), B_.get("unique_authors_90d")))
row("Bus factor", A_.get("bus_factor"), B_.get("bus_factor"),
    winner(A_.get("bus_factor"), B_.get("bus_factor")))
row("Top-author share (lower=better)",
    f"{A_.get('top_author_share'):.0%}" if isinstance(A_.get('top_author_share'), (int, float)) else "—",
    f"{B_.get('top_author_share'):.0%}" if isinstance(B_.get('top_author_share'), (int, float)) else "—",
    winner(A_.get("top_author_share"), B_.get("top_author_share"), higher_better=False))
row("Releases (total)", fmt_int(A_.get("releases_total")), fmt_int(B_.get("releases_total")),
    winner(A_.get("releases_total"), B_.get("releases_total")))
row("Forks", fmt_int(A_.get("forks")), fmt_int(B_.get("forks")),
    winner(A_.get("forks"), B_.get("forks")))
row("Open issues", fmt_int(A_.get("open_issues")), fmt_int(B_.get("open_issues")), "=")
row("Merged PRs", fmt_int(A_.get("merged_prs")), fmt_int(B_.get("merged_prs")),
    winner(A_.get("merged_prs"), B_.get("merged_prs")))
P("")

# --- Analysis
P("## What the numbers say")
P("")
ratio_stars = a_stars / b_stars if b_stars else 0
ratio_commits = (A_.get("commits_90d") or 0) / max(1, B_.get("commits_90d") or 1)
ratio_mom = (mom(A_) or 0) / max(1, mom(B_) or 1)
P(f"- **Adoption & momentum → OpenClaw.** {ratio_stars:.1f}× the stars and ~{ratio_mom:.1f}× "
  f"the 30-day momentum. It's also younger ({days_to_human(A_.get('age_days'))} vs "
  f"{days_to_human(B_.get('age_days'))}), so it reached a larger base faster.")
P(f"- **Velocity & release cadence → OpenClaw.** ~{ratio_commits:.1f}× the 90-day commits and "
  f"**{fmt_int(A_.get('releases_total'))} releases vs {fmt_int(B_.get('releases_total'))}** — a far "
  f"more established, iterative shipping process.")
P(f"- **Contributor breadth → Hermes.** {B_.get('unique_authors_90d')} unique authors in 90 days "
  f"vs {A_.get('unique_authors_90d')} — a wider bench, though its top author carries more "
  f"({B_.get('top_author_share'):.0%} vs {A_.get('top_author_share'):.0%}).")
P(f"- **Health → OpenClaw** ({A_.get('health_score')} vs {B_.get('health_score')}), and both "
  f"share bus factor {A_.get('bus_factor')} — neither is a one-person project, but neither is "
  f"deeply decentralised either.")
P(f"- **Stack split.** OpenClaw is **TypeScript**, Hermes is **Python** — often the deciding "
  f"factor for what you'll actually extend.")
P("")

# --- Ecosystem / graph
P("## Ecosystem & graph signal")
P("")
na, nb = node_for(A_REPO), node_for(B_REPO)
if na and nb:
    same = na.get("community") == nb.get("community")
    P(f"- **Communities:** OpenClaw is in community {na.get('community')}, Hermes in "
      f"{nb.get('community')} "
      f"({'same cluster' if same else 'different clusters'}). PageRank — OpenClaw "
      f"{na.get('pagerank',0):.4f} vs Hermes {nb.get('pagerank',0):.4f}.")
# direct edge?
edge = None
ida, idb = name_to_nodeid.get(A_REPO), name_to_nodeid.get(B_REPO)
for l in gr["links"]:
    if {l["source"], l["target"]} == {ida, idb}:
        edge = l
        break
if edge:
    why = []
    if edge.get("shared_topics"):
        why.append("shared topics: " + ", ".join(edge["shared_topics"][:5]))
    if edge.get("shared_authors"):
        why.append("shared authors: " + ", ".join(edge["shared_authors"][:3]))
    P(f"- **Direct similarity edge** between them (w={edge['weight']:.3f})"
      + (f" — {'; '.join(why)}." if why else "."))
else:
    P("- **No direct similarity edge** between them in the graph.")
P(f"- **Hermes explicitly tags the OpenClaw ecosystem** — its topics include "
  + ", ".join(f"`{t}`" for t in (B_.get("topics") or []) if t in
              ("openclaw", "clawdbot", "moltbot")) + " — i.e. it positions in/around the "
  "same space (interop or competition), not as an unrelated project.")
P(f"- **The accessory ecosystem orbits OpenClaw**, not Hermes: your stars already include "
  "`nanoclaw`, `clawhub`, `ClawRouter`, `opik-openclaw`, `openclaw-supermemory`, "
  "`NemoClaw`, `moltworker` — all OpenClaw-specific. That network effect is a real "
  "switching cost in OpenClaw's favour.")
P("")

# --- Broader field
P("## The broader field")
P("")
P("Where the two sit among the other personal-assistant / agent-harness projects in your "
  "stars:")
P("")
P("| Project | ★ Stars | Lang | Health | Lifecycle | Momentum (★/30d) | Note |")
P("|---|---|---|---|---|---|---|")
note = {
    "openclaw/openclaw": "**this comparison** — the hub",
    "NousResearch/hermes-agent": "**this comparison** — Python challenger",
    "bytedance/deer-flow": "long-horizon SuperAgent harness",
    "code-yeongyu/oh-my-openagent": "agent harness (ex oh-my-opencode)",
    "zeroclaw-labs/zeroclaw": "healthiest alternative (Rust)",
    "elizaOS/eliza": "agentic OS, always-on agents",
    "nanocoai/nanoclaw": "containerized secure OpenClaw alt",
    "nearai/ironclaw": "privacy/security Agent-OS (Rust)",
    "HKUDS/nanobot": "lightweight agent",
    "RightNow-AI/openfang": "open Agent-OS (Rust)",
}
field_present = [n for n in FIELD if n in by_name]
for n in sorted(field_present, key=lambda x: -by_name[x]["stars"]):
    r = by_name[n]
    P(f"| [{n}]({r['url']}) | {fmt_int(r['stars'])} | {r.get('primary_language') or '—'} | "
      f"{r.get('health_score','—')} | {r.get('lifecycle_stage','—')} | "
      f"{fmt_int(mom(r)) if mom(r) is not None else '—'} | {note.get(n,'')} |")
P("")

# --- When to pick which
P("## Which should you use?")
P("")
P("| Choose… | If you… |")
P("|---|---|")
P("| 🦞 **OpenClaw** | want the largest ecosystem + fastest shipping; rely on the accessory "
  "tools (skills, routers, memory) you've already starred; prefer TypeScript; want a broad "
  "assistant *platform*. |")
P("| ☤ **Hermes Agent** | are Python-first; value NousResearch's research lineage & community; "
  "want a single agent that *learns/grows* over time; prefer a wider contributor base. |")
P("| **Both (A/B them)** | `cc-switch` and `AionUi` (in your stars) run OpenClaw, Hermes, "
  "Claude Code & Codex side-by-side — try them on your own tasks before committing. |")
P("")

# --- Caveats
P("## Caveats")
P("")
P("- **Snapshot-bound.** All figures are the May-2026 dataset; this space moves weekly and "
  "momentum especially can flip fast.")
P("- **Stars ≠ fit.** Adoption and velocity don't decide *your* use case — language, "
  "extension model, and the specific tasks matter more. Treat this as a starting point.")
P("- Metrics (health, momentum, bus_factor) are precomputed by the analyzer pipeline.")
P("")
P(f"<sub>Snapshot: {gen} · regenerate via scripts/reports/hermes_vs_openclaw.py</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta -------------------------------------------------------------
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / Comparison",
    "summary": (f"Head-to-head: OpenClaw ({fmt_int(a_stars)}★) vs Hermes Agent "
                f"({fmt_int(b_stars)}★) on adoption, velocity, health, maintenance & ecosystem, "
                "plus the broader field of personal-assistant agents. Verdict: default OpenClaw; "
                "Hermes if Python-first."),
    "tool_count": len(field_present),
    "total_stars": sum(by_name[n]["stars"] for n in field_present),
    "categories": {"Principals": 2, "Field": len(field_present) - 2},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]}
                  for n in sorted(field_present, key=lambda x: -by_name[x]["stars"])[:5]],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/hermes_vs_openclaw.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  field projects present: {len(field_present)} / {len(FIELD)}")
missing = [n for n in FIELD if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
