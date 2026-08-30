#!/usr/bin/env python3
"""
Generate a landscape report on LLM/AI inference engines for the Jetson Orin
Nano Super 8GB — which ones actually run on the hardware, which are eliminated
by it, and what actually moves throughput.

The "Super" is not a different board: it is a software/firmware unlock on
identical hardware (40->67 TOPS, 68->102 GB/s, plus a 25W MAXN_SUPER mode).
That matters because LLM decode is memory-bandwidth-bound, so the 1.5x
bandwidth figure is the one that governs tok/s, not the 1.7x TOPS headline.

Unlike the other reports in this suite, the anchor here is *measured*: the
throughput table and the memory mechanics come from benchmark runs against a
real Orin Nano Super 8GB in MAXN_SUPER mode (see MEASURED / EVIDENCE_DATE). Engine verdicts are then
argued against those numbers rather than against vendor claims.

Deliberately excluded from the output: host addresses, service topology, and
anything host-identifying. This report is published publicly; only throughput
figures (already public via the jetson-bench project) and generalizable
hardware behaviour belong in it.

Inputs:
  data/classified.json
  public/data/graph.json

Output:
  reports/jetson-inference-engines.md   (+ .meta.json)

Run: python3 scripts/reports/jetson_inference.py
"""
import json
import os
from datetime import datetime, timezone

from lib import fmt_stars, CLASSIFIED, GRAPH, fmt_int, days_to_human, activity_label, make_node_for

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def cell(s):
    """Escape a value for a markdown table cell (pipes split rows otherwise)."""
    return str(s).replace("|", "\\|")


SLUG = "jetson-inference-engines"
TITLE = "Inference Engines for the Jetson Orin Nano Super 8GB — What Actually Runs, and What Actually Helps"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

EVIDENCE_DATE = "2026-08-23"

# ---- Curated taxonomy (engines that ARE in the stars) ------------------------
TAXONOMY = {
    # Edge-viable LLM runtimes
    "ggml-org/llama.cpp": ("Edge-viable LLM runtime", "The engine that actually matters on this box — GGUF, CUDA on SM 8.7, aggressive quantization, and a memory model that degrades gracefully instead of aborting."),
    "ollama/ollama": ("Edge-viable LLM runtime", "A management layer over llama.cpp: model pulls, keep-alive, an HTTP API, and quantized KV cache. Costs a little throughput for a lot of operational convenience."),
    "mozilla-ai/llamafile": ("Edge-viable LLM runtime", "Single-file distribution of llama.cpp — useful for shipping a fixed model to a device, less so for a box you already administer."),
    "nomic-ai/gpt4all": ("Edge-viable LLM runtime", "Desktop-oriented local runtime; Declining upstream and adds nothing llama.cpp doesn't already do here."),

    # Datacenter-oriented runtimes
    "vllm-project/vllm": ("Datacenter-oriented runtime", "PagedAttention and continuous batching win when VRAM is plentiful and concurrency is high — the opposite of this box's profile."),
    "sgl-project/sglang": ("Datacenter-oriented runtime", "RadixAttention and structured generation at serving scale; same headroom assumptions as vLLM."),
    "InternLM/lmdeploy": ("Datacenter-oriented runtime", "TurboMind engine with strong quantized serving, but targets discrete datacenter GPUs."),

    # The NVIDIA / Jetson-specific path
    "NVIDIA/TensorRT-LLM": ("NVIDIA / Jetson path", "The fastest NVIDIA LLM path on supported hardware — but Jetson support lives in a separate branch aimed at AGX Orin, not this SKU. See the verdict table."),
    "dusty-nv/jetson-containers": ("NVIDIA / Jetson path", "The single most Jetson-relevant repo in your stars: prebuilt ARM64/CUDA container images that solve the dependency problem which otherwise dominates a JetPack install."),

    # Speech / non-LLM runtimes that share the same 8 GB
    "ggml-org/whisper.cpp": ("Speech & non-LLM runtime", "GGML Whisper — the STT half of an edge pipeline, and a direct competitor for the same unified memory."),
    "SYSTRAN/faster-whisper": ("Speech & non-LLM runtime", "Whisper on CTranslate2; typically faster than whisper.cpp on CUDA, at the cost of a heavier Python dependency chain."),
    "k2-fsa/sherpa-onnx": ("Speech & non-LLM runtime", "ONNX Runtime STT/TTS with genuinely small footprints — the right shape for a box where every 300 MB is contested."),

    # Formats, quantization, sizing
    "onnx/onnx": ("Format & quantization", "The interchange format underneath the ONNX Runtime path; a format, not an engine."),
    "microsoft/BitNet": ("Format & quantization", "1-bit LLM inference. The most interesting long-shot for 8 GB: if a useful model fits in ternary weights, the memory constraint changes shape entirely."),
    "AlexsJones/llmfit": ("Sizing & fit", "'One command to find what runs on your hardware' — the fit question this report exists to answer, as a tool."),
    "lyogavin/airllm": ("Sizing & fit", "Layer-streaming to run 70B on 4 GB. Technically remarkable, and far too slow to be a serving answer here."),
    "exo-explore/exo": ("Sizing & fit", "Cluster several devices into one pool — the escape hatch when 8 GB is simply the wrong number."),

    # ===== Edge-viable LLM runtime — promoted from the gap table once starred =====
    "mlc-ai/mlc-llm": ("Edge-viable LLM runtime", "TVM-compiled, arch-specialized kernels with INT4 — the one engine with a credible claim to beating llama.cpp on Orin Nano, and the NVIDIA-quoted path for Jetson LLM figures."),
    "LostRuins/koboldcpp": ("Edge-viable LLM runtime", "A llama.cpp distribution with a wider sampler and format range in one binary; occasionally ships Jetson-relevant fixes earlier."),

    # ===== NVIDIA / Jetson path — promoted from the gap table once starred =====
    "NVIDIA/TensorRT": ("NVIDIA / Jetson path", "The core inference compiler. On Jetson this is the reliable big win for vision models, and the base of the TensorRT Edge-LLM path that does reach Orin Nano."),

    # ===== Speech & non-LLM runtime — promoted from the gap table once starred =====
    "OpenNMT/CTranslate2": ("Speech & non-LLM runtime", "The engine underneath `faster-whisper`, which you already star — quantized transformer inference with a small footprint."),

    # ===== Compiler & substrate — promoted from the gap table once starred =====
    "microsoft/onnxruntime": ("Compiler & substrate", "The actual runtime behind the ONNX format you already star, with CUDA and TensorRT execution providers. Everything small on this box — STT, TTS, embeddings — can run here."),
    "ggml-org/ggml": ("Compiler & substrate", "The tensor library underneath llama.cpp and whisper.cpp, both of which you star. Where quantization formats and CUDA kernels actually land."),
    "apache/tvm": ("Compiler & substrate", "The compiler MLC-LLM is built on — relevant if you want to understand or tune what MLC produces for SM 8.7."),
}

