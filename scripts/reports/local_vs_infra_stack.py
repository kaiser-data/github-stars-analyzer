#!/usr/bin/env python3
"""
Generate a deployment-tier comparison of the local-LLM / AI stack found in the
starred-repos dataset. For every layer of the stack (inference runtime, scaling
infra, gateway/UI, vector store, fine-tuning, agent framework, observability) it
classifies each tool by deployment tier — Local/edge, Scales-both, or
High-infra — and assembles two concrete reference stacks: one fully local, one
production-scale.

Inputs:
  data/classified.json
  public/data/graph.json

Output:
  reports/local-vs-infra-stack.md   (+ .meta.json)

Run: python3 scripts/reports/local_vs_infra_stack.py
"""
import json
import os
from datetime import datetime, timezone

from lib import fmt_stars, CLASSIFIED, GRAPH, fmt_int, days_to_human, activity_label, make_node_for

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "local-vs-infra-stack"
TITLE = "Local vs High-Infra AI Stack — A Deployment-Tier Comparison"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# Deployment tiers
LOCAL = "Local / edge"        # laptop, single consumer GPU, on-device, zero ops
BOTH = "Scales both"          # same tool runs local or cluster, config-dependent
INFRA = "High-infra"          # multi-GPU / datacenter / high-QPS / k8s

