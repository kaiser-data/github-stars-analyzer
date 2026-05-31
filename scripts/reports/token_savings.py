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
# Primary axis = WORKLOAD (what you're spending tokens on), because that's what
# decides which saver is relevant. full_name -> (workload, mechanism, claim, note)
WORKLOADS = [
    "Coding agents & codebases",
    "Generation & structured prompting",
    "Retrieval, RAG & documents",
    "Long-running agents & memory",
    "Model & inference level",
    "Methodology / cross-cutting",
]
TAXONOMY = {
    # ===== Coding agents & codebases =====
    "rtk-ai/rtk": ("Coding agents & codebases", "Wire-level proxy", "60–90% on dev cmds",
        "CLI proxy that intercepts common dev commands; integration-free 'install once, save everywhere'."),
    "colbymchenry/codegraph": ("Coding agents & codebases", "Code index/graph", "~70%",
        "Pre-indexed code knowledge graph for Claude Code/Codex/Cursor/OpenCode/Hermes — query instead of read."),
    "mksglu/context-mode": ("Coding agents & codebases", "Tool-output sandbox", "98% on tool output",
        "Sandboxes/truncates tool output in the context window; 15 platforms."),
    "MinishLab/semble": ("Coding agents & codebases", "Semantic code search", "~98% vs grep+read",
        "Fast, accurate code search for agents — replaces the grep+read pattern that dominates coding context."),
    "getagentseal/codeburn": ("Coding agents & codebases", "Measurement / observability", "— (measures)",
        "TUI dashboard showing where your Claude Code/Codex/Cursor tokens go. Measure before you optimize."),
    "yvgude/lean-ctx": ("Coding agents & codebases", "Context layer", "qualitative",
        "Cognitive context layer: 51+ MCP tools, multiple read modes, surgical reads (also in the MCP report)."),
    "JuliusBrussee/caveman": ("Coding agents & codebases", "Prompt-style skill", "~65%",
        "Claude Code skill that trims tokens by emitting terse 'caveman' output — cheap to try, trades readability."),
    "HKUDS/FastCode": ("Coding agents & codebases", "Code understanding", "qualitative",
        "Accelerates/streamlines code understanding — but low health and stale; verify first."),

    # ===== Generation & structured prompting =====
    "toon-format/toon": ("Generation & structured prompting", "Compact data format", "~30–50% on structured data",
        "Token-Oriented Object Notation — schema-aware, human-readable replacement for JSON when you feed data "
        "into prompts or ask for structured output. Cross-cutting, but lives at the generation/prompt layer."),

    # ===== Retrieval, RAG & documents =====
    "bytebase/dbhub": ("Retrieval, RAG & documents", "Token-efficient DB access", "qualitative",
        "Zero-dependency, token-efficient database MCP server (Postgres/MySQL/SQL Server/…) — keeps query results lean."),
    "iternal-technologies-partners/blockify-agentic-data-optimization": ("Retrieval, RAG & documents", "Data optimization (RAG)", "qualitative",
        "Replaces naive chunking with dense 'blocks' so retrieved context is smaller; declining/low health."),
    "deepseek-ai/DeepSeek-OCR": ("Retrieval, RAG & documents", "Optical context compression", "research",
        "'Contexts Optical Compression' — renders document context to images to fit more in window; low health & stale."),

    # ===== Long-running agents & memory =====
    "thedotmack/claude-mem": ("Long-running agents & memory", "Session compression", "qualitative",
        "Compresses & persists session context across runs so long projects don't re-pay for history (also in the Memory report)."),

    # ===== Model & inference level (not prompt tokens) =====
    "vllm-project/llm-compressor": ("Model & inference level", "Model weight compression", "n/a (inference, not prompt)",
        "Compresses model *weights* for cheaper/faster inference — a different layer than prompt-token savings; included for contrast."),

    # ===== Methodology / cross-cutting =====
    "davidkimai/Context-Engineering": ("Methodology / cross-cutting", "Methodology / guide", "— (educational)",
        "A guide to filling the context window with just the right info — concepts that apply to every workload above; stale."),
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
A("> **Read this first:** the right token-saver depends on **what you're spending tokens "
  "on** — reading code, generating structured output, retrieving documents, or carrying "
  "long-session memory. So this report is organized **by workload**, not by tool type. "
  "Tools at different layers mostly **compose** rather than compete. All **% figures are "
  "the projects' own claims** on the May-2026 snapshot — not independently benchmarked here.")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
by_workload = {w: [n for n in present if scope_of(n) == w] for w in WORKLOADS}
coding = by_workload["Coding agents & codebases"]

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} token-savings tools** in your stars (**{fmt_int(total_stars)}★**), "
  f"organized by workload:")
