#!/usr/bin/env python3
"""
Generate a builder's guide for a self-built NotebookLM-style app from the
starred-repos dataset: reference clones, source ingestion, grounded retrieval
with citations, Audio Overview (podcast) generation, audio/video source
understanding, interactive voice mode, mind-map views, and wow-factor add-ons
for a demo that goes beyond the original.

Inputs:
  data/classified.json
  public/data/graph.json

Output:
  reports/notebooklm-stack.md   (+ reports/notebooklm-stack.meta.json)

Run: python3 scripts/reports/notebooklm_stack.py
"""
import json
import os
from datetime import datetime, timezone

from lib import fmt_stars, CLASSIFIED, GRAPH, fmt_int, days_to_human, activity_label, make_node_for

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "notebooklm-stack"
TITLE = "Build Your Own NotebookLM — The Repo Stack for a Source-Grounded Notebook Clone"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy --------------------------------------------------------
TAXONOMY = {
    # Reference clones & direct NotebookLM tooling
    "lfnovo/open-notebook": ("Clone / reference app", "An actual OSS NotebookLM implementation — notebooks, sources, podcast generation. Study it before writing a line."),
    "Mintplex-Labs/anything-llm": ("Clone / reference app", "All-in-one private 'chat with your documents' app — the closest mature product shape to a notebook LLM."),
    "HKUDS/DeepTutor": ("Clone / reference app", "Agent-native personalized tutoring over documents — a 'NotebookLM as teacher' angle worth stealing."),
    "teng-lin/notebooklm-py": ("Clone / reference app", "Unofficial Python API for the real NotebookLM — benchmark your clone against the original programmatically."),
    "alexpinel/Dot": ("Clone / reference app", "Tiny fully-local docs+RAG+TTS desktop app — proof the whole loop runs on one laptop."),

    # Source ingestion & parsing
    "microsoft/markitdown": ("Source ingestion & parsing", "One converter for Office/PDF/anything → Markdown; the fastest path to 'add any source'."),
    "opendatalab/MinerU": ("Source ingestion & parsing", "Heavy-duty PDF/Office → LLM-ready markdown/JSON with layout understanding for hard documents."),
    "docling-project/docling": ("Source ingestion & parsing", "IBM's document conversion for gen-AI — tables, layout, OCR; the quality choice for PDF sources."),
    "Unstructured-IO/unstructured": ("Source ingestion & parsing", "Production ETL for messy documents → clean, chunk-ready elements."),
    "jina-ai/reader": ("Source ingestion & parsing", "Any URL → LLM-friendly text via r.jina.ai — instant 'add a website as source'."),
    "yt-dlp/yt-dlp": ("Source ingestion & parsing", "The YouTube/audio/video downloader — feeds media sources into your STT stage."),

    # Grounded retrieval & citations
    "run-llama/llama_index": ("Grounded retrieval & citations", "Document-agent framework with citation query engines — the reference toolkit for source-grounded answers."),
    "HKUDS/LightRAG": ("Grounded retrieval & citations", "Fast GraphRAG over chunks — multi-hop answers across sources, still simple to run."),
    "VectifyAI/PageIndex": ("Grounded retrieval & citations", "Vectorless reasoning-based retrieval over a document tree — page-level citations fall out naturally."),
    "StarTrail-org/LEANN": ("Grounded retrieval & citations", "~97% smaller index — the trick that makes a fully-local notebook on a laptop plausible."),
    "chonkie-inc/chonkie": ("Grounded retrieval & citations", "Lightweight chunking with many strategies — the quality lever for retrieval and citation granularity."),
    "lancedb/lancedb": ("Grounded retrieval & citations", "Embedded serverless vector DB — zero-ops storage that ships inside your app."),

    # Audio Overview (TTS / podcast generation) — the signature feature
    "resemble-ai/chatterbox": ("Audio Overview (TTS / podcast)", "SoTA open TTS with emotion control — the two-host podcast voice pair."),
    "OpenBMB/VoxCPM": ("Audio Overview (TTS / podcast)", "Tokenizer-free multilingual TTS with creative voice design — distinctive hosts nobody else's demo has."),
    "QwenLM/Qwen3-TTS": ("Audio Overview (TTS / podcast)", "Open TTS model series from Qwen — strong multilingual coverage for non-English Audio Overviews."),
    "coqui-ai/TTS": ("Audio Overview (TTS / podcast)", "Battle-tested TTS toolkit (XTTS voice cloning) — huge ecosystem, but check the maintenance signal below."),
    "supertone-inc/supertonic": ("Audio Overview (TTS / podcast)", "Lightning-fast on-device TTS via ONNX — podcast generation without a GPU server."),

    # Audio & video source understanding (STT)
    "openai/whisper": ("Audio/video understanding (STT)", "The reference open speech recognition — turns audio/video sources into searchable text."),
    "SYSTRAN/faster-whisper": ("Audio/video understanding (STT)", "CTranslate2 Whisper, ~4x faster — the practical engine for bulk source transcription."),
    "m-bain/whisperX": ("Audio/video understanding (STT)", "Word-level timestamps + diarization — the ingredient for clickable, second-accurate audio citations."),

    # Interactive voice mode ("join the conversation")
    "pipecat-ai/pipecat": ("Interactive voice mode", "Voice/multimodal conversation pipelines — the frame for 'interrupt the podcast and ask a question'."),
    "livekit/agents": ("Interactive voice mode", "Realtime voice agents on WebRTC — production-grade live rooms for your notebook."),
    "gradio-app/fastrtc": ("Interactive voice mode", "Realtime audio/video streams in a few lines of Python — the fastest demo path to live voice."),
    "KoljaB/RealtimeSTT": ("Interactive voice mode", "Low-latency streaming STT with voice-activity detection — makes barge-in feel instant."),

    # Mind map / knowledge graph view
    "getzep/graphiti": ("Mind map / knowledge graph", "Real-time knowledge graphs over your sources — the live mind-map data structure."),
    "microsoft/graphrag": ("Mind map / knowledge graph", "Entity graph + community summaries over a corpus — auto-generated topic maps per notebook."),
    "topoteretes/cognee": ("Mind map / knowledge graph", "AI memory platform building a queryable graph — notebook memory that persists across sessions."),

    # Wow-factor add-ons
    "bytedance/deer-flow": ("Wow-factor add-on", "Deep-research superagent that already ships podcast creation — 'research the web, then generate the episode'."),
    "screenpipe/screenpipe": ("Wow-factor add-on", "Records everything you see/say/hear — ambient auto-captured sources no cloud NotebookLM can offer."),
}

