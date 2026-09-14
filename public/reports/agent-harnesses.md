# Agent Harnesses — Six Approaches to Running Autonomous Agents

> Derived from **kaiser-data**'s 2,159 starred repos (snapshot `2026-09-14T11:08:08.535Z`), cross-referenced with the repo-similarity graph (2,159 nodes / 7,086 edges, 37 communities).
>
> Generated 2026-09-14 by `scripts/reports/agent_harnesses.py` (regenerate any time — no API cost).

![Top tools by stars](assets/agent-harnesses-top-tools.svg)

![Tools per category](assets/agent-harnesses-categories.svg)


## Executive summary

- A **harness** is everything around the model: the loop, tools, state, guardrails, and execution environment. **36 harness projects** in your stars (**1,517,221★** combined) cluster into **six distinct approaches** — they disagree about *where the harness lives* and *what the hard problem is*:
  - **Harness-as-SDK** (8): `pi`, `deepagents`, `jcode`, `parlant`, `harness-sdk`, `eve`, `pydantic-ai-harness`, `cheetahclaws`
  - **Meta-harness over coding agents** (6): `superpowers`, `ECC`, `ruflo`, `oh-my-openagent`, `oh-my-claudecode`, `Archon`
  - **Fleet / parallel orchestration** (7): `multica`, `vibe-kanban`, `gastown`, `Aperant`, `agent-orchestrator`, `ccpm`, `container-use`
  - **Determinism & spec-driven** (5): `spec-kit`, `planning-with-files`, `agents.md`, `loop-engineering`, `gsd-2`
  - **Sandbox substrate** (5): `daytona`, `cua`, `NemoClaw`, `OpenSandbox`, `forkd`
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
| [obra/superpowers](https://github.com/obra/superpowers) | Meta-harness over coding agents | Shell | MIT | 286,443 (▲4,259) | Hot | 78 | very active | 2d ago | 11mo | 6 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Meta-harness over coding agents | JavaScript | MIT | 258,025 (▲7,749) | Hot | 79 | very active | 0d ago | 7mo | 18 |
| [github/spec-kit](https://github.com/github/spec-kit) | Determinism & spec-driven | Python | MIT | 136,618 (▲2,975) | Hot | 99 | very active | 2d ago | 1.1y | 27 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness-as-SDK | TypeScript | MIT | 104,948 (▲2,733) | Hot | 90 | very active | 0d ago | 1.1y | 16 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Autonomous long-horizon | Python | MIT | 82,408 (▲954) | Hot | 84 | very active | 0d ago | 1.4y | 44 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Meta-harness over coding agents | TypeScript | MIT | 72,387 (▲1,604) | Hot | 76 | very active | 0d ago | 1.3y | 5 |
| [daytonaio/daytona](https://github.com/daytonaio/daytona) | Sandbox substrate | — | — | 71,713 (▼71) | Mature | 82 | active | 1mo ago | 2.6y | 15 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Meta-harness over coding agents | TypeScript | NOASSERTION | 69,029 (▲290) | Rising | 78 | very active | 0d ago | 9mo | 1 |
| [multica-ai/multica](https://github.com/multica-ai/multica) | Fleet / parallel orchestration | Go | NOASSERTION | 49,786 (▲771) | Hot | 82 | very active | 0d ago | 8mo | 18 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Meta-harness over coding agents | TypeScript | MIT | 39,149 (▲119) | Hot | 80 | very active | 0d ago | 8mo | 8 |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Harness-as-SDK | Python | MIT | 29,397 (▲349) | Hot | 89 | very active | 0d ago | 1.1y | 13 |
| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Fleet / parallel orchestration | Rust | Apache-2.0 | 28,078 (▲57) | Declining | 50 | active | 2d ago | 1.3y | 0 |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | Determinism & spec-driven | Shell | MIT | 26,876 (▲226) | Hot | 79 | very active | 0d ago | 8mo | 6 |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | Determinism & spec-driven | TypeScript | MIT | 24,359 (▲194) | Declining | 40 | active | 4d ago | 1.1y | 2 |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Meta-harness over coding agents | TypeScript | MIT | 23,457 (▲68) | Hot | 78 | very active | 0d ago | 1.6y | 3 |
| [trycua/cua](https://github.com/trycua/cua) | Sandbox substrate | HTML | MIT | 22,618 (▲368) | Hot | 75 | very active | 0d ago | 1.6y | 10 |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Sandbox substrate | TypeScript | Apache-2.0 | 22,452 (▲72) | Hot | 74 | very active | 0d ago | 6mo | 14 |
| [1jehuang/jcode](https://github.com/1jehuang/jcode) | Harness-as-SDK | Rust | MIT | 19,666 (▲477) | Hot | 76 | very active | 0d ago | 8mo | 4 |
| [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | Autonomous long-horizon | Python | NOASSERTION | 19,164 (▲63) | Mature | 79 | very active | 2d ago | 2.3y | 2 |
| [emcie-co/parlant](https://github.com/emcie-co/parlant) | Harness-as-SDK | Python | Apache-2.0 | 18,285 (▲7) | Mature | 60 | slowing | 2mo ago | 2.6y | 2 |
| [gastownhall/gastown](https://github.com/gastownhall/gastown) | Fleet / parallel orchestration | Go | MIT | 18,052 (▲113) | Hot | 77 | very active | 4d ago | 9mo | 9 |
| [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | Sandbox substrate | Python | Apache-2.0 | 15,202 (▲202) | Hot | 93 | very active | 0d ago | 9mo | 21 |
| [AndyMik90/Aperant](https://github.com/AndyMik90/Aperant) | Fleet / parallel orchestration | TypeScript | AGPL-3.0 | 14,560 (▲2) | Declining | 47 | slowing | 3mo ago | 9mo | 0 |
| [Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) | Fleet / parallel orchestration | Go | Apache-2.0 | 12,004 (▲1,021) | Hot | 98 | very active | 0d ago | 7mo | 30 |
| [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | Determinism & spec-driven | TypeScript | MIT | 11,202 (▲185) | Hot | 68 | very active | 0d ago | 3mo | 16 |
| [automazeio/ccpm](https://github.com/automazeio/ccpm) | Fleet / parallel orchestration | Shell | MIT | 8,372 (▲9) | Declining | 25 | slowing | 6mo ago | 1.1y | 0 |
| [gsd-build/gsd-2](https://github.com/gsd-build/gsd-2) | Determinism & spec-driven | TypeScript | MIT | 7,773 (▲1) | Declining | 45 | slowing | 3mo ago | 6mo | 0 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | Harness-as-SDK | Python | Apache-2.0 | 7,238 (▲75) | Hot | 92 | very active | 0d ago | 1.3y | 25 |
| [vercel/eve](https://github.com/vercel/eve) | Harness-as-SDK | TypeScript | Apache-2.0 | 5,107 (▲122) | Hot | 90 | very active | 0d ago | 3mo | 19 |
| [dagger/container-use](https://github.com/dagger/container-use) | Fleet / parallel orchestration | Go | Apache-2.0 | 4,042 (▲9) | Mature | 46 | active | 7d ago | 1.3y | 2 |
| [deeplethe/forkd](https://github.com/deeplethe/forkd) | Sandbox substrate | Rust | Apache-2.0 | 2,843 (▲12) | Hot | 79 | very active | 0d ago | 4mo | 4 |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | Autonomous long-horizon | Python | MIT | 2,150 (▲8) | Rising | 51 | active | 19d ago | 5mo | 7 |
| [stakpak/agent](https://github.com/stakpak/agent) | Autonomous long-horizon | Rust | Apache-2.0 | 1,783 (▲12) | Mature | 56 | slowing | 2mo ago | 1.8y | 2 |
| [pydantic/pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness) | Harness-as-SDK | Python | MIT | 890 (▲33) | Hot | 84 | very active | 2d ago | 5mo | 20 |
| [SAIL-Research-Lab/cheetahclaws](https://github.com/SAIL-Research-Lab/cheetahclaws) | Harness-as-SDK | Python | Apache-2.0 | 775 (▲4) | Hot | 74 | very active | 2d ago | 5mo | 7 |
| [aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch) | Autonomous long-horizon | Shell | MIT | 370 | Declining | 43 | active | 4d ago | 1.2y | 1 |

## By approach

### Harness-as-SDK

_The loop as a library: you import the harness, register tools, and own control flow. Maximum flexibility, maximum responsibility — you maintain planning, retries, memory, and safety yourself._

- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 104,948★ · TypeScript · Hot  
  Unified LLM API + agent loop + TUI + coding-agent CLI in one toolkit — the loop as a library.  
  <sub>topics: —</sub>
- **[langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)** · 29,397★ · Python · Hot  
  The 'batteries-included agent harness' — planning, sub-agents, filesystem, from the LangChain team.  
  <sub>topics: deepagents, langchain, langgraph, ai, python, typescript, harness, harness-engineering</sub>
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 19,666★ · Rust · Hot  
  Rust-built coding-agent harness — CLI agent loop with MCP support and multi-model wiring.  
  <sub>topics: ai, claude, cli, coding-agent, llm, mcp, openai, rust</sub>
- **[emcie-co/parlant](https://github.com/emcie-co/parlant)** · 18,285★ · Python · Mature  
  Interaction *control* harness — behavioral guidelines enforced at runtime for customer-facing agents.  
  <sub>topics: ai-agents, genai, llm, customer-service, customer-success, gemini, llama3, openai</sub>
- **[strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)** · 7,238★ · Python · Hot  
  AWS's open SDK to build an agent harness and control it end-to-end in production.  
  <sub>topics: agentic, agentic-ai, agents, ai, autonomous-agents, llm, multi-agent-systems, python</sub>
- **[vercel/eve](https://github.com/vercel/eve)** · 5,107★ · TypeScript · Hot  
  Vercel's framework for building agents — harness + sandbox as one integrated runtime.  
  <sub>topics: agent, framework, harness, javascript, markdown, typescript, vercel, sandbox</sub>
- **[pydantic/pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness)** · 890★ · Python · Hot  
  'Batteries for your Pydantic AI agent' — the harness as a thin add-on to a typed agent framework.  
  <sub>topics: —</sub>
- **[SAIL-Research-Lab/cheetahclaws](https://github.com/SAIL-Research-Lab/cheetahclaws)** · 775★ · Python · Hot  
  Fast, easy agent-harness infrastructure aimed at long-horizon, multi-model runs.  
  <sub>topics: agentic-ai, claude, claude-code, memory, python, skills, openclaw</sub>

### Meta-harness over coding agents

_These projects treat Claude Code / Codex as the engine and build the transmission: skills, personas, memory, token discipline, and multi-agent coordination injected via configs, hooks, and subagents._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 286,443★ · Shell · Hot  
  Skills framework + development methodology layered onto the agent you already run.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 258,025★ · JavaScript · Hot  
  Harness performance optimization: skills, instincts, memory, security, hooks on top of Claude Code.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 72,387★ · TypeScript · Hot  
  The leading agent *meta*-harness — swarms, coordination, and autonomy on top of existing agents.  
  <sub>topics: claude-code, swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 69,029★ · TypeScript · Rising  
  'The one and only agent harness for complex coding' — tokenmaxxer harness wrapping coding agents.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 39,149★ · TypeScript · Hot  
  Teams-first multi-agent orchestration living entirely inside Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>
- **[coleam00/Archon](https://github.com/coleam00/Archon)** · 23,457★ · TypeScript · Hot  
  'Harness builder' — make AI coding deterministic and repeatable by generating the harness itself.  
  <sub>topics: ai, automation, bun, claude, cli, coding-assistant, developer-tools, typescript</sub>

### Fleet / parallel orchestration

_One agent is a tool; a fleet is a team. The harness problem becomes scheduling, isolation (worktrees, containers), review queues, and merge discipline._

- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 49,786★ · Go · Hot  
  Managed-agents platform: assign tasks to coding agents like teammates and supervise them.  
  <sub>topics: —</sub>
- **[BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban)** · 28,078★ · Rust · Declining  
  A kanban board as the harness — queue, run, and review many agent tasks in parallel.  
  <sub>topics: agent, ai-agents, kanban, management, task-manager</sub>
- **[gastownhall/gastown](https://github.com/gastownhall/gastown)** · 18,052★ · Go · Hot  
  Multi-agent workspace manager — the 'town' where a fleet of agents live and work.  
  <sub>topics: —</sub>
- **[AndyMik90/Aperant](https://github.com/AndyMik90/Aperant)** · 14,560★ · TypeScript · Declining  
  Autonomous multi-session AI coding — sessions as the unit of parallelism.  
  <sub>topics: —</sub>
- **[Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator)** · 12,004★ · Go · Hot  
  Plans tasks, spawns parallel coding agents in worktrees, merges autonomously.  
  <sub>topics: claude-code, codex-cli, orchestration, orchestrator, skills, agent-fleet, agent-swarm, git-worktrees</sub>
- **[automazeio/ccpm](https://github.com/automazeio/ccpm)** · 8,372★ · Shell · Declining  
  GitHub Issues + git worktrees as the coordination fabric for parallel agents.  
  <sub>topics: ai-agents, ai-coding, claude, claude-code, project-management, vibe-coding</sub>
- **[dagger/container-use](https://github.com/dagger/container-use)** · 4,042★ · Go · Mature  
  Containerized dev environments so multiple agents work safely and independently.  
  <sub>topics: —</sub>

### Determinism & spec-driven

_The counter-culture: agents drift, so pin them down. Specs, standards files, and plans persisted to disk make runs reproducible, auditable, and resumable after crashes._

- **[github/spec-kit](https://github.com/github/spec-kit)** · 136,618★ · Python · Hot  
  Spec-Driven Development toolkit — the spec, not the prompt, steers the agent.  
  <sub>topics: ai, copilot, development, engineering, prd, spec, spec-driven</sub>
- **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** · 26,876★ · Shell · Hot  
  Persistent file-based planning — crash-proof, resumable long-running agent tasks.  
  <sub>topics: claude, claude-code, claude-skills, manus, agent-skills, planning, autonomous-agents, codex</sub>
- **[agentsmd/agents.md](https://github.com/agentsmd/agents.md)** · 24,359★ · TypeScript · Declining  
  The open AGENTS.md standard — a portable contract telling any harness how to behave in a repo.  
  <sub>topics: —</sub>
- **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** · 11,202★ · TypeScript · Hot  
  Patterns and starters for *loop engineering* — designing the iteration, not just the prompt.  
  <sub>topics: agentic-ai, ai-agents, claude-code, codex, devops-automation, github-actions, grok, llm</sub>
- **[gsd-build/gsd-2](https://github.com/gsd-build/gsd-2)** · 7,773★ · TypeScript · Declining  
  Meta-prompting + context engineering + spec-driven system for dependable outcomes.  
  <sub>topics: context-engineering, meta-prompting, spec-driven-development</sub>

### Sandbox substrate

_Infrastructure-first: before you scale agents you need somewhere safe and fast to run them. MicroVMs, container runtimes, and hardened sandboxes are the harness's floor._

- **[daytonaio/daytona](https://github.com/daytonaio/daytona)** · 71,713★ · — · Mature  
  Secure, elastic infrastructure for running AI-generated code — the harness's execution floor.  
  <sub>topics: developer-tools, agentic-workflow, ai, ai-agents, ai-runtime, code-execution, code-interpreter, ai-sandboxes</sub>
- **[trycua/cua](https://github.com/trycua/cua)** · 22,618★ · HTML · Hot  
  Sandboxes, SDKs, and benchmarks for computer-use agents — full-desktop harnessing.  
  <sub>topics: apple, cua, lume, macos, virtualization, virtualization-framework, swift, ai-agent</sub>
- **[NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)** · 22,452★ · TypeScript · Hot  
  Run harnesses (Hermes, Deep Agents, OpenClaw) inside hardened NVIDIA sandboxes.  
  <sub>topics: ai-agents, nvidia, openclaw, openshell, sandboxing, typescript, hermes, deep-agents</sub>
- **[opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)** · 15,202★ · Python · Hot  
  Secure, fast, extensible sandbox runtime purpose-built for AI agents.  
  <sub>topics: ai, ai-infra, kubernetes, sandbox, ai-agent</sub>
- **[deeplethe/forkd](https://github.com/deeplethe/forkd)** · 2,843★ · Rust · Hot  
  fork() for agent microVMs — spawn 100 children in ~100ms; branch a live VM mid-run.  
  <sub>topics: ai-agents, copy-on-write, kvm, microvm, rust, sandbox, snapshot</sub>

### Autonomous long-horizon

_Maximum autonomy: agents that run for hours or days, planning and re-planning, sometimes improving their own scaffolding. The harness is a resident process, not a CLI invocation._

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 82,408★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and creates with sub-agents in sandboxes.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[agent0ai/agent-zero](https://github.com/agent0ai/agent-zero)** · 19,164★ · Python · Mature  
  General autonomous framework — the agent builds its own tools as it goes.  
  <sub>topics: agent, ai, assistant, autonomous, linux, zero</sub>
- **[hexo-ai/sia](https://github.com/hexo-ai/sia)** · 2,150★ · Python · Rising  
  Self-Improving AI — a harness whose loop optimizes the underlying system over time.  
  <sub>topics: —</sub>
- **[stakpak/agent](https://github.com/stakpak/agent)** · 1,783★ · Rust · Mature  
  An agent that lives on your machines 24/7 and keeps shipping — harness as a resident daemon.  
  <sub>topics: agent, devops, devtool, generative-ai, hacktoberfest, ai-agent, autonomous-agent, llm-agent</sub>
- **[aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch)** · 370★ · Shell · Declining  
  Watches your Claude usage windows and executes queued tasks autonomously overnight.  
  <sub>topics: —</sub>

## Graph analysis — how they relate

**Community clustering.** These 36 tools span **16 of the graph's 37 communities**.

- **Community 16** (8): `vercel/eve`, `affaan-m/ECC`, `code-yeongyu/oh-my-openagent`, `ruvnet/ruflo`, `Yeachan-Heo/oh-my-claudecode`, `automazeio/ccpm`, `Untrivial-ai/agent-orchestrator`, `aniketkarne/ClaudeNightsWatch`
- **Community 3** (5): `langchain-ai/deepagents`, `obra/superpowers`, `BloopAI/vibe-kanban`, `daytonaio/daytona`, `opensandbox-group/OpenSandbox`
- **Community 14** (4): `strands-agents/harness-sdk`, `SAIL-Research-Lab/cheetahclaws`, `OthmanAdi/planning-with-files`, `deeplethe/forkd`
- **Community 5** (3): `earendil-works/pi`, `1jehuang/jcode`, `trycua/cua`
- **Community 24** (3): `emcie-co/parlant`, `multica-ai/multica`, `gsd-build/gsd-2`
- **Community 2** (2): `pydantic/pydantic-ai-harness`, `NVIDIA/NemoClaw`
- **Community 29** (2): `coleam00/Archon`, `agent0ai/agent-zero`

**Centrality (PageRank in the full 2,159-repo graph)** — most 'hub-like' harnesses in your ecosystem:

- `langchain-ai/deepagents` — PageRank 0.0015
- `affaan-m/ECC` — PageRank 0.0015
- `1jehuang/jcode` — PageRank 0.0009
- `multica-ai/multica` — PageRank 0.0008
- `code-yeongyu/oh-my-openagent` — PageRank 0.0007
- `strands-agents/harness-sdk` — PageRank 0.0006
- `cobusgreyling/loop-engineering` — PageRank 0.0006
- `vercel/eve` — PageRank 0.0006
- `stakpak/agent` — PageRank 0.0005
- `coleam00/Archon` — PageRank 0.0005

**Direct links between harness projects** (top similarity edges where both endpoints are in this report):

- `bytedance/deer-flow` ⇄ `langchain-ai/deepagents` (w=0.386) — topics: ai, langchain, langgraph, python; authors: dependabot[bot]
- `cobusgreyling/loop-engineering` ⇄ `affaan-m/ECC` (w=0.376) — topics: ai-agents, claude-code, llm, mcp; authors: dependabot[bot]
- `bytedance/deer-flow` ⇄ `strands-agents/harness-sdk` (w=0.336) — topics: agentic, ai, ai-agents, llm; authors: BlueX888, dependabot[bot]
- `Yeachan-Heo/oh-my-claudecode` ⇄ `automazeio/ccpm` (w=0.333) — topics: ai-agents, claude, claude-code, vibe-coding
- `cobusgreyling/loop-engineering` ⇄ `Yeachan-Heo/oh-my-claudecode` (w=0.311) — topics: ai-agents, claude-code, automation, claude; authors: Iams4kura
- `affaan-m/ECC` ⇄ `automazeio/ccpm` (w=0.273) — topics: ai-agents, claude, claude-code
- `github/spec-kit` ⇄ `langchain-ai/deepagents` (w=0.227) — topics: ai; authors: github-actions[bot], dependabot[bot]
- `strands-agents/harness-sdk` ⇄ `ruvnet/ruflo` (w=0.212) — topics: agentic-ai, agents, autonomous-agents, multi-agent-systems
- `stakpak/agent` ⇄ `BloopAI/vibe-kanban` (w=0.121) — topics: agent
- `multica-ai/multica` ⇄ `affaan-m/ECC` (w=0.057) — authors: Dante-dan

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Harnesses are a young, fast-moving category — expect churn; check lifecycle before betting on one.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| github/spec-kit | 99 | Hot | very active | 5 | 21% | 220 |
| Untrivial-ai/agent-orchestrator | 98 | Hot | very active | 7 | 11% | 192 |
| opensandbox-group/OpenSandbox | 93 | Hot | very active | 4 | 20% | 177 |
| strands-agents/harness-sdk | 92 | Hot | very active | 4 | 16% | 94 |
| earendil-works/pi | 90 | Hot | very active | 3 | 27% | 259 |
| vercel/eve | 90 | Hot | very active | 4 | 20% | 187 |
| langchain-ai/deepagents | 89 | Hot | very active | 3 | 23% | 280 |
| pydantic/pydantic-ai-harness | 84 | Hot | very active | 3 | 27% | 37 |
| bytedance/deer-flow | 84 | Hot | very active | 8 | 12% | 1 |
| multica-ai/multica | 82 | Hot | very active | 2 | 36% | 155 |
| daytonaio/daytona | 82 | Mature | active | 4 | 16% | 205 |
| Yeachan-Heo/oh-my-claudecode | 80 | Hot | very active | 1 | 62% | 251 |
| affaan-m/ECC | 79 | Hot | very active | 1 | 58% | 17 |
| OthmanAdi/planning-with-files | 79 | Hot | very active | 1 | 90% | 100 |
| deeplethe/forkd | 79 | Hot | very active | 1 | 66% | 24 |
| agent0ai/agent-zero | 79 | Mature | very active | 1 | 81% | 74 |
| obra/superpowers | 78 | Hot | very active | 1 | 82% | 12 |
| code-yeongyu/oh-my-openagent | 78 | Rising | very active | 1 | 100% | 281 |
| coleam00/Archon | 78 | Hot | very active | 1 | 98% | 22 |
| gastownhall/gastown | 77 | Hot | very active | 1 | 53% | 14 |
| 1jehuang/jcode | 76 | Hot | very active | 1 | 60% | 176 |
| ruvnet/ruflo | 76 | Hot | very active | 1 | 90% | 1645 |
| trycua/cua | 75 | Hot | very active | 1 | 52% | 679 |
| SAIL-Research-Lab/cheetahclaws | 74 | Hot | very active | 1 | 77% | 41 |
| NVIDIA/NemoClaw | 74 | Hot | very active | 3 | 28% | 0 |
| cobusgreyling/loop-engineering | 68 | Hot | very active | 1 | 54% | 2 |
| emcie-co/parlant | 60 | Mature | slowing | 1 | 71% | 33 |
| stakpak/agent | 56 | Mature | slowing | 1 | 67% | 315 |
| hexo-ai/sia | 51 | Rising | active | 2 | 29% | 0 |
| BloopAI/vibe-kanban | 50 | Declining | active | 0 | 0% | 284 |
| AndyMik90/Aperant | 47 | Declining | slowing | 0 | 0% | 37 |
| dagger/container-use | 46 | Mature | active | 1 | 86% | 14 |
| gsd-build/gsd-2 | 45 | Declining | slowing | 0 | 0% | 116 |
| aniketkarne/ClaudeNightsWatch | 43 | Declining | active | 1 | 100% | 0 |
| agentsmd/agents.md | 40 | Declining | active | 1 | 67% | 0 |
| automazeio/ccpm | 25 | Declining | slowing | 0 | 0% | 0 |

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

- **langchain-ai/langgraph** (41,611★) — agent *framework* (graphs, not harnesses) — see the agent-orchestration report
- **crewAIInc/crewAI** (58,514★) — role-playing agent framework — agent-orchestration report
- **microsoft/autogen** (60,979★) — multi-agent conversation framework — agent-orchestration report
- **eigent-ai/eigent** (15,273★) — cowork desktop product — agent-orchestration report
- **getpaseo/paseo** (17,227★) — desktop/mobile agent orchestrator — agent-orchestration report
- **wshobson/agents** (39,640★) — multi-harness plugin *marketplace* — content for harnesses, not a harness
- **EleutherAI/lm-evaluation-harness** (13,974★) — 'harness' for *model benchmarks*, not agent runtimes — see the LLM-evaluation report
- **anthropics/claude-code** (144,971★) — the coding agent itself — the thing meta-harnesses wrap

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (harness / autonomous / swarm / multi-agent / sandbox / worktree / spec-driven / long-horizon / loop…) + manual curation by *approach*. General agent frameworks and orchestration platforms live in the agent-orchestration report; Claude-Code configuration setups in the claude-code-setups report. A few boundary projects (`deer-flow`, `ruflo`, `oh-my-*`) appear in both, viewed through different lenses.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 36 · Snapshot: 2026-09-14T11:08:08.535Z</sub>
