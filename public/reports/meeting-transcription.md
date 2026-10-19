# Meeting Transcription & Conversation Analysis — Field Guide

> Derived from **kaiser-data**'s 2,398 starred repos (snapshot `2026-10-19T11:27:31.266Z`), cross-referenced with the repo-similarity graph (2,398 nodes / 8,025 edges, 39 communities).
>
> Generated 2026-10-19 by `scripts/reports/meeting_transcription.py` (regenerate any time — no API cost).

![Top tools by stars](assets/meeting-transcription-top-tools.svg)

![Tools per category](assets/meeting-transcription-categories.svg)


## TL;DR — which repo should you use?

| Your situation | Pick | Why it wins |
|---|---|---|
| **Just want meetings transcribed + summarized, locally, today** | `Zackriya-Solutions/meetily` | The most complete self-hosted meeting notetaker: live transcription (Parakeet/Whisper), speaker diarization, and Ollama summaries — 100% on-device, macOS & Windows. |
| **Best transcript quality for *analysis* (who said what, when)** | `m-bain/whisperX` | Whisper + word-level alignment + pyannote diarization in one pipeline — the gold standard speaker-attributed transcript that every downstream analysis needs. |
| **Batch-transcribe a backlog of recordings on your own server** | `rishikanthc/Scriberr` (app) on `SYSTRAN/faster-whisper` (engine) | Docker web UI with diarization + summaries; faster-whisper gives ~4× realtime throughput. |
| **Live captions / monitor a meeting as it happens** | `collabora/WhisperLive` or `KoljaB/RealtimeSTT` (+ `juanmc2005/diart` for live speakers) | Streaming websocket transcription with VAD; diart adds real-time 'who is speaking now'. |
| **Maximum accuracy or throughput (GPU server)** | `NVIDIA-NeMo/Speech` (Canary / Parakeet) | Canary tops the Open ASR leaderboard; Parakeet transcribes at >2000× realtime. |
| **Analyze transcripts at scale (calls, voice agents)** | `DrDroidLab/voicesummary` | Purpose-built transcript database: extraction, labelling, classification, call analytics. |
| **Qualitative research interviews** | `kaixxx/noScribe` | Diarized transcripts plus an editor designed for coding/analyzing interview data. |

**The one-line verdict:** for *using* — **meetily**; for *building* — **whisperX** (quality pipeline) on **faster-whisper** (speed), with **pyannote** doing the speaker math underneath nearly everything.

## Executive summary

- **33 transcription/analysis projects** in your stars (**482,429★** combined), organized along the meeting pipeline:
  - **Meeting assistant (end-to-end)** (8): `meetily`, `screenpipe`, `vibe`, `ecoute`, `Scriberr`, `whishper`, `noScribe`, `transcriptionstream`
  - **ASR engine / model** (14): `whisper`, `whisper.cpp`, `faster-whisper`, `FunASR`, `Speech`, `kaldi`, `vosk-api`, `speechbrain`, `moonshine`, `espnet`, `SenseVoice`, `distil-whisper`, `audio.cpp`, `delayed-streams-modeling`
  - **Diarization & alignment** (4): `whisperX`, `pyannote-audio`, `whisper-diarization`, `diart`
  - **Streaming / live capture** (4): `sherpa-onnx`, `silero-vad`, `RealtimeSTT`, `WhisperLive`
  - **Transcription server / API** (2): `speaches`, `whisper-asr-webservice`
  - **Transcript analysis** (1): `voicesummary`
- **Mental model** — a meeting stack is a pipeline: **capture → VAD → ASR (transcribe) → diarize/align (who said what, when) → summarize/analyze**. The apps bundle it; everything else is a building block you compose.
- **Diarization is the moat.** Raw ASR is commoditized (a dozen great engines below); the hard part of *meeting* transcription is speaker attribution — which is why `pyannote-audio` sits underneath whisperX, Scriberr, noScribe, and most of the apps.
- **Whisper is the center of gravity, but no longer alone.** NVIDIA's Parakeet/Canary (NeMo) beat it on speed/accuracy, Moonshine beats it on-device, FunASR/SenseVoice lead for Chinese + emotion signals, and Kyutai/sherpa-onnx own true streaming.
- **Analysis is the thin layer.** Once transcripts exist, only `voicesummary` (call analytics) and `noScribe` (qualitative coding) go beyond summarization — the conversation-intelligence layer is where open source is still thinnest.

