#!/usr/bin/env python3
"""
Generate a *methods* report on harness engineering — how to make an agent harness
good, not which harness to pick (that is the agent-harnesses report). Organized as
ten practices in build order, each backed by frozen evidence from published
studies/engineering posts and ranked against the repos in the starred dataset that
implement it.

Inputs:
  data/classified.json
  public/data/graph.json

Output:
  reports/harness-engineering.md   (+ reports/harness-engineering.meta.json)

Run: python3 scripts/reports/harness_engineering.py
"""
import json
import os
from datetime import datetime, timezone

from lib import fmt_stars, CLASSIFIED, GRAPH, fmt_int, days_to_human, activity_label, make_node_for

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "harness-engineering"
TITLE = "Harness Engineering — Ten Methods That Make an Agent Harness Good"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy (category = the method the repo helps you apply) --------
TAXONOMY = {
    # 1. Start from a minimal loop
    "earendil-works/pi": ("1. Minimal loop first", "Unified LLM API + small agent loop + TUI — a readable baseline to grow a harness from."),
    "SWE-agent/SWE-agent": ("1. Minimal loop first", "The project that named the *agent-computer interface* — proof that interface design moves scores."),
    "Piebald-AI/claude-code-system-prompts": ("1. Minimal loop first", "Every part of Claude Code's system prompt, tool descriptions and sub-agent prompts — a production harness to read."),
    "Nicolepcx/harness_engineering": ("1. Minimal loop first", "Code for the O'Reilly *Harness Engineering* book — worked examples of each harness layer."),

    # 2. Small instruction budget, progressive disclosure
    "agentsmd/agents.md": ("2. Small instruction budget", "AGENTS.md — one short, portable repo contract instead of a sprawling prompt."),
    "anthropics/skills": ("2. Small instruction budget", "Reference Agent Skills: knowledge loaded on demand, not pinned in every turn."),
    "obra/superpowers": ("2. Small instruction budget", "Skills + methodology (TDD, plans, review) delivered as progressively-disclosed skills."),
    "multica-ai/andrej-karpathy-skills": ("2. Small instruction budget", "A single short CLAUDE.md of behavioural rules — the minimal-instructions end of the spectrum."),

    # 3. Context engineering
    "mksglu/context-mode": ("3. Context engineering", "Sandboxes tool output out of the context window (claims ~98% reduction)."),
    "headroomlabs-ai/headroom": ("3. Context engineering", "Compresses tool outputs, logs, files and RAG chunks before they reach the model."),
    "rtk-ai/rtk": ("3. Context engineering", "CLI proxy that filters and condenses shell output for coding agents."),
    "alexgreensh/token-optimizer": ("3. Context engineering", "Finds 'ghost tokens' and helps sessions survive compaction without quality decay."),

    # 4. Lean action space / tool design
    "jgravelle/jcodemunch-mcp": ("4. Lean action space", "Symbol-level code retrieval — return the function, not the file."),
    "oraios/serena": ("4. Lean action space", "Semantic (LSP-backed) retrieval and editing tools — fewer, sharper code tools."),
    "vercel-labs/agent-browser": ("4. Lean action space", "Browser automation as a compact CLI built for agents rather than a large MCP surface."),
    "upstash/context7": ("4. Lean action space", "Fetches current, version-specific docs on demand instead of stuffing them into prompts."),

    # 5. Externally grounded verification (back-pressure)
    "microsoft/playwright-mcp": ("5. External verification", "Lets the agent drive the real app and check its own UI changes."),
    "haydenbleasel/ultracite": ("5. External verification", "Zero-config lint/format — cheap, deterministic back-pressure inside the loop."),
    "alibaba/open-code-review": ("5. External verification", "Hybrid deterministic + LLM code review run against the agent's diff."),
    "modem-dev/hunk": ("5. External verification", "Review-first terminal diff viewer — keeps a human verifying what the agent changed."),

    # 6. State on disk
    "OthmanAdi/planning-with-files": ("6. State on disk", "Plans and progress persisted to files — crash-proof, resumable long tasks."),
    "snarktank/ralph": ("6. State on disk", "Fresh-context loop that re-reads a PRD and progress file until every item is done."),
    "github/spec-kit": ("6. State on disk", "Spec-driven development: the spec on disk steers each session."),
    "cobusgreyling/loop-engineering": ("6. State on disk", "Patterns and starters for designing the iteration itself."),

    # 7. Sub-agents for context isolation
    "langchain-ai/deepagents": ("7. Sub-agents for isolation", "Planning + filesystem + sub-agents with isolated context windows, as a library."),
    "VoltAgent/awesome-claude-code-subagents": ("7. Sub-agents for isolation", "100+ sub-agent definitions — useful as patterns for scoped, condensed returns."),
    "Yeachan-Heo/oh-my-claudecode": ("7. Sub-agents for isolation", "Multi-agent orchestration inside Claude Code — delegation via sub-agents."),

    # 8. Executable guards & sandboxes
    "kenryu42/cc-safety-net": ("8. Guards & sandboxes", "Pre-execution hook that blocks destructive git and filesystem commands."),
    "dagger/container-use": ("8. Guards & sandboxes", "Per-agent containerized environments so agents can't trample each other or the host."),
    "daytonaio/daytona": ("8. Guards & sandboxes", "Secure, elastic sandboxes for running AI-generated code."),
    "NVIDIA/SkillSpector": ("8. Guards & sandboxes", "Scans agent skills for malicious or vulnerable patterns before you load them."),

    # 9. Durable runs & human checkpoints
    "open-multi-agent/open-multi-agent": ("9. Durable runs & approvals", "Agent runtime with durable approvals and verifiable run records."),
    "triggerdotdev/trigger.dev": ("9. Durable runs & approvals", "Durable execution for agents and workflows — retries, resumes, long waits."),
    "backnotprop/plannotator": ("9. Durable runs & approvals", "Annotate and approve agent plans and diffs before execution continues."),

    # 10. Observe and evaluate the harness itself
    "langfuse/langfuse": ("10. Observe & eval the harness", "Open-source tracing + evals — see which steps, tools and rules actually fire."),
    "getagentseal/codeburn": ("10. Observe & eval the harness", "Local token/cost tracking across 37 coding agents — measure harness overhead."),
    "harbor-framework/harbor": ("10. Observe & eval the harness", "Framework for evaluating and improving agents on frozen task sets."),
    "promptfoo/promptfoo": ("10. Observe & eval the harness", "Regression tests and red-teaming for prompts and agents in CI."),
}