# ---- Curated taxonomy: name -> (layer, tier, blurb) --------------------------
TAXONOMY = {
    # --- Inference runtime — actually run the model -----------------------------
    "ollama/ollama": ("Inference runtime", LOCAL,
        "The zero-config local default — `ollama run`, model registry, OpenAI-compatible API. Laptop-to-server, but single-node."),
    "ggml-org/llama.cpp": ("Inference runtime", LOCAL,
        "The CPU/edge engine under everything — GGUF quantization, runs on a Raspberry Pi to a Mac; the embeddable substrate."),
    "mozilla-ai/llamafile": ("Inference runtime", LOCAL,
        "One file = one runnable model. Maximum portability for shipping a local model with no install."),
    "mudler/LocalAI": ("Inference runtime", LOCAL,
        "Self-hosted, OpenAI-drop-in engine for LLM/TTS/STT/image on commodity hardware — the all-in-one local server."),
    "nomic-ai/gpt4all": ("Inference runtime", LOCAL,
        "Desktop-first local LLM app + bindings; privacy-focused, runs on plain CPUs."),
    "microsoft/foundry-local": ("Inference runtime", LOCAL,
        "Microsoft's on-device runtime — offline LLM + Whisper, hardware-accelerated where available."),
    "vllm-project/vllm": ("Inference runtime", INFRA,
        "The production serving standard — PagedAttention, continuous batching, tensor/pipeline parallelism for high QPS on GPU fleets."),
    "sgl-project/sglang": ("Inference runtime", INFRA,
        "High-throughput serving with RadixAttention prefix caching — excels at structured/agentic workloads at scale."),
    "InternLM/lmdeploy": ("Inference runtime", INFRA,
        "Toolkit for compressing + serving LLMs at scale (TurboMind engine); quantization-aware high-throughput inference."),
    "exo-explore/exo": ("Inference runtime", BOTH,
        "Stitches a *cluster out of your local devices* (phones, Macs, PCs) to run big models — distributed but home-grown."),
    "huggingface/transformers": ("Inference runtime", BOTH,
        "The model-definition library every runtime builds on; runs a notebook locally or a training cluster — the common denominator."),

    # --- Scaling / serving infra — get it to production -------------------------
    "skypilot-org/skypilot": ("Scaling / serving infra", INFRA,
        "Run/serve LLMs across any cloud or k8s with cost-aware scheduling & spot recovery — the multi-cloud orchestration layer."),
    "vllm-project/llm-compressor": ("Scaling / serving infra", INFRA,
        "Quantize/sparsify models (GPTQ/AWQ/SmoothQuant) so they serve cheaper on vLLM — the cost-optimization step."),

    # --- Model gateway & chat UI — front the models -----------------------------
    "BerriAI/litellm": ("Model gateway & UI", BOTH,
        "One OpenAI-compatible API over 100+ providers + a self-hostable proxy with keys/budgets/routing — local or enterprise gateway."),
    "Portkey-AI/gateway": ("Model gateway & UI", BOTH,
        "Fast AI gateway with routing, fallbacks, caching, and guardrails — drop in front of any tier."),
    "open-webui/open-webui": ("Model gateway & UI", LOCAL,
        "The self-hosted ChatGPT-style UI for local models (pairs with Ollama) — RAG, users, tools, fully offline."),
    "janhq/jan": ("Model gateway & UI", LOCAL,
        "Open-source desktop ChatGPT alternative that runs models 100% on your machine."),
    "Mintplex-Labs/anything-llm": ("Model gateway & UI", LOCAL,
        "All-in-one desktop/self-host app: chat + RAG + agents over local or API models."),

    # --- Vector store — where embeddings live -----------------------------------
    "facebookresearch/faiss": ("Vector store", LOCAL,
        "The in-process ANN library — no server, embed it in your app; the index inside many of the DBs below."),
    "lancedb/lancedb": ("Vector store", LOCAL,
        "Embedded, serverless vector DB (Lance columnar format) — zero-ops local RAG that still handles large on-disk sets."),
    "pgvector/pgvector": ("Vector store", BOTH,
        "Vector search inside the Postgres you already run — scales from a laptop to a managed cluster with no new infra."),
    "chroma-core/chroma": ("Vector store", BOTH,
        "AI-native store that runs embedded for prototyping and client/server for production — the easy on-ramp."),
    "alibaba/zvec": ("Vector store", LOCAL,
        "Lightweight, lightning-fast in-process vector database for embedded use."),
    "neuml/txtai": ("Vector store", LOCAL,
        "All-in-one embeddings DB + RAG + workflows in one local package."),
    "qdrant/qdrant": ("Vector store", BOTH,
        "Rust vector DB — single-binary local, but clusters with sharding/replication for billions of vectors."),
    "redis/redis": ("Vector store", BOTH,
        "The in-memory store you already run, now with vector search — local cache to HA cluster."),
    "marqo-ai/marqo": ("Vector store", BOTH,
        "End-to-end vector search that bundles embedding inference; deploys local or distributed."),
    "weaviate/weaviate": ("Vector store", INFRA,
        "Cloud-native vector DB with hybrid search & modules — designed for clustered, multi-tenant deployments."),
    "milvus-io/milvus": ("Vector store", INFRA,
        "The billion-scale, distributed OSS vector DB — heavy ops footprint, built for datacenter scale."),

    # --- Fine-tuning — adapt the model ------------------------------------------
    "unslothai/unsloth": ("Fine-tuning", LOCAL,
        "2× faster, lower-VRAM fine-tuning — train a LoRA on a single consumer GPU (even Colab)."),
    "huggingface/peft": ("Fine-tuning", BOTH,
        "Parameter-efficient fine-tuning (LoRA/QLoRA/adapters) — one consumer GPU or a multi-node run."),
    "axolotl-ai-cloud/axolotl": ("Fine-tuning", INFRA,
        "Config-driven fine-tuning that scales to multi-GPU/multi-node (DeepSpeed/FSDP) — the cluster-grade trainer."),

    # --- Agent framework — tier-agnostic logic ----------------------------------
    "langchain-ai/langgraph": ("Agent framework", BOTH,
        "Graph/stateful agent runtime — the orchestration logic is independent of where the model runs."),
    "run-llama/llama_index": ("Agent framework", BOTH,
        "Data/agent framework — point it at a local Ollama or a cloud endpoint; tier-agnostic."),
    "crewAIInc/crewAI": ("Agent framework", BOTH,
        "Role-based multi-agent framework — runs against any model backend, local or hosted."),
    "pydantic/pydantic-ai": ("Agent framework", BOTH,
        "Type-safe agent framework; model-agnostic, so the same code targets either tier."),

    # --- Observability & eval — self-host or cloud ------------------------------
    "langfuse/langfuse": ("Observability & eval", BOTH,
        "Self-hostable LLM tracing/eval/metrics — runs in Docker locally or as managed cloud."),
    "Arize-ai/phoenix": ("Observability & eval", BOTH,
        "Open-source LLM observability you can run locally; OTel-native tracing + evals."),
    "promptfoo/promptfoo": ("Observability & eval", LOCAL,
        "CLI-first prompt/model eval that runs entirely on your machine in CI — no backend needed."),
}

# Adjacent / deliberately not in the stack table
ADJACENT = [
    ("ggml-org/whisper.cpp", "speech runtime — covered in the *voice-agents* report"),
    ("comet-ml/opik", "eval/observability — see the *LLM-evaluation* report"),
    ("confident-ai/deepeval", "eval framework — see the *LLM-evaluation* report"),
    ("langchain-ai/langchain", "broad agent toolkit — see the *agent-orchestration* report"),
    ("microsoft/autogen", "multi-agent framework — see the *agent-orchestration* report"),
]

