# Agent Harnesses — Six Approaches to Running Autonomous Agents

> Derived from **kaiser-data**'s 1,350 starred repos (snapshot `2026-07-20T08:33:57.852Z`), cross-referenced with the repo-similarity graph (1,350 nodes / 4,379 edges, 28 communities).
>
> Generated 2026-07-20 by `scripts/reports/agent_harnesses.py` (regenerate any time — no API cost).

![Top tools by stars](assets/agent-harnesses-top-tools.svg)

![Tools per category](assets/agent-harnesses-categories.svg)


## Executive summary

- A **harness** is everything around the model: the loop, tools, state, guardrails, and execution environment. **36 harness projects** in your stars (**1,357,835★** combined) cluster into **six distinct approaches** — they disagree about *where the harness lives* and *what the hard problem is*:
  - **Harness-as-SDK** (8): `pi`, `deepagents`, `parlant`, `jcode`, `harness-sdk`, `eve`, `cheetahclaws`, `pydantic-ai-harness`
  - **Meta-harness over coding agents** (6): `superpowers`, `ECC`, `oh-my-openagent`, `ruflo`, `oh-my-claudecode`, `Archon`
  - **Fleet / parallel orchestration** (7): `multica`, `vibe-kanban`, `gastown`, `Aperant`, `agent-orchestrator`, `ccpm`, `container-use`
  - **Determinism & spec-driven** (5): `spec-kit`, `planning-with-files`, `agents.md`, `loop-engineering`, `gsd-2`
  - **Sandbox substrate** (5): `daytona`, `NemoClaw`, `cua`, `OpenSandbox`, `forkd`
  - **Autonomous long-horizon** (5): `deer-flow`, `agent-zero`, `sia`, `agent`, `ClaudeNightsWatch`
- The fault line: **build the loop** (Harness-as-SDK) vs **wrap an existing agent** (meta-harness) vs **multiply agents** (fleet) — with determinism, sandboxing, and long-horizon autonomy as orthogonal bets any of them can adopt.
- Star mass sits with the meta-harnesses (`superpowers`, `ECC`, `ruflo`) — the ecosystem is betting that the inner loop is a solved commodity and the value is in the layer above it.

## The six approaches, compared

