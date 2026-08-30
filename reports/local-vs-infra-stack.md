# Local vs High-Infra AI Stack — A Deployment-Tier Comparison

> Derived from **kaiser-data**'s 1,859 starred repos (snapshot `2026-08-29T23:54:34.573Z`), cross-referenced with the repo-similarity graph (1,859 nodes / 6,070 edges, 37 communities).
>
> Generated 2026-08-30 by `scripts/reports/local_vs_infra_stack.py` (regenerate any time — no API cost).

![Top tools by stars](assets/local-vs-infra-stack-top-tools.svg)

![Tools per category](assets/local-vs-infra-stack-categories.svg)


## Executive summary

- **39 stack tools** in your stars (**1,805,415★** combined), mapped to every layer of a self-hosted AI stack and tagged by deployment tier:
  - 🟢 **Local / edge** (15) — laptop, single consumer GPU, on-device, zero ops
  - 🟡 **Scales both** (16) — same tool, local *or* cluster, config-dependent
  - 🔴 **High-infra** (8) — multi-GPU / datacenter / high-QPS / k8s
- **The core split is the inference runtime.** Local tier optimizes for *one* of you on *one* box (`ollama`, `llama.cpp`, `llamafile`); high-infra optimizes for *throughput across many GPUs* (`vllm`, `sglang`, `lmdeploy`). Everything else (gateway, vector store, agent logic) is mostly the same code with a different deployment target.
- **Don't pick a runtime per tool — pick a tier, then fill each layer.** The two reference stacks below do exactly that.
- **The 🟡 'scales both' tools are the safe bets** when you'll start local and grow: `litellm` (gateway), `pgvector`/`qdrant`/`chroma` (store), `transformers`/`peft`, the agent frameworks, and `langfuse`/`phoenix` all migrate without a rewrite.

## The two reference stacks

Same job at every layer — different tier. Pick a column and go.

| Layer | 🟢 Fully-local stack | 🔴 High-infra stack |
|---|---|---|
| **Inference runtime** | `ollama/ollama` | `vllm-project/vllm` |
| **Scaling infra** | `— (single node)` | `skypilot-org/skypilot` |
| **Cost optimization** | `GGUF quant (llama.cpp)` | `vllm-project/llm-compressor` |
| **Gateway / UI** | `open-webui/open-webui` | `BerriAI/litellm` |
| **Vector store** | `lancedb / pgvector` | `milvus-io/milvus (or clustered qdrant)` |
| **Fine-tuning** | `unslothai/unsloth` | `axolotl-ai-cloud/axolotl` |
| **Agent logic** | `pydantic/pydantic-ai` | `pydantic/pydantic-ai (same)` |
| **Observability** | `promptfoo/promptfoo` | `langfuse/langfuse` |

**Reading it:** the agent logic and observability *code* is identical across columns — only the runtime, scaling, store, and trainer change as you move from one box to a fleet.

## The stack, layer by layer

### Inference runtime

