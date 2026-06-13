# Voice AI Agents — Landscape Report

> Derived from **kaiser-data**'s 1,243 starred repos (snapshot `2026-06-11T21:58:33.384Z`), cross-referenced with the repo-similarity graph (1,243 nodes / 4,017 edges, 31 communities).
>
> Generated 2026-06-13 by `scripts/reports/voice_agents.py` (regenerate any time — no API cost).

## Executive summary

- **28 voice-AI projects** in your stars (**574,235★** combined), organized along the voice-agent loop:
  - **Realtime voice-agent framework** (4): `pipecat`, `agents`, `ten-framework`, `fastrtc`
  - **Speech-to-text / ASR** (6): `whisper`, `whisper.cpp`, `faster-whisper`, `whisperX`, `RealtimeSTT`, `whisper.unity`
  - **Text-to-speech / TTS** (9): `TTS`, `bark`, `VoxCPM`, `chatterbox`, `Qwen3-TTS`, `supertonic`, `neutts`, `IMS-Toucan`, `voicebox-pytorch`
  - **Voice cloning / studio** (3): `Real-Time-Voice-Cloning`, `voicebox`, `OmniVoice-Studio`
  - **Speech-LLM / omni model** (1): `Qwen3-Omni`
  - **Voice-capable runtime / serving** (5): `LocalAI`, `cognitive-services-speech-sdk`, `Foundry-Local`, `Dot`, `picollm`
- **Mental model** — a voice agent is a real-time loop: **capture → VAD/turn-taking → STT (ears) → LLM/agent (brain) → TTS (voice) → stream back**. Latency budget is the whole game: every stage must be streaming, and total round-trip should land under ~800ms to feel conversational.
- **The orchestrators are the agents.** `pipecat`, `livekit/agents`, and `ten-framework` don't transcribe or synthesize themselves — they sequence the stages, handle barge-in (user interrupting the bot), and manage the WebRTC/telephony transport.
- **Two model trends.** (1) *Cascade* stacks (STT→LLM→TTS) still dominate because each piece is swappable and best-of-breed; (2) *omni / speech-native* models like `Qwen3-Omni` collapse the stack into one model for lower latency and richer prosody.
- **Whisper is the gravitational center of the ears.** Four of your STT picks (`whisper`, `whisper.cpp`, `faster-whisper`, `whisperX`) are Whisper or derivatives.

## The voice-agent loop at a glance

