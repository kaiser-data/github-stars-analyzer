#!/usr/bin/env python3
"""
Generate a report on the OpenClaw ecosystem (🦞, formerly Clawdbot/Moltbot) found
in the starred-repos dataset: the core assistant, alternative agents/forks,
hosting/security runtimes, skills & directories, routing, memory, observability,
desktop/orchestration UIs, and specialized agents built on OpenClaw.

Inputs:
  data/classified.json
  public/data/graph.json

Output:
  reports/openclaw-ecosystem.md   (+ reports/openclaw-ecosystem.meta.json)

Run: python3 scripts/reports/openclaw_ecosystem.py
"""
import json
import os
from datetime import datetime, timezone

from lib import fmt_stars, CLASSIFIED, GRAPH, fmt_int, days_to_human, activity_label, make_node_for

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "openclaw-ecosystem"
TITLE = "OpenClaw Ecosystem — What to Use Now"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy --------------------------------------------------------
TAXONOMY = {
    # The core
    "openclaw/openclaw": ("Core", "The OpenClaw assistant itself — your own personal AI, any OS/platform. Everything else extends this."),

    # Alternative agents / forks / agent-OSes
    "zeroclaw-labs/zeroclaw": ("Alternative agent / OS", "Fast, small, fully-autonomous assistant infra (Rust); the healthiest alternative in your stars."),
    "nearai/ironclaw": ("Alternative agent / OS", "Agent-OS focused on privacy, security & extensibility (Rust/WASM, CodeAct)."),
    "RightNow-AI/openfang": ("Alternative agent / OS", "Open-source 'Agent Operating System' (Rust), MCP-native."),
    "HKUDS/nanobot": ("Alternative agent / OS", "Lightweight open-source agent for tools, chats & workflows."),
    "NousResearch/hermes-agent": ("Alternative agent / OS", "'The agent that grows with you' — large, very active alternative."),

    # Hosting / deployment / secure runtimes
    "nanocoai/nanoclaw": ("Hosting / secure runtime", "Lightweight OpenClaw alternative that runs in containers for security; WhatsApp/Telegram/Slack connectors."),
    "cloudflare/moltworker": ("Hosting / secure runtime", "Run OpenClaw on Cloudflare Workers (serverless edge)."),
    "NVIDIA/NemoClaw": ("Hosting / secure runtime", "Run OpenClaw more securely inside NVIDIA OpenShell with managed inference."),

    # Skills / extensions / directories
    "openclaw/clawhub": ("Skills / directory", "The official skill directory for OpenClaw."),
    "hesamsheikh/awesome-openclaw-usecases": ("Skills / directory", "Community collection of OpenClaw use cases (large, but check freshness)."),
    "rohitg00/awesome-openclaw": ("Skills / directory", "Curated awesome-list for the OpenClaw ecosystem."),

    # LLM routing
    "BlockRunAI/ClawRouter": ("Routing", "Agent-native LLM router for OpenClaw — 41+ models, <1ms routing, on-chain payments."),

    # Memory (cross-referenced with the Memory report)
    "supermemoryai/openclaw-supermemory": ("Memory", "Long-term memory & recall packaged specifically for OpenClaw agents."),
    "TencentCloud/TencentDB-Agent-Memory": ("Memory", "Fully-local long-term memory (4-tier pipeline); ships as an OpenClaw plugin."),

    # Observability / evaluation
    "vivekchand/clawmetry": ("Observability", "Real-time observability dashboard — 'see your agent think' (OpenTelemetry)."),
    "comet-ml/opik-openclaw": ("Observability", "Official plugin exporting OpenClaw agent traces (cost/tokens/errors) to Opik."),
    "pinchbench/skill": ("Observability", "Benchmarks LLMs as OpenClaw coding agents on real tasks."),

    # Desktop / UI / orchestration
    "farion1231/cc-switch": ("Desktop / orchestration", "Cross-platform desktop hub for OpenClaw + Claude Code + Codex + Gemini CLI + Hermes."),
    "iOfficeAI/AionUi": ("Desktop / orchestration", "Free local 24/7 cowork app for OpenClaw, Hermes, Claude Code, Codex & more."),
    "CherryHQ/cherry-studio": ("Desktop / orchestration", "AI productivity studio (300+ assistants) with OpenClaw/skills support; highest health here."),
    "abhi1693/openclaw-mission-control": ("Desktop / orchestration", "Agent-orchestration dashboard for OpenClaw (assign tasks, coordinate agents)."),
    "crshdn/mission-control": ("Desktop / orchestration", "Autonomous Product Engine — agents research, build & ship via OpenClaw."),

    # Specialized agents built on / for OpenClaw
    "aiming-lab/AutoResearchClaw": ("Specialized agent", "Autonomous, self-evolving research: chat an idea → get a paper. 🦞"),
    "HKUDS/DeepTutor": ("Specialized agent", "Agent-native personalized tutoring."),
    "HKUDS/ClawWork": ("Specialized agent", "OpenClaw as an AI coworker (coding focus) — but check freshness."),
    "Gen-Verse/OpenClaw-RL": ("Specialized agent", "Train any OpenClaw agent simply by talking (RL/skill-learning)."),
    "SafeRL-Lab/cheetahclaws": ("Specialized agent", "Fast, production-ready Python-native personal assistant inspired by OpenClaw."),
    "hydro13/tandem-browser": ("Specialized agent", "AI-human symbiotic browser with OpenClaw integration."),
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

node_for = make_node_for(nodes_by_id, name_to_nodeid)

# ---- Helpers -----------------------------------------------------------------
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
  f"`scripts/reports/openclaw_ecosystem.py` (regenerate any time — no API cost).")
