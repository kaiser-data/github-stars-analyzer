# The AI Engineer's Stack — What's Fundamental, Must-Have, and Trending

> Derived from **kaiser-data**'s 2,304 starred repos (snapshot `2026-10-05T13:01:39.533Z`), cross-referenced with the repo-similarity graph (2,304 nodes / 7,632 edges, 40 communities) and the 2026 AI-engineering landscape.
>
> Generated 2026-10-05 by `scripts/reports/ai_engineer_stack.py` (regenerate any time — no API cost).

![Top tools by stars](assets/ai-engineer-stack-top-tools.svg)

![Tools per category](assets/ai-engineer-stack-categories.svg)


## The one thing to understand first

In 2026 the **model layer is commoditizing** — model differences matter less each quarter, and the infrastructure beneath your app (serving, vector search, basic RAG, tracing) is **largely solved**. The value has moved *up the stack*: to **reliability, evaluation, context engineering, and memory** for agentic systems. So this report does two jobs at once — it tells you **which repos to know** (Fundamental / Must-have / Trending) *and* **which problems are already solved** (integrate, don't rebuild) **vs. still frontier** (where you actually add value).

> **Rule of thumb:** if a capability is ✅ *Solved* below, your job is to *integrate the best repo well*. If it's 🔴 *Frontier*, that's where a portfolio project or a job actually gets you noticed.

## The three tiers

### Fundamental (13)

**Bedrock you must understand.** Long-lived base libraries and learning resources. Tools change; these don't. If you can't explain these, you're assembling black boxes.

- **[huggingface/transformers](https://github.com/huggingface/transformers)** · 166,966★ · _Base & training_  
  The model-definition framework — the de-facto way to load/run almost any open model. Know it cold.
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 130,358★ · _Inference & serving_  
  Inference in C/C++ — the primitive behind on-device/edge LLMs; teaches you what quantization actually costs.
- **[microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)** · 121,021★ · _Learning_  
  21-lesson on-ramp to building with generative AI — the gentle starting point.
- **[openai/whisper](https://github.com/openai/whisper)** · 109,986★ · _Voice & multimodal_  
  The reference open ASR model — the baseline for any speech-in pipeline.
- **[rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)** · 106,045★ · _Learning_  
  Build a GPT in PyTorch step by step — the single best way to actually understand what you're orchestrating.
- **[mlabonne/llm-course](https://github.com/mlabonne/llm-course)** · 83,291★ · _Learning_  
  Roadmap + notebooks from fundamentals to deployment — the structured curriculum.
- **[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)** · 78,835★ · _Learning_  
  The canonical prompt-engineering reference — still load-bearing in an agentic world.
- **[labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations)** · 67,520★ · _Learning_  
  60+ annotated paper implementations — read the architectures, don't just import them.
- **[deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed)** · 43,197★ · _Base & training_  
  Training-optimization library (ZeRO, offload) — how large models actually get trained on real hardware.
- **[facebookresearch/faiss](https://github.com/facebookresearch/faiss)** · 41,079★ · _Vector store_  
  The original similarity-search library — the math under every vector DB; understand it before reaching for one.
- **[Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning)** · 31,378★ · _Base & training_  
  Structured PyTorch training — the bridge between research code and reproducible training runs.
- **[karpathy/llm.c](https://github.com/karpathy/llm.c)** · 31,099★ · _Learning_  
  LLM training in raw C/CUDA — strips away the framework to show the actual compute.
- **[NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)** · 29,669★ · _RAG & retrieval_  
  A catalog of advanced RAG techniques with code — the reference when naive RAG isn't enough.

### Must-have (20)

**Your default production toolkit.** The repos you reach for on basically every project — the boring, load-bearing choices. Master integration, not novelty.

- **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** · 188,761★ · _Data & ingestion_  
  Search/scrape/crawl the web into LLM-ready data — the ingestion default for RAG & agents.
- **[ollama/ollama](https://github.com/ollama/ollama)** · 182,220★ · _Inference & serving_  
  One command to run open models locally — the dev-loop and prototyping default.
- **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** · 147,462★ · _Orchestration & agents_  
  The most-deployed agent/LLM framework — the lingua franca; you'll read code that uses it even if you don't.
- **[vllm-project/vllm](https://github.com/vllm-project/vllm)** · 93,206★ · _Inference & serving_  
  High-throughput serving engine (PagedAttention) — the production answer for self-hosting at scale.
- **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** · 91,689★ · _RAG & retrieval_  
  Batteries-included RAG engine with deep document understanding — RAG as a deployable product.
- **[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)** · 84,775★ · _Data & ingestion_  
  LLM-friendly open crawler/scraper — self-hosted ingestion when you don't want an API.
- **[unslothai/unsloth](https://github.com/unslothai/unsloth)** · 77,213★ · _Fine-tuning_  
  2× faster, lower-memory LoRA/QLoRA fine-tuning — the practical fine-tuning default.
- **[hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)** · 75,316★ · _Fine-tuning_  
  Unified fine-tuning UI/CLI for 100+ models — the no-code-ish path to a tuned model.
- **[BerriAI/litellm](https://github.com/BerriAI/litellm)** · 60,147★ · _Inference & serving_  
  OpenAI-compatible gateway to 100+ LLMs — swap/route/budget models from one endpoint. Non-negotiable glue.
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** · 59,356★ · _Orchestration & agents_  
  Role-playing multi-agent orchestration — the popular 'team of agents' framework.
- **[run-llama/llama_index](https://github.com/run-llama/llama_index)** · 52,410★ · _RAG & retrieval_  
  The leading data/RAG framework — connectors, indexing, query engines; the RAG default alongside LangChain.
- **[mudler/LocalAI](https://github.com/mudler/LocalAI)** · 49,394★ · _Inference & serving_  
  OpenAI-compatible local engine (LLM/vision/voice) — self-host the whole API surface.
- **[milvus-io/milvus](https://github.com/milvus-io/milvus)** · 46,317★ · _Vector store_  
  Cloud-native vector DB built for massive scale — when you outgrow a single box.
- **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** · 42,730★ · _Orchestration & agents_  
  Explicit graphs over implicit chains — the 2026 standard for *production-grade* agent control flow.
- **[stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)** · 38,503★ · _Orchestration & agents_  
  Program — don't prompt — LLMs; compile prompts against metrics. The antidote to prompt-spaghetti.
- **[sgl-project/sglang](https://github.com/sgl-project/sglang)** · 36,791★ · _Inference & serving_  
  Fast serving with structured-output + prefix-cache wins — vLLM's main rival; learn both.
- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 35,396★ · _Eval & observability_  
  Open-source LLM tracing/evals/prompts — you can't ship what you can't see (you run this).
- **[qdrant/qdrant](https://github.com/qdrant/qdrant)** · 34,934★ · _Vector store_  
  High-performance Rust vector DB — the popular standalone choice; great filtering.
- **[huggingface/smolagents](https://github.com/huggingface/smolagents)** · 29,680★ · _Orchestration & agents_  
  Barebones code-writing agents — the minimal mental model of what an agent loop *is*.
- **[chroma-core/chroma](https://github.com/chroma-core/chroma)** · 29,441★ · _Vector store_  
  The 'just works' embedded vector store — fastest path from zero to a working RAG.

### Trending (23)

**Where the energy is right now (2026).** Fast-moving, high-upside, often unstable. Learn these to stay current and to find differentiated things to build.

- **[obra/superpowers](https://github.com/obra/superpowers)** · 295,458★ · _Coding agents & MCP_  
  The headline agentic-skills framework — the most-starred repo in this whole set.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 179,723★ · _Coding agents & MCP_  
  Agent Skills — on-demand capability that's displacing always-on prompt bloat.
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 149,465★ · _Coding agents & MCP_  
  The agentic coding CLI — the flagship of the coding-agent wave (full ecosystem in the cc-setups report).
- **[github/spec-kit](https://github.com/github/spec-kit)** · 140,186★ · _Coding agents & MCP_  
  Spec-driven development toolkit — the 'write the spec, let the agent build' workflow.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 117,167★ · _Orchestration & agents_  
  Let agents drive real browsers — the computer-use frontier; high promise, still flaky.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 109,824★ · _Orchestration & agents_  
  Multi-agent trading framework — the template for *vertical* agent systems with real domain logic.
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 107,232★ · _Coding agents & MCP_  
  Gemini's terminal agent — the third major CLI harness; useful for model-shopping.
- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 95,829★ · _Coding agents & MCP_  
  The community MCP index — discovery for the fastest-growing integration ecosystem.
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 91,012★ · _Coding agents & MCP_  
  Reference MCP servers — MCP is the emerging standard for wiring tools/data into any agent.
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 90,020★ · _Coding agents & MCP_  
  Open autonomous software-engineering agent — the OSS face of the SWE-agent race.
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 83,401★ · _Orchestration & agents_  
  Long-horizon research+code SuperAgent — the 'deep research' pattern as a harness.
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 66,590★ · _Memory_  
  Universal memory layer for agents — the most-adopted bet on the unsolved memory problem.
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 59,413★ · _Memory_  
  Best-benchmarked open memory system — a strong contender in a still-open race.
- **[Aider-AI/aider](https://github.com/Aider-AI/aider)** · 49,374★ · _Coding agents & MCP_  
  AI pair-programming in the terminal with tight git integration — a beloved daily driver.
- **[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)** · 43,528★ · _Orchestration & agents_  
  Browser-automation CLI for agents — the lighter, scriptable take on web agents.
- **[agno-agi/agno](https://github.com/agno-agi/agno)** · 42,559★ · _Orchestration & agents_  
  Build/run/manage agent platforms — a fast-rising full-stack agent framework.
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 39,981★ · _RAG & retrieval_  
  Graph-augmented RAG that's simple and fast — the practical face of 'RAG beyond chunks'.
- **[google/langextract](https://github.com/google/langextract)** · 38,920★ · _Data & ingestion_  
  Structured extraction from unstructured text — turning documents into typed data.
- **[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** · 38,669★ · _RAG & retrieval_  
  Vectorless, reasoning-based retrieval — a bet that reasoning can replace embeddings.
- **[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)** · 37,827★ · _Coding agents & MCP_  
  Playwright as an MCP server — reliable, structured web control for agents.
- **[microsoft/graphrag](https://github.com/microsoft/graphrag)** · 36,226★ · _RAG & retrieval_  
  Graph-based RAG — structure-aware retrieval for global/whole-corpus questions.
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 22,385★ · _Eval & observability_  
  Eval-first LLM/agent observability — measuring agents, not just logging them.
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 11,713★ · _Eval & observability_  
  OpenTelemetry-based AI observability & eval — standards-based tracing for agents.

## What's solved vs. what's still frontier

The most useful map an AI engineer can carry: where to **stop building and integrate**, and where **building is still worth it**.

| Layer | Status | What that means for you | Your repos here |
|---|---|---|---|
| **Base & training** | ✅ Solved (for users) | HF Transformers + PyTorch are the substrate. Training *frontier* models isn't your job; using them is. | `transformers`, `DeepSpeed`, `pytorch-lightning` |
| **Inference & serving** | ✅ Solved | vLLM / SGLang / Ollama / llama.cpp cover edge→datacenter. Never write your own serving layer; pick by scale. | `ollama`, `llama.cpp`, `vllm`, `litellm`, `LocalAI` |
| **Vector store** | ✅ Solved | faiss/qdrant/milvus/chroma (+pgvector) are mature. Choose on ops + filtering needs, not capability. | `milvus`, `faiss`, `qdrant`, `chroma` |
| **RAG & retrieval** | 🟡 Split | Naive RAG (chunk→embed→retrieve→stuff) is commoditized. Advanced/agentic/graph retrieval (LightRAG, graphrag, PageIndex) is still frontier. | `ragflow`, `llama_index`, `LightRAG`, `PageIndex`, `graphrag` |
| **Orchestration & agents** | 🔴 Frontier | Frameworks are mature (langgraph). Reliable long-horizon autonomy is NOT — open agents trail humans badly on real workflows. | `langchain`, `browser-use`, `TradingAgents`, `deer-flow`, `crewAI` |
| **Memory** | 🔴 Open problem | mem0/mempalace are bets, not settled answers. Durable, selective, cheap long-term memory is unsolved. | `mem0`, `mempalace` |
| **Eval & observability** | 🟡 Split | Tracing is solved (langfuse/phoenix). Agent *evaluation* is frontier — SWE-bench is saturated; reliable eval harnesses are unsolved. | `langfuse`, `opik`, `phoenix` |
| **Fine-tuning** | 🟢 Mechanics solved | LoRA/QLoRA via unsloth/LlamaFactory is push-button. The real skill is knowing *when* to fine-tune vs RAG vs prompt. | `unsloth`, `LlamaFactory` |
| **Data & ingestion** | 🟡 Tooling solved | Crawling/OCR/extraction (firecrawl, crawl4ai, langextract) is solved. *Clean domain data* is still the real bottleneck. | `firecrawl`, `crawl4ai`, `langextract` |
| **Coding agents & MCP** | 🔴 Trending / unstable | Exploding fast; MCP is becoming the integration standard but the surface changes monthly. Learn now, expect churn. | `superpowers`, `skills`, `claude-code`, `spec-kit`, `gemini-cli` |
| **Voice & multimodal** | 🟡 Split | STT/TTS are solved (whisper et al.). Low-latency full-duplex voice agents are still hard — see the voice-agents report. | `whisper` |
| **Learning** | 📚 Reference | Bedrock knowledge — these don't go stale the way tools do. | `generative-ai-for-beginners`, `LLMs-from-scratch`, `llm-course`, `Prompt-Engineering-Guide`, `annotated_deep_learning_paper_implementations` |

**The short version:**

- ✅ **Solved — integrate, never rebuild:** inference & serving, vector search, the base model/runtime layer. Picking *well* is the skill; building it yourself is wasted effort.
- 🟡 **Split — solved at the bottom, frontier at the top:** RAG (naive=solved, graph/agentic=open), evaluation (tracing=solved, agent-evals=open), data (tools=solved, clean domain data=hard).
- 🔴 **Frontier — where to actually add value:** agent reliability & long-horizon autonomy, durable memory, trustworthy agent evaluation, and the still-churning coding-agent / MCP ecosystem. Open agents still trail humans badly on real-world workflows — that gap *is* the opportunity.

## What people are actually building right now

By 2026 a majority of organizations have agents in production. The application types that dominate, most-built first:

1. **RAG over private/domain data** — still the single most common production pattern. The bar has risen from 'it answers' to 'it answers *with good retrieval + evals*'.
2. **Task & research agents** — `langgraph`-style explicit-graph agents with tools, web access (`browser-use`/`firecrawl`), and memory (`mem0`).
3. **Coding agents & dev tools** — `claude-code`/`aider`/`OpenHands` + **MCP** servers; the fastest-growing category (full breakdown in the Claude-Code-setups report).
4. **Voice agents** — speech-in/speech-out; low latency is the moat (see voice-agents report).
5. **Vertical agent systems** — domain logic + multi-agent (e.g. `TradingAgents`); the highest-value, highest-difficulty class.

### Trending right now (by dataset momentum)

Ranked by a momentum signal (Hot/Rising lifecycle + recent age + 90-day commit velocity). This is *velocity*, not size — small fast-movers beat large mature repos here.

| Repo | Tier | ★ Stars | Age | 90d commits | Last push | Momentum |
|---|---|---|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | Trending | 295,458 | 12mo | 55 | 8d ago | 7 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Trending | 59,413 | 6mo | 601 | 2d ago | 7 |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Trending | 43,528 | 8mo | 89 | 2d ago | 7 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Trending | 149,465 | 1.6y | 211 | 0d ago | 5 |
| [github/spec-kit](https://github.com/github/spec-kit) | Trending | 140,186 | 1.1y | 801 | 2d ago | 5 |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Trending | 117,167 | 1.9y | 514 | 3d ago | 5 |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Trending | 109,824 | 1.8y | 231 | 2d ago | 5 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Trending | 107,232 | 1.5y | 175 | 0d ago | 5 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Trending | 95,829 | 1.8y | 3919 | 8d ago | 5 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Trending | 91,012 | 1.9y | 55 | 0d ago | 5 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Trending | 83,401 | 1.4y | 1312 | 0d ago | 5 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Trending | 38,669 | 1.5y | 170 | 0d ago | 5 |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Trending | 37,827 | 1.5y | 35 | 7d ago | 4 |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Must-have | 188,761 | 2.5y | 595 | 1d ago | 2 |
| [ollama/ollama](https://github.com/ollama/ollama) | Must-have | 182,220 | 3.3y | 294 | 1d ago | 2 |

## Projects to build (with the repos)

Tagged by *territory* — **Solved** = ship fast, low risk, great for a portfolio; **Frontier** = harder, but where you differentiate.

| Project | Stack | Territory | Level | Notes |
|---|---|---|---|---|
| **RAG assistant over your own docs** | llama_index + qdrant + litellm + langfuse (+ a reranker) | Solved territory | Beginner | Best first portfolio project. Everything exists — the value is doing retrieval quality + evals properly. |
| **Local-first private ChatGPT** | ollama + open-webui + chroma + whisper | Solved territory | Beginner | Cost/privacy play. 100% offline. Great for learning the full loop with zero API spend. |
| **Document → structured data pipeline** | firecrawl/MinerU + langextract + a vector store | Solved territory | Intermediate | High business value, low novelty risk. Turns messy PDFs/web into typed records. |
| **Agentic research assistant** | langgraph + browser-use + firecrawl + mem0 + langfuse | Frontier | Intermediate | The hard part is *reliability*, not wiring. This is where you differentiate. |
| **Graph-RAG knowledge base** | microsoft/graphrag or LightRAG + qdrant | Frontier | Intermediate | For global/whole-corpus questions naive RAG fails. Active research — a real edge if you nail it. |
| **Domain copilot with a tuned model** | unsloth (QLoRA) + llama_index RAG + opik evals | Mixed | Advanced | Decide fine-tune-vs-RAG with evidence (opik). The decision *is* the skill. |
| **Vertical multi-agent system** | crewAI/langgraph + TauricResearch/TradingAgents as a template + langfuse | Frontier | Advanced | Real domain logic + many agents = the highest-value, highest-difficulty class of project. |
| **Coding agent / dev tool** | claude-code + MCP servers (playwright-mcp, github-mcp) + codegraph | Trending | Intermediate | Build a tool for your own workflow. See the Claude-Code-setups report for the full ecosystem. |
| **Your own agent-eval harness** | phoenix/opik + a task suite + langgraph runner | Frontier | Advanced | Few good ones exist. Building trustworthy agent evals is genuinely unsolved — and very employable. |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Repo | Tier | Layer | Lang | ★ Stars | Lifecycle | Health | Activity | Last push | Age |
|---|---|---|---|---|---|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | Trending | Coding agents & MCP | Shell | 295,458 (▲4,081) | Hot | 73 | very active | 8d ago | 12mo |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Must-have | Data & ingestion | TypeScript | 188,761 (▲4,277) | Mature | 84 | very active | 1d ago | 2.5y |
| [ollama/ollama](https://github.com/ollama/ollama) | Must-have | Inference & serving | Go | 182,220 (▲547) | Classic | 83 | very active | 1d ago | 3.3y |
| [anthropics/skills](https://github.com/anthropics/skills) | Trending | Coding agents & MCP | Python | 179,723 (▲1,678) | Mature | 50 | active | 2d ago | 1.0y |
| [huggingface/transformers](https://github.com/huggingface/transformers) | Fundamental | Base & training | Python | 166,966 (▲337) | Classic | 100 | very active | 0d ago | 7.9y |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Trending | Coding agents & MCP | TypeScript | 149,465 (▲1,448) | Hot | 79 | very active | 0d ago | 1.6y |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Must-have | Orchestration & agents | Python | 147,462 (▲428) | Classic | 85 | very active | 0d ago | 4.0y |
| [github/spec-kit](https://github.com/github/spec-kit) | Trending | Coding agents & MCP | Python | 140,186 (▲1,361) | Hot | 84 | very active | 2d ago | 1.1y |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | Fundamental | Inference & serving | C++ | 130,358 (▲882) | Classic | 99 | very active | 0d ago | 3.6y |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | Fundamental | Learning | Jupyter Notebook | 121,021 (▲506) | Classic | 70 | very active | 0d ago | 3.3y |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Trending | Orchestration & agents | Python | 117,167 (▲931) | Hot | 79 | very active | 3d ago | 1.9y |
| [openai/whisper](https://github.com/openai/whisper) | Fundamental | Voice & multimodal | Python | 109,986 (▲414) | Mature | 46 | active | 1mo ago | 4.1y |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Trending | Orchestration & agents | Python | 109,824 (▲1,284) | Hot | 79 | very active | 2d ago | 1.8y |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Trending | Coding agents & MCP | TypeScript | 107,232 (▲73) | Hot | 95 | very active | 0d ago | 1.5y |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | Fundamental | Learning | Jupyter Notebook | 106,045 (▲499) | Classic | 56 | very active | 3d ago | 3.2y |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Trending | Coding agents & MCP | — | 95,829 (▲325) | Hot | 59 | very active | 8d ago | 1.8y |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | Must-have | Inference & serving | Python | 93,206 (▲545) | Classic | 99 | very active | 0d ago | 3.7y |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | Must-have | RAG & retrieval | Go | 91,689 (▲405) | Mature | 93 | very active | 1d ago | 2.8y |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Trending | Coding agents & MCP | TypeScript | 91,012 (▲428) | Hot | 94 | very active | 0d ago | 1.9y |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | Trending | Coding agents & MCP | TypeScript | 90,020 (▲890) | Mature | 99 | very active | 0d ago | 2.6y |
| [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | Must-have | Data & ingestion | Python | 84,775 (▲538) | Mature | 80 | very active | 0d ago | 2.4y |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Trending | Orchestration & agents | Python | 83,401 (▲439) | Hot | 87 | very active | 0d ago | 1.4y |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | Fundamental | Learning | — | 83,291 (▲154) | Declining | 13 | stale | 8mo ago | 3.3y |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | Fundamental | Learning | MDX | 78,835 (▲222) | Declining | 16 | stale | 6mo ago | 3.8y |
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | Must-have | Fine-tuning | Python | 77,213 (▲470) | Mature | 98 | very active | 0d ago | 2.9y |
| [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) | Must-have | Fine-tuning | Python | 75,316 (▲310) | Classic | 81 | very active | 7d ago | 3.4y |
| [labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | Fundamental | Learning | Python | 67,520 (▲15) | Declining | 17 | stale | 8mo ago | 6.1y |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Trending | Memory | Python | 66,590 (▲614) | Classic | 83 | very active | 0d ago | 3.3y |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Must-have | Inference & serving | Python | 60,147 (▲549) | Classic | 79 | very active | 0d ago | 3.2y |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Trending | Memory | Python | 59,413 (▲145) | Hot | 81 | very active | 2d ago | 6mo |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Must-have | Orchestration & agents | Python | 59,356 (▲351) | Mature | 89 | very active | 0d ago | 2.9y |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | Must-have | RAG & retrieval | Python | 52,410 (▲98) | Classic | 98 | very active | 4d ago | 3.9y |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | Must-have | Inference & serving | Go | 49,394 (▲132) | Classic | 79 | very active | 0d ago | 3.6y |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | Trending | Coding agents & MCP | Python | 49,374 (▲196) | Mature | 26 | slowing | 4mo ago | 3.4y |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | Must-have | Vector store | Go | 46,317 (▲64) | Classic | 99 | very active | 0d ago | 7.1y |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Trending | Orchestration & agents | Rust | 43,528 (▲350) | Hot | 77 | very active | 2d ago | 8mo |
| [deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed) | Fundamental | Base & training | Python | 43,197 (▲38) | Classic | 97 | very active | 0d ago | 6.7y |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Must-have | Orchestration & agents | Python | 42,730 (▲476) | Classic | 76 | very active | 0d ago | 3.2y |
| [agno-agi/agno](https://github.com/agno-agi/agno) | Trending | Orchestration & agents | Python | 42,559 (▲224) | Classic | 97 | very active | 0d ago | 4.4y |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | Fundamental | Vector store | C++ | 41,079 (▲101) | Classic | 99 | very active | 2d ago | 9.7y |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | Trending | RAG & retrieval | Python | 39,981 (▲132) | Mature | 78 | very active | 2d ago | 2.0y |
| [google/langextract](https://github.com/google/langextract) | Trending | Data & ingestion | Python | 38,920 (▲106) | Mature | 67 | active | 0d ago | 1.2y |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Trending | RAG & retrieval | Python | 38,669 (▲2,824) | Hot | 77 | very active | 0d ago | 1.5y |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | Must-have | Orchestration & agents | Python | 38,503 (▲233) | Classic | 83 | very active | 1d ago | 3.7y |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Trending | Coding agents & MCP | TypeScript | 37,827 (▲271) | Hot | 73 | very active | 7d ago | 1.5y |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | Must-have | Inference & serving | Python | 36,791 (▲370) | Mature | 99 | very active | 0d ago | 2.7y |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | Trending | RAG & retrieval | Python | 36,226 (▲129) | Mature | 72 | very active | 0d ago | 2.5y |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Must-have | Eval & observability | TypeScript | 35,396 (▲363) | Classic | 94 | very active | 0d ago | 3.4y |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | Must-have | Vector store | Rust | 34,934 (▲125) | Classic | 88 | very active | 0d ago | 6.4y |
| [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | Fundamental | Base & training | Python | 31,378 (▲18) | Classic | 68 | very active | 14d ago | 7.5y |
| [karpathy/llm.c](https://github.com/karpathy/llm.c) | Fundamental | Learning | Cuda | 31,099 (▲43) | Abandoned | 4 | stale | 1.3y ago | 2.5y |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | Must-have | Orchestration & agents | Python | 29,680 (▲196) | Mature | 56 | active | 5d ago | 1.8y |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | Fundamental | RAG & retrieval | Jupyter Notebook | 29,669 (▲74) | Mature | 58 | very active | 14d ago | 2.2y |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | Must-have | Vector store | Rust | 29,441 (▲71) | Classic | 83 | very active | 1d ago | 4.0y |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Trending | Eval & observability | Python | 22,385 (▲155) | Classic | 94 | very active | 0d ago | 3.4y |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Trending | Eval & observability | Python | 11,713 (▲104) | Classic | 83 | very active | 1d ago | 3.9y |

## Graph analysis — how they relate

**Community clustering.** These 56 repos span **18 of the graph's 40 communities** — the AI-engineering stack is genuinely cross-cutting, not one tidy neighborhood.

- **Community 0** (13): `firecrawl/firecrawl`, `langchain-ai/langchain`, `unclecode/crawl4ai`, `dair-ai/Prompt-Engineering-Guide`, `mem0ai/mem0`, `MemPalace/mempalace`, `crewAIInc/crewAI`, `Aider-AI/aider`, `langchain-ai/langgraph`, `agno-agi/agno`
- **Community 18** (6): `ollama/ollama`, `huggingface/transformers`, `vllm-project/vllm`, `hiyouga/LlamaFactory`, `sgl-project/sglang`, `huggingface/smolagents`
- **Community 14** (5): `rasbt/LLMs-from-scratch`, `labmlai/annotated_deep_learning_paper_implementations`, `deepspeedai/DeepSpeed`, `facebookresearch/faiss`, `Lightning-AI/pytorch-lightning`
- **Community 27** (4): `ggml-org/llama.cpp`, `openai/whisper`, `mlabonne/llm-course`, `unslothai/unsloth`
- **Community 17** (4): `BerriAI/litellm`, `langfuse/langfuse`, `comet-ml/opik`, `Arize-ai/phoenix`
- **Community 21** (4): `github/spec-kit`, `google-gemini/gemini-cli`, `punkpeye/awesome-mcp-servers`, `modelcontextprotocol/servers`
- **Community 9** (3): `microsoft/generative-ai-for-beginners`, `microsoft/playwright-mcp`, `microsoft/graphrag`
- **Community 24** (3): `infiniflow/ragflow`, `milvus-io/milvus`, `qdrant/qdrant`

**Centrality (PageRank in the full 2,304-repo graph)** — the most 'hub-like' AI-eng repos in your stars (good signal for *foundational*):

- `Lightning-AI/pytorch-lightning` — PageRank 0.0016 (Fundamental)
- `microsoft/generative-ai-for-beginners` — PageRank 0.0016 (Fundamental)
- `langchain-ai/langgraph` — PageRank 0.0013 (Must-have)
- `huggingface/smolagents` — PageRank 0.0012 (Must-have)
- `agno-agi/agno` — PageRank 0.0012 (Trending)
- `langchain-ai/langchain` — PageRank 0.0011 (Must-have)
- `microsoft/playwright-mcp` — PageRank 0.0011 (Trending)
- `VectifyAI/PageIndex` — PageRank 0.0010 (Trending)
- `qdrant/qdrant` — PageRank 0.0009 (Must-have)
- `microsoft/graphrag` — PageRank 0.0009 (Trending)

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). For *production* picks, prefer mature lifecycle + low single-author share; for *trending* picks, expect churn.

| Repo | Tier | Health | Lifecycle | Activity | Bus factor | Top-author share |
|---|---|---|---|---|---|---|
| huggingface/transformers | Fundamental | 100 | Classic | very active | 9 | 13% |
| ggml-org/llama.cpp | Fundamental | 99 | Classic | very active | 8 | 10% |
| facebookresearch/faiss | Fundamental | 99 | Classic | very active | 6 | 22% |
| vllm-project/vllm | Must-have | 99 | Classic | very active | 29 | 5% |
| sgl-project/sglang | Must-have | 99 | Mature | very active | 9 | 8% |
| milvus-io/milvus | Must-have | 99 | Classic | very active | 8 | 10% |
| OpenHands/OpenHands | Trending | 99 | Mature | very active | 6 | 13% |
| run-llama/llama_index | Must-have | 98 | Classic | very active | 11 | 14% |
| unslothai/unsloth | Must-have | 98 | Mature | very active | 10 | 17% |
| deepspeedai/DeepSpeed | Fundamental | 97 | Classic | very active | 5 | 14% |
| agno-agi/agno | Trending | 97 | Classic | very active | 8 | 12% |
| google-gemini/gemini-cli | Trending | 95 | Hot | very active | 4 | 19% |
| langfuse/langfuse | Must-have | 94 | Classic | very active | 4 | 16% |
| modelcontextprotocol/servers | Trending | 94 | Hot | very active | 5 | 18% |
| comet-ml/opik | Trending | 94 | Classic | very active | 4 | 14% |
| infiniflow/ragflow | Must-have | 93 | Mature | very active | 4 | 21% |
| crewAIInc/crewAI | Must-have | 89 | Mature | very active | 3 | 23% |
| qdrant/qdrant | Must-have | 88 | Classic | very active | 3 | 30% |
| bytedance/deer-flow | Trending | 87 | Hot | very active | 8 | 14% |
| langchain-ai/langchain | Must-have | 85 | Classic | very active | 2 | 35% |
| firecrawl/firecrawl | Must-have | 84 | Mature | very active | 2 | 39% |
| github/spec-kit | Trending | 84 | Hot | very active | 2 | 28% |
| ollama/ollama | Must-have | 83 | Classic | very active | 2 | 28% |
| chroma-core/chroma | Must-have | 83 | Classic | very active | 2 | 36% |
| stanfordnlp/dspy | Must-have | 83 | Classic | very active | 2 | 36% |
| mem0ai/mem0 | Trending | 83 | Classic | very active | 2 | 45% |
| Arize-ai/phoenix | Trending | 83 | Classic | very active | 2 | 41% |
| hiyouga/LlamaFactory | Must-have | 81 | Classic | very active | 5 | 19% |
| MemPalace/mempalace | Trending | 81 | Hot | very active | 2 | 47% |
| unclecode/crawl4ai | Must-have | 80 | Mature | very active | 1 | 61% |
| mudler/LocalAI | Must-have | 79 | Classic | very active | 1 | 55% |
| BerriAI/litellm | Must-have | 79 | Classic | very active | 1 | 66% |
| anthropics/claude-code | Trending | 79 | Hot | very active | 1 | 65% |
| browser-use/browser-use | Trending | 79 | Hot | very active | 1 | 62% |
| TauricResearch/TradingAgents | Trending | 79 | Hot | very active | 1 | 96% |
| HKUDS/LightRAG | Trending | 78 | Mature | very active | 1 | 60% |
| vercel-labs/agent-browser | Trending | 77 | Hot | very active | 2 | 44% |
| VectifyAI/PageIndex | Trending | 77 | Hot | very active | 1 | 51% |
| langchain-ai/langgraph | Must-have | 76 | Classic | very active | 1 | 61% |
| obra/superpowers | Trending | 73 | Hot | very active | 1 | 91% |
| microsoft/playwright-mcp | Trending | 73 | Hot | very active | 1 | 57% |
| microsoft/graphrag | Trending | 72 | Mature | very active | 1 | 56% |
| microsoft/generative-ai-for-beginners | Fundamental | 70 | Classic | very active | 2 | 36% |
| Lightning-AI/pytorch-lightning | Fundamental | 68 | Classic | very active | 1 | 54% |
| google/langextract | Trending | 67 | Mature | active | 1 | 74% |
| punkpeye/awesome-mcp-servers | Trending | 59 | Hot | very active | 1 | 59% |
| NirDiamant/RAG_Techniques | Fundamental | 58 | Mature | very active | 1 | 87% |
| rasbt/LLMs-from-scratch | Fundamental | 56 | Classic | very active | 1 | 64% |
| huggingface/smolagents | Must-have | 56 | Mature | active | 1 | 50% |
| anthropics/skills | Trending | 50 | Mature | active | 2 | 36% |
| openai/whisper | Fundamental | 46 | Mature | active | 2 | 33% |
| Aider-AI/aider | Trending | 26 | Mature | slowing | 0 | 0% |
| labmlai/annotated_deep_learning_paper_implementations | Fundamental | 17 | Declining | stale | 0 | 0% |
| dair-ai/Prompt-Engineering-Guide | Fundamental | 16 | Declining | stale | 0 | 0% |
| mlabonne/llm-course | Fundamental | 13 | Declining | stale | 0 | 0% |
| karpathy/llm.c | Fundamental | 4 | Abandoned | stale | 0 | 0% |

## Adjacent (deliberately not in the core list)

- **Comfy-Org/ComfyUI** (136,143★) — image/diffusion tooling — a different (creative) AI discipline, out of scope here
- **PaddlePaddle/PaddleOCR** (90,626★) — OCR engine — a data-ingestion building block, folded into 'Data & ingestion'
- **n8n-io/n8n** (206,698★) — workflow automation — orchestrates agents but isn't core AI-eng tooling (see agent-orchestration report)
- **microsoft/autogen** (61,256★) — multi-agent framework — slipping in activity; crewAI/langgraph lead the must-have slot now
- **nomic-ai/gpt4all** (77,384★) — local-LLM app — superseded for most by ollama; kept off the must-have list

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`, cross-checked against 2026 AI-engineering landscape reporting. No private calls; fully reproducible.
- **Tiers and the solved/frontier verdicts are opinionated** — a synthesis of dataset signal (stars, lifecycle, commit velocity) and the current state of the field, not a benchmark. Treat 'Trending' as *volatile by definition*.
- **Selection** favors recognizable, broadly-applicable AI-engineering tooling. The coding-agent/harness ecosystem and voice stack are summarized here but detailed in the Claude-Code-setups and voice-agents reports respectively.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.

<sub>Repos covered: 56 · Snapshot: 2026-10-05T13:01:39.533Z</sub>
