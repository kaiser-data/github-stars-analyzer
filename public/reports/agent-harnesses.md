# Agent Harnesses — Six Approaches to Running Autonomous Agents

> Derived from **kaiser-data**'s 2,304 starred repos (snapshot `2026-10-05T13:01:39.533Z`), cross-referenced with the repo-similarity graph (2,304 nodes / 7,632 edges, 40 communities).
>
> Generated 2026-10-05 by `scripts/reports/agent_harnesses.py` (regenerate any time — no API cost).

![Top tools by stars](assets/agent-harnesses-top-tools.svg)

![Tools per category](assets/agent-harnesses-categories.svg)


## Executive summary

- A **harness** is everything around the model: the loop, tools, state, guardrails, and execution environment. **33 harness projects** in your stars (**1,478,309★** combined) cluster into **six distinct approaches** — they disagree about *where the harness lives* and *what the hard problem is*:
  - **Harness-as-SDK** (8): `pi`, `deepagents`, `jcode`, `parlant`, `harness-sdk`, `eve`, `pydantic-ai-harness`, `cheetahclaws`
  - **Meta-harness over coding agents** (6): `superpowers`, `ECC`, `ruflo`, `oh-my-openagent`, `oh-my-claudecode`, `Archon`
  - **Fleet / parallel orchestration** (6): `multica`, `vibe-kanban`, `gastown`, `Aperant`, `ccpm`, `container-use`
  - **Determinism & spec-driven** (4): `spec-kit`, `planning-with-files`, `agents.md`, `loop-engineering`
  - **Sandbox substrate** (4): `cua`, `NemoClaw`, `OpenSandbox`, `forkd`
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
| [obra/superpowers](https://github.com/obra/superpowers) | Meta-harness over coding agents | Shell | MIT | 295,458 (▲4,081) | Hot | 73 | very active | 8d ago | 12mo | 5 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Meta-harness over coding agents | JavaScript | MIT | 273,296 (▲6,138) | Hot | 79 | very active | 0d ago | 8mo | 5 |
| [github/spec-kit](https://github.com/github/spec-kit) | Determinism & spec-driven | Python | MIT | 140,186 (▲1,361) | Hot | 84 | very active | 2d ago | 1.1y | 27 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Harness-as-SDK | TypeScript | MIT | 112,592 (▲3,333) | Hot | 80 | very active | 0d ago | 1.2y | 14 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | Autonomous long-horizon | Python | MIT | 83,401 (▲439) | Hot | 87 | very active | 0d ago | 1.4y | 37 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Meta-harness over coding agents | TypeScript | MIT | 73,892 (▲654) | Mature | 76 | very active | 0d ago | 1.3y | 1 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Meta-harness over coding agents | TypeScript | NOASSERTION | 69,807 (▲412) | Hot | 78 | very active | 0d ago | 10mo | 6 |
| [multica-ai/multica](https://github.com/multica-ai/multica) | Fleet / parallel orchestration | Go | NOASSERTION | 51,978 (▲655) | Hot | 81 | very active | 1d ago | 8mo | 22 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Meta-harness over coding agents | TypeScript | MIT | 39,585 (▲237) | Hot | 85 | very active | 0d ago | 8mo | 7 |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Harness-as-SDK | Python | MIT | 29,948 (▲188) | Hot | 84 | very active | 0d ago | 1.2y | 12 |
| [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Fleet / parallel orchestration | Rust | Apache-2.0 | 28,261 (▲72) | Mature | 62 | active | 16d ago | 1.3y | 4 |
| [trycua/cua](https://github.com/trycua/cua) | Sandbox substrate | Rust | MIT | 28,106 (▲1,796) | Hot | 81 | very active | 0d ago | 1.7y | 9 |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | Determinism & spec-driven | Shell | MIT | 27,287 (▲175) | Hot | 79 | very active | 4d ago | 9mo | 6 |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | Determinism & spec-driven | TypeScript | MIT | 24,772 (▲164) | Declining | 38 | active | 25d ago | 1.1y | 2 |
| [coleam00/Archon](https://github.com/coleam00/Archon) | Meta-harness over coding agents | TypeScript | MIT | 23,620 (▲69) | Hot | 79 | very active | 0d ago | 1.7y | 5 |
| [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | Sandbox substrate | TypeScript | Apache-2.0 | 22,660 (▲122) | Hot | 71 | very active | 0d ago | 6mo | 18 |
| [1jehuang/jcode](https://github.com/1jehuang/jcode) | Harness-as-SDK | Rust | MIT | 20,302 (▲184) | Hot | 76 | very active | 0d ago | 9mo | 11 |
| [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | Autonomous long-horizon | Python | NOASSERTION | 19,373 (▲113) | Mature | 79 | very active | 3d ago | 2.3y | 3 |
| [emcie-co/parlant](https://github.com/emcie-co/parlant) | Harness-as-SDK | Python | Apache-2.0 | 18,296 (▲6) | Mature | 54 | slowing | 2mo ago | 2.6y | 1 |
| [gastownhall/gastown](https://github.com/gastownhall/gastown) | Fleet / parallel orchestration | Go | MIT | 18,253 (▲68) | Hot | 75 | very active | 6d ago | 9mo | 9 |
| [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | Sandbox substrate | Python | Apache-2.0 | 15,672 (▲164) | Hot | 83 | very active | 4d ago | 9mo | 12 |
| [AndyMik90/Aperant](https://github.com/AndyMik90/Aperant) | Fleet / parallel orchestration | TypeScript | AGPL-3.0 | 14,578 (▲8) | Declining | 45 | slowing | 3mo ago | 10mo | 0 |
| [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | Determinism & spec-driven | TypeScript | MIT | 11,421 (▲112) | Hot | 68 | very active | 0d ago | 3mo | 12 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | Harness-as-SDK | Python | Apache-2.0 | 8,671 (▲300) | Hot | 92 | very active | 0d ago | 1.4y | 33 |
| [automazeio/ccpm](https://github.com/automazeio/ccpm) | Fleet / parallel orchestration | Shell | MIT | 8,398 (▲14) | Declining | 23 | stale | 6mo ago | 1.1y | 0 |
| [vercel/eve](https://github.com/vercel/eve) | Harness-as-SDK | TypeScript | Apache-2.0 | 5,457 (▲97) | Hot | 85 | very active | 0d ago | 3mo | 17 |
| [dagger/container-use](https://github.com/dagger/container-use) | Fleet / parallel orchestration | Go | Apache-2.0 | 4,055 (▲10) | Mature | 45 | active | 14d ago | 1.4y | 2 |
| [deeplethe/forkd](https://github.com/deeplethe/forkd) | Sandbox substrate | Rust | Apache-2.0 | 2,919 (▲16) | Hot | 77 | very active | 21d ago | 4mo | 4 |
| [hexo-ai/sia](https://github.com/hexo-ai/sia) | Autonomous long-horizon | Python | MIT | 2,158 (▲1) | Mature | 46 | active | 1mo ago | 6mo | 5 |
| [stakpak/agent](https://github.com/stakpak/agent) | Autonomous long-horizon | Rust | Apache-2.0 | 1,812 (▲16) | Declining | 43 | slowing | 3mo ago | 1.8y | 0 |
| [pydantic/pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness) | Harness-as-SDK | Python | MIT | 943 (▲17) | Hot | 79 | very active | 3d ago | 6mo | 6 |
| [SAIL-Research-Lab/cheetahclaws](https://github.com/SAIL-Research-Lab/cheetahclaws) | Harness-as-SDK | Python | Apache-2.0 | 783 (▲3) | Hot | 70 | very active | 15d ago | 6mo | 7 |
| [aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch) | Autonomous long-horizon | Shell | MIT | 369 (▼1) | Declining | 41 | active | 25d ago | 1.2y | 1 |

## By approach

### Harness-as-SDK

_The loop as a library: you import the harness, register tools, and own control flow. Maximum flexibility, maximum responsibility — you maintain planning, retries, memory, and safety yourself._

- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 112,592★ · TypeScript · Hot  
  Unified LLM API + agent loop + TUI + coding-agent CLI in one toolkit — the loop as a library.  
  <sub>topics: —</sub>
- **[langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)** · 29,948★ · Python · Hot  
  The 'batteries-included agent harness' — planning, sub-agents, filesystem, from the LangChain team.  
  <sub>topics: deepagents, langchain, langgraph, ai, python, typescript, harness, harness-engineering</sub>
- **[1jehuang/jcode](https://github.com/1jehuang/jcode)** · 20,302★ · Rust · Hot  
  Rust-built coding-agent harness — CLI agent loop with MCP support and multi-model wiring.  
  <sub>topics: ai, claude, cli, coding-agent, llm, mcp, openai, rust</sub>
- **[emcie-co/parlant](https://github.com/emcie-co/parlant)** · 18,296★ · Python · Mature  
  Interaction *control* harness — behavioral guidelines enforced at runtime for customer-facing agents.  
  <sub>topics: ai-agents, genai, llm, customer-service, customer-success, gemini, llama3, openai</sub>
- **[strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)** · 8,671★ · Python · Hot  
  AWS's open SDK to build an agent harness and control it end-to-end in production.  
  <sub>topics: agentic, agentic-ai, agents, ai, autonomous-agents, llm, multi-agent-systems, python</sub>
- **[vercel/eve](https://github.com/vercel/eve)** · 5,457★ · TypeScript · Hot  
  Vercel's framework for building agents — harness + sandbox as one integrated runtime.  
  <sub>topics: agent, framework, harness, javascript, markdown, typescript, vercel, sandbox</sub>
- **[pydantic/pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness)** · 943★ · Python · Hot  
  'Batteries for your Pydantic AI agent' — the harness as a thin add-on to a typed agent framework.  
  <sub>topics: —</sub>
- **[SAIL-Research-Lab/cheetahclaws](https://github.com/SAIL-Research-Lab/cheetahclaws)** · 783★ · Python · Hot  
  Fast, easy agent-harness infrastructure aimed at long-horizon, multi-model runs.  
  <sub>topics: agentic-ai, claude, claude-code, memory, python, skills, openclaw</sub>

### Meta-harness over coding agents

_These projects treat Claude Code / Codex as the engine and build the transmission: skills, personas, memory, token discipline, and multi-agent coordination injected via configs, hooks, and subagents._

- **[obra/superpowers](https://github.com/obra/superpowers)** · 295,458★ · Shell · Hot  
  Skills framework + development methodology layered onto the agent you already run.  
  <sub>topics: ai, brainstorming, coding, obra, sdlc, skills, superpowers, subagent-driven-development</sub>
- **[affaan-m/ECC](https://github.com/affaan-m/ECC)** · 273,296★ · JavaScript · Hot  
  Harness performance optimization: skills, instincts, memory, security, hooks on top of Claude Code.  
  <sub>topics: ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity</sub>
- **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** · 73,892★ · TypeScript · Mature  
  The leading agent *meta*-harness — swarms, coordination, and autonomy on top of existing agents.  
  <sub>topics: swarm, agentic-ai, agentic-framework, agentic-workflow, autonomous-agents, codex, mcp-server, multi-agent</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 69,807★ · TypeScript · Hot  
  'The one and only agent harness for complex coding' — tokenmaxxer harness wrapping coding agents.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** · 39,585★ · TypeScript · Hot  
  Teams-first multi-agent orchestration living entirely inside Claude Code.  
  <sub>topics: agentic-coding, ai-agents, claude, claude-code, oh-my-opencode, opencode, vibe-coding, automation</sub>
- **[coleam00/Archon](https://github.com/coleam00/Archon)** · 23,620★ · TypeScript · Hot  
  'Harness builder' — make AI coding deterministic and repeatable by generating the harness itself.  
  <sub>topics: ai, automation, bun, claude, cli, coding-assistant, developer-tools, typescript</sub>

### Fleet / parallel orchestration

_One agent is a tool; a fleet is a team. The harness problem becomes scheduling, isolation (worktrees, containers), review queues, and merge discipline._

- **[multica-ai/multica](https://github.com/multica-ai/multica)** · 51,978★ · Go · Hot  
  Managed-agents platform: assign tasks to coding agents like teammates and supervise them.  
  <sub>topics: —</sub>
- **[BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban)** · 28,261★ · Rust · Mature  
  A kanban board as the harness — queue, run, and review many agent tasks in parallel.  
  <sub>topics: agent, ai-agents, kanban, management, task-manager</sub>
- **[gastownhall/gastown](https://github.com/gastownhall/gastown)** · 18,253★ · Go · Hot  
  Multi-agent workspace manager — the 'town' where a fleet of agents live and work.  
  <sub>topics: —</sub>
- **[AndyMik90/Aperant](https://github.com/AndyMik90/Aperant)** · 14,578★ · TypeScript · Declining  
  Autonomous multi-session AI coding — sessions as the unit of parallelism.  
  <sub>topics: —</sub>
- **[automazeio/ccpm](https://github.com/automazeio/ccpm)** · 8,398★ · Shell · Declining  
  GitHub Issues + git worktrees as the coordination fabric for parallel agents.  
  <sub>topics: ai-agents, ai-coding, claude, claude-code, project-management, vibe-coding</sub>
- **[dagger/container-use](https://github.com/dagger/container-use)** · 4,055★ · Go · Mature  
  Containerized dev environments so multiple agents work safely and independently.  
  <sub>topics: —</sub>

### Determinism & spec-driven

_The counter-culture: agents drift, so pin them down. Specs, standards files, and plans persisted to disk make runs reproducible, auditable, and resumable after crashes._

- **[github/spec-kit](https://github.com/github/spec-kit)** · 140,186★ · Python · Hot  
  Spec-Driven Development toolkit — the spec, not the prompt, steers the agent.  
  <sub>topics: ai, copilot, development, engineering, prd, spec, spec-driven</sub>
- **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** · 27,287★ · Shell · Hot  
  Persistent file-based planning — crash-proof, resumable long-running agent tasks.  
  <sub>topics: claude, claude-code, claude-skills, manus, agent-skills, planning, autonomous-agents, codex</sub>
- **[agentsmd/agents.md](https://github.com/agentsmd/agents.md)** · 24,772★ · TypeScript · Declining  
  The open AGENTS.md standard — a portable contract telling any harness how to behave in a repo.  
  <sub>topics: —</sub>
- **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** · 11,421★ · TypeScript · Hot  
  Patterns and starters for *loop engineering* — designing the iteration, not just the prompt.  
  <sub>topics: agentic-ai, ai-agents, claude-code, codex, devops-automation, github-actions, grok, llm</sub>

### Sandbox substrate

_Infrastructure-first: before you scale agents you need somewhere safe and fast to run them. MicroVMs, container runtimes, and hardened sandboxes are the harness's floor._

- **[trycua/cua](https://github.com/trycua/cua)** · 28,106★ · Rust · Hot  
  Sandboxes, SDKs, and benchmarks for computer-use agents — full-desktop harnessing.  
  <sub>topics: apple, cua, lume, macos, virtualization, virtualization-framework, swift, ai-agent</sub>
- **[NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)** · 22,660★ · TypeScript · Hot  
  Run harnesses (Hermes, Deep Agents, OpenClaw) inside hardened NVIDIA sandboxes.  
  <sub>topics: ai-agents, nvidia, openclaw, openshell, sandboxing, typescript, hermes, deep-agents</sub>
- **[opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)** · 15,672★ · Python · Hot  
  Secure, fast, extensible sandbox runtime purpose-built for AI agents.  
  <sub>topics: ai, ai-infra, kubernetes, sandbox, ai-agent</sub>
- **[deeplethe/forkd](https://github.com/deeplethe/forkd)** · 2,919★ · Rust · Hot  
  fork() for agent microVMs — spawn 100 children in ~100ms; branch a live VM mid-run.  
  <sub>topics: ai-agents, copy-on-write, kvm, microvm, rust, sandbox, snapshot</sub>

### Autonomous long-horizon

_Maximum autonomy: agents that run for hours or days, planning and re-planning, sometimes improving their own scaffolding. The harness is a resident process, not a CLI invocation._

- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** · 83,401★ · Python · Hot  
  Long-horizon SuperAgent harness that researches, codes, and creates with sub-agents in sandboxes.  
  <sub>topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, langchain</sub>
- **[agent0ai/agent-zero](https://github.com/agent0ai/agent-zero)** · 19,373★ · Python · Mature  
  General autonomous framework — the agent builds its own tools as it goes.  
  <sub>topics: agent, ai, assistant, autonomous, linux, zero</sub>
- **[hexo-ai/sia](https://github.com/hexo-ai/sia)** · 2,158★ · Python · Mature  
  Self-Improving AI — a harness whose loop optimizes the underlying system over time.  
  <sub>topics: —</sub>
- **[stakpak/agent](https://github.com/stakpak/agent)** · 1,812★ · Rust · Declining  
  An agent that lives on your machines 24/7 and keeps shipping — harness as a resident daemon.  
  <sub>topics: agent, devops, devtool, generative-ai, hacktoberfest, ai-agent, autonomous-agent, llm-agent</sub>
- **[aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch)** · 369★ · Shell · Declining  
  Watches your Claude usage windows and executes queued tasks autonomously overnight.  
  <sub>topics: —</sub>

## Graph analysis — how they relate

**Community clustering.** These 33 tools span **16 of the graph's 40 communities**.

- **Community 0** (8): `langchain-ai/deepagents`, `strands-agents/harness-sdk`, `affaan-m/ECC`, `BloopAI/vibe-kanban`, `gastownhall/gastown`, `dagger/container-use`, `opensandbox-group/OpenSandbox`, `deeplethe/forkd`
- **Community 5** (4): `code-yeongyu/oh-my-openagent`, `ruvnet/ruflo`, `OthmanAdi/planning-with-files`, `aniketkarne/ClaudeNightsWatch`
- **Community 4** (3): `obra/superpowers`, `AndyMik90/Aperant`, `agentsmd/agents.md`
- **Community 11** (2): `pydantic/pydantic-ai-harness`, `NVIDIA/NemoClaw`
- **Community 31** (2): `1jehuang/jcode`, `coleam00/Archon`
- **Community 20** (2): `Yeachan-Heo/oh-my-claudecode`, `automazeio/ccpm`
- **Community 6** (2): `multica-ai/multica`, `cobusgreyling/loop-engineering`
- **Community 9** (2): `trycua/cua`, `stakpak/agent`

**Centrality (PageRank in the full 2,304-repo graph)** — most 'hub-like' harnesses in your ecosystem:

- `langchain-ai/deepagents` — PageRank 0.0012
- `affaan-m/ECC` — PageRank 0.0011
- `code-yeongyu/oh-my-openagent` — PageRank 0.0008
- `multica-ai/multica` — PageRank 0.0007
- `1jehuang/jcode` — PageRank 0.0007
- `NVIDIA/NemoClaw` — PageRank 0.0005
- `cobusgreyling/loop-engineering` — PageRank 0.0005
- `strands-agents/harness-sdk` — PageRank 0.0005
- `vercel/eve` — PageRank 0.0005
- `coleam00/Archon` — PageRank 0.0005

**Direct links between harness projects** (top similarity edges where both endpoints are in this report):

- `bytedance/deer-flow` ⇄ `langchain-ai/deepagents` (w=0.350) — topics: ai, langchain, langgraph, python
- `Yeachan-Heo/oh-my-claudecode` ⇄ `automazeio/ccpm` (w=0.333) — topics: ai-agents, claude, claude-code, vibe-coding
- `affaan-m/ECC` ⇄ `automazeio/ccpm` (w=0.273) — topics: ai-agents, claude, claude-code
- `cobusgreyling/loop-engineering` ⇄ `Yeachan-Heo/oh-my-claudecode` (w=0.224) — topics: ai-agents, claude-code, automation, claude
- `strands-agents/harness-sdk` ⇄ `ruvnet/ruflo` (w=0.212) — topics: agentic-ai, agents, autonomous-agents, multi-agent-systems
- `stakpak/agent` ⇄ `trycua/cua` (w=0.170) — topics: agent, hacktoberfest, ai-agent

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Harnesses are a young, fast-moving category — expect churn; check lifecycle before betting on one.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| strands-agents/harness-sdk | 92 | Hot | very active | 4 | 25% | 111 |
| bytedance/deer-flow | 87 | Hot | very active | 8 | 14% | 2 |
| vercel/eve | 85 | Hot | very active | 3 | 31% | 237 |
| Yeachan-Heo/oh-my-claudecode | 85 | Hot | very active | 2 | 48% | 254 |
| langchain-ai/deepagents | 84 | Hot | very active | 2 | 33% | 303 |
| github/spec-kit | 84 | Hot | very active | 2 | 28% | 228 |
| opensandbox-group/OpenSandbox | 83 | Hot | very active | 2 | 47% | 179 |
| multica-ai/multica | 81 | Hot | very active | 2 | 30% | 162 |
| trycua/cua | 81 | Hot | very active | 2 | 35% | 757 |
| earendil-works/pi | 80 | Hot | very active | 1 | 51% | 270 |
| pydantic/pydantic-ai-harness | 79 | Hot | very active | 1 | 54% | 42 |
| affaan-m/ECC | 79 | Hot | very active | 1 | 93% | 19 |
| coleam00/Archon | 79 | Hot | very active | 1 | 95% | 24 |
| OthmanAdi/planning-with-files | 79 | Hot | very active | 1 | 68% | 115 |
| agent0ai/agent-zero | 79 | Mature | very active | 1 | 78% | 75 |
| code-yeongyu/oh-my-openagent | 78 | Hot | very active | 1 | 82% | 329 |
| deeplethe/forkd | 77 | Hot | very active | 1 | 66% | 24 |
| 1jehuang/jcode | 76 | Hot | very active | 1 | 68% | 187 |
| ruvnet/ruflo | 76 | Mature | very active | 1 | 100% | 1664 |
| gastownhall/gastown | 75 | Hot | very active | 1 | 53% | 14 |
| obra/superpowers | 73 | Hot | very active | 1 | 91% | 14 |
| NVIDIA/NemoClaw | 71 | Hot | very active | 2 | 30% | 1 |
| SAIL-Research-Lab/cheetahclaws | 70 | Hot | very active | 1 | 66% | 42 |
| cobusgreyling/loop-engineering | 68 | Hot | very active | 1 | 69% | 2 |
| BloopAI/vibe-kanban | 62 | Mature | active | 1 | 50% | 284 |
| emcie-co/parlant | 54 | Mature | slowing | 1 | 100% | 33 |
| hexo-ai/sia | 46 | Mature | active | 2 | 43% | 0 |
| AndyMik90/Aperant | 45 | Declining | slowing | 0 | 0% | 37 |
| dagger/container-use | 45 | Mature | active | 1 | 86% | 14 |
| stakpak/agent | 43 | Declining | slowing | 0 | 0% | 315 |
| aniketkarne/ClaudeNightsWatch | 41 | Declining | active | 1 | 100% | 0 |
| agentsmd/agents.md | 38 | Declining | active | 1 | 67% | 0 |
| automazeio/ccpm | 23 | Declining | stale | 0 | 0% | 0 |

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

- **langchain-ai/langgraph** (42,730★) — agent *framework* (graphs, not harnesses) — see the agent-orchestration report
- **crewAIInc/crewAI** (59,356★) — role-playing agent framework — agent-orchestration report
- **microsoft/autogen** (61,256★) — multi-agent conversation framework — agent-orchestration report
- **eigent-ai/eigent** (15,453★) — cowork desktop product — agent-orchestration report
- **getpaseo/paseo** (19,571★) — desktop/mobile agent orchestrator — agent-orchestration report
- **wshobson/agents** (40,208★) — multi-harness plugin *marketplace* — content for harnesses, not a harness
- **EleutherAI/lm-evaluation-harness** (14,130★) — 'harness' for *model benchmarks*, not agent runtimes — see the LLM-evaluation report
- **anthropics/claude-code** (149,465★) — the coding agent itself — the thing meta-harnesses wrap

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: keyword scan (harness / autonomous / swarm / multi-agent / sandbox / worktree / spec-driven / long-horizon / loop…) + manual curation by *approach*. General agent frameworks and orchestration platforms live in the agent-orchestration report; Claude-Code configuration setups in the claude-code-setups report. A few boundary projects (`deer-flow`, `ruflo`, `oh-my-*`) appear in both, viewed through different lenses.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 33 · Snapshot: 2026-10-05T13:01:39.533Z</sub>