# Adjacent but deliberately excluded (kept honest in the report)
ADJACENT = [
    ("infiniflow/ragflow", "batteries-included RAG *engine* — covered in the RAG-tooling report; too opinionated to embed in your own app shell"),
    ("open-webui/open-webui", "general chat UI over Ollama/OpenAI — a chat product, not a source-grounded notebook"),
    ("qdrant/qdrant", "excellent vector DB, but a server to operate — `lancedb` keeps the demo self-contained (see RAG report for the full DB landscape)"),
    ("jamiepine/voicebox", "voice *studio* app — covered in the voice-agents report"),
    ("Zackriya-Solutions/meetily", "meeting assistant — covered in the meeting-transcription report"),
    ("suno-ai/bark", "generative audio pioneer, now largely superseded by the TTS picks above"),
    ("NirDiamant/RAG_Techniques", "tutorial collection — great study material, not a dependency"),
]

# The blueprint stacks referenced in the demo section
BLUEPRINT = [
    ("Weekend prototype", [
        ("Ingest", "microsoft/markitdown"),
        ("Retrieve", "HKUDS/LightRAG"),
        ("Store", "lancedb/lancedb"),
        ("Audio Overview", "resemble-ai/chatterbox"),
        ("UI / voice", "gradio-app/fastrtc"),
    ]),
    ("Show-stopper demo", [
        ("Ingest", "docling-project/docling"),
        ("Cited answers", "VectifyAI/PageIndex"),
        ("Audio sources", "m-bain/whisperX"),
        ("Podcast voices", "OpenBMB/VoxCPM"),
        ("Join-the-podcast", "pipecat-ai/pipecat"),
        ("Mind map", "getzep/graphiti"),
    ]),
    ("Fully local / private", [
        ("Ingest", "microsoft/markitdown"),
        ("Tiny index", "StarTrail-org/LEANN"),
        ("STT", "SYSTRAN/faster-whisper"),
        ("On-device TTS", "supertone-inc/supertonic"),
        ("Reference", "alexpinel/Dot"),
    ]),
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
  f"{len(gr['communities'])} communities).")
