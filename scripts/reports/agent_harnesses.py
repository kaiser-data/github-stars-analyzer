#!/usr/bin/env python3
"""
Generate a landscape report on agent harnesses in the starred-repos dataset —
the layer that wraps an LLM (or a whole coding agent) in a loop with tools,
state, and guardrails. Organized by *approach*: where each project puts the
harness and what it bets on.

Inputs:
  data/classified.json
  public/data/graph.json

Output:
  reports/agent-harnesses.md   (+ reports/agent-harnesses.meta.json)

Run: python3 scripts/reports/agent_harnesses.py
"""
import json
import os
from datetime import datetime, timezone

from lib import fmt_stars, CLASSIFIED, GRAPH, fmt_int, days_to_human, activity_label, make_node_for

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "agent-harnesses"
TITLE = "Agent Harnesses — Six Approaches to Running Autonomous Agents"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy --------------------------------------------------------
TAXONOMY = {
    # 1. The harness IS the agent — SDKs where the loop is the product
    "earendil-works/pi": ("Harness-as-SDK", "Unified LLM API + agent loop + TUI + coding-agent CLI in one toolkit — the loop as a library."),
    "langchain-ai/deepagents": ("Harness-as-SDK", "The 'batteries-included agent harness' — planning, sub-agents, filesystem, from the LangChain team."),
    "emcie-co/parlant": ("Harness-as-SDK", "Interaction *control* harness — behavioral guidelines enforced at runtime for customer-facing agents."),
    "strands-agents/harness-sdk": ("Harness-as-SDK", "AWS's open SDK to build an agent harness and control it end-to-end in production."),
    "vercel/eve": ("Harness-as-SDK", "Vercel's framework for building agents — harness + sandbox as one integrated runtime."),
    "SafeRL-Lab/cheetahclaws": ("Harness-as-SDK", "Fast, easy agent-harness infrastructure aimed at long-horizon, multi-model runs."),
    "pydantic/pydantic-ai-harness": ("Harness-as-SDK", "'Batteries for your Pydantic AI agent' — the harness as a thin add-on to a typed agent framework."),

    # 2. Meta-harness over existing coding agents
    "obra/superpowers": ("Meta-harness over coding agents", "Skills framework + development methodology layered onto the agent you already run."),
    "affaan-m/ECC": ("Meta-harness over coding agents", "Harness performance optimization: skills, instincts, memory, security, hooks on top of Claude Code."),
    "code-yeongyu/oh-my-openagent": ("Meta-harness over coding agents", "'The one and only agent harness for complex coding' — tokenmaxxer harness wrapping coding agents."),
    "ruvnet/ruflo": ("Meta-harness over coding agents", "The leading agent *meta*-harness — swarms, coordination, and autonomy on top of existing agents."),
    "Yeachan-Heo/oh-my-claudecode": ("Meta-harness over coding agents", "Teams-first multi-agent orchestration living entirely inside Claude Code."),
    "coleam00/Archon": ("Meta-harness over coding agents", "'Harness builder' — make AI coding deterministic and repeatable by generating the harness itself."),

    # 3. Fleet / parallel orchestration
    "multica-ai/multica": ("Fleet / parallel orchestration", "Managed-agents platform: assign tasks to coding agents like teammates and supervise them."),
    "BloopAI/vibe-kanban": ("Fleet / parallel orchestration", "A kanban board as the harness — queue, run, and review many agent tasks in parallel."),
    "gastownhall/gastown": ("Fleet / parallel orchestration", "Multi-agent workspace manager — the 'town' where a fleet of agents live and work."),
    "AndyMik90/Aperant": ("Fleet / parallel orchestration", "Autonomous multi-session AI coding — sessions as the unit of parallelism."),
    "automazeio/ccpm": ("Fleet / parallel orchestration", "GitHub Issues + git worktrees as the coordination fabric for parallel agents."),
    "AgentWrapper/agent-orchestrator": ("Fleet / parallel orchestration", "Plans tasks, spawns parallel coding agents in worktrees, merges autonomously."),
    "dagger/container-use": ("Fleet / parallel orchestration", "Containerized dev environments so multiple agents work safely and independently."),

    # 4. Determinism & spec-driven control
    "github/spec-kit": ("Determinism & spec-driven", "Spec-Driven Development toolkit — the spec, not the prompt, steers the agent."),
    "OthmanAdi/planning-with-files": ("Determinism & spec-driven", "Persistent file-based planning — crash-proof, resumable long-running agent tasks."),
    "agentsmd/agents.md": ("Determinism & spec-driven", "The open AGENTS.md standard — a portable contract telling any harness how to behave in a repo."),
    "gsd-build/gsd-2": ("Determinism & spec-driven", "Meta-prompting + context engineering + spec-driven system for dependable outcomes."),
    "cobusgreyling/loop-engineering": ("Determinism & spec-driven", "Patterns and starters for *loop engineering* — designing the iteration, not just the prompt."),

    # 5. Sandbox substrate
    "daytonaio/daytona": ("Sandbox substrate", "Secure, elastic infrastructure for running AI-generated code — the harness's execution floor."),
    "NVIDIA/NemoClaw": ("Sandbox substrate", "Run harnesses (Hermes, Deep Agents, OpenClaw) inside hardened NVIDIA sandboxes."),
    "trycua/cua": ("Sandbox substrate", "Sandboxes, SDKs, and benchmarks for computer-use agents — full-desktop harnessing."),
    "opensandbox-group/OpenSandbox": ("Sandbox substrate", "Secure, fast, extensible sandbox runtime purpose-built for AI agents."),
    "deeplethe/forkd": ("Sandbox substrate", "fork() for agent microVMs — spawn 100 children in ~100ms; branch a live VM mid-run."),

    # 6. Autonomous long-horizon loops
    "bytedance/deer-flow": ("Autonomous long-horizon", "Long-horizon SuperAgent harness that researches, codes, and creates with sub-agents in sandboxes."),
    "agent0ai/agent-zero": ("Autonomous long-horizon", "General autonomous framework — the agent builds its own tools as it goes."),
    "hexo-ai/sia": ("Autonomous long-horizon", "Self-Improving AI — a harness whose loop optimizes the underlying system over time."),
    "stakpak/agent": ("Autonomous long-horizon", "An agent that lives on your machines 24/7 and keeps shipping — harness as a resident daemon."),
    "aniketkarne/ClaudeNightsWatch": ("Autonomous long-horizon", "Watches your Claude usage windows and executes queued tasks autonomously overnight."),
}

