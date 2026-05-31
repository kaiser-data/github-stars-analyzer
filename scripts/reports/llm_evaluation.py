#!/usr/bin/env python3
"""
Generate a comprehensive report on LLM *evaluation* tooling found in the
starred-repos dataset: eval/observability platforms, evaluation frameworks,
benchmarks/leaderboards, and safety / red-teaming / hallucination detection.

Inputs:
  public/data/classified.json   (full repo metadata)
  public/data/graph.json        (repo-similarity graph: communities, pagerank, edges)

Output:
  reports/llm-evaluation-tooling.md

Run: python3 scripts/reports/llm_evaluation.py
"""
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLASSIFIED = os.path.join(ROOT, "public/data/classified.json")
GRAPH = os.path.join(ROOT, "public/data/graph.json")
OUT = os.path.join(ROOT, "reports/llm-evaluation-tooling.md")

# ---- Curated taxonomy (derived from scanning all 1071 repos) -----------------
# full_name -> (category, approach note)
TAXONOMY = {
    # Observability + eval platforms (tracing, datasets, online + offline eval)
    "langfuse/langfuse": ("Observability + eval platform", "LLM observability, metrics, evals, prompt management, datasets & playground; the most-adopted OSS platform here."),
    "mlflow/mlflow": ("Observability + eval platform", "Broad AI engineering platform; LLM tracing + evaluate + experiment tracking on top of classic MLOps."),
    "comet-ml/opik": ("Observability + eval platform", "Debug / evaluate / monitor LLM, RAG & agentic apps with tracing + automated scoring."),
    "traceloop/openllmetry": ("Observability + eval platform", "OpenTelemetry-native GenAI observability; standards-based traces & metrics."),
    "comet-ml/opik-openclaw": ("Observability + eval platform", "Opik plugin that exports OpenClaw agent traces (cost/tokens/errors) for monitoring."),

    # Evaluation frameworks (offline scoring, LLM-as-judge, metric libraries)
    "confident-ai/deepeval": ("Evaluation framework", "'The LLM eval framework' — pytest-style unit tests with metrics (faithfulness, relevancy, G-Eval/LLM-as-judge)."),
    "langchain-ai/openevals": ("Evaluation framework", "Readymade evaluators (prebuilt prompts + scorers) for LLM apps."),
    "langchain-ai/agentevals": ("Evaluation framework", "Evaluators specialized for agent *trajectories* (tool-call sequences, not just final output)."),
    "rhesis-ai/rhesis": ("Evaluation framework", "Testing platform that lets engineers + PMs + domain experts generate and run test suites."),

    # Benchmarks & leaderboards (fixed task sets, model ranking)
    "LiveBench/LiveBench": ("Benchmark / leaderboard", "Challenging, contamination-free benchmark refreshed over time to resist training-set leakage."),
    "pinchbench/skill": ("Benchmark / leaderboard", "Benchmarks LLMs as OpenClaw *coding agents* on real tasks."),
    "vllm-project/guidellm": ("Benchmark / leaderboard", "Performance/inference benchmark: evaluate LLM *deployments* for real-world throughput/latency."),
    "finos-labs/Open-Financial-LLMs-Leaderboard": ("Benchmark / leaderboard", "Domain leaderboard ranking LLMs on financial tasks."),
    "jszheng21/RACE": ("Benchmark / leaderboard", "Multi-dimensional code-generation benchmark (Readability, Maintainability, Correctness, Efficiency)."),

    # Safety / red-teaming / hallucination detection
    "NVIDIA/garak": ("Safety / red-team", "LLM vulnerability scanner — probes for jailbreaks, prompt injection, toxicity, data leakage."),
    "confident-ai/deepteam": ("Safety / red-team", "Framework to red-team LLMs & LLM systems (adversarial attack suites, from the DeepEval team)."),
    "cvs-health/uqlm": ("Safety / red-team", "Uncertainty quantification for LLMs; UQ-based hallucination detection."),
    "KRLabsOrg/LettuceDetect": ("Safety / red-team", "Lightweight hallucination-detection framework for RAG outputs."),
}

