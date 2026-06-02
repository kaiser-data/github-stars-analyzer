#!/usr/bin/env python3
"""
Generate a comprehensive report on MCP (Model Context Protocol) tooling found in
the starred-repos dataset: SDKs/frameworks for building servers, clients/hosts,
gateways/registries/control-planes, and the ecosystem of domain MCP servers
(browser, database, dev-tools, code-intelligence, docs/research, etc.).

Inputs:
  public/data/classified.json
  public/data/graph.json

Output:
  reports/mcp-tooling.md   (+ reports/mcp-tooling.meta.json)

Run: python3 scripts/reports/mcp_tooling.py
"""
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLASSIFIED = os.path.join(ROOT, "public/data/classified.json")
GRAPH = os.path.join(ROOT, "public/data/graph.json")
SLUG = "mcp-tooling"
TITLE = "MCP (Model Context Protocol) Tooling — Landscape Report"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy --------------------------------------------------------
TAXONOMY = {
    # SDKs / frameworks for building MCP servers & clients
    "PrefectHQ/fastmcp": ("SDK / framework", "The fast, Pythonic way to build MCP servers & clients; the de-facto Python framework."),
    "mcp-use/mcp-use": ("SDK / framework", "Fullstack MCP framework — build MCP apps for ChatGPT/Claude and MCP servers for agents."),
    "tadata-org/fastapi_mcp": ("SDK / framework", "Expose existing FastAPI endpoints as MCP tools, with auth — zero-rewrite server creation."),

    # Clients / hosts (consume MCP servers)
    "ravitemer/mcphub.nvim": ("Client / host", "MCP client for Neovim — integrates MCP servers into the editing workflow."),
    "Kochava-Studios/witsy": ("Client / host", "Desktop AI assistant doubling as a universal MCP client."),

    # Gateways / registries / control planes
    "Klavis-AI/klavis": ("Gateway / control plane", "MCP integration platform so agents use tools reliably at scale."),
    "aipotheosis-labs/gate22": ("Gateway / control plane", "Open-source MCP gateway & control plane to govern which tools agents may use."),
    "googleapis/mcp-toolbox": ("Gateway / control plane", "Google's open MCP server for databases — one gateway fronting many DBs."),

    # Browser / web automation servers
    "microsoft/playwright-mcp": ("Server · browser/web", "Microsoft's Playwright MCP server — drive a real browser from an agent."),
    "browserbase/mcp-server-browserbase": ("Server · browser/web", "Let LLMs control a cloud browser via Browserbase + Stagehand."),
    "hangwin/mcp-chrome": ("Server · browser/web", "Chrome-extension-based MCP server exposing the user's actual browser."),
    "brightdata/brightdata-mcp": ("Server · browser/web", "All-in-one MCP server for public web data access / scraping at scale."),

    # Database / data servers
    "bytebase/dbhub": ("Server · database/data", "Zero-dependency, token-efficient database MCP server (Postgres, MySQL, SQL Server, …)."),
    "neo4j/mcp": ("Server · database/data", "Neo4j's official MCP server for graph-database access."),
    "reading-plus-ai/mcp-server-data-exploration": ("Server · database/data", "MCP server for interactive data exploration."),

    # Dev-tooling / quality / observability servers
    "github/github-mcp-server": ("Server · dev-tooling", "GitHub's official MCP server — issues, PRs, repos as agent tools."),
    "getsentry/sentry-mcp": ("Server · dev-tooling", "Interact with Sentry (errors/issues) via LLMs."),
    "SonarSource/sonarqube-mcp-server": ("Server · dev-tooling", "Official SonarQube MCP server — code quality & security in agents."),
    "czlonkowski/n8n-mcp": ("Server · dev-tooling", "MCP server that helps agents build n8n workflows."),
    "storybookjs/mcp": ("Server · dev-tooling", "Storybook's MCP server for component-driven workflows."),

    # Code-intelligence / context servers
    "oraios/serena": ("Server · code intelligence", "Powerful MCP coding toolkit — semantic retrieval & editing (LSP-backed)."),
    "upstash/context7": ("Server · code intelligence", "Up-to-date library docs piped to LLMs/editors via MCP — kills version drift."),
    "mksglu/context-mode": ("Server · code intelligence", "Context-window optimization for coding agents; sandboxes tool output (~98% reduction)."),
    "yvgude/lean-ctx": ("Server · code intelligence", "Cognitive context layer — 51+ MCP tools, multiple read modes for agentic systems."),
    "shaneholloman/mcp-knowledge-graph": ("Server · code intelligence", "Persistent memory for Claude via a local knowledge graph (also in the memory report)."),

    # ===== Official protocol repos (SDKs / reference servers / tooling) =====
    "modelcontextprotocol/servers": ("SDK / framework", "Official reference-server monorepo — canonical examples for filesystem, git, fetch, etc."),
    "modelcontextprotocol/typescript-sdk": ("SDK / framework", "Official TypeScript SDK for building MCP servers & clients."),
    "modelcontextprotocol/inspector": ("Client / host", "Official visual debugger/inspector for testing MCP servers."),

    # Docs / research / knowledge servers
    "blazickjp/arxiv-mcp-server": ("Server · docs/research", "Search & analyze arXiv papers through MCP."),
    "VectifyAI/pageindex-mcp": ("Server · docs/research", "MCP front-end to PageIndex's vectorless reasoning-based RAG."),
    "hustcc/mcp-mermaid": ("Server · docs/research", "Generate Mermaid diagrams/charts dynamically via MCP."),

    # Game-engine / platform servers
    "Coding-Solo/godot-mcp": ("Server · game/platform", "MCP server to drive the Godot game engine (launch editor, run scenes)."),
    "CoderGamester/mcp-unity": ("Server · game/platform", "MCP plugin connecting agents (Cursor/Claude) to the Unity editor."),
    "mobile-next/mobile-mcp": ("Server · game/platform", "MCP server for mobile automation/scraping (iOS, Android, emulators)."),

    # Learning / reference (curated lists & curricula)
    "punkpeye/awesome-mcp-servers": ("Learning / reference", "The flagship awesome-list of MCP servers (88k★)."),
    "wong2/awesome-mcp-servers": ("Learning / reference", "Curated list of MCP servers."),
    "microsoft/mcp-for-beginners": ("Learning / reference", "Microsoft's open curriculum teaching MCP fundamentals."),
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
  f"`scripts/reports/mcp_tooling.py` (regenerate any time — no API cost).")