# Two reference stacks (layer -> recommended pick)
LOCAL_STACK = [
    ("Inference runtime", "ollama/ollama", "`ollama run llama3` and you're serving on a laptop."),
    ("Gateway / UI", "open-webui/open-webui", "Self-hosted chat UI over Ollama — offline, multi-user."),
    ("Vector store", "lancedb/lancedb", "Embedded, zero-ops; or `pgvector` if you already run Postgres."),
    ("Fine-tuning", "unslothai/unsloth", "LoRA on one consumer GPU."),
    ("Agent logic", "pydantic/pydantic-ai", "Type-safe, model-agnostic — point at the local endpoint."),
    ("Observability", "promptfoo/promptfoo", "CLI evals in CI; no backend to host."),
]
INFRA_STACK = [
    ("Inference runtime", "vllm-project/vllm", "PagedAttention + continuous batching for high QPS on GPUs."),
    ("Scaling infra", "skypilot-org/skypilot", "Schedule across clouds/k8s with spot + autoscale."),
    ("Cost optimization", "vllm-project/llm-compressor", "Quantize so each GPU serves more."),
    ("Gateway", "BerriAI/litellm", "Central proxy: keys, budgets, routing, fallbacks."),
    ("Vector store", "milvus-io/milvus", "Distributed, billion-vector ANN; or clustered `qdrant`."),
    ("Fine-tuning", "axolotl-ai-cloud/axolotl", "Multi-node DeepSpeed/FSDP training."),
    ("Observability", "langfuse/langfuse", "Team-wide tracing/eval, self-hosted or cloud."),
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
TIER_BADGE = {LOCAL: "🟢 Local", BOTH: "🟡 Both", INFRA: "🔴 Infra"}

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
  f"`scripts/reports/local_vs_infra_stack.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
layers = {}
for n in present:
    layers.setdefault(TAXONOMY[n][0], []).append(n)
layer_order = ["Inference runtime", "Scaling / serving infra", "Model gateway & UI",
               "Vector store", "Fine-tuning", "Agent framework", "Observability & eval"]
tier_counts = {LOCAL: 0, BOTH: 0, INFRA: 0}
for n in present:
    tier_counts[TAXONOMY[n][1]] += 1

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} stack tools** in your stars (**{fmt_int(total_stars)}★** combined), "
  f"mapped to every layer of a self-hosted AI stack and tagged by deployment tier:")
A(f"  - 🟢 **Local / edge** ({tier_counts[LOCAL]}) — laptop, single consumer GPU, on-device, zero ops")
A(f"  - 🟡 **Scales both** ({tier_counts[BOTH]}) — same tool, local *or* cluster, config-dependent")
A(f"  - 🔴 **High-infra** ({tier_counts[INFRA]}) — multi-GPU / datacenter / high-QPS / k8s")
A(f"- **The core split is the inference runtime.** Local tier optimizes for *one* of you on "
  f"*one* box (`ollama`, `llama.cpp`, `llamafile`); high-infra optimizes for *throughput "
  f"across many GPUs* (`vllm`, `sglang`, `lmdeploy`). Everything else (gateway, vector store, "
  f"agent logic) is mostly the same code with a different deployment target.")
A(f"- **Don't pick a runtime per tool — pick a tier, then fill each layer.** The two reference "
  f"stacks below do exactly that.")
A(f"- **The 🟡 'scales both' tools are the safe bets** when you'll start local and grow: "
  f"`litellm` (gateway), `pgvector`/`qdrant`/`chroma` (store), `transformers`/`peft`, the "
  f"agent frameworks, and `langfuse`/`phoenix` all migrate without a rewrite.")
A("")

# --- The two reference stacks (the headline)
A("## The two reference stacks")
A("")
A("Same job at every layer — different tier. Pick a column and go.")
A("")
A("| Layer | 🟢 Fully-local stack | 🔴 High-infra stack |")
A("|---|---|---|")
loc = {l: (p, w) for l, p, w in LOCAL_STACK}
inf = {l: (p, w) for l, p, w in INFRA_STACK}
rows = [
    ("Inference runtime", "ollama/ollama", "vllm-project/vllm"),
    ("Scaling infra", "— (single node)", "skypilot-org/skypilot"),
    ("Cost optimization", "GGUF quant (llama.cpp)", "vllm-project/llm-compressor"),
    ("Gateway / UI", "open-webui/open-webui", "BerriAI/litellm"),
    ("Vector store", "lancedb / pgvector", "milvus-io/milvus (or clustered qdrant)"),
    ("Fine-tuning", "unslothai/unsloth", "axolotl-ai-cloud/axolotl"),
    ("Agent logic", "pydantic/pydantic-ai", "pydantic/pydantic-ai (same)"),
    ("Observability", "promptfoo/promptfoo", "langfuse/langfuse"),
]
for layer, l, r in rows:
    A(f"| **{layer}** | `{l}` | `{r}` |")
