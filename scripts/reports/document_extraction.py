#!/usr/bin/env python3
"""
Generate a landscape report on document-extraction frameworks found in the
starred-repos dataset: end-to-end converters, OCR/layout engines, VLM document
parsers, LLM field extractors, and format-specific utilities — compared and
ranked per task, with external benchmark evidence (OmniDocBench,
opendataloader-bench) cited in the rankings.

Inputs:
  data/classified.json
  public/data/graph.json

Output:
  reports/document-extraction.md   (+ reports/document-extraction.meta.json)

Run: python3 scripts/reports/document_extraction.py
"""
import json
import os
from datetime import datetime, timezone

from lib import fmt_stars, CLASSIFIED, GRAPH, fmt_int, days_to_human, activity_label, make_node_for

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "document-extraction"
TITLE = "Document Extraction Frameworks — Landscape & Task Rankings"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy --------------------------------------------------------
TAXONOMY = {
    # End-to-end conversion frameworks
    "microsoft/markitdown": ("Conversion framework", "Microsoft's lightweight anything→Markdown converter — speed and format coverage over layout fidelity."),
    "opendatalab/MinerU": ("Conversion framework", "PDF/Office → LLM-ready markdown/JSON; the reference for complex layouts and CJK documents (MinerU2.5 VLM)."),
    "docling-project/docling": ("Conversion framework", "IBM's document toolkit — TableFormer table structure, PDF/DOCX/PPTX/HTML/audio, first-class LlamaIndex/LangChain integration."),
    "datalab-to/marker": ("Conversion framework", "Fast, accurate PDF → markdown + JSON; GPU-accelerated (Surya models), strong structure fidelity."),
    "Unstructured-IO/unstructured": ("Conversion framework", "Open-source ETL for 25+ file formats → clean structured elements; the enterprise-pipeline pick."),
    "xberg-io/xberg": ("Conversion framework", "Polyglot document-intelligence framework with a Rust core (ex-Kreuzberg) — 97+ formats, CPU-only, library/CLI/REST/MCP."),
    "run-llama/semtools": ("Conversion framework", "LlamaIndex's CLI: document parsing + semantic search as composable command-line tools."),

    # OCR & layout models (classic, pre-VLM)
    "PaddlePaddle/PaddleOCR": ("OCR / layout model", "The dominant OCR toolkit (80+ languages) + PP-Structure pipelines; its PaddleOCR-VL models top OmniDocBench."),
    "tesseract-ocr/tesseract": ("OCR / layout model", "The veteran C++ OCR engine — battle-tested baseline for clean printed scans, zero GPU."),
    "opendatalab/DocLayout-YOLO": ("OCR / layout model", "YOLO-v10-based layout detection — best standalone layout mAP on OmniDocBench component tests."),

    # VLM document parsers
    "deepseek-ai/DeepSeek-OCR": ("VLM document parser", "Contexts optical compression — ~10× fewer vision tokens per page at ≥90% decoding accuracy; built for LLM-scale corpora."),
    "deepseek-ai/DeepSeek-OCR-2": ("VLM document parser", "Second iteration ('Visual Causal Flow') — 91.1 on OmniDocBench v1.5, ahead of most open VLM parsers."),
    "allenai/olmocr": ("VLM document parser", "AllenAI's toolkit for linearizing PDFs into LLM training data — throughput-oriented, permissively licensed."),
    "getomni-ai/zerox": ("VLM document parser", "OCR by delegation: renders pages and asks a hosted vision model (GPT/Claude/Gemini) — zero local models."),
    "facebookresearch/nougat": ("VLM document parser", "Meta's neural OCR for academic PDFs (math → LaTeX) — historically important, now effectively unmaintained."),
    "bytedance/Dolphin": ("VLM document parser", "ByteDance's ACL-2025 parser — heterogeneous anchor prompting (layout first, parallel element parsing second)."),
    "rednote-hilab/dots.ocr": ("VLM document parser", "Multilingual layout + parsing in a single compact VLM (~3B); 88.4 on OmniDocBench v1.5."),
    "Yuliang-Liu/MonkeyOCR": ("VLM document parser", "Lightweight structure-recognition-relation model; MonkeyOCR-pro-3B beat Gemini/GPT-4o-class models on OmniDocBench."),

    # Structured / field extraction (LLM-driven)
    "google/langextract": ("Structured field extraction", "Google's library for LLM extraction of structured info with precise source grounding (char-level offsets)."),
    "landing-ai/ade-python": ("Structured field extraction", "LandingAI's Agentic Document Extraction client — schema-driven field extraction from visually complex docs."),
    "567-labs/instructor-js": ("Structured field extraction", "Schema-first structured outputs for LLMs (instructor's JS port) — the validation layer after parsing."),

    # Format-specific & serving
    "python-openxml/python-docx": ("Format-specific / serving", "The standard library for reading and writing Word .docx programmatically."),
    "JoshData/pdf-redactor": ("Format-specific / serving", "General-purpose PDF text-layer redaction for Python."),
    "AstraBert/PdfItDown": ("Format-specific / serving", "The inverse direction: convert anything → PDF (normalization before extraction)."),
    "adithya-s-k/marker-api": ("Format-specific / serving", "Deployable REST API wrapping marker — PDF→markdown as a service."),
    "docling-project/docling-mcp": ("Format-specific / serving", "Docling exposed as MCP tools — document conversion for agent workflows."),
}

