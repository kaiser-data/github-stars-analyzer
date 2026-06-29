#!/usr/bin/env python3
"""
Generate a report on the repos that matter most to an AI Engineer, drawn from the
starred-repos dataset and cross-checked against the 2026 AI-engineering landscape.

Three tiers (the reader's mental model):
  - Fundamental : bedrock you must understand; base libraries + learning.
  - Must-have   : the default production toolkit you reach for on every project.
  - Trending    : where the energy is right now in 2026.

Plus the two questions an engineer actually needs answered:
  - What is "in principle solved" (commoditized — integrate, don't build)?
  - What is still frontier (worth building / where you add value)?
  - And concrete project ideas pairing these repos.

Inputs:
  public/data/classified.json
  public/data/graph.json

Output:
  reports/ai-engineer-stack.md   (+ reports/ai-engineer-stack.meta.json)

Run: python3 scripts/reports/ai_engineer_stack.py
"""
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLASSIFIED = os.path.join(ROOT, "public/data/classified.json")
GRAPH = os.path.join(ROOT, "public/data/graph.json")
SLUG = "ai-engineer-stack"
TITLE = "The AI Engineer's Stack — What's Fundamental, Must-Have, and Trending"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy: full_name -> (TIER, LAYER, blurb) ---------------------
# TIER  : Fundamental | Must-have | Trending
# LAYER : the stack layer it occupies (used for the "solved vs frontier" verdict)
F, M, T = "Fundamental", "Must-have", "Trending"
TAXONOMY = {
    # --- Fundamental: bedrock + learning ------------------------------------
    "huggingface/transformers": (F, "Base & training", "The model-definition framework — the de-facto way to load/run almost any open model. Know it cold."),
    "ggml-org/llama.cpp": (F, "Inference & serving", "Inference in C/C++ — the primitive behind on-device/edge LLMs; teaches you what quantization actually costs."),
    "Lightning-AI/pytorch-lightning": (F, "Base & training", "Structured PyTorch training — the bridge between research code and reproducible training runs."),
    "deepspeedai/DeepSpeed": (F, "Base & training", "Training-optimization library (ZeRO, offload) — how large models actually get trained on real hardware."),
    "facebookresearch/faiss": (F, "Vector store", "The original similarity-search library — the math under every vector DB; understand it before reaching for one."),
    "openai/whisper": (F, "Voice & multimodal", "The reference open ASR model — the baseline for any speech-in pipeline."),
    "rasbt/LLMs-from-scratch": (F, "Learning", "Build a GPT in PyTorch step by step — the single best way to actually understand what you're orchestrating."),
    "mlabonne/llm-course": (F, "Learning", "Roadmap + notebooks from fundamentals to deployment — the structured curriculum."),
    "dair-ai/Prompt-Engineering-Guide": (F, "Learning", "The canonical prompt-engineering reference — still load-bearing in an agentic world."),
    "karpathy/llm.c": (F, "Learning", "LLM training in raw C/CUDA — strips away the framework to show the actual compute."),
    "labmlai/annotated_deep_learning_paper_implementations": (F, "Learning", "60+ annotated paper implementations — read the architectures, don't just import them."),
    "NirDiamant/RAG_Techniques": (F, "RAG & retrieval", "A catalog of advanced RAG techniques with code — the reference when naive RAG isn't enough."),
    "microsoft/generative-ai-for-beginners": (F, "Learning", "21-lesson on-ramp to building with generative AI — the gentle starting point."),

    # --- Must-have: the production toolkit ----------------------------------
    "langchain-ai/langchain": (M, "Orchestration & agents", "The most-deployed agent/LLM framework — the lingua franca; you'll read code that uses it even if you don't."),
    "langchain-ai/langgraph": (M, "Orchestration & agents", "Explicit graphs over implicit chains — the 2026 standard for *production-grade* agent control flow."),
    "run-llama/llama_index": (M, "RAG & retrieval", "The leading data/RAG framework — connectors, indexing, query engines; the RAG default alongside LangChain."),
    "vllm-project/vllm": (M, "Inference & serving", "High-throughput serving engine (PagedAttention) — the production answer for self-hosting at scale."),
    "sgl-project/sglang": (M, "Inference & serving", "Fast serving with structured-output + prefix-cache wins — vLLM's main rival; learn both."),
    "ollama/ollama": (M, "Inference & serving", "One command to run open models locally — the dev-loop and prototyping default."),
    "mudler/LocalAI": (M, "Inference & serving", "OpenAI-compatible local engine (LLM/vision/voice) — self-host the whole API surface."),
    "BerriAI/litellm": (M, "Inference & serving", "OpenAI-compatible gateway to 100+ LLMs — swap/route/budget models from one endpoint. Non-negotiable glue."),
    "qdrant/qdrant": (M, "Vector store", "High-performance Rust vector DB — the popular standalone choice; great filtering."),
    "milvus-io/milvus": (M, "Vector store", "Cloud-native vector DB built for massive scale — when you outgrow a single box."),
    "chroma-core/chroma": (M, "Vector store", "The 'just works' embedded vector store — fastest path from zero to a working RAG."),
    "langfuse/langfuse": (M, "Eval & observability", "Open-source LLM tracing/evals/prompts — you can't ship what you can't see (you run this)."),
    "stanfordnlp/dspy": (M, "Orchestration & agents", "Program — don't prompt — LLMs; compile prompts against metrics. The antidote to prompt-spaghetti."),
    "unslothai/unsloth": (M, "Fine-tuning", "2× faster, lower-memory LoRA/QLoRA fine-tuning — the practical fine-tuning default."),
    "hiyouga/LlamaFactory": (M, "Fine-tuning", "Unified fine-tuning UI/CLI for 100+ models — the no-code-ish path to a tuned model."),
    "huggingface/smolagents": (M, "Orchestration & agents", "Barebones code-writing agents — the minimal mental model of what an agent loop *is*."),
    "crewAIInc/crewAI": (M, "Orchestration & agents", "Role-playing multi-agent orchestration — the popular 'team of agents' framework."),
    "firecrawl/firecrawl": (M, "Data & ingestion", "Search/scrape/crawl the web into LLM-ready data — the ingestion default for RAG & agents."),
    "unclecode/crawl4ai": (M, "Data & ingestion", "LLM-friendly open crawler/scraper — self-hosted ingestion when you don't want an API."),
    "infiniflow/ragflow": (M, "RAG & retrieval", "Batteries-included RAG engine with deep document understanding — RAG as a deployable product."),

    # --- Trending: where the energy is in 2026 ------------------------------
    "anthropics/claude-code": (T, "Coding agents & MCP", "The agentic coding CLI — the flagship of the coding-agent wave (full ecosystem in the cc-setups report)."),
    "modelcontextprotocol/servers": (T, "Coding agents & MCP", "Reference MCP servers — MCP is the emerging standard for wiring tools/data into any agent."),
    "punkpeye/awesome-mcp-servers": (T, "Coding agents & MCP", "The community MCP index — discovery for the fastest-growing integration ecosystem."),
    "anthropics/skills": (T, "Coding agents & MCP", "Agent Skills — on-demand capability that's displacing always-on prompt bloat."),
    "obra/superpowers": (T, "Coding agents & MCP", "The headline agentic-skills framework — the most-starred repo in this whole set."),
    "browser-use/browser-use": (T, "Orchestration & agents", "Let agents drive real browsers — the computer-use frontier; high promise, still flaky."),
    "vercel-labs/agent-browser": (T, "Orchestration & agents", "Browser-automation CLI for agents — the lighter, scriptable take on web agents."),
    "microsoft/playwright-mcp": (T, "Coding agents & MCP", "Playwright as an MCP server — reliable, structured web control for agents."),
    "github/spec-kit": (T, "Coding agents & MCP", "Spec-driven development toolkit — the 'write the spec, let the agent build' workflow."),
    "OpenHands/OpenHands": (T, "Coding agents & MCP", "Open autonomous software-engineering agent — the OSS face of the SWE-agent race."),
    "google-gemini/gemini-cli": (T, "Coding agents & MCP", "Gemini's terminal agent — the third major CLI harness; useful for model-shopping."),
    "Aider-AI/aider": (T, "Coding agents & MCP", "AI pair-programming in the terminal with tight git integration — a beloved daily driver."),
    "mem0ai/mem0": (T, "Memory", "Universal memory layer for agents — the most-adopted bet on the unsolved memory problem."),
    "MemPalace/mempalace": (T, "Memory", "Best-benchmarked open memory system — a strong contender in a still-open race."),
    "HKUDS/LightRAG": (T, "RAG & retrieval", "Graph-augmented RAG that's simple and fast — the practical face of 'RAG beyond chunks'."),
    "microsoft/graphrag": (T, "RAG & retrieval", "Graph-based RAG — structure-aware retrieval for global/whole-corpus questions."),
    "VectifyAI/PageIndex": (T, "RAG & retrieval", "Vectorless, reasoning-based retrieval — a bet that reasoning can replace embeddings."),
    "google/langextract": (T, "Data & ingestion", "Structured extraction from unstructured text — turning documents into typed data."),
    "bytedance/deer-flow": (T, "Orchestration & agents", "Long-horizon research+code SuperAgent — the 'deep research' pattern as a harness."),
    "agno-agi/agno": (T, "Orchestration & agents", "Build/run/manage agent platforms — a fast-rising full-stack agent framework."),
    "comet-ml/opik": (T, "Eval & observability", "Eval-first LLM/agent observability — measuring agents, not just logging them."),
    "Arize-ai/phoenix": (T, "Eval & observability", "OpenTelemetry-based AI observability & eval — standards-based tracing for agents."),
    "TauricResearch/TradingAgents": (T, "Orchestration & agents", "Multi-agent trading framework — the template for *vertical* agent systems with real domain logic."),
}

