#!/usr/bin/env python3
"""
Generate a landscape report on terminal AI coding agents (TUIs) found in the
starred-repos dataset: the full coding agents themselves plus the terminal
ecosystem around them (token/session ops, safety, launchers, TUI frameworks) —
with explicit advantages/disadvantages per agent and task-ranked picks backed
by external evidence (Terminal-Bench 2.1, head-to-head comparisons).

Inputs:
  data/classified.json
  public/data/graph.json

Output:
  reports/ai-coding-tuis.md   (+ reports/ai-coding-tuis.meta.json)

Run: python3 scripts/reports/ai_coding_tuis.py
"""
import json
import os
from datetime import datetime, timezone

from lib import fmt_stars, CLASSIFIED, GRAPH, fmt_int, days_to_human, activity_label, make_node_for

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "ai-coding-tuis"
TITLE = "Terminal AI Coding Agents (TUIs) — Best Picks, Advantages & Disadvantages"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy --------------------------------------------------------
TAXONOMY = {
    # Terminal coding agents (the TUIs themselves)
    "anthropics/claude-code": ("Terminal coding agent", "Anthropic's agentic coding TUI — deep codebase understanding, subagents, hooks, skills, MCP."),
    "anomalyco/opencode": ("Terminal coding agent", "The most-starred open-source coding agent — provider-neutral (75+ LLM endpoints incl. local), MIT."),
    "google-gemini/gemini-cli": ("Terminal coding agent", "Gemini in the terminal with a 1M-token context window — but deprecated June 2026 in favor of closed-source Antigravity CLI."),
    "openai/codex": ("Terminal coding agent", "OpenAI's lightweight Rust terminal agent — tops Terminal-Bench 2.1 among named CLI agents (83.4% with GPT-5.5)."),
    "aaif-goose/goose": ("Terminal coding agent", "Block's extensible on-machine agent — MCP-first, goes beyond code (install, execute, test) with any LLM."),
    "Aider-AI/aider": ("Terminal coding agent", "The original AI pair programmer in the terminal — git-native, focused file-level edits, not an autonomous agent."),
    "charmbracelet/crush": ("Terminal coding agent", "Charm's glamorous multi-model coding agent — the best-looking TUI in the field (Bubble Tea pedigree)."),
    "QwenLM/qwen-code": ("Terminal coding agent", "Qwen team's terminal agent — strong with Qwen3-Coder and Chinese-language briefs; OAuth free tier ended 2026-04."),
    "github/copilot-cli": ("Terminal coding agent", "Copilot coding agent in the terminal — deep GitHub integration, premium-request pricing model."),
    "earendil-works/pi": ("Terminal coding agent", "Minimal AI toolkit: unified LLM API + agent loop + TUI + coding CLI — the hackable build-your-own base."),
    "code-yeongyu/oh-my-openagent": ("Terminal coding agent", "omo/lazycodex — token-obsessed harness layered on Codex/OpenCode for complex codebases."),
    "CodebuffAI/codebuff": ("Terminal coding agent", "Codegen from the terminal — smaller, focused alternative."),
    "rsrohan99/tig": ("Terminal coding agent", "Multi-LLM Claude-Code-alike — abandoned; listed as a cautionary tale of the category's churn."),

    # Session, token & cost ops
    "rtk-ai/rtk": ("Session / token ops", "CLI proxy that cuts LLM token use 60–90% on common dev commands — single Rust binary."),
    "mksglu/context-mode": ("Session / token ops", "Context-window optimizer for coding agents — sandboxes tool output (~98% reduction), persists session memory."),
    "getagentseal/codeburn": ("Session / token ops", "Local token/cost tracker across 31 coding tools and agents, by model, project, and tool."),
    "ctxrs/ctx": ("Session / token ops", "Search the coding-agent history already on your machine — cross-agent transcript recall."),
    "evrendom/rudel": ("Session / token ops", "Claude Code & Codex session analytics."),
    "terryso/claude-auto-resume": ("Session / token ops", "Shell utility that resumes Claude CLI tasks when usage limits lift."),
    "aniketkarne/ClaudeNightsWatch": ("Session / token ops", "Autonomous task runner that watches Claude usage windows and executes queued tasks."),

    # Safety & isolation
    "sheeki03/tirith": ("Safety / isolation", "Terminal security for devs and agents — intercepts homograph URLs, pipe-to-shell, ANSI injection, exfiltration."),
    "kenryu42/cc-safety-net": ("Safety / isolation", "Hook that catches destructive git/filesystem commands before they execute (Codex, Claude Code, more)."),
    "dagger/container-use": ("Safety / isolation", "Containerized dev environments so multiple agents work safely and independently."),
    "affaan-m/agentshield": ("Safety / isolation", "Scanner for agent configs, MCP servers, and tool permissions — CLI and CI modes."),

    # Multi-CLI glue & launchers
    "farion1231/cc-switch": ("Multi-CLI glue", "All-in-one switcher for Claude Code, Codex, OpenCode, OpenClaw, Gemini CLI & Hermes Agent."),
    "Alishahryar1/free-claude-code": ("Multi-CLI glue", "Run claude code, codex or pi free in terminal/VSCode/discord — proxy-style access layer."),
    "UfoMiao/zcf": ("Multi-CLI glue", "Zero-Config Code Flow — one-command setup for Claude Code & Codex."),
    "BA-CalderonMorales/terminal-jarvis": ("Multi-CLI glue", "A 'shovel' to install and try every terminal coding tool from one place."),
    "zamalali/langchain-code": ("Multi-CLI glue", "LangCode — combines gemini-cli and claude-code capabilities under one CLI; now declining."),

    # TUI building blocks
    "charmbracelet/bubbletea": ("TUI building blocks", "The Go TUI framework — the substrate under crush and much of the modern terminal-app wave."),
    "charmbracelet/bubbles": ("TUI building blocks", "Ready-made TUI components for Bubble Tea."),
}

