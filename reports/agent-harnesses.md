# Agent Harnesses — Six Approaches to Running Autonomous Agents

> Derived from **kaiser-data**'s 1,535 starred repos (snapshot `2026-08-07T23:57:40.892Z`), cross-referenced with the repo-similarity graph (1,535 nodes / 4,980 edges, 34 communities).
>
> Generated 2026-08-08 by `scripts/reports/agent_harnesses.py` (regenerate any time — no API cost).

## Executive summary

- A **harness** is everything around the model: the loop, tools, state, guardrails, and execution environment. **36 harness projects** in your stars (**1,414,906★** combined) cluster into **six distinct approaches** — they disagree about *where the harness lives* and *what the hard problem is*:
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
| [obra/superpowers](https://github.com/obra/superpowers) | Meta-harness over coding agents | Shell | MIT | 268,683 (▲6,878) | Hot | 78 | very active | 0d ago | 10mo | 6 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Meta-harness over coding agents | JavaScript | MIT | 238,551 (▲4,760) | Hot | 85 | very active | 0d ago | 6mo | 29 |
| [github/spec-kit](https://github.com/github/spec-kit) | Determinism & spec-driven | Python | MIT | 125,772 (▲1,760) | Hot | 89 | very active | 0d ago | 11mo | 13 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness-as-SDK | TypeScript | MIT | 85,266 (▲6,686) | Hot | 90 | very active | 0d ago | 12mo | 20 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Autonomous long-horizon | Python | MIT | 79,512 (▲1,572) | Hot | 84 | very active | 0d ago | 1.3y | 35 |
| [daytonaio/daytona](https://github.com/daytonaio/daytona) | Sandbox substrate | — | — | 72,023 (▼128) | Mature | 96 | very active | 15d ago | 2.5y | 21 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Meta-harness over coding agents | TypeScript | NOASSERTION | 67,452 (▲807) | Hot | 78 | very active | 1d ago | 8mo | 5 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Meta-harness over coding agents | TypeScript | MIT | 67,279 (▲1,090) | Hot | 76 | very active | 1d ago | 1.2y | 3 |
| [multica-ai/multica](https://github.com/multica-ai/multica) | Fleet / parallel orchestration | Go | NOASSERTION | 44,689 (▲2,523) | Hot | 81 | very active | 0d ago | 6mo | 16 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Meta-harness over coding agents | TypeScript | MIT | 38,422 (▲318) | Hot | 80 | very active | 1d ago | 7mo | 15 |
| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Fleet / parallel orchestration | Rust | Apache-2.0 | 27,698 (▲157) | Declining | 42 | slowing | 3mo ago | 1.1y | 0 |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Harness-as-SDK | Python | MIT | 27,487 (▲642) | Hot | 83 | very active | 0d ago | 1.0y | 9 |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | Determinism & spec-driven | Shell | MIT | 26,042 (▲269) | Hot | 78 | very active | 5d ago | 7mo | 17 |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | Determinism & spec-driven | TypeScript | MIT | 23,507 (▲277) | Declining | 19 | slowing | 4mo ago | 11mo | 0 |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Meta-harness over coding agents | TypeScript | MIT | 23,101 (▲86) | Hot | 78 | very active | 0d ago | 1.5y | 15 |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Sandbox substrate | TypeScript | Apache-2.0 | 22,085 (▲133) | Hot | 84 | very active | 0d ago | 4mo | 24 |
| [trycua/cua](https://github.com/trycua/cua) | Sandbox substrate | HTML | MIT | 21,022 (▲334) | Hot | 76 | very active | 0d ago | 1.5y | 18 |
| [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | Autonomous long-horizon | Python | NOASSERTION | 18,769 (▲203) | Mature | 78 | very active | 6d ago | 2.2y | 2 |
| [emcie-co/parlant](https://github.com/emcie-co/parlant) | Harness-as-SDK | Python | Apache-2.0 | 18,235 (▲56) | Mature | 64 | active | 26d ago | 2.5y | 4 |
| [gastownhall/gastown](https://github.com/gastownhall/gastown) | Fleet / parallel orchestration | Go | MIT | 17,495 (▲258) | Hot | 77 | very active | 3d ago | 7mo | 9 |
| [1jehuang/jcode](https://github.com/1jehuang/jcode) | Harness-as-SDK | Rust | MIT | 16,337 (▲4,598) | Rising | 76 | very active | 1d ago | 7mo | 1 |
| [AndyMik90/Aperant](https://github.com/AndyMik90/Aperant) | Fleet / parallel orchestration | TypeScript | AGPL-3.0 | 14,504 (▲17) | Declining | 56 | active | 1mo ago | 8mo | 1 |
| [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | Sandbox substrate | Python | Apache-2.0 | 12,395 (▲211) | Hot | 82 | very active | 2d ago | 7mo | 13 |
| [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | Determinism & spec-driven | JavaScript | MIT | 9,954 (▲488) | Hot | 78 | very active | 1d ago | 2mo | 15 |
| [Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) | Fleet / parallel orchestration | Go | Apache-2.0 | 8,852 | Hot | 93 | very active | 0d ago | 5mo | 20 |
| [automazeio/ccpm](https://github.com/automazeio/ccpm) | Fleet / parallel orchestration | Shell | MIT | 8,316 (▲27) | Declining | 28 | slowing | 4mo ago | 11mo | 0 |
| [gsd-build/gsd-2](https://github.com/gsd-build/gsd-2) | Determinism & spec-driven | TypeScript | MIT | 7,755 (▲5) | Rising | 74 | slowing | 2mo ago | 5mo | 2 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | Harness-as-SDK | Python | Apache-2.0 | 6,832 (▲129) | Hot | 92 | very active | 0d ago | 1.2y | 26 |
| [vercel/eve](https://github.com/vercel/eve) | Harness-as-SDK | TypeScript | Apache-2.0 | 4,450 (▲351) | Hot | 94 | very active | 0d ago | 1mo | 25 |
| [dagger/container-use](https://github.com/dagger/container-use) | Fleet / parallel orchestration | Go | Apache-2.0 | 3,997 (▲75) | Declining | 39 | active | 1mo ago | 1.2y | 1 |
| [deeplethe/forkd](https://github.com/deeplethe/forkd) | Sandbox substrate | Rust | Apache-2.0 | 2,732 (▲10) | Hot | 78 | very active | 5d ago | 2mo | 6 |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | Autonomous long-horizon | Python | MIT | 2,093 (▲15) | Rising | 52 | active | 1mo ago | 4mo | 8 |
| [stakpak/agent](https://github.com/stakpak/agent) | Autonomous long-horizon | Rust | Apache-2.0 | 1,720 (▲29) | Hot | 69 | active | 1mo ago | 1.7y | 4 |
| [SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws) | Harness-as-SDK | Python | Apache-2.0 | 764 (▲5) | Hot | 75 | very active | 8d ago | 4mo | 5 |
| [pydantic/pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness) | Harness-as-SDK | Python | MIT | 747 (▲40) | Hot | 78 | very active | 1d ago | 4mo | 11 |
| [aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch) | Autonomous long-horizon | Shell | MIT | 368 | Declining | 20 | stale | 6mo ago | 1.1y | 0 |

## By approach

### Harness-as-SDK

_The loop as a library: you import the harness, register tools, and own control flow. Maximum flexibility, maximum responsibility — you maintain planning, retries, memory, and safety yourself._

- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 85,266★ · TypeScript · Hot  
  Unified LLM API + agent loop + TUI + coding-agent CLI in one toolkit — the loop as a library.  
  <sub>topics: —</sub>
- **[langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)** · 27,487★ · Python · Hot  
  The 'batteries-included agent harness' — planning, sub-agents, filesystem, from the LangChain team.  
  <sub>topics: deepagents, langchain, langgraph, ai, python, typescript</sub>
- **[emcie-co/parlant](https://github.com/emcie-co/parlant)** · 18,235★ · Python · Mature  
  Interaction *control* harness — behavioral guidelines enforced at runtime for customer-facing agents.  
  <sub>topics: ai-agents, genai, llm, customer-service, customer-success, gemini, llama3, openai</sub>
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 16,337★ · Rust · Rising  
  Rust-built coding-agent harness — CLI agent loop with MCP support and multi-model wiring.  
  <sub>topics: ai, claude, cli, coding-agent, llm, mcp, openai, rust</sub>
- **[strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)** · 6,832★ · Python · Hot  
  AWS's open SDK to build an agent harness and control it end-to-end in production.  
  <sub>topics: agentic, agentic-ai, agents, ai, autonomous-agents, llm, multi-agent-systems, python</sub>
- **[vercel/eve](https://github.com/vercel/eve)** · 4,450★ · TypeScript · Hot  
  Vercel's framework for building agents — harness + sandbox as one integrated runtime.  
  <sub>topics: agent, framework, harness, javascript, markdown, typescript, vercel, sandbox</sub>
- **[SafeRL-Lab/cheetahclaws](https://github.com/SafeRL-Lab/cheetahclaws)** · 764★ · Python · Hot  
  Fast, easy agent-harness infrastructure aimed at long-horizon, multi-model runs.  
  <sub>topics: agentic-ai, claude, claude-code, memory, python, skills, openclaw</sub>
- **[pydantic/pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness)** · 747★ · Python · Hot  
  'Batteries for your Pydantic AI agent' — the harness as a thin add-on to a typed agent framework.  
  <sub>topics: —</sub>

### Meta-harness over coding agents

_These projects treat Claude Code / Codex as the engine and build the transmission: skills, personas, memory, token discipline, and multi-agent coordination injected via configs, hooks, and subagents._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 268,683★ · Shell · Hot  
  Skills framework + development methodology layered onto the agent you already run.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 238,551★ · JavaScript · Hot  
  Harness performance optimization: skills, instincts, memory, security, hooks on top of Claude Code.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 67,452★ · TypeScript · Hot  
  'The one and only agent harness for complex coding' — tokenmaxxer harness wrapping coding agents.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 67,279★ · TypeScript · Hot  
  The leading agent *meta*-harness — swarms, coordination, and autonomy on top of existing agents.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 38,422★ · TypeScript · Hot  
  Teams-first multi-agent orchestration living entirely inside Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>
- **[coleam00/Archon](https://github.com/coleam00/Archon)** · 23,101★ · TypeScript · Hot  
  'Harness builder' — make AI coding deterministic and repeatable by generating the harness itself.  
  <sub>topics: ai, automation, bun, claude, cli, coding-assistant, developer-tools, typescript</sub>

### Fleet / parallel orchestration

_One agent is a tool; a fleet is a team. The harness problem becomes scheduling, isolation (worktrees, containers), review queues, and merge discipline._

- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 44,689★ · Go · Hot  
  Managed-agents platform: assign tasks to coding agents like teammates and supervise them.  
  <sub>topics: —</sub>
- **[BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban)** · 27,698★ · Rust · Declining  
  A kanban board as the harness — queue, run, and review many agent tasks in parallel.  
  <sub>topics: agent, ai-agents, kanban, management, task-manager</sub>
- **[gastownhall/gastown](https://github.com/gastownhall/gastown)** · 17,495★ · Go · Hot  
  Multi-agent workspace manager — the 'town' where a fleet of agents live and work.  
  <sub>topics: —</sub>
- **[AndyMik90/Aperant](https://github.com/AndyMik90/Aperant)** · 14,504★ · TypeScript · Declining  
  Autonomous multi-session AI coding — sessions as the unit of parallelism.  
  <sub>topics: —</sub>
- **[Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator)** · 8,852★ · Go · Hot  
  Plans tasks, spawns parallel coding agents in worktrees, merges autonomously.  
  <sub>topics: claude-code, codex-cli, orchestration, orchestrator, skills, agent-fleet, agent-swarm, git-worktrees</sub>
- **[automazeio/ccpm](https://github.com/automazeio/ccpm)** · 8,316★ · Shell · Declining  
  GitHub Issues + git worktrees as the coordination fabric for parallel agents.  
  <sub>topics: ai-agents, ai-coding, claude, claude-code, project-management, vibe-coding</sub>
- **[dagger/container-use](https://github.com/dagger/container-use)** · 3,997★ · Go · Declining  
  Containerized dev environments so multiple agents work safely and independently.  
  <sub>topics: —</sub>

### Determinism & spec-driven

_The counter-culture: agents drift, so pin them down. Specs, standards files, and plans persisted to disk make runs reproducible, auditable, and resumable after crashes._

- **[github/spec-kit](https://github.com/github/spec-kit)** · 125,772★ · Python · Hot  
  Spec-Driven Development toolkit — the spec, not the prompt, steers the agent.  
  <sub>topics: ai, copilot, development, engineering, prd, spec, spec-driven</sub>
- **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** · 26,042★ · Shell · Hot  
  Persistent file-based planning — crash-proof, resumable long-running agent tasks.  
  <sub>topics: claude, claude-code, claude-skills, manus, agent-skills, planning, autonomous-agents, codex</sub>
- **[agentsmd/agents.md](https://github.com/agentsmd/agents.md)** · 23,507★ · TypeScript · Declining  
  The open AGENTS.md standard — a portable contract telling any harness how to behave in a repo.  
  <sub>topics: —</sub>
- **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** · 9,954★ · JavaScript · Hot  
  Patterns and starters for *loop engineering* — designing the iteration, not just the prompt.  
  <sub>topics: agentic-ai, ai-agents, claude-code, codex, devops-automation, github-actions, grok, llm</sub>
- **[gsd-build/gsd-2](https://github.com/gsd-build/gsd-2)** · 7,755★ · TypeScript · Rising  
  Meta-prompting + context engineering + spec-driven system for dependable outcomes.  
  <sub>topics: context-engineering, meta-prompting, spec-driven-development</sub>

### Sandbox substrate

_Infrastructure-first: before you scale agents you need somewhere safe and fast to run them. MicroVMs, container runtimes, and hardened sandboxes are the harness's floor._

- **[daytonaio/daytona](https://github.com/daytonaio/daytona)** · 72,023★ · — · Mature  
  Secure, elastic infrastructure for running AI-generated code — the harness's execution floor.  
  <sub>topics: developer-tools, agentic-workflow, ai, ai-agents, ai-runtime, code-execution, code-interpreter, ai-sandboxes</sub>
- **[NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)** · 22,085★ · TypeScript · Hot  
  Run harnesses (Hermes, Deep Agents, OpenClaw) inside hardened NVIDIA sandboxes.  
  <sub>topics: ai-agents, nvidia, openclaw, openshell, sandboxing, typescript, hermes</sub>
- **[trycua/cua](https://github.com/trycua/cua)** · 21,022★ · HTML · Hot  
  Sandboxes, SDKs, and benchmarks for computer-use agents — full-desktop harnessing.  
  <sub>topics: apple, cua, lume, macos, virtualization, virtualization-framework, swift, ai-agent</sub>
- **[opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)** · 12,395★ · Python · Hot  
  Secure, fast, extensible sandbox runtime purpose-built for AI agents.  
  <sub>topics: ai, ai-infra, kubernetes, sandbox, ai-agent</sub>
- **[deeplethe/forkd](https://github.com/deeplethe/forkd)** · 2,732★ · Rust · Hot  
  fork() for agent microVMs — spawn 100 children in ~100ms; branch a live VM mid-run.  
  <sub>topics: ai-agents, copy-on-write, kvm, microvm, rust, sandbox, snapshot</sub>

### Autonomous long-horizon

_Maximum autonomy: agents that run for hours or days, planning and re-planning, sometimes improving their own scaffolding. The harness is a resident process, not a CLI invocation._

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 79,512★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and creates with sub-agents in sandboxes.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[agent0ai/agent-zero](https://github.com/agent0ai/agent-zero)** · 18,769★ · Python · Mature  
  General autonomous framework — the agent builds its own tools as it goes.  
  <sub>topics: agent, ai, assistant, autonomous, linux, zero</sub>
- **[hexo-ai/sia](https://github.com/hexo-ai/sia)** · 2,093★ · Python · Rising  
  Self-Improving AI — a harness whose loop optimizes the underlying system over time.  
  <sub>topics: —</sub>
- **[stakpak/agent](https://github.com/stakpak/agent)** · 1,720★ · Rust · Hot  
  An agent that lives on your machines 24/7 and keeps shipping — harness as a resident daemon.  
  <sub>topics: agent, devops, devtool, generative-ai, hacktoberfest, ai-agent, autonomous-agent, llm-agent</sub>
- **[aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch)** · 368★ · Shell · Declining  
  Watches your Claude usage windows and executes queued tasks autonomously overnight.  
  <sub>topics: —</sub>

## Graph analysis — how they relate

**Community clustering.** These 36 tools span **12 of the graph's 34 communities**.

- **Community 20** (11): `langchain-ai/deepagents`, `emcie-co/parlant`, `pydantic/pydantic-ai-harness`, `obra/superpowers`, `BloopAI/vibe-kanban`, `gastownhall/gastown`, `gsd-build/gsd-2`, `daytonaio/daytona`, `deeplethe/forkd`, `bytedance/deer-flow`, `agent0ai/agent-zero`
- **Community 10** (9): `vercel/eve`, `1jehuang/jcode`, `affaan-m/ECC`, `code-yeongyu/oh-my-openagent`, `Yeachan-Heo/oh-my-claudecode`, `coleam00/Archon`, `automazeio/ccpm`, `OthmanAdi/planning-with-files`, `cobusgreyling/loop-engineering`
- **Community 8** (5): `earendil-works/pi`, `SafeRL-Lab/cheetahclaws`, `ruvnet/ruflo`, `Untrivial-ai/agent-orchestrator`, `trycua/cua`
- **Community 0** (2): `multica-ai/multica`, `dagger/container-use`
- **Community 2** (2): `AndyMik90/Aperant`, `agentsmd/agents.md`

**Centrality (PageRank in the full 1,535-repo graph)** — most 'hub-like' harnesses in your ecosystem:

- `affaan-m/ECC` — PageRank 0.0018
- `langchain-ai/deepagents` — PageRank 0.0017
- `cobusgreyling/loop-engineering` — PageRank 0.0008
- `strands-agents/harness-sdk` — PageRank 0.0008
- `coleam00/Archon` — PageRank 0.0008
- `NVIDIA/NemoClaw` — PageRank 0.0008
- `1jehuang/jcode` — PageRank 0.0007
- `code-yeongyu/oh-my-openagent` — PageRank 0.0007
- `bytedance/deer-flow` — PageRank 0.0006
- `multica-ai/multica` — PageRank 0.0006

**Direct links between harness projects** (top similarity edges where both endpoints are in this report):

- `cobusgreyling/loop-engineering` ⇄ `affaan-m/ECC` (w=0.412) — topics: ai-agents, claude-code, llm, mcp; authors: dependabot[bot]
- `bytedance/deer-flow` ⇄ `langchain-ai/deepagents` (w=0.360) — topics: ai, langchain, langgraph, python; authors: dependabot[bot]
- `opensandbox-group/OpenSandbox` ⇄ `langchain-ai/deepagents` (w=0.350) — topics: ai; authors: dependabot[bot], github-actions[bot]
- `Yeachan-Heo/oh-my-claudecode` ⇄ `automazeio/ccpm` (w=0.333) — topics: ai-agents, claude, claude-code, vibe-coding
- `affaan-m/ECC` ⇄ `automazeio/ccpm` (w=0.273) — topics: ai-agents, claude, claude-code
- `strands-agents/harness-sdk` ⇄ `ruvnet/ruflo` (w=0.212) — topics: agentic-ai, agents, autonomous-agents, multi-agent-systems
- `stakpak/agent` ⇄ `BloopAI/vibe-kanban` (w=0.121) — topics: agent

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Harnesses are a young, fast-moving category — expect churn; check lifecycle before betting on one.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| daytonaio/daytona | 96 | Mature | very active | 5 | 14% | 205 |
| vercel/eve | 94 | Hot | very active | 5 | 16% | 102 |
| Untrivial-ai/agent-orchestrator | 93 | Hot | very active | 4 | 20% | 108 |
| strands-agents/harness-sdk | 92 | Hot | very active | 4 | 26% | 84 |
| earendil-works/pi | 90 | Hot | very active | 3 | 34% | 254 |
| github/spec-kit | 89 | Hot | very active | 3 | 21% | 209 |
| affaan-m/ECC | 85 | Hot | very active | 2 | 39% | 15 |
| NVIDIA/NemoClaw | 84 | Hot | very active | 5 | 15% | 0 |
| bytedance/deer-flow | 84 | Hot | very active | 7 | 13% | 1 |
| langchain-ai/deepagents | 83 | Hot | very active | 2 | 37% | 248 |
| opensandbox-group/OpenSandbox | 82 | Hot | very active | 2 | 43% | 168 |
| multica-ai/multica | 81 | Hot | very active | 2 | 35% | 133 |
| Yeachan-Heo/oh-my-claudecode | 80 | Hot | very active | 1 | 64% | 242 |
| pydantic/pydantic-ai-harness | 78 | Hot | very active | 2 | 48% | 22 |
| obra/superpowers | 78 | Hot | very active | 1 | 82% | 11 |
| code-yeongyu/oh-my-openagent | 78 | Hot | very active | 1 | 82% | 225 |
| coleam00/Archon | 78 | Hot | very active | 1 | 79% | 19 |
| OthmanAdi/planning-with-files | 78 | Hot | very active | 1 | 76% | 83 |
| cobusgreyling/loop-engineering | 78 | Hot | very active | 3 | 29% | 2 |
| deeplethe/forkd | 78 | Hot | very active | 1 | 83% | 24 |
| agent0ai/agent-zero | 78 | Mature | very active | 1 | 89% | 70 |
| gastownhall/gastown | 77 | Hot | very active | 1 | 53% | 14 |
| 1jehuang/jcode | 76 | Rising | very active | 1 | 100% | 148 |
| ruvnet/ruflo | 76 | Hot | very active | 1 | 94% | 1617 |
| trycua/cua | 76 | Hot | very active | 1 | 58% | 600 |
| SafeRL-Lab/cheetahclaws | 75 | Hot | very active | 1 | 81% | 39 |
| gsd-build/gsd-2 | 74 | Rising | slowing | 1 | 76% | 116 |
| stakpak/agent | 69 | Hot | active | 1 | 61% | 315 |
| emcie-co/parlant | 64 | Mature | active | 1 | 50% | 33 |
| AndyMik90/Aperant | 56 | Declining | active | 1 | 100% | 37 |
| hexo-ai/sia | 52 | Rising | active | 2 | 35% | 0 |
| BloopAI/vibe-kanban | 42 | Declining | slowing | 0 | 0% | 284 |
| dagger/container-use | 39 | Declining | active | 1 | 100% | 14 |
| automazeio/ccpm | 28 | Declining | slowing | 0 | 0% | 0 |
| aniketkarne/ClaudeNightsWatch | 20 | Declining | stale | 0 | 0% | 0 |
| agentsmd/agents.md | 19 | Declining | slowing | 0 | 0% | 0 |

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

- **langchain-ai/langgraph** (39,143★) — agent *framework* (graphs, not harnesses) — see the agent-orchestration report
- **crewAIInc/crewAI** (56,752★) — role-playing agent framework — agent-orchestration report
- **microsoft/autogen** (60,299★) — multi-agent conversation framework — agent-orchestration report
- **eigent-ai/eigent** (14,808★) — cowork desktop product — agent-orchestration report
- **getpaseo/paseo** (12,640★) — desktop/mobile agent orchestrator — agent-orchestration report
- **wshobson/agents** (38,595★) — multi-harness plugin *marketplace* — content for harnesses, not a harness
- **EleutherAI/lm-evaluation-harness** (13,569★) — 'harness' for *model benchmarks*, not agent runtimes — see the LLM-evaluation report
- **anthropics/claude-code** (140,599★) — the coding agent itself — the thing meta-harnesses wrap

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (harness / autonomous / swarm / multi-agent / sandbox / worktree / spec-driven / long-horizon / loop…) + manual curation by *approach*. General agent frameworks and orchestration platforms live in the agent-orchestration report; Claude-Code configuration setups in the claude-code-setups report. A few boundary projects (`deer-flow`, `ruflo`, `oh-my-*`) appear in both, viewed through different lenses.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 36 · Snapshot: 2026-08-07T23:57:40.892Z</sub>
