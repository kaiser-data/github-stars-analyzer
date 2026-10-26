# The AI Engineer's Stack — What's Fundamental, Must-Have, and Trending

> Derived from **kaiser-data**'s 2,415 starred repos (snapshot `2026-10-26T11:46:04.025Z`), cross-referenced with the repo-similarity graph (2,415 nodes / 8,024 edges, 43 communities) and the 2026 AI-engineering landscape.
>
> Generated 2026-10-26 by `scripts/reports/ai_engineer_stack.py` (regenerate any time — no API cost).

![Top tools by stars](assets/ai-engineer-stack-top-tools.svg)

![Tools per category](assets/ai-engineer-stack-categories.svg)


## The one thing to understand first

In 2026 the **model layer is commoditizing** — model differences matter less each quarter, and the infrastructure beneath your app (serving, vector search, basic RAG, tracing) is **largely solved**. The value has moved *up the stack*: to **reliability, evaluation, context engineering, and memory** for agentic systems. So this report does two jobs at once — it tells you **which repos to know** (Fundamental / Must-have / Trending) *and* **which problems are already solved** (integrate, don't rebuild) **vs. still frontier** (where you actually add value).

> **Rule of thumb:** if a capability is ✅ *Solved* below, your job is to *integrate the best repo well*. If it's 🔴 *Frontier*, that's where a portfolio project or a job actually gets you noticed.

## The three tiers

### Fundamental (13)

**Bedrock you must understand.** Long-lived base libraries and learning resources. Tools change; these don't. If you can't explain these, you're assembling black boxes.

- **[huggingface/transformers](https://github.com/huggingface/transformers)** · 168,183★ · _Base & training_  
  The model-definition framework — the de-facto way to load/run almost any open model. Know it cold.
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 132,400★ · _Inference & serving_  
  Inference in C/C++ — the primitive behind on-device/edge LLMs; teaches you what quantization actually costs.
- **[microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)** · 122,198★ · _Learning_  
  21-lesson on-ramp to building with generative AI — the gentle starting point.
- **[openai/whisper](https://github.com/openai/whisper)** · 111,291★ · _Voice & multimodal_  
  The reference open ASR model — the baseline for any speech-in pipeline.
- **[rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)** · 107,311★ · _Learning_  
  Build a GPT in PyTorch step by step — the single best way to actually understand what you're orchestrating.
- **[mlabonne/llm-course](https://github.com/mlabonne/llm-course)** · 84,711★ · _Learning_  
  Roadmap + notebooks from fundamentals to deployment — the structured curriculum.
- **[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)** · 79,541★ · _Learning_  
  The canonical prompt-engineering reference — still load-bearing in an agentic world.
- **[labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations)** · 67,600★ · _Learning_  
  60+ annotated paper implementations — read the architectures, don't just import them.
- **[deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed)** · 43,275★ · _Base & training_  
  Training-optimization library (ZeRO, offload) — how large models actually get trained on real hardware.
- **[facebookresearch/faiss](https://github.com/facebookresearch/faiss)** · 41,214★ · _Vector store_  
  The original similarity-search library — the math under every vector DB; understand it before reaching for one.
- **[Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning)** · 31,433★ · _Base & training_  
  Structured PyTorch training — the bridge between research code and reproducible training runs.
- **[karpathy/llm.c](https://github.com/karpathy/llm.c)** · 31,219★ · _Learning_  
  LLM training in raw C/CUDA — strips away the framework to show the actual compute.
- **[NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)** · 30,010★ · _RAG & retrieval_  
  A catalog of advanced RAG techniques with code — the reference when naive RAG isn't enough.

### Must-have (20)

**Your default production toolkit.** The repos you reach for on basically every project — the boring, load-bearing choices. Master integration, not novelty.

- **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** · 195,479★ · _Data & ingestion_  
  Search/scrape/crawl the web into LLM-ready data — the ingestion default for RAG & agents.
- **[ollama/ollama](https://github.com/ollama/ollama)** · 184,829★ · _Inference & serving_  
  One command to run open models locally — the dev-loop and prototyping default.
- **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** · 148,485★ · _Orchestration & agents_  
  The most-deployed agent/LLM framework — the lingua franca; you'll read code that uses it even if you don't.
- **[vllm-project/vllm](https://github.com/vllm-project/vllm)** · 95,582★ · _Inference & serving_  
  High-throughput serving engine (PagedAttention) — the production answer for self-hosting at scale.
- **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** · 92,892★ · _RAG & retrieval_  
  Batteries-included RAG engine with deep document understanding — RAG as a deployable product.
- **[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)** · 86,290★ · _Data & ingestion_  
  LLM-friendly open crawler/scraper — self-hosted ingestion when you don't want an API.
- **[unslothai/unsloth](https://github.com/unslothai/unsloth)** · 78,581★ · _Fine-tuning_  
  2× faster, lower-memory LoRA/QLoRA fine-tuning — the practical fine-tuning default.
- **[hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)** · 75,741★ · _Fine-tuning_  
  Unified fine-tuning UI/CLI for 100+ models — the no-code-ish path to a tuned model.
- **[BerriAI/litellm](https://github.com/BerriAI/litellm)** · 62,055★ · _Inference & serving_  
  OpenAI-compatible gateway to 100+ LLMs — swap/route/budget models from one endpoint. Non-negotiable glue.
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** · 60,117★ · _Orchestration & agents_  
  Role-playing multi-agent orchestration — the popular 'team of agents' framework.
- **[run-llama/llama_index](https://github.com/run-llama/llama_index)** · 52,669★ · _RAG & retrieval_  
  The leading data/RAG framework — connectors, indexing, query engines; the RAG default alongside LangChain.
- **[mudler/LocalAI](https://github.com/mudler/LocalAI)** · 49,969★ · _Inference & serving_  
  OpenAI-compatible local engine (LLM/vision/voice) — self-host the whole API surface.
- **[milvus-io/milvus](https://github.com/milvus-io/milvus)** · 46,483★ · _Vector store_  
  Cloud-native vector DB built for massive scale — when you outgrow a single box.
- **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** · 43,924★ · _Orchestration & agents_  
  Explicit graphs over implicit chains — the 2026 standard for *production-grade* agent control flow.
- **[stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)** · 38,797★ · _Orchestration & agents_  
  Program — don't prompt — LLMs; compile prompts against metrics. The antidote to prompt-spaghetti.
- **[sgl-project/sglang](https://github.com/sgl-project/sglang)** · 38,194★ · _Inference & serving_  
  Fast serving with structured-output + prefix-cache wins — vLLM's main rival; learn both.
- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 36,512★ · _Eval & observability_  
  Open-source LLM tracing/evals/prompts — you can't ship what you can't see (you run this).
- **[qdrant/qdrant](https://github.com/qdrant/qdrant)** · 35,258★ · _Vector store_  
  High-performance Rust vector DB — the popular standalone choice; great filtering.
- **[huggingface/smolagents](https://github.com/huggingface/smolagents)** · 30,065★ · _Orchestration & agents_  
  Barebones code-writing agents — the minimal mental model of what an agent loop *is*.
- **[chroma-core/chroma](https://github.com/chroma-core/chroma)** · 29,583★ · _Vector store_  
  The 'just works' embedded vector store — fastest path from zero to a working RAG.

### Trending (24)

**Where the energy is right now (2026).** Fast-moving, high-upside, often unstable. Learn these to stay current and to find differentiated things to build.

- **[obra/superpowers](https://github.com/obra/superpowers)** · 305,321★ · _Coding agents & MCP_  
  The headline agentic-skills framework — the most-starred repo in this whole set.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 183,877★ · _Coding agents & MCP_  
  Agent Skills — on-demand capability that's displacing always-on prompt bloat.
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 153,420★ · _Coding agents & MCP_  
  The agentic coding CLI — the flagship of the coding-agent wave (full ecosystem in the cc-setups report).
- **[github/spec-kit](https://github.com/github/spec-kit)** · 142,957★ · _Coding agents & MCP_  
  Spec-driven development toolkit — the 'write the spec, let the agent build' workflow.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 119,178★ · _Orchestration & agents_  
  Let agents drive real browsers — the computer-use frontier; high promise, still flaky.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 115,250★ · _Orchestration & agents_  
  Multi-agent trading framework — the template for *vertical* agent systems with real domain logic.
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 108,398★ · _Coding agents & MCP_  
  Gemini's terminal agent — the third major CLI harness; useful for model-shopping.
- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 96,884★ · _Coding agents & MCP_  
  The community MCP index — discovery for the fastest-growing integration ecosystem.
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 91,884★ · _Coding agents & MCP_  
  Open autonomous software-engineering agent — the OSS face of the SWE-agent race.
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 91,575★ · _Coding agents & MCP_  
  Reference MCP servers — MCP is the emerging standard for wiring tools/data into any agent.
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 84,439★ · _Orchestration & agents_  
  Long-horizon research+code SuperAgent — the 'deep research' pattern as a harness.
- **[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)** · 73,018★ · _Coding agents & MCP_  
  Lighter-weight spec-driven development — agree on a change spec with the agent before it writes code.
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 67,839★ · _Memory_  
  Universal memory layer for agents — the most-adopted bet on the unsolved memory problem.
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 59,744★ · _Memory_  
  Best-benchmarked open memory system — a strong contender in a still-open race.
- **[Aider-AI/aider](https://github.com/Aider-AI/aider)** · 49,757★ · _Coding agents & MCP_  
  AI pair-programming in the terminal with tight git integration — a beloved daily driver.
- **[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)** · 44,615★ · _Orchestration & agents_  
  Browser-automation CLI for agents — the lighter, scriptable take on web agents.
- **[agno-agi/agno](https://github.com/agno-agi/agno)** · 42,899★ · _Orchestration & agents_  
  Build/run/manage agent platforms — a fast-rising full-stack agent framework.
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 40,340★ · _RAG & retrieval_  
  Graph-augmented RAG that's simple and fast — the practical face of 'RAG beyond chunks'.
- **[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** · 39,755★ · _RAG & retrieval_  
  Vectorless, reasoning-based retrieval — a bet that reasoning can replace embeddings.
- **[google/langextract](https://github.com/google/langextract)** · 39,045★ · _Data & ingestion_  
  Structured extraction from unstructured text — turning documents into typed data.
- **[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)** · 38,644★ · _Coding agents & MCP_  
  Playwright as an MCP server — reliable, structured web control for agents.
- **[microsoft/graphrag](https://github.com/microsoft/graphrag)** · 36,449★ · _RAG & retrieval_  
  Graph-based RAG — structure-aware retrieval for global/whole-corpus questions.
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 22,932★ · _Eval & observability_  
  Eval-first LLM/agent observability — measuring agents, not just logging them.
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 12,007★ · _Eval & observability_  
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
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Trending | 44,615 | 9mo | 103 | 0d ago | 7 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Trending | 59,744 | 6mo | 935 | 1d ago | 6 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Trending | 153,420 | 1.7y | 231 | 1d ago | 5 |
| [github/spec-kit](https://github.com/github/spec-kit) | Trending | 142,957 | 1.2y | 665 | 3d ago | 5 |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Trending | 119,178 | 2.0y | 490 | 2d ago | 5 |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Trending | 115,250 | 1.8y | 236 | 10d ago | 5 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Trending | 108,398 | 1.5y | 213 | 0d ago | 5 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Trending | 84,439 | 1.5y | 1687 | 0d ago | 5 |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | Trending | 73,018 | 1.2y | 299 | 0d ago | 5 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Trending | 39,755 | 1.6y | 231 | 0d ago | 5 |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Trending | 38,644 | 1.6y | 35 | 4d ago | 4 |
| [obra/superpowers](https://github.com/obra/superpowers) | Trending | 305,321 | 1.0y | 7 | 3d ago | 2 |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Must-have | 195,479 | 2.5y | 707 | 0d ago | 2 |
| [ollama/ollama](https://github.com/ollama/ollama) | Must-have | 184,829 | 3.3y | 366 | 0d ago | 2 |
| [anthropics/skills](https://github.com/anthropics/skills) | Trending | 183,877 | 1.1y | 14 | 17d ago | 2 |

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
| [obra/superpowers](https://github.com/obra/superpowers) | Trending | Coding agents & MCP | Shell | 305,321 (▲759) | Mature | 64 | active | 3d ago | 1.0y |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Must-have | Data & ingestion | TypeScript | 195,479 (▲554) | Mature | 88 | very active | 0d ago | 2.5y |
| [ollama/ollama](https://github.com/ollama/ollama) | Must-have | Inference & serving | Go | 184,829 (▲190) | Classic | 88 | very active | 0d ago | 3.3y |
| [anthropics/skills](https://github.com/anthropics/skills) | Trending | Coding agents & MCP | Python | 183,877 (▲412) | Mature | 44 | active | 17d ago | 1.1y |
| [huggingface/transformers](https://github.com/huggingface/transformers) | Fundamental | Base & training | Python | 168,183 (▲108) | Classic | 100 | very active | 0d ago | 8.0y |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Trending | Coding agents & MCP | TypeScript | 153,420 (▲155) | Hot | 78 | very active | 1d ago | 1.7y |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Must-have | Orchestration & agents | Python | 148,485 (▲116) | Classic | 79 | very active | 0d ago | 4.0y |
| [github/spec-kit](https://github.com/github/spec-kit) | Trending | Coding agents & MCP | Python | 142,957 (▲254) | Hot | 84 | very active | 3d ago | 1.2y |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | Fundamental | Inference & serving | C++ | 132,400 (▲172) | Classic | 99 | very active | 0d ago | 3.6y |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | Fundamental | Learning | Jupyter Notebook | 122,198 (▲121) | Classic | 70 | very active | 2d ago | 3.4y |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Trending | Orchestration & agents | Python | 119,178 (▲131) | Hot | 79 | very active | 2d ago | 2.0y |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Trending | Orchestration & agents | Python | 115,250 (▲1,659) | Hot | 78 | very active | 10d ago | 1.8y |
| [openai/whisper](https://github.com/openai/whisper) | Fundamental | Voice & multimodal | Python | 111,291 (▲99) | Mature | 44 | active | 1mo ago | 4.1y |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Trending | Coding agents & MCP | TypeScript | 108,398 (▲544) | Hot | 95 | very active | 0d ago | 1.5y |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | Fundamental | Learning | Jupyter Notebook | 107,311 (▲97) | Classic | 53 | active | 24d ago | 3.3y |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Trending | Coding agents & MCP | — | 96,884 (▲59) | Mature | 60 | very active | 3d ago | 1.9y |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | Must-have | Inference & serving | Python | 95,582 (▲260) | Classic | 99 | very active | 0d ago | 3.7y |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | Must-have | RAG & retrieval | Go | 92,892 (▲85) | Mature | 94 | very active | 0d ago | 2.9y |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | Trending | Coding agents & MCP | TypeScript | 91,884 (▲151) | Mature | 89 | very active | 0d ago | 2.6y |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Trending | Coding agents & MCP | TypeScript | 91,575 (▲31) | Mature | 79 | very active | 1d ago | 1.9y |
| [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | Must-have | Data & ingestion | Python | 86,290 (▲117) | Mature | 80 | very active | 0d ago | 2.5y |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | Fundamental | Learning | — | 84,711 (▲51) | Declining | 11 | stale | 8mo ago | 3.4y |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Trending | Orchestration & agents | Python | 84,439 (▲61) | Hot | 87 | very active | 0d ago | 1.5y |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | Fundamental | Learning | MDX | 79,541 (▲49) | Declining | 14 | stale | 7mo ago | 3.9y |
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | Must-have | Fine-tuning | Python | 78,581 (▲62) | Mature | 80 | very active | 0d ago | 2.9y |
| [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) | Must-have | Fine-tuning | Python | 75,741 (▲31) | Classic | 80 | very active | 5d ago | 3.4y |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | Trending | Coding agents & MCP | TypeScript | 73,018 (▲125) | Hot | 88 | very active | 0d ago | 1.2y |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Trending | Memory | Python | 67,839 (▲91) | Classic | 83 | very active | 3d ago | 3.4y |
| [labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | Fundamental | Learning | Python | 67,600 (▲4) | Mature | 47 | active | 1d ago | 6.2y |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Must-have | Inference & serving | Python | 62,055 (▲88) | Classic | 99 | very active | 0d ago | 3.3y |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Must-have | Orchestration & agents | Python | 60,117 (▲53) | Classic | 89 | very active | 0d ago | 3.0y |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Trending | Memory | Python | 59,744 (▲18) | Rising | 76 | very active | 1d ago | 6mo |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | Must-have | RAG & retrieval | Python | 52,669 (▲27) | Classic | 97 | very active | 3d ago | 4.0y |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | Must-have | Inference & serving | Go | 49,969 (▲49) | Classic | 79 | very active | 0d ago | 3.6y |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | Trending | Coding agents & MCP | Python | 49,757 (▲21) | Mature | 24 | slowing | 5mo ago | 3.5y |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | Must-have | Vector store | Go | 46,483 (▲17) | Classic | 99 | very active | 0d ago | 7.1y |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Trending | Orchestration & agents | Rust | 44,615 (▲86) | Hot | 79 | very active | 0d ago | 9mo |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Must-have | Orchestration & agents | Python | 43,924 (▲93) | Classic | 83 | very active | 0d ago | 3.2y |
| [deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed) | Fundamental | Base & training | Python | 43,275 (▲11) | Classic | 96 | very active | 0d ago | 6.8y |
| [agno-agi/agno](https://github.com/agno-agi/agno) | Trending | Orchestration & agents | Python | 42,899 (▲21) | Classic | 82 | very active | 0d ago | 4.5y |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | Fundamental | Vector store | C++ | 41,214 (▲14) | Classic | 94 | very active | 1d ago | 9.7y |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | Trending | RAG & retrieval | Python | 40,340 (▲29) | Mature | 78 | very active | 4d ago | 2.1y |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Trending | RAG & retrieval | Python | 39,755 (▲141) | Hot | 76 | very active | 0d ago | 1.6y |
| [google/langextract](https://github.com/google/langextract) | Trending | Data & ingestion | Python | 39,045 (▲15) | Mature | 67 | very active | 9d ago | 1.3y |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | Must-have | Orchestration & agents | Python | 38,797 (▲28) | Classic | 78 | very active | 1d ago | 3.8y |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Trending | Coding agents & MCP | TypeScript | 38,644 (▲59) | Hot | 78 | very active | 4d ago | 1.6y |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | Must-have | Inference & serving | Python | 38,194 (▲471) | Mature | 99 | very active | 0d ago | 2.8y |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Must-have | Eval & observability | TypeScript | 36,512 (▲164) | Classic | 89 | very active | 0d ago | 3.4y |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | Trending | RAG & retrieval | Python | 36,449 (▲17) | Mature | 70 | very active | 0d ago | 2.6y |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | Must-have | Vector store | Rust | 35,258 (▲30) | Classic | 83 | very active | 0d ago | 6.4y |
| [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | Fundamental | Base & training | Python | 31,433 (▲5) | Classic | 66 | active | 0d ago | 7.6y |
| [karpathy/llm.c](https://github.com/karpathy/llm.c) | Fundamental | Learning | Cuda | 31,219 (▲9) | Abandoned | 4 | stale | 1.3y ago | 2.6y |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | Must-have | Orchestration & agents | Python | 30,065 (▲36) | Mature | 60 | active | 4d ago | 1.9y |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | Fundamental | RAG & retrieval | Jupyter Notebook | 30,010 (▲17) | Mature | 59 | very active | 4d ago | 2.3y |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | Must-have | Vector store | Rust | 29,583 (▲13) | Classic | 81 | very active | 0d ago | 4.1y |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Trending | Eval & observability | Python | 22,932 (▲50) | Classic | 89 | very active | 0d ago | 3.5y |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Trending | Eval & observability | Python | 12,007 (▲22) | Classic | 78 | very active | 0d ago | 4.0y |

## Graph analysis — how they relate

**Community clustering.** These 57 repos span **21 of the graph's 43 communities** — the AI-engineering stack is genuinely cross-cutting, not one tidy neighborhood.

- **Community 11** (9): `infiniflow/ragflow`, `mem0ai/mem0`, `crewAIInc/crewAI`, `MemPalace/mempalace`, `Aider-AI/aider`, `agno-agi/agno`, `VectifyAI/PageIndex`, `NirDiamant/RAG_Techniques`, `chroma-core/chroma`
- **Community 6** (7): `ollama/ollama`, `TauricResearch/TradingAgents`, `vllm-project/vllm`, `unslothai/unsloth`, `hiyouga/LlamaFactory`, `labmlai/annotated_deep_learning_paper_implementations`, `sgl-project/sglang`
- **Community 7** (5): `openai/whisper`, `BerriAI/litellm`, `deepspeedai/DeepSpeed`, `facebookresearch/faiss`, `Lightning-AI/pytorch-lightning`
- **Community 8** (4): `github/spec-kit`, `punkpeye/awesome-mcp-servers`, `milvus-io/milvus`, `qdrant/qdrant`
- **Community 0** (4): `anthropics/skills`, `anthropics/claude-code`, `Fission-AI/OpenSpec`, `stanfordnlp/dspy`
- **Community 36** (3): `langchain-ai/langchain`, `dair-ai/Prompt-Engineering-Guide`, `langchain-ai/langgraph`
- **Community 12** (3): `microsoft/generative-ai-for-beginners`, `microsoft/playwright-mcp`, `microsoft/graphrag`
- **Community 25** (3): `langfuse/langfuse`, `comet-ml/opik`, `Arize-ai/phoenix`
- **Community 18** (3): `firecrawl/firecrawl`, `browser-use/browser-use`, `unclecode/crawl4ai`

**Centrality (PageRank in the full 2,415-repo graph)** — the most 'hub-like' AI-eng repos in your stars (good signal for *foundational*):

- `Fission-AI/OpenSpec` — PageRank 0.0018 (Trending)
- `Lightning-AI/pytorch-lightning` — PageRank 0.0016 (Fundamental)
- `microsoft/playwright-mcp` — PageRank 0.0016 (Trending)
- `langchain-ai/langchain` — PageRank 0.0013 (Must-have)
- `langchain-ai/langgraph` — PageRank 0.0013 (Must-have)
- `huggingface/smolagents` — PageRank 0.0012 (Must-have)
- `agno-agi/agno` — PageRank 0.0011 (Trending)
- `microsoft/generative-ai-for-beginners` — PageRank 0.0011 (Fundamental)
- `microsoft/graphrag` — PageRank 0.0010 (Trending)
- `VectifyAI/PageIndex` — PageRank 0.0009 (Trending)

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). For *production* picks, prefer mature lifecycle + low single-author share; for *trending* picks, expect churn.

| Repo | Tier | Health | Lifecycle | Activity | Bus factor | Top-author share |
|---|---|---|---|---|---|---|
| huggingface/transformers | Fundamental | 100 | Classic | very active | 11 | 10% |
| ggml-org/llama.cpp | Fundamental | 99 | Classic | very active | 11 | 15% |
| vllm-project/vllm | Must-have | 99 | Classic | very active | 20 | 5% |
| sgl-project/sglang | Must-have | 99 | Mature | very active | 7 | 21% |
| BerriAI/litellm | Must-have | 99 | Classic | very active | 5 | 13% |
| milvus-io/milvus | Must-have | 99 | Classic | very active | 6 | 16% |
| run-llama/llama_index | Must-have | 97 | Classic | very active | 10 | 15% |
| deepspeedai/DeepSpeed | Fundamental | 96 | Classic | very active | 5 | 18% |
| google-gemini/gemini-cli | Trending | 95 | Hot | very active | 4 | 17% |
| facebookresearch/faiss | Fundamental | 94 | Classic | very active | 4 | 21% |
| infiniflow/ragflow | Must-have | 94 | Mature | very active | 4 | 20% |
| langfuse/langfuse | Must-have | 89 | Classic | very active | 3 | 23% |
| crewAIInc/crewAI | Must-have | 89 | Classic | very active | 3 | 28% |
| OpenHands/OpenHands | Trending | 89 | Mature | very active | 3 | 37% |
| comet-ml/opik | Trending | 89 | Classic | very active | 3 | 20% |
| ollama/ollama | Must-have | 88 | Classic | very active | 3 | 31% |
| firecrawl/firecrawl | Must-have | 88 | Mature | very active | 3 | 27% |
| Fission-AI/OpenSpec | Trending | 88 | Hot | very active | 3 | 38% |
| bytedance/deer-flow | Trending | 87 | Hot | very active | 15 | 8% |
| github/spec-kit | Trending | 84 | Hot | very active | 2 | 30% |
| langchain-ai/langgraph | Must-have | 83 | Classic | very active | 2 | 41% |
| qdrant/qdrant | Must-have | 83 | Classic | very active | 2 | 41% |
| mem0ai/mem0 | Trending | 83 | Classic | very active | 2 | 45% |
| agno-agi/agno | Trending | 82 | Classic | very active | 2 | 38% |
| chroma-core/chroma | Must-have | 81 | Classic | very active | 2 | 34% |
| unslothai/unsloth | Must-have | 80 | Mature | very active | 1 | 73% |
| hiyouga/LlamaFactory | Must-have | 80 | Classic | very active | 5 | 24% |
| unclecode/crawl4ai | Must-have | 80 | Mature | very active | 1 | 53% |
| langchain-ai/langchain | Must-have | 79 | Classic | very active | 1 | 58% |
| mudler/LocalAI | Must-have | 79 | Classic | very active | 1 | 50% |
| modelcontextprotocol/servers | Trending | 79 | Mature | very active | 1 | 97% |
| browser-use/browser-use | Trending | 79 | Hot | very active | 1 | 66% |
| vercel-labs/agent-browser | Trending | 79 | Hot | very active | 2 | 42% |
| stanfordnlp/dspy | Must-have | 78 | Classic | very active | 1 | 56% |
| anthropics/claude-code | Trending | 78 | Hot | very active | 1 | 57% |
| microsoft/playwright-mcp | Trending | 78 | Hot | very active | 2 | 49% |
| HKUDS/LightRAG | Trending | 78 | Mature | very active | 1 | 63% |
| Arize-ai/phoenix | Trending | 78 | Classic | very active | 1 | 54% |
| TauricResearch/TradingAgents | Trending | 78 | Hot | very active | 1 | 95% |
| MemPalace/mempalace | Trending | 76 | Rising | very active | 1 | 99% |
| VectifyAI/PageIndex | Trending | 76 | Hot | very active | 1 | 51% |
| microsoft/generative-ai-for-beginners | Fundamental | 70 | Classic | very active | 2 | 43% |
| microsoft/graphrag | Trending | 70 | Mature | very active | 1 | 60% |
| google/langextract | Trending | 67 | Mature | very active | 1 | 70% |
| Lightning-AI/pytorch-lightning | Fundamental | 66 | Classic | active | 1 | 53% |
| obra/superpowers | Trending | 64 | Mature | active | 1 | 100% |
| huggingface/smolagents | Must-have | 60 | Mature | active | 2 | 43% |
| punkpeye/awesome-mcp-servers | Trending | 60 | Mature | very active | 1 | 99% |
| NirDiamant/RAG_Techniques | Fundamental | 59 | Mature | very active | 1 | 87% |
| rasbt/LLMs-from-scratch | Fundamental | 53 | Classic | active | 1 | 68% |
| labmlai/annotated_deep_learning_paper_implementations | Fundamental | 47 | Mature | active | 1 | 67% |
| openai/whisper | Fundamental | 44 | Mature | active | 2 | 33% |
| anthropics/skills | Trending | 44 | Mature | active | 1 | 50% |
| Aider-AI/aider | Trending | 24 | Mature | slowing | 0 | 0% |
| dair-ai/Prompt-Engineering-Guide | Fundamental | 14 | Declining | stale | 0 | 0% |
| mlabonne/llm-course | Fundamental | 11 | Declining | stale | 0 | 0% |
| karpathy/llm.c | Fundamental | 4 | Abandoned | stale | 0 | 0% |

## Adjacent (deliberately not in the core list)

- **Comfy-Org/ComfyUI** (143,114★) — image/diffusion tooling — a different (creative) AI discipline, out of scope here
- **PaddlePaddle/PaddleOCR** (91,698★) — OCR engine — a data-ingestion building block, folded into 'Data & ingestion'
- **n8n-io/n8n** (208,626★) — workflow automation — orchestrates agents but isn't core AI-eng tooling (see agent-orchestration report)
- **microsoft/autogen** (61,570★) — multi-agent framework — slipping in activity; crewAI/langgraph lead the must-have slot now
- **nomic-ai/gpt4all** (77,356★) — local-LLM app — superseded for most by ollama; kept off the must-have list

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`, cross-checked against 2026 AI-engineering landscape reporting. No private calls; fully reproducible.
- **Tiers and the solved/frontier verdicts are opinionated** — a synthesis of dataset signal (stars, lifecycle, commit velocity) and the current state of the field, not a benchmark. Treat 'Trending' as *volatile by definition*.
- **Selection** favors recognizable, broadly-applicable AI-engineering tooling. The coding-agent/harness ecosystem and voice stack are summarized here but detailed in the Claude-Code-setups and voice-agents reports respectively.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.

<sub>Repos covered: 57 · Snapshot: 2026-10-26T11:46:04.025Z</sub>
