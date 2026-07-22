# Document Extraction Frameworks — Landscape & Task Rankings

> Derived from **kaiser-data**'s 1,350 starred repos (snapshot `2026-07-20T08:33:57.852Z`), cross-referenced with the repo-similarity graph (1,350 nodes / 4,379 edges, 28 communities). Task rankings are additionally backed by external benchmarks (OmniDocBench, opendataloader-bench) — see Methodology.
>
> Generated 2026-07-22 by `scripts/reports/document_extraction.py` (regenerate any time — no API cost).

![Top tools by stars](assets/document-extraction-top-tools.svg)

![Tools per category](assets/document-extraction-categories.svg)


## Executive summary

- **26 document-extraction tools** in your stars (**673,054★** combined), organized along the extraction pipeline:
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
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Conversion framework | Python | MIT | 167,484 (▲167) | Declining | 51 | active | 3d ago | 1.7y | 2 |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | OCR / layout model | Python | Apache-2.0 | 85,841 (▲37) | Classic | 85 | very active | 5d ago | 6.2y | 18 |
| [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | OCR / layout model | C++ | Apache-2.0 | 75,449 (▲3) | Classic | 62 | very active | 1d ago | 11.9y | 7 |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | Conversion framework | Python | NOASSERTION | 75,161 (▲54) | Mature | 80 | very active | 3d ago | 2.4y | 1 |
| [docling-project/docling](https://github.com/docling-project/docling) | Conversion framework | Python | MIT | 63,487 (▲26) | Mature | 95 | very active | 0d ago | 2.0y | 33 |
| [datalab-to/marker](https://github.com/datalab-to/marker) | Conversion framework | Python | GPL-3.0 | 37,662 (▲7) | Mature | 61 | active | 13d ago | 2.7y | 2 |
| [google/langextract](https://github.com/google/langextract) | Structured field extraction | Python | Apache-2.0 | 37,591 (▲59) | Mature | 65 | active | 18d ago | 1.0y | 3 |
| [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) | VLM document parser | Python | MIT | 23,613 (▲4) | Declining | 17 | slowing | 5mo ago | 9mo | 0 |
| [allenai/olmocr](https://github.com/allenai/olmocr) | VLM document parser | Python | Apache-2.0 | 19,128 (▲6) | Declining | 43 | slowing | 3mo ago | 1.8y | 0 |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | Conversion framework | HTML | Apache-2.0 | 15,165 (▲4) | Classic | 69 | very active | 0d ago | 3.8y | 9 |
| [getomni-ai/zerox](https://github.com/getomni-ai/zerox) | VLM document parser | TypeScript | MIT | 12,259 (▲2) | Abandoned | 3 | stale | 1.2y ago | 2.0y | 0 |
| [facebookresearch/nougat](https://github.com/facebookresearch/nougat) | VLM document parser | Python | MIT | 10,047 | Abandoned | 5 | stale | 1.4y ago | 3.1y | 0 |
| [bytedance/Dolphin](https://github.com/bytedance/Dolphin) | VLM document parser | Python | NOASSERTION | 9,035 | Declining | 25 | slowing | 3mo ago | 1.2y | 0 |
| [rednote-hilab/dots.ocr](https://github.com/rednote-hilab/dots.ocr) | VLM document parser | Python | MIT | 9,015 (▲1) | Declining | 25 | slowing | 3mo ago | 11mo | 0 |
| [xberg-io/xberg](https://github.com/xberg-io/xberg) | Conversion framework | Rust | MIT | 8,675 (▲3) | Hot | 80 | very active | 0d ago | 1.5y | 4 |
| [Yuliang-Liu/MonkeyOCR](https://github.com/Yuliang-Liu/MonkeyOCR) | VLM document parser | Python | Apache-2.0 | 6,604 (▲1) | Mature | 50 | active | 1d ago | 1.1y | 2 |
| [python-openxml/python-docx](https://github.com/python-openxml/python-docx) | Format-specific / serving | Python | MIT | 5,682 (▲1) | Abandoned | 7 | stale | 1.1y ago | 12.8y | 0 |
| [deepseek-ai/DeepSeek-OCR-2](https://github.com/deepseek-ai/DeepSeek-OCR-2) | VLM document parser | Python | Apache-2.0 | 3,151 (▲6) | Declining | 16 | slowing | 5mo ago | 5mo | 0 |
| [opendatalab/DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO) | OCR / layout model | Python | AGPL-3.0 | 2,231 | Abandoned | 7 | stale | 1.3y ago | 1.8y | 0 |
| [run-llama/semtools](https://github.com/run-llama/semtools) | Conversion framework | Rust | MIT | 1,837 | Declining | 41 | slowing | 4mo ago | 11mo | 0 |
| [landing-ai/ade-python](https://github.com/landing-ai/ade-python) | Structured field extraction | Python | Apache-2.0 | 1,013 | Rising | 65 | very active | 0d ago | 10mo | 7 |
| [adithya-s-k/marker-api](https://github.com/adithya-s-k/marker-api) | Format-specific / serving | Python | GPL-3.0 | 978 | Abandoned | 2 | stale | 1.8y ago | 2.2y | 0 |
| [567-labs/instructor-js](https://github.com/567-labs/instructor-js) | Structured field extraction | TypeScript | MIT | 799 | Declining | 7 | stale | 1.5y ago | 2.5y | 0 |
| [docling-project/docling-mcp](https://github.com/docling-project/docling-mcp) | Format-specific / serving | Python | MIT | 689 | Mature | 66 | active | 4d ago | 1.4y | 6 |
| [AstraBert/PdfItDown](https://github.com/AstraBert/PdfItDown) | Format-specific / serving | Rust | MIT | 248 | Mature | 76 | very active | 11d ago | 1.6y | 2 |
| [JoshData/pdf-redactor](https://github.com/JoshData/pdf-redactor) | Format-specific / serving | Python | CC0-1.0 | 210 | Abandoned | 2 | stale | 2.1y ago | 9.8y | 0 |

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

- **[microsoft/markitdown](https://github.com/microsoft/markitdown)** · 167,484★ · Python · Declining  
  Microsoft's lightweight anything→Markdown converter — speed and format coverage over layout fidelity.  
  <sub>topics: langchain, openai, autogen-extension, autogen, markdown, microsoft-office, pdf</sub>
- **[opendatalab/MinerU](https://github.com/opendatalab/MinerU)** · 75,161★ · Python · Mature  
  PDF/Office → LLM-ready markdown/JSON; the reference for complex layouts and CJK documents (MinerU2.5 VLM).  
  <sub>topics: extract-data, layout-analysis, ocr, parser, pdf, pdf-converter, python, document-analysis</sub>
- **[docling-project/docling](https://github.com/docling-project/docling)** · 63,487★ · Python · Mature  
  IBM's document toolkit — TableFormer table structure, PDF/DOCX/PPTX/HTML/audio, first-class LlamaIndex/LangChain integration.  
  <sub>topics: ai, convert, documents, pdf, tables, document-parser, document-parsing, docx</sub>
- **[datalab-to/marker](https://github.com/datalab-to/marker)** · 37,662★ · Python · Mature  
  Fast, accurate PDF → markdown + JSON; GPU-accelerated (Surya models), strong structure fidelity.  
  <sub>topics: —</sub>
- **[Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)** · 15,165★ · HTML · Classic  
  Open-source ETL for 25+ file formats → clean structured elements; the enterprise-pipeline pick.  
  <sub>topics: deep-learning, document-parsing, machine-learning, nlp, ocr, information-retrieval, data-pipelines, ml</sub>
- **[xberg-io/xberg](https://github.com/xberg-io/xberg)** · 8,675★ · Rust · Hot  
  Polyglot document-intelligence framework with a Rust core (ex-Kreuzberg) — 97+ formats, CPU-only, library/CLI/REST/MCP.  
  <sub>topics: text-extraction, document-intelligence, metadata-extraction, pdf-extraction, pdfium, python, rag, table-extraction</sub>
- **[run-llama/semtools](https://github.com/run-llama/semtools)** · 1,837★ · Rust · Declining  
  LlamaIndex's CLI: document parsing + semantic search as composable command-line tools.  
  <sub>topics: cli, embeddings, parser, rust, search, semantic, semantic-search, static-embedding</sub>

### OCR / layout model

_The classic recognition layer: character recognition and layout detection as standalone engines/models, used inside the frameworks above._

- **[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** · 85,841★ · Python · Classic  
  The dominant OCR toolkit (80+ languages) + PP-Structure pipelines; its PaddleOCR-VL models top OmniDocBench.  
  <sub>topics: ocr, chineseocr, pdf2markdown, pp-ocr, pp-structure, document-parsing, document-translation, kie</sub>
- **[tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)** · 75,449★ · C++ · Classic  
  The veteran C++ OCR engine — battle-tested baseline for clean printed scans, zero GPU.  
  <sub>topics: tesseract, tesseract-ocr, ocr, lstm, machine-learning, ocr-engine, hacktoberfest</sub>
- **[opendatalab/DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)** · 2,231★ · Python · Abandoned  
  YOLO-v10-based layout detection — best standalone layout mAP on OmniDocBench component tests.  
  <sub>topics: —</sub>

### VLM document parser

_The disruption: one vision-language model reads the page end-to-end. Compact open models now beat closed generalist VLMs on document parsing benchmarks._

- **[deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)** · 23,613★ · Python · Declining  
  Contexts optical compression — ~10× fewer vision tokens per page at ≥90% decoding accuracy; built for LLM-scale corpora.  
  <sub>topics: —</sub>
- **[allenai/olmocr](https://github.com/allenai/olmocr)** · 19,128★ · Python · Declining  
  AllenAI's toolkit for linearizing PDFs into LLM training data — throughput-oriented, permissively licensed.  
  <sub>topics: —</sub>
- **[getomni-ai/zerox](https://github.com/getomni-ai/zerox)** · 12,259★ · TypeScript · Abandoned  
  OCR by delegation: renders pages and asks a hosted vision model (GPT/Claude/Gemini) — zero local models.  
  <sub>topics: ocr, pdf</sub>
- **[facebookresearch/nougat](https://github.com/facebookresearch/nougat)** · 10,047★ · Python · Abandoned  
  Meta's neural OCR for academic PDFs (math → LaTeX) — historically important, now effectively unmaintained.  
  <sub>topics: —</sub>
- **[bytedance/Dolphin](https://github.com/bytedance/Dolphin)** · 9,035★ · Python · Declining  
  ByteDance's ACL-2025 parser — heterogeneous anchor prompting (layout first, parallel element parsing second).  
  <sub>topics: document-analysis, layout-analysis, ocr, parser, pdf, pdf-converter, pdf-parser, python</sub>
- **[rednote-hilab/dots.ocr](https://github.com/rednote-hilab/dots.ocr)** · 9,015★ · Python · Declining  
  Multilingual layout + parsing in a single compact VLM (~3B); 88.4 on OmniDocBench v1.5.  
  <sub>topics: —</sub>
- **[Yuliang-Liu/MonkeyOCR](https://github.com/Yuliang-Liu/MonkeyOCR)** · 6,604★ · Python · Mature  
  Lightweight structure-recognition-relation model; MonkeyOCR-pro-3B beat Gemini/GPT-4o-class models on OmniDocBench.  
  <sub>topics: —</sub>
- **[deepseek-ai/DeepSeek-OCR-2](https://github.com/deepseek-ai/DeepSeek-OCR-2)** · 3,151★ · Python · Declining  
  Second iteration ('Visual Causal Flow') — 91.1 on OmniDocBench v1.5, ahead of most open VLM parsers.  
  <sub>topics: —</sub>

### Structured field extraction

_Post-parsing: pull typed, schema-validated values (entities, invoice fields, dates) out of the recovered text — with provenance._

- **[google/langextract](https://github.com/google/langextract)** · 37,591★ · Python · Mature  
  Google's library for LLM extraction of structured info with precise source grounding (char-level offsets).  
  <sub>topics: llm, nlp, python, gemini-ai, information-extration, large-language-models, structured-data, gemini</sub>
- **[landing-ai/ade-python](https://github.com/landing-ai/ade-python)** · 1,013★ · Python · Rising  
  LandingAI's Agentic Document Extraction client — schema-driven field extraction from visually complex docs.  
  <sub>topics: —</sub>
- **[567-labs/instructor-js](https://github.com/567-labs/instructor-js)** · 799★ · TypeScript · Declining  
  Schema-first structured outputs for LLMs (instructor's JS port) — the validation layer after parsing.  
  <sub>topics: llm, openai, zod</sub>

### Format-specific / serving

_Utilities and wrappers: format-native readers/writers, redaction, and API/MCP layers that put parsers behind an endpoint._

- **[python-openxml/python-docx](https://github.com/python-openxml/python-docx)** · 5,682★ · Python · Abandoned  
  The standard library for reading and writing Word .docx programmatically.  
  <sub>topics: —</sub>
- **[adithya-s-k/marker-api](https://github.com/adithya-s-k/marker-api)** · 978★ · Python · Abandoned  
  Deployable REST API wrapping marker — PDF→markdown as a service.  
  <sub>topics: fastapi, marker, pdf-converter, pdf-files, pdf-parser, pdf-parsing, api, rest-api</sub>
- **[docling-project/docling-mcp](https://github.com/docling-project/docling-mcp)** · 689★ · Python · Mature  
  Docling exposed as MCP tools — document conversion for agent workflows.  
  <sub>topics: —</sub>
- **[AstraBert/PdfItDown](https://github.com/AstraBert/PdfItDown)** · 248★ · Rust · Mature  
  The inverse direction: convert anything → PDF (normalization before extraction).  
  <sub>topics: csv, docx, html, json, markdown, package, pdf, pdf-conversion</sub>
- **[JoshData/pdf-redactor](https://github.com/JoshData/pdf-redactor)** · 210★ · Python · Abandoned  
  General-purpose PDF text-layer redaction for Python.  
  <sub>topics: —</sub>

## Spotlight: the single-VLM takeover

Two years ago document extraction meant a *pipeline of specialist models* (layout detector → OCR → table model → formula model). The 2025–26 wave collapses that into **one vision-language model per page**:

- **Accuracy**: on OmniDocBench v1.5, open parsers now score 88–95 (PaddleOCR-VL 94.5, DeepSeek-OCR-2 91.1, MinerU2.5 90.7, dots.ocr 88.4) — *above* generalist frontier VLMs on the same benchmark.
- **Size**: the winners are ~3B-parameter models (`dots.ocr`, `MonkeyOCR-pro-3B`, `DeepSeek-OCR`) — self-hostable on a single GPU.
- **Token economics**: `DeepSeek-OCR` reframes OCR as *context compression* — 1,000 text tokens → ~100 vision tokens at ~97% fidelity — which matters more than accuracy when feeding million-page corpora to LLMs.
- **Consequence**: classic engines (`tesseract`) and pipeline frameworks keep the CPU-only and clean-scan niches; everything else is converging on VLMs, with the frameworks (`MinerU`, `marker`, `docling`) absorbing them as backends.

## Graph analysis — how they relate

**Community clustering.** These 26 tools span **10 of the graph's 28 communities**.

- **Community 17** (6): `opendatalab/MinerU`, `opendatalab/DocLayout-YOLO`, `getomni-ai/zerox`, `bytedance/Dolphin`, `google/langextract`, `adithya-s-k/marker-api`
- **Community 2** (5): `docling-project/docling`, `datalab-to/marker`, `run-llama/semtools`, `landing-ai/ade-python`, `docling-project/docling-mcp`
- **Community 0** (5): `allenai/olmocr`, `rednote-hilab/dots.ocr`, `Yuliang-Liu/MonkeyOCR`, `python-openxml/python-docx`, `JoshData/pdf-redactor`
- **Community 21** (2): `microsoft/markitdown`, `tesseract-ocr/tesseract`
- **Community 16** (2): `PaddlePaddle/PaddleOCR`, `facebookresearch/nougat`
- **Community 25** (2): `deepseek-ai/DeepSeek-OCR`, `deepseek-ai/DeepSeek-OCR-2`

**Centrality (PageRank in the full 1,350-repo graph)** — most 'hub-like' extraction tools in your ecosystem:

- `datalab-to/marker` — PageRank 0.0011
- `Yuliang-Liu/MonkeyOCR` — PageRank 0.0011
- `deepseek-ai/DeepSeek-OCR-2` — PageRank 0.0010
- `opendatalab/MinerU` — PageRank 0.0009
- `google/langextract` — PageRank 0.0009
- `bytedance/Dolphin` — PageRank 0.0008
- `facebookresearch/nougat` — PageRank 0.0007
- `landing-ai/ade-python` — PageRank 0.0007
- `PaddlePaddle/PaddleOCR` — PageRank 0.0007
- `deepseek-ai/DeepSeek-OCR` — PageRank 0.0007

**Direct links between extraction tools** (top similarity edges where both endpoints are in this report):

- `docling-project/docling-mcp` ⇄ `docling-project/docling` (w=0.717) — authors: github-actions[bot], dolfim-ibm, ceberam
- `deepseek-ai/DeepSeek-OCR-2` ⇄ `deepseek-ai/DeepSeek-OCR` (w=0.550)
- `opendatalab/DocLayout-YOLO` ⇄ `opendatalab/MinerU` (w=0.550)
- `bytedance/Dolphin` ⇄ `opendatalab/MinerU` (w=0.521) — topics: document-analysis, layout-analysis, ocr, parser
- `datalab-to/marker` ⇄ `docling-project/docling-mcp` (w=0.336) — authors: github-actions[bot]
- `landing-ai/ade-python` ⇄ `datalab-to/marker` (w=0.300) — authors: github-actions[bot]
- `opendatalab/MinerU` ⇄ `docling-project/docling` (w=0.242) — topics: pdf, pdf-converter, docx, pptx
- `bytedance/Dolphin` ⇄ `getomni-ai/zerox` (w=0.222) — topics: ocr, pdf
- `PaddlePaddle/PaddleOCR` ⇄ `opendatalab/MinerU` (w=0.210) — topics: ocr, ai4science, pdf-extractor-rag, pdf-parser
- `Unstructured-IO/unstructured` ⇄ `docling-project/docling` (w=0.207) — topics: document-parsing, pdf-to-text, pdf, pdf-to-json
- `adithya-s-k/marker-api` ⇄ `bytedance/Dolphin` (w=0.183) — topics: pdf-converter, pdf-parser
- `PaddlePaddle/PaddleOCR` ⇄ `bytedance/Dolphin` (w=0.150) — topics: ocr, pdf-parser
- `adithya-s-k/marker-api` ⇄ `opendatalab/MinerU` (w=0.141) — topics: pdf-converter, pdf-parser
- `tesseract-ocr/tesseract` ⇄ `getomni-ai/zerox` (w=0.125) — topics: ocr
- `opendatalab/MinerU` ⇄ `getomni-ai/zerox` (w=0.125) — topics: ocr, pdf
- …and 1 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| docling-project/docling | 95 | Mature | very active | 5 | 13% | 195 |
| PaddlePaddle/PaddleOCR | 85 | Classic | very active | 3 | 36% | 33 |
| opendatalab/MinerU | 80 | Mature | very active | 1 | 100% | 181 |
| xberg-io/xberg | 80 | Hot | very active | 1 | 75% | 61 |
| AstraBert/PdfItDown | 76 | Mature | very active | 1 | 99% | 36 |
| Unstructured-IO/unstructured | 69 | Classic | very active | 1 | 52% | 234 |
| docling-project/docling-mcp | 66 | Mature | active | 2 | 25% | 16 |
| google/langextract | 65 | Mature | active | 1 | 89% | 18 |
| landing-ai/ade-python | 65 | Rising | very active | 1 | 55% | 56 |
| tesseract-ocr/tesseract | 62 | Classic | very active | 1 | 80% | 35 |
| datalab-to/marker | 61 | Mature | active | 1 | 67% | 71 |
| microsoft/markitdown | 51 | Declining | active | 1 | 50% | 19 |
| Yuliang-Liu/MonkeyOCR | 50 | Mature | active | 1 | 60% | 0 |
| allenai/olmocr | 43 | Declining | slowing | 0 | 0% | 44 |
| run-llama/semtools | 41 | Declining | slowing | 0 | 0% | 17 |
| bytedance/Dolphin | 25 | Declining | slowing | 0 | 0% | 0 |
| rednote-hilab/dots.ocr | 25 | Declining | slowing | 0 | 0% | 0 |
| deepseek-ai/DeepSeek-OCR | 17 | Declining | slowing | 0 | 0% | 0 |
| deepseek-ai/DeepSeek-OCR-2 | 16 | Declining | slowing | 0 | 0% | 0 |
| opendatalab/DocLayout-YOLO | 7 | Abandoned | stale | 0 | 0% | 0 |
| 567-labs/instructor-js | 7 | Declining | stale | 0 | 0% | 18 |
| python-openxml/python-docx | 7 | Abandoned | stale | 0 | 0% | 0 |
| facebookresearch/nougat | 5 | Abandoned | stale | 0 | 0% | 2 |
| getomni-ai/zerox | 3 | Abandoned | stale | 0 | 0% | 9 |
| JoshData/pdf-redactor | 2 | Abandoned | stale | 0 | 0% | 0 |
| adithya-s-k/marker-api | 2 | Abandoned | stale | 0 | 0% | 0 |

Watch items: `nougat` is effectively frozen (use `MinerU`/`marker` instead); `zerox` reads as abandoned in this snapshot — its hosted-VLM pattern is trivial to reimplement if it stays stale; `marker-api` and `pdf-redactor` are stale single-maintainer wrappers — pin versions or vendor them.

## Adjacent (deliberately not listed as extraction tools)

- **Stirling-Tools/Stirling-PDF** (87,476★) — PDF *manipulation* app (edit/merge/sign, OCR jobs via OCRmyPDF) — a toolbox, not an extraction framework
- **run-llama/llama_index** (50,953★) — positions itself as a 'document agent and OCR platform', but it's covered in the *RAG tooling* report
- **firecrawl/firecrawl** (153,281★) — extraction for the *web* (scraping/crawling), not documents
- **microsoft/OmniParser** (25,178★) — parses GUI *screenshots* for computer-use agents, not documents
- **VectifyAI/PageIndex** (34,121★) — document *retrieval* (vectorless RAG) — see the RAG tooling report
- **tjmlabs/ColiVara** (1,483★) — visual document *retrieval* (ColPali-style), not extraction
- **kba/awesome-ocr** (3,111★) — link collection, not a tool
- **tk04/Marker** (1,188★) — markdown *editor* that happens to share marker's name — no relation

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json` for all repo metrics and graph structure. No API calls at generation time; fully reproducible.
- **Selection**: keyword scan (pdf / ocr / document / layout / extract / parsing / docx / markdown-convert) + manual curation into pipeline stages. Retrieval, web scraping, GUI parsing, and PDF-editing apps were routed to adjacent reports or excluded (see above).
- **Task rankings** additionally cite external benchmark evidence gathered 2026-07: [OmniDocBench](https://github.com/opendatalab/OmniDocBench) v1.5 composite scores, the [opendataloader-bench 200-PDF comparison](https://pdfmux.com/blog/pdfmux-vs-pymupdf-vs-marker-vs-docling/), and vendor papers (MinerU2.5, dots.ocr, DeepSeek-OCR, Dolphin). Benchmark numbers are point-in-time and partly vendor-reported — treat rankings as defaults, not verdicts.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity; benchmark citations are frozen text and need manual review on major model releases.

<sub>Tools covered: 26 · Snapshot: 2026-07-20T08:33:57.852Z</sub>
