#!/usr/bin/env python3
"""
Generate a comprehensive comparison report of LLM / Agent *memory* frameworks
found in the starred-repos dataset.

Inputs:
  public/data/classified.json   (full repo metadata)
  public/data/graph.json        (repo-similarity graph: communities, pagerank, edges)

Output:
  reports/memory-frameworks-for-llm-agents.md

Run: python3 scripts/reports/memory_frameworks.py
"""
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLASSIFIED = os.path.join(ROOT, "public/data/classified.json")
GRAPH = os.path.join(ROOT, "public/data/graph.json")
OUT = os.path.join(ROOT, "reports/memory-frameworks-for-llm-agents.md")

# ---- Curated taxonomy (derived from scanning all 1071 repos) -----------------
# Each entry: full_name -> (tier, one-line "approach" note)
TAXONOMY = {
    # Tier 1 — General-purpose agent memory frameworks / platforms
    "mem0ai/mem0": ("General memory layer", "Universal, LLM-agnostic memory API; extract+store+retrieve facts across sessions."),
    "topoteretes/cognee": ("General memory layer", "'Memory control plane' — ECL (extract-cognify-load) pipelines into a knowledge graph + vector store."),
    "getzep/graphiti": ("General memory layer", "Temporal knowledge graph engine behind Zep; bi-temporal edges, real-time incremental updates."),
    "MemoriLabs/Memori": ("General memory layer", "Agent-native memory infra; turns execution & conversations into structured recall."),
    "memvid/memvid": ("General memory layer", "Serverless single-file memory layer; replaces RAG pipelines with a portable artifact."),
    "plastic-labs/honcho": ("General memory layer", "Memory library for stateful agents; user-modeling / theory-of-mind oriented."),
    "Tencent/TencentDB-Agent-Memory": ("General memory layer", "Fully-local long-term memory via a 4-tier progressive pipeline."),
    "memodb-io/Acontext": ("General memory layer", "Treats agent 'skills' as a memory layer."),
    "MemPalace/mempalace": ("General memory layer", "Benchmark-focused open-source memory system."),
    "supermemoryai/openclaw-supermemory": ("General memory layer", "Long-term memory & recall, packaged for OpenClaw agents."),
    "Einsia/OpenChronicle": ("General memory layer", "Local-first memory for any tool-capable LLM agent."),
    "ActiveMemory/ctx": ("General memory layer", "Single-binary, local-first 'convergent' memory for humans + machines."),

    # Tier 2 — Coding-agent / session memory (Claude Code & co.)
    "thedotmack/claude-mem": ("Coding-agent memory", "Persistent context across sessions; captures everything an agent does and re-injects it."),
    "campfirein/byterover-cli": ("Coding-agent memory", "Portable memory layer for autonomous coding agents (formerly Cipher)."),
    "gastownhall/beads": ("Coding-agent memory", "Distributed graph issue-tracker as durable agent memory (Dolt-backed)."),
    "andrewyng/context-hub": ("Coding-agent memory", "Curated, versioned docs so agents stop hallucinating APIs / forgetting."),

    # Tier 3 — Knowledge-graph / context-graph memory frameworks
    "trustgraph-ai/trustgraph": ("Knowledge-graph memory", "Agent runtime platform powered by context graphs + ontology."),
    "semantica-agi/semantica": ("Knowledge-graph memory", "AI-native KG framework: semantic retrieval, ontology reasoning, provenance."),
    "shaneholloman/mcp-knowledge-graph": ("Knowledge-graph memory", "MCP server giving Claude persistent memory via a local knowledge graph."),
    "needle-ai/needle-mcp": ("Knowledge-graph memory", "MCP server: long-term memory for LLMs via managed RAG."),

    # Tier 4 — LLM framework that bundles a memory module
    "zmedelis/bosquet": ("LLM framework w/ memory", "Clojure LLMOps toolkit; prompt composition + agents + LLM memory."),
}

# Memory *substrate* (vector / graph DBs) — enablers, listed separately.
SUBSTRATE = {
    "redis/redis": "In-memory data store; common KV/vector backing for memory layers.",
    "facebookresearch/faiss": "Dense-vector similarity search library; embedding index substrate.",
    "chroma-core/chroma": "AI-native search/vector DB used as memory storage.",
    "alibaba/zvec": "Lightweight in-process vector database.",
    "FalkorDB/FalkorDB": "Fast graph database (GraphBLAS) for graph-shaped memory.",
}

# ---- Load data ---------------------------------------------------------------
with open(CLASSIFIED) as f:
    cl = json.load(f)
with open(GRAPH) as f:
    gr = json.load(f)

by_name = {r["full_name"]: r for r in cl["repos"]}
nodes_by_id = {n["id"]: n for n in gr["nodes"]}
name_to_nodeid = {n["full_name"]: n["id"] for n in gr["nodes"]}