CAT_ORDER = [
    "Edge-viable LLM runtime",
    "NVIDIA / Jetson path",
    "Compiler & substrate",
    "Datacenter-oriented runtime",
    "Speech & non-LLM runtime",
    "Format & quantization",
    "Sizing & fit",
]

# ---- Measured on the box (first-party, EVIDENCE_DATE) ------------------------
# Generation: Ollama 0.30.10 over llama.cpp, desktop and voice stack running,
# memory-prep applied. tok/s from the runtime's own device-side counters.
MEASURED_GEN = [
    ("`qwen3.5:0.8b`", "0.8B Q8_0", "36.8", "8.6 s", "The reliable tier — never OOMs, leaves room for a second tenant."),
    ("`phi4-mini`", "3.8B Q4_K_M", "18.0–18.2", "9.3 s", "Best quality-per-token that still loads without ceremony."),
    ("`qwen3.5:4b`", "4.7B Q4_K_M + vision", "14.3–14.4", "11.5 s", "Only runs with memory-prep; returns HTTP 500 (cudaMalloc OOM) without it."),
]

# Embedding: nomic-embed-text (137M, F16, dim 768), texts/sec by batch size.
MEASURED_EMBED = [
    ("query (~18 tok)", "14.8", "35.2", "38.8", "**42.4**"),
    ("128 words (~176 tok)", "6.8", "20.2", "29.0", "**33.6**"),
    ("256 words (~357 tok)", "5.6", "17.5", "23.6", "**24.5**"),
    ("512 words (~699 tok)", "5.1", "10.6", "12.1", "**12.3**"),
]

# ---- Bandwidth roofline -------------------------------------------------------
# LLM decode reads every weight once per token, so peak tok/s <= bandwidth /
# weight-bytes. 102 GB/s is the Super's peak figure; achievable is typically
# 70-85% of peak, so both columns are given.
ROOFLINE = [
    ("`qwen3.5:0.8b`", "0.92 GB", "111", "36.8", "33%", "41%"),
    ("`phi4-mini`", "2.30 GB", "44", "18.1", "41%", "51%"),
    ("`qwen3.5:4b`", "2.64 GB", "39", "14.3", "37%", "46%"),
]

