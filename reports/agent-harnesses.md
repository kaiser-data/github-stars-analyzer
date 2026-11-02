# Agent Harnesses — Six Approaches to Running Autonomous Agents

> Derived from **kaiser-data**'s 2,587 starred repos (snapshot `2026-11-02T14:17:38.270Z`), cross-referenced with the repo-similarity graph (2,587 nodes / 8,732 edges, 42 communities).
>
> Generated 2026-11-02 by `scripts/reports/agent_harnesses.py` (regenerate any time — no API cost).

![Top tools by stars](assets/agent-harnesses-top-tools.svg)

![Tools per category](assets/agent-harnesses-categories.svg)


## Executive summary

- A **harness** is everything around the model: the loop, tools, state, guardrails, and execution environment. **41 harness projects** in your stars (**1,709,958★** combined) cluster into **six distinct approaches** — they disagree about *where the harness lives* and *what the hard problem is*:
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
| [obra/superpowers](https://github.com/obra/superpowers) | Meta-harness over coding agents | Shell | MIT | 310,991 (▲651) | Mature | 64 | active | 4d ago | 1.1y | 1 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Meta-harness over coding agents | JavaScript | MIT | 295,236 (▲835) | Hot | 79 | very active | 0d ago | 9mo | 4 |
| [github/spec-kit](https://github.com/github/spec-kit) | Determinism & spec-driven | Python | MIT | 145,248 (▲571) | Hot | 89 | very active | 3d ago | 1.2y | 26 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness-as-SDK | TypeScript | MIT | 119,536 (▲261) | Hot | 80 | very active | 0d ago | 1.2y | 8 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Autonomous long-horizon | Python | MIT | 84,879 (▲62) | Hot | 87 | very active | 0d ago | 1.5y | 45 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Meta-harness over coding agents | TypeScript | MIT | 80,601 (▲129) | Hot | 77 | very active | 0d ago | 1.4y | 11 |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | Determinism & spec-driven | TypeScript | MIT | 73,684 (▲114) | Hot | 88 | very active | 0d ago | 1.2y | 37 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Meta-harness over coding agents | TypeScript | NOASSERTION | 70,612 (▲43) | Rising | 77 | very active | 0d ago | 11mo | 1 |
| [multica-ai/multica](https://github.com/multica-ai/multica) | Fleet / parallel orchestration | Go | NOASSERTION | 54,629 (▲140) | Hot | 87 | very active | 0d ago | 9mo | 29 |
| [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Harness-as-SDK | Rust | GPL-3.0 | 42,496 (▲37) | Hot | 79 | very active | 0d ago | 8mo | 5 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Meta-harness over coding agents | TypeScript | MIT | 40,513 (▲36) | Hot | 80 | very active | 0d ago | 9mo | 7 |
| [trycua/cua](https://github.com/trycua/cua) | Sandbox substrate | Rust | MIT | 31,574 (▲106) | Hot | 75 | very active | 0d ago | 1.8y | 7 |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Harness-as-SDK | Python | MIT | 30,902 (▲54) | Hot | 84 | very active | 0d ago | 1.3y | 12 |
| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Fleet / parallel orchestration | Rust | Apache-2.0 | 28,562 (▲12) | Mature | 64 | active | 4d ago | 1.4y | 4 |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | Determinism & spec-driven | Shell | MIT | 27,826 (▲22) | Hot | 79 | very active | 3d ago | 10mo | 18 |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | Determinism & spec-driven | TypeScript | MIT | 25,277 (▲21) | Declining | 36 | active | 1mo ago | 1.2y | 2 |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Meta-harness over coding agents | TypeScript | MIT | 23,805 (▲9) | Hot | 79 | very active | 0d ago | 1.7y | 3 |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Sandbox substrate | TypeScript | Apache-2.0 | 22,918 (▲13) | Hot | 81 | very active | 0d ago | 7mo | 20 |
| [1jehuang/jcode](https://github.com/1jehuang/jcode) | Harness-as-SDK | Rust | MIT | 21,414 (▲31) | Rising | 76 | very active | 0d ago | 10mo | 2 |
| [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | Sandbox substrate | Rust | Apache-2.0 | 20,954 (▲87) | Hot | 98 | very active | 0d ago | 8mo | 31 |
| [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | Autonomous long-horizon | Python | NOASSERTION | 19,648 (▲22) | Mature | 79 | very active | 1d ago | 2.4y | 3 |
| [gastownhall/gastown](https://github.com/gastownhall/gastown) | Fleet / parallel orchestration | Go | MIT | 18,664 (▲14) | Mature | 63 | active | 5d ago | 10mo | 1 |
| [emcie-co/parlant](https://github.com/emcie-co/parlant) | Harness-as-SDK | Python | Apache-2.0 | 18,317 (▲5) | Mature | 53 | active | 0d ago | 2.7y | 0 |
| [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | Sandbox substrate | Python | Apache-2.0 | 16,391 (▲36) | Hot | 79 | very active | 0d ago | 10mo | 8 |
| [AndyMik90/Aperant](https://github.com/AndyMik90/Aperant) | Fleet / parallel orchestration | TypeScript | AGPL-3.0 | 14,585 | Declining | 43 | slowing | 4mo ago | 11mo | 0 |
| [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | Fleet / parallel orchestration | Go | Apache-2.0 | 14,010 (▲32) | Hot | 98 | very active | 0d ago | 8mo | 24 |
| [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | Determinism & spec-driven | TypeScript | MIT | 11,681 (▲5) | Hot | 68 | very active | 0d ago | 4mo | 11 |
| [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin) | Meta-harness over coding agents | JavaScript | MIT | 9,294 (▲29) | Rising | 74 | very active | 0d ago | 5mo | 1 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | Harness-as-SDK | Python | Apache-2.0 | 9,028 (▲9) | Hot | 87 | very active | 0d ago | 1.5y | 31 |
| [automazeio/ccpm](https://github.com/automazeio/ccpm) | Fleet / parallel orchestration | Shell | MIT | 8,425 | Declining | 45 | active | 14d ago | 1.2y | 1 |
| [vercel/eve](https://github.com/vercel/eve) | Harness-as-SDK | TypeScript | Apache-2.0 | 5,771 (▲15) | Hot | 87 | very active | 0d ago | 4mo | 14 |
| [dagger/container-use](https://github.com/dagger/container-use) | Fleet / parallel orchestration | Go | Apache-2.0 | 4,083 (▼1) | Mature | 43 | active | 1mo ago | 1.4y | 2 |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | Autonomous long-horizon | Python | MIT | 2,164 (▲1) | Mature | 44 | slowing | 2mo ago | 7mo | 5 |
| [stakpak/agent](https://github.com/stakpak/agent) | Autonomous long-horizon | Rust | Apache-2.0 | 1,843 (▲3) | Declining | 41 | slowing | 3mo ago | 1.9y | 0 |
| [e2b-dev/runtime](https://github.com/e2b-dev/runtime) | Sandbox substrate | Go | Apache-2.0 | 1,798 (▲4) | Classic | 88 | very active | 0d ago | 3.2y | 18 |
| [SAIL-Research-Lab/cheetahclaws](https://github.com/SAIL-Research-Lab/cheetahclaws) | Harness-as-SDK | Python | Apache-2.0 | 794 (▲1) | Hot | 68 | very active | 1d ago | 7mo | 7 |
| [truffle-ai/dexto](https://github.com/truffle-ai/dexto) | Harness-as-SDK | TypeScript | NOASSERTION | 659 | Hot | 80 | very active | 0d ago | 1.6y | 5 |
| [aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch) | Autonomous long-horizon | Shell | MIT | 369 | Declining | 44 | active | 18d ago | 1.3y | 1 |
| [yologdev/yoagent](https://github.com/yologdev/yoagent) | Harness-as-SDK | Rust | MIT | 367 (▲1) | Hot | 80 | very active | 0d ago | 8mo | 3 |
| [strands-agents/shell](https://github.com/strands-agents/shell) | Sandbox substrate | Rust | Apache-2.0 | 281 | Hot | 71 | very active | 0d ago | 8mo | 5 |
| [tinyhumansai/tinyagents](https://github.com/tinyhumansai/tinyagents) | Harness-as-SDK | Rust | GPL-3.0 | 129 (▲1) | Hot | 79 | very active | 3d ago | 4mo | 3 |

## By approach

### Harness-as-SDK

_The loop as a library: you import the harness, register tools, and own control flow. Maximum flexibility, maximum responsibility — you maintain planning, retries, memory, and safety yourself._

- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 119,536★ · TypeScript · Hot  
  Unified LLM API + agent loop + TUI + coding-agent CLI in one toolkit — the loop as a library.  
  <sub>topics: —</sub>
- **[tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman)** · 42,496★ · Rust · Hot  
  Lean open-source harness built for density — claims 500+ agents on a $10 VPS; the cost-floor end of the field.  
  <sub>topics: ai-agents, llm, local-first, rust, agent-orchestration, ai-assistant, desktop, mcp</sub>
- **[langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)** · 30,902★ · Python · Hot  
  The 'batteries-included agent harness' — planning, sub-agents, filesystem, from the LangChain team.  
  <sub>topics: deepagents, langchain, langgraph, ai, python, typescript, harness, harness-engineering</sub>
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 21,414★ · Rust · Rising  
  Rust-built coding-agent harness — CLI agent loop with MCP support and multi-model wiring.  
  <sub>topics: ai, claude, cli, coding-agent, llm, mcp, openai, rust</sub>
- **[emcie-co/parlant](https://github.com/emcie-co/parlant)** · 18,317★ · Python · Mature  
  Interaction *control* harness — behavioral guidelines enforced at runtime for customer-facing agents.  
  <sub>topics: ai-agents, genai, llm, customer-service, customer-success, gemini, llama3, openai</sub>
- **[strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)** · 9,028★ · Python · Hot  
  AWS's open SDK to build an agent harness and control it end-to-end in production.  
  <sub>topics: agentic, agentic-ai, agents, ai, autonomous-agents, llm, multi-agent-systems, python</sub>
- **[vercel/eve](https://github.com/vercel/eve)** · 5,771★ · TypeScript · Hot  
  Vercel's framework for building agents — harness + sandbox as one integrated runtime.  
  <sub>topics: agent, framework, harness, javascript, markdown, typescript, vercel, sandbox</sub>
- **[SAIL-Research-Lab/cheetahclaws](https://github.com/SAIL-Research-Lab/cheetahclaws)** · 794★ · Python · Hot  
  Fast, easy agent-harness infrastructure aimed at long-horizon, multi-model runs.  
  <sub>topics: agentic-ai, claude, claude-code, memory, python, skills, openclaw</sub>
- **[truffle-ai/dexto](https://github.com/truffle-ai/dexto)** · 659★ · TypeScript · Hot  
  Harness and toolkit for building agent apps — CLI plus SDKs, configured rather than coded.  
  <sub>topics: llm, mcp, typescript, ai-agents, ai-tools, modelcontextprotocol, ai, mcp-client</sub>
- **[yologdev/yoagent](https://github.com/yologdev/yoagent)** · 367★ · Rust · Hot  
  The agent loop as a Rust crate — streams from seven LLM protocols, runs tools, loops until done.  
  <sub>topics: agent, agent-framework, ai, ai-agents, anthropic, claude, coding-agent, gemini</sub>
- **[tinyhumansai/tinyagents](https://github.com/tinyhumansai/tinyagents)** · 129★ · Rust · Hot  
  Small, provider-neutral harness in Rust — a readable minimal loop from the openhuman team.  
  <sub>topics: agent-framework, ai-agents, llm, rust, artificial-intelligence, automation, developer-tools, multi-agent</sub>

### Meta-harness over coding agents

_These projects treat Claude Code / Codex as the engine and build the transmission: skills, personas, memory, token discipline, and multi-agent coordination injected via configs, hooks, and subagents._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 310,991★ · Shell · Mature  
  Skills framework + development methodology layered onto the agent you already run.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 295,236★ · JavaScript · Hot  
  Harness performance optimization: skills, instincts, memory, security, hooks on top of Claude Code.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 80,601★ · TypeScript · Hot  
  The leading agent *meta*-harness — swarms, coordination, and autonomy on top of existing agents.  
  <sub>topics: swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server, multi-agent</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 70,612★ · TypeScript · Rising  
  'The one and only agent harness for complex coding' — tokenmaxxer harness wrapping coding agents.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 40,513★ · TypeScript · Hot  
  Teams-first multi-agent orchestration living entirely inside Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>
- **[coleam00/Archon](https://github.com/coleam00/Archon)** · 23,805★ · TypeScript · Hot  
  'Harness builder' — make AI coding deterministic and repeatable by generating the harness itself.  
  <sub>topics: ai, automation, bun, claude, cli, coding-assistant, developer-tools, typescript</sub>
- **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** · 9,294★ · JavaScript · Rising  
  Runs an 'office' of Claude Code / Codex agents with roles — an open alternative to hosted agent-team products.  
  <sub>topics: agents, claude-code, harness, harness-engineering, memory, agent-orchestration, ai-agents, autonomous-agents</sub>

### Fleet / parallel orchestration

_One agent is a tool; a fleet is a team. The harness problem becomes scheduling, isolation (worktrees, containers), review queues, and merge discipline._

- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 54,629★ · Go · Hot  
  Managed-agents platform: assign tasks to coding agents like teammates and supervise them.  
  <sub>topics: —</sub>
- **[BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban)** · 28,562★ · Rust · Mature  
  A kanban board as the harness — queue, run, and review many agent tasks in parallel.  
  <sub>topics: agent, ai-agents, kanban, management, task-manager</sub>
- **[gastownhall/gastown](https://github.com/gastownhall/gastown)** · 18,664★ · Go · Mature  
  Multi-agent workspace manager — the 'town' where a fleet of agents live and work.  
  <sub>topics: —</sub>
- **[AndyMik90/Aperant](https://github.com/AndyMik90/Aperant)** · 14,585★ · TypeScript · Declining  
  Autonomous multi-session AI coding — sessions as the unit of parallelism.  
  <sub>topics: —</sub>
- **[OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator)** · 14,010★ · Go · Hot  
  Plans tasks, spawns parallel coding agents in worktrees, merges autonomously.  
  <sub>topics: claude-code, codex-cli, orchestration, orchestrator, skills, agent-fleet, agent-swarm, git-worktrees</sub>
- **[automazeio/ccpm](https://github.com/automazeio/ccpm)** · 8,425★ · Shell · Declining  
  GitHub Issues + git worktrees as the coordination fabric for parallel agents.  
  <sub>topics: ai-agents, ai-coding, claude, claude-code, project-management, vibe-coding</sub>
- **[dagger/container-use](https://github.com/dagger/container-use)** · 4,083★ · Go · Mature  
  Containerized dev environments so multiple agents work safely and independently.  
  <sub>topics: —</sub>

### Determinism & spec-driven

_The counter-culture: agents drift, so pin them down. Specs, standards files, and plans persisted to disk make runs reproducible, auditable, and resumable after crashes._

- **[github/spec-kit](https://github.com/github/spec-kit)** · 145,248★ · Python · Hot  
  Spec-Driven Development toolkit — the spec, not the prompt, steers the agent.  
  <sub>topics: ai, copilot, development, engineering, prd, spec, spec-driven</sub>
- **[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)** · 73,684★ · TypeScript · Hot  
  Lightweight spec-driven development — change proposals and specs in the repo that humans and agents agree on before code is written.  
  <sub>topics: spec, ai, context-engineering, engineering, planning, prd, sdlc, spec-driven-development</sub>
- **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** · 27,826★ · Shell · Hot  
  Persistent file-based planning — crash-proof, resumable long-running agent tasks.  
  <sub>topics: claude, claude-code, claude-skills, manus, agent-skills, planning, autonomous-agents, codex</sub>
- **[agentsmd/agents.md](https://github.com/agentsmd/agents.md)** · 25,277★ · TypeScript · Declining  
  The open AGENTS.md standard — a portable contract telling any harness how to behave in a repo.  
  <sub>topics: —</sub>
- **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** · 11,681★ · TypeScript · Hot  
  Patterns and starters for *loop engineering* — designing the iteration, not just the prompt.  
  <sub>topics: agentic-ai, ai-agents, claude-code, codex, devops-automation, github-actions, grok, llm</sub>

### Sandbox substrate

_Infrastructure-first: before you scale agents you need somewhere safe and fast to run them. MicroVMs, container runtimes, and hardened sandboxes are the harness's floor._

- **[trycua/cua](https://github.com/trycua/cua)** · 31,574★ · Rust · Hot  
  Sandboxes, SDKs, and benchmarks for computer-use agents — full-desktop harnessing.  
  <sub>topics: apple, cua, lume, macos, virtualization, virtualization-framework, swift, ai-agent</sub>
- **[NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)** · 22,918★ · TypeScript · Hot  
  Run harnesses (Hermes, Deep Agents, OpenClaw) inside hardened NVIDIA sandboxes.  
  <sub>topics: ai-agents, nvidia, openclaw, openshell, sandboxing, typescript, hermes, deep-agents</sub>
- **[NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)** · 20,954★ · Rust · Hot  
  NVIDIA's safe, private runtime for autonomous agents — the substrate NemoClaw runs on.  
  <sub>topics: —</sub>
- **[opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)** · 16,391★ · Python · Hot  
  Secure, fast, extensible sandbox runtime purpose-built for AI agents.  
  <sub>topics: ai, ai-infra, kubernetes, sandbox, ai-agent, aaif</sub>
- **[e2b-dev/runtime](https://github.com/e2b-dev/runtime)** · 1,798★ · Go · Classic  
  The runtime behind E2B's cloud and self-hosted sandboxes — isolated microVMs for AI-generated code; the harness's execution floor.  
  <sub>topics: ai-agents, code-interpreter, consul, devtools, firecracker, gcp, go, golang</sub>
- **[strands-agents/shell](https://github.com/strands-agents/shell)** · 281★ · Rust · Hot  
  A shell for the agent without the keys to your machine — scoped command execution as a library.  
  <sub>topics: —</sub>

### Autonomous long-horizon

_Maximum autonomy: agents that run for hours or days, planning and re-planning, sometimes improving their own scaffolding. The harness is a resident process, not a CLI invocation._

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 84,879★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and creates with sub-agents in sandboxes.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[agent0ai/agent-zero](https://github.com/agent0ai/agent-zero)** · 19,648★ · Python · Mature  
  General autonomous framework — the agent builds its own tools as it goes.  
  <sub>topics: agent, ai, assistant, autonomous, linux, zero</sub>
- **[hexo-ai/sia](https://github.com/hexo-ai/sia)** · 2,164★ · Python · Mature  
  Self-Improving AI — a harness whose loop optimizes the underlying system over time.  
  <sub>topics: —</sub>
- **[stakpak/agent](https://github.com/stakpak/agent)** · 1,843★ · Rust · Declining  
  An agent that lives on your machines 24/7 and keeps shipping — harness as a resident daemon.  
  <sub>topics: agent, devops, devtool, generative-ai, hacktoberfest, ai-agent, autonomous-agent, llm-agent</sub>
- **[aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch)** · 369★ · Shell · Declining  
  Watches your Claude usage windows and executes queued tasks autonomously overnight.  
  <sub>topics: —</sub>

## Graph analysis — how they relate

**Community clustering.** These 41 tools span **18 of the graph's 42 communities**.

- **Community 26** (8): `SAIL-Research-Lab/cheetahclaws`, `yologdev/yoagent`, `Yeachan-Heo/oh-my-claudecode`, `HarnessMD/munder-difflin`, `gastownhall/gastown`, `automazeio/ccpm`, `OrchestratorInc/agent-orchestrator`, `OthmanAdi/planning-with-files`
- **Community 1** (5): `earendil-works/pi`, `AndyMik90/Aperant`, `github/spec-kit`, `Fission-AI/OpenSpec`, `agentsmd/agents.md`
- **Community 5** (4): `langchain-ai/deepagents`, `code-yeongyu/oh-my-openagent`, `BloopAI/vibe-kanban`, `opensandbox-group/OpenSandbox`
- **Community 32** (4): `strands-agents/harness-sdk`, `ruvnet/ruflo`, `strands-agents/shell`, `bytedance/deer-flow`
- **Community 11** (3): `1jehuang/jcode`, `truffle-ai/dexto`, `coleam00/Archon`
- **Community 23** (2): `tinyhumansai/openhuman`, `tinyhumansai/tinyagents`
- **Community 6** (2): `affaan-m/ECC`, `cobusgreyling/loop-engineering`
- **Community 31** (2): `NVIDIA/NemoClaw`, `NVIDIA/OpenShell`
- **Community 0** (2): `hexo-ai/sia`, `stakpak/agent`

**Centrality (PageRank in the full 2,587-repo graph)** — most 'hub-like' harnesses in your ecosystem:

- `affaan-m/ECC` — PageRank 0.0013
- `1jehuang/jcode` — PageRank 0.0011
- `langchain-ai/deepagents` — PageRank 0.0010
- `multica-ai/multica` — PageRank 0.0008
- `truffle-ai/dexto` — PageRank 0.0006
- `tinyhumansai/tinyagents` — PageRank 0.0006
- `strands-agents/harness-sdk` — PageRank 0.0006
- `NVIDIA/OpenShell` — PageRank 0.0006
- `tinyhumansai/openhuman` — PageRank 0.0005
- `vercel/eve` — PageRank 0.0005

**Direct links between harness projects** (top similarity edges where both endpoints are in this report):

- `tinyhumansai/tinyagents` ⇄ `tinyhumansai/openhuman` (w=1.908) — topics: ai-agents, llm, rust; authors: senamakel, M3gA-Mind, oxoxDev
- `strands-agents/shell` ⇄ `strands-agents/harness-sdk` (w=0.682) — authors: dependabot[bot], pgrayy, arronbailiss
- `truffle-ai/dexto` ⇄ `1jehuang/jcode` (w=0.544) — topics: llm, mcp, ai, ai-agent; authors: github-actions[bot]
- `cobusgreyling/loop-engineering` ⇄ `affaan-m/ECC` (w=0.459) — topics: ai-agents, claude-code, llm, mcp; authors: dependabot[bot]
- `truffle-ai/dexto` ⇄ `cobusgreyling/loop-engineering` (w=0.456) — topics: llm, mcp, ai-agents; authors: github-actions[bot], georgeatparallel
- `Fission-AI/OpenSpec` ⇄ `github/spec-kit` (w=0.408) — topics: spec, ai, engineering, prd; authors: dependabot[bot], kevin9327, Khunjua
- `bytedance/deer-flow` ⇄ `langchain-ai/deepagents` (w=0.386) — topics: ai, langchain, langgraph, python; authors: dependabot[bot]
- `Yeachan-Heo/oh-my-claudecode` ⇄ `automazeio/ccpm` (w=0.333) — topics: ai-agents, claude, claude-code, vibe-coding
- `yologdev/yoagent` ⇄ `1jehuang/jcode` (w=0.330) — topics: ai, claude, coding-agent, llm
- `affaan-m/ECC` ⇄ `automazeio/ccpm` (w=0.273) — topics: ai-agents, claude, claude-code
- `HarnessMD/munder-difflin` ⇄ `OrchestratorInc/agent-orchestrator` (w=0.250) — topics: claude-code, agent-orchestration, ai-agents, codex
- `cobusgreyling/loop-engineering` ⇄ `Yeachan-Heo/oh-my-claudecode` (w=0.224) — topics: ai-agents, claude-code, automation, claude
- `HarnessMD/munder-difflin` ⇄ `ruvnet/ruflo` (w=0.212) — topics: agents, harness, ai-agents, autonomous-agents
- `strands-agents/harness-sdk` ⇄ `ruvnet/ruflo` (w=0.212) — topics: agentic-ai, agents, autonomous-agents, multi-agent-systems
- `stakpak/agent` ⇄ `trycua/cua` (w=0.170) — topics: agent, hacktoberfest, ai-agent
- …and 1 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Harnesses are a young, fast-moving category — expect churn; check lifecycle before betting on one.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| OrchestratorInc/agent-orchestrator | 98 | Hot | very active | 6 | 13% | 308 |
| NVIDIA/OpenShell | 98 | Hot | very active | 6 | 13% | 103 |
| github/spec-kit | 89 | Hot | very active | 3 | 24% | 237 |
| Fission-AI/OpenSpec | 88 | Hot | very active | 3 | 37% | 56 |
| e2b-dev/runtime | 88 | Classic | very active | 3 | 37% | 52 |
| strands-agents/harness-sdk | 87 | Hot | very active | 3 | 19% | 137 |
| vercel/eve | 87 | Hot | very active | 3 | 22% | 288 |
| multica-ai/multica | 87 | Hot | very active | 3 | 34% | 169 |
| bytedance/deer-flow | 87 | Hot | very active | 10 | 12% | 2 |
| langchain-ai/deepagents | 84 | Hot | very active | 2 | 36% | 332 |
| NVIDIA/NemoClaw | 81 | Hot | very active | 4 | 21% | 1 |
| earendil-works/pi | 80 | Hot | very active | 1 | 72% | 276 |
| yologdev/yoagent | 80 | Hot | very active | 1 | 98% | 75 |
| truffle-ai/dexto | 80 | Hot | very active | 2 | 40% | 1730 |
| Yeachan-Heo/oh-my-claudecode | 80 | Hot | very active | 1 | 85% | 285 |
| tinyhumansai/openhuman | 79 | Hot | very active | 1 | 53% | 63 |
| tinyhumansai/tinyagents | 79 | Hot | very active | 1 | 83% | 11 |
| affaan-m/ECC | 79 | Hot | very active | 1 | 96% | 19 |
| coleam00/Archon | 79 | Hot | very active | 1 | 96% | 29 |
| OthmanAdi/planning-with-files | 79 | Hot | very active | 1 | 57% | 125 |
| opensandbox-group/OpenSandbox | 79 | Hot | very active | 1 | 64% | 183 |
| agent0ai/agent-zero | 79 | Mature | very active | 1 | 76% | 77 |
| code-yeongyu/oh-my-openagent | 77 | Rising | very active | 1 | 100% | 358 |
| ruvnet/ruflo | 77 | Hot | very active | 1 | 60% | 1730 |
| 1jehuang/jcode | 76 | Rising | very active | 1 | 93% | 201 |
| trycua/cua | 75 | Hot | very active | 1 | 53% | 834 |
| HarnessMD/munder-difflin | 74 | Rising | very active | 1 | 100% | 42 |
| strands-agents/shell | 71 | Hot | very active | 1 | 50% | 8 |
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
- **langchain-ai/langgraph** (44,334★) — agent *framework* (graphs, not harnesses) — see the agent-orchestration report
- **crewAIInc/crewAI** (60,420★) — role-playing agent framework — agent-orchestration report
- **microsoft/autogen** (61,677★) — multi-agent conversation framework — agent-orchestration report
- **eigent-ai/eigent** (15,720★) — cowork desktop product — agent-orchestration report
- **getpaseo/paseo** (22,802★) — desktop/mobile agent orchestrator — agent-orchestration report
- **wshobson/agents** (42,097★) — multi-harness plugin *marketplace* — content for harnesses, not a harness
- **EleutherAI/lm-evaluation-harness** (14,371★) — 'harness' for *model benchmarks*, not agent runtimes — see the LLM-evaluation report
- **anthropics/claude-code** (154,257★) — the coding agent itself — the thing meta-harnesses wrap

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (harness / autonomous / swarm / multi-agent / sandbox / worktree / spec-driven / long-horizon / loop…) + manual curation by *approach*. General agent frameworks and orchestration platforms live in the agent-orchestration report; Claude-Code configuration setups in the claude-code-setups report. A few boundary projects (`deer-flow`, `ruflo`, `oh-my-*`) appear in both, viewed through different lenses.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 41 · Snapshot: 2026-11-02T14:17:38.270Z</sub>
