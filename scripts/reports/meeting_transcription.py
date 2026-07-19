#!/usr/bin/env python3
"""
Generate a report on Meeting Transcription & Conversation Analysis tools in the
starred-repos dataset: end-to-end meeting assistants, ASR engines (the
transcribers), diarization/alignment (who said what), streaming/live capture,
transcription servers, and transcript-analysis tools — with a clear verdict on
which repo to pick for transcribing and analyzing meetings.

Inputs:
  data/classified.json
  public/data/graph.json

Output:
  reports/meeting-transcription.md   (+ reports/meeting-transcription.meta.json)

Run: python3 scripts/reports/meeting_transcription.py
"""
import json
import os
from datetime import datetime, timezone

from lib import fmt_stars, CLASSIFIED, GRAPH, fmt_int, days_to_human, activity_label, make_node_for

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "meeting-transcription"
TITLE = "Meeting Transcription & Conversation Analysis — Field Guide"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy --------------------------------------------------------
# A meeting-transcription stack is a pipeline: capture audio → VAD → ASR
# (transcribe) → diarize/align (who said what, when) → summarize/analyze.
# Apps bundle the whole pipeline; the other categories are its building blocks.
TAXONOMY = {
    # End-to-end meeting assistants / notetakers — the bundled pipeline
    "Zackriya-Solutions/meetily": ("Meeting assistant (end-to-end)", "Privacy-first local meeting notetaker (macOS/Win) — live Parakeet/Whisper transcription, speaker diarization, Ollama summaries; 100% on-device."),
    "screenpipe/screenpipe": ("Meeting assistant (end-to-end)", "24/7 local screen + mic capture with transcription — a rolling, searchable record of everything said on your machine."),
    "thewh1teagle/vibe": ("Meeting assistant (end-to-end)", "Polished cross-platform desktop app for offline transcription (Whisper) with batch, subtitles, and diarization."),
    "SevaSk/ecoute": ("Meeting assistant (end-to-end)", "Live meeting listener — real-time transcription of mic + speaker audio with GPT-suggested responses as the call happens."),
    "rishikanthc/Scriberr": ("Meeting assistant (end-to-end)", "Self-hosted (Docker) team transcription service — upload recordings, get diarized transcripts + optional local-LLM summaries."),
    "pluja/whishper": ("Meeting assistant (end-to-end)", "Self-hosted transcription suite with web UI — transcribe, translate, edit, and export subtitles, fully offline."),
    "kaixxx/noScribe": ("Meeting assistant (end-to-end)", "Transcription built for qualitative researchers — diarized interview transcripts with an editor designed for coding/analysis."),
    "transcriptionstream/transcriptionstream": ("Meeting assistant (end-to-end)", "Turnkey self-hosted drop-folder: transcription + diarization + Ollama summarization as one service."),

    # ASR engines & models — the transcribers
    "openai/whisper": ("ASR engine / model", "The reference open ASR model — robust multilingual transcription; the baseline every meeting tool builds on."),
    "ggml-org/whisper.cpp": ("ASR engine / model", "C/C++ Whisper — runs on CPU/edge with no Python; powers many of the desktop meeting apps above."),
    "SYSTRAN/faster-whisper": ("ASR engine / model", "CTranslate2 Whisper — ~4× faster, lower memory; the production server-side transcription default."),
    "huggingface/distil-whisper": ("ASR engine / model", "Distilled Whisper — ~6× faster, 49% smaller, within ~1% WER; batch-transcribe long meetings cheaply."),
    "moonshine-ai/moonshine": ("ASR engine / model", "Edge-first ASR beating Whisper at 5–15× speed on short segments — built for live, on-device captioning."),
    "NVIDIA-NeMo/Speech": ("ASR engine / model", "NVIDIA's speech stack — Parakeet (fastest open ASR) and Canary (top of the Open ASR leaderboard) live here, plus diarization recipes."),
    "modelscope/FunASR": ("ASR engine / model", "Alibaba's production ASR toolkit — streaming + offline models with punctuation, timestamps, and speaker labels (Paraformer)."),
    "FunAudioLLM/SenseVoice": ("ASR engine / model", "Multilingual ASR with emotion recognition and audio-event detection — transcription plus conversational tone signals."),
    "kyutai-labs/delayed-streams-modeling": ("ASR engine / model", "Kyutai's streaming STT — word-level timestamps over live streams with seconds-level latency."),
    "alphacep/vosk-api": ("ASR engine / model", "Offline ASR for 20+ languages with tiny (~50MB) models — bindings for ~10 languages; runs on a Raspberry Pi."),
    "kaldi-asr/kaldi": ("ASR engine / model", "The classic ASR research toolkit — the foundation Vosk and a generation of speech systems were built on."),
    "espnet/espnet": ("ASR engine / model", "End-to-end speech toolkit (ASR/TTS/translation/diarization) — research breadth across 100+ recipes."),
    "speechbrain/speechbrain": ("ASR engine / model", "PyTorch conversational-AI toolkit — ASR, speaker ID, diarization, enhancement; strong for custom pipelines."),

    # Diarization & alignment — who said what, when
    "pyannote/pyannote-audio": ("Diarization & alignment", "THE open speaker-diarization toolkit — state-of-the-art pipelines for 'who spoke when'; the de-facto standard."),
    "m-bain/whisperX": ("Diarization & alignment", "Whisper + forced alignment (word-level timestamps) + pyannote diarization — the best single pipeline for 'who said what, when'."),
    "MahmoudAshraf97/whisper-diarization": ("Diarization & alignment", "Ready-made faster-whisper + NeMo MSDD diarization pipeline — speaker-labeled transcripts with one command."),
    "juanmc2005/diart": ("Diarization & alignment", "Real-time speaker diarization — streaming 'who is speaking now' for live meeting monitoring."),

    # Streaming / live capture — VAD + realtime
    "KoljaB/RealtimeSTT": ("Streaming / live capture", "Low-latency streaming STT with built-in VAD and wake-word — the easiest way to wire live mic → text."),
    "collabora/WhisperLive": ("Streaming / live capture", "Whisper as a real-time websocket server — stream mic/RTSP audio in, live transcript out."),
    "snakers4/silero-vad": ("Streaming / live capture", "The standard pre-trained voice-activity detector — <1ms per chunk; gates every serious live pipeline."),
    "k2-fsa/sherpa-onnx": ("Streaming / live capture", "On-device streaming ASR + diarization + VAD via ONNX — 10 languages of bindings, runs from RPi to server, no internet."),

    # Transcription servers / APIs
    "speaches-ai/speaches": ("Transcription server / API", "OpenAI-compatible STT/TTS server on faster-whisper — drop-in self-hosted replacement for the Whisper API."),
    "ahmetoner/whisper-asr-webservice": ("Transcription server / API", "Dockerized Whisper ASR webservice — the long-standing self-hosted transcription endpoint."),

    # Transcript analysis — after the words land
    "DrDroidLab/voicesummary": ("Transcript analysis", "Open AI database for voice/call transcripts — extraction, labelling, classification, and call analytics."),
}

