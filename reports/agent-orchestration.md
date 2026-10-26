# AI Agent Orchestration — Landscape Report

> Derived from **kaiser-data**'s 2,415 starred repos (snapshot `2026-10-26T11:46:04.025Z`), cross-referenced with the repo-similarity graph (2,415 nodes / 8,024 edges, 43 communities).
>
> Generated 2026-10-26 by `scripts/reports/agent_orchestration.py` (regenerate any time — no API cost).

![Top tools by stars](assets/agent-orchestration-top-tools.svg)

![Tools per category](assets/agent-orchestration-categories.svg)


> **Orchestration** = coordinating multiple agents / tools / steps toward a goal: routing, planning, parallelism, hand-offs, state and recovery. The tools below differ mostly in **how you express that coordination** — in code, on a visual canvas, across coding agents, or as durable production infra.

## Executive summary

- **38 agent-orchestration tools** in your stars (**1,626,196★**), organized by *how you express coordination*:
  - **Code-first agent frameworks** (17): `MetaGPT`, `autogen`, `crewAI`, `langgraph`, `agno`, `dspy`, `agentscope`, `openai-agents-python`, `smolagents`, `semantic-kernel`, `adk-python`, `camel`, `agent-framework`, `voltagent`, `harness-sdk`, `beeai-framework`, `AutoAgents`
  - **Visual / low-code platforms** (4): `n8n`, `dify`, `langflow`, `sim`
  - **Coding-agent orchestration** (9): `deer-flow`, `ruflo`, `oh-my-openagent`, `agents`, `oh-my-claudecode`, `paseo`, `eigent`, `agent-orchestrator`, `coding-agent-template`
  - **Agent OS / long-horizon harness** (1): `eliza`
  - **Durable / production infra** (2): `flyte`, `agent-kit`
  - **Vertical / domain systems** (2): `TradingAgents`, `gpt-researcher`
  - **Protocols & meta-frameworks** (3): `ROMA`, `tinyagi`, `agent-workflow-protocol`
- **The split that matters:** *code-first frameworks* (langgraph, openai-agents, semantic-kernel) give you fine control in a programming language; *visual platforms* (n8n, dify) trade control for speed and non-engineer access; *coding-agent orchestration* (ruflo, agent-orchestrator) is a newer niche that runs **swarms of coding agents** in parallel.
- **Big-tech has entered:** Microsoft (agent-framework, semantic-kernel), Google (adk-python), OpenAI (openai-agents-python), AWS (strands-agents) all ship first-party frameworks — a strong maturity signal.
- **Highest-health picks:** `n8n`/`dify` (100), `strands-agents` (96), `microsoft/agent-framework` & `semantic-kernel` (92). `Flowise` used to sit in this band and was **archived upstream** in August 2026 — see *Retired from the scored set*.

## Pick by how you want to express coordination

| You want… | Use this approach | Top picks |
|---|---|---|
| Fine-grained control, in code | Code-first framework | `langgraph`, `openai-agents-python` |
| Fast builds / non-engineers | Visual / low-code | `n8n`, `dify` |
| Parallel **coding** agents | Coding-agent orchestration | `ruflo`, `OrchestratorInc/agent-orchestrator` |
| Always-on autonomous agents | Agent OS / harness | `elizaOS/eliza`, `deer-flow` |
| Durable, fault-tolerant prod | Production infra | `flyte`, `inngest/agent-kit` |
| A standard, not a library | Protocol / meta | `agent-workflow-protocol` |

## Comparison by approach

