# Document Extraction Frameworks — Landscape & Task Rankings

> Derived from **kaiser-data**'s 2,587 starred repos (snapshot `2026-11-02T14:17:38.270Z`), cross-referenced with the repo-similarity graph (2,587 nodes / 8,732 edges, 42 communities). Task rankings are additionally backed by external benchmarks (OmniDocBench, opendataloader-bench) — see Methodology.
>
> Generated 2026-11-02 by `scripts/reports/document_extraction.py` (regenerate any time — no API cost).

![Top tools by stars](assets/document-extraction-top-tools.svg)

![Tools per category](assets/document-extraction-categories.svg)


## Executive summary

- **26 document-extraction tools** in your stars (**729,826★** combined), organized along the extraction pipeline:
  - **Conversion framework** (7): `markitdown`, `MinerU`, `docling`, `marker`, `unstructured`, `xberg`, `semtools`
  - **OCR / layout model** (3): `PaddleOCR`, `tesseract`, `DocLayout-YOLO`
  - **VLM document parser** (8): `DeepSeek-OCR`, `olmocr`, `zerox`, `nougat`, `dots.ocr`, `Dolphin`, `MonkeyOCR`, `DeepSeek-OCR-2`
  - **Structured field extraction** (3): `langextract`, `ade-python`, `instructor-js`
  - **Format-specific / serving** (5): `python-docx`, `marker-api`, `docling-mcp`, `PdfItDown`, `pdf-redactor`
- Mental model — extraction is a pipeline: **detect layout → OCR/parse elements → reconstruct structure (tables/formulas/reading order) → export markdown/JSON → extract typed fields**. Frameworks bundle the first four stages; field extractors sit on top.
- The field is mid-disruption: **single-VLM parsers** (`DeepSeek-OCR`, `dots.ocr`, `Dolphin`, `MonkeyOCR`) are replacing multi-model pipelines, and on OmniDocBench the best open models now beat GPT/Gemini-class generalists at parsing.
- Second trend: **token economics**. `DeepSeek-OCR`'s optical compression (~10× fewer vision tokens per page) and `olmocr`'s throughput focus optimize for LLM-corpus cost, not just accuracy.
- No single winner — the *task rankings* below are the point of this report: the best tool for table-heavy finance PDFs (`docling`) is not the best for CJK layouts (`MinerU`) or office-file bulk conversion (`markitdown`).

## The extraction pipeline at a glance