## The meeting pipeline at a glance

| Stage | What happens | Tools in your stars |
|---|---|---|
| **Capture** | Tap mic + system audio (both sides of the call) | `meetily`, `screenpipe`, `ecoute`, `vibe` |
| **VAD** | Detect speech vs. silence, segment the stream | `silero-vad`, built into `RealtimeSTT`, `sherpa-onnx` |
| **ASR — transcribe** | Audio → text (batch or streaming) | `whisper`, `faster-whisper`, `whisper.cpp`, `distil-whisper`, `moonshine`, `NeMo`, `FunASR`, `SenseVoice`, `vosk`, `kaldi`, `espnet`, `speechbrain`, `kyutai` |
| **Diarize / align** | Who said what, with word-level timestamps | `pyannote-audio`, `whisperX`, `whisper-diarization`, `diart` |
| **Serve** | Expose transcription as an API | `speaches`, `whisper-asr-webservice`, `WhisperLive` |
| **Summarize / analyze** | Notes, action items, labels, analytics | `meetily`, `Scriberr`, `transcriptionstream` (LLM summaries); `voicesummary`, `noScribe` (deeper analysis) |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [openai/whisper](https://github.com/openai/whisper) | ASR engine / model | Python | MIT | 110,850 (▲577) | Mature | 45 | active | 1mo ago | 4.1y | 3 |
| [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) | ASR engine / model | C++ | MIT | 54,481 (▲215) | Classic | 99 | very active | 7d ago | 4.1y | 54 |
| [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | Meeting assistant (end-to-end) | Rust | MIT | 31,926 (▲346) | Hot | 72 | active | 1mo ago | 1.8y | 8 |
| [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | ASR engine / model | Python | MIT | 25,967 (▲169) | Classic | 60 | active | 3d ago | 3.7y | 7 |
| [m-bain/whisperX](https://github.com/m-bain/whisperX) | Diarization & alignment | Python | BSD-2-Clause | 24,667 (▲214) | Mature | 64 | active | 1d ago | 3.9y | 3 |
| [screenpipe/screenpipe](https://github.com/screenpipe/screenpipe) | Meeting assistant (end-to-end) | Rust | NOASSERTION | 21,985 (▲88) | Mature | 80 | very active | 0d ago | 2.3y | 3 |
| [modelscope/FunASR](https://github.com/modelscope/FunASR) | ASR engine / model | Python | MIT | 20,750 (▲118) | Classic | 80 | very active | 1d ago | 3.9y | 17 |
| [NVIDIA-NeMo/Speech](https://github.com/NVIDIA-NeMo/Speech) | ASR engine / model | Python | Apache-2.0 | 18,604 (▲36) | Classic | 100 | very active | 0d ago | 7.2y | 40 |
| [kaldi-asr/kaldi](https://github.com/kaldi-asr/kaldi) | ASR engine / model | Shell | NOASSERTION | 15,502 (▲11) | Abandoned | 9 | stale | 1.1y ago | 11.5y | 0 |
| [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | Streaming / live capture | C++ | Apache-2.0 | 15,372 (▲171) | Classic | 76 | very active | 2d ago | 4.1y | 33 |
| [alphacep/vosk-api](https://github.com/alphacep/vosk-api) | ASR engine / model | Jupyter Notebook | Apache-2.0 | 15,183 (▲15) | Mature | 46 | active | 4d ago | 7.1y | 2 |
| [speechbrain/speechbrain](https://github.com/speechbrain/speechbrain) | ASR engine / model | Python | Apache-2.0 | 11,887 (▲25) | Classic | 76 | very active | 5d ago | 6.5y | 15 |
| [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | ASR engine / model | C++ | NOASSERTION | 11,257 (▲55) | Mature | 78 | very active | 17d ago | 2.0y | 2 |
| [pyannote/pyannote-audio](https://github.com/pyannote/pyannote-audio) | Diarization & alignment | Jupyter Notebook | MIT | 10,671 (▲43) | Mature | 52 | active | 0d ago | 10.6y | 0 |
| [snakers4/silero-vad](https://github.com/snakers4/silero-vad) | Streaming / live capture | Python | MIT | 10,465 (▲71) | Classic | 64 | very active | 20d ago | 5.9y | 7 |
| [KoljaB/RealtimeSTT](https://github.com/KoljaB/RealtimeSTT) | Streaming / live capture | Python | MIT | 10,194 (▲22) | Classic | 67 | very active | 1d ago | 3.1y | 4 |
| [espnet/espnet](https://github.com/espnet/espnet) | ASR engine / model | Python | Apache-2.0 | 9,990 (▲8) | Classic | 84 | very active | 1d ago | 8.9y | 12 |
| [QwenAudio/SenseVoice](https://github.com/QwenAudio/SenseVoice) | ASR engine / model | C | MIT | 9,534 (▲51) | Mature | 71 | very active | 19d ago | 2.3y | 5 |
| [thewh1teagle/vibe](https://github.com/thewh1teagle/vibe) | Meeting assistant (end-to-end) | TypeScript | MIT | 7,823 (▲80) | Mature | 77 | very active | 13d ago | 2.8y | 2 |
| [SevaSk/ecoute](https://github.com/SevaSk/ecoute) | Meeting assistant (end-to-end) | Python | MIT | 6,037 (▼2) | Declining | 18 | stale | 6mo ago | 3.5y | 0 |
| [MahmoudAshraf97/whisper-diarization](https://github.com/MahmoudAshraf97/whisper-diarization) | Diarization & alignment | Jupyter Notebook | BSD-2-Clause | 5,663 (▲1) | Mature | 41 | slowing | 2mo ago | 3.7y | 2 |
| [collabora/WhisperLive](https://github.com/collabora/WhisperLive) | Streaming / live capture | Python | MIT | 4,324 (▲13) | Classic | 70 | very active | 0d ago | 3.5y | 7 |
| [huggingface/distil-whisper](https://github.com/huggingface/distil-whisper) | ASR engine / model | Python | MIT | 4,120 (▲4) | Abandoned | 4 | stale | 1.8y ago | 3.0y | 0 |
| [speaches-ai/speaches](https://github.com/speaches-ai/speaches) | Transcription server / API | Python | MIT | 3,723 (▲15) | Mature | 41 | active | 2d ago | 2.4y | 0 |
| [0xShug0/audio.cpp](https://github.com/0xShug0/audio.cpp) | ASR engine / model | C++ | NOASSERTION | 3,634 (▲204) | Hot | 80 | very active | 0d ago | 3mo | 17 |
| [ahmetoner/whisper-asr-webservice](https://github.com/ahmetoner/whisper-asr-webservice) | Transcription server / API | Python | MIT | 3,356 (▲1) | Mature | 54 | very active | 18d ago | 4.1y | 1 |
| [rishikanthc/Scriberr](https://github.com/rishikanthc/Scriberr) | Meeting assistant (end-to-end) | Go | MIT | 3,104 (▲12) | Mature | 43 | active | 29d ago | 2.0y | 1 |
| [pluja/whishper](https://github.com/pluja/whishper) | Meeting assistant (end-to-end) | Svelte | AGPL-3.0 | 3,092 (▲6) | Mature | 27 | slowing | 2mo ago | 3.2y | 0 |
| [kyutai-labs/delayed-streams-modeling](https://github.com/kyutai-labs/delayed-streams-modeling) | ASR engine / model | Python | Apache-2.0 | 3,041 | Declining | 15 | stale | 8mo ago | 1.3y | 0 |
| [kaixxx/noScribe](https://github.com/kaixxx/noScribe) | Meeting assistant (end-to-end) | Python | GPL-3.0 | 2,204 (▲10) | Classic | 71 | very active | 0d ago | 3.4y | 4 |
| [juanmc2005/diart](https://github.com/juanmc2005/diart) | Diarization & alignment | Python | MIT | 2,041 (▲1) | Mature | 27 | slowing | 4mo ago | 5.2y | 0 |
| [transcriptionstream/transcriptionstream](https://github.com/transcriptionstream/transcriptionstream) | Meeting assistant (end-to-end) | Python | GPL-3.0 | 946 (▼2) | Declining | 16 | stale | 9mo ago | 2.9y | 0 |
| [DrDroidLab/voicesummary](https://github.com/DrDroidLab/voicesummary) | Transcript analysis | Python | MIT | 36 | Declining | 7 | stale | 11mo ago | 1.2y | 0 |

## By category

### Meeting assistant (end-to-end)

_The bundled pipeline — capture, transcribe, diarize, summarize in one app. Pick one of these if you want a product, not a project._

- **[Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily)** · 31,926★ · Rust · Hot  
  Privacy-first local meeting notetaker (macOS/Win) — live Parakeet/Whisper transcription, speaker diarization, Ollama summaries; 100% on-device.  
  <sub>topics: meeting-minutes, meeting-notes, llm, mac, windows, rust, whisper, whisper-cpp</sub>
- **[screenpipe/screenpipe](https://github.com/screenpipe/screenpipe)** · 21,985★ · Rust · Mature  
  24/7 local screen + mic capture with transcription — a rolling, searchable record of everything said on your machine.  
  <sub>topics: ai, computer-vision, llm, machine-learning, multimodal, agents, agi, audio-recording</sub>
- **[thewh1teagle/vibe](https://github.com/thewh1teagle/vibe)** · 7,823★ · TypeScript · Mature  
  Polished cross-platform desktop app for offline transcription (Whisper) with batch, subtitles, and diarization.  
  <sub>topics: ai, cross-platform, desktop, openai, rust, transcribe, whisper</sub>
- **[SevaSk/ecoute](https://github.com/SevaSk/ecoute)** · 6,037★ · Python · Declining  
  Live meeting listener — real-time transcription of mic + speaker audio with GPT-suggested responses as the call happens.  
  <sub>topics: gpt-35-turbo, whisper-ai, windows</sub>
- **[rishikanthc/Scriberr](https://github.com/rishikanthc/Scriberr)** · 3,104★ · Go · Mature  
  Self-hosted (Docker) team transcription service — upload recordings, get diarized transcripts + optional local-LLM summaries.  
  <sub>topics: ai, audio, transcript, transcription</sub>
- **[pluja/whishper](https://github.com/pluja/whishper)** · 3,092★ · Svelte · Mature  
  Self-hosted transcription suite with web UI — transcribe, translate, edit, and export subtitles, fully offline.  
  <sub>topics: ai, audio-to-text, golang, subtitles, sveltekit, transcription, whisper, ui</sub>
- **[kaixxx/noScribe](https://github.com/kaixxx/noScribe)** · 2,204★ · Python · Classic  
  Transcription built for qualitative researchers — diarized interview transcripts with an editor designed for coding/analysis.  
  <sub>topics: audio-transcription, interview, pyannote, qualitative-research, transcription, faster-whisper</sub>
- **[transcriptionstream/transcriptionstream](https://github.com/transcriptionstream/transcriptionstream)** · 946★ · Python · Declining  
  Turnkey self-hosted drop-folder: transcription + diarization + Ollama summarization as one service.  
  <sub>topics: automation, diarization, llm, speaker-diarization, speech-recognition, transcription, whisper, ollama</sub>

### ASR engine / model

_The transcribers. Raw word-error-rate is near-parity at the top; choose by deployment target (CPU/GPU/edge), language coverage, and streaming support._

- **[openai/whisper](https://github.com/openai/whisper)** · 110,850★ · Python · Mature  
  The reference open ASR model — robust multilingual transcription; the baseline every meeting tool builds on.  
  <sub>topics: —</sub>
- **[ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)** · 54,481★ · C++ · Classic  
  C/C++ Whisper — runs on CPU/edge with no Python; powers many of the desktop meeting apps above.  
  <sub>topics: openai, speech-to-text, transformer, whisper, inference, speech-recognition</sub>
- **[SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)** · 25,967★ · Python · Classic  
  CTranslate2 Whisper — ~4× faster, lower memory; the production server-side transcription default.  
  <sub>topics: deep-learning, inference, quantization, speech-recognition, speech-to-text, transformer, whisper, openai</sub>
- **[modelscope/FunASR](https://github.com/modelscope/FunASR)** · 20,750★ · Python · Classic  
  Alibaba's production ASR toolkit — streaming + offline models with punctuation, timestamps, and speaker labels (Paraformer).  
  <sub>topics: pytorch, speech-recognition, paraformer, punctuation, speaker-diarization, voice-activity-detection, asr, multilingual-asr</sub>
- **[NVIDIA-NeMo/Speech](https://github.com/NVIDIA-NeMo/Speech)** · 18,604★ · Python · Classic  
  NVIDIA's speech stack — Parakeet (fastest open ASR) and Canary (top of the Open ASR leaderboard) live here, plus diarization recipes.  
  <sub>topics: machine-translation, speaker-recognition, asr, tts, generative-ai, deeplearning, neural-networks, speaker-diariazation</sub>
- **[kaldi-asr/kaldi](https://github.com/kaldi-asr/kaldi)** · 15,502★ · Shell · Abandoned  
  The classic ASR research toolkit — the foundation Vosk and a generation of speech systems were built on.  
  <sub>topics: kaldi, c-plus-plus, cuda, shell, speech-recognition, speech-to-text, speaker-verification, speaker-id</sub>
- **[alphacep/vosk-api](https://github.com/alphacep/vosk-api)** · 15,183★ · Jupyter Notebook · Mature  
  Offline ASR for 20+ languages with tiny (~50MB) models — bindings for ~10 languages; runs on a Raspberry Pi.  
  <sub>topics: speech-recognition, asr, voice-recognition, speech-to-text, android, ios, raspberry-pi, deep-learning</sub>
- **[speechbrain/speechbrain](https://github.com/speechbrain/speechbrain)** · 11,887★ · Python · Classic  
  PyTorch conversational-AI toolkit — ASR, speaker ID, diarization, enhancement; strong for custom pipelines.  
  <sub>topics: speech-recognition, speech-toolkit, speaker-recognition, speech-to-text, speech-enhancement, speech-separation, audio, audio-processing</sub>
- **[moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine)** · 11,257★ · C++ · Mature  
  Edge-first ASR beating Whisper at 5–15× speed on short segments — built for live, on-device captioning.  
  <sub>topics: intent-recognition, stt, tts, voice, voice-recognition</sub>
- **[espnet/espnet](https://github.com/espnet/espnet)** · 9,990★ · Python · Classic  
  End-to-end speech toolkit (ASR/TTS/translation/diarization) — research breadth across 100+ recipes.  
  <sub>topics: deep-learning, end-to-end, chainer, pytorch, kaldi, speech-recognition, speech-synthesis, speech-translation</sub>
- **[QwenAudio/SenseVoice](https://github.com/QwenAudio/SenseVoice)** · 9,534★ · C · Mature  
  Multilingual ASR with emotion recognition and audio-event detection — transcription plus conversational tone signals.  
  <sub>topics: asr, speech-recognition, speech-to-text, cross-lingual, pytorch, speech-emotion-recognition, multilingual, audio-analysis</sub>
- **[huggingface/distil-whisper](https://github.com/huggingface/distil-whisper)** · 4,120★ · Python · Abandoned  
  Distilled Whisper — ~6× faster, 49% smaller, within ~1% WER; batch-transcribe long meetings cheaply.  
  <sub>topics: audio, speech-recognition, whisper</sub>
- **[0xShug0/audio.cpp](https://github.com/0xShug0/audio.cpp)** · 3,634★ · C++ · Hot  
  Pure C++ ggml engine for audio models — STT, TTS and VAD in one runtime; whisper.cpp's design applied to the wider audio-model zoo.  
  <sub>topics: ai, amd-gpu, apple-silicon, asr, audio, cpp, edge-ai, ggml</sub>
- **[kyutai-labs/delayed-streams-modeling](https://github.com/kyutai-labs/delayed-streams-modeling)** · 3,041★ · Python · Declining  
  Kyutai's streaming STT — word-level timestamps over live streams with seconds-level latency.  
  <sub>topics: —</sub>

### Diarization & alignment

_Who said what, when — the part that turns a wall of text into an analyzable conversation. Hardest stage, fewest options, pyannote underneath most._

- **[m-bain/whisperX](https://github.com/m-bain/whisperX)** · 24,667★ · Python · Mature  
  Whisper + forced alignment (word-level timestamps) + pyannote diarization — the best single pipeline for 'who said what, when'.  
  <sub>topics: asr, speech, speech-recognition, speech-to-text, whisper</sub>
- **[pyannote/pyannote-audio](https://github.com/pyannote/pyannote-audio)** · 10,671★ · Jupyter Notebook · Mature  
  THE open speaker-diarization toolkit — state-of-the-art pipelines for 'who spoke when'; the de-facto standard.  
  <sub>topics: pytorch, speech-processing, speaker-diarization, speech-activity-detection, speaker-change-detection, speaker-embedding, voice-activity-detection, pretrained-models</sub>
- **[MahmoudAshraf97/whisper-diarization](https://github.com/MahmoudAshraf97/whisper-diarization)** · 5,663★ · Jupyter Notebook · Mature  
  Ready-made faster-whisper + NeMo MSDD diarization pipeline — speaker-labeled transcripts with one command.  
  <sub>topics: asr, speaker-diarization, speech, speech-recognition, speech-to-text, whisper</sub>
- **[juanmc2005/diart](https://github.com/juanmc2005/diart)** · 2,041★ · Python · Mature  
  Real-time speaker diarization — streaming 'who is speaking now' for live meeting monitoring.  
  <sub>topics: speaker-diarization, streaming-audio, real-time, speaker-embedding, deep-learning, transcription, voice-activity-detection</sub>

### Streaming / live capture

_Live transcription needs VAD, chunking, and endpointing — these own the real-time path._

- **[k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx)** · 15,372★ · C++ · Classic  
  On-device streaming ASR + diarization + VAD via ONNX — 10 languages of bindings, runs from RPi to server, no internet.  
  <sub>topics: asr, onnx, windows, linux, macos, cpp, android, ios</sub>
- **[snakers4/silero-vad](https://github.com/snakers4/silero-vad)** · 10,465★ · Python · Classic  
  The standard pre-trained voice-activity detector — <1ms per chunk; gates every serious live pipeline.  
  <sub>topics: voice-detection, voice-recognition, voice-commands, pytorch, onnx, voice-activity-detection, voice-control, onnx-runtime</sub>
- **[KoljaB/RealtimeSTT](https://github.com/KoljaB/RealtimeSTT)** · 10,194★ · Python · Classic  
  Low-latency streaming STT with built-in VAD and wake-word — the easiest way to wire live mic → text.  
  <sub>topics: python, realtime, speech-to-text</sub>
- **[collabora/WhisperLive](https://github.com/collabora/WhisperLive)** · 4,324★ · Python · Classic  
  Whisper as a real-time websocket server — stream mic/RTSP audio in, live transcript out.  
  <sub>topics: dictation, obs, openai, text-to-speech, translation, voice-recognition, whisper, tensorrt</sub>

### Transcription server / API

_Self-hosted OpenAI-compatible endpoints — point any Whisper-API client at your own box._

- **[speaches-ai/speaches](https://github.com/speaches-ai/speaches)** · 3,723★ · Python · Mature  
  OpenAI-compatible STT/TTS server on faster-whisper — drop-in self-hosted replacement for the Whisper API.  
  <sub>topics: docker, docker-compose, faster-whisper, openai-api, openai-whisper-translation, whisper, whisper-ai, openai-whisper</sub>
- **[ahmetoner/whisper-asr-webservice](https://github.com/ahmetoner/whisper-asr-webservice)** · 3,356★ · Python · Mature  
  Dockerized Whisper ASR webservice — the long-standing self-hosted transcription endpoint.  
  <sub>topics: automatic-speech-recognition, speech-recognition, speech-to-text, openai-whisper, docker, asr, speech</sub>

### Transcript analysis

_After the words land: extraction, labelling, classification, analytics. The thinnest open-source layer — most stacks stop at summarization._

- **[DrDroidLab/voicesummary](https://github.com/DrDroidLab/voicesummary)** · 36★ · Python · Declining  
  Open AI database for voice/call transcripts — extraction, labelling, classification, and call analytics.  
  <sub>topics: ai, database, livekit, llm, retell, vapi, voice-agents, voice-ai</sub>

## Three reference stacks

**1. Zero-effort local notetaker** — install and forget:
```
meetily  (capture + Parakeet/Whisper ASR + diarization + Ollama summaries)
```

**2. Best-quality analysis pipeline** — for transcripts you'll actually mine:
```
recording → faster-whisper (ASR)
          → whisperX (word-level alignment + pyannote diarization)
          → voicesummary / your LLM (extraction, labels, analytics)
```

**3. Live monitoring** — captions and speaker tracking while the meeting runs:
```
mic/system audio → silero-vad → WhisperLive or RealtimeSTT (streaming ASR)
                 → diart (live 'who is speaking')
                 → ecoute-style LLM pass for live suggestions
```

## Graph analysis — how they relate

**Community clustering.** These 33 tools span **11 of the graph's 39 communities**.

- **Community 20** (16): `rishikanthc/Scriberr`, `pluja/whishper`, `transcriptionstream/transcriptionstream`, `ggml-org/whisper.cpp`, `SYSTRAN/faster-whisper`, `modelscope/FunASR`, `kyutai-labs/delayed-streams-modeling`, `kaldi-asr/kaldi`, `speechbrain/speechbrain`, `0xShug0/audio.cpp`, `pyannote/pyannote-audio`, `m-bain/whisperX`, `MahmoudAshraf97/whisper-diarization`, `juanmc2005/diart`, `speaches-ai/speaches`, `ahmetoner/whisper-asr-webservice`
- **Community 14** (3): `Zackriya-Solutions/meetily`, `SevaSk/ecoute`, `k2-fsa/sherpa-onnx`
- **Community 9** (3): `thewh1teagle/vibe`, `espnet/espnet`, `snakers4/silero-vad`
- **Community 25** (2): `kaixxx/noScribe`, `huggingface/distil-whisper`
- **Community 21** (2): `openai/whisper`, `KoljaB/RealtimeSTT`
- **Community 15** (2): `collabora/WhisperLive`, `DrDroidLab/voicesummary`

**Centrality (PageRank in the full 2,398-repo graph)** — most 'hub-like' transcription tools in your ecosystem:

- `m-bain/whisperX` — PageRank 0.0009
- `MahmoudAshraf97/whisper-diarization` — PageRank 0.0007
- `ggml-org/whisper.cpp` — PageRank 0.0007
- `QwenAudio/SenseVoice` — PageRank 0.0006
- `modelscope/FunASR` — PageRank 0.0005
- `SYSTRAN/faster-whisper` — PageRank 0.0005
- `KoljaB/RealtimeSTT` — PageRank 0.0005
- `NVIDIA-NeMo/Speech` — PageRank 0.0005
- `ahmetoner/whisper-asr-webservice` — PageRank 0.0005
- `thewh1teagle/vibe` — PageRank 0.0004

**Direct links between these tools** (top similarity edges where both endpoints are in this report):

- `MahmoudAshraf97/whisper-diarization` ⇄ `m-bain/whisperX` (w=0.833) — topics: asr, speech, speech-recognition, speech-to-text
- `ggml-org/whisper.cpp` ⇄ `SYSTRAN/faster-whisper` (w=0.750) — topics: openai, speech-to-text, transformer, whisper
- `ahmetoner/whisper-asr-webservice` ⇄ `m-bain/whisperX` (w=0.550) — topics: speech-recognition, speech-to-text, asr, speech
- `ahmetoner/whisper-asr-webservice` ⇄ `MahmoudAshraf97/whisper-diarization` (w=0.444) — topics: speech-recognition, speech-to-text, asr, speech
- `m-bain/whisperX` ⇄ `SYSTRAN/faster-whisper` (w=0.350) — topics: speech-recognition, speech-to-text, whisper
- `QwenAudio/SenseVoice` ⇄ `modelscope/FunASR` (w=0.345) — topics: asr, speech-recognition, speech-to-text, pytorch; authors: LauraGPT
- `modelscope/FunASR` ⇄ `speechbrain/speechbrain` (w=0.291) — topics: pytorch, speech-recognition, speaker-diarization, asr; authors: li-lizhe
- `speechbrain/speechbrain` ⇄ `espnet/espnet` (w=0.291) — topics: speech-recognition, speech-enhancement, speech-separation, spoken-language-understanding
- `kaldi-asr/kaldi` ⇄ `m-bain/whisperX` (w=0.273) — topics: speech-recognition, speech-to-text, speech
- `speechbrain/speechbrain` ⇄ `SYSTRAN/faster-whisper` (w=0.265) — topics: speech-recognition, speech-to-text, deep-learning; authors: sungbin1015
- `MahmoudAshraf97/whisper-diarization` ⇄ `kaldi-asr/kaldi` (w=0.250) — topics: speech, speech-recognition, speech-to-text
- `transcriptionstream/transcriptionstream` ⇄ `huggingface/distil-whisper` (w=0.232) — topics: speech-recognition, whisper
- `transcriptionstream/transcriptionstream` ⇄ `MahmoudAshraf97/whisper-diarization` (w=0.231) — topics: speaker-diarization, speech-recognition, whisper
- `ahmetoner/whisper-asr-webservice` ⇄ `kaldi-asr/kaldi` (w=0.231) — topics: speech-recognition, speech-to-text, speech
- `transcriptionstream/transcriptionstream` ⇄ `m-bain/whisperX` (w=0.204) — topics: speech-recognition, whisper
- …and 13 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Several of the desktop apps are passion projects — check before betting a workflow on them.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| NVIDIA-NeMo/Speech | 100 | Classic | very active | 6 | 20% | 87 |
| ggml-org/whisper.cpp | 99 | Classic | very active | 11 | 11% | 45 |
| espnet/espnet | 84 | Classic | very active | 2 | 48% | 64 |
| screenpipe/screenpipe | 80 | Mature | very active | 1 | 76% | 497 |
| modelscope/FunASR | 80 | Classic | very active | 1 | 72% | 65 |
| 0xShug0/audio.cpp | 80 | Hot | very active | 1 | 51% | 23 |
| moonshine-ai/moonshine | 78 | Mature | very active | 1 | 99% | 23 |
| thewh1teagle/vibe | 77 | Mature | very active | 1 | 98% | 98 |
| speechbrain/speechbrain | 76 | Classic | very active | 4 | 24% | 17 |
| k2-fsa/sherpa-onnx | 76 | Classic | very active | 1 | 50% | 192 |
| Zackriya-Solutions/meetily | 72 | Hot | active | 2 | 44% | 12 |
| kaixxx/noScribe | 71 | Classic | very active | 2 | 48% | 9 |
| QwenAudio/SenseVoice | 71 | Mature | very active | 1 | 89% | 7 |
| collabora/WhisperLive | 70 | Classic | very active | 2 | 49% | 21 |
| KoljaB/RealtimeSTT | 67 | Classic | very active | 1 | 84% | 47 |
| m-bain/whisperX | 64 | Mature | active | 1 | 50% | 44 |
| snakers4/silero-vad | 64 | Classic | very active | 1 | 55% | 14 |
| SYSTRAN/faster-whisper | 60 | Classic | active | 2 | 45% | 21 |
| ahmetoner/whisper-asr-webservice | 54 | Mature | very active | 1 | 100% | 27 |
| pyannote/pyannote-audio | 52 | Mature | active | 0 | 0% | 18 |
| alphacep/vosk-api | 46 | Mature | active | 1 | 75% | 20 |
| openai/whisper | 45 | Mature | active | 2 | 33% | 13 |
| rishikanthc/Scriberr | 43 | Mature | active | 1 | 100% | 16 |
| MahmoudAshraf97/whisper-diarization | 41 | Mature | slowing | 1 | 50% | 0 |
| speaches-ai/speaches | 41 | Mature | active | 0 | 0% | 9 |
| pluja/whishper | 27 | Mature | slowing | 0 | 0% | 21 |
| juanmc2005/diart | 27 | Mature | slowing | 0 | 0% | 13 |
| SevaSk/ecoute | 18 | Declining | stale | 0 | 0% | 0 |
| transcriptionstream/transcriptionstream | 16 | Declining | stale | 0 | 0% | 0 |
| kyutai-labs/delayed-streams-modeling | 15 | Declining | stale | 0 | 0% | 0 |
| kaldi-asr/kaldi | 9 | Abandoned | stale | 0 | 0% | 0 |
| DrDroidLab/voicesummary | 7 | Declining | stale | 0 | 0% | 2 |
| huggingface/distil-whisper | 4 | Abandoned | stale | 0 | 0% | 0 |

## Adjacent (deliberately not listed here)

- **pipecat-ai/pipecat** (16,592★) — realtime voice-*agent* framework — building bots that talk, not transcribing meetings (see voice-agents report)
- **livekit/agents** (14,834★) — voice-agent framework with transcription as a component — see voice-agents report
- **TEN-framework/ten-framework** (11,180★) — conversational voice-AI agent framework — see voice-agents report
- **Macoron/whisper.unity** (755★) — whisper.cpp in Unity — game/XR captioning, not meetings
- **kaiser-data/claude-code-langfuse-tracing** (3★) — transcript observability for *Claude Code sessions*, not audio conversations
- **coqui-ai/TTS** (46,136★) — text-to-*speech* — the other direction; see voice-agents report

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: gap analysis against the 2026 open-source transcription landscape (25 repos newly starred for this report) + keyword scan (transcribe / diarization / asr / speech-to-text / meeting / vad) + manual curation into the meeting pipeline. Voice-*agent* frameworks and TTS were routed to the voice-agents report.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 33 · Snapshot: 2026-10-19T11:27:31.266Z</sub>
