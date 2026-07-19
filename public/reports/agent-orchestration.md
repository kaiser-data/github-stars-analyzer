# AI Agent Orchestration — Landscape Report

> Derived from **kaiser-data**'s 1,327 starred repos (snapshot `2026-07-13T08:42:30.177Z`), cross-referenced with the repo-similarity graph (1,327 nodes / 4,302 edges, 26 communities).
>
> Generated 2026-07-19 by `scripts/reports/agent_orchestration.py` (regenerate any time — no API cost).

![Top tools by stars](assets/agent-orchestration-top-tools.svg)

![Tools per category](assets/agent-orchestration-categories.svg)


> **Orchestration** = coordinating multiple agents / tools / steps toward a goal: routing, planning, parallelism, hand-offs, state and recovery. The tools below differ mostly in **how you express that coordination** — in code, on a visual canvas, across coding agents, or as durable production infra.

## Executive summary

- **37 agent-orchestration tools** in your stars (**1,520,898★**), organized by *how you express coordination*:
  - **Code-first agent frameworks** (16): `MetaGPT`, `autogen`, `crewAI`, `agno`, `langgraph`, `dspy`, `smolagents`, `semantic-kernel`, `openai-agents-python`, `agentscope`, `adk-python`, `camel`, `agent-framework`, `voltagent`, `beeai-framework`, `AutoAgents`
  - **Visual / low-code platforms** (5): `n8n`, `langflow`, `dify`, `Flowise`, `sim`
  - **Coding-agent orchestration** (8): `deer-flow`, `oh-my-openagent`, `ruflo`, `agents`, `oh-my-claudecode`, `eigent`, `paseo`, `coding-agent-template`
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
| [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 69,333 (▲606) | Python | 25 | slowing | Mature | 0 |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 59,693 (▲814) | Python | 41 | slowing | Mature | 0 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 55,417 (▲2,137) | Python | 85 | very active | Mature | 2 |
| [agno-agi/agno](https://github.com/agno-agi/agno) | 41,121 (▲475) | Python | 98 | very active | Classic | 6 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 37,147 (▲2,689) | Python | 77 | very active | Mature | 1 |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | 36,085 (▲1,095) | Python | 83 | very active | Classic | 2 |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | 28,315 (▲498) | Python | 66 | active | Mature | 1 |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | 28,303 (▲197) | C# | 82 | very active | Classic | 2 |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 27,866 (▲782) | Python | 80 | very active | Hot | 1 |
| [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | 27,795 (▲1,091) | Python | 87 | very active | Mature | 3 |
| [google/adk-python](https://github.com/google/adk-python) | 20,580 (▲506) | Python | 93 | very active | Hot | 4 |
| [camel-ai/camel](https://github.com/camel-ai/camel) | 17,372 (▲211) | Python | 86 | very active | Classic | 3 |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | 12,082 (▲821) | Python | 98 | very active | Hot | 5 |
| [VoltAgent/voltagent](https://github.com/VoltAgent/voltagent) | 10,032 (▲487) | TypeScript | 79 | very active | Hot | 2 |
| [i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework) | 3,315 (▲25) | Python | 85 | very active | Hot | 3 |
| [liquidos-ai/AutoAgents](https://github.com/liquidos-ai/AutoAgents) | 711 (▲38) | Rust | 69 | very active | Hot | 1 |

### Visual / low-code platforms

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 196,233 (▲4,138) | TypeScript | 100 | very active | Classic | 12 |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 151,795 (▲2,243) | Python | 79 | very active | Classic | 1 |
| [langgenius/dify](https://github.com/langgenius/dify) | 148,658 (▲3,783) | TypeScript | 90 | very active | Classic | 3 |
| [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | 54,567 (▲1,080) | TypeScript | 90 | very active | Classic | 4 |
| [simstudioai/sim](https://github.com/simstudioai/sim) | 29,082 (▲332) | TypeScript | 78 | very active | Hot | 1 |

### Coding-agent orchestration

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 76,889 (▲5,901) | Python | 79 | very active | Hot | 4 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 65,655 (▲3,730) | TypeScript | 78 | very active | Hot | 1 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 64,230 (▲5,237) | TypeScript | 76 | very active | Mature | 1 |
| [wshobson/agents](https://github.com/wshobson/agents) | 37,852 (▲1,215) | Python | 65 | very active | Hot | 1 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | 37,719 (▲1,498) | TypeScript | 80 | very active | Hot | 1 |
| [eigent-ai/eigent](https://github.com/eigent-ai/eigent) | 14,553 (▲292) | TypeScript | 74 | very active | Rising | 2 |
| [getpaseo/paseo](https://github.com/getpaseo/paseo) | 10,300 (▲1,937) | TypeScript | 74 | very active | Hot | 1 |
| [vercel-labs/coding-agent-template](https://github.com/vercel-labs/coding-agent-template) | 1,742 (▲16) | TypeScript | 27 | slowing | Declining | 0 |

### Agent OS / long-horizon harness

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [elizaOS/eliza](https://github.com/elizaOS/eliza) | 18,736 (▲178) | TypeScript | 72 | very active | Mature | 1 |

### Durable / production infra

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [flyteorg/flyte](https://github.com/flyteorg/flyte) | 7,136 (▲57) | Go | 85 | very active | Classic | 2 |
| [inngest/agent-kit](https://github.com/inngest/agent-kit) | 912 (▲26) | TypeScript | 50 | slowing | Declining | 1 |

### Vertical / domain systems

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 92,695 (▲7,465) | Python | 75 | very active | Mature | 1 |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | 28,279 (▲634) | Python | 75 | very active | Classic | 1 |

### Protocols & meta-frameworks

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [sentient-agi/ROMA](https://github.com/sentient-agi/ROMA) | 5,088 (▲16) | Python | 29 | slowing | Declining | 0 |
| [TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi) | 3,592 (▲16) | TypeScript | 41 | slowing | Declining | 0 |
| [veegee82/agent-workflow-protocol](https://github.com/veegee82/agent-workflow-protocol) | 18 | Python | 55 | active | Rising | 1 |

## Details

### Code-first agent frameworks

_SDKs you write agents in — maximum control over routing, state and hand-offs; the engineer's default._

- **[FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT)** · 69,333★ · Python · Mature · health 25  
  Multi-agent 'software company' — assigns SOPs/roles (PM, architect, engineer).  
  <sub>topics: agent, gpt, llm, metagpt, multi-agent</sub>
- **[microsoft/autogen](https://github.com/microsoft/autogen)** · 59,693★ · Python · Mature · health 41  
  Microsoft's conversational multi-agent framework; agents talk to solve tasks.  
  <sub>topics: chatgpt, llm-agent, llm-framework, agentic, agentic-agi, agents</sub>
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** · 55,417★ · Python · Mature · health 85  
  Role-based 'crew' multi-agent framework — agents with roles, goals & tools collaborate.  
  <sub>topics: agents, ai, ai-agents, llms, aiagentframework</sub>
- **[agno-agi/agno](https://github.com/agno-agi/agno)** · 41,121★ · Python · Classic · health 98  
  Fast multimodal agent framework (ex-phidata) with memory/tools/teams.  
  <sub>topics: developer-tools, python, agents, ai, ai-agents</sub>
- **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** · 37,147★ · Python · Mature · health 77  
  Graph-based agent runtime — explicit nodes/edges/state; the de-facto control-flow framework.  
  <sub>topics: agents, ai, ai-agents, chatgpt, deepagents, enterprise</sub>
- **[stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)** · 36,085★ · Python · Classic · health 83  
  Programmatic prompt/pipeline optimization — compile agent behavior instead of hand-prompting.  
  <sub>topics: —</sub>
- **[huggingface/smolagents](https://github.com/huggingface/smolagents)** · 28,315★ · Python · Mature · health 66  
  Minimalist code-agent framework — agents that write & run Python to act.  
  <sub>topics: —</sub>
- **[microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)** · 28,303★ · C# · Classic · health 82  
  Microsoft's enterprise SDK (C#/Python) for plugging LLMs + planning into apps.  
  <sub>topics: ai, artificial-intelligence, llm, openai, sdk</sub>
- **[openai/openai-agents-python](https://github.com/openai/openai-agents-python)** · 27,866★ · Python · Hot · health 80  
  Lightweight, powerful framework for multi-agent workflows; handoffs + guardrails + tracing.  
  <sub>topics: agents, ai, framework, llm, python, openai</sub>
- **[agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)** · 27,795★ · Python · Mature · health 87  
  Build agents you can see/understand/trust; strong observability + multi-agent.  
  <sub>topics: agent, chatbot, large-language-models, llm, llm-agent, multi-agent</sub>
- **[google/adk-python](https://github.com/google/adk-python)** · 20,580★ · Python · Hot · health 93  
  Google's code-first Agent Development Kit — build, evaluate & deploy agents.  
  <sub>topics: agent, agents, agents-sdk, ai, ai-agents, multi-agent-systems</sub>
- **[camel-ai/camel](https://github.com/camel-ai/camel)** · 17,372★ · Python · Classic · health 86  
  Large multi-agent 'society' framework for studying agent cooperation at scale.  
  <sub>topics: ai-societies, artificial-intelligence, deep-learning, large-language-models, multi-agent-systems, natural-language-processing</sub>
- **[microsoft/agent-framework](https://github.com/microsoft/agent-framework)** · 12,082★ · Python · Hot · health 98  
  Microsoft's framework to build, orchestrate & deploy multi-agent workflows (health 92).  
  <sub>topics: agent-framework, agentic-ai, agents, ai, multi-agent, orchestration</sub>
- **[VoltAgent/voltagent](https://github.com/VoltAgent/voltagent)** · 10,032★ · TypeScript · Hot · health 79  
  TypeScript agent-engineering platform + open-source framework.  
  <sub>topics: agents, ai, chatbots, llm, mcp, nodejs</sub>
- **[i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework)** · 3,315★ · Python · Hot · health 85  
  Production-ready agents in both Python and TypeScript.  
  <sub>topics: agents, ai, framework, ai-agent, llm, multiagent</sub>
- **[liquidos-ai/AutoAgents](https://github.com/liquidos-ai/AutoAgents)** · 711★ · Rust · Hot · health 69  
  Rust multi-agent framework to build, deploy & coordinate agents.  
  <sub>topics: agents, ai, ai-agents, ai-agents-framework, llm</sub>

### Visual / low-code platforms

_Drag-and-drop canvases — fastest to a working flow, accessible to non-engineers, less granular control._

- **[n8n-io/n8n](https://github.com/n8n-io/n8n)** · 196,233★ · TypeScript · Classic · health 100  
  Fair-code workflow automation with native AI nodes — the giant (189k★, health 100).  
  <sub>topics: automation, ipaas, n8n, workflow, typescript, self-hosted</sub>
- **[langflow-ai/langflow](https://github.com/langflow-ai/langflow)** · 151,795★ · Python · Classic · health 79  
  Popular drag-and-drop builder for agents & flows; visual graph of components.  
  <sub>topics: react-flow, chatgpt, large-language-models, generative-ai, agents, multiagent</sub>
- **[langgenius/dify](https://github.com/langgenius/dify)** · 148,658★ · TypeScript · Classic · health 90  
  Production-ready platform for agentic workflow development (health 100).  
  <sub>topics: ai, gpt, llm, openai, python, rag</sub>
- **[FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)** · 54,567★ · TypeScript · Classic · health 90  
  Build AI agents visually; popular drag-and-drop builder.  
  <sub>topics: artificial-intelligence, chatgpt, large-language-models, low-code, no-code, javascript</sub>
- **[simstudioai/sim](https://github.com/simstudioai/sim)** · 29,082★ · TypeScript · Hot · health 78  
  Build, deploy & orchestrate agents — 'central intelligence layer for your AI workforce'.  
  <sub>topics: agentic-workflow, agents, ai, nextjs, typescript, agent-workflow</sub>

### Coding-agent orchestration

_Coordinate *swarms of coding agents* (Claude Code, Codex, Cursor…) on a codebase — plan, spawn, run in parallel, handle CI._

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 76,889★ · Python · Hot · health 79  
  Long-horizon SuperAgent harness that researches, codes & creates with sandboxes (bf6).  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 65,655★ · TypeScript · Hot · health 78  
  'omo' — agent harness (formerly oh-my-opencode) for coding workflows.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 64,230★ · TypeScript · Mature · health 76  
  Agent-orchestration platform for Claude — multi-agent swarms coordinating autonomous coding.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents</sub>
- **[wshobson/agents](https://github.com/wshobson/agents)** · 37,852★ · Python · Hot · health 65  
  Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor, OpenCode, Gemini).  
  <sub>topics: agents, anthropic, automation, workflows, orchestration, agent-skills</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 37,719★ · TypeScript · Hot · health 80  
  Teams-first multi-agent orchestration for Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode</sub>
- **[eigent-ai/eigent](https://github.com/eigent-ai/eigent)** · 14,553★ · TypeScript · Rising · health 74  
  Open-source cowork desktop — local/free multi-agent productivity workspace.  
  <sub>topics: agent-framework, agent-skills, agentic-ai, agentic-workflow, claude-cowork, claude-cowork-alternative</sub>
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 10,300★ · TypeScript · Hot · health 74  
  Run & coordinate coding agents from phone, desktop and CLI.  
  <sub>topics: agents, claude-code, codex, opencode, ade, copilot</sub>
- **[vercel-labs/coding-agent-template](https://github.com/vercel-labs/coding-agent-template)** · 1,742★ · TypeScript · Declining · health 27  
  Multi-agent coding platform on Vercel Sandbox + AI Gateway; declining, verify first.  
  <sub>topics: —</sub>

### Agent OS / long-horizon harness

_Runtimes for always-on, long-running autonomous agents._

- **[elizaOS/eliza](https://github.com/elizaOS/eliza)** · 18,736★ · TypeScript · Mature · health 72  
  Open-source 'agentic operating system' — long-running autonomous agents.  
  <sub>topics: agent, agentic, ai, autonomous, chatbot, crypto</sub>

### Durable / production infra

_Fault-tolerant execution — retries, checkpointing, deterministic routing for production._

- **[flyteorg/flyte](https://github.com/flyteorg/flyte)** · 7,136★ · Go · Classic · health 85  
  Dynamic, resilient orchestration (Go/K8s) — coordinate data, models & compute durably.  
  <sub>topics: flyte, machine-learning, golang, scale, workflow, data-science</sub>
- **[inngest/agent-kit](https://github.com/inngest/agent-kit)** · 912★ · TypeScript · Declining · health 50  
  Build multi-agent networks in TS with deterministic routing + durable execution via MCP.  
  <sub>topics: agent, ai, ai-agent-framework, ai-agents, llm</sub>

### Vertical / domain systems

_Reference multi-agent architectures for a specific domain._

- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 92,695★ · Python · Mature · health 75  
  Multi-agent LLM framework for financial trading — a vertical reference architecture (79k★).  
  <sub>topics: agent, finance, llm, multiagent, trading</sub>
- **[assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)** · 28,279★ · Python · Classic · health 75  
  Autonomous research agent that plans, searches & writes cited reports.  
  <sub>topics: ai, python, agent, automation, research, search</sub>

### Protocols & meta-frameworks

_Standards and meta-layers above any single framework._

- **[sentient-agi/ROMA](https://github.com/sentient-agi/ROMA)** · 5,088★ · Python · Declining · health 29  
  Recursive meta-agent framework to build multi-agent systems; declining/low health.  
  <sub>topics: —</sub>
- **[TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi)** · 3,592★ · TypeScript · Declining · health 41  
  Agent-teams orchestrator aimed at one-person companies.  
  <sub>topics: —</sub>
- **[veegee82/agent-workflow-protocol](https://github.com/veegee82/agent-workflow-protocol)** · 18★ · Python · Rising · health 55  
  Open standard for multi-agent workflows — scripted pipelines to self-organizing teams.  
  <sub>topics: agentic, agentic-ai, agentic-ai-development, agentic-engineering, agentic-framework, agentic-workflow</sub>

## Graph analysis — how they relate

**Community clustering.** These 37 tools span **14 of the graph's 26 communities**.

- **Community 1** (6): `liquidos-ai/AutoAgents`, `crewAIInc/crewAI`, `agno-agi/agno`, `assafelovic/gpt-researcher`, `n8n-io/n8n`, `inngest/agent-kit`
- **Community 7** (5): `langchain-ai/langgraph`, `VoltAgent/voltagent`, `i-am-bee/beeai-framework`, `langflow-ai/langflow`, `bytedance/deer-flow`
- **Community 20** (5): `agentscope-ai/agentscope`, `huggingface/smolagents`, `camel-ai/camel`, `eigent-ai/eigent`, `flyteorg/flyte`
- **Community 19** (3): `microsoft/semantic-kernel`, `microsoft/agent-framework`, `microsoft/autogen`
- **Community 17** (3): `FoundationAgents/MetaGPT`, `TauricResearch/TradingAgents`, `veegee82/agent-workflow-protocol`
- **Community 9** (3): `langgenius/dify`, `FlowiseAI/Flowise`, `simstudioai/sim`
- **Community 16** (3): `code-yeongyu/oh-my-openagent`, `ruvnet/ruflo`, `getpaseo/paseo`
- **Community 8** (3): `wshobson/agents`, `vercel-labs/coding-agent-template`, `TinyAGI/tinyagi`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' orchestration tools in your ecosystem:

- `langchain-ai/langgraph` — PageRank 0.0026
- `agno-agi/agno` — PageRank 0.0025
- `liquidos-ai/AutoAgents` — PageRank 0.0023
- `openai/openai-agents-python` — PageRank 0.0021
- `microsoft/semantic-kernel` — PageRank 0.0019
- `crewAIInc/crewAI` — PageRank 0.0017
- `microsoft/agent-framework` — PageRank 0.0016
- `VoltAgent/voltagent` — PageRank 0.0015
- `langgenius/dify` — PageRank 0.0015
- `huggingface/smolagents` — PageRank 0.0014

**Direct links between orchestration tools** (top similarity edges where both endpoints are in this report):

- `microsoft/agent-framework` ⇄ `microsoft/semantic-kernel` (w=0.965) — topics: ai, sdk; authors: eavanvalkenburg, westey-m, moonbox3
- `microsoft/autogen` ⇄ `microsoft/agent-framework` (w=0.661) — topics: agents, ai
- `i-am-bee/beeai-framework` ⇄ `openai/openai-agents-python` (w=0.547) — topics: agents, ai, framework, llm; authors: dependabot[bot]
- `agno-agi/agno` ⇄ `crewAIInc/crewAI` (w=0.479) — topics: agents, ai, ai-agents
- `FlowiseAI/Flowise` ⇄ `simstudioai/sim` (w=0.450) — topics: artificial-intelligence, low-code, no-code, react
- `agno-agi/agno` ⇄ `liquidos-ai/AutoAgents` (w=0.429) — topics: agents, ai, ai-agents
- `crewAIInc/crewAI` ⇄ `liquidos-ai/AutoAgents` (w=0.429) — topics: agents, ai, ai-agents
- `liquidos-ai/AutoAgents` ⇄ `inngest/agent-kit` (w=0.429) — topics: ai, ai-agents, llm
- `langchain-ai/langgraph` ⇄ `i-am-bee/beeai-framework` (w=0.398) — topics: agents, ai, framework, llm; authors: dependabot[bot]
- `VoltAgent/voltagent` ⇄ `i-am-bee/beeai-framework` (w=0.394) — topics: agents, ai, llm, typescript; authors: octo-patch, kriptoburak
- `simstudioai/sim` ⇄ `langgenius/dify` (w=0.360) — topics: agentic-workflow, ai, nextjs, gemini
- `FoundationAgents/MetaGPT` ⇄ `agentscope-ai/agentscope` (w=0.323) — topics: agent, llm, multi-agent
- `FoundationAgents/MetaGPT` ⇄ `TauricResearch/TradingAgents` (w=0.300) — topics: agent, llm
- `wshobson/agents` ⇄ `microsoft/agent-framework` (w=0.288) — topics: agents, workflows, orchestration, agentic-ai; authors: dependabot[bot]
- `camel-ai/camel` ⇄ `eigent-ai/eigent` (w=0.287) — topics: multi-agent-systems; authors: Wendong-Fan, fengju0213, octo-patch
- …and 7 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Orchestration is load-bearing — weigh this heavily before standardizing on one.

| Tool | Approach | Health | Lifecycle | Activity | Bus factor |
|---|---|---|---|---|---|
| n8n-io/n8n | Visual / low-code platforms | 100 | Classic | very active | 12 |
| microsoft/agent-framework | Code-first agent frameworks | 98 | Hot | very active | 5 |
| agno-agi/agno | Code-first agent frameworks | 98 | Classic | very active | 6 |
| google/adk-python | Code-first agent frameworks | 93 | Hot | very active | 4 |
| langgenius/dify | Visual / low-code platforms | 90 | Classic | very active | 3 |
| FlowiseAI/Flowise | Visual / low-code platforms | 90 | Classic | very active | 4 |
| agentscope-ai/agentscope | Code-first agent frameworks | 87 | Mature | very active | 3 |
| camel-ai/camel | Code-first agent frameworks | 86 | Classic | very active | 3 |
| i-am-bee/beeai-framework | Code-first agent frameworks | 85 | Hot | very active | 3 |
| crewAIInc/crewAI | Code-first agent frameworks | 85 | Mature | very active | 2 |
| flyteorg/flyte | Durable / production infra | 85 | Classic | very active | 2 |
| stanfordnlp/dspy | Code-first agent frameworks | 83 | Classic | very active | 2 |
| microsoft/semantic-kernel | Code-first agent frameworks | 82 | Classic | very active | 2 |
| openai/openai-agents-python | Code-first agent frameworks | 80 | Hot | very active | 1 |
| Yeachan-Heo/oh-my-claudecode | Coding-agent orchestration | 80 | Hot | very active | 1 |
| VoltAgent/voltagent | Code-first agent frameworks | 79 | Hot | very active | 2 |
| langflow-ai/langflow | Visual / low-code platforms | 79 | Classic | very active | 1 |
| bytedance/deer-flow | Coding-agent orchestration | 79 | Hot | very active | 4 |
| simstudioai/sim | Visual / low-code platforms | 78 | Hot | very active | 1 |
| code-yeongyu/oh-my-openagent | Coding-agent orchestration | 78 | Hot | very active | 1 |
| langchain-ai/langgraph | Code-first agent frameworks | 77 | Mature | very active | 1 |
| ruvnet/ruflo | Coding-agent orchestration | 76 | Mature | very active | 1 |
| assafelovic/gpt-researcher | Vertical / domain systems | 75 | Classic | very active | 1 |
| TauricResearch/TradingAgents | Vertical / domain systems | 75 | Mature | very active | 1 |
| eigent-ai/eigent | Coding-agent orchestration | 74 | Rising | very active | 2 |
| getpaseo/paseo | Coding-agent orchestration | 74 | Hot | very active | 1 |
| elizaOS/eliza | Agent OS / long-horizon harness | 72 | Mature | very active | 1 |
| liquidos-ai/AutoAgents | Code-first agent frameworks | 69 | Hot | very active | 1 |
| huggingface/smolagents | Code-first agent frameworks | 66 | Mature | active | 1 |
| wshobson/agents | Coding-agent orchestration | 65 | Hot | very active | 1 |
| veegee82/agent-workflow-protocol | Protocols & meta-frameworks | 55 | Rising | active | 1 |
| inngest/agent-kit | Durable / production infra | 50 | Declining | slowing | 1 |
| microsoft/autogen | Code-first agent frameworks | 41 | Mature | slowing | 0 |
| TinyAGI/tinyagi | Protocols & meta-frameworks | 41 | Declining | slowing | 0 |
| sentient-agi/ROMA | Protocols & meta-frameworks | 29 | Declining | slowing | 0 |
| vercel-labs/coding-agent-template | Coding-agent orchestration | 27 | Declining | slowing | 0 |
| FoundationAgents/MetaGPT | Code-first agent frameworks | 25 | Mature | slowing | 0 |

⚠️ **Adopt with caution** (low health and/or declining): `FoundationAgents/MetaGPT`, `vercel-labs/coding-agent-template`, `sentient-agi/ROMA`, `microsoft/autogen`, `TinyAGI/tinyagi`, `inngest/agent-kit`.

## Coverage

Your stars now cover the canonical orchestration frameworks (crewAI, AutoGen, LangGraph, langflow, semantic-kernel, ADK, agentscope, …) — no major gaps left in this category.

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: scan for orchestration / multi-agent / swarm / workflow / agent-framework signals, then manual curation by approach. RAG frameworks, eval/observability platforms, and single-purpose agents were routed to their own reports or excluded; only tools whose *primary* job is coordinating agents/steps appear here.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub. Re-run after a fresh `classified.json` to refresh.

<sub>Tools covered: 37 across 7 approaches · Snapshot: 2026-07-13T08:42:30.177Z</sub>