ORDER = [
    "1. Minimal loop first", "2. Small instruction budget", "3. Context engineering",
    "4. Lean action space", "5. External verification", "6. State on disk",
    "7. Sub-agents for isolation", "8. Guards & sandboxes",
    "9. Durable runs & approvals", "10. Observe & eval the harness",
]

# Method → (the rule, the evidence behind it). Evidence is frozen at authoring time
# (retrieved 2026-10-01) — see Methodology for sources; it does NOT refresh on rebuild.
METHODS = {
    "1. Minimal loop first":
        ("Start from the smallest loop that works, and add a harness component only in "
         "response to an observed failure — never on the assumption the model can't cope.",
         "Practitioner consensus in 2026 (HumanLayer, marmelab survey). Fan et al. (176 "
         "configurations, 4 models) found a bash-only action space gives capable models "
         "*substantially lower cost* at equal performance; heavy scaffolding mostly helps "
         "weaker models."),
    "2. Small instruction budget":
        ("Keep the always-loaded instruction file short and hand-written (~60–100 lines); "
         "push everything else into skills or docs that load on demand.",
         "HumanLayer recommends <60 lines; OpenAI's harness write-up (via marmelab) lists "
         "context crowding, importance dilution, decay and untestability as failure modes "
         "of large instruction files. marmelab reports machine-generated context files "
         "*reduced* success and raised cost 20%+; human-written ones gained only ~4%."),
    "3. Context engineering":
        ("Treat the context window as the scarcest resource: keep the prefix stable for "
         "KV-cache hits, make history append-only, elide bulky tool output with rules "
         "*before* resorting to LLM summarization, and make compression restorable.",
         "Fan et al.: context management matters most as budgets shrink, and rule-based "
         "elision before summarization works best — mainly by preventing overflow "
         "failures. Manus: KV-cache hit rate is the key production metric (cached input "
         "~10× cheaper); keep URLs/paths so dropped content can be re-fetched."),
    "4. Lean action space":
        ("Fewer, sharper tools. Prefer CLIs the model already knows over wide MCP "
         "surfaces, load tool definitions on demand, and let the agent write code against "
         "tools so intermediate data never enters context.",
         "Anthropic's *code execution with MCP* (Nov 2025): a Drive→Salesforce workflow "
         "fell from ~150k to ~2k tokens (−98.7%). Vercel (as reported by marmelab) removed "
         "80% of an agent's tools: success 80%→100%, latency 724s→141s. HumanLayer swapped "
         "the Linear MCP server for a small CLI + examples."),
    "5. External verification":
        ("Give the agent back-pressure it cannot talk its way past: type checks, tests, "
         "linters, a browser on the real app. Swallow success output; surface only errors, "
         "with the fix written into the message.",
         "Park & Choi (2026): self-evaluating loops claimed improvement 100% of the time "
         "while 56% of cycles made zero or negative progress (the 'progress mirage'); LLM "
         "judges accepted 44% of real regressions. The mirage vanished on tasks with an "
         "externally verifiable boundary."),
    "6. State on disk":
        ("Persist the plan, feature list and progress to files (JSON beats markdown for "
         "anything the agent must not rewrite), commit often, and let each fresh session "
         "re-orient from those artifacts.",
         "Anthropic's long-running harness (Nov 2025): an initializer agent writes a feature "
         "list + progress file + git repo; each coding session picks one item, verifies it, "
         "updates the files. JSON was edited inappropriately less often than markdown. "
         "Manus keeps a live todo.md to hold goals in recent attention."),
    "7. Sub-agents for isolation":
        ("Use sub-agents to *isolate context*, not to role-play: give them a bounded task "
         "(explore, trace, research) and have them return a condensed answer with "
         "`file:line` citations. Keep handoff chains short.",
         "HumanLayer: sub-agents keep the parent in the 'smart zone' and can run on cheaper "
         "models. marmelab collects counter-evidence on *reviewer* agents (one study: −8pp "
         "on a 41% baseline) and Microsoft's finding that >4 handoffs almost always failed."),
    "8. Guards & sandboxes":
        ("Enforce rules with code, not prose: pre-execution hooks, permission gates, and an "
         "isolated sandbox per agent. Scan third-party skills and MCP servers before trust.",
         "marmelab cites an analysis of 481 public CLAUDE.md files where only 4–16% of "
         "written security rules had any detectable enforcement, and reports action-by-"
         "action approval beating pre-written permission rules by 20+pp at blocking bad "
         "actions. HumanLayer warns skill registries have shipped malicious skills."),
    "9. Durable runs & approvals":
        ("Make long runs survivable: checkpoint, retry and resume instead of restarting; put "
         "human approval at the plan and at irreversible actions rather than everywhere.",
         "Follows from methods 6 and 8: durable state lets a crashed or rate-limited run "
         "resume, and approval at the irreversible step is where action-by-action review "
         "pays off. Evidence here is architectural rather than benchmarked."),
    "10. Observe & eval the harness":
        ("Trace what the harness actually does (which rules fire, hook blocks, iterations, "
         "tokens), evaluate harness changes on a frozen task set with both should-fire and "
         "should-not-fire cases, and record why every control exists so it can be removed "
         "when models improve.",
         "marmelab's survey: only 5 of 391 harness repos logged skill activations or blocks, "
         "and only one published before/after measurements for its rules. Fan et al. show "
         "component effects are model- and budget-dependent — so measure on *your* model."),
}

