#!/usr/bin/env python3
"""
Generate a report on token-savings / context-efficiency tooling found in the
starred-repos dataset, split into CODING (coding-agent / codebase context) vs
GENERAL (everything else), tagged by mechanism.

Inputs:
  public/data/classified.json
  public/data/graph.json

Output:
  reports/token-savings.md   (+ reports/token-savings.meta.json)

Run: python3 scripts/reports/token_savings.py
"""
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLASSIFIED = os.path.join(ROOT, "public/data/classified.json")
GRAPH = os.path.join(ROOT, "public/data/graph.json")
SLUG = "token-savings"
TITLE = "Token-Savings & Context-Efficiency Tooling"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy --------------------------------------------------------
# full_name -> (scope, mechanism, claimed_saving, note)
TAXONOMY = {
    # ===== CODING (coding agents / codebase context) =====
    "rtk-ai/rtk": ("Coding", "Wire-level proxy", "60–90% on dev cmds",
        "CLI proxy that intercepts common dev commands; integration-free 'install once, save everywhere'."),
    "colbymchenry/codegraph": ("Coding", "Code index/graph", "~70%",
        "Pre-indexed code knowledge graph for Claude Code/Codex/Cursor/OpenCode/Hermes — query instead of read."),
    "mksglu/context-mode": ("Coding", "Tool-output sandbox", "98% on tool output",
        "Sandboxes/truncates tool output in the context window; 15 platforms."),
    "MinishLab/semble": ("Coding", "Semantic code search", "~98% vs grep+read",
        "Fast, accurate code search for agents — replaces the grep+read pattern that dominates coding context."),
    "getagentseal/codeburn": ("Coding", "Measurement / observability", "— (measures)",
        "TUI dashboard showing where your Claude Code/Codex/Cursor tokens go. Measure before you optimize."),
    "yvgude/lean-ctx": ("Coding", "Context layer", "qualitative",
        "Cognitive context layer: 51+ MCP tools, multiple read modes, surgical reads (also in the MCP report)."),
    "JuliusBrussee/caveman": ("Coding", "Prompt-style skill", "~65%",
        "Claude Code skill that trims tokens by emitting terse 'caveman' output — cheap to try, trades readability."),
    "HKUDS/FastCode": ("Coding", "Code understanding", "qualitative",
        "Accelerates/streamlines code understanding — but low health and stale; verify first."),

    # ===== GENERAL (formats, data, model/inference, knowledge) =====
    "toon-format/toon": ("General", "Compact data format", "~30–50% on structured data",
        "Token-Oriented Object Notation — schema-aware, human-readable replacement for JSON in prompts."),
    "bytebase/dbhub": ("General", "Token-efficient DB access", "qualitative",
        "Zero-dependency, token-efficient database MCP server (Postgres/MySQL/SQL Server/…)."),
    "thedotmack/claude-mem": ("General", "Session compression", "qualitative",
        "Compresses & persists session context across runs (also in the Memory report)."),
    "vllm-project/llm-compressor": ("General", "Model weight compression", "n/a (inference, not prompt)",
        "Compresses model *weights* for cheaper inference — different layer than prompt-token savings; included for contrast."),
    "deepseek-ai/DeepSeek-OCR": ("General", "Optical context compression", "research",
        "'Contexts Optical Compression' — renders context to images to fit more in window; low health & stale."),
    "iternal-technologies-partners/blockify-agentic-data-optimization": ("General", "Data optimization (RAG)", "qualitative",
        "Replaces naive chunking with dense 'blocks' for enterprise RAG; declining/low health."),
    "davidkimai/Context-Engineering": ("General", "Methodology / guide", "— (educational)",
        "A guide to filling the context window with just the right info — concepts, not a tool; stale."),
}

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
inter_edges = [l for l in gr["links"]
               if l["source"] in sel_node_ids and l["target"] in sel_node_ids]

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

def scope_of(n):
    return TAXONOMY[n][0]

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
  f"`scripts/reports/token_savings.py` (regenerate any time — no API cost).")
