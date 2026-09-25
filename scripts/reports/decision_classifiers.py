#!/usr/bin/env python3
"""
Generate a landscape report on decision classifiers and guard models in the
starred-repos dataset: typed "System One" decision APIs (Jev), zero-shot and
few-shot classifiers, guard models and guardrail frameworks, deterministic
pre-execution policy, decision routers, calibration / uncertainty tooling, and
the incumbent "prompt an LLM into a typed answer" pattern.

Task rankings carry evidence frozen at authoring time (2026-09-25): the
Apart x CeSIA incident-sprint batteries and a Jev-Omni run in
../jev-studies/results/, plus vendor/secondary sources cited in Methodology.

Inputs:
  data/classified.json
  public/data/graph.json

Output:
  reports/decision-classifiers.md   (+ reports/decision-classifiers.meta.json)

Run: python3 scripts/reports/decision_classifiers.py
"""
import json
import os
from datetime import datetime, timezone

from lib import fmt_stars, CLASSIFIED, GRAPH, fmt_int, days_to_human, activity_label, make_node_for

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "decision-classifiers"
TITLE = "Decision Classifiers & Guard Models — Landscape Report"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy --------------------------------------------------------
TAXONOMY = {
    # Typed decision APIs ("System One" models)
    "FrancoisChastel/jev-code": ("Typed decision API", "Jev (TypeSafe's System One model) as classify / check / score / rank / ask tools inside Claude Code, Codex, Pi, OpenCode."),

    # Zero-shot encoder classifiers & extractors
    "Knowledgator/GLiClass": ("Zero-shot encoder", "GLiNER-family zero-shot text classifier — labels supplied at runtime, CPU-friendly; closest open analogue to Jev."),
    "fastino-ai/GLiNER2": ("Zero-shot encoder", "Unified schema-based extraction (entities, classification, structure) in one small encoder."),
    "urchade/GLiNER": ("Zero-shot encoder", "Generalist lightweight NER — any entity type named at runtime; the GLiNER family's origin."),

    # Few-shot / trained classifiers
    "huggingface/setfit": ("Few-shot classifier", "Few-shot classification on Sentence Transformers — 8–64 labelled examples, no prompts, fast CPU inference."),
    "pemistahl/lingua-py": ("Few-shot classifier", "Language detection that stays accurate on short and mixed-language text — a narrow, dependable classifier."),

    # Guard models & guardrail frameworks
    "ibm-granite/granite-guardian": ("Guard model / guardrails", "Open risk-detection models for prompts, responses, RAG groundedness and function calls, with probabilities."),
    "fastino-ai/GLiGuard": ("Guard model / guardrails", "Fastino's small-encoder LLM guardrail (GLiNER lineage)."),
    "NVIDIA-NeMo/Guardrails": ("Guard model / guardrails", "Programmable rails (Colang) around LLM apps; calls a model or classifier to do each check."),
    "guardrails-ai/guardrails": ("Guard model / guardrails", "Validator framework for LLM I/O — a hub of checks composed into input/output guards."),

    # Deterministic pre-execution policy
    "kenryu42/cc-safety-net": ("Deterministic policy", "Pre-execution guard for coding agents: blocks destructive git/filesystem commands by rule, before they run."),

    # Decision routers
    "aurelio-labs/semantic-router": ("Decision router", "Embedding-based decision layer — route by utterance similarity instead of an LLM call."),
    "vllm-project/semantic-router": ("Decision router", "Mixture-of-Models router for vLLM: classifies each request to pick a model, with safety filters."),
    "katanemo/plano": ("Decision router", "AI-native proxy (formerly archgw) with small built-in router and guard models at the data plane."),
    "BlockRunAI/ClawRouter": ("Decision router", "Agent-native LLM router with <1 ms local routing across frontier models."),

    # Calibration & uncertainty
    "scikit-learn-contrib/MAPIE": ("Calibration / uncertainty", "Conformal prediction and risk control — wraps any classifier's scores in coverage guarantees."),
    "cvs-health/uqlm": ("Calibration / uncertainty", "Uncertainty quantification for LLM outputs — confidence scores for hallucination detection."),

    # LLM as classifier (the incumbent pattern)
    "BoundaryML/baml": ("LLM as classifier", "Typed prompt functions — the cleanest way to force an LLM into an enum/bool/score answer."),
    "explosion/spacy-llm": ("LLM as classifier", "LLM-backed components inside spaCy pipelines (textcat, NER) — LLM classification in an NLP framework."),
    "davidfowl/tally": ("LLM as classifier", "Agents classify bank transactions — a concrete closed-label LLM-classification app."),
}