# Adjacent but deliberately excluded (kept honest in the report)
ADJACENT = [
    ("Stirling-Tools/Stirling-PDF", "PDF *manipulation* app (edit/merge/sign, OCR jobs via OCRmyPDF) — a toolbox, not an extraction framework"),
    ("run-llama/llama_index", "positions itself as a 'document agent and OCR platform', but it's covered in the *RAG tooling* report"),
    ("firecrawl/firecrawl", "extraction for the *web* (scraping/crawling), not documents"),
    ("microsoft/OmniParser", "parses GUI *screenshots* for computer-use agents, not documents"),
    ("VectifyAI/PageIndex", "document *retrieval* (vectorless RAG) — see the RAG tooling report"),
    ("tjmlabs/ColiVara", "visual document *retrieval* (ColPali-style), not extraction"),
    ("kba/awesome-ocr", "link collection, not a tool"),
    ("tk04/Marker", "markdown *editor* that happens to share marker's name — no relation"),
]

# Task-ranked picks: (task, [(repo, note) x3], evidence)
TASK_RANKINGS = [
    ("PDF → Markdown for RAG ingestion (general)",
     [("docling-project/docling", "best accuracy of the free frameworks"),
      ("datalab-to/marker", "close second, faster with a GPU"),
      ("opendatalab/MinerU", "strong but heavier")],
     "opendataloader-bench (200 PDFs): docling 0.877 > marker 0.861 > MinerU 0.831."),
    ("Complex layouts, CJK & multilingual docs",
     [("opendatalab/MinerU", "nothing else close for Chinese/Japanese/Korean layout"),
      ("rednote-hilab/dots.ocr", "one compact VLM, 100+ languages"),
      ("PaddlePaddle/PaddleOCR", "PaddleOCR-VL tops OmniDocBench composite")],
     "OmniDocBench v1.5: PaddleOCR-VL 94.5, MinerU2.5 90.7, dots.ocr 88.4."),
    ("Tables & financial documents",
     [("docling-project/docling", "TableFormer — the table-structure specialist"),
      ("opendatalab/MinerU", "robust table + layout models"),
      ("datalab-to/marker", "good table fidelity, JSON output")],
     "Docling is the consensus pick when documents are table-heavy."),
    ("Scientific papers & formulas",
     [("opendatalab/MinerU", "formula → LaTeX built in"),
      ("datalab-to/marker", "strong math handling via Surya"),
      ("facebookresearch/nougat", "the pioneer — only for legacy pipelines")],
     "Nougat defined the task but is unmaintained; MinerU/marker superseded it."),
    ("Scanned documents & handwriting",
     [("deepseek-ai/DeepSeek-OCR", "VLM robustness + handwriting"),
      ("PaddlePaddle/PaddleOCR", "classic pick, 80+ languages"),
      ("tesseract-ocr/tesseract", "fine for clean printed scans only")],
     "VLM parsers degrade gracefully on noise where classic OCR breaks."),
    ("Office documents (DOCX/PPTX/XLSX) at speed",
     [("microsoft/markitdown", "instant, dependency-light"),
      ("xberg-io/xberg", "Rust-core speed, 97+ formats, no GPU"),
      ("docling-project/docling", "when you also need layout fidelity")],
     "Native-format parsing needs no vision models — lightweight tools win."),
    ("Enterprise ETL across many formats",
     [("Unstructured-IO/unstructured", "25+ formats, chunking, connectors"),
      ("xberg-io/xberg", "self-hosted polyglot core, REST/MCP"),
      ("docling-project/docling", "IBM backing, growing connector set")],
     "Pick by ops model: managed pipeline vs. embedded library."),
    ("Structured field extraction (invoices, entities, forms)",
     [("google/langextract", "grounded extraction with source offsets"),
      ("getomni-ai/zerox", "simplest path via hosted vision models"),
      ("landing-ai/ade-python", "schema-driven agentic extraction")],
     "Parse-then-extract beats end-to-end when you need auditable provenance."),
    ("Building LLM training corpora at scale",
     [("allenai/olmocr", "purpose-built for dataset linearization"),
      ("deepseek-ai/DeepSeek-OCR", "10× token compression cuts corpus cost"),
      ("opendatalab/MinerU", "the OpenDataLab production pipeline")],
     "Throughput and token economics dominate accuracy deltas at corpus scale."),
    ("Agent / CLI integration",
     [("docling-project/docling-mcp", "document conversion as MCP tools"),
      ("run-llama/semtools", "parse + semantic search on the command line"),
      ("adithya-s-k/marker-api", "marker behind a REST endpoint")],
     "Serving wrappers matter more than parser choice for agent workflows."),
]

