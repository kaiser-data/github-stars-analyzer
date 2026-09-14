# RAG (Retrieval-Augmented Generation) Tooling — Landscape Report

> Derived from **kaiser-data**'s 2,159 starred repos (snapshot `2026-09-14T11:08:08.535Z`), cross-referenced with the repo-similarity graph (2,159 nodes / 7,086 edges, 37 communities).
>
> Generated 2026-09-14 by `scripts/reports/rag_tooling.py` (regenerate any time — no API cost).

![Top tools by stars](assets/rag-tooling-top-tools.svg)

![Tools per category](assets/rag-tooling-categories.svg)


## Executive summary

- **31 RAG tools** in your stars (**727,344★** combined) — the largest AI category here — organized along the RAG pipeline:
  - **RAG framework / engine** (11): `ragflow`, `llama_index`, `LightRAG`, `graphrag`, `haystack`, `RAG-Anything`, `llmware`, `txtai`, `AdalFlow`, `GraphRAG-SDK`, `RAGLight`
  - **Vector DB / search** (10): `milvus`, `faiss`, `qdrant`, `chroma`, `pgvector`, `weaviate`, `zvec`, `lancedb`, `FalkorDB`, `marqo`
  - **Ingestion / parsing / chunking** (4): `PaddleOCR`, `unstructured`, `chonkie`, `chonkiejs`
  - **Embeddings / rerankers** (3): `sentence-transformers`, `sie`, `colpali`
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
|---|---|---|---|---|---|---|---|---|---|---|
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | RAG framework / engine | Go | Apache-2.0 | 90,667 (▲554) | Mature | 98 | very active | 0d ago | 2.8y | 44 |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Ingestion / parsing / chunking | Python | Apache-2.0 | 89,488 (▲547) | Mature | 65 | active | 1mo ago | 6.4y | 4 |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | RAG framework / engine | Python | MIT | 52,155 (▲124) | Classic | 98 | very active | 3d ago | 3.9y | 60 |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | Vector DB / search | Go | Apache-2.0 | 46,101 (▲107) | Classic | 99 | very active | 0d ago | 7.0y | 33 |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | Vector DB / search | C++ | MIT | 40,903 (▲44) | Classic | 99 | very active | 0d ago | 9.6y | 42 |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | RAG framework / engine | Python | MIT | 39,633 (▲204) | Hot | 79 | very active | 0d ago | 2.0y | 8 |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | RAG framework / engine | Python | MIT | 35,972 (▲122) | Mature | 71 | very active | 0d ago | 2.5y | 4 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Novel retrieval approach | Python | MIT | 35,643 (▲99) | Hot | 77 | very active | 1d ago | 1.5y | 4 |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | Vector DB / search | Rust | Apache-2.0 | 34,536 (▲132) | Classic | 93 | very active | 0d ago | 6.3y | 22 |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | Vector DB / search | Rust | Apache-2.0 | 29,294 (▲58) | Classic | 83 | very active | 2d ago | 3.9y | 9 |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | RAG framework / engine | Python | Apache-2.0 | 26,509 (▲79) | Classic | 90 | very active | 0d ago | 6.8y | 36 |
| [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | RAG framework / engine | Python | MIT | 23,316 (▲95) | Hot | 75 | very active | 12d ago | 1.3y | 15 |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | Vector DB / search | C | NOASSERTION | 23,008 (▲84) | Classic | 65 | very active | 4d ago | 5.4y | 3 |
| [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers) | Embeddings / rerankers | Python | Apache-2.0 | 19,093 (▲19) | Classic | 75 | very active | 3d ago | 7.1y | 24 |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | Vector DB / search | Go | NOASSERTION | 16,805 (▲20) | Classic | 78 | very active | 0d ago | 10.5y | 9 |
| [alibaba/zvec](https://github.com/alibaba/zvec) | Vector DB / search | C++ | Apache-2.0 | 15,915 (▲115) | Hot | 93 | very active | 0d ago | 9mo | 17 |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | Ingestion / parsing / chunking | HTML | Apache-2.0 | 15,425 (▲26) | Classic | 80 | very active | 4d ago | 4.0y | 13 |
| [llmware-ai/llmware](https://github.com/llmware-ai/llmware) | RAG framework / engine | Python | Apache-2.0 | 14,843 (▼6) | Mature | 32 | slowing | 4mo ago | 3.0y | 0 |
| [neuml/txtai](https://github.com/neuml/txtai) | RAG framework / engine | Python | Apache-2.0 | 12,947 (▲20) | Classic | 85 | very active | 3d ago | 6.1y | 16 |
| [StarTrail-org/LEANN](https://github.com/StarTrail-org/LEANN) | Novel retrieval approach | Python | MIT | 12,935 (▲44) | Hot | 77 | very active | 9d ago | 1.3y | 17 |
| [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | Novel retrieval approach | TypeScript | MIT | 12,525 (▲39) | Declining | 39 | slowing | 2mo ago | 1.3y | 2 |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | Vector DB / search | Rust | Apache-2.0 | 11,419 (▲57) | Classic | 92 | very active | 0d ago | 3.5y | 14 |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | Vector DB / search | Rust | NOASSERTION | 6,092 (▲188) | Classic | 80 | very active | 0d ago | 3.2y | 10 |
| [marqo-ai/marqo](https://github.com/marqo-ai/marqo) | Vector DB / search | Python | Apache-2.0 | 5,032 | Mature | 48 | active | 11d ago | 4.1y | 0 |
| [feyninc/chonkie](https://github.com/feyninc/chonkie) | Ingestion / parsing / chunking | Python | MIT | 4,744 (▲21) | Hot | 74 | very active | 12d ago | 1.5y | 5 |
| [SylphAI-Inc/AdalFlow](https://github.com/SylphAI-Inc/AdalFlow) | RAG framework / engine | Python | MIT | 4,213 | Mature | 29 | slowing | 3mo ago | 2.4y | 0 |
| [superlinked/sie](https://github.com/superlinked/sie) | Embeddings / rerankers | Python | Apache-2.0 | 3,281 (▲65) | Mature | 79 | very active | 4d ago | 2.9y | 11 |
| [illuin-tech/colpali](https://github.com/illuin-tech/colpali) | Embeddings / rerankers | Python | MIT | 2,810 (▲1) | Mature | 63 | active | 6d ago | 2.2y | 3 |
| [FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK) | RAG framework / engine | Python | Apache-2.0 | 999 (▲4) | Mature | 77 | very active | 0d ago | 2.6y | 3 |
| [Bessouat40/RAGLight](https://github.com/Bessouat40/RAGLight) | RAG framework / engine | Python | MIT | 672 (▼1) | Mature | 61 | active | 12d ago | 1.8y | 1 |
| [feyninc/chonkiejs](https://github.com/feyninc/chonkiejs) | Ingestion / parsing / chunking | TypeScript | MIT | 369 (▼1) | Mature | 71 | very active | 3d ago | 1.4y | 1 |

## By category

### RAG framework / engine

_End-to-end systems that orchestrate the whole pipeline. Engines (ragflow) are batteries-included apps; libraries (llama_index, haystack) are composable toolkits._

- **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** · 90,667★ · Go · Mature  
  Leading OSS RAG engine; deep document understanding + template-based chunking, batteries included.  
  <sub>topics: ai, ai-agents, context-engine, rag, retrieval-augmented-generation, agentic-ai, agentic-retrieval, agentic-search</sub>
- **[run-llama/llama_index](https://github.com/run-llama/llama_index)** · 52,155★ · Python · Classic  
  The 'document agent' framework — data connectors, indices, query engines; foundational RAG toolkit.  
  <sub>topics: agents, application, data, fine-tuning, framework, llamaindex, llm, rag</sub>
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 39,633★ · Python · Hot  
  Simple & fast RAG that builds a graph index over chunks (GraphRAG-style) for better multi-hop recall.  
  <sub>topics: knowledge-graph, large-language-models, retrieval-augmented-generation, genai, graphrag, llm, rag, gpt</sub>
- **[microsoft/graphrag](https://github.com/microsoft/graphrag)** · 35,972★ · Python · Mature  
  Microsoft's reference GraphRAG — LLM-built entity graph + community summaries over a corpus.  
  <sub>topics: graphrag, rag, llm, llms, gpt, gpt-4, gpt4</sub>
- **[deepset-ai/haystack](https://github.com/deepset-ai/haystack)** · 26,509★ · Python · Classic  
  Pipeline-oriented orchestration for production RAG / context-engineered LLM apps.  
  <sub>topics: semantic-search, information-retrieval, ai, python, large-language-models, generative-ai, llm, rag</sub>
- **[HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything)** · 23,316★ · Python · Hot  
  All-in-one multimodal RAG over text, tables, images, equations.  
  <sub>topics: multi-modal-rag, retrieval-augmented-generation</sub>
- **[llmware-ai/llmware](https://github.com/llmware-ai/llmware)** · 14,843★ · Python · Mature  
  Enterprise RAG with small, specialized models; private-deployment focus.  
  <sub>topics: parsing, retrieval-augmented-generation, agents, generative-ai-tools, llamacpp, llm, small-specialized-models, onnx</sub>
- **[neuml/txtai](https://github.com/neuml/txtai)** · 12,947★ · Python · Classic  
  All-in-one embeddings DB + RAG + workflows in one package.  
  <sub>topics: python, search, nlp, semantic-search, vector-search, txtai, llm, vector-database</sub>
- **[SylphAI-Inc/AdalFlow](https://github.com/SylphAI-Inc/AdalFlow)** · 4,213★ · Python · Mature  
  Library to build & *auto-optimize* LLM/RAG apps (prompt + retriever tuning).  
  <sub>topics: agent, framework, llm, rag, generative-ai, machine-learning, nlp, python</sub>
- **[FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK)** · 999★ · Python · Mature  
  SDK to build GraphRAG apps on FalkorDB at scale.  
  <sub>topics: falkordb, graphrag, knowledge-graph, rag, graph-database, open-source, sdk, genai</sub>
- **[Bessouat40/RAGLight](https://github.com/Bessouat40/RAGLight)** · 672★ · Python · Mature  
  Lightweight modular RAG framework for quick pipelines.  
  <sub>topics: data-science, framework, huggingface, ollama, retrieval-augmented-generation, vector-database, artificial-intelligence, rag</sub>

### Vector DB / search

_Where embeddings live and approximate-nearest-neighbour search happens. Choice often comes down to scale, hybrid search, and ops footprint._

- **[milvus-io/milvus](https://github.com/milvus-io/milvus)** · 46,101★ · Go · Classic  
  Largest-scale OSS vector database — distributed, billion-vector ANN search.  
  <sub>topics: anns, nearest-neighbor-search, faiss, vector-search, image-search, hnsw, vector-database, embedding-database</sub>
- **[facebookresearch/faiss](https://github.com/facebookresearch/faiss)** · 40,903★ · C++ · Classic  
  Foundational dense-vector similarity-search library; the index under many DBs.  
  <sub>topics: —</sub>
- **[qdrant/qdrant](https://github.com/qdrant/qdrant)** · 34,536★ · Rust · Classic  
  High-performance, massive-scale vector DB & search engine (Rust).  
  <sub>topics: neural-network, search-engine, knn-algorithm, hnsw, vector-search, nearest-neighbor-search, image-search, embeddings-similarity</sub>
- **[chroma-core/chroma](https://github.com/chroma-core/chroma)** · 29,294★ · Rust · Classic  
  AI-native search/vector DB; popular default for prototyping RAG.  
  <sub>topics: database, rust, rust-lang, ai, agents, ai-agents</sub>
- **[pgvector/pgvector](https://github.com/pgvector/pgvector)** · 23,008★ · C · Classic  
  Vector similarity search as a Postgres extension — RAG without new infra.  
  <sub>topics: nearest-neighbor-search, approximate-nearest-neighbor-search</sub>
- **[weaviate/weaviate](https://github.com/weaviate/weaviate)** · 16,805★ · Go · Classic  
  Vector DB storing objects + vectors with hybrid (keyword+vector) search.  
  <sub>topics: search-engine, semantic-search, semantic-search-engine, vector-search, vector-search-engine, vector-database, approximate-nearest-neighbor-search, image-search</sub>
- **[alibaba/zvec](https://github.com/alibaba/zvec)** · 15,915★ · C++ · Hot  
  Lightweight, lightning-fast in-process vector database.  
  <sub>topics: rag, agent-skills, embedded, faiss, hnsw, llm-memory, search-engine, semantic-search</sub>
- **[lancedb/lancedb](https://github.com/lancedb/lancedb)** · 11,419★ · Rust · Classic  
  Embedded, serverless vector DB (columnar/Lance format); zero-ops local RAG.  
  <sub>topics: approximate-nearest-neighbor-search, image-search, nearest-neighbor-search, recommender-system, search-engine, semantic-search, similarity-search, vector-database</sub>
- **[FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB)** · 6,092★ · Rust · Classic  
  Fast graph database (GraphBLAS) — substrate for graph-shaped retrieval.  
  <sub>topics: graph-database, knowledge-graph, database-as-a-service, cloud-database, database, developer-tools, devtools, realtime-database</sub>
- **[marqo-ai/marqo](https://github.com/marqo-ai/marqo)** · 5,032★ · Python · Mature  
  End-to-end vector search that bundles embedding inference (text + image).  
  <sub>topics: multi-modal, search-engine, machine-learning, ecommerce</sub>

### Ingestion / parsing / chunking

_The unglamorous-but-decisive front of the pipeline: garbage chunks in → garbage retrieval out._

- **[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** · 89,488★ · Python · Mature  
  Powerful OCR — turns PDFs/images into structured text for the RAG ingest stage.  
  <sub>topics: ocr, chineseocr, pdf2markdown, pp-ocr, pp-structure, document-parsing, document-translation, kie</sub>
- **[Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)** · 15,425★ · HTML · Classic  
  ETL that turns PDFs/docs/HTML into clean, chunk-ready structured elements.  
  <sub>topics: deep-learning, document-parsing, machine-learning, nlp, ocr, information-retrieval, data-pipelines, ml</sub>
- **[feyninc/chonkie](https://github.com/feyninc/chonkie)** · 4,744★ · Python · Hot  
  Lightweight, fast chunking library (the 🦛) — many strategies, minimal deps.  
  <sub>topics: rag, chonkie, chunker, chunking-algorithm, retrieval-systems, semantic-chunker, similarity-search, text-splitter</sub>
- **[feyninc/chonkiejs](https://github.com/feyninc/chonkiejs)** · 369★ · TypeScript · Mature  
  TypeScript port of Chonkie for JS/TS RAG pipelines.  
  <sub>topics: typescript, ai, splitting-algorithms, chunker, rag, retrieval-systems, chunking-algorithm, text-splitter</sub>

### Embeddings / rerankers

_The models that turn text (or page images) into vectors and reorder candidate hits for precision._

- **[huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers)** · 19,093★ · Python · Classic  
  SoTA embeddings, retrieval & reranking models — the encoder layer of RAG.  
  <sub>topics: —</sub>
- **[superlinked/sie](https://github.com/superlinked/sie)** · 3,281★ · Python · Mature  
  Inference engine/server for embeddings & rerankers in production retrieval.  
  <sub>topics: embeddings, vector-search, data-pipeline, deep-learning, information-retrieval, llm, ml, mlops</sub>
- **[illuin-tech/colpali](https://github.com/illuin-tech/colpali)** · 2,810★ · Python · Mature  
  Vision embeddings (ColPali/ColQwen) for document retrieval straight from page images.  
  <sub>topics: colpali, information-retrieval, retrieval-augmented-generation, vision-language-model, colqwen2, colsmol</sub>

### Novel retrieval approach

_Projects challenging the embed-everything-into-a-vector-DB default — vectorless, storage-frugal, or domain-specialized retrieval._

- **[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** · 35,643★ · Python · Hot  
  Vectorless, reasoning-based RAG — builds a document index/tree, navigates with the LLM.  
  <sub>topics: agentic-ai, agents, ai, ai-agents, context-engineering, llm, rag, reasoning</sub>
- **[StarTrail-org/LEANN](https://github.com/StarTrail-org/LEANN)** · 12,935★ · Python · Hot  
  Storage-frugal RAG: ~97% storage savings while keeping fast, accurate retrieval.  
  <sub>topics: ai, faiss, langchain, llama-index, llm, localstorage, offline-first, ollama</sub>
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,525★ · TypeScript · Declining  
  Code-search MCP that makes an entire codebase the retrievable context for coding agents.  
  <sub>topics: agent, agentic-rag, ai-coding, code-search, cursor, embedding, mcp, nodejs</sub>

## Spotlight: GraphRAG

A cross-cutting trend — instead of a flat vector store, build a **knowledge graph** over chunks so retrieval can follow relationships (better for multi-hop questions). In your stars:

- **[microsoft/graphrag](https://github.com/microsoft/graphrag)** · 35,972★ — Microsoft's reference GraphRAG — LLM-built entity graph + community summaries over a corpus.
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 39,633★ — Simple & fast RAG that builds a graph index over chunks (GraphRAG-style) for better multi-hop recall.
- **[FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK)** · 999★ — SDK to build GraphRAG apps on FalkorDB at scale.
- **[FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB)** · 6,092★ — Fast graph database (GraphBLAS) — substrate for graph-shaped retrieval.

## Graph analysis — how they relate

**Community clustering.** These 31 tools span **13 of the graph's 37 communities**.

- **Community 14** (9): `infiniflow/ragflow`, `run-llama/llama_index`, `deepset-ai/haystack`, `llmware-ai/llmware`, `Bessouat40/RAGLight`, `neuml/txtai`, `VectifyAI/PageIndex`, `StarTrail-org/LEANN`, `zilliztech/claude-context`
- **Community 1** (5): `qdrant/qdrant`, `weaviate/weaviate`, `pgvector/pgvector`, `milvus-io/milvus`, `lancedb/lancedb`
- **Community 6** (4): `facebookresearch/faiss`, `Unstructured-IO/unstructured`, `feyninc/chonkie`, `feyninc/chonkiejs`
- **Community 11** (2): `HKUDS/LightRAG`, `HKUDS/RAG-Anything`
- **Community 3** (2): `SylphAI-Inc/AdalFlow`, `chroma-core/chroma`
- **Community 30** (2): `FalkorDB/GraphRAG-SDK`, `FalkorDB/FalkorDB`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' RAG tools in your ecosystem:

- `VectifyAI/PageIndex` — PageRank 0.0011
- `qdrant/qdrant` — PageRank 0.0010
- `microsoft/graphrag` — PageRank 0.0010
- `deepset-ai/haystack` — PageRank 0.0009
- `chroma-core/chroma` — PageRank 0.0008
- `FalkorDB/GraphRAG-SDK` — PageRank 0.0007
- `neuml/txtai` — PageRank 0.0006
- `feyninc/chonkie` — PageRank 0.0006
- `FalkorDB/FalkorDB` — PageRank 0.0006
- `lancedb/lancedb` — PageRank 0.0006

**Direct links between RAG tools** (top similarity edges where both endpoints are in this report):

- `feyninc/chonkiejs` ⇄ `feyninc/chonkie` (w=1.733) — topics: ai, splitting-algorithms, chunker, rag; authors: chonk-lain
- `FalkorDB/GraphRAG-SDK` ⇄ `FalkorDB/FalkorDB` (w=0.867) — topics: graphrag, knowledge-graph, graph-database; authors: dependabot[bot]
- `HKUDS/RAG-Anything` ⇄ `HKUDS/LightRAG` (w=0.633) — topics: retrieval-augmented-generation
- `VectifyAI/PageIndex` ⇄ `deepset-ai/haystack` (w=0.441) — topics: agentic-ai, agents, ai, ai-agents
- `weaviate/weaviate` ⇄ `qdrant/qdrant` (w=0.429) — topics: search-engine, vector-search, vector-search-engine, vector-database
- `neuml/txtai` ⇄ `deepset-ai/haystack` (w=0.423) — topics: python, semantic-search, llm, large-language-models; authors: sainikhiljuluri
- `lancedb/lancedb` ⇄ `weaviate/weaviate` (w=0.400) — topics: approximate-nearest-neighbor-search, image-search, nearest-neighbor-search, recommender-system
- `neuml/txtai` ⇄ `VectifyAI/PageIndex` (w=0.383) — topics: llm, vector-database, information-retrieval, retrieval-augmented-generation
- `lancedb/lancedb` ⇄ `qdrant/qdrant` (w=0.380) — topics: image-search, nearest-neighbor-search, recommender-system, search-engine; authors: dependabot[bot]
- `neuml/txtai` ⇄ `StarTrail-org/LEANN` (w=0.291) — topics: python, vector-search, llm, vector-database
- `VectifyAI/PageIndex` ⇄ `infiniflow/ragflow` (w=0.286) — topics: agentic-ai, ai, ai-agents, context-engineering
- `lancedb/lancedb` ⇄ `alibaba/zvec` (w=0.277) — topics: search-engine, semantic-search, similarity-search, vector-database; authors: dependabot[bot]
- `SylphAI-Inc/AdalFlow` ⇄ `deepset-ai/haystack` (w=0.262) — topics: framework, llm, rag, generative-ai
- `lancedb/lancedb` ⇄ `pgvector/pgvector` (w=0.250) — topics: approximate-nearest-neighbor-search, nearest-neighbor-search
- `Bessouat40/RAGLight` ⇄ `deepset-ai/haystack` (w=0.232) — topics: framework, retrieval-augmented-generation, rag, agentic-rag
- …and 7 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| facebookresearch/faiss | 99 | Classic | very active | 5 | 26% | 28 |
| milvus-io/milvus | 99 | Classic | very active | 8 | 10% | 172 |
| infiniflow/ragflow | 98 | Mature | very active | 9 | 10% | 55 |
| run-llama/llama_index | 98 | Classic | very active | 13 | 11% | 496 |
| qdrant/qdrant | 93 | Classic | very active | 4 | 18% | 117 |
| alibaba/zvec | 93 | Hot | very active | 4 | 15% | 11 |
| lancedb/lancedb | 92 | Classic | very active | 4 | 19% | 499 |
| deepset-ai/haystack | 90 | Classic | very active | 3 | 44% | 243 |
| neuml/txtai | 85 | Classic | very active | 2 | 43% | 67 |
| chroma-core/chroma | 83 | Classic | very active | 2 | 41% | 137 |
| FalkorDB/FalkorDB | 80 | Classic | very active | 2 | 43% | 81 |
| Unstructured-IO/unstructured | 80 | Classic | very active | 3 | 23% | 239 |
| HKUDS/LightRAG | 79 | Hot | very active | 1 | 73% | 83 |
| superlinked/sie | 79 | Mature | very active | 2 | 29% | 48 |
| weaviate/weaviate | 78 | Classic | very active | 1 | 54% | 580 |
| FalkorDB/GraphRAG-SDK | 77 | Mature | very active | 1 | 61% | 31 |
| VectifyAI/PageIndex | 77 | Hot | very active | 1 | 65% | 15 |
| StarTrail-org/LEANN | 77 | Hot | very active | 4 | 24% | 29 |
| HKUDS/RAG-Anything | 75 | Hot | very active | 3 | 27% | 21 |
| huggingface/sentence-transformers | 75 | Classic | very active | 1 | 66% | 71 |
| feyninc/chonkie | 74 | Hot | very active | 1 | 85% | 45 |
| microsoft/graphrag | 71 | Mature | very active | 1 | 65% | 42 |
| feyninc/chonkiejs | 71 | Mature | very active | 1 | 100% | 7 |
| pgvector/pgvector | 65 | Classic | very active | 1 | 98% | 0 |
| PaddlePaddle/PaddleOCR | 65 | Mature | active | 2 | 40% | 33 |
| illuin-tech/colpali | 63 | Mature | active | 1 | 63% | 23 |
| Bessouat40/RAGLight | 61 | Mature | active | 1 | 100% | 45 |
| marqo-ai/marqo | 48 | Mature | active | 0 | 0% | 113 |
| zilliztech/claude-context | 39 | Declining | slowing | 1 | 50% | 0 |
| llmware-ai/llmware | 32 | Mature | slowing | 0 | 0% | 3 |
| SylphAI-Inc/AdalFlow | 29 | Mature | slowing | 0 | 0% | 7 |

## Which one should you use?

| If you want… | Start with | Why |
|---|---|---|
| A batteries-included RAG app over your docs | `infiniflow/ragflow` | Most-starred engine here (health 96); strong document parsing + chunking out of the box. |
| A composable toolkit to build custom RAG | `run-llama/llama_index` or `deepset-ai/haystack` | Mature libraries; connectors, indices, and pipeline primitives. |
| Graph-structured / multi-hop retrieval | `HKUDS/LightRAG` | Fast GraphRAG; builds an entity graph over chunks. |
| A production vector store at scale | `qdrant/qdrant` | High-performance Rust vector DB; health 88, widely deployed. |
| RAG with zero new infrastructure | `pgvector/pgvector` | Adds vector search to the Postgres you already run. |
| Best document parsing for ingestion | `Unstructured-IO/unstructured` (+ `PaddleOCR`) | Turns messy PDFs/HTML into clean, chunkable elements; OCR for scanned docs. |
| Good chunking without heavy deps | `feyninc/chonkie` | Lightweight, many strategies; JS port available. |
| To skip vector DBs entirely | `VectifyAI/PageIndex` | Vectorless, reasoning-based retrieval over a document tree. |
| Tiny-footprint / on-device RAG | `StarTrail-org/LEANN` | ~97% storage savings vs. a conventional vector index. |

## Adjacent (deliberately not listed as RAG tools)

- **langchain-ai/langchain** (146,288★) — general agent/LLM framework — RAG is one use case, too broad to list as RAG-specific
- **topoteretes/cognee** (30,674★) — covered in the *memory frameworks* report (graph memory, RAG-adjacent)
- **memvid/memvid** (16,539★) — covered in the *memory frameworks* report
- **NirDiamant/RAG_Techniques** (29,481★) — excellent *tutorial* collection, not a tool/library
- **KRLabsOrg/LettuceDetect** (606★) — RAG *evaluation* (hallucination detection) — see the LLM-evaluation report

## Build something with this stack

Ready-to-paste build prompts generated from this report's stack — the tools above, wired into a brief an LLM can act on.

- **Retrieval-evaluation harness** — A retrieval-evaluation harness that scores recall@k and MRR against a fixed question set, with a keyword-only baseline so every number has a floor.  
  <sub>`prompts/rag-eval-harness.md`</sub>

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (rag / retrieval-augmented / graphrag / vector db / embedding / rerank / chunk / semantic-search) + manual curation into pipeline stages. Tutorials, general agent frameworks, and memory-layer projects were routed to adjacent reports or excluded (see above).
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

### Retired from the scored set

Archived upstream, so they no longer appear in this report's tables — `sample.mjs` excludes archived repos. Metrics are frozen at the date shown and are not refreshed.

| Project | Category | Why it left | Metrics as of |
|---|---|---|---|
| [`airweave-ai/airweave`](https://github.com/airweave-ai/airweave) | RAG framework / engine | Archived upstream; last in the dataset 2026-08-28. Context-retrieval layer that syncs apps/DBs into agent-queryable knowledge. | 2026-08-28 |

<sub>Tools covered: 31 · Snapshot: 2026-09-14T11:08:08.535Z</sub>
