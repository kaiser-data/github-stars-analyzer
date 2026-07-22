# Local vs High-Infra AI Stack — A Deployment-Tier Comparison

> Derived from **kaiser-data**'s 1,350 starred repos (snapshot `2026-07-20T08:33:57.852Z`), cross-referenced with the repo-similarity graph (1,350 nodes / 4,379 edges, 28 communities).
>
> Generated 2026-07-22 by `scripts/reports/local_vs_infra_stack.py` (regenerate any time — no API cost).

![Top tools by stars](assets/local-vs-infra-stack-top-tools.svg)

![Tools per category](assets/local-vs-infra-stack-categories.svg)


## Executive summary

- **39 stack tools** in your stars (**1,755,526★** combined), mapped to every layer of a self-hosted AI stack and tagged by deployment tier:
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
| [ollama/ollama](https://github.com/ollama/ollama) | 🟢 Local | 176,491 (▲33) | Go | Classic | The zero-config local default — `ollama run`, model registry, OpenAI-compatible API. Laptop-to-server, but single-node. |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 🟢 Local | 121,006 (▲42) | C++ | Classic | The CPU/edge engine under everything — GGUF quantization, runs on a Raspberry Pi to a Mac; the embeddable substrate. |
| [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | 🟢 Local | 77,392 (▼1) | C++ | Declining | Desktop-first local LLM app + bindings; privacy-focused, runs on plain CPUs. |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | 🟢 Local | 47,698 (▲15) | Go | Classic | Self-hosted, OpenAI-drop-in engine for LLM/TTS/STT/image on commodity hardware — the all-in-one local server. |
| [mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile) | 🟢 Local | 25,402 (▲11) | C++ | Mature | One file = one runnable model. Maximum portability for shipping a local model with no install. |
| [microsoft/foundry-local](https://github.com/microsoft/foundry-local) | 🟢 Local | 2,436 (▼1) | C++ | Hot | Microsoft's on-device runtime — offline LLM + Whisper, hardware-accelerated where available. |
| [huggingface/transformers](https://github.com/huggingface/transformers) | 🟡 Both | 162,754 (▲15) | Python | Classic | The model-definition library every runtime builds on; runs a notebook locally or a training cluster — the common denominator. |
| [exo-explore/exo](https://github.com/exo-explore/exo) | 🟡 Both | 46,379 (▲7) | Python | Mature | Stitches a *cluster out of your local devices* (phones, Macs, PCs) to run big models — distributed but home-grown. |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 🔴 Infra | 86,682 (▲34) | Python | Classic | The production serving standard — PagedAttention, continuous batching, tensor/pipeline parallelism for high QPS on GPU fleets. |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | 🔴 Infra | 30,534 (▲26) | Python | Mature | High-throughput serving with RadixAttention prefix caching — excels at structured/agentic workloads at scale. |
| [InternLM/lmdeploy](https://github.com/InternLM/lmdeploy) | 🔴 Infra | 7,965 | Python | Classic | Toolkit for compressing + serving LLMs at scale (TurboMind engine); quantization-aware high-throughput inference. |

### Scaling / serving infra

_How you get a runtime onto many machines, cheaply. Only relevant once you outgrow a single node._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [skypilot-org/skypilot](https://github.com/skypilot-org/skypilot) | 🔴 Infra | 10,317 (▲2) | Python | Classic | Run/serve LLMs across any cloud or k8s with cost-aware scheduling & spot recovery — the multi-cloud orchestration layer. |
| [vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor) | 🔴 Infra | 3,560 (▼1) | Python | Mature | Quantize/sparsify models (GPTQ/AWQ/SmoothQuant) so they serve cheaper on vLLM — the cost-optimization step. |

### Model gateway & UI

_What sits in front of the model(s) — a chat UI for one user, or a proxy that fans out across providers for a whole org._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | 🟢 Local | 146,021 (▲42) | Python | Mature | The self-hosted ChatGPT-style UI for local models (pairs with Ollama) — RAG, users, tools, fully offline. |
| [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | 🟢 Local | 63,590 (▲26) | JavaScript | Classic | All-in-one desktop/self-host app: chat + RAG + agents over local or API models. |
| [janhq/jan](https://github.com/janhq/jan) | 🟢 Local | 43,646 (▲10) | TypeScript | Mature | Open-source desktop ChatGPT alternative that runs models 100% on your machine. |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | 🟡 Both | 54,074 (▲48) | Python | Mature | One OpenAI-compatible API over 100+ providers + a self-hostable proxy with keys/budgets/routing — local or enterprise gateway. |
| [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway) | 🟡 Both | 12,475 (▲5) | TypeScript | Mature | Fast AI gateway with routing, fallbacks, caching, and guardrails — drop in front of any tier. |

### Vector store

_Where embeddings live for RAG. Many of these span tiers — start embedded, cluster later._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | 🟢 Local | 40,544 (▲3) | C++ | Classic | The in-process ANN library — no server, embed it in your app; the index inside many of the DBs below. |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 🟢 Local | 15,166 (▲22) | C++ | Hot | Lightweight, lightning-fast in-process vector database for embedded use. |
| [neuml/txtai](https://github.com/neuml/txtai) | 🟢 Local | 12,737 (▲3) | Python | Classic | All-in-one embeddings DB + RAG + workflows in one local package. |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | 🟢 Local | 10,935 (▲3) | HTML | Classic | Embedded, serverless vector DB (Lance columnar format) — zero-ops local RAG that still handles large on-disk sets. |
| [redis/redis](https://github.com/redis/redis) | 🟡 Both | 75,592 (▲1) | C | Classic | The in-memory store you already run, now with vector search — local cache to HA cluster. |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | 🟡 Both | 33,423 (▲16) | Rust | Classic | Rust vector DB — single-binary local, but clusters with sharding/replication for billions of vectors. |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | 🟡 Both | 28,833 (▲5) | Rust | Classic | AI-native store that runs embedded for prototyping and client/server for production — the easy on-ramp. |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | 🟡 Both | 22,266 (▲12) | C | Classic | Vector search inside the Postgres you already run — scales from a laptop to a managed cluster with no new infra. |
| [marqo-ai/marqo](https://github.com/marqo-ai/marqo) | 🟡 Both | 5,017 | Python | Mature | End-to-end vector search that bundles embedding inference; deploys local or distributed. |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | 🔴 Infra | 45,277 (▲3) | Go | Classic | The billion-scale, distributed OSS vector DB — heavy ops footprint, built for datacenter scale. |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | 🔴 Infra | 16,619 (▲2) | Go | Classic | Cloud-native vector DB with hybrid search & modules — designed for clustered, multi-tenant deployments. |

### Fine-tuning

_Adapting a model. LoRA on one GPU vs. multi-node full fine-tunes._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | 🟢 Local | 68,445 (▲19) | Python | Mature | 2× faster, lower-VRAM fine-tuning — train a LoRA on a single consumer GPU (even Colab). |
| [huggingface/peft](https://github.com/huggingface/peft) | 🟡 Both | 21,418 (▲3) | Python | Classic | Parameter-efficient fine-tuning (LoRA/QLoRA/adapters) — one consumer GPU or a multi-node run. |
| [axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) | 🔴 Infra | 12,217 (▲2) | Python | Classic | Config-driven fine-tuning that scales to multi-GPU/multi-node (DeepSpeed/FSDP) — the cluster-grade trainer. |

### Agent framework

_The orchestration logic — deliberately tier-agnostic; it targets whatever endpoint you give it._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 🟡 Both | 55,823 (▲35) | Python | Mature | Role-based multi-agent framework — runs against any model backend, local or hosted. |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 🟡 Both | 50,953 (▲10) | Python | Classic | Data/agent framework — point it at a local Ollama or a cloud endpoint; tier-agnostic. |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 🟡 Both | 37,654 (▲39) | Python | Mature | Graph/stateful agent runtime — the orchestration logic is independent of where the model runs. |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | 🟡 Both | 18,664 (▲12) | Python | Mature | Type-safe agent framework; model-agnostic, so the same code targets either tier. |

### Observability & eval

_Tracing, metrics, and evals. Most self-host locally and also offer managed cloud._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 🟢 Local | 23,429 (▲18) | TypeScript | Classic | CLI-first prompt/model eval that runs entirely on your machine in CI — no backend needed. |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | 🟡 Both | 31,458 (▲30) | TypeScript | Classic | Self-hostable LLM tracing/eval/metrics — runs in Docker locally or as managed cloud. |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | 🟡 Both | 10,634 (▲8) | Python | Classic | Open-source LLM observability you can run locally; OTel-native tracing + evals. |

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
| [ollama](https://github.com/ollama/ollama) | Inference runtime | Local | Go | MIT | 176,491 (▲33) | Classic | 88 | very active | 2d ago | 17 |
| [open-webui](https://github.com/open-webui/open-webui) | Model gateway & UI | Local | Python | NOASSERTION | 146,021 (▲42) | Mature | 80 | very active | 0d ago | 10 |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Inference runtime | Local | C++ | MIT | 121,006 (▲42) | Classic | 99 | very active | 0d ago | 55 |
| [gpt4all](https://github.com/nomic-ai/gpt4all) | Inference runtime | Local | C++ | MIT | 77,392 (▼1) | Declining | 7 | stale | 1.1y ago | 0 |
| [unsloth](https://github.com/unslothai/unsloth) | Fine-tuning | Local | Python | Apache-2.0 | 68,445 (▲19) | Mature | 88 | very active | 0d ago | 22 |
| [anything-llm](https://github.com/Mintplex-Labs/anything-llm) | Model gateway & UI | Local | JavaScript | MIT | 63,590 (▲26) | Classic | 79 | very active | 2d ago | 6 |
| [LocalAI](https://github.com/mudler/LocalAI) | Inference runtime | Local | Go | MIT | 47,698 (▲15) | Classic | 79 | very active | 0d ago | 11 |
| [jan](https://github.com/janhq/jan) | Model gateway & UI | Local | TypeScript | NOASSERTION | 43,646 (▲10) | Mature | 79 | very active | 0d ago | 7 |
| [faiss](https://github.com/facebookresearch/faiss) | Vector store | Local | C++ | MIT | 40,544 (▲3) | Classic | 89 | very active | 2d ago | 23 |
| [llamafile](https://github.com/mozilla-ai/llamafile) | Inference runtime | Local | C++ | NOASSERTION | 25,402 (▲11) | Mature | 65 | very active | 2d ago | 7 |
| [promptfoo](https://github.com/promptfoo/promptfoo) | Observability & eval | Local | TypeScript | MIT | 23,429 (▲18) | Classic | 89 | very active | 0d ago | 22 |
| [zvec](https://github.com/alibaba/zvec) | Vector store | Local | C++ | Apache-2.0 | 15,166 (▲22) | Hot | 87 | very active | 0d ago | 16 |
| [txtai](https://github.com/neuml/txtai) | Vector store | Local | Python | Apache-2.0 | 12,737 (▲3) | Classic | 78 | very active | 6d ago | 5 |
| [lancedb](https://github.com/lancedb/lancedb) | Vector store | Local | HTML | Apache-2.0 | 10,935 (▲3) | Classic | 91 | very active | 2d ago | 28 |
| [foundry-local](https://github.com/microsoft/foundry-local) | Inference runtime | Local | C++ | NOASSERTION | 2,436 (▼1) | Hot | 87 | very active | 2d ago | 17 |
| [transformers](https://github.com/huggingface/transformers) | Inference runtime | Both | Python | Apache-2.0 | 162,754 (▲15) | Classic | 99 | very active | 0d ago | 48 |
| [redis](https://github.com/redis/redis) | Vector store | Both | C | NOASSERTION | 75,592 (▲1) | Classic | 97 | very active | 0d ago | 39 |
| [crewAI](https://github.com/crewAIInc/crewAI) | Agent framework | Both | Python | MIT | 55,823 (▲35) | Mature | 85 | very active | 1d ago | 11 |
| [litellm](https://github.com/BerriAI/litellm) | Model gateway & UI | Both | Python | NOASSERTION | 54,074 (▲48) | Mature | 89 | very active | 0d ago | 9 |
| [llama_index](https://github.com/run-llama/llama_index) | Agent framework | Both | Python | MIT | 50,953 (▲10) | Classic | 99 | very active | 4d ago | 48 |
| [exo](https://github.com/exo-explore/exo) | Inference runtime | Both | Python | Apache-2.0 | 46,379 (▲7) | Mature | 81 | very active | 27d ago | 16 |
| [langgraph](https://github.com/langchain-ai/langgraph) | Agent framework | Both | Python | MIT | 37,654 (▲39) | Mature | 77 | very active | 0d ago | 13 |
| [qdrant](https://github.com/qdrant/qdrant) | Vector store | Both | Rust | Apache-2.0 | 33,423 (▲16) | Classic | 93 | very active | 0d ago | 16 |
| [langfuse](https://github.com/langfuse/langfuse) | Observability & eval | Both | TypeScript | NOASSERTION | 31,458 (▲30) | Classic | 89 | very active | 0d ago | 14 |
| [chroma](https://github.com/chroma-core/chroma) | Vector store | Both | Rust | Apache-2.0 | 28,833 (▲5) | Classic | 83 | very active | 2d ago | 8 |
| [pgvector](https://github.com/pgvector/pgvector) | Vector store | Both | C | NOASSERTION | 22,266 (▲12) | Classic | 61 | very active | 9d ago | 3 |
| [peft](https://github.com/huggingface/peft) | Fine-tuning | Both | Python | Apache-2.0 | 21,418 (▲3) | Classic | 86 | very active | 6d ago | 38 |
| [pydantic-ai](https://github.com/pydantic/pydantic-ai) | Agent framework | Both | Python | MIT | 18,664 (▲12) | Mature | 89 | very active | 0d ago | 24 |
| [gateway](https://github.com/Portkey-AI/gateway) | Model gateway & UI | Both | TypeScript | MIT | 12,475 (▲5) | Mature | 61 | active | 1mo ago | 3 |
| [phoenix](https://github.com/Arize-ai/phoenix) | Observability & eval | Both | Python | NOASSERTION | 10,634 (▲8) | Classic | 79 | very active | 0d ago | 11 |
| [marqo](https://github.com/marqo-ai/marqo) | Vector store | Both | Python | Apache-2.0 | 5,017 | Mature | 49 | active | 6d ago | 0 |
| [vllm](https://github.com/vllm-project/vllm) | Inference runtime | Infra | Python | Apache-2.0 | 86,682 (▲34) | Classic | 99 | very active | 0d ago | 70 |
| [milvus](https://github.com/milvus-io/milvus) | Vector store | Infra | Go | Apache-2.0 | 45,277 (▲3) | Classic | 99 | very active | 0d ago | 30 |
| [sglang](https://github.com/sgl-project/sglang) | Inference runtime | Infra | Python | Apache-2.0 | 30,534 (▲26) | Mature | 99 | very active | 0d ago | 51 |
| [weaviate](https://github.com/weaviate/weaviate) | Vector store | Infra | Go | BSD-3-Clause | 16,619 (▲2) | Classic | 84 | very active | 0d ago | 11 |
| [axolotl](https://github.com/axolotl-ai-cloud/axolotl) | Fine-tuning | Infra | Python | Apache-2.0 | 12,217 (▲2) | Classic | 84 | very active | 3d ago | 15 |
| [skypilot](https://github.com/skypilot-org/skypilot) | Scaling / serving infra | Infra | Python | Apache-2.0 | 10,317 (▲2) | Classic | 100 | very active | 0d ago | 22 |
| [lmdeploy](https://github.com/InternLM/lmdeploy) | Inference runtime | Infra | Python | Apache-2.0 | 7,965 | Classic | 88 | very active | 0d ago | 14 |
| [llm-compressor](https://github.com/vllm-project/llm-compressor) | Scaling / serving infra | Infra | Python | Apache-2.0 | 3,560 (▼1) | Mature | 84 | very active | 0d ago | 31 |

## Graph analysis — how the stack hangs together

**Community clustering.** These 39 tools span **13 of the graph's 28 communities** — the stack cuts across the inference, RAG/vector, and agent neighborhoods rather than forming one cluster.

- **Community 22** (11): `ollama/ollama`, `mozilla-ai/llamafile`, `nomic-ai/gpt4all`, `vllm-project/vllm`, `sgl-project/sglang`, `InternLM/lmdeploy`, `huggingface/transformers`, `vllm-project/llm-compressor`, `unslothai/unsloth`, `huggingface/peft`, `axolotl-ai-cloud/axolotl`
- **Community 13** (6): `lancedb/lancedb`, `pgvector/pgvector`, `alibaba/zvec`, `qdrant/qdrant`, `weaviate/weaviate`, `milvus-io/milvus`
- **Community 10** (4): `BerriAI/litellm`, `Portkey-AI/gateway`, `langfuse/langfuse`, `promptfoo/promptfoo`
- **Community 8** (4): `open-webui/open-webui`, `janhq/jan`, `Mintplex-Labs/anything-llm`, `neuml/txtai`
- **Community 5** (4): `chroma-core/chroma`, `langchain-ai/langgraph`, `crewAIInc/crewAI`, `pydantic/pydantic-ai`
- **Community 16** (3): `skypilot-org/skypilot`, `facebookresearch/faiss`, `marqo-ai/marqo`

**Centrality (PageRank in the full 1,350-repo graph)** — the 'hub' tools your other stars cluster around:

- `langchain-ai/langgraph` — PageRank 0.0020 (🟡 Both)
- `huggingface/peft` — PageRank 0.0017 (🟡 Both)
- `neuml/txtai` — PageRank 0.0016 (🟢 Local)
- `crewAIInc/crewAI` — PageRank 0.0015 (🟡 Both)
- `axolotl-ai-cloud/axolotl` — PageRank 0.0015 (🔴 Infra)
- `huggingface/transformers` — PageRank 0.0014 (🟡 Both)
- `vllm-project/vllm` — PageRank 0.0012 (🔴 Infra)
- `weaviate/weaviate` — PageRank 0.0012 (🔴 Infra)
- `chroma-core/chroma` — PageRank 0.0012 (🟡 Both)
- `lancedb/lancedb` — PageRank 0.0011 (🟢 Local)

**Direct links between stack tools** (top similarity edges where both endpoints are in this report):

- `huggingface/peft` ⇄ `huggingface/transformers` (w=0.713) — topics: llm, python, pytorch; authors: kaixuanliu, jiqing-feng
- `vllm-project/llm-compressor` ⇄ `vllm-project/vllm` (w=0.590) — authors: HDCharles, mgoin
- `weaviate/weaviate` ⇄ `qdrant/qdrant` (w=0.429) — topics: search-engine, vector-search, vector-search-engine, vector-database
- `unslothai/unsloth` ⇄ `ollama/ollama` (w=0.417) — topics: llama, llms, mistral, gemma
- `vllm-project/vllm` ⇄ `sgl-project/sglang` (w=0.407) — topics: llm, transformer, inference, llama
- `lancedb/lancedb` ⇄ `weaviate/weaviate` (w=0.400) — topics: approximate-nearest-neighbor-search, image-search, nearest-neighbor-search, recommender-system
- `crewAIInc/crewAI` ⇄ `chroma-core/chroma` (w=0.375) — topics: agents, ai, ai-agents
- `BerriAI/litellm` ⇄ `Portkey-AI/gateway` (w=0.348) — topics: langchain, llm, llmops, openai
- `huggingface/peft` ⇄ `axolotl-ai-cloud/axolotl` (w=0.328) — topics: llm, fine-tuning; authors: dependabot[bot], lxcxjxhx
- `lancedb/lancedb` ⇄ `qdrant/qdrant` (w=0.319) — topics: image-search, nearest-neighbor-search, recommender-system, search-engine; authors: dependabot[bot]
- `lancedb/lancedb` ⇄ `alibaba/zvec` (w=0.282) — topics: search-engine, semantic-search, similarity-search, vector-database; authors: dependabot[bot]
- `sgl-project/sglang` ⇄ `ollama/ollama` (w=0.269) — topics: llama, llm, deepseek, gpt-oss
- `lancedb/lancedb` ⇄ `pgvector/pgvector` (w=0.250) — topics: approximate-nearest-neighbor-search, nearest-neighbor-search
- `huggingface/transformers` ⇄ `sgl-project/sglang` (w=0.244) — topics: transformer, deepseek, glm, llm
- `sgl-project/sglang` ⇄ `unslothai/unsloth` (w=0.244) — topics: llama, llm, deepseek, gpt-oss
- …and 11 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). For infra you'll depend on, weight health + activity heavily.

| Tool | Tier | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|---|
| skypilot | Infra | 100 | Classic | very active | 5 | 14% | 40 |
| llama.cpp | Local | 99 | Classic | very active | 11 | 11% | 6652 |
| vllm | Infra | 99 | Classic | very active | 20 | 5% | 100 |
| sglang | Infra | 99 | Mature | very active | 11 | 9% | 56 |
| transformers | Both | 99 | Classic | very active | 9 | 9% | 268 |
| milvus | Infra | 99 | Classic | very active | 9 | 8% | 167 |
| llama_index | Both | 99 | Classic | very active | 8 | 20% | 495 |
| redis | Both | 97 | Classic | very active | 7 | 17% | 132 |
| qdrant | Both | 93 | Classic | very active | 4 | 18% | 115 |
| lancedb | Local | 91 | Classic | very active | 4 | 20% | 464 |
| litellm | Both | 89 | Mature | very active | 3 | 26% | 1409 |
| faiss | Local | 89 | Classic | very active | 3 | 20% | 27 |
| pydantic-ai | Both | 89 | Mature | very active | 3 | 24% | 286 |
| langfuse | Both | 89 | Classic | very active | 3 | 30% | 624 |
| promptfoo | Local | 89 | Classic | very active | 3 | 29% | 419 |
| ollama | Local | 88 | Classic | very active | 3 | 22% | 232 |
| lmdeploy | Infra | 88 | Classic | very active | 3 | 17% | 67 |
| unsloth | Local | 88 | Mature | very active | 3 | 20% | 43 |
| foundry-local | Local | 87 | Hot | very active | 3 | 20% | 20 |
| zvec | Local | 87 | Hot | very active | 3 | 31% | 10 |
| peft | Both | 86 | Classic | very active | 3 | 36% | 32 |
| crewAI | Both | 85 | Mature | very active | 2 | 41% | 217 |
| llm-compressor | Infra | 84 | Mature | very active | 2 | 35% | 27 |
| weaviate | Infra | 84 | Classic | very active | 2 | 32% | 561 |
| axolotl | Infra | 84 | Classic | very active | 2 | 41% | 32 |
| chroma | Both | 83 | Classic | very active | 2 | 30% | 137 |
| exo | Both | 81 | Mature | very active | 3 | 19% | 16 |
| open-webui | Local | 80 | Mature | very active | 1 | 84% | 166 |
| LocalAI | Local | 79 | Classic | very active | 1 | 65% | 132 |
| jan | Local | 79 | Mature | very active | 1 | 91% | 103 |
| anything-llm | Local | 79 | Classic | very active | 1 | 72% | 33 |
| phoenix | Both | 79 | Classic | very active | 1 | 68% | 753 |
| txtai | Local | 78 | Classic | very active | 1 | 94% | 65 |
| langgraph | Both | 77 | Mature | very active | 1 | 57% | 553 |
| llamafile | Local | 65 | Mature | very active | 1 | 75% | 41 |
| gateway | Both | 61 | Mature | active | 1 | 63% | 81 |
| pgvector | Both | 61 | Classic | very active | 1 | 98% | 0 |
| marqo | Both | 49 | Mature | active | 0 | 0% | 113 |
| gpt4all | Local | 7 | Declining | stale | 0 | 0% | 38 |

## Adjacent (covered elsewhere)

- **ggml-org/whisper.cpp** (51,885★) — speech runtime — covered in the *voice-agents* report
- **comet-ml/opik** (20,714★) — eval/observability — see the *LLM-evaluation* report
- **confident-ai/deepeval** (16,960★) — eval framework — see the *LLM-evaluation* report
- **langchain-ai/langchain** (142,141★) — broad agent toolkit — see the *agent-orchestration* report
- **microsoft/autogen** (59,832★) — multi-agent framework — see the *agent-orchestration* report

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Tiering** is an editorial judgment about each tool's *sweet spot*, not a hard limit — many 🟢 tools can be pushed onto servers and some 🔴 tools run (slowly) on a laptop. The tag reflects what the project is *optimized and typically used* for.
- **Selection**: keyword scan (inference / serving / vllm / ollama / vector db / gateway / fine-tune / quantize) + manual curation into stack layers. Speech runtimes, pure eval frameworks, and broad agent toolkits were routed to adjacent reports.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 39 · Tiers: 15 local / 16 both / 8 infra · Snapshot: 2026-07-20T08:33:57.852Z</sub>
