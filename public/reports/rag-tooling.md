# RAG (Retrieval-Augmented Generation) Tooling — Landscape Report

> Derived from **kaiser-data**'s 1,341 starred repos (snapshot `2026-07-19T22:39:07.967Z`), cross-referenced with the repo-similarity graph (1,341 nodes / 4,341 edges, 28 communities).
>
> Generated 2026-07-19 by `scripts/reports/rag_tooling.py` (regenerate any time — no API cost).

![Top tools by stars](assets/rag-tooling-top-tools.svg)

![Tools per category](assets/rag-tooling-categories.svg)


## Executive summary

- **32 RAG tools** in your stars (**708,346★** combined) — the largest AI category here — organized along the RAG pipeline:
  - **RAG framework / engine** (12): `ragflow`, `llama_index`, `LightRAG`, `graphrag`, `haystack`, `RAG-Anything`, `llmware`, `txtai`, `airweave`, `AdalFlow`, `GraphRAG-SDK`, `RAGLight`
  - **Vector DB / search** (10): `milvus`, `faiss`, `qdrant`, `chroma`, `pgvector`, `weaviate`, `zvec`, `lancedb`, `marqo`, `FalkorDB`
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
|---|---|---|---|---|---|---|---|---|---|---|
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Ingestion / parsing / chunking | Python | Apache-2.0 | 85,804 (▲459) | Classic | 80 | very active | 5d ago | 6.2y | 18 |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | RAG framework / engine | Go | Apache-2.0 | 85,399 (▲477) | Mature | 98 | very active | 0d ago | 2.6y | 27 |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | RAG framework / engine | Python | MIT | 50,943 (▲130) | Classic | 99 | very active | 4d ago | 3.7y | 48 |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | Vector DB / search | Go | Apache-2.0 | 45,274 (▲69) | Classic | 99 | very active | 0d ago | 6.8y | 29 |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | Vector DB / search | C++ | MIT | 40,541 (▲41) | Classic | 89 | very active | 2d ago | 9.4y | 23 |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | RAG framework / engine | Python | MIT | 37,842 (▲238) | Hot | 79 | very active | 0d ago | 1.8y | 4 |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | RAG framework / engine | Python | MIT | 34,511 (▲115) | Mature | 69 | active | 2d ago | 2.3y | 4 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Novel retrieval approach | Python | MIT | 34,110 (▲130) | Hot | 63 | very active | 1d ago | 1.3y | 7 |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | Vector DB / search | Rust | Apache-2.0 | 33,407 (▲176) | Classic | 93 | very active | 1d ago | 6.1y | 16 |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | Vector DB / search | Rust | Apache-2.0 | 28,828 (▲51) | Classic | 83 | very active | 2d ago | 3.8y | 8 |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | RAG framework / engine | MDX | Apache-2.0 | 25,945 (▲65) | Classic | 90 | very active | 2d ago | 6.7y | 17 |
| [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | RAG framework / engine | Python | MIT | 22,285 (▲117) | Hot | 70 | very active | 10d ago | 1.1y | 18 |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | Vector DB / search | C | NOASSERTION | 22,254 (▲86) | Classic | 61 | very active | 9d ago | 5.2y | 3 |
| [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers) | Embeddings / rerankers | Python | Apache-2.0 | 18,920 (▲16) | Classic | 78 | very active | 3d ago | 7.0y | 28 |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | Vector DB / search | Go | BSD-3-Clause | 16,617 (▲30) | Classic | 84 | very active | 0d ago | 10.3y | 11 |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | Ingestion / parsing / chunking | HTML | Apache-2.0 | 15,161 (▲36) | Classic | 69 | very active | 4d ago | 3.8y | 9 |
| [alibaba/zvec](https://github.com/alibaba/zvec) | Vector DB / search | C++ | Apache-2.0 | 15,144 (▲309) | Hot | 87 | very active | 1d ago | 7mo | 16 |
| [llmware-ai/llmware](https://github.com/llmware-ai/llmware) | RAG framework / engine | Python | Apache-2.0 | 14,827 (▲13) | Mature | 49 | slowing | 2mo ago | 2.8y | 1 |
| [neuml/txtai](https://github.com/neuml/txtai) | RAG framework / engine | Python | Apache-2.0 | 12,734 (▲14) | Classic | 78 | very active | 5d ago | 5.9y | 5 |
| [StarTrail-org/LEANN](https://github.com/StarTrail-org/LEANN) | Novel retrieval approach | Python | MIT | 12,712 (▲48) | Hot | 82 | very active | 1d ago | 1.1y | 17 |
| [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | Novel retrieval approach | TypeScript | MIT | 12,163 (▲37) | Hot | 60 | very active | 5d ago | 1.1y | 18 |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | Vector DB / search | HTML | Apache-2.0 | 10,932 (▲52) | Classic | 91 | very active | 1d ago | 3.4y | 28 |
| [airweave-ai/airweave](https://github.com/airweave-ai/airweave) | RAG framework / engine | Python | MIT | 6,488 (▲9) | Mature | 69 | active | 1mo ago | 1.6y | 5 |
| [marqo-ai/marqo](https://github.com/marqo-ai/marqo) | Vector DB / search | Python | Apache-2.0 | 5,017 (▲2) | Mature | 49 | active | 6d ago | 4.0y | 0 |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | Vector DB / search | C | NOASSERTION | 4,803 (▲46) | Classic | 82 | very active | 2d ago | 3.0y | 10 |
| [feyninc/chonkie](https://github.com/feyninc/chonkie) | Ingestion / parsing / chunking | Python | MIT | 4,520 (▲69) | Hot | 78 | very active | 2d ago | 1.3y | 4 |
| [SylphAI-Inc/AdalFlow](https://github.com/SylphAI-Inc/AdalFlow) | RAG framework / engine | Python | MIT | 4,184 (▲5) | Mature | 50 | active | 1mo ago | 2.3y | 2 |
| [illuin-tech/colpali](https://github.com/illuin-tech/colpali) | Embeddings / rerankers | Python | MIT | 2,702 (▲2) | Mature | 60 | active | 6d ago | 2.1y | 4 |
| [superlinked/sie](https://github.com/superlinked/sie) | Embeddings / rerankers | Python | Apache-2.0 | 2,274 (▲128) | Mature | 80 | very active | 1d ago | 2.7y | 5 |
| [FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK) | RAG framework / engine | Python | Apache-2.0 | 972 (▲3) | Mature | 77 | very active | 5d ago | 2.5y | 3 |
| [Bessouat40/RAGLight](https://github.com/Bessouat40/RAGLight) | RAG framework / engine | Python | MIT | 670 | Declining | 58 | active | 24d ago | 1.6y | 1 |
| [feyninc/chonkiejs](https://github.com/feyninc/chonkiejs) | Ingestion / parsing / chunking | TypeScript | MIT | 363 (▲1) | Mature | 71 | very active | 13d ago | 1.2y | 1 |

## By category

### RAG framework / engine

_End-to-end systems that orchestrate the whole pipeline. Engines (ragflow) are batteries-included apps; libraries (llama_index, haystack) are composable toolkits._

- **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** · 85,399★ · Go · Mature  
  Leading OSS RAG engine; deep document understanding + template-based chunking, batteries included.  
  <sub>topics: ai, ai-agents, context-engine, llm-apps, rag, retrieval-augmented-generation, agentic-ai, agentic-retrieval</sub>
- **[run-llama/llama_index](https://github.com/run-llama/llama_index)** · 50,943★ · Python · Classic  
  The 'document agent' framework — data connectors, indices, query engines; foundational RAG toolkit.  
  <sub>topics: agents, application, data, fine-tuning, framework, llamaindex, llm, rag</sub>
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 37,842★ · Python · Hot  
  Simple & fast RAG that builds a graph index over chunks (GraphRAG-style) for better multi-hop recall.  
  <sub>topics: knowledge-graph, large-language-models, retrieval-augmented-generation, genai, graphrag, llm, rag, gpt</sub>
- **[microsoft/graphrag](https://github.com/microsoft/graphrag)** · 34,511★ · Python · Mature  
  Microsoft's reference GraphRAG — LLM-built entity graph + community summaries over a corpus.  
  <sub>topics: graphrag, rag, llm, llms, gpt, gpt-4, gpt4</sub>
- **[deepset-ai/haystack](https://github.com/deepset-ai/haystack)** · 25,945★ · MDX · Classic  
  Pipeline-oriented orchestration for production RAG / context-engineered LLM apps.  
  <sub>topics: nlp, question-answering, pytorch, semantic-search, information-retrieval, summarization, transformers, machine-learning</sub>
- **[HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything)** · 22,285★ · Python · Hot  
  All-in-one multimodal RAG over text, tables, images, equations.  
  <sub>topics: multi-modal-rag, retrieval-augmented-generation</sub>
- **[llmware-ai/llmware](https://github.com/llmware-ai/llmware)** · 14,827★ · Python · Mature  
  Enterprise RAG with small, specialized models; private-deployment focus.  
  <sub>topics: parsing, retrieval-augmented-generation, agents, generative-ai-tools, llamacpp, llm, small-specialized-models, onnx</sub>
- **[neuml/txtai](https://github.com/neuml/txtai)** · 12,734★ · Python · Classic  
  All-in-one embeddings DB + RAG + workflows in one package.  
  <sub>topics: python, search, nlp, semantic-search, vector-search, txtai, llm, vector-database</sub>
- **[airweave-ai/airweave](https://github.com/airweave-ai/airweave)** · 6,488★ · Python · Mature  
  Context-retrieval layer that syncs apps/DBs into agent-queryable knowledge.  
  <sub>topics: llm, rag, search, agent-infrastructure, ai, ai-agents, ai-infrastructure, api</sub>
- **[SylphAI-Inc/AdalFlow](https://github.com/SylphAI-Inc/AdalFlow)** · 4,184★ · Python · Mature  
  Library to build & *auto-optimize* LLM/RAG apps (prompt + retriever tuning).  
  <sub>topics: agent, framework, llm, rag, generative-ai, machine-learning, nlp, python</sub>
- **[FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK)** · 972★ · Python · Mature  
  SDK to build GraphRAG apps on FalkorDB at scale.  
  <sub>topics: falkordb, graphrag, knowledge-graph, rag, graph-database, open-source, sdk, genai</sub>
- **[Bessouat40/RAGLight](https://github.com/Bessouat40/RAGLight)** · 670★ · Python · Declining  
  Lightweight modular RAG framework for quick pipelines.  
  <sub>topics: data-science, framework, huggingface, ollama, retrieval-augmented-generation, vector-database, artificial-intelligence, rag</sub>

### Vector DB / search

_Where embeddings live and approximate-nearest-neighbour search happens. Choice often comes down to scale, hybrid search, and ops footprint._

- **[milvus-io/milvus](https://github.com/milvus-io/milvus)** · 45,274★ · Go · Classic  
  Largest-scale OSS vector database — distributed, billion-vector ANN search.  
  <sub>topics: anns, nearest-neighbor-search, faiss, vector-search, image-search, hnsw, vector-database, embedding-database</sub>
- **[facebookresearch/faiss](https://github.com/facebookresearch/faiss)** · 40,541★ · C++ · Classic  
  Foundational dense-vector similarity-search library; the index under many DBs.  
  <sub>topics: —</sub>
- **[qdrant/qdrant](https://github.com/qdrant/qdrant)** · 33,407★ · Rust · Classic  
  High-performance, massive-scale vector DB & search engine (Rust).  
  <sub>topics: neural-network, search-engine, knn-algorithm, hnsw, vector-search, nearest-neighbor-search, image-search, embeddings-similarity</sub>
- **[chroma-core/chroma](https://github.com/chroma-core/chroma)** · 28,828★ · Rust · Classic  
  AI-native search/vector DB; popular default for prototyping RAG.  
  <sub>topics: database, rust, rust-lang, ai, agents, ai-agents</sub>
- **[pgvector/pgvector](https://github.com/pgvector/pgvector)** · 22,254★ · C · Classic  
  Vector similarity search as a Postgres extension — RAG without new infra.  
  <sub>topics: nearest-neighbor-search, approximate-nearest-neighbor-search</sub>
- **[weaviate/weaviate](https://github.com/weaviate/weaviate)** · 16,617★ · Go · Classic  
  Vector DB storing objects + vectors with hybrid (keyword+vector) search.  
  <sub>topics: search-engine, semantic-search, semantic-search-engine, vector-search, vector-search-engine, vector-database, approximate-nearest-neighbor-search, image-search</sub>
- **[alibaba/zvec](https://github.com/alibaba/zvec)** · 15,144★ · C++ · Hot  
  Lightweight, lightning-fast in-process vector database.  
  <sub>topics: rag, agent-skills, embedded, faiss, hnsw, llm-memory, search-engine, semantic-search</sub>
- **[lancedb/lancedb](https://github.com/lancedb/lancedb)** · 10,932★ · HTML · Classic  
  Embedded, serverless vector DB (columnar/Lance format); zero-ops local RAG.  
  <sub>topics: approximate-nearest-neighbor-search, image-search, nearest-neighbor-search, recommender-system, search-engine, semantic-search, similarity-search, vector-database</sub>
- **[marqo-ai/marqo](https://github.com/marqo-ai/marqo)** · 5,017★ · Python · Mature  
  End-to-end vector search that bundles embedding inference (text + image).  
  <sub>topics: multi-modal, search-engine, machine-learning, ecommerce</sub>
- **[FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB)** · 4,803★ · C · Classic  
  Fast graph database (GraphBLAS) — substrate for graph-shaped retrieval.  
  <sub>topics: graph-database, knowledge-graph, database-as-a-service, cloud-database, database, developer-tools, devtools, realtime-database</sub>

### Ingestion / parsing / chunking

_The unglamorous-but-decisive front of the pipeline: garbage chunks in → garbage retrieval out._

- **[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** · 85,804★ · Python · Classic  
  Powerful OCR — turns PDFs/images into structured text for the RAG ingest stage.  
  <sub>topics: ocr, chineseocr, pdf2markdown, pp-ocr, pp-structure, document-parsing, document-translation, kie</sub>
- **[Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)** · 15,161★ · HTML · Classic  
  ETL that turns PDFs/docs/HTML into clean, chunk-ready structured elements.  
  <sub>topics: deep-learning, document-parsing, machine-learning, nlp, ocr, information-retrieval, data-pipelines, ml</sub>
- **[feyninc/chonkie](https://github.com/feyninc/chonkie)** · 4,520★ · Python · Hot  
  Lightweight, fast chunking library (the 🦛) — many strategies, minimal deps.  
  <sub>topics: rag, chonkie, chunker, chunking-algorithm, retrieval-systems, semantic-chunker, similarity-search, text-splitter</sub>
- **[feyninc/chonkiejs](https://github.com/feyninc/chonkiejs)** · 363★ · TypeScript · Mature  
  TypeScript port of Chonkie for JS/TS RAG pipelines.  
  <sub>topics: typescript, ai, splitting-algorithms, chunker, rag, retrieval-systems, chunking-algorithm, text-splitter</sub>

### Embeddings / rerankers

_The models that turn text (or page images) into vectors and reorder candidate hits for precision._

- **[huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers)** · 18,920★ · Python · Classic  
  SoTA embeddings, retrieval & reranking models — the encoder layer of RAG.  
  <sub>topics: —</sub>
- **[illuin-tech/colpali](https://github.com/illuin-tech/colpali)** · 2,702★ · Python · Mature  
  Vision embeddings (ColPali/ColQwen) for document retrieval straight from page images.  
  <sub>topics: colpali, information-retrieval, retrieval-augmented-generation, vision-language-model, colqwen2, colsmol</sub>
- **[superlinked/sie](https://github.com/superlinked/sie)** · 2,274★ · Python · Mature  
  Inference engine/server for embeddings & rerankers in production retrieval.  
  <sub>topics: embeddings, vector-search, data-pipeline, deep-learning, information-retrieval, llm, ml, mlops</sub>

### Novel retrieval approach

_Projects challenging the embed-everything-into-a-vector-DB default — vectorless, storage-frugal, or domain-specialized retrieval._

- **[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** · 34,110★ · Python · Hot  
  Vectorless, reasoning-based RAG — builds a document index/tree, navigates with the LLM.  
  <sub>topics: agentic-ai, agents, ai, ai-agents, context-engineering, llm, rag, reasoning</sub>
- **[StarTrail-org/LEANN](https://github.com/StarTrail-org/LEANN)** · 12,712★ · Python · Hot  
  Storage-frugal RAG: ~97% storage savings while keeping fast, accurate retrieval.  
  <sub>topics: ai, faiss, langchain, llama-index, llm, localstorage, offline-first, ollama</sub>
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 12,163★ · TypeScript · Hot  
  Code-search MCP that makes an entire codebase the retrievable context for coding agents.  
  <sub>topics: agent, agentic-rag, ai-coding, code-search, cursor, embedding, mcp, nodejs</sub>

## Spotlight: GraphRAG

A cross-cutting trend — instead of a flat vector store, build a **knowledge graph** over chunks so retrieval can follow relationships (better for multi-hop questions). In your stars:

- **[microsoft/graphrag](https://github.com/microsoft/graphrag)** · 34,511★ — Microsoft's reference GraphRAG — LLM-built entity graph + community summaries over a corpus.
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 37,842★ — Simple & fast RAG that builds a graph index over chunks (GraphRAG-style) for better multi-hop recall.
- **[FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK)** · 972★ — SDK to build GraphRAG apps on FalkorDB at scale.
- **[FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB)** · 4,803★ — Fast graph database (GraphBLAS) — substrate for graph-shaped retrieval.

## Graph analysis — how they relate

**Community clustering.** These 32 tools span **11 of the graph's 28 communities**.

- **Community 20** (8): `infiniflow/ragflow`, `deepset-ai/haystack`, `SylphAI-Inc/AdalFlow`, `airweave-ai/airweave`, `Bessouat40/RAGLight`, `neuml/txtai`, `VectifyAI/PageIndex`, `StarTrail-org/LEANN`
- **Community 13** (6): `qdrant/qdrant`, `weaviate/weaviate`, `pgvector/pgvector`, `alibaba/zvec`, `milvus-io/milvus`, `lancedb/lancedb`
- **Community 9** (3): `llmware-ai/llmware`, `chroma-core/chroma`, `zilliztech/claude-context`
- **Community 18** (3): `facebookresearch/faiss`, `marqo-ai/marqo`, `PaddlePaddle/PaddleOCR`
- **Community 16** (3): `feyninc/chonkie`, `feyninc/chonkiejs`, `illuin-tech/colpali`
- **Community 5** (2): `HKUDS/LightRAG`, `HKUDS/RAG-Anything`
- **Community 10** (2): `FalkorDB/GraphRAG-SDK`, `FalkorDB/FalkorDB`
- **Community 12** (2): `Unstructured-IO/unstructured`, `superlinked/sie`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' RAG tools in your ecosystem:

- `VectifyAI/PageIndex` — PageRank 0.0022
- `HKUDS/LightRAG` — PageRank 0.0020
- `FalkorDB/GraphRAG-SDK` — PageRank 0.0017
- `neuml/txtai` — PageRank 0.0016
- `StarTrail-org/LEANN` — PageRank 0.0013
- `weaviate/weaviate` — PageRank 0.0012
- `chroma-core/chroma` — PageRank 0.0012
- `lancedb/lancedb` — PageRank 0.0011
- `superlinked/sie` — PageRank 0.0011
- `feyninc/chonkie` — PageRank 0.0010

**Direct links between RAG tools** (top similarity edges where both endpoints are in this report):

- `feyninc/chonkiejs` ⇄ `feyninc/chonkie` (w=1.833) — topics: ai, splitting-algorithms, chunker, rag; authors: chonk-lain
- `FalkorDB/GraphRAG-SDK` ⇄ `FalkorDB/FalkorDB` (w=0.867) — topics: graphrag, knowledge-graph, graph-database; authors: dependabot[bot]
- `FalkorDB/GraphRAG-SDK` ⇄ `HKUDS/LightRAG` (w=0.768) — topics: graphrag, knowledge-graph, rag, genai; authors: dependabot[bot]
- `HKUDS/RAG-Anything` ⇄ `HKUDS/LightRAG` (w=0.745) — topics: retrieval-augmented-generation; authors: danielaskdd
- `neuml/txtai` ⇄ `deepset-ai/haystack` (w=0.475) — topics: python, nlp, semantic-search, llm; authors: chuenchen309
- `weaviate/weaviate` ⇄ `qdrant/qdrant` (w=0.429) — topics: search-engine, vector-search, vector-search-engine, vector-database
- `VectifyAI/PageIndex` ⇄ `HKUDS/LightRAG` (w=0.417) — topics: llm, rag, retrieval-augmented-generation; authors: dependabot[bot]
- `lancedb/lancedb` ⇄ `weaviate/weaviate` (w=0.400) — topics: approximate-nearest-neighbor-search, image-search, nearest-neighbor-search, recommender-system
- `neuml/txtai` ⇄ `VectifyAI/PageIndex` (w=0.383) — topics: llm, vector-database, information-retrieval, retrieval-augmented-generation
- `SylphAI-Inc/AdalFlow` ⇄ `deepset-ai/haystack` (w=0.379) — topics: agent, llm, rag, generative-ai
- `VectifyAI/PageIndex` ⇄ `airweave-ai/airweave` (w=0.330) — topics: ai, ai-agents, llm, rag
- `lancedb/lancedb` ⇄ `qdrant/qdrant` (w=0.319) — topics: image-search, nearest-neighbor-search, recommender-system, search-engine; authors: dependabot[bot]
- `VectifyAI/PageIndex` ⇄ `deepset-ai/haystack` (w=0.318) — topics: agents, ai, llm, rag; authors: dependabot[bot]
- `neuml/txtai` ⇄ `airweave-ai/airweave` (w=0.300) — topics: search, semantic-search, llm, information-retrieval
- `VectifyAI/PageIndex` ⇄ `infiniflow/ragflow` (w=0.300) — topics: agentic-ai, ai, ai-agents, context-engineering
- …and 18 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| run-llama/llama_index | 99 | Classic | very active | 8 | 20% | 495 |
| milvus-io/milvus | 99 | Classic | very active | 8 | 9% | 167 |
| infiniflow/ragflow | 98 | Mature | very active | 6 | 12% | 52 |
| qdrant/qdrant | 93 | Classic | very active | 4 | 18% | 115 |
| lancedb/lancedb | 91 | Classic | very active | 4 | 20% | 464 |
| deepset-ai/haystack | 90 | Classic | very active | 3 | 22% | 235 |
| facebookresearch/faiss | 89 | Classic | very active | 3 | 20% | 27 |
| alibaba/zvec | 87 | Hot | very active | 3 | 31% | 9 |
| weaviate/weaviate | 84 | Classic | very active | 2 | 32% | 560 |
| chroma-core/chroma | 83 | Classic | very active | 2 | 30% | 137 |
| FalkorDB/FalkorDB | 82 | Classic | very active | 3 | 25% | 78 |
| StarTrail-org/LEANN | 82 | Hot | very active | 3 | 38% | 29 |
| PaddlePaddle/PaddleOCR | 80 | Classic | very active | 2 | 35% | 33 |
| superlinked/sie | 80 | Mature | very active | 2 | 45% | 34 |
| HKUDS/LightRAG | 79 | Hot | very active | 1 | 85% | 78 |
| neuml/txtai | 78 | Classic | very active | 1 | 94% | 65 |
| feyninc/chonkie | 78 | Hot | very active | 1 | 84% | 45 |
| huggingface/sentence-transformers | 78 | Classic | very active | 2 | 49% | 67 |
| FalkorDB/GraphRAG-SDK | 77 | Mature | very active | 1 | 82% | 30 |
| feyninc/chonkiejs | 71 | Mature | very active | 1 | 100% | 7 |
| HKUDS/RAG-Anything | 70 | Hot | very active | 1 | 53% | 19 |
| airweave-ai/airweave | 69 | Mature | active | 2 | 35% | 470 |
| microsoft/graphrag | 69 | Mature | active | 1 | 50% | 41 |
| Unstructured-IO/unstructured | 69 | Classic | very active | 1 | 52% | 234 |
| VectifyAI/PageIndex | 63 | Hot | very active | 2 | 40% | 2 |
| pgvector/pgvector | 61 | Classic | very active | 1 | 98% | 0 |
| illuin-tech/colpali | 60 | Mature | active | 1 | 50% | 22 |
| zilliztech/claude-context | 60 | Hot | very active | 2 | 38% | 0 |
| Bessouat40/RAGLight | 58 | Declining | active | 1 | 100% | 45 |
| SylphAI-Inc/AdalFlow | 50 | Mature | active | 1 | 60% | 7 |
| llmware-ai/llmware | 49 | Mature | slowing | 1 | 100% | 3 |
| marqo-ai/marqo | 49 | Mature | active | 0 | 0% | 113 |

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

- **langchain-ai/langchain** (142,098★) — general agent/LLM framework — RAG is one use case, too broad to list as RAG-specific
- **topoteretes/cognee** (28,491★) — covered in the *memory frameworks* report (graph memory, RAG-adjacent)
- **memvid/memvid** (16,005★) — covered in the *memory frameworks* report
- **NirDiamant/RAG_Techniques** (28,707★) — excellent *tutorial* collection, not a tool/library
- **KRLabsOrg/LettuceDetect** (585★) — RAG *evaluation* (hallucination detection) — see the LLM-evaluation report

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (rag / retrieval-augmented / graphrag / vector db / embedding / rerank / chunk / semantic-search) + manual curation into pipeline stages. Tutorials, general agent frameworks, and memory-layer projects were routed to adjacent reports or excluded (see above).
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 32 · Snapshot: 2026-07-19T22:39:07.967Z</sub>