A("")
A("> **Read this first:** these tools cut tokens at *different layers* (codebase reads, "
  "tool output, data format, the wire, model weights). They mostly **compose** rather than "
  "compete. All **% figures are the projects' own claims** on the May-2026 snapshot — not "
  "independently benchmarked here.")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
coding = [n for n in present if scope_of(n) == "Coding"]
general = [n for n in present if scope_of(n) == "General"]

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} token-savings tools** in your stars (**{fmt_int(total_stars)}★**), "
  f"split into **{len(coding)} coding-focused** and **{len(general)} general-purpose**.")
A(f"- **Coding is where the tokens are.** For coding agents the biggest sink is "
  f"*reading the codebase* — so the highest-leverage tools index/search code "
  f"(`semble`, `codegraph`) or tame tool output (`context-mode`).")
A(f"- **The one integration-free win:** `rtk` (a CLI proxy) claims 60–90% with no per-agent "
  f"setup — the best 'install once' option, and the most-starred ({fmt_int(by_name['rtk-ai/rtk']['stars'])}★).")
A(f"- **General tooling works at the format/data layer** (`toon` compact serialization, "
  f"`dbhub` efficient DB access) and **composes** with the coding tools above.")
A(f"- **Measure first:** `codeburn` shows where tokens actually go before you optimize.")
A("")

# --- Quick comparison tables per scope
def comp_table(names, header):
    A(f"### {header}")
    A("")
    A("| Tool | ★ | Health | Activity | Mechanism | Claimed saving |")
    A("|---|---|---|---|---|---|")
    for n in sorted(names, key=lambda x: -by_name[x]["stars"]):
        r = by_name[n]
        scope, mech, claim, _ = TAXONOMY[n]
        A(f"| [{n}]({r['url']}) | {fmt_int(r['stars'])} | {r.get('health_score','—')} | "
          f"{activity_label(r)} | {mech} | {claim} |")
    A("")

A("## Comparison")
A("")
comp_table(coding, "Coding-agent / codebase token savings")
comp_table(general, "General / other token savings")

# --- Deep dives
A("## Details")
A("")
for scope, names, blurb in [
    ("Coding", coding, "Token savings aimed at coding agents (Claude Code, Codex, Cursor, "
        "OpenCode, Hermes) and codebase context — the largest token sink for most users."),
    ("General", general, "Token / context savings that aren't coding-specific: data formats, "
        "DB access, session compression, model-weight & research approaches."),
]:
    A(f"### {scope}")
    A("")
    A(f"_{blurb}_")
    A("")
    for n in sorted(names, key=lambda x: -by_name[x]["stars"]):
        r = by_name[n]
        scope2, mech, claim, note = TAXONOMY[n]
        topics = ", ".join((r.get("topics") or [])[:6]) or "—"
        A(f"- **[{n}]({r['url']})** · {fmt_int(r['stars'])}★ · {r.get('primary_language') or '—'} · "
          f"{r.get('lifecycle_stage','—')} · health {r.get('health_score','—')} · _{mech}_ · **{claim}**  ")
        A(f"  {note}  ")
        A(f"  <sub>topics: {topics}</sub>")
    A("")

# --- How to combine
A("## How to stack them")
A("")
A("Because they hit different layers, a strong setup combines several:")
A("")
A("| Your token sink | Reach for | Layer |")
A("|---|---|---|")
A("| Reading source code | `MinishLab/semble` or `colbymchenry/codegraph` | retrieval |")
A("| Noisy tool / command output | `mksglu/context-mode` | tool output |")
A("| Everything, no integration | `rtk-ai/rtk` | wire (proxy) |")
A("| Structured data in prompts | `toon-format/toon` | format |")
A("| Database queries | `bytebase/dbhub` | data access |")
A("| Long multi-session work | `thedotmack/claude-mem` | session memory |")
A("| Don't know yet | `getagentseal/codeburn` | measurement |")
A("")

# --- Recommendations
A("## Recommendations")
A("")
A("**For coding agents (most people):**")
A("1. `rtk-ai/rtk` — best general, integration-free reduction (60–90%, "
  f"{fmt_int(by_name['rtk-ai/rtk']['stars'])}★, health {by_name['rtk-ai/rtk'].get('health_score')}).")
