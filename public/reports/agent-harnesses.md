# Agent Harnesses — Six Approaches to Running Autonomous Agents

> Derived from **kaiser-data**'s 1,857 starred repos (snapshot `2026-08-29T15:31:31.780Z`), cross-referenced with the repo-similarity graph (1,857 nodes / 6,041 edges, 37 communities).
>
> Generated 2026-08-29 by `scripts/reports/agent_harnesses.py` (regenerate any time — no API cost).

![Top tools by stars](assets/agent-harnesses-top-tools.svg)

![Tools per category](assets/agent-harnesses-categories.svg)


## Executive summary

- A **harness** is everything around the model: the loop, tools, state, guardrails, and execution environment. **36 harness projects** in your stars (**1,472,558★** combined) cluster into **six distinct approaches** — they disagree about *where the harness lives* and *what the hard problem is*:
  - **Harness-as-SDK** (8): `pi`, `deepagents`, `jcode`, `parlant`, `harness-sdk`, `eve`, `pydantic-ai-harness`, `cheetahclaws`
  - **Meta-harness over coding agents** (6): `superpowers`, `ECC`, `ruflo`, `oh-my-openagent`, `oh-my-claudecode`, `Archon`
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
| [obra/superpowers](https://github.com/obra/superpowers) | Meta-harness over coding agents | Shell | MIT | 279,271 (▲610) | Hot | 79 | very active | 1d ago | 10mo | 6 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Meta-harness over coding agents | JavaScript | MIT | 244,094 (▲329) | Hot | 79 | very active | 0d ago | 7mo | 20 |
| [github/spec-kit](https://github.com/github/spec-kit) | Determinism & spec-driven | Python | MIT | 132,136 (▲235) | Hot | 84 | very active | 1d ago | 1.0y | 18 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness-as-SDK | TypeScript | MIT | 99,005 (▲694) | Hot | 85 | very active | 0d ago | 1.1y | 13 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Autonomous long-horizon | Python | MIT | 81,091 (▲73) | Hot | 84 | very active | 0d ago | 1.3y | 53 |
| [daytonaio/daytona](https://github.com/daytonaio/daytona) | Sandbox substrate | — | — | 71,857 (▼1) | Mature | 94 | active | 1mo ago | 2.6y | 21 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Meta-harness over coding agents | TypeScript | MIT | 69,703 (▲135) | Hot | 76 | very active | 0d ago | 1.2y | 7 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Meta-harness over coding agents | TypeScript | NOASSERTION | 68,499 (▲50) | Hot | 78 | very active | 0d ago | 9mo | 5 |
| [multica-ai/multica](https://github.com/multica-ai/multica) | Fleet / parallel orchestration | Go | NOASSERTION | 48,215 (▲199) | Hot | 86 | very active | 1d ago | 7mo | 32 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Meta-harness over coding agents | TypeScript | MIT | 38,867 (▲39) | Hot | 80 | very active | 1d ago | 7mo | 4 |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Harness-as-SDK | Python | MIT | 28,691 (▲81) | Hot | 79 | very active | 0d ago | 1.1y | 7 |
| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Fleet / parallel orchestration | Rust | Apache-2.0 | 27,949 (▲6) | Declining | 40 | slowing | 4mo ago | 1.2y | 0 |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | Determinism & spec-driven | Shell | MIT | 26,413 (▲26) | Hot | 79 | very active | 0d ago | 7mo | 14 |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | Determinism & spec-driven | TypeScript | MIT | 23,976 (▲23) | Declining | 38 | active | 4d ago | 1.0y | 1 |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Meta-harness over coding agents | TypeScript | MIT | 23,302 (▲8) | Mature | 78 | very active | 0d ago | 1.6y | 1 |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Sandbox substrate | TypeScript | Apache-2.0 | 22,304 (▲8) | Hot | 74 | very active | 0d ago | 5mo | 16 |
| [trycua/cua](https://github.com/trycua/cua) | Sandbox substrate | HTML | MIT | 22,005 (▲57) | Hot | 80 | very active | 0d ago | 1.6y | 15 |
| [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | Autonomous long-horizon | Python | NOASSERTION | 19,010 (▲23) | Mature | 79 | very active | 2d ago | 2.2y | 9 |
| [1jehuang/jcode](https://github.com/1jehuang/jcode) | Harness-as-SDK | Rust | MIT | 18,775 (▲67) | Rising | 76 | very active | 0d ago | 7mo | 2 |
| [emcie-co/parlant](https://github.com/emcie-co/parlant) | Harness-as-SDK | Python | Apache-2.0 | 18,270 (▲1) | Mature | 62 | active | 1mo ago | 2.5y | 3 |
| [gastownhall/gastown](https://github.com/gastownhall/gastown) | Fleet / parallel orchestration | Go | MIT | 17,832 (▲20) | Hot | 76 | very active | 10d ago | 8mo | 9 |
| [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | Sandbox substrate | Go | Apache-2.0 | 14,808 (▲38) | Hot | 83 | very active | 1d ago | 8mo | 11 |
| [AndyMik90/Aperant](https://github.com/AndyMik90/Aperant) | Fleet / parallel orchestration | TypeScript | AGPL-3.0 | 14,541 (▲3) | Declining | 54 | slowing | 2mo ago | 8mo | 1 |
| [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | Determinism & spec-driven | TypeScript | MIT | 10,730 (▲22) | Hot | 73 | very active | 1d ago | 2mo | 14 |
| [Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) | Fleet / parallel orchestration | Go | Apache-2.0 | 10,484 (▲343) | Hot | 97 | very active | 0d ago | 6mo | 20 |
| [automazeio/ccpm](https://github.com/automazeio/ccpm) | Fleet / parallel orchestration | Shell | MIT | 8,357 (▲7) | Declining | 26 | slowing | 5mo ago | 1.0y | 0 |
| [gsd-build/gsd-2](https://github.com/gsd-build/gsd-2) | Determinism & spec-driven | TypeScript | MIT | 7,771 (▲4) | Declining | 47 | slowing | 3mo ago | 5mo | 0 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | Harness-as-SDK | Python | Apache-2.0 | 7,044 (▲11) | Hot | 97 | very active | 1d ago | 1.3y | 35 |
| [vercel/eve](https://github.com/vercel/eve) | Harness-as-SDK | TypeScript | Apache-2.0 | 4,864 (▲26) | Hot | 95 | very active | 0d ago | 2mo | 21 |
| [dagger/container-use](https://github.com/dagger/container-use) | Fleet / parallel orchestration | Go | Apache-2.0 | 4,022 (▲1) | Mature | 46 | active | 12d ago | 1.3y | 3 |
| [deeplethe/forkd](https://github.com/deeplethe/forkd) | Sandbox substrate | Rust | Apache-2.0 | 2,815 (▲43) | Hot | 83 | very active | 7d ago | 3mo | 7 |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | Autonomous long-horizon | Python | MIT | 2,126 (▲1) | Rising | 55 | very active | 3d ago | 5mo | 10 |
| [stakpak/agent](https://github.com/stakpak/agent) | Autonomous long-horizon | Rust | Apache-2.0 | 1,759 (▲2) | Hot | 65 | active | 1mo ago | 1.7y | 3 |
| [pydantic/pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness) | Harness-as-SDK | Python | MIT | 834 (▲6) | Hot | 79 | very active | 1d ago | 5mo | 17 |
| [SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws) | Harness-as-SDK | Python | Apache-2.0 | 768 | Hot | 76 | very active | 3d ago | 5mo | 7 |
| [aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch) | Autonomous long-horizon | Shell | MIT | 370 | Declining | 18 | stale | 7mo ago | 1.1y | 0 |

## By approach

### Harness-as-SDK

_The loop as a library: you import the harness, register tools, and own control flow. Maximum flexibility, maximum responsibility — you maintain planning, retries, memory, and safety yourself._

- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 99,005★ · TypeScript · Hot  
  Unified LLM API + agent loop + TUI + coding-agent CLI in one toolkit — the loop as a library.  
  <sub>topics: —</sub>
- **[langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)** · 28,691★ · Python · Hot  
  The 'batteries-included agent harness' — planning, sub-agents, filesystem, from the LangChain team.  
  <sub>topics: deepagents, langchain, langgraph, ai, python, typescript, harness, harness-engineering</sub>
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 18,775★ · Rust · Rising  
  Rust-built coding-agent harness — CLI agent loop with MCP support and multi-model wiring.  
  <sub>topics: ai, claude, cli, coding-agent, llm, mcp, openai, rust</sub>
- **[emcie-co/parlant](https://github.com/emcie-co/parlant)** · 18,270★ · Python · Mature  
  Interaction *control* harness — behavioral guidelines enforced at runtime for customer-facing agents.  
  <sub>topics: ai-agents, genai, llm, customer-service, customer-success, gemini, llama3, openai</sub>
- **[strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)** · 7,044★ · Python · Hot  
  AWS's open SDK to build an agent harness and control it end-to-end in production.  
  <sub>topics: agentic, agentic-ai, agents, ai, autonomous-agents, llm, multi-agent-systems, python</sub>
- **[vercel/eve](https://github.com/vercel/eve)** · 4,864★ · TypeScript · Hot  
  Vercel's framework for building agents — harness + sandbox as one integrated runtime.  
  <sub>topics: agent, framework, harness, javascript, markdown, typescript, vercel, sandbox</sub>
- **[pydantic/pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness)** · 834★ · Python · Hot  
  'Batteries for your Pydantic AI agent' — the harness as a thin add-on to a typed agent framework.  
  <sub>topics: —</sub>
- **[SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws)** · 768★ · Python · Hot  
  Fast, easy agent-harness infrastructure aimed at long-horizon, multi-model runs.  
  <sub>topics: agentic-ai, claude, claude-code, memory, python, skills, openclaw</sub>

### Meta-harness over coding agents

_These projects treat Claude Code / Codex as the engine and build the transmission: skills, personas, memory, token discipline, and multi-agent coordination injected via configs, hooks, and subagents._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 279,271★ · Shell · Hot  
  Skills framework + development methodology layered onto the agent you already run.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 244,094★ · JavaScript · Hot  
  Harness performance optimization: skills, instincts, memory, security, hooks on top of Claude Code.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 69,703★ · TypeScript · Hot  
  The leading agent *meta*-harness — swarms, coordination, and autonomy on top of existing agents.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 68,499★ · TypeScript · Hot  
  'The one and only agent harness for complex coding' — tokenmaxxer harness wrapping coding agents.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 38,867★ · TypeScript · Hot  
  Teams-first multi-agent orchestration living entirely inside Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>
- **[coleam00/Archon](https://github.com/coleam00/Archon)** · 23,302★ · TypeScript · Mature  
  'Harness builder' — make AI coding deterministic and repeatable by generating the harness itself.  
  <sub>topics: ai, automation, bun, claude, cli, coding-assistant, developer-tools, typescript</sub>

### Fleet / parallel orchestration

_One agent is a tool; a fleet is a team. The harness problem becomes scheduling, isolation (worktrees, containers), review queues, and merge discipline._

- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 48,215★ · Go · Hot  
  Managed-agents platform: assign tasks to coding agents like teammates and supervise them.  
  <sub>topics: —</sub>
- **[BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban)** · 27,949★ · Rust · Declining  
  A kanban board as the harness — queue, run, and review many agent tasks in parallel.  
  <sub>topics: agent, ai-agents, kanban, management, task-manager</sub>
- **[gastownhall/gastown](https://github.com/gastownhall/gastown)** · 17,832★ · Go · Hot  
  Multi-agent workspace manager — the 'town' where a fleet of agents live and work.  
  <sub>topics: —</sub>
- **[AndyMik90/Aperant](https://github.com/AndyMik90/Aperant)** · 14,541★ · TypeScript · Declining  
  Autonomous multi-session AI coding — sessions as the unit of parallelism.  
  <sub>topics: —</sub>
- **[Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator)** · 10,484★ · Go · Hot  
  Plans tasks, spawns parallel coding agents in worktrees, merges autonomously.  
  <sub>topics: claude-code, codex-cli, orchestration, orchestrator, skills, agent-fleet, agent-swarm, git-worktrees</sub>
- **[automazeio/ccpm](https://github.com/automazeio/ccpm)** · 8,357★ · Shell · Declining  
  GitHub Issues + git worktrees as the coordination fabric for parallel agents.  
  <sub>topics: ai-agents, ai-coding, claude, claude-code, project-management, vibe-coding</sub>
- **[dagger/container-use](https://github.com/dagger/container-use)** · 4,022★ · Go · Mature  
  Containerized dev environments so multiple agents work safely and independently.  
  <sub>topics: —</sub>

### Determinism & spec-driven

_The counter-culture: agents drift, so pin them down. Specs, standards files, and plans persisted to disk make runs reproducible, auditable, and resumable after crashes._

- **[github/spec-kit](https://github.com/github/spec-kit)** · 132,136★ · Python · Hot  
  Spec-Driven Development toolkit — the spec, not the prompt, steers the agent.  
  <sub>topics: ai, copilot, development, engineering, prd, spec, spec-driven</sub>
- **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** · 26,413★ · Shell · Hot  
  Persistent file-based planning — crash-proof, resumable long-running agent tasks.  
  <sub>topics: claude, claude-code, claude-skills, manus, agent-skills, planning, autonomous-agents, codex</sub>
- **[agentsmd/agents.md](https://github.com/agentsmd/agents.md)** · 23,976★ · TypeScript · Declining  
  The open AGENTS.md standard — a portable contract telling any harness how to behave in a repo.  
  <sub>topics: —</sub>
- **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** · 10,730★ · TypeScript · Hot  
  Patterns and starters for *loop engineering* — designing the iteration, not just the prompt.  
  <sub>topics: agentic-ai, ai-agents, claude-code, codex, devops-automation, github-actions, grok, llm</sub>
- **[gsd-build/gsd-2](https://github.com/gsd-build/gsd-2)** · 7,771★ · TypeScript · Declining  
  Meta-prompting + context engineering + spec-driven system for dependable outcomes.  
  <sub>topics: context-engineering, meta-prompting, spec-driven-development</sub>

### Sandbox substrate

_Infrastructure-first: before you scale agents you need somewhere safe and fast to run them. MicroVMs, container runtimes, and hardened sandboxes are the harness's floor._

- **[daytonaio/daytona](https://github.com/daytonaio/daytona)** · 71,857★ · — · Mature  
  Secure, elastic infrastructure for running AI-generated code — the harness's execution floor.  
  <sub>topics: developer-tools, agentic-workflow, ai, ai-agents, ai-runtime, code-execution, code-interpreter, ai-sandboxes</sub>
- **[NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)** · 22,304★ · TypeScript · Hot  
  Run harnesses (Hermes, Deep Agents, OpenClaw) inside hardened NVIDIA sandboxes.  
  <sub>topics: ai-agents, nvidia, openclaw, openshell, sandboxing, typescript, hermes</sub>
- **[trycua/cua](https://github.com/trycua/cua)** · 22,005★ · HTML · Hot  
  Sandboxes, SDKs, and benchmarks for computer-use agents — full-desktop harnessing.  
  <sub>topics: apple, cua, lume, macos, virtualization, virtualization-framework, swift, ai-agent</sub>
- **[opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)** · 14,808★ · Go · Hot  
  Secure, fast, extensible sandbox runtime purpose-built for AI agents.  
  <sub>topics: ai, ai-infra, kubernetes, sandbox, ai-agent</sub>
- **[deeplethe/forkd](https://github.com/deeplethe/forkd)** · 2,815★ · Rust · Hot  
  fork() for agent microVMs — spawn 100 children in ~100ms; branch a live VM mid-run.  
  <sub>topics: ai-agents, copy-on-write, kvm, microvm, rust, sandbox, snapshot</sub>

### Autonomous long-horizon

_Maximum autonomy: agents that run for hours or days, planning and re-planning, sometimes improving their own scaffolding. The harness is a resident process, not a CLI invocation._

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 81,091★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and creates with sub-agents in sandboxes.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[agent0ai/agent-zero](https://github.com/agent0ai/agent-zero)** · 19,010★ · Python · Mature  
  General autonomous framework — the agent builds its own tools as it goes.  
  <sub>topics: agent, ai, assistant, autonomous, linux, zero</sub>
- **[hexo-ai/sia](https://github.com/hexo-ai/sia)** · 2,126★ · Python · Rising  
  Self-Improving AI — a harness whose loop optimizes the underlying system over time.  
  <sub>topics: —</sub>
- **[stakpak/agent](https://github.com/stakpak/agent)** · 1,759★ · Rust · Hot  
  An agent that lives on your machines 24/7 and keeps shipping — harness as a resident daemon.  
  <sub>topics: agent, devops, devtool, generative-ai, hacktoberfest, ai-agent, autonomous-agent, llm-agent</sub>
- **[aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch)** · 370★ · Shell · Declining  
  Watches your Claude usage windows and executes queued tasks autonomously overnight.  
  <sub>topics: —</sub>

## Graph analysis — how they relate

**Community clustering.** These 36 tools span **16 of the graph's 37 communities**.

- **Community 11** (6): `affaan-m/ECC`, `Yeachan-Heo/oh-my-claudecode`, `automazeio/ccpm`, `OthmanAdi/planning-with-files`, `cobusgreyling/loop-engineering`, `deeplethe/forkd`
- **Community 8** (5): `earendil-works/pi`, `1jehuang/jcode`, `code-yeongyu/oh-my-openagent`, `trycua/cua`, `opensandbox-group/OpenSandbox`
- **Community 9** (4): `langchain-ai/deepagents`, `obra/superpowers`, `BloopAI/vibe-kanban`, `daytonaio/daytona`
- **Community 19** (3): `SafeRL-Lab/cheetahclaws`, `gastownhall/gastown`, `Untrivial-ai/agent-orchestrator`
- **Community 13** (2): `emcie-co/parlant`, `gsd-build/gsd-2`
- **Community 7** (2): `strands-agents/harness-sdk`, `ruvnet/ruflo`
- **Community 22** (2): `vercel/eve`, `stakpak/agent`
- **Community 10** (2): `pydantic/pydantic-ai-harness`, `agentsmd/agents.md`
- **Community 16** (2): `coleam00/Archon`, `agent0ai/agent-zero`
- **Community 0** (2): `bytedance/deer-flow`, `hexo-ai/sia`

**Centrality (PageRank in the full 1,857-repo graph)** — most 'hub-like' harnesses in your ecosystem:

- `1jehuang/jcode` — PageRank 0.0018
- `affaan-m/ECC` — PageRank 0.0014
- `langchain-ai/deepagents` — PageRank 0.0011
- `code-yeongyu/oh-my-openagent` — PageRank 0.0011
- `multica-ai/multica` — PageRank 0.0008
- `cobusgreyling/loop-engineering` — PageRank 0.0008
- `bytedance/deer-flow` — PageRank 0.0006
- `vercel/eve` — PageRank 0.0006
- `coleam00/Archon` — PageRank 0.0006
- `strands-agents/harness-sdk` — PageRank 0.0006

**Direct links between harness projects** (top similarity edges where both endpoints are in this report):

- `1jehuang/jcode` ⇄ `code-yeongyu/oh-my-openagent` (w=0.507) — topics: ai, claude, openai, tui; authors: github-actions[bot]
- `bytedance/deer-flow` ⇄ `langchain-ai/deepagents` (w=0.350) — topics: ai, langchain, langgraph, python
- `Yeachan-Heo/oh-my-claudecode` ⇄ `automazeio/ccpm` (w=0.333) — topics: ai-agents, claude, claude-code, vibe-coding
- `1jehuang/jcode` ⇄ `opensandbox-group/OpenSandbox` (w=0.300) — topics: ai, ai-agent; authors: github-actions[bot]
- `affaan-m/ECC` ⇄ `automazeio/ccpm` (w=0.273) — topics: ai-agents, claude, claude-code
- `cobusgreyling/loop-engineering` ⇄ `Yeachan-Heo/oh-my-claudecode` (w=0.224) — topics: ai-agents, claude-code, automation, claude

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Harnesses are a young, fast-moving category — expect churn; check lifecycle before betting on one.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| strands-agents/harness-sdk | 97 | Hot | very active | 6 | 14% | 90 |
| Untrivial-ai/agent-orchestrator | 97 | Hot | very active | 5 | 13% | 160 |
| vercel/eve | 95 | Hot | very active | 5 | 16% | 157 |
| daytonaio/daytona | 94 | Mature | active | 5 | 14% | 205 |
| multica-ai/multica | 86 | Hot | very active | 3 | 25% | 148 |
| earendil-works/pi | 85 | Hot | very active | 2 | 33% | 257 |
| github/spec-kit | 84 | Hot | very active | 2 | 39% | 215 |
| bytedance/deer-flow | 84 | Hot | very active | 12 | 9% | 1 |
| opensandbox-group/OpenSandbox | 83 | Hot | very active | 2 | 29% | 176 |
| deeplethe/forkd | 83 | Hot | very active | 2 | 42% | 24 |
| Yeachan-Heo/oh-my-claudecode | 80 | Hot | very active | 1 | 60% | 247 |
| trycua/cua | 80 | Hot | very active | 2 | 34% | 652 |
| langchain-ai/deepagents | 79 | Hot | very active | 1 | 71% | 271 |
| pydantic/pydantic-ai-harness | 79 | Hot | very active | 2 | 47% | 31 |
| obra/superpowers | 79 | Hot | very active | 1 | 82% | 12 |
| affaan-m/ECC | 79 | Hot | very active | 1 | 71% | 16 |
| OthmanAdi/planning-with-files | 79 | Hot | very active | 1 | 77% | 89 |
| agent0ai/agent-zero | 79 | Mature | very active | 1 | 75% | 73 |
| code-yeongyu/oh-my-openagent | 78 | Hot | very active | 1 | 73% | 251 |
| coleam00/Archon | 78 | Mature | very active | 1 | 100% | 20 |
| SafeRL-Lab/cheetahclaws | 76 | Hot | very active | 1 | 77% | 41 |
| 1jehuang/jcode | 76 | Rising | very active | 1 | 93% | 168 |
| ruvnet/ruflo | 76 | Hot | very active | 1 | 79% | 1637 |
| gastownhall/gastown | 76 | Hot | very active | 1 | 53% | 14 |
| NVIDIA/NemoClaw | 74 | Hot | very active | 3 | 25% | 0 |
| cobusgreyling/loop-engineering | 73 | Hot | very active | 2 | 46% | 2 |
| stakpak/agent | 65 | Hot | active | 1 | 59% | 315 |
| emcie-co/parlant | 62 | Mature | active | 1 | 56% | 33 |
| hexo-ai/sia | 55 | Rising | very active | 2 | 36% | 0 |
| AndyMik90/Aperant | 54 | Declining | slowing | 1 | 100% | 37 |
| gsd-build/gsd-2 | 47 | Declining | slowing | 0 | 0% | 116 |
| dagger/container-use | 46 | Mature | active | 1 | 75% | 14 |
| BloopAI/vibe-kanban | 40 | Declining | slowing | 0 | 0% | 284 |
| agentsmd/agents.md | 38 | Declining | active | 1 | 100% | 0 |
| automazeio/ccpm | 26 | Declining | slowing | 0 | 0% | 0 |
| aniketkarne/ClaudeNightsWatch | 18 | Declining | stale | 0 | 0% | 0 |

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

- **langchain-ai/langgraph** (40,664★) — agent *framework* (graphs, not harnesses) — see the agent-orchestration report
- **crewAIInc/crewAI** (57,789★) — role-playing agent framework — agent-orchestration report
- **microsoft/autogen** (60,689★) — multi-agent conversation framework — agent-orchestration report
- **eigent-ai/eigent** (15,155★) — cowork desktop product — agent-orchestration report
- **getpaseo/paseo** (15,411★) — desktop/mobile agent orchestrator — agent-orchestration report
- **wshobson/agents** (39,241★) — multi-harness plugin *marketplace* — content for harnesses, not a harness
- **EleutherAI/lm-evaluation-harness** (13,827★) — 'harness' for *model benchmarks*, not agent runtimes — see the LLM-evaluation report
- **anthropics/claude-code** (143,373★) — the coding agent itself — the thing meta-harnesses wrap

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (harness / autonomous / swarm / multi-agent / sandbox / worktree / spec-driven / long-horizon / loop…) + manual curation by *approach*. General agent frameworks and orchestration platforms live in the agent-orchestration report; Claude-Code configuration setups in the claude-code-setups report. A few boundary projects (`deer-flow`, `ruflo`, `oh-my-*`) appear in both, viewed through different lenses.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 36 · Snapshot: 2026-08-29T15:31:31.780Z</sub>
