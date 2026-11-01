# Local vs High-Infra AI Stack — A Deployment-Tier Comparison

> Derived from **kaiser-data**'s 2,585 starred repos (snapshot `2026-11-01T12:41:55.392Z`), cross-referenced with the repo-similarity graph (2,585 nodes / 8,670 edges, 45 communities).
>
> Generated 2026-11-01 by `scripts/reports/local_vs_infra_stack.py` (regenerate any time — no API cost).

![Top tools by stars](assets/local-vs-infra-stack-top-tools.svg)

![Tools per category](assets/local-vs-infra-stack-categories.svg)


## Executive summary

- **41 stack tools** in your stars (**1,882,372★** combined), mapped to every layer of a self-hosted AI stack and tagged by deployment tier:
  - 🟢 **Local / edge** (17) — laptop, single consumer GPU, on-device, zero ops
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
| [ollama/ollama](https://github.com/ollama/ollama) | 🟢 Local | 185,540 (▲711) | Go | Classic | The zero-config local default — `ollama run`, model registry, OpenAI-compatible API. Laptop-to-server, but single-node. |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 🟢 Local | 133,039 (▲639) | C++ | Classic | The CPU/edge engine under everything — GGUF quantization, runs on a Raspberry Pi to a Mac; the embeddable substrate. |
| [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | 🟢 Local | 77,342 (▼14) | C++ | Abandoned | Desktop-first local LLM app + bindings; privacy-focused, runs on plain CPUs. |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | 🟢 Local | 50,108 (▲139) | Go | Classic | Self-hosted, OpenAI-drop-in engine for LLM/TTS/STT/image on commodity hardware — the all-in-one local server. |
| [mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile) | 🟢 Local | 26,537 (▲48) | C++ | Classic | One file = one runnable model. Maximum portability for shipping a local model with no install. |
| [microsoft/foundry-local](https://github.com/microsoft/foundry-local) | 🟢 Local | 2,604 (▲5) | C++ | Hot | Microsoft's on-device runtime — offline LLM + Whisper, hardware-accelerated where available. |
| [withcatai/node-llama-cpp](https://github.com/withcatai/node-llama-cpp) | 🟢 Local | 2,197 (▲4) | TypeScript | Classic | llama.cpp bindings for Node.js — run GGUF models in-process with JSON-schema-constrained output; the JS-native local path. |
| [StayLameBro/backburner](https://github.com/StayLameBro/backburner) | 🟢 Local | 1,147 (▲26) | Python | Hot | Pairs an iPhone with a Mac over USB-C to run a 27B model with faster prefill and more context — a novel local-only scaling trick. |
| [huggingface/transformers](https://github.com/huggingface/transformers) | 🟡 Both | 168,404 (▲221) | Python | Classic | The model-definition library every runtime builds on; runs a notebook locally or a training cluster — the common denominator. |
| [exo-explore/exo](https://github.com/exo-explore/exo) | 🟡 Both | 48,143 (▲87) | Python | Mature | Stitches a *cluster out of your local devices* (phones, Macs, PCs) to run big models — distributed but home-grown. |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 🔴 Infra | 96,036 (▲454) | Python | Classic | The production serving standard — PagedAttention, continuous batching, tensor/pipeline parallelism for high QPS on GPU fleets. |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | 🔴 Infra | 38,337 (▲143) | Python | Mature | High-throughput serving with RadixAttention prefix caching — excels at structured/agentic workloads at scale. |
| [InternLM/lmdeploy](https://github.com/InternLM/lmdeploy) | 🔴 Infra | 8,126 (▲9) | Python | Classic | Toolkit for compressing + serving LLMs at scale (TurboMind engine); quantization-aware high-throughput inference. |

### Scaling / serving infra

_How you get a runtime onto many machines, cheaply. Only relevant once you outgrow a single node._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [skypilot-org/skypilot](https://github.com/skypilot-org/skypilot) | 🔴 Infra | 10,776 (▲25) | Python | Classic | Run/serve LLMs across any cloud or k8s with cost-aware scheduling & spot recovery — the multi-cloud orchestration layer. |
| [vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor) | 🔴 Infra | 3,931 (▲17) | Python | Mature | Quantize/sparsify models (GPTQ/AWQ/SmoothQuant) so they serve cheaper on vLLM — the cost-optimization step. |

### Model gateway & UI

_What sits in front of the model(s) — a chat UI for one user, or a proxy that fans out across providers for a whole org._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | 🟢 Local | 157,449 (▲653) | Python | Classic | The self-hosted ChatGPT-style UI for local models (pairs with Ollama) — RAG, users, tools, fully offline. |
| [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | 🟢 Local | 67,809 (▲234) | JavaScript | Classic | All-in-one desktop/self-host app: chat + RAG + agents over local or API models. |
| [janhq/jan](https://github.com/janhq/jan) | 🟢 Local | 45,212 (▲121) | Rust | Classic | Open-source desktop ChatGPT alternative that runs models 100% on your machine. |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | 🟡 Both | 62,484 (▲429) | Python | Classic | One OpenAI-compatible API over 100+ providers + a self-hostable proxy with keys/budgets/routing — local or enterprise gateway. |
| [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway) | 🟡 Both | 13,300 (▲26) | TypeScript | Mature | Fast AI gateway with routing, fallbacks, caching, and guardrails — drop in front of any tier. |

### Vector store

_Where embeddings live for RAG. Many of these span tiers — start embedded, cluster later._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | 🟢 Local | 41,245 (▲31) | C++ | Classic | The in-process ANN library — no server, embed it in your app; the index inside many of the DBs below. |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 🟢 Local | 16,167 (▲15) | C++ | Hot | Lightweight, lightning-fast in-process vector database for embedded use. |
| [neuml/txtai](https://github.com/neuml/txtai) | 🟢 Local | 13,054 (▲18) | Python | Classic | All-in-one embeddings DB + RAG + workflows in one local package. |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | 🟢 Local | 11,823 (▲48) | Rust | Classic | Embedded, serverless vector DB (Lance columnar format) — zero-ops local RAG that still handles large on-disk sets. |
| [redis/redis](https://github.com/redis/redis) | 🟡 Both | 77,128 (▲19) | C | Classic | The in-memory store you already run, now with vector search — local cache to HA cluster. |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | 🟡 Both | 35,360 (▲102) | Rust | Classic | Rust vector DB — single-binary local, but clusters with sharding/replication for billions of vectors. |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | 🟡 Both | 29,616 (▲33) | Rust | Classic | AI-native store that runs embedded for prototyping and client/server for production — the easy on-ramp. |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | 🟡 Both | 23,555 (▲72) | C | Classic | Vector search inside the Postgres you already run — scales from a laptop to a managed cluster with no new infra. |
| [marqo-ai/marqo](https://github.com/marqo-ai/marqo) | 🟡 Both | 5,026 (▼4) | Python | Mature | End-to-end vector search that bundles embedding inference; deploys local or distributed. |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | 🔴 Infra | 46,548 (▲65) | Go | Classic | The billion-scale, distributed OSS vector DB — heavy ops footprint, built for datacenter scale. |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | 🔴 Infra | 16,933 (▲18) | Go | Classic | Cloud-native vector DB with hybrid search & modules — designed for clustered, multi-tenant deployments. |

### Fine-tuning

_Adapting a model. LoRA on one GPU vs. multi-node full fine-tunes._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | 🟢 Local | 78,905 (▲324) | Python | Mature | 2× faster, lower-VRAM fine-tuning — train a LoRA on a single consumer GPU (even Colab). |
| [huggingface/peft](https://github.com/huggingface/peft) | 🟡 Both | 21,867 (▲16) | Python | Classic | Parameter-efficient fine-tuning (LoRA/QLoRA/adapters) — one consumer GPU or a multi-node run. |
| [axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) | 🔴 Infra | 12,650 (▲18) | Python | Classic | Config-driven fine-tuning that scales to multi-GPU/multi-node (DeepSpeed/FSDP) — the cluster-grade trainer. |

### Agent framework

_The orchestration logic — deliberately tier-agnostic; it targets whatever endpoint you give it._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 🟡 Both | 60,369 (▲252) | Python | Classic | Role-based multi-agent framework — runs against any model backend, local or hosted. |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 🟡 Both | 52,767 (▲98) | Python | Classic | Data/agent framework — point it at a local Ollama or a cloud endpoint; tier-agnostic. |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 🟡 Both | 44,260 (▲336) | Python | Classic | Graph/stateful agent runtime — the orchestration logic is independent of where the model runs. |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | 🟡 Both | 20,977 (▲97) | Python | Mature | Type-safe agent framework; model-agnostic, so the same code targets either tier. |

### Observability & eval

_Tracing, metrics, and evals. Most self-host locally and also offer managed cloud._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 🟢 Local | 26,688 (▲240) | TypeScript | Classic | CLI-first prompt/model eval that runs entirely on your machine in CI — no backend needed. |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | 🟡 Both | 36,823 (▲311) | TypeScript | Classic | Self-hostable LLM tracing/eval/metrics — runs in Docker locally or as managed cloud. |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | 🟡 Both | 12,090 (▲83) | Python | Classic | Open-source LLM observability you can run locally; OTel-native tracing + evals. |

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
| [ollama](https://github.com/ollama/ollama) | Inference runtime | Local | Go | MIT | 185,540 (▲711) | Classic | 83 | very active | 1d ago | 12 |
| [open-webui](https://github.com/open-webui/open-webui) | Model gateway & UI | Local | Python | NOASSERTION | 157,449 (▲653) | Classic | 85 | very active | 0d ago | 7 |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Inference runtime | Local | C++ | MIT | 133,039 (▲639) | Classic | 99 | very active | 0d ago | 48 |
| [unsloth](https://github.com/unslothai/unsloth) | Fine-tuning | Local | Python | Apache-2.0 | 78,905 (▲324) | Mature | 80 | very active | 0d ago | 10 |
| [gpt4all](https://github.com/nomic-ai/gpt4all) | Inference runtime | Local | C++ | MIT | 77,342 (▼14) | Abandoned | 7 | stale | 1.4y ago | 0 |
| [anything-llm](https://github.com/Mintplex-Labs/anything-llm) | Model gateway & UI | Local | JavaScript | MIT | 67,809 (▲234) | Classic | 99 | very active | 2d ago | 33 |
| [LocalAI](https://github.com/mudler/LocalAI) | Inference runtime | Local | Go | MIT | 50,108 (▲139) | Classic | 79 | very active | 0d ago | 6 |
| [jan](https://github.com/janhq/jan) | Model gateway & UI | Local | Rust | NOASSERTION | 45,212 (▲121) | Classic | 79 | very active | 1d ago | 4 |
| [faiss](https://github.com/facebookresearch/faiss) | Vector store | Local | C++ | MIT | 41,245 (▲31) | Classic | 89 | very active | 0d ago | 24 |
| [promptfoo](https://github.com/promptfoo/promptfoo) | Observability & eval | Local | TypeScript | MIT | 26,688 (▲240) | Classic | 79 | very active | 0d ago | 13 |
| [llamafile](https://github.com/mozilla-ai/llamafile) | Inference runtime | Local | C++ | NOASSERTION | 26,537 (▲48) | Classic | 62 | active | 21d ago | 6 |
| [zvec](https://github.com/alibaba/zvec) | Vector store | Local | C++ | Apache-2.0 | 16,167 (▲15) | Hot | 93 | very active | 0d ago | 18 |
| [txtai](https://github.com/neuml/txtai) | Vector store | Local | Python | Apache-2.0 | 13,054 (▲18) | Classic | 100 | very active | 1d ago | 35 |
| [lancedb](https://github.com/lancedb/lancedb) | Vector store | Local | Rust | Apache-2.0 | 11,823 (▲48) | Classic | 92 | very active | 0d ago | 38 |
| [foundry-local](https://github.com/microsoft/foundry-local) | Inference runtime | Local | C++ | NOASSERTION | 2,604 (▲5) | Hot | 83 | very active | 0d ago | 15 |
| [node-llama-cpp](https://github.com/withcatai/node-llama-cpp) | Inference runtime | Local | TypeScript | MIT | 2,197 (▲4) | Classic | 67 | active | 12d ago | 5 |
| [backburner](https://github.com/StayLameBro/backburner) | Inference runtime | Local | Python | MIT | 1,147 (▲26) | Hot | 62 | very active | 5d ago | 5 |
| [transformers](https://github.com/huggingface/transformers) | Inference runtime | Both | Python | Apache-2.0 | 168,404 (▲221) | Classic | 100 | very active | 0d ago | 41 |
| [redis](https://github.com/redis/redis) | Vector store | Both | C | NOASSERTION | 77,128 (▲19) | Classic | 97 | very active | 0d ago | 39 |
| [litellm](https://github.com/BerriAI/litellm) | Model gateway & UI | Both | Python | NOASSERTION | 62,484 (▲429) | Classic | 99 | very active | 0d ago | 27 |
| [crewAI](https://github.com/crewAIInc/crewAI) | Agent framework | Both | Python | MIT | 60,369 (▲252) | Classic | 84 | very active | 0d ago | 18 |
| [llama_index](https://github.com/run-llama/llama_index) | Agent framework | Both | Python | MIT | 52,767 (▲98) | Classic | 97 | very active | 6d ago | 50 |
| [exo](https://github.com/exo-explore/exo) | Inference runtime | Both | Python | Apache-2.0 | 48,143 (▲87) | Mature | 77 | very active | 0d ago | 1 |
| [langgraph](https://github.com/langchain-ai/langgraph) | Agent framework | Both | Python | MIT | 44,260 (▲336) | Classic | 83 | very active | 0d ago | 16 |
| [langfuse](https://github.com/langfuse/langfuse) | Observability & eval | Both | TypeScript | NOASSERTION | 36,823 (▲311) | Classic | 94 | very active | 0d ago | 19 |
| [qdrant](https://github.com/qdrant/qdrant) | Vector store | Both | Rust | Apache-2.0 | 35,360 (▲102) | Classic | 83 | very active | 0d ago | 20 |
| [chroma](https://github.com/chroma-core/chroma) | Vector store | Both | Rust | Apache-2.0 | 29,616 (▲33) | Classic | 80 | very active | 2d ago | 9 |
| [pgvector](https://github.com/pgvector/pgvector) | Vector store | Both | C | NOASSERTION | 23,555 (▲72) | Classic | 63 | very active | 1d ago | 2 |
| [peft](https://github.com/huggingface/peft) | Fine-tuning | Both | Python | Apache-2.0 | 21,867 (▲16) | Classic | 100 | very active | 0d ago | 47 |
| [pydantic-ai](https://github.com/pydantic/pydantic-ai) | Agent framework | Both | Python | MIT | 20,977 (▲97) | Mature | 82 | very active | 0d ago | 10 |
| [gateway](https://github.com/Portkey-AI/gateway) | Model gateway & UI | Both | TypeScript | MIT | 13,300 (▲26) | Mature | 39 | slowing | 5mo ago | 0 |
| [phoenix](https://github.com/Arize-ai/phoenix) | Observability & eval | Both | Python | NOASSERTION | 12,090 (▲83) | Classic | 84 | very active | 0d ago | 17 |
| [marqo](https://github.com/marqo-ai/marqo) | Vector store | Both | Python | Apache-2.0 | 5,026 (▼4) | Mature | 44 | active | 1mo ago | 0 |
| [vllm](https://github.com/vllm-project/vllm) | Inference runtime | Infra | Python | Apache-2.0 | 96,036 (▲454) | Classic | 99 | very active | 0d ago | 76 |
| [milvus](https://github.com/milvus-io/milvus) | Vector store | Infra | Go | Apache-2.0 | 46,548 (▲65) | Classic | 99 | very active | 0d ago | 34 |
| [sglang](https://github.com/sgl-project/sglang) | Inference runtime | Infra | Python | Apache-2.0 | 38,337 (▲143) | Mature | 99 | very active | 0d ago | 49 |
| [weaviate](https://github.com/weaviate/weaviate) | Vector store | Infra | Go | NOASSERTION | 16,933 (▲18) | Classic | 78 | very active | 0d ago | 7 |
| [axolotl](https://github.com/axolotl-ai-cloud/axolotl) | Fine-tuning | Infra | Python | Apache-2.0 | 12,650 (▲18) | Classic | 79 | very active | 0d ago | 8 |
| [skypilot](https://github.com/skypilot-org/skypilot) | Scaling / serving infra | Infra | Python | Apache-2.0 | 10,776 (▲25) | Classic | 90 | very active | 1d ago | 22 |
| [lmdeploy](https://github.com/InternLM/lmdeploy) | Inference runtime | Infra | Python | Apache-2.0 | 8,126 (▲9) | Classic | 97 | very active | 2d ago | 25 |
| [llm-compressor](https://github.com/vllm-project/llm-compressor) | Scaling / serving infra | Infra | Python | Apache-2.0 | 3,931 (▲17) | Mature | 89 | very active | 1d ago | 31 |

## Graph analysis — how the stack hangs together

**Community clustering.** These 41 tools span **15 of the graph's 45 communities** — the stack cuts across the inference, RAG/vector, and agent neighborhoods rather than forming one cluster.

- **Community 4** (10): `nomic-ai/gpt4all`, `InternLM/lmdeploy`, `open-webui/open-webui`, `Mintplex-Labs/anything-llm`, `chroma-core/chroma`, `alibaba/zvec`, `neuml/txtai`, `langchain-ai/langgraph`, `crewAIInc/crewAI`, `pydantic/pydantic-ai`
- **Community 35** (5): `ollama/ollama`, `vllm-project/vllm`, `sgl-project/sglang`, `vllm-project/llm-compressor`, `unslothai/unsloth`
- **Community 14** (5): `ggml-org/llama.cpp`, `withcatai/node-llama-cpp`, `StayLameBro/backburner`, `janhq/jan`, `marqo-ai/marqo`
- **Community 22** (5): `mozilla-ai/llamafile`, `BerriAI/litellm`, `Portkey-AI/gateway`, `langfuse/langfuse`, `Arize-ai/phoenix`
- **Community 27** (5): `lancedb/lancedb`, `pgvector/pgvector`, `qdrant/qdrant`, `weaviate/weaviate`, `milvus-io/milvus`
- **Community 2** (2): `huggingface/transformers`, `huggingface/peft`

**Centrality (PageRank in the full 2,585-repo graph)** — the 'hub' tools your other stars cluster around:

- `langchain-ai/langgraph` — PageRank 0.0012 (🟡 Both)
- `qdrant/qdrant` — PageRank 0.0007 (🟡 Both)
- `vllm-project/vllm` — PageRank 0.0006 (🔴 Infra)
- `neuml/txtai` — PageRank 0.0006 (🟢 Local)
- `huggingface/transformers` — PageRank 0.0006 (🟡 Both)
- `ggml-org/llama.cpp` — PageRank 0.0006 (🟢 Local)
- `run-llama/llama_index` — PageRank 0.0006 (🟡 Both)
- `chroma-core/chroma` — PageRank 0.0006 (🟡 Both)
- `unslothai/unsloth` — PageRank 0.0006 (🟢 Local)
- `crewAIInc/crewAI` — PageRank 0.0006 (🟡 Both)

**Direct links between stack tools** (top similarity edges where both endpoints are in this report):

- `huggingface/peft` ⇄ `huggingface/transformers` (w=0.761) — topics: llm, python, pytorch; authors: albertvillanova, michaelbenayoun, mishig25
- `vllm-project/llm-compressor` ⇄ `vllm-project/vllm` (w=0.550)
- `vllm-project/vllm` ⇄ `sgl-project/sglang` (w=0.440) — topics: llm, transformer, inference, llama; authors: hshrivastava-droid, Alex-Wengg
- `weaviate/weaviate` ⇄ `qdrant/qdrant` (w=0.429) — topics: search-engine, vector-search, vector-search-engine, vector-database
- `lancedb/lancedb` ⇄ `weaviate/weaviate` (w=0.400) — topics: approximate-nearest-neighbor-search, image-search, nearest-neighbor-search, recommender-system
- `BerriAI/litellm` ⇄ `Portkey-AI/gateway` (w=0.348) — topics: langchain, llm, llmops, openai
- `lancedb/lancedb` ⇄ `qdrant/qdrant` (w=0.323) — topics: image-search, nearest-neighbor-search, recommender-system, search-engine
- `neuml/txtai` ⇄ `Mintplex-Labs/anything-llm` (w=0.288) — topics: llm, vector-database, rag, ai-agents; authors: MohammadHijjawi97, rtmalikian, moneebullah25
- `Arize-ai/phoenix` ⇄ `BerriAI/litellm` (w=0.288) — topics: llmops, anthropic, openai, langchain; authors: pcbeingused333, dependabot[bot]
- `sgl-project/sglang` ⇄ `ollama/ollama` (w=0.280) — topics: llama, llm, deepseek, gpt-oss
- `promptfoo/promptfoo` ⇄ `langfuse/langfuse` (w=0.271) — topics: llm, prompt-engineering, llmops, evaluation; authors: dependabot[bot]
- `unslothai/unsloth` ⇄ `open-webui/open-webui` (w=0.257) — topics: llms, llm, openai, self-hosted
- `lancedb/lancedb` ⇄ `pgvector/pgvector` (w=0.250) — topics: approximate-nearest-neighbor-search, nearest-neighbor-search
- `unslothai/unsloth` ⇄ `ollama/ollama` (w=0.214) — topics: llama, llms, gemma, llm
- `milvus-io/milvus` ⇄ `weaviate/weaviate` (w=0.202) — topics: nearest-neighbor-search, vector-search, image-search, hnsw
- …and 1 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). For infra you'll depend on, weight health + activity heavily.

| Tool | Tier | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|---|
| transformers | Both | 100 | Classic | very active | 8 | 12% | 282 |
| txtai | Local | 100 | Classic | very active | 5 | 29% | 68 |
| peft | Both | 100 | Classic | very active | 7 | 22% | 36 |
| llama.cpp | Local | 99 | Classic | very active | 9 | 11% | 7932 |
| vllm | Infra | 99 | Classic | very active | 26 | 9% | 108 |
| sglang | Infra | 99 | Mature | very active | 7 | 12% | 63 |
| litellm | Both | 99 | Classic | very active | 7 | 10% | 1543 |
| anything-llm | Local | 99 | Classic | very active | 5 | 24% | 39 |
| milvus | Infra | 99 | Classic | very active | 7 | 10% | 180 |
| lmdeploy | Infra | 97 | Classic | very active | 5 | 15% | 71 |
| redis | Both | 97 | Classic | very active | 9 | 14% | 163 |
| llama_index | Both | 97 | Classic | very active | 10 | 14% | 497 |
| langfuse | Both | 94 | Classic | very active | 4 | 22% | 731 |
| zvec | Local | 93 | Hot | very active | 4 | 17% | 15 |
| lancedb | Local | 92 | Classic | very active | 4 | 24% | 537 |
| skypilot | Infra | 90 | Classic | very active | 3 | 24% | 47 |
| llm-compressor | Infra | 89 | Mature | very active | 3 | 23% | 40 |
| faiss | Local | 89 | Classic | very active | 3 | 25% | 29 |
| open-webui | Local | 85 | Classic | very active | 2 | 37% | 177 |
| crewAI | Both | 84 | Classic | very active | 2 | 45% | 247 |
| phoenix | Both | 84 | Classic | very active | 2 | 34% | 893 |
| ollama | Local | 83 | Classic | very active | 2 | 38% | 271 |
| foundry-local | Local | 83 | Hot | very active | 2 | 31% | 28 |
| qdrant | Both | 83 | Classic | very active | 2 | 41% | 119 |
| langgraph | Both | 83 | Classic | very active | 2 | 43% | 593 |
| pydantic-ai | Both | 82 | Mature | very active | 2 | 45% | 352 |
| chroma | Both | 80 | Classic | very active | 2 | 31% | 137 |
| unsloth | Local | 80 | Mature | very active | 1 | 72% | 83 |
| LocalAI | Local | 79 | Classic | very active | 1 | 75% | 140 |
| jan | Local | 79 | Classic | very active | 1 | 74% | 108 |
| axolotl | Infra | 79 | Classic | very active | 1 | 65% | 36 |
| promptfoo | Local | 79 | Classic | very active | 1 | 72% | 432 |
| weaviate | Infra | 78 | Classic | very active | 1 | 64% | 609 |
| exo | Both | 77 | Mature | very active | 1 | 100% | 16 |
| node-llama-cpp | Local | 67 | Classic | active | 1 | 76% | 142 |
| pgvector | Both | 63 | Classic | very active | 1 | 99% | 0 |
| llamafile | Local | 62 | Classic | active | 1 | 58% | 43 |
| backburner | Local | 62 | Hot | very active | 1 | 73% | 4 |
| marqo | Both | 44 | Mature | active | 0 | 0% | 113 |
| gateway | Both | 39 | Mature | slowing | 0 | 0% | 81 |
| gpt4all | Local | 7 | Abandoned | stale | 0 | 0% | 38 |

## Adjacent (covered elsewhere)

- **ggml-org/whisper.cpp** (54,835★) — speech runtime — covered in the *voice-agents* report
- **comet-ml/opik** (23,081★) — eval/observability — see the *LLM-evaluation* report
- **confident-ai/deepeval** (19,222★) — eval framework — see the *LLM-evaluation* report
- **langchain-ai/langchain** (148,809★) — broad agent toolkit — see the *agent-orchestration* report
- **microsoft/autogen** (61,660★) — multi-agent framework — see the *agent-orchestration* report

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Tiering** is an editorial judgment about each tool's *sweet spot*, not a hard limit — many 🟢 tools can be pushed onto servers and some 🔴 tools run (slowly) on a laptop. The tag reflects what the project is *optimized and typically used* for.
- **Selection**: keyword scan (inference / serving / vllm / ollama / vector db / gateway / fine-tune / quantize) + manual curation into stack layers. Speech runtimes, pure eval frameworks, and broad agent toolkits were routed to adjacent reports.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 41 · Tiers: 17 local / 16 both / 8 infra · Snapshot: 2026-11-01T12:41:55.392Z</sub>