# Ranked picks per method: (method, [(repo, note) × 3])
RANKINGS = [
    ("1. Minimal loop first",
     [("earendil-works/pi", "smallest complete loop to fork"),
      ("Piebald-AI/claude-code-system-prompts", "read a mature harness's prompts"),
      ("SWE-agent/SWE-agent", "ACI design as a research reference")]),
    ("2. Small instruction budget",
     [("agentsmd/agents.md", "the portable short contract"),
      ("anthropics/skills", "canonical progressive-disclosure format"),
      ("obra/superpowers", "methodology packaged as skills")]),
    ("3. Context engineering",
     [("mksglu/context-mode", "keeps raw tool output out of context"),
      ("rtk-ai/rtk", "drop-in shell-output filter"),
      ("headroomlabs-ai/headroom", "compresses logs/files/RAG chunks")]),
    ("4. Lean action space",
     [("jgravelle/jcodemunch-mcp", "symbol-level reads, not whole files"),
      ("oraios/serena", "LSP-backed retrieval + edits"),
      ("vercel-labs/agent-browser", "compact agent-first CLI")]),
    ("5. External verification",
     [("microsoft/playwright-mcp", "agent checks the running app"),
      ("haydenbleasel/ultracite", "fast deterministic lint gate"),
      ("alibaba/open-code-review", "review pass on every diff")]),
    ("6. State on disk",
     [("OthmanAdi/planning-with-files", "plan/progress files out of the box"),
      ("github/spec-kit", "spec as the durable source of truth"),
      ("snarktank/ralph", "fresh-context loop over a PRD")]),
    ("7. Sub-agents for isolation",
     [("langchain-ai/deepagents", "isolation built into the SDK"),
      ("VoltAgent/awesome-claude-code-subagents", "patterns to copy"),
      ("Yeachan-Heo/oh-my-claudecode", "delegation inside Claude Code")]),
    ("8. Guards & sandboxes",
     [("kenryu42/cc-safety-net", "blocks destructive commands pre-exec"),
      ("dagger/container-use", "one container per agent"),
      ("NVIDIA/SkillSpector", "vet skills before loading")]),
    ("9. Durable runs & approvals",
     [("open-multi-agent/open-multi-agent", "durable approvals + run records"),
      ("triggerdotdev/trigger.dev", "retries/resume for long jobs"),
      ("backnotprop/plannotator", "human approves the plan")]),
    ("10. Observe & eval the harness",
     [("langfuse/langfuse", "traces + evals, self-hostable"),
      ("harbor-framework/harbor", "frozen task-set evals"),
      ("getagentseal/codeburn", "token/cost per agent, local")]),
]