# ---- Load --------------------------------------------------------------------
with open(CLASSIFIED) as f:
    cl = json.load(f)
with open(GRAPH) as f:
    gr = json.load(f)

by_name = {r["full_name"]: r for r in cl["repos"]}
nodes_by_id = {n["id"]: n for n in gr["nodes"]}
name_to_nodeid = {n["full_name"]: n["id"] for n in gr["nodes"]}

sel_names = list(TAXONOMY.keys())
sel_node_ids = {name_to_nodeid[n] for n in sel_names if n in name_to_nodeid}
inter_edges = [l for l in gr["links"]
               if l["source"] in sel_node_ids and l["target"] in sel_node_ids]

node_for = make_node_for(nodes_by_id, name_to_nodeid)

# ---- Build -------------------------------------------------------------------
gen = cl.get("generatedAt", "")
user = cl.get("username", "")
lines = []
A = lines.append

A(f"# {TITLE}")
A("")
A(f"> Derived from **{user}**'s {fmt_int(cl['total'])} starred repos "
  f"(snapshot `{gen}`), cross-referenced with the repo-similarity graph "
  f"({fmt_int(len(gr['nodes']))} nodes / {fmt_int(len(gr['links']))} edges, "
  f"{len(gr['communities'])} communities). Task rankings are additionally "
  f"backed by external benchmarks (OmniDocBench, opendataloader-bench) — "
  f"see Methodology.")
A(">")
A(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/document_extraction.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)
order = ["Conversion framework", "OCR / layout model", "VLM document parser",
         "Structured field extraction", "Format-specific / serving"]

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} document-extraction tools** in your stars "
  f"(**{fmt_int(total_stars)}★** combined), organized along the extraction pipeline:")
for c in order:
    if cats.get(c):
        A(f"  - **{c}** ({len(cats[c])}): "
          + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(cats[c], key=lambda x: -by_name[x]['stars'])))
