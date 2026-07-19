#!/usr/bin/env python3
"""
Generate a landscape report on the fine-tuning / post-training stack found in
the starred-repos dataset: full-stack trainers, PEFT & alignment libraries,
agent RL post-training, learn-by-building repos, domain/on-device tuning, and
the serving layer for tuned models — compared and ranked per task, with
external evidence (2026 framework round-ups, GRPO landscape surveys) cited in
the rankings.

Inputs:
  data/classified.json
  public/data/graph.json

Output:
  reports/finetuning-stack.md   (+ reports/finetuning-stack.meta.json)

Run: python3 scripts/reports/finetuning_stack.py
"""
import json
import os
from datetime import datetime, timezone

from lib import fmt_stars, CLASSIFIED, GRAPH, fmt_int, days_to_human, activity_label, make_node_for

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "finetuning-stack"
TITLE = "Fine-Tuning & Post-Training Stack — Which Trainer for Which Task"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy --------------------------------------------------------
TAXONOMY = {
    # Full-stack fine-tuning frameworks
    "hiyouga/LlamaFactory": ("Full-stack fine-tuning framework", "Unified efficient fine-tuning of 100+ LLMs & VLMs — the zero-code pick (LlamaBoard web UI, CLI, ACL 2024)."),
    "unslothai/unsloth": ("Full-stack fine-tuning framework", "The single-GPU speed king — custom Triton kernels give ~2× faster training and ~70% less VRAM than stock HF."),
    "axolotl-ai-cloud/axolotl": ("Full-stack fine-tuning framework", "YAML-driven, reproducible post-training with FSDP & DeepSpeed out of the box — the team/multi-GPU pick."),
    "huggingface/transformers": ("Full-stack fine-tuning framework", "The model-definition layer everything above builds on; `Trainer` remains the vanilla baseline."),
    "Lightning-AI/pytorch-lightning": ("Full-stack fine-tuning framework", "Generic training orchestration — pretrain/finetune any model on 1 or 10,000 GPUs with zero code changes."),
    "PaddlePaddle/PaddleNLP": ("Full-stack fine-tuning framework", "Baidu's LLM/SLM training & serving library — the pick inside the Paddle ecosystem."),

    # PEFT & alignment libraries
    "huggingface/peft": ("PEFT & alignment library", "State-of-the-art parameter-efficient fine-tuning: LoRA, QLoRA, DoRA, IA³ — the adapter layer under most trainers."),
    "huggingface/trl": ("PEFT & alignment library", "The post-training reference: SFT, reward modeling, DPO and GRPO unified in one library (v1.0, 2026)."),

    # RL post-training for agents
    "OpenPipe/ART": ("RL post-training for agents", "Agent Reinforcement Trainer — GRPO for *multi-turn* tool-using agents; vLLM rollouts + TRL/Unsloth training under the hood."),
    "Gen-Verse/OpenClaw-RL": ("RL post-training for agents", "'Train any agent simply by talking' — natural-language-driven agent RL on top of the OpenClaw ecosystem."),
    "huggingface/OpenEnv": ("RL post-training for agents", "Interface library for RL post-training environments — the emerging standard for plugging envs into trainers."),
    "Memento-Teams/Memento": ("RL post-training for agents", "The counterpoint: fine-tune LLM *agents* without fine-tuning LLMs — case-based memory instead of weight updates."),

    # Learn-by-building (from-scratch training)
    "rasbt/LLMs-from-scratch": ("Learn-by-building", "Implement a ChatGPT-like LLM in PyTorch step by step — the book-quality path from zero to pretraining + finetuning."),
    "karpathy/nanoGPT": ("Learn-by-building", "The simplest, fastest repo for training/finetuning mid-sized GPTs — frozen by design, still the canonical teaching codebase."),
    "labmlai/annotated_deep_learning_paper_implementations": ("Learn-by-building", "60+ paper implementations with side-by-side notes — transformers, LoRA, RLHF internals, readable."),
    "yandexdataschool/Practical_RL": ("Learn-by-building", "A course in reinforcement learning in the wild — the RL foundations under DPO/GRPO."),
    "pico-lm/pico-train": ("Learn-by-building", "Minimalistic framework for *transparently* training LMs — every checkpoint + activation logged for research."),
    "SylphAI-Inc/LLM-engineer-handbook": ("Learn-by-building", "Curated map of training/serving/fine-tuning resources — orientation, not code."),
    "unslothai/notebooks": ("Learn-by-building", "250+ ready-to-run fine-tuning & RL notebooks (text, vision, audio, TTS, embeddings) — the recipe box."),

    # Domain & on-device tuning
    "Blaizzy/mlx-vlm": ("Domain & on-device tuning", "Fine-tune and run vision-language models natively on Apple Silicon via MLX — unified memory instead of CUDA."),
    "huggingface/distil-whisper": ("Domain & on-device tuning", "Knowledge distillation applied: Whisper 6× faster / 50% smaller within 1% WER — the distillation reference recipe."),
    "roboflow/rf-detr": ("Domain & on-device tuning", "Real-time detection/segmentation architecture built to be fine-tuned on custom vision datasets."),
    "VectorInstitute/fed-rag": ("Domain & on-device tuning", "Fine-tune RAG systems end-to-end (retriever + generator), including federated setups."),

    # Hardware fit & serving tuned models
    "AlexsJones/llmfit": ("Hardware fit & serving", "One command to find which models your hardware can run or train — the planning step before any tuning run."),
    "lyogavin/airllm": ("Hardware fit & serving", "Layer-by-layer offloading: 70B-class inference on a single 4GB GPU — run what you tuned on tiny hardware."),
    "predibase/lorax": ("Hardware fit & serving", "Multi-LoRA inference server — dynamically batch 1000s of fine-tuned adapters on one GPU."),
    "transformerlab/transformerlab-app": ("Hardware fit & serving", "Open research workbench GUI: train, tune, evaluate and chat with models locally (CUDA + MLX backends)."),
}

