#!/usr/bin/env python3
"""
Generate a report on Claude Code "superpower" tooling found in the starred-repos
dataset, organized into the layers of an agentic-coding setup — harnesses,
skills, memory/context, token-savers, code-graph/retrieval, MCP, observability,
config/setup kits, and local runtimes — then maps them into ready-to-run setup
strategies (token-saver / balanced / max-performance).

Inputs:
  data/classified.json
  public/data/graph.json

Output:
  reports/claude-code-setups.md   (+ reports/claude-code-setups.meta.json)

Run: python3 scripts/reports/claude_code_setups.py
"""
import json
import os
from datetime import datetime, timezone

from lib import fmt_stars, CLASSIFIED, GRAPH, fmt_int, days_to_human, activity_label, make_node_for

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "claude-code-setups"
TITLE = "Claude Code Superpowers — Setup Strategies from Your Stars"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy --------------------------------------------------------
# A modern Claude-Code setup is layered: a harness/agent runs the loop; skills &
# config shape behavior on demand; memory persists context across sessions;
# token-savers compress what the model sees; code-graph/retrieval feed it the
# right code; MCP adds external reach; observability measures it; local runtimes
# cut cost. Each repo below owns one layer.
TAXONOMY = {
    # Harnesses / coding agents — the loop itself
    "anthropics/claude-code": ("Harness / coding agent", "Claude Code itself — the agentic CLI that lives in your terminal; the baseline every setup here extends."),
    "openclaw/openclaw": ("Harness / coding agent", "Cross-platform personal-assistant harness — an 'any OS, any platform' agent runtime."),
    "anomalyco/opencode": ("Harness / coding agent", "Open-source terminal coding agent — a provider-agnostic alternative harness."),
    "openai/codex": ("Harness / coding agent", "OpenAI's lightweight terminal coding agent — useful as a second harness to diff behavior against Claude Code."),
    "google-gemini/gemini-cli": ("Harness / coding agent", "Gemini's open-source terminal agent — the third major CLI harness; handy for model-shopping."),
    "cline/cline": ("Harness / coding agent", "Autonomous coding agent as SDK / IDE extension / CLI — strong for in-editor agentic workflows."),
    "aaif-goose/goose": ("Harness / coding agent", "Extensible open agent that installs and runs tools, not just suggestions — MCP-native."),
    "NousResearch/hermes-agent": ("Harness / coding agent", "Long-lived 'agent that grows with you' harness — persistent, personalized agent loop."),
    "earendil-works/pi": ("Harness / coding agent", "Unified LLM-API + agent-loop + TUI toolkit — a kit for rolling your own coding agent."),
    "bytedance/deer-flow": ("Harness / coding agent", "Long-horizon SuperAgent harness that researches, codes, and writes — multi-step autonomy."),
    "ruvnet/ruflo": ("Harness / coding agent", "Agent meta-harness for Claude — deploys multi-agent swarms with coordination."),
    "Yeachan-Heo/oh-my-claudecode": ("Harness / coding agent", "Teams-first multi-agent orchestration layer for Claude Code."),

    # Skills frameworks — on-demand expertise (the modern superpower)
    "obra/superpowers": ("Skills framework", "Agentic skills framework + dev methodology — the headline 'give your agent superpowers' skill collection."),
    "anthropics/skills": ("Skills framework", "Anthropic's official Agent Skills repo — canonical examples of the skills format."),
    "affaan-m/ECC": ("Skills framework", "Agent-harness performance system bundling skills, instincts, and memory into one optimization layer."),
    "ComposioHQ/awesome-claude-skills": ("Skills framework", "Curated index of Claude Skills + tooling — the discovery hub for what's worth installing."),
    "wshobson/agents": ("Skills framework", "Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor) — subagents & commands."),
    "K-Dense-AI/scientific-agent-skills": ("Skills framework", "Domain skill pack that turns an agent into a research scientist — example of vertical skills."),

    # Config / setup kits — shape behavior up front
    "multica-ai/andrej-karpathy-skills": ("Config / setup kit", "A single CLAUDE.md derived from Karpathy's habits — the 'one good config file' approach."),
    "garrytan/gstack": ("Config / setup kit", "Garry Tan's exact Claude Code setup — 23 opinionated tools as a turnkey starting point."),
    "centminmod/my-claude-code-setup": ("Config / setup kit", "A shared starter CLAUDE.md + memory-bank configuration template you can fork."),
    "davila7/claude-code-templates": ("Config / setup kit", "CLI to configure AND monitor Claude Code — installs commands/agents/hooks and watches usage."),
    "farion1231/cc-switch": ("Config / setup kit", "Desktop all-in-one for managing Claude Code/Codex/OpenClaw — swap providers & configs fast."),
    "luongnv89/claude-howto": ("Config / setup kit", "Visual, example-driven guide to Claude Code from basics to advanced — the learning path."),
    "shanraisshan/claude-code-best-practice": ("Config / setup kit", "Best-practices collection: vibe-coding → agentic engineering."),
    "hesreallyhim/awesome-claude-code": ("Config / setup kit", "The awesome-list for Claude Code skills, hooks, slash-commands, and orchestrators."),
    "Piebald-AI/claude-code-system-prompts": ("Config / setup kit", "Claude Code's full system prompt + 27 builtin tool descriptions — know what you're configuring."),
    "x1xhlol/system-prompts-and-models-of-ai-tools": ("Config / setup kit", "Leaked/collected system prompts of major AI coding tools — prompt-engineering reference."),
    "anthropics/claude-cookbooks": ("Config / setup kit", "Official recipes/notebooks for effective Claude usage patterns."),

    # Memory / persistent context
    "thedotmack/claude-mem": ("Memory / context", "Persistent context across sessions for every agent — captures work and re-injects it (you run this)."),
    "mem0ai/mem0": ("Memory / context", "Universal memory layer for AI agents — the most-adopted general memory backend."),
    "MemPalace/mempalace": ("Memory / context", "Best-benchmarked open-source AI memory system — drop-in long-term memory."),
    "memvid/memvid": ("Memory / context", "Memory layer that replaces RAG pipelines with a compact server — novel storage approach."),
    "campfirein/byterover-cli": ("Memory / context", "Portable memory layer (brv) for autonomous coding agents — agent-agnostic."),
    "Gentleman-Programming/engram": ("Memory / context", "Agent-agnostic Go binary giving coding agents persistent memory."),
    "memodb-io/Acontext": ("Memory / context", "Treats Agent Skills as a memory layer — skills-as-memory hybrid."),

    # Token-savers / context compression
    "JuliusBrussee/caveman": ("Token-saver / compression", "'Why use many token when few token do trick' — a Claude Code skill that aggressively trims tokens."),
    "rtk-ai/rtk": ("Token-saver / compression", "CLI proxy that cuts LLM token consumption 60–90% on common dev commands — sits in front of the agent."),
    "code-yeongyu/oh-my-openagent": ("Token-saver / compression", "omo/lazycodex — a coding agent built for 'tokenmaxxers'; efficiency-first harness."),
    "toon-format/toon": ("Token-saver / compression", "Token-Oriented Object Notation — compact schema-aware encoding to shrink structured payloads."),
    "headroomlabs-ai/headroom": ("Token-saver / compression", "Compresses tool outputs, logs, files, and RAG chunks before they hit the model's context."),
    "getagentseal/codeburn": ("Token-saver / compression", "TUI dashboard showing where your AI coding tokens go — measure before you optimize."),
    "MinishLab/semble": ("Token-saver / compression", "Fast, accurate code search for agents using ~98% fewer tokens than reading files."),

    # Code-graph / retrieval — feed the right code
    "Graphify-Labs/graphify": ("Code-graph / retrieval", "Coding-assistant skill that turns a repo into a knowledge graph (you use this on this project)."),
    "colbymchenry/codegraph": ("Code-graph / retrieval", "Pre-indexed code knowledge graph for Claude Code/Codex/Cursor — structural retrieval."),
    "abhigyanpatwari/GitNexus": ("Code-graph / retrieval", "Zero-server code-intelligence engine — client-side code graph."),
    "Egonex-AI/Understand-Anything": ("Code-graph / retrieval", "Turns any code into an interactive teaching graph — comprehension over impression."),
    "DeusData/codebase-memory-mcp": ("Code-graph / retrieval", "High-performance code-intelligence MCP server — indexes codebases for retrieval."),

    # MCP — external reach
    "modelcontextprotocol/servers": ("MCP ecosystem", "The official reference MCP servers — the canonical catalog of capabilities to plug in."),
    "punkpeye/awesome-mcp-servers": ("MCP ecosystem", "The big community index of MCP servers — discovery for what to connect."),
    "upstash/context7": ("MCP ecosystem", "Up-to-date library docs for LLMs via MCP — kills 'hallucinated API' errors (you have this wired)."),

    # Observability / evals — measure the agent
    "langfuse/langfuse": ("Observability / evals", "Open-source LLM engineering platform: traces, evals, metrics, prompts (you trace Claude Code into this)."),
    "comet-ml/opik": ("Observability / evals", "Debug/evaluate/monitor LLM apps, RAG, and agents — eval-first observability."),
    "Arize-ai/phoenix": ("Observability / evals", "AI observability & evaluation — OpenTelemetry-based tracing for agents."),
    "traceloop/openllmetry": ("Observability / evals", "Open-source OpenTelemetry-based observability for LLM apps — standards-based traces."),
    "patoles/agent-flow": ("Observability / evals", "Real-time visualization of Claude Code agent orchestration — watch agents think, branch, coordinate."),
    "ingo-eichhorst/Irrlicht": ("Observability / evals", "Claude Code session lights in the macOS menu bar — at-a-glance session state."),

    # Local runtimes — cut cost / go offline
    "ollama/ollama": ("Local runtime", "Run open models locally with one command — point an agent at it to slash API cost or go offline."),
    "BerriAI/litellm": ("Local runtime", "OpenAI-compatible proxy/gateway to 100+ LLMs — swap models under any harness from one endpoint."),
}

