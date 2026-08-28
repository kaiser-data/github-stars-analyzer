# Fine-Tuning & Post-Training Stack — Which Trainer for Which Task

> Derived from **kaiser-data**'s 1,752 starred repos (snapshot `2026-08-28T01:21:50.535Z`), cross-referenced with the repo-similarity graph (1,752 nodes / 5,707 edges, 35 communities). Task rankings are additionally backed by external 2026 framework comparisons and agent-RL surveys — see Methodology.
>
> Generated 2026-08-28 by `scripts/reports/finetuning_stack.py` (regenerate any time — no API cost).

![Top tools by stars](assets/finetuning-stack-top-tools.svg)

![Tools per category](assets/finetuning-stack-categories.svg)


## Executive summary

- **27 fine-tuning / post-training tools** in your stars (**778,978★** combined), organized along the training ladder:
  - **Full-stack fine-tuning framework** (6): `transformers`, `unsloth`, `LlamaFactory`, `pytorch-lightning`, `PaddleNLP`, `axolotl`
  - **PEFT & alignment library** (2): `peft`, `trl`
  - **RL post-training for agents** (4): `ART`, `OpenClaw-RL`, `Memento`, `OpenEnv`
  - **Learn-by-building** (7): `LLMs-from-scratch`, `annotated_deep_learning_paper_implementations`, `nanoGPT`, `Practical_RL`, `notebooks`, `LLM-engineer-handbook`, `pico-train`
  - **Domain & on-device tuning** (4): `rf-detr`, `mlx-vlm`, `distil-whisper`, `fed-rag`
  - **Hardware fit & serving** (4): `llmfit`, `airllm`, `transformerlab-app`, `lorax`
- Mental model — post-training is a ladder: **check hardware fit → SFT/LoRA on your data → preference alignment (DPO) → RL post-training (GRPO) → serve the tuned artifact**. Most projects stop at rung two; the interesting 2026 action is on rungs three and four.
- The frameworks have **converged on features and now compete on ergonomics**: `unsloth` (speed on one GPU), `LlamaFactory` (zero-code breadth), `axolotl` (reproducible team configs) all do LoRA/QLoRA/DPO/GRPO/vision — the choice is about *how you want to work*, not what's possible.
- Second trend: **RL post-training went agentic.** `trl` shipped GRPO for everyone, `ART` rebuilt it around multi-turn tool-using rollouts, and `OpenEnv` is standardizing the environment side. Meanwhile `Memento` argues the contrarian case: adapt the agent's *memory*, keep the weights frozen.
- No single winner — the *task rankings* below are the point: the best tool for a weekend QLoRA (`unsloth`) is not the best for team SFT (`axolotl`) or for understanding what the optimizer actually does (`nanoGPT`).

## The post-training ladder at a glance