# Adjacent but deliberately excluded (kept honest in the report)
ADJACENT = [
    ("cline/cline", "primarily an IDE extension (CLI mode is secondary) — not a TUI-first agent"),
    ("continuedev/continue", "same: IDE-first open-source coding agent"),
    ("OpenHands/OpenHands", "AI-dev *platform* (web/headless), not a terminal UI"),
    ("langchain-ai/open-swe", "asynchronous *cloud* coding agent — no terminal in the loop"),
    ("NousResearch/hermes-agent", "covered in the *hermes-vs-openclaw* and *agent-harnesses* reports"),
    ("affaan-m/ECC", "harness/config framework on top of coding TUIs — see *claude-code-setups*"),
    ("SuperClaude-Org/SuperClaude_Framework", "config framework — see *claude-code-setups* (retired upstream 2026-07)"),
    ("BloopAI/vibe-kanban", "GUI orchestrator *over* coding agents, not a TUI"),
    ("iOfficeAI/AionUi", "GUI wrapper over the CLIs, not a TUI"),
    ("winfunc/opcode", "GUI toolkit for Claude Code"),
    ("jesseduffield/lazygit", "beloved git TUI, but no AI"),
]

# Advantages / disadvantages per core agent (curated from web evidence + dataset)
PROS_CONS = [
    ("anthropics/claude-code",
     "Best-in-class multi-file refactoring and reasoning depth (SWE-bench Pro 69.2%); asks clarifying questions; subagents/hooks/skills/MCP ecosystem is the deepest; 83.1% Terminal-Bench 2.1 with Fable 5",
     "Not open source (no OSS license in repo); Anthropic-models only; subscription/usage costs add up on heavy agentic use"),
    ("anomalyco/opencode",
     "Most-starred OSS agent, MIT license; provider-neutral — 75+ endpoints incl. Bedrock, OpenRouter, local Ollama; strong TUI; no vendor lock-in",
     "Bring-your-own-model means quality varies with the model you pick; harness benchmark scores trail the vendor-tuned agents"),
    ("openai/codex",
     "#1 named CLI agent on Terminal-Bench 2.1 (83.4% w/ GPT-5.5); fast single-binary Rust TUI; excels at intent-driven, pattern-following edits",
     "OpenAI-models only; less transparent reasoning than Claude Code on big refactors; ecosystem (hooks/plugins) thinner"),
    ("google-gemini/gemini-cli",
     "1M-token context — holds a monorepo in one window; Apache-2.0; was the best free tier in the field",
     "Deprecated June 2026: replaced by closed-source Antigravity CLI (agy), free tier cut from ~1,000 to ~20 requests/day — adopt with exit plan"),
    ("aaif-goose/goose",
     "MCP-first and extensible beyond coding (install/execute/test); any-LLM incl. local; Block-backed, health 99 in this snapshot",
     "Less specialized for pure code-editing loops; leaderboard results modest — team optimizes for failure-pattern fixes, not benchmark rank"),
    ("Aider-AI/aider",
     "Best git discipline (clean auto-commits); precise file-scoped edits; provider-resilient; the safest 'pair programmer' rather than autonomous agent",
     "Not autonomous — no system-wide orchestration; no MCP support; momentum slowing (52d since push, health 50 in snapshot)"),
    ("charmbracelet/crush",
     "The most polished TUI aesthetics in the field; multi-model; Charm's Bubble Tea expertise shows in UX",
     "Youngest of the majors — no public benchmark record; non-standard license; smaller ecosystem"),
    ("QwenLM/qwen-code",
     "Competitive Qwen3-Coder models; best-in-class on Chinese-language briefs and Alibaba-cloud ecosystem; Apache-2.0",
     "OAuth free tier discontinued 2026-04 — headline value now requires paid API; less strong outside the Qwen model family"),
    ("github/copilot-cli",
     "Copilot agent with native GitHub integration (issues, PRs, Actions); familiar billing for Copilot shops",
     "Premium-request pricing — one debugging session can eat a week's free allocation; value collapses off-GitHub (GitLab/Bitbucket)"),
    ("earendil-works/pi",
     "Minimal, hackable toolkit (API + agent loop + TUI + CLI) — ideal base for building your own agent; MIT",
     "A toolkit, not a turnkey product — you assemble the workflow yourself; smaller community than the big four"),
    ("code-yeongyu/oh-my-openagent",
     "Token-efficiency-first harness (the 'tokenmaxxer' pick) layered on Codex/OpenCode for complex codebases",
     "Depends on underlying agents; opinionated workflow; no OSS license declared"),
    ("CodebuffAI/codebuff",
     "Simple terminal codegen with low setup friction; Apache-2.0",
     "Far smaller scope and community than the majors; fewer agentic features (no deep hooks/MCP story)"),
    ("rsrohan99/tig",
     "Historic multi-LLM flexibility (Gemini, Groq, Deepseek) before the majors had it",
     "Abandoned (437d since push, health 5) — do not adopt; kept here to show the category's churn"),
]