A(">")
A(f"> Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')} by "
  f"`scripts/reports/notebooklm_stack.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)
order = ["Clone / reference app", "Source ingestion & parsing",
         "Grounded retrieval & citations", "Audio Overview (TTS / podcast)",
         "Audio/video understanding (STT)", "Interactive voice mode",
         "Mind map / knowledge graph", "Wow-factor add-on"]

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **Goal**: everything needed to build (and demo) your own NotebookLM — a "
  f"source-grounded notebook with cited answers, an *Audio Overview* podcast "
  f"generator, live voice interaction, and a mind-map view — from "
  f"**{len(present)} repos already in your stars** (**{fmt_int(total_stars)}★** combined).")
for c in order:
    if cats.get(c):
        A(f"  - **{c}** ({len(cats[c])}): "
          + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(cats[c], key=lambda x: -by_name[x]['stars'])))
A("- The signature NotebookLM feature — the two-host **Audio Overview** — is fully "
  "reproducible with open TTS (`chatterbox`, `VoxCPM`) plus an LLM-written dialogue script; "
  "`open-notebook` proves the end-to-end shape already exists in OSS.")
A("- Your unfair advantages over the real NotebookLM: **fully local/private** operation "
  "(`LEANN` + `supertonic` + `faster-whisper`), **clickable second-accurate audio citations** "
  "(`whisperX` word timestamps), **interruptible live podcasts** (`pipecat`), and "
  "**ambient source capture** (`screenpipe`).")
A("")

# --- Anatomy table
A("## Anatomy of a NotebookLM clone")
A("")
A("| NotebookLM feature | What it needs | Tools in your stars |")
A("|---|---|---|")
A("| **Add sources** (PDF, docs, URLs, YouTube, audio) | parse anything → clean text | "
  "`markitdown`, `docling`, `MinerU`, `unstructured`, `reader`, `yt-dlp` |")
A("| **Grounded chat with citations** | retrieval that keeps provenance | "
  "`llama_index`, `LightRAG`, `PageIndex`, `LEANN`, `chonkie`, `lancedb` |")
A("| **Audio Overview** (podcast) | dialogue script → two distinct voices | "
  "`chatterbox`, `VoxCPM`, `Qwen3-TTS`, `TTS`, `supertonic` |")
A("| **Audio/video sources** | transcribe + timestamp + diarize | "
  "`whisper`, `faster-whisper`, `whisperX` |")
A("| **Interactive mode** (join the conversation) | realtime duplex voice | "
  "`pipecat`, `agents` (LiveKit), `fastrtc`, `RealtimeSTT` |")
A("| **Mind map** | entity/topic graph over sources | "
  "`graphiti`, `graphrag`, `cognee` |")
A("| **Beyond NotebookLM** | the demo-day differentiators | "
  "`deer-flow`, `screenpipe` |")
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

# --- Category deep dives
A("## By category")
A("")
cat_blurb = {
    "Clone / reference app": "Working implementations of the notebook-LLM shape. Read their "
        "source before designing yours — `open-notebook` in particular is the map.",
    "Source ingestion & parsing": "The 'add source' button. NotebookLM's magic starts with "
        "accepting *anything*; these tools normalize PDFs, Office docs, URLs, and media "
        "into clean text.",
    "Grounded retrieval & citations": "The core contract of a notebook LLM: answers cite "
        "the exact source passage. Retrieval must preserve provenance, not just find "
        "relevant chunks.",
    "Audio Overview (TTS / podcast)": "The feature that made NotebookLM famous. An LLM writes "
        "a two-host dialogue from the sources; TTS renders each host with a distinct voice.",
    "Audio/video understanding (STT)": "Podcasts, lectures, and YouTube links as *input* "
        "sources — plus word-level timestamps so audio can be cited like a page number.",
    "Interactive voice mode": "NotebookLM lets you 'join' the audio overview. These realtime "
        "voice frameworks make interruption and follow-up questions feel live.",
    "Mind map / knowledge graph": "NotebookLM renders mind maps of your sources; a knowledge "
        "graph over extracted entities gives you the same view — and a navigable one.",
    "Wow-factor add-on": "Add-ons the original doesn't have — the reason a jury remembers "
        "*your* clone.",
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

# --- Blueprint
A("## Demo blueprints — three stacks, pick your ambition")
A("")
A("Each blueprint is a minimal, coherent pipeline; every tool is in the tables above.")
A("")
for name, steps in BLUEPRINT:
    A(f"### {name}")
    A("")
    A(" → ".join(f"**{stage}** `{repo.split('/')[-1]}`" for stage, repo in steps))
    A("")
blurbs = [
    "**Weekend prototype** — one converter, one RAG engine, one embedded store, one TTS, "
    "one UI library. Upload a PDF, chat with citations, press *Generate Audio Overview*, "
    "get a two-host episode. All Python, no infra.",
    "**Show-stopper demo** — the three moments that land: (1) click a citation in an "
    "*audio* source and playback jumps to the exact second (`whisperX` word timestamps); "
    "(2) *interrupt the generated podcast mid-sentence* and ask a follow-up — the hosts "
    "answer from your sources (`pipecat` duplex voice); (3) the mind map (`graphiti`) "
    "reorganizes live as sources are added.",
    "**Fully local / private** — the anti-cloud pitch: `LEANN`'s ~97% smaller index plus "
    "on-device ONNX TTS and `faster-whisper` means the entire notebook — sources, index, "
    "podcast — never leaves the laptop. `Dot` proves the packaging as a desktop app.",
]
for b in blurbs:
    A(f"- {b}")
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
A(f"**Centrality (PageRank in the full {fmt_int(len(gr['nodes']))}-repo graph)** — most "
  "'hub-like' picks in your ecosystem:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between stack picks** (top similarity edges where both endpoints are in "
  "this report):")
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
  "+ activity before adopting — TTS projects in particular have a history of going quiet.")
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