A("- Mental model — extraction is a pipeline: **detect layout → OCR/parse elements → "
  "reconstruct structure (tables/formulas/reading order) → export markdown/JSON → "
  "extract typed fields**. Frameworks bundle the first four stages; field extractors "
  "sit on top.")
A("- The field is mid-disruption: **single-VLM parsers** (`DeepSeek-OCR`, `dots.ocr`, "
  "`Dolphin`, `MonkeyOCR`) are replacing multi-model pipelines, and on OmniDocBench "
  "the best open models now beat GPT/Gemini-class generalists at parsing.")
A("- Second trend: **token economics**. `DeepSeek-OCR`'s optical compression "
  "(~10× fewer vision tokens per page) and `olmocr`'s throughput focus optimize for "
  "LLM-corpus cost, not just accuracy.")
A("- No single winner — the *task rankings* below are the point of this report: "
  "the best tool for table-heavy finance PDFs (`docling`) is not the best for CJK "
  "layouts (`MinerU`) or office-file bulk conversion (`markitdown`).")
A("")

# --- Pipeline table
A("## The extraction pipeline at a glance")
A("")
A("| Stage | What happens | Tools in your stars |")
A("|---|---|---|")
A("| **Layout detection** | Find blocks: text, tables, figures, formulas | "
  "`DocLayout-YOLO` (also built into every framework) |")
A("| **OCR / recognition** | Pixels → characters | "
  "`PaddleOCR`, `tesseract`, all VLM parsers |")
A("| **Structure reconstruction** | Tables, formulas, reading order | "
  "`docling` (TableFormer), `MinerU`, `marker`, `Dolphin`, `MonkeyOCR` |")
A("| **Export** | Markdown / JSON / HTML for LLMs | "
  "`markitdown`, `xberg`, `unstructured`, `semtools`, `zerox`, `olmocr`, `nougat`, `dots.ocr`, `DeepSeek-OCR` |")
A("| **Field extraction** | Typed, schema'd values out of parsed text | "
  "`langextract`, `ade-python`, `instructor-js` |")
A("| **Serving / glue** | APIs, MCP, format utilities | "
  "`marker-api`, `docling-mcp`, `python-docx`, `pdf-redactor`, `PdfItDown` |")
A("")

# --- Master comparison
A("## Master comparison")
A("")
A("Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits.")
A("")
A("| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | "
  "Activity | Last push | Age | Contrib(90d) |")
A("|" + "---|" * 11)
for n in sorted(present, key=lambda x: -by_name[x]["stars"]):
    r = by_name[n]
    A("| [{name}]({url}) | {cat} | {lang} | {lic} | {stars} | {lc} | {hs} | "
      "{act} | {push} | {age} | {auth} |".format(
        name=n, url=r["url"], cat=TAXONOMY[n][0],
        lang=r.get("primary_language") or "—",
        lic=(r.get("license") or "—"),
        stars=fmt_stars(r),
        lc=r.get("lifecycle_stage") or "—",
        hs=r.get("health_score") if r.get("health_score") is not None else "—",
        act=activity_label(r),
        push=days_to_human(r.get("days_since_push")) + " ago",
        age=days_to_human(r.get("age_days")),
        auth=r.get("unique_authors_90d") if r.get("unique_authors_90d") is not None else "—",
    ))
A("")

# --- Task rankings (the core ask of this report)
A("## Task rankings — which framework for which job")
A("")
A("Ranked picks per task. Dataset metrics say who's *healthy*; external "
  "benchmarks say who's *accurate* — both feed these rankings (evidence noted "
  "per row, sources in Methodology).")
A("")
A("| Task | 🥇 First pick | 🥈 Second | 🥉 Third | Evidence / note |")
A("|" + "---|" * 5)
for task, picks, evidence in TASK_RANKINGS:
    cells = [f"`{repo.split('/')[-1]}` — {note}" for repo, note in picks]
    A(f"| **{task}** | {cells[0]} | {cells[1]} | {cells[2]} | {evidence} |")
A("")