# What the evidence says does NOT work (frozen; sources in Methodology)
ANTI_PATTERNS = [
    ("Auto-generated CLAUDE.md / AGENTS.md", "Lowered task success vs. no file and raised cost 20%+ (marmelab survey)."),
    ("Prose security rules without enforcement", "4–16% of written rules had detectable enforcement across 481 CLAUDE.md files."),
    ("Letting the agent grade its own progress", "100% claimed improvement vs. 56% no-or-negative progress (Park & Choi)."),
    ("Adding a reviewer agent by default", "One reported study: −8pp on a 41% baseline; separate generator/evaluator only with external signal."),
    ("Long specialist handoff chains", ">4 handoffs almost always failed in Microsoft's Azure ops agent (via marmelab)."),
    ("Exposing every tool you have", "Removing 80% of tools raised success to 100% and cut latency ~5× (Vercel, via marmelab)."),
    ("Timestamps / mutable history in the prompt prefix", "Invalidates the KV-cache from that token on — ~10× input cost (Manus)."),
    ("Irreversible summarization", "Lost detail can't be recovered; prefer elision that keeps a path/URL (Manus, Fan et al.)."),
]

# Practical scorecard — one check per method
SCORECARD = [
    ("1", "Can you name the failure each harness component was added to fix?"),
    ("2", "Is the always-loaded instruction file under ~100 hand-written lines?"),
    ("3", "Is the prompt prefix byte-stable across turns, and is bulky tool output elided before it lands?"),
    ("4", "Could you delete a third of the tools without losing a task? (Try it.)"),
    ("5", "Does every 'done' claim pass a check the model can't fake — tests, types, a browser?"),
    ("6", "If the process dies now, can a fresh session resume from files alone?"),
    ("7", "Do sub-agents return condensed answers with `file:line` refs, in ≤4 hops?"),
    ("8", "Is every safety rule enforced by a hook or sandbox, not just written down?"),
    ("9", "Is human approval placed at the plan and at irreversible actions?"),
    ("10", "Do you have a frozen task set, and before/after numbers for your last harness change?"),
]

ADJACENT = [
    ("affaan-m/ECC", "a full meta-harness *product* — compared in the agent-harnesses report"),
    ("ruvnet/ruflo", "swarm meta-harness — agent-harnesses / agent-orchestration reports"),
    ("dair-ai/Prompt-Engineering-Guide", "prompt-level, not harness-level — see the ai-engineer-stack report"),
    ("guardrails-ai/guardrails", "output guardrails for LLM apps, not agent-loop enforcement — decision-classifiers report"),
    ("topoteretes/cognee", "long-term memory platform — agent-memory / memory-frameworks reports"),
    ("openai/codex", "a coding agent (the thing being harnessed) — ai-coding-tuis report"),
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


def short(repo):
    return repo.split("/")[-1]


def stale_note(repo):
    r = by_name.get(repo)
    if r and r.get("lifecycle_stage") in ("Declining", "Abandoned"):
        return f" _(⚠ {r['lifecycle_stage'].lower()})_"
    return ""


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
  f"{len(gr['communities'])} communities). Evidence frozen 2026-10-01.")
