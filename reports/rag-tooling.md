# RAG (Retrieval-Augmented Generation) Tooling — Landscape Report

> Derived from **kaiser-data**'s 1,243 starred repos (snapshot `2026-06-11T21:58:33.384Z`), cross-referenced with the repo-similarity graph (1,243 nodes / 4,017 edges, 31 communities).
>
> Generated 2026-06-11 by `scripts/reports/rag_tooling.py` (regenerate any time — no API cost).

## Executive summary

- **31 RAG tools** in your stars (**671,976★** combined) — the largest AI category here — organized along the RAG pipeline:
  - **RAG framework / engine** (12): `ragflow`, `llama_index`, `LightRAG`, `graphrag`, `haystack`, `RAG-Anything`, `llmware`, `txtai`, `airweave`, `AdalFlow`, `GraphRAG-SDK`, `RAGLight`
  - **Vector DB / search** (10): `milvus`, `faiss`, `qdrant`, `chroma`, `pgvector`, `weaviate`, `lancedb`, `zvec`, `marqo`, `FalkorDB`
  - **Ingestion / parsing / chunking** (4): `PaddleOCR`, `unstructured`, `chonkie`, `chonkiejs`
  - **Embeddings / rerankers** (3): `sentence-transformers`, `colpali`, `sie`
  - **Novel retrieval approach** (2): `PageIndex`, `claude-context`
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
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | RAG framework / engine | Python | Apache-2.0 | 82,476 | Mature | 96 | very active | 0d ago | 2.5y | 33 |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Ingestion / parsing / chunking | Python | Apache-2.0 | 81,861 | Classic | 81 | very active | 0d ago | 6.1y | 22 |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | RAG framework / engine | Python | MIT | 50,083 | Classic | 100 | very active | 0d ago | 3.6y | 49 |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | Vector DB / search | Go | Apache-2.0 | 44,729 | Classic | 100 | very active | 0d ago | 6.7y | 30 |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | Vector DB / search | C++ | MIT | 40,266 | Classic | 88 | very active | 0d ago | 9.3y | 33 |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | RAG framework / engine | Python | MIT | 36,460 | Mature | 79 | very active | 0d ago | 1.7y | 2 |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | RAG framework / engine | Python | MIT | 33,661 | Mature | 68 | active | 6d ago | 2.2y | 4 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Novel retrieval approach | Python | MIT | 32,927 | Hot | 50 | very active | 6d ago | 1.2y | 5 |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | Vector DB / search | Rust | Apache-2.0 | 32,039 | Classic | 93 | very active | 0d ago | 6.0y | 16 |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | Vector DB / search | Rust | Apache-2.0 | 28,387 | Classic | 83 | very active | 1d ago | 3.7y | 8 |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | RAG framework / engine | MDX | Apache-2.0 | 25,538 | Classic | 90 | very active | 0d ago | 6.6y | 22 |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | Vector DB / search | C | NOASSERTION | 21,711 | Classic | 56 | very active | 1d ago | 5.1y | 3 |
| [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | RAG framework / engine | Python | MIT | 21,204 | Hot | 72 | very active | 1d ago | 1.0y | 19 |
| [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers) | Embeddings / rerankers | Python | Apache-2.0 | 18,800 | Classic | 75 | very active | 0d ago | 6.9y | 18 |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | Vector DB / search | Go | BSD-3-Clause | 16,313 | Classic | 84 | very active | 0d ago | 10.2y | 11 |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | Ingestion / parsing / chunking | HTML | Apache-2.0 | 14,889 | Classic | 82 | very active | 0d ago | 3.7y | 11 |
| [llmware-ai/llmware](https://github.com/llmware-ai/llmware) | RAG framework / engine | Python | Apache-2.0 | 14,845 | Mature | 58 | very active | 25d ago | 2.7y | 1 |
| [neuml/txtai](https://github.com/neuml/txtai) | RAG framework / engine | Python | Apache-2.0 | 12,650 | Mature | 78 | very active | 0d ago | 5.8y | 1 |
| [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | Novel retrieval approach | TypeScript | MIT | 11,818 | Hot | 60 | very active | 4d ago | 1.0y | 18 |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | Vector DB / search | HTML | Apache-2.0 | 10,579 | Classic | 96 | very active | 0d ago | 3.3y | 29 |
| [alibaba/zvec](https://github.com/alibaba/zvec) | Vector DB / search | C++ | Apache-2.0 | 9,776 | Hot | 87 | very active | 1d ago | 6mo | 15 |
| [airweave-ai/airweave](https://github.com/airweave-ai/airweave) | RAG framework / engine | Python | MIT | 6,436 | Hot | 75 | very active | 7d ago | 1.5y | 6 |
| [marqo-ai/marqo](https://github.com/marqo-ai/marqo) | Vector DB / search | Python | Apache-2.0 | 5,020 | Classic | 68 | very active | 3d ago | 3.9y | 3 |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | Vector DB / search | C | NOASSERTION | 4,547 | Mature | 84 | very active | 1d ago | 2.9y | 10 |
| [SylphAI-Inc/AdalFlow](https://github.com/SylphAI-Inc/AdalFlow) | RAG framework / engine | Python | MIT | 4,168 | Mature | 56 | active | 14d ago | 2.1y | 2 |
| [chonkie-inc/chonkie](https://github.com/chonkie-inc/chonkie) | Ingestion / parsing / chunking | Python | MIT | 4,139 | Hot | 78 | very active | 0d ago | 1.2y | 5 |
| [illuin-tech/colpali](https://github.com/illuin-tech/colpali) | Embeddings / rerankers | Python | MIT | 2,666 | Mature | 66 | active | 1d ago | 2.0y | 6 |
| [superlinked/sie](https://github.com/superlinked/sie) | Embeddings / rerankers | Python | Apache-2.0 | 2,042 | Mature | 72 | very active | 1d ago | 2.6y | 4 |
| [FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK) | RAG framework / engine | Python | Apache-2.0 | 935 | Mature | 77 | very active | 7d ago | 2.4y | 3 |
| [Bessouat40/RAGLight](https://github.com/Bessouat40/RAGLight) | RAG framework / engine | Python | MIT | 665 | Mature | 64 | slowing | 2mo ago | 1.5y | 1 |
| [chonkie-inc/chonkiejs](https://github.com/chonkie-inc/chonkiejs) | Ingestion / parsing / chunking | TypeScript | MIT | 346 | Hot | 64 | very active | 10d ago | 1.1y | 3 |

## By category

### RAG framework / engine

_End-to-end systems that orchestrate the whole pipeline. Engines (ragflow) are batteries-included apps; libraries (llama_index, haystack) are composable toolkits._

- **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** · 82,476★ · Python · Mature  
  Leading OSS RAG engine; deep document understanding + template-based chunking, batteries included.  
  <sub>topics: ai, ai-agents, context-engine, llm-apps, rag, retrieval-augmented-generation, agentic-ai, agentic-retrieval</sub>
- **[run-llama/llama_index](https://github.com/run-llama/llama_index)** · 50,083★ · Python · Classic  
  The 'document agent' framework — data connectors, indices, query engines; foundational RAG toolkit.  
  <sub>topics: agents, application, data, fine-tuning, framework, llamaindex, llm, rag</sub>
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 36,460★ · Python · Mature  
  Simple & fast RAG that builds a graph index over chunks (GraphRAG-style) for better multi-hop recall.  
  <sub>topics: knowledge-graph, large-language-models, retrieval-augmented-generation, genai, graphrag, llm, rag, gpt</sub>
- **[microsoft/graphrag](https://github.com/microsoft/graphrag)** · 33,661★ · Python · Mature  
  Microsoft's reference GraphRAG — LLM-built entity graph + community summaries over a corpus.  
  <sub>topics: graphrag, rag, llm, llms, gpt, gpt-4, gpt4</sub>
- **[deepset-ai/haystack](https://github.com/deepset-ai/haystack)** · 25,538★ · MDX · Classic  
  Pipeline-oriented orchestration for production RAG / context-engineered LLM apps.  
  <sub>topics: nlp, question-answering, pytorch, semantic-search, information-retrieval, summarization, transformers, machine-learning</sub>
- **[HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything)** · 21,204★ · Python · Hot  
  All-in-one multimodal RAG over text, tables, images, equations.  
  <sub>topics: multi-modal-rag, retrieval-augmented-generation</sub>
- **[llmware-ai/llmware](https://github.com/llmware-ai/llmware)** · 14,845★ · Python · Mature  
  Enterprise RAG with small, specialized models; private-deployment focus.  
  <sub>topics: parsing, retrieval-augmented-generation, agents, generative-ai-tools, llamacpp, llm, small-specialized-models, onnx</sub>
- **[neuml/txtai](https://github.com/neuml/txtai)** · 12,650★ · Python · Mature  
  All-in-one embeddings DB + RAG + workflows in one package.  
  <sub>topics: python, search, nlp, semantic-search, vector-search, txtai, llm, vector-database</sub>
- **[airweave-ai/airweave](https://github.com/airweave-ai/airweave)** · 6,436★ · Python · Hot  
  Context-retrieval layer that syncs apps/DBs into agent-queryable knowledge.  
  <sub>topics: llm, rag, search, agent-infrastructure, ai, ai-agents, ai-infrastructure, api</sub>
- **[SylphAI-Inc/AdalFlow](https://github.com/SylphAI-Inc/AdalFlow)** · 4,168★ · Python · Mature  
  Library to build & *auto-optimize* LLM/RAG apps (prompt + retriever tuning).  
  <sub>topics: agent, framework, llm, rag, generative-ai, machine-learning, nlp, python</sub>
- **[FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK)** · 935★ · Python · Mature  
  SDK to build GraphRAG apps on FalkorDB at scale.  
  <sub>topics: falkordb, graphrag, knowledge-graph, rag, graph-database, open-source, sdk, genai</sub>
- **[Bessouat40/RAGLight](https://github.com/Bessouat40/RAGLight)** · 665★ · Python · Mature  
  Lightweight modular RAG framework for quick pipelines.  
  <sub>topics: data-science, framework, huggingface, ollama, retrieval-augmented-generation, vector-database, artificial-intelligence, rag</sub>

### Vector DB / search

_Where embeddings live and approximate-nearest-neighbour search happens. Choice often comes down to scale, hybrid search, and ops footprint._

- **[milvus-io/milvus](https://github.com/milvus-io/milvus)** · 44,729★ · Go · Classic  
  Largest-scale OSS vector database — distributed, billion-vector ANN search.  
  <sub>topics: anns, nearest-neighbor-search, faiss, vector-search, image-search, hnsw, vector-database, embedding-database</sub>
- **[facebookresearch/faiss](https://github.com/facebookresearch/faiss)** · 40,266★ · C++ · Classic  
  Foundational dense-vector similarity-search library; the index under many DBs.  
  <sub>topics: —</sub>
- **[qdrant/qdrant](https://github.com/qdrant/qdrant)** · 32,039★ · Rust · Classic  
  High-performance, massive-scale vector DB & search engine (Rust).  
  <sub>topics: neural-network, search-engine, knn-algorithm, hnsw, vector-search, nearest-neighbor-search, image-search, embeddings-similarity</sub>
- **[chroma-core/chroma](https://github.com/chroma-core/chroma)** · 28,387★ · Rust · Classic  
  AI-native search/vector DB; popular default for prototyping RAG.  
  <sub>topics: database, rust, rust-lang, ai, agents, ai-agents</sub>
- **[pgvector/pgvector](https://github.com/pgvector/pgvector)** · 21,711★ · C · Classic  
  Vector similarity search as a Postgres extension — RAG without new infra.  
  <sub>topics: nearest-neighbor-search, approximate-nearest-neighbor-search</sub>
- **[weaviate/weaviate](https://github.com/weaviate/weaviate)** · 16,313★ · Go · Classic  
  Vector DB storing objects + vectors with hybrid (keyword+vector) search.  
  <sub>topics: search-engine, semantic-search, semantic-search-engine, vector-search, vector-search-engine, vector-database, approximate-nearest-neighbor-search, image-search</sub>
- **[lancedb/lancedb](https://github.com/lancedb/lancedb)** · 10,579★ · HTML · Classic  
  Embedded, serverless vector DB (columnar/Lance format); zero-ops local RAG.  
  <sub>topics: approximate-nearest-neighbor-search, image-search, nearest-neighbor-search, recommender-system, search-engine, semantic-search, similarity-search, vector-database</sub>
- **[alibaba/zvec](https://github.com/alibaba/zvec)** · 9,776★ · C++ · Hot  
  Lightweight, lightning-fast in-process vector database.  
  <sub>topics: rag, agent-skills, embedded, faiss, hnsw, llm-memory, search-engine, semantic-search</sub>
- **[marqo-ai/marqo](https://github.com/marqo-ai/marqo)** · 5,020★ · Python · Classic  
  End-to-end vector search that bundles embedding inference (text + image).  
  <sub>topics: multi-modal, search-engine, machine-learning, ecommerce</sub>
- **[FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB)** · 4,547★ · C · Mature  
  Fast graph database (GraphBLAS) — substrate for graph-shaped retrieval.  
  <sub>topics: graph-database, knowledge-graph, database-as-a-service, cloud-database, database, developer-tools, devtools, realtime-database</sub>

### Ingestion / parsing / chunking

_The unglamorous-but-decisive front of the pipeline: garbage chunks in → garbage retrieval out._

- **[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** · 81,861★ · Python · Classic  
  Powerful OCR — turns PDFs/images into structured text for the RAG ingest stage.  
  <sub>topics: ocr, chineseocr, pdf2markdown, pp-ocr, pp-structure, document-parsing, document-translation, kie</sub>
- **[Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)** · 14,889★ · HTML · Classic  
  ETL that turns PDFs/docs/HTML into clean, chunk-ready structured elements.  
  <sub>topics: deep-learning, document-parsing, machine-learning, nlp, ocr, information-retrieval, data-pipelines, ml</sub>
- **[chonkie-inc/chonkie](https://github.com/chonkie-inc/chonkie)** · 4,139★ · Python · Hot  
  Lightweight, fast chunking library (the 🦛) — many strategies, minimal deps.  
  <sub>topics: rag, chonkie, chunker, chunking-algorithm, retrieval-systems, semantic-chunker, similarity-search, text-splitter</sub>
- **[chonkie-inc/chonkiejs](https://github.com/chonkie-inc/chonkiejs)** · 346★ · TypeScript · Hot  
  TypeScript port of Chonkie for JS/TS RAG pipelines.  
  <sub>topics: typescript, ai, splitting-algorithms, chunker, rag, retrieval-systems, chunking-algorithm, text-splitter</sub>

### Embeddings / rerankers

_The models that turn text (or page images) into vectors and reorder candidate hits for precision._

- **[huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers)** · 18,800★ · Python · Classic  
  SoTA embeddings, retrieval & reranking models — the encoder layer of RAG.  
  <sub>topics: —</sub>
- **[illuin-tech/colpali](https://github.com/illuin-tech/colpali)** · 2,666★ · Python · Mature  
  Vision embeddings (ColPali/ColQwen) for document retrieval straight from page images.  
  <sub>topics: colpali, information-retrieval, retrieval-augmented-generation, vision-language-model, colqwen2, colsmol</sub>
- **[superlinked/sie](https://github.com/superlinked/sie)** · 2,042★ · Python · Mature  
  Inference engine/server for embeddings & rerankers in production retrieval.  
  <sub>topics: embeddings, vector-search, data-pipeline, deep-learning, information-retrieval, llm, ml, mlops</sub>

### Novel retrieval approach

_Projects challenging the embed-everything-into-a-vector-DB default — vectorless, storage-frugal, or domain-specialized retrieval._

- **[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** · 32,927★ · Python · Hot  
  Vectorless, reasoning-based RAG — builds a document index/tree, navigates with the LLM.  
  <sub>topics: agentic-ai, agents, ai, ai-agents, context-engineering, llm, rag, reasoning</sub>
- **[zilliztech/claude-context](https://github.com/zilliztech/claude-context)** · 11,818★ · TypeScript · Hot  
  Code-search MCP that makes an entire codebase the retrievable context for coding agents.  
  <sub>topics: agent, agentic-rag, ai-coding, code-search, cursor, embedding, mcp, nodejs</sub>

## Spotlight: GraphRAG

A cross-cutting trend — instead of a flat vector store, build a **knowledge graph** over chunks so retrieval can follow relationships (better for multi-hop questions). In your stars:

- **[microsoft/graphrag](https://github.com/microsoft/graphrag)** · 33,661★ — Microsoft's reference GraphRAG — LLM-built entity graph + community summaries over a corpus.
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 36,460★ — Simple & fast RAG that builds a graph index over chunks (GraphRAG-style) for better multi-hop recall.
- **[FalkorDB/GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK)** · 935★ — SDK to build GraphRAG apps on FalkorDB at scale.
- **[FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB)** · 4,547★ — Fast graph database (GraphBLAS) — substrate for graph-shaped retrieval.

## Graph analysis — how they relate

**Community clustering.** These 31 tools span **11 of the graph's 31 communities**.

- **Community 3** (9): `infiniflow/ragflow`, `HKUDS/LightRAG`, `deepset-ai/haystack`, `llmware-ai/llmware`, `SylphAI-Inc/AdalFlow`, `airweave-ai/airweave`, `Bessouat40/RAGLight`, `neuml/txtai`, `VectifyAI/PageIndex`
- **Community 17** (6): `qdrant/qdrant`, `weaviate/weaviate`, `pgvector/pgvector`, `alibaba/zvec`, `milvus-io/milvus`, `lancedb/lancedb`
- **Community 8** (5): `FalkorDB/GraphRAG-SDK`, `FalkorDB/FalkorDB`, `chonkie-inc/chonkie`, `chonkie-inc/chonkiejs`, `illuin-tech/colpali`
- **Community 6** (3): `facebookresearch/faiss`, `marqo-ai/marqo`, `PaddlePaddle/PaddleOCR`
- **Community 11** (2): `Unstructured-IO/unstructured`, `superlinked/sie`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' RAG tools in your ecosystem:

- `VectifyAI/PageIndex` — PageRank 0.0024
- `FalkorDB/GraphRAG-SDK` — PageRank 0.0022
- `HKUDS/LightRAG` — PageRank 0.0017
- `neuml/txtai` — PageRank 0.0012
- `lancedb/lancedb` — PageRank 0.0012
- `weaviate/weaviate` — PageRank 0.0012
- `microsoft/graphrag` — PageRank 0.0011
- `FalkorDB/FalkorDB` — PageRank 0.0011
- `chroma-core/chroma` — PageRank 0.0010
- `chonkie-inc/chonkie` — PageRank 0.0010

**Direct links between RAG tools** (top similarity edges where both endpoints are in this report):

- `chonkie-inc/chonkiejs` ⇄ `chonkie-inc/chonkie` (w=1.619) — topics: ai, splitting-algorithms, chunker, rag; authors: chonk-lain
- `FalkorDB/GraphRAG-SDK` ⇄ `FalkorDB/FalkorDB` (w=0.867) — topics: graphrag, knowledge-graph, graph-database; authors: dependabot[bot]
- `HKUDS/RAG-Anything` ⇄ `HKUDS/LightRAG` (w=0.750) — topics: retrieval-augmented-generation; authors: danielaskdd
- `FalkorDB/GraphRAG-SDK` ⇄ `VectifyAI/PageIndex` (w=0.441) — topics: rag, llm; authors: dependabot[bot]
- `weaviate/weaviate` ⇄ `qdrant/qdrant` (w=0.429) — topics: search-engine, vector-search, vector-search-engine, vector-database
- `lancedb/lancedb` ⇄ `weaviate/weaviate` (w=0.400) — topics: approximate-nearest-neighbor-search, image-search, nearest-neighbor-search, recommender-system
- `neuml/txtai` ⇄ `VectifyAI/PageIndex` (w=0.383) — topics: llm, vector-database, information-retrieval, retrieval-augmented-generation
- `neuml/txtai` ⇄ `deepset-ai/haystack` (w=0.379) — topics: python, nlp, semantic-search, llm
- `SylphAI-Inc/AdalFlow` ⇄ `deepset-ai/haystack` (w=0.379) — topics: agent, llm, rag, generative-ai
- `VectifyAI/PageIndex` ⇄ `illuin-tech/colpali` (w=0.375) — topics: retrieval-augmented-generation, information-retrieval; authors: dependabot[bot]
- `VectifyAI/PageIndex` ⇄ `infiniflow/ragflow` (w=0.344) — topics: agentic-ai, ai, ai-agents, rag
- `VectifyAI/PageIndex` ⇄ `airweave-ai/airweave` (w=0.330) — topics: ai, ai-agents, llm, rag
- `lancedb/lancedb` ⇄ `qdrant/qdrant` (w=0.318) — topics: image-search, nearest-neighbor-search, recommender-system, search-engine; authors: dependabot[bot]
- `neuml/txtai` ⇄ `airweave-ai/airweave` (w=0.300) — topics: search, semantic-search, llm, information-retrieval
- `lancedb/lancedb` ⇄ `alibaba/zvec` (w=0.282) — topics: search-engine, semantic-search, similarity-search, vector-database; authors: dependabot[bot]
- …and 12 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| run-llama/llama_index | 100 | Classic | very active | 7 | 25% | 494 |
| milvus-io/milvus | 100 | Classic | very active | 8 | 8% | 164 |
| infiniflow/ragflow | 96 | Mature | very active | 8 | 12% | 48 |
| lancedb/lancedb | 96 | Classic | very active | 5 | 14% | 442 |
| qdrant/qdrant | 93 | Classic | very active | 4 | 18% | 114 |
| deepset-ai/haystack | 90 | Classic | very active | 3 | 33% | 230 |
| facebookresearch/faiss | 88 | Classic | very active | 3 | 21% | 26 |
| alibaba/zvec | 87 | Hot | very active | 3 | 23% | 7 |
| weaviate/weaviate | 84 | Classic | very active | 2 | 48% | 545 |
| FalkorDB/FalkorDB | 84 | Mature | very active | 3 | 25% | 75 |
| chroma-core/chroma | 83 | Classic | very active | 2 | 39% | 137 |
| Unstructured-IO/unstructured | 82 | Classic | very active | 3 | 28% | 231 |
| PaddlePaddle/PaddleOCR | 81 | Classic | very active | 2 | 35% | 33 |
| HKUDS/LightRAG | 79 | Mature | very active | 1 | 89% | 75 |
| neuml/txtai | 78 | Mature | very active | 1 | 100% | 64 |
| chonkie-inc/chonkie | 78 | Hot | very active | 1 | 84% | 44 |
| FalkorDB/GraphRAG-SDK | 77 | Mature | very active | 1 | 82% | 30 |
| airweave-ai/airweave | 75 | Hot | very active | 1 | 50% | 470 |
| huggingface/sentence-transformers | 75 | Classic | very active | 1 | 72% | 66 |
| HKUDS/RAG-Anything | 72 | Hot | very active | 1 | 54% | 19 |
| superlinked/sie | 72 | Mature | very active | 1 | 55% | 18 |
| microsoft/graphrag | 68 | Mature | active | 1 | 69% | 40 |
| marqo-ai/marqo | 68 | Classic | very active | 1 | 71% | 113 |
| illuin-tech/colpali | 66 | Mature | active | 1 | 50% | 22 |
| Bessouat40/RAGLight | 64 | Mature | slowing | 1 | 100% | 45 |
| chonkie-inc/chonkiejs | 64 | Hot | very active | 1 | 93% | 5 |
| zilliztech/claude-context | 60 | Hot | very active | 2 | 40% | 0 |
| llmware-ai/llmware | 58 | Mature | very active | 1 | 100% | 3 |
| SylphAI-Inc/AdalFlow | 56 | Mature | active | 1 | 60% | 7 |
| pgvector/pgvector | 56 | Classic | very active | 1 | 83% | 0 |
| VectifyAI/PageIndex | 50 | Hot | very active | 1 | 73% | 0 |

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

- **langchain-ai/langchain** (139,060★) — general agent/LLM framework — RAG is one use case, too broad to list as RAG-specific
- **topoteretes/cognee** (17,792★) — covered in the *memory frameworks* report (graph memory, RAG-adjacent)
- **memvid/memvid** (15,642★) — covered in the *memory frameworks* report
- **NirDiamant/RAG_Techniques** (27,870★) — excellent *tutorial* collection, not a tool/library
- **KRLabsOrg/LettuceDetect** (577★) — RAG *evaluation* (hallucination detection) — see the LLM-evaluation report

## Methodology & caveats

- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (rag / retrieval-augmented / graphrag / vector db / embedding / rerank / chunk / semantic-search) + manual curation into pipeline stages. Tutorials, general agent frameworks, and memory-layer projects were routed to adjacent reports or excluded (see above).
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 31 · Snapshot: 2026-06-11T21:58:33.384Z</sub>