ADJACENT = [
    ("BerriAI/litellm", "gateway; can pass through to Jev but routes by config, not by decision — see *local-vs-infra-stack*"),
    ("Portkey-AI/gateway", "gateway with guardrail hooks — see *local-vs-infra-stack*"),
    ("maximhq/bifrost", "gateway with guardrails; infrastructure rather than a decision model"),
    ("confident-ai/deepteam", "red-teaming framework that *attacks* guards — see *llm-evaluation-tooling*"),
    ("KRLabsOrg/LettuceDetect", "grounding verification for RAG outputs — see *llm-evaluation-tooling*"),
    ("NVIDIA/SkillSpector", "static scanner for agent skills — audits configuration, makes no runtime decisions"),
    ("affaan-m/agentshield", "static scanner for agent configs / MCP permissions — see *ai-coding-tuis*"),
    ("huggingface/sentence-transformers", "the encoder under SetFit and semantic-router — see *rag-tooling*"),
    ("catboost/catboost", "tabular classifier — decisions over features, not over text"),
    ("google-research/tabfm", "tabular foundation model — same reason"),
    ("explosion/spaCy", "general NLP framework; its textcat is one component among many"),
    ("haizelabs/verdict", "LLM-as-judge scaling; evaluation rather than runtime decisions"),
]

# Task rankings — evidence frozen 2026-09-25. "Sprint" = Apart x CeSIA incident sprint
# (48-row authority battery, 30-case message-kind set); Jev-Omni run 20260925-102614.
TASK_RANKINGS = [
    ("Allow/block an agent tool call",
     [("kenryu42/cc-safety-net", "rules on resolved resources; the final say"),
      ("ibm-granite/granite-guardian", "open function-call risk model with probabilities (untested here)"),
      ("FrancoisChastel/jev-code", "triage and decomposition, not the oracle")],
     "Sprint: deterministic policy 48/48; Llama 3.3 70B 42/48; Jev-Omni 39/48 with 7 overblocks (cap ≤4); "
     "Qwen3 30B 37/48; GLiNER2 24/48. Without the grant every model sits at 24/48."),
    ("High-volume closed-label triage (inbox, tickets, spam)",
     [("FrancoisChastel/jev-code", "hosted, $0.042/M input, calibrated probabilities (vendor)"),
      ("Knowledgator/GLiClass", "local zero-shot, private data stays on-box"),
      ("huggingface/setfit", "best once you have 8–64 labels per class")],
     "eesel: 93% triage accuracy, 0 spam false positives on 284 chats (secondary). Not yet measured on your data."),
    ("Tell an action from a quoted action",
     [("BoundaryML/baml", "typed prompt to a 30B-class LLM"),
      ("fastino-ai/GLiNER2", "catches actions, misses quotations"),
      ("Knowledgator/GLiClass", "untested; same encoder family")],
     "Sprint, 30 cases: quotations recognised — Qwen3 30B 6/7, GLiNER2 2/7, Jev-Omni 2/7. "
     "Small classifiers read form, not intent."),
    ("Route a request to a model or agent",
     [("aurelio-labs/semantic-router", "embedding routes, near-free, local"),
      ("vllm-project/semantic-router", "classifier-based Mixture-of-Models inside vLLM"),
      ("katanemo/plano", "router models at the proxy layer")],
     "Jev routing decisions reported at 145–271 ms (KDnuggets, secondary); must beat embedding routes on "
     "criteria-defined routes to earn its API call."),
    ("Put a guarantee on a classifier's threshold",
     [("scikit-learn-contrib/MAPIE", "conformal coverage over any score"),
      ("cvs-health/uqlm", "confidence for LLM outputs"),
      ("FrancoisChastel/jev-code", "claims built-in calibration")],
     "Jev-Omni ECE 0.161 (author claims 0.040); wrong answers at 0.82–0.99 confidence. "
     "Calibration claims need a reliability diagram on your own data."),
    ("Extract the resource before deciding",
     [("fastino-ai/GLiNER2", "schema extraction in one pass"),
      ("urchade/GLiNER", "runtime entity types"),
      ("explosion/spacy-llm", "LLM-backed NER in a pipeline")],
     "Sprint: authority needs the resolved resource and the grant — extraction feeds the decision, "
     "it cannot replace it."),
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
inter_edges = [e for e in gr["links"]
               if e["source"] in sel_node_ids and e["target"] in sel_node_ids]

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
  f"`scripts/reports/decision_classifiers.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)
order = ["Typed decision API", "Zero-shot encoder", "Few-shot classifier",
         "Guard model / guardrails", "Deterministic policy", "Decision router",
         "Calibration / uncertainty", "LLM as classifier"]

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} tools** (**{fmt_int(total_stars)}★** combined) that turn text into a "
  f"decision software can act on — a label, a yes/no, a score, a route — instead of prose:")
