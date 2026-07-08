# The AI Engineer's Stack — What's Fundamental, Must-Have, and Trending

> Derived from **kaiser-data**'s 1,243 starred repos (snapshot `2026-06-11T21:58:33.384Z`), cross-referenced with the repo-similarity graph (1,243 nodes / 4,017 edges, 31 communities) and the 2026 AI-engineering landscape.
>
> Generated 2026-07-08 by `scripts/reports/ai_engineer_stack.py` (regenerate any time — no API cost).

![Top tools by stars](assets/ai-engineer-stack-top-tools.svg)

![Tools per category](assets/ai-engineer-stack-categories.svg)


## The one thing to understand first

In 2026 the **model layer is commoditizing** — model differences matter less each quarter, and the infrastructure beneath your app (serving, vector search, basic RAG, tracing) is **largely solved**. The value has moved *up the stack*: to **reliability, evaluation, context engineering, and memory** for agentic systems. So this report does two jobs at once — it tells you **which repos to know** (Fundamental / Must-have / Trending) *and* **which problems are already solved** (integrate, don't rebuild) **vs. still frontier** (where you actually add value).

> **Rule of thumb:** if a capability is ✅ *Solved* below, your job is to *integrate the best repo well*. If it's 🔴 *Frontier*, that's where a portfolio project or a job actually gets you noticed.

## The three tiers

### Fundamental (13)

**Bedrock you must understand.** Long-lived base libraries and learning resources. Tools change; these don't. If you can't explain these, you're assembling black boxes.

- **[huggingface/transformers](https://github.com/huggingface/transformers)** · 161,513★ · _Base & training_  
  The model-definition framework — the de-facto way to load/run almost any open model. Know it cold.
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 116,094★ · _Inference & serving_  
  Inference in C/C++ — the primitive behind on-device/edge LLMs; teaches you what quantization actually costs.
- **[microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)** · 111,875★ · _Learning_  
  21-lesson on-ramp to building with generative AI — the gentle starting point.
- **[openai/whisper](https://github.com/openai/whisper)** · 102,488★ · _Voice & multimodal_  
  The reference open ASR model — the baseline for any speech-in pipeline.
- **[rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)** · 96,993★ · _Learning_  
  Build a GPT in PyTorch step by step — the single best way to actually understand what you're orchestrating.
- **[mlabonne/llm-course](https://github.com/mlabonne/llm-course)** · 80,039★ · _Learning_  
  Roadmap + notebooks from fundamentals to deployment — the structured curriculum.
- **[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)** · 75,540★ · _Learning_  
  The canonical prompt-engineering reference — still load-bearing in an agentic world.
- **[labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations)** · 66,923★ · _Learning_  
  60+ annotated paper implementations — read the architectures, don't just import them.
- **[deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed)** · 42,498★ · _Base & training_  
  Training-optimization library (ZeRO, offload) — how large models actually get trained on real hardware.
- **[facebookresearch/faiss](https://github.com/facebookresearch/faiss)** · 40,266★ · _Vector store_  
  The original similarity-search library — the math under every vector DB; understand it before reaching for one.
- **[Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning)** · 31,181★ · _Base & training_  
  Structured PyTorch training — the bridge between research code and reproducible training runs.
- **[karpathy/llm.c](https://github.com/karpathy/llm.c)** · 30,195★ · _Learning_  
  LLM training in raw C/CUDA — strips away the framework to show the actual compute.
- **[NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)** · 27,870★ · _RAG & retrieval_  
  A catalog of advanced RAG techniques with code — the reference when naive RAG isn't enough.

### Must-have (20)

**Your default production toolkit.** The repos you reach for on basically every project — the boring, load-bearing choices. Master integration, not novelty.

- **[ollama/ollama](https://github.com/ollama/ollama)** · 173,893★ · _Inference & serving_  
  One command to run open models locally — the dev-loop and prototyping default.
- **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** · 139,060★ · _Orchestration & agents_  
  The most-deployed agent/LLM framework — the lingua franca; you'll read code that uses it even if you don't.
- **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** · 131,527★ · _Data & ingestion_  
  Search/scrape/crawl the web into LLM-ready data — the ingestion default for RAG & agents.
- **[vllm-project/vllm](https://github.com/vllm-project/vllm)** · 82,581★ · _Inference & serving_  
  High-throughput serving engine (PagedAttention) — the production answer for self-hosting at scale.
- **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** · 82,476★ · _RAG & retrieval_  
  Batteries-included RAG engine with deep document understanding — RAG as a deployable product.
- **[hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)** · 72,090★ · _Fine-tuning_  
  Unified fine-tuning UI/CLI for 100+ models — the no-code-ish path to a tuned model.
- **[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)** · 68,283★ · _Data & ingestion_  
  LLM-friendly open crawler/scraper — self-hosted ingestion when you don't want an API.
- **[unslothai/unsloth](https://github.com/unslothai/unsloth)** · 66,258★ · _Fine-tuning_  
  2× faster, lower-memory LoRA/QLoRA fine-tuning — the practical fine-tuning default.
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** · 53,280★ · _Orchestration & agents_  
  Role-playing multi-agent orchestration — the popular 'team of agents' framework.
- **[run-llama/llama_index](https://github.com/run-llama/llama_index)** · 50,083★ · _RAG & retrieval_  
  The leading data/RAG framework — connectors, indexing, query engines; the RAG default alongside LangChain.
- **[BerriAI/litellm](https://github.com/BerriAI/litellm)** · 50,082★ · _Inference & serving_  
  OpenAI-compatible gateway to 100+ LLMs — swap/route/budget models from one endpoint. Non-negotiable glue.
- **[mudler/LocalAI](https://github.com/mudler/LocalAI)** · 46,792★ · _Inference & serving_  
  OpenAI-compatible local engine (LLM/vision/voice) — self-host the whole API surface.
- **[milvus-io/milvus](https://github.com/milvus-io/milvus)** · 44,729★ · _Vector store_  
  Cloud-native vector DB built for massive scale — when you outgrow a single box.
- **[stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)** · 34,990★ · _Orchestration & agents_  
  Program — don't prompt — LLMs; compile prompts against metrics. The antidote to prompt-spaghetti.
- **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** · 34,458★ · _Orchestration & agents_  
  Explicit graphs over implicit chains — the 2026 standard for *production-grade* agent control flow.
- **[qdrant/qdrant](https://github.com/qdrant/qdrant)** · 32,039★ · _Vector store_  
  High-performance Rust vector DB — the popular standalone choice; great filtering.
- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 28,929★ · _Eval & observability_  
  Open-source LLM tracing/evals/prompts — you can't ship what you can't see (you run this).
- **[sgl-project/sglang](https://github.com/sgl-project/sglang)** · 28,913★ · _Inference & serving_  
  Fast serving with structured-output + prefix-cache wins — vLLM's main rival; learn both.
- **[chroma-core/chroma](https://github.com/chroma-core/chroma)** · 28,387★ · _Vector store_  
  The 'just works' embedded vector store — fastest path from zero to a working RAG.
- **[huggingface/smolagents](https://github.com/huggingface/smolagents)** · 27,817★ · _Orchestration & agents_  
  Barebones code-writing agents — the minimal mental model of what an agent loop *is*.

### Trending (23)

**Where the energy is right now (2026).** Fast-moving, high-upside, often unstable. Learn these to stay current and to find differentiated things to build.

- **[obra/superpowers](https://github.com/obra/superpowers)** · 224,734★ · _Coding agents & MCP_  
  The headline agentic-skills framework — the most-starred repo in this whole set.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 149,487★ · _Coding agents & MCP_  
  Agent Skills — on-demand capability that's displacing always-on prompt bloat.
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 131,796★ · _Coding agents & MCP_  
  The agentic coding CLI — the flagship of the coding-agent wave (full ecosystem in the cc-setups report).
- **[github/spec-kit](https://github.com/github/spec-kit)** · 111,475★ · _Coding agents & MCP_  
  Spec-driven development toolkit — the 'write the spec, let the agent build' workflow.
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 105,171★ · _Coding agents & MCP_  
  Gemini's terminal agent — the third major CLI harness; useful for model-shopping.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 98,327★ · _Orchestration & agents_  
  Let agents drive real browsers — the computer-use frontier; high promise, still flaky.
- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 88,887★ · _Coding agents & MCP_  
  The community MCP index — discovery for the fastest-growing integration ecosystem.
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 87,070★ · _Coding agents & MCP_  
  Reference MCP servers — MCP is the emerging standard for wiring tools/data into any agent.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 85,230★ · _Orchestration & agents_  
  Multi-agent trading framework — the template for *vertical* agent systems with real domain logic.
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 76,482★ · _Coding agents & MCP_  
  Open autonomous software-engineering agent — the OSS face of the SWE-agent race.
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 70,988★ · _Orchestration & agents_  
  Long-horizon research+code SuperAgent — the 'deep research' pattern as a harness.
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 58,361★ · _Memory_  
  Universal memory layer for agents — the most-adopted bet on the unsolved memory problem.
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 55,384★ · _Memory_  
  Best-benchmarked open memory system — a strong contender in a still-open race.
- **[Aider-AI/aider](https://github.com/Aider-AI/aider)** · 46,008★ · _Coding agents & MCP_  
  AI pair-programming in the terminal with tight git integration — a beloved daily driver.
- **[agno-agi/agno](https://github.com/agno-agi/agno)** · 40,646★ · _Orchestration & agents_  
  Build/run/manage agent platforms — a fast-rising full-stack agent framework.
- **[google/langextract](https://github.com/google/langextract)** · 36,873★ · _Data & ingestion_  
  Structured extraction from unstructured text — turning documents into typed data.
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 36,460★ · _RAG & retrieval_  
  Graph-augmented RAG that's simple and fast — the practical face of 'RAG beyond chunks'.
- **[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)** · 35,849★ · _Orchestration & agents_  
  Browser-automation CLI for agents — the lighter, scriptable take on web agents.
- **[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)** · 33,783★ · _Coding agents & MCP_  
  Playwright as an MCP server — reliable, structured web control for agents.
- **[microsoft/graphrag](https://github.com/microsoft/graphrag)** · 33,661★ · _RAG & retrieval_  
  Graph-based RAG — structure-aware retrieval for global/whole-corpus questions.
- **[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** · 32,927★ · _RAG & retrieval_  
  Vectorless, reasoning-based retrieval — a bet that reasoning can replace embeddings.
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 19,579★ · _Eval & observability_  
  Eval-first LLM/agent observability — measuring agents, not just logging them.
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 10,100★ · _Eval & observability_  
  OpenTelemetry-based AI observability & eval — standards-based tracing for agents.

## What's solved vs. what's still frontier

The most useful map an AI engineer can carry: where to **stop building and integrate**, and where **building is still worth it**.

| Layer | Status | What that means for you | Your repos here |
|---|---|---|---|
| **Base & training** | ✅ Solved (for users) | HF Transformers + PyTorch are the substrate. Training *frontier* models isn't your job; using them is. | `transformers`, `DeepSpeed`, `pytorch-lightning` |
| **Inference & serving** | ✅ Solved | vLLM / SGLang / Ollama / llama.cpp cover edge→datacenter. Never write your own serving layer; pick by scale. | `ollama`, `llama.cpp`, `vllm`, `litellm`, `LocalAI` |
| **Vector store** | ✅ Solved | faiss/qdrant/milvus/chroma (+pgvector) are mature. Choose on ops + filtering needs, not capability. | `milvus`, `faiss`, `qdrant`, `chroma` |
| **RAG & retrieval** | 🟡 Split | Naive RAG (chunk→embed→retrieve→stuff) is commoditized. Advanced/agentic/graph retrieval (LightRAG, graphrag, PageIndex) is still frontier. | `ragflow`, `llama_index`, `LightRAG`, `graphrag`, `PageIndex` |
| **Orchestration & agents** | 🔴 Frontier | Frameworks are mature (langgraph). Reliable long-horizon autonomy is NOT — open agents trail humans badly on real workflows. | `langchain`, `browser-use`, `TradingAgents`, `deer-flow`, `crewAI` |
| **Memory** | 🔴 Open problem | mem0/mempalace are bets, not settled answers. Durable, selective, cheap long-term memory is unsolved. | `mem0`, `mempalace` |
| **Eval & observability** | 🟡 Split | Tracing is solved (langfuse/phoenix). Agent *evaluation* is frontier — SWE-bench is saturated; reliable eval harnesses are unsolved. | `langfuse`, `opik`, `phoenix` |
| **Fine-tuning** | 🟢 Mechanics solved | LoRA/QLoRA via unsloth/LlamaFactory is push-button. The real skill is knowing *when* to fine-tune vs RAG vs prompt. | `LlamaFactory`, `unsloth` |
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
| [obra/superpowers](https://github.com/obra/superpowers) | Trending | 224,734 | 8mo | 86 | 0d ago | 7 |
| [github/spec-kit](https://github.com/github/spec-kit) | Trending | 111,475 | 9mo | 504 | 0d ago | 7 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Trending | 55,384 | 2mo | 1237 | 1d ago | 7 |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Trending | 35,849 | 5mo | 235 | 1d ago | 7 |
| [google/langextract](https://github.com/google/langextract) | Trending | 36,873 | 11mo | 35 | 22d ago | 6 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Trending | 131,796 | 1.3y | 105 | 1d ago | 5 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Trending | 105,171 | 1.2y | 968 | 0d ago | 5 |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Trending | 98,327 | 1.6y | 908 | 0d ago | 5 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Trending | 88,887 | 1.5y | 3362 | 0d ago | 5 |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Trending | 85,230 | 1.5y | 113 | 11d ago | 5 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Trending | 70,988 | 1.1y | 653 | 0d ago | 5 |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Trending | 33,783 | 1.2y | 62 | 2d ago | 5 |
| [anthropics/skills](https://github.com/anthropics/skills) | Trending | 149,487 | 8mo | 18 | 2d ago | 4 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Trending | 87,070 | 1.6y | 41 | 4d ago | 4 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Trending | 32,927 | 1.2y | 41 | 6d ago | 4 |

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
| [obra/superpowers](https://github.com/obra/superpowers) | Trending | Coding agents & MCP | Shell | 224,734 | Hot | 71 | very active | 0d ago | 8mo |
| [ollama/ollama](https://github.com/ollama/ollama) | Must-have | Inference & serving | Go | 173,893 | Mature | 88 | very active | 0d ago | 3.0y |
| [huggingface/transformers](https://github.com/huggingface/transformers) | Fundamental | Base & training | Python | 161,513 | Classic | 99 | very active | 0d ago | 7.6y |
| [anthropics/skills](https://github.com/anthropics/skills) | Trending | Coding agents & MCP | Python | 149,487 | Rising | 46 | active | 2d ago | 8mo |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Must-have | Orchestration & agents | Python | 139,060 | Classic | 80 | very active | 0d ago | 3.7y |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Trending | Coding agents & MCP | Python | 131,796 | Hot | 77 | very active | 1d ago | 1.3y |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Must-have | Data & ingestion | TypeScript | 131,527 | Mature | 84 | very active | 0d ago | 2.2y |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | Fundamental | Inference & serving | C++ | 116,094 | Classic | 99 | very active | 0d ago | 3.3y |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | Fundamental | Learning | Jupyter Notebook | 111,875 | Mature | 67 | very active | 1d ago | 3.0y |
| [github/spec-kit](https://github.com/github/spec-kit) | Trending | Coding agents & MCP | Python | 111,475 | Hot | 88 | very active | 0d ago | 9mo |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Trending | Coding agents & MCP | TypeScript | 105,171 | Hot | 99 | very active | 0d ago | 1.2y |
| [openai/whisper](https://github.com/openai/whisper) | Fundamental | Voice & multimodal | Python | 102,488 | Mature | 40 | active | 1mo ago | 3.7y |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Trending | Orchestration & agents | Python | 98,327 | Hot | 80 | very active | 0d ago | 1.6y |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | Fundamental | Learning | Jupyter Notebook | 96,993 | Mature | 54 | active | 9d ago | 2.9y |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Trending | Coding agents & MCP | — | 88,887 | Hot | 65 | very active | 0d ago | 1.5y |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Trending | Coding agents & MCP | TypeScript | 87,070 | Hot | 85 | very active | 4d ago | 1.6y |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Trending | Orchestration & agents | Python | 85,230 | Hot | 70 | very active | 11d ago | 1.5y |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | Must-have | Inference & serving | Python | 82,581 | Classic | 99 | very active | 0d ago | 3.3y |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | Must-have | RAG & retrieval | Python | 82,476 | Mature | 96 | very active | 0d ago | 2.5y |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | Fundamental | Learning | — | 80,039 | Mature | 23 | slowing | 4mo ago | 3.0y |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | Trending | Coding agents & MCP | Python | 76,482 | Mature | 90 | very active | 0d ago | 2.2y |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | Fundamental | Learning | MDX | 75,540 | Mature | 25 | slowing | 3mo ago | 3.5y |
| [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) | Must-have | Fine-tuning | Python | 72,090 | Classic | 86 | very active | 2d ago | 3.0y |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Trending | Orchestration & agents | Python | 70,988 | Hot | 81 | very active | 0d ago | 1.1y |
| [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | Must-have | Data & ingestion | Python | 68,283 | Mature | 82 | very active | 8d ago | 2.1y |
| [labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | Fundamental | Learning | Python | 66,923 | Mature | 26 | slowing | 4mo ago | 5.8y |
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | Must-have | Fine-tuning | Python | 66,258 | Mature | 82 | very active | 0d ago | 2.5y |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Trending | Memory | Python | 58,361 | Mature | 94 | very active | 0d ago | 3.0y |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Trending | Memory | Python | 55,384 | Hot | 76 | very active | 1d ago | 2mo |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Must-have | Orchestration & agents | Python | 53,280 | Mature | 85 | very active | 0d ago | 2.6y |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | Must-have | RAG & retrieval | Python | 50,083 | Classic | 100 | very active | 0d ago | 3.6y |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Must-have | Inference & serving | Python | 50,082 | Mature | 89 | very active | 0d ago | 2.9y |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | Must-have | Inference & serving | Go | 46,792 | Classic | 79 | very active | 0d ago | 3.2y |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | Trending | Coding agents & MCP | Python | 46,008 | Classic | 57 | very active | 20d ago | 3.1y |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | Must-have | Vector store | Go | 44,729 | Classic | 100 | very active | 0d ago | 6.7y |
| [deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed) | Fundamental | Base & training | Python | 42,498 | Classic | 94 | very active | 0d ago | 6.4y |
| [agno-agi/agno](https://github.com/agno-agi/agno) | Trending | Orchestration & agents | Python | 40,646 | Classic | 98 | very active | 0d ago | 4.1y |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | Fundamental | Vector store | C++ | 40,266 | Classic | 88 | very active | 0d ago | 9.3y |
| [google/langextract](https://github.com/google/langextract) | Trending | Data & ingestion | Python | 36,873 | Hot | 68 | very active | 22d ago | 11mo |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | Trending | RAG & retrieval | Python | 36,460 | Mature | 79 | very active | 0d ago | 1.7y |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Trending | Orchestration & agents | Rust | 35,849 | Hot | 75 | very active | 1d ago | 5mo |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | Must-have | Orchestration & agents | Python | 34,990 | Classic | 83 | very active | 0d ago | 3.4y |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Must-have | Orchestration & agents | Python | 34,458 | Mature | 83 | very active | 0d ago | 2.8y |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Trending | Coding agents & MCP | TypeScript | 33,783 | Hot | 76 | very active | 2d ago | 1.2y |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | Trending | RAG & retrieval | Python | 33,661 | Mature | 68 | active | 6d ago | 2.2y |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Trending | RAG & retrieval | Python | 32,927 | Hot | 50 | very active | 6d ago | 1.2y |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | Must-have | Vector store | Rust | 32,039 | Classic | 93 | very active | 0d ago | 6.0y |
| [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | Fundamental | Base & training | Python | 31,181 | Classic | 81 | very active | 1d ago | 7.2y |
| [karpathy/llm.c](https://github.com/karpathy/llm.c) | Fundamental | Learning | Cuda | 30,195 | Declining | 5 | stale | 11mo ago | 2.2y |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Must-have | Eval & observability | TypeScript | 28,929 | Classic | 89 | very active | 0d ago | 3.1y |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | Must-have | Inference & serving | Python | 28,913 | Mature | 99 | very active | 0d ago | 2.4y |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | Must-have | Vector store | Rust | 28,387 | Classic | 83 | very active | 1d ago | 3.7y |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | Fundamental | RAG & retrieval | Jupyter Notebook | 27,870 | Mature | 61 | very active | 0d ago | 1.9y |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | Must-have | Orchestration & agents | Python | 27,817 | Mature | 66 | active | 2d ago | 1.5y |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Trending | Eval & observability | Python | 19,579 | Classic | 99 | very active | 0d ago | 3.1y |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Trending | Eval & observability | Python | 10,100 | Classic | 84 | very active | 0d ago | 3.6y |

## Graph analysis — how they relate

**Community clustering.** These 56 repos span **20 of the graph's 31 communities** — the AI-engineering stack is genuinely cross-cutting, not one tidy neighborhood.

- **Community 5** (7): `ollama/ollama`, `huggingface/transformers`, `vllm-project/vllm`, `hiyouga/LlamaFactory`, `unslothai/unsloth`, `sgl-project/sglang`, `huggingface/smolagents`
- **Community 1** (7): `google-gemini/gemini-cli`, `browser-use/browser-use`, `punkpeye/awesome-mcp-servers`, `MemPalace/mempalace`, `crewAIInc/crewAI`, `agno-agi/agno`, `chroma-core/chroma`
- **Community 7** (6): `langchain-ai/langchain`, `dair-ai/Prompt-Engineering-Guide`, `bytedance/deer-flow`, `mem0ai/mem0`, `google/langextract`, `langchain-ai/langgraph`
- **Community 6** (5): `rasbt/LLMs-from-scratch`, `labmlai/annotated_deep_learning_paper_implementations`, `deepspeedai/DeepSpeed`, `facebookresearch/faiss`, `Lightning-AI/pytorch-lightning`
- **Community 3** (4): `infiniflow/ragflow`, `HKUDS/LightRAG`, `VectifyAI/PageIndex`, `NirDiamant/RAG_Techniques`
- **Community 20** (4): `BerriAI/litellm`, `langfuse/langfuse`, `comet-ml/opik`, `Arize-ai/phoenix`
- **Community 19** (4): `firecrawl/firecrawl`, `TauricResearch/TradingAgents`, `OpenHands/OpenHands`, `vercel-labs/agent-browser`
- **Community 13** (3): `microsoft/generative-ai-for-beginners`, `microsoft/playwright-mcp`, `microsoft/graphrag`

**Centrality (PageRank in the full 1,243-repo graph)** — the most 'hub-like' AI-eng repos in your stars (good signal for *foundational*):

- `Lightning-AI/pytorch-lightning` — PageRank 0.0041 (Fundamental)
- `microsoft/generative-ai-for-beginners` — PageRank 0.0030 (Fundamental)
- `langchain-ai/langgraph` — PageRank 0.0028 (Must-have)
- `NirDiamant/RAG_Techniques` — PageRank 0.0028 (Fundamental)
- `langchain-ai/langchain` — PageRank 0.0028 (Must-have)
- `agno-agi/agno` — PageRank 0.0026 (Trending)
- `VectifyAI/PageIndex` — PageRank 0.0024 (Trending)
- `HKUDS/LightRAG` — PageRank 0.0017 (Trending)
- `crewAIInc/crewAI` — PageRank 0.0017 (Must-have)
- `openai/whisper` — PageRank 0.0016 (Fundamental)

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). For *production* picks, prefer mature lifecycle + low single-author share; for *trending* picks, expect churn.

| Repo | Tier | Health | Lifecycle | Activity | Bus factor | Top-author share |
|---|---|---|---|---|---|---|
| run-llama/llama_index | Must-have | 100 | Classic | very active | 7 | 25% |
| milvus-io/milvus | Must-have | 100 | Classic | very active | 8 | 8% |
| huggingface/transformers | Fundamental | 99 | Classic | very active | 7 | 18% |
| ggml-org/llama.cpp | Fundamental | 99 | Classic | very active | 9 | 12% |
| vllm-project/vllm | Must-have | 99 | Classic | very active | 26 | 6% |
| sgl-project/sglang | Must-have | 99 | Mature | very active | 13 | 8% |
| google-gemini/gemini-cli | Trending | 99 | Hot | very active | 7 | 12% |
| comet-ml/opik | Trending | 99 | Classic | very active | 5 | 25% |
| agno-agi/agno | Trending | 98 | Classic | very active | 6 | 13% |
| infiniflow/ragflow | Must-have | 96 | Mature | very active | 8 | 12% |
| deepspeedai/DeepSpeed | Fundamental | 94 | Classic | very active | 5 | 28% |
| mem0ai/mem0 | Trending | 94 | Mature | very active | 4 | 30% |
| qdrant/qdrant | Must-have | 93 | Classic | very active | 4 | 18% |
| OpenHands/OpenHands | Trending | 90 | Mature | very active | 3 | 27% |
| BerriAI/litellm | Must-have | 89 | Mature | very active | 3 | 19% |
| langfuse/langfuse | Must-have | 89 | Classic | very active | 3 | 21% |
| facebookresearch/faiss | Fundamental | 88 | Classic | very active | 3 | 21% |
| ollama/ollama | Must-have | 88 | Mature | very active | 3 | 32% |
| github/spec-kit | Trending | 88 | Hot | very active | 3 | 38% |
| hiyouga/LlamaFactory | Must-have | 86 | Classic | very active | 5 | 20% |
| crewAIInc/crewAI | Must-have | 85 | Mature | very active | 2 | 49% |
| modelcontextprotocol/servers | Trending | 85 | Hot | very active | 4 | 24% |
| firecrawl/firecrawl | Must-have | 84 | Mature | very active | 2 | 33% |
| Arize-ai/phoenix | Trending | 84 | Classic | very active | 2 | 41% |
| langchain-ai/langgraph | Must-have | 83 | Mature | very active | 2 | 43% |
| chroma-core/chroma | Must-have | 83 | Classic | very active | 2 | 39% |
| stanfordnlp/dspy | Must-have | 83 | Classic | very active | 2 | 35% |
| unslothai/unsloth | Must-have | 82 | Mature | very active | 2 | 48% |
| unclecode/crawl4ai | Must-have | 82 | Mature | very active | 2 | 44% |
| Lightning-AI/pytorch-lightning | Fundamental | 81 | Classic | very active | 2 | 41% |
| bytedance/deer-flow | Trending | 81 | Hot | very active | 5 | 16% |
| langchain-ai/langchain | Must-have | 80 | Classic | very active | 1 | 55% |
| browser-use/browser-use | Trending | 80 | Hot | very active | 1 | 62% |
| mudler/LocalAI | Must-have | 79 | Classic | very active | 1 | 79% |
| HKUDS/LightRAG | Trending | 79 | Mature | very active | 1 | 89% |
| anthropics/claude-code | Trending | 77 | Hot | very active | 1 | 84% |
| microsoft/playwright-mcp | Trending | 76 | Hot | very active | 1 | 71% |
| MemPalace/mempalace | Trending | 76 | Hot | very active | 1 | 66% |
| vercel-labs/agent-browser | Trending | 75 | Hot | very active | 1 | 70% |
| obra/superpowers | Trending | 71 | Hot | very active | 1 | 59% |
| TauricResearch/TradingAgents | Trending | 70 | Hot | very active | 1 | 86% |
| microsoft/graphrag | Trending | 68 | Mature | active | 1 | 69% |
| google/langextract | Trending | 68 | Hot | very active | 1 | 80% |
| microsoft/generative-ai-for-beginners | Fundamental | 67 | Mature | very active | 2 | 37% |
| huggingface/smolagents | Must-have | 66 | Mature | active | 1 | 53% |
| punkpeye/awesome-mcp-servers | Trending | 65 | Hot | very active | 1 | 86% |
| NirDiamant/RAG_Techniques | Fundamental | 61 | Mature | very active | 1 | 98% |
| Aider-AI/aider | Trending | 57 | Classic | very active | 1 | 82% |
| rasbt/LLMs-from-scratch | Fundamental | 54 | Mature | active | 1 | 67% |
| VectifyAI/PageIndex | Trending | 50 | Hot | very active | 1 | 73% |
| anthropics/skills | Trending | 46 | Rising | active | 1 | 56% |
| openai/whisper | Fundamental | 40 | Mature | active | 1 | 50% |
| labmlai/annotated_deep_learning_paper_implementations | Fundamental | 26 | Mature | slowing | 0 | 0% |
| dair-ai/Prompt-Engineering-Guide | Fundamental | 25 | Mature | slowing | 0 | 0% |
| mlabonne/llm-course | Fundamental | 23 | Mature | slowing | 0 | 0% |
| karpathy/llm.c | Fundamental | 5 | Declining | stale | 0 | 0% |

## Adjacent (deliberately not in the core list)

- **Comfy-Org/ComfyUI** (116,627★) — image/diffusion tooling — a different (creative) AI discipline, out of scope here
- **PaddlePaddle/PaddleOCR** (81,861★) — OCR engine — a data-ingestion building block, folded into 'Data & ingestion'
- **n8n-io/n8n** (192,095★) — workflow automation — orchestrates agents but isn't core AI-eng tooling (see agent-orchestration report)
- **microsoft/autogen** (58,879★) — multi-agent framework — slipping in activity; crewAI/langgraph lead the must-have slot now
- **nomic-ai/gpt4all** (77,353★) — local-LLM app — superseded for most by ollama; kept off the must-have list

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`, cross-checked against 2026 AI-engineering landscape reporting. No private calls; fully reproducible.
- **Tiers and the solved/frontier verdicts are opinionated** — a synthesis of dataset signal (stars, lifecycle, commit velocity) and the current state of the field, not a benchmark. Treat 'Trending' as *volatile by definition*.
- **Selection** favors recognizable, broadly-applicable AI-engineering tooling. The coding-agent/harness ecosystem and voice stack are summarized here but detailed in the Claude-Code-setups and voice-agents reports respectively.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.

<sub>Repos covered: 56 · Snapshot: 2026-06-11T21:58:33.384Z</sub>