A("2. `MinishLab/semble` (sharpest claim) or `colbymchenry/codegraph` (most adopted) — "
  "kill the read-the-codebase cost.")
A("3. `mksglu/context-mode` — pair on top to tame tool output.")
A("")
A("**General add-ons:**")
A("- `toon-format/toon` if you feed structured data into prompts (format-level, composes "
  "with everything).")
A("- `getagentseal/codeburn` first if you want evidence on where to focus.")
A("")

# --- Risk
A("## ⚠️ Adopt with caution")
A("")
A("Low health and/or stale — verify before relying on:")
A("")
risky = [n for n in present
         if (by_name[n].get("health_score") or 100) < 50
         or (by_name[n].get("days_since_push") or 0) > 45
         or by_name[n].get("lifecycle_stage") in ("Declining", "Abandoned")]
if risky:
    A("| Tool | Scope | Health | Lifecycle | Last push |")
    A("|---|---|---|---|---|")
    for n in sorted(risky, key=lambda x: by_name[x].get("health_score") or 0):
        r = by_name[n]
        A(f"| [{n}]({r['url']}) | {scope_of(n)} | {r.get('health_score','—')} | "
          f"{r.get('lifecycle_stage','—')} | {days_to_human(r.get('days_since_push'))} ago |")
    A("")
else:
    A("- _Nothing flagged._")
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
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities** — token-savings is "
  f"a cross-cutting concern, not a single cluster.")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 2:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in names))
A("")

ranked = sorted(
    [(node_for(n).get("pagerank", 0) if node_for(n) else 0, n) for n in present],
    key=lambda x: -x[0],
)
A("**Centrality (PageRank in the full 1,071-repo graph):**")
A("")
for pr, n in ranked[:8]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between these tools** (similarity edges where both endpoints are in this "
  "report):")
A("")
if inter_edges:
    id_to_name = {v: k for k, v in name_to_nodeid.items()}
    for e in sorted(inter_edges, key=lambda x: -x["weight"])[:12]:
        a = id_to_name.get(e["source"], e["source"])
        b = id_to_name.get(e["target"], e["target"])
        why = []
        if e.get("shared_topics"):
            why.append("topics: " + ", ".join(e["shared_topics"][:4]))
        if e.get("shared_authors"):
            why.append("authors: " + ", ".join(e["shared_authors"][:3]))
        A(f"- `{a}` ⇄ `{b}` (w={e['weight']:.3f})" + (f" — {'; '.join(why)}" if why else ""))
else:
    A("- _None._ These tools connect out to the agents/data they optimize rather than to "
      "each other — consistent with them being complementary layers.")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external "
  "calls; fully reproducible.")
A("- **Selection**: scan for token / context-window / compression signals (and explicit "
  "`NN% fewer/less` claims) across name/description/topics/README, then manual curation "
  "into Coding vs General and by mechanism.")
A("- **% savings are vendor-claimed**, measured on the projects' own workloads — not "
  "verified here. Real savings depend heavily on *your* usage pattern.")
A("- **Metrics** (health, lifecycle, days_since_push) are precomputed at snapshot time and "
  "may lag GitHub. Re-run after a fresh `classified.json` to refresh.")
A("")
A(f"<sub>Tools covered: {len(present)} ({len(coding)} coding / {len(general)} general) · "
  f"Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta -------------------------------------------------------------
top = sorted(present, key=lambda x: -by_name[x]["stars"])[:5]
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / Efficiency",
    "summary": (f"{len(present)} token-savings tools ({fmt_int(total_stars)}★), split "
                f"{len(coding)} coding (code search/index, tool-output sandbox, CLI proxy) vs "
                f"{len(general)} general (compact formats, DB access, session/model "
                "compression). Includes a stacking guide and risk flags."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {"Coding": len(coding), "General": len(general)},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/token_savings.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)}  (coding: {len(coding)}, general: {len(general)})")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