# Adjacent but deliberately excluded (kept honest in the report)
ADJACENT = [
    ("n8n-io/n8n", "workflow-automation platform — orchestrates agents but isn't a Claude-Code setup layer"),
    ("langgenius/dify", "agentic-workflow platform — covered by the agent-orchestration report"),
    ("langchain-ai/langchain", "agent-engineering library — app framework, not a CC setup tool"),
    ("open-webui/open-webui", "chat UI for local models — a frontend, not an agent setup"),
    ("ultraworkers/claw-code", "art/exhibit harness — not a practical setup layer"),
    ("multica-ai/multica", "managed-agents platform — team product, see agent-orchestration report"),
]

# Layer order for the narrative
ORDER = [
    "Harness / coding agent", "Skills framework", "Config / setup kit",
    "Memory / context", "Token-saver / compression", "Code-graph / retrieval",
    "MCP ecosystem", "Observability / evals", "Local runtime",
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
  f"`scripts/reports/claude_code_setups.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)

# --- The big idea
A("## The big idea")
A("")
A("A modern Claude Code setup is **layered**, and the 2026 superpower is *on-demand "
  "context*, not a big always-loaded instruction blob. A harness runs the loop; **skills** "
  "and config shape behavior only when triggered; **memory** persists context across "
  "sessions; **token-savers** compress what the model sees; **code-graph/retrieval** feeds "
  "it the right code; **MCP** adds reach; **observability** measures it; **local runtimes** "
  "cut cost. Your stars already contain a best-in-class tool for every one of those layers — "
  "this report assembles them into three ready-to-run strategies.")
A("")

# --- The three strategies (the headline deliverable)
A("## Three setup strategies (built from your stars)")
A("")
A("| Layer | 🟢 Token-saver | 🟡 Balanced (recommended) | 🔴 Max-performance |")
A("|---|---|---|---|")
strat = [
    ("Harness", "`claude-code` (Sonnet)", "`claude-code` (Sonnet→Opus on hard tasks)", "`claude-code` (Opus) + `cc-switch` to model-shop"),
    ("Skills", "`caveman` (trim) + 1–2 essentials", "`obra/superpowers` + `anthropics/skills`", "`superpowers` + `wshobson/agents` + vertical packs"),
    ("Config", "one lean `CLAUDE.md` (karpathy-skills)", "`claude-code-templates` (configure+monitor)", "`gstack` / `centminmod` full kit"),
    ("Memory", "off / minimal", "`claude-mem` (you run this)", "`claude-mem` + `mem0` backend"),
    ("Token-saver", "`rtk` proxy + `semble` search + `headroom`", "`semble` for code search; `codeburn` to watch spend", "`codeburn` dashboard; spend where it pays"),
    ("Code-graph", "`graphify` (AST, no API)", "`graphify` / `codegraph`", "`codegraph` + `codebase-memory-mcp`"),
    ("MCP", "none global", "`context7` (live docs)", "`context7` + curated from `awesome-mcp-servers`"),
    ("Observability", "skip", "`langfuse` (you wire this)", "`langfuse` + `opik`/`phoenix` evals"),
    ("Local runtime", "`ollama` for grunt work", "`litellm` gateway, escalate to cloud", "cloud frontier; `litellm` for fallback"),
]
for layer, a, b, c in strat:
    A(f"| **{layer}** | {a} | {b} | {c} |")
A("")
A("**One-line verdict:** the *token-saver* and *max-performance* columns share the same "
  "backbone — a lean harness, on-demand skills, and a clean context. They differ mainly in "
  "*model tier* and *how many measurement/eval layers* you bolt on. The expensive mistake is "
  "the same in both: front-loading instructions the model only half-reads.")
A("")

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} Claude-Code 'superpower' projects** in your stars "
  f"(**{fmt_int(total_stars)}★** combined), spanning {len(cats)} setup layers:")
