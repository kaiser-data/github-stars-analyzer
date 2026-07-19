# Build Your Own NotebookLM — The Repo Stack for a Source-Grounded Notebook Clone

> Derived from **kaiser-data**'s 1,243 starred repos (snapshot `2026-06-11T21:58:33.384Z`), cross-referenced with the repo-similarity graph (1,243 nodes / 4,017 edges, 32 communities).
>
> Generated 2026-07-19 by `scripts/reports/notebooklm_stack.py` (regenerate any time — no API cost).

![Top tools by stars](assets/notebooklm-stack-top-tools.svg)

![Tools per category](assets/notebooklm-stack-categories.svg)


## Executive summary

- **Goal**: everything needed to build (and demo) your own NotebookLM — a source-grounded notebook with cited answers, an *Audio Overview* podcast generator, live voice interaction, and a mind-map view — from **34 repos already in your stars** (**1,233,462★** combined).
  - **Clone / reference app** (5): `anything-llm`, `open-notebook`, `DeepTutor`, `notebooklm-py`, `Dot`
  - **Source ingestion & parsing** (6): `yt-dlp`, `markitdown`, `MinerU`, `docling`, `unstructured`, `reader`
  - **Grounded retrieval & citations** (6): `llama_index`, `LightRAG`, `PageIndex`, `LEANN`, `lancedb`, `chonkie`
  - **Audio Overview (TTS / podcast)** (5): `TTS`, `VoxCPM`, `chatterbox`, `Qwen3-TTS`, `supertonic`
  - **Audio/video understanding (STT)** (3): `whisper`, `faster-whisper`, `whisperX`
  - **Interactive voice mode** (4): `pipecat`, `agents`, `RealtimeSTT`, `fastrtc`
  - **Mind map / knowledge graph** (3): `graphrag`, `graphiti`, `cognee`
  - **Wow-factor add-on** (2): `deer-flow`, `screenpipe`
- The signature NotebookLM feature — the two-host **Audio Overview** — is fully reproducible with open TTS (`chatterbox`, `VoxCPM`) plus an LLM-written dialogue script; `open-notebook` proves the end-to-end shape already exists in OSS.
- Your unfair advantages over the real NotebookLM: **fully local/private** operation (`LEANN` + `supertonic` + `faster-whisper`), **clickable second-accurate audio citations** (`whisperX` word timestamps), **interruptible live podcasts** (`pipecat`), and **ambient source capture** (`screenpipe`).

## Anatomy of a NotebookLM clone

