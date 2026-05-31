# AI Agent Orchestration — Landscape Report

> Derived from **kaiser-data**'s 1,071 starred repos (snapshot `2026-05-24T19:57:47.245Z`), cross-referenced with the repo-similarity graph (1,071 nodes / 3,486 edges, 23 communities).
>
> Generated 2026-05-31 by `scripts/reports/agent_orchestration.py` (regenerate any time — no API cost).

> **Orchestration** = coordinating multiple agents / tools / steps toward a goal: routing, planning, parallelism, hand-offs, state and recovery. The tools below differ mostly in **how you express that coordination** — in code, on a visual canvas, across coding agents, or as durable production infra.

## Executive summary

- **30 agent-orchestration tools** in your stars (**974,076★**), organized by *how you express coordination*:
  - **Code-first agent frameworks** (10): `langgraph`, `semantic-kernel`, `openai-agents-python`, `agentscope`, `adk-python`, `agent-framework`, `voltagent`, `sdk-python`, `beeai-framework`, `AutoAgents`
  - **Visual / low-code platforms** (4): `n8n`, `dify`, `Flowise`, `sim`
  - **Coding-agent orchestration** (9): `deer-flow`, `oh-my-openagent`, `ruflo`, `agents`, `oh-my-claudecode`, `eigent`, `agent-orchestrator`, `paseo`, `coding-agent-template`
  - **Agent OS / long-horizon harness** (1): `eliza`
  - **Durable / production infra** (2): `flyte`, `agent-kit`
  - **Vertical / domain systems** (1): `TradingAgents`
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
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 32,833 | Python | 83 | very active | Mature | 2 |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | 27,967 | C# | 92 | very active | Classic | 4 |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 26,622 | Python | 90 | very active | Hot | 3 |
| [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | 25,528 | Python | 79 | very active | Mature | 2 |
| [google/adk-python](https://github.com/google/adk-python) | 19,832 | Python | 88 | very active | Hot | 3 |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | 10,696 | Python | 92 | very active | Hot | 4 |
| [VoltAgent/voltagent](https://github.com/VoltAgent/voltagent) | 9,122 | TypeScript | 82 | very active | Hot | 2 |
| [strands-agents/sdk-python](https://github.com/strands-agents/sdk-python) | 5,926 | Python | 96 | very active | Hot | 7 |
| [i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework) | 3,266 | Python | 70 | very active | Mature | 1 |
| [liquidos-ai/AutoAgents](https://github.com/liquidos-ai/AutoAgents) | 654 | Rust | 69 | very active | Hot | 1 |

### Visual / low-code platforms

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 189,534 | TypeScript | 100 | very active | Classic | 9 |
| [langgenius/dify](https://github.com/langgenius/dify) | 142,465 | TypeScript | 100 | very active | Classic | 5 |
| [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | 53,045 | TypeScript | 92 | very active | Classic | 4 |
| [simstudioai/sim](https://github.com/simstudioai/sim) | 28,600 | TypeScript | 78 | very active | Hot | 1 |

### Coding-agent orchestration

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 69,408 | Python | 81 | very active | Hot | 6 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 59,264 | TypeScript | 78 | very active | Hot | 1 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 54,749 | TypeScript | 77 | very active | Hot | 1 |
| [wshobson/agents](https://github.com/wshobson/agents) | 35,881 | Python | 65 | very active | Hot | 1 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | 34,738 | TypeScript | 80 | very active | Hot | 1 |
| [eigent-ai/eigent](https://github.com/eigent-ai/eigent) | 14,111 | TypeScript | 87 | very active | Hot | 3 |
| [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | 7,246 | TypeScript | 79 | very active | Hot | 2 |
| [getpaseo/paseo](https://github.com/getpaseo/paseo) | 6,646 | TypeScript | 73 | very active | Hot | 1 |
| [vercel-labs/coding-agent-template](https://github.com/vercel-labs/coding-agent-template) | 1,714 | TypeScript | 31 | active | Declining | 0 |

### Agent OS / long-horizon harness

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [elizaOS/eliza](https://github.com/elizaOS/eliza) | 18,445 | TypeScript | 80 | very active | Hot | 1 |

### Durable / production infra

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [flyteorg/flyte](https://github.com/flyteorg/flyte) | 7,046 | Go | 85 | very active | Classic | 3 |
| [inngest/agent-kit](https://github.com/inngest/agent-kit) | 868 | TypeScript | 57 | active | Declining | 1 |

### Vertical / domain systems

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 79,218 | Python | 69 | very active | Hot | 1 |

### Protocols & meta-frameworks

| Tool | ★ | Lang | Health | Activity | Lifecycle | Bus factor |
|---|---|---|---|---|---|---|
| [sentient-agi/ROMA](https://github.com/sentient-agi/ROMA) | 5,067 | Python | 33 | slowing | Declining | 0 |
| [TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi) | 3,568 | TypeScript | 71 | active | Rising | 1 |
| [veegee82/agent-workflow-protocol](https://github.com/veegee82/agent-workflow-protocol) | 17 | Python | 59 | very active | Rising | 1 |

## Details

### Code-first agent frameworks

_SDKs you write agents in — maximum control over routing, state and hand-offs; the engineer's default._

- **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** · 32,833★ · Python · Mature · health 83  
  Graph-based agent runtime — explicit nodes/edges/state; the de-facto control-flow framework.  
  <sub>topics: agents, ai, ai-agents, chatgpt, deepagents, enterprise</sub>
- **[microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)** · 27,967★ · C# · Classic · health 92  
  Microsoft's enterprise SDK (C#/Python) for plugging LLMs + planning into apps.  
  <sub>topics: ai, artificial-intelligence, llm, openai, sdk</sub>
- **[openai/openai-agents-python](https://github.com/openai/openai-agents-python)** · 26,622★ · Python · Hot · health 90  
  Lightweight, powerful framework for multi-agent workflows; handoffs + guardrails + tracing.  
  <sub>topics: agents, ai, framework, llm, python, openai</sub>
- **[agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)** · 25,528★ · Python · Mature · health 79  
  Build agents you can see/understand/trust; strong observability + multi-agent.  
  <sub>topics: agent, chatbot, large-language-models, llm, llm-agent, multi-agent</sub>
- **[google/adk-python](https://github.com/google/adk-python)** · 19,832★ · Python · Hot · health 88  
  Google's code-first Agent Development Kit — build, evaluate & deploy agents.  
  <sub>topics: agent, agents, agents-sdk, ai, ai-agents, multi-agent-systems</sub>
- **[microsoft/agent-framework](https://github.com/microsoft/agent-framework)** · 10,696★ · Python · Hot · health 92  
  Microsoft's framework to build, orchestrate & deploy multi-agent workflows (health 92).  
  <sub>topics: agent-framework, agentic-ai, agents, ai, multi-agent, orchestration</sub>
- **[VoltAgent/voltagent](https://github.com/VoltAgent/voltagent)** · 9,122★ · TypeScript · Hot · health 82  
  TypeScript agent-engineering platform + open-source framework.  
  <sub>topics: agents, ai, chatbots, llm, mcp, nodejs</sub>
- **[strands-agents/sdk-python](https://github.com/strands-agents/sdk-python)** · 5,926★ · Python · Hot · health 96  
  Model-driven agents in a few lines; very high health (96) and bus factor 7.  
  <sub>topics: agentic, agentic-ai, agents, ai, autonomous-agents, genai</sub>
- **[i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework)** · 3,266★ · Python · Mature · health 70  
  Production-ready agents in both Python and TypeScript.  
  <sub>topics: agents, ai, framework, ai-agent, llm, multiagent</sub>
- **[liquidos-ai/AutoAgents](https://github.com/liquidos-ai/AutoAgents)** · 654★ · Rust · Hot · health 69  
  Rust multi-agent framework to build, deploy & coordinate agents.  
  <sub>topics: agents, ai, ai-agents, ai-agents-framework, llm</sub>

### Visual / low-code platforms

_Drag-and-drop canvases — fastest to a working flow, accessible to non-engineers, less granular control._

- **[n8n-io/n8n](https://github.com/n8n-io/n8n)** · 189,534★ · TypeScript · Classic · health 100  
  Fair-code workflow automation with native AI nodes — the giant (189k★, health 100).  
  <sub>topics: automation, ipaas, n8n, workflow, typescript, self-hosted</sub>
- **[langgenius/dify](https://github.com/langgenius/dify)** · 142,465★ · TypeScript · Classic · health 100  
  Production-ready platform for agentic workflow development (health 100).  
  <sub>topics: ai, gpt, llm, openai, python, rag</sub>
- **[FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)** · 53,045★ · TypeScript · Classic · health 92  
  Build AI agents visually; popular drag-and-drop builder.  
  <sub>topics: artificial-intelligence, chatgpt, large-language-models, low-code, no-code, javascript</sub>
- **[simstudioai/sim](https://github.com/simstudioai/sim)** · 28,600★ · TypeScript · Hot · health 78  
  Build, deploy & orchestrate agents — 'central intelligence layer for your AI workforce'.  
  <sub>topics: agentic-workflow, agents, ai, nextjs, typescript, agent-workflow</sub>

### Coding-agent orchestration

_Coordinate *swarms of coding agents* (Claude Code, Codex, Cursor…) on a codebase — plan, spawn, run in parallel, handle CI._

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 69,408★ · Python · Hot · health 81  
  Long-horizon SuperAgent harness that researches, codes & creates with sandboxes (bf6).  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 59,264★ · TypeScript · Hot · health 78  
  'omo' — agent harness (formerly oh-my-opencode) for coding workflows.  
  <sub>topics: claude-code, opencode, ai, amp, anthropic, claude</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 54,749★ · TypeScript · Hot · health 77  
  Agent-orchestration platform for Claude — multi-agent swarms coordinating autonomous coding.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-rag, agentic-workflow</sub>
- **[wshobson/agents](https://github.com/wshobson/agents)** · 35,881★ · Python · Hot · health 65  
  Multi-harness agentic plugin marketplace (Claude Code, Codex, Cursor, OpenCode, Gemini).  
  <sub>topics: agents, anthropic, automation, workflows, orchestration, agent-skills</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 34,738★ · TypeScript · Hot · health 80  
  Teams-first multi-agent orchestration for Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode</sub>
- **[eigent-ai/eigent](https://github.com/eigent-ai/eigent)** · 14,111★ · TypeScript · Hot · health 87  
  Open-source cowork desktop — local/free multi-agent productivity workspace.  
  <sub>topics: agent-framework, agent-skills, agentic-ai, agentic-workflow, claude-cowork, claude-cowork-alternative</sub>
- **[ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator)** · 7,246★ · TypeScript · Hot · health 79  
  Orchestrates parallel coding agents — plans tasks, spawns agents, handles CI autonomously.  
  <sub>topics: claude-code, codex-cli, orchestration, orchestrator, skills, agent-fleet</sub>
- **[getpaseo/paseo](https://github.com/getpaseo/paseo)** · 6,646★ · TypeScript · Hot · health 73  
  Run & coordinate coding agents from phone, desktop and CLI.  
  <sub>topics: agents, claude-code, codex, opencode, ade, copilot</sub>
- **[vercel-labs/coding-agent-template](https://github.com/vercel-labs/coding-agent-template)** · 1,714★ · TypeScript · Declining · health 31  
  Multi-agent coding platform on Vercel Sandbox + AI Gateway; declining, verify first.  
  <sub>topics: —</sub>

### Agent OS / long-horizon harness

_Runtimes for always-on, long-running autonomous agents._

- **[elizaOS/eliza](https://github.com/elizaOS/eliza)** · 18,445★ · TypeScript · Hot · health 80  
  Open-source 'agentic operating system' — long-running autonomous agents.  
  <sub>topics: agent, agentic, ai, autonomous, chatbot, crypto</sub>

### Durable / production infra

_Fault-tolerant execution — retries, checkpointing, deterministic routing for production._

- **[flyteorg/flyte](https://github.com/flyteorg/flyte)** · 7,046★ · Go · Classic · health 85  
  Dynamic, resilient orchestration (Go/K8s) — coordinate data, models & compute durably.  
  <sub>topics: flyte, machine-learning, golang, scale, workflow, data-science</sub>
- **[inngest/agent-kit](https://github.com/inngest/agent-kit)** · 868★ · TypeScript · Declining · health 57  
  Build multi-agent networks in TS with deterministic routing + durable execution via MCP.  
  <sub>topics: agent, ai, ai-agent-framework, ai-agents, llm</sub>

### Vertical / domain systems

_Reference multi-agent architectures for a specific domain._

- **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** · 79,218★ · Python · Hot · health 69  
  Multi-agent LLM framework for financial trading — a vertical reference architecture (79k★).  
  <sub>topics: agent, finance, llm, multiagent, trading</sub>

### Protocols & meta-frameworks

_Standards and meta-layers above any single framework._

- **[sentient-agi/ROMA](https://github.com/sentient-agi/ROMA)** · 5,067★ · Python · Declining · health 33  
  Recursive meta-agent framework to build multi-agent systems; declining/low health.  
  <sub>topics: —</sub>
- **[TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi)** · 3,568★ · TypeScript · Rising · health 71  
  Agent-teams orchestrator aimed at one-person companies.  
  <sub>topics: —</sub>
- **[veegee82/agent-workflow-protocol](https://github.com/veegee82/agent-workflow-protocol)** · 17★ · Python · Rising · health 59  
  Open standard for multi-agent workflows — scripted pipelines to self-organizing teams.  
  <sub>topics: agentic, agentic-ai, agentic-ai-development, agentic-engineering, agentic-framework, agentic-workflow</sub>

## Graph analysis — how they relate

**Community clustering.** These 30 tools span **10 of the graph's 23 communities**.

- **Community 12** (10): `langchain-ai/langgraph`, `google/adk-python`, `VoltAgent/voltagent`, `strands-agents/sdk-python`, `i-am-bee/beeai-framework`, `liquidos-ai/AutoAgents`, `FlowiseAI/Flowise`, `simstudioai/sim`, `bytedance/deer-flow`, `veegee82/agent-workflow-protocol`
- **Community 10** (6): `code-yeongyu/oh-my-openagent`, `ruvnet/ruflo`, `wshobson/agents`, `Yeachan-Heo/oh-my-claudecode`, `ComposioHQ/agent-orchestrator`, `getpaseo/paseo`
- **Community 0** (5): `n8n-io/n8n`, `langgenius/dify`, `vercel-labs/coding-agent-template`, `inngest/agent-kit`, `TinyAGI/tinyagi`
- **Community 16** (2): `microsoft/semantic-kernel`, `microsoft/agent-framework`
- **Community 15** (2): `agentscope-ai/agentscope`, `TauricResearch/TradingAgents`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' orchestration tools in your ecosystem:

- `langchain-ai/langgraph` — PageRank 0.0030
- `inngest/agent-kit` — PageRank 0.0024
- `code-yeongyu/oh-my-openagent` — PageRank 0.0022
- `microsoft/semantic-kernel` — PageRank 0.0021
- `openai/openai-agents-python` — PageRank 0.0021
- `liquidos-ai/AutoAgents` — PageRank 0.0020
- `langgenius/dify` — PageRank 0.0020
- `microsoft/agent-framework` — PageRank 0.0018
- `VoltAgent/voltagent` — PageRank 0.0017
- `i-am-bee/beeai-framework` — PageRank 0.0016

**Direct links between orchestration tools** (top similarity edges where both endpoints are in this report):

- `microsoft/agent-framework` ⇄ `microsoft/semantic-kernel` (w=1.187) — topics: ai, sdk; authors: westey-m, moonbox3, alliscode
- `Yeachan-Heo/oh-my-claudecode` ⇄ `code-yeongyu/oh-my-openagent` (w=0.540) — topics: ai-agents, claude, claude-code, opencode; authors: Yeachan-Heo, bellman@bellmanui-MacBookAir.local
- `i-am-bee/beeai-framework` ⇄ `openai/openai-agents-python` (w=0.505) — topics: agents, ai, framework, llm
- `FlowiseAI/Flowise` ⇄ `simstudioai/sim` (w=0.450) — topics: artificial-intelligence, low-code, no-code, react
- `langchain-ai/langgraph` ⇄ `i-am-bee/beeai-framework` (w=0.431) — topics: agents, ai, framework, llm; authors: dependabot[bot]
- `liquidos-ai/AutoAgents` ⇄ `inngest/agent-kit` (w=0.429) — topics: ai, ai-agents, llm
- `simstudioai/sim` ⇄ `langgenius/dify` (w=0.360) — topics: agentic-workflow, ai, nextjs, gemini
- `strands-agents/sdk-python` ⇄ `google/adk-python` (w=0.300) — topics: agentic, agentic-ai, agents, ai
- `strands-agents/sdk-python` ⇄ `openai/openai-agents-python` (w=0.288) — topics: agents, ai, llm, python
- `wshobson/agents` ⇄ `microsoft/agent-framework` (w=0.250) — topics: agents, workflows, orchestration, agentic-ai
- `inngest/agent-kit` ⇄ `TauricResearch/TradingAgents` (w=0.250) — topics: agent, llm
- `VoltAgent/voltagent` ⇄ `FlowiseAI/Flowise` (w=0.244) — topics: agents, typescript, javascript, rag
- `langgenius/dify` ⇄ `n8n-io/n8n` (w=0.226) — topics: ai, workflow, automation, low-code
- `getpaseo/paseo` ⇄ `code-yeongyu/oh-my-openagent` (w=0.224) — topics: claude-code, opencode, gemini, orchestration
- `veegee82/agent-workflow-protocol` ⇄ `google/adk-python` (w=0.217) — topics: agentic, agentic-ai, agents, llms
- …and 3 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Orchestration is load-bearing — weigh this heavily before standardizing on one.

| Tool | Approach | Health | Lifecycle | Activity | Bus factor |
|---|---|---|---|---|---|
| n8n-io/n8n | Visual / low-code platforms | 100 | Classic | very active | 9 |
| langgenius/dify | Visual / low-code platforms | 100 | Classic | very active | 5 |
| strands-agents/sdk-python | Code-first agent frameworks | 96 | Hot | very active | 7 |
| microsoft/semantic-kernel | Code-first agent frameworks | 92 | Classic | very active | 4 |
| microsoft/agent-framework | Code-first agent frameworks | 92 | Hot | very active | 4 |
| FlowiseAI/Flowise | Visual / low-code platforms | 92 | Classic | very active | 4 |
| openai/openai-agents-python | Code-first agent frameworks | 90 | Hot | very active | 3 |
| google/adk-python | Code-first agent frameworks | 88 | Hot | very active | 3 |
| eigent-ai/eigent | Coding-agent orchestration | 87 | Hot | very active | 3 |
| flyteorg/flyte | Durable / production infra | 85 | Classic | very active | 3 |
| langchain-ai/langgraph | Code-first agent frameworks | 83 | Mature | very active | 2 |
| VoltAgent/voltagent | Code-first agent frameworks | 82 | Hot | very active | 2 |
| bytedance/deer-flow | Coding-agent orchestration | 81 | Hot | very active | 6 |
| Yeachan-Heo/oh-my-claudecode | Coding-agent orchestration | 80 | Hot | very active | 1 |
| elizaOS/eliza | Agent OS / long-horizon harness | 80 | Hot | very active | 1 |
| agentscope-ai/agentscope | Code-first agent frameworks | 79 | Mature | very active | 2 |
| ComposioHQ/agent-orchestrator | Coding-agent orchestration | 79 | Hot | very active | 2 |
| simstudioai/sim | Visual / low-code platforms | 78 | Hot | very active | 1 |
| code-yeongyu/oh-my-openagent | Coding-agent orchestration | 78 | Hot | very active | 1 |
| ruvnet/ruflo | Coding-agent orchestration | 77 | Hot | very active | 1 |
| getpaseo/paseo | Coding-agent orchestration | 73 | Hot | very active | 1 |
| TinyAGI/tinyagi | Protocols & meta-frameworks | 71 | Rising | active | 1 |
| i-am-bee/beeai-framework | Code-first agent frameworks | 70 | Mature | very active | 1 |
| liquidos-ai/AutoAgents | Code-first agent frameworks | 69 | Hot | very active | 1 |
| TauricResearch/TradingAgents | Vertical / domain systems | 69 | Hot | very active | 1 |
| wshobson/agents | Coding-agent orchestration | 65 | Hot | very active | 1 |
| veegee82/agent-workflow-protocol | Protocols & meta-frameworks | 59 | Rising | very active | 1 |
| inngest/agent-kit | Durable / production infra | 57 | Declining | active | 1 |
| sentient-agi/ROMA | Protocols & meta-frameworks | 33 | Declining | slowing | 0 |
| vercel-labs/coding-agent-template | Coding-agent orchestration | 31 | Declining | active | 0 |

⚠️ **Adopt with caution** (low health and/or declining): `vercel-labs/coding-agent-template`, `sentient-agi/ROMA`, `inngest/agent-kit`.

## Notably absent from your stars

Major orchestration tools **not** in this dataset — worth knowing before treating the above as complete:

- **crewAIInc/crewAI** — the popular role-based multi-agent 'crew' framework
- **microsoft/autogen** — Microsoft's research multi-agent conversation framework
- **langflow-ai/langflow** — popular visual agent/flow builder

## Methodology & caveats

- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: scan for orchestration / multi-agent / swarm / workflow / agent-framework signals, then manual curation by approach. RAG frameworks, eval/observability platforms, and single-purpose agents were routed to their own reports or excluded; only tools whose *primary* job is coordinating agents/steps appear here.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub. Re-run after a fresh `classified.json` to refresh.

<sub>Tools covered: 30 across 7 approaches · Snapshot: 2026-05-24T19:57:47.245Z</sub>