for c in ORDER:
    if cats.get(c):
        A(f"  - **{c}** ({len(cats[c])}): "
          + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(cats[c], key=lambda x: -by_name[x]['stars'])))
A("- **Skills are the leverage point.** `obra/superpowers` (the most-starred repo in this "
  "whole set) and `anthropics/skills` replace most always-on `CLAUDE.md` prose with "
  "on-demand expertise — cheaper *and* sharper.")
A("- **Token-saving is now a stack, not a setting.** A proxy (`rtk`), a leaner code-search "
  "(`semble`, ~98% fewer tokens than reading files), output compression (`headroom`), and a "
  "spend dashboard (`codeburn`) compose into 60–90% reductions on real dev loops.")
A("- **You already run three layers well** — `claude-mem` (memory), `graphify` (code-graph), "
  "and `langfuse` (observability) — plus `context7` over MCP. The gap is a **skills "
  "framework** and a deliberate **model-tier policy**.")
A("")

# --- The layered mental model
A("## The setup, layer by layer")
A("")
A("| Layer | What it buys you | Your starred picks |")
A("|---|---|---|")
layer_blurb = {
    "Harness / coding agent": "The agent loop itself",
    "Skills framework": "On-demand expertise (the modern superpower)",
    "Config / setup kit": "Shape behavior up front, cheaply",
    "Memory / context": "Persist context across sessions",
    "Token-saver / compression": "Shrink what the model has to read",
    "Code-graph / retrieval": "Feed the *right* code, not all of it",
    "MCP ecosystem": "External reach (docs, tools, data)",
    "Observability / evals": "Measure cost & quality",
    "Local runtime": "Cut cost / go offline",
}
for c in ORDER:
    members = cats.get(c) or []
    if not members:
        continue
    picks = ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(members, key=lambda x: -by_name[x]['stars'])[:6])
    A(f"| **{c}** | {layer_blurb[c]} | {picks} |")