# Build adjacency for edges among our selected set
sel_names = list(TAXONOMY.keys())
sel_node_ids = {name_to_nodeid[n] for n in sel_names if n in name_to_nodeid}

inter_edges = []  # edges where BOTH endpoints are selected memory frameworks
neighbor_count = {}  # node_id -> total degree to anything
for link in gr["links"]:
    s, t = link["source"], link["target"]
    if s in sel_node_ids and t in sel_node_ids:
        inter_edges.append(link)

# community membership for selected
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

# ---- Build report ------------------------------------------------------------
gen = cl.get("generatedAt", "")
user = cl.get("username", "")
lines = []
A = lines.append

A(f"# Memory Frameworks for LLMs & Agents — Comparative Report")
A("")
A(f"> Derived from **{user}**'s {fmt_int(cl['total'])} starred repos "
  f"(snapshot `{gen}`), cross-referenced with the repo-similarity graph "
  f"({fmt_int(gr['stats'].get('nodes', len(gr['nodes'])))} nodes / "
  f"{fmt_int(gr['stats'].get('edges', len(gr['links'])))} edges, "
  f"{len(gr['communities'])} communities).")
A(f">")
A(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/memory_frameworks.py` (regenerate any time — no API cost).")
A("")

# --- Executive summary
present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
langs = {}
for n in present:
    l = by_name[n].get("primary_language") or "—"
    langs[l] = langs.get(l, 0) + 1
top_lang = sorted(langs.items(), key=lambda x: -x[1])
A("## Executive summary")
A("")
A(f"- **{len(present)} dedicated memory frameworks** identified across your stars, "
  f"plus **{len(SUBSTRATE)} storage substrates** (vector/graph DBs) they build on.")
A(f"- Combined reach: **{fmt_int(total_stars)}★**. The space is overwhelmingly "
  f"**{top_lang[0][0]}** ({top_lang[0][1]}/{len(present)} projects).")
A(f"- Four sub-categories emerge: **general memory layers**, **coding-agent/session "
  f"memory**, **knowledge-graph memory**, and frameworks that **bundle a memory module**.")
A(f"- The dominant architectural split is **vector-recall vs. knowledge-graph** memory — "
  f"with a clear trend toward *temporal knowledge graphs* (graphiti) and "
  f"*local-first* designs (OpenChronicle, ctx, TencentDB-Agent-Memory).")
A("")

# --- Master comparison table
A("## Master comparison")
A("")
A("Sorted by stars. `Health` and `Momentum` come from the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits.")
A("")
hdr = ("| Project | Category | Lang | License | ★ Stars | Lifecycle | Health | "
       "Activity | Last push | Age | Contrib(90d) |")
A(hdr)
A("|" + "---|" * 12)
for n in sorted(present, key=lambda x: -by_name[x]["stars"]):
    r = by_name[n]
    cat = TAXONOMY[n][0]
    A("| [{name}]({url}) | {cat} | {lang} | {lic} | {stars} | {lc} | {hs} | "
      "{act} | {push} | {age} | {auth} |".format(
        name=n, url=r["url"], cat=cat,
        lang=r.get("primary_language") or "—",
        lic=(r.get("license") or "—"),
        stars=fmt_int(r["stars"]),
        lc=r.get("lifecycle_stage") or "—",
        hs=r.get("health_score") if r.get("health_score") is not None else "—",
        act=activity_label(r),
        push=days_to_human(r.get("days_since_push")) + " ago",
        age=days_to_human(r.get("age_days")),
        auth=r.get("unique_authors_90d") if r.get("unique_authors_90d") is not None else "—",
    ))
A("")

# --- Category deep dives
A("## By category")
A("")
order = ["General memory layer", "Coding-agent memory", "Knowledge-graph memory", "LLM framework w/ memory"]
cat_blurb = {
    "General memory layer": "Drop-in memory APIs for any agent: store interactions/facts, "
        "retrieve relevant context on demand. The crowded, fast-moving core of the space.",
    "Coding-agent memory": "Memory specialized for coding assistants (Claude Code, Cursor, "
        "OpenClaw): persist project context, decisions, and history across sessions.",
    "Knowledge-graph memory": "Memory as a structured graph/ontology rather than a vector "
        "blob — better provenance, reasoning, and explainability.",
    "LLM framework w/ memory": "Broader LLMOps toolkits that ship memory as one module.",
}
for cat in order:
    members = [n for n in present if TAXONOMY[n][0] == cat]
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

# --- Graph analysis
A("## Graph analysis — how they relate")
A("")
# community distribution
comm = {}
for n in present:
    nd = node_for(n)
    if nd is not None:
        c = nd.get("community")
        comm.setdefault(c, []).append(n)
A(f"**Community clustering.** The {len(present)} frameworks fall into "
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities** — "
  f"meaning memory tooling does *not* form one tight cluster but is spread across "
  f"the AI-infra landscape (each tends to cluster with its neighbors: vector DBs, "
  f"agent frameworks, or MCP tooling).")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 2:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in names))
A("")

# centrality
ranked = sorted(
    [(node_for(n).get("pagerank", 0) if node_for(n) else 0, n) for n in present],
    key=lambda x: -x[0],
)
A("**Centrality (PageRank in the full 1,071-repo graph).** Higher = more "
  "connected to the rest of your starred ecosystem (a proxy for how 'hub-like' "
  "the project is):")
A("")
for pr, n in ranked[:8]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

# inter-framework edges
A("**Direct links between memory frameworks** (similarity edges where both "
  "endpoints are in this report):")
A("")
if inter_edges:
    id_to_name = {v: k for k, v in name_to_nodeid.items()}
    for e in sorted(inter_edges, key=lambda x: -x["weight"]):
        a = id_to_name.get(e["source"], e["source"])
        b = id_to_name.get(e["target"], e["target"])
        why = []
        if e.get("shared_topics"):
            why.append("topics: " + ", ".join(e["shared_topics"][:4]))
        if e.get("shared_authors"):
            why.append("authors: " + ", ".join(e["shared_authors"][:3]))
        A(f"- `{a}` ⇄ `{b}` (w={e['weight']:.3f})" + (f" — {'; '.join(why)}" if why else ""))
else:
    A("- _None._ These frameworks are competitors that don't share authors or "
      "topic tags directly — each connects to substrate/agent repos instead, "
      "confirming a fragmented, early-stage market.")
A("")

# --- Maintenance / risk ranking
A("## Maintenance & risk signal")
A("")
A("Bus factor = how concentrated commits are in one author (1 = single-maintainer risk). "
  "Use alongside lifecycle + activity before adopting.")
A("")
A("| Project | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |")
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

# --- Selection guidance
A("## Which one should you use?")
A("")
A("| If you want… | Start with | Why |")
A("|---|---|---|")
guide = [
    ("A batteries-included, widely-adopted memory API", "`mem0ai/mem0`",
     "Largest mindshare among dedicated layers; LLM-agnostic; well-documented."),
    ("Temporal / relationship-aware memory (knowledge graph)", "`getzep/graphiti`",
     "Bi-temporal KG with real-time incremental updates; strongest graph design."),
    ("A full 'memory control plane' with pipelines", "`topoteretes/cognee`",
     "ECL pipelines + graph + vector; more framework than library."),
    ("Memory for a coding agent (Claude Code/Cursor)", "`thedotmack/claude-mem`",
     "Purpose-built session persistence; by far the most-starred in this niche."),
    ("Local-first / no-cloud memory", "`Einsia/OpenChronicle` or `Tencent/TencentDB-Agent-Memory`",
     "Both emphasize fully-local long-term memory."),
    ("Provenance / explainable, ontology-driven memory", "`trustgraph-ai/trustgraph` / `semantica-agi/semantica`",
     "Context graphs with reasoning + full provenance."),
    ("Drop-in via MCP (no SDK lock-in)", "`shaneholloman/mcp-knowledge-graph` / `needle-ai/needle-mcp`",
     "Expose memory to any MCP-capable client."),
]
for want, pick, why in guide:
    A(f"| {want} | {pick} | {why} |")
A("")

# --- Substrate
A("## Memory substrate (storage layer)")
A("")
A("Not memory *frameworks*, but the databases these layers typically sit on. "
  "Several are also in your stars:")
A("")
A("| Store | ★ Stars | Lang | Role |")
A("|---|---|---|---|")
for n, role in SUBSTRATE.items():
    r = by_name.get(n)
    if not r:
        continue
    A(f"| [{n}]({r['url']}) | {fmt_int(r['stars'])} | {r.get('primary_language') or '—'} | {role} |")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `public/data/classified.json` (full metadata) + "
  "`public/data/graph.json` (similarity graph). No external calls; fully reproducible.")
A("- **Selection**: keyword scan across name/description/topics/README for memory + "
  "LLM/agent signals, then manual curation into the taxonomy in this script. Generic "
  "'memory-efficient' infra (e.g. vLLM) and pure tutorials/awesome-lists were excluded.")
A("- **Metrics** (health, momentum, lifecycle, bus_factor) are precomputed by the "
  "analyzer pipeline at snapshot time and may lag GitHub's current state.")
A("- **The market is young**: many of these launched in the last 12 months; star counts "
  "and activity shift fast. Re-run this script after a fresh `classified.json` to refresh.")
A("")
A(f"<sub>Frameworks covered: {len(present)} · Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

print(f"Wrote {OUT}")
print(f"  frameworks: {len(present)} | substrate: {sum(1 for n in SUBSTRATE if n in by_name)}")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing from dataset:", missing)