# Task-ranked picks: (task, [(repo, note) x3], evidence)
TASK_RANKINGS = [
    ("Complex multi-file refactors in a large repo",
     [("anthropics/claude-code", "reasoning depth + style consistency"),
      ("openai/codex", "pattern-faithful edits, benchmark leader"),
      ("anomalyco/opencode", "same job, any model, MIT")],
     "Claude Code leads SWE-bench Pro (69.2%); Codex CLI leads Terminal-Bench 2.1 (83.4%)."),
    ("Best raw agentic benchmark ceiling",
     [("openai/codex", "83.4% Terminal-Bench 2.1 (GPT-5.5)"),
      ("anthropics/claude-code", "83.1% with Fable 5; 78.9% with Opus 4.8"),
      ("aaif-goose/goose", "solid but optimizes failure patterns over rank")],
     "Terminal-Bench 2.1 public leaderboard, June 2026 snapshot."),
    ("Model freedom / local LLMs (no vendor lock-in)",
     [("anomalyco/opencode", "75+ endpoints incl. Ollama"),
      ("aaif-goose/goose", "any LLM, MCP-first"),
      ("charmbracelet/crush", "multi-model with the nicest TUI")],
     "opencode is the most-starred OSS agent and the de-facto neutral choice."),
    ("Monorepo-scale context in one window",
     [("google-gemini/gemini-cli", "1M-token context — but see deprecation caveat"),
      ("anthropics/claude-code", "subagents fan out instead of one big window"),
      ("anomalyco/opencode", "pair with a long-context model of your choice")],
     "Gemini's 1M context is unmatched, but the OSS CLI was frozen June 2026 (Antigravity)."),
    ("Careful pair-programming with git discipline",
     [("Aider-AI/aider", "clean scoped diffs, auto-commits"),
      ("anthropics/claude-code", "plan mode + hooks for guarded edits"),
      ("openai/codex", "tight, reviewable single-file changes")],
     "Aider remains the reference for git-native, human-in-the-loop editing."),
    ("Token- and cost-conscious agentic coding",
     [("code-yeongyu/oh-my-openagent", "built for tokenmaxxers"),
      ("anomalyco/opencode", "route to cheap/local models; add rtk proxy"),
      ("QwenLM/qwen-code", "cheap capable models — free tier gone though")],
     "Pair any pick with `rtk` (60–90% token cut) and `codeburn` (cost tracking)."),
    ("GitHub-centric team workflows",
     [("github/copilot-cli", "native issues/PR/Actions integration"),
      ("anthropics/claude-code", "gh CLI + hooks cover most of it"),
      ("openai/codex", "cloud-task handoff to the Codex platform")],
     "Copilot CLI's value is the GitHub integration; it collapses off-platform."),
    ("Building your own agent / custom TUI",
     [("earendil-works/pi", "toolkit: LLM API + loop + TUI ready-made"),
      ("charmbracelet/bubbletea", "the TUI framework everything's built on"),
      ("anomalyco/opencode", "fork-friendly MIT reference implementation")],
     "pi gives the agent loop; Bubble Tea gives the terminal UI substrate."),
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
  f"{len(gr['communities'])} communities). Pros/cons and task rankings are "
  f"additionally backed by external evidence (Terminal-Bench 2.1, 2026 "
  f"head-to-head comparisons) — see Methodology.")