# Adjacent but deliberately excluded (kept honest in the report)
ADJACENT = [
    ("vllm-project/vllm", "the serving standard for *finished* models — covered in the local-vs-infra-stack report"),
    ("ollama/ollama", "local inference runtime, not a trainer — see local-vs-infra-stack"),
    ("flyteorg/flyte", "general ML/data orchestration — schedules training, doesn't implement it"),
    ("beam-cloud/beta9", "serverless GPU substrate *where* you train, not *how*"),
    ("zai-org/GLM-V", "open model weights trained with scalable RL — a result of this stack, not a tool in it"),
    ("openai/CLIP", "landmark pretraining research, effectively frozen — read it, don't build on the repo"),
    ("NVIDIA/physicsnemo", "training framework for physics/simulation models, out of LLM post-training scope"),
    ("facebookresearch/BenchMARL", "multi-agent RL *benchmarking* research, not LLM post-training"),
    ("microsoft/generative-ai-for-beginners", "general GenAI curriculum — broader than training"),
]

# Task-ranked picks: (task, [(repo, note) x3], evidence)
TASK_RANKINGS = [
    ("LoRA/QLoRA on a single consumer GPU",
     [("unslothai/unsloth", "~2× faster, ~70% less VRAM via Triton kernels"),
      ("hiyouga/LlamaFactory", "zero-code; wraps Unsloth kernels, small overhead"),
      ("axolotl-ai-cloud/axolotl", "works, but slowest of the three on one GPU")],
     "Llama-3.1-8B QLoRA, A100-40GB, identical configs: Unsloth 3.2 h, LLaMA-Factory 3.4 h, Axolotl 5.8 h (2026 round-ups)."),
    ("Zero-code / GUI fine-tuning",
     [("hiyouga/LlamaFactory", "LlamaBoard web UI over 100+ LLMs/VLMs"),
      ("transformerlab/transformerlab-app", "full train/eval/chat workbench"),
      ("unslothai/unsloth", "Unsloth Studio web UI for train + run")],
     "LLaMA-Factory is the consensus no-code pick across 2026 comparisons."),
    ("Team-scale SFT (multi-GPU, reproducible)",
     [("axolotl-ai-cloud/axolotl", "YAML configs, FSDP & DeepSpeed built in"),
      ("hiyouga/LlamaFactory", "scales up with a larger method matrix"),
      ("Lightning-AI/pytorch-lightning", "the generic 1→10k-GPU trainer")],
     "Axolotl is repeatedly cited as the reproducible multi-GPU default in its free OSS version."),
    ("Preference alignment (DPO / reward models)",
     [("huggingface/trl", "SFT + RM + DPO + GRPO unified in v1.0"),
      ("hiyouga/LlamaFactory", "DPO/KTO/ORPO behind config flags"),
      ("axolotl-ai-cloud/axolotl", "DPO/GRPO via YAML recipes")],
     "TRL v1.0 (April 2026) unified the post-training stack; the frameworks wrap its trainers."),
    ("RL post-training for tool-using agents (GRPO)",
     [("OpenPipe/ART", "built for multi-turn agent rollouts; vLLM + TRL/Unsloth inside"),
      ("huggingface/trl", "most accessible GRPOTrainer — single GPU, synchronous loop"),
      ("huggingface/OpenEnv", "the environment interface to plug tasks into either")],
     "2026 agent-RL surveys: ART/Unsloth for accessible GRPO; verl/OpenRLHF (not starred) for datacenter-scale async RL."),
    ("Understanding LLM training from first principles",
     [("rasbt/LLMs-from-scratch", "the structured, book-quality path"),
      ("karpathy/nanoGPT", "smallest real training loop that works"),
      ("pico-lm/pico-train", "training with full checkpoint transparency")],
     "nanoGPT is frozen by design (no push ~8 months) — that's a feature for learning, a bug for production."),
    ("Fine-tuning on Apple Silicon",
     [("Blaizzy/mlx-vlm", "VLM tuning on unified memory, no CUDA"),
      ("transformerlab/transformerlab-app", "MLX backend behind a GUI"),
      ("rasbt/LLMs-from-scratch", "runs fine on MPS at teaching scale")],
     "MLX ecosystem: a Mistral-7B LoRA adapter trains in <30 min on an M2 16GB (mlx-lm docs, 2026)."),
    ("Serving fleets of tuned models on small hardware",
     [("predibase/lorax", "1000s of LoRA adapters batched on one GPU"),
      ("lyogavin/airllm", "70B-class inference on a single 4GB GPU"),
      ("AlexsJones/llmfit", "plan the hardware fit *before* you train")],
     "LoRAX's per-request adapter loading is unmatched at high adapter counts; for a handful of adapters vLLM suffices (see local-vs-infra report)."),
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
  f"{len(gr['communities'])} communities). Task rankings are additionally "
  f"backed by external 2026 framework comparisons and agent-RL surveys — "
  f"see Methodology.")
