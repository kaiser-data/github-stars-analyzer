# RAG (Retrieval-Augmented Generation) Tooling — Landscape Report

> Derived from **kaiser-data**'s 1,071 starred repos (snapshot `2026-05-24T19:57:47.245Z`), cross-referenced with the repo-similarity graph (1,071 nodes / 3,486 edges, 23 communities).
>
> Generated 2026-06-02 by `scripts/reports/rag_tooling.py` (regenerate any time — no API cost).

## Executive summary

- **27 RAG tools** in your stars (**567,212★** combined) — the largest AI category here — organized along the RAG pipeline:
  - **RAG framework / engine** (10): `ragflow`, `llama_index`, `LightRAG`, `haystack`, `RAG-Anything`, `llmware`, `airweave`, `AdalFlow`, `GraphRAG-SDK`, `RAGLight`
  - **Vector DB / search** (7): `faiss`, `qdrant`, `chroma`, `pgvector`, `weaviate`, `zvec`, `FalkorDB`
  - **Ingestion / parsing / chunking** (4): `PaddleOCR`, `unstructured`, `chonkie`, `chonkiejs`
  - **Embeddings / rerankers** (3): `sentence-transformers`, `colpali`, `sie`
  - **Novel retrieval approach** (3): `PageIndex`, `LEANN`, `claude-context`
- Mental model — RAG is a pipeline: **ingest/parse → chunk → embed → store/index → retrieve/rerank → generate**. Each category above owns one stage; the frameworks stitch them together.
- Two clear trends: **GraphRAG** (graph-structured retrieval — `LightRAG`, `GraphRAG-SDK`, `FalkorDB`) and **post-vector** retrieval that questions the embed-everything default (`PageIndex` vectorless, `LEANN` 97% storage savings).
- Python dominates the frameworks; the vector-DB layer is mostly systems languages (Rust/Go/C/C++) for performance.

## The RAG pipeline at a glance