# Solved-status verdict per layer (the analytical core)
SOLVED = {
    "Inference & serving": ("✅ Solved", "vLLM / SGLang / Ollama / llama.cpp cover edge→datacenter. Never write your own serving layer; pick by scale."),
    "Vector store": ("✅ Solved", "faiss/qdrant/milvus/chroma (+pgvector) are mature. Choose on ops + filtering needs, not capability."),
    "Base & training": ("✅ Solved (for users)", "HF Transformers + PyTorch are the substrate. Training *frontier* models isn't your job; using them is."),
    "Fine-tuning": ("🟢 Mechanics solved", "LoRA/QLoRA via unsloth/LlamaFactory is push-button. The real skill is knowing *when* to fine-tune vs RAG vs prompt."),
    "RAG & retrieval": ("🟡 Split", "Naive RAG (chunk→embed→retrieve→stuff) is commoditized. Advanced/agentic/graph retrieval (LightRAG, graphrag, PageIndex) is still frontier."),
    "Data & ingestion": ("🟡 Tooling solved", "Crawling/OCR/extraction (firecrawl, crawl4ai, langextract) is solved. *Clean domain data* is still the real bottleneck."),
    "Eval & observability": ("🟡 Split", "Tracing is solved (langfuse/phoenix). Agent *evaluation* is frontier — SWE-bench is saturated; reliable eval harnesses are unsolved."),
    "Orchestration & agents": ("🔴 Frontier", "Frameworks are mature (langgraph). Reliable long-horizon autonomy is NOT — open agents trail humans badly on real workflows."),
    "Memory": ("🔴 Open problem", "mem0/mempalace are bets, not settled answers. Durable, selective, cheap long-term memory is unsolved."),
    "Coding agents & MCP": ("🔴 Trending / unstable", "Exploding fast; MCP is becoming the integration standard but the surface changes monthly. Learn now, expect churn."),
    "Voice & multimodal": ("🟡 Split", "STT/TTS are solved (whisper et al.). Low-latency full-duplex voice agents are still hard — see the voice-agents report."),
    "Learning": ("📚 Reference", "Bedrock knowledge — these don't go stale the way tools do."),
}