# ---- Engine verdicts against this specific hardware --------------------------
# (engine, runs on Orin Nano 8GB?, verdict, the reason)
VERDICTS = [
    ("**llama.cpp**", "✅ Yes — the reference path",
     "**Use it.** Directly, or via Ollama.",
     "CUDA on SM 8.7, GGUF quantization down to Q4 and below, and — critically — it degrades into slower paths instead of aborting when memory is tight. On a box where `cudaMalloc` fails rather than reclaiming, graceful degradation *is* the feature."),
    ("**Ollama**", "✅ Yes — currently in place",
     "**Keep it** unless you need the last ~10%.",
     "It is llama.cpp underneath, so the throughput ceiling is the same. You trade a small overhead for model management, keep-alive, quantized KV cache, and an HTTP API. Dropping to raw llama.cpp buys tuning freedom, not a new performance tier."),
    ("**MLC-LLM**", "✅ Yes — genuinely supported",
     "**The one worth benchmarking.** Not in your stars.",
     "TVM-compiled kernels specialized per model and per GPU arch; NVIDIA's own Orin Nano LLM figures have historically been quoted via the MLC path with INT4. It is the only credible claim to beating llama.cpp on this SKU — and the only way to know is to measure it against the numbers in this report."),
    ("**TensorRT-LLM**", "⚠️ Not this SKU",
     "**Don't.** Wrong artifact for this board.",
     "Jetson support is not in the main branch; it lives in a separate `v0.12.0-jetson` branch targeting **AGX Orin**, with other Orin devices described as under testing. You star the repo (14,326★); it does not target your hardware. The NVIDIA path that *does* reach Orin Nano is TensorRT Edge-LLM via the Jetson AI Lab tutorials."),
    ("**TensorRT (core)**", "✅ Yes — for vision, not LLMs",
     "**Use for CNN/vision**, not for text generation.",
     "The classic Jetson win: compile a YOLO or ResNet graph to a TensorRT engine and get a large, reliable speedup. This is where TensorRT earns its reputation on Jetson; LLM decoding is a different problem."),
    ("**vLLM**", "❌ Effectively no",
     "**Skip.** Wrong machine class.",
     "PagedAttention and continuous batching are optimizations for many concurrent sequences against plentiful VRAM. On an 8 GB unified pool serving one user, they buy nothing and the headroom requirement alone rules it out — published guidance for the 8 GB SKU points to llama.cpp for exactly this reason."),
    ("**SGLang / LMDeploy**", "❌ Effectively no",
     "**Skip.**",
     "Same class of assumption as vLLM: discrete datacenter GPUs, high concurrency, generous memory."),
    ("**ONNX Runtime**", "✅ Yes — strong for small models",
     "**Use for speech and embeddings.**",
     "With the CUDA or TensorRT execution provider it is an excellent fit for the sub-1B models that populate an edge pipeline. `sherpa-onnx` (in your stars) is the practical expression of this."),
    ("**ExecuTorch**", "◐ Emerging",
     "Watch.",
     "PyTorch's edge runtime is maturing quickly but is aimed more squarely at mobile NPUs than at CUDA-capable Jetsons."),
    ("**BitNet (1-bit)**", "◐ Experimental",
     "Watch — the highest-upside long shot.",
     "If a genuinely useful model ships in ternary weights, an 8 GB box stops being memory-bound. That is a real possibility and not yet a plan."),
]

# ---- What actually moves throughput, ranked by measured effect ---------------
# (intervention, measured effect, evidence, effort)
INTERVENTIONS = [
    ("**Verify the board is in `MAXN_SUPER` (25W)**",
     "up to ~1.5× decode",
     "The Super unlock is bandwidth: 68 → 102 GB/s. Since decode is bandwidth-bound, a box left in 15W mode gives up most of that. Free, instant, no quality cost — check it before tuning anything else. (The measurements in this report were already taken in MAXN_SUPER.)",
     "None — one command"),
    ("**Apply the memory-prep recipe before loading a large model**",
     "HTTP 500 → working",
     "A 4.7B model that reliably failed with `cudaMalloc failed: out of memory` runs at 14.4 tok/s once page cache is evicted and kept evicted during load. This is the difference between *works* and *does not work* — no engine swap competes with it.",
     "Low — user-space, no root"),
    ("**Batch embedding calls to ≥32**",
     "≈4× prefill",
     "A 357-token chunk embeds at ~2.0k tok/s at batch 1 and saturates at ~8.6k tok/s at batch ≥32; per-request overhead (~60 ms) dominates below that. Never embed a corpus one text at a time.",
     "Low — caller-side change"),
    ("**Drop a model tier (4B → 0.8B)**",
     "≈2.6× generation",
     "36.8 tok/s at 0.8B vs 14.3 tok/s at 4.7B, measured on the same box the same day. Larger than any plausible engine swap.",
     "Low — but costs quality"),
    ("**Benchmark MLC-LLM against the llama.cpp baseline**",
     "Unknown — plausibly 1.2–2×",
     "The only engine with a credible claim to beating llama.cpp on this SKU. Unmeasured here; the numbers in this report are the baseline it must beat.",
     "Medium — new toolchain"),
    ("**Test whether two models can stay resident at once**",
     "Unknown — removes swap thrash",
     "With a one-model-at-a-time limit, an embedder and a generator evict each other continuously and every interleaved call pays a full load cycle. Whether a ~1 GB generator plus a ~0.3 GB embedder fits is the highest-value open experiment on the box.",
     "Low to try, high to trust"),
    ("**Move from Ollama to raw llama.cpp**",
     "Small — maybe ~10%",
     "Same engine underneath. Buys flag-level control (batch size, context, offload split) and loses model management. Do this last, not first.",
     "Medium"),
    ("**Compile vision models to TensorRT**",
     "Large for CNNs",
     "The classic Jetson optimization — but orthogonal to LLM throughput. Relevant only if the pipeline also does detection or classification.",
     "Medium"),
]

