# Local vs High-Infra AI Stack — A Deployment-Tier Comparison

> Derived from **kaiser-data**'s 1,900 starred repos (snapshot `2026-08-31T12:10:08.018Z`), cross-referenced with the repo-similarity graph (1,900 nodes / 6,181 edges, 37 communities).
>
> Generated 2026-08-31 by `scripts/reports/local_vs_infra_stack.py` (regenerate any time — no API cost).

![Top tools by stars](assets/local-vs-infra-stack-top-tools.svg)

![Tools per category](assets/local-vs-infra-stack-categories.svg)


## Executive summary

- **39 stack tools** in your stars (**1,809,471★** combined), mapped to every layer of a self-hosted AI stack and tagged by deployment tier:
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
| [ollama/ollama](https://github.com/ollama/ollama) | 🟢 Local | 179,825 (▲237) | Go | Classic | The zero-config local default — `ollama run`, model registry, OpenAI-compatible API. Laptop-to-server, but single-node. |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 🟢 Local | 126,473 (▲504) | C++ | Classic | The CPU/edge engine under everything — GGUF quantization, runs on a Raspberry Pi to a Mac; the embeddable substrate. |
| [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | 🟢 Local | 77,390 (▼6) | C++ | Abandoned | Desktop-first local LLM app + bindings; privacy-focused, runs on plain CPUs. |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | 🟢 Local | 48,780 (▲69) | Go | Classic | Self-hosted, OpenAI-drop-in engine for LLM/TTS/STT/image on commodity hardware — the all-in-one local server. |
| [mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile) | 🟢 Local | 25,810 (▲103) | C++ | Mature | One file = one runnable model. Maximum portability for shipping a local model with no install. |
| [microsoft/foundry-local](https://github.com/microsoft/foundry-local) | 🟢 Local | 2,533 (▲5) | C++ | Hot | Microsoft's on-device runtime — offline LLM + Whisper, hardware-accelerated where available. |
| [huggingface/transformers](https://github.com/huggingface/transformers) | 🟡 Both | 164,656 (▲137) | Python | Classic | The model-definition library every runtime builds on; runs a notebook locally or a training cluster — the common denominator. |
| [exo-explore/exo](https://github.com/exo-explore/exo) | 🟡 Both | 47,170 (▲68) | Python | Mature | Stitches a *cluster out of your local devices* (phones, Macs, PCs) to run big models — distributed but home-grown. |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 🔴 Infra | 90,578 (▲329) | Python | Classic | The production serving standard — PagedAttention, continuous batching, tensor/pipeline parallelism for high QPS on GPU fleets. |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | 🔴 Infra | 32,977 (▲393) | Python | Mature | High-throughput serving with RadixAttention prefix caching — excels at structured/agentic workloads at scale. |
| [InternLM/lmdeploy](https://github.com/InternLM/lmdeploy) | 🔴 Infra | 8,036 (▲7) | Python | Classic | Toolkit for compressing + serving LLMs at scale (TurboMind engine); quantization-aware high-throughput inference. |

### Scaling / serving infra

_How you get a runtime onto many machines, cheaply. Only relevant once you outgrow a single node._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [skypilot-org/skypilot](https://github.com/skypilot-org/skypilot) | 🔴 Infra | 10,541 (▲11) | Python | Classic | Run/serve LLMs across any cloud or k8s with cost-aware scheduling & spot recovery — the multi-cloud orchestration layer. |
| [vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor) | 🔴 Infra | 3,744 (▲10) | Python | Mature | Quantize/sparsify models (GPTQ/AWQ/SmoothQuant) so they serve cheaper on vLLM — the cost-optimization step. |

### Model gateway & UI

_What sits in front of the model(s) — a chat UI for one user, or a proxy that fans out across providers for a whole org._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | 🟢 Local | 150,483 (▲335) | Python | Mature | The self-hosted ChatGPT-style UI for local models (pairs with Ollama) — RAG, users, tools, fully offline. |
| [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | 🟢 Local | 65,422 (▲117) | JavaScript | Classic | All-in-one desktop/self-host app: chat + RAG + agents over local or API models. |
| [janhq/jan](https://github.com/janhq/jan) | 🟢 Local | 44,278 (▲65) | TypeScript | Classic | Open-source desktop ChatGPT alternative that runs models 100% on your machine. |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | 🟡 Both | 57,662 (▲237) | Python | Classic | One OpenAI-compatible API over 100+ providers + a self-hostable proxy with keys/budgets/routing — local or enterprise gateway. |
| [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway) | 🟡 Both | 12,863 (▲21) | TypeScript | Mature | Fast AI gateway with routing, fallbacks, caching, and guardrails — drop in front of any tier. |

### Vector store

_Where embeddings live for RAG. Many of these span tiers — start embedded, cluster later._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | 🟢 Local | 40,829 (▲17) | C++ | Classic | The in-process ANN library — no server, embed it in your app; the index inside many of the DBs below. |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 🟢 Local | 15,544 (▲16) | C++ | Hot | Lightweight, lightning-fast in-process vector database for embedded use. |
| [neuml/txtai](https://github.com/neuml/txtai) | 🟢 Local | 12,913 (▲3) | Python | Classic | All-in-one embeddings DB + RAG + workflows in one local package. |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | 🟢 Local | 11,318 (▲20) | Rust | Classic | Embedded, serverless vector DB (Lance columnar format) — zero-ops local RAG that still handles large on-disk sets. |
| [redis/redis](https://github.com/redis/redis) | 🟡 Both | 76,154 (▲29) | C | Classic | The in-memory store you already run, now with vector search — local cache to HA cluster. |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | 🟡 Both | 34,290 (▲62) | Rust | Classic | Rust vector DB — single-binary local, but clusters with sharding/replication for billions of vectors. |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | 🟡 Both | 29,191 (▲25) | Rust | Classic | AI-native store that runs embedded for prototyping and client/server for production — the easy on-ramp. |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | 🟡 Both | 22,834 (▲47) | C | Classic | Vector search inside the Postgres you already run — scales from a laptop to a managed cluster with no new infra. |
| [marqo-ai/marqo](https://github.com/marqo-ai/marqo) | 🟡 Both | 5,031 (▲2) | Python | Mature | End-to-end vector search that bundles embedding inference; deploys local or distributed. |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | 🔴 Infra | 45,902 (▲68) | Go | Classic | The billion-scale, distributed OSS vector DB — heavy ops footprint, built for datacenter scale. |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | 🔴 Infra | 16,767 (▲10) | Go | Classic | Cloud-native vector DB with hybrid search & modules — designed for clustered, multi-tenant deployments. |

### Fine-tuning

_Adapting a model. LoRA on one GPU vs. multi-node full fine-tunes._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | 🟢 Local | 75,324 (▲329) | Python | Mature | 2× faster, lower-VRAM fine-tuning — train a LoRA on a single consumer GPU (even Colab). |
| [huggingface/peft](https://github.com/huggingface/peft) | 🟡 Both | 21,613 (▲13) | Python | Classic | Parameter-efficient fine-tuning (LoRA/QLoRA/adapters) — one consumer GPU or a multi-node run. |
| [axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) | 🔴 Infra | 12,429 (▲16) | Python | Classic | Config-driven fine-tuning that scales to multi-GPU/multi-node (DeepSpeed/FSDP) — the cluster-grade trainer. |

### Agent framework

_The orchestration logic — deliberately tier-agnostic; it targets whatever endpoint you give it._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 🟡 Both | 57,866 (▲178) | Python | Mature | Role-based multi-agent framework — runs against any model backend, local or hosted. |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 🟡 Both | 51,936 (▲42) | Python | Classic | Data/agent framework — point it at a local Ollama or a cloud endpoint; tier-agnostic. |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 🟡 Both | 40,776 (▲206) | Python | Classic | Graph/stateful agent runtime — the orchestration logic is independent of where the model runs. |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | 🟡 Both | 19,608 (▲67) | Python | Mature | Type-safe agent framework; model-agnostic, so the same code targets either tier. |

### Observability & eval

_Tracing, metrics, and evals. Most self-host locally and also offer managed cloud._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 🟢 Local | 24,693 (▲70) | TypeScript | Classic | CLI-first prompt/model eval that runs entirely on your machine in CI — no backend needed. |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | 🟡 Both | 33,971 (▲151) | TypeScript | Classic | Self-hostable LLM tracing/eval/metrics — runs in Docker locally or as managed cloud. |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | 🟡 Both | 11,261 (▲43) | Python | Classic | Open-source LLM observability you can run locally; OTel-native tracing + evals. |

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
| [ollama](https://github.com/ollama/ollama) | Inference runtime | Local | Go | MIT | 179,825 (▲237) | Classic | 83 | very active | 2d ago | 9 |
| [open-webui](https://github.com/open-webui/open-webui) | Model gateway & UI | Local | Python | NOASSERTION | 150,483 (▲335) | Mature | 80 | very active | 0d ago | 9 |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Inference runtime | Local | C++ | MIT | 126,473 (▲504) | Classic | 99 | very active | 0d ago | 62 |
| [gpt4all](https://github.com/nomic-ai/gpt4all) | Inference runtime | Local | C++ | MIT | 77,390 (▼6) | Abandoned | 7 | stale | 1.3y ago | 0 |
| [unsloth](https://github.com/unslothai/unsloth) | Fine-tuning | Local | Python | Apache-2.0 | 75,324 (▲329) | Mature | 83 | very active | 0d ago | 17 |
| [anything-llm](https://github.com/Mintplex-Labs/anything-llm) | Model gateway & UI | Local | JavaScript | MIT | 65,422 (▲117) | Classic | 79 | very active | 2d ago | 21 |
| [LocalAI](https://github.com/mudler/LocalAI) | Inference runtime | Local | Go | MIT | 48,780 (▲69) | Classic | 84 | very active | 0d ago | 10 |
| [jan](https://github.com/janhq/jan) | Model gateway & UI | Local | TypeScript | NOASSERTION | 44,278 (▲65) | Classic | 79 | very active | 0d ago | 3 |
| [faiss](https://github.com/facebookresearch/faiss) | Vector store | Local | C++ | MIT | 40,829 (▲17) | Classic | 94 | very active | 3d ago | 35 |
| [llamafile](https://github.com/mozilla-ai/llamafile) | Inference runtime | Local | C++ | NOASSERTION | 25,810 (▲103) | Mature | 66 | very active | 5d ago | 5 |
| [promptfoo](https://github.com/promptfoo/promptfoo) | Observability & eval | Local | TypeScript | MIT | 24,693 (▲70) | Classic | 79 | very active | 0d ago | 12 |
| [zvec](https://github.com/alibaba/zvec) | Vector store | Local | C++ | Apache-2.0 | 15,544 (▲16) | Hot | 93 | very active | 1d ago | 19 |
| [txtai](https://github.com/neuml/txtai) | Vector store | Local | Python | Apache-2.0 | 12,913 (▲3) | Classic | 80 | very active | 4d ago | 17 |
| [lancedb](https://github.com/lancedb/lancedb) | Vector store | Local | Rust | Apache-2.0 | 11,318 (▲20) | Classic | 87 | very active | 0d ago | 12 |
| [foundry-local](https://github.com/microsoft/foundry-local) | Inference runtime | Local | C++ | NOASSERTION | 2,533 (▲5) | Hot | 87 | very active | 0d ago | 19 |
| [transformers](https://github.com/huggingface/transformers) | Inference runtime | Both | Python | Apache-2.0 | 164,656 (▲137) | Classic | 100 | very active | 0d ago | 44 |
| [redis](https://github.com/redis/redis) | Vector store | Both | C | NOASSERTION | 76,154 (▲29) | Classic | 97 | very active | 0d ago | 39 |
| [crewAI](https://github.com/crewAIInc/crewAI) | Agent framework | Both | Python | MIT | 57,866 (▲178) | Mature | 85 | very active | 0d ago | 9 |
| [litellm](https://github.com/BerriAI/litellm) | Model gateway & UI | Both | Python | NOASSERTION | 57,662 (▲237) | Classic | 84 | very active | 0d ago | 8 |
| [llama_index](https://github.com/run-llama/llama_index) | Agent framework | Both | Python | MIT | 51,936 (▲42) | Classic | 98 | very active | 2d ago | 59 |
| [exo](https://github.com/exo-explore/exo) | Inference runtime | Both | Python | Apache-2.0 | 47,170 (▲68) | Mature | 73 | active | 6d ago | 5 |
| [langgraph](https://github.com/langchain-ai/langgraph) | Agent framework | Both | Python | MIT | 40,776 (▲206) | Classic | 77 | very active | 1d ago | 17 |
| [qdrant](https://github.com/qdrant/qdrant) | Vector store | Both | Rust | Apache-2.0 | 34,290 (▲62) | Classic | 88 | very active | 0d ago | 15 |
| [langfuse](https://github.com/langfuse/langfuse) | Observability & eval | Both | TypeScript | NOASSERTION | 33,971 (▲151) | Classic | 89 | very active | 0d ago | 13 |
| [chroma](https://github.com/chroma-core/chroma) | Vector store | Both | Rust | Apache-2.0 | 29,191 (▲25) | Classic | 83 | very active | 1d ago | 10 |
| [pgvector](https://github.com/pgvector/pgvector) | Vector store | Both | C | NOASSERTION | 22,834 (▲47) | Classic | 64 | very active | 11d ago | 3 |
| [peft](https://github.com/huggingface/peft) | Fine-tuning | Both | Python | Apache-2.0 | 21,613 (▲13) | Classic | 95 | very active | 0d ago | 45 |
| [pydantic-ai](https://github.com/pydantic/pydantic-ai) | Agent framework | Both | Python | MIT | 19,608 (▲67) | Mature | 88 | very active | 0d ago | 26 |
| [gateway](https://github.com/Portkey-AI/gateway) | Model gateway & UI | Both | TypeScript | MIT | 12,863 (▲21) | Mature | 45 | slowing | 3mo ago | 0 |
| [phoenix](https://github.com/Arize-ai/phoenix) | Observability & eval | Both | Python | NOASSERTION | 11,261 (▲43) | Classic | 84 | very active | 0d ago | 21 |
| [marqo](https://github.com/marqo-ai/marqo) | Vector store | Both | Python | Apache-2.0 | 5,031 (▲2) | Mature | 47 | active | 23d ago | 0 |
| [vllm](https://github.com/vllm-project/vllm) | Inference runtime | Infra | Python | Apache-2.0 | 90,578 (▲329) | Classic | 99 | very active | 0d ago | 71 |
| [milvus](https://github.com/milvus-io/milvus) | Vector store | Infra | Go | Apache-2.0 | 45,902 (▲68) | Classic | 99 | very active | 0d ago | 30 |
| [sglang](https://github.com/sgl-project/sglang) | Inference runtime | Infra | Python | Apache-2.0 | 32,977 (▲393) | Mature | 99 | very active | 0d ago | 50 |
| [weaviate](https://github.com/weaviate/weaviate) | Vector store | Infra | Go | BSD-3-Clause | 16,767 (▲10) | Classic | 83 | very active | 0d ago | 7 |
| [axolotl](https://github.com/axolotl-ai-cloud/axolotl) | Fine-tuning | Infra | Python | Apache-2.0 | 12,429 (▲16) | Classic | 89 | very active | 0d ago | 17 |
| [skypilot](https://github.com/skypilot-org/skypilot) | Scaling / serving infra | Infra | Python | Apache-2.0 | 10,541 (▲11) | Classic | 90 | very active | 0d ago | 20 |
| [lmdeploy](https://github.com/InternLM/lmdeploy) | Inference runtime | Infra | Python | Apache-2.0 | 8,036 (▲7) | Classic | 93 | very active | 0d ago | 23 |
| [llm-compressor](https://github.com/vllm-project/llm-compressor) | Scaling / serving infra | Infra | Python | Apache-2.0 | 3,744 (▲10) | Mature | 89 | very active | 1d ago | 35 |

## Graph analysis — how the stack hangs together

**Community clustering.** These 39 tools span **12 of the graph's 37 communities** — the stack cuts across the inference, RAG/vector, and agent neighborhoods rather than forming one cluster.

- **Community 16** (9): `Mintplex-Labs/anything-llm`, `lancedb/lancedb`, `pgvector/pgvector`, `alibaba/zvec`, `neuml/txtai`, `qdrant/qdrant`, `redis/redis`, `weaviate/weaviate`, `milvus-io/milvus`
- **Community 19** (6): `mudler/LocalAI`, `BerriAI/litellm`, `Portkey-AI/gateway`, `langfuse/langfuse`, `Arize-ai/phoenix`, `promptfoo/promptfoo`
- **Community 20** (6): `nomic-ai/gpt4all`, `InternLM/lmdeploy`, `huggingface/transformers`, `open-webui/open-webui`, `unslothai/unsloth`, `huggingface/peft`
- **Community 13** (4): `ollama/ollama`, `vllm-project/vllm`, `sgl-project/sglang`, `vllm-project/llm-compressor`
- **Community 6** (4): `ggml-org/llama.cpp`, `mozilla-ai/llamafile`, `marqo-ai/marqo`, `axolotl-ai-cloud/axolotl`
- **Community 7** (3): `chroma-core/chroma`, `langchain-ai/langgraph`, `crewAIInc/crewAI`
- **Community 14** (2): `microsoft/foundry-local`, `skypilot-org/skypilot`

**Centrality (PageRank in the full 1,900-repo graph)** — the 'hub' tools your other stars cluster around:

- `langchain-ai/langgraph` — PageRank 0.0016 (🟡 Both)
- `crewAIInc/crewAI` — PageRank 0.0014 (🟡 Both)
- `axolotl-ai-cloud/axolotl` — PageRank 0.0012 (🔴 Infra)
- `huggingface/peft` — PageRank 0.0011 (🟡 Both)
- `chroma-core/chroma` — PageRank 0.0010 (🟡 Both)
- `ggml-org/llama.cpp` — PageRank 0.0010 (🟢 Local)
- `microsoft/foundry-local` — PageRank 0.0009 (🟢 Local)
- `weaviate/weaviate` — PageRank 0.0009 (🔴 Infra)
- `mudler/LocalAI` — PageRank 0.0008 (🟢 Local)
- `neuml/txtai` — PageRank 0.0008 (🟢 Local)

**Direct links between stack tools** (top similarity edges where both endpoints are in this report):

- `huggingface/peft` ⇄ `huggingface/transformers` (w=0.760) — topics: llm, python, pytorch; authors: qgallouedec, kaixuanliu, jiqing-feng
- `vllm-project/llm-compressor` ⇄ `vllm-project/vllm` (w=0.550)
- `weaviate/weaviate` ⇄ `qdrant/qdrant` (w=0.524) — topics: search-engine, vector-search, vector-search-engine, vector-database; authors: dependabot[bot]
- `vllm-project/vllm` ⇄ `sgl-project/sglang` (w=0.407) — topics: llm, transformer, inference, llama
- `lancedb/lancedb` ⇄ `weaviate/weaviate` (w=0.400) — topics: approximate-nearest-neighbor-search, image-search, nearest-neighbor-search, recommender-system
- `BerriAI/litellm` ⇄ `Portkey-AI/gateway` (w=0.348) — topics: langchain, llm, llmops, openai
- `lancedb/lancedb` ⇄ `qdrant/qdrant` (w=0.323) — topics: image-search, nearest-neighbor-search, recommender-system, search-engine
- `huggingface/peft` ⇄ `axolotl-ai-cloud/axolotl` (w=0.317) — topics: llm, fine-tuning; authors: dependabot[bot], latent-9
- `sgl-project/sglang` ⇄ `ollama/ollama` (w=0.269) — topics: llama, llm, deepseek, gpt-oss
- `alibaba/zvec` ⇄ `weaviate/weaviate` (w=0.259) — topics: hnsw, search-engine, semantic-search, similarity-search; authors: dependabot[bot]
- `unslothai/unsloth` ⇄ `open-webui/open-webui` (w=0.257) — topics: llms, llm, openai, self-hosted
- `lancedb/lancedb` ⇄ `pgvector/pgvector` (w=0.250) — topics: approximate-nearest-neighbor-search, nearest-neighbor-search
- `huggingface/transformers` ⇄ `sgl-project/sglang` (w=0.244) — topics: transformer, deepseek, glm, llm
- `InternLM/lmdeploy` ⇄ `axolotl-ai-cloud/axolotl` (w=0.239) — topics: llm; authors: Anai-Guo, latent-9
- `lancedb/lancedb` ⇄ `alibaba/zvec` (w=0.235) — topics: search-engine, semantic-search, similarity-search, vector-database
- …and 6 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). For infra you'll depend on, weight health + activity heavily.

| Tool | Tier | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|---|
| transformers | Both | 100 | Classic | very active | 6 | 18% | 272 |
| llama.cpp | Local | 99 | Classic | very active | 13 | 10% | 7025 |
| vllm | Infra | 99 | Classic | very active | 21 | 5% | 104 |
| sglang | Infra | 99 | Mature | very active | 8 | 13% | 59 |
| milvus | Infra | 99 | Classic | very active | 8 | 11% | 171 |
| llama_index | Both | 98 | Classic | very active | 15 | 8% | 496 |
| redis | Both | 97 | Classic | very active | 7 | 11% | 150 |
| peft | Both | 95 | Classic | very active | 5 | 20% | 33 |
| faiss | Local | 94 | Classic | very active | 4 | 27% | 28 |
| lmdeploy | Infra | 93 | Classic | very active | 4 | 22% | 69 |
| zvec | Local | 93 | Hot | very active | 4 | 22% | 11 |
| skypilot | Infra | 90 | Classic | very active | 3 | 26% | 42 |
| llm-compressor | Infra | 89 | Mature | very active | 3 | 31% | 32 |
| axolotl | Infra | 89 | Classic | very active | 3 | 23% | 32 |
| langfuse | Both | 89 | Classic | very active | 3 | 23% | 669 |
| qdrant | Both | 88 | Classic | very active | 3 | 34% | 116 |
| pydantic-ai | Both | 88 | Mature | very active | 3 | 20% | 319 |
| foundry-local | Local | 87 | Hot | very active | 3 | 21% | 22 |
| lancedb | Local | 87 | Classic | very active | 3 | 21% | 491 |
| crewAI | Both | 85 | Mature | very active | 2 | 46% | 232 |
| LocalAI | Local | 84 | Classic | very active | 2 | 45% | 136 |
| litellm | Both | 84 | Classic | very active | 2 | 39% | 1449 |
| phoenix | Both | 84 | Classic | very active | 2 | 44% | 796 |
| ollama | Local | 83 | Classic | very active | 2 | 35% | 249 |
| chroma | Both | 83 | Classic | very active | 2 | 45% | 137 |
| weaviate | Infra | 83 | Classic | very active | 2 | 43% | 576 |
| unsloth | Local | 83 | Mature | very active | 2 | 44% | 58 |
| open-webui | Local | 80 | Mature | very active | 1 | 61% | 169 |
| txtai | Local | 80 | Classic | very active | 1 | 51% | 67 |
| jan | Local | 79 | Classic | very active | 1 | 67% | 104 |
| anything-llm | Local | 79 | Classic | very active | 1 | 60% | 35 |
| promptfoo | Local | 79 | Classic | very active | 1 | 51% | 424 |
| langgraph | Both | 77 | Classic | very active | 1 | 60% | 561 |
| exo | Both | 73 | Mature | active | 3 | 20% | 16 |
| llamafile | Local | 66 | Mature | very active | 1 | 71% | 42 |
| pgvector | Both | 64 | Classic | very active | 1 | 98% | 0 |
| marqo | Both | 47 | Mature | active | 0 | 0% | 113 |
| gateway | Both | 45 | Mature | slowing | 0 | 0% | 81 |
| gpt4all | Local | 7 | Abandoned | stale | 0 | 0% | 38 |

## Adjacent (covered elsewhere)

- **ggml-org/whisper.cpp** (53,323★) — speech runtime — covered in the *voice-agents* report
- **comet-ml/opik** (21,710★) — eval/observability — see the *LLM-evaluation* report
- **confident-ai/deepeval** (17,998★) — eval framework — see the *LLM-evaluation* report
- **langchain-ai/langchain** (145,332★) — broad agent toolkit — see the *agent-orchestration* report
- **microsoft/autogen** (60,719★) — multi-agent framework — see the *agent-orchestration* report

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Tiering** is an editorial judgment about each tool's *sweet spot*, not a hard limit — many 🟢 tools can be pushed onto servers and some 🔴 tools run (slowly) on a laptop. The tag reflects what the project is *optimized and typically used* for.
- **Selection**: keyword scan (inference / serving / vllm / ollama / vector db / gateway / fine-tune / quantize) + manual curation into stack layers. Speech runtimes, pure eval frameworks, and broad agent toolkits were routed to adjacent reports.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 39 · Tiers: 15 local / 16 both / 8 infra · Snapshot: 2026-08-31T12:10:08.018Z</sub>