### Code-first agent frameworks

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 71,021 (▲17) | Python | 17 | stale | Declining | 0 |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 61,570 (▲22) | Python | 44 | active | Mature | 1 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 60,117 (▲53) | Python | 89 | very active | Classic | 3 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 43,924 (▲93) | Python | 83 | very active | Classic | 2 |
| [agno-agi/agno](https://github.com/agno-agi/agno) | 42,899 (▲21) | Python | 82 | very active | Classic | 2 |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | 38,797 (▲28) | Python | 78 | very active | Classic | 1 |
| [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | 34,147 (▲319) | Python | 97 | very active | Mature | 11 |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 30,293 (▲33) | Python | 85 | very active | Hot | 2 |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | 30,065 (▲36) | Python | 60 | active | Mature | 2 |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | 28,697 (▲3) | C# | 81 | very active | Classic | 2 |
| [google/adk-python](https://github.com/google/adk-python) | 22,012 (▲22) | Python | 99 | very active | Hot | 5 |
| [camel-ai/camel](https://github.com/camel-ai/camel) | 17,977 (▲13) | Python | 76 | very active | Classic | 2 |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | 14,320 (▲16) | Python | 98 | very active | Hot | 5 |
| [VoltAgent/voltagent](https://github.com/VoltAgent/voltagent) | 10,872 (▲8) | TypeScript | 71 | active | Mature | 2 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | 8,953 (▲12) | Python | 87 | very active | Hot | 3 |
| [i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework) | 3,443 | Python | 100 | very active | Mature | 6 |
| [liquidos-ai/AutoAgents](https://github.com/liquidos-ai/AutoAgents) | 768 (▲3) | Rust | 68 | active | Mature | 2 |

### Visual / low-code platforms

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 208,626 (▲134) | TypeScript | 100 | very active | Classic | 9 |
| [langgenius/dify](https://github.com/langgenius/dify) | 159,587 (▲158) | Python | 85 | very active | Classic | 2 |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 156,031 (▲49) | Python | 79 | very active | Classic | 1 |
| [simstudioai/sim](https://github.com/simstudioai/sim) | 29,921 (▲14) | TypeScript | 78 | very active | Mature | 1 |

### Coding-agent orchestration

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 84,439 (▲61) | Python | 87 | very active | Hot | 15 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 79,392 (▲426) | TypeScript | 77 | very active | Hot | 1 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 70,345 (▲36) | TypeScript | 77 | very active | Rising | 1 |
| [wshobson/agents](https://github.com/wshobson/agents) | 41,740 (▲111) | Python | 62 | very active | Hot | 1 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | 40,280 (▲49) | TypeScript | 80 | very active | Hot | 1 |
| [getpaseo/paseo](https://github.com/getpaseo/paseo) | 22,080 (▲207) | TypeScript | 77 | very active | Hot | 1 |
| [eigent-ai/eigent](https://github.com/eigent-ai/eigent) | 15,664 (▲11) | TypeScript | 78 | very active | Hot | 1 |
| [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | 13,674 (▲103) | Go | 93 | very active | Hot | 4 |
| [vercel-labs/coding-agent-template](https://github.com/vercel-labs/coding-agent-template) | 1,791 (▲1) | TypeScript | 29 | slowing | Declining | 0 |

### Agent OS / long-horizon harness

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [elizaOS/eliza](https://github.com/elizaOS/eliza) | 19,652 (▲7) | TypeScript | 80 | very active | Mature | 1 |

### Durable / production infra

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [flyteorg/flyte](https://github.com/flyteorg/flyte) | 7,762 (▲7) | Go | 80 | very active | Classic | 1 |
| [inngest/agent-kit](https://github.com/inngest/agent-kit) | 956 | TypeScript | 22 | slowing | Declining | 0 |

### Vertical / domain systems

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 115,250 (▲1,659) | Python | 78 | very active | Hot | 1 |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | 30,297 (▲20) | Python | 79 | very active | Classic | 1 |

### Protocols & meta-frameworks

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [sentient-agi/ROMA](https://github.com/sentient-agi/ROMA) | 5,187 (▲2) | Python | 17 | stale | Declining | 0 |
| [TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi) | 3,628 (▲2) | TypeScript | 33 | stale | Declining | 0 |
| [veegee82/agent-workflow-protocol](https://github.com/veegee82/agent-workflow-protocol) | 19 | Python | 21 | slowing | Declining | 0 |

## Details

### Code-first agent frameworks

_SDKs you write agents in — maximum control over routing, state and hand-offs; the engineer's default._

- **[FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT)** · 71,021★ · Python · Declining · health 17  
  Multi-agent 'software company' — assigns SOPs/roles (PM, architect, engineer).  
  <sub>topics: agent, gpt, llm, metagpt, multi-agent</sub>
- **[microsoft/autogen](https://github.com/microsoft/autogen)** · 61,570★ · Python · Mature · health 44  
  Microsoft's conversational multi-agent framework; agents talk to solve tasks.  
  <sub>topics: chatgpt, llm-agent, llm-framework, agentic, agentic-agi, agents</sub>
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** · 60,117★ · Python · Classic · health 89  
  Role-based 'crew' multi-agent framework — agents with roles, goals & tools collaborate.  
  <sub>topics: agents, ai, ai-agents, llms, aiagentframework</sub>
- **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** · 43,924★ · Python · Classic · health 83  
  Graph-based agent runtime — explicit nodes/edges/state; the de-facto control-flow framework.  
  <sub>topics: agents, ai, ai-agents, chatgpt, deepagents, enterprise</sub>
- **[agno-agi/agno](https://github.com/agno-agi/agno)** · 42,899★ · Python · Classic · health 82  
  Fast multimodal agent framework (ex-phidata) with memory/tools/teams.  
  <sub>topics: developer-tools, python, agents, ai, ai-agents</sub>
- **[stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)** · 38,797★ · Python · Classic · health 78  
  Programmatic prompt/pipeline optimization — compile agent behavior instead of hand-prompting.  
  <sub>topics: —</sub>
- **[agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)** · 34,147★ · Python · Mature · health 97  
  Build agents you can see/understand/trust; strong observability + multi-agent.  
  <sub>topics: agent, chatbot, large-language-models, llm, llm-agent, multi-agent</sub>
- **[openai/openai-agents-python](https://github.com/openai/openai-agents-python)** · 30,293★ · Python · Hot · health 85  
  Lightweight, powerful framework for multi-agent workflows; handoffs + guardrails + tracing.  
  <sub>topics: agents, ai, framework, llm, python, openai</sub>
- **[huggingface/smolagents](https://github.com/huggingface/smolagents)** · 30,065★ · Python · Mature · health 60  
  Minimalist code-agent framework — agents that write & run Python to act.  
  <sub>topics: —</sub>
- **[microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)** · 28,697★ · C# · Classic · health 81  
  Microsoft's enterprise SDK (C#/Python) for plugging LLMs + planning into apps.  
  <sub>topics: ai, artificial-intelligence, llm, openai, sdk</sub>
- **[google/adk-python](https://github.com/google/adk-python)** · 22,012★ · Python · Hot · health 99  
  Google's code-first Agent Development Kit — build, evaluate & deploy agents.  
  <sub>topics: agent, agents, agents-sdk, ai, ai-agents, multi-agent-systems</sub>
- **[camel-ai/camel](https://github.com/camel-ai/camel)** · 17,977★ · Python · Classic · health 76  
  Large multi-agent 'society' framework for studying agent cooperation at scale.  
  <sub>topics: ai-societies, artificial-intelligence, deep-learning, large-language-models, multi-agent-systems, natural-language-processing</sub>
- **[microsoft/agent-framework](https://github.com/microsoft/agent-framework)** · 14,320★ · Python · Hot · health 98  
  Microsoft's framework to build, orchestrate & deploy multi-agent workflows (health 92).  
  <sub>topics: agent-framework, agentic-ai, agents, ai, multi-agent, orchestration</sub>
- **[VoltAgent/voltagent](https://github.com/VoltAgent/voltagent)** · 10,872★ · TypeScript · Mature · health 71  
  TypeScript agent-engineering platform + open-source framework.  
  <sub>topics: agents, ai, chatbots, llm, mcp, nodejs</sub>
- **[strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)** · 8,953★ · Python · Hot · health 87  
  Model-driven agents in a few lines; very high health (96) and bus factor 7.  
  <sub>topics: agentic, agentic-ai, agents, ai, autonomous-agents, llm</sub>
- **[i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework)** · 3,443★ · Python · Mature · health 100  
  Production-ready agents in both Python and TypeScript.  
  <sub>topics: agents, ai, framework, ai-agent, llm, multiagent</sub>
- **[liquidos-ai/AutoAgents](https://github.com/liquidos-ai/AutoAgents)** · 768★ · Rust · Mature · health 68  
  Rust multi-agent framework to build, deploy & coordinate agents.  
  <sub>topics: agents, ai, ai-agents, ai-agents-framework, llm</sub>

### Visual / low-code platforms

_Drag-and-drop canvases — fastest to a working flow, accessible to non-engineers, less granular control._

- **[n8n-io/n8n](https://github.com/n8n-io/n8n)** · 208,626★ · TypeScript · Classic · health 100  
  Fair-code workflow automation with native AI nodes — the giant (189k★, health 100).  
  <sub>topics: automation, ipaas, n8n, workflow, typescript, self-hosted</sub>
- **[langgenius/dify](https://github.com/langgenius/dify)** · 159,587★ · Python · Classic · health 85  
  Production-ready platform for agentic workflow development (health 100).  
  <sub>topics: ai, gpt, llm, openai, python, agent</sub>
- **[langflow-ai/langflow](https://github.com/langflow-ai/langflow)** · 156,031★ · Python · Classic · health 79  
  Popular drag-and-drop builder for agents & flows; visual graph of components.  
  <sub>topics: react-flow, chatgpt, large-language-models, generative-ai, agents, multiagent</sub>
- **[simstudioai/sim](https://github.com/simstudioai/sim)** · 29,921★ · TypeScript · Mature · health 78  
  Build, deploy & orchestrate agents — 'central intelligence layer for your AI workforce'.  
  <sub>topics: agentic-workflow, agents, ai, nextjs, typescript, agent-workflow</sub>

### Coding-agent orchestration

_Coordinate *swarms of coding agents* (Claude Code, Codex, Cursor…) on a codebase — plan, spawn, run in parallel, handle CI._

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 84,439★ · Python · Hot · health 87  
  Long-horizon SuperAgent harness that researches, codes & creates with sandboxes (bf6).  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 79,392★ · TypeScript · Hot · health 77  
  Agent-orchestration platform for Claude — multi-agent swarms coordinating autonomous coding.  
  <sub>topics: swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 70,345★ · TypeScript · Rising · health 77  
  'omo' — agent harness (formerly oh-my-opencode) for coding workflows.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor</sub>
- **[wshobson/agents](https://github.com/wshobson/agents)** · 41,740★ · Python · Hot · health 62  
  Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor, OpenCode, Gemini).  
  <sub>topics: anthropic, agent-skills, agentic-ai, ai-agents, cursor, cursor-rules</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 40,280★ · TypeScript · Hot · health 80  
  Teams-first multi-agent orchestration for Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode</sub>
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 22,080★ · TypeScript · Hot · health 77  
  Run & coordinate coding agents from phone, desktop and CLI.  
  <sub>topics: agents, claude-code, codex, opencode, ade, copilot</sub>
- **[eigent-ai/eigent](https://github.com/eigent-ai/eigent)** · 15,664★ · TypeScript · Hot · health 78  
  Open-source cowork desktop — local/free multi-agent productivity workspace.  
  <sub>topics: agent-framework, agent-skills, agentic-ai, agentic-workflow, claude-cowork, claude-cowork-alternative</sub>
- **[OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator)** · 13,674★ · Go · Hot · health 93  
  Orchestrates parallel coding agents — plans tasks, spawns agents, handles CI autonomously.  
  <sub>topics: claude-code, codex-cli, orchestration, orchestrator, skills, agent-fleet</sub>
- **[vercel-labs/coding-agent-template](https://github.com/vercel-labs/coding-agent-template)** · 1,791★ · TypeScript · Declining · health 29  
  Multi-agent coding platform on Vercel Sandbox + AI Gateway; declining, verify first.  
  <sub>topics: —</sub>

### Agent OS / long-horizon harness

_Runtimes for always-on, long-running autonomous agents._

- **[elizaOS/eliza](https://github.com/elizaOS/eliza)** · 19,652★ · TypeScript · Mature · health 80  
  Open-source 'agentic operating system' — long-running autonomous agents.  
  <sub>topics: agent, agentic, ai, autonomous, chatbot, crypto</sub>

### Durable / production infra

_Fault-tolerant execution — retries, checkpointing, deterministic routing for production._

- **[flyteorg/flyte](https://github.com/flyteorg/flyte)** · 7,762★ · Go · Classic · health 80  
  Dynamic, resilient orchestration (Go/K8s) — coordinate data, models & compute durably.  
  <sub>topics: machine-learning, scale, workflow, mlops, python, agent-runtime</sub>
- **[inngest/agent-kit](https://github.com/inngest/agent-kit)** · 956★ · TypeScript · Declining · health 22  
  Build multi-agent networks in TS with deterministic routing + durable execution via MCP.  
  <sub>topics: agent, ai, ai-agent-framework, ai-agents, llm</sub>

### Vertical / domain systems

_Reference multi-agent architectures for a specific domain._

- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 115,250★ · Python · Hot · health 78  
  Multi-agent LLM framework for financial trading — a vertical reference architecture (79k★).  
  <sub>topics: agent, finance, llm, multiagent, trading</sub>
- **[assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)** · 30,297★ · Python · Classic · health 79  
  Autonomous research agent that plans, searches & writes cited reports.  
  <sub>topics: ai, python, agent, automation, research, search</sub>

### Protocols & meta-frameworks

_Standards and meta-layers above any single framework._

- **[sentient-agi/ROMA](https://github.com/sentient-agi/ROMA)** · 5,187★ · Python · Declining · health 17  
  Recursive meta-agent framework to build multi-agent systems; declining/low health.  
  <sub>topics: —</sub>
- **[TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi)** · 3,628★ · TypeScript · Declining · health 33  
  Agent-teams orchestrator aimed at one-person companies.  
  <sub>topics: —</sub>
- **[veegee82/agent-workflow-protocol](https://github.com/veegee82/agent-workflow-protocol)** · 19★ · Python · Declining · health 21  
  Open standard for multi-agent workflows — scripted pipelines to self-organizing teams.  
  <sub>topics: agentic, agentic-ai, agentic-ai-development, agentic-engineering, agentic-framework, agentic-workflow</sub>

## Graph analysis — how they relate

**Community clustering.** These 38 tools span **14 of the graph's 43 communities**.

- **Community 11** (10): `agentscope-ai/agentscope`, `liquidos-ai/AutoAgents`, `crewAIInc/crewAI`, `agno-agi/agno`, `langgenius/dify`, `code-yeongyu/oh-my-openagent`, `ruvnet/ruflo`, `eigent-ai/eigent`, `flyteorg/flyte`, `inngest/agent-kit`
- **Community 36** (4): `langchain-ai/langgraph`, `VoltAgent/voltagent`, `i-am-bee/beeai-framework`, `langflow-ai/langflow`
- **Community 12** (3): `microsoft/semantic-kernel`, `microsoft/agent-framework`, `microsoft/autogen`
- **Community 0** (3): `stanfordnlp/dspy`, `sentient-agi/ROMA`, `TinyAGI/tinyagi`
- **Community 2** (3): `assafelovic/gpt-researcher`, `wshobson/agents`, `Yeachan-Heo/oh-my-claudecode`
- **Community 7** (2): `openai/openai-agents-python`, `camel-ai/camel`
- **Community 27** (2): `strands-agents/harness-sdk`, `vercel-labs/coding-agent-template`
- **Community 6** (2): `FoundationAgents/MetaGPT`, `TauricResearch/TradingAgents`
- **Community 20** (2): `simstudioai/sim`, `elizaOS/eliza`
- **Community 32** (2): `bytedance/deer-flow`, `veegee82/agent-workflow-protocol`
- **Community 3** (2): `OrchestratorInc/agent-orchestrator`, `getpaseo/paseo`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' orchestration tools in your ecosystem:

- `openai/openai-agents-python` — PageRank 0.0016
- `langchain-ai/langgraph` — PageRank 0.0013
- `liquidos-ai/AutoAgents` — PageRank 0.0012
- `huggingface/smolagents` — PageRank 0.0012
- `agno-agi/agno` — PageRank 0.0011
- `microsoft/semantic-kernel` — PageRank 0.0009
- `strands-agents/harness-sdk` — PageRank 0.0008
- `inngest/agent-kit` — PageRank 0.0007
- `langgenius/dify` — PageRank 0.0007
- `crewAIInc/crewAI` — PageRank 0.0007

**Direct links between orchestration tools** (top similarity edges where both endpoints are in this report):

- `microsoft/agent-framework` ⇄ `microsoft/semantic-kernel` (w=0.995) — topics: ai, sdk; authors: dependabot[bot], eavanvalkenburg, westey-m
- `microsoft/autogen` ⇄ `microsoft/agent-framework` (w=0.720) — topics: agents, ai; authors: westey-m
- `microsoft/autogen` ⇄ `microsoft/semantic-kernel` (w=0.714) — topics: ai; authors: westey-m
- `i-am-bee/beeai-framework` ⇄ `openai/openai-agents-python` (w=0.551) — topics: agents, ai, framework, llm; authors: dependabot[bot]
- `agno-agi/agno` ⇄ `crewAIInc/crewAI` (w=0.518) — topics: agents, ai, ai-agents; authors: RaycarlLei
- `agno-agi/agno` ⇄ `liquidos-ai/AutoAgents` (w=0.429) — topics: agents, ai, ai-agents
- `crewAIInc/crewAI` ⇄ `liquidos-ai/AutoAgents` (w=0.429) — topics: agents, ai, ai-agents
- `liquidos-ai/AutoAgents` ⇄ `inngest/agent-kit` (w=0.429) — topics: ai, ai-agents, llm
- `langchain-ai/langgraph` ⇄ `i-am-bee/beeai-framework` (w=0.378) — topics: agents, ai, framework, llm; authors: dependabot[bot]
- `FoundationAgents/MetaGPT` ⇄ `TauricResearch/TradingAgents` (w=0.300) — topics: agent, llm
- `simstudioai/sim` ⇄ `langgenius/dify` (w=0.276) — topics: agentic-workflow, ai, nextjs, deepseek
- `strands-agents/harness-sdk` ⇄ `ruvnet/ruflo` (w=0.268) — topics: agentic-ai, agents, autonomous-agents, multi-agent-systems; authors: dependabot[bot]
- `FoundationAgents/MetaGPT` ⇄ `agentscope-ai/agentscope` (w=0.264) — topics: agent, llm, multi-agent
- `langflow-ai/langflow` ⇄ `langchain-ai/langgraph` (w=0.250) — topics: chatgpt, generative-ai, agents, multiagent
- `veegee82/agent-workflow-protocol` ⇄ `google/adk-python` (w=0.217) — topics: agentic, agentic-ai, agents, llms
- …and 2 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Orchestration is load-bearing — weigh this heavily before standardizing on one.

| Tool | Approach | Health | Lifecycle | Activity | Bus factor |
|---|---|---|---|---|---|
| i-am-bee/beeai-framework | Code-first agent frameworks | 100 | Mature | very active | 6 |
| n8n-io/n8n | Visual / low-code platforms | 100 | Classic | very active | 9 |
| google/adk-python | Code-first agent frameworks | 99 | Hot | very active | 5 |
| microsoft/agent-framework | Code-first agent frameworks | 98 | Hot | very active | 5 |
| agentscope-ai/agentscope | Code-first agent frameworks | 97 | Mature | very active | 11 |
| OrchestratorInc/agent-orchestrator | Coding-agent orchestration | 93 | Hot | very active | 4 |
| crewAIInc/crewAI | Code-first agent frameworks | 89 | Classic | very active | 3 |
| strands-agents/harness-sdk | Code-first agent frameworks | 87 | Hot | very active | 3 |
| bytedance/deer-flow | Coding-agent orchestration | 87 | Hot | very active | 15 |
| openai/openai-agents-python | Code-first agent frameworks | 85 | Hot | very active | 2 |
| langgenius/dify | Visual / low-code platforms | 85 | Classic | very active | 2 |
| langchain-ai/langgraph | Code-first agent frameworks | 83 | Classic | very active | 2 |
| agno-agi/agno | Code-first agent frameworks | 82 | Classic | very active | 2 |
| microsoft/semantic-kernel | Code-first agent frameworks | 81 | Classic | very active | 2 |
| Yeachan-Heo/oh-my-claudecode | Coding-agent orchestration | 80 | Hot | very active | 1 |
| elizaOS/eliza | Agent OS / long-horizon harness | 80 | Mature | very active | 1 |
| flyteorg/flyte | Durable / production infra | 80 | Classic | very active | 1 |
| assafelovic/gpt-researcher | Vertical / domain systems | 79 | Classic | very active | 1 |
| langflow-ai/langflow | Visual / low-code platforms | 79 | Classic | very active | 1 |
| stanfordnlp/dspy | Code-first agent frameworks | 78 | Classic | very active | 1 |
| simstudioai/sim | Visual / low-code platforms | 78 | Mature | very active | 1 |
| eigent-ai/eigent | Coding-agent orchestration | 78 | Hot | very active | 1 |
| TauricResearch/TradingAgents | Vertical / domain systems | 78 | Hot | very active | 1 |
| code-yeongyu/oh-my-openagent | Coding-agent orchestration | 77 | Rising | very active | 1 |
| ruvnet/ruflo | Coding-agent orchestration | 77 | Hot | very active | 1 |
| getpaseo/paseo | Coding-agent orchestration | 77 | Hot | very active | 1 |
| camel-ai/camel | Code-first agent frameworks | 76 | Classic | very active | 2 |
| VoltAgent/voltagent | Code-first agent frameworks | 71 | Mature | active | 2 |
| liquidos-ai/AutoAgents | Code-first agent frameworks | 68 | Mature | active | 2 |
| wshobson/agents | Coding-agent orchestration | 62 | Hot | very active | 1 |
| huggingface/smolagents | Code-first agent frameworks | 60 | Mature | active | 2 |
| microsoft/autogen | Code-first agent frameworks | 44 | Mature | active | 1 |
| TinyAGI/tinyagi | Protocols & meta-frameworks | 33 | Declining | stale | 0 |
| vercel-labs/coding-agent-template | Coding-agent orchestration | 29 | Declining | slowing | 0 |
| inngest/agent-kit | Durable / production infra | 22 | Declining | slowing | 0 |
| veegee82/agent-workflow-protocol | Protocols & meta-frameworks | 21 | Declining | slowing | 0 |
| FoundationAgents/MetaGPT | Code-first agent frameworks | 17 | Declining | stale | 0 |
| sentient-agi/ROMA | Protocols & meta-frameworks | 17 | Declining | stale | 0 |

⚠️ **Adopt with caution** (low health and/or declining): `FoundationAgents/MetaGPT`, `sentient-agi/ROMA`, `veegee82/agent-workflow-protocol`, `inngest/agent-kit`, `vercel-labs/coding-agent-template`, `TinyAGI/tinyagi`, `microsoft/autogen`.

## Coverage

Your stars now cover the canonical orchestration frameworks (crewAI, AutoGen, LangGraph, langflow, semantic-kernel, ADK, agentscope, …) — no major gaps left in this category.

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: scan for orchestration / multi-agent / swarm / workflow / agent-framework signals, then manual curation by approach. RAG frameworks, eval/observability platforms, and single-purpose agents were routed to their own reports or excluded; only tools whose *primary* job is coordinating agents/steps appear here.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub. Re-run after a fresh `classified.json` to refresh.

### Retired from the scored set

Archived upstream, so they no longer appear in this report's tables — `sample.mjs` excludes archived repos. Metrics are frozen at the date shown and are not refreshed.

| Project | Category | Why it left | Metrics as of |
|---|---|---|---|
| [`FlowiseAI/Flowise`](https://github.com/FlowiseAI/Flowise) | Visual / low-code platforms | Archived upstream; last in the dataset 2026-08-11. Build AI agents visually; popular drag-and-drop builder. | 2026-08-11 |

<sub>Tools covered: 38 across 7 approaches · Snapshot: 2026-10-26T11:46:04.025Z</sub>