A(">")
A(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/finetuning_stack.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)
order = ["Full-stack fine-tuning framework", "PEFT & alignment library",
         "RL post-training for agents", "Learn-by-building",
         "Domain & on-device tuning", "Hardware fit & serving"]

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} fine-tuning / post-training tools** in your stars "
  f"(**{fmt_int(total_stars)}★** combined), organized along the training ladder:")
for c in order:
    if cats.get(c):
        A(f"  - **{c}** ({len(cats[c])}): "
          + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(cats[c], key=lambda x: -by_name[x]['stars'])))
A("- Mental model — post-training is a ladder: **check hardware fit → SFT/LoRA on "
  "your data → preference alignment (DPO) → RL post-training (GRPO) → serve the "
  "tuned artifact**. Most projects stop at rung two; the interesting 2026 action "
  "is on rungs three and four.")
A("- The frameworks have **converged on features and now compete on ergonomics**: "
  "`unsloth` (speed on one GPU), `LlamaFactory` (zero-code breadth), `axolotl` "
  "(reproducible team configs) all do LoRA/QLoRA/DPO/GRPO/vision — the choice is "
  "about *how you want to work*, not what's possible.")
A("- Second trend: **RL post-training went agentic.** `trl` shipped GRPO for "
  "everyone, `ART` rebuilt it around multi-turn tool-using rollouts, and `OpenEnv` "
  "is standardizing the environment side. Meanwhile `Memento` argues the "
  "contrarian case: adapt the agent's *memory*, keep the weights frozen.")
A("- No single winner — the *task rankings* below are the point: the best tool "
  "for a weekend QLoRA (`unsloth`) is not the best for team SFT (`axolotl`) or "
  "for understanding what the optimizer actually does (`nanoGPT`).")