# Adjacent but deliberately excluded (kept honest in the report)
ADJACENT = [
    ("pipecat-ai/pipecat", "realtime voice-*agent* framework — building bots that talk, not transcribing meetings (see voice-agents report)"),
    ("livekit/agents", "voice-agent framework with transcription as a component — see voice-agents report"),
    ("TEN-framework/ten-framework", "conversational voice-AI agent framework — see voice-agents report"),
    ("Macoron/whisper.unity", "whisper.cpp in Unity — game/XR captioning, not meetings"),
    ("kaiser-data/claude-code-langfuse-tracing", "transcript observability for *Claude Code sessions*, not audio conversations"),
    ("coqui-ai/TTS", "text-to-*speech* — the other direction; see voice-agents report"),
]

# The pipeline stages for the verdict table
APPS = [n for n, (c, _) in TAXONOMY.items() if c == "Meeting assistant (end-to-end)"]

# ---- Load --------------------------------------------------------------------
with open(CLASSIFIED) as f:
    cl = json.load(f)
with open(GRAPH) as f:
    gr = json.load(f)

by_name = {r["full_name"]: r for r in cl["repos"]}
# tolerate renamed repos (old full_name in curation, new in dataset or vice versa)
ALIASES = {
    "NVIDIA/NeMo": "NVIDIA-NeMo/Speech",
    "usefulsensors/moonshine": "moonshine-ai/moonshine",
    "mediar-ai/screenpipe": "screenpipe/screenpipe",
    "Zackriya-Solutions/meeting-minutes": "Zackriya-Solutions/meetily",
}
for old, new in ALIASES.items():
    if old in by_name and new not in by_name:
        by_name[new] = by_name[old]

