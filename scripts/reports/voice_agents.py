#!/usr/bin/env python3
"""
Generate a comprehensive report on Voice AI Agents found in the starred-repos
dataset: realtime voice-agent frameworks (the orchestrators), speech-to-text /
ASR (the ears), text-to-speech / TTS (the voice), voice cloning / studios,
speech-LLM / omni models (the brain), and voice-capable runtimes (the hosts).

Inputs:
  public/data/classified.json
  public/data/graph.json

Output:
  reports/voice-agents.md   (+ reports/voice-agents.meta.json)

Run: python3 scripts/reports/voice_agents.py
"""
import json
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLASSIFIED = os.path.join(ROOT, "public/data/classified.json")
GRAPH = os.path.join(ROOT, "public/data/graph.json")
SLUG = "voice-agents"
TITLE = "Voice AI Agents — Landscape Report"
OUT = os.path.join(ROOT, f"reports/{SLUG}.md")
META_OUT = os.path.join(ROOT, f"reports/{SLUG}.meta.json")

# ---- Curated taxonomy --------------------------------------------------------
# A voice agent is a loop: capture audio → VAD/turn-taking → STT (ears) →
# LLM/agent (brain) → TTS (voice) → stream back over a realtime transport.
# Each category below owns one stage; the frameworks stitch them together.
TAXONOMY = {
    # Realtime voice-agent frameworks — the orchestrators (the actual "agents")
    "pipecat-ai/pipecat": ("Realtime voice-agent framework", "Open-source framework for voice & multimodal conversational AI; wires STT→LLM→TTS with interruptions, VAD, and pluggable vendors."),
    "livekit/agents": ("Realtime voice-agent framework", "Realtime voice-AI agent framework on LiveKit's WebRTC transport — turn detection, telephony (SIP), and tool calling built in."),
    "TEN-framework/ten-framework": ("Realtime voice-agent framework", "Low-latency framework for conversational voice-AI agents; graph of multimodal extensions for real-time pipelines."),
    "gradio-app/fastrtc": ("Realtime voice-agent framework", "Python real-time audio/video (WebRTC) library — the browser transport layer that turns a model into a live voice app."),

    # Speech-to-text / ASR — the ears
    "openai/whisper": ("Speech-to-text / ASR", "The reference open ASR model — robust multilingual transcription via large-scale weak supervision."),
    "ggml-org/whisper.cpp": ("Speech-to-text / ASR", "C/C++ port of Whisper — runs on CPU/edge/mobile with no Python; the embeddable ASR workhorse."),
    "SYSTRAN/faster-whisper": ("Speech-to-text / ASR", "CTranslate2 reimplementation of Whisper — up to 4× faster, lower memory; the production STT default."),
    "m-bain/whisperX": ("Speech-to-text / ASR", "Whisper + word-level timestamps + speaker diarization — adds the 'who said what, when' a transcript agent needs."),
    "KoljaB/RealtimeSTT": ("Speech-to-text / ASR", "Low-latency streaming STT with built-in voice-activity detection and wake-word — purpose-built for live voice agents."),
    "Macoron/whisper.unity": ("Speech-to-text / ASR", "whisper.cpp bindings for Unity — on-device speech-to-text inside games/XR."),

    # Text-to-speech / TTS — the voice
    "coqui-ai/TTS": ("Text-to-speech / TTS", "Battle-tested deep-learning TTS toolkit — many models, voice cloning, 1000+ languages; the OSS TTS staple."),
    "suno-ai/bark": ("Text-to-speech / TTS", "Generative audio model — expressive, prompt-driven speech (laughs, music, SFX), not just plain narration."),
    "OpenBMB/VoxCPM": ("Text-to-speech / TTS", "Tokenizer-free multilingual TTS with creative voice design and strong zero-shot cloning."),
    "resemble-ai/chatterbox": ("Text-to-speech / TTS", "SoTA open-source TTS with emotion/exaggeration control — a credible ElevenLabs-class voice."),
    "QwenLM/Qwen3-TTS": ("Text-to-speech / TTS", "Qwen team's open TTS series — high-quality multilingual synthesis from a frontier-model lab."),
    "supertone-inc/supertonic": ("Text-to-speech / TTS", "Lightning-fast on-device multilingual TTS running natively via ONNX — edge-friendly voice."),
    "neuphonic/neutts": ("Text-to-speech / TTS", "Compact on-device TTS model focused on natural, low-footprint speech."),
    "DigitalPhonetics/IMS-Toucan": ("Text-to-speech / TTS", "Controllable, fast TTS covering 7000+ languages — breadth-first multilingual synthesis."),
    "lucidrains/voicebox-pytorch": ("Text-to-speech / TTS", "Clean PyTorch implementation of Meta's Voicebox — non-autoregressive flow-matching TTS research base."),

    # Voice cloning / studios
    "CorentinJ/Real-Time-Voice-Cloning": ("Voice cloning / studio", "The classic 5-second voice-cloning demo (SV2TTS) — the repo that popularized OSS voice cloning."),
    "jamiepine/voicebox": ("Voice cloning / studio", "Open-source AI voice studio — clone, dictate, and create voices through a polished app."),
    "debpalash/OmniVoice-Studio": ("Voice cloning / studio", "Local ElevenLabs alternative — voice cloning, design, and generation without the cloud."),

    # Speech-LLM / omni model — the brain that hears and speaks
    "QwenLM/Qwen3-Omni": ("Speech-LLM / omni model", "Natively end-to-end omni-modal LLM (text/audio/vision) — collapses STT+LLM+TTS into one speech-native model."),

    # Voice-capable runtime / serving — the host
    "mudler/LocalAI": ("Voice-capable runtime / serving", "Drop-in local AI engine exposing OpenAI-compatible TTS/STT/LLM endpoints — self-host the whole voice stack."),
    "microsoft/Foundry-Local": ("Voice-capable runtime / serving", "Microsoft's local model runtime bundling speech-to-text (Whisper) for offline, on-device voice."),
    "Azure-Samples/cognitive-services-speech-sdk": ("Voice-capable runtime / serving", "Reference samples for Azure's hosted Speech SDK — STT/TTS/translation if you prefer a managed cloud."),
    "Picovoice/picollm": ("Voice-capable runtime / serving", "On-device LLM inference from the Picovoice (Porcupine/Cheetah wake-word & STT) voice stack."),
    "alexpinel/Dot": ("Voice-capable runtime / serving", "Self-contained local app combining TTS, RAG, and LLMs — an all-local talking assistant."),
}

