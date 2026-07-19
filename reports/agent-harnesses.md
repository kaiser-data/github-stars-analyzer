# Agent Harnesses — Six Approaches to Running Autonomous Agents

> Derived from **kaiser-data**'s 1,327 starred repos (snapshot `2026-07-13T08:42:30.177Z`), cross-referenced with the repo-similarity graph (1,327 nodes / 4,302 edges, 26 communities).
>
> Generated 2026-07-19 by `scripts/reports/agent_harnesses.py` (regenerate any time — no API cost).

![Top tools by stars](assets/agent-harnesses-top-tools.svg)

![Tools per category](assets/agent-harnesses-categories.svg)


## Executive summary

- A **harness** is everything around the model: the loop, tools, state, guardrails, and execution environment. **35 harness projects** in your stars (**1,328,972★** combined) cluster into **six distinct approaches** — they disagree about *where the harness lives* and *what the hard problem is*:
  - **Harness-as-SDK** (7): `pi`, `deepagents`, `parlant`, `harness-sdk`, `eve`, `cheetahclaws`, `pydantic-ai-harness`
  - **Meta-harness over coding agents** (6): `superpowers`, `ECC`, `oh-my-openagent`, `ruflo`, `oh-my-claudecode`, `Archon`
  - **Fleet / parallel orchestration** (7): `multica`, `vibe-kanban`, `gastown`, `Aperant`, `ccpm`, `agent-orchestrator`, `container-use`
  - **Determinism & spec-driven** (5): `spec-kit`, `planning-with-files`, `agents.md`, `gsd-2`, `loop-engineering`
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
| [obra/superpowers](https://github.com/obra/superpowers) | Meta-harness over coding agents | Shell | MIT | 253,346 (▲28,612) | Hot | 78 | very active | 3d ago | 9mo | 3 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Meta-harness over coding agents | JavaScript | MIT | 229,056 (▲15,622) | Hot | 90 | very active | 0d ago | 5mo | 35 |
| [github/spec-kit](https://github.com/github/spec-kit) | Determinism & spec-driven | Python | MIT | 120,147 (▲8,672) | Hot | 93 | very active | 3d ago | 10mo | 18 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Autonomous long-horizon | Python | MIT | 76,889 (▲5,901) | Hot | 79 | very active | 0d ago | 1.2y | 24 |
| [daytonaio/daytona](https://github.com/daytonaio/daytona) | Sandbox substrate | — | — | 72,197 (▼261) | Mature | 97 | very active | 4d ago | 2.4y | 21 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness-as-SDK | TypeScript | MIT | 70,188 (▲8,410) | Hot | 85 | very active | 0d ago | 11mo | 16 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Meta-harness over coding agents | TypeScript | NOASSERTION | 65,655 (▲3,730) | Hot | 78 | very active | 0d ago | 7mo | 4 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Meta-harness over coding agents | TypeScript | MIT | 64,230 (▲5,237) | Mature | 76 | very active | 0d ago | 1.1y | 2 |
| [multica-ai/multica](https://github.com/multica-ai/multica) | Fleet / parallel orchestration | Go | NOASSERTION | 40,056 (▲3,769) | Hot | 81 | very active | 0d ago | 6mo | 15 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Meta-harness over coding agents | TypeScript | MIT | 37,719 (▲1,498) | Hot | 80 | very active | 0d ago | 6mo | 18 |
| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Fleet / parallel orchestration | Rust | Apache-2.0 | 27,351 (▲413) | Mature | 58 | slowing | 2mo ago | 1.1y | 2 |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Harness-as-SDK | Python | MIT | 26,162 (▲1,676) | Hot | 79 | very active | 0d ago | 11mo | 14 |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | Determinism & spec-driven | Python | MIT | 25,254 (▲2,207) | Hot | 78 | very active | 0d ago | 6mo | 21 |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | Determinism & spec-driven | TypeScript | MIT | 22,981 (▲831) | Declining | 21 | slowing | 4mo ago | 10mo | 0 |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Meta-harness over coding agents | TypeScript | MIT | 22,862 (▲515) | Hot | 77 | very active | 2d ago | 1.4y | 9 |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Sandbox substrate | TypeScript | Apache-2.0 | 21,759 (▲627) | Hot | 74 | very active | 0d ago | 4mo | 27 |
| [trycua/cua](https://github.com/trycua/cua) | Sandbox substrate | HTML | MIT | 19,602 (▲1,763) | Hot | 76 | very active | 0d ago | 1.4y | 8 |
| [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | Autonomous long-horizon | Python | NOASSERTION | 18,408 (▲380) | Mature | 78 | very active | 1d ago | 2.1y | 1 |
| [emcie-co/parlant](https://github.com/emcie-co/parlant) | Harness-as-SDK | Python | Apache-2.0 | 18,172 (▲63) | Mature | 75 | very active | 1d ago | 2.4y | 8 |
| [gastownhall/gastown](https://github.com/gastownhall/gastown) | Fleet / parallel orchestration | Go | MIT | 16,990 | Hot | 78 | very active | 3d ago | 6mo | 5 |
| [AndyMik90/Aperant](https://github.com/AndyMik90/Aperant) | Fleet / parallel orchestration | TypeScript | AGPL-3.0 | 14,443 (▲102) | Declining | 58 | active | 29d ago | 7mo | 1 |
| [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | Sandbox substrate | Python | Apache-2.0 | 11,976 (▲512) | Hot | 78 | very active | 0d ago | 6mo | 9 |
| [automazeio/ccpm](https://github.com/automazeio/ccpm) | Fleet / parallel orchestration | Shell | MIT | 8,261 (▲76) | Declining | 30 | slowing | 3mo ago | 10mo | 0 |
| [AgentWrapper/agent-orchestrator](https://github.com/AgentWrapper/agent-orchestrator) | Fleet / parallel orchestration | Go | Apache-2.0 | 8,222 (▲714) | Hot | 97 | very active | 0d ago | 5mo | 26 |
| [gsd-build/gsd-2](https://github.com/gsd-build/gsd-2) | Determinism & spec-driven | TypeScript | MIT | 7,744 (▲7) | Rising | 76 | active | 1mo ago | 4mo | 2 |
| [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | Determinism & spec-driven | JavaScript | MIT | 7,233 | Hot | 69 | very active | 0d ago | 1mo | 18 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | Harness-as-SDK | Python | Apache-2.0 | 6,545 (▲438) | Hot | 92 | very active | 0d ago | 1.2y | 25 |
| [dagger/container-use](https://github.com/dagger/container-use) | Fleet / parallel orchestration | Go | Apache-2.0 | 3,911 (▲79) | Declining | 49 | active | 1mo ago | 1.1y | 1 |
| [vercel/eve](https://github.com/vercel/eve) | Harness-as-SDK | TypeScript | Apache-2.0 | 3,460 | Hot | 83 | very active | 0d ago | 27d | 21 |
| [deeplethe/forkd](https://github.com/deeplethe/forkd) | Sandbox substrate | Rust | Apache-2.0 | 2,717 (▲551) | Hot | 78 | very active | 4d ago | 2mo | 5 |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | Autonomous long-horizon | Python | MIT | 2,011 (▲789) | Rising | 54 | very active | 11d ago | 3mo | 8 |
| [stakpak/agent](https://github.com/stakpak/agent) | Autonomous long-horizon | Rust | Apache-2.0 | 1,655 (▲59) | Hot | 81 | very active | 7d ago | 1.6y | 6 |
| [SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws) | Harness-as-SDK | Python | Apache-2.0 | 757 (▲36) | Hot | 76 | very active | 2d ago | 3mo | 5 |
| [pydantic/pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness) | Harness-as-SDK | Python | MIT | 644 (▲105) | Hot | 73 | very active | 1d ago | 3mo | 9 |
| [aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch) | Autonomous long-horizon | Shell | MIT | 369 | Declining | 22 | slowing | 6mo ago | 12mo | 0 |

## By approach

### Harness-as-SDK

_The loop as a library: you import the harness, register tools, and own control flow. Maximum flexibility, maximum responsibility — you maintain planning, retries, memory, and safety yourself._

- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 70,188★ · TypeScript · Hot  
  Unified LLM API + agent loop + TUI + coding-agent CLI in one toolkit — the loop as a library.  
  <sub>topics: —</sub>
- **[langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)** · 26,162★ · Python · Hot  
  The 'batteries-included agent harness' — planning, sub-agents, filesystem, from the LangChain team.  
  <sub>topics: deepagents, langchain, langgraph, ai, python, typescript</sub>
- **[emcie-co/parlant](https://github.com/emcie-co/parlant)** · 18,172★ · Python · Mature  
  Interaction *control* harness — behavioral guidelines enforced at runtime for customer-facing agents.  
  <sub>topics: ai-agents, genai, llm, customer-service, customer-success, gemini, llama3, openai</sub>
- **[strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)** · 6,545★ · Python · Hot  
  AWS's open SDK to build an agent harness and control it end-to-end in production.  
  <sub>topics: agentic, agentic-ai, agents, ai, autonomous-agents, llm, multi-agent-systems, python</sub>
- **[vercel/eve](https://github.com/vercel/eve)** · 3,460★ · TypeScript · Hot  
  Vercel's framework for building agents — harness + sandbox as one integrated runtime.  
  <sub>topics: agent, framework, harness, javascript, markdown, typescript, vercel, sandbox</sub>
- **[SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws)** · 757★ · Python · Hot  
  Fast, easy agent-harness infrastructure aimed at long-horizon, multi-model runs.  
  <sub>topics: agentic-ai, claude, claude-code, memory, python, skills, openclaw</sub>
- **[pydantic/pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness)** · 644★ · Python · Hot  
  'Batteries for your Pydantic AI agent' — the harness as a thin add-on to a typed agent framework.  
  <sub>topics: —</sub>

### Meta-harness over coding agents

_These projects treat Claude Code / Codex as the engine and build the transmission: skills, personas, memory, token discipline, and multi-agent coordination injected via configs, hooks, and subagents._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 253,346★ · Shell · Hot  
  Skills framework + development methodology layered onto the agent you already run.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 229,056★ · JavaScript · Hot  
  Harness performance optimization: skills, instincts, memory, security, hooks on top of Claude Code.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 65,655★ · TypeScript · Hot  
  'The one and only agent harness for complex coding' — tokenmaxxer harness wrapping coding agents.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 64,230★ · TypeScript · Mature  
  The leading agent *meta*-harness — swarms, coordination, and autonomy on top of existing agents.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 37,719★ · TypeScript · Hot  
  Teams-first multi-agent orchestration living entirely inside Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>
- **[coleam00/Archon](https://github.com/coleam00/Archon)** · 22,862★ · TypeScript · Hot  
  'Harness builder' — make AI coding deterministic and repeatable by generating the harness itself.  
  <sub>topics: ai, automation, bun, claude, cli, coding-assistant, developer-tools, typescript</sub>

### Fleet / parallel orchestration

_One agent is a tool; a fleet is a team. The harness problem becomes scheduling, isolation (worktrees, containers), review queues, and merge discipline._

- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 40,056★ · Go · Hot  
  Managed-agents platform: assign tasks to coding agents like teammates and supervise them.  
  <sub>topics: —</sub>
- **[BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban)** · 27,351★ · Rust · Mature  
  A kanban board as the harness — queue, run, and review many agent tasks in parallel.  
  <sub>topics: agent, ai-agents, kanban, management, task-manager</sub>
- **[gastownhall/gastown](https://github.com/gastownhall/gastown)** · 16,990★ · Go · Hot  
  Multi-agent workspace manager — the 'town' where a fleet of agents live and work.  
  <sub>topics: —</sub>
- **[AndyMik90/Aperant](https://github.com/AndyMik90/Aperant)** · 14,443★ · TypeScript · Declining  
  Autonomous multi-session AI coding — sessions as the unit of parallelism.  
  <sub>topics: —</sub>
- **[automazeio/ccpm](https://github.com/automazeio/ccpm)** · 8,261★ · Shell · Declining  
  GitHub Issues + git worktrees as the coordination fabric for parallel agents.  
  <sub>topics: ai-agents, ai-coding, claude, claude-code, project-management, vibe-coding</sub>
- **[AgentWrapper/agent-orchestrator](https://github.com/AgentWrapper/agent-orchestrator)** · 8,222★ · Go · Hot  
  Plans tasks, spawns parallel coding agents in worktrees, merges autonomously.  
  <sub>topics: claude-code, codex-cli, orchestration, orchestrator, skills, agent-fleet, agent-swarm, git-worktrees</sub>
- **[dagger/container-use](https://github.com/dagger/container-use)** · 3,911★ · Go · Declining  
  Containerized dev environments so multiple agents work safely and independently.  
  <sub>topics: —</sub>

### Determinism & spec-driven

_The counter-culture: agents drift, so pin them down. Specs, standards files, and plans persisted to disk make runs reproducible, auditable, and resumable after crashes._

- **[github/spec-kit](https://github.com/github/spec-kit)** · 120,147★ · Python · Hot  
  Spec-Driven Development toolkit — the spec, not the prompt, steers the agent.  
  <sub>topics: ai, copilot, development, engineering, prd, spec, spec-driven</sub>
- **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** · 25,254★ · Python · Hot  
  Persistent file-based planning — crash-proof, resumable long-running agent tasks.  
  <sub>topics: claude, claude-code, claude-skills, manus, agent-skills, planning, copilot, pi</sub>
- **[agentsmd/agents.md](https://github.com/agentsmd/agents.md)** · 22,981★ · TypeScript · Declining  
  The open AGENTS.md standard — a portable contract telling any harness how to behave in a repo.  
  <sub>topics: —</sub>
- **[gsd-build/gsd-2](https://github.com/gsd-build/gsd-2)** · 7,744★ · TypeScript · Rising  
  Meta-prompting + context engineering + spec-driven system for dependable outcomes.  
  <sub>topics: context-engineering, meta-prompting, spec-driven-development</sub>
- **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** · 7,233★ · JavaScript · Hot  
  Patterns and starters for *loop engineering* — designing the iteration, not just the prompt.  
  <sub>topics: agentic-ai, ai-agents, claude-code, codex, devops-automation, github-actions, grok, llm</sub>

### Sandbox substrate

_Infrastructure-first: before you scale agents you need somewhere safe and fast to run them. MicroVMs, container runtimes, and hardened sandboxes are the harness's floor._

- **[daytonaio/daytona](https://github.com/daytonaio/daytona)** · 72,197★ · — · Mature  
  Secure, elastic infrastructure for running AI-generated code — the harness's execution floor.  
  <sub>topics: developer-tools, agentic-workflow, ai, ai-agents, ai-runtime, code-execution, code-interpreter, ai-sandboxes</sub>
- **[NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)** · 21,759★ · TypeScript · Hot  
  Run harnesses (Hermes, Deep Agents, OpenClaw) inside hardened NVIDIA sandboxes.  
  <sub>topics: ai-agents, nvidia, openclaw, openshell, sandboxing, typescript, hermes</sub>
- **[trycua/cua](https://github.com/trycua/cua)** · 19,602★ · HTML · Hot  
  Sandboxes, SDKs, and benchmarks for computer-use agents — full-desktop harnessing.  
  <sub>topics: apple, cua, lume, macos, virtualization, virtualization-framework, swift, ai-agent</sub>
- **[opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)** · 11,976★ · Python · Hot  
  Secure, fast, extensible sandbox runtime purpose-built for AI agents.  
  <sub>topics: ai, ai-infra, kubernetes, sandbox, ai-agent</sub>
- **[deeplethe/forkd](https://github.com/deeplethe/forkd)** · 2,717★ · Rust · Hot  
  fork() for agent microVMs — spawn 100 children in ~100ms; branch a live VM mid-run.  
  <sub>topics: ai-agents, copy-on-write, kvm, microvm, rust, sandbox, snapshot</sub>

### Autonomous long-horizon

_Maximum autonomy: agents that run for hours or days, planning and re-planning, sometimes improving their own scaffolding. The harness is a resident process, not a CLI invocation._

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 76,889★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and creates with sub-agents in sandboxes.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[agent0ai/agent-zero](https://github.com/agent0ai/agent-zero)** · 18,408★ · Python · Mature  
  General autonomous framework — the agent builds its own tools as it goes.  
  <sub>topics: agent, ai, assistant, autonomous, linux, zero</sub>
- **[hexo-ai/sia](https://github.com/hexo-ai/sia)** · 2,011★ · Python · Rising  
  Self-Improving AI — a harness whose loop optimizes the underlying system over time.  
  <sub>topics: —</sub>
- **[stakpak/agent](https://github.com/stakpak/agent)** · 1,655★ · Rust · Hot  
  An agent that lives on your machines 24/7 and keeps shipping — harness as a resident daemon.  
  <sub>topics: agent, devops, devtool, generative-ai, hacktoberfest, ai-agent, autonomous-agent, llm-agent</sub>
- **[aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch)** · 369★ · Shell · Declining  
  Watches your Claude usage windows and executes queued tasks autonomously overnight.  
  <sub>topics: —</sub>

## Graph analysis — how they relate

**Community clustering.** These 35 tools span **14 of the graph's 26 communities**.

- **Community 16** (9): `earendil-works/pi`, `SafeRL-Lab/cheetahclaws`, `code-yeongyu/oh-my-openagent`, `ruvnet/ruflo`, `coleam00/Archon`, `gastownhall/gastown`, `AgentWrapper/agent-orchestrator`, `trycua/cua`, `opensandbox-group/OpenSandbox`
- **Community 8** (6): `affaan-m/ECC`, `AndyMik90/Aperant`, `OthmanAdi/planning-with-files`, `agentsmd/agents.md`, `cobusgreyling/loop-engineering`, `agent0ai/agent-zero`
- **Community 1** (4): `pydantic/pydantic-ai-harness`, `obra/superpowers`, `daytonaio/daytona`, `deeplethe/forkd`
- **Community 7** (3): `langchain-ai/deepagents`, `gsd-build/gsd-2`, `bytedance/deer-flow`
- **Community 17** (2): `emcie-co/parlant`, `strands-agents/harness-sdk`
- **Community 18** (2): `Yeachan-Heo/oh-my-claudecode`, `automazeio/ccpm`
- **Community 3** (2): `multica-ai/multica`, `BloopAI/vibe-kanban`

**Centrality (PageRank in the full 1,327-repo graph)** — most 'hub-like' harnesses in your ecosystem:

- `langchain-ai/deepagents` — PageRank 0.0023
- `affaan-m/ECC` — PageRank 0.0022
- `NVIDIA/NemoClaw` — PageRank 0.0016
- `cobusgreyling/loop-engineering` — PageRank 0.0014
- `code-yeongyu/oh-my-openagent` — PageRank 0.0012
- `coleam00/Archon` — PageRank 0.0010
- `bytedance/deer-flow` — PageRank 0.0010
- `stakpak/agent` — PageRank 0.0008
- `hexo-ai/sia` — PageRank 0.0008
- `OthmanAdi/planning-with-files` — PageRank 0.0008

**Direct links between harness projects** (top similarity edges where both endpoints are in this report):

- `cobusgreyling/loop-engineering` ⇄ `affaan-m/ECC` (w=0.404) — topics: ai-agents, claude-code, llm, mcp; authors: dependabot[bot]
- `bytedance/deer-flow` ⇄ `langchain-ai/deepagents` (w=0.367) — topics: ai, langchain, langgraph, python; authors: dependabot[bot]
- `code-yeongyu/oh-my-openagent` ⇄ `coleam00/Archon` (w=0.353) — topics: ai, claude, typescript; authors: github-actions[bot]
- `Yeachan-Heo/oh-my-claudecode` ⇄ `automazeio/ccpm` (w=0.333) — topics: ai-agents, claude, claude-code, vibe-coding
- `affaan-m/ECC` ⇄ `automazeio/ccpm` (w=0.273) — topics: ai-agents, claude, claude-code
- `strands-agents/harness-sdk` ⇄ `ruvnet/ruflo` (w=0.212) — topics: agentic-ai, agents, autonomous-agents, multi-agent-systems
- `bytedance/deer-flow` ⇄ `ruvnet/ruflo` (w=0.188) — topics: agentic-framework, agentic-workflow, ai-agents, multi-agent

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Harnesses are a young, fast-moving category — expect churn; check lifecycle before betting on one.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| AgentWrapper/agent-orchestrator | 97 | Hot | very active | 6 | 16% | 70 |
| daytonaio/daytona | 97 | Mature | very active | 5 | 14% | 205 |
| github/spec-kit | 93 | Hot | very active | 4 | 18% | 187 |
| strands-agents/harness-sdk | 92 | Hot | very active | 4 | 22% | 72 |
| affaan-m/ECC | 90 | Hot | very active | 3 | 35% | 14 |
| earendil-works/pi | 85 | Hot | very active | 2 | 44% | 243 |
| vercel/eve | 83 | Hot | very active | 3 | 23% | 53 |
| multica-ai/multica | 81 | Hot | very active | 2 | 39% | 111 |
| stakpak/agent | 81 | Hot | very active | 2 | 49% | 315 |
| Yeachan-Heo/oh-my-claudecode | 80 | Hot | very active | 1 | 52% | 238 |
| langchain-ai/deepagents | 79 | Hot | very active | 1 | 65% | 213 |
| bytedance/deer-flow | 79 | Hot | very active | 4 | 20% | 1 |
| obra/superpowers | 78 | Hot | very active | 1 | 69% | 10 |
| code-yeongyu/oh-my-openagent | 78 | Hot | very active | 1 | 95% | 217 |
| gastownhall/gastown | 78 | Hot | very active | 1 | 55% | 14 |
| OthmanAdi/planning-with-files | 78 | Hot | very active | 1 | 70% | 76 |
| opensandbox-group/OpenSandbox | 78 | Hot | very active | 1 | 53% | 160 |
| deeplethe/forkd | 78 | Hot | very active | 1 | 85% | 23 |
| agent0ai/agent-zero | 78 | Mature | very active | 1 | 100% | 66 |
| coleam00/Archon | 77 | Hot | very active | 1 | 83% | 15 |
| SafeRL-Lab/cheetahclaws | 76 | Hot | very active | 1 | 86% | 39 |
| ruvnet/ruflo | 76 | Mature | very active | 1 | 98% | 1571 |
| gsd-build/gsd-2 | 76 | Rising | active | 1 | 76% | 116 |
| trycua/cua | 76 | Hot | very active | 1 | 82% | 552 |
| emcie-co/parlant | 75 | Mature | very active | 1 | 66% | 33 |
| NVIDIA/NemoClaw | 74 | Hot | very active | 3 | 34% | 0 |
| pydantic/pydantic-ai-harness | 73 | Hot | very active | 2 | 30% | 9 |
| cobusgreyling/loop-engineering | 69 | Hot | very active | 2 | 40% | 1 |
| BloopAI/vibe-kanban | 58 | Mature | slowing | 1 | 85% | 284 |
| AndyMik90/Aperant | 58 | Declining | active | 1 | 100% | 37 |
| hexo-ai/sia | 54 | Rising | very active | 2 | 35% | 0 |
| dagger/container-use | 49 | Declining | active | 1 | 100% | 14 |
| automazeio/ccpm | 30 | Declining | slowing | 0 | 0% | 0 |
| aniketkarne/ClaudeNightsWatch | 22 | Declining | slowing | 0 | 0% | 0 |
| agentsmd/agents.md | 21 | Declining | slowing | 0 | 0% | 0 |

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

- **langchain-ai/langgraph** (37,147★) — agent *framework* (graphs, not harnesses) — see the agent-orchestration report
- **crewAIInc/crewAI** (55,417★) — role-playing agent framework — agent-orchestration report
- **microsoft/autogen** (59,693★) — multi-agent conversation framework — agent-orchestration report
- **eigent-ai/eigent** (14,553★) — cowork desktop product — agent-orchestration report
- **getpaseo/paseo** (10,300★) — desktop/mobile agent orchestrator — agent-orchestration report
- **wshobson/agents** (37,852★) — multi-harness plugin *marketplace* — content for harnesses, not a harness
- **EleutherAI/lm-evaluation-harness** (13,267★) — 'harness' for *model benchmarks*, not agent runtimes — see the LLM-evaluation report
- **anthropics/claude-code** (137,635★) — the coding agent itself — the thing meta-harnesses wrap

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (harness / autonomous / swarm / multi-agent / sandbox / worktree / spec-driven / long-horizon / loop…) + manual curation by *approach*. General agent frameworks and orchestration platforms live in the agent-orchestration report; Claude-Code configuration setups in the claude-code-setups report. A few boundary projects (`deer-flow`, `ruflo`, `oh-my-*`) appear in both, viewed through different lenses.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 35 · Snapshot: 2026-07-13T08:42:30.177Z</sub>