| Rung | What happens | Tools in your stars |
|---|---|---|
| **0 · Hardware fit** | What can this machine train/run? | `llmfit` |
| **1 · Learn the mechanics** | From-scratch training loops, courses, recipes | `LLMs-from-scratch`, `nanoGPT`, `annotated_…_implementations`, `Practical_RL`, `pico-train`, `notebooks` |
| **2 · SFT / LoRA** | Supervised fine-tune on your data | `unsloth`, `LlamaFactory`, `axolotl`, `transformers`, `peft`, `pytorch-lightning`, `PaddleNLP` |
| **3 · Preference alignment** | DPO / reward models | `trl` (+ framework wrappers) |
| **4 · RL post-training** | GRPO on tasks & tool-use rollouts | `ART`, `OpenClaw-RL`, `OpenEnv` |
| **Domain variants** | Vision, speech, RAG, Apple Silicon | `mlx-vlm`, `rf-detr`, `distil-whisper`, `fed-rag` |
| **5 · Serve the artifact** | Adapters & tuned weights in production | `lorax`, `airllm`, `transformerlab-app` |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [huggingface/transformers](https://github.com/huggingface/transformers) | Full-stack fine-tuning framework | Python | Apache-2.0 | 164,519 (▲1,075) | Classic | 100 | very active | 0d ago | 7.8y | 43 |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | Learn-by-building | Jupyter Notebook | NOASSERTION | 103,916 (▲3,024) | Mature | 57 | active | 1d ago | 3.1y | 6 |
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | Full-stack fine-tuning framework | Python | Apache-2.0 | 74,995 (▲5,310) | Mature | 83 | very active | 0d ago | 2.7y | 21 |
| [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) | Full-stack fine-tuning framework | Python | Apache-2.0 | 74,403 (▲504) | Classic | 84 | very active | 1d ago | 3.3y | 31 |
| [labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | Learn-by-building | Python | MIT | 67,365 (▲73) | Declining | 20 | stale | 7mo ago | 6.0y | 0 |
| [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | Learn-by-building | Python | MIT | 62,529 (▲583) | Declining | 9 | stale | 9mo ago | 3.7y | 0 |
| [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | Hardware fit & serving | Rust | MIT | 34,371 (▲3,139) | Hot | 88 | very active | 0d ago | 6mo | 33 |
| [lyogavin/airllm](https://github.com/lyogavin/airllm) | Hardware fit & serving | Jupyter Notebook | Apache-2.0 | 32,693 (▲2,808) | Mature | 65 | very active | 1d ago | 3.2y | 1 |
| [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | Full-stack fine-tuning framework | Python | Apache-2.0 | 31,313 (▲37) | Classic | 76 | very active | 2d ago | 7.4y | 12 |
| [huggingface/peft](https://github.com/huggingface/peft) | PEFT & alignment library | Python | Apache-2.0 | 21,600 (▲85) | Classic | 95 | very active | 1d ago | 3.8y | 45 |
| [huggingface/trl](https://github.com/huggingface/trl) | PEFT & alignment library | Python | Apache-2.0 | 19,160 (▲135) | Classic | 80 | very active | 0d ago | 6.4y | 10 |
| [PaddlePaddle/PaddleNLP](https://github.com/PaddlePaddle/PaddleNLP) | Full-stack fine-tuning framework | Python | Apache-2.0 | 12,968 (▲4) | Mature | 32 | slowing | 3mo ago | 5.6y | 0 |
| [axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) | Full-stack fine-tuning framework | Python | Apache-2.0 | 12,413 (▲87) | Classic | 84 | very active | 1d ago | 3.4y | 13 |
| [OpenPipe/ART](https://github.com/OpenPipe/ART) | RL post-training for agents | Python | Apache-2.0 | 10,669 (▲107) | Hot | 75 | very active | 0d ago | 1.5y | 6 |
| [roboflow/rf-detr](https://github.com/roboflow/rf-detr) | Domain & on-device tuning | Python | Apache-2.0 | 9,077 (▲181) | Hot | 84 | very active | 2d ago | 1.4y | 13 |
| [yandexdataschool/Practical_RL](https://github.com/yandexdataschool/Practical_RL) | Learn-by-building | Jupyter Notebook | Unlicense | 6,565 (▲12) | Mature | 26 | slowing | 4mo ago | 9.6y | 0 |
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | RL post-training for agents | Python | Apache-2.0 | 5,657 (▲30) | Declining | 24 | slowing | 3mo ago | 6mo | 0 |
| [unslothai/notebooks](https://github.com/unslothai/notebooks) | Learn-by-building | Jupyter Notebook | LGPL-3.0 | 5,633 (▲81) | Hot | 55 | very active | 0d ago | 1.7y | 3 |
| [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | Domain & on-device tuning | Python | MIT | 5,428 (▲124) | Mature | 84 | very active | 0d ago | 2.4y | 13 |
| [transformerlab/transformerlab-app](https://github.com/transformerlab/transformerlab-app) | Hardware fit & serving | Python | AGPL-3.0 | 5,180 (▲10) | Mature | 78 | very active | 19d ago | 2.7y | 3 |
| [SylphAI-Inc/LLM-engineer-handbook](https://github.com/SylphAI-Inc/LLM-engineer-handbook) | Learn-by-building | — | MIT | 5,027 (▲27) | Abandoned | 5 | stale | 1.0y ago | 1.8y | 0 |
| [huggingface/distil-whisper](https://github.com/huggingface/distil-whisper) | Domain & on-device tuning | Python | MIT | 4,112 (▲11) | Abandoned | 4 | stale | 1.6y ago | 2.8y | 0 |
| [predibase/lorax](https://github.com/predibase/lorax) | Hardware fit & serving | Python | Apache-2.0 | 3,826 (▲3) | Mature | 27 | slowing | 3mo ago | 2.9y | 0 |
| [Memento-Teams/Memento](https://github.com/Memento-Teams/Memento) | RL post-training for agents | Python | MIT | 2,569 (▲9) | Declining | 8 | stale | 10mo ago | 1.2y | 0 |
| [huggingface/OpenEnv](https://github.com/huggingface/OpenEnv) | RL post-training for agents | Python | BSD-3-Clause | 2,521 (▲34) | Hot | 74 | very active | 1d ago | 11mo | 9 |
| [pico-lm/pico-train](https://github.com/pico-lm/pico-train) | Learn-by-building | Python | Apache-2.0 | 319 (▲1) | Declining | 21 | stale | 6mo ago | 2.0y | 0 |
| [VectorInstitute/fed-rag](https://github.com/VectorInstitute/fed-rag) | Domain & on-device tuning | Python | Apache-2.0 | 150 | Declining | 32 | slowing | 2mo ago | 1.6y | 0 |

## Task rankings — which stack for which job

Ranked picks per task. Dataset metrics say who's *healthy*; external comparisons say who's *fast or capable* — both feed these rankings (evidence noted per row, sources in Methodology).

| Task | 🥇 First pick | 🥈 Second | 🥉 Third | Evidence / note |
|---|---|---|---|---|
| **LoRA/QLoRA on a single consumer GPU** | `unsloth` — ~2× faster, ~70% less VRAM via Triton kernels | `LlamaFactory` — zero-code; wraps Unsloth kernels, small overhead | `axolotl` — works, but slowest of the three on one GPU | Llama-3.1-8B QLoRA, A100-40GB, identical configs: Unsloth 3.2 h, LLaMA-Factory 3.4 h, Axolotl 5.8 h (2026 round-ups). |
| **Zero-code / GUI fine-tuning** | `LlamaFactory` — LlamaBoard web UI over 100+ LLMs/VLMs | `transformerlab-app` — full train/eval/chat workbench | `unsloth` — Unsloth Studio web UI for train + run | LLaMA-Factory is the consensus no-code pick across 2026 comparisons. |
| **Team-scale SFT (multi-GPU, reproducible)** | `axolotl` — YAML configs, FSDP & DeepSpeed built in | `LlamaFactory` — scales up with a larger method matrix | `pytorch-lightning` — the generic 1→10k-GPU trainer | Axolotl is repeatedly cited as the reproducible multi-GPU default in its free OSS version. |
| **Preference alignment (DPO / reward models)** | `trl` — SFT + RM + DPO + GRPO unified in v1.0 | `LlamaFactory` — DPO/KTO/ORPO behind config flags | `axolotl` — DPO/GRPO via YAML recipes | TRL v1.0 (April 2026) unified the post-training stack; the frameworks wrap its trainers. |
| **RL post-training for tool-using agents (GRPO)** | `ART` — built for multi-turn agent rollouts; vLLM + TRL/Unsloth inside | `trl` — most accessible GRPOTrainer — single GPU, synchronous loop | `OpenEnv` — the environment interface to plug tasks into either | 2026 agent-RL surveys: ART/Unsloth for accessible GRPO; verl/OpenRLHF (not starred) for datacenter-scale async RL. |
| **Understanding LLM training from first principles** | `LLMs-from-scratch` — the structured, book-quality path | `nanoGPT` — smallest real training loop that works | `pico-train` — training with full checkpoint transparency | nanoGPT is frozen by design (no push ~8 months) — that's a feature for learning, a bug for production. |
| **Fine-tuning on Apple Silicon** | `mlx-vlm` — VLM tuning on unified memory, no CUDA | `transformerlab-app` — MLX backend behind a GUI | `LLMs-from-scratch` — runs fine on MPS at teaching scale | MLX ecosystem: a Mistral-7B LoRA adapter trains in <30 min on an M2 16GB (mlx-lm docs, 2026). |
| **Serving fleets of tuned models on small hardware** | `lorax` — 1000s of LoRA adapters batched on one GPU | `airllm` — 70B-class inference on a single 4GB GPU | `llmfit` — plan the hardware fit *before* you train | LoRAX's per-request adapter loading is unmatched at high adapter counts; for a handful of adapters vLLM suffices (see local-vs-infra report). |

## By category

### Full-stack fine-tuning framework

_End-to-end trainers: data in, tuned weights out. Feature parity is near-total in 2026 (LoRA/QLoRA/DPO/GRPO/vision everywhere) — pick by workflow: speed (`unsloth`), zero-code (`LlamaFactory`), YAML reproducibility (`axolotl`)._

- **[huggingface/transformers](https://github.com/huggingface/transformers)** · 164,519★ · Python · Classic  
  The model-definition layer everything above builds on; `Trainer` remains the vanilla baseline.  
  <sub>topics: nlp, natural-language-processing, pytorch, pytorch-transformers, transformer, model-hub, pretrained-models, speech-recognition</sub>
- **[unslothai/unsloth](https://github.com/unslothai/unsloth)** · 74,995★ · Python · Mature  
  The single-GPU speed king — custom Triton kernels give ~2× faster training and ~70% less VRAM than stock HF.  
  <sub>topics: fine-tuning, llama, llms, gemma, unsloth, llm, deepseek, text-to-speech</sub>
- **[hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)** · 74,403★ · Python · Classic  
  Unified efficient fine-tuning of 100+ LLMs & VLMs — the zero-code pick (LlamaBoard web UI, CLI, ACL 2024).  
  <sub>topics: fine-tuning, llama, llm, peft, transformers, rlhf, qlora, quantization</sub>
- **[Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning)** · 31,313★ · Python · Classic  
  Generic training orchestration — pretrain/finetune any model on 1 or 10,000 GPUs with zero code changes.  
  <sub>topics: python, deep-learning, artificial-intelligence, ai, pytorch, data-science, machine-learning</sub>
- **[PaddlePaddle/PaddleNLP](https://github.com/PaddlePaddle/PaddleNLP)** · 12,968★ · Python · Mature  
  Baidu's LLM/SLM training & serving library — the pick inside the Paddle ecosystem.  
  <sub>topics: nlp, embedding, bert, ernie, paddlenlp, pretrained-models, transformers, information-extraction</sub>
- **[axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl)** · 12,413★ · Python · Classic  
  YAML-driven, reproducible post-training with FSDP & DeepSpeed out of the box — the team/multi-GPU pick.  
  <sub>topics: fine-tuning, llm</sub>

### PEFT & alignment library

_The Hugging Face layer the frameworks wrap: `peft` for adapter methods, `trl` for the SFT→DPO→GRPO trainer stack. Use directly when you want control, via a framework when you want convenience._

- **[huggingface/peft](https://github.com/huggingface/peft)** · 21,600★ · Python · Classic  
  State-of-the-art parameter-efficient fine-tuning: LoRA, QLoRA, DoRA, IA³ — the adapter layer under most trainers.  
  <sub>topics: adapter, diffusion, llm, parameter-efficient-learning, python, pytorch, transformers, lora</sub>
- **[huggingface/trl](https://github.com/huggingface/trl)** · 19,160★ · Python · Classic  
  The post-training reference: SFT, reward modeling, DPO and GRPO unified in one library (v1.0, 2026).  
  <sub>topics: —</sub>

### RL post-training for agents

_The 2026 frontier: reward multi-step *agent behavior*, not single responses. GRPO made it tractable; the fight is now over rollout infrastructure and environment interfaces._

- **[OpenPipe/ART](https://github.com/OpenPipe/ART)** · 10,669★ · Python · Hot  
  Agent Reinforcement Trainer — GRPO for *multi-turn* tool-using agents; vLLM rollouts + TRL/Unsloth training under the hood.  
  <sub>topics: llms, lora, reinforcement-learning, agent, agentic-ai, grpo, rl, qwen</sub>
- **[Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL)** · 5,657★ · Python · Declining  
  'Train any agent simply by talking' — natural-language-driven agent RL on top of the OpenClaw ecosystem.  
  <sub>topics: async, memory-systems, open-claw, openclaw-skills, rlhf, sglang, skill-learning, slime</sub>
- **[Memento-Teams/Memento](https://github.com/Memento-Teams/Memento)** · 2,569★ · Python · Declining  
  The counterpoint: fine-tune LLM *agents* without fine-tuning LLMs — case-based memory instead of weight updates.  
  <sub>topics: —</sub>
- **[huggingface/OpenEnv](https://github.com/huggingface/OpenEnv)** · 2,521★ · Python · Hot  
  Interface library for RL post-training environments — the emerging standard for plugging envs into trainers.  
  <sub>topics: —</sub>

### Learn-by-building

_Repos whose product is understanding: from-scratch GPTs, annotated papers, RL courses. Several are intentionally frozen — fine for learning, wrong as dependencies._

- **[rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)** · 103,916★ · Jupyter Notebook · Mature  
  Implement a ChatGPT-like LLM in PyTorch step by step — the book-quality path from zero to pretraining + finetuning.  
  <sub>topics: gpt, large-language-models, llm, python, pytorch, ai, artificial-intelligence, language-model</sub>
- **[labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations)** · 67,365★ · Python · Declining  
  60+ paper implementations with side-by-side notes — transformers, LoRA, RLHF internals, readable.  
  <sub>topics: deep-learning, deep-learning-tutorial, pytorch, gan, transformers, reinforcement-learning, optimizers, neural-networks</sub>
- **[karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)** · 62,529★ · Python · Declining  
  The simplest, fastest repo for training/finetuning mid-sized GPTs — frozen by design, still the canonical teaching codebase.  
  <sub>topics: —</sub>
- **[yandexdataschool/Practical_RL](https://github.com/yandexdataschool/Practical_RL)** · 6,565★ · Jupyter Notebook · Mature  
  A course in reinforcement learning in the wild — the RL foundations under DPO/GRPO.  
  <sub>topics: reinforcement-learning, course-materials, deep-learning, deep-reinforcement-learning, git-course, mooc, tensorflow, pytorch</sub>
- **[unslothai/notebooks](https://github.com/unslothai/notebooks)** · 5,633★ · Jupyter Notebook · Hot  
  250+ ready-to-run fine-tuning & RL notebooks (text, vision, audio, TTS, embeddings) — the recipe box.  
  <sub>topics: unsloth</sub>
- **[SylphAI-Inc/LLM-engineer-handbook](https://github.com/SylphAI-Inc/LLM-engineer-handbook)** · 5,027★ · — · Abandoned  
  Curated map of training/serving/fine-tuning resources — orientation, not code.  
  <sub>topics: —</sub>
- **[pico-lm/pico-train](https://github.com/pico-lm/pico-train)** · 319★ · Python · Declining  
  Minimalistic framework for *transparently* training LMs — every checkpoint + activation logged for research.  
  <sub>topics: —</sub>

### Domain & on-device tuning

_Fine-tuning beyond cloud-GPU text LLMs: vision models, speech distillation, RAG systems, and Apple-Silicon-native training._

- **[roboflow/rf-detr](https://github.com/roboflow/rf-detr)** · 9,077★ · Python · Hot  
  Real-time detection/segmentation architecture built to be fine-tuned on custom vision datasets.  
  <sub>topics: computer-vision, detr, machine-learning, object-detection, rf-detr, instance-segmentation, sota</sub>
- **[Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)** · 5,428★ · Python · Mature  
  Fine-tune and run vision-language models natively on Apple Silicon via MLX — unified memory instead of CUDA.  
  <sub>topics: llava, llm, mlx, vision-transformer, apple-silicon, idefics, local-ai, paligemma</sub>
- **[huggingface/distil-whisper](https://github.com/huggingface/distil-whisper)** · 4,112★ · Python · Abandoned  
  Knowledge distillation applied: Whisper 6× faster / 50% smaller within 1% WER — the distillation reference recipe.  
  <sub>topics: audio, speech-recognition, whisper</sub>
- **[VectorInstitute/fed-rag](https://github.com/VectorInstitute/fed-rag)** · 150★ · Python · Declining  
  Fine-tune RAG systems end-to-end (retriever + generator), including federated setups.  
  <sub>topics: deep-learning, federated-learning, llms, machine-learning, rag</sub>

### Hardware fit & serving

_Before and after the training run: planning what fits, and serving the tuned adapters/weights — including the many-adapters and tiny-GPU cases._

- **[AlexsJones/llmfit](https://github.com/AlexsJones/llmfit)** · 34,371★ · Rust · Hot  
  One command to find which models your hardware can run or train — the planning step before any tuning run.  
  <sub>topics: llm, skill, localai, gguf, mlx, unsloth</sub>
- **[lyogavin/airllm](https://github.com/lyogavin/airllm)** · 32,693★ · Jupyter Notebook · Mature  
  Layer-by-layer offloading: 70B-class inference on a single 4GB GPU — run what you tuned on tiny hardware.  
  <sub>topics: chinese-nlp, finetune, generative-ai, instruct-gpt, instruction-set, llama, llm, lora</sub>
- **[transformerlab/transformerlab-app](https://github.com/transformerlab/transformerlab-app)** · 5,180★ · Python · Mature  
  Open research workbench GUI: train, tune, evaluate and chat with models locally (CUDA + MLX backends).  
  <sub>topics: electron, llama, llms, lora, rlhf, transformers, mlx, diffusion</sub>
- **[predibase/lorax](https://github.com/predibase/lorax)** · 3,826★ · Python · Mature  
  Multi-LoRA inference server — dynamically batch 1000s of fine-tuned adapters on one GPU.  
  <sub>topics: fine-tuning, gpt, llama, llm, llm-inference, llm-serving, llmops, lora</sub>

## Spotlight: SFT → DPO → GRPO — post-training became a ladder

Fine-tuning in 2024 meant one thing: LoRA on instruction data. The 2026 stack is a **ladder of increasingly behavioral objectives**, and your stars cover every rung:

- **SFT commoditized.** `unsloth`, `LlamaFactory` and `axolotl` reached feature parity (all: LoRA/QLoRA, full FT, DPO, GRPO, VLMs). Differentiation moved to kernels (`unsloth`: ~2× faster, ~70% less VRAM on one GPU) and workflow (zero-code UI vs YAML).
- **Alignment standardized.** `trl` v1.0 unified SFT, reward modeling, DPO and GRPO into one library — every framework above now wraps its trainers rather than reimplementing them.
- **The agent turn.** Single-turn GRPO trains chatbots; agents need credit assignment across *multi-turn tool-use rollouts*. That's `ART`'s pitch (vLLM-powered rollouts, TRL/Unsloth training), `OpenEnv`'s environment interface, and `OpenClaw-RL`'s train-by-talking layer.
- **The contrarian rung.** `Memento` fine-tunes the agent's episodic *memory* instead of its weights — worth knowing before you spend GPU-weeks: sometimes the cheapest post-training is no training.
- **What's deliberately absent**: datacenter-scale async RL (verl, OpenRLHF) isn't in your stars — if you outgrow `ART`/`trl` scale, that's the next ecosystem to evaluate.

## Graph analysis — how they relate

**Community clustering.** These 27 tools span **11 of the graph's 35 communities**.

- **Community 21** (8): `hiyouga/LlamaFactory`, `huggingface/transformers`, `huggingface/peft`, `huggingface/trl`, `huggingface/OpenEnv`, `huggingface/distil-whisper`, `lyogavin/airllm`, `predibase/lorax`
- **Community 18** (6): `Lightning-AI/pytorch-lightning`, `PaddlePaddle/PaddleNLP`, `rasbt/LLMs-from-scratch`, `labmlai/annotated_deep_learning_paper_implementations`, `yandexdataschool/Practical_RL`, `roboflow/rf-detr`
- **Community 22** (2): `unslothai/unsloth`, `unslothai/notebooks`
- **Community 7** (2): `axolotl-ai-cloud/axolotl`, `Blaizzy/mlx-vlm`
- **Community 20** (2): `Gen-Verse/OpenClaw-RL`, `AlexsJones/llmfit`
- **Community 0** (2): `Memento-Teams/Memento`, `pico-lm/pico-train`

**Centrality (PageRank in the full 1,752-repo graph)** — most 'hub-like' training tools in your ecosystem:

- `Lightning-AI/pytorch-lightning` — PageRank 0.0027
- `huggingface/peft` — PageRank 0.0013
- `axolotl-ai-cloud/axolotl` — PageRank 0.0012
- `huggingface/trl` — PageRank 0.0009
- `huggingface/OpenEnv` — PageRank 0.0008
- `huggingface/transformers` — PageRank 0.0008
- `roboflow/rf-detr` — PageRank 0.0007
- `predibase/lorax` — PageRank 0.0007
- `huggingface/distil-whisper` — PageRank 0.0006
- `unslothai/unsloth` — PageRank 0.0006

**Direct links between training tools** (top similarity edges where both endpoints are in this report):

- `unslothai/notebooks` ⇄ `unslothai/unsloth` (w=0.836) — topics: unsloth; authors: danielhanchen, Etherll, shimmyshimmer
- `huggingface/trl` ⇄ `huggingface/OpenEnv` (w=0.785) — authors: sergiopaniego, dependabot[bot]
- `huggingface/peft` ⇄ `huggingface/transformers` (w=0.736) — topics: llm, python, pytorch; authors: qgallouedec, kaixuanliu, jiqing-feng
- `huggingface/peft` ⇄ `huggingface/trl` (w=0.665) — authors: qgallouedec, dependabot[bot], albertvillanova
- `huggingface/distil-whisper` ⇄ `huggingface/transformers` (w=0.650) — topics: audio, speech-recognition
- `huggingface/peft` ⇄ `predibase/lorax` (w=0.362) — topics: llm, pytorch, transformers, lora
- `huggingface/peft` ⇄ `axolotl-ai-cloud/axolotl` (w=0.321) — topics: llm, fine-tuning; authors: dependabot[bot], latentofmythos@gmail.com
- `hiyouga/LlamaFactory` ⇄ `unslothai/unsloth` (w=0.300) — topics: fine-tuning, llama, llm, qwen
- `rasbt/LLMs-from-scratch` ⇄ `Lightning-AI/pytorch-lightning` (w=0.300) — topics: python, pytorch, ai, artificial-intelligence
- `hiyouga/LlamaFactory` ⇄ `predibase/lorax` (w=0.290) — topics: fine-tuning, llama, llm, transformers
- `huggingface/peft` ⇄ `hiyouga/LlamaFactory` (w=0.250) — topics: llm, transformers, lora, fine-tuning
- `Blaizzy/mlx-vlm` ⇄ `axolotl-ai-cloud/axolotl` (w=0.201) — topics: llm; authors: Anai-Guo
- `AlexsJones/llmfit` ⇄ `axolotl-ai-cloud/axolotl` (w=0.187) — topics: llm; authors: dependabot[bot]
- `AlexsJones/llmfit` ⇄ `unslothai/notebooks` (w=0.167) — topics: unsloth
- `lyogavin/airllm` ⇄ `predibase/lorax` (w=0.143) — topics: llama, llm, lora
- …and 1 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| huggingface/transformers | 100 | Classic | very active | 6 | 23% | 272 |
| huggingface/peft | 95 | Classic | very active | 5 | 20% | 33 |
| AlexsJones/llmfit | 88 | Hot | very active | 3 | 22% | 129 |
| hiyouga/LlamaFactory | 84 | Classic | very active | 7 | 10% | 36 |
| axolotl-ai-cloud/axolotl | 84 | Classic | very active | 2 | 30% | 32 |
| Blaizzy/mlx-vlm | 84 | Mature | very active | 2 | 40% | 80 |
| roboflow/rf-detr | 84 | Hot | very active | 2 | 44% | 28 |
| unslothai/unsloth | 83 | Mature | very active | 2 | 43% | 58 |
| huggingface/trl | 80 | Classic | very active | 1 | 54% | 95 |
| transformerlab/transformerlab-app | 78 | Mature | very active | 1 | 83% | 114 |
| Lightning-AI/pytorch-lightning | 76 | Classic | very active | 2 | 42% | 174 |
| OpenPipe/ART | 75 | Hot | very active | 1 | 60% | 59 |
| huggingface/OpenEnv | 74 | Hot | very active | 1 | 55% | 7 |
| lyogavin/airllm | 65 | Mature | very active | 1 | 100% | 4 |
| rasbt/LLMs-from-scratch | 57 | Mature | active | 2 | 44% | 0 |
| unslothai/notebooks | 55 | Hot | very active | 1 | 84% | 0 |
| PaddlePaddle/PaddleNLP | 32 | Mature | slowing | 0 | 0% | 49 |
| VectorInstitute/fed-rag | 32 | Declining | slowing | 0 | 0% | 35 |
| predibase/lorax | 27 | Mature | slowing | 0 | 0% | 21 |
| yandexdataschool/Practical_RL | 26 | Mature | slowing | 0 | 0% | 2 |
| Gen-Verse/OpenClaw-RL | 24 | Declining | slowing | 0 | 0% | 0 |
| pico-lm/pico-train | 21 | Declining | stale | 0 | 0% | 1 |
| labmlai/annotated_deep_learning_paper_implementations | 20 | Declining | stale | 0 | 0% | 0 |
| karpathy/nanoGPT | 9 | Declining | stale | 0 | 0% | 0 |
| Memento-Teams/Memento | 8 | Declining | stale | 0 | 0% | 0 |
| SylphAI-Inc/LLM-engineer-handbook | 5 | Abandoned | stale | 0 | 0% | 0 |
| huggingface/distil-whisper | 4 | Abandoned | stale | 0 | 0% | 0 |

Watch items: `nanoGPT` and most learn-by-building repos read as frozen — expected and fine for their purpose, but don't depend on them. `distil-whisper` is abandoned in this snapshot (the *technique* lives on in papers and Whisper forks). `Memento` has gone quiet since its paper. `lorax` is slowing (single-maintainer, ~2 months between pushes) — if adapter serving is on your critical path, benchmark vLLM's multi-LoRA as the fallback. `PaddleNLP` is healthy mainly inside the Paddle ecosystem.

## Which one should you use?

- **One consumer GPU, weekend project** → `unsloth` (fastest, least VRAM), recipes from `unslothai/notebooks`.
- **You want a UI, not YAML** → `LlamaFactory` (LlamaBoard) or `transformerlab-app` (research workbench).
- **Team runs, reproducible configs, multi-GPU** → `axolotl`.
- **You're aligning, not just tuning** → `trl` directly (SFT→DPO→GRPO), frameworks when convenient.
- **Training an *agent*, not a chatbot** → `ART` (+ `OpenEnv` for environments); read `Memento` first to check whether memory beats weights for your case.
- **You want to *understand* it** → `LLMs-from-scratch` cover to cover, then `nanoGPT`, then `pico-train` for introspection.
- **Mac-only hardware** → `mlx-vlm` and the MLX ecosystem.
- **After training** → `lorax` for many adapters, `airllm` for big models on tiny GPUs, `llmfit` *before* all of this to plan the fit.

## Adjacent (deliberately not listed as training tools)

- **vllm-project/vllm** (90,249★) — the serving standard for *finished* models — covered in the local-vs-infra-stack report
- **ollama/ollama** (179,588★) — local inference runtime, not a trainer — see local-vs-infra-stack
- **flyteorg/flyte** (7,281★) — general ML/data orchestration — schedules training, doesn't implement it
- **beam-cloud/beta9** (1,756★) — serverless GPU substrate *where* you train, not *how*
- **zai-org/GLM-V** (2,377★) — open model weights trained with scalable RL — a result of this stack, not a tool in it
- **openai/CLIP** (34,240★) — landmark pretraining research, effectively frozen — read it, don't build on the repo
- **NVIDIA/physicsnemo** (3,205★) — training framework for physics/simulation models, out of LLM post-training scope
- **facebookresearch/BenchMARL** (654★) — multi-agent RL *benchmarking* research, not LLM post-training
- **microsoft/generative-ai-for-beginners** (118,665★) — general GenAI curriculum — broader than training

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json` for all repo metrics and graph structure. No API calls at generation time; fully reproducible.
- **Selection**: keyword scan (fine-tune / lora / peft / post-train / rlhf / grpo / dpo / pretrain / distill) + manual curation into ladder stages. Serving runtimes, orchestrators, and model-weight repos were routed to adjacent reports or excluded (see above).
- **Task rankings** additionally cite external evidence gathered 2026-07: the [Spheron](https://www.spheron.network/blog/axolotl-vs-unsloth-vs-torchtune/) and [index.dev](https://www.index.dev/skill-vs-skill/ai-axolotl-vs-llama-factory-vs-unsloth) framework comparisons (A100/RTX-4070 timings), the [Turing Post agent-RL tools survey](https://www.turingpost.com/p/agent-rl-training-tools), Hugging Face's [async-RL landscape post](https://huggingface.co/blog/async-rl-training-landscape), the [OpenPipe ART announcement](https://openpipe.ai/blog/art-trainer-a-new-rl-trainer-for-agents), and MLX ecosystem docs. Timings are point-in-time and partly vendor-reported — treat rankings as defaults, not verdicts.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity; benchmark citations are frozen text and need manual review when major releases land.

<sub>Tools covered: 27 · Snapshot: 2026-08-28T01:21:50.535Z</sub>