A("")

# --- Master comparison
A("## Master comparison")
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
    "Harness / coding agent": "The loop that reads, plans, edits, and runs. Pick one as your "
        "daily driver; keep a second installed to diff behavior and model-shop.",
    "Skills framework": "The biggest 2026 upgrade. Skills load only when triggered, so they add "
        "capability without taxing every session — the opposite of a big always-on CLAUDE.md.",
    "Config / setup kit": "Turnkey CLAUDE.md / command / hook bundles. Steal a good one, then "
        "trim to what you actually use — bloat here is paid on every prompt.",
    "Memory / context": "Persist decisions and context across sessions so the agent doesn't "
        "re-derive what it already learned. The backend is swappable.",
    "Token-saver / compression": "Measure first (`codeburn`), then compress: leaner code search, "
        "output trimming, and a front proxy stack to 60–90% on common loops.",
    "Code-graph / retrieval": "Give the agent structure instead of raw files — graphs and indexes "
        "answer 'how does X relate to Y' without scanning the repo.",
    "MCP ecosystem": "External capabilities via a standard protocol. Each connected server costs "
        "context, so connect deliberately — `context7` (live docs) is the highest-ROI default.",
    "Observability / evals": "You can't optimize what you can't see. Trace runs, watch spend, and "
        "score outputs before trusting an autonomous setup.",
    "Local runtime": "Run open models locally or proxy many models behind one endpoint — the cost "
        "floor for grunt work and the fallback when the cloud is down.",
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