A("")
A("**Reading it:** the agent logic and observability *code* is identical across columns — "
  "only the runtime, scaling, store, and trainer change as you move from one box to a fleet.")
A("")

# --- Layer-by-layer
A("## The stack, layer by layer")
A("")
layer_intro = {
    "Inference runtime": "Where the model actually executes. This is the layer where the "
        "local/high-infra distinction is sharpest.",
    "Scaling / serving infra": "How you get a runtime onto many machines, cheaply. Only "
        "relevant once you outgrow a single node.",
    "Model gateway & UI": "What sits in front of the model(s) — a chat UI for one user, or a "
        "proxy that fans out across providers for a whole org.",
    "Vector store": "Where embeddings live for RAG. Many of these span tiers — start embedded, "
        "cluster later.",
    "Fine-tuning": "Adapting a model. LoRA on one GPU vs. multi-node full fine-tunes.",
    "Agent framework": "The orchestration logic — deliberately tier-agnostic; it targets "
        "whatever endpoint you give it.",
    "Observability & eval": "Tracing, metrics, and evals. Most self-host locally and also offer "
        "managed cloud.",
}
for layer in layer_order:
    members = layers.get(layer) or []
    if not members:
        continue
    A(f"### {layer}")
    A("")
    A(f"_{layer_intro[layer]}_")
    A("")
    A("| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |")
    A("|---|---|---|---|---|---|")
    # order: Local, Both, Infra; then by stars
    trank = {LOCAL: 0, BOTH: 1, INFRA: 2}
    for n in sorted(members, key=lambda x: (trank[TAXONOMY[x][1]], -by_name[x]["stars"])):
        r = by_name[n]
        A("| [{name}]({url}) | {tier} | {stars} | {lang} | {lc} | {blurb} |".format(
            name=n, url=r["url"], tier=TIER_BADGE[TAXONOMY[n][1]],
            stars=fmt_stars(r), lang=r.get("primary_language") or "—",
            lc=r.get("lifecycle_stage") or "—", blurb=TAXONOMY[n][2]))
    A("")

# --- Decision table
A("## Which tier should you use?")
A("")
A("| Your situation | Tier | Runtime to start with |")
A("|---|---|---|")
decide = [
    ("Laptop / Mac, privacy, one user", "🟢 Local", "`ollama` (+ `open-webui`)"),
    ("Single consumer GPU (e.g. 1×4090)", "🟢 Local", "`ollama` or `llama.cpp` w/ GGUF"),
    ("CPU-only / edge / air-gapped", "🟢 Local", "`llama.cpp` / `llamafile` / `LocalAI`"),
    ("Prototype now, scale later", "🟡 Both", "`vllm` behind `litellm`; `pgvector` store"),
    ("Many users, steady traffic", "🔴 Infra", "`vllm` (continuous batching)"),
    ("Agentic / structured-output at scale", "🔴 Infra", "`sglang` (RadixAttention)"),
    ("Multi-cloud / spot-GPU cost control", "🔴 Infra", "`vllm` orchestrated by `skypilot`"),
    ("Pool several home devices", "🟡 Both", "`exo-explore/exo`"),
]
for sit, tier, rt in decide:
    A(f"| {sit} | {tier} | {rt} |")
A("")

# --- Master comparison
A("## Master comparison (operational metrics)")
A("")
A("Sorted by tier then stars. `Health`/`Lifecycle` are the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits.")
A("")
A("| Tool | Layer | Tier | Lang | License | ★ Stars | Lifecycle | Health | "
  "Activity | Last push | Contrib(90d) |")