# Approach-comparison rows: (approach, core bet, when it wins)
APPROACHES = [
    ("Harness-as-SDK", "You own the loop in code — tools, state, and control flow are a library you compose.",
     "Building a *product* around an agent; you need custom behavior and testability."),
    ("Meta-harness over coding agents", "Claude Code/Codex already won the inner loop — add skills, memory, and orchestration *around* it.",
     "Developer workflows; you want leverage today without rebuilding tool-use."),
    ("Fleet / parallel orchestration", "Throughput beats IQ — run many agents in worktrees/sandboxes and manage them like a team.",
     "Large backlogs of separable tasks; PR-shaped work."),
    ("Determinism & spec-driven", "Repeatability beats improvisation — specs, plans-on-disk, and standards steer the loop.",
     "Teams that need auditable, resumable, low-variance agent output."),
    ("Sandbox substrate", "The hard problem is *where* agents run — isolation, speed, and forking are the product.",
     "Untrusted/generated code, computer-use, or massively parallel execution."),
    ("Autonomous long-horizon", "Maximize wall-clock autonomy — agents that plan, persist, and keep going for hours or days.",
     "Research, background maintenance, overnight queues; outcome > oversight."),
]

# Adjacent but deliberately excluded (kept honest in the report)
ADJACENT = [
    ("langchain-ai/langgraph", "agent *framework* (graphs, not harnesses) — see the agent-orchestration report"),
    ("crewAIInc/crewAI", "role-playing agent framework — agent-orchestration report"),
    ("microsoft/autogen", "multi-agent conversation framework — agent-orchestration report"),
    ("eigent-ai/eigent", "cowork desktop product — agent-orchestration report"),
    ("getpaseo/paseo", "desktop/mobile agent orchestrator — agent-orchestration report"),
    ("wshobson/agents", "multi-harness plugin *marketplace* — content for harnesses, not a harness"),
    ("EleutherAI/lm-evaluation-harness", "'harness' for *model benchmarks*, not agent runtimes — see the LLM-evaluation report"),
    ("anthropics/claude-code", "the coding agent itself — the thing meta-harnesses wrap"),
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

node_for = make_node_for(nodes_by_id, name_to_nodeid)

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
  f"`scripts/reports/agent_harnesses.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)
order = ["Harness-as-SDK", "Meta-harness over coding agents",
         "Fleet / parallel orchestration", "Determinism & spec-driven",
         "Sandbox substrate", "Autonomous long-horizon"]

# --- Executive summary
A("## Executive summary")
A("")
A(f"- A **harness** is everything around the model: the loop, tools, state, "
  f"guardrails, and execution environment. **{len(present)} harness projects** in "
  f"your stars (**{fmt_int(total_stars)}★** combined) cluster into **six distinct "
  f"approaches** — they disagree about *where the harness lives* and *what the "
  f"hard problem is*:")
for c in order:
    if cats.get(c):
        A(f"  - **{c}** ({len(cats[c])}): "
          + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(cats[c], key=lambda x: -by_name[x]['stars'])))