short_counts = {}
for n in present:
    s = n.split("/")[-1].lower()
    short_counts[s] = short_counts.get(s, 0) + 1


def short(n):
    """Repo name alone, unless another tool here shares it (two semantic-routers, two guardrails)."""
    return n if short_counts[n.split("/")[-1].lower()] > 1 else n.split("/")[-1]


for c in order:
    if cats.get(c):
        A(f"  - **{c}** ({len(cats[c])}): "
          + ", ".join(f"`{short(x)}`" for x in sorted(cats[c], key=lambda x: -by_name[x]['stars'])))
A("- The newcomer is **Jev** (TypeSafe, launched 2026-09-15): a hosted model that answers typed "
  "questions with probabilities in one pass. It competes with small open encoders (GLiClass, "
  "GLiNER2) on price and latency, and with prompted LLMs (BAML-style) on consistency.")
A("- Evidence from the incident sprint: **no classifier replaces policy for authorization** — "
  "rules scored 48/48, the best model 42/48, and every model fell to 24/48 without the grant. "
  "Classifiers earn their place as triage in front of rules and humans.")
A("- **Calibration is the claim to check.** The unofficial Jev-Omni measured ECE 0.161 against a "
  "claimed 0.040. `MAPIE` puts a coverage guarantee on any of these scores.")
A("")

# --- Anatomy table
A("## Where each layer sits in a decision")
A("")
A("| Step | What happens | Tools in your stars |")
A("|---|---|---|")
A("| **Extract** | Pull the resource, argument or entity out of the text | `GLiNER2`, `GLiNER`, `spacy-llm` |")
A("| **Classify** | Answer a typed question: label, yes/no, score | `jev-code`, `GLiClass`, `setfit`, `lingua-py`, `baml` |")
A("| **Guard** | Flag risky prompts, outputs or tool calls | `granite-guardian`, `GLiGuard`, `NVIDIA-NeMo/Guardrails`, `guardrails-ai/guardrails` |")
A("| **Decide by rule** | Deterministic allow/deny on resolved facts | `cc-safety-net` |")
A("| **Route** | Pick the model, agent or path | `aurelio-labs/semantic-router`, `vllm-project/semantic-router`, `plano`, `ClawRouter` |")
A("| **Calibrate** | Turn scores into thresholds with known error rates | `MAPIE`, `uqlm` |")
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

# --- Task rankings
A("## Ranked by task")
A("")
A("Evidence frozen 2026-09-25. Sprint numbers come from runs on 48 synthetic authority "
  "fixtures and 30 message-kind cases; vendor and secondary figures are marked. "
  "Hosted Jev itself has not been run on these fixtures yet.")
A("")
A("| Task | 🥇 First pick | 🥈 Second | 🥉 Third | Evidence / note |")
A("|---|---|---|---|---|")
for task, picks, evidence in TASK_RANKINGS:
    cells = [f"`{repo.split('/')[-1]}` — {note}" for repo, note in picks]
    A(f"| **{task}** | {cells[0]} | {cells[1]} | {cells[2]} | {evidence} |")
A("")

# --- Category deep dives
A("## By category")
A("")
cat_blurb = {
    "Typed decision API": "Hosted models built for decisions rather than text: typed questions in, "
        "probabilities out, many questions per pass. Early access; 32k-token context (per review).",
    "Zero-shot encoder": "Small bidirectional encoders that take label or entity names at runtime. "
        "Local, cheap, fast — but they read surface form, so intent-level distinctions slip.",
    "Few-shot classifier": "Train on a handful of your own labels. The baseline any hosted model "
        "has to beat once labelled data exists.",
    "Guard model / guardrails": "Models that flag risk, and the frameworks that wire checks around "
        "an LLM app. Frameworks are model-agnostic: any classifier here can be the check.",
    "Deterministic policy": "Rules over resolved facts. Exact where the facts are available, "
        "blind where they are not.",
    "Decision router": "Choose the model, agent or path for a request — by embedding similarity, "
        "a routing classifier, or a proxy-level model.",
    "Calibration / uncertainty": "Make scores mean something: coverage guarantees, reliability, "
        "and confidence for LLM outputs.",
    "LLM as classifier": "The incumbent: prompt a general LLM into a typed answer. Flexible and "
        "strong on intent, but slower, costlier and less self-consistent.",
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
A("## Spotlight: where a System One model has the edge")
A("")
A("Jev's advantage is volume × closed labels × a tunable threshold, with humans or an LLM "
  "handling the uncertain middle band. Applications ranked by fit:")
A("")
A("| Application | Fit | Beats | Watch out for |")
A("|---|---|---|---|")
A("| Landscape relevance in this repo (`discover.mjs`) | strong | keyword-overlap scoring "
  "(`dotnet/runtime` scored 60+ on \"runtime\") | ~1M tokens per pass over all stars ≈ $0.04 at list price |")
A("| Inbox / reply triage | strong | prompted LLM on cost per 1,000 mails | German text, GDPR for a US API |")
A("| Coding-agent micro-decisions (CI failures, finding severity) | strong | frontier-model calls | 32k context |")
A("| Model / agent routing | plausible | embedding routes only on criteria-defined routes | embedding routes are near-free |")
A("| Tool-call guard | triage only | fast guards on latency and determinism | overblocks; quotations; needs the grant |")
A("| Private data on the Jetson | weak | — | hosted API; Jev-Omni needs ~24 GB |")
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
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities** — decision tooling "
  f"is scattered across the agent, gateway and NLP neighbourhoods rather than forming its own cluster.")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 2:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in names))