A("|" + "---|" * 11)
trank = {LOCAL: 0, BOTH: 1, INFRA: 2}
for n in sorted(present, key=lambda x: (trank[TAXONOMY[x][1]], -by_name[x]["stars"])):
    r = by_name[n]
    A("| [{name}]({url}) | {layer} | {tier} | {lang} | {lic} | {stars} | {lc} | {hs} | "
      "{act} | {push} | {auth} |".format(
        name=n.split("/")[-1], url=r["url"], layer=TAXONOMY[n][0],
        tier=TIER_BADGE[TAXONOMY[n][1]].split()[1],
        lang=r.get("primary_language") or "—", lic=(r.get("license") or "—"),
        stars=fmt_stars(r), lc=r.get("lifecycle_stage") or "—",
        hs=r.get("health_score") if r.get("health_score") is not None else "—",
        act=activity_label(r), push=days_to_human(r.get("days_since_push")) + " ago",
        auth=r.get("unique_authors_90d") if r.get("unique_authors_90d") is not None else "—"))
A("")

# --- Graph analysis
A("## Graph analysis — how the stack hangs together")
A("")
comm = {}
for n in present:
    nd = node_for(n)
    if nd is not None:
        comm.setdefault(nd.get("community"), []).append(n)
A(f"**Community clustering.** These {len(present)} tools span "
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities** — the stack cuts "
  f"across the inference, RAG/vector, and agent neighborhoods rather than forming one cluster.")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 2:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in names))
A("")

ranked = sorted(
    [(node_for(n).get("pagerank", 0) if node_for(n) else 0, n) for n in present],
    key=lambda x: -x[0])
A(f"**Centrality (PageRank in the full {fmt_int(len(gr['nodes']))}-repo graph)** — the "
  "'hub' tools your other stars cluster around:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f} ({TIER_BADGE[TAXONOMY[n][1]]})")
A("")

A("**Direct links between stack tools** (top similarity edges where both endpoints are in "
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
    A("- _None — the stack tools relate through their broader neighborhoods, not direct edges._")
A("")

# --- Maintenance / risk
A("## Maintenance & risk signal")
A("")
A("Bus factor = commit concentration (1 = single-maintainer risk). For infra you'll depend "
  "on, weight health + activity heavily.")
A("")
A("| Tool | Tier | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |")
A("|---|---|---|---|---|---|---|---|")
for n in sorted(present, key=lambda x: -(by_name[x].get("health_score") or 0)):
    r = by_name[n]
    tas = r.get("top_author_share")
    A("| {n} | {tier} | {h} | {lc} | {act} | {bf} | {tas} | {rel} |".format(
        n=n.split("/")[-1], tier=TIER_BADGE[TAXONOMY[n][1]].split()[1],
        h=r.get("health_score", "—"), lc=r.get("lifecycle_stage", "—"),
        act=activity_label(r), bf=r.get("bus_factor", "—"),
        tas=f"{tas:.0%}" if isinstance(tas, (int, float)) else "—",
        rel=r.get("releases_total", "—")))
A("")

# --- Adjacent
A("## Adjacent (covered elsewhere)")
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
A("- **Tiering** is an editorial judgment about each tool's *sweet spot*, not a hard limit — "
  "many 🟢 tools can be pushed onto servers and some 🔴 tools run (slowly) on a laptop. The "
  "tag reflects what the project is *optimized and typically used* for.")
A("- **Selection**: keyword scan (inference / serving / vllm / ollama / vector db / gateway / "
  "fine-tune / quantize) + manual curation into stack layers. Speech runtimes, pure eval "
  "frameworks, and broad agent toolkits were routed to adjacent reports.")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag "
  "GitHub's current state.")
A("- Re-run after a fresh `classified.json` to refresh stars/activity.")
A("")
A(f"<sub>Tools covered: {len(present)} · Tiers: {tier_counts[LOCAL]} local / "
  f"{tier_counts[BOTH]} both / {tier_counts[INFRA]} infra · Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta -------------------------------------------------------------
top = sorted(present, key=lambda x: -by_name[x]["stars"])[:5]
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / Infrastructure",
    "summary": (f"{len(present)} stack tools ({fmt_int(total_stars)}★) mapped to every layer "
                f"(runtime, serving, gateway, vector store, fine-tuning, agents, observability) "
                f"and tagged by deployment tier — {tier_counts[LOCAL]} local / "
                f"{tier_counts[BOTH]} both / {tier_counts[INFRA]} high-infra — with two "
                "ready-to-use reference stacks."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {l: len(layers.get(l, [])) for l in layer_order},
    "tiers": {"local": tier_counts[LOCAL], "both": tier_counts[BOTH], "infra": tier_counts[INFRA]},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/local_vs_infra_stack.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
