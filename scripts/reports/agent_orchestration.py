#!/usr/bin/env python3
"""
Generate a report on AI-agent orchestration tooling found in the starred-repos
dataset, organized by orchestration *approach*: code-first frameworks, visual /
low-code platforms, coding-agent orchestration, agent OS / long-horizon
harnesses, durable production infra, vertical systems, and protocols.

Inputs:
  public/data/classified.json
  public/data/graph.json

Output:
  reports/agent-orchestration.md   (+ reports/agent-orchestration.meta.json)

Run: python3 scripts/reports/agent_orchestration.py
"""
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLASSIFIED = os.path.join(ROOT, "public/data/classified.json")
GRAPH = os.path.join(ROOT, "public/data/graph.json")
SLUG = "agent-orchestration"
TITLE = "AI Agent Orchestration — Landscape Report"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy (primary axis = orchestration approach) ----------------
APPROACHES = [
    "Code-first agent frameworks",
    "Visual / low-code platforms",
    "Coding-agent orchestration",
    "Agent OS / long-horizon harness",
    "Durable / production infra",
    "Vertical / domain systems",
    "Protocols & meta-frameworks",
]
TAXONOMY = {
    # ===== Code-first agent frameworks (SDKs you write agents in) =====
    "langchain-ai/langgraph": ("Code-first agent frameworks", "Graph-based agent runtime — explicit nodes/edges/state; the de-facto control-flow framework."),
    "microsoft/semantic-kernel": ("Code-first agent frameworks", "Microsoft's enterprise SDK (C#/Python) for plugging LLMs + planning into apps."),
    "openai/openai-agents-python": ("Code-first agent frameworks", "Lightweight, powerful framework for multi-agent workflows; handoffs + guardrails + tracing."),
    "google/adk-python": ("Code-first agent frameworks", "Google's code-first Agent Development Kit — build, evaluate & deploy agents."),
    "agentscope-ai/agentscope": ("Code-first agent frameworks", "Build agents you can see/understand/trust; strong observability + multi-agent."),
    "microsoft/agent-framework": ("Code-first agent frameworks", "Microsoft's framework to build, orchestrate & deploy multi-agent workflows (health 92)."),
    "VoltAgent/voltagent": ("Code-first agent frameworks", "TypeScript agent-engineering platform + open-source framework."),
    "strands-agents/sdk-python": ("Code-first agent frameworks", "Model-driven agents in a few lines; very high health (96) and bus factor 7."),
    "i-am-bee/beeai-framework": ("Code-first agent frameworks", "Production-ready agents in both Python and TypeScript."),
    "liquidos-ai/AutoAgents": ("Code-first agent frameworks", "Rust multi-agent framework to build, deploy & coordinate agents."),

    # ===== Visual / low-code workflow platforms =====
    "n8n-io/n8n": ("Visual / low-code platforms", "Fair-code workflow automation with native AI nodes — the giant (189k★, health 100)."),
    "langgenius/dify": ("Visual / low-code platforms", "Production-ready platform for agentic workflow development (health 100)."),
    "FlowiseAI/Flowise": ("Visual / low-code platforms", "Build AI agents visually; popular drag-and-drop builder."),
    "simstudioai/sim": ("Visual / low-code platforms", "Build, deploy & orchestrate agents — 'central intelligence layer for your AI workforce'."),

    # ===== Coding-agent orchestration (coordinate multiple coding agents) =====
    "bytedance/deer-flow": ("Coding-agent orchestration", "Long-horizon SuperAgent harness that researches, codes & creates with sandboxes (bf6)."),
    "code-yeongyu/oh-my-openagent": ("Coding-agent orchestration", "'omo' — agent harness (formerly oh-my-opencode) for coding workflows."),
    "ruvnet/ruflo": ("Coding-agent orchestration", "Agent-orchestration platform for Claude — multi-agent swarms coordinating autonomous coding."),
    "wshobson/agents": ("Coding-agent orchestration", "Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor, OpenCode, Gemini)."),
    "Yeachan-Heo/oh-my-claudecode": ("Coding-agent orchestration", "Teams-first multi-agent orchestration for Claude Code."),
    "eigent-ai/eigent": ("Coding-agent orchestration", "Open-source cowork desktop — local/free multi-agent productivity workspace."),
    "ComposioHQ/agent-orchestrator": ("Coding-agent orchestration", "Orchestrates parallel coding agents — plans tasks, spawns agents, handles CI autonomously."),
    "getpaseo/paseo": ("Coding-agent orchestration", "Run & coordinate coding agents from phone, desktop and CLI."),
    "vercel-labs/coding-agent-template": ("Coding-agent orchestration", "Multi-agent coding platform on Vercel Sandbox + AI Gateway; declining, verify first."),

    # ===== Agent OS / long-horizon harness =====
    "elizaOS/eliza": ("Agent OS / long-horizon harness", "Open-source 'agentic operating system' — long-running autonomous agents."),

    # ===== Durable / production infra =====
    "flyteorg/flyte": ("Durable / production infra", "Dynamic, resilient orchestration (Go/K8s) — coordinate data, models & compute durably."),
    "inngest/agent-kit": ("Durable / production infra", "Build multi-agent networks in TS with deterministic routing + durable execution via MCP."),

    # ===== Vertical / domain systems =====
    "TauricResearch/TradingAgents": ("Vertical / domain systems", "Multi-agent LLM framework for financial trading — a vertical reference architecture (79k★)."),

    # ===== Protocols & meta-frameworks =====
    "veegee82/agent-workflow-protocol": ("Protocols & meta-frameworks", "Open standard for multi-agent workflows — scripted pipelines to self-organizing teams."),
    "sentient-agi/ROMA": ("Protocols & meta-frameworks", "Recursive meta-agent framework to build multi-agent systems; declining/low health."),
    "TinyAGI/tinyagi": ("Protocols & meta-frameworks", "Agent-teams orchestrator aimed at one-person companies."),
}