# Buildable projects pairing the repos
PROJECTS = [
    ("RAG assistant over your own docs", "llama_index + qdrant + litellm + langfuse (+ a reranker)",
     "Solved territory", "Beginner", "Best first portfolio project. Everything exists — the value is doing retrieval quality + evals properly."),
    ("Local-first private ChatGPT", "ollama + open-webui + chroma + whisper",
     "Solved territory", "Beginner", "Cost/privacy play. 100% offline. Great for learning the full loop with zero API spend."),
    ("Document → structured data pipeline", "firecrawl/MinerU + langextract + a vector store",
     "Solved territory", "Intermediate", "High business value, low novelty risk. Turns messy PDFs/web into typed records."),
    ("Agentic research assistant", "langgraph + browser-use + firecrawl + mem0 + langfuse",
     "Frontier", "Intermediate", "The hard part is *reliability*, not wiring. This is where you differentiate."),
    ("Graph-RAG knowledge base", "microsoft/graphrag or LightRAG + qdrant",
     "Frontier", "Intermediate", "For global/whole-corpus questions naive RAG fails. Active research — a real edge if you nail it."),
    ("Domain copilot with a tuned model", "unsloth (QLoRA) + llama_index RAG + opik evals",
     "Mixed", "Advanced", "Decide fine-tune-vs-RAG with evidence (opik). The decision *is* the skill."),
    ("Vertical multi-agent system", "crewAI/langgraph + TauricResearch/TradingAgents as a template + langfuse",
     "Frontier", "Advanced", "Real domain logic + many agents = the highest-value, highest-difficulty class of project."),
    ("Coding agent / dev tool", "claude-code + MCP servers (playwright-mcp, github-mcp) + codegraph",
     "Trending", "Intermediate", "Build a tool for your own workflow. See the Claude-Code-setups report for the full ecosystem."),
    ("Your own agent-eval harness", "phoenix/opik + a task suite + langgraph runner",
     "Frontier", "Advanced", "Few good ones exist. Building trustworthy agent evals is genuinely unsolved — and very employable."),
]