| Stage | What happens | Tools in your stars |
|---|---|---|
| **Layout detection** | Find blocks: text, tables, figures, formulas | `DocLayout-YOLO` (also built into every framework) |
| **OCR / recognition** | Pixels → characters | `PaddleOCR`, `tesseract`, all VLM parsers |
| **Structure reconstruction** | Tables, formulas, reading order | `docling` (TableFormer), `MinerU`, `marker`, `Dolphin`, `MonkeyOCR` |
| **Export** | Markdown / JSON / HTML for LLMs | `markitdown`, `xberg`, `unstructured`, `semtools`, `zerox`, `olmocr`, `nougat`, `dots.ocr`, `DeepSeek-OCR` |
| **Field extraction** | Typed, schema'd values out of parsed text | `langextract`, `ade-python`, `instructor-js` |
| **Serving / glue** | APIs, MCP, format utilities | `marker-api`, `docling-mcp`, `python-docx`, `pdf-redactor`, `PdfItDown` |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Conversion framework | Python | MIT | 193,512 (▲184) | Hot | 89 | very active | 5d ago | 2.0y | 45 |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | OCR / layout model | Python | Apache-2.0 | 92,127 (▲71) | Mature | 58 | active | 1mo ago | 6.5y | 1 |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | Conversion framework | Python | NOASSERTION | 82,996 (▲70) | Mature | 80 | very active | 0d ago | 2.7y | 4 |
| [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | OCR / layout model | C++ | Apache-2.0 | 77,299 (▲16) | Classic | 68 | very active | 0d ago | 12.2y | 18 |
| [docling-project/docling](https://github.com/docling-project/docling) | Conversion framework | Python | MIT | 70,009 (▲64) | Mature | 97 | very active | 1d ago | 2.3y | 49 |
| [datalab-to/marker](https://github.com/datalab-to/marker) | Conversion framework | Python | Apache-2.0 | 40,751 (▲13) | Classic | 55 | active | 4d ago | 3.0y | 3 |
| [google/langextract](https://github.com/google/langextract) | Structured field extraction | Python | Apache-2.0 | 39,244 (▲19) | Mature | 69 | very active | 0d ago | 1.3y | 7 |
| [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) | VLM document parser | Python | MIT | 24,111 (▲3) | Declining | 8 | stale | 9mo ago | 1.0y | 0 |
| [allenai/olmocr](https://github.com/allenai/olmocr) | VLM document parser | Python | Apache-2.0 | 19,814 (▲1) | Declining | 34 | stale | 7mo ago | 2.1y | 0 |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | Conversion framework | HTML | Apache-2.0 | 15,670 (▲14) | Classic | 98 | very active | 0d ago | 4.1y | 44 |
| [getomni-ai/zerox](https://github.com/getomni-ai/zerox) | VLM document parser | TypeScript | MIT | 12,253 (▲4) | Abandoned | 3 | stale | 1.5y ago | 2.3y | 0 |
| [facebookresearch/nougat](https://github.com/facebookresearch/nougat) | VLM document parser | Python | MIT | 10,092 (▲2) | Abandoned | 5 | stale | 1.7y ago | 3.4y | 0 |
| [xberg-io/xberg](https://github.com/xberg-io/xberg) | Conversion framework | Rust | MIT | 9,512 (▲9) | Mature | 80 | very active | 0d ago | 1.8y | 2 |
| [studio-dots-ai/dots.ocr](https://github.com/studio-dots-ai/dots.ocr) | VLM document parser | Python | MIT | 9,185 (▲1) | Declining | 16 | stale | 7mo ago | 1.3y | 0 |
| [bytedance/Dolphin](https://github.com/bytedance/Dolphin) | VLM document parser | Python | NOASSERTION | 9,066 | Declining | 17 | stale | 7mo ago | 1.5y | 0 |
| [Yuliang-Liu/MonkeyOCR](https://github.com/Yuliang-Liu/MonkeyOCR) | VLM document parser | Python | Apache-2.0 | 6,649 | Declining | 31 | slowing | 3mo ago | 1.4y | 0 |
| [python-openxml/python-docx](https://github.com/python-openxml/python-docx) | Format-specific / serving | Python | MIT | 5,755 | Mature | 29 | slowing | 3mo ago | 13.1y | 0 |
| [deepseek-ai/DeepSeek-OCR-2](https://github.com/deepseek-ai/DeepSeek-OCR-2) | VLM document parser | Python | Apache-2.0 | 3,528 (▲4) | Declining | 8 | stale | 9mo ago | 9mo | 0 |
| [opendatalab/DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO) | OCR / layout model | Python | AGPL-3.0 | 2,303 (▲2) | Mature | 36 | active | 12d ago | 2.1y | 0 |
| [run-llama/semtools](https://github.com/run-llama/semtools) | Conversion framework | Rust | MIT | 1,879 (▲1) | Declining | 29 | stale | 7mo ago | 1.2y | 0 |
| [landing-ai/ade-python](https://github.com/landing-ai/ade-python) | Structured field extraction | Python | Apache-2.0 | 1,037 | Mature | 69 | active | 1mo ago | 1.1y | 4 |
| [adithya-s-k/marker-api](https://github.com/adithya-s-k/marker-api) | Format-specific / serving | Python | GPL-3.0 | 983 (▼1) | Abandoned | 2 | stale | 2.0y ago | 2.5y | 0 |
| [567-labs/instructor-js](https://github.com/567-labs/instructor-js) | Structured field extraction | TypeScript | MIT | 805 (▲1) | Abandoned | 7 | stale | 1.8y ago | 2.8y | 0 |
| [docling-project/docling-mcp](https://github.com/docling-project/docling-mcp) | Format-specific / serving | Python | MIT | 782 | Mature | 73 | very active | 6d ago | 1.6y | 7 |
| [AstraBert/PdfItDown](https://github.com/AstraBert/PdfItDown) | Format-specific / serving | Rust | MIT | 251 | Declining | 45 | slowing | 3mo ago | 1.8y | 0 |
| [JoshData/pdf-redactor](https://github.com/JoshData/pdf-redactor) | Format-specific / serving | Python | CC0-1.0 | 213 | Abandoned | 2 | stale | 2.4y ago | 10.1y | 0 |

## Task rankings — which framework for which job

Ranked picks per task. Dataset metrics say who's *healthy*; external benchmarks say who's *accurate* — both feed these rankings (evidence noted per row, sources in Methodology).

| Task | 🥇 First pick | 🥈 Second | 🥉 Third | Evidence / note |
|---|---|---|---|---|
| **PDF → Markdown for RAG ingestion (general)** | `docling` — best accuracy of the free frameworks | `marker` — close second, faster with a GPU | `MinerU` — strong but heavier | opendataloader-bench (200 PDFs): docling 0.877 > marker 0.861 > MinerU 0.831. |
| **Complex layouts, CJK & multilingual docs** | `MinerU` — nothing else close for Chinese/Japanese/Korean layout | `dots.ocr` — one compact VLM, 100+ languages | `PaddleOCR` — PaddleOCR-VL tops OmniDocBench composite | OmniDocBench v1.5: PaddleOCR-VL 94.5, MinerU2.5 90.7, dots.ocr 88.4. |
| **Tables & financial documents** | `docling` — TableFormer — the table-structure specialist | `MinerU` — robust table + layout models | `marker` — good table fidelity, JSON output | Docling is the consensus pick when documents are table-heavy. |
| **Scientific papers & formulas** | `MinerU` — formula → LaTeX built in | `marker` — strong math handling via Surya | `nougat` — the pioneer — only for legacy pipelines | Nougat defined the task but is unmaintained; MinerU/marker superseded it. |
| **Scanned documents & handwriting** | `DeepSeek-OCR` — VLM robustness + handwriting | `PaddleOCR` — classic pick, 80+ languages | `tesseract` — fine for clean printed scans only | VLM parsers degrade gracefully on noise where classic OCR breaks. |
| **Office documents (DOCX/PPTX/XLSX) at speed** | `markitdown` — instant, dependency-light | `xberg` — Rust-core speed, 97+ formats, no GPU | `docling` — when you also need layout fidelity | Native-format parsing needs no vision models — lightweight tools win. |
| **Enterprise ETL across many formats** | `unstructured` — 25+ formats, chunking, connectors | `xberg` — self-hosted polyglot core, REST/MCP | `docling` — IBM backing, growing connector set | Pick by ops model: managed pipeline vs. embedded library. |
| **Structured field extraction (invoices, entities, forms)** | `langextract` — grounded extraction with source offsets | `zerox` — simplest path via hosted vision models | `ade-python` — schema-driven agentic extraction | Parse-then-extract beats end-to-end when you need auditable provenance. |
| **Building LLM training corpora at scale** | `olmocr` — purpose-built for dataset linearization | `DeepSeek-OCR` — 10× token compression cuts corpus cost | `MinerU` — the OpenDataLab production pipeline | Throughput and token economics dominate accuracy deltas at corpus scale. |
| **Agent / CLI integration** | `docling-mcp` — document conversion as MCP tools | `semtools` — parse + semantic search on the command line | `marker-api` — marker behind a REST endpoint | Serving wrappers matter more than parser choice for agent workflows. |

## By category

### Conversion framework

_End-to-end document → markdown/JSON systems — the layer most people mean by 'document extraction'. Differ mainly in accuracy/speed trade-off, format breadth, and GPU appetite._

- **[microsoft/markitdown](https://github.com/microsoft/markitdown)** · 193,512★ · Python · Hot  
  Microsoft's lightweight anything→Markdown converter — speed and format coverage over layout fidelity.  
  <sub>topics: langchain, openai, autogen-extension, autogen, markdown, microsoft-office, pdf</sub>
- **[opendatalab/MinerU](https://github.com/opendatalab/MinerU)** · 82,996★ · Python · Mature  
  PDF/Office → LLM-ready markdown/JSON; the reference for complex layouts and CJK documents (MinerU2.5 VLM).  
  <sub>topics: extract-data, layout-analysis, ocr, parser, pdf, pdf-converter, python, document-analysis</sub>
- **[docling-project/docling](https://github.com/docling-project/docling)** · 70,009★ · Python · Mature  
  IBM's document toolkit — TableFormer table structure, PDF/DOCX/PPTX/HTML/audio, first-class LlamaIndex/LangChain integration.  
  <sub>topics: ai, convert, documents, pdf, tables, document-parser, document-parsing, docx</sub>
- **[datalab-to/marker](https://github.com/datalab-to/marker)** · 40,751★ · Python · Classic  
  Fast, accurate PDF → markdown + JSON; GPU-accelerated (Surya models), strong structure fidelity.  
  <sub>topics: —</sub>
- **[Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)** · 15,670★ · HTML · Classic  
  Open-source ETL for 25+ file formats → clean structured elements; the enterprise-pipeline pick.  
  <sub>topics: deep-learning, document-parsing, machine-learning, nlp, ocr, information-retrieval, data-pipelines, ml</sub>
- **[xberg-io/xberg](https://github.com/xberg-io/xberg)** · 9,512★ · Rust · Mature  
  Polyglot document-intelligence framework with a Rust core (ex-Kreuzberg) — 97+ formats, CPU-only, library/CLI/REST/MCP.  
  <sub>topics: text-extraction, document-intelligence, metadata-extraction, pdf-extraction, python, rag, table-extraction, tesseract</sub>
- **[run-llama/semtools](https://github.com/run-llama/semtools)** · 1,879★ · Rust · Declining  
  LlamaIndex's CLI: document parsing + semantic search as composable command-line tools.  
  <sub>topics: cli, embeddings, parser, rust, search, semantic, semantic-search, static-embedding</sub>

### OCR / layout model

_The classic recognition layer: character recognition and layout detection as standalone engines/models, used inside the frameworks above._

- **[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** · 92,127★ · Python · Mature  
  The dominant OCR toolkit (80+ languages) + PP-Structure pipelines; its PaddleOCR-VL models top OmniDocBench.  
  <sub>topics: ocr, chineseocr, pdf2markdown, pp-ocr, pp-structure, document-parsing, document-translation, kie</sub>
- **[tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)** · 77,299★ · C++ · Classic  
  The veteran C++ OCR engine — battle-tested baseline for clean printed scans, zero GPU.  
  <sub>topics: tesseract, tesseract-ocr, ocr, lstm, machine-learning, ocr-engine, hacktoberfest</sub>
- **[opendatalab/DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)** · 2,303★ · Python · Mature  
  YOLO-v10-based layout detection — best standalone layout mAP on OmniDocBench component tests.  
  <sub>topics: —</sub>

### VLM document parser

_The disruption: one vision-language model reads the page end-to-end. Compact open models now beat closed generalist VLMs on document parsing benchmarks._

- **[deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)** · 24,111★ · Python · Declining  
  Contexts optical compression — ~10× fewer vision tokens per page at ≥90% decoding accuracy; built for LLM-scale corpora.  
  <sub>topics: —</sub>
- **[allenai/olmocr](https://github.com/allenai/olmocr)** · 19,814★ · Python · Declining  
  AllenAI's toolkit for linearizing PDFs into LLM training data — throughput-oriented, permissively licensed.  
  <sub>topics: —</sub>
- **[getomni-ai/zerox](https://github.com/getomni-ai/zerox)** · 12,253★ · TypeScript · Abandoned  
  OCR by delegation: renders pages and asks a hosted vision model (GPT/Claude/Gemini) — zero local models.  
  <sub>topics: ocr, pdf</sub>
- **[facebookresearch/nougat](https://github.com/facebookresearch/nougat)** · 10,092★ · Python · Abandoned  
  Meta's neural OCR for academic PDFs (math → LaTeX) — historically important, now effectively unmaintained.  
  <sub>topics: —</sub>
- **[studio-dots-ai/dots.ocr](https://github.com/studio-dots-ai/dots.ocr)** · 9,185★ · Python · Declining  
  Multilingual layout + parsing in a single compact VLM (~3B); 88.4 on OmniDocBench v1.5.  
  <sub>topics: —</sub>
- **[bytedance/Dolphin](https://github.com/bytedance/Dolphin)** · 9,066★ · Python · Declining  
  ByteDance's ACL-2025 parser — heterogeneous anchor prompting (layout first, parallel element parsing second).  
  <sub>topics: document-analysis, layout-analysis, ocr, parser, pdf, pdf-converter, pdf-parser, python</sub>
- **[Yuliang-Liu/MonkeyOCR](https://github.com/Yuliang-Liu/MonkeyOCR)** · 6,649★ · Python · Declining  
  Lightweight structure-recognition-relation model; MonkeyOCR-pro-3B beat Gemini/GPT-4o-class models on OmniDocBench.  
  <sub>topics: —</sub>
- **[deepseek-ai/DeepSeek-OCR-2](https://github.com/deepseek-ai/DeepSeek-OCR-2)** · 3,528★ · Python · Declining  
  Second iteration ('Visual Causal Flow') — 91.1 on OmniDocBench v1.5, ahead of most open VLM parsers.  
  <sub>topics: —</sub>

### Structured field extraction

_Post-parsing: pull typed, schema-validated values (entities, invoice fields, dates) out of the recovered text — with provenance._

- **[google/langextract](https://github.com/google/langextract)** · 39,244★ · Python · Mature  
  Google's library for LLM extraction of structured info with precise source grounding (char-level offsets).  
  <sub>topics: llm, nlp, python, gemini-ai, information-extration, large-language-models, structured-data, gemini</sub>
- **[landing-ai/ade-python](https://github.com/landing-ai/ade-python)** · 1,037★ · Python · Mature  
  LandingAI's Agentic Document Extraction client — schema-driven field extraction from visually complex docs.  
  <sub>topics: —</sub>
- **[567-labs/instructor-js](https://github.com/567-labs/instructor-js)** · 805★ · TypeScript · Abandoned  
  Schema-first structured outputs for LLMs (instructor's JS port) — the validation layer after parsing.  
  <sub>topics: llm, openai, zod</sub>

### Format-specific / serving

_Utilities and wrappers: format-native readers/writers, redaction, and API/MCP layers that put parsers behind an endpoint._

- **[python-openxml/python-docx](https://github.com/python-openxml/python-docx)** · 5,755★ · Python · Mature  
  The standard library for reading and writing Word .docx programmatically.  
  <sub>topics: —</sub>
- **[adithya-s-k/marker-api](https://github.com/adithya-s-k/marker-api)** · 983★ · Python · Abandoned  
  Deployable REST API wrapping marker — PDF→markdown as a service.  
  <sub>topics: fastapi, marker, pdf-converter, pdf-files, pdf-parser, pdf-parsing, api, rest-api</sub>
- **[docling-project/docling-mcp](https://github.com/docling-project/docling-mcp)** · 782★ · Python · Mature  
  Docling exposed as MCP tools — document conversion for agent workflows.  
  <sub>topics: —</sub>
- **[AstraBert/PdfItDown](https://github.com/AstraBert/PdfItDown)** · 251★ · Rust · Declining  
  The inverse direction: convert anything → PDF (normalization before extraction).  
  <sub>topics: csv, docx, html, json, markdown, package, pdf, pdf-conversion</sub>
- **[JoshData/pdf-redactor](https://github.com/JoshData/pdf-redactor)** · 213★ · Python · Abandoned  
  General-purpose PDF text-layer redaction for Python.  
  <sub>topics: —</sub>

## Spotlight: the single-VLM takeover

Two years ago document extraction meant a *pipeline of specialist models* (layout detector → OCR → table model → formula model). The 2025–26 wave collapses that into **one vision-language model per page**:

- **Accuracy**: on OmniDocBench v1.5, open parsers now score 88–95 (PaddleOCR-VL 94.5, DeepSeek-OCR-2 91.1, MinerU2.5 90.7, dots.ocr 88.4) — *above* generalist frontier VLMs on the same benchmark.
- **Size**: the winners are ~3B-parameter models (`dots.ocr`, `MonkeyOCR-pro-3B`, `DeepSeek-OCR`) — self-hostable on a single GPU.
- **Token economics**: `DeepSeek-OCR` reframes OCR as *context compression* — 1,000 text tokens → ~100 vision tokens at ~97% fidelity — which matters more than accuracy when feeding million-page corpora to LLMs.
- **Consequence**: classic engines (`tesseract`) and pipeline frameworks keep the CPU-only and clean-scan niches; everything else is converging on VLMs, with the frameworks (`MinerU`, `marker`, `docling`) absorbing them as backends.

## Graph analysis — how they relate

**Community clustering.** These 26 tools span **11 of the graph's 42 communities**.

- **Community 32** (7): `opendatalab/MinerU`, `run-llama/semtools`, `opendatalab/DocLayout-YOLO`, `getomni-ai/zerox`, `bytedance/Dolphin`, `landing-ai/ade-python`, `adithya-s-k/marker-api`
- **Community 0** (5): `allenai/olmocr`, `studio-dots-ai/dots.ocr`, `Yuliang-Liu/MonkeyOCR`, `python-openxml/python-docx`, `JoshData/pdf-redactor`
- **Community 2** (3): `microsoft/markitdown`, `xberg-io/xberg`, `567-labs/instructor-js`
- **Community 14** (3): `docling-project/docling`, `Unstructured-IO/unstructured`, `docling-project/docling-mcp`
- **Community 16** (2): `deepseek-ai/DeepSeek-OCR`, `deepseek-ai/DeepSeek-OCR-2`

**Centrality (PageRank in the full 2,587-repo graph)** — most 'hub-like' extraction tools in your ecosystem:

- `deepseek-ai/DeepSeek-OCR-2` — PageRank 0.0005
- `opendatalab/MinerU` — PageRank 0.0005
- `microsoft/markitdown` — PageRank 0.0004
- `bytedance/Dolphin` — PageRank 0.0004
- `Yuliang-Liu/MonkeyOCR` — PageRank 0.0004
- `run-llama/semtools` — PageRank 0.0004
- `google/langextract` — PageRank 0.0004
- `PaddlePaddle/PaddleOCR` — PageRank 0.0004
- `facebookresearch/nougat` — PageRank 0.0003
- `docling-project/docling` — PageRank 0.0003

**Direct links between extraction tools** (top similarity edges where both endpoints are in this report):

- `docling-project/docling-mcp` ⇄ `docling-project/docling` (w=0.663) — authors: ceberam, github-actions[bot], dolfim-ibm
- `deepseek-ai/DeepSeek-OCR-2` ⇄ `deepseek-ai/DeepSeek-OCR` (w=0.550)
- `opendatalab/DocLayout-YOLO` ⇄ `opendatalab/MinerU` (w=0.550)
- `bytedance/Dolphin` ⇄ `opendatalab/MinerU` (w=0.521) — topics: document-analysis, layout-analysis, ocr, parser
- `Unstructured-IO/unstructured` ⇄ `docling-project/docling` (w=0.345) — topics: document-parsing, pdf-to-text, pdf, pdf-to-json; authors: tanishqbaweja, chrikrah, Eapp1e
- `bytedance/Dolphin` ⇄ `getomni-ai/zerox` (w=0.222) — topics: ocr, pdf
- `PaddlePaddle/PaddleOCR` ⇄ `opendatalab/MinerU` (w=0.210) — topics: ocr, ai4science, pdf-extractor-rag, pdf-parser
- `adithya-s-k/marker-api` ⇄ `bytedance/Dolphin` (w=0.183) — topics: pdf-converter, pdf-parser
- `adithya-s-k/marker-api` ⇄ `opendatalab/MinerU` (w=0.141) — topics: pdf-converter, pdf-parser

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| Unstructured-IO/unstructured | 98 | Classic | very active | 8 | 14% | 255 |
| docling-project/docling | 97 | Mature | very active | 7 | 16% | 234 |
| microsoft/markitdown | 89 | Hot | very active | 4 | 35% | 24 |
| opendatalab/MinerU | 80 | Mature | very active | 1 | 93% | 204 |
| xberg-io/xberg | 80 | Mature | very active | 1 | 97% | 126 |
| docling-project/docling-mcp | 73 | Mature | very active | 2 | 41% | 25 |
| google/langextract | 69 | Mature | very active | 1 | 75% | 20 |
| landing-ai/ade-python | 69 | Mature | active | 2 | 44% | 62 |
| tesseract-ocr/tesseract | 68 | Classic | very active | 1 | 74% | 37 |
| PaddlePaddle/PaddleOCR | 58 | Mature | active | 1 | 100% | 33 |
| datalab-to/marker | 55 | Classic | active | 1 | 61% | 73 |
| AstraBert/PdfItDown | 45 | Declining | slowing | 0 | 0% | 36 |
| opendatalab/DocLayout-YOLO | 36 | Mature | active | 0 | 0% | 0 |
| allenai/olmocr | 34 | Declining | stale | 0 | 0% | 44 |
| Yuliang-Liu/MonkeyOCR | 31 | Declining | slowing | 0 | 0% | 0 |
| run-llama/semtools | 29 | Declining | stale | 0 | 0% | 17 |
| python-openxml/python-docx | 29 | Mature | slowing | 0 | 0% | 0 |
| bytedance/Dolphin | 17 | Declining | stale | 0 | 0% | 0 |
| studio-dots-ai/dots.ocr | 16 | Declining | stale | 0 | 0% | 0 |
| deepseek-ai/DeepSeek-OCR | 8 | Declining | stale | 0 | 0% | 0 |
| deepseek-ai/DeepSeek-OCR-2 | 8 | Declining | stale | 0 | 0% | 0 |
| 567-labs/instructor-js | 7 | Abandoned | stale | 0 | 0% | 18 |
| facebookresearch/nougat | 5 | Abandoned | stale | 0 | 0% | 2 |
| getomni-ai/zerox | 3 | Abandoned | stale | 0 | 0% | 9 |
| JoshData/pdf-redactor | 2 | Abandoned | stale | 0 | 0% | 0 |
| adithya-s-k/marker-api | 2 | Abandoned | stale | 0 | 0% | 0 |

Watch items: `nougat` is effectively frozen (use `MinerU`/`marker` instead); `zerox` reads as abandoned in this snapshot — its hosted-VLM pattern is trivial to reimplement if it stays stale; `marker-api` and `pdf-redactor` are stale single-maintainer wrappers — pin versions or vendor them.

## Adjacent (deliberately not listed as extraction tools)

- **Stirling-Tools/Stirling-PDF** (95,557★) — PDF *manipulation* app (edit/merge/sign, OCR jobs via OCRmyPDF) — a toolbox, not an extraction framework
- **run-llama/llama_index** (52,777★) — positions itself as a 'document agent and OCR platform', but it's covered in the *RAG tooling* report
- **firecrawl/firecrawl** (197,852★) — extraction for the *web* (scraping/crawling), not documents
- **microsoft/OmniParser** (25,601★) — parses GUI *screenshots* for computer-use agents, not documents
- **VectifyAI/PageIndex** (39,955★) — document *retrieval* (vectorless RAG) — see the RAG tooling report
- **tjmlabs/ColiVara** (1,486★) — visual document *retrieval* (ColPali-style), not extraction
- **kba/awesome-ocr** (3,127★) — link collection, not a tool
- **tk04/Marker** (1,192★) — markdown *editor* that happens to share marker's name — no relation

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json` for all repo metrics and graph structure. No API calls at generation time; fully reproducible.
- **Selection**: keyword scan (pdf / ocr / document / layout / extract / parsing / docx / markdown-convert) + manual curation into pipeline stages. Retrieval, web scraping, GUI parsing, and PDF-editing apps were routed to adjacent reports or excluded (see above).
- **Task rankings** additionally cite external benchmark evidence gathered 2026-07: [OmniDocBench](https://github.com/opendatalab/OmniDocBench) v1.5 composite scores, the [opendataloader-bench 200-PDF comparison](https://pdfmux.com/blog/pdfmux-vs-pymupdf-vs-marker-vs-docling/), and vendor papers (MinerU2.5, dots.ocr, DeepSeek-OCR, Dolphin). Benchmark numbers are point-in-time and partly vendor-reported — treat rankings as defaults, not verdicts.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity; benchmark citations are frozen text and need manual review on major model releases.

<sub>Tools covered: 26 · Snapshot: 2026-11-02T14:17:38.270Z</sub>
