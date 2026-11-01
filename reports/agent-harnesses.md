# Agent Harnesses — Six Approaches to Running Autonomous Agents

> Derived from **kaiser-data**'s 2,585 starred repos (snapshot `2026-11-01T12:41:55.392Z`), cross-referenced with the repo-similarity graph (2,585 nodes / 8,670 edges, 45 communities).
>
> Generated 2026-11-01 by `scripts/reports/agent_harnesses.py` (regenerate any time — no API cost).

![Top tools by stars](assets/agent-harnesses-top-tools.svg)

![Tools per category](assets/agent-harnesses-categories.svg)


## Executive summary

- A **harness** is everything around the model: the loop, tools, state, guardrails, and execution environment. **41 harness projects** in your stars (**1,706,547★** combined) cluster into **six distinct approaches** — they disagree about *where the harness lives* and *what the hard problem is*:
  - **Harness-as-SDK** (11): `pi`, `openhuman`, `deepagents`, `jcode`, `parlant`, `harness-sdk`, `eve`, `cheetahclaws`, `dexto`, `yoagent`, `tinyagents`
  - **Meta-harness over coding agents** (7): `superpowers`, `ECC`, `ruflo`, `oh-my-openagent`, `oh-my-claudecode`, `Archon`, `munder-difflin`
  - **Fleet / parallel orchestration** (7): `multica`, `vibe-kanban`, `gastown`, `Aperant`, `agent-orchestrator`, `ccpm`, `container-use`
  - **Determinism & spec-driven** (5): `spec-kit`, `OpenSpec`, `planning-with-files`, `agents.md`, `loop-engineering`
  - **Sandbox substrate** (6): `cua`, `NemoClaw`, `OpenShell`, `OpenSandbox`, `runtime`, `shell`
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
| [obra/superpowers](https://github.com/obra/superpowers) | Meta-harness over coding agents | Shell | MIT | 310,340 (▲5,019) | Mature | 64 | active | 3d ago | 1.1y | 1 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Meta-harness over coding agents | JavaScript | MIT | 294,401 (▲5,192) | Hot | 79 | very active | 2d ago | 9mo | 4 |
| [github/spec-kit](https://github.com/github/spec-kit) | Determinism & spec-driven | Python | MIT | 144,677 (▲1,720) | Hot | 89 | very active | 2d ago | 1.2y | 26 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness-as-SDK | TypeScript | MIT | 119,275 (▲1,355) | Hot | 80 | very active | 0d ago | 1.2y | 9 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Autonomous long-horizon | Python | MIT | 84,817 (▲378) | Hot | 87 | very active | 0d ago | 1.5y | 47 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Meta-harness over coding agents | TypeScript | MIT | 80,472 (▲1,080) | Hot | 77 | very active | 0d ago | 1.4y | 13 |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | Determinism & spec-driven | TypeScript | MIT | 73,570 (▲552) | Hot | 88 | very active | 2d ago | 1.2y | 37 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Meta-harness over coding agents | TypeScript | NOASSERTION | 70,569 (▲224) | Rising | 77 | very active | 0d ago | 11mo | 1 |
| [multica-ai/multica](https://github.com/multica-ai/multica) | Fleet / parallel orchestration | Go | NOASSERTION | 54,489 (▲648) | Hot | 81 | very active | 0d ago | 9mo | 25 |
| [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Harness-as-SDK | Rust | GPL-3.0 | 42,459 (▲113) | Hot | 84 | very active | 1d ago | 8mo | 5 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Meta-harness over coding agents | TypeScript | MIT | 40,477 (▲197) | Hot | 80 | very active | 0d ago | 9mo | 7 |
| [trycua/cua](https://github.com/trycua/cua) | Sandbox substrate | Rust | MIT | 31,468 (▲471) | Hot | 75 | very active | 0d ago | 1.8y | 12 |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Harness-as-SDK | Python | MIT | 30,848 (▲245) | Hot | 84 | very active | 0d ago | 1.3y | 13 |
| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Fleet / parallel orchestration | Rust | Apache-2.0 | 28,550 (▲88) | Mature | 64 | active | 3d ago | 1.4y | 4 |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | Determinism & spec-driven | Shell | MIT | 27,804 (▲146) | Hot | 80 | very active | 2d ago | 10mo | 18 |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | Determinism & spec-driven | TypeScript | MIT | 25,256 (▲135) | Declining | 36 | active | 1mo ago | 1.2y | 2 |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Meta-harness over coding agents | TypeScript | MIT | 23,796 (▲26) | Hot | 79 | very active | 1d ago | 1.7y | 3 |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Sandbox substrate | TypeScript | Apache-2.0 | 22,905 (▲59) | Hot | 81 | very active | 0d ago | 7mo | 20 |
| [1jehuang/jcode](https://github.com/1jehuang/jcode) | Harness-as-SDK | Rust | MIT | 21,383 (▲169) | Hot | 76 | very active | 0d ago | 10mo | 4 |
| [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | Sandbox substrate | Rust | Apache-2.0 | 20,867 (▲888) | Hot | 98 | very active | 0d ago | 8mo | 31 |
| [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | Autonomous long-horizon | Python | NOASSERTION | 19,626 (▲56) | Mature | 79 | very active | 0d ago | 2.4y | 6 |
| [gastownhall/gastown](https://github.com/gastownhall/gastown) | Fleet / parallel orchestration | Go | MIT | 18,650 (▲103) | Mature | 63 | active | 4d ago | 10mo | 1 |
| [emcie-co/parlant](https://github.com/emcie-co/parlant) | Harness-as-SDK | Python | Apache-2.0 | 18,312 (▲2) | Mature | 53 | active | 4d ago | 2.7y | 0 |
| [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | Sandbox substrate | Python | Apache-2.0 | 16,355 (▲173) | Hot | 79 | very active | 0d ago | 10mo | 13 |
| [AndyMik90/Aperant](https://github.com/AndyMik90/Aperant) | Fleet / parallel orchestration | TypeScript | AGPL-3.0 | 14,585 (▼3) | Declining | 43 | slowing | 4mo ago | 11mo | 0 |
| [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | Fleet / parallel orchestration | Go | Apache-2.0 | 13,978 (▲304) | Hot | 98 | very active | 0d ago | 8mo | 23 |
| [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | Determinism & spec-driven | TypeScript | MIT | 11,676 (▲43) | Hot | 68 | very active | 0d ago | 4mo | 11 |
| [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin) | Meta-harness over coding agents | JavaScript | MIT | 9,265 (▲190) | Rising | 74 | very active | 0d ago | 5mo | 1 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | Harness-as-SDK | Python | Apache-2.0 | 9,019 (▲66) | Hot | 87 | very active | 2d ago | 1.5y | 31 |
| [automazeio/ccpm](https://github.com/automazeio/ccpm) | Fleet / parallel orchestration | Shell | MIT | 8,425 (▲9) | Declining | 45 | active | 13d ago | 1.2y | 1 |
| [vercel/eve](https://github.com/vercel/eve) | Harness-as-SDK | TypeScript | Apache-2.0 | 5,756 (▲77) | Hot | 87 | very active | 0d ago | 4mo | 14 |
| [dagger/container-use](https://github.com/dagger/container-use) | Fleet / parallel orchestration | Go | Apache-2.0 | 4,084 (▲6) | Mature | 43 | active | 1mo ago | 1.4y | 2 |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | Autonomous long-horizon | Python | MIT | 2,163 (▲1) | Mature | 44 | slowing | 2mo ago | 7mo | 5 |
| [stakpak/agent](https://github.com/stakpak/agent) | Autonomous long-horizon | Rust | Apache-2.0 | 1,840 (▲7) | Declining | 41 | slowing | 3mo ago | 1.9y | 0 |
| [e2b-dev/runtime](https://github.com/e2b-dev/runtime) | Sandbox substrate | Go | Apache-2.0 | 1,794 (▲21) | Classic | 88 | very active | 2d ago | 3.2y | 19 |
| [SAIL-Research-Lab/cheetahclaws](https://github.com/SAIL-Research-Lab/cheetahclaws) | Harness-as-SDK | Python | Apache-2.0 | 793 (▲2) | Hot | 68 | very active | 0d ago | 7mo | 7 |
| [truffle-ai/dexto](https://github.com/truffle-ai/dexto) | Harness-as-SDK | TypeScript | NOASSERTION | 659 (▲2) | Hot | 80 | very active | 0d ago | 1.6y | 5 |
| [aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch) | Autonomous long-horizon | Shell | MIT | 369 | Declining | 44 | active | 17d ago | 1.3y | 1 |
| [yologdev/yoagent](https://github.com/yologdev/yoagent) | Harness-as-SDK | Rust | MIT | 366 (▲1) | Hot | 79 | very active | 2d ago | 8mo | 3 |
| [strands-agents/shell](https://github.com/strands-agents/shell) | Sandbox substrate | Rust | Apache-2.0 | 281 (▲1) | Hot | 70 | very active | 4d ago | 8mo | 5 |
| [tinyhumansai/tinyagents](https://github.com/tinyhumansai/tinyagents) | Harness-as-SDK | Rust | GPL-3.0 | 128 (▲2) | Hot | 79 | very active | 2d ago | 4mo | 3 |

## By approach

### Harness-as-SDK

_The loop as a library: you import the harness, register tools, and own control flow. Maximum flexibility, maximum responsibility — you maintain planning, retries, memory, and safety yourself._

- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 119,275★ · TypeScript · Hot  
  Unified LLM API + agent loop + TUI + coding-agent CLI in one toolkit — the loop as a library.  
  <sub>topics: —</sub>
- **[tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman)** · 42,459★ · Rust · Hot  
  Lean open-source harness built for density — claims 500+ agents on a $10 VPS; the cost-floor end of the field.  
  <sub>topics: ai-agents, llm, local-first, rust, agent-orchestration, ai-assistant, desktop, mcp</sub>
- **[langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)** · 30,848★ · Python · Hot  
  The 'batteries-included agent harness' — planning, sub-agents, filesystem, from the LangChain team.  
  <sub>topics: deepagents, langchain, langgraph, ai, python, typescript, harness, harness-engineering</sub>
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 21,383★ · Rust · Hot  
  Rust-built coding-agent harness — CLI agent loop with MCP support and multi-model wiring.  
  <sub>topics: ai, claude, cli, coding-agent, llm, mcp, openai, rust</sub>
- **[emcie-co/parlant](https://github.com/emcie-co/parlant)** · 18,312★ · Python · Mature  
  Interaction *control* harness — behavioral guidelines enforced at runtime for customer-facing agents.  
  <sub>topics: ai-agents, genai, llm, customer-service, customer-success, gemini, llama3, openai</sub>
- **[strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)** · 9,019★ · Python · Hot  
  AWS's open SDK to build an agent harness and control it end-to-end in production.  
  <sub>topics: agentic, agentic-ai, agents, ai, autonomous-agents, llm, multi-agent-systems, python</sub>
- **[vercel/eve](https://github.com/vercel/eve)** · 5,756★ · TypeScript · Hot  
  Vercel's framework for building agents — harness + sandbox as one integrated runtime.  
  <sub>topics: agent, framework, harness, javascript, markdown, typescript, vercel, sandbox</sub>
- **[SAIL-Research-Lab/cheetahclaws](https://github.com/SAIL-Research-Lab/cheetahclaws)** · 793★ · Python · Hot  
  Fast, easy agent-harness infrastructure aimed at long-horizon, multi-model runs.  
  <sub>topics: agentic-ai, claude, claude-code, memory, python, skills, openclaw</sub>
- **[truffle-ai/dexto](https://github.com/truffle-ai/dexto)** · 659★ · TypeScript · Hot  
  Harness and toolkit for building agent apps — CLI plus SDKs, configured rather than coded.  
  <sub>topics: llm, mcp, typescript, ai-agents, ai-tools, modelcontextprotocol, ai, mcp-client</sub>
- **[yologdev/yoagent](https://github.com/yologdev/yoagent)** · 366★ · Rust · Hot  
  The agent loop as a Rust crate — streams from seven LLM protocols, runs tools, loops until done.  
  <sub>topics: agent, agent-framework, ai, ai-agents, anthropic, claude, coding-agent, gemini</sub>
- **[tinyhumansai/tinyagents](https://github.com/tinyhumansai/tinyagents)** · 128★ · Rust · Hot  
  Small, provider-neutral harness in Rust — a readable minimal loop from the openhuman team.  
  <sub>topics: agent-framework, ai-agents, llm, rust, artificial-intelligence, automation, developer-tools, multi-agent</sub>

### Meta-harness over coding agents

_These projects treat Claude Code / Codex as the engine and build the transmission: skills, personas, memory, token discipline, and multi-agent coordination injected via configs, hooks, and subagents._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 310,340★ · Shell · Mature  
  Skills framework + development methodology layered onto the agent you already run.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 294,401★ · JavaScript · Hot  
  Harness performance optimization: skills, instincts, memory, security, hooks on top of Claude Code.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 80,472★ · TypeScript · Hot  
  The leading agent *meta*-harness — swarms, coordination, and autonomy on top of existing agents.  
  <sub>topics: swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server, multi-agent</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 70,569★ · TypeScript · Rising  
  'The one and only agent harness for complex coding' — tokenmaxxer harness wrapping coding agents.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 40,477★ · TypeScript · Hot  
  Teams-first multi-agent orchestration living entirely inside Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>
- **[coleam00/Archon](https://github.com/coleam00/Archon)** · 23,796★ · TypeScript · Hot  
  'Harness builder' — make AI coding deterministic and repeatable by generating the harness itself.  
  <sub>topics: ai, automation, bun, claude, cli, coding-assistant, developer-tools, typescript</sub>
- **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** · 9,265★ · JavaScript · Rising  
  Runs an 'office' of Claude Code / Codex agents with roles — an open alternative to hosted agent-team products.  
  <sub>topics: agents, claude-code, harness, harness-engineering, memory, agent-orchestration, ai-agents, autonomous-agents</sub>

### Fleet / parallel orchestration

_One agent is a tool; a fleet is a team. The harness problem becomes scheduling, isolation (worktrees, containers), review queues, and merge discipline._

- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 54,489★ · Go · Hot  
  Managed-agents platform: assign tasks to coding agents like teammates and supervise them.  
  <sub>topics: —</sub>
- **[BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban)** · 28,550★ · Rust · Mature  
  A kanban board as the harness — queue, run, and review many agent tasks in parallel.  
  <sub>topics: agent, ai-agents, kanban, management, task-manager</sub>
- **[gastownhall/gastown](https://github.com/gastownhall/gastown)** · 18,650★ · Go · Mature  
  Multi-agent workspace manager — the 'town' where a fleet of agents live and work.  
  <sub>topics: —</sub>
- **[AndyMik90/Aperant](https://github.com/AndyMik90/Aperant)** · 14,585★ · TypeScript · Declining  
  Autonomous multi-session AI coding — sessions as the unit of parallelism.  
  <sub>topics: —</sub>
- **[OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator)** · 13,978★ · Go · Hot  
  Plans tasks, spawns parallel coding agents in worktrees, merges autonomously.  
  <sub>topics: claude-code, codex-cli, orchestration, orchestrator, skills, agent-fleet, agent-swarm, git-worktrees</sub>
- **[automazeio/ccpm](https://github.com/automazeio/ccpm)** · 8,425★ · Shell · Declining  
  GitHub Issues + git worktrees as the coordination fabric for parallel agents.  
  <sub>topics: ai-agents, ai-coding, claude, claude-code, project-management, vibe-coding</sub>
- **[dagger/container-use](https://github.com/dagger/container-use)** · 4,084★ · Go · Mature  
  Containerized dev environments so multiple agents work safely and independently.  
  <sub>topics: —</sub>

### Determinism & spec-driven

_The counter-culture: agents drift, so pin them down. Specs, standards files, and plans persisted to disk make runs reproducible, auditable, and resumable after crashes._

- **[github/spec-kit](https://github.com/github/spec-kit)** · 144,677★ · Python · Hot  
  Spec-Driven Development toolkit — the spec, not the prompt, steers the agent.  
  <sub>topics: ai, copilot, development, engineering, prd, spec, spec-driven</sub>
- **[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)** · 73,570★ · TypeScript · Hot  
  Lightweight spec-driven development — change proposals and specs in the repo that humans and agents agree on before code is written.  
  <sub>topics: spec, ai, context-engineering, engineering, planning, prd, sdlc, spec-driven-development</sub>
- **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** · 27,804★ · Shell · Hot  
  Persistent file-based planning — crash-proof, resumable long-running agent tasks.  
  <sub>topics: claude, claude-code, claude-skills, manus, agent-skills, planning, autonomous-agents, codex</sub>
- **[agentsmd/agents.md](https://github.com/agentsmd/agents.md)** · 25,256★ · TypeScript · Declining  
  The open AGENTS.md standard — a portable contract telling any harness how to behave in a repo.  
  <sub>topics: —</sub>
- **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** · 11,676★ · TypeScript · Hot  
  Patterns and starters for *loop engineering* — designing the iteration, not just the prompt.  
  <sub>topics: agentic-ai, ai-agents, claude-code, codex, devops-automation, github-actions, grok, llm</sub>

### Sandbox substrate

_Infrastructure-first: before you scale agents you need somewhere safe and fast to run them. MicroVMs, container runtimes, and hardened sandboxes are the harness's floor._

- **[trycua/cua](https://github.com/trycua/cua)** · 31,468★ · Rust · Hot  
  Sandboxes, SDKs, and benchmarks for computer-use agents — full-desktop harnessing.  
  <sub>topics: apple, cua, lume, macos, virtualization, virtualization-framework, swift, ai-agent</sub>
- **[NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)** · 22,905★ · TypeScript · Hot  
  Run harnesses (Hermes, Deep Agents, OpenClaw) inside hardened NVIDIA sandboxes.  
  <sub>topics: ai-agents, nvidia, openclaw, openshell, sandboxing, typescript, hermes, deep-agents</sub>
- **[NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)** · 20,867★ · Rust · Hot  
  NVIDIA's safe, private runtime for autonomous agents — the substrate NemoClaw runs on.  
  <sub>topics: —</sub>
- **[opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)** · 16,355★ · Python · Hot  
  Secure, fast, extensible sandbox runtime purpose-built for AI agents.  
  <sub>topics: ai, ai-infra, kubernetes, sandbox, ai-agent, aaif</sub>
- **[e2b-dev/runtime](https://github.com/e2b-dev/runtime)** · 1,794★ · Go · Classic  
  The runtime behind E2B's cloud and self-hosted sandboxes — isolated microVMs for AI-generated code; the harness's execution floor.  
  <sub>topics: ai-agents, code-interpreter, consul, devtools, firecracker, gcp, go, golang</sub>
- **[strands-agents/shell](https://github.com/strands-agents/shell)** · 281★ · Rust · Hot  
  A shell for the agent without the keys to your machine — scoped command execution as a library.  
  <sub>topics: —</sub>

### Autonomous long-horizon

_Maximum autonomy: agents that run for hours or days, planning and re-planning, sometimes improving their own scaffolding. The harness is a resident process, not a CLI invocation._

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 84,817★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and creates with sub-agents in sandboxes.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[agent0ai/agent-zero](https://github.com/agent0ai/agent-zero)** · 19,626★ · Python · Mature  
  General autonomous framework — the agent builds its own tools as it goes.  
  <sub>topics: agent, ai, assistant, autonomous, linux, zero</sub>
- **[hexo-ai/sia](https://github.com/hexo-ai/sia)** · 2,163★ · Python · Mature  
  Self-Improving AI — a harness whose loop optimizes the underlying system over time.  
  <sub>topics: —</sub>
- **[stakpak/agent](https://github.com/stakpak/agent)** · 1,840★ · Rust · Declining  
  An agent that lives on your machines 24/7 and keeps shipping — harness as a resident daemon.  
  <sub>topics: agent, devops, devtool, generative-ai, hacktoberfest, ai-agent, autonomous-agent, llm-agent</sub>
- **[aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch)** · 369★ · Shell · Declining  
  Watches your Claude usage windows and executes queued tasks autonomously overnight.  
  <sub>topics: —</sub>

## Graph analysis — how they relate

**Community clustering.** These 41 tools span **19 of the graph's 45 communities**.

- **Community 5** (7): `truffle-ai/dexto`, `ruvnet/ruflo`, `Yeachan-Heo/oh-my-claudecode`, `HarnessMD/munder-difflin`, `automazeio/ccpm`, `OrchestratorInc/agent-orchestrator`, `cobusgreyling/loop-engineering`
- **Community 4** (6): `langchain-ai/deepagents`, `emcie-co/parlant`, `code-yeongyu/oh-my-openagent`, `BloopAI/vibe-kanban`, `gastownhall/gastown`, `opensandbox-group/OpenSandbox`
- **Community 1** (3): `earendil-works/pi`, `AndyMik90/Aperant`, `agentsmd/agents.md`
- **Community 34** (3): `strands-agents/harness-sdk`, `SAIL-Research-Lab/cheetahclaws`, `strands-agents/shell`
- **Community 9** (3): `yologdev/yoagent`, `trycua/cua`, `stakpak/agent`
- **Community 11** (2): `1jehuang/jcode`, `coleam00/Archon`
- **Community 25** (2): `tinyhumansai/openhuman`, `tinyhumansai/tinyagents`
- **Community 16** (2): `github/spec-kit`, `Fission-AI/OpenSpec`
- **Community 15** (2): `OthmanAdi/planning-with-files`, `aniketkarne/ClaudeNightsWatch`
- **Community 33** (2): `NVIDIA/NemoClaw`, `NVIDIA/OpenShell`

**Centrality (PageRank in the full 2,585-repo graph)** — most 'hub-like' harnesses in your ecosystem:

- `affaan-m/ECC` — PageRank 0.0014
- `langchain-ai/deepagents` — PageRank 0.0010
- `multica-ai/multica` — PageRank 0.0007
- `1jehuang/jcode` — PageRank 0.0007
- `strands-agents/harness-sdk` — PageRank 0.0007
- `truffle-ai/dexto` — PageRank 0.0007
- `tinyhumansai/openhuman` — PageRank 0.0006
- `tinyhumansai/tinyagents` — PageRank 0.0006
- `NVIDIA/OpenShell` — PageRank 0.0006
- `vercel/eve` — PageRank 0.0005

**Direct links between harness projects** (top similarity edges where both endpoints are in this report):

- `tinyhumansai/tinyagents` ⇄ `tinyhumansai/openhuman` (w=1.908) — topics: ai-agents, llm, rust; authors: senamakel, M3gA-Mind, oxoxDev
- `strands-agents/shell` ⇄ `strands-agents/harness-sdk` (w=0.682) — authors: dependabot[bot], pgrayy, arronbailiss
- `cobusgreyling/loop-engineering` ⇄ `affaan-m/ECC` (w=0.459) — topics: ai-agents, claude-code, llm, mcp; authors: dependabot[bot]
- `truffle-ai/dexto` ⇄ `cobusgreyling/loop-engineering` (w=0.456) — topics: llm, mcp, ai-agents; authors: github-actions[bot], georgeatparallel
- `tinyhumansai/openhuman` ⇄ `1jehuang/jcode` (w=0.443) — topics: llm, rust, mcp; authors: github-actions[bot]
- `Fission-AI/OpenSpec` ⇄ `github/spec-kit` (w=0.408) — topics: spec, ai, engineering, prd; authors: dependabot[bot], kevin9327, Khunjua
- `bytedance/deer-flow` ⇄ `langchain-ai/deepagents` (w=0.384) — topics: ai, langchain, langgraph, python; authors: dependabot[bot]
- `Yeachan-Heo/oh-my-claudecode` ⇄ `automazeio/ccpm` (w=0.333) — topics: ai-agents, claude, claude-code, vibe-coding
- `yologdev/yoagent` ⇄ `1jehuang/jcode` (w=0.330) — topics: ai, claude, coding-agent, llm
- `affaan-m/ECC` ⇄ `automazeio/ccpm` (w=0.273) — topics: ai-agents, claude, claude-code
- `HarnessMD/munder-difflin` ⇄ `OrchestratorInc/agent-orchestrator` (w=0.250) — topics: claude-code, agent-orchestration, ai-agents, codex
- `cobusgreyling/loop-engineering` ⇄ `Yeachan-Heo/oh-my-claudecode` (w=0.224) — topics: ai-agents, claude-code, automation, claude
- `stakpak/agent` ⇄ `trycua/cua` (w=0.170) — topics: agent, hacktoberfest, ai-agent
- `yologdev/yoagent` ⇄ `stakpak/agent` (w=0.121) — topics: agent, llm-agent

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Harnesses are a young, fast-moving category — expect churn; check lifecycle before betting on one.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| OrchestratorInc/agent-orchestrator | 98 | Hot | very active | 5 | 13% | 307 |
| NVIDIA/OpenShell | 98 | Hot | very active | 6 | 13% | 103 |
| github/spec-kit | 89 | Hot | very active | 3 | 24% | 237 |
| Fission-AI/OpenSpec | 88 | Hot | very active | 3 | 37% | 56 |
| e2b-dev/runtime | 88 | Classic | very active | 3 | 37% | 52 |
| strands-agents/harness-sdk | 87 | Hot | very active | 3 | 19% | 137 |
| vercel/eve | 87 | Hot | very active | 3 | 22% | 288 |
| bytedance/deer-flow | 87 | Hot | very active | 10 | 11% | 2 |
| langchain-ai/deepagents | 84 | Hot | very active | 2 | 33% | 332 |
| tinyhumansai/openhuman | 84 | Hot | very active | 2 | 46% | 63 |
| multica-ai/multica | 81 | Hot | very active | 2 | 33% | 169 |
| NVIDIA/NemoClaw | 81 | Hot | very active | 4 | 23% | 1 |
| earendil-works/pi | 80 | Hot | very active | 1 | 63% | 275 |
| truffle-ai/dexto | 80 | Hot | very active | 2 | 42% | 1708 |
| Yeachan-Heo/oh-my-claudecode | 80 | Hot | very active | 1 | 87% | 282 |
| OthmanAdi/planning-with-files | 80 | Hot | very active | 1 | 57% | 125 |
| yologdev/yoagent | 79 | Hot | very active | 1 | 98% | 73 |
| tinyhumansai/tinyagents | 79 | Hot | very active | 1 | 83% | 11 |
| affaan-m/ECC | 79 | Hot | very active | 1 | 96% | 19 |
| coleam00/Archon | 79 | Hot | very active | 1 | 96% | 29 |
| opensandbox-group/OpenSandbox | 79 | Hot | very active | 1 | 58% | 183 |
| agent0ai/agent-zero | 79 | Mature | very active | 1 | 94% | 76 |
| code-yeongyu/oh-my-openagent | 77 | Rising | very active | 1 | 100% | 356 |
| ruvnet/ruflo | 77 | Hot | very active | 1 | 56% | 1727 |
| 1jehuang/jcode | 76 | Hot | very active | 1 | 94% | 198 |
| trycua/cua | 75 | Hot | very active | 1 | 51% | 829 |
| HarnessMD/munder-difflin | 74 | Rising | very active | 1 | 100% | 42 |
| strands-agents/shell | 70 | Hot | very active | 1 | 52% | 8 |
| SAIL-Research-Lab/cheetahclaws | 68 | Hot | very active | 1 | 77% | 43 |
| cobusgreyling/loop-engineering | 68 | Hot | very active | 1 | 69% | 2 |
| obra/superpowers | 64 | Mature | active | 1 | 100% | 16 |
| BloopAI/vibe-kanban | 64 | Mature | active | 1 | 62% | 284 |
| gastownhall/gastown | 63 | Mature | active | 1 | 100% | 14 |
| emcie-co/parlant | 53 | Mature | active | 0 | 0% | 33 |
| automazeio/ccpm | 45 | Declining | active | 1 | 100% | 0 |
| hexo-ai/sia | 44 | Mature | slowing | 2 | 43% | 0 |
| aniketkarne/ClaudeNightsWatch | 44 | Declining | active | 1 | 100% | 0 |
| AndyMik90/Aperant | 43 | Declining | slowing | 0 | 0% | 37 |
| dagger/container-use | 43 | Mature | active | 1 | 86% | 14 |
| stakpak/agent | 41 | Declining | slowing | 0 | 0% | 315 |
| agentsmd/agents.md | 36 | Declining | active | 1 | 67% | 0 |

## Which one should you use?

| If you want… | Start with | Why |
|---|---|---|
| A harness you fully own, in code | `langchain-ai/deepagents` or `earendil-works/pi` | Batteries-included loops with planning and sub-agents; pi adds a unified LLM API + TUI. |
| More out of the Claude Code you already run | `obra/superpowers` (+ `affaan-m/ECC`) | Skills + methodology layered on today; ECC adds memory, instincts, and hooks. |
| Swarms / heavy multi-agent coordination | `ruvnet/ruflo` | The meta-harness with the deepest swarm tooling in your stars. |
| A team of agents working a backlog | `BloopAI/vibe-kanban` | Kanban-shaped orchestration over Claude Code/Codex; `ccpm` if you prefer GitHub Issues + worktrees. |
| Reproducible, auditable agent output | `github/spec-kit` + `agentsmd/agents.md` | Spec-driven development plus the portable AGENTS.md behavior contract; `Fission-AI/OpenSpec` if you want a lighter, change-by-change spec workflow. |
| Crash-proof long tasks | `OthmanAdi/planning-with-files` | Plans persisted to disk — resume after any failure. |
| Safe execution for untrusted agent code | `e2b-dev/runtime` | Purpose-built sandbox runtime (cloud or self-hosted); `forkd` when you need 100 microVMs in 100ms. |
| A 24/7 resident agent | `stakpak/agent` (or `aniketkarne/ClaudeNightsWatch`) | Daemon-style autonomy; NightsWatch exploits idle Claude usage windows overnight. |
| Research-grade long-horizon autonomy | `bytedance/deer-flow` | SuperAgent harness with sub-agents and sandboxes; strongest end-to-end autonomy here. |

## Adjacent (deliberately not listed as harnesses)

- **daytonaio/daytona** — archived upstream (2026-10) — replaced by `e2b-dev/runtime` as the sandbox substrate
- **gsd-build/gsd-2** — archived upstream (2026-10) — spec-driven control is still covered by `github/spec-kit`
- **langchain-ai/langgraph** (44,260★) — agent *framework* (graphs, not harnesses) — see the agent-orchestration report
- **crewAIInc/crewAI** (60,369★) — role-playing agent framework — agent-orchestration report
- **microsoft/autogen** (61,660★) — multi-agent conversation framework — agent-orchestration report
- **eigent-ai/eigent** (15,707★) — cowork desktop product — agent-orchestration report
- **getpaseo/paseo** (22,684★) — desktop/mobile agent orchestrator — agent-orchestration report
- **wshobson/agents** (42,069★) — multi-harness plugin *marketplace* — content for harnesses, not a harness
- **EleutherAI/lm-evaluation-harness** (14,358★) — 'harness' for *model benchmarks*, not agent runtimes — see the LLM-evaluation report
- **anthropics/claude-code** (154,131★) — the coding agent itself — the thing meta-harnesses wrap

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (harness / autonomous / swarm / multi-agent / sandbox / worktree / spec-driven / long-horizon / loop…) + manual curation by *approach*. General agent frameworks and orchestration platforms live in the agent-orchestration report; Claude-Code configuration setups in the claude-code-setups report. A few boundary projects (`deer-flow`, `ruflo`, `oh-my-*`) appear in both, viewed through different lenses.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 41 · Snapshot: 2026-11-01T12:41:55.392Z</sub>
