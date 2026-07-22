# The AI Engineer's Stack — What's Fundamental, Must-Have, and Trending

> Derived from **kaiser-data**'s 1,350 starred repos (snapshot `2026-07-20T08:33:57.852Z`), cross-referenced with the repo-similarity graph (1,350 nodes / 4,379 edges, 28 communities) and the 2026 AI-engineering landscape.
>
> Generated 2026-07-22 by `scripts/reports/ai_engineer_stack.py` (regenerate any time — no API cost).

![Top tools by stars](assets/ai-engineer-stack-top-tools.svg)

![Tools per category](assets/ai-engineer-stack-categories.svg)


## The one thing to understand first

In 2026 the **model layer is commoditizing** — model differences matter less each quarter, and the infrastructure beneath your app (serving, vector search, basic RAG, tracing) is **largely solved**. The value has moved *up the stack*: to **reliability, evaluation, context engineering, and memory** for agentic systems. So this report does two jobs at once — it tells you **which repos to know** (Fundamental / Must-have / Trending) *and* **which problems are already solved** (integrate, don't rebuild) **vs. still frontier** (where you actually add value).

> **Rule of thumb:** if a capability is ✅ *Solved* below, your job is to *integrate the best repo well*. If it's 🔴 *Frontier*, that's where a portfolio project or a job actually gets you noticed.

## The three tiers

### Fundamental (13)

**Bedrock you must understand.** Long-lived base libraries and learning resources. Tools change; these don't. If you can't explain these, you're assembling black boxes.

- **[huggingface/transformers](https://github.com/huggingface/transformers)** · 162,754★ · _Base & training_  
  The model-definition framework — the de-facto way to load/run almost any open model. Know it cold.
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 121,006★ · _Inference & serving_  
  Inference in C/C++ — the primitive behind on-device/edge LLMs; teaches you what quantization actually costs.
- **[microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)** · 113,260★ · _Learning_  
  21-lesson on-ramp to building with generative AI — the gentle starting point.
- **[openai/whisper](https://github.com/openai/whisper)** · 105,272★ · _Voice & multimodal_  
  The reference open ASR model — the baseline for any speech-in pipeline.
- **[rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)** · 99,415★ · _Learning_  
  Build a GPT in PyTorch step by step — the single best way to actually understand what you're orchestrating.
- **[mlabonne/llm-course](https://github.com/mlabonne/llm-course)** · 81,104★ · _Learning_  
  Roadmap + notebooks from fundamentals to deployment — the structured curriculum.
- **[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)** · 76,757★ · _Learning_  
  The canonical prompt-engineering reference — still load-bearing in an agentic world.
- **[labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations)** · 67,190★ · _Learning_  
  60+ annotated paper implementations — read the architectures, don't just import them.
- **[deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed)** · 42,750★ · _Base & training_  
  Training-optimization library (ZeRO, offload) — how large models actually get trained on real hardware.
- **[facebookresearch/faiss](https://github.com/facebookresearch/faiss)** · 40,544★ · _Vector store_  
  The original similarity-search library — the math under every vector DB; understand it before reaching for one.
- **[Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning)** · 31,240★ · _Base & training_  
  Structured PyTorch training — the bridge between research code and reproducible training runs.
- **[karpathy/llm.c](https://github.com/karpathy/llm.c)** · 30,589★ · _Learning_  
  LLM training in raw C/CUDA — strips away the framework to show the actual compute.
- **[NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)** · 28,719★ · _RAG & retrieval_  
  A catalog of advanced RAG techniques with code — the reference when naive RAG isn't enough.

### Must-have (20)

**Your default production toolkit.** The repos you reach for on basically every project — the boring, load-bearing choices. Master integration, not novelty.

- **[ollama/ollama](https://github.com/ollama/ollama)** · 176,491★ · _Inference & serving_  
  One command to run open models locally — the dev-loop and prototyping default.
- **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** · 153,281★ · _Data & ingestion_  
  Search/scrape/crawl the web into LLM-ready data — the ingestion default for RAG & agents.
- **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** · 142,141★ · _Orchestration & agents_  
  The most-deployed agent/LLM framework — the lingua franca; you'll read code that uses it even if you don't.
- **[vllm-project/vllm](https://github.com/vllm-project/vllm)** · 86,682★ · _Inference & serving_  
  High-throughput serving engine (PagedAttention) — the production answer for self-hosting at scale.
- **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** · 85,442★ · _RAG & retrieval_  
  Batteries-included RAG engine with deep document understanding — RAG as a deployable product.
- **[hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)** · 73,385★ · _Fine-tuning_  
  Unified fine-tuning UI/CLI for 100+ models — the no-code-ish path to a tuned model.
- **[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)** · 73,359★ · _Data & ingestion_  
  LLM-friendly open crawler/scraper — self-hosted ingestion when you don't want an API.
- **[unslothai/unsloth](https://github.com/unslothai/unsloth)** · 68,445★ · _Fine-tuning_  
  2× faster, lower-memory LoRA/QLoRA fine-tuning — the practical fine-tuning default.
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** · 55,823★ · _Orchestration & agents_  
  Role-playing multi-agent orchestration — the popular 'team of agents' framework.
- **[BerriAI/litellm](https://github.com/BerriAI/litellm)** · 54,074★ · _Inference & serving_  
  OpenAI-compatible gateway to 100+ LLMs — swap/route/budget models from one endpoint. Non-negotiable glue.
- **[run-llama/llama_index](https://github.com/run-llama/llama_index)** · 50,953★ · _RAG & retrieval_  
  The leading data/RAG framework — connectors, indexing, query engines; the RAG default alongside LangChain.
- **[mudler/LocalAI](https://github.com/mudler/LocalAI)** · 47,698★ · _Inference & serving_  
  OpenAI-compatible local engine (LLM/vision/voice) — self-host the whole API surface.
- **[milvus-io/milvus](https://github.com/milvus-io/milvus)** · 45,277★ · _Vector store_  
  Cloud-native vector DB built for massive scale — when you outgrow a single box.
- **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** · 37,654★ · _Orchestration & agents_  
  Explicit graphs over implicit chains — the 2026 standard for *production-grade* agent control flow.
- **[stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)** · 36,237★ · _Orchestration & agents_  
  Program — don't prompt — LLMs; compile prompts against metrics. The antidote to prompt-spaghetti.
- **[qdrant/qdrant](https://github.com/qdrant/qdrant)** · 33,423★ · _Vector store_  
  High-performance Rust vector DB — the popular standalone choice; great filtering.
- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 31,458★ · _Eval & observability_  
  Open-source LLM tracing/evals/prompts — you can't ship what you can't see (you run this).
- **[sgl-project/sglang](https://github.com/sgl-project/sglang)** · 30,534★ · _Inference & serving_  
  Fast serving with structured-output + prefix-cache wins — vLLM's main rival; learn both.
- **[chroma-core/chroma](https://github.com/chroma-core/chroma)** · 28,833★ · _Vector store_  
  The 'just works' embedded vector store — fastest path from zero to a working RAG.
- **[huggingface/smolagents](https://github.com/huggingface/smolagents)** · 28,441★ · _Orchestration & agents_  
  Barebones code-writing agents — the minimal mental model of what an agent loop *is*.

### Trending (23)

**Where the energy is right now (2026).** Fast-moving, high-upside, often unstable. Learn these to stay current and to find differentiated things to build.

- **[obra/superpowers](https://github.com/obra/superpowers)** · 257,811★ · _Coding agents & MCP_  
  The headline agentic-skills framework — the most-starred repo in this whole set.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 162,818★ · _Coding agents & MCP_  
  Agent Skills — on-demand capability that's displacing always-on prompt bloat.
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 138,390★ · _Coding agents & MCP_  
  The agentic coding CLI — the flagship of the coding-agent wave (full ecosystem in the cc-setups report).
- **[github/spec-kit](https://github.com/github/spec-kit)** · 122,508★ · _Coding agents & MCP_  
  Spec-driven development toolkit — the 'write the spec, let the agent build' workflow.
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 106,079★ · _Coding agents & MCP_  
  Gemini's terminal agent — the third major CLI harness; useful for model-shopping.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 105,645★ · _Orchestration & agents_  
  Let agents drive real browsers — the computer-use frontier; high promise, still flaky.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 93,746★ · _Orchestration & agents_  
  Multi-agent trading framework — the template for *vertical* agent systems with real domain logic.
- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 90,979★ · _Coding agents & MCP_  
  The community MCP index — discovery for the fastest-growing integration ecosystem.
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 88,650★ · _Coding agents & MCP_  
  Reference MCP servers — MCP is the emerging standard for wiring tools/data into any agent.
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 81,363★ · _Coding agents & MCP_  
  Open autonomous software-engineering agent — the OSS face of the SWE-agent race.
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 77,423★ · _Orchestration & agents_  
  Long-horizon research+code SuperAgent — the 'deep research' pattern as a harness.
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 61,274★ · _Memory_  
  Universal memory layer for agents — the most-adopted bet on the unsolved memory problem.
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 57,493★ · _Memory_  
  Best-benchmarked open memory system — a strong contender in a still-open race.
- **[Aider-AI/aider](https://github.com/Aider-AI/aider)** · 47,529★ · _Coding agents & MCP_  
  AI pair-programming in the terminal with tight git integration — a beloved daily driver.
- **[agno-agi/agno](https://github.com/agno-agi/agno)** · 41,301★ · _Orchestration & agents_  
  Build/run/manage agent platforms — a fast-rising full-stack agent framework.
- **[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)** · 38,809★ · _Orchestration & agents_  
  Browser-automation CLI for agents — the lighter, scriptable take on web agents.
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 37,870★ · _RAG & retrieval_  
  Graph-augmented RAG that's simple and fast — the practical face of 'RAG beyond chunks'.
- **[google/langextract](https://github.com/google/langextract)** · 37,591★ · _Data & ingestion_  
  Structured extraction from unstructured text — turning documents into typed data.
- **[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)** · 35,277★ · _Coding agents & MCP_  
  Playwright as an MCP server — reliable, structured web control for agents.
- **[microsoft/graphrag](https://github.com/microsoft/graphrag)** · 34,522★ · _RAG & retrieval_  
  Graph-based RAG — structure-aware retrieval for global/whole-corpus questions.
- **[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** · 34,121★ · _RAG & retrieval_  
  Vectorless, reasoning-based retrieval — a bet that reasoning can replace embeddings.
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 20,714★ · _Eval & observability_  
  Eval-first LLM/agent observability — measuring agents, not just logging them.
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 10,634★ · _Eval & observability_  
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
| [obra/superpowers](https://github.com/obra/superpowers) | Trending | 257,811 | 9mo | 191 | 0d ago | 7 |
| [github/spec-kit](https://github.com/github/spec-kit) | Trending | 122,508 | 11mo | 641 | 2d ago | 7 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Trending | 57,493 | 3mo | 992 | 3d ago | 7 |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Trending | 38,809 | 6mo | 49 | 1d ago | 6 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Trending | 138,390 | 1.4y | 109 | 0d ago | 5 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Trending | 106,079 | 1.3y | 420 | 0d ago | 5 |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Trending | 105,645 | 1.7y | 671 | 3d ago | 5 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Trending | 90,979 | 1.6y | 2923 | 7d ago | 5 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Trending | 77,423 | 1.2y | 750 | 0d ago | 5 |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | Trending | 37,870 | 1.8y | 1707 | 0d ago | 5 |
| [anthropics/skills](https://github.com/anthropics/skills) | Trending | 162,818 | 10mo | 14 | 3d ago | 4 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Trending | 88,650 | 1.7y | 44 | 10d ago | 4 |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Trending | 35,277 | 1.3y | 39 | 5d ago | 4 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Trending | 34,121 | 1.3y | 48 | 1d ago | 4 |
| [ollama/ollama](https://github.com/ollama/ollama) | Must-have | 176,491 | 3.1y | 212 | 2d ago | 2 |

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
| [obra/superpowers](https://github.com/obra/superpowers) | Trending | Coding agents & MCP | Shell | 257,811 (▲280) | Hot | 78 | very active | 0d ago | 9mo |
| [ollama/ollama](https://github.com/ollama/ollama) | Must-have | Inference & serving | Go | 176,491 (▲33) | Classic | 88 | very active | 2d ago | 3.1y |
| [anthropics/skills](https://github.com/anthropics/skills) | Trending | Coding agents & MCP | Python | 162,818 (▲125) | Rising | 45 | active | 3d ago | 10mo |
| [huggingface/transformers](https://github.com/huggingface/transformers) | Fundamental | Base & training | Python | 162,754 (▲15) | Classic | 99 | very active | 0d ago | 7.7y |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Must-have | Data & ingestion | TypeScript | 153,281 (▲143) | Mature | 84 | very active | 0d ago | 2.3y |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Must-have | Orchestration & agents | Python | 142,141 (▲43) | Classic | 85 | very active | 1d ago | 3.8y |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Trending | Coding agents & MCP | Python | 138,390 (▲60) | Hot | 77 | very active | 0d ago | 1.4y |
| [github/spec-kit](https://github.com/github/spec-kit) | Trending | Coding agents & MCP | Python | 122,508 (▲209) | Hot | 89 | very active | 2d ago | 11mo |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | Fundamental | Inference & serving | C++ | 121,006 (▲42) | Classic | 99 | very active | 0d ago | 3.4y |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | Fundamental | Learning | Jupyter Notebook | 113,260 (▲13) | Classic | 70 | very active | 2d ago | 3.1y |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Trending | Coding agents & MCP | TypeScript | 106,079 (▲6) | Hot | 99 | very active | 0d ago | 1.3y |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Trending | Orchestration & agents | Python | 105,645 (▲82) | Hot | 79 | very active | 3d ago | 1.7y |
| [openai/whisper](https://github.com/openai/whisper) | Fundamental | Voice & multimodal | Python | 105,272 (▲19) | Mature | 27 | slowing | 3mo ago | 3.8y |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | Fundamental | Learning | Jupyter Notebook | 99,415 (▲37) | Mature | 52 | active | 8d ago | 3.0y |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Trending | Orchestration & agents | Python | 93,746 (▲63) | Mature | 75 | very active | 2d ago | 1.6y |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Trending | Coding agents & MCP | — | 90,979 (▲11) | Hot | 64 | very active | 7d ago | 1.6y |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Trending | Coding agents & MCP | TypeScript | 88,650 (▲11) | Hot | 75 | very active | 10d ago | 1.7y |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | Must-have | Inference & serving | Python | 86,682 (▲34) | Classic | 99 | very active | 0d ago | 3.4y |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | Must-have | RAG & retrieval | Go | 85,442 (▲43) | Mature | 98 | very active | 0d ago | 2.6y |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | Trending | Coding agents & MCP | Python | 81,363 (▲46) | Mature | 95 | very active | 1d ago | 2.4y |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | Fundamental | Learning | — | 81,104 (▲6) | Mature | 20 | slowing | 5mo ago | 3.1y |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Trending | Orchestration & agents | Python | 77,423 (▲32) | Hot | 84 | very active | 0d ago | 1.2y |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | Fundamental | Learning | MDX | 76,757 (▲11) | Mature | 22 | slowing | 4mo ago | 3.6y |
| [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) | Must-have | Fine-tuning | Python | 73,385 (▲11) | Classic | 84 | very active | 3d ago | 3.1y |
| [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | Must-have | Data & ingestion | Python | 73,359 (▲46) | Mature | 83 | very active | 5d ago | 2.2y |
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | Must-have | Fine-tuning | Python | 68,445 (▲19) | Mature | 88 | very active | 0d ago | 2.6y |
| [labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | Fundamental | Learning | Python | 67,190 (▲9) | Mature | 23 | slowing | 5mo ago | 5.9y |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Trending | Memory | TypeScript | 61,274 (▲67) | Classic | 89 | very active | 0d ago | 3.1y |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Trending | Memory | Python | 57,493 (▲13) | Hot | 76 | very active | 3d ago | 3mo |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Must-have | Orchestration & agents | Python | 55,823 (▲35) | Mature | 85 | very active | 1d ago | 2.7y |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Must-have | Inference & serving | Python | 54,074 (▲48) | Mature | 89 | very active | 0d ago | 3.0y |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | Must-have | RAG & retrieval | Python | 50,953 (▲10) | Classic | 99 | very active | 4d ago | 3.7y |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | Must-have | Inference & serving | Go | 47,698 (▲15) | Classic | 79 | very active | 0d ago | 3.3y |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | Trending | Coding agents & MCP | Python | 47,529 (▲15) | Classic | 49 | active | 1mo ago | 3.2y |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | Must-have | Vector store | Go | 45,277 (▲3) | Classic | 99 | very active | 0d ago | 6.8y |
| [deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed) | Fundamental | Base & training | Python | 42,750 (▲2) | Classic | 96 | very active | 1d ago | 6.5y |
| [agno-agi/agno](https://github.com/agno-agi/agno) | Trending | Orchestration & agents | Python | 41,301 (▲10) | Classic | 93 | very active | 0d ago | 4.2y |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | Fundamental | Vector store | C++ | 40,544 (▲3) | Classic | 89 | very active | 2d ago | 9.5y |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Trending | Orchestration & agents | Rust | 38,809 (▲45) | Hot | 69 | very active | 1d ago | 6mo |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | Trending | RAG & retrieval | Python | 37,870 (▲28) | Hot | 79 | very active | 0d ago | 1.8y |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Must-have | Orchestration & agents | Python | 37,654 (▲39) | Mature | 77 | very active | 0d ago | 2.9y |
| [google/langextract](https://github.com/google/langextract) | Trending | Data & ingestion | Python | 37,591 (▲59) | Mature | 65 | active | 18d ago | 1.0y |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | Must-have | Orchestration & agents | Python | 36,237 (▲8) | Classic | 82 | very active | 4d ago | 3.5y |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Trending | Coding agents & MCP | TypeScript | 35,277 (▲7) | Hot | 73 | very active | 5d ago | 1.3y |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | Trending | RAG & retrieval | Python | 34,522 (▲11) | Mature | 69 | active | 0d ago | 2.3y |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Trending | RAG & retrieval | Python | 34,121 (▲11) | Hot | 63 | very active | 1d ago | 1.3y |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | Must-have | Vector store | Rust | 33,423 (▲16) | Classic | 93 | very active | 0d ago | 6.1y |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Must-have | Eval & observability | TypeScript | 31,458 (▲30) | Classic | 89 | very active | 0d ago | 3.2y |
| [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | Fundamental | Base & training | Python | 31,240 | Classic | 78 | very active | 0d ago | 7.3y |
| [karpathy/llm.c](https://github.com/karpathy/llm.c) | Fundamental | Learning | Cuda | 30,589 (▲6) | Abandoned | 4 | stale | 1.1y ago | 2.3y |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | Must-have | Inference & serving | Python | 30,534 (▲26) | Mature | 99 | very active | 0d ago | 2.5y |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | Must-have | Vector store | Rust | 28,833 (▲5) | Classic | 83 | very active | 2d ago | 3.8y |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | Fundamental | RAG & retrieval | Jupyter Notebook | 28,719 (▲12) | Mature | 59 | very active | 6d ago | 2.0y |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | Must-have | Orchestration & agents | Python | 28,441 (▲5) | Mature | 66 | active | 6d ago | 1.6y |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Trending | Eval & observability | Python | 20,714 (▲11) | Classic | 94 | very active | 0d ago | 3.2y |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Trending | Eval & observability | Python | 10,634 (▲8) | Classic | 79 | very active | 0d ago | 3.7y |

## Graph analysis — how they relate

**Community clustering.** These 56 repos span **20 of the graph's 28 communities** — the AI-engineering stack is genuinely cross-cutting, not one tidy neighborhood.

- **Community 5** (10): `langchain-ai/langchain`, `browser-use/browser-use`, `punkpeye/awesome-mcp-servers`, `dair-ai/Prompt-Engineering-Guide`, `mem0ai/mem0`, `MemPalace/mempalace`, `crewAIInc/crewAI`, `agno-agi/agno`, `langchain-ai/langgraph`, `chroma-core/chroma`
- **Community 22** (8): `ollama/ollama`, `huggingface/transformers`, `vllm-project/vllm`, `mlabonne/llm-course`, `hiyouga/LlamaFactory`, `unslothai/unsloth`, `sgl-project/sglang`, `huggingface/smolagents`
- **Community 16** (6): `openai/whisper`, `rasbt/LLMs-from-scratch`, `labmlai/annotated_deep_learning_paper_implementations`, `deepspeedai/DeepSpeed`, `facebookresearch/faiss`, `Lightning-AI/pytorch-lightning`
- **Community 8** (5): `TauricResearch/TradingAgents`, `infiniflow/ragflow`, `OpenHands/OpenHands`, `VectifyAI/PageIndex`, `NirDiamant/RAG_Techniques`
- **Community 21** (3): `microsoft/generative-ai-for-beginners`, `microsoft/playwright-mcp`, `microsoft/graphrag`
- **Community 7** (3): `obra/superpowers`, `google-gemini/gemini-cli`, `mudler/LocalAI`
- **Community 10** (3): `BerriAI/litellm`, `langfuse/langfuse`, `comet-ml/opik`

**Centrality (PageRank in the full 1,350-repo graph)** — the most 'hub-like' AI-eng repos in your stars (good signal for *foundational*):

- `microsoft/generative-ai-for-beginners` — PageRank 0.0038 (Fundamental)
- `Lightning-AI/pytorch-lightning` — PageRank 0.0033 (Fundamental)
- `agno-agi/agno` — PageRank 0.0025 (Trending)
- `VectifyAI/PageIndex` — PageRank 0.0021 (Trending)
- `HKUDS/LightRAG` — PageRank 0.0020 (Trending)
- `langchain-ai/langgraph` — PageRank 0.0020 (Must-have)
- `langchain-ai/langchain` — PageRank 0.0020 (Must-have)
- `NirDiamant/RAG_Techniques` — PageRank 0.0016 (Fundamental)
- `crewAIInc/crewAI` — PageRank 0.0015 (Must-have)
- `MemPalace/mempalace` — PageRank 0.0015 (Trending)

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). For *production* picks, prefer mature lifecycle + low single-author share; for *trending* picks, expect churn.

| Repo | Tier | Health | Lifecycle | Activity | Bus factor | Top-author share |
|---|---|---|---|---|---|---|
| huggingface/transformers | Fundamental | 99 | Classic | very active | 9 | 9% |
| ggml-org/llama.cpp | Fundamental | 99 | Classic | very active | 11 | 11% |
| run-llama/llama_index | Must-have | 99 | Classic | very active | 8 | 20% |
| vllm-project/vllm | Must-have | 99 | Classic | very active | 20 | 5% |
| sgl-project/sglang | Must-have | 99 | Mature | very active | 11 | 9% |
| milvus-io/milvus | Must-have | 99 | Classic | very active | 9 | 8% |
| google-gemini/gemini-cli | Trending | 99 | Hot | very active | 5 | 18% |
| infiniflow/ragflow | Must-have | 98 | Mature | very active | 6 | 13% |
| deepspeedai/DeepSpeed | Fundamental | 96 | Classic | very active | 6 | 29% |
| OpenHands/OpenHands | Trending | 95 | Mature | very active | 4 | 16% |
| comet-ml/opik | Trending | 94 | Classic | very active | 4 | 24% |
| qdrant/qdrant | Must-have | 93 | Classic | very active | 4 | 18% |
| agno-agi/agno | Trending | 93 | Classic | very active | 4 | 28% |
| facebookresearch/faiss | Fundamental | 89 | Classic | very active | 3 | 20% |
| BerriAI/litellm | Must-have | 89 | Mature | very active | 3 | 26% |
| langfuse/langfuse | Must-have | 89 | Classic | very active | 3 | 30% |
| github/spec-kit | Trending | 89 | Hot | very active | 3 | 20% |
| mem0ai/mem0 | Trending | 89 | Classic | very active | 3 | 37% |
| ollama/ollama | Must-have | 88 | Classic | very active | 3 | 22% |
| unslothai/unsloth | Must-have | 88 | Mature | very active | 3 | 20% |
| langchain-ai/langchain | Must-have | 85 | Classic | very active | 2 | 36% |
| crewAIInc/crewAI | Must-have | 85 | Mature | very active | 2 | 41% |
| hiyouga/LlamaFactory | Must-have | 84 | Classic | very active | 7 | 12% |
| firecrawl/firecrawl | Must-have | 84 | Mature | very active | 2 | 31% |
| bytedance/deer-flow | Trending | 84 | Hot | very active | 5 | 20% |
| chroma-core/chroma | Must-have | 83 | Classic | very active | 2 | 30% |
| unclecode/crawl4ai | Must-have | 83 | Mature | very active | 2 | 47% |
| stanfordnlp/dspy | Must-have | 82 | Classic | very active | 2 | 41% |
| mudler/LocalAI | Must-have | 79 | Classic | very active | 1 | 65% |
| browser-use/browser-use | Trending | 79 | Hot | very active | 1 | 70% |
| HKUDS/LightRAG | Trending | 79 | Hot | very active | 1 | 83% |
| Arize-ai/phoenix | Trending | 79 | Classic | very active | 1 | 68% |
| Lightning-AI/pytorch-lightning | Fundamental | 78 | Classic | very active | 2 | 37% |
| obra/superpowers | Trending | 78 | Hot | very active | 1 | 69% |
| langchain-ai/langgraph | Must-have | 77 | Mature | very active | 1 | 57% |
| anthropics/claude-code | Trending | 77 | Hot | very active | 1 | 84% |
| MemPalace/mempalace | Trending | 76 | Hot | very active | 1 | 53% |
| modelcontextprotocol/servers | Trending | 75 | Hot | very active | 2 | 41% |
| TauricResearch/TradingAgents | Trending | 75 | Mature | very active | 1 | 98% |
| microsoft/playwright-mcp | Trending | 73 | Hot | very active | 1 | 62% |
| microsoft/generative-ai-for-beginners | Fundamental | 70 | Classic | very active | 2 | 36% |
| vercel-labs/agent-browser | Trending | 69 | Hot | very active | 1 | 82% |
| microsoft/graphrag | Trending | 69 | Mature | active | 1 | 50% |
| huggingface/smolagents | Must-have | 66 | Mature | active | 1 | 56% |
| google/langextract | Trending | 65 | Mature | active | 1 | 89% |
| punkpeye/awesome-mcp-servers | Trending | 64 | Hot | very active | 1 | 96% |
| VectifyAI/PageIndex | Trending | 63 | Hot | very active | 2 | 40% |
| NirDiamant/RAG_Techniques | Fundamental | 59 | Mature | very active | 1 | 95% |
| rasbt/LLMs-from-scratch | Fundamental | 52 | Mature | active | 1 | 64% |
| Aider-AI/aider | Trending | 49 | Classic | active | 1 | 82% |
| anthropics/skills | Trending | 45 | Rising | active | 1 | 79% |
| openai/whisper | Fundamental | 27 | Mature | slowing | 0 | 0% |
| labmlai/annotated_deep_learning_paper_implementations | Fundamental | 23 | Mature | slowing | 0 | 0% |
| dair-ai/Prompt-Engineering-Guide | Fundamental | 22 | Mature | slowing | 0 | 0% |
| mlabonne/llm-course | Fundamental | 20 | Mature | slowing | 0 | 0% |
| karpathy/llm.c | Fundamental | 4 | Abandoned | stale | 0 | 0% |

## Adjacent (deliberately not in the core list)

- **Comfy-Org/ComfyUI** (121,488★) — image/diffusion tooling — a different (creative) AI discipline, out of scope here
- **PaddlePaddle/PaddleOCR** (85,841★) — OCR engine — a data-ingestion building block, folded into 'Data & ingestion'
- **n8n-io/n8n** (197,128★) — workflow automation — orchestrates agents but isn't core AI-eng tooling (see agent-orchestration report)
- **microsoft/autogen** (59,832★) — multi-agent framework — slipping in activity; crewAI/langgraph lead the must-have slot now
- **nomic-ai/gpt4all** (77,392★) — local-LLM app — superseded for most by ollama; kept off the must-have list

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`, cross-checked against 2026 AI-engineering landscape reporting. No private calls; fully reproducible.
- **Tiers and the solved/frontier verdicts are opinionated** — a synthesis of dataset signal (stars, lifecycle, commit velocity) and the current state of the field, not a benchmark. Treat 'Trending' as *volatile by definition*.
- **Selection** favors recognizable, broadly-applicable AI-engineering tooling. The coding-agent/harness ecosystem and voice stack are summarized here but detailed in the Claude-Code-setups and voice-agents reports respectively.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.

<sub>Repos covered: 56 · Snapshot: 2026-07-20T08:33:57.852Z</sub>