nodes_by_id = {n["id"]: n for n in gr["nodes"]}
name_to_nodeid = {n["full_name"]: n["id"] for n in gr["nodes"]}
for old, new in ALIASES.items():
    if old in name_to_nodeid and new not in name_to_nodeid:
        name_to_nodeid[new] = name_to_nodeid[old]

sel_names = list(TAXONOMY.keys())
sel_node_ids = {name_to_nodeid[n] for n in sel_names if n in name_to_nodeid}
inter_edges = [l for l in gr["links"]
               if l["source"] in sel_node_ids and l["target"] in sel_node_ids]

node_for = make_node_for(nodes_by_id, name_to_nodeid)

# ---- Helpers -----------------------------------------------------------------
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
  f"`scripts/reports/meeting_transcription.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)
order = ["Meeting assistant (end-to-end)", "ASR engine / model",
         "Diarization & alignment", "Streaming / live capture",
         "Transcription server / API", "Transcript analysis"]

# --- Executive summary / verdict
A("## TL;DR — which repo should you use?")
A("")
A("| Your situation | Pick | Why it wins |")
A("|---|---|---|")
verdict = [
    ("**Just want meetings transcribed + summarized, locally, today**",
     "`Zackriya-Solutions/meetily`",
     "The most complete self-hosted meeting notetaker: live transcription (Parakeet/Whisper), "
     "speaker diarization, and Ollama summaries — 100% on-device, macOS & Windows."),
    ("**Best transcript quality for *analysis* (who said what, when)**",
     "`m-bain/whisperX`",
     "Whisper + word-level alignment + pyannote diarization in one pipeline — the gold standard "
     "speaker-attributed transcript that every downstream analysis needs."),
    ("**Batch-transcribe a backlog of recordings on your own server**",
     "`rishikanthc/Scriberr` (app) on `SYSTRAN/faster-whisper` (engine)",
     "Docker web UI with diarization + summaries; faster-whisper gives ~4× realtime throughput."),
    ("**Live captions / monitor a meeting as it happens**",
     "`collabora/WhisperLive` or `KoljaB/RealtimeSTT` (+ `juanmc2005/diart` for live speakers)",
     "Streaming websocket transcription with VAD; diart adds real-time 'who is speaking now'."),
    ("**Maximum accuracy or throughput (GPU server)**",
     "`NVIDIA-NeMo/Speech` (Canary / Parakeet)",
     "Canary tops the Open ASR leaderboard; Parakeet transcribes at >2000× realtime."),
    ("**Analyze transcripts at scale (calls, voice agents)**",
     "`DrDroidLab/voicesummary`",
     "Purpose-built transcript database: extraction, labelling, classification, call analytics."),
    ("**Qualitative research interviews**",
     "`kaixxx/noScribe`",
     "Diarized transcripts plus an editor designed for coding/analyzing interview data."),
]
for sit, pick, why in verdict:
    A(f"| {sit} | {pick} | {why} |")
A("")
A("**The one-line verdict:** for *using* — **meetily**; for *building* — **whisperX** "
  "(quality pipeline) on **faster-whisper** (speed), with **pyannote** doing the speaker math "
  "underneath nearly everything.")
A("")

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} transcription/analysis projects** in your stars "
  f"(**{fmt_int(total_stars)}★** combined), organized along the meeting pipeline:")
for c in order:
    if cats.get(c):
        A(f"  - **{c}** ({len(cats[c])}): "
          + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(cats[c], key=lambda x: -by_name[x]['stars'])))
A("- **Mental model** — a meeting stack is a pipeline: **capture → VAD → ASR (transcribe) → "
  "diarize/align (who said what, when) → summarize/analyze**. The apps bundle it; "
  "everything else is a building block you compose.")
A("- **Diarization is the moat.** Raw ASR is commoditized (a dozen great engines below); the "
  "hard part of *meeting* transcription is speaker attribution — which is why `pyannote-audio` "
  "sits underneath whisperX, Scriberr, noScribe, and most of the apps.")
A("- **Whisper is the center of gravity, but no longer alone.** NVIDIA's Parakeet/Canary "
  "(NeMo) beat it on speed/accuracy, Moonshine beats it on-device, FunASR/SenseVoice lead for "
  "Chinese + emotion signals, and Kyutai/sherpa-onnx own true streaming.")
A("- **Analysis is the thin layer.** Once transcripts exist, only `voicesummary` (call "
  "analytics) and `noScribe` (qualitative coding) go beyond summarization — the "
  "conversation-intelligence layer is where open source is still thinnest.")