ADJACENT = [
    ("Comfy-Org/ComfyUI", "image/diffusion tooling — a different (creative) AI discipline, out of scope here"),
    ("PaddlePaddle/PaddleOCR", "OCR engine — a data-ingestion building block, folded into 'Data & ingestion'"),
    ("n8n-io/n8n", "workflow automation — orchestrates agents but isn't core AI-eng tooling (see agent-orchestration report)"),
    ("microsoft/autogen", "multi-agent framework — slipping in activity; crewAI/langgraph lead the must-have slot now"),
    ("nomic-ai/gpt4all", "local-LLM app — superseded for most by ollama; kept off the must-have list"),
]

TIER_ORDER = [F, M, T]
LAYER_ORDER = ["Base & training", "Inference & serving", "Vector store", "RAG & retrieval",
               "Orchestration & agents", "Memory", "Eval & observability", "Fine-tuning",
               "Data & ingestion", "Coding agents & MCP", "Voice & multimodal", "Learning"]

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

def trend_score(r):
    """Dataset-derived momentum signal."""
    s = 0.0
    if (r.get("lifecycle_stage") or "") == "Hot":
        s += 3
    if (r.get("lifecycle_stage") or "") == "Rising":
        s += 2
    age = r.get("age_days") or 9999
    c90 = r.get("commits_90d") or 0
    dsp = r.get("days_since_push")
    dsp = 999 if dsp is None else dsp
    if age < 400:
        s += 2
    if c90 >= 50 and dsp <= 14:
        s += 2
    elif c90 >= 20 and dsp <= 30:
        s += 1
    return s

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
  f"{len(gr['communities'])} communities) and the 2026 AI-engineering landscape.")
A(">")
A(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/ai_engineer_stack.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
tiers = {F: [], M: [], T: []}
layers = {}
for n in present:
    tier, layer, _ = TAXONOMY[n]
    tiers[tier].append(n)
    layers.setdefault(layer, []).append(n)

# --- The thesis
A("## The one thing to understand first")
A("")
A("In 2026 the **model layer is commoditizing** — model differences matter less each quarter, "
  "and the infrastructure beneath your app (serving, vector search, basic RAG, tracing) is "
  "**largely solved**. The value has moved *up the stack*: to **reliability, evaluation, "
  "context engineering, and memory** for agentic systems. So this report does two jobs at "
  "once — it tells you **which repos to know** (Fundamental / Must-have / Trending) *and* "
  "**which problems are already solved** (integrate, don't rebuild) **vs. still frontier** "
  "(where you actually add value).")
A("")
A("> **Rule of thumb:** if a capability is ✅ *Solved* below, your job is to *integrate the "
  "best repo well*. If it's 🔴 *Frontier*, that's where a portfolio project or a job actually "
  "gets you noticed.")
A("")

# --- The three tiers (headline)
A("## The three tiers")
A("")
tier_intro = {
    F: "**Bedrock you must understand.** Long-lived base libraries and learning resources. "
       "Tools change; these don't. If you can't explain these, you're assembling black boxes.",
    M: "**Your default production toolkit.** The repos you reach for on basically every "
       "project — the boring, load-bearing choices. Master integration, not novelty.",
    T: "**Where the energy is right now (2026).** Fast-moving, high-upside, often unstable. "
       "Learn these to stay current and to find differentiated things to build.",
}
for tier in TIER_ORDER:
    members = sorted(tiers[tier], key=lambda x: -by_name[x]["stars"])
    A(f"### {tier} ({len(members)})")
    A("")
    A(tier_intro[tier])
    A("")
    for n in members:
        r = by_name[n]
        A(f"- **[{n}]({r['url']})** · {fmt_int(r['stars'])}★ · _{TAXONOMY[n][1]}_  ")
        A(f"  {TAXONOMY[n][2]}")
    A("")

# --- Solved vs frontier (the analytical core)
A("## What's solved vs. what's still frontier")
A("")
A("The most useful map an AI engineer can carry: where to **stop building and integrate**, "
  "and where **building is still worth it**.")
A("")
A("| Layer | Status | What that means for you | Your repos here |")
A("|---|---|---|---|")
for layer in LAYER_ORDER:
    if layer not in SOLVED:
        continue
    status, meaning = SOLVED[layer]
    members = layers.get(layer, [])
    picks = ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(members, key=lambda x: -by_name[x]['stars'])[:5]) or "—"
    A(f"| **{layer}** | {status} | {meaning} | {picks} |")