# Canonical tools NOT in this user's stars — for honest landscape context.
NOTABLY_ABSENT = [
    ("explodinggradients/ragas", "the standard RAG evaluation metric library"),
    ("promptfoo/promptfoo", "popular CLI for prompt/eval testing & red-teaming"),
    ("openai/evals", "OpenAI's eval registry/framework"),
    ("EleutherAI/lm-evaluation-harness", "de-facto academic benchmark harness"),
    ("Arize-ai/phoenix", "open-source LLM tracing & eval"),
    ("huggingface/lighteval", "HF's lightweight eval suite"),
    ("stanford-crfm/helm", "holistic benchmark from Stanford"),
    ("truera/trulens", "feedback-function evaluation"),
]

# ---- Load data ---------------------------------------------------------------
with open(CLASSIFIED) as f:
    cl = json.load(f)
with open(GRAPH) as f:
    gr = json.load(f)

by_name = {r["full_name"]: r for r in cl["repos"]}
nodes_by_id = {n["id"]: n for n in gr["nodes"]}
name_to_nodeid = {n["full_name"]: n["id"] for n in gr["nodes"]}

sel_names = list(TAXONOMY.keys())
sel_node_ids = {name_to_nodeid[n] for n in sel_names if n in name_to_nodeid}

inter_edges = []
for link in gr["links"]:
    if link["source"] in sel_node_ids and link["target"] in sel_node_ids:
        inter_edges.append(link)

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

A("# LLM Evaluation Tooling — Landscape Report")
A("")
A(f"> Derived from **{user}**'s {fmt_int(cl['total'])} starred repos "
  f"(snapshot `{gen}`), cross-referenced with the repo-similarity graph "
  f"({fmt_int(len(gr['nodes']))} nodes / {fmt_int(len(gr['links']))} edges, "
  f"{len(gr['communities'])} communities).")
A(">")
A(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/llm_evaluation.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} evaluation-focused tools** found in your stars "
  f"(**{fmt_int(total_stars)}★** combined), spanning four categories:")
order = ["Observability + eval platform", "Evaluation framework",
         "Benchmark / leaderboard", "Safety / red-team"]
for c in order:
    if cats.get(c):
        A(f"  - **{c}** ({len(cats[c])}): "
          + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(cats[c], key=lambda x: -by_name[x]['stars'])))
A(f"- The field splits cleanly into **online** evaluation (tracing/observability in "
  f"production) and **offline** evaluation (datasets, metrics, benchmarks before ship). "
  f"Platforms increasingly do both.")
A(f"- Evaluation method has converged on **LLM-as-a-judge** (deepeval, openevals) "
  f"alongside classic reference metrics, plus a fast-growing **safety/red-team** wing "
  f"(garak, deepteam) and **hallucination detection** (uqlm, LettuceDetect).")
A(f"- Python dominates ({sum(1 for n in present if by_name[n].get('primary_language')=='Python')}/"
  f"{len(present)}); the lone TypeScript-first platform is Langfuse.")
A("")

# --- Master comparison
A("## Master comparison")
A("")
A("Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits.")
A("")
A("| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | "
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
    "Observability + eval platform": "Capture traces from live LLM apps, attach scores, "
        "manage prompts & datasets. Online-first, but most now run offline eval suites too.",
    "Evaluation framework": "Libraries to score outputs offline — reference metrics + "
        "LLM-as-a-judge — wired into CI like unit tests.",
    "Benchmark / leaderboard": "Fixed task sets that rank models/agents. Watch for "
        "contamination (LiveBench is explicitly designed against it).",
    "Safety / red-team": "Adversarial testing, vulnerability scanning, and hallucination / "
        "uncertainty detection — evaluating *failure modes* rather than task accuracy.",
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

# --- Online vs offline framing
A("## Online vs. offline evaluation")
A("")
A("| | What it measures | Tools in your stars |")
A("|---|---|---|")
A("| **Online** (production) | Live traces, cost/latency, drift, real-user feedback | "
  "`langfuse`, `mlflow`, `opik`, `openllmetry`, `opik-openclaw` |")
A("| **Offline** (pre-ship) | Metric scores on datasets, regression gates in CI | "
  "`deepeval`, `openevals`, `agentevals`, `rhesis` |")
A("| **Comparative** (ranking) | Model/agent leaderboards on fixed tasks | "
  "`LiveBench`, `pinchbench`, `guidellm`, `RACE`, `Open-Financial-LLMs-Leaderboard` |")
A("| **Adversarial** (safety) | Jailbreaks, injection, hallucination, uncertainty | "
  "`garak`, `deepteam`, `uqlm`, `LettuceDetect` |")
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
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities** — evaluation "
  f"tooling co-locates with the broader LLM-app / agent-infra clusters rather than "
  f"forming an isolated island.")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 2:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in names))