| Stage | What happens | Tools in your stars |
|---|---|---|
| **Transport / capture** | Stream mic audio in & speech out (WebRTC/SIP) | `pipecat`, `livekit/agents`, `fastrtc`, `ten-framework` |
| **VAD / turn-taking** | Detect speech, endpointing, barge-in | `RealtimeSTT` (built-in VAD); handled inside the frameworks |
| **STT — ears** | Audio → text, ideally streaming + timestamps | `whisper`, `whisper.cpp`, `faster-whisper`, `whisperX`, `RealtimeSTT` |
| **LLM / agent — brain** | Decide what to say / which tool to call | your LLM + agent frameworks (see agent-orchestration report) |
| **TTS — voice** | Text → natural, low-latency speech | `coqui-TTS`, `chatterbox`, `bark`, `VoxCPM`, `Qwen3-TTS`, `supertonic`, `neutts` |
| **Voice identity** | Clone / design a specific voice | `Real-Time-Voice-Cloning`, `voicebox`, `OmniVoice-Studio` |
| **Collapse the stack** | One speech-native model for all of it | `Qwen3-Omni` |
| **Host it** | Serve the models locally / in cloud | `LocalAI`, `Foundry-Local`, `Azure speech-sdk`, `picollm`, `Dot` |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [openai/whisper](https://github.com/openai/whisper) | Speech-to-text / ASR | Python | MIT | 102,488 | Mature | 40 | active | 1mo ago | 3.7y | 2 |
| [CorentinJ/Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning) | Voice cloning / studio | Python | NOASSERTION | 59,906 | Mature | 31 | slowing | 3mo ago | 7.1y | 0 |
| [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) | Speech-to-text / ASR | C++ | MIT | 50,646 | Classic | 94 | very active | 2d ago | 3.7y | 41 |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | Voice-capable runtime / serving | Go | MIT | 46,792 | Classic | 79 | very active | 0d ago | 3.2y | 11 |
| [coqui-ai/TTS](https://github.com/coqui-ai/TTS) | Text-to-speech / TTS | Python | MPL-2.0 | 45,540 | Abandoned | 10 | stale | 1.8y ago | 6.1y | 0 |
| [suno-ai/bark](https://github.com/suno-ai/bark) | Text-to-speech / TTS | Jupyter Notebook | MIT | 39,149 | Abandoned | 5 | stale | 1.8y ago | 3.2y | 0 |
| [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | Voice cloning / studio | TypeScript | MIT | 29,774 | Hot | 69 | active | 1mo ago | 4mo | 22 |
| [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | Text-to-speech / TTS | Python | Apache-2.0 | 28,454 | Hot | 78 | very active | 2d ago | 8mo | 14 |
| [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) | Text-to-speech / TTS | Python | MIT | 25,021 | Declining | 48 | active | 1d ago | 1.1y | 4 |
| [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Speech-to-text / ASR | Python | MIT | 23,549 | Declining | 24 | stale | 6mo ago | 3.3y | 0 |
| [m-bain/whisperX](https://github.com/m-bain/whisperX) | Speech-to-text / ASR | Python | BSD-2-Clause | 22,396 | Classic | 69 | very active | 9d ago | 3.5y | 5 |
| [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat) | Realtime voice-agent framework | Python | BSD-2-Clause | 12,772 | Mature | 79 | very active | 0d ago | 2.5y | 3 |
| [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | Text-to-speech / TTS | Python | Apache-2.0 | 11,883 | Declining | 36 | slowing | 2mo ago | 4mo | 1 |
| [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | Text-to-speech / TTS | Swift | MIT | 11,477 | Rising | 54 | active | 21d ago | 6mo | 6 |
| [livekit/agents](https://github.com/livekit/agents) | Realtime voice-agent framework | Python | Apache-2.0 | 10,945 | Mature | 99 | very active | 0d ago | 2.6y | 30 |
| [TEN-framework/ten-framework](https://github.com/TEN-framework/ten-framework) | Realtime voice-agent framework | Python | NOASSERTION | 10,666 | Hot | 81 | very active | 2d ago | 2.0y | 10 |
| [KoljaB/RealtimeSTT](https://github.com/KoljaB/RealtimeSTT) | Speech-to-text / ASR | Python | MIT | 9,890 | Mature | 61 | very active | 2d ago | 2.8y | 2 |
| [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | Voice cloning / studio | Python | NOASSERTION | 6,827 | Hot | 79 | very active | 0d ago | 2mo | 4 |
| [neuphonic/neutts](https://github.com/neuphonic/neutts) | Text-to-speech / TTS | Python | NOASSERTION | 5,993 | Declining | 36 | active | 0d ago | 8mo | 0 |
| [gradio-app/fastrtc](https://github.com/gradio-app/fastrtc) | Realtime voice-agent framework | JavaScript | MIT | 4,604 | Declining | 38 | slowing | 5mo ago | 1.7y | 0 |
| [QwenLM/Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni) | Speech-LLM / omni model | Jupyter Notebook | Apache-2.0 | 3,825 | Declining | 44 | active | 1mo ago | 8mo | 1 |
| [Azure-Samples/cognitive-services-speech-sdk](https://github.com/Azure-Samples/cognitive-services-speech-sdk) | Voice-capable runtime / serving | C# | MIT | 3,430 | Classic | 64 | active | 0d ago | 8.1y | 8 |
| [microsoft/Foundry-Local](https://github.com/microsoft/Foundry-Local) | Voice-capable runtime / serving | C++ | NOASSERTION | 2,361 | Hot | 94 | very active | 0d ago | 1.2y | 17 |
| [DigitalPhonetics/IMS-Toucan](https://github.com/DigitalPhonetics/IMS-Toucan) | Text-to-speech / TTS | Python | Apache-2.0 | 2,203 | Mature | 28 | slowing | 4mo ago | 4.9y | 0 |
| [alexpinel/Dot](https://github.com/alexpinel/Dot) | Voice-capable runtime / serving | JavaScript | GPL-3.0 | 1,908 | Abandoned | 1 | stale | 1.5y ago | 2.2y | 0 |
| [Macoron/whisper.unity](https://github.com/Macoron/whisper.unity) | Speech-to-text / ASR | C# | MIT | 733 | Declining | 5 | stale | 1.2y ago | 3.2y | 0 |
| [lucidrains/voicebox-pytorch](https://github.com/lucidrains/voicebox-pytorch) | Text-to-speech / TTS | Python | MIT | 691 | Abandoned | 6 | stale | 1.7y ago | 2.9y | 0 |
| [Picovoice/picollm](https://github.com/Picovoice/picollm) | Voice-capable runtime / serving | Python | Apache-2.0 | 312 | Mature | 60 | very active | 1d ago | 2.2y | 5 |

## By category

### Realtime voice-agent framework

_The orchestrators — they own the real-time loop, turn-taking, barge-in, and transport. This is where you actually *build* a voice agent._

- **[pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat)** · 12,772★ · Python · Mature  
  Open-source framework for voice & multimodal conversational AI; wires STT→LLM→TTS with interruptions, VAD, and pluggable vendors.  
  <sub>topics: ai, real-time, voice, voice-assistant, chatbot-framework, chatbots</sub>
- **[livekit/agents](https://github.com/livekit/agents)** · 10,945★ · Python · Mature  
  Realtime voice-AI agent framework on LiveKit's WebRTC transport — turn detection, telephony (SIP), and tool calling built in.  
  <sub>topics: ai, real-time, voice, video, agents, openai</sub>
- **[TEN-framework/ten-framework](https://github.com/TEN-framework/ten-framework)** · 10,666★ · Python · Hot  
  Low-latency framework for conversational voice-AI agents; graph of multimodal extensions for real-time pipelines.  
  <sub>topics: ai, multi-modal, real-time, video, voice</sub>
- **[gradio-app/fastrtc](https://github.com/gradio-app/fastrtc)** · 4,604★ · JavaScript · Declining  
  Python real-time audio/video (WebRTC) library — the browser transport layer that turns a model into a live voice app.  
  <sub>topics: artificial-intelligence, llm, python, real-time, speech-to-text, text-to-speech, hacktoberfest, hacktoberfest2025</sub>

### Speech-to-text / ASR

_The ears. Streaming + word timestamps + diarization matter more than raw accuracy once you're in a live conversation._

- **[openai/whisper](https://github.com/openai/whisper)** · 102,488★ · Python · Mature  
  The reference open ASR model — robust multilingual transcription via large-scale weak supervision.  
  <sub>topics: —</sub>
- **[ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)** · 50,646★ · C++ · Classic  
  C/C++ port of Whisper — runs on CPU/edge/mobile with no Python; the embeddable ASR workhorse.  
  <sub>topics: openai, speech-to-text, transformer, whisper, inference, speech-recognition</sub>
- **[SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)** · 23,549★ · Python · Declining  
  CTranslate2 reimplementation of Whisper — up to 4× faster, lower memory; the production STT default.  
  <sub>topics: deep-learning, inference, quantization, speech-recognition, speech-to-text, transformer, whisper, openai</sub>
- **[m-bain/whisperX](https://github.com/m-bain/whisperX)** · 22,396★ · Python · Classic  
  Whisper + word-level timestamps + speaker diarization — adds the 'who said what, when' a transcript agent needs.  
  <sub>topics: asr, speech, speech-recognition, speech-to-text, whisper</sub>
- **[KoljaB/RealtimeSTT](https://github.com/KoljaB/RealtimeSTT)** · 9,890★ · Python · Mature  
  Low-latency streaming STT with built-in voice-activity detection and wake-word — purpose-built for live voice agents.  
  <sub>topics: python, realtime, speech-to-text</sub>
- **[Macoron/whisper.unity](https://github.com/Macoron/whisper.unity)** · 733★ · C# · Declining  
  whisper.cpp bindings for Unity — on-device speech-to-text inside games/XR.  
  <sub>topics: asr, stt, speech-to-text, openai, speech-recognition, whisper, unity3d</sub>

### Text-to-speech / TTS

_The voice. The trade-off is naturalness vs. latency vs. on-device footprint; streaming (first-audio-chunk time) beats total render time for agents._

- **[coqui-ai/TTS](https://github.com/coqui-ai/TTS)** · 45,540★ · Python · Abandoned  
  Battle-tested deep-learning TTS toolkit — many models, voice cloning, 1000+ languages; the OSS TTS staple.  
  <sub>topics: python, text-to-speech, deep-learning, speech, pytorch, tts, vocoder, tacotron</sub>
- **[suno-ai/bark](https://github.com/suno-ai/bark)** · 39,149★ · Jupyter Notebook · Abandoned  
  Generative audio model — expressive, prompt-driven speech (laughs, music, SFX), not just plain narration.  
  <sub>topics: —</sub>
- **[OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM)** · 28,454★ · Python · Hot  
  Tokenizer-free multilingual TTS with creative voice design and strong zero-shot cloning.  
  <sub>topics: audio, deeplearning, minicpm, python, pytorch, speech, speech-synthesis, text-to-speech</sub>
- **[resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox)** · 25,021★ · Python · Declining  
  SoTA open-source TTS with emotion/exaggeration control — a credible ElevenLabs-class voice.  
  <sub>topics: —</sub>
- **[QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS)** · 11,883★ · Python · Declining  
  Qwen team's open TTS series — high-quality multilingual synthesis from a frontier-model lab.  
  <sub>topics: —</sub>
- **[supertone-inc/supertonic](https://github.com/supertone-inc/supertonic)** · 11,477★ · Swift · Rising  
  Lightning-fast on-device multilingual TTS running natively via ONNX — edge-friendly voice.  
  <sub>topics: cpp, csharp, go, ios, java, lightweight, nodejs, on-device</sub>
- **[neuphonic/neutts](https://github.com/neuphonic/neutts)** · 5,993★ · Python · Declining  
  Compact on-device TTS model focused on natural, low-footprint speech.  
  <sub>topics: —</sub>
- **[DigitalPhonetics/IMS-Toucan](https://github.com/DigitalPhonetics/IMS-Toucan)** · 2,203★ · Python · Mature  
  Controllable, fast TTS covering 7000+ languages — breadth-first multilingual synthesis.  
  <sub>topics: text-to-speech, toolkit, speech-synthesis, deep-learning, speech-processing, tts, pytorch, speech</sub>
- **[lucidrains/voicebox-pytorch](https://github.com/lucidrains/voicebox-pytorch)** · 691★ · Python · Abandoned  
  Clean PyTorch implementation of Meta's Voicebox — non-autoregressive flow-matching TTS research base.  
  <sub>topics: artificial-intelligence, deep-learning, text-to-speech</sub>

### Voice cloning / studio

_Give the agent a specific identity — clone a reference voice or design a new one. Mind consent/ethics here._

- **[CorentinJ/Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning)** · 59,906★ · Python · Mature  
  The classic 5-second voice-cloning demo (SV2TTS) — the repo that popularized OSS voice cloning.  
  <sub>topics: deep-learning, pytorch, tensorflow, tts, voice-cloning, python</sub>
- **[jamiepine/voicebox](https://github.com/jamiepine/voicebox)** · 29,774★ · TypeScript · Hot  
  Open-source AI voice studio — clone, dictate, and create voices through a polished app.  
  <sub>topics: ai, voice-clone, qwen3-tts, voice-ai, whisper, qwen3-tts-ui, cuda, mlx</sub>
- **[debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio)** · 6,827★ · Python · Hot  
  Local ElevenLabs alternative — voice cloning, design, and generation without the cloud.  
  <sub>topics: tts, voice-cloning, voice-generation, voice-ai, asr, elevenlabs, local-ai, self-hosted</sub>

### Speech-LLM / omni model

_The brain that natively hears and speaks — one model instead of a cascade, trading swappability for lower latency and better prosody._

- **[QwenLM/Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni)** · 3,825★ · Jupyter Notebook · Declining  
  Natively end-to-end omni-modal LLM (text/audio/vision) — collapses STT+LLM+TTS into one speech-native model.  
  <sub>topics: —</sub>

### Voice-capable runtime / serving

_Where the models actually run — local OpenAI-compatible servers or hosted SDKs that expose STT/TTS endpoints._

- **[mudler/LocalAI](https://github.com/mudler/LocalAI)** · 46,792★ · Go · Classic  
  Drop-in local AI engine exposing OpenAI-compatible TTS/STT/LLM endpoints — self-host the whole voice stack.  
  <sub>topics: llama, ai, llm, stable-diffusion, api, tts, musicgen, mamba</sub>
- **[Azure-Samples/cognitive-services-speech-sdk](https://github.com/Azure-Samples/cognitive-services-speech-sdk)** · 3,430★ · C# · Classic  
  Reference samples for Azure's hosted Speech SDK — STT/TTS/translation if you prefer a managed cloud.  
  <sub>topics: —</sub>
- **[microsoft/Foundry-Local](https://github.com/microsoft/Foundry-Local)** · 2,361★ · C++ · Hot  
  Microsoft's local model runtime bundling speech-to-text (Whisper) for offline, on-device voice.  
  <sub>topics: ai-sdk, chat-completions, foundry-local, gpu-acceleration, local-ai, microsoft, on-device-inference, onnx-runtime</sub>
- **[alexpinel/Dot](https://github.com/alexpinel/Dot)** · 1,908★ · JavaScript · Abandoned  
  Self-contained local app combining TTS, RAG, and LLMs — an all-local talking assistant.  
  <sub>topics: embeddings, llm, local, rag, standalone, standalone-app, document-chat, faiss</sub>
- **[Picovoice/picollm](https://github.com/Picovoice/picollm)** · 312★ · Python · Mature  
  On-device LLM inference from the Picovoice (Porcupine/Cheetah wake-word & STT) voice stack.  
  <sub>topics: llm, compression, efficient-inference, gemma, generative-ai, language-model, language-models, large-language-model</sub>

## Spotlight: the orchestration frameworks

These are the projects that make something a *voice agent* rather than a model. They sequence ears→brain→voice, cut latency, and — critically — handle **barge-in** so a user can interrupt the bot mid-sentence. Pick the framework first, then slot in STT/TTS.

- **[pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat)** · 12,772★ · Python — Open-source framework for voice & multimodal conversational AI; wires STT→LLM→TTS with interruptions, VAD, and pluggable vendors.
- **[livekit/agents](https://github.com/livekit/agents)** · 10,945★ · Python — Realtime voice-AI agent framework on LiveKit's WebRTC transport — turn detection, telephony (SIP), and tool calling built in.
- **[TEN-framework/ten-framework](https://github.com/TEN-framework/ten-framework)** · 10,666★ · Python — Low-latency framework for conversational voice-AI agents; graph of multimodal extensions for real-time pipelines.
- **[gradio-app/fastrtc](https://github.com/gradio-app/fastrtc)** · 4,604★ · JavaScript — Python real-time audio/video (WebRTC) library — the browser transport layer that turns a model into a live voice app.

## Graph analysis — how they relate

**Community clustering.** These 28 tools span **12 of the graph's 31 communities** — voice work is spread across the speech-model, agent-framework, and local-runtime neighborhoods rather than forming one tidy cluster.

- **Community 0** (8): `ggml-org/whisper.cpp`, `SYSTRAN/faster-whisper`, `m-bain/whisperX`, `Macoron/whisper.unity`, `suno-ai/bark`, `resemble-ai/chatterbox`, `neuphonic/neutts`, `debpalash/OmniVoice-Studio`
- **Community 6** (5): `coqui-ai/TTS`, `OpenBMB/VoxCPM`, `DigitalPhonetics/IMS-Toucan`, `lucidrains/voicebox-pytorch`, `CorentinJ/Real-Time-Voice-Cloning`
- **Community 4** (4): `pipecat-ai/pipecat`, `livekit/agents`, `TEN-framework/ten-framework`, `openai/whisper`
- **Community 28** (2): `QwenLM/Qwen3-TTS`, `QwenLM/Qwen3-Omni`
- **Community 8** (2): `mudler/LocalAI`, `Picovoice/picollm`

**Centrality (PageRank in the full 1,243-repo graph)** — most 'hub-like' voice tools in your ecosystem:

- `m-bain/whisperX` — PageRank 0.0024
- `ggml-org/whisper.cpp` — PageRank 0.0021
- `Macoron/whisper.unity` — PageRank 0.0019
- `openai/whisper` — PageRank 0.0016
- `CorentinJ/Real-Time-Voice-Cloning` — PageRank 0.0015
- `SYSTRAN/faster-whisper` — PageRank 0.0013
- `QwenLM/Qwen3-TTS` — PageRank 0.0012
- `QwenLM/Qwen3-Omni` — PageRank 0.0012
- `KoljaB/RealtimeSTT` — PageRank 0.0012
- `livekit/agents` — PageRank 0.0011

**Direct links between voice tools** (top similarity edges where both endpoints are in this report):

- `QwenLM/Qwen3-TTS` ⇄ `QwenLM/Qwen3-Omni` (w=2.500) — authors: wangxiongts
- `ggml-org/whisper.cpp` ⇄ `SYSTRAN/faster-whisper` (w=0.750) — topics: openai, speech-to-text, transformer, whisper
- `livekit/agents` ⇄ `TEN-framework/ten-framework` (w=0.621) — topics: ai, real-time, voice, video
- `m-bain/whisperX` ⇄ `Macoron/whisper.unity` (w=0.500) — topics: asr, speech-recognition, speech-to-text, whisper
- `ggml-org/whisper.cpp` ⇄ `Macoron/whisper.unity` (w=0.444) — topics: openai, speech-to-text, whisper, speech-recognition
- `TEN-framework/ten-framework` ⇄ `pipecat-ai/pipecat` (w=0.425) — topics: ai, real-time, voice
- `livekit/agents` ⇄ `pipecat-ai/pipecat` (w=0.383) — topics: ai, real-time, voice
- `ggml-org/whisper.cpp` ⇄ `m-bain/whisperX` (w=0.375) — topics: speech-to-text, whisper, speech-recognition
- `OpenBMB/VoxCPM` ⇄ `coqui-ai/TTS` (w=0.370) — topics: python, pytorch, speech, speech-synthesis
- `SYSTRAN/faster-whisper` ⇄ `Macoron/whisper.unity` (w=0.364) — topics: speech-recognition, speech-to-text, whisper, openai
- `m-bain/whisperX` ⇄ `SYSTRAN/faster-whisper` (w=0.350) — topics: speech-recognition, speech-to-text, whisper
- `OpenBMB/VoxCPM` ⇄ `DigitalPhonetics/IMS-Toucan` (w=0.344) — topics: pytorch, speech, speech-synthesis, text-to-speech
- `coqui-ai/TTS` ⇄ `DigitalPhonetics/IMS-Toucan` (w=0.336) — topics: text-to-speech, deep-learning, speech, pytorch
- `CorentinJ/Real-Time-Voice-Cloning` ⇄ `DigitalPhonetics/IMS-Toucan` (w=0.323) — topics: deep-learning, pytorch, tts
- `OpenBMB/VoxCPM` ⇄ `CorentinJ/Real-Time-Voice-Cloning` (w=0.300) — topics: python, pytorch, tts, voice-cloning
- …and 6 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting — voice models in particular churn fast.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| livekit/agents | 99 | Mature | very active | 5 | 18% | 357 |
| ggml-org/whisper.cpp | 94 | Classic | very active | 7 | 17% | 34 |
| microsoft/Foundry-Local | 94 | Hot | very active | 4 | 25% | 18 |
| TEN-framework/ten-framework | 81 | Hot | very active | 3 | 27% | 116 |
| pipecat-ai/pipecat | 79 | Mature | very active | 1 | 69% | 112 |
| debpalash/OmniVoice-Studio | 79 | Hot | very active | 1 | 97% | 15 |
| mudler/LocalAI | 79 | Classic | very active | 1 | 79% | 118 |
| OpenBMB/VoxCPM | 78 | Hot | very active | 2 | 41% | 14 |
| m-bain/whisperX | 69 | Classic | very active | 1 | 55% | 43 |
| jamiepine/voicebox | 69 | Hot | active | 1 | 74% | 25 |
| Azure-Samples/cognitive-services-speech-sdk | 64 | Classic | active | 3 | 27% | 106 |
| KoljaB/RealtimeSTT | 61 | Mature | very active | 1 | 94% | 42 |
| Picovoice/picollm | 60 | Mature | very active | 1 | 65% | 6 |
| supertone-inc/supertonic | 54 | Rising | active | 2 | 40% | 1 |
| resemble-ai/chatterbox | 48 | Declining | active | 2 | 25% | 1 |
| QwenLM/Qwen3-Omni | 44 | Declining | active | 1 | 100% | 0 |
| openai/whisper | 40 | Mature | active | 1 | 50% | 13 |
| gradio-app/fastrtc | 38 | Declining | slowing | 0 | 0% | 22 |
| QwenLM/Qwen3-TTS | 36 | Declining | slowing | 1 | 100% | 0 |
| neuphonic/neutts | 36 | Declining | active | 0 | 0% | 0 |
| CorentinJ/Real-Time-Voice-Cloning | 31 | Mature | slowing | 0 | 0% | 0 |
| DigitalPhonetics/IMS-Toucan | 28 | Mature | slowing | 0 | 0% | 14 |
| SYSTRAN/faster-whisper | 24 | Declining | stale | 0 | 0% | 21 |
| coqui-ai/TTS | 10 | Abandoned | stale | 0 | 0% | 98 |
| lucidrains/voicebox-pytorch | 6 | Abandoned | stale | 0 | 0% | 65 |
| Macoron/whisper.unity | 5 | Declining | stale | 0 | 0% | 12 |
| suno-ai/bark | 5 | Abandoned | stale | 0 | 0% | 0 |
| alexpinel/Dot | 1 | Abandoned | stale | 0 | 0% | 4 |

## Which one should you use?

| If you want… | Start with | Why |
|---|---|---|
| To build a phone/web voice agent fast | `pipecat-ai/pipecat` or `livekit/agents` | Purpose-built orchestrators with STT/LLM/TTS plugins, barge-in, and SIP/WebRTC transport. |
| Production STT at low cost/latency | `SYSTRAN/faster-whisper` | 4× faster Whisper via CTranslate2; the default server-side ASR. |
| On-device / embedded STT | `ggml-org/whisper.cpp` | No Python, runs on CPU/edge/mobile; pairs with `RealtimeSTT` for streaming + VAD. |
| Transcripts with speakers & timestamps | `m-bain/whisperX` | Word-level alignment + diarization — 'who said what, when'. |
| Best-quality open TTS voice | `resemble-ai/chatterbox` or `coqui-ai/TTS` | SoTA naturalness with emotion control (chatterbox); broad model zoo + cloning (coqui). |
| Fast on-device TTS | `supertone-inc/supertonic` or `neuphonic/neutts` | ONNX/edge-friendly synthesis for low-latency, offline voice. |
| To clone a specific voice | `OmniVoice-Studio` or `coqui-ai/TTS` | Local ElevenLabs-style cloning — mind consent/ethics. |
| Lowest latency / richest prosody | `QwenLM/Qwen3-Omni` | Speech-native omni model collapses STT+LLM+TTS into one — fewer hops. |
| Self-host the whole stack with one API | `mudler/LocalAI` | OpenAI-compatible TTS/STT/LLM endpoints; swap it under any framework above. |

## Adjacent (deliberately not listed as voice-AI tools)

- **Chainlit/chainlit** (12,204★) — conversational-AI *chat UI* (audio is secondary) — not a voice-pipeline framework
- **mastra-ai/mastra** (24,971★) — general TS agent framework with a TTS module — covered by the agent-orchestration report
- **VoltAgent/voltagent** (9,545★) — general TS agent platform that *can* do TTS — not voice-specific
- **Fosowl/agenticSeek** (26,501★) — autonomous local agent with an optional voice front-end — general agent, not a voice stack
- **mozilla-ai/llamafile** (24,890★) — single-file LLM runner that bundles whisper.cpp — general runtime, see inference reports
- **huggingface/transformers** (161,513★) — hosts most of these speech models, but far too broad to list as a 'voice' tool
- **unslothai/unsloth** (66,258★) — fine-tunes TTS/audio models among many others — a training tool, not a voice agent

## Methodology & caveats

- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (voice / speech / tts / stt / asr / whisper / transcribe / diarization / vad / wake-word / realtime-voice / conversational) + manual curation into the voice-agent loop. General agent frameworks, chat UIs, and broad training/runtime tools were routed to adjacent reports or excluded (see above).
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 28 · Snapshot: 2026-06-11T21:58:33.384Z</sub>