A("")
A("**The short version:**")
A("")
A("- ✅ **Solved — integrate, never rebuild:** inference & serving, vector search, the base "
  "model/runtime layer. Picking *well* is the skill; building it yourself is wasted effort.")
A("- 🟡 **Split — solved at the bottom, frontier at the top:** RAG (naive=solved, "
  "graph/agentic=open), evaluation (tracing=solved, agent-evals=open), data (tools=solved, "
  "clean domain data=hard).")
A("- 🔴 **Frontier — where to actually add value:** agent reliability & long-horizon "
  "autonomy, durable memory, trustworthy agent evaluation, and the still-churning "
  "coding-agent / MCP ecosystem. Open agents still trail humans badly on real-world workflows "
  "— that gap *is* the opportunity.")
A("")

# --- What people are actually building
A("## What people are actually building right now")
A("")
A("By 2026 a majority of organizations have agents in production. The application types that "
  "dominate, most-built first:")
A("")
A("1. **RAG over private/domain data** — still the single most common production pattern. "
   "The bar has risen from 'it answers' to 'it answers *with good retrieval + evals*'.")
A("2. **Task & research agents** — `langgraph`-style explicit-graph agents with tools, "
   "web access (`browser-use`/`firecrawl`), and memory (`mem0`).")
A("3. **Coding agents & dev tools** — `claude-code`/`aider`/`OpenHands` + **MCP** servers; "
   "the fastest-growing category (full breakdown in the Claude-Code-setups report).")
A("4. **Voice agents** — speech-in/speech-out; low latency is the moat (see voice-agents report).")
A("5. **Vertical agent systems** — domain logic + multi-agent (e.g. `TradingAgents`); the "
   "highest-value, highest-difficulty class.")
A("")

# --- Trending right now (dataset signal)
A("### Trending right now (by dataset momentum)")
A("")
A("Ranked by a momentum signal (Hot/Rising lifecycle + recent age + 90-day commit velocity). "
  "This is *velocity*, not size — small fast-movers beat large mature repos here.")
A("")
A("| Repo | Tier | ★ Stars | Age | 90d commits | Last push | Momentum |")
A("|---|---|---|---|---|---|---|")
for n in sorted(present, key=lambda x: (-trend_score(by_name[x]), -by_name[x]["stars"]))[:15]:
    r = by_name[n]
    A("| [{n}]({u}) | {tier} | {s} | {age} | {c90} | {push} | {ts:.0f} |".format(
        n=n, u=r["url"], tier=TAXONOMY[n][0], s=fmt_int(r["stars"]),
        age=days_to_human(r.get("age_days")), c90=r.get("commits_90d", "—"),
        push=days_to_human(r.get("days_since_push")) + " ago", ts=trend_score(r)))
A("")

# --- Project suggestions
A("## Projects to build (with the repos)")
A("")
A("Tagged by *territory* — **Solved** = ship fast, low risk, great for a portfolio; "
  "**Frontier** = harder, but where you differentiate.")
A("")
A("| Project | Stack | Territory | Level | Notes |")
A("|---|---|---|---|---|")
for name, stack, terr, level, notes in PROJECTS:
    A(f"| **{name}** | {stack} | {terr} | {level} | {notes} |")
A("")

