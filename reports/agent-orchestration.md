# AI Agent Orchestration — Landscape Report

> Derived from **kaiser-data**'s 2,159 starred repos (snapshot `2026-09-14T11:08:08.535Z`), cross-referenced with the repo-similarity graph (2,159 nodes / 7,086 edges, 37 communities).
>
> Generated 2026-09-14 by `scripts/reports/agent_orchestration.py` (regenerate any time — no API cost).

![Top tools by stars](assets/agent-orchestration-top-tools.svg)

![Tools per category](assets/agent-orchestration-categories.svg)


> **Orchestration** = coordinating multiple agents / tools / steps toward a goal: routing, planning, parallelism, hand-offs, state and recovery. The tools below differ mostly in **how you express that coordination** — in code, on a visual canvas, across coding agents, or as durable production infra.

## Executive summary

- **38 agent-orchestration tools** in your stars (**1,570,157★**), organized by *how you express coordination*:
  - **Code-first agent frameworks** (17): `MetaGPT`, `autogen`, `crewAI`, `agno`, `langgraph`, `dspy`, `agentscope`, `openai-agents-python`, `smolagents`, `semantic-kernel`, `adk-python`, `camel`, `agent-framework`, `voltagent`, `harness-sdk`, `beeai-framework`, `AutoAgents`
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
| Parallel **coding** agents | Coding-agent orchestration | `ruflo`, `Untrivial-ai/agent-orchestrator` |
| Always-on autonomous agents | Agent OS / harness | `elizaOS/eliza`, `deer-flow` |
| Durable, fault-tolerant prod | Production infra | `flyte`, `inngest/agent-kit` |
| A standard, not a library | Protocol / meta | `agent-workflow-protocol` |

## Comparison by approach