A("")

# --- Pipeline table
A("## The meeting pipeline at a glance")
A("")
A("| Stage | What happens | Tools in your stars |")
A("|---|---|---|")
A("| **Capture** | Tap mic + system audio (both sides of the call) | "
  "`meetily`, `screenpipe`, `ecoute`, `vibe` |")
A("| **VAD** | Detect speech vs. silence, segment the stream | "
  "`silero-vad`, built into `RealtimeSTT`, `sherpa-onnx` |")
A("| **ASR — transcribe** | Audio → text (batch or streaming) | "
  "`whisper`, `faster-whisper`, `whisper.cpp`, `distil-whisper`, `moonshine`, "
  "`NeMo`, `FunASR`, `SenseVoice`, `vosk`, `kaldi`, `espnet`, `speechbrain`, `kyutai` |")
A("| **Diarize / align** | Who said what, with word-level timestamps | "
  "`pyannote-audio`, `whisperX`, `whisper-diarization`, `diart` |")
A("| **Serve** | Expose transcription as an API | "
  "`speaches`, `whisper-asr-webservice`, `WhisperLive` |")
A("| **Summarize / analyze** | Notes, action items, labels, analytics | "
  "`meetily`, `Scriberr`, `transcriptionstream` (LLM summaries); "
  "`voicesummary`, `noScribe` (deeper analysis) |")
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
    "Meeting assistant (end-to-end)": "The bundled pipeline — capture, transcribe, diarize, "
        "summarize in one app. Pick one of these if you want a product, not a project.",
    "ASR engine / model": "The transcribers. Raw word-error-rate is near-parity at the top; "
        "choose by deployment target (CPU/GPU/edge), language coverage, and streaming support.",
    "Diarization & alignment": "Who said what, when — the part that turns a wall of text into "
        "an analyzable conversation. Hardest stage, fewest options, pyannote underneath most.",
    "Streaming / live capture": "Live transcription needs VAD, chunking, and endpointing — "
        "these own the real-time path.",
    "Transcription server / API": "Self-hosted OpenAI-compatible endpoints — point any "
        "Whisper-API client at your own box.",
    "Transcript analysis": "After the words land: extraction, labelling, classification, "
        "analytics. The thinnest open-source layer — most stacks stop at summarization.",
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

# --- Spotlight: the recommended stacks
A("## Three reference stacks")
A("")
A("**1. Zero-effort local notetaker** — install and forget:")
A("```")
A("meetily  (capture + Parakeet/Whisper ASR + diarization + Ollama summaries)")
A("```")
A("")
A("**2. Best-quality analysis pipeline** — for transcripts you'll actually mine:")
A("```")
A("recording → faster-whisper (ASR)")
A("          → whisperX (word-level alignment + pyannote diarization)")
A("          → voicesummary / your LLM (extraction, labels, analytics)")
A("```")
A("")
A("**3. Live monitoring** — captions and speaker tracking while the meeting runs:")
A("```")
A("mic/system audio → silero-vad → WhisperLive or RealtimeSTT (streaming ASR)")
A("                 → diart (live 'who is speaking')")
A("                 → ecoute-style LLM pass for live suggestions")
A("```")
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
  "'hub-like' transcription tools in your ecosystem:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between these tools** (top similarity edges where both endpoints are in "
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
    A("- _None yet — freshly starred repos need a graph rebuild to link up._")
A("")

# --- Maintenance / risk
A("## Maintenance & risk signal")
A("")
A("Bus factor = commit concentration (1 = single-maintainer risk). Several of the "
  "desktop apps are passion projects — check before betting a workflow on them.")
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

# --- Adjacent
A("## Adjacent (deliberately not listed here)")
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
A("- **Selection**: gap analysis against the 2026 open-source transcription landscape "
  "(25 repos newly starred for this report) + keyword scan (transcribe / diarization / asr / "
  "speech-to-text / meeting / vad) + manual curation into the meeting pipeline. Voice-*agent* "
  "frameworks and TTS were routed to the voice-agents report.")
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
    "category": "AI / Voice",
    "summary": (f"{len(present)} meeting-transcription & conversation-analysis projects "
                f"({fmt_int(total_stars)}★) across the pipeline: end-to-end notetakers, ASR "
                "engines, diarization, live streaming, servers, and transcript analytics — "
                "with a verdict per use case."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in order},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/meeting_transcription.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