A("")
A("> **What is OpenClaw?** A personal AI assistant (🦞, formerly *Clawdbot* / *Moltbot*) "
  "that runs on any OS/platform. It has spawned a fast-moving ecosystem of runtimes, "
  "skills, routers, memory layers, dashboards, and specialized agents — this report maps "
  "the parts in your stars and flags what's worth adopting **now**.")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)
order = [
    "Core", "Alternative agent / OS", "Hosting / secure runtime", "Skills / directory",
    "Routing", "Memory", "Observability", "Desktop / orchestration", "Specialized agent",
]

# --- Recommended stack (the "what should I use" answer) -----------------------
def best_in(cat, **filters):
    pool = cats.get(cat, [])
    def ok(n):
        r = by_name[n]
        if filters.get("min_health") and (r.get("health_score") or 0) < filters["min_health"]:
            return False
        if filters.get("fresh") and (r.get("days_since_push") or 999) > 45:
            return False
        return True
    pool = [n for n in pool if ok(n)]
    return sorted(pool, key=lambda n: -(by_name[n].get("health_score") or 0))

A("## Recommended stack (use now)")
A("")
A("Opinionated picks — filtered for **healthy + actively maintained** (high health score, "
  "recent pushes). See the risk table below for what to avoid.")
A("")
A("| Layer | Pick | ★ | Health | Why |")
A("|---|---|---|---|---|")
rec_rows = [
    ("Core assistant", "openclaw/openclaw"),
    ("Secure runtime", "nanocoai/nanoclaw"),
    ("Serverless host", "cloudflare/moltworker"),
    ("Skills directory", "openclaw/clawhub"),
    ("LLM router", "BlockRunAI/ClawRouter"),
    ("Memory", "TencentCloud/TencentDB-Agent-Memory"),
    ("Observability", "vivekchand/clawmetry"),
    ("Desktop hub", "farion1231/cc-switch"),
]
for layer, n in rec_rows:
    r = by_name.get(n)
    if not r:
        continue
    A(f"| {layer} | [{n}]({r['url']}) | {fmt_stars(r)} | "
      f"{r.get('health_score','—')} | {TAXONOMY[n][1]} |")
A("")
A("**One-liner:** keep `openclaw/openclaw` as the core; run it via **nanoclaw** (security) "
  "or **moltworker** (serverless); add **clawhub** skills, **ClawRouter** routing, and "
  "**clawmetry** observability. Want a fresh start? **zeroclaw-labs/zeroclaw** is the "
  "highest-health alternative you've starred.")
A("")

# --- Master comparison
A("## Master comparison")
A("")
A("Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits.")
A("")
A("| Project | Category | Lang | ★ Stars | Lifecycle | Health | "
  "Activity | Last push | Bus factor |")
A("|" + "---|" * 9)
for n in sorted(present, key=lambda x: -by_name[x]["stars"]):
    r = by_name[n]
    A("| [{name}]({url}) | {cat} | {lang} | {stars} | {lc} | {hs} | "
      "{act} | {push} | {bf} |".format(
        name=n, url=r["url"], cat=TAXONOMY[n][0],
        lang=r.get("primary_language") or "—",
        stars=fmt_stars(r),
        lc=r.get("lifecycle_stage") or "—",
        hs=r.get("health_score") if r.get("health_score") is not None else "—",
        act=activity_label(r),
        push=days_to_human(r.get("days_since_push")) + " ago",
        bf=r.get("bus_factor") if r.get("bus_factor") is not None else "—",
    ))
A("")