A("")

# --- Pipeline table
A("## The post-training ladder at a glance")
A("")
A("| Rung | What happens | Tools in your stars |")
A("|---|---|---|")
A("| **0 · Hardware fit** | What can this machine train/run? | `llmfit` |")
A("| **1 · Learn the mechanics** | From-scratch training loops, courses, recipes | "
  "`LLMs-from-scratch`, `nanoGPT`, `annotated_…_implementations`, `Practical_RL`, `pico-train`, `notebooks` |")
A("| **2 · SFT / LoRA** | Supervised fine-tune on your data | "
  "`unsloth`, `LlamaFactory`, `axolotl`, `transformers`, `peft`, `pytorch-lightning`, `PaddleNLP` |")
A("| **3 · Preference alignment** | DPO / reward models | `trl` (+ framework wrappers) |")
A("| **4 · RL post-training** | GRPO on tasks & tool-use rollouts | `ART`, `OpenClaw-RL`, `OpenEnv` |")
A("| **Domain variants** | Vision, speech, RAG, Apple Silicon | `mlx-vlm`, `rf-detr`, `distil-whisper`, `fed-rag` |")
A("| **5 · Serve the artifact** | Adapters & tuned weights in production | `lorax`, `airllm`, `transformerlab-app` |")
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

# --- Task rankings (the core ask of this report)
A("## Task rankings — which stack for which job")
A("")
A("Ranked picks per task. Dataset metrics say who's *healthy*; external "
  "comparisons say who's *fast or capable* — both feed these rankings "
  "(evidence noted per row, sources in Methodology).")
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
    "Full-stack fine-tuning framework": "End-to-end trainers: data in, tuned weights out. "
        "Feature parity is near-total in 2026 (LoRA/QLoRA/DPO/GRPO/vision everywhere) — "
        "pick by workflow: speed (`unsloth`), zero-code (`LlamaFactory`), YAML reproducibility (`axolotl`).",
    "PEFT & alignment library": "The Hugging Face layer the frameworks wrap: `peft` for "
        "adapter methods, `trl` for the SFT→DPO→GRPO trainer stack. Use directly when you "
        "want control, via a framework when you want convenience.",
    "RL post-training for agents": "The 2026 frontier: reward multi-step *agent behavior*, "
        "not single responses. GRPO made it tractable; the fight is now over rollout "
        "infrastructure and environment interfaces.",
    "Learn-by-building": "Repos whose product is understanding: from-scratch GPTs, annotated "
        "papers, RL courses. Several are intentionally frozen — fine for learning, wrong as "
        "dependencies.",
    "Domain & on-device tuning": "Fine-tuning beyond cloud-GPU text LLMs: vision models, "
        "speech distillation, RAG systems, and Apple-Silicon-native training.",
    "Hardware fit & serving": "Before and after the training run: planning what fits, and "
        "serving the tuned adapters/weights — including the many-adapters and tiny-GPU cases.",
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
A("## Spotlight: SFT → DPO → GRPO — post-training became a ladder")
A("")
A("Fine-tuning in 2024 meant one thing: LoRA on instruction data. The 2026 stack "
  "is a **ladder of increasingly behavioral objectives**, and your stars cover "
  "every rung:")
A("")
A("- **SFT commoditized.** `unsloth`, `LlamaFactory` and `axolotl` reached feature "
  "parity (all: LoRA/QLoRA, full FT, DPO, GRPO, VLMs). Differentiation moved to "
  "kernels (`unsloth`: ~2× faster, ~70% less VRAM on one GPU) and workflow "
  "(zero-code UI vs YAML).")
A("- **Alignment standardized.** `trl` v1.0 unified SFT, reward modeling, DPO and "
  "GRPO into one library — every framework above now wraps its trainers rather "
  "than reimplementing them.")
A("- **The agent turn.** Single-turn GRPO trains chatbots; agents need credit "
  "assignment across *multi-turn tool-use rollouts*. That's `ART`'s pitch "
  "(vLLM-powered rollouts, TRL/Unsloth training), `OpenEnv`'s environment "
  "interface, and `OpenClaw-RL`'s train-by-talking layer.")