# Canonical orchestration tools NOT in this user's stars (honest landscape context).
NOTABLY_ABSENT = [
    ("crewAIInc/crewAI", "the popular role-based multi-agent 'crew' framework"),
    ("microsoft/autogen", "Microsoft's research multi-agent conversation framework"),
    ("langflow-ai/langflow", "popular visual agent/flow builder"),
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

def approach_of(n):
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
  f"`scripts/reports/agent_orchestration.py` (regenerate any time — no API cost).")
A("")
A("> **Orchestration** = coordinating multiple agents / tools / steps toward a goal: "
  "routing, planning, parallelism, hand-offs, state and recovery. The tools below differ "
  "mostly in **how you express that coordination** — in code, on a visual canvas, across "
  "coding agents, or as durable production infra.")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
by_app = {a: [n for n in present if approach_of(n) == a] for a in APPROACHES}

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} agent-orchestration tools** in your stars (**{fmt_int(total_stars)}★**), "
  f"organized by *how you express coordination*:")
for a in APPROACHES:
    m = by_app[a]
    if m:
        A(f"  - **{a}** ({len(m)}): "
          + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(m, key=lambda x: -by_name[x]['stars'])))
A("- **The split that matters:** *code-first frameworks* (langgraph, openai-agents, "
  "semantic-kernel) give you fine control in a programming language; *visual platforms* "
  "(n8n, dify, Flowise) trade control for speed and non-engineer access; *coding-agent "
  "orchestration* (ruflo, agent-orchestrator) is a newer niche that runs **swarms of coding "
  "agents** in parallel.")
A("- **Big-tech has entered:** Microsoft (agent-framework, semantic-kernel), Google "
  "(adk-python), OpenAI (openai-agents-python), AWS (strands-agents) all ship first-party "
  "frameworks — a strong maturity signal.")
A("- **Highest-health picks:** `n8n`/`dify` (100), `strands-agents` (96), "
  "`microsoft/agent-framework` & `semantic-kernel` & `Flowise` (92).")
A("")

# --- Decision framing
A("## Pick by how you want to express coordination")
A("")
A("| You want… | Use this approach | Top picks |")
A("|---|---|---|")
A("| Fine-grained control, in code | Code-first framework | `langgraph`, `openai-agents-python` |")
A("| Fast builds / non-engineers | Visual / low-code | `n8n`, `dify`, `Flowise` |")
A("| Parallel **coding** agents | Coding-agent orchestration | `ruflo`, `ComposioHQ/agent-orchestrator` |")
A("| Always-on autonomous agents | Agent OS / harness | `elizaOS/eliza`, `deer-flow` |")
A("| Durable, fault-tolerant prod | Production infra | `flyte`, `inngest/agent-kit` |")
A("| A standard, not a library | Protocol / meta | `agent-workflow-protocol` |")
A("")

# --- Comparison tables per approach
def comp_table(names, header):
    A(f"### {header}")
    A("")
    A("| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |")
    A("|---|---|---|---|---|---|---|")
    for n in sorted(names, key=lambda x: -by_name[x]["stars"]):
        r = by_name[n]
        A(f"| [{n}]({r['url']}) | {fmt_int(r['stars'])} | {r.get('primary_language') or '—'} | "
          f"{r.get('health_score','—')} | {activity_label(r)} | {r.get('lifecycle_stage','—')} | "
          f"{r.get('bus_factor','—')} |")
    A("")

A("## Comparison by approach")
A("")
for a in APPROACHES:
    if by_app[a]:
        comp_table(by_app[a], a)