_Where the model actually executes. This is the layer where the local/high-infra distinction is sharpest._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [ollama/ollama](https://github.com/ollama/ollama) | 🟢 Local | 179,588 | Go | Classic | The zero-config local default — `ollama run`, model registry, OpenAI-compatible API. Laptop-to-server, but single-node. |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 🟢 Local | 125,969 | C++ | Classic | The CPU/edge engine under everything — GGUF quantization, runs on a Raspberry Pi to a Mac; the embeddable substrate. |
| [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | 🟢 Local | 77,396 | C++ | Abandoned | Desktop-first local LLM app + bindings; privacy-focused, runs on plain CPUs. |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | 🟢 Local | 48,711 | Go | Classic | Self-hosted, OpenAI-drop-in engine for LLM/TTS/STT/image on commodity hardware — the all-in-one local server. |
| [mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile) | 🟢 Local | 25,707 | C++ | Mature | One file = one runnable model. Maximum portability for shipping a local model with no install. |
| [microsoft/foundry-local](https://github.com/microsoft/foundry-local) | 🟢 Local | 2,528 | C++ | Hot | Microsoft's on-device runtime — offline LLM + Whisper, hardware-accelerated where available. |
| [huggingface/transformers](https://github.com/huggingface/transformers) | 🟡 Both | 164,519 | Python | Classic | The model-definition library every runtime builds on; runs a notebook locally or a training cluster — the common denominator. |
| [exo-explore/exo](https://github.com/exo-explore/exo) | 🟡 Both | 47,102 | Python | Mature | Stitches a *cluster out of your local devices* (phones, Macs, PCs) to run big models — distributed but home-grown. |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 🔴 Infra | 90,249 | Python | Classic | The production serving standard — PagedAttention, continuous batching, tensor/pipeline parallelism for high QPS on GPU fleets. |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | 🔴 Infra | 32,584 | Python | Mature | High-throughput serving with RadixAttention prefix caching — excels at structured/agentic workloads at scale. |
| [InternLM/lmdeploy](https://github.com/InternLM/lmdeploy) | 🔴 Infra | 8,029 | Python | Classic | Toolkit for compressing + serving LLMs at scale (TurboMind engine); quantization-aware high-throughput inference. |

### Scaling / serving infra

_How you get a runtime onto many machines, cheaply. Only relevant once you outgrow a single node._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [skypilot-org/skypilot](https://github.com/skypilot-org/skypilot) | 🔴 Infra | 10,530 | Python | Classic | Run/serve LLMs across any cloud or k8s with cost-aware scheduling & spot recovery — the multi-cloud orchestration layer. |
| [vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor) | 🔴 Infra | 3,734 | Python | Mature | Quantize/sparsify models (GPTQ/AWQ/SmoothQuant) so they serve cheaper on vLLM — the cost-optimization step. |

### Model gateway & UI

_What sits in front of the model(s) — a chat UI for one user, or a proxy that fans out across providers for a whole org._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | 🟢 Local | 150,148 | Python | Mature | The self-hosted ChatGPT-style UI for local models (pairs with Ollama) — RAG, users, tools, fully offline. |
| [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | 🟢 Local | 65,305 | JavaScript | Classic | All-in-one desktop/self-host app: chat + RAG + agents over local or API models. |
| [janhq/jan](https://github.com/janhq/jan) | 🟢 Local | 44,213 | TypeScript | Classic | Open-source desktop ChatGPT alternative that runs models 100% on your machine. |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | 🟡 Both | 57,425 | Python | Classic | One OpenAI-compatible API over 100+ providers + a self-hostable proxy with keys/budgets/routing — local or enterprise gateway. |
| [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway) | 🟡 Both | 12,842 | TypeScript | Mature | Fast AI gateway with routing, fallbacks, caching, and guardrails — drop in front of any tier. |

### Vector store

_Where embeddings live for RAG. Many of these span tiers — start embedded, cluster later._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | 🟢 Local | 40,812 | C++ | Classic | The in-process ANN library — no server, embed it in your app; the index inside many of the DBs below. |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 🟢 Local | 15,528 | C++ | Hot | Lightweight, lightning-fast in-process vector database for embedded use. |
| [neuml/txtai](https://github.com/neuml/txtai) | 🟢 Local | 12,910 | Python | Classic | All-in-one embeddings DB + RAG + workflows in one local package. |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | 🟢 Local | 11,298 | Rust | Classic | Embedded, serverless vector DB (Lance columnar format) — zero-ops local RAG that still handles large on-disk sets. |
| [redis/redis](https://github.com/redis/redis) | 🟡 Both | 76,125 | C | Classic | The in-memory store you already run, now with vector search — local cache to HA cluster. |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | 🟡 Both | 34,228 | Rust | Classic | Rust vector DB — single-binary local, but clusters with sharding/replication for billions of vectors. |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | 🟡 Both | 29,166 | Rust | Classic | AI-native store that runs embedded for prototyping and client/server for production — the easy on-ramp. |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | 🟡 Both | 22,787 | C | Classic | Vector search inside the Postgres you already run — scales from a laptop to a managed cluster with no new infra. |
| [marqo-ai/marqo](https://github.com/marqo-ai/marqo) | 🟡 Both | 5,029 | Python | Mature | End-to-end vector search that bundles embedding inference; deploys local or distributed. |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | 🔴 Infra | 45,834 | Go | Classic | The billion-scale, distributed OSS vector DB — heavy ops footprint, built for datacenter scale. |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | 🔴 Infra | 16,757 | Go | Classic | Cloud-native vector DB with hybrid search & modules — designed for clustered, multi-tenant deployments. |

### Fine-tuning

_Adapting a model. LoRA on one GPU vs. multi-node full fine-tunes._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | 🟢 Local | 74,995 | Python | Mature | 2× faster, lower-VRAM fine-tuning — train a LoRA on a single consumer GPU (even Colab). |
| [huggingface/peft](https://github.com/huggingface/peft) | 🟡 Both | 21,600 | Python | Classic | Parameter-efficient fine-tuning (LoRA/QLoRA/adapters) — one consumer GPU or a multi-node run. |
| [axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) | 🔴 Infra | 12,413 | Python | Classic | Config-driven fine-tuning that scales to multi-GPU/multi-node (DeepSpeed/FSDP) — the cluster-grade trainer. |

### Agent framework

_The orchestration logic — deliberately tier-agnostic; it targets whatever endpoint you give it._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 🟡 Both | 57,688 | Python | Mature | Role-based multi-agent framework — runs against any model backend, local or hosted. |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 🟡 Both | 51,894 | Python | Classic | Data/agent framework — point it at a local Ollama or a cloud endpoint; tier-agnostic. |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 🟡 Both | 40,570 | Python | Classic | Graph/stateful agent runtime — the orchestration logic is independent of where the model runs. |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | 🟡 Both | 19,541 | Python | Mature | Type-safe agent framework; model-agnostic, so the same code targets either tier. |

### Observability & eval

_Tracing, metrics, and evals. Most self-host locally and also offer managed cloud._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 🟢 Local | 24,623 | TypeScript | Classic | CLI-first prompt/model eval that runs entirely on your machine in CI — no backend needed. |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | 🟡 Both | 33,820 | TypeScript | Classic | Self-hostable LLM tracing/eval/metrics — runs in Docker locally or as managed cloud. |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | 🟡 Both | 11,218 | Python | Classic | Open-source LLM observability you can run locally; OTel-native tracing + evals. |

## Which tier should you use?

| Your situation | Tier | Runtime to start with |
|---|---|---|
| Laptop / Mac, privacy, one user | 🟢 Local | `ollama` (+ `open-webui`) |
| Single consumer GPU (e.g. 1×4090) | 🟢 Local | `ollama` or `llama.cpp` w/ GGUF |
| CPU-only / edge / air-gapped | 🟢 Local | `llama.cpp` / `llamafile` / `LocalAI` |
| Prototype now, scale later | 🟡 Both | `vllm` behind `litellm`; `pgvector` store |
| Many users, steady traffic | 🔴 Infra | `vllm` (continuous batching) |
| Agentic / structured-output at scale | 🔴 Infra | `sglang` (RadixAttention) |
| Multi-cloud / spot-GPU cost control | 🔴 Infra | `vllm` orchestrated by `skypilot` |
| Pool several home devices | 🟡 Both | `exo-explore/exo` |

## Master comparison (operational metrics)

Sorted by tier then stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Layer | Tier | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [ollama](https://github.com/ollama/ollama) | Inference runtime | Local | Go | MIT | 179,588 | Classic | 83 | very active | 2d ago | 9 |
| [open-webui](https://github.com/open-webui/open-webui) | Model gateway & UI | Local | Python | NOASSERTION | 150,148 | Mature | 80 | very active | 2d ago | 5 |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Inference runtime | Local | C++ | MIT | 125,969 | Classic | 99 | very active | 2d ago | 48 |
| [gpt4all](https://github.com/nomic-ai/gpt4all) | Inference runtime | Local | C++ | MIT | 77,396 | Abandoned | 7 | stale | 1.3y ago | 0 |
| [unsloth](https://github.com/unslothai/unsloth) | Fine-tuning | Local | Python | Apache-2.0 | 74,995 | Mature | 83 | very active | 2d ago | 21 |
| [anything-llm](https://github.com/Mintplex-Labs/anything-llm) | Model gateway & UI | Local | JavaScript | MIT | 65,305 | Classic | 79 | very active | 2d ago | 20 |
| [LocalAI](https://github.com/mudler/LocalAI) | Inference runtime | Local | Go | MIT | 48,711 | Classic | 84 | very active | 2d ago | 12 |
| [jan](https://github.com/janhq/jan) | Model gateway & UI | Local | TypeScript | NOASSERTION | 44,213 | Classic | 79 | very active | 3d ago | 6 |
| [faiss](https://github.com/facebookresearch/faiss) | Vector store | Local | C++ | MIT | 40,812 | Classic | 94 | very active | 3d ago | 34 |
| [llamafile](https://github.com/mozilla-ai/llamafile) | Inference runtime | Local | C++ | NOASSERTION | 25,707 | Mature | 66 | very active | 3d ago | 5 |
| [promptfoo](https://github.com/promptfoo/promptfoo) | Observability & eval | Local | TypeScript | MIT | 24,623 | Classic | 84 | very active | 2d ago | 10 |
| [zvec](https://github.com/alibaba/zvec) | Vector store | Local | C++ | Apache-2.0 | 15,528 | Hot | 93 | very active | 3d ago | 19 |
| [txtai](https://github.com/neuml/txtai) | Vector store | Local | Python | Apache-2.0 | 12,910 | Classic | 80 | very active | 2d ago | 17 |
| [lancedb](https://github.com/lancedb/lancedb) | Vector store | Local | Rust | Apache-2.0 | 11,298 | Classic | 87 | very active | 2d ago | 16 |
| [foundry-local](https://github.com/microsoft/foundry-local) | Inference runtime | Local | C++ | NOASSERTION | 2,528 | Hot | 87 | very active | 2d ago | 19 |
| [transformers](https://github.com/huggingface/transformers) | Inference runtime | Both | Python | Apache-2.0 | 164,519 | Classic | 99 | very active | 2d ago | 43 |
| [redis](https://github.com/redis/redis) | Vector store | Both | C | NOASSERTION | 76,125 | Classic | 97 | very active | 2d ago | 40 |
| [crewAI](https://github.com/crewAIInc/crewAI) | Agent framework | Both | Python | MIT | 57,688 | Mature | 84 | very active | 2d ago | 9 |
| [litellm](https://github.com/BerriAI/litellm) | Model gateway & UI | Both | Python | NOASSERTION | 57,425 | Classic | 84 | very active | 2d ago | 9 |
| [llama_index](https://github.com/run-llama/llama_index) | Agent framework | Both | Python | MIT | 51,894 | Classic | 97 | very active | 2d ago | 59 |
| [exo](https://github.com/exo-explore/exo) | Inference runtime | Both | Python | Apache-2.0 | 47,102 | Mature | 73 | active | 4d ago | 6 |
| [langgraph](https://github.com/langchain-ai/langgraph) | Agent framework | Both | Python | MIT | 40,570 | Classic | 77 | very active | 2d ago | 16 |
| [qdrant](https://github.com/qdrant/qdrant) | Vector store | Both | Rust | Apache-2.0 | 34,228 | Classic | 87 | very active | 2d ago | 15 |
| [langfuse](https://github.com/langfuse/langfuse) | Observability & eval | Both | TypeScript | NOASSERTION | 33,820 | Classic | 94 | very active | 2d ago | 16 |
| [chroma](https://github.com/chroma-core/chroma) | Vector store | Both | Rust | Apache-2.0 | 29,166 | Classic | 83 | very active | 3d ago | 10 |
| [pgvector](https://github.com/pgvector/pgvector) | Vector store | Both | C | NOASSERTION | 22,787 | Classic | 64 | very active | 10d ago | 3 |
| [peft](https://github.com/huggingface/peft) | Fine-tuning | Both | Python | Apache-2.0 | 21,600 | Classic | 95 | very active | 3d ago | 45 |
| [pydantic-ai](https://github.com/pydantic/pydantic-ai) | Agent framework | Both | Python | MIT | 19,541 | Mature | 83 | very active | 2d ago | 25 |
| [gateway](https://github.com/Portkey-AI/gateway) | Model gateway & UI | Both | TypeScript | MIT | 12,842 | Mature | 45 | slowing | 3mo ago | 0 |
| [phoenix](https://github.com/Arize-ai/phoenix) | Observability & eval | Both | Python | NOASSERTION | 11,218 | Classic | 84 | very active | 2d ago | 19 |
| [marqo](https://github.com/marqo-ai/marqo) | Vector store | Both | Python | Apache-2.0 | 5,029 | Mature | 47 | active | 22d ago | 0 |
| [vllm](https://github.com/vllm-project/vllm) | Inference runtime | Infra | Python | Apache-2.0 | 90,249 | Classic | 99 | very active | 2d ago | 78 |
| [milvus](https://github.com/milvus-io/milvus) | Vector store | Infra | Go | Apache-2.0 | 45,834 | Classic | 99 | very active | 2d ago | 33 |
| [sglang](https://github.com/sgl-project/sglang) | Inference runtime | Infra | Python | Apache-2.0 | 32,584 | Mature | 99 | very active | 2d ago | 48 |
| [weaviate](https://github.com/weaviate/weaviate) | Vector store | Infra | Go | BSD-3-Clause | 16,757 | Classic | 78 | very active | 2d ago | 9 |
| [axolotl](https://github.com/axolotl-ai-cloud/axolotl) | Fine-tuning | Infra | Python | Apache-2.0 | 12,413 | Classic | 84 | very active | 2d ago | 13 |
| [skypilot](https://github.com/skypilot-org/skypilot) | Scaling / serving infra | Infra | Python | Apache-2.0 | 10,530 | Classic | 89 | very active | 2d ago | 19 |
| [lmdeploy](https://github.com/InternLM/lmdeploy) | Inference runtime | Infra | Python | Apache-2.0 | 8,029 | Classic | 92 | very active | 2d ago | 23 |
| [llm-compressor](https://github.com/vllm-project/llm-compressor) | Scaling / serving infra | Infra | Python | Apache-2.0 | 3,734 | Mature | 89 | very active | 2d ago | 35 |

## Graph analysis — how the stack hangs together

**Community clustering.** These 39 tools span **12 of the graph's 37 communities** — the stack cuts across the inference, RAG/vector, and agent neighborhoods rather than forming one cluster.

- **Community 18** (8): `ollama/ollama`, `nomic-ai/gpt4all`, `vllm-project/vllm`, `sgl-project/sglang`, `InternLM/lmdeploy`, `huggingface/transformers`, `vllm-project/llm-compressor`, `huggingface/peft`
- **Community 8** (8): `Mintplex-Labs/anything-llm`, `lancedb/lancedb`, `pgvector/pgvector`, `alibaba/zvec`, `neuml/txtai`, `qdrant/qdrant`, `weaviate/weaviate`, `milvus-io/milvus`
- **Community 14** (6): `BerriAI/litellm`, `Portkey-AI/gateway`, `axolotl-ai-cloud/axolotl`, `langfuse/langfuse`, `Arize-ai/phoenix`, `promptfoo/promptfoo`
- **Community 11** (4): `open-webui/open-webui`, `redis/redis`, `unslothai/unsloth`, `pydantic/pydantic-ai`
- **Community 2** (3): `ggml-org/llama.cpp`, `mozilla-ai/llamafile`, `marqo-ai/marqo`
- **Community 16** (2): `skypilot-org/skypilot`, `facebookresearch/faiss`
- **Community 19** (2): `janhq/jan`, `langchain-ai/langgraph`
- **Community 10** (2): `chroma-core/chroma`, `crewAIInc/crewAI`

**Centrality (PageRank in the full 1,859-repo graph)** — the 'hub' tools your other stars cluster around:

- `langchain-ai/langgraph` — PageRank 0.0016 (🟡 Both)
- `crewAIInc/crewAI` — PageRank 0.0013 (🟡 Both)
- `axolotl-ai-cloud/axolotl` — PageRank 0.0013 (🔴 Infra)
- `huggingface/peft` — PageRank 0.0012 (🟡 Both)
- `chroma-core/chroma` — PageRank 0.0010 (🟡 Both)
- `microsoft/foundry-local` — PageRank 0.0010 (🟢 Local)
- `ggml-org/llama.cpp` — PageRank 0.0010 (🟢 Local)
- `neuml/txtai` — PageRank 0.0009 (🟢 Local)
- `mudler/LocalAI` — PageRank 0.0008 (🟢 Local)
- `weaviate/weaviate` — PageRank 0.0008 (🔴 Infra)

**Direct links between stack tools** (top similarity edges where both endpoints are in this report):

- `huggingface/peft` ⇄ `huggingface/transformers` (w=0.736) — topics: llm, python, pytorch; authors: qgallouedec, kaixuanliu, jiqing-feng
- `vllm-project/llm-compressor` ⇄ `vllm-project/vllm` (w=0.550)
- `weaviate/weaviate` ⇄ `qdrant/qdrant` (w=0.429) — topics: search-engine, vector-search, vector-search-engine, vector-database
- `vllm-project/vllm` ⇄ `sgl-project/sglang` (w=0.407) — topics: llm, transformer, inference, llama
- `lancedb/lancedb` ⇄ `weaviate/weaviate` (w=0.400) — topics: approximate-nearest-neighbor-search, image-search, nearest-neighbor-search, recommender-system
- `lancedb/lancedb` ⇄ `qdrant/qdrant` (w=0.389) — topics: image-search, nearest-neighbor-search, recommender-system, search-engine; authors: dependabot[bot]
- `BerriAI/litellm` ⇄ `Portkey-AI/gateway` (w=0.348) — topics: langchain, llm, llmops, openai
- `huggingface/peft` ⇄ `axolotl-ai-cloud/axolotl` (w=0.321) — topics: llm, fine-tuning; authors: dependabot[bot], latentofmythos@gmail.com
- `lancedb/lancedb` ⇄ `alibaba/zvec` (w=0.294) — topics: search-engine, semantic-search, similarity-search, vector-database; authors: dependabot[bot]
- `sgl-project/sglang` ⇄ `ollama/ollama` (w=0.269) — topics: llama, llm, deepseek, gpt-oss
- `unslothai/unsloth` ⇄ `open-webui/open-webui` (w=0.257) — topics: llms, llm, openai, self-hosted
- `InternLM/lmdeploy` ⇄ `axolotl-ai-cloud/axolotl` (w=0.251) — topics: llm; authors: Anai-Guo, latentofmythos@gmail.com
- `lancedb/lancedb` ⇄ `pgvector/pgvector` (w=0.250) — topics: approximate-nearest-neighbor-search, nearest-neighbor-search
- `huggingface/transformers` ⇄ `sgl-project/sglang` (w=0.244) — topics: transformer, deepseek, glm, llm
- `milvus-io/milvus` ⇄ `weaviate/weaviate` (w=0.202) — topics: nearest-neighbor-search, vector-search, image-search, hnsw
- …and 4 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). For infra you'll depend on, weight health + activity heavily.

| Tool | Tier | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|---|
| llama.cpp | Local | 99 | Classic | very active | 6 | 17% | 6977 |
| vllm | Infra | 99 | Classic | very active | 28 | 6% | 104 |
| sglang | Infra | 99 | Mature | very active | 11 | 12% | 59 |
| transformers | Both | 99 | Classic | very active | 6 | 23% | 272 |
| milvus | Infra | 99 | Classic | very active | 8 | 12% | 170 |
| redis | Both | 97 | Classic | very active | 7 | 11% | 150 |
| llama_index | Both | 97 | Classic | very active | 16 | 6% | 496 |
| peft | Both | 95 | Classic | very active | 5 | 20% | 33 |
| faiss | Local | 94 | Classic | very active | 4 | 27% | 28 |
| langfuse | Both | 94 | Classic | very active | 4 | 23% | 666 |
| zvec | Local | 93 | Hot | very active | 4 | 23% | 11 |
| lmdeploy | Infra | 92 | Classic | very active | 4 | 21% | 69 |
| skypilot | Infra | 89 | Classic | very active | 3 | 22% | 42 |
| llm-compressor | Infra | 89 | Mature | very active | 3 | 31% | 32 |
| foundry-local | Local | 87 | Hot | very active | 3 | 22% | 22 |
| lancedb | Local | 87 | Classic | very active | 3 | 22% | 487 |
| qdrant | Both | 87 | Classic | very active | 3 | 34% | 116 |
| LocalAI | Local | 84 | Classic | very active | 2 | 47% | 136 |
| litellm | Both | 84 | Classic | very active | 2 | 41% | 1446 |
| axolotl | Infra | 84 | Classic | very active | 2 | 30% | 32 |
| crewAI | Both | 84 | Mature | very active | 2 | 47% | 232 |
| phoenix | Both | 84 | Classic | very active | 2 | 38% | 793 |
| promptfoo | Local | 84 | Classic | very active | 2 | 49% | 422 |
| ollama | Local | 83 | Classic | very active | 2 | 35% | 249 |
| chroma | Both | 83 | Classic | very active | 2 | 48% | 137 |
| unsloth | Local | 83 | Mature | very active | 2 | 43% | 58 |
| pydantic-ai | Both | 83 | Mature | very active | 2 | 27% | 318 |
| open-webui | Local | 80 | Mature | very active | 1 | 72% | 168 |
| txtai | Local | 80 | Classic | very active | 1 | 51% | 67 |
| jan | Local | 79 | Classic | very active | 1 | 81% | 104 |
| anything-llm | Local | 79 | Classic | very active | 1 | 60% | 35 |
| weaviate | Infra | 78 | Classic | very active | 1 | 52% | 576 |
| langgraph | Both | 77 | Classic | very active | 1 | 60% | 561 |
| exo | Both | 73 | Mature | active | 3 | 17% | 16 |
| llamafile | Local | 66 | Mature | very active | 1 | 71% | 42 |
| pgvector | Both | 64 | Classic | very active | 1 | 98% | 0 |
| marqo | Both | 47 | Mature | active | 0 | 0% | 113 |
| gateway | Both | 45 | Mature | slowing | 0 | 0% | 81 |
| gpt4all | Local | 7 | Abandoned | stale | 0 | 0% | 38 |

## Adjacent (covered elsewhere)

- **ggml-org/whisper.cpp** (53,239★) — speech runtime — covered in the *voice-agents* report
- **comet-ml/opik** (21,642★) — eval/observability — see the *LLM-evaluation* report
- **confident-ai/deepeval** (17,914★) — eval framework — see the *LLM-evaluation* report
- **langchain-ai/langchain** (145,151★) — broad agent toolkit — see the *agent-orchestration* report
- **microsoft/autogen** (60,659★) — multi-agent framework — see the *agent-orchestration* report

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Tiering** is an editorial judgment about each tool's *sweet spot*, not a hard limit — many 🟢 tools can be pushed onto servers and some 🔴 tools run (slowly) on a laptop. The tag reflects what the project is *optimized and typically used* for.
- **Selection**: keyword scan (inference / serving / vllm / ollama / vector db / gateway / fine-tune / quantize) + manual curation into stack layers. Speech runtimes, pure eval frameworks, and broad agent toolkits were routed to adjacent reports.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 39 · Tiers: 15 local / 16 both / 8 infra · Snapshot: 2026-08-29T23:54:34.573Z</sub>