# ---- The gap: engines NOT in the stars ---------------------------------------
def gap(name, stars, lang, lic, fresh, why, verdict):
    return {"name": name, "stars": stars, "lang": lang, "lic": lic,
            "fresh": fresh, "why": why, "verdict": verdict}


MISSING = [
    gap("dusty-nv/jetson-inference", 8967, "C++", "MIT", "⚠ pushed 2025-10-16 — ~10mo",
        "The classic Jetson vision tutorial stack (detection, segmentation, TensorRT). Still the best on-ramp for the vision half, but no longer actively pushed.",
        "Star for reference; note the staleness."),
    gap("pytorch/executorch", 4941, "Python", "NOASSERTION", "pushed same-day",
        "PyTorch's edge runtime — very active, aimed more at mobile NPUs than CUDA Jetsons, but the direction of travel for on-device PyTorch.",
        "Watch."),
    gap("NVIDIA-AI-IOT/torch2trt", 4877, "Python", "MIT", "⚠ pushed 2024-08-17 — ~2y stale",
        "PyTorch→TensorRT converter that was the standard Jetson shortcut. Two years without a push is disqualifying for new work.",
        "**Skip** — use TensorRT or ONNX Runtime directly."),
    gap("turboderp-org/exllamav2", 4611, "Python", "MIT", "⚠ pushed 2026-03-04 — ~6mo",
        "EXL2 quantization, excellent on discrete consumer GPUs; not a Jetson target and slowing.",
        "Skip."),
]

# ---- Adjacent ----------------------------------------------------------------
ADJACENT = [
    ("huggingface/transformers", "The reference implementation, not a serving engine — too heavy to serve from on 8 GB."),
    ("deepspeedai/DeepSpeed", "Training-scale optimization; irrelevant to single-board inference."),
    ("openvinotoolkit/openvino", "Excellent engine, wrong vendor — Intel CPU/GPU/NPU, not Tegra CUDA."),
    ("ultralytics/yolov5", "A model family, not an engine; it is however the classic TensorRT-on-Jetson workload."),
    ("hiyouga/LlamaFactory", "Fine-tuning — see the `finetuning-stack` report."),
    ("BerriAI/litellm", "A gateway in front of engines, covered by `ai-engineer-stack`."),
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

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)

missing_stars = sum(m["stars"] for m in MISSING)

# ---- Build -------------------------------------------------------------------
gen = cl.get("generatedAt", "")
user = cl.get("username", "")
lines = []
A = lines.append

A(f"# {TITLE}")
A("")
A(f"> Engine roster derived from **{user}**'s {fmt_int(cl['total'])} starred repos "
  f"(snapshot `{gen}`), cross-referenced with the repo-similarity graph "
  f"({fmt_int(len(gr['nodes']))} nodes / {fmt_int(len(gr['links']))} edges, "
  f"{len(gr['communities'])} communities).")
A(">")
A(f"> **The throughput numbers in this report are measured, not quoted** — benchmark "
  f"runs against a real Jetson Orin Nano Super 8GB in **MAXN_SUPER** (25W) mode on "
  f"{EVIDENCE_DATE}, with the desktop and a voice stack running. Engine verdicts are "
  f"argued against those numbers. "
  f"See Methodology.")