A(">")
A(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/ai_coding_tuis.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)
order = ["Terminal coding agent", "Session / token ops", "Safety / isolation",
         "Multi-CLI glue", "TUI building blocks"]

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} terminal-AI-coding tools** in your stars "
  f"(**{fmt_int(total_stars)}★** combined), split into the agents themselves "
  f"and the terminal ecosystem around them:")
for c in order:
    if cats.get(c):
        A(f"  - **{c}** ({len(cats[c])}): "
          + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(cats[c], key=lambda x: -by_name[x]['stars'])))
A("- **Short answer to 'which TUI is best':** `claude-code` for reasoning depth and "
  "the richest extension ecosystem, `codex` for the highest benchmark ceiling, "
  "`opencode` if you want open source and model freedom. `aider` remains the best "
  "*pair programmer* (as opposed to autonomous agent); `goose` the best MCP-native "
  "generalist; `crush` the best-looking.")
A("- **The harness matters more than the model**: the same GPT-5.5 scores 83.4% on "
  "Terminal-Bench 2.1 inside Codex CLI but 76.4% inside a generic harness — a "
  "7-point gap that is pure agent-loop engineering.")
A("- **Platform risk is real**: Gemini CLI was deprecated for a closed-source "
  "replacement in June 2026 with the free tier cut ~50×, and qwen-code's OAuth free "
  "tier ended in April — open-source-ness and provider neutrality (`opencode`, "
  "`goose`) are hedges, not ideology.")
A("")

# --- Anatomy table
A("## The terminal-agent stack at a glance")
A("")
A("| Layer | What it does | Tools in your stars |")
A("|---|---|---|")
A("| **The agent (TUI)** | Plan, edit, run, iterate in your terminal | "
  "`claude-code`, `opencode`, `gemini-cli`, `codex`, `goose`, `aider`, `crush`, "
  "`qwen-code`, `copilot-cli`, `pi`, `oh-my-openagent`, `codebuff` |")
A("| **Token / session ops** | Cut cost, track spend, recall history | "
  "`rtk`, `context-mode`, `codeburn`, `ctx`, `rudel`, `claude-auto-resume`, `ClaudeNightsWatch` |")
A("| **Safety** | Guard the shell the agent drives | "
  "`tirith`, `cc-safety-net`, `container-use`, `agentshield` |")
A("| **Glue / launchers** | Switch, combine, and provision the CLIs | "
  "`cc-switch`, `free-claude-code`, `zcf`, `terminal-jarvis`, `langchain-code` |")
A("| **Build-your-own** | Frameworks the TUIs are made of | "
  "`bubbletea`, `bubbles`, `pi` |")
A("")