A("- **The contrarian rung.** `Memento` fine-tunes the agent's episodic *memory* "
  "instead of its weights — worth knowing before you spend GPU-weeks: sometimes "
  "the cheapest post-training is no training.")
A("- **What's deliberately absent**: datacenter-scale async RL (verl, OpenRLHF) "
  "isn't in your stars — if you outgrow `ART`/`trl` scale, that's the next "
  "ecosystem to evaluate.")
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
  "most 'hub-like' training tools in your ecosystem:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between training tools** (top similarity edges where both "
  "endpoints are in this report):")
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
A("Watch items: `nanoGPT` and most learn-by-building repos read as frozen — "
  "expected and fine for their purpose, but don't depend on them. "
  "`distil-whisper` is abandoned in this snapshot (the *technique* lives on in "
  "papers and Whisper forks). `Memento` has gone quiet since its paper. "
  "`lorax` is slowing (single-maintainer, ~2 months between pushes) — if adapter "
  "serving is on your critical path, benchmark vLLM's multi-LoRA as the fallback. "
  "`PaddleNLP` is healthy mainly inside the Paddle ecosystem.")
A("")

# --- Which one should you use?
A("## Which one should you use?")
A("")
A("- **One consumer GPU, weekend project** → `unsloth` (fastest, least VRAM), "
  "recipes from `unslothai/notebooks`.")
A("- **You want a UI, not YAML** → `LlamaFactory` (LlamaBoard) or "
  "`transformerlab-app` (research workbench).")
A("- **Team runs, reproducible configs, multi-GPU** → `axolotl`.")
A("- **You're aligning, not just tuning** → `trl` directly (SFT→DPO→GRPO), "
  "frameworks when convenient.")
A("- **Training an *agent*, not a chatbot** → `ART` (+ `OpenEnv` for environments); "
  "read `Memento` first to check whether memory beats weights for your case.")
A("- **You want to *understand* it** → `LLMs-from-scratch` cover to cover, then "
  "`nanoGPT`, then `pico-train` for introspection.")
A("- **Mac-only hardware** → `mlx-vlm` and the MLX ecosystem.")
A("- **After training** → `lorax` for many adapters, `airllm` for big models on "
  "tiny GPUs, `llmfit` *before* all of this to plan the fit.")
A("")

# --- Adjacent
A("## Adjacent (deliberately not listed as training tools)")
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
A("- **Selection**: keyword scan (fine-tune / lora / peft / post-train / rlhf / "
  "grpo / dpo / pretrain / distill) + manual curation into ladder stages. Serving "
  "runtimes, orchestrators, and model-weight repos were routed to adjacent "
  "reports or excluded (see above).")
A("- **Task rankings** additionally cite external evidence gathered 2026-07: "
  "the [Spheron](https://www.spheron.network/blog/axolotl-vs-unsloth-vs-torchtune/) "
  "and [index.dev](https://www.index.dev/skill-vs-skill/ai-axolotl-vs-llama-factory-vs-unsloth) "
  "framework comparisons (A100/RTX-4070 timings), the "
  "[Turing Post agent-RL tools survey](https://www.turingpost.com/p/agent-rl-training-tools), "
  "Hugging Face's [async-RL landscape post](https://huggingface.co/blog/async-rl-training-landscape), "
  "the [OpenPipe ART announcement](https://openpipe.ai/blog/art-trainer-a-new-rl-trainer-for-agents), "
  "and MLX ecosystem docs. Timings are point-in-time and partly vendor-reported — "
  "treat rankings as defaults, not verdicts.")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and "
  "may lag GitHub's current state.")
A("- Re-run after a fresh `classified.json` to refresh stars/activity; benchmark "
  "citations are frozen text and need manual review when major releases land.")
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
    "category": "AI / Engineering",
    "summary": (f"{len(present)} fine-tuning & post-training tools ({fmt_int(total_stars)}★) "
                "compared and ranked per task: full-stack trainers, PEFT/alignment "
                "libraries, agent RL (GRPO), learn-by-building repos, on-device "
                "tuning, and the adapter-serving layer — with 2026 "
                "benchmark-backed task rankings."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in order},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/finetuning_stack.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
