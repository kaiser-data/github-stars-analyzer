# RAG (Retrieval-Augmented Generation) Tooling — Landscape Report

> Derived from **kaiser-data**'s 1,859 starred repos (snapshot `2026-08-29T23:54:34.573Z`), cross-referenced with the repo-similarity graph (1,859 nodes / 6,070 edges, 37 communities).
>
> Generated 2026-08-30 by `scripts/reports/rag_tooling.py` (regenerate any time — no API cost).

![Top tools by stars](assets/rag-tooling-top-tools.svg)

![Tools per category](assets/rag-tooling-categories.svg)


## Executive summary

- **31 RAG tools** in your stars (**720,515★** combined) — the largest AI category here — organized along the RAG pipeline:
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
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | RAG framework / engine | Go | Apache-2.0 | 89,410 | Mature | 98 | very active | 2d ago | 2.7y | 37 |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Ingestion / parsing / chunking | Python | Apache-2.0 | 88,359 | Classic | 78 | active | 1mo ago | 6.3y | 11 |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | RAG framework / engine | Python | MIT | 51,894 | Classic | 97 | very active | 2d ago | 3.8y | 59 |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | Vector DB / search | Go | Apache-2.0 | 45,834 | Classic | 99 | very active | 2d ago | 7.0y | 33 |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | Vector DB / search | C++ | MIT | 40,812 | Classic | 94 | very active | 3d ago | 9.6y | 34 |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | RAG framework / engine | Python | MIT | 39,235 | Hot | 79 | very active | 2d ago | 1.9y | 11 |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | RAG framework / engine | Python | MIT | 35,707 | Mature | 71 | very active | 5d ago | 2.4y | 4 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Novel retrieval approach | Python | MIT | 35,344 | Hot | 73 | very active | 2d ago | 1.4y | 9 |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | Vector DB / search | Rust | Apache-2.0 | 34,228 | Classic | 87 | very active | 2d ago | 6.3y | 15 |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | Vector DB / search | Rust | Apache-2.0 | 29,166 | Classic | 83 | very active | 3d ago | 3.9y | 10 |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | RAG framework / engine | Python | Apache-2.0 | 26,343 | Classic | 85 | very active | 2d ago | 6.8y | 24 |
| [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | RAG framework / engine | Python | MIT | 23,087 | Hot | 70 | very active | 10d ago | 1.2y | 15 |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | Vector DB / search | C | NOASSERTION | 22,787 | Classic | 64 | very active | 10d ago | 5.4y | 3 |
| [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers) | Embeddings / rerankers | Python | Apache-2.0 | 19,040 | Classic | 75 | very active | 2d ago | 7.1y | 14 |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | Vector DB / search | Go | BSD-3-Clause | 16,757 | Classic | 78 | very active | 2d ago | 10.4y | 9 |
| [alibaba/zvec](https://github.com/alibaba/zvec) | Vector DB / search | C++ | Apache-2.0 | 15,528 | Hot | 93 | very active | 3d ago | 8mo | 19 |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | Ingestion / parsing / chunking | HTML | Apache-2.0 | 15,354 | Classic | 80 | very active | 2d ago | 3.9y | 10 |
| [llmware-ai/llmware](https://github.com/llmware-ai/llmware) | RAG framework / engine | Python | Apache-2.0 | 14,852 | Mature | 33 | slowing | 3mo ago | 2.9y | 0 |
| [neuml/txtai](https://github.com/neuml/txtai) | RAG framework / engine | Python | Apache-2.0 | 12,910 | Classic | 80 | very active | 2d ago | 6.1y | 17 |
| [StarTrail-org/LEANN](https://github.com/StarTrail-org/LEANN) | Novel retrieval approach | Python | MIT | 12,839 | Hot | 75 | very active | 4d ago | 1.2y | 15 |
| [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | Novel retrieval approach | TypeScript | MIT | 12,450 | Mature | 42 | active | 1mo ago | 1.2y | 3 |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | Vector DB / search | Rust | Apache-2.0 | 11,298 | Classic | 87 | very active | 2d ago | 3.5y | 16 |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | Vector DB / search | Rust | NOASSERTION | 5,666 | Classic | 85 | very active | 2d ago | 3.1y | 10 |
| [marqo-ai/marqo](https://github.com/marqo-ai/marqo) | Vector DB / search | Python | Apache-2.0 | 5,029 | Mature | 47 | active | 22d ago | 4.1y | 0 |
| [feyninc/chonkie](https://github.com/feyninc/chonkie) | Ingestion / parsing / chunking | Python | MIT | 4,706 | Hot | 76 | very active | 3d ago | 1.4y | 6 |
| [SylphAI-Inc/AdalFlow](https://github.com/SylphAI-Inc/AdalFlow) | RAG framework / engine | Python | MIT | 4,212 | Mature | 30 | slowing | 3mo ago | 2.4y | 0 |
| [superlinked/sie](https://github.com/superlinked/sie) | Embeddings / rerankers | Python | Apache-2.0 | 2,837 | Mature | 79 | very active | 2d ago | 2.8y | 8 |
| [illuin-tech/colpali](https://github.com/illuin-tech/colpali) | Embeddings / rerankers | Python | MIT | 2,800 | Mature | 64 | active | 5d ago | 2.2y | 5 |
| [FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK) | RAG framework / engine | Python | Apache-2.0 | 990 | Mature | 80 | very active | 2d ago | 2.6y | 8 |
| [Bessouat40/RAGLight](https://github.com/Bessouat40/RAGLight) | RAG framework / engine | Python | MIT | 671 | Declining | 55 | slowing | 2mo ago | 1.7y | 1 |
| [feyninc/chonkiejs](https://github.com/feyninc/chonkiejs) | Ingestion / parsing / chunking | TypeScript | MIT | 370 | Mature | 69 | very active | 21d ago | 1.3y | 1 |

## By category

### RAG framework / engine

_End-to-end systems that orchestrate the whole pipeline. Engines (ragflow) are batteries-included apps; libraries (llama_index, haystack) are composable toolkits._

- **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** · 89,410★ · Go · Mature  
  Leading OSS RAG engine; deep document understanding + template-based chunking, batteries included.  
  <sub>topics: ai, ai-agents, context-engine, llm-apps, rag, retrieval-augmented-generation, agentic-ai, agentic-retrieval</sub>
- **[run-llama/llama_index](https://github.com/run-llama/llama_index)** · 51,894★ · Python · Classic  
  The 'document agent' framework — data connectors, indices, query engines; foundational RAG toolkit.  
  <sub>topics: agents, application, data, fine-tuning, framework, llamaindex, llm, rag</sub>
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 39,235★ · Python · Hot  
  Simple & fast RAG that builds a graph index over chunks (GraphRAG-style) for better multi-hop recall.  
  <sub>topics: knowledge-graph, large-language-models, retrieval-augmented-generation, genai, graphrag, llm, rag, gpt</sub>
- **[microsoft/graphrag](https://github.com/microsoft/graphrag)** · 35,707★ · Python · Mature  
  Microsoft's reference GraphRAG — LLM-built entity graph + community summaries over a corpus.  
  <sub>topics: graphrag, rag, llm, llms, gpt, gpt-4, gpt4</sub>
- **[deepset-ai/haystack](https://github.com/deepset-ai/haystack)** · 26,343★ · Python · Classic  
  Pipeline-oriented orchestration for production RAG / context-engineered LLM apps.  
  <sub>topics: semantic-search, information-retrieval, ai, python, large-language-models, generative-ai, llm, rag</sub>
- **[HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything)** · 23,087★ · Python · Hot  
  All-in-one multimodal RAG over text, tables, images, equations.  
  <sub>topics: multi-modal-rag, retrieval-augmented-generation</sub>
- **[llmware-ai/llmware](https://github.com/llmware-ai/llmware)** · 14,852★ · Python · Mature  
  Enterprise RAG with small, specialized models; private-deployment focus.  
  <sub>topics: parsing, retrieval-augmented-generation, agents, generative-ai-tools, llamacpp, llm, small-specialized-models, onnx</sub>
- **[neuml/txtai](https://github.com/neuml/txtai)** · 12,910★ · Python · Classic  
  All-in-one embeddings DB + RAG + workflows in one package.  
  <sub>topics: python, search, nlp, semantic-search, vector-search, txtai, llm, vector-database</sub>
- **[SylphAI-Inc/AdalFlow](https://github.com/SylphAI-Inc/AdalFlow)** · 4,212★ · Python · Mature  
  Library to build & *auto-optimize* LLM/RAG apps (prompt + retriever tuning).  
  <sub>topics: agent, framework, llm, rag, generative-ai, machine-learning, nlp, python</sub>
- **[FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK)** · 990★ · Python · Mature  
  SDK to build GraphRAG apps on FalkorDB at scale.  
  <sub>topics: falkordb, graphrag, knowledge-graph, rag, graph-database, open-source, sdk, genai</sub>
- **[Bessouat40/RAGLight](https://github.com/Bessouat40/RAGLight)** · 671★ · Python · Declining  
  Lightweight modular RAG framework for quick pipelines.  
  <sub>topics: data-science, framework, huggingface, ollama, retrieval-augmented-generation, vector-database, artificial-intelligence, rag</sub>

### Vector DB / search

_Where embeddings live and approximate-nearest-neighbour search happens. Choice often comes down to scale, hybrid search, and ops footprint._

- **[milvus-io/milvus](https://github.com/milvus-io/milvus)** · 45,834★ · Go · Classic  
  Largest-scale OSS vector database — distributed, billion-vector ANN search.  
  <sub>topics: anns, nearest-neighbor-search, faiss, vector-search, image-search, hnsw, vector-database, embedding-database</sub>
- **[facebookresearch/faiss](https://github.com/facebookresearch/faiss)** · 40,812★ · C++ · Classic  
  Foundational dense-vector similarity-search library; the index under many DBs.  
  <sub>topics: —</sub>
- **[qdrant/qdrant](https://github.com/qdrant/qdrant)** · 34,228★ · Rust · Classic  
  High-performance, massive-scale vector DB & search engine (Rust).  
  <sub>topics: neural-network, search-engine, knn-algorithm, hnsw, vector-search, nearest-neighbor-search, image-search, embeddings-similarity</sub>
- **[chroma-core/chroma](https://github.com/chroma-core/chroma)** · 29,166★ · Rust · Classic  
  AI-native search/vector DB; popular default for prototyping RAG.  
  <sub>topics: database, rust, rust-lang, ai, agents, ai-agents</sub>
- **[pgvector/pgvector](https://github.com/pgvector/pgvector)** · 22,787★ · C · Classic  
  Vector similarity search as a Postgres extension — RAG without new infra.  
  <sub>topics: nearest-neighbor-search, approximate-nearest-neighbor-search</sub>
- **[weaviate/weaviate](https://github.com/weaviate/weaviate)** · 16,757★ · Go · Classic  
  Vector DB storing objects + vectors with hybrid (keyword+vector) search.  
  <sub>topics: search-engine, semantic-search, semantic-search-engine, vector-search, vector-search-engine, vector-database, approximate-nearest-neighbor-search, image-search</sub>
- **[alibaba/zvec](https://github.com/alibaba/zvec)** · 15,528★ · C++ · Hot  
  Lightweight, lightning-fast in-process vector database.  
  <sub>topics: rag, agent-skills, embedded, faiss, hnsw, llm-memory, search-engine, semantic-search</sub>
- **[lancedb/lancedb](https://github.com/lancedb/lancedb)** · 11,298★ · Rust · Classic  
  Embedded, serverless vector DB (columnar/Lance format); zero-ops local RAG.  
  <sub>topics: approximate-nearest-neighbor-search, image-search, nearest-neighbor-search, recommender-system, search-engine, semantic-search, similarity-search, vector-database</sub>
- **[FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB)** · 5,666★ · Rust · Classic  
  Fast graph database (GraphBLAS) — substrate for graph-shaped retrieval.  
  <sub>topics: graph-database, knowledge-graph, database-as-a-service, cloud-database, database, developer-tools, devtools, realtime-database</sub>
- **[marqo-ai/marqo](https://github.com/marqo-ai/marqo)** · 5,029★ · Python · Mature  
  End-to-end vector search that bundles embedding inference (text + image).  
  <sub>topics: multi-modal, search-engine, machine-learning, ecommerce</sub>

### Ingestion / parsing / chunking

_The unglamorous-but-decisive front of the pipeline: garbage chunks in → garbage retrieval out._

- **[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** · 88,359★ · Python · Classic  
  Powerful OCR — turns PDFs/images into structured text for the RAG ingest stage.  
  <sub>topics: ocr, chineseocr, pdf2markdown, pp-ocr, pp-structure, document-parsing, document-translation, kie</sub>
- **[Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)** · 15,354★ · HTML · Classic  
  ETL that turns PDFs/docs/HTML into clean, chunk-ready structured elements.  
  <sub>topics: deep-learning, document-parsing, machine-learning, nlp, ocr, information-retrieval, data-pipelines, ml</sub>
- **[feyninc/chonkie](https://github.com/feyninc/chonkie)** · 4,706★ · Python · Hot  
  Lightweight, fast chunking library (the 🦛) — many strategies, minimal deps.  
  <sub>topics: rag, chonkie, chunker, chunking-algorithm, retrieval-systems, semantic-chunker, similarity-search, text-splitter</sub>
- **[feyninc/chonkiejs](https://github.com/feyninc/chonkiejs)** · 370★ · TypeScript · Mature  
  TypeScript port of Chonkie for JS/TS RAG pipelines.  
  <sub>topics: typescript, ai, splitting-algorithms, chunker, rag, retrieval-systems, chunking-algorithm, text-splitter</sub>

### Embeddings / rerankers

_The models that turn text (or page images) into vectors and reorder candidate hits for precision._

- **[huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers)** · 19,040★ · Python · Classic  
  SoTA embeddings, retrieval & reranking models — the encoder layer of RAG.  
  <sub>topics: —</sub>
- **[superlinked/sie](https://github.com/superlinked/sie)** · 2,837★ · Python · Mature  
  Inference engine/server for embeddings & rerankers in production retrieval.  
  <sub>topics: embeddings, vector-search, data-pipeline, deep-learning, information-retrieval, llm, ml, mlops</sub>
- **[illuin-tech/colpali](https://github.com/illuin-tech/colpali)** · 2,800★ · Python · Mature  
  Vision embeddings (ColPali/ColQwen) for document retrieval straight from page images.  
  <sub>topics: colpali, information-retrieval, retrieval-augmented-generation, vision-language-model, colqwen2, colsmol</sub>

### Novel retrieval approach

_Projects challenging the embed-everything-into-a-vector-DB default — vectorless, storage-frugal, or domain-specialized retrieval._

- **[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** · 35,344★ · Python · Hot  
  Vectorless, reasoning-based RAG — builds a document index/tree, navigates with the LLM.  
  <sub>topics: agentic-ai, agents, ai, ai-agents, context-engineering, llm, rag, reasoning</sub>
- **[StarTrail-org/LEANN](https://github.com/StarTrail-org/LEANN)** · 12,839★ · Python · Hot  
  Storage-frugal RAG: ~97% storage savings while keeping fast, accurate retrieval.  
  <sub>topics: ai, faiss, langchain, llama-index, llm, localstorage, offline-first, ollama</sub>
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,450★ · TypeScript · Mature  
  Code-search MCP that makes an entire codebase the retrievable context for coding agents.  
  <sub>topics: agent, agentic-rag, ai-coding, code-search, cursor, embedding, mcp, nodejs</sub>

## Spotlight: GraphRAG

A cross-cutting trend — instead of a flat vector store, build a **knowledge graph** over chunks so retrieval can follow relationships (better for multi-hop questions). In your stars:

- **[microsoft/graphrag](https://github.com/microsoft/graphrag)** · 35,707★ — Microsoft's reference GraphRAG — LLM-built entity graph + community summaries over a corpus.
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 39,235★ — Simple & fast RAG that builds a graph index over chunks (GraphRAG-style) for better multi-hop recall.
- **[FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK)** · 990★ — SDK to build GraphRAG apps on FalkorDB at scale.
- **[FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB)** · 5,666★ — Fast graph database (GraphBLAS) — substrate for graph-shaped retrieval.

## Graph analysis — how they relate

**Community clustering.** These 31 tools span **12 of the graph's 37 communities**.

- **Community 8** (14): `infiniflow/ragflow`, `deepset-ai/haystack`, `llmware-ai/llmware`, `SylphAI-Inc/AdalFlow`, `Bessouat40/RAGLight`, `qdrant/qdrant`, `weaviate/weaviate`, `pgvector/pgvector`, `alibaba/zvec`, `milvus-io/milvus`, `lancedb/lancedb`, `neuml/txtai`, `VectifyAI/PageIndex`, `StarTrail-org/LEANN`
- **Community 15** (4): `HKUDS/LightRAG`, `HKUDS/RAG-Anything`, `FalkorDB/GraphRAG-SDK`, `FalkorDB/FalkorDB`
- **Community 16** (3): `facebookresearch/faiss`, `feyninc/chonkie`, `feyninc/chonkiejs`
- **Community 0** (2): `Unstructured-IO/unstructured`, `superlinked/sie`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' RAG tools in your ecosystem:

- `VectifyAI/PageIndex` — PageRank 0.0016
- `deepset-ai/haystack` — PageRank 0.0013
- `microsoft/graphrag` — PageRank 0.0011
- `chroma-core/chroma` — PageRank 0.0010
- `HKUDS/LightRAG` — PageRank 0.0010
- `FalkorDB/GraphRAG-SDK` — PageRank 0.0009
- `neuml/txtai` — PageRank 0.0009
- `StarTrail-org/LEANN` — PageRank 0.0008
- `weaviate/weaviate` — PageRank 0.0008
- `FalkorDB/FalkorDB` — PageRank 0.0007

**Direct links between RAG tools** (top similarity edges where both endpoints are in this report):

- `feyninc/chonkiejs` ⇄ `feyninc/chonkie` (w=1.667) — topics: ai, splitting-algorithms, chunker, rag; authors: chonk-lain
- `FalkorDB/GraphRAG-SDK` ⇄ `FalkorDB/FalkorDB` (w=1.100) — topics: graphrag, knowledge-graph, graph-database; authors: gkorland, dudizimber, dependabot[bot]
- `HKUDS/RAG-Anything` ⇄ `HKUDS/LightRAG` (w=0.713) — topics: retrieval-augmented-generation; authors: danielaskdd
- `VectifyAI/PageIndex` ⇄ `deepset-ai/haystack` (w=0.504) — topics: agentic-ai, agents, ai, ai-agents; authors: dependabot[bot]
- `FalkorDB/GraphRAG-SDK` ⇄ `HKUDS/LightRAG` (w=0.494) — topics: graphrag, knowledge-graph, rag, genai; authors: dependabot[bot]
- `neuml/txtai` ⇄ `deepset-ai/haystack` (w=0.486) — topics: python, semantic-search, llm, large-language-models; authors: sainikhiljuluri, LHMQ878
- `weaviate/weaviate` ⇄ `qdrant/qdrant` (w=0.429) — topics: search-engine, vector-search, vector-search-engine, vector-database
- `lancedb/lancedb` ⇄ `weaviate/weaviate` (w=0.400) — topics: approximate-nearest-neighbor-search, image-search, nearest-neighbor-search, recommender-system
- `lancedb/lancedb` ⇄ `qdrant/qdrant` (w=0.389) — topics: image-search, nearest-neighbor-search, recommender-system, search-engine; authors: dependabot[bot]
- `neuml/txtai` ⇄ `VectifyAI/PageIndex` (w=0.383) — topics: llm, vector-database, information-retrieval, retrieval-augmented-generation
- `VectifyAI/PageIndex` ⇄ `infiniflow/ragflow` (w=0.300) — topics: agentic-ai, ai, ai-agents, context-engineering
- `lancedb/lancedb` ⇄ `alibaba/zvec` (w=0.294) — topics: search-engine, semantic-search, similarity-search, vector-database; authors: dependabot[bot]
- `neuml/txtai` ⇄ `StarTrail-org/LEANN` (w=0.291) — topics: python, vector-search, llm, vector-database
- `SylphAI-Inc/AdalFlow` ⇄ `deepset-ai/haystack` (w=0.262) — topics: framework, llm, rag, generative-ai
- `lancedb/lancedb` ⇄ `pgvector/pgvector` (w=0.250) — topics: approximate-nearest-neighbor-search, nearest-neighbor-search
- …and 10 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| milvus-io/milvus | 99 | Classic | very active | 8 | 12% | 170 |
| infiniflow/ragflow | 98 | Mature | very active | 7 | 9% | 53 |
| run-llama/llama_index | 97 | Classic | very active | 16 | 6% | 496 |
| facebookresearch/faiss | 94 | Classic | very active | 4 | 27% | 28 |
| alibaba/zvec | 93 | Hot | very active | 4 | 23% | 11 |
| qdrant/qdrant | 87 | Classic | very active | 3 | 34% | 116 |
| lancedb/lancedb | 87 | Classic | very active | 3 | 22% | 487 |
| deepset-ai/haystack | 85 | Classic | very active | 2 | 31% | 241 |
| FalkorDB/FalkorDB | 85 | Classic | very active | 3 | 30% | 81 |
| chroma-core/chroma | 83 | Classic | very active | 2 | 48% | 137 |
| FalkorDB/GraphRAG-SDK | 80 | Mature | very active | 2 | 43% | 31 |
| neuml/txtai | 80 | Classic | very active | 1 | 51% | 67 |
| Unstructured-IO/unstructured | 80 | Classic | very active | 3 | 33% | 238 |
| HKUDS/LightRAG | 79 | Hot | very active | 1 | 71% | 82 |
| superlinked/sie | 79 | Mature | very active | 2 | 38% | 47 |
| weaviate/weaviate | 78 | Classic | very active | 1 | 52% | 576 |
| PaddlePaddle/PaddleOCR | 78 | Classic | active | 3 | 22% | 33 |
| feyninc/chonkie | 76 | Hot | very active | 1 | 84% | 45 |
| huggingface/sentence-transformers | 75 | Classic | very active | 1 | 81% | 70 |
| StarTrail-org/LEANN | 75 | Hot | very active | 3 | 28% | 29 |
| VectifyAI/PageIndex | 73 | Hot | very active | 1 | 68% | 9 |
| microsoft/graphrag | 71 | Mature | very active | 1 | 65% | 42 |
| HKUDS/RAG-Anything | 70 | Hot | very active | 3 | 29% | 19 |
| feyninc/chonkiejs | 69 | Mature | very active | 1 | 100% | 7 |
| pgvector/pgvector | 64 | Classic | very active | 1 | 98% | 0 |
| illuin-tech/colpali | 64 | Mature | active | 1 | 50% | 23 |
| Bessouat40/RAGLight | 55 | Declining | slowing | 1 | 100% | 45 |
| marqo-ai/marqo | 47 | Mature | active | 0 | 0% | 113 |
| zilliztech/claude-context | 42 | Mature | active | 1 | 57% | 0 |
| llmware-ai/llmware | 33 | Mature | slowing | 0 | 0% | 3 |
| SylphAI-Inc/AdalFlow | 30 | Mature | slowing | 0 | 0% | 7 |

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

- **langchain-ai/langchain** (145,151★) — general agent/LLM framework — RAG is one use case, too broad to list as RAG-specific
- **topoteretes/cognee** (30,299★) — covered in the *memory frameworks* report (graph memory, RAG-adjacent)
- **memvid/memvid** (16,456★) — covered in the *memory frameworks* report
- **NirDiamant/RAG_Techniques** (29,253★) — excellent *tutorial* collection, not a tool/library
- **KRLabsOrg/LettuceDetect** (601★) — RAG *evaluation* (hallucination detection) — see the LLM-evaluation report

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

<sub>Tools covered: 31 · Snapshot: 2026-08-29T23:54:34.573Z</sub>
