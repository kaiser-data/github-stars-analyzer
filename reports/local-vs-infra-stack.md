# Local vs High-Infra AI Stack — A Deployment-Tier Comparison

> Derived from **kaiser-data**'s 2,398 starred repos (snapshot `2026-10-19T11:27:31.266Z`), cross-referenced with the repo-similarity graph (2,398 nodes / 8,025 edges, 39 communities).
>
> Generated 2026-10-19 by `scripts/reports/local_vs_infra_stack.py` (regenerate any time — no API cost).

![Top tools by stars](assets/local-vs-infra-stack-top-tools.svg)

![Tools per category](assets/local-vs-infra-stack-categories.svg)


## Executive summary

- **41 stack tools** in your stars (**1,866,766★** combined), mapped to every layer of a self-hosted AI stack and tagged by deployment tier:
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
| [ollama/ollama](https://github.com/ollama/ollama) | 🟢 Local | 183,801 (▲1,188) | Go | Classic | The zero-config local default — `ollama run`, model registry, OpenAI-compatible API. Laptop-to-server, but single-node. |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 🟢 Local | 131,681 (▲947) | C++ | Classic | The CPU/edge engine under everything — GGUF quantization, runs on a Raspberry Pi to a Mac; the embeddable substrate. |
| [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | 🟢 Local | 77,350 (▼18) | C++ | Abandoned | Desktop-first local LLM app + bindings; privacy-focused, runs on plain CPUs. |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | 🟢 Local | 49,635 (▲178) | Go | Classic | Self-hosted, OpenAI-drop-in engine for LLM/TTS/STT/image on commodity hardware — the all-in-one local server. |
| [mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile) | 🟢 Local | 26,431 (▲215) | C++ | Classic | One file = one runnable model. Maximum portability for shipping a local model with no install. |
| [microsoft/foundry-local](https://github.com/microsoft/foundry-local) | 🟢 Local | 2,592 (▲14) | C++ | Hot | Microsoft's on-device runtime — offline LLM + Whisper, hardware-accelerated where available. |
| [withcatai/node-llama-cpp](https://github.com/withcatai/node-llama-cpp) | 🟢 Local | 2,192 (▲3) | TypeScript | Classic | llama.cpp bindings for Node.js — run GGUF models in-process with JSON-schema-constrained output; the JS-native local path. |
| [StayLameBro/backburner](https://github.com/StayLameBro/backburner) | 🟢 Local | 1,042 (▲116) | Python | Hot | Pairs an iPhone with a Mac over USB-C to run a 27B model with faster prefill and more context — a novel local-only scaling trick. |
| [huggingface/transformers](https://github.com/huggingface/transformers) | 🟡 Both | 167,850 (▲792) | Python | Classic | The model-definition library every runtime builds on; runs a notebook locally or a training cluster — the common denominator. |
| [exo-explore/exo](https://github.com/exo-explore/exo) | 🟡 Both | 47,954 (▲141) | Python | Mature | Stitches a *cluster out of your local devices* (phones, Macs, PCs) to run big models — distributed but home-grown. |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 🔴 Infra | 94,123 (▲615) | Python | Classic | The production serving standard — PagedAttention, continuous batching, tensor/pipeline parallelism for high QPS on GPU fleets. |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | 🔴 Infra | 37,364 (▲402) | Python | Mature | High-throughput serving with RadixAttention prefix caching — excels at structured/agentic workloads at scale. |
| [InternLM/lmdeploy](https://github.com/InternLM/lmdeploy) | 🔴 Infra | 8,109 (▲6) | Python | Classic | Toolkit for compressing + serving LLMs at scale (TurboMind engine); quantization-aware high-throughput inference. |

### Scaling / serving infra

_How you get a runtime onto many machines, cheaply. Only relevant once you outgrow a single node._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [skypilot-org/skypilot](https://github.com/skypilot-org/skypilot) | 🔴 Infra | 10,721 (▲31) | Python | Classic | Run/serve LLMs across any cloud or k8s with cost-aware scheduling & spot recovery — the multi-cloud orchestration layer. |
| [vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor) | 🔴 Infra | 3,885 (▲22) | Python | Mature | Quantize/sparsify models (GPTQ/AWQ/SmoothQuant) so they serve cheaper on vLLM — the cost-optimization step. |

### Model gateway & UI

_What sits in front of the model(s) — a chat UI for one user, or a proxy that fans out across providers for a whole org._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | 🟢 Local | 156,140 (▲1,949) | Python | Classic | The self-hosted ChatGPT-style UI for local models (pairs with Ollama) — RAG, users, tools, fully offline. |
| [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | 🟢 Local | 67,308 (▲421) | JavaScript | Classic | All-in-one desktop/self-host app: chat + RAG + agents over local or API models. |
| [janhq/jan](https://github.com/janhq/jan) | 🟢 Local | 45,010 (▲134) | Rust | Classic | Open-source desktop ChatGPT alternative that runs models 100% on your machine. |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | 🟡 Both | 61,553 (▲674) | Python | Classic | One OpenAI-compatible API over 100+ providers + a self-hostable proxy with keys/budgets/routing — local or enterprise gateway. |
| [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway) | 🟡 Both | 13,220 (▲59) | TypeScript | Mature | Fast AI gateway with routing, fallbacks, caching, and guardrails — drop in front of any tier. |

### Vector store

_Where embeddings live for RAG. Many of these span tiers — start embedded, cluster later._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | 🟢 Local | 41,166 (▲42) | C++ | Classic | The in-process ANN library — no server, embed it in your app; the index inside many of the DBs below. |
| [alibaba/zvec](https://github.com/alibaba/zvec) | 🟢 Local | 16,126 (▲34) | C++ | Hot | Lightweight, lightning-fast in-process vector database for embedded use. |
| [neuml/txtai](https://github.com/neuml/txtai) | 🟢 Local | 13,027 (▲24) | Python | Classic | All-in-one embeddings DB + RAG + workflows in one local package. |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | 🟢 Local | 11,701 (▲69) | Rust | Classic | Embedded, serverless vector DB (Lance columnar format) — zero-ops local RAG that still handles large on-disk sets. |
| [redis/redis](https://github.com/redis/redis) | 🟡 Both | 77,014 (▲319) | C | Classic | The in-memory store you already run, now with vector search — local cache to HA cluster. |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | 🟡 Both | 35,136 (▲128) | Rust | Classic | Rust vector DB — single-binary local, but clusters with sharding/replication for billions of vectors. |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | 🟡 Both | 29,531 (▲59) | Rust | Classic | AI-native store that runs embedded for prototyping and client/server for production — the easy on-ramp. |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | 🟡 Both | 23,408 (▲114) | C | Classic | Vector search inside the Postgres you already run — scales from a laptop to a managed cluster with no new infra. |
| [marqo-ai/marqo](https://github.com/marqo-ai/marqo) | 🟡 Both | 5,028 | Python | Mature | End-to-end vector search that bundles embedding inference; deploys local or distributed. |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | 🔴 Infra | 46,427 (▲80) | Go | Classic | The billion-scale, distributed OSS vector DB — heavy ops footprint, built for datacenter scale. |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | 🔴 Infra | 16,891 (▲13) | Go | Classic | Cloud-native vector DB with hybrid search & modules — designed for clustered, multi-tenant deployments. |

### Fine-tuning

_Adapting a model. LoRA on one GPU vs. multi-node full fine-tunes._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | 🟢 Local | 78,244 (▲547) | Python | Mature | 2× faster, lower-VRAM fine-tuning — train a LoRA on a single consumer GPU (even Colab). |
| [huggingface/peft](https://github.com/huggingface/peft) | 🟡 Both | 21,807 (▲29) | Python | Classic | Parameter-efficient fine-tuning (LoRA/QLoRA/adapters) — one consumer GPU or a multi-node run. |
| [axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) | 🔴 Infra | 12,591 (▲40) | Python | Classic | Config-driven fine-tuning that scales to multi-GPU/multi-node (DeepSpeed/FSDP) — the cluster-grade trainer. |

### Agent framework

_The orchestration logic — deliberately tier-agnostic; it targets whatever endpoint you give it._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 🟡 Both | 59,863 (▲334) | Python | Mature | Role-based multi-agent framework — runs against any model backend, local or hosted. |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 🟡 Both | 52,566 (▲109) | Python | Classic | Data/agent framework — point it at a local Ollama or a cloud endpoint; tier-agnostic. |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 🟡 Both | 43,496 (▲481) | Python | Classic | Graph/stateful agent runtime — the orchestration logic is independent of where the model runs. |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | 🟡 Both | 20,726 (▲195) | Python | Mature | Type-safe agent framework; model-agnostic, so the same code targets either tier. |

### Observability & eval

_Tracing, metrics, and evals. Most self-host locally and also offer managed cloud._

| Tool | Tier | ★ Stars | Lang | Lifecycle | What it's for |
|---|---|---|---|---|---|
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 🟢 Local | 26,135 (▲266) | TypeScript | Classic | CLI-first prompt/model eval that runs entirely on your machine in CI — no backend needed. |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | 🟡 Both | 36,015 (▲415) | TypeScript | Classic | Self-hostable LLM tracing/eval/metrics — runs in Docker locally or as managed cloud. |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | 🟡 Both | 11,907 (▲133) | Python | Classic | Open-source LLM observability you can run locally; OTel-native tracing + evals. |

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
| [ollama](https://github.com/ollama/ollama) | Inference runtime | Local | Go | MIT | 183,801 (▲1,188) | Classic | 88 | very active | 1d ago | 15 |
| [open-webui](https://github.com/open-webui/open-webui) | Model gateway & UI | Local | Python | NOASSERTION | 156,140 (▲1,949) | Classic | 80 | very active | 1d ago | 6 |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Inference runtime | Local | C++ | MIT | 131,681 (▲947) | Classic | 99 | very active | 0d ago | 59 |
| [unsloth](https://github.com/unslothai/unsloth) | Fine-tuning | Local | Python | Apache-2.0 | 78,244 (▲547) | Mature | 85 | very active | 0d ago | 13 |
| [gpt4all](https://github.com/nomic-ai/gpt4all) | Inference runtime | Local | C++ | MIT | 77,350 (▼18) | Abandoned | 7 | stale | 1.4y ago | 0 |
| [anything-llm](https://github.com/Mintplex-Labs/anything-llm) | Model gateway & UI | Local | JavaScript | MIT | 67,308 (▲421) | Classic | 84 | very active | 2d ago | 20 |
| [LocalAI](https://github.com/mudler/LocalAI) | Inference runtime | Local | Go | MIT | 49,635 (▲178) | Classic | 84 | very active | 0d ago | 12 |
| [jan](https://github.com/janhq/jan) | Model gateway & UI | Local | Rust | NOASSERTION | 45,010 (▲134) | Classic | 84 | very active | 0d ago | 4 |
| [faiss](https://github.com/facebookresearch/faiss) | Vector store | Local | C++ | MIT | 41,166 (▲42) | Classic | 99 | very active | 1d ago | 40 |
| [llamafile](https://github.com/mozilla-ai/llamafile) | Inference runtime | Local | C++ | NOASSERTION | 26,431 (▲215) | Classic | 66 | very active | 7d ago | 8 |
| [promptfoo](https://github.com/promptfoo/promptfoo) | Observability & eval | Local | TypeScript | MIT | 26,135 (▲266) | Classic | 84 | very active | 0d ago | 12 |
| [zvec](https://github.com/alibaba/zvec) | Vector store | Local | C++ | Apache-2.0 | 16,126 (▲34) | Hot | 92 | very active | 0d ago | 17 |
| [txtai](https://github.com/neuml/txtai) | Vector store | Local | Python | Apache-2.0 | 13,027 (▲24) | Classic | 100 | very active | 3d ago | 36 |
| [lancedb](https://github.com/lancedb/lancedb) | Vector store | Local | Rust | Apache-2.0 | 11,701 (▲69) | Classic | 87 | very active | 0d ago | 24 |
| [foundry-local](https://github.com/microsoft/foundry-local) | Inference runtime | Local | C++ | NOASSERTION | 2,592 (▲14) | Hot | 83 | very active | 1d ago | 16 |
| [node-llama-cpp](https://github.com/withcatai/node-llama-cpp) | Inference runtime | Local | TypeScript | MIT | 2,192 (▲3) | Classic | 68 | active | 2d ago | 3 |
| [backburner](https://github.com/StayLameBro/backburner) | Inference runtime | Local | Python | MIT | 1,042 (▲116) | Hot | 62 | very active | 6d ago | 5 |
| [transformers](https://github.com/huggingface/transformers) | Inference runtime | Both | Python | Apache-2.0 | 167,850 (▲792) | Classic | 100 | very active | 0d ago | 43 |
| [redis](https://github.com/redis/redis) | Vector store | Both | C | NOASSERTION | 77,014 (▲319) | Classic | 97 | very active | 0d ago | 41 |
| [litellm](https://github.com/BerriAI/litellm) | Model gateway & UI | Both | Python | NOASSERTION | 61,553 (▲674) | Classic | 94 | very active | 0d ago | 23 |
| [crewAI](https://github.com/crewAIInc/crewAI) | Agent framework | Both | Python | MIT | 59,863 (▲334) | Mature | 84 | very active | 0d ago | 23 |
| [llama_index](https://github.com/run-llama/llama_index) | Agent framework | Both | Python | MIT | 52,566 (▲109) | Classic | 97 | very active | 5d ago | 53 |
| [exo](https://github.com/exo-explore/exo) | Inference runtime | Both | Python | Apache-2.0 | 47,954 (▲141) | Mature | 75 | very active | 6d ago | 2 |
| [langgraph](https://github.com/langchain-ai/langgraph) | Agent framework | Both | Python | MIT | 43,496 (▲481) | Classic | 83 | very active | 0d ago | 14 |
| [langfuse](https://github.com/langfuse/langfuse) | Observability & eval | Both | TypeScript | NOASSERTION | 36,015 (▲415) | Classic | 94 | very active | 0d ago | 21 |
| [qdrant](https://github.com/qdrant/qdrant) | Vector store | Both | Rust | Apache-2.0 | 35,136 (▲128) | Classic | 88 | very active | 0d ago | 17 |
| [chroma](https://github.com/chroma-core/chroma) | Vector store | Both | Rust | Apache-2.0 | 29,531 (▲59) | Classic | 82 | very active | 2d ago | 10 |
| [pgvector](https://github.com/pgvector/pgvector) | Vector store | Both | C | NOASSERTION | 23,408 (▲114) | Classic | 64 | very active | 1d ago | 3 |
| [peft](https://github.com/huggingface/peft) | Fine-tuning | Both | Python | Apache-2.0 | 21,807 (▲29) | Classic | 100 | very active | 0d ago | 42 |
| [pydantic-ai](https://github.com/pydantic/pydantic-ai) | Agent framework | Both | Python | MIT | 20,726 (▲195) | Mature | 77 | very active | 0d ago | 7 |
| [gateway](https://github.com/Portkey-AI/gateway) | Model gateway & UI | Both | TypeScript | MIT | 13,220 (▲59) | Mature | 41 | slowing | 4mo ago | 0 |
| [phoenix](https://github.com/Arize-ai/phoenix) | Observability & eval | Both | Python | NOASSERTION | 11,907 (▲133) | Classic | 84 | very active | 0d ago | 22 |
| [marqo](https://github.com/marqo-ai/marqo) | Vector store | Both | Python | Apache-2.0 | 5,028 | Mature | 45 | active | 1mo ago | 0 |
| [vllm](https://github.com/vllm-project/vllm) | Inference runtime | Infra | Python | Apache-2.0 | 94,123 (▲615) | Classic | 99 | very active | 0d ago | 68 |
| [milvus](https://github.com/milvus-io/milvus) | Vector store | Infra | Go | Apache-2.0 | 46,427 (▲80) | Classic | 99 | very active | 0d ago | 30 |
| [sglang](https://github.com/sgl-project/sglang) | Inference runtime | Infra | Python | Apache-2.0 | 37,364 (▲402) | Mature | 99 | very active | 0d ago | 53 |
| [weaviate](https://github.com/weaviate/weaviate) | Vector store | Infra | Go | NOASSERTION | 16,891 (▲13) | Classic | 83 | very active | 0d ago | 9 |
| [axolotl](https://github.com/axolotl-ai-cloud/axolotl) | Fine-tuning | Infra | Python | Apache-2.0 | 12,591 (▲40) | Classic | 79 | very active | 0d ago | 15 |
| [skypilot](https://github.com/skypilot-org/skypilot) | Scaling / serving infra | Infra | Python | Apache-2.0 | 10,721 (▲31) | Classic | 90 | very active | 0d ago | 22 |
| [lmdeploy](https://github.com/InternLM/lmdeploy) | Inference runtime | Infra | Python | Apache-2.0 | 8,109 (▲6) | Classic | 93 | very active | 0d ago | 25 |
| [llm-compressor](https://github.com/vllm-project/llm-compressor) | Scaling / serving infra | Infra | Python | Apache-2.0 | 3,885 (▲22) | Mature | 84 | very active | 2d ago | 30 |

## Graph analysis — how the stack hangs together

**Community clustering.** These 41 tools span **14 of the graph's 39 communities** — the stack cuts across the inference, RAG/vector, and agent neighborhoods rather than forming one cluster.

- **Community 20** (12): `ollama/ollama`, `ggml-org/llama.cpp`, `nomic-ai/gpt4all`, `vllm-project/vllm`, `sgl-project/sglang`, `InternLM/lmdeploy`, `vllm-project/llm-compressor`, `open-webui/open-webui`, `janhq/jan`, `marqo-ai/marqo`, `unslothai/unsloth`, `axolotl-ai-cloud/axolotl`
- **Community 18** (6): `lancedb/lancedb`, `pgvector/pgvector`, `alibaba/zvec`, `qdrant/qdrant`, `weaviate/weaviate`, `milvus-io/milvus`
- **Community 0** (4): `mozilla-ai/llamafile`, `exo-explore/exo`, `BerriAI/litellm`, `Portkey-AI/gateway`
- **Community 15** (4): `Mintplex-Labs/anything-llm`, `chroma-core/chroma`, `neuml/txtai`, `crewAIInc/crewAI`
- **Community 17** (3): `langfuse/langfuse`, `Arize-ai/phoenix`, `promptfoo/promptfoo`
- **Community 3** (2): `withcatai/node-llama-cpp`, `StayLameBro/backburner`
- **Community 25** (2): `huggingface/transformers`, `huggingface/peft`
- **Community 24** (2): `langchain-ai/langgraph`, `pydantic/pydantic-ai`

**Centrality (PageRank in the full 2,398-repo graph)** — the 'hub' tools your other stars cluster around:

- `langchain-ai/langgraph` — PageRank 0.0013 (🟡 Both)
- `axolotl-ai-cloud/axolotl` — PageRank 0.0010 (🔴 Infra)
- `qdrant/qdrant` — PageRank 0.0008 (🟡 Both)
- `crewAIInc/crewAI` — PageRank 0.0008 (🟡 Both)
- `neuml/txtai` — PageRank 0.0007 (🟢 Local)
- `vllm-project/vllm` — PageRank 0.0007 (🔴 Infra)
- `mudler/LocalAI` — PageRank 0.0006 (🟢 Local)
- `huggingface/transformers` — PageRank 0.0006 (🟡 Both)
- `unslothai/unsloth` — PageRank 0.0006 (🟢 Local)
- `microsoft/foundry-local` — PageRank 0.0006 (🟢 Local)

**Direct links between stack tools** (top similarity edges where both endpoints are in this report):

- `huggingface/peft` ⇄ `huggingface/transformers` (w=0.714) — topics: llm, python, pytorch; authors: michaelbenayoun, kaixuanliu
- `vllm-project/llm-compressor` ⇄ `vllm-project/vllm` (w=0.571) — authors: BeichenHuang
- `weaviate/weaviate` ⇄ `qdrant/qdrant` (w=0.509) — topics: search-engine, vector-search, vector-search-engine, vector-database; authors: dependabot[bot]
- `vllm-project/vllm` ⇄ `sgl-project/sglang` (w=0.424) — topics: llm, transformer, inference, llama; authors: cipheraxat
- `lancedb/lancedb` ⇄ `weaviate/weaviate` (w=0.400) — topics: approximate-nearest-neighbor-search, image-search, nearest-neighbor-search, recommender-system
- `BerriAI/litellm` ⇄ `Portkey-AI/gateway` (w=0.348) — topics: langchain, llm, llmops, openai
- `neuml/txtai` ⇄ `Mintplex-Labs/anything-llm` (w=0.325) — topics: llm, vector-database, rag, ai-agents; authors: devYRPauli, rtmalikian, MohammadHijjawi97
- `lancedb/lancedb` ⇄ `qdrant/qdrant` (w=0.323) — topics: image-search, nearest-neighbor-search, recommender-system, search-engine
- `InternLM/lmdeploy` ⇄ `axolotl-ai-cloud/axolotl` (w=0.295) — topics: llm; authors: Anai-Guo, li-lizhe, David-Wu1119
- `promptfoo/promptfoo` ⇄ `langfuse/langfuse` (w=0.269) — topics: llm, prompt-engineering, llmops, evaluation; authors: kumarpriyanshu09
- `sgl-project/sglang` ⇄ `ollama/ollama` (w=0.269) — topics: llama, llm, deepseek, gpt-oss
- `unslothai/unsloth` ⇄ `open-webui/open-webui` (w=0.257) — topics: llms, llm, openai, self-hosted
- `lancedb/lancedb` ⇄ `pgvector/pgvector` (w=0.250) — topics: approximate-nearest-neighbor-search, nearest-neighbor-search
- `milvus-io/milvus` ⇄ `weaviate/weaviate` (w=0.202) — topics: nearest-neighbor-search, vector-search, image-search, hnsw
- `pgvector/pgvector` ⇄ `weaviate/weaviate` (w=0.100) — topics: nearest-neighbor-search, approximate-nearest-neighbor-search

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). For infra you'll depend on, weight health + activity heavily.

| Tool | Tier | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|---|
| transformers | Both | 100 | Classic | very active | 9 | 9% | 277 |
| txtai | Local | 100 | Classic | very active | 5 | 33% | 68 |
| peft | Both | 100 | Classic | very active | 6 | 19% | 36 |
| llama.cpp | Local | 99 | Classic | very active | 15 | 9% | 7727 |
| vllm | Infra | 99 | Classic | very active | 18 | 8% | 108 |
| sglang | Infra | 99 | Mature | very active | 10 | 16% | 63 |
| faiss | Local | 99 | Classic | very active | 5 | 18% | 29 |
| milvus | Infra | 99 | Classic | very active | 5 | 17% | 177 |
| redis | Both | 97 | Classic | very active | 8 | 19% | 155 |
| llama_index | Both | 97 | Classic | very active | 11 | 15% | 497 |
| litellm | Both | 94 | Classic | very active | 4 | 18% | 1517 |
| langfuse | Both | 94 | Classic | very active | 4 | 24% | 719 |
| lmdeploy | Infra | 93 | Classic | very active | 4 | 21% | 71 |
| zvec | Local | 92 | Hot | very active | 4 | 16% | 13 |
| skypilot | Infra | 90 | Classic | very active | 3 | 25% | 45 |
| ollama | Local | 88 | Classic | very active | 3 | 31% | 265 |
| qdrant | Both | 88 | Classic | very active | 3 | 30% | 118 |
| lancedb | Local | 87 | Classic | very active | 3 | 35% | 527 |
| unsloth | Local | 85 | Mature | very active | 2 | 48% | 78 |
| LocalAI | Local | 84 | Classic | very active | 2 | 44% | 138 |
| llm-compressor | Infra | 84 | Mature | very active | 2 | 39% | 36 |
| jan | Local | 84 | Classic | very active | 2 | 44% | 106 |
| anything-llm | Local | 84 | Classic | very active | 2 | 35% | 38 |
| crewAI | Both | 84 | Mature | very active | 2 | 38% | 242 |
| phoenix | Both | 84 | Classic | very active | 2 | 48% | 869 |
| promptfoo | Local | 84 | Classic | very active | 2 | 40% | 430 |
| foundry-local | Local | 83 | Hot | very active | 2 | 32% | 25 |
| weaviate | Infra | 83 | Classic | very active | 2 | 37% | 601 |
| langgraph | Both | 83 | Classic | very active | 2 | 38% | 581 |
| chroma | Both | 82 | Classic | very active | 2 | 36% | 137 |
| open-webui | Local | 80 | Classic | very active | 1 | 59% | 175 |
| axolotl | Infra | 79 | Classic | very active | 1 | 60% | 35 |
| pydantic-ai | Both | 77 | Mature | very active | 1 | 56% | 343 |
| exo | Both | 75 | Mature | very active | 1 | 99% | 16 |
| node-llama-cpp | Local | 68 | Classic | active | 1 | 87% | 142 |
| llamafile | Local | 66 | Classic | very active | 1 | 50% | 43 |
| pgvector | Both | 64 | Classic | very active | 1 | 98% | 0 |
| backburner | Local | 62 | Hot | very active | 1 | 75% | 4 |
| marqo | Both | 45 | Mature | active | 0 | 0% | 113 |
| gateway | Both | 41 | Mature | slowing | 0 | 0% | 81 |
| gpt4all | Local | 7 | Abandoned | stale | 0 | 0% | 38 |

## Adjacent (covered elsewhere)

- **ggml-org/whisper.cpp** (54,481★) — speech runtime — covered in the *voice-agents* report
- **comet-ml/opik** (22,734★) — eval/observability — see the *LLM-evaluation* report
- **confident-ai/deepeval** (18,955★) — eval framework — see the *LLM-evaluation* report
- **langchain-ai/langchain** (148,069★) — broad agent toolkit — see the *agent-orchestration* report
- **microsoft/autogen** (61,478★) — multi-agent framework — see the *agent-orchestration* report

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Tiering** is an editorial judgment about each tool's *sweet spot*, not a hard limit — many 🟢 tools can be pushed onto servers and some 🔴 tools run (slowly) on a laptop. The tag reflects what the project is *optimized and typically used* for.
- **Selection**: keyword scan (inference / serving / vllm / ollama / vector db / gateway / fine-tune / quantize) + manual curation into stack layers. Speech runtimes, pure eval frameworks, and broad agent toolkits were routed to adjacent reports.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 41 · Tiers: 17 local / 16 both / 8 infra · Snapshot: 2026-10-19T11:27:31.266Z</sub>
