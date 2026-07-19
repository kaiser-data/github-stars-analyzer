# Document Extraction Frameworks — Landscape & Task Rankings

> Derived from **kaiser-data**'s 1,327 starred repos (snapshot `2026-07-13T08:42:30.177Z`), cross-referenced with the repo-similarity graph (1,327 nodes / 4,302 edges, 26 communities). Task rankings are additionally backed by external benchmarks (OmniDocBench, opendataloader-bench) — see Methodology.
>
> Generated 2026-07-19 by `scripts/reports/document_extraction.py` (regenerate any time — no API cost).

![Top tools by stars](assets/document-extraction-top-tools.svg)

![Tools per category](assets/document-extraction-categories.svg)


## Executive summary

- **26 document-extraction tools** in your stars (**668,011★** combined), organized along the extraction pipeline:
  - **Conversion framework** (7): `markitdown`, `MinerU`, `docling`, `marker`, `unstructured`, `xberg`, `semtools`
  - **OCR / layout model** (3): `PaddleOCR`, `tesseract`, `DocLayout-YOLO`
  - **VLM document parser** (8): `DeepSeek-OCR`, `olmocr`, `zerox`, `nougat`, `Dolphin`, `dots.ocr`, `MonkeyOCR`, `DeepSeek-OCR-2`
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
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Conversion framework | Python | MIT | 165,256 (▲14,113) | Declining | 51 | active | 19d ago | 1.7y | 3 |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | OCR / layout model | Python | Apache-2.0 | 85,345 (▲3,484) | Classic | 79 | very active | 17d ago | 6.2y | 19 |
| [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | OCR / layout model | C++ | Apache-2.0 | 75,286 (▲656) | Classic | 61 | very active | 4d ago | 11.9y | 6 |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | Conversion framework | Python | NOASSERTION | 74,412 (▲7,157) | Mature | 80 | very active | 0d ago | 2.4y | 1 |
| [docling-project/docling](https://github.com/docling-project/docling) | Conversion framework | Python | MIT | 63,059 (▲1,654) | Mature | 95 | very active | 0d ago | 2.0y | 35 |
| [datalab-to/marker](https://github.com/datalab-to/marker) | Conversion framework | Python | GPL-3.0 | 37,433 (▲1,424) | Mature | 62 | active | 6d ago | 2.7y | 2 |
| [google/langextract](https://github.com/google/langextract) | Structured field extraction | Python | Apache-2.0 | 37,135 (▲262) | Mature | 67 | very active | 11d ago | 1.0y | 6 |
| [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) | VLM document parser | Python | MIT | 23,562 (▲288) | Declining | 17 | slowing | 5mo ago | 8mo | 0 |
| [allenai/olmocr](https://github.com/allenai/olmocr) | VLM document parser | Python | Apache-2.0 | 19,077 (▲1,691) | Declining | 44 | slowing | 3mo ago | 1.8y | 0 |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | Conversion framework | HTML | Apache-2.0 | 15,125 (▲236) | Classic | 69 | very active | 0d ago | 3.8y | 8 |
| [getomni-ai/zerox](https://github.com/getomni-ai/zerox) | VLM document parser | TypeScript | MIT | 12,242 (▲3) | Abandoned | 3 | stale | 1.1y ago | 2.0y | 0 |
| [facebookresearch/nougat](https://github.com/facebookresearch/nougat) | VLM document parser | Python | MIT | 10,043 (▲34) | Abandoned | 5 | stale | 1.4y ago | 3.1y | 0 |
| [bytedance/Dolphin](https://github.com/bytedance/Dolphin) | VLM document parser | Python | NOASSERTION | 9,031 (▲20) | Declining | 26 | slowing | 3mo ago | 1.2y | 0 |
| [rednote-hilab/dots.ocr](https://github.com/rednote-hilab/dots.ocr) | VLM document parser | Python | MIT | 8,996 (▲80) | Declining | 25 | slowing | 3mo ago | 11mo | 0 |
| [xberg-io/xberg](https://github.com/xberg-io/xberg) | Conversion framework | Rust | MIT | 8,631 | Hot | 80 | very active | 0d ago | 1.4y | 4 |
| [Yuliang-Liu/MonkeyOCR](https://github.com/Yuliang-Liu/MonkeyOCR) | VLM document parser | Python | Apache-2.0 | 6,598 (▲2) | Declining | 43 | slowing | 2mo ago | 1.1y | 1 |
| [python-openxml/python-docx](https://github.com/python-openxml/python-docx) | Format-specific / serving | Python | MIT | 5,673 (▲41) | Abandoned | 7 | stale | 1.1y ago | 12.8y | 0 |
| [deepseek-ai/DeepSeek-OCR-2](https://github.com/deepseek-ai/DeepSeek-OCR-2) | VLM document parser | Python | Apache-2.0 | 3,128 (▲175) | Declining | 17 | slowing | 5mo ago | 5mo | 0 |
| [opendatalab/DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO) | OCR / layout model | Python | AGPL-3.0 | 2,224 (▲41) | Abandoned | 7 | stale | 1.2y ago | 1.7y | 0 |
| [run-llama/semtools](https://github.com/run-llama/semtools) | Conversion framework | Rust | MIT | 1,831 (▲18) | Declining | 42 | slowing | 4mo ago | 10mo | 0 |
| [landing-ai/ade-python](https://github.com/landing-ai/ade-python) | Structured field extraction | Python | Apache-2.0 | 1,008 (▲8) | Rising | 63 | active | 0d ago | 9mo | 5 |
| [adithya-s-k/marker-api](https://github.com/adithya-s-k/marker-api) | Format-specific / serving | Python | GPL-3.0 | 975 (▲8) | Abandoned | 2 | stale | 1.7y ago | 2.2y | 0 |
| [567-labs/instructor-js](https://github.com/567-labs/instructor-js) | Structured field extraction | TypeScript | MIT | 799 (▲3) | Declining | 7 | stale | 1.5y ago | 2.5y | 0 |
| [docling-project/docling-mcp](https://github.com/docling-project/docling-mcp) | Format-specific / serving | Python | MIT | 683 (▲29) | Mature | 63 | active | 28d ago | 1.3y | 5 |
| [AstraBert/PdfItDown](https://github.com/AstraBert/PdfItDown) | Format-specific / serving | Rust | MIT | 248 (▲16) | Mature | 76 | very active | 4d ago | 1.5y | 2 |
| [JoshData/pdf-redactor](https://github.com/JoshData/pdf-redactor) | Format-specific / serving | Python | CC0-1.0 | 211 (▼1) | Abandoned | 2 | stale | 2.1y ago | 9.7y | 0 |

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

- **[microsoft/markitdown](https://github.com/microsoft/markitdown)** · 165,256★ · Python · Declining  
  Microsoft's lightweight anything→Markdown converter — speed and format coverage over layout fidelity.  
  <sub>topics: langchain, openai, autogen-extension, autogen, markdown, microsoft-office, pdf</sub>
- **[opendatalab/MinerU](https://github.com/opendatalab/MinerU)** · 74,412★ · Python · Mature  
  PDF/Office → LLM-ready markdown/JSON; the reference for complex layouts and CJK documents (MinerU2.5 VLM).  
  <sub>topics: extract-data, layout-analysis, ocr, parser, pdf, pdf-converter, python, document-analysis</sub>
- **[docling-project/docling](https://github.com/docling-project/docling)** · 63,059★ · Python · Mature  
  IBM's document toolkit — TableFormer table structure, PDF/DOCX/PPTX/HTML/audio, first-class LlamaIndex/LangChain integration.  
  <sub>topics: ai, convert, documents, pdf, tables, document-parser, document-parsing, docx</sub>
- **[datalab-to/marker](https://github.com/datalab-to/marker)** · 37,433★ · Python · Mature  
  Fast, accurate PDF → markdown + JSON; GPU-accelerated (Surya models), strong structure fidelity.  
  <sub>topics: —</sub>
- **[Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)** · 15,125★ · HTML · Classic  
  Open-source ETL for 25+ file formats → clean structured elements; the enterprise-pipeline pick.  
  <sub>topics: deep-learning, document-parsing, machine-learning, nlp, ocr, information-retrieval, data-pipelines, ml</sub>
- **[xberg-io/xberg](https://github.com/xberg-io/xberg)** · 8,631★ · Rust · Hot  
  Polyglot document-intelligence framework with a Rust core (ex-Kreuzberg) — 97+ formats, CPU-only, library/CLI/REST/MCP.  
  <sub>topics: text-extraction, document-intelligence, metadata-extraction, pdf-extraction, pdfium, python, rag, table-extraction</sub>
- **[run-llama/semtools](https://github.com/run-llama/semtools)** · 1,831★ · Rust · Declining  
  LlamaIndex's CLI: document parsing + semantic search as composable command-line tools.  
  <sub>topics: cli, embeddings, parser, rust, search, semantic, semantic-search, static-embedding</sub>

### OCR / layout model

_The classic recognition layer: character recognition and layout detection as standalone engines/models, used inside the frameworks above._

- **[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** · 85,345★ · Python · Classic  
  The dominant OCR toolkit (80+ languages) + PP-Structure pipelines; its PaddleOCR-VL models top OmniDocBench.  
  <sub>topics: ocr, chineseocr, pdf2markdown, pp-ocr, pp-structure, document-parsing, document-translation, kie</sub>
- **[tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)** · 75,286★ · C++ · Classic  
  The veteran C++ OCR engine — battle-tested baseline for clean printed scans, zero GPU.  
  <sub>topics: tesseract, tesseract-ocr, ocr, lstm, machine-learning, ocr-engine, hacktoberfest</sub>
- **[opendatalab/DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)** · 2,224★ · Python · Abandoned  
  YOLO-v10-based layout detection — best standalone layout mAP on OmniDocBench component tests.  
  <sub>topics: —</sub>

### VLM document parser

_The disruption: one vision-language model reads the page end-to-end. Compact open models now beat closed generalist VLMs on document parsing benchmarks._

- **[deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)** · 23,562★ · Python · Declining  
  Contexts optical compression — ~10× fewer vision tokens per page at ≥90% decoding accuracy; built for LLM-scale corpora.  
  <sub>topics: —</sub>
- **[allenai/olmocr](https://github.com/allenai/olmocr)** · 19,077★ · Python · Declining  
  AllenAI's toolkit for linearizing PDFs into LLM training data — throughput-oriented, permissively licensed.  
  <sub>topics: —</sub>
- **[getomni-ai/zerox](https://github.com/getomni-ai/zerox)** · 12,242★ · TypeScript · Abandoned  
  OCR by delegation: renders pages and asks a hosted vision model (GPT/Claude/Gemini) — zero local models.  
  <sub>topics: ocr, pdf</sub>
- **[facebookresearch/nougat](https://github.com/facebookresearch/nougat)** · 10,043★ · Python · Abandoned  
  Meta's neural OCR for academic PDFs (math → LaTeX) — historically important, now effectively unmaintained.  
  <sub>topics: —</sub>
- **[bytedance/Dolphin](https://github.com/bytedance/Dolphin)** · 9,031★ · Python · Declining  
  ByteDance's ACL-2025 parser — heterogeneous anchor prompting (layout first, parallel element parsing second).  
  <sub>topics: document-analysis, layout-analysis, ocr, parser, pdf, pdf-converter, pdf-parser, python</sub>
- **[rednote-hilab/dots.ocr](https://github.com/rednote-hilab/dots.ocr)** · 8,996★ · Python · Declining  
  Multilingual layout + parsing in a single compact VLM (~3B); 88.4 on OmniDocBench v1.5.  
  <sub>topics: —</sub>
- **[Yuliang-Liu/MonkeyOCR](https://github.com/Yuliang-Liu/MonkeyOCR)** · 6,598★ · Python · Declining  
  Lightweight structure-recognition-relation model; MonkeyOCR-pro-3B beat Gemini/GPT-4o-class models on OmniDocBench.  
  <sub>topics: —</sub>
- **[deepseek-ai/DeepSeek-OCR-2](https://github.com/deepseek-ai/DeepSeek-OCR-2)** · 3,128★ · Python · Declining  
  Second iteration ('Visual Causal Flow') — 91.1 on OmniDocBench v1.5, ahead of most open VLM parsers.  
  <sub>topics: —</sub>

### Structured field extraction

_Post-parsing: pull typed, schema-validated values (entities, invoice fields, dates) out of the recovered text — with provenance._

- **[google/langextract](https://github.com/google/langextract)** · 37,135★ · Python · Mature  
  Google's library for LLM extraction of structured info with precise source grounding (char-level offsets).  
  <sub>topics: llm, nlp, python, gemini-ai, information-extration, large-language-models, structured-data, gemini</sub>
- **[landing-ai/ade-python](https://github.com/landing-ai/ade-python)** · 1,008★ · Python · Rising  
  LandingAI's Agentic Document Extraction client — schema-driven field extraction from visually complex docs.  
  <sub>topics: —</sub>
- **[567-labs/instructor-js](https://github.com/567-labs/instructor-js)** · 799★ · TypeScript · Declining  
  Schema-first structured outputs for LLMs (instructor's JS port) — the validation layer after parsing.  
  <sub>topics: llm, openai, zod</sub>

### Format-specific / serving

_Utilities and wrappers: format-native readers/writers, redaction, and API/MCP layers that put parsers behind an endpoint._

- **[python-openxml/python-docx](https://github.com/python-openxml/python-docx)** · 5,673★ · Python · Abandoned  
  The standard library for reading and writing Word .docx programmatically.  
  <sub>topics: —</sub>
- **[adithya-s-k/marker-api](https://github.com/adithya-s-k/marker-api)** · 975★ · Python · Abandoned  
  Deployable REST API wrapping marker — PDF→markdown as a service.  
  <sub>topics: fastapi, marker, pdf-converter, pdf-files, pdf-parser, pdf-parsing, api, rest-api</sub>
- **[docling-project/docling-mcp](https://github.com/docling-project/docling-mcp)** · 683★ · Python · Mature  
  Docling exposed as MCP tools — document conversion for agent workflows.  
  <sub>topics: —</sub>
- **[AstraBert/PdfItDown](https://github.com/AstraBert/PdfItDown)** · 248★ · Rust · Mature  
  The inverse direction: convert anything → PDF (normalization before extraction).  
  <sub>topics: csv, docx, html, json, markdown, package, pdf, pdf-conversion</sub>
- **[JoshData/pdf-redactor](https://github.com/JoshData/pdf-redactor)** · 211★ · Python · Abandoned  
  General-purpose PDF text-layer redaction for Python.  
  <sub>topics: —</sub>

## Spotlight: the single-VLM takeover

Two years ago document extraction meant a *pipeline of specialist models* (layout detector → OCR → table model → formula model). The 2025–26 wave collapses that into **one vision-language model per page**:

- **Accuracy**: on OmniDocBench v1.5, open parsers now score 88–95 (PaddleOCR-VL 94.5, DeepSeek-OCR-2 91.1, MinerU2.5 90.7, dots.ocr 88.4) — *above* generalist frontier VLMs on the same benchmark.
- **Size**: the winners are ~3B-parameter models (`dots.ocr`, `MonkeyOCR-pro-3B`, `DeepSeek-OCR`) — self-hostable on a single GPU.
- **Token economics**: `DeepSeek-OCR` reframes OCR as *context compression* — 1,000 text tokens → ~100 vision tokens at ~97% fidelity — which matters more than accuracy when feeding million-page corpora to LLMs.
- **Consequence**: classic engines (`tesseract`) and pipeline frameworks keep the CPU-only and clean-scan niches; everything else is converging on VLMs, with the frameworks (`MinerU`, `marker`, `docling`) absorbing them as backends.

## Graph analysis — how they relate

**Community clustering.** These 26 tools span **12 of the graph's 26 communities**.

- **Community 7** (5): `opendatalab/MinerU`, `opendatalab/DocLayout-YOLO`, `getomni-ai/zerox`, `bytedance/Dolphin`, `adithya-s-k/marker-api`
- **Community 0** (5): `allenai/olmocr`, `rednote-hilab/dots.ocr`, `Yuliang-Liu/MonkeyOCR`, `python-openxml/python-docx`, `JoshData/pdf-redactor`
- **Community 16** (4): `docling-project/docling`, `datalab-to/marker`, `run-llama/semtools`, `docling-project/docling-mcp`
- **Community 11** (2): `xberg-io/xberg`, `tesseract-ocr/tesseract`
- **Community 13** (2): `PaddlePaddle/PaddleOCR`, `facebookresearch/nougat`
- **Community 22** (2): `deepseek-ai/DeepSeek-OCR`, `deepseek-ai/DeepSeek-OCR-2`

**Centrality (PageRank in the full 1,327-repo graph)** — most 'hub-like' extraction tools in your ecosystem:

- `google/langextract` — PageRank 0.0010
- `deepseek-ai/DeepSeek-OCR-2` — PageRank 0.0010
- `opendatalab/MinerU` — PageRank 0.0009
- `datalab-to/marker` — PageRank 0.0009
- `landing-ai/ade-python` — PageRank 0.0008
- `facebookresearch/nougat` — PageRank 0.0007
- `bytedance/Dolphin` — PageRank 0.0007
- `Yuliang-Liu/MonkeyOCR` — PageRank 0.0007
- `run-llama/semtools` — PageRank 0.0007
- `567-labs/instructor-js` — PageRank 0.0007

**Direct links between extraction tools** (top similarity edges where both endpoints are in this report):

- `docling-project/docling-mcp` ⇄ `docling-project/docling` (w=0.712) — authors: github-actions[bot], dolfim-ibm, ceberam
- `deepseek-ai/DeepSeek-OCR-2` ⇄ `deepseek-ai/DeepSeek-OCR` (w=0.550)
- `opendatalab/DocLayout-YOLO` ⇄ `opendatalab/MinerU` (w=0.550)
- `bytedance/Dolphin` ⇄ `opendatalab/MinerU` (w=0.521) — topics: document-analysis, layout-analysis, ocr, parser
- `opendatalab/MinerU` ⇄ `docling-project/docling` (w=0.242) — topics: pdf, pdf-converter, docx, pptx
- `bytedance/Dolphin` ⇄ `getomni-ai/zerox` (w=0.222) — topics: ocr, pdf
- `PaddlePaddle/PaddleOCR` ⇄ `opendatalab/MinerU` (w=0.210) — topics: ocr, ai4science, pdf-extractor-rag, pdf-parser
- `Unstructured-IO/unstructured` ⇄ `docling-project/docling` (w=0.207) — topics: document-parsing, pdf-to-text, pdf, pdf-to-json
- `adithya-s-k/marker-api` ⇄ `bytedance/Dolphin` (w=0.183) — topics: pdf-converter, pdf-parser
- `adithya-s-k/marker-api` ⇄ `opendatalab/MinerU` (w=0.141) — topics: pdf-converter, pdf-parser
- `tesseract-ocr/tesseract` ⇄ `getomni-ai/zerox` (w=0.125) — topics: ocr
- `opendatalab/MinerU` ⇄ `getomni-ai/zerox` (w=0.125) — topics: ocr, pdf
- `getomni-ai/zerox` ⇄ `microsoft/markitdown` (w=0.125) — topics: pdf

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| docling-project/docling | 95 | Mature | very active | 5 | 13% | 194 |
| opendatalab/MinerU | 80 | Mature | very active | 1 | 100% | 179 |
| xberg-io/xberg | 80 | Hot | very active | 1 | 95% | 56 |
| PaddlePaddle/PaddleOCR | 79 | Classic | very active | 2 | 37% | 33 |
| AstraBert/PdfItDown | 76 | Mature | very active | 1 | 99% | 36 |
| Unstructured-IO/unstructured | 69 | Classic | very active | 1 | 57% | 234 |
| google/langextract | 67 | Mature | very active | 1 | 81% | 18 |
| landing-ai/ade-python | 63 | Rising | active | 1 | 57% | 54 |
| docling-project/docling-mcp | 63 | Mature | active | 2 | 30% | 16 |
| datalab-to/marker | 62 | Mature | active | 1 | 67% | 71 |
| tesseract-ocr/tesseract | 61 | Classic | very active | 1 | 77% | 35 |
| microsoft/markitdown | 51 | Declining | active | 1 | 50% | 19 |
| allenai/olmocr | 44 | Declining | slowing | 0 | 0% | 44 |
| Yuliang-Liu/MonkeyOCR | 43 | Declining | slowing | 1 | 100% | 0 |
| run-llama/semtools | 42 | Declining | slowing | 0 | 0% | 17 |
| bytedance/Dolphin | 26 | Declining | slowing | 0 | 0% | 0 |
| rednote-hilab/dots.ocr | 25 | Declining | slowing | 0 | 0% | 0 |
| deepseek-ai/DeepSeek-OCR | 17 | Declining | slowing | 0 | 0% | 0 |
| deepseek-ai/DeepSeek-OCR-2 | 17 | Declining | slowing | 0 | 0% | 0 |
| opendatalab/DocLayout-YOLO | 7 | Abandoned | stale | 0 | 0% | 0 |
| 567-labs/instructor-js | 7 | Declining | stale | 0 | 0% | 18 |
| python-openxml/python-docx | 7 | Abandoned | stale | 0 | 0% | 0 |
| facebookresearch/nougat | 5 | Abandoned | stale | 0 | 0% | 2 |
| getomni-ai/zerox | 3 | Abandoned | stale | 0 | 0% | 9 |
| JoshData/pdf-redactor | 2 | Abandoned | stale | 0 | 0% | 0 |
| adithya-s-k/marker-api | 2 | Abandoned | stale | 0 | 0% | 0 |

Watch items: `nougat` is effectively frozen (use `MinerU`/`marker` instead); `zerox` reads as abandoned in this snapshot — its hosted-VLM pattern is trivial to reimplement if it stays stale; `marker-api` and `pdf-redactor` are stale single-maintainer wrappers — pin versions or vendor them.

## Adjacent (deliberately not listed as extraction tools)

- **Stirling-Tools/Stirling-PDF** (86,955★) — PDF *manipulation* app (edit/merge/sign, OCR jobs via OCRmyPDF) — a toolbox, not an extraction framework
- **run-llama/llama_index** (50,813★) — positions itself as a 'document agent and OCR platform', but it's covered in the *RAG tooling* report
- **firecrawl/firecrawl** (150,087★) — extraction for the *web* (scraping/crawling), not documents
- **microsoft/OmniParser** (25,059★) — parses GUI *screenshots* for computer-use agents, not documents
- **VectifyAI/PageIndex** (33,980★) — document *retrieval* (vectorless RAG) — see the RAG tooling report
- **tjmlabs/ColiVara** (1,483★) — visual document *retrieval* (ColPali-style), not extraction
- **kba/awesome-ocr** (3,111★) — link collection, not a tool
- **tk04/Marker** (1,189★) — markdown *editor* that happens to share marker's name — no relation

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json` for all repo metrics and graph structure. No API calls at generation time; fully reproducible.
- **Selection**: keyword scan (pdf / ocr / document / layout / extract / parsing / docx / markdown-convert) + manual curation into pipeline stages. Retrieval, web scraping, GUI parsing, and PDF-editing apps were routed to adjacent reports or excluded (see above).
- **Task rankings** additionally cite external benchmark evidence gathered 2026-07: [OmniDocBench](https://github.com/opendatalab/OmniDocBench) v1.5 composite scores, the [opendataloader-bench 200-PDF comparison](https://pdfmux.com/blog/pdfmux-vs-pymupdf-vs-marker-vs-docling/), and vendor papers (MinerU2.5, dots.ocr, DeepSeek-OCR, Dolphin). Benchmark numbers are point-in-time and partly vendor-reported — treat rankings as defaults, not verdicts.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity; benchmark citations are frozen text and need manual review on major model releases.

<sub>Tools covered: 26 · Snapshot: 2026-07-13T08:42:30.177Z</sub>