for w in WORKLOADS:
    m = by_workload[w]
    if m:
        A(f"  - **{w}** ({len(m)}): "
          + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(m, key=lambda x: -by_name[x]['stars'])))
A(f"- **Your collection skews hard to coding** — {len(coding)} of {len(present)} tools. The "
  f"big coding sink is *reading the codebase*, so the highest-leverage picks index/search "
  f"code (`semble`, `codegraph`) or tame tool output (`context-mode`).")
A(f"- **Different workload, different layer:** generation savings live in the *prompt/format* "
  f"(`toon`); retrieval savings in *what you fetch* (`dbhub`, `blockify`); long agents in "
  f"*session memory* (`claude-mem`); and model-level compression (`llm-compressor`) is a "
  f"separate concern entirely (cheaper inference, not fewer prompt tokens).")
A(f"- **The one integration-free win:** `rtk` (a CLI proxy) claims 60–90% with no per-agent "
  f"setup — and it's the most-starred here ({fmt_int(by_name['rtk-ai/rtk']['stars'])}★).")
A(f"- **Measure first:** `codeburn` shows where tokens actually go before you optimize.")
A("")

# --- Comparison tables, one per workload
def comp_table(names, header):
    A(f"### {header}")
    A("")
    A("| Tool | ★ | Health | Activity | Mechanism | Claimed saving |")
    A("|---|---|---|---|---|---|")
    for n in sorted(names, key=lambda x: -by_name[x]["stars"]):
        r = by_name[n]
        _, mech, claim, _note = TAXONOMY[n]
        A(f"| [{n}]({r['url']}) | {fmt_int(r['stars'])} | {r.get('health_score','—')} | "
          f"{activity_label(r)} | {mech} | {claim} |")
    A("")

A("## Comparison by workload")
A("")
for w in WORKLOADS:
    if by_workload[w]:
        comp_table(by_workload[w], w)

# --- Deep dives
A("## Details")
A("")
workload_blurb = {
    "Coding agents & codebases": "Claude Code, Codex, Cursor, OpenCode, Hermes — the biggest "
        "token sink for most users, dominated by reading/searching source and tool output.",
    "Generation & structured prompting": "When you feed data into prompts or ask for "
        "structured output — savings come from a tighter serialization format.",
    "Retrieval, RAG & documents": "When tokens go to fetched context — keep what you retrieve "
        "small and dense.",
    "Long-running agents & memory": "Multi-session work where re-sending history is the cost — "
        "compress and persist instead.",
    "Model & inference level": "A different layer: shrink the *model* for cheaper inference "
        "(doesn't reduce your prompt tokens).",
    "Methodology / cross-cutting": "Principles that apply across every workload above.",
}
for w in WORKLOADS:
    names = by_workload[w]
    if not names:
        continue
    A(f"### {w}")
    A("")
    A(f"_{workload_blurb[w]}_")
    A("")
    for n in sorted(names, key=lambda x: -by_name[x]["stars"]):
        r = by_name[n]
        _, mech, claim, note = TAXONOMY[n]
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
    A("| Tool | Workload | Health | Lifecycle | Last push |")
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
A(f"<sub>Tools covered: {len(present)} across {sum(1 for w in WORKLOADS if by_workload[w])} "
  f"workloads · Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta -------------------------------------------------------------
top = sorted(present, key=lambda x: -by_name[x]["stars"])[:5]
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / Efficiency",
    "summary": (f"{len(present)} token-savings tools ({fmt_int(total_stars)}★), organized by "
                "workload — coding agents/codebases, generation/prompting, retrieval/RAG, "
                "long-running memory, and model-level. Includes a stacking guide and risk flags."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {
        "Coding": len(by_workload["Coding agents & codebases"]),
        "Generation": len(by_workload["Generation & structured prompting"]),
        "Retrieval": len(by_workload["Retrieval, RAG & documents"]),
        "Memory": len(by_workload["Long-running agents & memory"]),
        "Model-level": len(by_workload["Model & inference level"]),
    },
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/token_savings.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)}  "
      + " | ".join(f"{w.split()[0]}:{len(by_workload[w])}" for w in WORKLOADS if by_workload[w]))
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
