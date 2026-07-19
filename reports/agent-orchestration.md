# AI Agent Orchestration — Landscape Report

> Derived from **kaiser-data**'s 1,341 starred repos (snapshot `2026-07-19T22:39:07.967Z`), cross-referenced with the repo-similarity graph (1,341 nodes / 4,341 edges, 28 communities).
>
> Generated 2026-07-19 by `scripts/reports/agent_orchestration.py` (regenerate any time — no API cost).

![Top tools by stars](assets/agent-orchestration-top-tools.svg)

![Tools per category](assets/agent-orchestration-categories.svg)


> **Orchestration** = coordinating multiple agents / tools / steps toward a goal: routing, planning, parallelism, hand-offs, state and recovery. The tools below differ mostly in **how you express that coordination** — in code, on a visual canvas, across coding agents, or as durable production infra.

## Executive summary

- **39 agent-orchestration tools** in your stars (**1,544,472★**), organized by *how you express coordination*:
  - **Code-first agent frameworks** (17): `MetaGPT`, `autogen`, `crewAI`, `agno`, `langgraph`, `dspy`, `smolagents`, `semantic-kernel`, `openai-agents-python`, `agentscope`, `adk-python`, `camel`, `agent-framework`, `voltagent`, `harness-sdk`, `beeai-framework`, `AutoAgents`
  - **Visual / low-code platforms** (5): `n8n`, `langflow`, `dify`, `Flowise`, `sim`
  - **Coding-agent orchestration** (9): `deer-flow`, `oh-my-openagent`, `ruflo`, `agents`, `oh-my-claudecode`, `eigent`, `paseo`, `agent-orchestrator`, `coding-agent-template`
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
| Parallel **coding** agents | Coding-agent orchestration | `ruflo`, `AgentWrapper/agent-orchestrator` |
| Always-on autonomous agents | Agent OS / harness | `elizaOS/eliza`, `deer-flow` |
| Durable, fault-tolerant prod | Production infra | `flyte`, `inngest/agent-kit` |
| A standard, not a library | Protocol / meta | `agent-workflow-protocol` |

## Comparison by approach