# Adjacent but deliberately excluded (kept honest in the report)
ADJACENT = [
    ("Chainlit/chainlit", "conversational-AI *chat UI* (audio is secondary) — not a voice-pipeline framework"),
    ("mastra-ai/mastra", "general TS agent framework with a TTS module — covered by the agent-orchestration report"),
    ("VoltAgent/voltagent", "general TS agent platform that *can* do TTS — not voice-specific"),
    ("Fosowl/agenticSeek", "autonomous local agent with an optional voice front-end — general agent, not a voice stack"),
    ("mozilla-ai/llamafile", "single-file LLM runner that bundles whisper.cpp — general runtime, see inference reports"),
    ("huggingface/transformers", "hosts most of these speech models, but far too broad to list as a 'voice' tool"),
    ("unslothai/unsloth", "fine-tunes TTS/audio models among many others — a training tool, not a voice agent"),
]

# Cross-cutting theme: the 'ears → brain → voice' realtime loop
PIPELINE_FRAMEWORKS = ["pipecat-ai/pipecat", "livekit/agents", "TEN-framework/ten-framework", "gradio-app/fastrtc"]

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

def node_for(name):
    nid = name_to_nodeid.get(name)
    return nodes_by_id.get(nid) if nid else None

# ---- Helpers -----------------------------------------------------------------
def fmt_int(n):
    try:
        return f"{int(n):,}"
    except Exception:
        return str(n)

def days_to_human(d):
    if d is None:
        return "?"
    d = int(d)
    if d < 30:
        return f"{d}d"
    if d < 365:
        return f"{d//30}mo"
    return f"{d/365:.1f}y"

def activity_label(r):
    dsp = r.get("days_since_push")
    c90 = r.get("commits_90d") or 0
    if dsp is None:
        return "unknown"
    if dsp <= 30 and c90 >= 20:
        return "very active"
    if dsp <= 60:
        return "active"
    if dsp <= 180:
        return "slowing"
    return "stale"

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
  f"`scripts/reports/voice_agents.py` (regenerate any time — no API cost).")
A("")

present = [n for n in sel_names if n in by_name]
total_stars = sum(by_name[n]["stars"] for n in present)
cats = {}
for n in present:
    cats.setdefault(TAXONOMY[n][0], []).append(n)
order = ["Realtime voice-agent framework", "Speech-to-text / ASR",
         "Text-to-speech / TTS", "Voice cloning / studio",
         "Speech-LLM / omni model", "Voice-capable runtime / serving"]

# --- Executive summary
A("## Executive summary")
A("")
A(f"- **{len(present)} voice-AI projects** in your stars (**{fmt_int(total_stars)}★** "
  f"combined), organized along the voice-agent loop:")