# --- Category deep dives
A("## By category")
A("")
cat_blurb = {
    "Conversion framework": "End-to-end document → markdown/JSON systems — the layer most "
        "people mean by 'document extraction'. Differ mainly in accuracy/speed trade-off, "
        "format breadth, and GPU appetite.",
    "OCR / layout model": "The classic recognition layer: character recognition and layout "
        "detection as standalone engines/models, used inside the frameworks above.",
    "VLM document parser": "The disruption: one vision-language model reads the page "
        "end-to-end. Compact open models now beat closed generalist VLMs on document "
        "parsing benchmarks.",
    "Structured field extraction": "Post-parsing: pull typed, schema-validated values "
        "(entities, invoice fields, dates) out of the recovered text — with provenance.",
    "Format-specific / serving": "Utilities and wrappers: format-native readers/writers, "
        "redaction, and API/MCP layers that put parsers behind an endpoint.",
}
for cat in order:
    members = cats.get(cat) or []
    if not members:
        continue
    A(f"### {cat}")
    A("")
    A(f"_{cat_blurb[cat]}_")
    A("")
    for n in sorted(members, key=lambda x: -by_name[x]["stars"]):
        r = by_name[n]
        topics = ", ".join((r.get("topics") or [])[:8]) or "—"
        A(f"- **[{n}]({r['url']})** · {fmt_int(r['stars'])}★ · {r.get('primary_language') or '—'} · "
          f"{r.get('lifecycle_stage','—')}  ")
        A(f"  {TAXONOMY[n][1]}  ")
        A(f"  <sub>topics: {topics}</sub>")
    A("")

# --- Spotlight: the VLM takeover
A("## Spotlight: the single-VLM takeover")
A("")
A("Two years ago document extraction meant a *pipeline of specialist models* "
  "(layout detector → OCR → table model → formula model). The 2025–26 wave "
  "collapses that into **one vision-language model per page**:")
A("")
A("- **Accuracy**: on OmniDocBench v1.5, open parsers now score 88–95 "
  "(PaddleOCR-VL 94.5, DeepSeek-OCR-2 91.1, MinerU2.5 90.7, dots.ocr 88.4) — "
  "*above* generalist frontier VLMs on the same benchmark.")
A("- **Size**: the winners are ~3B-parameter models (`dots.ocr`, `MonkeyOCR-pro-3B`, "
  "`DeepSeek-OCR`) — self-hostable on a single GPU.")
A("- **Token economics**: `DeepSeek-OCR` reframes OCR as *context compression* — "
  "1,000 text tokens → ~100 vision tokens at ~97% fidelity — which matters more "
  "than accuracy when feeding million-page corpora to LLMs.")
A("- **Consequence**: classic engines (`tesseract`) and pipeline frameworks keep "
  "the CPU-only and clean-scan niches; everything else is converging on VLMs, "
  "with the frameworks (`MinerU`, `marker`, `docling`) absorbing them as backends.")
A("")

# --- Graph analysis
A("## Graph analysis — how they relate")
A("")
comm = {}
for n in present:
    nd = node_for(n)
    if nd is not None:
        comm.setdefault(nd.get("community"), []).append(n)