A("- The fault line: **build the loop** (Harness-as-SDK) vs **wrap an existing agent** "
  "(meta-harness) vs **multiply agents** (fleet) — with determinism, sandboxing, and "
  "long-horizon autonomy as orthogonal bets any of them can adopt.")
A("- Star mass sits with the meta-harnesses (`superpowers`, `ECC`, `ruflo`) — the "
  "ecosystem is betting that the inner loop is a solved commodity and the value is in "
  "the layer above it.")
A("")

# --- Approaches compared
A("## The six approaches, compared")
A("")
A("| Approach | Core bet | When it wins |")
A("|---|---|---|")
for name, bet, wins in APPROACHES:
    A(f"| **{name}** | {bet} | {wins} |")
A("")

# --- Master comparison
A("## Master comparison")
A("")
A("Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits.")
A("")
A("| Tool | Approach | Lang | License | ★ Stars | Lifecycle | Health | "
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
A("## By approach")
A("")
cat_blurb = {
    "Harness-as-SDK": "The loop as a library: you import the harness, register tools, and "
        "own control flow. Maximum flexibility, maximum responsibility — you maintain "
        "planning, retries, memory, and safety yourself.",
    "Meta-harness over coding agents": "These projects treat Claude Code / Codex as the "
        "engine and build the transmission: skills, personas, memory, token discipline, "
        "and multi-agent coordination injected via configs, hooks, and subagents.",
    "Fleet / parallel orchestration": "One agent is a tool; a fleet is a team. The harness "
        "problem becomes scheduling, isolation (worktrees, containers), review queues, "
        "and merge discipline.",
    "Determinism & spec-driven": "The counter-culture: agents drift, so pin them down. "
        "Specs, standards files, and plans persisted to disk make runs reproducible, "
        "auditable, and resumable after crashes.",
    "Sandbox substrate": "Infrastructure-first: before you scale agents you need somewhere "
        "safe and fast to run them. MicroVMs, container runtimes, and hardened sandboxes "
        "are the harness's floor.",
    "Autonomous long-horizon": "Maximum autonomy: agents that run for hours or days, "
        "planning and re-planning, sometimes improving their own scaffolding. The harness "
        "is a resident process, not a CLI invocation.",
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
A(f"**Centrality (PageRank in the full {fmt_int(len(gr['nodes']))}-repo graph)** — most "
  "'hub-like' harnesses in your ecosystem:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between harness projects** (top similarity edges where both endpoints "
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
    A("- _None._")
A("")

# --- Maintenance / risk
A("## Maintenance & risk signal")
A("")
A("Bus factor = commit concentration (1 = single-maintainer risk). Harnesses are a "
  "young, fast-moving category — expect churn; check lifecycle before betting on one.")
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

# --- Selection guidance
A("## Which one should you use?")
A("")
A("| If you want… | Start with | Why |")
A("|---|---|---|")
guide = [
    ("A harness you fully own, in code", "`langchain-ai/deepagents` or `earendil-works/pi`",
     "Batteries-included loops with planning and sub-agents; pi adds a unified LLM API + TUI."),
    ("More out of the Claude Code you already run", "`obra/superpowers` (+ `affaan-m/ECC`)",
     "Skills + methodology layered on today; ECC adds memory, instincts, and hooks."),
    ("Swarms / heavy multi-agent coordination", "`ruvnet/ruflo`",
     "The meta-harness with the deepest swarm tooling in your stars."),
    ("A team of agents working a backlog", "`BloopAI/vibe-kanban`",
     "Kanban-shaped orchestration over Claude Code/Codex; `ccpm` if you prefer GitHub Issues + worktrees."),
    ("Reproducible, auditable agent output", "`github/spec-kit` + `agentsmd/agents.md`",
     "Spec-driven development plus the portable AGENTS.md behavior contract."),
    ("Crash-proof long tasks", "`OthmanAdi/planning-with-files`",
     "Plans persisted to disk — resume after any failure."),
    ("Safe execution for untrusted agent code", "`daytonaio/daytona`",
     "Purpose-built elastic sandbox infra; `forkd` when you need 100 microVMs in 100ms."),
    ("A 24/7 resident agent", "`stakpak/agent` (or `aniketkarne/ClaudeNightsWatch`)",
     "Daemon-style autonomy; NightsWatch exploits idle Claude usage windows overnight."),
    ("Research-grade long-horizon autonomy", "`bytedance/deer-flow`",
     "SuperAgent harness with sub-agents and sandboxes; strongest end-to-end autonomy here."),
]
for want, pick, why in guide:
    A(f"| {want} | {pick} | {why} |")
A("")

# --- Adjacent
A("## Adjacent (deliberately not listed as harnesses)")
A("")
for name, why in ADJACENT:
    r = by_name.get(name)
    star = f" ({fmt_int(r['stars'])}★)" if r else ""
    A(f"- **{name}**{star} — {why}")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `data/classified.json` + `public/data/graph.json`. No external "
  "calls; fully reproducible.")
A("- **Selection**: keyword scan (harness / autonomous / swarm / multi-agent / sandbox / "
  "worktree / spec-driven / long-horizon / loop…) + manual curation by *approach*. "
  "General agent frameworks and orchestration platforms live in the agent-orchestration "
  "report; Claude-Code configuration setups in the claude-code-setups report. A few "
  "boundary projects (`deer-flow`, `ruflo`, `oh-my-*`) appear in both, viewed through "
  "different lenses.")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may "
  "lag GitHub's current state.")
A("- Re-run after a fresh `classified.json` to refresh stars/activity.")
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
    "category": "AI / Agents",
    "summary": (f"{len(present)} harness projects ({fmt_int(total_stars)}★) across six "
                "approaches: harness-as-SDK, meta-harnesses over coding agents, fleet "
                "orchestration, spec-driven determinism, sandbox substrates, and "
                "long-horizon autonomy."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in order},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/agent_harnesses.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
