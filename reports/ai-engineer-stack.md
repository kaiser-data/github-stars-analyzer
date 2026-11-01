# The AI Engineer's Stack — What's Fundamental, Must-Have, and Trending

> Derived from **kaiser-data**'s 2,585 starred repos (snapshot `2026-11-01T12:41:55.392Z`), cross-referenced with the repo-similarity graph (2,585 nodes / 8,670 edges, 45 communities) and the 2026 AI-engineering landscape.
>
> Generated 2026-11-01 by `scripts/reports/ai_engineer_stack.py` (regenerate any time — no API cost).

![Top tools by stars](assets/ai-engineer-stack-top-tools.svg)

![Tools per category](assets/ai-engineer-stack-categories.svg)


## The one thing to understand first

In 2026 the **model layer is commoditizing** — model differences matter less each quarter, and the infrastructure beneath your app (serving, vector search, basic RAG, tracing) is **largely solved**. The value has moved *up the stack*: to **reliability, evaluation, context engineering, and memory** for agentic systems. So this report does two jobs at once — it tells you **which repos to know** (Fundamental / Must-have / Trending) *and* **which problems are already solved** (integrate, don't rebuild) **vs. still frontier** (where you actually add value).

> **Rule of thumb:** if a capability is ✅ *Solved* below, your job is to *integrate the best repo well*. If it's 🔴 *Frontier*, that's where a portfolio project or a job actually gets you noticed.

## The three tiers

### Fundamental (13)

**Bedrock you must understand.** Long-lived base libraries and learning resources. Tools change; these don't. If you can't explain these, you're assembling black boxes.

- **[huggingface/transformers](https://github.com/huggingface/transformers)** · 168,404★ · _Base & training_  
  The model-definition framework — the de-facto way to load/run almost any open model. Know it cold.
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** · 133,039★ · _Inference & serving_  
  Inference in C/C++ — the primitive behind on-device/edge LLMs; teaches you what quantization actually costs.
- **[microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)** · 122,712★ · _Learning_  
  21-lesson on-ramp to building with generative AI — the gentle starting point.
- **[openai/whisper](https://github.com/openai/whisper)** · 111,694★ · _Voice & multimodal_  
  The reference open ASR model — the baseline for any speech-in pipeline.
- **[rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)** · 107,629★ · _Learning_  
  Build a GPT in PyTorch step by step — the single best way to actually understand what you're orchestrating.
- **[mlabonne/llm-course](https://github.com/mlabonne/llm-course)** · 84,831★ · _Learning_  
  Roadmap + notebooks from fundamentals to deployment — the structured curriculum.
- **[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)** · 79,729★ · _Learning_  
  The canonical prompt-engineering reference — still load-bearing in an agentic world.
- **[labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations)** · 67,627★ · _Learning_  
  60+ annotated paper implementations — read the architectures, don't just import them.
- **[deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed)** · 43,278★ · _Base & training_  
  Training-optimization library (ZeRO, offload) — how large models actually get trained on real hardware.
- **[facebookresearch/faiss](https://github.com/facebookresearch/faiss)** · 41,245★ · _Vector store_  
  The original similarity-search library — the math under every vector DB; understand it before reaching for one.
- **[Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning)** · 31,434★ · _Base & training_  
  Structured PyTorch training — the bridge between research code and reproducible training runs.
- **[karpathy/llm.c](https://github.com/karpathy/llm.c)** · 31,346★ · _Learning_  
  LLM training in raw C/CUDA — strips away the framework to show the actual compute.
- **[NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)** · 30,167★ · _RAG & retrieval_  
  A catalog of advanced RAG techniques with code — the reference when naive RAG isn't enough.

### Must-have (20)

**Your default production toolkit.** The repos you reach for on basically every project — the boring, load-bearing choices. Master integration, not novelty.

- **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** · 197,537★ · _Data & ingestion_  
  Search/scrape/crawl the web into LLM-ready data — the ingestion default for RAG & agents.
- **[ollama/ollama](https://github.com/ollama/ollama)** · 185,540★ · _Inference & serving_  
  One command to run open models locally — the dev-loop and prototyping default.
- **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** · 148,809★ · _Orchestration & agents_  
  The most-deployed agent/LLM framework — the lingua franca; you'll read code that uses it even if you don't.
- **[vllm-project/vllm](https://github.com/vllm-project/vllm)** · 96,036★ · _Inference & serving_  
  High-throughput serving engine (PagedAttention) — the production answer for self-hosting at scale.
- **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** · 93,284★ · _RAG & retrieval_  
  Batteries-included RAG engine with deep document understanding — RAG as a deployable product.
- **[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)** · 86,692★ · _Data & ingestion_  
  LLM-friendly open crawler/scraper — self-hosted ingestion when you don't want an API.
- **[unslothai/unsloth](https://github.com/unslothai/unsloth)** · 78,905★ · _Fine-tuning_  
  2× faster, lower-memory LoRA/QLoRA fine-tuning — the practical fine-tuning default.
- **[hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)** · 75,817★ · _Fine-tuning_  
  Unified fine-tuning UI/CLI for 100+ models — the no-code-ish path to a tuned model.
- **[BerriAI/litellm](https://github.com/BerriAI/litellm)** · 62,484★ · _Inference & serving_  
  OpenAI-compatible gateway to 100+ LLMs — swap/route/budget models from one endpoint. Non-negotiable glue.
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** · 60,369★ · _Orchestration & agents_  
  Role-playing multi-agent orchestration — the popular 'team of agents' framework.
- **[run-llama/llama_index](https://github.com/run-llama/llama_index)** · 52,767★ · _RAG & retrieval_  
  The leading data/RAG framework — connectors, indexing, query engines; the RAG default alongside LangChain.
- **[mudler/LocalAI](https://github.com/mudler/LocalAI)** · 50,108★ · _Inference & serving_  
  OpenAI-compatible local engine (LLM/vision/voice) — self-host the whole API surface.
- **[milvus-io/milvus](https://github.com/milvus-io/milvus)** · 46,548★ · _Vector store_  
  Cloud-native vector DB built for massive scale — when you outgrow a single box.
- **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** · 44,260★ · _Orchestration & agents_  
  Explicit graphs over implicit chains — the 2026 standard for *production-grade* agent control flow.
- **[stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)** · 38,873★ · _Orchestration & agents_  
  Program — don't prompt — LLMs; compile prompts against metrics. The antidote to prompt-spaghetti.
- **[sgl-project/sglang](https://github.com/sgl-project/sglang)** · 38,337★ · _Inference & serving_  
  Fast serving with structured-output + prefix-cache wins — vLLM's main rival; learn both.
- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 36,823★ · _Eval & observability_  
  Open-source LLM tracing/evals/prompts — you can't ship what you can't see (you run this).
- **[qdrant/qdrant](https://github.com/qdrant/qdrant)** · 35,360★ · _Vector store_  
  High-performance Rust vector DB — the popular standalone choice; great filtering.
- **[huggingface/smolagents](https://github.com/huggingface/smolagents)** · 30,163★ · _Orchestration & agents_  
  Barebones code-writing agents — the minimal mental model of what an agent loop *is*.
- **[chroma-core/chroma](https://github.com/chroma-core/chroma)** · 29,616★ · _Vector store_  
  The 'just works' embedded vector store — fastest path from zero to a working RAG.

### Trending (24)

**Where the energy is right now (2026).** Fast-moving, high-upside, often unstable. Learn these to stay current and to find differentiated things to build.

- **[obra/superpowers](https://github.com/obra/superpowers)** · 310,340★ · _Coding agents & MCP_  
  The headline agentic-skills framework — the most-starred repo in this whole set.
- **[anthropics/skills](https://github.com/anthropics/skills)** · 186,105★ · _Coding agents & MCP_  
  Agent Skills — on-demand capability that's displacing always-on prompt bloat.
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 154,131★ · _Coding agents & MCP_  
  The agentic coding CLI — the flagship of the coding-agent wave (full ecosystem in the cc-setups report).
- **[github/spec-kit](https://github.com/github/spec-kit)** · 144,677★ · _Coding agents & MCP_  
  Spec-driven development toolkit — the 'write the spec, let the agent build' workflow.
- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** · 119,728★ · _Orchestration & agents_  
  Let agents drive real browsers — the computer-use frontier; high promise, still flaky.
- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 119,283★ · _Orchestration & agents_  
  Multi-agent trading framework — the template for *vertical* agent systems with real domain logic.
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 108,646★ · _Coding agents & MCP_  
  Gemini's terminal agent — the third major CLI harness; useful for model-shopping.
- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 97,152★ · _Coding agents & MCP_  
  The community MCP index — discovery for the fastest-growing integration ecosystem.
- **[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)** · 92,408★ · _Coding agents & MCP_  
  Open autonomous software-engineering agent — the OSS face of the SWE-agent race.
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 91,730★ · _Coding agents & MCP_  
  Reference MCP servers — MCP is the emerging standard for wiring tools/data into any agent.
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 84,817★ · _Orchestration & agents_  
  Long-horizon research+code SuperAgent — the 'deep research' pattern as a harness.
- **[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)** · 73,570★ · _Coding agents & MCP_  
  Lighter-weight spec-driven development — agree on a change spec with the agent before it writes code.
- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** · 68,212★ · _Memory_  
  Universal memory layer for agents — the most-adopted bet on the unsolved memory problem.
- **[MemPalace/mempalace](https://github.com/MemPalace/mempalace)** · 60,213★ · _Memory_  
  Best-benchmarked open memory system — a strong contender in a still-open race.
- **[Aider-AI/aider](https://github.com/Aider-AI/aider)** · 49,873★ · _Coding agents & MCP_  
  AI pair-programming in the terminal with tight git integration — a beloved daily driver.
- **[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)** · 45,084★ · _Orchestration & agents_  
  Browser-automation CLI for agents — the lighter, scriptable take on web agents.
- **[agno-agi/agno](https://github.com/agno-agi/agno)** · 43,002★ · _Orchestration & agents_  
  Build/run/manage agent platforms — a fast-rising full-stack agent framework.
- **[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)** · 40,460★ · _RAG & retrieval_  
  Graph-augmented RAG that's simple and fast — the practical face of 'RAG beyond chunks'.
- **[VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)** · 39,937★ · _RAG & retrieval_  
  Vectorless, reasoning-based retrieval — a bet that reasoning can replace embeddings.
- **[google/langextract](https://github.com/google/langextract)** · 39,225★ · _Data & ingestion_  
  Structured extraction from unstructured text — turning documents into typed data.
- **[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)** · 38,931★ · _Coding agents & MCP_  
  Playwright as an MCP server — reliable, structured web control for agents.
- **[microsoft/graphrag](https://github.com/microsoft/graphrag)** · 36,512★ · _RAG & retrieval_  
  Graph-based RAG — structure-aware retrieval for global/whole-corpus questions.
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 23,081★ · _Eval & observability_  
  Eval-first LLM/agent observability — measuring agents, not just logging them.
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 12,090★ · _Eval & observability_  
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
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Trending | 60,213 | 7mo | 914 | 1d ago | 7 |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Trending | 45,084 | 9mo | 148 | 1d ago | 7 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Trending | 154,131 | 1.7y | 243 | 1d ago | 5 |
| [github/spec-kit](https://github.com/github/spec-kit) | Trending | 144,677 | 1.2y | 631 | 2d ago | 5 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Trending | 108,646 | 1.5y | 238 | 0d ago | 5 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Trending | 84,817 | 1.5y | 1710 | 0d ago | 5 |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | Trending | 73,570 | 1.2y | 302 | 2d ago | 5 |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Trending | 39,937 | 1.6y | 206 | 3d ago | 5 |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Trending | 38,931 | 1.6y | 42 | 1d ago | 4 |
| [obra/superpowers](https://github.com/obra/superpowers) | Trending | 310,340 | 1.1y | 6 | 3d ago | 2 |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Must-have | 197,537 | 2.5y | 699 | 1d ago | 2 |
| [ollama/ollama](https://github.com/ollama/ollama) | Must-have | 185,540 | 3.4y | 367 | 1d ago | 2 |
| [huggingface/transformers](https://github.com/huggingface/transformers) | Fundamental | 168,404 | 8.0y | 1031 | 0d ago | 2 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Must-have | 148,809 | 4.0y | 600 | 0d ago | 2 |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | Fundamental | 133,039 | 3.6y | 1792 | 0d ago | 2 |

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
| [obra/superpowers](https://github.com/obra/superpowers) | Trending | Coding agents & MCP | Shell | 310,340 (▲5,019) | Mature | 64 | active | 3d ago | 1.1y |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Must-have | Data & ingestion | TypeScript | 197,537 (▲2,058) | Mature | 86 | very active | 1d ago | 2.5y |
| [anthropics/skills](https://github.com/anthropics/skills) | Trending | Coding agents & MCP | Python | 186,105 (▲2,228) | Mature | 50 | active | 4d ago | 1.1y |
| [ollama/ollama](https://github.com/ollama/ollama) | Must-have | Inference & serving | Go | 185,540 (▲711) | Classic | 83 | very active | 1d ago | 3.4y |
| [huggingface/transformers](https://github.com/huggingface/transformers) | Fundamental | Base & training | Python | 168,404 (▲221) | Classic | 100 | very active | 0d ago | 8.0y |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Trending | Coding agents & MCP | TypeScript | 154,131 (▲711) | Hot | 78 | very active | 1d ago | 1.7y |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Must-have | Orchestration & agents | Python | 148,809 (▲324) | Classic | 84 | very active | 0d ago | 4.0y |
| [github/spec-kit](https://github.com/github/spec-kit) | Trending | Coding agents & MCP | Python | 144,677 (▲1,720) | Hot | 89 | very active | 2d ago | 1.2y |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | Fundamental | Inference & serving | C++ | 133,039 (▲639) | Classic | 99 | very active | 0d ago | 3.6y |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | Fundamental | Learning | Jupyter Notebook | 122,712 (▲514) | Classic | 70 | very active | 0d ago | 3.4y |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Trending | Orchestration & agents | Python | 119,728 (▲550) | Mature | 79 | very active | 1d ago | 2.0y |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | Trending | Orchestration & agents | Python | 119,283 (▲4,033) | Mature | 79 | very active | 5d ago | 1.8y |
| [openai/whisper](https://github.com/openai/whisper) | Fundamental | Voice & multimodal | Python | 111,694 (▲403) | Mature | 36 | slowing | 2mo ago | 4.1y |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Trending | Coding agents & MCP | TypeScript | 108,646 (▲248) | Hot | 100 | very active | 0d ago | 1.5y |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | Fundamental | Learning | Jupyter Notebook | 107,629 (▲318) | Classic | 56 | very active | 2d ago | 3.3y |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Trending | Coding agents & MCP | — | 97,152 (▲268) | Mature | 59 | very active | 9d ago | 1.9y |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | Must-have | Inference & serving | Python | 96,036 (▲454) | Classic | 99 | very active | 0d ago | 3.7y |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | Must-have | RAG & retrieval | Go | 93,284 (▲392) | Mature | 99 | very active | 1d ago | 2.9y |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | Trending | Coding agents & MCP | TypeScript | 92,408 (▲524) | Mature | 84 | very active | 0d ago | 2.6y |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Trending | Coding agents & MCP | TypeScript | 91,730 (▲155) | Mature | 80 | very active | 3d ago | 2.0y |
| [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | Must-have | Data & ingestion | Python | 86,692 (▲402) | Mature | 79 | very active | 0d ago | 2.5y |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | Fundamental | Learning | — | 84,831 (▲120) | Declining | 11 | stale | 8mo ago | 3.4y |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Trending | Orchestration & agents | Python | 84,817 (▲378) | Hot | 87 | very active | 0d ago | 1.5y |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | Fundamental | Learning | MDX | 79,729 (▲188) | Declining | 13 | stale | 7mo ago | 3.9y |
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | Must-have | Fine-tuning | Python | 78,905 (▲324) | Mature | 80 | very active | 0d ago | 2.9y |
| [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) | Must-have | Fine-tuning | Python | 75,817 (▲76) | Classic | 75 | very active | 1d ago | 3.4y |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | Trending | Coding agents & MCP | TypeScript | 73,570 (▲552) | Hot | 88 | very active | 2d ago | 1.2y |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Trending | Memory | Python | 68,212 (▲373) | Classic | 83 | very active | 2d ago | 3.4y |
| [labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | Fundamental | Learning | Python | 67,627 (▲27) | Mature | 46 | active | 7d ago | 6.2y |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Must-have | Inference & serving | Python | 62,484 (▲429) | Classic | 99 | very active | 0d ago | 3.3y |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Must-have | Orchestration & agents | Python | 60,369 (▲252) | Classic | 84 | very active | 0d ago | 3.0y |
| [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | Trending | Memory | Python | 60,213 (▲469) | Hot | 76 | very active | 1d ago | 7mo |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | Must-have | RAG & retrieval | Python | 52,767 (▲98) | Classic | 97 | very active | 6d ago | 4.0y |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | Must-have | Inference & serving | Go | 50,108 (▲139) | Classic | 79 | very active | 0d ago | 3.6y |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | Trending | Coding agents & MCP | Python | 49,873 (▲116) | Mature | 23 | slowing | 5mo ago | 3.5y |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | Must-have | Vector store | Go | 46,548 (▲65) | Classic | 99 | very active | 0d ago | 7.1y |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Trending | Orchestration & agents | Rust | 45,084 (▲469) | Hot | 76 | very active | 1d ago | 9mo |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Must-have | Orchestration & agents | Python | 44,260 (▲336) | Classic | 83 | very active | 0d ago | 3.2y |
| [deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed) | Fundamental | Base & training | Python | 43,278 (▲3) | Classic | 91 | very active | 0d ago | 6.8y |
| [agno-agi/agno](https://github.com/agno-agi/agno) | Trending | Orchestration & agents | Python | 43,002 (▲103) | Classic | 87 | very active | 1d ago | 4.5y |
| [facebookresearch/faiss](https://github.com/facebookresearch/faiss) | Fundamental | Vector store | C++ | 41,245 (▲31) | Classic | 89 | very active | 0d ago | 9.7y |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | Trending | RAG & retrieval | Python | 40,460 (▲120) | Mature | 78 | very active | 3d ago | 2.1y |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Trending | RAG & retrieval | Python | 39,937 (▲182) | Hot | 76 | very active | 3d ago | 1.6y |
| [google/langextract](https://github.com/google/langextract) | Trending | Data & ingestion | Python | 39,225 (▲180) | Mature | 68 | very active | 2d ago | 1.3y |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Trending | Coding agents & MCP | TypeScript | 38,931 (▲287) | Hot | 79 | very active | 1d ago | 1.6y |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | Must-have | Orchestration & agents | Python | 38,873 (▲76) | Classic | 78 | very active | 2d ago | 3.8y |
| [sgl-project/sglang](https://github.com/sgl-project/sglang) | Must-have | Inference & serving | Python | 38,337 (▲143) | Mature | 99 | very active | 0d ago | 2.8y |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Must-have | Eval & observability | TypeScript | 36,823 (▲311) | Classic | 94 | very active | 0d ago | 3.5y |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | Trending | RAG & retrieval | Python | 36,512 (▲63) | Mature | 70 | very active | 3d ago | 2.6y |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | Must-have | Vector store | Rust | 35,360 (▲102) | Classic | 83 | very active | 0d ago | 6.4y |
| [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | Fundamental | Base & training | Python | 31,434 (▲1) | Classic | 71 | active | 2d ago | 7.6y |
| [karpathy/llm.c](https://github.com/karpathy/llm.c) | Fundamental | Learning | Cuda | 31,346 (▲127) | Abandoned | 4 | stale | 1.4y ago | 2.6y |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | Fundamental | RAG & retrieval | Jupyter Notebook | 30,167 (▲157) | Mature | 62 | very active | 1d ago | 2.3y |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | Must-have | Orchestration & agents | Python | 30,163 (▲98) | Mature | 60 | active | 3d ago | 1.9y |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | Must-have | Vector store | Rust | 29,616 (▲33) | Classic | 80 | very active | 2d ago | 4.1y |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Trending | Eval & observability | Python | 23,081 (▲149) | Classic | 89 | very active | 0d ago | 3.5y |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Trending | Eval & observability | Python | 12,090 (▲83) | Classic | 84 | very active | 0d ago | 4.0y |

## Graph analysis — how they relate

**Community clustering.** These 57 repos span **24 of the graph's 45 communities** — the AI-engineering stack is genuinely cross-cutting, not one tidy neighborhood.

- **Community 4** (11): `langchain-ai/langchain`, `infiniflow/ragflow`, `dair-ai/Prompt-Engineering-Guide`, `mem0ai/mem0`, `crewAIInc/crewAI`, `MemPalace/mempalace`, `Aider-AI/aider`, `langchain-ai/langgraph`, `agno-agi/agno`, `VectifyAI/PageIndex`
- **Community 35** (6): `ollama/ollama`, `TauricResearch/TradingAgents`, `vllm-project/vllm`, `unslothai/unsloth`, `hiyouga/LlamaFactory`, `sgl-project/sglang`
- **Community 22** (4): `BerriAI/litellm`, `langfuse/langfuse`, `comet-ml/opik`, `Arize-ai/phoenix`
- **Community 14** (3): `ggml-org/llama.cpp`, `mlabonne/llm-course`, `labmlai/annotated_deep_learning_paper_implementations`
- **Community 24** (3): `deepspeedai/DeepSpeed`, `facebookresearch/faiss`, `Lightning-AI/pytorch-lightning`
- **Community 9** (3): `microsoft/generative-ai-for-beginners`, `microsoft/playwright-mcp`, `microsoft/graphrag`
- **Community 30** (3): `firecrawl/firecrawl`, `browser-use/browser-use`, `unclecode/crawl4ai`

**Centrality (PageRank in the full 2,585-repo graph)** — the most 'hub-like' AI-eng repos in your stars (good signal for *foundational*):

- `punkpeye/awesome-mcp-servers` — PageRank 0.0018 (Trending)
- `microsoft/playwright-mcp` — PageRank 0.0016 (Trending)
- `Lightning-AI/pytorch-lightning` — PageRank 0.0014 (Fundamental)
- `microsoft/graphrag` — PageRank 0.0013 (Trending)
- `langchain-ai/langchain` — PageRank 0.0013 (Must-have)
- `langchain-ai/langgraph` — PageRank 0.0012 (Must-have)
- `huggingface/smolagents` — PageRank 0.0011 (Must-have)
- `microsoft/generative-ai-for-beginners` — PageRank 0.0010 (Fundamental)
- `agno-agi/agno` — PageRank 0.0010 (Trending)
- `MemPalace/mempalace` — PageRank 0.0008 (Trending)

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). For *production* picks, prefer mature lifecycle + low single-author share; for *trending* picks, expect churn.

| Repo | Tier | Health | Lifecycle | Activity | Bus factor | Top-author share |
|---|---|---|---|---|---|---|
| huggingface/transformers | Fundamental | 100 | Classic | very active | 8 | 12% |
| google-gemini/gemini-cli | Trending | 100 | Hot | very active | 5 | 14% |
| ggml-org/llama.cpp | Fundamental | 99 | Classic | very active | 9 | 11% |
| vllm-project/vllm | Must-have | 99 | Classic | very active | 26 | 9% |
| sgl-project/sglang | Must-have | 99 | Mature | very active | 7 | 12% |
| BerriAI/litellm | Must-have | 99 | Classic | very active | 7 | 10% |
| milvus-io/milvus | Must-have | 99 | Classic | very active | 7 | 10% |
| infiniflow/ragflow | Must-have | 99 | Mature | very active | 5 | 13% |
| run-llama/llama_index | Must-have | 97 | Classic | very active | 10 | 14% |
| langfuse/langfuse | Must-have | 94 | Classic | very active | 4 | 22% |
| deepspeedai/DeepSpeed | Fundamental | 91 | Classic | very active | 4 | 17% |
| facebookresearch/faiss | Fundamental | 89 | Classic | very active | 3 | 25% |
| github/spec-kit | Trending | 89 | Hot | very active | 3 | 24% |
| comet-ml/opik | Trending | 89 | Classic | very active | 3 | 26% |
| Fission-AI/OpenSpec | Trending | 88 | Hot | very active | 3 | 37% |
| bytedance/deer-flow | Trending | 87 | Hot | very active | 10 | 11% |
| agno-agi/agno | Trending | 87 | Classic | very active | 3 | 29% |
| firecrawl/firecrawl | Must-have | 86 | Mature | very active | 3 | 24% |
| langchain-ai/langchain | Must-have | 84 | Classic | very active | 2 | 47% |
| crewAIInc/crewAI | Must-have | 84 | Classic | very active | 2 | 45% |
| OpenHands/OpenHands | Trending | 84 | Mature | very active | 2 | 35% |
| Arize-ai/phoenix | Trending | 84 | Classic | very active | 2 | 34% |
| langchain-ai/langgraph | Must-have | 83 | Classic | very active | 2 | 43% |
| ollama/ollama | Must-have | 83 | Classic | very active | 2 | 38% |
| qdrant/qdrant | Must-have | 83 | Classic | very active | 2 | 41% |
| mem0ai/mem0 | Trending | 83 | Classic | very active | 2 | 43% |
| chroma-core/chroma | Must-have | 80 | Classic | very active | 2 | 31% |
| unslothai/unsloth | Must-have | 80 | Mature | very active | 1 | 72% |
| modelcontextprotocol/servers | Trending | 80 | Mature | very active | 1 | 98% |
| mudler/LocalAI | Must-have | 79 | Classic | very active | 1 | 75% |
| unclecode/crawl4ai | Must-have | 79 | Mature | very active | 1 | 53% |
| browser-use/browser-use | Trending | 79 | Mature | very active | 1 | 63% |
| microsoft/playwright-mcp | Trending | 79 | Hot | very active | 2 | 40% |
| TauricResearch/TradingAgents | Trending | 79 | Mature | very active | 1 | 97% |
| stanfordnlp/dspy | Must-have | 78 | Classic | very active | 1 | 58% |
| anthropics/claude-code | Trending | 78 | Hot | very active | 1 | 59% |
| HKUDS/LightRAG | Trending | 78 | Mature | very active | 1 | 63% |
| vercel-labs/agent-browser | Trending | 76 | Hot | very active | 1 | 51% |
| MemPalace/mempalace | Trending | 76 | Hot | very active | 1 | 70% |
| VectifyAI/PageIndex | Trending | 76 | Hot | very active | 1 | 50% |
| hiyouga/LlamaFactory | Must-have | 75 | Classic | very active | 4 | 29% |
| Lightning-AI/pytorch-lightning | Fundamental | 71 | Classic | active | 2 | 47% |
| microsoft/generative-ai-for-beginners | Fundamental | 70 | Classic | very active | 2 | 33% |
| microsoft/graphrag | Trending | 70 | Mature | very active | 1 | 60% |
| google/langextract | Trending | 68 | Mature | very active | 1 | 72% |
| obra/superpowers | Trending | 64 | Mature | active | 1 | 100% |
| NirDiamant/RAG_Techniques | Fundamental | 62 | Mature | very active | 1 | 88% |
| huggingface/smolagents | Must-have | 60 | Mature | active | 2 | 43% |
| punkpeye/awesome-mcp-servers | Trending | 59 | Mature | very active | 1 | 99% |
| rasbt/LLMs-from-scratch | Fundamental | 56 | Classic | very active | 1 | 61% |
| anthropics/skills | Trending | 50 | Mature | active | 2 | 47% |
| labmlai/annotated_deep_learning_paper_implementations | Fundamental | 46 | Mature | active | 1 | 67% |
| openai/whisper | Fundamental | 36 | Mature | slowing | 1 | 100% |
| Aider-AI/aider | Trending | 23 | Mature | slowing | 0 | 0% |
| dair-ai/Prompt-Engineering-Guide | Fundamental | 13 | Declining | stale | 0 | 0% |
| mlabonne/llm-course | Fundamental | 11 | Declining | stale | 0 | 0% |
| karpathy/llm.c | Fundamental | 4 | Abandoned | stale | 0 | 0% |

## Adjacent (deliberately not in the core list)

- **Comfy-Org/ComfyUI** (144,428★) — image/diffusion tooling — a different (creative) AI discipline, out of scope here
- **PaddlePaddle/PaddleOCR** (92,056★) — OCR engine — a data-ingestion building block, folded into 'Data & ingestion'
- **n8n-io/n8n** (209,256★) — workflow automation — orchestrates agents but isn't core AI-eng tooling (see agent-orchestration report)
- **microsoft/autogen** (61,660★) — multi-agent framework — slipping in activity; crewAI/langgraph lead the must-have slot now
- **nomic-ai/gpt4all** (77,342★) — local-LLM app — superseded for most by ollama; kept off the must-have list

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`, cross-checked against 2026 AI-engineering landscape reporting. No private calls; fully reproducible.
- **Tiers and the solved/frontier verdicts are opinionated** — a synthesis of dataset signal (stars, lifecycle, commit velocity) and the current state of the field, not a benchmark. Treat 'Trending' as *volatile by definition*.
- **Selection** favors recognizable, broadly-applicable AI-engineering tooling. The coding-agent/harness ecosystem and voice stack are summarized here but detailed in the Claude-Code-setups and voice-agents reports respectively.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.

<sub>Repos covered: 57 · Snapshot: 2026-11-01T12:41:55.392Z</sub>
