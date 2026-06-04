# Local vs High-Infra AI Stack — A Deployment-Tier Comparison

> Derived from **kaiser-data**'s 1,185 starred repos (snapshot `2026-06-04T15:28:30.136Z`), cross-referenced with the repo-similarity graph (1,185 nodes / 3,849 edges, 26 communities).
>
> Generated 2026-06-04 by `scripts/reports/local_vs_infra_stack.py` (regenerate any time — no API cost).

## Executive summary

- **39 stack tools** in your stars (**1,688,714★** combined), mapped to every layer of a self-hosted AI stack and tagged by deployment tier:
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
| [ollama/ollama](https://github.com/ollama/ollama) | 🟢 Local | 172,956 | Go | Mature | The zero-config local default — `ollama run`, model registry, OpenAI-compatible API. Laptop-to-server, but single-node. |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 🟢 Local | 114,334 | C++ | Classic | The CPU/edge engine under everything — GGUF quantization, runs on a Raspberry Pi to a Mac; the embeddable substrate. |
| [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | 🟢 Local | 77,351 | C++ | Declining | Desktop-first local LLM app + bindings; privacy-focused, runs on plain CPUs. |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | 🟢 Local | 46,623 | Go | Classic | Self-hosted, OpenAI-drop-in engine for LLM/TTS/STT/image on commodity hardware — the all-in-one local server. |
| [mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile) | 🟢 Local | 24,626 | C++ | Mature | One file = one runnable model. Maximum portability for shipping a local model with no install. |
| [microsoft/Foundry-Local](https://github.com/microsoft/Foundry-Local) | 🟢 Local | 2,318 | C++ | Hot | Microsoft's on-device runtime — offline LLM + Whisper, hardware-accelerated where available. |
| [huggingface/transformers](https://github.com/huggingface/transformers) | 🟡 Both | 161,208 | Python | Classic | The model-definition library every runtime builds on; runs a notebook locally or a training cluster — the common denominator. |
| [exo-explore/exo](https://github.com/exo-explore/exo) | 🟡 Both | 45,142 | Python | Hot | Stitches a *cluster out of your local devices* (phones, Macs, PCs) to run big models — distributed but home-grown. |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 🔴 Infra | 81,744 | Python | Classic | The production serving standard — PagedAttention, continuous batching, tensor/pipeline parallelism for high QPS on GPU fleets. |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | 🔴 Infra | 28,899 | Python | Mature | High-throughput serving with RadixAttention prefix caching — excels at structured/agentic workloads at scale. |
| [InternLM/lmdeploy](https://github.com/InternLM/lmdeploy) | 🔴 Infra | 7,879 | Python | Mature | Toolkit for compressing + serving LLMs at scale (TurboMind engine); quantization-aware high-throughput inference. |

### Scaling / serving infra

_How you get a runtime onto many machines, cheaply. Only relevant once you outgrow a single node._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [skypilot-org/skypilot](https://github.com/skypilot-org/skypilot) | 🔴 Infra | 10,055 | Python | Classic | Run/serve LLMs across any cloud or k8s with cost-aware scheduling & spot recovery — the multi-cloud orchestration layer. |
| [vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor) | 🔴 Infra | 3,312 | Python | Hot | Quantize/sparsify models (GPTQ/AWQ/SmoothQuant) so they serve cheaper on vLLM — the cost-optimization step. |

### Model gateway & UI

_What sits in front of the model(s) — a chat UI for one user, or a proxy that fans out across providers for a whole org._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | 🟢 Local | 139,724 | Python | Mature | The self-hosted ChatGPT-style UI for local models (pairs with Ollama) — RAG, users, tools, fully offline. |
| [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | 🟢 Local | 60,949 | JavaScript | Classic | All-in-one desktop/self-host app: chat + RAG + agents over local or API models. |
| [janhq/jan](https://github.com/janhq/jan) | 🟢 Local | 42,821 | TypeScript | Mature | Open-source desktop ChatGPT alternative that runs models 100% on your machine. |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | 🟡 Both | 49,067 | Python | Mature | One OpenAI-compatible API over 100+ providers + a self-hostable proxy with keys/budgets/routing — local or enterprise gateway. |
| [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway) | 🟡 Both | 11,944 | TypeScript | Mature | Fast AI gateway with routing, fallbacks, caching, and guardrails — drop in front of any tier. |

### Vector store

_Where embeddings live for RAG. Many of these span tiers — start embedded, cluster later._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | 🟢 Local | 40,189 | C++ | Classic | The in-process ANN library — no server, embed it in your app; the index inside many of the DBs below. |
| [neuml/txtai](https://github.com/neuml/txtai) | 🟢 Local | 12,625 | Python | Classic | All-in-one embeddings DB + RAG + workflows in one local package. |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | 🟢 Local | 10,483 | HTML | Classic | Embedded, serverless vector DB (Lance columnar format) — zero-ops local RAG that still handles large on-disk sets. |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 🟢 Local | 9,742 | C++ | Hot | Lightweight, lightning-fast in-process vector database for embedded use. |
| [redis/redis](https://github.com/redis/redis) | 🟡 Both | 74,657 | C | Classic | The in-memory store you already run, now with vector search — local cache to HA cluster. |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | 🟡 Both | 31,755 | Rust | Classic | Rust vector DB — single-binary local, but clusters with sharding/replication for billions of vectors. |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | 🟡 Both | 28,190 | Rust | Classic | AI-native store that runs embedded for prototyping and client/server for production — the easy on-ramp. |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | 🟡 Both | 21,566 | C | Classic | Vector search inside the Postgres you already run — scales from a laptop to a managed cluster with no new infra. |
| [marqo-ai/marqo](https://github.com/marqo-ai/marqo) | 🟡 Both | 5,023 | Python | Classic | End-to-end vector search that bundles embedding inference; deploys local or distributed. |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | 🔴 Infra | 44,597 | Go | Classic | The billion-scale, distributed OSS vector DB — heavy ops footprint, built for datacenter scale. |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | 🔴 Infra | 16,264 | Go | Classic | Cloud-native vector DB with hybrid search & modules — designed for clustered, multi-tenant deployments. |

### Fine-tuning

_Adapting a model. LoRA on one GPU vs. multi-node full fine-tunes._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | 🟢 Local | 65,593 | Python | Mature | 2× faster, lower-VRAM fine-tuning — train a LoRA on a single consumer GPU (even Colab). |
| [huggingface/peft](https://github.com/huggingface/peft) | 🟡 Both | 21,225 | Python | Classic | Parameter-efficient fine-tuning (LoRA/QLoRA/adapters) — one consumer GPU or a multi-node run. |
| [axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) | 🔴 Infra | 12,001 | Python | Classic | Config-driven fine-tuning that scales to multi-GPU/multi-node (DeepSpeed/FSDP) — the cluster-grade trainer. |

### Agent framework

_The orchestration logic — deliberately tier-agnostic; it targets whatever endpoint you give it._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 🟡 Both | 52,682 | Python | Mature | Role-based multi-agent framework — runs against any model backend, local or hosted. |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 🟡 Both | 49,861 | Python | Classic | Data/agent framework — point it at a local Ollama or a cloud endpoint; tier-agnostic. |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 🟡 Both | 33,674 | Python | Mature | Graph/stateful agent runtime — the orchestration logic is independent of where the model runs. |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | 🟡 Both | 17,472 | Python | Hot | Type-safe agent framework; model-agnostic, so the same code targets either tier. |

### Observability & eval

_Tracing, metrics, and evals. Most self-host locally and also offer managed cloud._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 🟢 Local | 21,810 | TypeScript | Classic | CLI-first prompt/model eval that runs entirely on your machine in CI — no backend needed. |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | 🟡 Both | 28,386 | TypeScript | Classic | Self-hostable LLM tracing/eval/metrics — runs in Docker locally or as managed cloud. |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | 🟡 Both | 9,967 | Python | Classic | Open-source LLM observability you can run locally; OTel-native tracing + evals. |

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
| [ollama](https://github.com/ollama/ollama) | Inference runtime | Local | Go | MIT | 172,956 | Mature | 83 | very active | 2d ago | 13 |
| [open-webui](https://github.com/open-webui/open-webui) | Model gateway & UI | Local | Python | NOASSERTION | 139,724 | Mature | 80 | very active | 3d ago | 17 |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Inference runtime | Local | C++ | MIT | 114,334 | Classic | 99 | very active | 2d ago | 50 |
| [gpt4all](https://github.com/nomic-ai/gpt4all) | Inference runtime | Local | C++ | MIT | 77,351 | Declining | 7 | stale | 1.0y ago | 0 |
| [unsloth](https://github.com/unslothai/unsloth) | Fine-tuning | Local | Python | Apache-2.0 | 65,593 | Mature | 77 | very active | 2d ago | 23 |
| [anything-llm](https://github.com/Mintplex-Labs/anything-llm) | Model gateway & UI | Local | JavaScript | MIT | 60,949 | Classic | 79 | very active | 2d ago | 15 |
| [LocalAI](https://github.com/mudler/LocalAI) | Inference runtime | Local | Go | MIT | 46,623 | Classic | 79 | very active | 2d ago | 12 |
| [jan](https://github.com/janhq/jan) | Model gateway & UI | Local | TypeScript | NOASSERTION | 42,821 | Mature | 79 | very active | 3d ago | 2 |
| [faiss](https://github.com/facebookresearch/faiss) | Vector store | Local | C++ | MIT | 40,189 | Classic | 93 | very active | 2d ago | 31 |
| [llamafile](https://github.com/mozilla-ai/llamafile) | Inference runtime | Local | C++ | NOASSERTION | 24,626 | Mature | 62 | very active | 2d ago | 7 |
| [promptfoo](https://github.com/promptfoo/promptfoo) | Observability & eval | Local | TypeScript | MIT | 21,810 | Classic | 84 | very active | 2d ago | 17 |
| [txtai](https://github.com/neuml/txtai) | Vector store | Local | Python | Apache-2.0 | 12,625 | Classic | 77 | very active | 2d ago | 2 |
| [lancedb](https://github.com/lancedb/lancedb) | Vector store | Local | HTML | Apache-2.0 | 10,483 | Classic | 91 | very active | 2d ago | 26 |
| [zvec](https://github.com/alibaba/zvec) | Vector store | Local | C++ | Apache-2.0 | 9,742 | Hot | 91 | very active | 2d ago | 15 |
| [Foundry-Local](https://github.com/microsoft/Foundry-Local) | Inference runtime | Local | C++ | NOASSERTION | 2,318 | Hot | 89 | very active | 2d ago | 17 |
| [transformers](https://github.com/huggingface/transformers) | Inference runtime | Both | Python | Apache-2.0 | 161,208 | Classic | 99 | very active | 2d ago | 52 |
| [redis](https://github.com/redis/redis) | Vector store | Both | C | NOASSERTION | 74,657 | Classic | 97 | very active | 2d ago | 38 |
| [crewAI](https://github.com/crewAIInc/crewAI) | Agent framework | Both | Python | MIT | 52,682 | Mature | 80 | very active | 2d ago | 20 |
| [llama_index](https://github.com/run-llama/llama_index) | Agent framework | Both | Python | MIT | 49,861 | Classic | 99 | very active | 6d ago | 46 |
| [litellm](https://github.com/BerriAI/litellm) | Model gateway & UI | Both | Python | NOASSERTION | 49,067 | Mature | 89 | very active | 2d ago | 8 |
| [exo](https://github.com/exo-explore/exo) | Inference runtime | Both | Python | Apache-2.0 | 45,142 | Hot | 88 | very active | 0d ago | 18 |
| [langgraph](https://github.com/langchain-ai/langgraph) | Agent framework | Both | Python | MIT | 33,674 | Mature | 82 | very active | 2d ago | 11 |
| [qdrant](https://github.com/qdrant/qdrant) | Vector store | Both | Rust | Apache-2.0 | 31,755 | Classic | 87 | very active | 2d ago | 14 |
| [langfuse](https://github.com/langfuse/langfuse) | Observability & eval | Both | TypeScript | NOASSERTION | 28,386 | Classic | 84 | very active | 2d ago | 19 |
| [chroma](https://github.com/chroma-core/chroma) | Vector store | Both | Rust | Apache-2.0 | 28,190 | Classic | 83 | very active | 2d ago | 9 |
| [pgvector](https://github.com/pgvector/pgvector) | Vector store | Both | C | NOASSERTION | 21,566 | Classic | 55 | very active | 5d ago | 3 |
| [peft](https://github.com/huggingface/peft) | Fine-tuning | Both | Python | Apache-2.0 | 21,225 | Classic | 87 | very active | 3d ago | 35 |
| [pydantic-ai](https://github.com/pydantic/pydantic-ai) | Agent framework | Both | Python | MIT | 17,472 | Hot | 93 | very active | 2d ago | 34 |
| [gateway](https://github.com/Portkey-AI/gateway) | Model gateway & UI | Both | TypeScript | MIT | 11,944 | Mature | 66 | active | 10d ago | 3 |
| [phoenix](https://github.com/Arize-ai/phoenix) | Observability & eval | Both | Python | NOASSERTION | 9,967 | Classic | 84 | very active | 2d ago | 11 |
| [marqo](https://github.com/marqo-ai/marqo) | Vector store | Both | Python | Apache-2.0 | 5,023 | Classic | 64 | active | 1mo ago | 3 |
| [vllm](https://github.com/vllm-project/vllm) | Inference runtime | Infra | Python | Apache-2.0 | 81,744 | Classic | 99 | very active | 2d ago | 68 |
| [milvus](https://github.com/milvus-io/milvus) | Vector store | Infra | Go | Apache-2.0 | 44,597 | Classic | 99 | very active | 2d ago | 29 |
| [sglang](https://github.com/sgl-project/sglang) | Inference runtime | Infra | Python | Apache-2.0 | 28,899 | Mature | 99 | very active | 2d ago | 59 |
| [weaviate](https://github.com/weaviate/weaviate) | Vector store | Infra | Go | BSD-3-Clause | 16,264 | Classic | 84 | very active | 2d ago | 11 |
| [axolotl](https://github.com/axolotl-ai-cloud/axolotl) | Fine-tuning | Infra | Python | Apache-2.0 | 12,001 | Classic | 84 | very active | 2d ago | 20 |
| [skypilot](https://github.com/skypilot-org/skypilot) | Scaling / serving infra | Infra | Python | Apache-2.0 | 10,055 | Classic | 94 | very active | 2d ago | 22 |
| [lmdeploy](https://github.com/InternLM/lmdeploy) | Inference runtime | Infra | Python | Apache-2.0 | 7,879 | Mature | 87 | very active | 2d ago | 17 |
| [llm-compressor](https://github.com/vllm-project/llm-compressor) | Scaling / serving infra | Infra | Python | Apache-2.0 | 3,312 | Hot | 89 | very active | 2d ago | 23 |

## Graph analysis — how the stack hangs together

**Community clustering.** These 39 tools span **10 of the graph's 26 communities** — the stack cuts across the inference, RAG/vector, and agent neighborhoods rather than forming one cluster.

- **Community 2** (12): `ollama/ollama`, `ggml-org/llama.cpp`, `mozilla-ai/llamafile`, `vllm-project/vllm`, `sgl-project/sglang`, `InternLM/lmdeploy`, `huggingface/transformers`, `vllm-project/llm-compressor`, `unslothai/unsloth`, `huggingface/peft`, `axolotl-ai-cloud/axolotl`, `run-llama/llama_index`
- **Community 9** (6): `lancedb/lancedb`, `pgvector/pgvector`, `alibaba/zvec`, `qdrant/qdrant`, `weaviate/weaviate`, `milvus-io/milvus`
- **Community 13** (5): `mudler/LocalAI`, `open-webui/open-webui`, `janhq/jan`, `langchain-ai/langgraph`, `pydantic/pydantic-ai`
- **Community 12** (5): `nomic-ai/gpt4all`, `Mintplex-Labs/anything-llm`, `chroma-core/chroma`, `neuml/txtai`, `crewAIInc/crewAI`
- **Community 11** (4): `BerriAI/litellm`, `Portkey-AI/gateway`, `langfuse/langfuse`, `promptfoo/promptfoo`
- **Community 3** (2): `skypilot-org/skypilot`, `facebookresearch/faiss`
- **Community 5** (2): `marqo-ai/marqo`, `Arize-ai/phoenix`

**Centrality (PageRank in the full 1,185-repo graph)** — the 'hub' tools your other stars cluster around:

- `exo-explore/exo` — PageRank 0.0063 (🟡 Both)
- `langchain-ai/langgraph` — PageRank 0.0029 (🟡 Both)
- `neuml/txtai` — PageRank 0.0016 (🟢 Local)
- `huggingface/peft` — PageRank 0.0016 (🟡 Both)
- `axolotl-ai-cloud/axolotl` — PageRank 0.0016 (🔴 Infra)
- `vllm-project/vllm` — PageRank 0.0016 (🔴 Infra)
- `weaviate/weaviate` — PageRank 0.0014 (🔴 Infra)
- `crewAIInc/crewAI` — PageRank 0.0014 (🟡 Both)
- `huggingface/transformers` — PageRank 0.0014 (🟡 Both)
- `lancedb/lancedb` — PageRank 0.0012 (🟢 Local)

**Direct links between stack tools** (top similarity edges where both endpoints are in this report):

- `huggingface/peft` ⇄ `huggingface/transformers` (w=0.762) — topics: llm, python, pytorch; authors: kaixuanliu, Anai-Guo, blipbyte
- `vllm-project/llm-compressor` ⇄ `vllm-project/vllm` (w=0.572) — authors: brian-dellabetta
- `weaviate/weaviate` ⇄ `qdrant/qdrant` (w=0.512) — topics: search-engine, vector-search, vector-search-engine, vector-database; authors: dependabot[bot]
- `lancedb/lancedb` ⇄ `weaviate/weaviate` (w=0.456) — topics: approximate-nearest-neighbor-search, image-search, nearest-neighbor-search, recommender-system; authors: dependabot[bot]
- `unslothai/unsloth` ⇄ `ollama/ollama` (w=0.417) — topics: llama, llms, mistral, gemma
- `vllm-project/vllm` ⇄ `sgl-project/sglang` (w=0.407) — topics: llm, transformer, inference, llama
- `BerriAI/litellm` ⇄ `Portkey-AI/gateway` (w=0.381) — topics: langchain, llm, llmops, openai
- `crewAIInc/crewAI` ⇄ `chroma-core/chroma` (w=0.375) — topics: agents, ai, ai-agents
- `lancedb/lancedb` ⇄ `qdrant/qdrant` (w=0.324) — topics: image-search, nearest-neighbor-search, recommender-system, search-engine; authors: dependabot[bot]
- `axolotl-ai-cloud/axolotl` ⇄ `run-llama/llama_index` (w=0.313) — topics: fine-tuning, llm; authors: joaquinhuigomez, github-actions[bot]
- `lancedb/lancedb` ⇄ `alibaba/zvec` (w=0.285) — topics: search-engine, semantic-search, similarity-search, vector-database; authors: dependabot[bot]
- `sgl-project/sglang` ⇄ `ollama/ollama` (w=0.269) — topics: llama, llm, deepseek, gpt-oss
- `alibaba/zvec` ⇄ `weaviate/weaviate` (w=0.259) — topics: hnsw, search-engine, semantic-search, similarity-search; authors: dependabot[bot]
- `lancedb/lancedb` ⇄ `pgvector/pgvector` (w=0.250) — topics: approximate-nearest-neighbor-search, nearest-neighbor-search
- `huggingface/transformers` ⇄ `sgl-project/sglang` (w=0.244) — topics: transformer, deepseek, glm, llm
- …and 10 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). For infra you'll depend on, weight health + activity heavily.

| Tool | Tier | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|---|
| llama.cpp | Local | 99 | Classic | very active | 10 | 16% | 6237 |
| vllm | Infra | 99 | Classic | very active | 18 | 6% | 95 |
| sglang | Infra | 99 | Mature | very active | 12 | 14% | 52 |
| transformers | Both | 99 | Classic | very active | 10 | 11% | 258 |
| milvus | Infra | 99 | Classic | very active | 7 | 10% | 163 |
| llama_index | Both | 99 | Classic | very active | 6 | 27% | 494 |
| redis | Both | 97 | Classic | very active | 7 | 16% | 129 |
| skypilot | Infra | 94 | Classic | very active | 4 | 14% | 37 |
| faiss | Local | 93 | Classic | very active | 4 | 23% | 26 |
| pydantic-ai | Both | 93 | Hot | very active | 4 | 26% | 265 |
| lancedb | Local | 91 | Classic | very active | 4 | 18% | 438 |
| zvec | Local | 91 | Hot | very active | 4 | 17% | 7 |
| Foundry-Local | Local | 89 | Hot | very active | 3 | 28% | 16 |
| llm-compressor | Infra | 89 | Hot | very active | 3 | 25% | 25 |
| litellm | Both | 89 | Mature | very active | 3 | 24% | 1340 |
| exo | Both | 88 | Hot | very active | 3 | 29% | 16 |
| lmdeploy | Infra | 87 | Mature | very active | 3 | 31% | 65 |
| qdrant | Both | 87 | Classic | very active | 3 | 27% | 113 |
| peft | Both | 87 | Classic | very active | 3 | 42% | 32 |
| weaviate | Infra | 84 | Classic | very active | 2 | 40% | 541 |
| axolotl | Infra | 84 | Classic | very active | 2 | 39% | 30 |
| langfuse | Both | 84 | Classic | very active | 2 | 35% | 567 |
| phoenix | Both | 84 | Classic | very active | 2 | 46% | 710 |
| promptfoo | Local | 84 | Classic | very active | 2 | 31% | 413 |
| ollama | Local | 83 | Mature | very active | 2 | 29% | 218 |
| chroma | Both | 83 | Classic | very active | 2 | 33% | 137 |
| langgraph | Both | 82 | Mature | very active | 2 | 44% | 544 |
| open-webui | Local | 80 | Mature | very active | 1 | 56% | 163 |
| crewAI | Both | 80 | Mature | very active | 1 | 61% | 194 |
| LocalAI | Local | 79 | Classic | very active | 1 | 72% | 116 |
| jan | Local | 79 | Mature | very active | 1 | 97% | 102 |
| anything-llm | Local | 79 | Classic | very active | 1 | 64% | 29 |
| txtai | Local | 77 | Classic | very active | 1 | 99% | 63 |
| unsloth | Local | 77 | Mature | very active | 1 | 51% | 37 |
| gateway | Both | 66 | Mature | active | 1 | 64% | 81 |
| marqo | Both | 64 | Classic | active | 1 | 69% | 113 |
| llamafile | Local | 62 | Mature | very active | 1 | 74% | 40 |
| pgvector | Both | 55 | Classic | very active | 1 | 80% | 0 |
| gpt4all | Local | 7 | Declining | stale | 0 | 0% | 38 |

## Adjacent (covered elsewhere)

- **ggml-org/whisper.cpp** (50,441★) — speech runtime — covered in the *voice-agents* report
- **comet-ml/opik** (19,424★) — eval/observability — see the *LLM-evaluation* report
- **confident-ai/deepeval** (15,866★) — eval framework — see the *LLM-evaluation* report
- **langchain-ai/langchain** (138,334★) — broad agent toolkit — see the *agent-orchestration* report
- **microsoft/autogen** (58,646★) — multi-agent framework — see the *agent-orchestration* report

## Methodology & caveats

- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Tiering** is an editorial judgment about each tool's *sweet spot*, not a hard limit — many 🟢 tools can be pushed onto servers and some 🔴 tools run (slowly) on a laptop. The tag reflects what the project is *optimized and typically used* for.
- **Selection**: keyword scan (inference / serving / vllm / ollama / vector db / gateway / fine-tune / quantize) + manual curation into stack layers. Speech runtimes, pure eval frameworks, and broad agent toolkits were routed to adjacent reports.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 39 · Tiers: 15 local / 16 both / 8 infra · Snapshot: 2026-06-04T15:28:30.136Z</sub>