A("")
A("> **What is MCP?** The Model Context Protocol is an open standard (Anthropic, late "
  "2024) that lets LLM apps talk to external tools/data through a uniform interface — "
  "the 'USB-C port' for AI. **Servers** expose capabilities; **clients/hosts** (Claude "
  "Desktop, Cursor, editors) consume them; **gateways** govern them at scale.")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)
order = [
    "SDK / framework", "Client / host", "Gateway / control plane",
    "Server · browser/web", "Server · database/data", "Server · dev-tooling",
    "Server · code intelligence", "Server · docs/research", "Server · game/platform",
    "Learning / reference",
]
server_cats = [c for c in order if c.startswith("Server ·")]
n_servers = sum(len(cats.get(c, [])) for c in server_cats)

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} MCP projects** in your stars (**{fmt_int(total_stars)}★** combined) — "
  f"spanning the whole stack: SDKs, clients, gateways, and **{n_servers} domain servers**.")
A(f"- The architecture has three roles — and your stars cover all of them:")
A(f"  - **Build** (SDKs/frameworks): "
  + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(cats.get('SDK / framework', []), key=lambda x: -by_name[x]['stars'])))
A(f"  - **Consume** (clients/hosts): "
  + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(cats.get('Client / host', []), key=lambda x: -by_name[x]['stars'])))
A(f"  - **Govern** (gateways/control planes): "
  + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(cats.get('Gateway / control plane', []), key=lambda x: -by_name[x]['stars'])))