| NotebookLM feature | What it needs | Tools in your stars |
|---|---|---|
| **Add sources** (PDF, docs, URLs, YouTube, audio) | parse anything → clean text | `markitdown`, `docling`, `MinerU`, `unstructured`, `reader`, `yt-dlp` |
| **Grounded chat with citations** | retrieval that keeps provenance | `llama_index`, `LightRAG`, `PageIndex`, `LEANN`, `chonkie`, `lancedb` |
| **Audio Overview** (podcast) | dialogue script → two distinct voices | `chatterbox`, `VoxCPM`, `Qwen3-TTS`, `TTS`, `supertonic` |
| **Audio/video sources** | transcribe + timestamp + diarize | `whisper`, `faster-whisper`, `whisperX` |
| **Interactive mode** (join the conversation) | realtime duplex voice | `pipecat`, `agents` (LiveKit), `fastrtc`, `RealtimeSTT` |
| **Mind map** | entity/topic graph over sources | `graphiti`, `graphrag`, `cognee` |
| **Beyond NotebookLM** | the demo-day differentiators | `deer-flow`, `screenpipe` |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | Source ingestion & parsing | Python | Unlicense | 169,895 | Classic | 75 | very active | 0d ago | 5.6y | 22 |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Source ingestion & parsing | Python | MIT | 151,143 | Mature | 51 | active | 16d ago | 1.6y | 4 |
| [openai/whisper](https://github.com/openai/whisper) | Audio/video understanding (STT) | Python | MIT | 102,488 | Mature | 40 | active | 1mo ago | 3.7y | 2 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Wow-factor add-on | Python | MIT | 70,988 | Hot | 81 | very active | 0d ago | 1.1y | 27 |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | Source ingestion & parsing | Python | NOASSERTION | 67,255 | Mature | 80 | very active | 0d ago | 2.3y | 1 |
| [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | Clone / reference app | JavaScript | MIT | 61,453 | Classic | 79 | very active | 0d ago | 3.0y | 17 |
| [docling-project/docling](https://github.com/docling-project/docling) | Source ingestion & parsing | Python | MIT | 61,405 | Hot | 95 | very active | 0d ago | 1.9y | 35 |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | Grounded retrieval & citations | Python | MIT | 50,083 | Classic | 100 | very active | 0d ago | 3.6y | 49 |
| [coqui-ai/TTS](https://github.com/coqui-ai/TTS) | Audio Overview (TTS / podcast) | Python | MPL-2.0 | 45,540 | Abandoned | 10 | stale | 1.8y ago | 6.1y | 0 |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | Grounded retrieval & citations | Python | MIT | 36,460 | Mature | 79 | very active | 0d ago | 1.7y | 2 |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | Mind map / knowledge graph | Python | MIT | 33,661 | Mature | 68 | active | 6d ago | 2.2y | 4 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Grounded retrieval & citations | Python | MIT | 32,927 | Hot | 50 | very active | 6d ago | 1.2y | 5 |
| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | Clone / reference app | TypeScript | MIT | 29,257 | Hot | 76 | very active | 7d ago | 1.6y | 17 |
| [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | Audio Overview (TTS / podcast) | Python | Apache-2.0 | 28,454 | Hot | 78 | very active | 2d ago | 8mo | 14 |
| [getzep/graphiti](https://github.com/getzep/graphiti) | Mind map / knowledge graph | Python | Apache-2.0 | 27,306 | Hot | 77 | very active | 0d ago | 1.8y | 10 |
| [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) | Audio Overview (TTS / podcast) | Python | MIT | 25,021 | Declining | 48 | active | 1d ago | 1.1y | 4 |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Clone / reference app | Python | Apache-2.0 | 24,708 | Hot | 79 | very active | 0d ago | 5mo | 14 |
| [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Audio/video understanding (STT) | Python | MIT | 23,549 | Declining | 24 | stale | 6mo ago | 3.3y | 0 |
| [m-bain/whisperX](https://github.com/m-bain/whisperX) | Audio/video understanding (STT) | Python | BSD-2-Clause | 22,396 | Classic | 69 | very active | 9d ago | 3.5y | 5 |
| [screenpipe/screenpipe](https://github.com/screenpipe/screenpipe) | Wow-factor add-on | Rust | NOASSERTION | 19,259 | Hot | 80 | very active | 0d ago | 2.0y | 7 |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | Mind map / knowledge graph | Python | Apache-2.0 | 17,792 | Mature | 80 | very active | 0d ago | 2.8y | 6 |
| [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | Clone / reference app | Python | MIT | 16,263 | Hot | 80 | very active | 0d ago | 5mo | 3 |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | Source ingestion & parsing | HTML | Apache-2.0 | 14,889 | Classic | 82 | very active | 0d ago | 3.7y | 11 |
| [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat) | Interactive voice mode | Python | BSD-2-Clause | 12,772 | Mature | 79 | very active | 0d ago | 2.5y | 3 |
| [StarTrail-org/LEANN](https://github.com/StarTrail-org/LEANN) | Grounded retrieval & citations | Python | MIT | 11,908 | Hot | 76 | very active | 3d ago | 1.0y | 17 |
| [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | Audio Overview (TTS / podcast) | Python | Apache-2.0 | 11,883 | Declining | 36 | slowing | 2mo ago | 4mo | 1 |
| [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | Audio Overview (TTS / podcast) | Swift | MIT | 11,477 | Rising | 54 | active | 21d ago | 6mo | 6 |
| [jina-ai/reader](https://github.com/jina-ai/reader) | Source ingestion & parsing | TypeScript | Apache-2.0 | 11,165 | Mature | 54 | very active | 21d ago | 2.2y | 2 |
| [livekit/agents](https://github.com/livekit/agents) | Interactive voice mode | Python | Apache-2.0 | 10,945 | Mature | 99 | very active | 0d ago | 2.6y | 30 |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | Grounded retrieval & citations | HTML | Apache-2.0 | 10,579 | Classic | 96 | very active | 0d ago | 3.3y | 29 |
| [KoljaB/RealtimeSTT](https://github.com/KoljaB/RealtimeSTT) | Interactive voice mode | Python | MIT | 9,890 | Mature | 61 | very active | 2d ago | 2.8y | 2 |
| [gradio-app/fastrtc](https://github.com/gradio-app/fastrtc) | Interactive voice mode | JavaScript | MIT | 4,604 | Declining | 38 | slowing | 5mo ago | 1.7y | 0 |
| [chonkie-inc/chonkie](https://github.com/chonkie-inc/chonkie) | Grounded retrieval & citations | Python | MIT | 4,139 | Hot | 78 | very active | 0d ago | 1.2y | 5 |
| [alexpinel/Dot](https://github.com/alexpinel/Dot) | Clone / reference app | JavaScript | GPL-3.0 | 1,908 | Abandoned | 1 | stale | 1.5y ago | 2.2y | 0 |

## By category

### Clone / reference app

_Working implementations of the notebook-LLM shape. Read their source before designing yours — `open-notebook` in particular is the map._

- **[Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)** · 61,453★ · JavaScript · Classic  
  All-in-one private 'chat with your documents' app — the closest mature product shape to a notebook LLM.  
  <sub>topics: rag, localai, vector-database, llm, ai-agents, multimodal, no-code, agent-harness</sub>
- **[lfnovo/open-notebook](https://github.com/lfnovo/open-notebook)** · 29,257★ · TypeScript · Hot  
  An actual OSS NotebookLM implementation — notebooks, sources, podcast generation. Study it before writing a line.  
  <sub>topics: assistant, learning, note-taking, notebook, notes-app, self-learning</sub>
- **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · 24,708★ · Python · Hot  
  Agent-native personalized tutoring over documents — a 'NotebookLM as teacher' angle worth stealing.  
  <sub>topics: ai-tutor, deepresearch, interactive-learning, large-language-models, multi-agent-systems, rag, ai-agents, clawdbot</sub>
- **[teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py)** · 16,263★ · Python · Hot  
  Unofficial Python API for the real NotebookLM — benchmark your clone against the original programmatically.  
  <sub>topics: api, claude, python, sdk, skills, google-notebooklm, notebooklm, notebooklm-api</sub>
- **[alexpinel/Dot](https://github.com/alexpinel/Dot)** · 1,908★ · JavaScript · Abandoned  
  Tiny fully-local docs+RAG+TTS desktop app — proof the whole loop runs on one laptop.  
  <sub>topics: embeddings, llm, local, rag, standalone, standalone-app, document-chat, faiss</sub>

### Source ingestion & parsing

_The 'add source' button. NotebookLM's magic starts with accepting *anything*; these tools normalize PDFs, Office docs, URLs, and media into clean text._

- **[yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)** · 169,895★ · Python · Classic  
  The YouTube/audio/video downloader — feeds media sources into your STT stage.  
  <sub>topics: youtube-dl, python, sponsorblock, yt-dlp, youtube-downloader, cli, downloader</sub>
- **[microsoft/markitdown](https://github.com/microsoft/markitdown)** · 151,143★ · Python · Mature  
  One converter for Office/PDF/anything → Markdown; the fastest path to 'add any source'.  
  <sub>topics: langchain, openai, autogen-extension, autogen, markdown, microsoft-office, pdf</sub>
- **[opendatalab/MinerU](https://github.com/opendatalab/MinerU)** · 67,255★ · Python · Mature  
  Heavy-duty PDF/Office → LLM-ready markdown/JSON with layout understanding for hard documents.  
  <sub>topics: extract-data, layout-analysis, ocr, parser, pdf, pdf-converter, python, document-analysis</sub>
- **[docling-project/docling](https://github.com/docling-project/docling)** · 61,405★ · Python · Hot  
  IBM's document conversion for gen-AI — tables, layout, OCR; the quality choice for PDF sources.  
  <sub>topics: ai, convert, documents, pdf, tables, document-parser, document-parsing, docx</sub>
- **[Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)** · 14,889★ · HTML · Classic  
  Production ETL for messy documents → clean, chunk-ready elements.  
  <sub>topics: deep-learning, document-parsing, machine-learning, nlp, ocr, information-retrieval, data-pipelines, ml</sub>
- **[jina-ai/reader](https://github.com/jina-ai/reader)** · 11,165★ · TypeScript · Mature  
  Any URL → LLM-friendly text via r.jina.ai — instant 'add a website as source'.  
  <sub>topics: llm, proxy</sub>

### Grounded retrieval & citations

_The core contract of a notebook LLM: answers cite the exact source passage. Retrieval must preserve provenance, not just find relevant chunks._

- **[run-llama/llama_index](https://github.com/run-llama/llama_index)** · 50,083★ · Python · Classic  
  Document-agent framework with citation query engines — the reference toolkit for source-grounded answers.  
  <sub>topics: agents, application, data, fine-tuning, framework, llamaindex, llm, rag</sub>
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 36,460★ · Python · Mature  
  Fast GraphRAG over chunks — multi-hop answers across sources, still simple to run.  
  <sub>topics: knowledge-graph, large-language-models, retrieval-augmented-generation, genai, graphrag, llm, rag, gpt</sub>
- **[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** · 32,927★ · Python · Hot  
  Vectorless reasoning-based retrieval over a document tree — page-level citations fall out naturally.  
  <sub>topics: agentic-ai, agents, ai, ai-agents, context-engineering, llm, rag, reasoning</sub>
- **[StarTrail-org/LEANN](https://github.com/StarTrail-org/LEANN)** · 11,908★ · Python · Hot  
  ~97% smaller index — the trick that makes a fully-local notebook on a laptop plausible.  
  <sub>topics: ai, faiss, langchain, llama-index, llm, localstorage, offline-first, ollama</sub>
- **[lancedb/lancedb](https://github.com/lancedb/lancedb)** · 10,579★ · HTML · Classic  
  Embedded serverless vector DB — zero-ops storage that ships inside your app.  
  <sub>topics: approximate-nearest-neighbor-search, image-search, nearest-neighbor-search, recommender-system, search-engine, semantic-search, similarity-search, vector-database</sub>
- **[chonkie-inc/chonkie](https://github.com/chonkie-inc/chonkie)** · 4,139★ · Python · Hot  
  Lightweight chunking with many strategies — the quality lever for retrieval and citation granularity.  
  <sub>topics: rag, chonkie, chunker, chunking-algorithm, retrieval-systems, semantic-chunker, similarity-search, text-splitter</sub>

### Audio Overview (TTS / podcast)

_The feature that made NotebookLM famous. An LLM writes a two-host dialogue from the sources; TTS renders each host with a distinct voice._

- **[coqui-ai/TTS](https://github.com/coqui-ai/TTS)** · 45,540★ · Python · Abandoned  
  Battle-tested TTS toolkit (XTTS voice cloning) — huge ecosystem, but check the maintenance signal below.  
  <sub>topics: python, text-to-speech, deep-learning, speech, pytorch, tts, vocoder, tacotron</sub>
- **[OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM)** · 28,454★ · Python · Hot  
  Tokenizer-free multilingual TTS with creative voice design — distinctive hosts nobody else's demo has.  
  <sub>topics: audio, deeplearning, minicpm, python, pytorch, speech, speech-synthesis, text-to-speech</sub>
- **[resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox)** · 25,021★ · Python · Declining  
  SoTA open TTS with emotion control — the two-host podcast voice pair.  
  <sub>topics: —</sub>
- **[QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS)** · 11,883★ · Python · Declining  
  Open TTS model series from Qwen — strong multilingual coverage for non-English Audio Overviews.  
  <sub>topics: —</sub>
- **[supertone-inc/supertonic](https://github.com/supertone-inc/supertonic)** · 11,477★ · Swift · Rising  
  Lightning-fast on-device TTS via ONNX — podcast generation without a GPU server.  
  <sub>topics: cpp, csharp, go, ios, java, lightweight, nodejs, on-device</sub>

### Audio/video understanding (STT)

_Podcasts, lectures, and YouTube links as *input* sources — plus word-level timestamps so audio can be cited like a page number._

- **[openai/whisper](https://github.com/openai/whisper)** · 102,488★ · Python · Mature  
  The reference open speech recognition — turns audio/video sources into searchable text.  
  <sub>topics: —</sub>
- **[SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)** · 23,549★ · Python · Declining  
  CTranslate2 Whisper, ~4x faster — the practical engine for bulk source transcription.  
  <sub>topics: deep-learning, inference, quantization, speech-recognition, speech-to-text, transformer, whisper, openai</sub>
- **[m-bain/whisperX](https://github.com/m-bain/whisperX)** · 22,396★ · Python · Classic  
  Word-level timestamps + diarization — the ingredient for clickable, second-accurate audio citations.  
  <sub>topics: asr, speech, speech-recognition, speech-to-text, whisper</sub>

### Interactive voice mode

_NotebookLM lets you 'join' the audio overview. These realtime voice frameworks make interruption and follow-up questions feel live._

- **[pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat)** · 12,772★ · Python · Mature  
  Voice/multimodal conversation pipelines — the frame for 'interrupt the podcast and ask a question'.  
  <sub>topics: ai, real-time, voice, voice-assistant, chatbot-framework, chatbots</sub>
- **[livekit/agents](https://github.com/livekit/agents)** · 10,945★ · Python · Mature  
  Realtime voice agents on WebRTC — production-grade live rooms for your notebook.  
  <sub>topics: ai, real-time, voice, video, agents, openai</sub>
- **[KoljaB/RealtimeSTT](https://github.com/KoljaB/RealtimeSTT)** · 9,890★ · Python · Mature  
  Low-latency streaming STT with voice-activity detection — makes barge-in feel instant.  
  <sub>topics: python, realtime, speech-to-text</sub>
- **[gradio-app/fastrtc](https://github.com/gradio-app/fastrtc)** · 4,604★ · JavaScript · Declining  
  Realtime audio/video streams in a few lines of Python — the fastest demo path to live voice.  
  <sub>topics: artificial-intelligence, llm, python, real-time, speech-to-text, text-to-speech, hacktoberfest, hacktoberfest2025</sub>

### Mind map / knowledge graph

_NotebookLM renders mind maps of your sources; a knowledge graph over extracted entities gives you the same view — and a navigable one._

- **[microsoft/graphrag](https://github.com/microsoft/graphrag)** · 33,661★ · Python · Mature  
  Entity graph + community summaries over a corpus — auto-generated topic maps per notebook.  
  <sub>topics: graphrag, rag, llm, llms, gpt, gpt-4, gpt4</sub>
- **[getzep/graphiti](https://github.com/getzep/graphiti)** · 27,306★ · Python · Hot  
  Real-time knowledge graphs over your sources — the live mind-map data structure.  
  <sub>topics: agents, graph, llms, rag</sub>
- **[topoteretes/cognee](https://github.com/topoteretes/cognee)** · 17,792★ · Python · Mature  
  AI memory platform building a queryable graph — notebook memory that persists across sessions.  
  <sub>topics: ai, cognitive-architecture, vector-database, ai-agents, graph-database, ai-memory, cognitive-memory, knowledge</sub>

### Wow-factor add-on

_Add-ons the original doesn't have — the reason a jury remembers *your* clone._

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 70,988★ · Python · Hot  
  Deep-research superagent that already ships podcast creation — 'research the web, then generate the episode'.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[screenpipe/screenpipe](https://github.com/screenpipe/screenpipe)** · 19,259★ · Rust · Hot  
  Records everything you see/say/hear — ambient auto-captured sources no cloud NotebookLM can offer.  
  <sub>topics: ai, computer-vision, llm, machine-learning, ml, multimodal, vision, agents</sub>

## Demo blueprints — three stacks, pick your ambition

Each blueprint is a minimal, coherent pipeline; every tool is in the tables above.

### Weekend prototype

**Ingest** `markitdown` → **Retrieve** `LightRAG` → **Store** `lancedb` → **Audio Overview** `chatterbox` → **UI / voice** `fastrtc`

### Show-stopper demo

**Ingest** `docling` → **Cited answers** `PageIndex` → **Audio sources** `whisperX` → **Podcast voices** `VoxCPM` → **Join-the-podcast** `pipecat` → **Mind map** `graphiti`

### Fully local / private

**Ingest** `markitdown` → **Tiny index** `LEANN` → **STT** `faster-whisper` → **On-device TTS** `supertonic` → **Reference** `Dot`

- **Weekend prototype** — one converter, one RAG engine, one embedded store, one TTS, one UI library. Upload a PDF, chat with citations, press *Generate Audio Overview*, get a two-host episode. All Python, no infra.
- **Show-stopper demo** — the three moments that land: (1) click a citation in an *audio* source and playback jumps to the exact second (`whisperX` word timestamps); (2) *interrupt the generated podcast mid-sentence* and ask a follow-up — the hosts answer from your sources (`pipecat` duplex voice); (3) the mind map (`graphiti`) reorganizes live as sources are added.
- **Fully local / private** — the anti-cloud pitch: `LEANN`'s ~97% smaller index plus on-device ONNX TTS and `faster-whisper` means the entire notebook — sources, index, podcast — never leaves the laptop. `Dot` proves the packaging as a desktop app.

## Graph analysis — how they relate

**Community clustering.** These 34 tools span **17 of the graph's 32 communities**.

- **Community 13** (5): `Mintplex-Labs/anything-llm`, `VectifyAI/PageIndex`, `StarTrail-org/LEANN`, `topoteretes/cognee`, `bytedance/deer-flow`
- **Community 7** (3): `lfnovo/open-notebook`, `teng-lin/notebooklm-py`, `chonkie-inc/chonkie`
- **Community 6** (3): `opendatalab/MinerU`, `OpenBMB/VoxCPM`, `coqui-ai/TTS`
- **Community 17** (3): `docling-project/docling`, `Unstructured-IO/unstructured`, `supertone-inc/supertonic`
- **Community 20** (3): `yt-dlp/yt-dlp`, `gradio-app/fastrtc`, `KoljaB/RealtimeSTT`
- **Community 0** (3): `resemble-ai/chatterbox`, `SYSTRAN/faster-whisper`, `m-bain/whisperX`
- **Community 12** (2): `microsoft/markitdown`, `microsoft/graphrag`
- **Community 4** (2): `pipecat-ai/pipecat`, `livekit/agents`
- **Community 1** (2): `getzep/graphiti`, `screenpipe/screenpipe`

**Centrality (PageRank in the full 1,243-repo graph)** — most 'hub-like' picks in your ecosystem:

- `m-bain/whisperX` — PageRank 0.0024
- `VectifyAI/PageIndex` — PageRank 0.0024
- `HKUDS/LightRAG` — PageRank 0.0017
- `openai/whisper` — PageRank 0.0016
- `getzep/graphiti` — PageRank 0.0014
- `SYSTRAN/faster-whisper` — PageRank 0.0013
- `QwenLM/Qwen3-TTS` — PageRank 0.0012
- `KoljaB/RealtimeSTT` — PageRank 0.0012
- `lancedb/lancedb` — PageRank 0.0012
- `microsoft/graphrag` — PageRank 0.0011

**Direct links between stack picks** (top similarity edges where both endpoints are in this report):

- `m-bain/whisperX` ⇄ `teng-lin/notebooklm-py` (w=0.717) — authors: claude, dependabot[bot]
- `HKUDS/DeepTutor` ⇄ `HKUDS/LightRAG` (w=0.675) — topics: large-language-models, rag
- `livekit/agents` ⇄ `pipecat-ai/pipecat` (w=0.383) — topics: ai, real-time, voice
- `OpenBMB/VoxCPM` ⇄ `coqui-ai/TTS` (w=0.370) — topics: python, pytorch, speech, speech-synthesis
- `m-bain/whisperX` ⇄ `SYSTRAN/faster-whisper` (w=0.350) — topics: speech-recognition, speech-to-text, whisper
- `opendatalab/MinerU` ⇄ `docling-project/docling` (w=0.242) — topics: pdf, pdf-converter, docx, pptx
- `VectifyAI/PageIndex` ⇄ `Mintplex-Labs/anything-llm` (w=0.238) — topics: agentic-ai, ai-agents, llm, rag
- `KoljaB/RealtimeSTT` ⇄ `gradio-app/fastrtc` (w=0.222) — topics: python, speech-to-text
- `Unstructured-IO/unstructured` ⇄ `docling-project/docling` (w=0.207) — topics: document-parsing, pdf-to-text, pdf, pdf-to-json
- `VectifyAI/PageIndex` ⇄ `topoteretes/cognee` (w=0.198) — topics: ai, ai-agents, context-engineering, vector-database
- `supertone-inc/supertonic` ⇄ `OpenBMB/VoxCPM` (w=0.172) — topics: python, text-to-speech, tts, multilingual
- `screenpipe/screenpipe` ⇄ `Mintplex-Labs/anything-llm` (w=0.154) — topics: llm, multimodal, local-ai, local-first
- `StarTrail-org/LEANN` ⇄ `alexpinel/Dot` (w=0.148) — topics: faiss, langchain, llm, rag

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting — TTS projects in particular have a history of going quiet.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| run-llama/llama_index | 100 | Classic | very active | 7 | 25% | 494 |
| livekit/agents | 99 | Mature | very active | 5 | 18% | 357 |
| lancedb/lancedb | 96 | Classic | very active | 5 | 14% | 442 |
| docling-project/docling | 95 | Hot | very active | 5 | 15% | 181 |
| Unstructured-IO/unstructured | 82 | Classic | very active | 3 | 28% | 231 |
| bytedance/deer-flow | 81 | Hot | very active | 5 | 16% | 0 |
| teng-lin/notebooklm-py | 80 | Hot | very active | 1 | 97% | 14 |
| opendatalab/MinerU | 80 | Mature | very active | 1 | 100% | 174 |
| topoteretes/cognee | 80 | Mature | very active | 1 | 52% | 114 |
| screenpipe/screenpipe | 80 | Hot | very active | 1 | 56% | 378 |
| Mintplex-Labs/anything-llm | 79 | Classic | very active | 1 | 63% | 30 |
| HKUDS/DeepTutor | 79 | Hot | very active | 1 | 58% | 40 |
| HKUDS/LightRAG | 79 | Mature | very active | 1 | 89% | 75 |
| pipecat-ai/pipecat | 79 | Mature | very active | 1 | 69% | 112 |
| chonkie-inc/chonkie | 78 | Hot | very active | 1 | 84% | 44 |
| OpenBMB/VoxCPM | 78 | Hot | very active | 2 | 41% | 14 |
| getzep/graphiti | 77 | Hot | very active | 2 | 47% | 196 |
| lfnovo/open-notebook | 76 | Hot | very active | 1 | 58% | 37 |
| StarTrail-org/LEANN | 76 | Hot | very active | 2 | 36% | 29 |
| yt-dlp/yt-dlp | 75 | Classic | very active | 1 | 55% | 134 |
| m-bain/whisperX | 69 | Classic | very active | 1 | 55% | 43 |
| microsoft/graphrag | 68 | Mature | active | 1 | 69% | 40 |
| KoljaB/RealtimeSTT | 61 | Mature | very active | 1 | 94% | 42 |
| jina-ai/reader | 54 | Mature | very active | 1 | 95% | 0 |
| supertone-inc/supertonic | 54 | Rising | active | 2 | 40% | 1 |
| microsoft/markitdown | 51 | Mature | active | 1 | 50% | 19 |
| VectifyAI/PageIndex | 50 | Hot | very active | 1 | 73% | 0 |
| resemble-ai/chatterbox | 48 | Declining | active | 2 | 25% | 1 |
| openai/whisper | 40 | Mature | active | 1 | 50% | 13 |
| gradio-app/fastrtc | 38 | Declining | slowing | 0 | 0% | 22 |
| QwenLM/Qwen3-TTS | 36 | Declining | slowing | 1 | 100% | 0 |
| SYSTRAN/faster-whisper | 24 | Declining | stale | 0 | 0% | 21 |
| coqui-ai/TTS | 10 | Abandoned | stale | 0 | 0% | 98 |
| alexpinel/Dot | 1 | Abandoned | stale | 0 | 0% | 4 |

## Which one should you use?

| If you want… | Start with | Why |
|---|---|---|
| A working reference before you build | `lfnovo/open-notebook` | OSS NotebookLM implementation — the feature map and the pitfalls, already solved once. |
| One 'add any source' button | `microsoft/markitdown` | Single dependency converts Office/PDF/HTML to Markdown; upgrade to `docling`/`MinerU` for hard PDFs. |
| Cited answers with page-level provenance | `VectifyAI/PageIndex` | Vectorless tree retrieval keeps document structure — citations point at real pages. |
| Multi-hop questions across many sources | `HKUDS/LightRAG` | GraphRAG index over chunks; still light enough for a demo box. |
| The two-host podcast voices | `resemble-ai/chatterbox` (or `OpenBMB/VoxCPM`) | SoTA open TTS with emotion control; VoxCPM adds creative voice *design*. |
| Audio sources you can cite by the second | `m-bain/whisperX` | Word-level timestamps + diarization — click a citation, playback jumps there. |
| 'Join the conversation' live | `pipecat-ai/pipecat` | Duplex voice pipelines with interruption handling; `fastrtc` if you want it in 20 lines. |
| The mind-map view | `getzep/graphiti` | Real-time knowledge graph that updates as sources arrive. |
| Everything offline on a laptop | `StarTrail-org/LEANN` + `supertone-inc/supertonic` | Tiny index + on-device ONNX TTS — the private-notebook pitch NotebookLM can't make. |
| A demo nobody else has | `screenpipe/screenpipe` | Ambient screen/audio capture auto-feeds your notebook — sources add themselves. |

## Adjacent (deliberately not listed as stack picks)

- **infiniflow/ragflow** (82,476★) — batteries-included RAG *engine* — covered in the RAG-tooling report; too opinionated to embed in your own app shell
- **open-webui/open-webui** (141,111★) — general chat UI over Ollama/OpenAI — a chat product, not a source-grounded notebook
- **qdrant/qdrant** (32,039★) — excellent vector DB, but a server to operate — `lancedb` keeps the demo self-contained (see RAG report for the full DB landscape)
- **jamiepine/voicebox** (29,774★) — voice *studio* app — covered in the voice-agents report
- **Zackriya-Solutions/meetily** (12,672★) — meeting assistant — covered in the meeting-transcription report
- **suno-ai/bark** (39,149★) — generative audio pioneer, now largely superseded by the TTS picks above
- **NirDiamant/RAG_Techniques** (27,870★) — tutorial collection — great study material, not a dependency

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (notebook / notebooklm / podcast / tts / speech / pdf / document / parse / rag / retrieval / knowledge graph / voice / transcri…) + manual curation into the NotebookLM feature anatomy. Vector-DB, voice-agent, and meeting-transcription landscapes have their own reports; overlaps were routed there (see above).
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 34 · Snapshot: 2026-06-11T21:58:33.384Z</sub>