A(">")
A(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/harness_engineering.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)

# --- Executive summary
A("## Executive summary")
A("")
A("- The **agent-harnesses** report asks *which* harness approach to pick. This one asks "
  "*how to make any harness good* — ten methods, in the order you'd apply them, each "
  f"backed by published evidence and mapped to **{len(present)} repos** in your stars "
  f"(**{fmt_int(total_stars)}★**) that implement it.")
A("- **The through-line: the harness should do less, and verify more.** The 2026 "
  "evidence consistently rewards *subtraction* (fewer tools, shorter instructions, "
  "elided context) and *external ground truth* (tests, browsers, hooks), and punishes "
  "self-assessment and unenforced prose.")
A("- **Three highest-leverage moves**, if you do nothing else:")
A("  1. **External verification** — self-grading loops claimed progress 100% of the time "
  "while 56% of cycles made none (Park & Choi, 2026).")
A("  2. **Lean action space** — code-against-tools cut one workflow from ~150k to ~2k tokens "
  "(Anthropic); removing 80% of tools took one agent from 80% to 100% success (Vercel).")
A("  3. **Context management** — the single most important component as budgets shrink, "
  "mostly by preventing overflow failures (Fan et al., 176 configs).")
A("- **Measure your own harness.** Component effects are model- and budget-dependent, "
  "and almost no public harness repos log whether their rules fire.")
A("")

# --- Methods overview
A("## The ten methods")
A("")
A("| # | Method | The rule | Evidence |")
A("|---|---|---|---|")
for m in ORDER:
    rule, ev = METHODS[m]
    num, name = m.split(". ", 1)
    A(f"| {num} | **{name}** | {rule} | {ev} |")
A("")

# --- Ranked picks
A("## Best repo per method")
A("")
A("Top three from your stars for applying each method. ⚠ marks picks the snapshot "
  "reads as declining/abandoned.")
A("")
A("| Method | 🥇 First pick | 🥈 Second | 🥉 Third |")
A("|---|---|---|---|")
for m, picks in RANKINGS:
    cells = [f"`{short(repo)}` — {note}{stale_note(repo)}" for repo, note in picks]
    A(f"| **{m}** | {cells[0]} | {cells[1]} | {cells[2]} |")
A("")

# --- Master comparison
A("## Master comparison")
A("")
A("Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits.")
A("")
A("| Tool | Method | Lang | License | ★ Stars | Lifecycle | Health | "
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

# --- Per-method deep dives
A("## By method")
A("")
for m in ORDER:
    members = cats.get(m) or []
    if not members:
        continue
    rule, ev = METHODS[m]
    A(f"### {m}")
    A("")
    A(f"**Rule.** {rule}")
    A("")
    A(f"**Evidence.** {ev}")
    A("")
    for n in sorted(members, key=lambda x: -by_name[x]["stars"]):
        r = by_name[n]
        topics = ", ".join((r.get("topics") or [])[:8]) or "—"
        A(f"- **[{n}]({r['url']})** · {fmt_int(r['stars'])}★ · {r.get('primary_language') or '—'} · "
          f"{r.get('lifecycle_stage','—')}  ")
        A(f"  {TAXONOMY[n][1]}  ")
        A(f"  <sub>topics: {topics}</sub>")
    A("")

# --- Anti-patterns
A("## What the evidence says does *not* work")
A("")
A("| Anti-pattern | Why |")
A("|---|---|")
for pat, why in ANTI_PATTERNS:
    A(f"| {pat} | {why} |")
A("")

# --- Scorecard
A("## Harness scorecard")
A("")
A("Ten yes/no checks, one per method. A \"no\" is where to work next.")
A("")
A("| # | Check |")
A("|---|---|")
for num, check in SCORECARD:
    A(f"| {num} | {check} |")
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
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities** — harness "
  "methods draw on very different corners of the ecosystem (context tooling, sandboxes, "
  "observability, skills).")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 2:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in names))
A("")

ranked = sorted(
    [(node_for(n).get("pagerank", 0) if node_for(n) else 0, n) for n in present],
    key=lambda x: -x[0],
)
A(f"**Centrality (PageRank in the full {fmt_int(len(gr['nodes']))}-repo graph)**:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between repos in this report** (top similarity edges):")
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
A("Bus factor = commit concentration (1 = single-maintainer risk). Methods outlive "
  "tools — if a pick goes stale, the method still applies; swap the repo.")
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
watch = [n for n in present if by_name[n].get("lifecycle_stage") in ("Declining", "Abandoned")]
if watch:
    A("**Watch items** (snapshot reads declining/abandoned): "
      + ", ".join(f"`{n}`" for n in watch) + ".")
    A("")