# --- Graph analysis
A("## Graph analysis — how they relate")
A("")
comm = {}
for n in present:
    nd = node_for(n)
    if nd is not None:
        comm.setdefault(nd.get("community"), []).append(n)
A(f"**Community clustering.** These {len(present)} tools span "
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities** — the Claude-Code "
  f"ecosystem is spread across agent-framework, memory, retrieval, and observability "
  f"neighborhoods rather than forming one tidy cluster.")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 2:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in names))
A("")

ranked = sorted(
    [(node_for(n).get("pagerank", 0) if node_for(n) else 0, n) for n in present],
    key=lambda x: -x[0],
)
A(f"**Centrality (PageRank in the full {fmt_int(len(gr['nodes']))}-repo graph)** — the most "
  "'hub-like' setup tools in your ecosystem:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between these tools** (top similarity edges where both endpoints are in "
  "this report):")
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
    A("- _None — these tools don't link tightly in the similarity graph; they cluster with "
      "their broader neighborhoods instead._")
A("")

# --- Maintenance / risk
A("## Maintenance & risk signal")
A("")
A("Bus factor = commit concentration (1 = single-maintainer risk). This ecosystem moves fast "
  "and a lot of it is one-person projects — check before wiring one into your daily loop.")
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

# --- Adjacent
A("## Adjacent (deliberately not listed here)")
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
A("- **Selection**: keyword scan (claude-code / skill / agent harness / mcp / memory / token "
  "/ observability / code-graph / setup) across name+description+topics, then manual curation "
  "into the nine setup layers. General agent *application* frameworks, chat UIs, and broad "
  "platforms were routed to adjacent reports or excluded (see above).")
A("- **The three-strategy table is opinionated**, built only from repos in your stars — it "
  "is a starting point, not a benchmark. Validate model-tier and token-saver claims against "
  "your own `langfuse`/`codeburn` traces.")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may "
  "lag GitHub's current state.")
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
    "summary": (f"{len(present)} Claude-Code 'superpower' projects ({fmt_int(total_stars)}★) "
                "organized into 9 setup layers — harnesses, skills, memory, token-savers, "
                "code-graph, MCP, observability, config kits, local runtimes — plus three "
                "ready-to-run setup strategies (token-saver / balanced / max-performance)."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in ORDER},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/claude_code_setups.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