# --- Details
A("## Details")
A("")
app_blurb = {
    "Code-first agent frameworks": "SDKs you write agents in — maximum control over routing, "
        "state and hand-offs; the engineer's default.",
    "Visual / low-code platforms": "Drag-and-drop canvases — fastest to a working flow, "
        "accessible to non-engineers, less granular control.",
    "Coding-agent orchestration": "Coordinate *swarms of coding agents* (Claude Code, Codex, "
        "Cursor…) on a codebase — plan, spawn, run in parallel, handle CI.",
    "Agent OS / long-horizon harness": "Runtimes for always-on, long-running autonomous agents.",
    "Durable / production infra": "Fault-tolerant execution — retries, checkpointing, "
        "deterministic routing for production.",
    "Vertical / domain systems": "Reference multi-agent architectures for a specific domain.",
    "Protocols & meta-frameworks": "Standards and meta-layers above any single framework.",
}
for a in APPROACHES:
    names = by_app[a]
    if not names:
        continue
    A(f"### {a}")
    A("")
    A(f"_{app_blurb[a]}_")
    A("")
    for n in sorted(names, key=lambda x: -by_name[x]["stars"]):
        r = by_name[n]
        topics = ", ".join((r.get("topics") or [])[:6]) or "—"
        A(f"- **[{n}]({r['url']})** · {fmt_int(r['stars'])}★ · {r.get('primary_language') or '—'} · "
          f"{r.get('lifecycle_stage','—')} · health {r.get('health_score','—')}  ")
        A(f"  {TAXONOMY[n][1]}  ")
        A(f"  <sub>topics: {topics}</sub>")
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
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities**.")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 2:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in names))
A("")

ranked = sorted(
    [(node_for(n).get("pagerank", 0) if node_for(n) else 0, n) for n in present],
    key=lambda x: -x[0],
)
A("**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' orchestration "
  "tools in your ecosystem:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between orchestration tools** (top similarity edges where both endpoints "
  "are in this report):")
A("")
if inter_edges:
    id_to_name = {v: k for k, v in name_to_nodeid.items()}
    for e in sorted(inter_edges, key=lambda x: -x["weight"])[:15]:
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
A("Bus factor = commit concentration (1 = single-maintainer risk). Orchestration is "
  "load-bearing — weigh this heavily before standardizing on one.")
A("")
A("| Tool | Approach | Health | Lifecycle | Activity | Bus factor |")
A("|---|---|---|---|---|---|")
for n in sorted(present, key=lambda x: -(by_name[x].get("health_score") or 0)):
    r = by_name[n]
    A(f"| {n} | {approach_of(n)} | {r.get('health_score','—')} | {r.get('lifecycle_stage','—')} | "
      f"{activity_label(r)} | {r.get('bus_factor','—')} |")
A("")
risky = [n for n in present
         if (by_name[n].get("health_score") or 100) < 45
         or by_name[n].get("lifecycle_stage") in ("Declining", "Abandoned")]
if risky:
    A("⚠️ **Adopt with caution** (low health and/or declining): "
      + ", ".join(f"`{n}`" for n in sorted(risky, key=lambda x: by_name[x].get('health_score') or 0)) + ".")
    A("")

# --- Notably absent
A("## Notably absent from your stars")
A("")
A("Major orchestration tools **not** in this dataset — worth knowing before treating the "
  "above as complete:")
A("")
for name, what in NOTABLY_ABSENT:
    A(f"- **{name}** — {what}")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external "
  "calls; fully reproducible.")
A("- **Selection**: scan for orchestration / multi-agent / swarm / workflow / agent-framework "
  "signals, then manual curation by approach. RAG frameworks, eval/observability platforms, "
  "and single-purpose agents were routed to their own reports or excluded; only tools whose "
  "*primary* job is coordinating agents/steps appear here.")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may "
  "lag GitHub. Re-run after a fresh `classified.json` to refresh.")
A("")
A(f"<sub>Tools covered: {len(present)} across {sum(1 for a in APPROACHES if by_app[a])} "
  f"approaches · Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta -------------------------------------------------------------
top = sorted(present, key=lambda x: -by_name[x]["stars"])[:5]
card_cats = {
    "Code-first": len(by_app["Code-first agent frameworks"]),
    "Visual": len(by_app["Visual / low-code platforms"]),
    "Coding-agent": len(by_app["Coding-agent orchestration"]),
    "Agent OS": len(by_app["Agent OS / long-horizon harness"]),
    "Infra": len(by_app["Durable / production infra"]),
}
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / Agents",
    "summary": (f"{len(present)} agent-orchestration tools ({fmt_int(total_stars)}★) by "
                "approach: code-first frameworks (langgraph, openai-agents, semantic-kernel), "
                "visual platforms (n8n, dify, Flowise), coding-agent swarms (ruflo), agent OS, "
                "and durable infra (flyte)."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": card_cats,
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/agent_orchestration.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)}  "
      + " | ".join(f"{a.split()[0]}:{len(by_app[a])}" for a in APPROACHES if by_app[a]))
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