A(">")
A(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/jetson_inference.py` (regenerate any time — no API cost).")
A("")

# --- Executive summary
A("## Executive summary")
A("")
A("- **The Super is a software unlock, not a different board.** Same silicon as the "
  "original Orin Nano 8GB, with JetPack raising it from 40→67 TOPS and **68→102 GB/s** "
  "and adding a 25W `MAXN_SUPER` mode. Because LLM decoding is memory-bandwidth-bound, "
  "**the 1.5× bandwidth figure — not the 1.7× TOPS headline — is what governs tok/s**. "
  "The TOPS number is the one that matters for vision and prefill.")
A("- **Confirm you are actually in `MAXN_SUPER`.** It is the cheapest performance in "
  "this entire report: nothing to install, no quality trade-off, and up to ~1.5× on "
  "decode if the box is sitting in 15W mode. All measurements below were taken with it "
  "already active, so they are Super-mode numbers, not 15W numbers.")
A("- **The honest headline: on this board, engine choice is not your biggest lever.** "
  "The measured spread between model tiers (2.6×) and the measured effect of batching "
  "embeddings (4×) both exceed what any realistic engine swap would buy. The one "
  "intervention that changed *whether the box works at all* was a memory-prep recipe, "
  "not a new runtime.")
A("- **Use `llama.cpp`** — directly or through Ollama, which is llama.cpp underneath. "
  "It is the only engine that combines SM 8.7 CUDA support, sub-Q4 quantization, and "
  "the one property that matters most here: it degrades into slower paths instead of "
  "aborting when memory runs out.")
A("- **`TensorRT-LLM` is in your stars and does not target this board.** Jetson support "
  "is not in the main branch; it lives in a `v0.12.0-jetson` branch aimed at **AGX "
  "Orin**. The NVIDIA path that does reach Orin Nano is TensorRT Edge-LLM. This is the "
  "single most actionable correction in the report.")
A("- **`vLLM`, `SGLang` and `LMDeploy` are the wrong machine class.** PagedAttention "
  "and continuous batching optimize for many concurrent sequences against plentiful "
  "VRAM. Serving one user from an 8 GB unified pool inverts every one of those "
  "assumptions.")
A("- **`MLC-LLM` is the one engine genuinely worth benchmarking, and it is now in "
  "your stars.** TVM-compiled, architecture-specialized INT4 kernels are the only "
  "credible claim to beating llama.cpp on this SKU. The numbers below are the baseline "
  "it has to beat — running that benchmark is the open action here, not starring it.")
A("- **Measured ceiling on this box:** **36.8 tok/s** at 0.8B, **18 tok/s** at 3.8B, "
  "**14.3 tok/s** at 4.7B. Embedding prefill saturates at **~8.6k tok/s**, but only "
  "at batch ≥ 32.")
A(f"- **Engine coverage is now good at both layers.** {len(present)} engines present "
  f"({fmt_int(total_stars)}★), with only {len(MISSING)} relevant projects still missing "
  f"({fmt_int(missing_stars)}★). The substrate gap earlier editions flagged is closed: "
  f"`onnxruntime` (the engine under the ONNX *format*), `ggml` (the substrate of "
  f"`llama.cpp` and `whisper.cpp`), `tvm` (what MLC compiles through) and `CTranslate2` "
  f"(the engine under `faster-whisper`) are all held now. What remains missing is "
  f"stale or off-target rather than structural — see the gap table.")
A("")

# --- The constraint
A("## The constraint that decides everything")
A("")
A("Before comparing engines, understand what the hardware does under pressure. The "
  "Super unlock raises the ceiling but changes none of the following, and these three "
  "properties of an 8 GB Jetson invalidate most desktop-GPU intuition:")
A("")
A("1. **The 8 GB is a unified CPU/GPU pool.** There is no separate VRAM to fill. Every "
  "megabyte the desktop, the page cache, or another process holds is a megabyte the "
  "model cannot have.")
A("2. **CUDA allocations cannot be swap-backed, and on Tegra `cudaMalloc` fails rather "
  "than forcing page-cache reclaim.** This is the crux: on a desktop, memory pressure "
  "makes things slow. Here it makes them *fail*. A tool reporting several gigabytes "
  "\"available\" can still refuse a 500 MB allocation, because only genuinely **free** "
  "memory counts.")
A("3. **Resident cost is far higher than model size.** Measured: a model reporting "
  "**916 MB** of device memory left the serving process at **2.9 GB RSS**. CUDA "
  "context, KV cache, and memory-mapped weights all land in the same pool. Budget from "
  "measured RSS, never from a model tag's size field.")
A("")
A("The practical consequence is a counterintuitive ranking: **an engine that is 15% "
  "faster but 500 MB hungrier is a worse engine on this board**, because the failure "
  "mode is not slowness, it is a hard allocation error. That single fact eliminates "
  "the entire datacenter-serving tier.")
A("")

# --- Measured baseline
A("## Measured baseline — what this box actually does")
A("")
A(f"Generation, measured {EVIDENCE_DATE} via llama.cpp (through Ollama 0.30.10), with "
  f"the desktop and a voice stack running and memory-prep applied. Throughput comes "
  f"from the runtime's own device-side counters, not wall-clock.")
A("")
A("| Model | Quant | tok/s | Load | Note |")
A("|---|---|---|---|---|")
for m, q, tps, load, note in MEASURED_GEN:
    A(f"| {cell(m)} | {cell(q)} | **{tps}** | {load} | {cell(note)} |")
A("")
A("Embedding throughput (texts/sec) for a 137M F16 embedder, by batch size — the table "
  "that makes the case for batching:")
A("")
A("| Text size | batch 1 | batch 8 | batch 32 | batch 64 |")
A("|---|---|---|---|---|")
for size, b1, b8, b32, b64 in MEASURED_EMBED:
    A(f"| {cell(size)} | {b1} | {b8} | {b32} | {b64} |")
A("")
A("**Read the first column as a warning.** At batch 1 a 357-token chunk runs ~4× below "
  "the achievable prefill ceiling, because ~60 ms of per-request overhead dominates. "
  "The engine is not the problem there; the calling pattern is.")
A("")
A("**One caveat that matters for anyone reproducing this:** compute on this box is "
  "rock-steady (~2% spread at batch ≥ 32) while *wall-clock* is not — repeated "
  "identical embedding runs shifted by 5× between regimes, with the entire difference "
  "in reported load time rather than compute. Quote compute-derived throughput, record "
  "whether a model reload was charged, and never trust a single-run wall-clock "
  "benchmark here.")
A("")

# --- Roofline
A("## How much headroom is left? A bandwidth roofline")
A("")
A("Token generation reads every weight from memory once per token, so decode is "
  "**memory-bandwidth-bound**, not compute-bound. That gives a hard ceiling: "
  "`tok/s ≤ bandwidth ÷ weight-bytes`. Against the Super's **102 GB/s**:")
A("")
A("| Model | Weights | Roofline tok/s | Measured | % of peak BW | % of ~achievable BW |")
A("|---|---|---|---|---|---|")
for m, w, roof, meas, pk, ach in ROOFLINE:
    A(f"| {cell(m)} | {w} | {roof} | **{meas}** | {pk} | {ach} |")
A("")
A("The consistency is the interesting part: **33–41% of peak across three very "
  "different model sizes**, or roughly 41–51% once you discount peak bandwidth to the "
  "70–85% a real memory subsystem achieves. A single outlier would suggest a "
  "model-specific problem; a flat ratio says the box is running at a stable, "
  "engine-determined fraction of its memory ceiling.")
A("")
A("**What that implies for engine choice.** There is real headroom — but less than the "
  "raw gap suggests. Part of it is irreducible: KV-cache reads that grow with context, "
  "attention compute, and the desktop and voice stack competing for the same bus during "
  "these runs. A realistic ceiling for a better-tuned engine on this board is perhaps "
  "**1.2–1.6×**, not the 2–3× a naive reading of the roofline would promise. That is "
  "the honest size of the prize for benchmarking MLC-LLM — worth doing, and not a "
  "transformation.")
A("")
A("It also explains why the datacenter engines are pointless here. vLLM's advantages "
  "are about scheduling many concurrent sequences; they do nothing for a single stream "
  "that is already waiting on memory.")
A("")

# --- Verdicts
A("## Engine verdicts against this hardware")
A("")
A("| Engine | Runs on Orin Nano 8GB? | Verdict | Why |")
A("|---|---|---|---|")
for eng, runs, verdict, why in VERDICTS:
    A(f"| {cell(eng)} | {cell(runs)} | {cell(verdict)} | {cell(why)} |")
A("")

# --- Interventions
A("## What actually moves throughput, ranked by measured effect")
A("")
A("This is the section to act on. Interventions are ordered by the size of the effect "
  "actually observed, not by how interesting they are.")
A("")
A("| Intervention | Measured effect | Evidence | Effort |")
A("|---|---|---|---|")
for iv, effect, ev, effort in INTERVENTIONS:
    A(f"| {cell(iv)} | {cell(effect)} | {cell(ev)} | {cell(effort)} |")
A("")
A("Note the shape of that table: **the top three interventions are all free, and none "
  "of them is an engine swap.** The engine question only becomes the binding one after "
  "memory discipline, batching, and model sizing have been settled.")
A("")

# --- Master comparison
A("## The engines in your stars")
A("")
A("Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits.")
A("")
A("| Engine | Class | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Contrib(90d) |")
A("|---|---|---|---|---|---|---|---|---|---|")
for n in sorted(present, key=lambda x: -by_name[x]["stars"]):
    r = by_name[n]
    A("| [{n}](https://github.com/{n}) | {cat} | {lang} | {lic} | {st} | {lc} | {h} | {act} | {dsp} ago | {au} |".format(
        n=n, cat=TAXONOMY[n][0], lang=cell(r.get("primary_language") or "—"),
        lic=cell((r.get("license_name") or "—").replace("License", "").strip() or "—"),
        st=fmt_stars(r), lc=r.get("lifecycle_stage") or "—",
        h=r.get("health_score", "—"), act=activity_label(r),
        dsp=days_to_human(r.get("days_since_push")),
        au=r.get("unique_authors_90d", "—")))
A("")
for c in CAT_ORDER:
    if not cats.get(c):
        continue
    A(f"**{c}**")
    A("")
    for n in sorted(cats[c], key=lambda x: -by_name[x]["stars"]):
        A(f"- **{n}** ({fmt_int(by_name[n]['stars'])}★) — {TAXONOMY[n][1]}")
    A("")

# --- Gap
A("## The gap — inference projects missing from your stars")
A("")
A(f"{len(MISSING)} repos, **{fmt_int(missing_stars)}★** combined. Metrics read from the "
  f"GitHub API on **{EVIDENCE_DATE}** and frozen into the generator — they are *not* "
  f"dataset metrics and do **not** refresh when the pipeline re-runs.")
A("")
A("| Repo | ★ | Lang | License | Freshness | Why it matters on Jetson | Verdict |")
A("|---|---|---|---|---|---|---|")
for m in sorted(MISSING, key=lambda x: -x["stars"]):
    A(f"| [{m['name']}](https://github.com/{m['name']}) | {fmt_int(m['stars'])} | "
      f"{cell(m['lang'])} | {cell(m['lic'])} | {cell(m['fresh'])} | {cell(m['why'])} | "
      f"{cell(m['verdict'])} |")
A("")
star_now = [m for m in MISSING if m["verdict"].startswith("**Star it")]
A(f"**Priority shortlist** — {len(star_now)} repos, each closing a structural hole "
  f"rather than adding a variant of something you already have:")
A("")
for m in sorted(star_now, key=lambda x: -x["stars"]):
    A(f"- `{m['name']}` ({fmt_int(m['stars'])}★)")
A("")

# --- Recommended stack
A("## Which engine should you use?")
A("")
A("```")
A("What are you running?")
A("│")
A("├─ Text generation ──────► llama.cpp (via Ollama, or direct)")
A("│                          Benchmark MLC-LLM against the numbers above")
A("│                          before concluding llama.cpp is the ceiling.")
A("│")
A("├─ Embeddings ───────────► same runtime, but BATCH ≥ 32.")
A("│                          Batch size matters ~4x more than engine choice.")
A("│")
A("├─ Speech (STT/TTS) ─────► sherpa-onnx / ONNX Runtime, or whisper.cpp")
A("│                          Small footprints matter more than peak speed —")
A("│                          they compete with the LLM for the same 8 GB.")
A("│")
A("├─ Vision (detect/classify) ─► TensorRT. This is the classic Jetson win,")
A("│                          and it is orthogonal to LLM throughput.")
A("│")
A("└─ Dependency hell ──────► jetson-containers (already in your stars).")
A("                           On JetPack, the build problem usually costs")
A("                           more time than the inference problem.")
A("```")
A("")
A("**The recommended stack, stated plainly:** `llama.cpp` for generation, ONNX Runtime "
  "or `sherpa-onnx` for speech, `TensorRT` for vision, all installed via "
  "`jetson-containers` rather than fought with by hand — and the memory-prep discipline "
  "applied before any large load. Then, and only then, benchmark `MLC-LLM` to find out "
  "whether the generation tier can be beaten.")
A("")
A("**What not to do:** don't reach for `vLLM` because it is the fastest engine in "
  "benchmarks run on datacenter GPUs, and don't invest in `TensorRT-LLM` for text "
  "generation on this board — it is not built for it.")
A("")

# --- Graph analysis
A("## Graph analysis")
A("")
comm = {}
for n in present:
    nd = node_for(n)
    if nd is not None:
        comm.setdefault(nd.get("community"), []).append(n)
A(f"**Community clustering.** These {len(present)} engines span "
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
A(f"**Centrality (PageRank in the full {fmt_int(len(gr['nodes']))}-repo graph)**:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")
A("**Direct links between these engines:**")
A("")
if inter_edges:
    id_to_name = {v: k for k, v in name_to_nodeid.items()}
    for e in sorted(inter_edges, key=lambda x: -x["weight"])[:12]:
        a = id_to_name.get(e["source"], e["source"])
        b = id_to_name.get(e["target"], e["target"])
        why = []
        if e.get("shared_topics"):
            why.append("topics: " + ", ".join(e["shared_topics"][:4]))
        A(f"- `{a}` ⇄ `{b}` (w={e['weight']:.3f})" + (f" — {'; '.join(why)}" if why else ""))
    if len(inter_edges) > 12:
        A(f"- …and {len(inter_edges) - 12} more.")
else:
    A("- _None._")
A("")

# --- Maintenance
A("## Maintenance & risk signal")
A("")
A("| Engine | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |")
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
A("Watch items: `nomic-ai/gpt4all` is Declining and adds nothing here. Outside the "
  "dataset, `NVIDIA-AI-IOT/torch2trt` (~2 years without a push) and "
  "`dusty-nv/jetson-inference` (~10 months) are both widely-cited Jetson resources that "
  "have gone quiet — treat tutorials built on them as dated. `turboderp-org/exllamav2` "
  "is also slowing, though it was never a Jetson target.")
A("")

# --- Adjacent
A("## Adjacent (deliberately not counted as inference engines)")
A("")
for name, why in ADJACENT:
    r = by_name.get(name)
    star = f" ({fmt_int(r['stars'])}★)" if r else ""
    A(f"- **{name}**{star} — {why}")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Hardware.** This report is about the **Jetson Orin Nano 8GB** (Ampere, SM 8.7). "
  "The original Jetson Nano is a different, much weaker board that never shipped with "
  "8 GB — almost nothing here transfers to it.")
A(f"- **The throughput figures are first-party measurements**, taken {EVIDENCE_DATE} "
  f"against a real Orin Nano 8GB with the desktop environment and a voice pipeline "
  f"running — i.e. under realistic contention, not on an idle box. Generation "
  f"throughput comes from the runtime's own device-side token counters; embedding "
  f"figures are compute-derived. A quieter box would score higher; the numbers are "
  f"deliberately not best-case.")
A("- **What is *not* measured here:** MLC-LLM, ONNX Runtime, and raw llama.cpp without "
  "Ollama were **not** benchmarked on this box. Their verdicts above are reasoned from "
  "architecture and published support status, and are explicitly weaker evidence than "
  "the measured rows. The MLC-LLM recommendation is a recommendation *to measure*, not "
  "a claim that it wins.")
A("- **TensorRT-LLM support status** comes from the project's own Jetson branch "
  "arrangement — Jetson builds living in a `v0.12.0-jetson` branch aimed at AGX Orin, "
  "with main-branch Jetson support absent "
  "([discussion](https://github.com/NVIDIA/TensorRT-LLM/discussions/10054), "
  "[Jetson AI Lab](https://www.jetson-ai-lab.com/tensorrt_llm)). Re-check before "
  "acting: this is exactly the kind of status that changes between releases.")
A("- **Third-party comparisons** were consulted for cross-checking only "
  "([ProventusNova](https://proventusnova.com/blog/llm-inference-jetson-orin-llamacpp-ollama), "
  "[Jetson AI Lab](https://www.jetson-ai-lab.com/tensorrt_llm)). Where published "
  "figures for 7B-class models on this SKU disagree with the measurements here, the "
  "measurements win — several public benchmarks appear to run on an idle headless box "
  "and do not survive contention.")
A("- **Deliberately omitted:** host addresses, service topology, and configuration "
  "specific to one machine. This report is published publicly; only throughput figures "
  "and generalizable hardware behaviour belong in it.")
A("- **The roofline is an estimate, not a measurement.** It assumes one full read of "
  "the weights per token at the vendor's 102 GB/s peak, and ignores KV-cache traffic, "
  "attention compute, and the contention present during these runs. Weight sizes come "
  "from measured device memory where available and from nominal quantization "
  "bits-per-parameter otherwise. Treat the percentages as a consistency check on where "
  "the box sits, not as a precise efficiency figure.")
A("- **Board identification.** Specs for the Super (67 TOPS, 102 GB/s, 7W/15W/25W) are "
  "NVIDIA's published figures for the Orin Nano Super Developer Kit; the uplift from "
  "40 TOPS / 68 GB/s is a software unlock on identical hardware, not a new board.")
A("- **The gap table does not refresh** with the pipeline; its metrics and the frozen "
  "citations need a manual pass.")
A("")
A(f"<sub>Engines covered: {len(present)} · Missing catalogued: {len(MISSING)} · "
  f"Measurements: {EVIDENCE_DATE} · Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta -------------------------------------------------------------
top = sorted(present, key=lambda x: -by_name[x]["stars"])[:5]
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / Infrastructure",
    "summary": (f"Which inference engine to run on a Jetson Orin Nano 8GB, argued "
                f"against first-party measurements (36.8 tok/s at 0.8B, 14.3 at 4.7B): "
                f"llama.cpp is the answer, TensorRT-LLM does not target this SKU, the "
                f"datacenter tier is the wrong machine class — and the three biggest "
                f"throughput levers are not engine swaps at all. Covers {len(present)} "
                f"engines in the dataset plus {len(MISSING)} missing "
                f"({fmt_int(missing_stars)}★)."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in CAT_ORDER},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/jetson_inference.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  engines: {len(present)} / {len(sel_names)} curated")
print(f"  missing catalogued: {len(MISSING)} ({fmt_int(missing_stars)}★)")
absent = [n for n in sel_names if n not in by_name]
if absent:
    print("  WARNING missing:", absent)
now_starred = [m["name"] for m in MISSING if m["name"] in by_name]
if now_starred:
    print("  WARNING gap table stale — now in dataset:", now_starred)