A(f"- **Official vendor servers dominate the top** — GitHub, Microsoft (Playwright), "
  f"Google (mcp-toolbox), Neo4j, Sentry, SonarSource all ship first-party MCP servers, a "
  f"strong signal the protocol has crossed into mainstream adoption.")
A(f"- TypeScript is the lingua franca of MCP servers; Python leads the SDK/framework layer "
  f"(fastmcp, fastapi_mcp).")
A("")

# --- Roles table
A("## The MCP stack at a glance")
A("")
A("| Role | What it does | Tools in your stars |")
A("|---|---|---|")
A("| **SDK / framework** | Build servers/clients | `fastmcp`, `mcp-use`, `fastapi_mcp` |")
A("| **Client / host** | Apps that consume servers | `mcphub.nvim`, `witsy` |")
A("| **Gateway / control plane** | Route, secure & govern servers | `klavis`, `gate22`, `mcp-toolbox` |")
A("| **Servers** | Expose a capability to agents | "
  + str(n_servers) + " across browser, DB, dev-tools, code-intel, docs, game engines |")
A("| **Learning** | Lists & curricula | `awesome-mcp-servers` (×2), `mcp-for-beginners` |")
A("")

# --- Master comparison
A("## Master comparison")
A("")
A("Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits.")
A("")
A("| Project | Category | Lang | License | ★ Stars | Lifecycle | Health | "
  "Activity | Last push | Age | Contrib(90d) |")
A("|" + "---|" * 12)
for n in sorted(present, key=lambda x: -by_name[x]["stars"]):
    r = by_name[n]
    A("| [{name}]({url}) | {cat} | {lang} | {lic} | {stars} | {lc} | {hs} | "
      "{act} | {push} | {age} | {auth} |".format(
        name=n, url=r["url"], cat=TAXONOMY[n][0],
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
cat_blurb = {
    "SDK / framework": "The layer you reach for to *author* an MCP server or client.",
    "Client / host": "Apps/editors that connect to servers and surface their tools to the user.",
    "Gateway / control plane": "Front many servers behind one endpoint; add auth, routing, and "
        "policy — the enterprise-readiness layer.",
    "Server · browser/web": "Give agents a browser or the open web.",
    "Server · database/data": "Expose databases and datasets as agent-queryable tools.",
    "Server · dev-tooling": "Wire agents into the software-delivery toolchain (VCS, CI, quality, errors).",
    "Server · code intelligence": "Feed agents accurate code/library context — the antidote to hallucinated APIs.",
    "Server · docs/research": "Documents, papers, and diagram generation.",
    "Server · game/platform": "Drive game engines and mobile/desktop platforms.",
    "Learning / reference": "Where the ecosystem is catalogued and taught.",
}
for cat in order:
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

# --- Official vs community
A("## Spotlight: official vendor servers")
A("")
A("A maturity signal — major vendors shipping **first-party** MCP servers in your stars:")
A("")
official = {
    "github/github-mcp-server": "GitHub", "microsoft/playwright-mcp": "Microsoft",
    "googleapis/mcp-toolbox": "Google", "neo4j/mcp": "Neo4j",
    "getsentry/sentry-mcp": "Sentry", "SonarSource/sonarqube-mcp-server": "SonarSource",
    "storybookjs/mcp": "Storybook", "upstash/context7": "Upstash",
    "microsoft/mcp-for-beginners": "Microsoft (edu)",
}
for n, vendor in sorted(official.items(), key=lambda kv: -(by_name.get(kv[0], {}).get("stars", 0))):
    r = by_name.get(n)
    if r:
        A(f"- **{vendor}** — [{n}]({r['url']}) · {fmt_int(r['stars'])}★ · health {r.get('health_score','—')}")
A("")

# --- Graph analysis
A("## Graph analysis — how they relate")
A("")
comm = {}
for n in present:
    nd = node_for(n)
    if nd is not None:
        comm.setdefault(nd.get("community"), []).append(n)
A(f"**Community clustering.** These {len(present)} projects span "
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities** — MCP tooling is "
  f"woven through the whole agent-infra landscape rather than sitting in one bucket.")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 2:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in names))
A("")