A("")

ranked = sorted(
    [(node_for(n).get("pagerank", 0) if node_for(n) else 0, n) for n in present],
    key=lambda x: -x[0],
)
A("**Centrality (PageRank in the full 1,071-repo graph)** — how 'hub-like' each tool "
  "is within your starred ecosystem:")
A("")
for pr, n in ranked[:8]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between eval tools** (similarity edges where both endpoints are in "
  "this report):")
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
    A("- _None_ — these tools don't share authors/topics directly in the graph; each "
      "links out to the LLM-app repos it instruments rather than to its competitors.")
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

# --- Selection guidance
A("## Which one should you use?")
A("")
A("| If you want… | Start with | Why |")
A("|---|---|---|")
guide = [
    ("End-to-end observability + evals for a production app", "`langfuse/langfuse`",
     "Most-starred OSS platform here; tracing + evals + prompt mgmt + datasets, TS-friendly."),
    ("Offline eval as CI unit tests (LLM-as-judge)", "`confident-ai/deepeval`",
     "Pytest-style metrics (faithfulness, relevancy, G-Eval); largest dedicated framework."),
    ("To evaluate agent *trajectories*, not just answers", "`langchain-ai/agentevals`",
     "Scores tool-call sequences / multi-step behavior."),
    ("Standards-based tracing (vendor-neutral)", "`traceloop/openllmetry`",
     "Built on OpenTelemetry; plugs into existing observability stacks."),
    ("To red-team / security-scan a model", "`NVIDIA/garak` + `confident-ai/deepteam`",
     "garak = vulnerability scanner; deepteam = adversarial attack framework."),
    ("Hallucination / uncertainty detection", "`cvs-health/uqlm` or `KRLabsOrg/LettuceDetect`",
     "UQ-based detection; LettuceDetect targets RAG outputs specifically."),
    ("A contamination-resistant model leaderboard", "`LiveBench/LiveBench`",
     "Refreshed tasks designed to resist training-set leakage."),
    ("To benchmark coding agents", "`pinchbench/skill`",
     "Runs LLMs as coding agents on real tasks."),
]
for want, pick, why in guide:
    A(f"| {want} | {pick} | {why} |")
A("")

# --- Notably absent
A("## Notably absent from your stars")
A("")
A("Several widely-used evaluation tools are **not** in this dataset — worth knowing "
  "when treating the above as a complete picture:")
A("")
for name, what in NOTABLY_ABSENT:
    A(f"- **{name}** — {what}")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external "
  "calls; fully reproducible via the generator script.")
A("- **Selection**: keyword scan (eval/benchmark/leaderboard/red-team/guardrail/"
  "observability/hallucination + LLM/agent signals) across name/description/topics/README, "
  "then manual curation. Adjacent-but-excluded: RAG engines, vector DBs, LLM gateways "
  "(e.g. `litellm`), and agent frameworks that merely *embed* an eval module.")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and "
  "may lag GitHub's current state.")
A("- Re-run after a fresh `classified.json` to refresh stars/activity.")
A("")
A(f"<sub>Tools covered: {len(present)} · Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta (consumed by build_reports_index.py) ------------------------
_top = sorted(present, key=lambda x: -by_name[x]["stars"])[:5]
meta = {
    "slug": "llm-evaluation-tooling",
    "title": "LLM Evaluation Tooling — Landscape Report",
    "file": "llm-evaluation-tooling.md",
    "category": "AI / Evaluation",
    "summary": (f"{len(present)} LLM evaluation tools ({fmt_int(total_stars)}★): "
                "observability+eval platforms, eval frameworks, benchmarks/leaderboards, "
                "and safety/red-team — framed online vs. offline."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in order},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in _top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/llm_evaluation.py",
}
with open(os.path.join(ROOT, "reports/llm-evaluation-tooling.meta.json"), "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing from dataset:", missing)