# --- Category deep dives
A("## By category")
A("")
cat_blurb = {
    "Core": "The assistant everything else plugs into.",
    "Alternative agent / OS": "Standalone agents/agent-OSes you'd pick *instead of* OpenClaw.",
    "Hosting / secure runtime": "Where & how to run it safely — containers, edge, managed GPU.",
    "Skills / directory": "Extend capabilities; find what others have built.",
    "Routing": "Send each request to the right/cheapest model.",
    "Memory": "Long-term recall across sessions (see also the Memory report).",
    "Observability": "See, measure & benchmark what your agent is doing.",
    "Desktop / orchestration": "GUIs and multi-agent control panels.",
    "Specialized agent": "Purpose-built agents on top of OpenClaw (research, tutoring, coding, browser…).",
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
          f"{r.get('lifecycle_stage','—')} · health {r.get('health_score','—')}  ")
        A(f"  {TAXONOMY[n][1]}  ")
        A(f"  <sub>topics: {topics}</sub>")
    A("")

# --- Risk
A("## ⚠️ Adopt with caution")
A("")
A("Low health and/or not pushed recently — verify before wiring into anything you rely on:")
A("")
risky = [n for n in present
         if (by_name[n].get("health_score") or 100) < 50
         or (by_name[n].get("days_since_push") or 0) > 45
         or by_name[n].get("lifecycle_stage") in ("Declining", "Abandoned")]
if risky:
    A("| Project | Health | Lifecycle | Last push | Note |")
    A("|---|---|---|---|---|")
    for n in sorted(risky, key=lambda x: by_name[x].get("health_score") or 0):
        r = by_name[n]
        note = []
        if (r.get("days_since_push") or 0) > 45:
            note.append(f"{r['days_since_push']}d stale")
        if (r.get("health_score") or 100) < 50:
            note.append("low health")
        if r.get("lifecycle_stage") in ("Declining", "Abandoned"):
            note.append(r["lifecycle_stage"].lower())
        A(f"| [{n}]({r['url']}) | {r.get('health_score','—')} | {r.get('lifecycle_stage','—')} | "
          f"{days_to_human(r.get('days_since_push'))} ago | {'; '.join(note)} |")
    A("")
    A("> Note: `openagen/zeroclaw` (1.9k★, 70d stale) is a *different, older* project than "
      "the healthy **`zeroclaw-labs/zeroclaw`** (h93) recommended above — don't confuse them.")
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
A(f"**Community clustering.** These {len(present)} projects span "
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities** — the OpenClaw "
  f"ecosystem is spread across agent-infra rather than forming one isolated cluster.")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 2:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in names))
A("")

ranked = sorted(
    [(node_for(n).get("pagerank", 0) if node_for(n) else 0, n) for n in present],
    key=lambda x: -x[0],
)
A("**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' OpenClaw "
  "projects in your ecosystem:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between OpenClaw projects** (top similarity edges where both endpoints "
  "are in this report):")
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
    A("- _None._ Ecosystem repos connect out to OpenClaw / shared infra rather than to "
      "each other directly.")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `data/classified.json` + `public/data/graph.json`. No external "
  "calls; fully reproducible.")
A("- **Selection**: scan for `openclaw` / `clawd*` / `moltbot` across "
  "name/description/topics/README, then manual curation. Repos that merely *mention* "
  "OpenClaw in passing (general agent harnesses, awesome-lists, unrelated tools) were "
  "excluded; memory/MCP-centric repos are covered in their own reports and only the "
  "OpenClaw-specific ones appear here.")
A("- **Metrics** (health, lifecycle, bus_factor, days_since_push) are precomputed at "
  "snapshot time. **OpenClaw moves extremely fast** — treat all ages/stars as a "
  "May-2026 snapshot and re-verify before adopting.")
A("- Re-run after a fresh `classified.json` to refresh.")
A("")
A(f"<sub>Projects covered: {len(present)} · Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta -------------------------------------------------------------
top = sorted(present, key=lambda x: -by_name[x]["stars"])[:5]
card_cats = {
    "Alternatives": len(cats.get("Alternative agent / OS", [])),
    "Hosting": len(cats.get("Hosting / secure runtime", [])),
    "Skills": len(cats.get("Skills / directory", [])),
    "UIs": len(cats.get("Desktop / orchestration", [])),
    "Specialized": len(cats.get("Specialized agent", [])),
}
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / OpenClaw",
    "summary": (f"{len(present)} OpenClaw (\U0001f99e) ecosystem projects ({fmt_int(total_stars)}★): "
                "the core assistant, alternative agent-OSes, secure runtimes, skills, "
                "routing, memory, observability, UIs & specialized agents — with an "
                "opinionated 'use now' stack and risk flags."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": card_cats,
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/openclaw_ecosystem.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  projects: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
