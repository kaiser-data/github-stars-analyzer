# Recommended to Star — Gaps in Your Collection

> **What this is:** popular AI/LLM frameworks that are **not** in your 1,071 starred repos
> (snapshot `2026-05-24`), cross-checked against the dataset so each is verified-absent.
>
> ⚠️ **Different from the other reports.** Every other report is derived *purely* from your
> stars. This one leans on external knowledge (training data, cutoff early 2026) to suggest
> what's *missing* — so a few entries may have been renamed/merged since the snapshot. Three
> apparent gaps were already caught as org-renames and excluded: `ragas` → `vibrantlabsai/ragas`,
> `fastmcp` → `prefecthq/fastmcp`, `goose` → `aaif-goose/goose`.

## 🔴 Tier 1 — grab these first (8)

The highest-value gaps given what you already collect.

| Repo | Category | Why |
|---|---|---|
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | Inference / serving | Foundational local LLM inference engine — the layer under Ollama/LM Studio. You have vLLM/Ollama/sglang but not this. |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | RAG | Reference GraphRAG implementation; complements your LightRAG/FalkorDB. |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | Coding agents | One of the most-used terminal coding agents. |
| [cline/cline](https://github.com/cline/cline) | Coding agents | Dominant agentic VS Code extension. |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | Vector DB | Largest-scale OSS vector database; you have qdrant/weaviate/chroma but not Milvus. |
| [letta-ai/letta](https://github.com/letta-ai/letta) | Memory | Ex-MemGPT — coined "agent memory"; conspicuous gap next to mem0/cognee. |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | Agent frameworks | Programmatic prompt optimization — a paradigm none of your stars cover. |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | LLM evaluation | Leading prompt/eval + red-team CLI. |

## 🟠 Tier 2 — strong additions by category (25)

### Agent frameworks / orchestration
_(you already have: langgraph, openai-agents, adk-python, semantic-kernel, agentscope, pydantic-ai)_
- [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) — role-based multi-agent crews; huge mindshare.
- [microsoft/autogen](https://github.com/microsoft/autogen) — conversational multi-agent framework.
- [langflow-ai/langflow](https://github.com/langflow-ai/langflow) — visual flow builder; complements n8n/dify/Flowise.
- [huggingface/smolagents](https://github.com/huggingface/smolagents) — minimalist code-agent framework.
- [agno-agi/agno](https://github.com/agno-agi/agno) — fast multimodal agent framework (ex-phidata).
- [geekan/MetaGPT](https://github.com/geekan/MetaGPT) — multi-agent software-company simulation.
- [camel-ai/camel](https://github.com/camel-ai/camel) — large multi-agent society framework.
- [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) — autonomous research agent.

### LLM evaluation
_(you already have: deepeval, langfuse, opik, openllmetry — but the offline-benchmark side is empty)_
- [openai/evals](https://github.com/openai/evals) — OpenAI eval registry/framework.
- [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — de-facto academic benchmark harness.
- [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) — OSS LLM tracing + eval.
- [huggingface/lighteval](https://github.com/huggingface/lighteval) — lightweight eval suite.
- [truera/trulens](https://github.com/truera/trulens) — feedback-function evaluation.

### RAG / vector DB
_(you already have: ragflow, llama_index, LightRAG, qdrant, weaviate, chroma, pgvector, faiss)_
- [lancedb/lancedb](https://github.com/lancedb/lancedb) — embedded, serverless vector DB.
- [neuml/txtai](https://github.com/neuml/txtai) — all-in-one embeddings DB + RAG.
- [marqo-ai/marqo](https://github.com/marqo-ai/marqo) — end-to-end vector search incl. inference.

### MCP
_(you already have: fastmcp, github-mcp-server, playwright-mcp, mcp python-sdk, + many servers)_
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — official reference-servers monorepo.
- [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) — official TS SDK.
- [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) — official MCP debugging tool.

### Inference / serving
_(you already have: vLLM, Ollama, sglang, transformers, vercel/ai)_
- [huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference) — HF production inference server.
- [guidance-ai/guidance](https://github.com/guidance-ai/guidance) — constrained/structured generation; you have nothing like it.
- [InternLM/lmdeploy](https://github.com/InternLM/lmdeploy) — high-perf inference & serving toolkit.

### Coding agents
_(you already have: OpenHands, Continue, goose)_
- [princeton-nlp/SWE-agent](https://github.com/princeton-nlp/SWE-agent) — resolves real GitHub issues (SWE-bench).
- [sourcegraph/cody](https://github.com/sourcegraph/cody) — context-aware coding assistant.

### Observability
_(you already have: langfuse, opik, openllmetry, Portkey gateway, litellm)_
- [helicone/helicone](https://github.com/helicone/helicone) — OSS LLM observability/gateway.

## Quick-star list (copy/paste)

```
ggml-org/llama.cpp
microsoft/graphrag
Aider-AI/aider
cline/cline
milvus-io/milvus
letta-ai/letta
stanfordnlp/dspy
promptfoo/promptfoo
crewAIInc/crewAI
microsoft/autogen
langflow-ai/langflow
huggingface/smolagents
agno-agi/agno
geekan/MetaGPT
camel-ai/camel
assafelovic/gpt-researcher
openai/evals
EleutherAI/lm-evaluation-harness
Arize-ai/phoenix
huggingface/lighteval
truera/trulens
lancedb/lancedb
neuml/txtai
marqo-ai/marqo
modelcontextprotocol/servers
modelcontextprotocol/typescript-sdk
modelcontextprotocol/inspector
huggingface/text-generation-inference
guidance-ai/guidance
InternLM/lmdeploy
princeton-nlp/SWE-agent
sourcegraph/cody
helicone/helicone
```

## Deliberately excluded

- **Already yours under a different org:** `ragas` (`vibrantlabsai/ragas`), `fastmcp` (`prefecthq/fastmcp`), `goose` (`aaif-goose/goose`), OpenHands, transformers, sglang, BitNet, Continue, mcp python-sdk.
- **Historically important but largely superseded:** `Significant-Gravitas/AutoGPT`, `yoheinakajima/babyagi`, `TransformerOptimus/SuperAGI`, `OpenBMB/ChatDev`.

<sub>33 verified-absent recommendations · checked against snapshot 2026-05-24 · knowledge cutoff early 2026.</sub>
