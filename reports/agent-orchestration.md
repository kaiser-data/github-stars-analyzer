# AI Agent Orchestration — Landscape Report

> Derived from **kaiser-data**'s 1,172 starred repos (snapshot `2026-06-02T22:59:34.535Z`), cross-referenced with the repo-similarity graph (1,172 nodes / 3,814 edges, 27 communities).
>
> Generated 2026-06-02 by `scripts/reports/agent_orchestration.py` (regenerate any time — no API cost).

> **Orchestration** = coordinating multiple agents / tools / steps toward a goal: routing, planning, parallelism, hand-offs, state and recovery. The tools below differ mostly in **how you express that coordination** — in code, on a visual canvas, across coding agents, or as durable production infra.

## Executive summary

- **38 agent-orchestration tools** in your stars (**1,459,773★**), organized by *how you express coordination*:
  - **Code-first agent frameworks** (16): `MetaGPT`, `autogen`, `crewAI`, `agno`, `dspy`, `langgraph`, `semantic-kernel`, `smolagents`, `openai-agents-python`, `agentscope`, `adk-python`, `camel`, `agent-framework`, `voltagent`, `beeai-framework`, `AutoAgents`
  - **Visual / low-code platforms** (5): `n8n`, `langflow`, `dify`, `Flowise`, `sim`
  - **Coding-agent orchestration** (9): `deer-flow`, `oh-my-openagent`, `ruflo`, `agents`, `oh-my-claudecode`, `eigent`, `agent-orchestrator`, `paseo`, `coding-agent-template`
  - **Agent OS / long-horizon harness** (1): `eliza`
  - **Durable / production infra** (2): `flyte`, `agent-kit`
  - **Vertical / domain systems** (2): `TradingAgents`, `gpt-researcher`
  - **Protocols & meta-frameworks** (3): `ROMA`, `tinyagi`, `agent-workflow-protocol`
- **The split that matters:** *code-first frameworks* (langgraph, openai-agents, semantic-kernel) give you fine control in a programming language; *visual platforms* (n8n, dify, Flowise) trade control for speed and non-engineer access; *coding-agent orchestration* (ruflo, agent-orchestrator) is a newer niche that runs **swarms of coding agents** in parallel.
- **Big-tech has entered:** Microsoft (agent-framework, semantic-kernel), Google (adk-python), OpenAI (openai-agents-python), AWS (strands-agents) all ship first-party frameworks — a strong maturity signal.
- **Highest-health picks:** `n8n`/`dify` (100), `strands-agents` (96), `microsoft/agent-framework` & `semantic-kernel` & `Flowise` (92).

## Pick by how you want to express coordination

| You want… | Use this approach | Top picks |
|---|---|---|
| Fine-grained control, in code | Code-first framework | `langgraph`, `openai-agents-python` |
| Fast builds / non-engineers | Visual / low-code | `n8n`, `dify`, `Flowise` |
| Parallel **coding** agents | Coding-agent orchestration | `ruflo`, `ComposioHQ/agent-orchestrator` |
| Always-on autonomous agents | Agent OS / harness | `elizaOS/eliza`, `deer-flow` |
| Durable, fault-tolerant prod | Production infra | `flyte`, `inngest/agent-kit` |
| A standard, not a library | Protocol / meta | `agent-workflow-protocol` |

## Comparison by approach