| Stage | What happens | Tools in your stars |
|---|---|---|
| **Ingest / parse** | PDFs, images, HTML → clean text/elements | `unstructured`, `PaddleOCR` |
| **Chunk** | Split documents into retrievable units | `chonkie`, `chonkiejs` |
| **Embed / rerank** | Encode chunks & queries; reorder hits | `sentence-transformers`, `colpali`, `sie` |
| **Store / index** | Persist vectors/graphs for ANN search | `qdrant`, `chroma`, `weaviate`, `pgvector`, `zvec`, `faiss`, `FalkorDB` |
| **Retrieve / generate** | Orchestrate retrieval + LLM answer | `ragflow`, `llama_index`, `haystack`, `LightRAG`, `RAG-Anything`, `llmware`, `AdalFlow`, `airweave`, `RAGLight`, `GraphRAG-SDK` |
| **Rethink** | Approaches that change the pipeline itself | `PageIndex` (vectorless), `LEANN` (tiny storage), `claude-context` (code) |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | RAG framework / engine | Python | Apache-2.0 | 81,143 | Mature | 96 | very active | 2d ago | 2.5y | 41 |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Ingestion / parsing / chunking | Python | Apache-2.0 | 78,454 | Classic | 85 | very active | 5d ago | 6.0y | 21 |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | RAG framework / engine | Python | MIT | 49,640 | Classic | 89 | very active | 4d ago | 3.6y | 40 |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | Vector DB / search | C++ | MIT | 40,116 | Classic | 88 | very active | 2d ago | 9.3y | 26 |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | RAG framework / engine | Python | MIT | 35,669 | Hot | 79 | very active | 0d ago | 1.6y | 6 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Novel retrieval approach | Python | MIT | 32,069 | Hot | 56 | very active | 9d ago | 1.1y | 8 |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | Vector DB / search | Rust | Apache-2.0 | 31,568 | Classic | 88 | very active | 0d ago | 6.0y | 14 |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | Vector DB / search | Rust | Apache-2.0 | 28,084 | Classic | 83 | very active | 0d ago | 3.6y | 12 |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | RAG framework / engine | MDX | Apache-2.0 | 25,361 | Classic | 85 | very active | 2d ago | 6.5y | 17 |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | Vector DB / search | C | NOASSERTION | 21,452 | Classic | 54 | very active | 27d ago | 5.1y | 3 |
| [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | RAG framework / engine | Python | MIT | 20,583 | Hot | 73 | very active | 2d ago | 11mo | 17 |
| [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers) | Embeddings / rerankers | Python | Apache-2.0 | 18,718 | Classic | 75 | very active | 3d ago | 6.8y | 10 |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | Vector DB / search | Go | BSD-3-Clause | 16,234 | Classic | 84 | very active | 0d ago | 10.2y | 11 |
| [llmware-ai/llmware](https://github.com/llmware-ai/llmware) | RAG framework / engine | Python | Apache-2.0 | 14,860 | Mature | 60 | very active | 7d ago | 2.7y | 1 |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | Ingestion / parsing / chunking | HTML | Apache-2.0 | 14,768 | Classic | 88 | very active | 1d ago | 3.7y | 13 |
| [yichuan-w/LEANN](https://github.com/yichuan-w/LEANN) | Novel retrieval approach | Python | MIT | 11,713 | Hot | 81 | very active | 1d ago | 11mo | 15 |
| [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | Novel retrieval approach | TypeScript | MIT | 11,549 | Hot | 61 | very active | 3d ago | 11mo | 17 |
| [alibaba/zvec](https://github.com/alibaba/zvec) | Vector DB / search | C++ | Apache-2.0 | 9,685 | Hot | 91 | very active | 1d ago | 5mo | 15 |
| [airweave-ai/airweave](https://github.com/airweave-ai/airweave) | RAG framework / engine | Python | MIT | 6,357 | Hot | 75 | very active | 2d ago | 1.4y | 5 |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | Vector DB / search | C | NOASSERTION | 4,456 | Mature | 84 | very active | 0d ago | 2.8y | 9 |
| [SylphAI-Inc/AdalFlow](https://github.com/SylphAI-Inc/AdalFlow) | RAG framework / engine | Python | MIT | 4,147 | Mature | 42 | active | 27d ago | 2.1y | 0 |
| [chonkie-inc/chonkie](https://github.com/chonkie-inc/chonkie) | Ingestion / parsing / chunking | Python | MIT | 4,087 | Hot | 78 | very active | 4d ago | 1.2y | 8 |
| [illuin-tech/colpali](https://github.com/illuin-tech/colpali) | Embeddings / rerankers | Python | MIT | 2,640 | Mature | 64 | active | 5d ago | 1.9y | 4 |
| [superlinked/sie](https://github.com/superlinked/sie) | Embeddings / rerankers | Python | Apache-2.0 | 1,952 | Mature | 71 | very active | 0d ago | 2.5y | 4 |
| [FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK) | RAG framework / engine | Python | Apache-2.0 | 903 | Mature | 76 | very active | 3d ago | 2.3y | 3 |
| [Bessouat40/RAGLight](https://github.com/Bessouat40/RAGLight) | RAG framework / engine | Python | MIT | 662 | Mature | 69 | slowing | 2mo ago | 1.4y | 1 |
| [chonkie-inc/chonkiejs](https://github.com/chonkie-inc/chonkiejs) | Ingestion / parsing / chunking | TypeScript | MIT | 342 | Hot | 66 | very active | 12d ago | 1.1y | 3 |

## By category

### RAG framework / engine

_End-to-end systems that orchestrate the whole pipeline. Engines (ragflow) are batteries-included apps; libraries (llama_index, haystack) are composable toolkits._

- **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** · 81,143★ · Python · Mature  
  Leading OSS RAG engine; deep document understanding + template-based chunking, batteries included.  
  <sub>topics: ai, ai-agents, context-engine, llm-apps, rag, retrieval-augmented-generation, agentic-ai, agentic-retrieval</sub>
- **[run-llama/llama_index](https://github.com/run-llama/llama_index)** · 49,640★ · Python · Classic  
  The 'document agent' framework — data connectors, indices, query engines; foundational RAG toolkit.  
  <sub>topics: agents, application, data, fine-tuning, framework, llamaindex, llm, rag</sub>
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 35,669★ · Python · Hot  
  Simple & fast RAG that builds a graph index over chunks (GraphRAG-style) for better multi-hop recall.  
  <sub>topics: knowledge-graph, large-language-models, retrieval-augmented-generation, genai, graphrag, llm, rag, gpt</sub>
- **[deepset-ai/haystack](https://github.com/deepset-ai/haystack)** · 25,361★ · MDX · Classic  
  Pipeline-oriented orchestration for production RAG / context-engineered LLM apps.  
  <sub>topics: nlp, question-answering, pytorch, semantic-search, information-retrieval, summarization, transformers, machine-learning</sub>
- **[HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything)** · 20,583★ · Python · Hot  
  All-in-one multimodal RAG over text, tables, images, equations.  
  <sub>topics: multi-modal-rag, retrieval-augmented-generation</sub>
- **[llmware-ai/llmware](https://github.com/llmware-ai/llmware)** · 14,860★ · Python · Mature  
  Enterprise RAG with small, specialized models; private-deployment focus.  
  <sub>topics: parsing, retrieval-augmented-generation, agents, generative-ai-tools, llamacpp, llm, small-specialized-models, onnx</sub>
- **[airweave-ai/airweave](https://github.com/airweave-ai/airweave)** · 6,357★ · Python · Hot  
  Context-retrieval layer that syncs apps/DBs into agent-queryable knowledge.  
  <sub>topics: llm, rag, search, agent-infrastructure, ai, ai-agents, ai-infrastructure, api</sub>
- **[SylphAI-Inc/AdalFlow](https://github.com/SylphAI-Inc/AdalFlow)** · 4,147★ · Python · Mature  
  Library to build & *auto-optimize* LLM/RAG apps (prompt + retriever tuning).  
  <sub>topics: agent, framework, llm, rag, generative-ai, machine-learning, nlp, python</sub>
- **[FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK)** · 903★ · Python · Mature  
  SDK to build GraphRAG apps on FalkorDB at scale.  
  <sub>topics: falkordb, graphrag, knowledge-graph, rag, graph-database, open-source, sdk, genai</sub>
- **[Bessouat40/RAGLight](https://github.com/Bessouat40/RAGLight)** · 662★ · Python · Mature  
  Lightweight modular RAG framework for quick pipelines.  
  <sub>topics: data-science, framework, huggingface, ollama, retrieval-augmented-generation, vector-database, artificial-intelligence, rag</sub>

### Vector DB / search

_Where embeddings live and approximate-nearest-neighbour search happens. Choice often comes down to scale, hybrid search, and ops footprint._

- **[facebookresearch/faiss](https://github.com/facebookresearch/faiss)** · 40,116★ · C++ · Classic  
  Foundational dense-vector similarity-search library; the index under many DBs.  
  <sub>topics: —</sub>
- **[qdrant/qdrant](https://github.com/qdrant/qdrant)** · 31,568★ · Rust · Classic  
  High-performance, massive-scale vector DB & search engine (Rust).  
  <sub>topics: neural-network, search-engine, knn-algorithm, hnsw, vector-search, nearest-neighbor-search, image-search, embeddings-similarity</sub>
- **[chroma-core/chroma](https://github.com/chroma-core/chroma)** · 28,084★ · Rust · Classic  
  AI-native search/vector DB; popular default for prototyping RAG.  
  <sub>topics: database, rust, rust-lang, ai, agents, ai-agents</sub>
- **[pgvector/pgvector](https://github.com/pgvector/pgvector)** · 21,452★ · C · Classic  
  Vector similarity search as a Postgres extension — RAG without new infra.  
  <sub>topics: nearest-neighbor-search, approximate-nearest-neighbor-search</sub>
- **[weaviate/weaviate](https://github.com/weaviate/weaviate)** · 16,234★ · Go · Classic  
  Vector DB storing objects + vectors with hybrid (keyword+vector) search.  
  <sub>topics: search-engine, semantic-search, semantic-search-engine, vector-search, vector-search-engine, vector-database, approximate-nearest-neighbor-search, image-search</sub>
- **[alibaba/zvec](https://github.com/alibaba/zvec)** · 9,685★ · C++ · Hot  
  Lightweight, lightning-fast in-process vector database.  
  <sub>topics: rag, agent-skills, embedded, faiss, hnsw, llm-memory, search-engine, semantic-search</sub>
- **[FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB)** · 4,456★ · C · Mature  
  Fast graph database (GraphBLAS) — substrate for graph-shaped retrieval.  
  <sub>topics: graph-database, knowledge-graph, database-as-a-service, cloud-database, database, developer-tools, devtools, realtime-database</sub>

### Ingestion / parsing / chunking

_The unglamorous-but-decisive front of the pipeline: garbage chunks in → garbage retrieval out._

- **[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** · 78,454★ · Python · Classic  
  Powerful OCR — turns PDFs/images into structured text for the RAG ingest stage.  
  <sub>topics: ocr, chineseocr, pdf2markdown, pp-ocr, pp-structure, document-parsing, document-translation, kie</sub>
- **[Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)** · 14,768★ · HTML · Classic  
  ETL that turns PDFs/docs/HTML into clean, chunk-ready structured elements.  
  <sub>topics: deep-learning, document-parsing, machine-learning, nlp, ocr, information-retrieval, data-pipelines, ml</sub>
- **[chonkie-inc/chonkie](https://github.com/chonkie-inc/chonkie)** · 4,087★ · Python · Hot  
  Lightweight, fast chunking library (the 🦛) — many strategies, minimal deps.  
  <sub>topics: rag, chonkie, chunker, chunking-algorithm, retrieval-systems, semantic-chunker, similarity-search, text-splitter</sub>
- **[chonkie-inc/chonkiejs](https://github.com/chonkie-inc/chonkiejs)** · 342★ · TypeScript · Hot  
  TypeScript port of Chonkie for JS/TS RAG pipelines.  
  <sub>topics: typescript, ai, splitting-algorithms, chunker, rag, retrieval-systems, chunking-algorithm, text-splitter</sub>

### Embeddings / rerankers

_The models that turn text (or page images) into vectors and reorder candidate hits for precision._

- **[huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers)** · 18,718★ · Python · Classic  
  SoTA embeddings, retrieval & reranking models — the encoder layer of RAG.  
  <sub>topics: —</sub>
- **[illuin-tech/colpali](https://github.com/illuin-tech/colpali)** · 2,640★ · Python · Mature  
  Vision embeddings (ColPali/ColQwen) for document retrieval straight from page images.  
  <sub>topics: colpali, information-retrieval, retrieval-augmented-generation, vision-language-model, colqwen2, colsmol</sub>
- **[superlinked/sie](https://github.com/superlinked/sie)** · 1,952★ · Python · Mature  
  Inference engine/server for embeddings & rerankers in production retrieval.  
  <sub>topics: embeddings, vector-search, data-pipeline, deep-learning, information-retrieval, llm, ml, mlops</sub>

### Novel retrieval approach

_Projects challenging the embed-everything-into-a-vector-DB default — vectorless, storage-frugal, or domain-specialized retrieval._

- **[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** · 32,069★ · Python · Hot  
  Vectorless, reasoning-based RAG — builds a document index/tree, navigates with the LLM.  
  <sub>topics: agentic-ai, agents, ai, ai-agents, context-engineering, llm, rag, reasoning</sub>
- **[yichuan-w/LEANN](https://github.com/yichuan-w/LEANN)** · 11,713★ · Python · Hot  
  Storage-frugal RAG: ~97% storage savings while keeping fast, accurate retrieval.  
  <sub>topics: ai, faiss, langchain, llama-index, llm, localstorage, offline-first, ollama</sub>
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 11,549★ · TypeScript · Hot  
  Code-search MCP that makes an entire codebase the retrievable context for coding agents.  
  <sub>topics: agent, agentic-rag, ai-coding, code-search, cursor, embedding, mcp, nodejs</sub>

## Spotlight: GraphRAG

A cross-cutting trend — instead of a flat vector store, build a **knowledge graph** over chunks so retrieval can follow relationships (better for multi-hop questions). In your stars:

- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 35,669★ — Simple & fast RAG that builds a graph index over chunks (GraphRAG-style) for better multi-hop recall.
- **[FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK)** · 903★ — SDK to build GraphRAG apps on FalkorDB at scale.
- **[FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB)** · 4,456★ — Fast graph database (GraphBLAS) — substrate for graph-shaped retrieval.

## Graph analysis — how they relate

**Community clustering.** These 27 tools span **12 of the graph's 23 communities**.

- **Community 12** (8): `infiniflow/ragflow`, `deepset-ai/haystack`, `llmware-ai/llmware`, `SylphAI-Inc/AdalFlow`, `airweave-ai/airweave`, `Bessouat40/RAGLight`, `VectifyAI/PageIndex`, `yichuan-w/LEANN`
- **Community 9** (3): `qdrant/qdrant`, `weaviate/weaviate`, `alibaba/zvec`
- **Community 3** (3): `chonkie-inc/chonkie`, `chonkie-inc/chonkiejs`, `illuin-tech/colpali`
- **Community 10** (2): `HKUDS/LightRAG`, `HKUDS/RAG-Anything`
- **Community 11** (2): `FalkorDB/GraphRAG-SDK`, `FalkorDB/FalkorDB`
- **Community 8** (2): `facebookresearch/faiss`, `PaddlePaddle/PaddleOCR`
- **Community 6** (2): `Unstructured-IO/unstructured`, `superlinked/sie`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' RAG tools in your ecosystem:

- `VectifyAI/PageIndex` — PageRank 0.0030
- `HKUDS/LightRAG` — PageRank 0.0018
- `FalkorDB/FalkorDB` — PageRank 0.0015
- `FalkorDB/GraphRAG-SDK` — PageRank 0.0015
- `huggingface/sentence-transformers` — PageRank 0.0013
- `chonkie-inc/chonkie` — PageRank 0.0012
- `chroma-core/chroma` — PageRank 0.0012
- `weaviate/weaviate` — PageRank 0.0011
- `HKUDS/RAG-Anything` — PageRank 0.0011
- `deepset-ai/haystack` — PageRank 0.0011

**Direct links between RAG tools** (top similarity edges where both endpoints are in this report):

- `chonkie-inc/chonkiejs` ⇄ `chonkie-inc/chonkie` (w=1.778) — topics: ai, splitting-algorithms, chunker, rag; authors: chonk-lain, chonknick
- `FalkorDB/GraphRAG-SDK` ⇄ `FalkorDB/FalkorDB` (w=0.700) — topics: graphrag, knowledge-graph, graph-database
- `HKUDS/RAG-Anything` ⇄ `HKUDS/LightRAG` (w=0.650) — topics: retrieval-augmented-generation
- `FalkorDB/GraphRAG-SDK` ⇄ `HKUDS/LightRAG` (w=0.435) — topics: graphrag, knowledge-graph, rag, genai
- `weaviate/weaviate` ⇄ `qdrant/qdrant` (w=0.429) — topics: search-engine, vector-search, vector-search-engine, vector-database
- `SylphAI-Inc/AdalFlow` ⇄ `deepset-ai/haystack` (w=0.379) — topics: agent, llm, rag, generative-ai
- `VectifyAI/PageIndex` ⇄ `infiniflow/ragflow` (w=0.344) — topics: agentic-ai, ai, ai-agents, rag
- `VectifyAI/PageIndex` ⇄ `airweave-ai/airweave` (w=0.330) — topics: ai, ai-agents, llm, rag
- `VectifyAI/PageIndex` ⇄ `deepset-ai/haystack` (w=0.314) — topics: agents, ai, llm, rag; authors: dependabot[bot]
- `HKUDS/LightRAG` ⇄ `deepset-ai/haystack` (w=0.299) — topics: large-language-models, retrieval-augmented-generation, llm, rag; authors: dependabot[bot]
- `VectifyAI/PageIndex` ⇄ `yichuan-w/LEANN` (w=0.267) — topics: ai, llm, rag, retrieval-augmented-generation
- `VectifyAI/PageIndex` ⇄ `llmware-ai/llmware` (w=0.217) — topics: agents, llm, retrieval-augmented-generation
- `yichuan-w/LEANN` ⇄ `infiniflow/ragflow` (w=0.217) — topics: ai, rag, retrieval-augmented-generation; authors: qizwiz
- `FalkorDB/GraphRAG-SDK` ⇄ `airweave-ai/airweave` (w=0.210) — topics: rag, open-source, sdk, llm
- `alibaba/zvec` ⇄ `qdrant/qdrant` (w=0.209) — topics: hnsw, search-engine, similarity-search, vector-database; authors: dependabot[bot]
- …and 6 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| infiniflow/ragflow | 96 | Mature | very active | 8 | 10% | 46 |
| alibaba/zvec | 91 | Hot | very active | 4 | 20% | 7 |
| run-llama/llama_index | 89 | Classic | very active | 3 | 36% | 494 |
| qdrant/qdrant | 88 | Classic | very active | 3 | 27% | 113 |
| facebookresearch/faiss | 88 | Classic | very active | 3 | 22% | 26 |
| Unstructured-IO/unstructured | 88 | Classic | very active | 4 | 20% | 229 |
| deepset-ai/haystack | 85 | Classic | very active | 2 | 33% | 226 |
| PaddlePaddle/PaddleOCR | 85 | Classic | very active | 3 | 24% | 31 |
| weaviate/weaviate | 84 | Classic | very active | 2 | 48% | 534 |
| FalkorDB/FalkorDB | 84 | Mature | very active | 3 | 28% | 73 |
| chroma-core/chroma | 83 | Classic | very active | 2 | 27% | 137 |
| yichuan-w/LEANN | 81 | Hot | very active | 3 | 30% | 29 |
| HKUDS/LightRAG | 79 | Hot | very active | 1 | 81% | 72 |
| chonkie-inc/chonkie | 78 | Hot | very active | 1 | 70% | 42 |
| FalkorDB/GraphRAG-SDK | 76 | Mature | very active | 1 | 80% | 28 |
| airweave-ai/airweave | 75 | Hot | very active | 1 | 51% | 468 |
| huggingface/sentence-transformers | 75 | Classic | very active | 1 | 88% | 66 |
| HKUDS/RAG-Anything | 73 | Hot | very active | 1 | 52% | 19 |
| superlinked/sie | 71 | Mature | very active | 1 | 63% | 709 |
| Bessouat40/RAGLight | 69 | Mature | slowing | 1 | 100% | 45 |
| chonkie-inc/chonkiejs | 66 | Hot | very active | 1 | 77% | 5 |
| illuin-tech/colpali | 64 | Mature | active | 1 | 64% | 21 |
| zilliztech/claude-context | 61 | Hot | very active | 2 | 46% | 0 |
| llmware-ai/llmware | 60 | Mature | very active | 1 | 100% | 3 |
| VectifyAI/PageIndex | 56 | Hot | very active | 2 | 46% | 0 |
| pgvector/pgvector | 54 | Classic | very active | 1 | 84% | 0 |
| SylphAI-Inc/AdalFlow | 42 | Mature | active | 0 | 0% | 7 |

## Which one should you use?

| If you want… | Start with | Why |
|---|---|---|
| A batteries-included RAG app over your docs | `infiniflow/ragflow` | Most-starred engine here (health 96); strong document parsing + chunking out of the box. |
| A composable toolkit to build custom RAG | `run-llama/llama_index` or `deepset-ai/haystack` | Mature libraries; connectors, indices, and pipeline primitives. |
| Graph-structured / multi-hop retrieval | `HKUDS/LightRAG` | Fast GraphRAG; builds an entity graph over chunks. |
| A production vector store at scale | `qdrant/qdrant` | High-performance Rust vector DB; health 88, widely deployed. |
| RAG with zero new infrastructure | `pgvector/pgvector` | Adds vector search to the Postgres you already run. |
| Best document parsing for ingestion | `Unstructured-IO/unstructured` (+ `PaddleOCR`) | Turns messy PDFs/HTML into clean, chunkable elements; OCR for scanned docs. |
| Good chunking without heavy deps | `chonkie-inc/chonkie` | Lightweight, many strategies; JS port available. |
| To skip vector DBs entirely | `VectifyAI/PageIndex` | Vectorless, reasoning-based retrieval over a document tree. |
| Tiny-footprint / on-device RAG | `yichuan-w/LEANN` | ~97% storage savings vs. a conventional vector index. |

## Adjacent (deliberately not listed as RAG tools)

- **langchain-ai/langchain** (137,543★) — general agent/LLM framework — RAG is one use case, too broad to list as RAG-specific
- **topoteretes/cognee** (17,491★) — covered in the *memory frameworks* report (graph memory, RAG-adjacent)
- **memvid/memvid** (15,559★) — covered in the *memory frameworks* report
- **NirDiamant/RAG_Techniques** (27,531★) — excellent *tutorial* collection, not a tool/library
- **KRLabsOrg/LettuceDetect** (576★) — RAG *evaluation* (hallucination detection) — see the LLM-evaluation report

## Methodology & caveats

- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (rag / retrieval-augmented / graphrag / vector db / embedding / rerank / chunk / semantic-search) + manual curation into pipeline stages. Tutorials, general agent frameworks, and memory-layer projects were routed to adjacent reports or excluded (see above).
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 27 · Snapshot: 2026-05-24T19:57:47.245Z</sub>