# --- Master comparison
A("## Master comparison")
A("")
A("Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits.")
A("")
A("| Repo | Tier | Layer | Lang | ★ Stars | Lifecycle | Health | Activity | Last push | Age |")
A("|" + "---|" * 10)
for n in sorted(present, key=lambda x: -by_name[x]["stars"]):
    r = by_name[n]
    A("| [{name}]({url}) | {tier} | {layer} | {lang} | {stars} | {lc} | {hs} | {act} | {push} | {age} |".format(
        name=n, url=r["url"], tier=TAXONOMY[n][0], layer=TAXONOMY[n][1],
        lang=r.get("primary_language") or "—",
        stars=fmt_int(r["stars"]),
        lc=r.get("lifecycle_stage") or "—",
        hs=r.get("health_score") if r.get("health_score") is not None else "—",
        act=activity_label(r),
        push=days_to_human(r.get("days_since_push")) + " ago",
        age=days_to_human(r.get("age_days")),
    ))
A("")

# --- Graph analysis
A("## Graph analysis — how they relate")
A("")
comm = {}
for n in present:
    nd = node_for(n)
    if nd is not None:
        comm.setdefault(nd.get("community"), []).append(n)
A(f"**Community clustering.** These {len(present)} repos span "
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities** — the AI-engineering "
  f"stack is genuinely cross-cutting, not one tidy neighborhood.")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 3:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in sorted(names, key=lambda x:-by_name[x]['stars'])[:10]))
A("")
ranked = sorted(
    [(node_for(n).get("pagerank", 0) if node_for(n) else 0, n) for n in present],
    key=lambda x: -x[0],
)
A(f"**Centrality (PageRank in the full {fmt_int(len(gr['nodes']))}-repo graph)** — the most "
  "'hub-like' AI-eng repos in your stars (good signal for *foundational*):")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f} ({TAXONOMY[n][0]})")
A("")

# --- Maintenance / risk
A("## Maintenance & risk signal")
A("")
A("Bus factor = commit concentration (1 = single-maintainer risk). For *production* picks, "
  "prefer mature lifecycle + low single-author share; for *trending* picks, expect churn.")
A("")
A("| Repo | Tier | Health | Lifecycle | Activity | Bus factor | Top-author share |")
A("|---|---|---|---|---|---|---|")
for n in sorted(present, key=lambda x: -(by_name[x].get("health_score") or 0)):
    r = by_name[n]
    tas = r.get("top_author_share")
    A("| {n} | {tier} | {h} | {lc} | {act} | {bf} | {tas} |".format(
        n=n, tier=TAXONOMY[n][0], h=r.get("health_score", "—"), lc=r.get("lifecycle_stage", "—"),
        act=activity_label(r), bf=r.get("bus_factor", "—"),
        tas=f"{tas:.0%}" if isinstance(tas, (int, float)) else "—"))
A("")

# --- Adjacent
A("## Adjacent (deliberately not in the core list)")
A("")
for name, why in ADJACENT:
    r = by_name.get(name)
    star = f" ({fmt_int(r['stars'])}★)" if r else ""
    A(f"- **{name}**{star} — {why}")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `public/data/classified.json` + `public/data/graph.json`, cross-checked "
  "against 2026 AI-engineering landscape reporting. No private calls; fully reproducible.")
A("- **Tiers and the solved/frontier verdicts are opinionated** — a synthesis of dataset "
  "signal (stars, lifecycle, commit velocity) and the current state of the field, not a "
  "benchmark. Treat 'Trending' as *volatile by definition*.")
A("- **Selection** favors recognizable, broadly-applicable AI-engineering tooling. The "
  "coding-agent/harness ecosystem and voice stack are summarized here but detailed in the "
  "Claude-Code-setups and voice-agents reports respectively.")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may "
  "lag GitHub's current state.")
A("")
A(f"<sub>Repos covered: {len(present)} · Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta -------------------------------------------------------------
top = sorted(present, key=lambda x: -by_name[x]["stars"])[:5]
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / Engineering",
    "summary": (f"{len(present)} repos every AI engineer should know ({fmt_int(total_stars)}★), "
                f"sorted into Fundamental / Must-have / Trending — plus a map of what's already "
                "solved (integrate, don't build) vs. still frontier, and 9 buildable project ideas."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {t: len(tiers[t]) for t in TIER_ORDER},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/ai_engineer_stack.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  repos: {len(present)} / {len(sel_names)} curated  "
      f"(Fundamental={len(tiers[F])}, Must-have={len(tiers[M])}, Trending={len(tiers[T])})")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