### Code-first agent frameworks

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 68,480 | Python | 29 | slowing | Mature | 0 |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 58,646 | Python | 58 | active | Mature | 1 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 52,682 | Python | 80 | very active | Mature | 1 |
| [agno-agi/agno](https://github.com/agno-agi/agno) | 40,470 | Python | 98 | very active | Classic | 5 |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | 34,792 | Python | 83 | very active | Classic | 2 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 33,674 | Python | 83 | very active | Mature | 2 |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | 28,032 | C# | 87 | very active | Classic | 3 |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | 27,666 | Python | 67 | active | Mature | 1 |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 26,856 | Python | 89 | very active | Hot | 3 |
| [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | 26,029 | Python | 80 | very active | Mature | 2 |
| [google/adk-python](https://github.com/google/adk-python) | 19,962 | Python | 98 | very active | Hot | 5 |
| [camel-ai/camel](https://github.com/camel-ai/camel) | 17,108 | Python | 82 | very active | Classic | 2 |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | 10,971 | Python | 98 | very active | Hot | 6 |
| [VoltAgent/voltagent](https://github.com/VoltAgent/voltagent) | 9,318 | TypeScript | 81 | very active | Hot | 2 |
| [i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework) | 3,278 | Python | 72 | very active | Mature | 1 |
| [liquidos-ai/AutoAgents](https://github.com/liquidos-ai/AutoAgents) | 664 | Rust | 68 | very active | Hot | 1 |

### Visual / low-code platforms

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 190,785 | TypeScript | 100 | very active | Classic | 9 |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 149,111 | Python | 84 | very active | Classic | 2 |
| [langgenius/dify](https://github.com/langgenius/dify) | 143,556 | TypeScript | 100 | very active | Classic | 6 |
| [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | 53,281 | TypeScript | 92 | very active | Classic | 4 |
| [simstudioai/sim](https://github.com/simstudioai/sim) | 28,673 | TypeScript | 78 | very active | Hot | 1 |

### Coding-agent orchestration

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 70,299 | Python | 81 | very active | Hot | 5 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 60,730 | TypeScript | 78 | very active | Hot | 1 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 57,513 | TypeScript | 77 | very active | Hot | 1 |
| [wshobson/agents](https://github.com/wshobson/agents) | 36,276 | Python | 70 | very active | Hot | 2 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | 35,609 | TypeScript | 80 | very active | Hot | 1 |
| [eigent-ai/eigent](https://github.com/eigent-ai/eigent) | 14,191 | TypeScript | 80 | very active | Hot | 2 |
| [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | 7,379 | TypeScript | 79 | very active | Hot | 2 |
| [getpaseo/paseo](https://github.com/getpaseo/paseo) | 7,174 | TypeScript | 73 | very active | Hot | 1 |
| [vercel-labs/coding-agent-template](https://github.com/vercel-labs/coding-agent-template) | 1,724 | TypeScript | 30 | active | Declining | 0 |

### Agent OS / long-horizon harness

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [elizaOS/eliza](https://github.com/elizaOS/eliza) | 18,501 | TypeScript | 80 | very active | Hot | 1 |

### Durable / production infra

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [flyteorg/flyte](https://github.com/flyteorg/flyte) | 7,060 | Go | 87 | very active | Classic | 3 |
| [inngest/agent-kit](https://github.com/inngest/agent-kit) | 880 | TypeScript | 57 | active | Declining | 1 |

### Vertical / domain systems

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 82,281 | Python | 72 | very active | Hot | 1 |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | 27,463 | Python | 75 | very active | Classic | 1 |

### Protocols & meta-frameworks

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [sentient-agi/ROMA](https://github.com/sentient-agi/ROMA) | 5,071 | Python | 32 | slowing | Declining | 0 |
| [TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi) | 3,571 | TypeScript | 69 | slowing | Rising | 1 |
| [veegee82/agent-workflow-protocol](https://github.com/veegee82/agent-workflow-protocol) | 17 | Python | 58 | very active | Rising | 1 |

## Details

### Code-first agent frameworks

_SDKs you write agents in — maximum control over routing, state and hand-offs; the engineer's default._

- **[FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT)** · 68,480★ · Python · Mature · health 29  
  Multi-agent 'software company' — assigns SOPs/roles (PM, architect, engineer).  
  <sub>topics: agent, gpt, llm, metagpt, multi-agent</sub>
- **[microsoft/autogen](https://github.com/microsoft/autogen)** · 58,646★ · Python · Mature · health 58  
  Microsoft's conversational multi-agent framework; agents talk to solve tasks.  
  <sub>topics: chatgpt, llm-agent, llm-framework, agentic, agentic-agi, agents</sub>
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** · 52,682★ · Python · Mature · health 80  
  Role-based 'crew' multi-agent framework — agents with roles, goals & tools collaborate.  
  <sub>topics: agents, ai, ai-agents, llms, aiagentframework</sub>
- **[agno-agi/agno](https://github.com/agno-agi/agno)** · 40,470★ · Python · Classic · health 98  
  Fast multimodal agent framework (ex-phidata) with memory/tools/teams.  
  <sub>topics: developer-tools, python, agents, ai, ai-agents</sub>
- **[stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)** · 34,792★ · Python · Classic · health 83  
  Programmatic prompt/pipeline optimization — compile agent behavior instead of hand-prompting.  
  <sub>topics: —</sub>
- **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** · 33,674★ · Python · Mature · health 83  
  Graph-based agent runtime — explicit nodes/edges/state; the de-facto control-flow framework.  
  <sub>topics: agents, ai, ai-agents, chatgpt, deepagents, enterprise</sub>
- **[microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)** · 28,032★ · C# · Classic · health 87  
  Microsoft's enterprise SDK (C#/Python) for plugging LLMs + planning into apps.  
  <sub>topics: ai, artificial-intelligence, llm, openai, sdk</sub>
- **[huggingface/smolagents](https://github.com/huggingface/smolagents)** · 27,666★ · Python · Mature · health 67  
  Minimalist code-agent framework — agents that write & run Python to act.  
  <sub>topics: —</sub>
- **[openai/openai-agents-python](https://github.com/openai/openai-agents-python)** · 26,856★ · Python · Hot · health 89  
  Lightweight, powerful framework for multi-agent workflows; handoffs + guardrails + tracing.  
  <sub>topics: agents, ai, framework, llm, python, openai</sub>
- **[agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)** · 26,029★ · Python · Mature · health 80  
  Build agents you can see/understand/trust; strong observability + multi-agent.  
  <sub>topics: agent, chatbot, large-language-models, llm, llm-agent, multi-agent</sub>
- **[google/adk-python](https://github.com/google/adk-python)** · 19,962★ · Python · Hot · health 98  
  Google's code-first Agent Development Kit — build, evaluate & deploy agents.  
  <sub>topics: agent, agents, agents-sdk, ai, ai-agents, multi-agent-systems</sub>
- **[camel-ai/camel](https://github.com/camel-ai/camel)** · 17,108★ · Python · Classic · health 82  
  Large multi-agent 'society' framework for studying agent cooperation at scale.  
  <sub>topics: ai-societies, artificial-intelligence, deep-learning, large-language-models, multi-agent-systems, natural-language-processing</sub>
- **[microsoft/agent-framework](https://github.com/microsoft/agent-framework)** · 10,971★ · Python · Hot · health 98  
  Microsoft's framework to build, orchestrate & deploy multi-agent workflows (health 92).  
  <sub>topics: agent-framework, agentic-ai, agents, ai, multi-agent, orchestration</sub>
- **[VoltAgent/voltagent](https://github.com/VoltAgent/voltagent)** · 9,318★ · TypeScript · Hot · health 81  
  TypeScript agent-engineering platform + open-source framework.  
  <sub>topics: agents, ai, chatbots, llm, mcp, nodejs</sub>
- **[i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework)** · 3,278★ · Python · Mature · health 72  
  Production-ready agents in both Python and TypeScript.  
  <sub>topics: agents, ai, framework, ai-agent, llm, multiagent</sub>
- **[liquidos-ai/AutoAgents](https://github.com/liquidos-ai/AutoAgents)** · 664★ · Rust · Hot · health 68  
  Rust multi-agent framework to build, deploy & coordinate agents.  
  <sub>topics: agents, ai, ai-agents, ai-agents-framework, llm</sub>

### Visual / low-code platforms

_Drag-and-drop canvases — fastest to a working flow, accessible to non-engineers, less granular control._

- **[n8n-io/n8n](https://github.com/n8n-io/n8n)** · 190,785★ · TypeScript · Classic · health 100  
  Fair-code workflow automation with native AI nodes — the giant (189k★, health 100).  
  <sub>topics: automation, ipaas, n8n, workflow, typescript, self-hosted</sub>
- **[langflow-ai/langflow](https://github.com/langflow-ai/langflow)** · 149,111★ · Python · Classic · health 84  
  Popular drag-and-drop builder for agents & flows; visual graph of components.  
  <sub>topics: react-flow, chatgpt, large-language-models, generative-ai, agents, multiagent</sub>
- **[langgenius/dify](https://github.com/langgenius/dify)** · 143,556★ · TypeScript · Classic · health 100  
  Production-ready platform for agentic workflow development (health 100).  
  <sub>topics: ai, gpt, llm, openai, python, rag</sub>
- **[FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)** · 53,281★ · TypeScript · Classic · health 92  
  Build AI agents visually; popular drag-and-drop builder.  
  <sub>topics: artificial-intelligence, chatgpt, large-language-models, low-code, no-code, javascript</sub>
- **[simstudioai/sim](https://github.com/simstudioai/sim)** · 28,673★ · TypeScript · Hot · health 78  
  Build, deploy & orchestrate agents — 'central intelligence layer for your AI workforce'.  
  <sub>topics: agentic-workflow, agents, ai, nextjs, typescript, agent-workflow</sub>

### Coding-agent orchestration

_Coordinate *swarms of coding agents* (Claude Code, Codex, Cursor…) on a codebase — plan, spawn, run in parallel, handle CI._

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 70,299★ · Python · Hot · health 81  
  Long-horizon SuperAgent harness that researches, codes & creates with sandboxes (bf6).  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 60,730★ · TypeScript · Hot · health 78  
  'omo' — agent harness (formerly oh-my-opencode) for coding workflows.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 57,513★ · TypeScript · Hot · health 77  
  Agent-orchestration platform for Claude — multi-agent swarms coordinating autonomous coding.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-rag, agentic-workflow</sub>
- **[wshobson/agents](https://github.com/wshobson/agents)** · 36,276★ · Python · Hot · health 70  
  Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor, OpenCode, Gemini).  
  <sub>topics: agents, anthropic, automation, workflows, orchestration, agent-skills</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 35,609★ · TypeScript · Hot · health 80  
  Teams-first multi-agent orchestration for Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode</sub>
- **[eigent-ai/eigent](https://github.com/eigent-ai/eigent)** · 14,191★ · TypeScript · Hot · health 80  
  Open-source cowork desktop — local/free multi-agent productivity workspace.  
  <sub>topics: agent-framework, agent-skills, agentic-ai, agentic-workflow, claude-cowork, claude-cowork-alternative</sub>
- **[ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator)** · 7,379★ · TypeScript · Hot · health 79  
  Orchestrates parallel coding agents — plans tasks, spawns agents, handles CI autonomously.  
  <sub>topics: claude-code, codex-cli, orchestration, orchestrator, skills, agent-fleet</sub>
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 7,174★ · TypeScript · Hot · health 73  
  Run & coordinate coding agents from phone, desktop and CLI.  
  <sub>topics: agents, claude-code, codex, opencode, ade, copilot</sub>
- **[vercel-labs/coding-agent-template](https://github.com/vercel-labs/coding-agent-template)** · 1,724★ · TypeScript · Declining · health 30  
  Multi-agent coding platform on Vercel Sandbox + AI Gateway; declining, verify first.  
  <sub>topics: —</sub>

### Agent OS / long-horizon harness

_Runtimes for always-on, long-running autonomous agents._

- **[elizaOS/eliza](https://github.com/elizaOS/eliza)** · 18,501★ · TypeScript · Hot · health 80  
  Open-source 'agentic operating system' — long-running autonomous agents.  
  <sub>topics: agent, agentic, ai, autonomous, chatbot, crypto</sub>

### Durable / production infra

_Fault-tolerant execution — retries, checkpointing, deterministic routing for production._

- **[flyteorg/flyte](https://github.com/flyteorg/flyte)** · 7,060★ · Go · Classic · health 87  
  Dynamic, resilient orchestration (Go/K8s) — coordinate data, models & compute durably.  
  <sub>topics: flyte, machine-learning, golang, scale, workflow, data-science</sub>
- **[inngest/agent-kit](https://github.com/inngest/agent-kit)** · 880★ · TypeScript · Declining · health 57  
  Build multi-agent networks in TS with deterministic routing + durable execution via MCP.  
  <sub>topics: agent, ai, ai-agent-framework, ai-agents, llm</sub>

### Vertical / domain systems

_Reference multi-agent architectures for a specific domain._

- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 82,281★ · Python · Hot · health 72  
  Multi-agent LLM framework for financial trading — a vertical reference architecture (79k★).  
  <sub>topics: agent, finance, llm, multiagent, trading</sub>
- **[assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)** · 27,463★ · Python · Classic · health 75  
  Autonomous research agent that plans, searches & writes cited reports.  
  <sub>topics: ai, python, agent, automation, research, search</sub>

### Protocols & meta-frameworks

_Standards and meta-layers above any single framework._

- **[sentient-agi/ROMA](https://github.com/sentient-agi/ROMA)** · 5,071★ · Python · Declining · health 32  
  Recursive meta-agent framework to build multi-agent systems; declining/low health.  
  <sub>topics: —</sub>
- **[TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi)** · 3,571★ · TypeScript · Rising · health 69  
  Agent-teams orchestrator aimed at one-person companies.  
  <sub>topics: —</sub>
- **[veegee82/agent-workflow-protocol](https://github.com/veegee82/agent-workflow-protocol)** · 17★ · Python · Rising · health 58  
  Open standard for multi-agent workflows — scripted pipelines to self-organizing teams.  
  <sub>topics: agentic, agentic-ai, agentic-ai-development, agentic-engineering, agentic-framework, agentic-workflow</sub>

## Graph analysis — how they relate

**Community clustering.** These 38 tools span **13 of the graph's 27 communities**.

- **Community 6** (9): `google/adk-python`, `agentscope-ai/agentscope`, `VoltAgent/voltagent`, `liquidos-ai/AutoAgents`, `crewAIInc/crewAI`, `agno-agi/agno`, `n8n-io/n8n`, `inngest/agent-kit`, `veegee82/agent-workflow-protocol`
- **Community 8** (8): `langchain-ai/langgraph`, `i-am-bee/beeai-framework`, `langgenius/dify`, `FlowiseAI/Flowise`, `simstudioai/sim`, `langflow-ai/langflow`, `bytedance/deer-flow`, `elizaOS/eliza`
- **Community 11** (4): `code-yeongyu/oh-my-openagent`, `wshobson/agents`, `ComposioHQ/agent-orchestrator`, `getpaseo/paseo`
- **Community 12** (3): `microsoft/semantic-kernel`, `microsoft/agent-framework`, `microsoft/autogen`
- **Community 9** (3): `FoundationAgents/MetaGPT`, `vercel-labs/coding-agent-template`, `TauricResearch/TradingAgents`
- **Community 16** (3): `camel-ai/camel`, `eigent-ai/eigent`, `flyteorg/flyte`
- **Community 5** (2): `assafelovic/gpt-researcher`, `Yeachan-Heo/oh-my-claudecode`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' orchestration tools in your ecosystem:

- `langchain-ai/langgraph` — PageRank 0.0030
- `agno-agi/agno` — PageRank 0.0029
- `huggingface/smolagents` — PageRank 0.0020
- `microsoft/semantic-kernel` — PageRank 0.0019
- `openai/openai-agents-python` — PageRank 0.0019
- `liquidos-ai/AutoAgents` — PageRank 0.0019
- `inngest/agent-kit` — PageRank 0.0019
- `code-yeongyu/oh-my-openagent` — PageRank 0.0016
- `langgenius/dify` — PageRank 0.0015
- `crewAIInc/crewAI` — PageRank 0.0014

**Direct links between orchestration tools** (top similarity edges where both endpoints are in this report):

- `microsoft/agent-framework` ⇄ `microsoft/semantic-kernel` (w=1.167) — topics: ai, sdk; authors: westey-m, alliscode, eavanvalkenburg
- `microsoft/autogen` ⇄ `microsoft/agent-framework` (w=0.661) — topics: agents, ai
- `i-am-bee/beeai-framework` ⇄ `openai/openai-agents-python` (w=0.505) — topics: agents, ai, framework, llm
- `agno-agi/agno` ⇄ `crewAIInc/crewAI` (w=0.479) — topics: agents, ai, ai-agents
- `FlowiseAI/Flowise` ⇄ `simstudioai/sim` (w=0.450) — topics: artificial-intelligence, low-code, no-code, react
- `langchain-ai/langgraph` ⇄ `i-am-bee/beeai-framework` (w=0.436) — topics: agents, ai, framework, llm; authors: dependabot[bot]
- `agno-agi/agno` ⇄ `liquidos-ai/AutoAgents` (w=0.429) — topics: agents, ai, ai-agents
- `crewAIInc/crewAI` ⇄ `liquidos-ai/AutoAgents` (w=0.429) — topics: agents, ai, ai-agents
- `liquidos-ai/AutoAgents` ⇄ `inngest/agent-kit` (w=0.429) — topics: ai, ai-agents, llm
- `camel-ai/camel` ⇄ `eigent-ai/eigent` (w=0.384) — topics: multi-agent-systems; authors: Wendong-Fan, fengju0213, Zephyroam
- `crewAIInc/crewAI` ⇄ `google/adk-python` (w=0.362) — topics: agents, ai, ai-agents, llms
- `simstudioai/sim` ⇄ `langgenius/dify` (w=0.360) — topics: agentic-workflow, ai, nextjs, gemini
- `FoundationAgents/MetaGPT` ⇄ `agentscope-ai/agentscope` (w=0.323) — topics: agent, llm, multi-agent
- `FoundationAgents/MetaGPT` ⇄ `TauricResearch/TradingAgents` (w=0.300) — topics: agent, llm
- `langflow-ai/langflow` ⇄ `langchain-ai/langgraph` (w=0.250) — topics: chatgpt, generative-ai, agents, multiagent
- …and 7 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Orchestration is load-bearing — weigh this heavily before standardizing on one.

| Tool | Approach | Health | Lifecycle | Activity | Bus factor |
|---|---|---|---|---|---|
| n8n-io/n8n | Visual / low-code platforms | 100 | Classic | very active | 9 |
| langgenius/dify | Visual / low-code platforms | 100 | Classic | very active | 6 |
| google/adk-python | Code-first agent frameworks | 98 | Hot | very active | 5 |
| microsoft/agent-framework | Code-first agent frameworks | 98 | Hot | very active | 6 |
| agno-agi/agno | Code-first agent frameworks | 98 | Classic | very active | 5 |
| FlowiseAI/Flowise | Visual / low-code platforms | 92 | Classic | very active | 4 |
| openai/openai-agents-python | Code-first agent frameworks | 89 | Hot | very active | 3 |
| microsoft/semantic-kernel | Code-first agent frameworks | 87 | Classic | very active | 3 |
| flyteorg/flyte | Durable / production infra | 87 | Classic | very active | 3 |
| langflow-ai/langflow | Visual / low-code platforms | 84 | Classic | very active | 2 |
| langchain-ai/langgraph | Code-first agent frameworks | 83 | Mature | very active | 2 |
| stanfordnlp/dspy | Code-first agent frameworks | 83 | Classic | very active | 2 |
| camel-ai/camel | Code-first agent frameworks | 82 | Classic | very active | 2 |
| VoltAgent/voltagent | Code-first agent frameworks | 81 | Hot | very active | 2 |
| bytedance/deer-flow | Coding-agent orchestration | 81 | Hot | very active | 5 |
| agentscope-ai/agentscope | Code-first agent frameworks | 80 | Mature | very active | 2 |
| crewAIInc/crewAI | Code-first agent frameworks | 80 | Mature | very active | 1 |
| Yeachan-Heo/oh-my-claudecode | Coding-agent orchestration | 80 | Hot | very active | 1 |
| eigent-ai/eigent | Coding-agent orchestration | 80 | Hot | very active | 2 |
| elizaOS/eliza | Agent OS / long-horizon harness | 80 | Hot | very active | 1 |
| ComposioHQ/agent-orchestrator | Coding-agent orchestration | 79 | Hot | very active | 2 |
| simstudioai/sim | Visual / low-code platforms | 78 | Hot | very active | 1 |
| code-yeongyu/oh-my-openagent | Coding-agent orchestration | 78 | Hot | very active | 1 |
| ruvnet/ruflo | Coding-agent orchestration | 77 | Hot | very active | 1 |
| assafelovic/gpt-researcher | Vertical / domain systems | 75 | Classic | very active | 1 |
| getpaseo/paseo | Coding-agent orchestration | 73 | Hot | very active | 1 |
| i-am-bee/beeai-framework | Code-first agent frameworks | 72 | Mature | very active | 1 |
| TauricResearch/TradingAgents | Vertical / domain systems | 72 | Hot | very active | 1 |
| wshobson/agents | Coding-agent orchestration | 70 | Hot | very active | 2 |
| TinyAGI/tinyagi | Protocols & meta-frameworks | 69 | Rising | slowing | 1 |
| liquidos-ai/AutoAgents | Code-first agent frameworks | 68 | Hot | very active | 1 |
| huggingface/smolagents | Code-first agent frameworks | 67 | Mature | active | 1 |
| microsoft/autogen | Code-first agent frameworks | 58 | Mature | active | 1 |
| veegee82/agent-workflow-protocol | Protocols & meta-frameworks | 58 | Rising | very active | 1 |
| inngest/agent-kit | Durable / production infra | 57 | Declining | active | 1 |
| sentient-agi/ROMA | Protocols & meta-frameworks | 32 | Declining | slowing | 0 |
| vercel-labs/coding-agent-template | Coding-agent orchestration | 30 | Declining | active | 0 |
| FoundationAgents/MetaGPT | Code-first agent frameworks | 29 | Mature | slowing | 0 |

⚠️ **Adopt with caution** (low health and/or declining): `FoundationAgents/MetaGPT`, `vercel-labs/coding-agent-template`, `sentient-agi/ROMA`, `inngest/agent-kit`.

## Coverage

Your stars now cover the canonical orchestration frameworks (crewAI, AutoGen, LangGraph, langflow, semantic-kernel, ADK, agentscope, …) — no major gaps left in this category.

## Methodology & caveats

- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: scan for orchestration / multi-agent / swarm / workflow / agent-framework signals, then manual curation by approach. RAG frameworks, eval/observability platforms, and single-purpose agents were routed to their own reports or excluded; only tools whose *primary* job is coordinating agents/steps appear here.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub. Re-run after a fresh `classified.json` to refresh.

<sub>Tools covered: 38 across 7 approaches · Snapshot: 2026-06-02T22:59:34.535Z</sub>