for c in order:
    if cats.get(c):
        A(f"  - **{c}** ({len(cats[c])}): "
          + ", ".join(f"`{x.split('/')[-1]}`" for x in sorted(cats[c], key=lambda x: -by_name[x]['stars'])))
A(f"- **Mental model** — a voice agent is a real-time loop: **capture → VAD/turn-taking → "
  f"STT (ears) → LLM/agent (brain) → TTS (voice) → stream back**. Latency budget is the "
  f"whole game: every stage must be streaming, and total round-trip should land under "
  f"~800ms to feel conversational.")
A(f"- **The orchestrators are the agents.** `pipecat`, `livekit/agents`, and `ten-framework` "
  f"don't transcribe or synthesize themselves — they sequence the stages, handle barge-in "
  f"(user interrupting the bot), and manage the WebRTC/telephony transport.")
A(f"- **Two model trends.** (1) *Cascade* stacks (STT→LLM→TTS) still dominate because each "
  f"piece is swappable and best-of-breed; (2) *omni / speech-native* models like "
  f"`Qwen3-Omni` collapse the stack into one model for lower latency and richer prosody.")
A(f"- **Whisper is the gravitational center of the ears.** Four of your STT picks "
  f"(`whisper`, `whisper.cpp`, `faster-whisper`, `whisperX`) are Whisper or derivatives.")
A("")

# --- Pipeline table
A("## The voice-agent loop at a glance")
A("")
A("| Stage | What happens | Tools in your stars |")
A("|---|---|---|")
A("| **Transport / capture** | Stream mic audio in & speech out (WebRTC/SIP) | "
  "`pipecat`, `livekit/agents`, `fastrtc`, `ten-framework` |")
A("| **VAD / turn-taking** | Detect speech, endpointing, barge-in | "
  "`RealtimeSTT` (built-in VAD); handled inside the frameworks |")
A("| **STT — ears** | Audio → text, ideally streaming + timestamps | "
  "`whisper`, `whisper.cpp`, `faster-whisper`, `whisperX`, `RealtimeSTT` |")
A("| **LLM / agent — brain** | Decide what to say / which tool to call | "
  "your LLM + agent frameworks (see agent-orchestration report) |")
A("| **TTS — voice** | Text → natural, low-latency speech | "
  "`coqui-TTS`, `chatterbox`, `bark`, `VoxCPM`, `Qwen3-TTS`, `supertonic`, `neutts` |")
A("| **Voice identity** | Clone / design a specific voice | "
  "`Real-Time-Voice-Cloning`, `voicebox`, `OmniVoice-Studio` |")
A("| **Collapse the stack** | One speech-native model for all of it | "
  "`Qwen3-Omni` |")
A("| **Host it** | Serve the models locally / in cloud | "
  "`LocalAI`, `Foundry-Local`, `Azure speech-sdk`, `picollm`, `Dot` |")
A("")

# --- Master comparison
A("## Master comparison")
A("")
A("Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; "
  "`Activity` is derived from days-since-push + 90-day commits.")
A("")
A("| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | "
  "Activity | Last push | Age | Contrib(90d) |")
A("|" + "---|" * 12)
for n in sorted(present, key=lambda x: -by_name[x]["stars"]):
    r = by_name[n]
    A("| [{name}]({url}) | {cat} | {lang} | {lic} | {stars} | {lc} | {hs} | "
      "{act} | {push} | {age} | {auth} |".format(
        name=n, url=r["url"], cat=TAXONOMY[n][0],
        lang=r.get("primary_language") or "—",
        lic=(r.get("license") or "—"),
        stars=fmt_int(r["stars"]),
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
    "Realtime voice-agent framework": "The orchestrators — they own the real-time loop, "
        "turn-taking, barge-in, and transport. This is where you actually *build* a voice agent.",
    "Speech-to-text / ASR": "The ears. Streaming + word timestamps + diarization matter more "
        "than raw accuracy once you're in a live conversation.",
    "Text-to-speech / TTS": "The voice. The trade-off is naturalness vs. latency vs. on-device "
        "footprint; streaming (first-audio-chunk time) beats total render time for agents.",
    "Voice cloning / studio": "Give the agent a specific identity — clone a reference voice or "
        "design a new one. Mind consent/ethics here.",
    "Speech-LLM / omni model": "The brain that natively hears and speaks — one model instead of "
        "a cascade, trading swappability for lower latency and better prosody.",
    "Voice-capable runtime / serving": "Where the models actually run — local OpenAI-compatible "
        "servers or hosted SDKs that expose STT/TTS endpoints.",
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

# --- Spotlight: orchestration frameworks
A("## Spotlight: the orchestration frameworks")
A("")
A("These are the projects that make something a *voice agent* rather than a model. They "
  "sequence ears→brain→voice, cut latency, and — critically — handle **barge-in** so a user "
  "can interrupt the bot mid-sentence. Pick the framework first, then slot in STT/TTS.")
A("")
for n in PIPELINE_FRAMEWORKS:
    r = by_name.get(n)
    if r:
        A(f"- **[{n}]({r['url']})** · {fmt_int(r['stars'])}★ · {r.get('primary_language') or '—'} — {TAXONOMY[n][1]}")
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
  f"**{len(comm)} of the graph's {len(gr['communities'])} communities** — voice work is "
  f"spread across the speech-model, agent-framework, and local-runtime neighborhoods rather "
  f"than forming one tidy cluster.")
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
  "'hub-like' voice tools in your ecosystem:")