### Code-first agent frameworks

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 70,370 (▲136) | Python | 20 | stale | Declining | 0 |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 60,979 (▲148) | Python | 28 | slowing | Mature | 0 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 58,514 (▲378) | Python | 84 | very active | Mature | 2 |
| [agno-agi/agno](https://github.com/agno-agi/agno) | 42,163 (▲95) | Python | 93 | very active | Classic | 4 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 41,611 (▲500) | Python | 76 | very active | Classic | 1 |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | 38,006 (▲210) | Python | 83 | very active | Classic | 2 |
| [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | 31,617 (▲792) | Python | 88 | very active | Mature | 3 |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 29,417 (▲202) | Python | 85 | very active | Hot | 2 |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | 29,320 (▲136) | Python | 55 | active | Mature | 1 |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | 28,556 (▲19) | C# | 82 | very active | Classic | 2 |
| [google/adk-python](https://github.com/google/adk-python) | 21,529 (▲107) | Python | 84 | very active | Hot | 2 |
| [camel-ai/camel](https://github.com/camel-ai/camel) | 17,713 (▲40) | Python | 85 | very active | Classic | 3 |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | 13,509 (▲157) | Python | 88 | very active | Hot | 3 |
| [VoltAgent/voltagent](https://github.com/VoltAgent/voltagent) | 10,611 (▲56) | TypeScript | 75 | very active | Hot | 2 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | 7,238 (▲75) | Python | 92 | very active | Hot | 4 |
| [i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework) | 3,399 (▲9) | Python | 96 | very active | Mature | 5 |
| [liquidos-ai/AutoAgents](https://github.com/liquidos-ai/AutoAgents) | 750 (▲5) | Rust | 67 | very active | Hot | 1 |

### Visual / low-code platforms

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 204,240 (▲735) | TypeScript | 100 | very active | Classic | 9 |
| [langgenius/dify](https://github.com/langgenius/dify) | 155,674 (▲1,099) | TypeScript | 95 | very active | Classic | 4 |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 154,779 (▲468) | Python | 79 | very active | Classic | 1 |
| [simstudioai/sim](https://github.com/simstudioai/sim) | 29,628 (▲71) | TypeScript | 78 | very active | Hot | 1 |

### Coding-agent orchestration

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 82,408 (▲954) | Python | 84 | very active | Hot | 8 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 72,387 (▲1,604) | TypeScript | 76 | very active | Hot | 1 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 69,029 (▲290) | TypeScript | 78 | very active | Rising | 1 |
| [wshobson/agents](https://github.com/wshobson/agents) | 39,640 (▲190) | Python | 64 | very active | Hot | 1 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | 39,149 (▲119) | TypeScript | 80 | very active | Hot | 1 |
| [getpaseo/paseo](https://github.com/getpaseo/paseo) | 17,227 (▲1,069) | TypeScript | 77 | very active | Hot | 1 |
| [eigent-ai/eigent](https://github.com/eigent-ai/eigent) | 15,273 (▲78) | TypeScript | 79 | very active | Hot | 2 |
| [Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) | 12,004 (▲1,021) | Go | 98 | very active | Hot | 7 |
| [vercel-labs/coding-agent-template](https://github.com/vercel-labs/coding-agent-template) | 1,782 (▲4) | TypeScript | 33 | active | Declining | 0 |

### Agent OS / long-horizon harness

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [elizaOS/eliza](https://github.com/elizaOS/eliza) | 19,332 (▲71) | TypeScript | 79 | very active | Mature | 1 |

### Durable / production infra

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [flyteorg/flyte](https://github.com/flyteorg/flyte) | 7,487 (▲80) | Go | 85 | very active | Classic | 2 |
| [inngest/agent-kit](https://github.com/inngest/agent-kit) | 928 (▲2) | TypeScript | 39 | slowing | Declining | 0 |

### Vertical / domain systems

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 105,629 (▲2,980) | Python | 72 | very active | Mature | 1 |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | 29,445 (▲137) | Python | 82 | very active | Classic | 2 |

### Protocols & meta-frameworks

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [sentient-agi/ROMA](https://github.com/sentient-agi/ROMA) | 5,181 (▲3) | Python | 22 | stale | Declining | 0 |
| [TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi) | 3,614 (▲3) | TypeScript | 36 | slowing | Declining | 0 |
| [veegee82/agent-workflow-protocol](https://github.com/veegee82/agent-workflow-protocol) | 19 | Python | 25 | slowing | Declining | 0 |

## Details

### Code-first agent frameworks

_SDKs you write agents in — maximum control over routing, state and hand-offs; the engineer's default._

- **[FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT)** · 70,370★ · Python · Declining · health 20  
  Multi-agent 'software company' — assigns SOPs/roles (PM, architect, engineer).  
  <sub>topics: agent, gpt, llm, metagpt, multi-agent</sub>
- **[microsoft/autogen](https://github.com/microsoft/autogen)** · 60,979★ · Python · Mature · health 28  
  Microsoft's conversational multi-agent framework; agents talk to solve tasks.  
  <sub>topics: chatgpt, llm-agent, llm-framework, agentic, agentic-agi, agents</sub>
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** · 58,514★ · Python · Mature · health 84  
  Role-based 'crew' multi-agent framework — agents with roles, goals & tools collaborate.  
  <sub>topics: agents, ai, ai-agents, llms, aiagentframework</sub>
- **[agno-agi/agno](https://github.com/agno-agi/agno)** · 42,163★ · Python · Classic · health 93  
  Fast multimodal agent framework (ex-phidata) with memory/tools/teams.  
  <sub>topics: developer-tools, python, agents, ai, ai-agents</sub>
- **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** · 41,611★ · Python · Classic · health 76  
  Graph-based agent runtime — explicit nodes/edges/state; the de-facto control-flow framework.  
  <sub>topics: agents, ai, ai-agents, chatgpt, deepagents, enterprise</sub>
- **[stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)** · 38,006★ · Python · Classic · health 83  
  Programmatic prompt/pipeline optimization — compile agent behavior instead of hand-prompting.  
  <sub>topics: —</sub>
- **[agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)** · 31,617★ · Python · Mature · health 88  
  Build agents you can see/understand/trust; strong observability + multi-agent.  
  <sub>topics: agent, chatbot, large-language-models, llm, llm-agent, multi-agent</sub>
- **[openai/openai-agents-python](https://github.com/openai/openai-agents-python)** · 29,417★ · Python · Hot · health 85  
  Lightweight, powerful framework for multi-agent workflows; handoffs + guardrails + tracing.  
  <sub>topics: agents, ai, framework, llm, python, openai</sub>
- **[huggingface/smolagents](https://github.com/huggingface/smolagents)** · 29,320★ · Python · Mature · health 55  
  Minimalist code-agent framework — agents that write & run Python to act.  
  <sub>topics: —</sub>
- **[microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)** · 28,556★ · C# · Classic · health 82  
  Microsoft's enterprise SDK (C#/Python) for plugging LLMs + planning into apps.  
  <sub>topics: ai, artificial-intelligence, llm, openai, sdk</sub>
- **[google/adk-python](https://github.com/google/adk-python)** · 21,529★ · Python · Hot · health 84  
  Google's code-first Agent Development Kit — build, evaluate & deploy agents.  
  <sub>topics: agent, agents, agents-sdk, ai, ai-agents, multi-agent-systems</sub>
- **[camel-ai/camel](https://github.com/camel-ai/camel)** · 17,713★ · Python · Classic · health 85  
  Large multi-agent 'society' framework for studying agent cooperation at scale.  
  <sub>topics: ai-societies, artificial-intelligence, deep-learning, large-language-models, multi-agent-systems, natural-language-processing</sub>
- **[microsoft/agent-framework](https://github.com/microsoft/agent-framework)** · 13,509★ · Python · Hot · health 88  
  Microsoft's framework to build, orchestrate & deploy multi-agent workflows (health 92).  
  <sub>topics: agent-framework, agentic-ai, agents, ai, multi-agent, orchestration</sub>
- **[VoltAgent/voltagent](https://github.com/VoltAgent/voltagent)** · 10,611★ · TypeScript · Hot · health 75  
  TypeScript agent-engineering platform + open-source framework.  
  <sub>topics: agents, ai, chatbots, llm, mcp, nodejs</sub>
- **[strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)** · 7,238★ · Python · Hot · health 92  
  Model-driven agents in a few lines; very high health (96) and bus factor 7.  
  <sub>topics: agentic, agentic-ai, agents, ai, autonomous-agents, llm</sub>
- **[i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework)** · 3,399★ · Python · Mature · health 96  
  Production-ready agents in both Python and TypeScript.  
  <sub>topics: agents, ai, framework, ai-agent, llm, multiagent</sub>
- **[liquidos-ai/AutoAgents](https://github.com/liquidos-ai/AutoAgents)** · 750★ · Rust · Hot · health 67  
  Rust multi-agent framework to build, deploy & coordinate agents.  
  <sub>topics: agents, ai, ai-agents, ai-agents-framework, llm</sub>

### Visual / low-code platforms

_Drag-and-drop canvases — fastest to a working flow, accessible to non-engineers, less granular control._

- **[n8n-io/n8n](https://github.com/n8n-io/n8n)** · 204,240★ · TypeScript · Classic · health 100  
  Fair-code workflow automation with native AI nodes — the giant (189k★, health 100).  
  <sub>topics: automation, ipaas, n8n, workflow, typescript, self-hosted</sub>
- **[langgenius/dify](https://github.com/langgenius/dify)** · 155,674★ · TypeScript · Classic · health 95  
  Production-ready platform for agentic workflow development (health 100).  
  <sub>topics: ai, gpt, llm, openai, python, agent</sub>
- **[langflow-ai/langflow](https://github.com/langflow-ai/langflow)** · 154,779★ · Python · Classic · health 79  
  Popular drag-and-drop builder for agents & flows; visual graph of components.  
  <sub>topics: react-flow, chatgpt, large-language-models, generative-ai, agents, multiagent</sub>
- **[simstudioai/sim](https://github.com/simstudioai/sim)** · 29,628★ · TypeScript · Hot · health 78  
  Build, deploy & orchestrate agents — 'central intelligence layer for your AI workforce'.  
  <sub>topics: agentic-workflow, agents, ai, nextjs, typescript, agent-workflow</sub>

### Coding-agent orchestration

_Coordinate *swarms of coding agents* (Claude Code, Codex, Cursor…) on a codebase — plan, spawn, run in parallel, handle CI._

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 82,408★ · Python · Hot · health 84  
  Long-horizon SuperAgent harness that researches, codes & creates with sandboxes (bf6).  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 72,387★ · TypeScript · Hot · health 76  
  Agent-orchestration platform for Claude — multi-agent swarms coordinating autonomous coding.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 69,029★ · TypeScript · Rising · health 78  
  'omo' — agent harness (formerly oh-my-opencode) for coding workflows.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor</sub>
- **[wshobson/agents](https://github.com/wshobson/agents)** · 39,640★ · Python · Hot · health 64  
  Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor, OpenCode, Gemini).  
  <sub>topics: anthropic, agent-skills, agentic-ai, ai-agents, cursor, cursor-rules</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 39,149★ · TypeScript · Hot · health 80  
  Teams-first multi-agent orchestration for Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode</sub>
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 17,227★ · TypeScript · Hot · health 77  
  Run & coordinate coding agents from phone, desktop and CLI.  
  <sub>topics: agents, claude-code, codex, opencode, ade, copilot</sub>
- **[eigent-ai/eigent](https://github.com/eigent-ai/eigent)** · 15,273★ · TypeScript · Hot · health 79  
  Open-source cowork desktop — local/free multi-agent productivity workspace.  
  <sub>topics: agent-framework, agent-skills, agentic-ai, agentic-workflow, claude-cowork, claude-cowork-alternative</sub>
- **[Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator)** · 12,004★ · Go · Hot · health 98  
  Orchestrates parallel coding agents — plans tasks, spawns agents, handles CI autonomously.  
  <sub>topics: claude-code, codex-cli, orchestration, orchestrator, skills, agent-fleet</sub>
- **[vercel-labs/coding-agent-template](https://github.com/vercel-labs/coding-agent-template)** · 1,782★ · TypeScript · Declining · health 33  
  Multi-agent coding platform on Vercel Sandbox + AI Gateway; declining, verify first.  
  <sub>topics: —</sub>

### Agent OS / long-horizon harness

_Runtimes for always-on, long-running autonomous agents._

- **[elizaOS/eliza](https://github.com/elizaOS/eliza)** · 19,332★ · TypeScript · Mature · health 79  
  Open-source 'agentic operating system' — long-running autonomous agents.  
  <sub>topics: agent, agentic, ai, autonomous, chatbot, crypto</sub>

### Durable / production infra

_Fault-tolerant execution — retries, checkpointing, deterministic routing for production._

- **[flyteorg/flyte](https://github.com/flyteorg/flyte)** · 7,487★ · Go · Classic · health 85  
  Dynamic, resilient orchestration (Go/K8s) — coordinate data, models & compute durably.  
  <sub>topics: flyte, machine-learning, golang, scale, workflow, data-science</sub>
- **[inngest/agent-kit](https://github.com/inngest/agent-kit)** · 928★ · TypeScript · Declining · health 39  
  Build multi-agent networks in TS with deterministic routing + durable execution via MCP.  
  <sub>topics: agent, ai, ai-agent-framework, ai-agents, llm</sub>

### Vertical / domain systems

_Reference multi-agent architectures for a specific domain._

- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 105,629★ · Python · Mature · health 72  
  Multi-agent LLM framework for financial trading — a vertical reference architecture (79k★).  
  <sub>topics: agent, finance, llm, multiagent, trading</sub>
- **[assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)** · 29,445★ · Python · Classic · health 82  
  Autonomous research agent that plans, searches & writes cited reports.  
  <sub>topics: ai, python, agent, automation, research, search</sub>

### Protocols & meta-frameworks

_Standards and meta-layers above any single framework._

- **[sentient-agi/ROMA](https://github.com/sentient-agi/ROMA)** · 5,181★ · Python · Declining · health 22  
  Recursive meta-agent framework to build multi-agent systems; declining/low health.  
  <sub>topics: —</sub>
- **[TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi)** · 3,614★ · TypeScript · Declining · health 36  
  Agent-teams orchestrator aimed at one-person companies.  
  <sub>topics: —</sub>
- **[veegee82/agent-workflow-protocol](https://github.com/veegee82/agent-workflow-protocol)** · 19★ · Python · Declining · health 25  
  Open standard for multi-agent workflows — scripted pipelines to self-organizing teams.  
  <sub>topics: agentic, agentic-ai, agentic-ai-development, agentic-engineering, agentic-framework, agentic-workflow</sub>

## Graph analysis — how they relate

**Community clustering.** These 38 tools span **14 of the graph's 37 communities**.

- **Community 3** (10): `langchain-ai/langgraph`, `VoltAgent/voltagent`, `i-am-bee/beeai-framework`, `liquidos-ai/AutoAgents`, `crewAIInc/crewAI`, `agno-agi/agno`, `n8n-io/n8n`, `langflow-ai/langflow`, `flyteorg/flyte`, `inngest/agent-kit`
- **Community 16** (8): `langgenius/dify`, `simstudioai/sim`, `code-yeongyu/oh-my-openagent`, `ruvnet/ruflo`, `Yeachan-Heo/oh-my-claudecode`, `Untrivial-ai/agent-orchestrator`, `getpaseo/paseo`, `elizaOS/eliza`
- **Community 24** (4): `FoundationAgents/MetaGPT`, `camel-ai/camel`, `eigent-ai/eigent`, `TauricResearch/TradingAgents`
- **Community 4** (3): `microsoft/semantic-kernel`, `microsoft/agent-framework`, `microsoft/autogen`
- **Community 7** (2): `google/adk-python`, `veegee82/agent-workflow-protocol`
- **Community 0** (2): `agentscope-ai/agentscope`, `sentient-agi/ROMA`
- **Community 19** (2): `stanfordnlp/dspy`, `wshobson/agents`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' orchestration tools in your ecosystem:

- `langchain-ai/langgraph` — PageRank 0.0015
- `agno-agi/agno` — PageRank 0.0013
- `microsoft/semantic-kernel` — PageRank 0.0013
- `liquidos-ai/AutoAgents` — PageRank 0.0012
- `huggingface/smolagents` — PageRank 0.0012
- `crewAIInc/crewAI` — PageRank 0.0010
- `inngest/agent-kit` — PageRank 0.0010
- `openai/openai-agents-python` — PageRank 0.0009
- `agentscope-ai/agentscope` — PageRank 0.0009
- `VoltAgent/voltagent` — PageRank 0.0008

**Direct links between orchestration tools** (top similarity edges where both endpoints are in this report):

- `microsoft/agent-framework` ⇄ `microsoft/semantic-kernel` (w=1.254) — topics: ai, sdk; authors: eavanvalkenburg, baywet, dependabot[bot]
- `microsoft/autogen` ⇄ `microsoft/agent-framework` (w=0.661) — topics: agents, ai
- `i-am-bee/beeai-framework` ⇄ `openai/openai-agents-python` (w=0.540) — topics: agents, ai, framework, llm; authors: dependabot[bot]
- `agno-agi/agno` ⇄ `crewAIInc/crewAI` (w=0.533) — topics: agents, ai, ai-agents; authors: Ghraven, Shxiao101
- `agno-agi/agno` ⇄ `liquidos-ai/AutoAgents` (w=0.429) — topics: agents, ai, ai-agents
- `crewAIInc/crewAI` ⇄ `liquidos-ai/AutoAgents` (w=0.429) — topics: agents, ai, ai-agents
- `liquidos-ai/AutoAgents` ⇄ `inngest/agent-kit` (w=0.429) — topics: ai, ai-agents, llm
- `langchain-ai/langgraph` ⇄ `i-am-bee/beeai-framework` (w=0.381) — topics: agents, ai, framework, llm; authors: dependabot[bot]
- `bytedance/deer-flow` ⇄ `strands-agents/harness-sdk` (w=0.336) — topics: agentic, ai, ai-agents, llm; authors: BlueX888, dependabot[bot]
- `simstudioai/sim` ⇄ `langgenius/dify` (w=0.326) — topics: agentic-workflow, ai, nextjs, deepseek
- `FoundationAgents/MetaGPT` ⇄ `TauricResearch/TradingAgents` (w=0.300) — topics: agent, llm
- `FoundationAgents/MetaGPT` ⇄ `agentscope-ai/agentscope` (w=0.264) — topics: agent, llm, multi-agent
- `langflow-ai/langflow` ⇄ `langchain-ai/langgraph` (w=0.250) — topics: chatgpt, generative-ai, agents, multiagent
- `langgenius/dify` ⇄ `n8n-io/n8n` (w=0.232) — topics: ai, workflow, automation, low-code
- `camel-ai/camel` ⇄ `agentscope-ai/agentscope` (w=0.219) — topics: large-language-models, agent; authors: AmirF194, helloJamest
- …and 4 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Orchestration is load-bearing — weigh this heavily before standardizing on one.

| Tool | Approach | Health | Lifecycle | Activity | Bus factor |
|---|---|---|---|---|---|
| n8n-io/n8n | Visual / low-code platforms | 100 | Classic | very active | 9 |
| Untrivial-ai/agent-orchestrator | Coding-agent orchestration | 98 | Hot | very active | 7 |
| i-am-bee/beeai-framework | Code-first agent frameworks | 96 | Mature | very active | 5 |
| langgenius/dify | Visual / low-code platforms | 95 | Classic | very active | 4 |
| agno-agi/agno | Code-first agent frameworks | 93 | Classic | very active | 4 |
| strands-agents/harness-sdk | Code-first agent frameworks | 92 | Hot | very active | 4 |
| agentscope-ai/agentscope | Code-first agent frameworks | 88 | Mature | very active | 3 |
| microsoft/agent-framework | Code-first agent frameworks | 88 | Hot | very active | 3 |
| openai/openai-agents-python | Code-first agent frameworks | 85 | Hot | very active | 2 |
| camel-ai/camel | Code-first agent frameworks | 85 | Classic | very active | 3 |
| flyteorg/flyte | Durable / production infra | 85 | Classic | very active | 2 |
| google/adk-python | Code-first agent frameworks | 84 | Hot | very active | 2 |
| crewAIInc/crewAI | Code-first agent frameworks | 84 | Mature | very active | 2 |
| bytedance/deer-flow | Coding-agent orchestration | 84 | Hot | very active | 8 |
| stanfordnlp/dspy | Code-first agent frameworks | 83 | Classic | very active | 2 |
| microsoft/semantic-kernel | Code-first agent frameworks | 82 | Classic | very active | 2 |
| assafelovic/gpt-researcher | Vertical / domain systems | 82 | Classic | very active | 2 |
| Yeachan-Heo/oh-my-claudecode | Coding-agent orchestration | 80 | Hot | very active | 1 |
| langflow-ai/langflow | Visual / low-code platforms | 79 | Classic | very active | 1 |
| eigent-ai/eigent | Coding-agent orchestration | 79 | Hot | very active | 2 |
| elizaOS/eliza | Agent OS / long-horizon harness | 79 | Mature | very active | 1 |
| simstudioai/sim | Visual / low-code platforms | 78 | Hot | very active | 1 |
| code-yeongyu/oh-my-openagent | Coding-agent orchestration | 78 | Rising | very active | 1 |
| getpaseo/paseo | Coding-agent orchestration | 77 | Hot | very active | 1 |
| langchain-ai/langgraph | Code-first agent frameworks | 76 | Classic | very active | 1 |
| ruvnet/ruflo | Coding-agent orchestration | 76 | Hot | very active | 1 |
| VoltAgent/voltagent | Code-first agent frameworks | 75 | Hot | very active | 2 |
| TauricResearch/TradingAgents | Vertical / domain systems | 72 | Mature | very active | 1 |
| liquidos-ai/AutoAgents | Code-first agent frameworks | 67 | Hot | very active | 1 |
| wshobson/agents | Coding-agent orchestration | 64 | Hot | very active | 1 |
| huggingface/smolagents | Code-first agent frameworks | 55 | Mature | active | 1 |
| inngest/agent-kit | Durable / production infra | 39 | Declining | slowing | 0 |
| TinyAGI/tinyagi | Protocols & meta-frameworks | 36 | Declining | slowing | 0 |
| vercel-labs/coding-agent-template | Coding-agent orchestration | 33 | Declining | active | 0 |
| microsoft/autogen | Code-first agent frameworks | 28 | Mature | slowing | 0 |
| veegee82/agent-workflow-protocol | Protocols & meta-frameworks | 25 | Declining | slowing | 0 |
| sentient-agi/ROMA | Protocols & meta-frameworks | 22 | Declining | stale | 0 |
| FoundationAgents/MetaGPT | Code-first agent frameworks | 20 | Declining | stale | 0 |

⚠️ **Adopt with caution** (low health and/or declining): `FoundationAgents/MetaGPT`, `sentient-agi/ROMA`, `veegee82/agent-workflow-protocol`, `microsoft/autogen`, `vercel-labs/coding-agent-template`, `TinyAGI/tinyagi`, `inngest/agent-kit`.

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

<sub>Tools covered: 38 across 7 approaches · Snapshot: 2026-09-14T11:08:08.535Z</sub>