| Approach | Core bet | When it wins |
|---|---|---|
| **Harness-as-SDK** | You own the loop in code — tools, state, and control flow are a library you compose. | Building a *product* around an agent; you need custom behavior and testability. |
| **Meta-harness over coding agents** | Claude Code/Codex already won the inner loop — add skills, memory, and orchestration *around* it. | Developer workflows; you want leverage today without rebuilding tool-use. |
| **Fleet / parallel orchestration** | Throughput beats IQ — run many agents in worktrees/sandboxes and manage them like a team. | Large backlogs of separable tasks; PR-shaped work. |
| **Determinism & spec-driven** | Repeatability beats improvisation — specs, plans-on-disk, and standards steer the loop. | Teams that need auditable, resumable, low-variance agent output. |
| **Sandbox substrate** | The hard problem is *where* agents run — isolation, speed, and forking are the product. | Untrusted/generated code, computer-use, or massively parallel execution. |
| **Autonomous long-horizon** | Maximize wall-clock autonomy — agents that plan, persist, and keep going for hours or days. | Research, background maintenance, overnight queues; outcome > oversight. |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Approach | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | Meta-harness over coding agents | Shell | MIT | 257,811 (▲280) | Hot | 78 | very active | 0d ago | 9mo | 3 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Meta-harness over coding agents | JavaScript | MIT | 231,351 (▲141) | Hot | 95 | very active | 0d ago | 6mo | 38 |
| [github/spec-kit](https://github.com/github/spec-kit) | Determinism & spec-driven | Python | MIT | 122,508 (▲209) | Hot | 89 | very active | 2d ago | 11mo | 18 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Autonomous long-horizon | Python | MIT | 77,423 (▲32) | Hot | 84 | very active | 0d ago | 1.2y | 34 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness-as-SDK | TypeScript | MIT | 72,998 (▲250) | Hot | 85 | very active | 0d ago | 11mo | 13 |
| [daytonaio/daytona](https://github.com/daytonaio/daytona) | Sandbox substrate | — | — | 72,244 (▲1) | Mature | 97 | very active | 11d ago | 2.5y | 21 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Meta-harness over coding agents | TypeScript | NOASSERTION | 66,217 (▲44) | Hot | 78 | very active | 0d ago | 7mo | 5 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Meta-harness over coding agents | TypeScript | MIT | 65,237 (▲46) | Hot | 76 | very active | 0d ago | 1.1y | 4 |
| [multica-ai/multica](https://github.com/multica-ai/multica) | Fleet / parallel orchestration | Go | NOASSERTION | 41,133 (▲60) | Hot | 86 | very active | 0d ago | 6mo | 27 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Meta-harness over coding agents | TypeScript | MIT | 37,902 (▲5) | Hot | 80 | very active | 1d ago | 6mo | 18 |
| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Fleet / parallel orchestration | Rust | Apache-2.0 | 27,455 (▲6) | Mature | 54 | slowing | 2mo ago | 1.1y | 2 |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Harness-as-SDK | Python | MIT | 26,552 (▲36) | Hot | 79 | very active | 0d ago | 11mo | 12 |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | Determinism & spec-driven | Python | MIT | 25,552 (▲34) | Hot | 78 | very active | 2d ago | 6mo | 20 |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | Determinism & spec-driven | TypeScript | MIT | 23,104 (▲8) | Declining | 21 | slowing | 4mo ago | 11mo | 0 |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Meta-harness over coding agents | TypeScript | MIT | 22,949 (▲3) | Hot | 78 | very active | 3d ago | 1.4y | 13 |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Sandbox substrate | TypeScript | Apache-2.0 | 21,848 (▲7) | Hot | 84 | very active | 0d ago | 4mo | 26 |
| [trycua/cua](https://github.com/trycua/cua) | Sandbox substrate | HTML | MIT | 20,305 (▲86) | Hot | 75 | very active | 0d ago | 1.5y | 10 |
| [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | Autonomous long-horizon | Python | NOASSERTION | 18,457 (▲2) | Mature | 78 | very active | 0d ago | 2.1y | 2 |
| [emcie-co/parlant](https://github.com/emcie-co/parlant) | Harness-as-SDK | Python | Apache-2.0 | 18,179 (▲2) | Mature | 73 | very active | 8d ago | 2.4y | 7 |
| [gastownhall/gastown](https://github.com/gastownhall/gastown) | Fleet / parallel orchestration | Go | MIT | 17,110 (▲7) | Hot | 78 | very active | 2d ago | 7mo | 8 |
| [AndyMik90/Aperant](https://github.com/AndyMik90/Aperant) | Fleet / parallel orchestration | TypeScript | AGPL-3.0 | 14,470 (▲1) | Declining | 57 | active | 1mo ago | 7mo | 1 |
| [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | Sandbox substrate | Python | Apache-2.0 | 12,068 (▲10) | Hot | 78 | very active | 0d ago | 7mo | 13 |
| [1jehuang/jcode](https://github.com/1jehuang/jcode) | Harness-as-SDK | Rust | MIT | 9,118 (▲264) | Rising | 77 | very active | 0d ago | 6mo | 1 |
| [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | Determinism & spec-driven | JavaScript | MIT | 8,721 (▲83) | Hot | 70 | very active | 0d ago | 1mo | 19 |
| [AgentWrapper/agent-orchestrator](https://github.com/AgentWrapper/agent-orchestrator) | Fleet / parallel orchestration | Go | Apache-2.0 | 8,398 (▲13) | Hot | 97 | very active | 0d ago | 5mo | 30 |
| [automazeio/ccpm](https://github.com/automazeio/ccpm) | Fleet / parallel orchestration | Shell | MIT | 8,276 | Declining | 30 | slowing | 4mo ago | 11mo | 0 |
| [gsd-build/gsd-2](https://github.com/gsd-build/gsd-2) | Determinism & spec-driven | TypeScript | MIT | 7,752 | Rising | 75 | active | 1mo ago | 4mo | 2 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | Harness-as-SDK | Python | Apache-2.0 | 6,648 (▲7) | Hot | 92 | very active | 0d ago | 1.2y | 27 |
| [dagger/container-use](https://github.com/dagger/container-use) | Fleet / parallel orchestration | Go | Apache-2.0 | 3,914 | Declining | 44 | active | 1mo ago | 1.2y | 1 |
| [vercel/eve](https://github.com/vercel/eve) | Harness-as-SDK | TypeScript | Apache-2.0 | 3,891 (▲12) | Hot | 83 | very active | 0d ago | 1mo | 19 |
| [deeplethe/forkd](https://github.com/deeplethe/forkd) | Sandbox substrate | Rust | Apache-2.0 | 2,711 (▲1) | Hot | 78 | very active | 11d ago | 2mo | 5 |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | Autonomous long-horizon | Python | MIT | 2,051 | Rising | 54 | very active | 18d ago | 3mo | 8 |
| [stakpak/agent](https://github.com/stakpak/agent) | Autonomous long-horizon | Rust | Apache-2.0 | 1,680 | Hot | 80 | very active | 14d ago | 1.6y | 6 |
| [SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws) | Harness-as-SDK | Python | Apache-2.0 | 760 | Hot | 76 | very active | 5d ago | 3mo | 5 |
| [pydantic/pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness) | Harness-as-SDK | Python | MIT | 674 | Hot | 75 | very active | 0d ago | 4mo | 9 |
| [aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch) | Autonomous long-horizon | Shell | MIT | 368 | Declining | 21 | stale | 6mo ago | 1.0y | 0 |

## By approach

### Harness-as-SDK

_The loop as a library: you import the harness, register tools, and own control flow. Maximum flexibility, maximum responsibility — you maintain planning, retries, memory, and safety yourself._

- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 72,998★ · TypeScript · Hot  
  Unified LLM API + agent loop + TUI + coding-agent CLI in one toolkit — the loop as a library.  
  <sub>topics: —</sub>
- **[langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)** · 26,552★ · Python · Hot  
  The 'batteries-included agent harness' — planning, sub-agents, filesystem, from the LangChain team.  
  <sub>topics: deepagents, langchain, langgraph, ai, python, typescript</sub>
- **[emcie-co/parlant](https://github.com/emcie-co/parlant)** · 18,179★ · Python · Mature  
  Interaction *control* harness — behavioral guidelines enforced at runtime for customer-facing agents.  
  <sub>topics: ai-agents, genai, llm, customer-service, customer-success, gemini, llama3, openai</sub>
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 9,118★ · Rust · Rising  
  Rust-built coding-agent harness — CLI agent loop with MCP support and multi-model wiring.  
  <sub>topics: ai, claude, cli, coding-agent, llm, mcp, openai, rust</sub>
- **[strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)** · 6,648★ · Python · Hot  
  AWS's open SDK to build an agent harness and control it end-to-end in production.  
  <sub>topics: agentic, agentic-ai, agents, ai, autonomous-agents, llm, multi-agent-systems, python</sub>
- **[vercel/eve](https://github.com/vercel/eve)** · 3,891★ · TypeScript · Hot  
  Vercel's framework for building agents — harness + sandbox as one integrated runtime.  
  <sub>topics: agent, framework, harness, javascript, markdown, typescript, vercel, sandbox</sub>
- **[SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws)** · 760★ · Python · Hot  
  Fast, easy agent-harness infrastructure aimed at long-horizon, multi-model runs.  
  <sub>topics: agentic-ai, claude, claude-code, memory, python, skills, openclaw</sub>
- **[pydantic/pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness)** · 674★ · Python · Hot  
  'Batteries for your Pydantic AI agent' — the harness as a thin add-on to a typed agent framework.  
  <sub>topics: —</sub>

### Meta-harness over coding agents

_These projects treat Claude Code / Codex as the engine and build the transmission: skills, personas, memory, token discipline, and multi-agent coordination injected via configs, hooks, and subagents._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 257,811★ · Shell · Hot  
  Skills framework + development methodology layered onto the agent you already run.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 231,351★ · JavaScript · Hot  
  Harness performance optimization: skills, instincts, memory, security, hooks on top of Claude Code.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 66,217★ · TypeScript · Hot  
  'The one and only agent harness for complex coding' — tokenmaxxer harness wrapping coding agents.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 65,237★ · TypeScript · Hot  
  The leading agent *meta*-harness — swarms, coordination, and autonomy on top of existing agents.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 37,902★ · TypeScript · Hot  
  Teams-first multi-agent orchestration living entirely inside Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>
- **[coleam00/Archon](https://github.com/coleam00/Archon)** · 22,949★ · TypeScript · Hot  
  'Harness builder' — make AI coding deterministic and repeatable by generating the harness itself.  
  <sub>topics: ai, automation, bun, claude, cli, coding-assistant, developer-tools, typescript</sub>

### Fleet / parallel orchestration

_One agent is a tool; a fleet is a team. The harness problem becomes scheduling, isolation (worktrees, containers), review queues, and merge discipline._

- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 41,133★ · Go · Hot  
  Managed-agents platform: assign tasks to coding agents like teammates and supervise them.  
  <sub>topics: —</sub>
- **[BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban)** · 27,455★ · Rust · Mature  
  A kanban board as the harness — queue, run, and review many agent tasks in parallel.  
  <sub>topics: agent, ai-agents, kanban, management, task-manager</sub>
- **[gastownhall/gastown](https://github.com/gastownhall/gastown)** · 17,110★ · Go · Hot  
  Multi-agent workspace manager — the 'town' where a fleet of agents live and work.  
  <sub>topics: —</sub>
- **[AndyMik90/Aperant](https://github.com/AndyMik90/Aperant)** · 14,470★ · TypeScript · Declining  
  Autonomous multi-session AI coding — sessions as the unit of parallelism.  
  <sub>topics: —</sub>
- **[AgentWrapper/agent-orchestrator](https://github.com/AgentWrapper/agent-orchestrator)** · 8,398★ · Go · Hot  
  Plans tasks, spawns parallel coding agents in worktrees, merges autonomously.  
  <sub>topics: claude-code, codex-cli, orchestration, orchestrator, skills, agent-fleet, agent-swarm, git-worktrees</sub>
- **[automazeio/ccpm](https://github.com/automazeio/ccpm)** · 8,276★ · Shell · Declining  
  GitHub Issues + git worktrees as the coordination fabric for parallel agents.  
  <sub>topics: ai-agents, ai-coding, claude, claude-code, project-management, vibe-coding</sub>
- **[dagger/container-use](https://github.com/dagger/container-use)** · 3,914★ · Go · Declining  
  Containerized dev environments so multiple agents work safely and independently.  
  <sub>topics: —</sub>

### Determinism & spec-driven

_The counter-culture: agents drift, so pin them down. Specs, standards files, and plans persisted to disk make runs reproducible, auditable, and resumable after crashes._

- **[github/spec-kit](https://github.com/github/spec-kit)** · 122,508★ · Python · Hot  
  Spec-Driven Development toolkit — the spec, not the prompt, steers the agent.  
  <sub>topics: ai, copilot, development, engineering, prd, spec, spec-driven</sub>
- **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** · 25,552★ · Python · Hot  
  Persistent file-based planning — crash-proof, resumable long-running agent tasks.  
  <sub>topics: claude, claude-code, claude-skills, manus, agent-skills, planning, copilot, pi</sub>
- **[agentsmd/agents.md](https://github.com/agentsmd/agents.md)** · 23,104★ · TypeScript · Declining  
  The open AGENTS.md standard — a portable contract telling any harness how to behave in a repo.  
  <sub>topics: —</sub>
- **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** · 8,721★ · JavaScript · Hot  
  Patterns and starters for *loop engineering* — designing the iteration, not just the prompt.  
  <sub>topics: agentic-ai, ai-agents, claude-code, codex, devops-automation, github-actions, grok, llm</sub>
- **[gsd-build/gsd-2](https://github.com/gsd-build/gsd-2)** · 7,752★ · TypeScript · Rising  
  Meta-prompting + context engineering + spec-driven system for dependable outcomes.  
  <sub>topics: context-engineering, meta-prompting, spec-driven-development</sub>

### Sandbox substrate

_Infrastructure-first: before you scale agents you need somewhere safe and fast to run them. MicroVMs, container runtimes, and hardened sandboxes are the harness's floor._

- **[daytonaio/daytona](https://github.com/daytonaio/daytona)** · 72,244★ · — · Mature  
  Secure, elastic infrastructure for running AI-generated code — the harness's execution floor.  
  <sub>topics: developer-tools, agentic-workflow, ai, ai-agents, ai-runtime, code-execution, code-interpreter, ai-sandboxes</sub>
- **[NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)** · 21,848★ · TypeScript · Hot  
  Run harnesses (Hermes, Deep Agents, OpenClaw) inside hardened NVIDIA sandboxes.  
  <sub>topics: ai-agents, nvidia, openclaw, openshell, sandboxing, typescript, hermes</sub>
- **[trycua/cua](https://github.com/trycua/cua)** · 20,305★ · HTML · Hot  
  Sandboxes, SDKs, and benchmarks for computer-use agents — full-desktop harnessing.  
  <sub>topics: apple, cua, lume, macos, virtualization, virtualization-framework, swift, ai-agent</sub>
- **[opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)** · 12,068★ · Python · Hot  
  Secure, fast, extensible sandbox runtime purpose-built for AI agents.  
  <sub>topics: ai, ai-infra, kubernetes, sandbox, ai-agent</sub>
- **[deeplethe/forkd](https://github.com/deeplethe/forkd)** · 2,711★ · Rust · Hot  
  fork() for agent microVMs — spawn 100 children in ~100ms; branch a live VM mid-run.  
  <sub>topics: ai-agents, copy-on-write, kvm, microvm, rust, sandbox, snapshot</sub>

### Autonomous long-horizon

_Maximum autonomy: agents that run for hours or days, planning and re-planning, sometimes improving their own scaffolding. The harness is a resident process, not a CLI invocation._

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 77,423★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and creates with sub-agents in sandboxes.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[agent0ai/agent-zero](https://github.com/agent0ai/agent-zero)** · 18,457★ · Python · Mature  
  General autonomous framework — the agent builds its own tools as it goes.  
  <sub>topics: agent, ai, assistant, autonomous, linux, zero</sub>
- **[hexo-ai/sia](https://github.com/hexo-ai/sia)** · 2,051★ · Python · Rising  
  Self-Improving AI — a harness whose loop optimizes the underlying system over time.  
  <sub>topics: —</sub>
- **[stakpak/agent](https://github.com/stakpak/agent)** · 1,680★ · Rust · Hot  
  An agent that lives on your machines 24/7 and keeps shipping — harness as a resident daemon.  
  <sub>topics: agent, devops, devtool, generative-ai, hacktoberfest, ai-agent, autonomous-agent, llm-agent</sub>
- **[aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch)** · 368★ · Shell · Declining  
  Watches your Claude usage windows and executes queued tasks autonomously overnight.  
  <sub>topics: —</sub>

## Graph analysis — how they relate

**Community clustering.** These 36 tools span **14 of the graph's 28 communities**.

- **Community 5** (8): `langchain-ai/deepagents`, `emcie-co/parlant`, `SafeRL-Lab/cheetahclaws`, `pydantic/pydantic-ai-harness`, `gsd-build/gsd-2`, `daytonaio/daytona`, `deeplethe/forkd`, `agent0ai/agent-zero`
- **Community 1** (8): `affaan-m/ECC`, `Yeachan-Heo/oh-my-claudecode`, `coleam00/Archon`, `AndyMik90/Aperant`, `automazeio/ccpm`, `OthmanAdi/planning-with-files`, `agentsmd/agents.md`, `cobusgreyling/loop-engineering`
- **Community 2** (6): `earendil-works/pi`, `code-yeongyu/oh-my-openagent`, `ruvnet/ruflo`, `gastownhall/gastown`, `AgentWrapper/agent-orchestrator`, `trycua/cua`
- **Community 7** (2): `vercel/eve`, `obra/superpowers`
- **Community 11** (2): `multica-ai/multica`, `BloopAI/vibe-kanban`
- **Community 12** (2): `dagger/container-use`, `opensandbox-group/OpenSandbox`

**Centrality (PageRank in the full 1,350-repo graph)** — most 'hub-like' harnesses in your ecosystem:

- `affaan-m/ECC` — PageRank 0.0023
- `langchain-ai/deepagents` — PageRank 0.0022
- `code-yeongyu/oh-my-openagent` — PageRank 0.0014
- `NVIDIA/NemoClaw` — PageRank 0.0014
- `cobusgreyling/loop-engineering` — PageRank 0.0013
- `1jehuang/jcode` — PageRank 0.0012
- `bytedance/deer-flow` — PageRank 0.0011
- `coleam00/Archon` — PageRank 0.0011
- `stakpak/agent` — PageRank 0.0009
- `hexo-ai/sia` — PageRank 0.0008

**Direct links between harness projects** (top similarity edges where both endpoints are in this report):

- `cobusgreyling/loop-engineering` ⇄ `affaan-m/ECC` (w=0.402) — topics: ai-agents, claude-code, llm, mcp; authors: dependabot[bot]
- `bytedance/deer-flow` ⇄ `langchain-ai/deepagents` (w=0.358) — topics: ai, langchain, langgraph, python; authors: dependabot[bot]
- `Yeachan-Heo/oh-my-claudecode` ⇄ `automazeio/ccpm` (w=0.333) — topics: ai-agents, claude, claude-code, vibe-coding
- `code-yeongyu/oh-my-openagent` ⇄ `coleam00/Archon` (w=0.304) — topics: ai, claude, typescript; authors: github-actions[bot]
- `affaan-m/ECC` ⇄ `automazeio/ccpm` (w=0.273) — topics: ai-agents, claude, claude-code
- `strands-agents/harness-sdk` ⇄ `ruvnet/ruflo` (w=0.212) — topics: agentic-ai, agents, autonomous-agents, multi-agent-systems
- `bytedance/deer-flow` ⇄ `ruvnet/ruflo` (w=0.188) — topics: agentic-framework, agentic-workflow, ai-agents, multi-agent

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Harnesses are a young, fast-moving category — expect churn; check lifecycle before betting on one.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| AgentWrapper/agent-orchestrator | 97 | Hot | very active | 7 | 12% | 77 |
| daytonaio/daytona | 97 | Mature | very active | 5 | 14% | 205 |
| affaan-m/ECC | 95 | Hot | very active | 4 | 29% | 14 |
| strands-agents/harness-sdk | 92 | Hot | very active | 4 | 23% | 74 |
| github/spec-kit | 89 | Hot | very active | 3 | 20% | 195 |
| multica-ai/multica | 86 | Hot | very active | 3 | 24% | 116 |
| earendil-works/pi | 85 | Hot | very active | 2 | 40% | 247 |
| NVIDIA/NemoClaw | 84 | Hot | very active | 5 | 15% | 0 |
| bytedance/deer-flow | 84 | Hot | very active | 5 | 20% | 1 |
| vercel/eve | 83 | Hot | very active | 3 | 22% | 64 |
| Yeachan-Heo/oh-my-claudecode | 80 | Hot | very active | 1 | 53% | 240 |
| stakpak/agent | 80 | Hot | very active | 2 | 49% | 315 |
| langchain-ai/deepagents | 79 | Hot | very active | 1 | 67% | 222 |
| obra/superpowers | 78 | Hot | very active | 1 | 69% | 10 |
| code-yeongyu/oh-my-openagent | 78 | Hot | very active | 1 | 93% | 221 |
| coleam00/Archon | 78 | Hot | very active | 1 | 83% | 15 |
| gastownhall/gastown | 78 | Hot | very active | 1 | 51% | 14 |
| OthmanAdi/planning-with-files | 78 | Hot | very active | 1 | 73% | 79 |
| opensandbox-group/OpenSandbox | 78 | Hot | very active | 1 | 52% | 160 |
| deeplethe/forkd | 78 | Hot | very active | 1 | 85% | 23 |
| agent0ai/agent-zero | 78 | Mature | very active | 1 | 97% | 67 |
| 1jehuang/jcode | 77 | Rising | very active | 1 | 100% | 127 |
| SafeRL-Lab/cheetahclaws | 76 | Hot | very active | 1 | 86% | 39 |
| ruvnet/ruflo | 76 | Hot | very active | 1 | 97% | 1583 |
| pydantic/pydantic-ai-harness | 75 | Hot | very active | 2 | 31% | 11 |
| gsd-build/gsd-2 | 75 | Rising | active | 1 | 76% | 116 |
| trycua/cua | 75 | Hot | very active | 1 | 50% | 560 |
| emcie-co/parlant | 73 | Mature | very active | 1 | 63% | 33 |
| cobusgreyling/loop-engineering | 70 | Hot | very active | 2 | 27% | 1 |
| AndyMik90/Aperant | 57 | Declining | active | 1 | 100% | 37 |
| BloopAI/vibe-kanban | 54 | Mature | slowing | 1 | 83% | 284 |
| hexo-ai/sia | 54 | Rising | very active | 2 | 35% | 0 |
| dagger/container-use | 44 | Declining | active | 1 | 100% | 14 |
| automazeio/ccpm | 30 | Declining | slowing | 0 | 0% | 0 |
| agentsmd/agents.md | 21 | Declining | slowing | 0 | 0% | 0 |
| aniketkarne/ClaudeNightsWatch | 21 | Declining | stale | 0 | 0% | 0 |

## Which one should you use?

| If you want… | Start with | Why |
|---|---|---|
| A harness you fully own, in code | `langchain-ai/deepagents` or `earendil-works/pi` | Batteries-included loops with planning and sub-agents; pi adds a unified LLM API + TUI. |
| More out of the Claude Code you already run | `obra/superpowers` (+ `affaan-m/ECC`) | Skills + methodology layered on today; ECC adds memory, instincts, and hooks. |
| Swarms / heavy multi-agent coordination | `ruvnet/ruflo` | The meta-harness with the deepest swarm tooling in your stars. |
| A team of agents working a backlog | `BloopAI/vibe-kanban` | Kanban-shaped orchestration over Claude Code/Codex; `ccpm` if you prefer GitHub Issues + worktrees. |
| Reproducible, auditable agent output | `github/spec-kit` + `agentsmd/agents.md` | Spec-driven development plus the portable AGENTS.md behavior contract. |
| Crash-proof long tasks | `OthmanAdi/planning-with-files` | Plans persisted to disk — resume after any failure. |
| Safe execution for untrusted agent code | `daytonaio/daytona` | Purpose-built elastic sandbox infra; `forkd` when you need 100 microVMs in 100ms. |
| A 24/7 resident agent | `stakpak/agent` (or `aniketkarne/ClaudeNightsWatch`) | Daemon-style autonomy; NightsWatch exploits idle Claude usage windows overnight. |
| Research-grade long-horizon autonomy | `bytedance/deer-flow` | SuperAgent harness with sub-agents and sandboxes; strongest end-to-end autonomy here. |

## Adjacent (deliberately not listed as harnesses)

- **langchain-ai/langgraph** (37,654★) — agent *framework* (graphs, not harnesses) — see the agent-orchestration report
- **crewAIInc/crewAI** (55,823★) — role-playing agent framework — agent-orchestration report
- **microsoft/autogen** (59,832★) — multi-agent conversation framework — agent-orchestration report
- **eigent-ai/eigent** (14,613★) — cowork desktop product — agent-orchestration report
- **getpaseo/paseo** (10,891★) — desktop/mobile agent orchestrator — agent-orchestration report
- **wshobson/agents** (38,069★) — multi-harness plugin *marketplace* — content for harnesses, not a harness
- **EleutherAI/lm-evaluation-harness** (13,339★) — 'harness' for *model benchmarks*, not agent runtimes — see the LLM-evaluation report
- **anthropics/claude-code** (138,390★) — the coding agent itself — the thing meta-harnesses wrap

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (harness / autonomous / swarm / multi-agent / sandbox / worktree / spec-driven / long-horizon / loop…) + manual curation by *approach*. General agent frameworks and orchestration platforms live in the agent-orchestration report; Claude-Code configuration setups in the claude-code-setups report. A few boundary projects (`deer-flow`, `ruflo`, `oh-my-*`) appear in both, viewed through different lenses.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 36 · Snapshot: 2026-07-20T08:33:57.852Z</sub>