# --- Selection guidance
A("## Where should you start?")
A("")
A("| If your harness… | Apply method | Start with |")
A("|---|---|---|")
guide = [
    ("declares success on work that's broken", "5. External verification", "`microsoft/playwright-mcp` + tests behind a hook"),
    ("burns tokens / hits context limits", "3. Context engineering", "`mksglu/context-mode` or `rtk-ai/rtk`"),
    ("picks the wrong tool or loops on tool calls", "4. Lean action space", "cut tools; `jgravelle/jcodemunch-mcp` for code reads"),
    ("ignores its CLAUDE.md", "2. Small instruction budget", "shrink it; move detail into `anthropics/skills`-style skills"),
    ("loses the thread on multi-hour tasks", "6. State on disk", "`OthmanAdi/planning-with-files`"),
    ("has done something destructive", "8. Guards & sandboxes", "`kenryu42/cc-safety-net` + `dagger/container-use`"),
    ("changed and you can't tell if it got better", "10. Observe & eval", "`harbor-framework/harbor` + `langfuse/langfuse`"),
    ("is being designed from scratch", "1. Minimal loop first", "fork `earendil-works/pi`; read `Piebald-AI/claude-code-system-prompts`"),
]
for want, method, pick in guide:
    A(f"| {want} | {method} | {pick} |")
A("")

# --- Adjacent
A("## Adjacent (deliberately not listed)")
A("")
for name, why in ADJACENT:
    r = by_name.get(name)
    star = f" ({fmt_int(r['stars'])}★)" if r else ""
    A(f"- **{name}**{star} — {why}")
A("")

# --- Methodology
A("## Methodology & sources")
A("")
A("- **Repo data**: `data/classified.json` + `public/data/graph.json`; deterministic, no "
  "API calls at generation time. Selection: keyword scan (context / compaction / tool / "
  "sandbox / guard / hook / verification / planning / durable / tracing / eval / harness) "
  "then manual curation by *the method a repo helps you apply*. Several repos also appear "
  "in the agent-harnesses report under an approach lens.")
A("- **Evidence** was gathered by web research on 2026-10-01 and is frozen in the generator "
  "— it does not refresh on rebuild. Numbers are point-in-time; several are vendor- or "
  "practitioner-reported, and some (Vercel, Microsoft, the 481-file and reviewer-agent "
  "studies, OpenAI's harness write-up) are cited **second-hand via the marmelab survey**, "
  "not from the primary source. Re-verify before quoting.")
A("- **Sources:**")
A("  - Fan et al., *An Empirical Study of Harness Design for Coding Agents*, arXiv:2609.20804 (2026-09-17) — https://arxiv.org/abs/2609.20804")
A("  - Park & Choi, *When Do Agent Loops Mistake Stagnation for Progress?*, arXiv:2607.25152 (2026-07-27, rev. 2026-09-29) — https://arxiv.org/abs/2607.25152")
A("  - marmelab, *The State of AI Harness Engineering 2026* (2026-09-24) — https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html")
A("  - HumanLayer, *Skill Issue: Harness Engineering for Coding Agents* (2026-03-12) — https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents")
A("  - Anthropic Engineering, *Code execution with MCP* (Nov 2025) — summarized at https://www.marktechpost.com/2025/11/08/anthropic-turns-mcp-agents-into-code-first-systems-with-code-execution-with-mcp-approach/")
A("  - Anthropic Engineering, *Effective harnesses for long-running agents* (Nov 2025) — summarized at https://www.zenml.io/llmops-database/long-running-agent-harness-for-multi-context-software-development")
A("  - Peak Ji (Manus), *Context Engineering for AI Agents: Lessons from Building Manus* (Jul 2025) — https://medium.com/@peakji/context-engineering-for-ai-agents-lessons-from-building-manus-71883f0a67f2")
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
    "summary": (f"Ten evidence-backed methods for building a good agent harness — minimal "
                "loops, small instruction budgets, context engineering, lean tools, external "
                "verification, state on disk, sub-agent isolation, guards, durable runs, and "
                f"harness evals — mapped to {len(present)} repos ({fmt_int(total_stars)}★)."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in ORDER},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/harness_engineering.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
