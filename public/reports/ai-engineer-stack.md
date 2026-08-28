# The AI Engineer's Stack — What's Fundamental, Must-Have, and Trending

> Derived from **kaiser-data**'s 1,752 starred repos (snapshot `2026-08-28T01:21:50.535Z`), cross-referenced with the repo-similarity graph (1,752 nodes / 5,707 edges, 35 communities) and the 2026 AI-engineering landscape.
>
> Generated 2026-08-28 by `scripts/reports/ai_engineer_stack.py` (regenerate any time — no API cost).

![Top tools by stars](assets/ai-engineer-stack-top-tools.svg)

![Tools per category](assets/ai-engineer-stack-categories.svg)


## The one thing to understand first

In 2026 the **model layer is commoditizing** — model differences matter less each quarter, and the infrastructure beneath your app (serving, vector search, basic RAG, tracing) is **largely solved**. The value has moved *up the stack*: to **reliability, evaluation, context engineering, and memory** for agentic systems. So this report does two jobs at once — it tells you **which repos to know** (Fundamental / Must-have / Trending) *and* **which problems are already solved** (integrate, don't rebuild) **vs. still frontier** (where you actually add value).

> **Rule of thumb:** if a capability is ✅ *Solved* below, your job is to *integrate the best repo well*. If it's 🔴 *Frontier*, that's where a portfolio project or a job actually gets you noticed.

## The three tiers

### Fundamental (13)

**Bedrock you must understand.** Long-lived base libraries and learning resources. Tools change; these don't. If you can't explain these, you're assembling black boxes.

- **[huggingface/transformers](https://github.com/huggingface/transformers)** · 164,519★ · _Base & training_  
  The model-definition framework — the de-facto way to load/run almost any open model. Know it cold.
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 125,969★ · _Inference & serving_  
  Inference in C/C++ — the primitive behind on-device/edge LLMs; teaches you what quantization actually costs.
- **[microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)** · 118,665★ · _Learning_  
  21-lesson on-ramp to building with generative AI — the gentle starting point.
- **[openai/whisper](https://github.com/openai/whisper)** · 108,031★ · _Voice & multimodal_  
  The reference open ASR model — the baseline for any speech-in pipeline.
- **[rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)** · 103,916★ · _Learning_  
  Build a GPT in PyTorch step by step — the single best way to actually understand what you're orchestrating.
- **[mlabonne/llm-course](https://github.com/mlabonne/llm-course)** · 82,034★ · _Learning_  
  Roadmap + notebooks from fundamentals to deployment — the structured curriculum.
- **[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)** · 77,842★ · _Learning_  
  The canonical prompt-engineering reference — still load-bearing in an agentic world.
- **[labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations)** · 67,365★ · _Learning_  
  60+ annotated paper implementations — read the architectures, don't just import them.
- **[deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed)** · 43,014★ · _Base & training_  
  Training-optimization library (ZeRO, offload) — how large models actually get trained on real hardware.
- **[facebookresearch/faiss](https://github.com/facebookresearch/faiss)** · 40,812★ · _Vector store_  
  The original similarity-search library — the math under every vector DB; understand it before reaching for one.
- **[Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning)** · 31,313★ · _Base & training_  
  Structured PyTorch training — the bridge between research code and reproducible training runs.
- **[karpathy/llm.c](https://github.com/karpathy/llm.c)** · 30,886★ · _Learning_  
  LLM training in raw C/CUDA — strips away the framework to show the actual compute.
- **[NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)** · 29,253★ · _RAG & retrieval_  
  A catalog of advanced RAG techniques with code — the reference when naive RAG isn't enough.

### Must-have (20)

**Your default production toolkit.** The repos you reach for on basically every project — the boring, load-bearing choices. Master integration, not novelty.

- **[ollama/ollama](https://github.com/ollama/ollama)** · 179,588★ · _Inference & serving_  
  One command to run open models locally — the dev-loop and prototyping default.
- **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** · 173,242★ · _Data & ingestion_  
  Search/scrape/crawl the web into LLM-ready data — the ingestion default for RAG & agents.
- **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** · 145,151★ · _Orchestration & agents_  
  The most-deployed agent/LLM framework — the lingua franca; you'll read code that uses it even if you don't.
- **[vllm-project/vllm](https://github.com/vllm-project/vllm)** · 90,249★ · _Inference & serving_  
  High-throughput serving engine (PagedAttention) — the production answer for self-hosting at scale.
- **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** · 89,410★ · _RAG & retrieval_  
  Batteries-included RAG engine with deep document understanding — RAG as a deployable product.
- **[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)** · 79,574★ · _Data & ingestion_  
  LLM-friendly open crawler/scraper — self-hosted ingestion when you don't want an API.
- **[unslothai/unsloth](https://github.com/unslothai/unsloth)** · 74,995★ · _Fine-tuning_  
  2× faster, lower-memory LoRA/QLoRA fine-tuning — the practical fine-tuning default.
- **[hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)** · 74,403★ · _Fine-tuning_  
  Unified fine-tuning UI/CLI for 100+ models — the no-code-ish path to a tuned model.
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** · 57,688★ · _Orchestration & agents_  
  Role-playing multi-agent orchestration — the popular 'team of agents' framework.
- **[BerriAI/litellm](https://github.com/BerriAI/litellm)** · 57,425★ · _Inference & serving_  
  OpenAI-compatible gateway to 100+ LLMs — swap/route/budget models from one endpoint. Non-negotiable glue.
- **[run-llama/llama_index](https://github.com/run-llama/llama_index)** · 51,894★ · _RAG & retrieval_  
  The leading data/RAG framework — connectors, indexing, query engines; the RAG default alongside LangChain.
- **[mudler/LocalAI](https://github.com/mudler/LocalAI)** · 48,711★ · _Inference & serving_  
  OpenAI-compatible local engine (LLM/vision/voice) — self-host the whole API surface.
- **[milvus-io/milvus](https://github.com/milvus-io/milvus)** · 45,834★ · _Vector store_  
  Cloud-native vector DB built for massive scale — when you outgrow a single box.
- **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** · 40,570★ · _Orchestration & agents_  
  Explicit graphs over implicit chains — the 2026 standard for *production-grade* agent control flow.
- **[stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)** · 37,627★ · _Orchestration & agents_  
  Program — don't prompt — LLMs; compile prompts against metrics. The antidote to prompt-spaghetti.
- **[qdrant/qdrant](https://github.com/qdrant/qdrant)** · 34,228★ · _Vector store_  
  High-performance Rust vector DB — the popular standalone choice; great filtering.
- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 33,820★ · _Eval & observability_  
  Open-source LLM tracing/evals/prompts — you can't ship what you can't see (you run this).
- **[sgl-project/sglang](https://github.com/sgl-project/sglang)** · 32,584★ · _Inference & serving_  
  Fast serving with structured-output + prefix-cache wins — vLLM's main rival; learn both.
- **[chroma-core/chroma](https://github.com/chroma-core/chroma)** · 29,166★ · _Vector store_  
  The 'just works' embedded vector store — fastest path from zero to a working RAG.
- **[huggingface/smolagents](https://github.com/huggingface/smolagents)** · 29,022★ · _Orchestration & agents_  
  Barebones code-writing agents — the minimal mental model of what an agent loop *is*.

### Trending (23)

**Where the energy is right now (2026).** Fast-moving, high-upside, often unstable. Learn these to stay current and to find differentiated things to build.

- **[obra/superpowers](https://github.com/obra/superpowers)** · 278,661★ · _Coding agents & MCP_  
  The headline agentic-skills framework — the most-starred repo in this whole set.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 172,083★ · _Coding agents & MCP_  
  Agent Skills — on-demand capability that's displacing always-on prompt bloat.
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 143,202★ · _Coding agents & MCP_  
  The agentic coding CLI — the flagship of the coding-agent wave (full ecosystem in the cc-setups report).
- **[github/spec-kit](https://github.com/github/spec-kit)** · 131,901★ · _Coding agents & MCP_  
  Spec-driven development toolkit — the 'write the spec, let the agent build' workflow.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 111,455★ · _Orchestration & agents_  
  Let agents drive real browsers — the computer-use frontier; high promise, still flaky.
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 106,719★ · _Coding agents & MCP_  
  Gemini's terminal agent — the third major CLI harness; useful for model-shopping.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 101,235★ · _Orchestration & agents_  
  Multi-agent trading framework — the template for *vertical* agent systems with real domain logic.
- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 92,895★ · _Coding agents & MCP_  
  The community MCP index — discovery for the fastest-growing integration ecosystem.
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 89,915★ · _Coding agents & MCP_  
  Reference MCP servers — MCP is the emerging standard for wiring tools/data into any agent.
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 85,316★ · _Coding agents & MCP_  
  Open autonomous software-engineering agent — the OSS face of the SWE-agent race.
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 81,018★ · _Orchestration & agents_  
  Long-horizon research+code SuperAgent — the 'deep research' pattern as a harness.
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 64,203★ · _Memory_  
  Universal memory layer for agents — the most-adopted bet on the unsolved memory problem.
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 58,685★ · _Memory_  
  Best-benchmarked open memory system — a strong contender in a still-open race.
- **[Aider-AI/aider](https://github.com/Aider-AI/aider)** · 48,536★ · _Coding agents & MCP_  
  AI pair-programming in the terminal with tight git integration — a beloved daily driver.
- **[agno-agi/agno](https://github.com/agno-agi/agno)** · 41,945★ · _Orchestration & agents_  
  Build/run/manage agent platforms — a fast-rising full-stack agent framework.
- **[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)** · 41,443★ · _Orchestration & agents_  
  Browser-automation CLI for agents — the lighter, scriptable take on web agents.
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 39,235★ · _RAG & retrieval_  
  Graph-augmented RAG that's simple and fast — the practical face of 'RAG beyond chunks'.
- **[google/langextract](https://github.com/google/langextract)** · 38,497★ · _Data & ingestion_  
  Structured extraction from unstructured text — turning documents into typed data.
- **[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)** · 36,552★ · _Coding agents & MCP_  
  Playwright as an MCP server — reliable, structured web control for agents.
- **[microsoft/graphrag](https://github.com/microsoft/graphrag)** · 35,707★ · _RAG & retrieval_  
  Graph-based RAG — structure-aware retrieval for global/whole-corpus questions.
- **[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** · 35,344★ · _RAG & retrieval_  
  Vectorless, reasoning-based retrieval — a bet that reasoning can replace embeddings.
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 21,642★ · _Eval & observability_  
  Eval-first LLM/agent observability — measuring agents, not just logging them.
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 11,218★ · _Eval & observability_  
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
| [obra/superpowers](https://github.com/obra/superpowers) | Trending | 278,661 | 10mo | 240 | 8d ago | 7 |
| [github/spec-kit](https://github.com/github/spec-kit) | Trending | 131,901 | 1.0y | 831 | 0d ago | 7 |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Trending | 58,685 | 4mo | 725 | 0d ago | 7 |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Trending | 41,443 | 7mo | 70 | 1d ago | 7 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Trending | 143,202 | 1.5y | 95 | 0d ago | 5 |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Trending | 111,455 | 1.8y | 799 | 0d ago | 5 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Trending | 106,719 | 1.4y | 156 | 0d ago | 5 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Trending | 92,895 | 1.7y | 2698 | 0d ago | 5 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Trending | 89,915 | 1.8y | 54 | 8d ago | 5 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Trending | 81,018 | 1.3y | 860 | 0d ago | 5 |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | Trending | 39,235 | 1.9y | 1809 | 0d ago | 5 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Trending | 35,344 | 1.4y | 105 | 0d ago | 5 |
| [anthropics/skills](https://github.com/anthropics/skills) | Trending | 172,083 | 11mo | 15 | 6d ago | 4 |
| [ollama/ollama](https://github.com/ollama/ollama) | Must-have | 179,588 | 3.2y | 297 | 0d ago | 2 |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Must-have | 173,242 | 2.4y | 627 | 0d ago | 2 |

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
| [obra/superpowers](https://github.com/obra/superpowers) | Trending | Coding agents & MCP | Shell | 278,661 (▲9,978) | Hot | 78 | very active | 8d ago | 10mo |
| [ollama/ollama](https://github.com/ollama/ollama) | Must-have | Inference & serving | Go | 179,588 (▲1,574) | Classic | 83 | very active | 0d ago | 3.2y |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Must-have | Data & ingestion | TypeScript | 173,242 (▲10,390) | Mature | 89 | very active | 0d ago | 2.4y |
| [anthropics/skills](https://github.com/anthropics/skills) | Trending | Coding agents & MCP | Python | 172,083 (▲5,199) | Rising | 50 | active | 6d ago | 11mo |
| [huggingface/transformers](https://github.com/huggingface/transformers) | Fundamental | Base & training | Python | 164,519 (▲1,075) | Classic | 100 | very active | 0d ago | 7.8y |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Must-have | Orchestration & agents | Python | 145,151 (▲1,505) | Classic | 90 | very active | 0d ago | 3.9y |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Trending | Coding agents & MCP | Python | 143,202 (▲2,603) | Hot | 77 | very active | 0d ago | 1.5y |
| [github/spec-kit](https://github.com/github/spec-kit) | Trending | Coding agents & MCP | Python | 131,901 (▲6,129) | Hot | 84 | very active | 0d ago | 1.0y |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | Fundamental | Inference & serving | C++ | 125,969 (▲2,958) | Classic | 99 | very active | 0d ago | 3.5y |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | Fundamental | Learning | Jupyter Notebook | 118,665 (▲1,742) | Classic | 70 | very active | 1d ago | 3.2y |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Trending | Orchestration & agents | Python | 111,455 (▲3,258) | Hot | 84 | very active | 0d ago | 1.8y |
| [openai/whisper](https://github.com/openai/whisper) | Fundamental | Voice & multimodal | Python | 108,031 (▲1,175) | Mature | 40 | active | 1mo ago | 3.9y |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Trending | Coding agents & MCP | TypeScript | 106,719 (▲311) | Hot | 90 | very active | 0d ago | 1.4y |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | Fundamental | Learning | Jupyter Notebook | 103,916 (▲3,024) | Mature | 57 | active | 1d ago | 3.1y |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Trending | Orchestration & agents | Python | 101,235 (▲5,162) | Mature | 69 | active | 1mo ago | 1.7y |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Trending | Coding agents & MCP | — | 92,895 (▲954) | Hot | 65 | very active | 0d ago | 1.7y |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | Must-have | Inference & serving | Python | 90,249 (▲1,791) | Classic | 99 | very active | 0d ago | 3.6y |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Trending | Coding agents & MCP | TypeScript | 89,915 (▲588) | Hot | 78 | very active | 8d ago | 1.8y |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | Must-have | RAG & retrieval | Go | 89,410 (▲2,376) | Mature | 98 | very active | 0d ago | 2.7y |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | Trending | Coding agents & MCP | TypeScript | 85,316 (▲1,924) | Mature | 94 | very active | 0d ago | 2.5y |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | Fundamental | Learning | — | 82,034 (▲524) | Declining | 16 | stale | 6mo ago | 3.2y |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Trending | Orchestration & agents | Python | 81,018 (▲1,506) | Hot | 84 | very active | 0d ago | 1.3y |
| [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | Must-have | Data & ingestion | Python | 79,574 (▲2,375) | Mature | 81 | very active | 3d ago | 2.3y |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | Fundamental | Learning | MDX | 77,842 (▲508) | Mature | 19 | slowing | 5mo ago | 3.7y |
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | Must-have | Fine-tuning | Python | 74,995 (▲5,310) | Mature | 83 | very active | 0d ago | 2.7y |
| [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) | Must-have | Fine-tuning | Python | 74,403 (▲504) | Classic | 84 | very active | 1d ago | 3.3y |
| [labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | Fundamental | Learning | Python | 67,365 (▲73) | Declining | 20 | stale | 7mo ago | 6.0y |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Trending | Memory | Python | 64,203 (▲1,424) | Classic | 79 | very active | 0d ago | 3.2y |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Trending | Memory | Python | 58,685 (▲493) | Hot | 76 | very active | 0d ago | 4mo |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Must-have | Orchestration & agents | Python | 57,688 (▲936) | Mature | 85 | very active | 0d ago | 2.8y |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Must-have | Inference & serving | Python | 57,425 (▲1,599) | Classic | 84 | very active | 0d ago | 3.1y |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | Must-have | RAG & retrieval | Python | 51,894 (▲447) | Classic | 98 | very active | 0d ago | 3.8y |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | Must-have | Inference & serving | Go | 48,711 (▲401) | Classic | 84 | very active | 0d ago | 3.4y |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | Trending | Coding agents & MCP | Python | 48,536 (▲507) | Mature | 29 | slowing | 3mo ago | 3.3y |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | Must-have | Vector store | Go | 45,834 (▲281) | Classic | 99 | very active | 0d ago | 7.0y |
| [deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed) | Fundamental | Base & training | Python | 43,014 (▲135) | Classic | 97 | very active | 0d ago | 6.6y |
| [agno-agi/agno](https://github.com/agno-agi/agno) | Trending | Orchestration & agents | Python | 41,945 (▲326) | Classic | 98 | very active | 0d ago | 4.3y |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Trending | Orchestration & agents | Rust | 41,443 (▲1,280) | Hot | 71 | very active | 1d ago | 7mo |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | Fundamental | Vector store | C++ | 40,812 (▲122) | Classic | 94 | very active | 1d ago | 9.6y |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Must-have | Orchestration & agents | Python | 40,570 (▲1,427) | Classic | 77 | very active | 0d ago | 3.1y |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | Trending | RAG & retrieval | Python | 39,235 (▲615) | Hot | 79 | very active | 0d ago | 1.9y |
| [google/langextract](https://github.com/google/langextract) | Trending | Data & ingestion | Python | 38,497 (▲505) | Mature | 64 | active | 0d ago | 1.1y |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | Must-have | Orchestration & agents | Python | 37,627 (▲943) | Classic | 83 | very active | 0d ago | 3.6y |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Trending | Coding agents & MCP | TypeScript | 36,552 (▲657) | Mature | 76 | very active | 0d ago | 1.4y |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | Trending | RAG & retrieval | Python | 35,707 (▲388) | Mature | 71 | very active | 3d ago | 2.4y |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Trending | RAG & retrieval | Python | 35,344 (▲278) | Hot | 73 | very active | 0d ago | 1.4y |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | Must-have | Vector store | Rust | 34,228 (▲393) | Classic | 87 | very active | 0d ago | 6.2y |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Must-have | Eval & observability | TypeScript | 33,820 (▲1,112) | Classic | 94 | very active | 0d ago | 3.3y |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | Must-have | Inference & serving | Python | 32,584 (▲1,082) | Mature | 99 | very active | 0d ago | 2.6y |
| [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | Fundamental | Base & training | Python | 31,313 (▲37) | Classic | 76 | very active | 2d ago | 7.4y |
| [karpathy/llm.c](https://github.com/karpathy/llm.c) | Fundamental | Learning | Cuda | 30,886 (▲137) | Abandoned | 4 | stale | 1.2y ago | 2.4y |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | Fundamental | RAG & retrieval | Jupyter Notebook | 29,253 (▲277) | Mature | 60 | very active | 0d ago | 2.1y |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | Must-have | Vector store | Rust | 29,166 (▲192) | Classic | 83 | very active | 1d ago | 3.9y |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | Must-have | Orchestration & agents | Python | 29,022 (▲303) | Mature | 60 | active | 2d ago | 1.7y |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Trending | Eval & observability | Python | 21,642 (▲445) | Classic | 93 | very active | 0d ago | 3.3y |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Trending | Eval & observability | Python | 11,218 (▲281) | Classic | 84 | very active | 0d ago | 3.8y |

## Graph analysis — how they relate

**Community clustering.** These 56 repos span **18 of the graph's 35 communities** — the AI-engineering stack is genuinely cross-cutting, not one tidy neighborhood.

- **Community 8** (10): `langchain-ai/langchain`, `infiniflow/ragflow`, `OpenHands/OpenHands`, `dair-ai/Prompt-Engineering-Guide`, `mem0ai/mem0`, `milvus-io/milvus`, `langchain-ai/langgraph`, `VectifyAI/PageIndex`, `qdrant/qdrant`, `NirDiamant/RAG_Techniques`
- **Community 21** (7): `ollama/ollama`, `huggingface/transformers`, `ggml-org/llama.cpp`, `vllm-project/vllm`, `hiyouga/LlamaFactory`, `sgl-project/sglang`, `huggingface/smolagents`
- **Community 6** (7): `obra/superpowers`, `firecrawl/firecrawl`, `browser-use/browser-use`, `MemPalace/mempalace`, `crewAIInc/crewAI`, `agno-agi/agno`, `chroma-core/chroma`
- **Community 18** (5): `rasbt/LLMs-from-scratch`, `labmlai/annotated_deep_learning_paper_implementations`, `deepspeedai/DeepSpeed`, `facebookresearch/faiss`, `Lightning-AI/pytorch-lightning`
- **Community 10** (5): `BerriAI/litellm`, `mudler/LocalAI`, `langfuse/langfuse`, `comet-ml/opik`, `Arize-ai/phoenix`
- **Community 26** (4): `github/spec-kit`, `google-gemini/gemini-cli`, `punkpeye/awesome-mcp-servers`, `modelcontextprotocol/servers`
- **Community 22** (3): `openai/whisper`, `unclecode/crawl4ai`, `unslothai/unsloth`
- **Community 15** (3): `microsoft/generative-ai-for-beginners`, `microsoft/playwright-mcp`, `microsoft/graphrag`

**Centrality (PageRank in the full 1,752-repo graph)** — the most 'hub-like' AI-eng repos in your stars (good signal for *foundational*):

- `microsoft/generative-ai-for-beginners` — PageRank 0.0028 (Fundamental)
- `Lightning-AI/pytorch-lightning` — PageRank 0.0027 (Fundamental)
- `langchain-ai/langgraph` — PageRank 0.0019 (Must-have)
- `agno-agi/agno` — PageRank 0.0018 (Trending)
- `VectifyAI/PageIndex` — PageRank 0.0017 (Trending)
- `langchain-ai/langchain` — PageRank 0.0016 (Must-have)
- `MemPalace/mempalace` — PageRank 0.0015 (Trending)
- `crewAIInc/crewAI` — PageRank 0.0014 (Must-have)
- `NirDiamant/RAG_Techniques` — PageRank 0.0013 (Fundamental)
- `comet-ml/opik` — PageRank 0.0011 (Trending)

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). For *production* picks, prefer mature lifecycle + low single-author share; for *trending* picks, expect churn.

| Repo | Tier | Health | Lifecycle | Activity | Bus factor | Top-author share |
|---|---|---|---|---|---|---|
| huggingface/transformers | Fundamental | 100 | Classic | very active | 6 | 23% |
| ggml-org/llama.cpp | Fundamental | 99 | Classic | very active | 6 | 17% |
| vllm-project/vllm | Must-have | 99 | Classic | very active | 28 | 6% |
| sgl-project/sglang | Must-have | 99 | Mature | very active | 11 | 12% |
| milvus-io/milvus | Must-have | 99 | Classic | very active | 8 | 12% |
| run-llama/llama_index | Must-have | 98 | Classic | very active | 16 | 6% |
| infiniflow/ragflow | Must-have | 98 | Mature | very active | 7 | 9% |
| agno-agi/agno | Trending | 98 | Classic | very active | 5 | 27% |
| deepspeedai/DeepSpeed | Fundamental | 97 | Classic | very active | 6 | 14% |
| facebookresearch/faiss | Fundamental | 94 | Classic | very active | 4 | 27% |
| langfuse/langfuse | Must-have | 94 | Classic | very active | 4 | 23% |
| OpenHands/OpenHands | Trending | 94 | Mature | very active | 4 | 16% |
| comet-ml/opik | Trending | 93 | Classic | very active | 4 | 19% |
| langchain-ai/langchain | Must-have | 90 | Classic | very active | 3 | 31% |
| google-gemini/gemini-cli | Trending | 90 | Hot | very active | 3 | 19% |
| firecrawl/firecrawl | Must-have | 89 | Mature | very active | 3 | 19% |
| qdrant/qdrant | Must-have | 87 | Classic | very active | 3 | 34% |
| crewAIInc/crewAI | Must-have | 85 | Mature | very active | 2 | 47% |
| mudler/LocalAI | Must-have | 84 | Classic | very active | 2 | 47% |
| BerriAI/litellm | Must-have | 84 | Classic | very active | 2 | 41% |
| hiyouga/LlamaFactory | Must-have | 84 | Classic | very active | 7 | 10% |
| browser-use/browser-use | Trending | 84 | Hot | very active | 2 | 49% |
| github/spec-kit | Trending | 84 | Hot | very active | 2 | 38% |
| bytedance/deer-flow | Trending | 84 | Hot | very active | 12 | 10% |
| Arize-ai/phoenix | Trending | 84 | Classic | very active | 2 | 38% |
| ollama/ollama | Must-have | 83 | Classic | very active | 2 | 35% |
| chroma-core/chroma | Must-have | 83 | Classic | very active | 2 | 48% |
| stanfordnlp/dspy | Must-have | 83 | Classic | very active | 2 | 47% |
| unslothai/unsloth | Must-have | 83 | Mature | very active | 2 | 43% |
| unclecode/crawl4ai | Must-have | 81 | Mature | very active | 2 | 42% |
| mem0ai/mem0 | Trending | 79 | Classic | very active | 1 | 52% |
| HKUDS/LightRAG | Trending | 79 | Hot | very active | 1 | 71% |
| modelcontextprotocol/servers | Trending | 78 | Hot | very active | 2 | 31% |
| obra/superpowers | Trending | 78 | Hot | very active | 1 | 82% |
| langchain-ai/langgraph | Must-have | 77 | Classic | very active | 1 | 60% |
| anthropics/claude-code | Trending | 77 | Hot | very active | 1 | 89% |
| Lightning-AI/pytorch-lightning | Fundamental | 76 | Classic | very active | 2 | 42% |
| microsoft/playwright-mcp | Trending | 76 | Mature | very active | 2 | 43% |
| MemPalace/mempalace | Trending | 76 | Hot | very active | 1 | 75% |
| VectifyAI/PageIndex | Trending | 73 | Hot | very active | 1 | 68% |
| vercel-labs/agent-browser | Trending | 71 | Hot | very active | 1 | 61% |
| microsoft/graphrag | Trending | 71 | Mature | very active | 1 | 65% |
| microsoft/generative-ai-for-beginners | Fundamental | 70 | Classic | very active | 2 | 36% |
| TauricResearch/TradingAgents | Trending | 69 | Mature | active | 1 | 100% |
| punkpeye/awesome-mcp-servers | Trending | 65 | Hot | very active | 1 | 74% |
| google/langextract | Trending | 64 | Mature | active | 1 | 92% |
| NirDiamant/RAG_Techniques | Fundamental | 60 | Mature | very active | 1 | 96% |
| huggingface/smolagents | Must-have | 60 | Mature | active | 1 | 63% |
| rasbt/LLMs-from-scratch | Fundamental | 57 | Mature | active | 2 | 44% |
| anthropics/skills | Trending | 50 | Rising | active | 2 | 47% |
| openai/whisper | Fundamental | 40 | Mature | active | 1 | 50% |
| Aider-AI/aider | Trending | 29 | Mature | slowing | 0 | 0% |
| labmlai/annotated_deep_learning_paper_implementations | Fundamental | 20 | Declining | stale | 0 | 0% |
| dair-ai/Prompt-Engineering-Guide | Fundamental | 19 | Mature | slowing | 0 | 0% |
| mlabonne/llm-course | Fundamental | 16 | Declining | stale | 0 | 0% |
| karpathy/llm.c | Fundamental | 4 | Abandoned | stale | 0 | 0% |

## Adjacent (deliberately not in the core list)

- **Comfy-Org/ComfyUI** (130,325★) — image/diffusion tooling — a different (creative) AI discipline, out of scope here
- **PaddlePaddle/PaddleOCR** (88,359★) — OCR engine — a data-ingestion building block, folded into 'Data & ingestion'
- **n8n-io/n8n** (202,638★) — workflow automation — orchestrates agents but isn't core AI-eng tooling (see agent-orchestration report)
- **microsoft/autogen** (60,659★) — multi-agent framework — slipping in activity; crewAI/langgraph lead the must-have slot now
- **nomic-ai/gpt4all** (77,396★) — local-LLM app — superseded for most by ollama; kept off the must-have list

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`, cross-checked against 2026 AI-engineering landscape reporting. No private calls; fully reproducible.
- **Tiers and the solved/frontier verdicts are opinionated** — a synthesis of dataset signal (stars, lifecycle, commit velocity) and the current state of the field, not a benchmark. Treat 'Trending' as *volatile by definition*.
- **Selection** favors recognizable, broadly-applicable AI-engineering tooling. The coding-agent/harness ecosystem and voice stack are summarized here but detailed in the Claude-Code-setups and voice-agents reports respectively.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.

<sub>Repos covered: 56 · Snapshot: 2026-08-28T01:21:50.535Z</sub>