A("")
for pr, n in ranked[:10]:
    A(f"- `{n}` — PageRank {pr:.4f}")
A("")

A("**Direct links between voice tools** (top similarity edges where both endpoints are in "
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
    A("- _None — the voice tools don't link tightly to each other in the similarity graph "
      "(they cluster with their broader speech-model / agent-framework neighbors instead)._")
A("")

# --- Maintenance / risk
A("## Maintenance & risk signal")
A("")
A("Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle "
  "+ activity before adopting — voice models in particular churn fast.")
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
    ("To build a phone/web voice agent fast", "`pipecat-ai/pipecat` or `livekit/agents`",
     "Purpose-built orchestrators with STT/LLM/TTS plugins, barge-in, and SIP/WebRTC transport."),
    ("Production STT at low cost/latency", "`SYSTRAN/faster-whisper`",
     "4× faster Whisper via CTranslate2; the default server-side ASR."),
    ("On-device / embedded STT", "`ggml-org/whisper.cpp`",
     "No Python, runs on CPU/edge/mobile; pairs with `RealtimeSTT` for streaming + VAD."),
    ("Transcripts with speakers & timestamps", "`m-bain/whisperX`",
     "Word-level alignment + diarization — 'who said what, when'."),
    ("Best-quality open TTS voice", "`resemble-ai/chatterbox` or `coqui-ai/TTS`",
     "SoTA naturalness with emotion control (chatterbox); broad model zoo + cloning (coqui)."),
    ("Fast on-device TTS", "`supertone-inc/supertonic` or `neuphonic/neutts`",
     "ONNX/edge-friendly synthesis for low-latency, offline voice."),
    ("To clone a specific voice", "`OmniVoice-Studio` or `coqui-ai/TTS`",
     "Local ElevenLabs-style cloning — mind consent/ethics."),
    ("Lowest latency / richest prosody", "`QwenLM/Qwen3-Omni`",
     "Speech-native omni model collapses STT+LLM+TTS into one — fewer hops."),
    ("Self-host the whole stack with one API", "`mudler/LocalAI`",
     "OpenAI-compatible TTS/STT/LLM endpoints; swap it under any framework above."),
]
for want, pick, why in guide:
    A(f"| {want} | {pick} | {why} |")
A("")

# --- Adjacent
A("## Adjacent (deliberately not listed as voice-AI tools)")
A("")
for name, why in ADJACENT:
    r = by_name.get(name)
    star = f" ({fmt_int(r['stars'])}★)" if r else ""
    A(f"- **{name}**{star} — {why}")
A("")

# --- Methodology
A("## Methodology & caveats")
A("")
A("- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external "
  "calls; fully reproducible.")
A("- **Selection**: keyword scan (voice / speech / tts / stt / asr / whisper / "
  "transcribe / diarization / vad / wake-word / realtime-voice / conversational) + manual "
  "curation into the voice-agent loop. General agent frameworks, chat UIs, and broad "
  "training/runtime tools were routed to adjacent reports or excluded (see above).")
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
    "summary": (f"{len(present)} voice-AI projects ({fmt_int(total_stars)}★) across the "
                "voice-agent loop: realtime frameworks, STT/ASR, TTS, voice cloning, "
                "speech-LLM/omni models, and voice-capable runtimes."),
    "tool_count": len(present),
    "total_stars": total_stars,
    "categories": {c: len(cats.get(c, [])) for c in order},
    "top_tools": [{"name": n, "stars": by_name[n]["stars"]} for n in top],
    "snapshot": gen,
    "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "generator": "scripts/reports/voice_agents.py",
}
with open(META_OUT, "w") as f:
    json.dump(meta, f, indent=2)

print(f"Wrote {OUT}")
print(f"Wrote {META_OUT}")
print(f"  tools: {len(present)} / {len(sel_names)} curated")
missing = [n for n in sel_names if n not in by_name]
if missing:
    print("  WARNING missing:", missing)