# --- Selection guidance
A("## Which one should you use?")
A("")
A("| If you want… | Start with | Why |")
A("|---|---|---|")
guide = [
    ("A working reference before you build", "`lfnovo/open-notebook`",
     "OSS NotebookLM implementation — the feature map and the pitfalls, already solved once."),
    ("One 'add any source' button", "`microsoft/markitdown`",
     "Single dependency converts Office/PDF/HTML to Markdown; upgrade to `docling`/`MinerU` for hard PDFs."),
    ("Cited answers with page-level provenance", "`VectifyAI/PageIndex`",
     "Vectorless tree retrieval keeps document structure — citations point at real pages."),
    ("Multi-hop questions across many sources", "`HKUDS/LightRAG`",
     "GraphRAG index over chunks; still light enough for a demo box."),
    ("The two-host podcast voices", "`resemble-ai/chatterbox` (or `OpenBMB/VoxCPM`)",
     "SoTA open TTS with emotion control; VoxCPM adds creative voice *design*."),
    ("Audio sources you can cite by the second", "`m-bain/whisperX`",
     "Word-level timestamps + diarization — click a citation, playback jumps there."),
    ("'Join the conversation' live", "`pipecat-ai/pipecat`",
     "Duplex voice pipelines with interruption handling; `fastrtc` if you want it in 20 lines."),
    ("The mind-map view", "`getzep/graphiti`",
     "Real-time knowledge graph that updates as sources arrive."),
    ("Everything offline on a laptop", "`StarTrail-org/LEANN` + `supertone-inc/supertonic`",
     "Tiny index + on-device ONNX TTS — the private-notebook pitch NotebookLM can't make."),
    ("A demo nobody else has", "`screenpipe/screenpipe`",
     "Ambient screen/audio capture auto-feeds your notebook — sources add themselves."),
]
for want, pick, why in guide:
    A(f"| {want} | {pick} | {why} |")
A("")

# --- Adjacent
A("## Adjacent (deliberately not listed as stack picks)")
A("")
for name, why in ADJACENT:
    r = by_name.get(name)
    star = f" ({fmt_int(r['stars'])}★)" if r else ""
    A(f"- **{name}**{star} — {why}")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `data/classified.json` + `public/data/graph.json`. No external "
  "calls; fully reproducible.")
A("- **Selection**: keyword scan (notebook / notebooklm / podcast / tts / speech / pdf / "
  "document / parse / rag / retrieval / knowledge graph / voice / transcri…) + manual "
  "curation into the NotebookLM feature anatomy. Vector-DB, voice-agent, and meeting-"
  "transcription landscapes have their own reports; overlaps were routed there (see above).")
A("- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may "
  "lag GitHub's current state.")
A("- Re-run after a fresh `classified.json` to refresh stars/activity.")
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
    "category": "AI / Apps",
    "summary": (f"{len(present)} repos ({fmt_int(total_stars)}★) to build a NotebookLM clone: "
                "reference apps, source ingestion, cited retrieval, Audio Overview TTS, "
                "live voice mode, mind maps, and demo-day add-ons."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in order},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/notebooklm_stack.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