ranked = sorted(
    [(node_for(n).get("pagerank", 0) if node_for(n) else 0, n) for n in present],
    key=lambda x: -x[0],
)
A("**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' MCP projects "
  "in your ecosystem:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between MCP projects** (top similarity edges where both endpoints are "
  "in this report):")
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
A("Bus factor = commit concentration (1 = single-maintainer risk). MCP servers are often "
  "weekend projects — check this before wiring one into production agents.")
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
# Flag risky ones
risky = [n for n in present
         if (by_name[n].get("health_score") or 100) < 45
         or by_name[n].get("lifecycle_stage") in ("Declining", "Abandoned")]
if risky:
    A("⚠️ **Adopt with caution** (low health and/or declining): "
      + ", ".join(f"`{n}`" for n in sorted(risky, key=lambda x: by_name[x].get('health_score') or 0)) + ".")
    A("")

# --- Selection guidance
A("## Which one should you use?")
A("")
A("| If you want… | Start with | Why |")
A("|---|---|---|")
guide = [
    ("To build an MCP server in Python", "`PrefectHQ/fastmcp`",
     "The standard Pythonic framework; health 84, very active."),
    ("To expose an existing FastAPI app as MCP", "`tadata-org/fastapi_mcp`",
     "No rewrite — but note declining health (25); verify before relying on it."),
    ("A fullstack/TS way to build MCP apps", "`mcp-use/mcp-use`",
     "Build both servers and ChatGPT/Claude MCP apps."),
    ("To give an agent a real browser", "`microsoft/playwright-mcp`",
     "First-party Microsoft server; most-starred browser MCP here."),
    ("Database access for agents", "`googleapis/mcp-toolbox` or `bytebase/dbhub`",
     "Google's multi-DB gateway (health 92) or a zero-dep single server."),
    ("GitHub as agent tools", "`github/github-mcp-server`",
     "Official, Go, health 88 — issues/PRs/repos out of the box."),
    ("Accurate, current library docs in your editor", "`upstash/context7`",
     "56k★; pipes up-to-date docs to LLMs, killing version drift."),
    ("Semantic code editing for a coding agent", "`oraios/serena`",
     "LSP-backed semantic retrieval & editing toolkit; health 84."),
    ("To govern which tools agents can use", "`aipotheosis-labs/gate22` or `Klavis-AI/klavis`",
     "Gateway/control-plane layer for policy & scale."),
]
for want, pick, why in guide:
    A(f"| {want} | {pick} | {why} |")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external "
  "calls; fully reproducible.")
A("- **Selection**: word-boundary scan for `mcp` / 'model context protocol' across "
  "name/description/topics/README, then manual curation into roles + server domains. "
  "Many repos *mention* MCP support (agents, IDEs, gateways like litellm/Portkey) but "
  "aren't MCP-specific tools — those were excluded to keep the list about MCP itself.")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may "
  "lag GitHub's current state. MCP moves *very* fast — treat ages/stars as a May-2026 "
  "snapshot.")
A("- Re-run after a fresh `classified.json` to refresh.")
A("")
A(f"<sub>Projects covered: {len(present)} ({n_servers} servers) · Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta -------------------------------------------------------------
top = sorted(present, key=lambda x: -by_name[x]["stars"])[:5]
# Compact category counts for the card (group all servers).
card_cats = {
    "SDK/framework": len(cats.get("SDK / framework", [])),
    "Client/host": len(cats.get("Client / host", [])),
    "Gateway": len(cats.get("Gateway / control plane", [])),
    "Servers": n_servers,
    "Learning": len(cats.get("Learning / reference", [])),
}
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / MCP",
    "summary": (f"{len(present)} MCP projects ({fmt_int(total_stars)}★): SDKs/frameworks, "
                f"clients, gateways, and {n_servers} domain servers (browser, DB, dev-tools, "
                "code-intel, docs, game engines) — incl. official GitHub/Microsoft/Google servers."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": card_cats,
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/mcp_tooling.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  projects: {len(present)} / {len(sel_names)} curated  (servers: {n_servers})")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