# --- Master comparison
A("## Master comparison")
A("")
A("Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits.")
A("")
A("| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | "
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

# --- Advantages / disadvantages (the core ask)
A("## Advantages & disadvantages — agent by agent")
A("")
A("The core comparison. Sourced from 2026 head-to-head reviews, Terminal-Bench "
  "results, and this dataset's health/lifecycle metrics (sources in Methodology).")
A("")
A("| Agent | ★ Stars | Advantages | Disadvantages |")
A("|" + "---|" * 4)
for n, pros, cons in PROS_CONS:
    r = by_name.get(n)
    if r is None:
        continue
    A(f"| **[{n.split('/')[-1]}]({r['url']})** | {fmt_int(r['stars'])} | {pros} | {cons} |")
A("")

# --- Task rankings
A("## Task rankings — which TUI for which job")
A("")
A("| Task | 🥇 First pick | 🥈 Second | 🥉 Third | Evidence / note |")
A("|" + "---|" * 5)
for task, picks, evidence in TASK_RANKINGS:
    cells = [f"`{repo.split('/')[-1]}` — {note}" for repo, note in picks]
    A(f"| **{task}** | {cells[0]} | {cells[1]} | {cells[2]} | {evidence} |")
A("")

# --- Category deep dives
A("## By category")
A("")
cat_blurb = {
    "Terminal coding agent": "The TUIs themselves — full agentic loops (plan → edit → "
        "run → iterate) living in your terminal. Differ in model access, autonomy "
        "level, ecosystem depth, and openness.",
    "Session / token ops": "The cost layer: agentic coding burns tokens, and these "
        "tools cut, track, and recycle them across sessions.",
    "Safety / isolation": "An agent driving your shell is a security surface — these "
        "guard commands, sandbox environments, and audit configurations.",
    "Multi-CLI glue": "Most people end up running several agents; these switch "
        "between, combine, and provision them.",
    "TUI building blocks": "The frameworks the agents' interfaces are built from — "
        "relevant if you build rather than buy.",
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

# --- Spotlight
A("## Spotlight: the harness matters more than the model")
A("")
A("The June 2026 Terminal-Bench 2.1 snapshot makes one thing unambiguous — the "
  "agent loop wrapping the model is worth real percentage points:")
A("")
A("- Same GPT-5.5 model: **83.4%** inside Codex CLI vs **76.4%** inside the generic "
  "Terminus 2 harness — a 7-point gap that is pure harness engineering.")
A("- Claude Code posts **83.1%** with Fable 5 and **78.9%** with Opus 4.8 — the "
  "model swap moves it more than most competitor-harness swaps do.")
A("- Consequence for choosing: pick the *harness* whose ecosystem you can invest in "
  "(hooks, skills, MCP servers, safety nets), because vendor-tuned harness+model "
  "pairs beat mix-and-match on agentic work — while `opencode`/`goose` hedge the "
  "platform risk the Gemini CLI deprecation just demonstrated.")
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
A(f"**Centrality (PageRank in the full {fmt_int(len(gr['nodes']))}-repo graph)** — "
  "most 'hub-like' terminal-coding tools in your ecosystem:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between these tools** (top similarity edges where both endpoints "
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
A("Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle "
  "+ activity before adopting.")
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
A("Watch items: `gemini-cli` is deprecated upstream (Antigravity CLI replaced it, "
  "June 2026) despite healthy-looking repo metrics; `aider` is slowing (52d since "
  "push in this snapshot); `tig` and `langchain-code` are effectively dead; "
  "`claude-auto-resume` and `ClaudeNightsWatch` are declining single-maintainer "
  "shell utilities.")
A("")

# --- Adjacent
A("## Adjacent (deliberately not listed as terminal coding agents)")
A("")
for name, why in ADJACENT:
    r = by_name.get(name)
    star = f" ({fmt_int(r['stars'])}★)" if r else ""
    A(f"- **{name}**{star} — {why}")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `data/classified.json` + `public/data/graph.json` for all repo "
  "metrics and graph structure. No API calls at generation time; fully reproducible.")
A("- **Selection**: keyword scan (terminal / tui / cli / coding agent / pair "
  "programming) + manual curation. IDE-first agents, GUI wrappers, cloud agents, and "
  "config frameworks were routed to adjacent reports (see above).")
A("- **Pros/cons & task rankings** cite external evidence gathered 2026-07: the "
  "[Terminal-Bench](https://www.tbench.ai/) 2.1 public leaderboard (June 2026 "
  "snapshot: Codex CLI 83.4% w/ GPT-5.5, Claude Code 83.1% w/ Fable 5 / 78.9% w/ "
  "Opus 4.8; same GPT-5.5 at 76.4% in the Terminus 2 harness), 2026 head-to-head "
  "comparisons ([tembo.io](https://www.tembo.io/blog/coding-cli-tools-comparison), "
  "[morphllm.com](https://www.morphllm.com/ai-coding-agent), "
  "[kilo.ai](https://kilo.ai/articles/best-cli-coding-agents)), and vendor "
  "announcements (Gemini CLI → Antigravity deprecation, qwen-code free-tier "
  "retirement). Benchmark numbers are point-in-time — treat rankings as defaults, "
  "not verdicts.")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and "
  "may lag GitHub's current state.")
A("- Re-run after a fresh `classified.json` to refresh stars/activity; frozen "
  "benchmark citations need manual review as new models/agents ship.")
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
    "category": "AI / Comparison",
    "summary": (f"{len(present)} terminal AI coding tools ({fmt_int(total_stars)}★): "
                "the TUI agents themselves with per-agent advantages/disadvantages "
                "and Terminal-Bench-backed task rankings, plus the token-ops, "
                "safety, and launcher ecosystem around them."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in order},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/ai_coding_tuis.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