A("")

ranked = sorted(
    [(node_for(n).get("pagerank", 0) if node_for(n) else 0, n) for n in present],
    key=lambda x: -x[0],
)
A(f"**Centrality (PageRank in the full {fmt_int(len(gr['nodes']))}-repo graph):**")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between tools in this report:**")
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
A("Watch items: `jev-code` is a days-old wrapper around a closed, early-access API — the repo's "
  "health says little about the model. `GLiGuard` and `spacy-llm` read as Declining.")
A("")

# --- Selection guidance
A("## Which one should you use?")
A("")
A("| If you want… | Start with | Why |")
A("|---|---|---|")
guide = [
    ("To block dangerous agent actions", "`kenryu42/cc-safety-net` + your own policy",
     "Rules on resolved facts were the only 48/48 in the sprint."),
    ("Cheap, fast labels on text you can send out", "`FrancoisChastel/jev-code`",
     "Typed answers with probabilities; output tokens free."),
    ("The same, but data must stay local", "`Knowledgator/GLiClass`",
     "Zero-shot on CPU; no API."),
    ("A classifier trained on your own labels", "`huggingface/setfit`",
     "Few-shot, no prompts, strong baseline."),
    ("Intent-level distinctions (quoted vs real actions)", "`BoundaryML/baml` with a capable LLM",
     "Small classifiers read form; a 30B LLM got 6/7 quotations vs 2/7."),
    ("Routing between models", "`aurelio-labs/semantic-router`",
     "Local, near-free; escalate to a classifier only where routes need criteria."),
    ("A threshold with a known error rate", "`scikit-learn-contrib/MAPIE`",
     "Conformal coverage over any classifier's score."),
    ("Guard checks wired around an LLM app", "`NVIDIA-NeMo/Guardrails`",
     "Model-agnostic rails; plug in any classifier above."),
]
for want, pick, why in guide:
    A(f"| {want} | {pick} | {why} |")
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
A("## Methodology & caveats")
A("")
A("- **Source**: `data/classified.json` + `public/data/graph.json`. No external "
  "calls at generation time; fully reproducible.")
A("- **Selection**: keyword scan (classif / guard / router / calibrat / zero-shot / moderation / "
  "policy) + manual curation. Gateways, red-teaming, static scanners and tabular models were "
  "routed to adjacent reports or excluded.")
A("- **Evidence (frozen 2026-09-25)**: sprint batteries and the Jev-Omni run "
  "(`jev-studies/results/jev-omni-20260925-102614.md`; unofficial model, not TypeSafe's). "
  "Vendor: TypeSafe launch post (typesafe.ai/blog/introducing-system-one-models-and-jev) — "
  "price, latency, calibration claims. Secondary: eesel review (eesel.ai/blog/typesafe-jev-review) — "
  "93% triage, 32k context; KDnuggets (kdnuggets.com/what-everyone-is-getting-wrong-about-typesafe-ais-jev) — "
  "145–271 ms routing. Retrieved 2026-09-25.")
A("- Frozen evidence does **not** refresh with `build_index.py`; re-verify when hosted Jev "
  "results land or new guard models ship.")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may "
  "lag GitHub's current state.")
A("")
A(f"<sub>Tools covered: {len(present)} · Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta --------------------------------------------------------------
top = sorted(present, key=lambda x: -by_name[x]["stars"])[:5]
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / Evaluation",
    "summary": (f"{len(present)} tools ({fmt_int(total_stars)}★) that turn text into typed decisions: "
                "Jev, zero-shot and few-shot classifiers, guard models, policy, routers, "
                "calibration — ranked by task with sprint evidence."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in order},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/decision_classifiers.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