A(f"**Community clustering.** These {len(present)} tools span "
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities**.")
A("")
for c, names in sorted(comm.items(), key=lambda x: -len(x[1])):
    if len(names) >= 2:
        A(f"- **Community {c}** ({len(names)}): " + ", ".join(f"`{x}`" for x in names))
A("")

ranked = sorted(
    [(node_for(n).get("pagerank", 0) if node_for(n) else 0, n) for n in present],
    key=lambda x: -x[0],
)
A(f"**Centrality (PageRank in the full {fmt_int(len(gr['nodes']))}-repo graph)** — "
  "most 'hub-like' extraction tools in your ecosystem:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between extraction tools** (top similarity edges where both "
  "endpoints are in this report):")
A("")
if inter_edges:
    id_to_name = {v: k for k, v in name_to_nodeid.items()}
    shown = sorted(inter_edges, key=lambda x: -x["weight"])[:15]
    for e in shown:
        a = id_to_name.get(e["source"], e["source"])
        b = id_to_name.get(e["target"], e["target"])
        why = []
        if e.get("shared_topics"):
            why.append("topics: " + ", ".join(e["shared_topics"][:4]))
        if e.get("shared_authors"):
            why.append("authors: " + ", ".join(e["shared_authors"][:3]))
        A(f"- `{a}` ⇄ `{b}` (w={e['weight']:.3f})" + (f" — {'; '.join(why)}" if why else ""))
    if len(inter_edges) > 15:
        A(f"- …and {len(inter_edges) - 15} more.")
else:
    A("- _None._")
A("")

# --- Maintenance / risk
A("## Maintenance & risk signal")
A("")
A("Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle "
  "+ activity before adopting.")
A("")
A("| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |")
A("|---|---|---|---|---|---|---|")
for n in sorted(present, key=lambda x: -(by_name[x].get("health_score") or 0)):
    r = by_name[n]
    tas = r.get("top_author_share")
    A("| {n} | {h} | {lc} | {act} | {bf} | {tas} | {rel} |".format(
        n=n, h=r.get("health_score", "—"), lc=r.get("lifecycle_stage", "—"),
        act=activity_label(r), bf=r.get("bus_factor", "—"),
        tas=f"{tas:.0%}" if isinstance(tas, (int, float)) else "—",
        rel=r.get("releases_total", "—")))
A("")
A("Watch items: `nougat` is effectively frozen (use `MinerU`/`marker` instead); "
  "`zerox` reads as abandoned in this snapshot — its hosted-VLM pattern is trivial "
  "to reimplement if it stays stale; `marker-api` and `pdf-redactor` are stale "
  "single-maintainer wrappers — pin versions or vendor them.")
A("")

# --- Adjacent
A("## Adjacent (deliberately not listed as extraction tools)")
A("")
for name, why in ADJACENT:
    r = by_name.get(name)
    star = f" ({fmt_int(r['stars'])}★)" if r else ""
    A(f"- **{name}**{star} — {why}")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `data/classified.json` + `public/data/graph.json` for all repo "
  "metrics and graph structure. No API calls at generation time; fully reproducible.")
A("- **Selection**: keyword scan (pdf / ocr / document / layout / extract / parsing / "
  "docx / markdown-convert) + manual curation into pipeline stages. Retrieval, web "
  "scraping, GUI parsing, and PDF-editing apps were routed to adjacent reports or "
  "excluded (see above).")
A("- **Task rankings** additionally cite external benchmark evidence gathered "
  "2026-07: [OmniDocBench](https://github.com/opendatalab/OmniDocBench) v1.5 "
  "composite scores, the [opendataloader-bench 200-PDF comparison]"
  "(https://pdfmux.com/blog/pdfmux-vs-pymupdf-vs-marker-vs-docling/), and vendor "
  "papers (MinerU2.5, dots.ocr, DeepSeek-OCR, Dolphin). Benchmark numbers are "
  "point-in-time and partly vendor-reported — treat rankings as defaults, not verdicts.")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and "
  "may lag GitHub's current state.")
A("- Re-run after a fresh `classified.json` to refresh stars/activity; benchmark "
  "citations are frozen text and need manual review on major model releases.")
A("")
A(f"<sub>Tools covered: {len(present)} · Snapshot: {gen}</sub>")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

# --- Sidecar meta (consumed by build_index.py) --------------------------------
top = sorted(present, key=lambda x: -by_name[x]["stars"])[:5]
meta = {
    "slug": SLUG,
    "title": TITLE,
    "file": f"{SLUG}.md",
    "category": "AI / Documents",
    "summary": (f"{len(present)} document-extraction tools ({fmt_int(total_stars)}★) "
                "compared and ranked per task: conversion frameworks, OCR/layout "
                "models, VLM parsers, field extractors, and serving glue — with "
                "OmniDocBench-backed task rankings."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in order},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/document_extraction.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