### Code-first agent frameworks

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 69,432 (▲99) | Python | 25 | slowing | Mature | 0 |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 59,817 (▲124) | Python | 40 | slowing | Mature | 0 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 55,788 (▲371) | Python | 85 | very active | Mature | 2 |
| [agno-agi/agno](https://github.com/agno-agi/agno) | 41,291 (▲170) | Python | 93 | very active | Classic | 4 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 37,615 (▲468) | Python | 77 | very active | Mature | 1 |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | 36,229 (▲144) | Python | 82 | very active | Classic | 2 |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | 28,436 (▲121) | Python | 66 | active | Mature | 1 |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | 28,331 (▲28) | C# | 82 | very active | Classic | 2 |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 28,019 (▲153) | Python | 80 | very active | Hot | 1 |
| [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | 28,012 (▲217) | Python | 87 | very active | Mature | 3 |
| [google/adk-python](https://github.com/google/adk-python) | 20,730 (▲150) | Python | 88 | very active | Hot | 3 |
| [camel-ai/camel](https://github.com/camel-ai/camel) | 17,424 (▲52) | Python | 86 | very active | Classic | 3 |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | 12,226 (▲144) | Python | 93 | very active | Hot | 4 |
| [VoltAgent/voltagent](https://github.com/VoltAgent/voltagent) | 10,096 (▲64) | TypeScript | 79 | very active | Hot | 2 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | 6,641 (▲96) | Python | 91 | very active | Hot | 4 |
| [i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework) | 3,328 (▲13) | Python | 85 | very active | Hot | 3 |
| [liquidos-ai/AutoAgents](https://github.com/liquidos-ai/AutoAgents) | 713 (▲2) | Rust | 69 | very active | Hot | 1 |

### Visual / low-code platforms

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 197,066 (▲833) | TypeScript | 100 | very active | Classic | 12 |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 152,041 (▲246) | Python | 79 | very active | Classic | 1 |
| [langgenius/dify](https://github.com/langgenius/dify) | 149,351 (▲693) | TypeScript | 90 | very active | Classic | 3 |
| [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | 54,742 (▲175) | TypeScript | 85 | very active | Classic | 3 |
| [simstudioai/sim](https://github.com/simstudioai/sim) | 29,156 (▲74) | TypeScript | 78 | very active | Hot | 1 |

### Coding-agent orchestration

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 77,391 (▲502) | Python | 84 | very active | Hot | 5 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 66,173 (▲518) | TypeScript | 78 | very active | Hot | 1 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 65,191 (▲961) | TypeScript | 76 | very active | Hot | 1 |
| [wshobson/agents](https://github.com/wshobson/agents) | 38,060 (▲208) | Python | 65 | very active | Hot | 1 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | 37,897 (▲178) | TypeScript | 80 | very active | Hot | 1 |
| [eigent-ai/eigent](https://github.com/eigent-ai/eigent) | 14,606 (▲53) | TypeScript | 83 | very active | Hot | 3 |
| [getpaseo/paseo](https://github.com/getpaseo/paseo) | 10,864 (▲564) | TypeScript | 74 | very active | Hot | 1 |
| [AgentWrapper/agent-orchestrator](https://github.com/AgentWrapper/agent-orchestrator) | 8,385 (▲163) | Go | 97 | very active | Hot | 7 |
| [vercel-labs/coding-agent-template](https://github.com/vercel-labs/coding-agent-template) | 1,748 (▲6) | TypeScript | 26 | slowing | Declining | 0 |

### Agent OS / long-horizon harness

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [elizaOS/eliza](https://github.com/elizaOS/eliza) | 18,768 (▲32) | TypeScript | 74 | very active | Mature | 1 |

### Durable / production infra

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [flyteorg/flyte](https://github.com/flyteorg/flyte) | 7,146 (▲10) | Go | 85 | very active | Classic | 2 |
| [inngest/agent-kit](https://github.com/inngest/agent-kit) | 914 (▲2) | TypeScript | 50 | slowing | Declining | 1 |

### Vertical / domain systems

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 93,683 (▲988) | Python | 75 | very active | Mature | 1 |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | 28,451 (▲172) | Python | 84 | very active | Classic | 2 |

### Protocols & meta-frameworks

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [sentient-agi/ROMA](https://github.com/sentient-agi/ROMA) | 5,094 (▲6) | Python | 28 | slowing | Declining | 0 |
| [TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi) | 3,599 (▲7) | TypeScript | 41 | slowing | Declining | 0 |
| [veegee82/agent-workflow-protocol](https://github.com/veegee82/agent-workflow-protocol) | 18 | Python | 44 | slowing | Rising | 1 |

## Details

### Code-first agent frameworks

_SDKs you write agents in — maximum control over routing, state and hand-offs; the engineer's default._

- **[FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT)** · 69,432★ · Python · Mature · health 25  
  Multi-agent 'software company' — assigns SOPs/roles (PM, architect, engineer).  
  <sub>topics: agent, gpt, llm, metagpt, multi-agent</sub>
- **[microsoft/autogen](https://github.com/microsoft/autogen)** · 59,817★ · Python · Mature · health 40  
  Microsoft's conversational multi-agent framework; agents talk to solve tasks.  
  <sub>topics: chatgpt, llm-agent, llm-framework, agentic, agentic-agi, agents</sub>
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** · 55,788★ · Python · Mature · health 85  
  Role-based 'crew' multi-agent framework — agents with roles, goals & tools collaborate.  
  <sub>topics: agents, ai, ai-agents, llms, aiagentframework</sub>
- **[agno-agi/agno](https://github.com/agno-agi/agno)** · 41,291★ · Python · Classic · health 93  
  Fast multimodal agent framework (ex-phidata) with memory/tools/teams.  
  <sub>topics: developer-tools, python, agents, ai, ai-agents</sub>
- **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** · 37,615★ · Python · Mature · health 77  
  Graph-based agent runtime — explicit nodes/edges/state; the de-facto control-flow framework.  
  <sub>topics: agents, ai, ai-agents, chatgpt, deepagents, enterprise</sub>
- **[stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)** · 36,229★ · Python · Classic · health 82  
  Programmatic prompt/pipeline optimization — compile agent behavior instead of hand-prompting.  
  <sub>topics: —</sub>
- **[huggingface/smolagents](https://github.com/huggingface/smolagents)** · 28,436★ · Python · Mature · health 66  
  Minimalist code-agent framework — agents that write & run Python to act.  
  <sub>topics: —</sub>
- **[microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)** · 28,331★ · C# · Classic · health 82  
  Microsoft's enterprise SDK (C#/Python) for plugging LLMs + planning into apps.  
  <sub>topics: ai, artificial-intelligence, llm, openai, sdk</sub>
- **[openai/openai-agents-python](https://github.com/openai/openai-agents-python)** · 28,019★ · Python · Hot · health 80  
  Lightweight, powerful framework for multi-agent workflows; handoffs + guardrails + tracing.  
  <sub>topics: agents, ai, framework, llm, python, openai</sub>
- **[agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)** · 28,012★ · Python · Mature · health 87  
  Build agents you can see/understand/trust; strong observability + multi-agent.  
  <sub>topics: agent, chatbot, large-language-models, llm, llm-agent, multi-agent</sub>
- **[google/adk-python](https://github.com/google/adk-python)** · 20,730★ · Python · Hot · health 88  
  Google's code-first Agent Development Kit — build, evaluate & deploy agents.  
  <sub>topics: agent, agents, agents-sdk, ai, ai-agents, multi-agent-systems</sub>
- **[camel-ai/camel](https://github.com/camel-ai/camel)** · 17,424★ · Python · Classic · health 86  
  Large multi-agent 'society' framework for studying agent cooperation at scale.  
  <sub>topics: ai-societies, artificial-intelligence, deep-learning, large-language-models, multi-agent-systems, natural-language-processing</sub>
- **[microsoft/agent-framework](https://github.com/microsoft/agent-framework)** · 12,226★ · Python · Hot · health 93  
  Microsoft's framework to build, orchestrate & deploy multi-agent workflows (health 92).  
  <sub>topics: agent-framework, agentic-ai, agents, ai, multi-agent, orchestration</sub>
- **[VoltAgent/voltagent](https://github.com/VoltAgent/voltagent)** · 10,096★ · TypeScript · Hot · health 79  
  TypeScript agent-engineering platform + open-source framework.  
  <sub>topics: agents, ai, chatbots, llm, mcp, nodejs</sub>
- **[strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)** · 6,641★ · Python · Hot · health 91  
  Model-driven agents in a few lines; very high health (96) and bus factor 7.  
  <sub>topics: agentic, agentic-ai, agents, ai, autonomous-agents, llm</sub>
- **[i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework)** · 3,328★ · Python · Hot · health 85  
  Production-ready agents in both Python and TypeScript.  
  <sub>topics: agents, ai, framework, ai-agent, llm, multiagent</sub>
- **[liquidos-ai/AutoAgents](https://github.com/liquidos-ai/AutoAgents)** · 713★ · Rust · Hot · health 69  
  Rust multi-agent framework to build, deploy & coordinate agents.  
  <sub>topics: agents, ai, ai-agents, ai-agents-framework, llm</sub>

### Visual / low-code platforms

_Drag-and-drop canvases — fastest to a working flow, accessible to non-engineers, less granular control._

- **[n8n-io/n8n](https://github.com/n8n-io/n8n)** · 197,066★ · TypeScript · Classic · health 100  
  Fair-code workflow automation with native AI nodes — the giant (189k★, health 100).  
  <sub>topics: automation, ipaas, n8n, workflow, typescript, self-hosted</sub>
- **[langflow-ai/langflow](https://github.com/langflow-ai/langflow)** · 152,041★ · Python · Classic · health 79  
  Popular drag-and-drop builder for agents & flows; visual graph of components.  
  <sub>topics: react-flow, chatgpt, large-language-models, generative-ai, agents, multiagent</sub>
- **[langgenius/dify](https://github.com/langgenius/dify)** · 149,351★ · TypeScript · Classic · health 90  
  Production-ready platform for agentic workflow development (health 100).  
  <sub>topics: ai, gpt, llm, openai, python, rag</sub>
- **[FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)** · 54,742★ · TypeScript · Classic · health 85  
  Build AI agents visually; popular drag-and-drop builder.  
  <sub>topics: artificial-intelligence, chatgpt, large-language-models, low-code, no-code, javascript</sub>
- **[simstudioai/sim](https://github.com/simstudioai/sim)** · 29,156★ · TypeScript · Hot · health 78  
  Build, deploy & orchestrate agents — 'central intelligence layer for your AI workforce'.  
  <sub>topics: agentic-workflow, agents, ai, nextjs, typescript, agent-workflow</sub>

### Coding-agent orchestration

_Coordinate *swarms of coding agents* (Claude Code, Codex, Cursor…) on a codebase — plan, spawn, run in parallel, handle CI._

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 77,391★ · Python · Hot · health 84  
  Long-horizon SuperAgent harness that researches, codes & creates with sandboxes (bf6).  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 66,173★ · TypeScript · Hot · health 78  
  'omo' — agent harness (formerly oh-my-opencode) for coding workflows.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 65,191★ · TypeScript · Hot · health 76  
  Agent-orchestration platform for Claude — multi-agent swarms coordinating autonomous coding.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents</sub>
- **[wshobson/agents](https://github.com/wshobson/agents)** · 38,060★ · Python · Hot · health 65  
  Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor, OpenCode, Gemini).  
  <sub>topics: agents, anthropic, automation, workflows, orchestration, agent-skills</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 37,897★ · TypeScript · Hot · health 80  
  Teams-first multi-agent orchestration for Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode</sub>
- **[eigent-ai/eigent](https://github.com/eigent-ai/eigent)** · 14,606★ · TypeScript · Hot · health 83  
  Open-source cowork desktop — local/free multi-agent productivity workspace.  
  <sub>topics: agent-framework, agent-skills, agentic-ai, agentic-workflow, claude-cowork, claude-cowork-alternative</sub>
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 10,864★ · TypeScript · Hot · health 74  
  Run & coordinate coding agents from phone, desktop and CLI.  
  <sub>topics: agents, claude-code, codex, opencode, ade, copilot</sub>
- **[AgentWrapper/agent-orchestrator](https://github.com/AgentWrapper/agent-orchestrator)** · 8,385★ · Go · Hot · health 97  
  Orchestrates parallel coding agents — plans tasks, spawns agents, handles CI autonomously.  
  <sub>topics: claude-code, codex-cli, orchestration, orchestrator, skills, agent-fleet</sub>
- **[vercel-labs/coding-agent-template](https://github.com/vercel-labs/coding-agent-template)** · 1,748★ · TypeScript · Declining · health 26  
  Multi-agent coding platform on Vercel Sandbox + AI Gateway; declining, verify first.  
  <sub>topics: —</sub>

### Agent OS / long-horizon harness

_Runtimes for always-on, long-running autonomous agents._

- **[elizaOS/eliza](https://github.com/elizaOS/eliza)** · 18,768★ · TypeScript · Mature · health 74  
  Open-source 'agentic operating system' — long-running autonomous agents.  
  <sub>topics: agent, agentic, ai, autonomous, chatbot, crypto</sub>

### Durable / production infra

_Fault-tolerant execution — retries, checkpointing, deterministic routing for production._

- **[flyteorg/flyte](https://github.com/flyteorg/flyte)** · 7,146★ · Go · Classic · health 85  
  Dynamic, resilient orchestration (Go/K8s) — coordinate data, models & compute durably.  
  <sub>topics: flyte, machine-learning, golang, scale, workflow, data-science</sub>
- **[inngest/agent-kit](https://github.com/inngest/agent-kit)** · 914★ · TypeScript · Declining · health 50  
  Build multi-agent networks in TS with deterministic routing + durable execution via MCP.  
  <sub>topics: agent, ai, ai-agent-framework, ai-agents, llm</sub>

### Vertical / domain systems

_Reference multi-agent architectures for a specific domain._

- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 93,683★ · Python · Mature · health 75  
  Multi-agent LLM framework for financial trading — a vertical reference architecture (79k★).  
  <sub>topics: agent, finance, llm, multiagent, trading</sub>
- **[assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)** · 28,451★ · Python · Classic · health 84  
  Autonomous research agent that plans, searches & writes cited reports.  
  <sub>topics: ai, python, agent, automation, research, search</sub>

### Protocols & meta-frameworks

_Standards and meta-layers above any single framework._

- **[sentient-agi/ROMA](https://github.com/sentient-agi/ROMA)** · 5,094★ · Python · Declining · health 28  
  Recursive meta-agent framework to build multi-agent systems; declining/low health.  
  <sub>topics: —</sub>
- **[TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi)** · 3,599★ · TypeScript · Declining · health 41  
  Agent-teams orchestrator aimed at one-person companies.  
  <sub>topics: —</sub>
- **[veegee82/agent-workflow-protocol](https://github.com/veegee82/agent-workflow-protocol)** · 18★ · Python · Rising · health 44  
  Open standard for multi-agent workflows — scripted pipelines to self-organizing teams.  
  <sub>topics: agentic, agentic-ai, agentic-ai-development, agentic-engineering, agentic-framework, agentic-workflow</sub>

## Graph analysis — how they relate

**Community clustering.** These 39 tools span **12 of the graph's 28 communities**.

- **Community 9** (10): `langchain-ai/langgraph`, `VoltAgent/voltagent`, `i-am-bee/beeai-framework`, `liquidos-ai/AutoAgents`, `crewAIInc/crewAI`, `agno-agi/agno`, `assafelovic/gpt-researcher`, `langflow-ai/langflow`, `inngest/agent-kit`, `veegee82/agent-workflow-protocol`
- **Community 2** (6): `wshobson/agents`, `Yeachan-Heo/oh-my-claudecode`, `getpaseo/paseo`, `vercel-labs/coding-agent-template`, `elizaOS/eliza`, `TinyAGI/tinyagi`
- **Community 22** (5): `agentscope-ai/agentscope`, `huggingface/smolagents`, `camel-ai/camel`, `eigent-ai/eigent`, `flyteorg/flyte`
- **Community 21** (3): `microsoft/semantic-kernel`, `microsoft/agent-framework`, `microsoft/autogen`
- **Community 20** (3): `strands-agents/harness-sdk`, `FoundationAgents/MetaGPT`, `TauricResearch/TradingAgents`
- **Community 15** (3): `langgenius/dify`, `FlowiseAI/Flowise`, `simstudioai/sim`
- **Community 8** (3): `code-yeongyu/oh-my-openagent`, `ruvnet/ruflo`, `AgentWrapper/agent-orchestrator`
- **Community 19** (2): `google/adk-python`, `bytedance/deer-flow`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' orchestration tools in your ecosystem:

- `agno-agi/agno` — PageRank 0.0026
- `langchain-ai/langgraph` — PageRank 0.0021
- `liquidos-ai/AutoAgents` — PageRank 0.0021
- `openai/openai-agents-python` — PageRank 0.0020
- `microsoft/semantic-kernel` — PageRank 0.0019
- `crewAIInc/crewAI` — PageRank 0.0016
- `microsoft/agent-framework` — PageRank 0.0016
- `VoltAgent/voltagent` — PageRank 0.0015
- `google/adk-python` — PageRank 0.0015
- `langgenius/dify` — PageRank 0.0013

**Direct links between orchestration tools** (top similarity edges where both endpoints are in this report):

- `microsoft/agent-framework` ⇄ `microsoft/semantic-kernel` (w=0.928) — topics: ai, sdk; authors: eavanvalkenburg, westey-m, moonbox3
- `microsoft/autogen` ⇄ `microsoft/agent-framework` (w=0.661) — topics: agents, ai
- `i-am-bee/beeai-framework` ⇄ `openai/openai-agents-python` (w=0.552) — topics: agents, ai, framework, llm; authors: dependabot[bot]
- `agno-agi/agno` ⇄ `crewAIInc/crewAI` (w=0.479) — topics: agents, ai, ai-agents
- `FlowiseAI/Flowise` ⇄ `simstudioai/sim` (w=0.450) — topics: artificial-intelligence, low-code, no-code, react
- `agno-agi/agno` ⇄ `liquidos-ai/AutoAgents` (w=0.429) — topics: agents, ai, ai-agents
- `crewAIInc/crewAI` ⇄ `liquidos-ai/AutoAgents` (w=0.429) — topics: agents, ai, ai-agents
- `liquidos-ai/AutoAgents` ⇄ `inngest/agent-kit` (w=0.429) — topics: ai, ai-agents, llm
- `VoltAgent/voltagent` ⇄ `i-am-bee/beeai-framework` (w=0.399) — topics: agents, ai, llm, typescript; authors: octo-patch, kriptoburak
- `strands-agents/harness-sdk` ⇄ `openai/openai-agents-python` (w=0.377) — topics: agents, ai, llm, python; authors: dependabot[bot]
- `simstudioai/sim` ⇄ `langgenius/dify` (w=0.360) — topics: agentic-workflow, ai, nextjs, gemini
- `strands-agents/harness-sdk` ⇄ `microsoft/agent-framework` (w=0.329) — topics: agentic-ai, agents, ai, python; authors: dependabot[bot]
- `bytedance/deer-flow` ⇄ `google/adk-python` (w=0.328) — topics: agent, agentic, ai, ai-agents; authors: VectorPeak, dependabot[bot]
- `FoundationAgents/MetaGPT` ⇄ `agentscope-ai/agentscope` (w=0.323) — topics: agent, llm, multi-agent
- `FoundationAgents/MetaGPT` ⇄ `TauricResearch/TradingAgents` (w=0.300) — topics: agent, llm
- …and 14 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Orchestration is load-bearing — weigh this heavily before standardizing on one.

| Tool | Approach | Health | Lifecycle | Activity | Bus factor |
|---|---|---|---|---|---|
| n8n-io/n8n | Visual / low-code platforms | 100 | Classic | very active | 12 |
| AgentWrapper/agent-orchestrator | Coding-agent orchestration | 97 | Hot | very active | 7 |
| microsoft/agent-framework | Code-first agent frameworks | 93 | Hot | very active | 4 |
| agno-agi/agno | Code-first agent frameworks | 93 | Classic | very active | 4 |
| strands-agents/harness-sdk | Code-first agent frameworks | 91 | Hot | very active | 4 |
| langgenius/dify | Visual / low-code platforms | 90 | Classic | very active | 3 |
| google/adk-python | Code-first agent frameworks | 88 | Hot | very active | 3 |
| agentscope-ai/agentscope | Code-first agent frameworks | 87 | Mature | very active | 3 |
| camel-ai/camel | Code-first agent frameworks | 86 | Classic | very active | 3 |
| i-am-bee/beeai-framework | Code-first agent frameworks | 85 | Hot | very active | 3 |
| crewAIInc/crewAI | Code-first agent frameworks | 85 | Mature | very active | 2 |
| FlowiseAI/Flowise | Visual / low-code platforms | 85 | Classic | very active | 3 |
| flyteorg/flyte | Durable / production infra | 85 | Classic | very active | 2 |
| assafelovic/gpt-researcher | Vertical / domain systems | 84 | Classic | very active | 2 |
| bytedance/deer-flow | Coding-agent orchestration | 84 | Hot | very active | 5 |
| eigent-ai/eigent | Coding-agent orchestration | 83 | Hot | very active | 3 |
| microsoft/semantic-kernel | Code-first agent frameworks | 82 | Classic | very active | 2 |
| stanfordnlp/dspy | Code-first agent frameworks | 82 | Classic | very active | 2 |
| openai/openai-agents-python | Code-first agent frameworks | 80 | Hot | very active | 1 |
| Yeachan-Heo/oh-my-claudecode | Coding-agent orchestration | 80 | Hot | very active | 1 |
| VoltAgent/voltagent | Code-first agent frameworks | 79 | Hot | very active | 2 |
| langflow-ai/langflow | Visual / low-code platforms | 79 | Classic | very active | 1 |
| simstudioai/sim | Visual / low-code platforms | 78 | Hot | very active | 1 |
| code-yeongyu/oh-my-openagent | Coding-agent orchestration | 78 | Hot | very active | 1 |
| langchain-ai/langgraph | Code-first agent frameworks | 77 | Mature | very active | 1 |
| ruvnet/ruflo | Coding-agent orchestration | 76 | Hot | very active | 1 |
| TauricResearch/TradingAgents | Vertical / domain systems | 75 | Mature | very active | 1 |
| getpaseo/paseo | Coding-agent orchestration | 74 | Hot | very active | 1 |
| elizaOS/eliza | Agent OS / long-horizon harness | 74 | Mature | very active | 1 |
| liquidos-ai/AutoAgents | Code-first agent frameworks | 69 | Hot | very active | 1 |
| huggingface/smolagents | Code-first agent frameworks | 66 | Mature | active | 1 |
| wshobson/agents | Coding-agent orchestration | 65 | Hot | very active | 1 |
| inngest/agent-kit | Durable / production infra | 50 | Declining | slowing | 1 |
| veegee82/agent-workflow-protocol | Protocols & meta-frameworks | 44 | Rising | slowing | 1 |
| TinyAGI/tinyagi | Protocols & meta-frameworks | 41 | Declining | slowing | 0 |
| microsoft/autogen | Code-first agent frameworks | 40 | Mature | slowing | 0 |
| sentient-agi/ROMA | Protocols & meta-frameworks | 28 | Declining | slowing | 0 |
| vercel-labs/coding-agent-template | Coding-agent orchestration | 26 | Declining | slowing | 0 |
| FoundationAgents/MetaGPT | Code-first agent frameworks | 25 | Mature | slowing | 0 |

⚠️ **Adopt with caution** (low health and/or declining): `FoundationAgents/MetaGPT`, `vercel-labs/coding-agent-template`, `sentient-agi/ROMA`, `microsoft/autogen`, `TinyAGI/tinyagi`, `veegee82/agent-workflow-protocol`, `inngest/agent-kit`.

## Coverage

Your stars now cover the canonical orchestration frameworks (crewAI, AutoGen, LangGraph, langflow, semantic-kernel, ADK, agentscope, …) — no major gaps left in this category.

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: scan for orchestration / multi-agent / swarm / workflow / agent-framework signals, then manual curation by approach. RAG frameworks, eval/observability platforms, and single-purpose agents were routed to their own reports or excluded; only tools whose *primary* job is coordinating agents/steps appear here.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub. Re-run after a fresh `classified.json` to refresh.

<sub>Tools covered: 39 across 7 approaches · Snapshot: 2026-07-19T22:39:07.967Z</sub>
