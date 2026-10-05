# Terminal AI Coding Agents (TUIs) — Best Picks, Advantages & Disadvantages

> Derived from **kaiser-data**'s 2,304 starred repos (snapshot `2026-10-05T13:01:39.533Z`), cross-referenced with the repo-similarity graph (2,304 nodes / 7,632 edges, 40 communities). Pros/cons and task rankings are additionally backed by external evidence (Terminal-Bench 2.1, 2026 head-to-head comparisons) — see Methodology.
>
> Generated 2026-10-05 by `scripts/reports/ai_coding_tuis.py` (regenerate any time — no API cost).

![Top tools by stars](assets/ai-coding-tuis-top-tools.svg)

![Tools per category](assets/ai-coding-tuis-categories.svg)


## Executive summary

- **31 terminal-AI-coding tools** in your stars (**1,353,785★** combined), split into the agents themselves and the terminal ecosystem around them:
  - **Terminal coding agent** (13): `opencode`, `claude-code`, `codex`, `pi`, `gemini-cli`, `oh-my-openagent`, `goose`, `aider`, `crush`, `qwen-code`, `freebuff`, `copilot-cli`, `tig`
  - **Session / token ops** (7): `rtk`, `context-mode`, `codeburn`, `ctx`, `claude-auto-resume`, `ClaudeNightsWatch`, `cli`
  - **Safety / isolation** (4): `container-use`, `tirith`, `cc-safety-net`, `agentshield`
  - **Multi-CLI glue** (5): `cc-switch`, `free-claude-code`, `zcf`, `langchain-code`, `terminal-jarvis`
  - **TUI building blocks** (2): `bubbletea`, `bubbles`
- **Short answer to 'which TUI is best':** `claude-code` for reasoning depth and the richest extension ecosystem, `codex` for the highest benchmark ceiling, `opencode` if you want open source and model freedom. `aider` remains the best *pair programmer* (as opposed to autonomous agent); `goose` the best MCP-native generalist; `crush` the best-looking.
- **The harness matters more than the model**: the same GPT-5.5 scores 83.4% on Terminal-Bench 2.1 inside Codex CLI but 76.4% inside a generic harness — a 7-point gap that is pure agent-loop engineering.
- **Platform risk is real**: Gemini CLI was deprecated for a closed-source replacement in June 2026 with the free tier cut ~50×, and qwen-code's OAuth free tier ended in April — open-source-ness and provider neutrality (`opencode`, `goose`) are hedges, not ideology.

## The terminal-agent stack at a glance

| Layer | What it does | Tools in your stars |
|---|---|---|
| **The agent (TUI)** | Plan, edit, run, iterate in your terminal | `claude-code`, `opencode`, `gemini-cli`, `codex`, `goose`, `aider`, `crush`, `qwen-code`, `copilot-cli`, `pi`, `oh-my-openagent`, `freebuff` |
| **Token / session ops** | Cut cost, track spend, recall history | `rtk`, `context-mode`, `codeburn`, `ctx`, `opaline`, `claude-auto-resume`, `ClaudeNightsWatch` |
| **Safety** | Guard the shell the agent drives | `tirith`, `cc-safety-net`, `container-use`, `agentshield` |
| **Glue / launchers** | Switch, combine, and provision the CLIs | `cc-switch`, `free-claude-code`, `zcf`, `terminal-jarvis`, `langchain-code` |
| **Build-your-own** | Frameworks the TUIs are made of | `bubbletea`, `bubbles`, `pi` |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | Terminal coding agent | TypeScript | MIT | 211,816 (▲1,876) | Hot | 88 | very active | 0d ago | 1.4y | 16 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Terminal coding agent | TypeScript | — | 149,465 (▲1,448) | Hot | 79 | very active | 0d ago | 1.6y | 7 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Multi-CLI glue | Rust | MIT | 140,188 (▲3,512) | Hot | 76 | very active | 0d ago | 1.2y | 5 |
| [openai/codex](https://github.com/openai/codex) | Terminal coding agent | Rust | Apache-2.0 | 127,900 (▲1,513) | Hot | 84 | very active | 0d ago | 1.5y | 30 |
| [earendil-works/pi](https://github.com/earendil-works/pi) | Terminal coding agent | TypeScript | MIT | 112,592 (▲3,333) | Hot | 80 | very active | 0d ago | 1.2y | 14 |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Terminal coding agent | TypeScript | Apache-2.0 | 107,232 (▲73) | Hot | 95 | very active | 0d ago | 1.5y | 14 |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Session / token ops | Rust | Apache-2.0 | 82,410 (▲723) | Hot | 75 | very active | 0d ago | 8mo | 12 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | Terminal coding agent | TypeScript | NOASSERTION | 69,807 (▲412) | Hot | 78 | very active | 0d ago | 10mo | 6 |
| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Multi-CLI glue | Python | NOASSERTION | 56,692 (▲783) | Hot | 77 | very active | 0d ago | 8mo | 8 |
| [aaif-goose/goose](https://github.com/aaif-goose/goose) | Terminal coding agent | Rust | Apache-2.0 | 54,950 (▲316) | Mature | 99 | very active | 0d ago | 2.1y | 42 |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | Terminal coding agent | Python | Apache-2.0 | 49,374 (▲196) | Mature | 26 | slowing | 4mo ago | 3.4y | 0 |
| [charmbracelet/bubbletea](https://github.com/charmbracelet/bubbletea) | TUI building blocks | Go | MIT | 45,279 (▲163) | Classic | 88 | active | 3d ago | 6.7y | 15 |
| [charmbracelet/crush](https://github.com/charmbracelet/crush) | Terminal coding agent | Go | NOASSERTION | 28,494 (▲204) | Hot | 81 | very active | 0d ago | 1.4y | 13 |
| [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | Terminal coding agent | TypeScript | Apache-2.0 | 28,311 (▲186) | Hot | 83 | very active | 0d ago | 1.3y | 20 |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | Session / token ops | TypeScript | NOASSERTION | 25,441 (▲1,390) | Rising | 77 | very active | 0d ago | 7mo | 1 |
| [CodebuffAI/freebuff](https://github.com/CodebuffAI/freebuff) | Terminal coding agent | TypeScript | Apache-2.0 | 13,200 (▲500) | Mature | 77 | very active | 0d ago | 2.2y | 1 |
| [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | Session / token ops | TypeScript | MIT | 11,341 (▲113) | Hot | 84 | very active | 0d ago | 5mo | 14 |
| [github/copilot-cli](https://github.com/github/copilot-cli) | Terminal coding agent | Shell | NOASSERTION | 11,237 (▲28) | Classic | 69 | very active | 1d ago | 3.7y | 7 |
| [charmbracelet/bubbles](https://github.com/charmbracelet/bubbles) | TUI building blocks | Go | MIT | 8,969 (▲27) | Classic | 70 | active | 2d ago | 6.7y | 7 |
| [UfoMiao/zcf](https://github.com/UfoMiao/zcf) | Multi-CLI glue | TypeScript | MIT | 6,081 (▲1) | Hot | 68 | active | 1mo ago | 1.2y | 4 |
| [dagger/container-use](https://github.com/dagger/container-use) | Safety / isolation | Go | Apache-2.0 | 4,055 (▲10) | Mature | 45 | active | 14d ago | 1.4y | 2 |
| [sheeki03/tirith](https://github.com/sheeki03/tirith) | Safety / isolation | Rust | AGPL-3.0 | 2,751 (▲14) | Rising | 79 | very active | 0d ago | 8mo | 2 |
| [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) | Safety / isolation | TypeScript | MIT | 1,574 (▲19) | Rising | 80 | very active | 0d ago | 9mo | 2 |
| [affaan-m/agentshield](https://github.com/affaan-m/agentshield) | Safety / isolation | TypeScript | MIT | 1,254 (▲35) | Hot | 64 | very active | 25d ago | 7mo | 7 |
| [ctxrs/ctx](https://github.com/ctxrs/ctx) | Session / token ops | Rust | Apache-2.0 | 1,149 (▲16) | Hot | 80 | very active | 3d ago | 7mo | 7 |
| [terryso/claude-auto-resume](https://github.com/terryso/claude-auto-resume) | Session / token ops | Shell | MIT | 822 (▼1) | Declining | 22 | slowing | 4mo ago | 1.3y | 0 |
| [zamalali/langchain-code](https://github.com/zamalali/langchain-code) | Multi-CLI glue | Python | Apache-2.0 | 439 | Declining | 7 | stale | 10mo ago | 1.1y | 0 |
| [aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch) | Session / token ops | Shell | MIT | 369 (▼1) | Declining | 41 | active | 25d ago | 1.2y | 1 |
| [opalinehq/cli](https://github.com/opalinehq/cli) | Session / token ops | TypeScript | MIT | 305 (▲4) | Rising | 76 | very active | 1d ago | 7mo | 2 |
| [rsrohan99/tig](https://github.com/rsrohan99/tig) | Terminal coding agent | Python | — | 152 | Abandoned | 5 | stale | 1.4y ago | 1.5y | 0 |
| [BA-CalderonMorales/terminal-jarvis](https://github.com/BA-CalderonMorales/terminal-jarvis) | Multi-CLI glue | Rust | MIT | 136 (▲1) | Hot | 77 | very active | 26d ago | 1.2y | 4 |

## Advantages & disadvantages — agent by agent

The core comparison. Sourced from 2026 head-to-head reviews, Terminal-Bench results, and this dataset's health/lifecycle metrics (sources in Methodology).

| Agent | ★ Stars | Advantages | Disadvantages |
|---|---|---|---|
| **[claude-code](https://github.com/anthropics/claude-code)** | 149,465 | Best-in-class multi-file refactoring and reasoning depth (SWE-bench Pro 69.2%); asks clarifying questions; subagents/hooks/skills/MCP ecosystem is the deepest; 83.1% Terminal-Bench 2.1 with Fable 5 | Not open source (no OSS license in repo); Anthropic-models only; subscription/usage costs add up on heavy agentic use |
| **[opencode](https://github.com/anomalyco/opencode)** | 211,816 | Most-starred OSS agent, MIT license; provider-neutral — 75+ endpoints incl. Bedrock, OpenRouter, local Ollama; strong TUI; no vendor lock-in | Bring-your-own-model means quality varies with the model you pick; harness benchmark scores trail the vendor-tuned agents |
| **[codex](https://github.com/openai/codex)** | 127,900 | #1 named CLI agent on Terminal-Bench 2.1 (83.4% w/ GPT-5.5); fast single-binary Rust TUI; excels at intent-driven, pattern-following edits | OpenAI-models only; less transparent reasoning than Claude Code on big refactors; ecosystem (hooks/plugins) thinner |
| **[gemini-cli](https://github.com/google-gemini/gemini-cli)** | 107,232 | 1M-token context — holds a monorepo in one window; Apache-2.0; was the best free tier in the field | Deprecated June 2026: replaced by closed-source Antigravity CLI (agy), free tier cut from ~1,000 to ~20 requests/day — adopt with exit plan |
| **[goose](https://github.com/aaif-goose/goose)** | 54,950 | MCP-first and extensible beyond coding (install/execute/test); any-LLM incl. local; Block-backed, health 99 in this snapshot | Less specialized for pure code-editing loops; leaderboard results modest — team optimizes for failure-pattern fixes, not benchmark rank |
| **[aider](https://github.com/Aider-AI/aider)** | 49,374 | Best git discipline (clean auto-commits); precise file-scoped edits; provider-resilient; the safest 'pair programmer' rather than autonomous agent | Not autonomous — no system-wide orchestration; no MCP support; momentum slowing (52d since push, health 50 in snapshot) |
| **[crush](https://github.com/charmbracelet/crush)** | 28,494 | The most polished TUI aesthetics in the field; multi-model; Charm's Bubble Tea expertise shows in UX | Youngest of the majors — no public benchmark record; non-standard license; smaller ecosystem |
| **[qwen-code](https://github.com/QwenLM/qwen-code)** | 28,311 | Competitive Qwen3-Coder models; best-in-class on Chinese-language briefs and Alibaba-cloud ecosystem; Apache-2.0 | OAuth free tier discontinued 2026-04 — headline value now requires paid API; less strong outside the Qwen model family |
| **[copilot-cli](https://github.com/github/copilot-cli)** | 11,237 | Copilot agent with native GitHub integration (issues, PRs, Actions); familiar billing for Copilot shops | Premium-request pricing — one debugging session can eat a week's free allocation; value collapses off-GitHub (GitLab/Bitbucket) |
| **[pi](https://github.com/earendil-works/pi)** | 112,592 | Minimal, hackable toolkit (API + agent loop + TUI + CLI) — ideal base for building your own agent; MIT | A toolkit, not a turnkey product — you assemble the workflow yourself; smaller community than the big four |
| **[oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** | 69,807 | Token-efficiency-first harness (the 'tokenmaxxer' pick) layered on Codex/OpenCode for complex codebases | Depends on underlying agents; opinionated workflow; no OSS license declared |
| **[freebuff](https://github.com/CodebuffAI/freebuff)** | 13,200 | Simple terminal codegen with low setup friction; Apache-2.0 | Far smaller scope and community than the majors; fewer agentic features (no deep hooks/MCP story) |
| **[tig](https://github.com/rsrohan99/tig)** | 152 | Historic multi-LLM flexibility (Gemini, Groq, Deepseek) before the majors had it | Abandoned (437d since push, health 5) — do not adopt; kept here to show the category's churn |

## Task rankings — which TUI for which job

| Task | 🥇 First pick | 🥈 Second | 🥉 Third | Evidence / note |
|---|---|---|---|---|
| **Complex multi-file refactors in a large repo** | `claude-code` — reasoning depth + style consistency | `codex` — pattern-faithful edits, benchmark leader | `opencode` — same job, any model, MIT | Claude Code leads SWE-bench Pro (69.2%); Codex CLI leads Terminal-Bench 2.1 (83.4%). |
| **Best raw agentic benchmark ceiling** | `codex` — 83.4% Terminal-Bench 2.1 (GPT-5.5) | `claude-code` — 83.1% with Fable 5; 78.9% with Opus 4.8 | `goose` — solid but optimizes failure patterns over rank | Terminal-Bench 2.1 public leaderboard, June 2026 snapshot. |
| **Model freedom / local LLMs (no vendor lock-in)** | `opencode` — 75+ endpoints incl. Ollama | `goose` — any LLM, MCP-first | `crush` — multi-model with the nicest TUI | opencode is the most-starred OSS agent and the de-facto neutral choice. |
| **Monorepo-scale context in one window** | `gemini-cli` — 1M-token context — but see deprecation caveat | `claude-code` — subagents fan out instead of one big window | `opencode` — pair with a long-context model of your choice | Gemini's 1M context is unmatched, but the OSS CLI was frozen June 2026 (Antigravity). |
| **Careful pair-programming with git discipline** | `aider` — clean scoped diffs, auto-commits | `claude-code` — plan mode + hooks for guarded edits | `codex` — tight, reviewable single-file changes | Aider remains the reference for git-native, human-in-the-loop editing. |
| **Token- and cost-conscious agentic coding** | `oh-my-openagent` — built for tokenmaxxers | `opencode` — route to cheap/local models; add rtk proxy | `qwen-code` — cheap capable models — free tier gone though | Pair any pick with `rtk` (60–90% token cut) and `codeburn` (cost tracking). |
| **GitHub-centric team workflows** | `copilot-cli` — native issues/PR/Actions integration | `claude-code` — gh CLI + hooks cover most of it | `codex` — cloud-task handoff to the Codex platform | Copilot CLI's value is the GitHub integration; it collapses off-platform. |
| **Building your own agent / custom TUI** | `pi` — toolkit: LLM API + loop + TUI ready-made | `bubbletea` — the TUI framework everything's built on | `opencode` — fork-friendly MIT reference implementation | pi gives the agent loop; Bubble Tea gives the terminal UI substrate. |

## By category

### Terminal coding agent

_The TUIs themselves — full agentic loops (plan → edit → run → iterate) living in your terminal. Differ in model access, autonomy level, ecosystem depth, and openness._

- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** · 211,816★ · TypeScript · Hot  
  The most-starred open-source coding agent — provider-neutral (75+ LLM endpoints incl. local), MIT.  
  <sub>topics: —</sub>
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** · 149,465★ · TypeScript · Hot  
  Anthropic's agentic coding TUI — deep codebase understanding, subagents, hooks, skills, MCP.  
  <sub>topics: —</sub>
- **[openai/codex](https://github.com/openai/codex)** · 127,900★ · Rust · Hot  
  OpenAI's lightweight Rust terminal agent — tops Terminal-Bench 2.1 among named CLI agents (83.4% with GPT-5.5).  
  <sub>topics: —</sub>
- **[earendil-works/pi](https://github.com/earendil-works/pi)** · 112,592★ · TypeScript · Hot  
  Minimal AI toolkit: unified LLM API + agent loop + TUI + coding CLI — the hackable build-your-own base.  
  <sub>topics: —</sub>
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** · 107,232★ · TypeScript · Hot  
  Gemini in the terminal with a 1M-token context window — but deprecated June 2026 in favor of closed-source Antigravity CLI.  
  <sub>topics: gemini, gemini-api, ai, ai-agents, cli, mcp-client, mcp-server</sub>
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** · 69,807★ · TypeScript · Hot  
  omo/lazycodex — token-obsessed harness layered on Codex/OpenCode for complex codebases.  
  <sub>topics: opencode, ai, anthropic, claude, claude-skills, cursor, gemini, ide</sub>
- **[aaif-goose/goose](https://github.com/aaif-goose/goose)** · 54,950★ · Rust · Mature  
  Block's extensible on-machine agent — MCP-first, goes beyond code (install, execute, test) with any LLM.  
  <sub>topics: mcp, acp, ai, ai-agents</sub>
- **[Aider-AI/aider](https://github.com/Aider-AI/aider)** · 49,374★ · Python · Mature  
  The original AI pair programmer in the terminal — git-native, focused file-level edits, not an autonomous agent.  
  <sub>topics: chatgpt, cli, command-line, gpt-4, openai, gpt-3, gpt-35-turbo, claude-3</sub>
- **[charmbracelet/crush](https://github.com/charmbracelet/crush)** · 28,494★ · Go · Hot  
  Charm's glamorous multi-model coding agent — the best-looking TUI in the field (Bubble Tea pedigree).  
  <sub>topics: agentic-ai, ai, llms, ravishing</sub>
- **[QwenLM/qwen-code](https://github.com/QwenLM/qwen-code)** · 28,311★ · TypeScript · Hot  
  Qwen team's terminal agent — strong with Qwen3-Coder and Chinese-language briefs; OAuth free tier ended 2026-04.  
  <sub>topics: agentic, ai, ai-agent, ai-coding, cli, coding-agent, developer-tools, llm</sub>
- **[CodebuffAI/freebuff](https://github.com/CodebuffAI/freebuff)** · 13,200★ · TypeScript · Mature  
  Codegen from the terminal — smaller, focused alternative.  
  <sub>topics: —</sub>
- **[github/copilot-cli](https://github.com/github/copilot-cli)** · 11,237★ · Shell · Classic  
  Copilot coding agent in the terminal — deep GitHub integration, premium-request pricing model.  
  <sub>topics: —</sub>
- **[rsrohan99/tig](https://github.com/rsrohan99/tig)** · 152★ · Python · Abandoned  
  Multi-LLM Claude-Code-alike — abandoned; listed as a cautionary tale of the category's churn.  
  <sub>topics: —</sub>

### Session / token ops

_The cost layer: agentic coding burns tokens, and these tools cut, track, and recycle them across sessions._

- **[rtk-ai/rtk](https://github.com/rtk-ai/rtk)** · 82,410★ · Rust · Hot  
  CLI proxy that cuts LLM token use 60–90% on common dev commands — single Rust binary.  
  <sub>topics: agentic-coding, ai-coding, anthropic, claude-code, cli, command-line-tool, cost-reduction, developer-tools</sub>
- **[mksglu/context-mode](https://github.com/mksglu/context-mode)** · 25,441★ · TypeScript · Rising  
  Context-window optimizer for coding agents — sandboxes tool output (~98% reduction), persists session memory.  
  <sub>topics: claude, claude-code, claude-code-plugins, mcp, skills, codex, copilot, opencode</sub>
- **[getagentseal/codeburn](https://github.com/getagentseal/codeburn)** · 11,341★ · TypeScript · Hot  
  Local token/cost tracker across 31 coding tools and agents, by model, project, and tool.  
  <sub>topics: ai-coding, claude-code, cli, codex, cost-tracking, developer-tools, observability, terminal-ui</sub>
- **[ctxrs/ctx](https://github.com/ctxrs/ctx)** · 1,149★ · Rust · Hot  
  Search the coding-agent history already on your machine — cross-agent transcript recall.  
  <sub>topics: agents, ai, claude, codex, coding-agents, cursor, developer-tools, rust</sub>
- **[terryso/claude-auto-resume](https://github.com/terryso/claude-auto-resume)** · 822★ · Shell · Declining  
  Shell utility that resumes Claude CLI tasks when usage limits lift.  
  <sub>topics: auto-resume, claude, claude-ai, claude-code, shell-script</sub>
- **[aniketkarne/ClaudeNightsWatch](https://github.com/aniketkarne/ClaudeNightsWatch)** · 369★ · Shell · Declining  
  Autonomous task runner that watches Claude usage windows and executes queued tasks.  
  <sub>topics: —</sub>
- **[opalinehq/cli](https://github.com/opalinehq/cli)** · 305★ · TypeScript · Rising  
  Claude Code & Codex session analytics. Formerly `rudel`.  
  <sub>topics: analytics, claude-code, cli, codex, developer-tools, opaline</sub>

### Safety / isolation

_An agent driving your shell is a security surface — these guard commands, sandbox environments, and audit configurations._

- **[dagger/container-use](https://github.com/dagger/container-use)** · 4,055★ · Go · Mature  
  Containerized dev environments so multiple agents work safely and independently.  
  <sub>topics: —</sub>
- **[sheeki03/tirith](https://github.com/sheeki03/tirith)** · 2,751★ · Rust · Rising  
  Terminal security for devs and agents — intercepts homograph URLs, pipe-to-shell, ANSI injection, exfiltration.  
  <sub>topics: cli, devtools, homograph-attack, rust, security, shell, supply-chain-security, terminal</sub>
- **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** · 1,574★ · TypeScript · Rising  
  Hook that catches destructive git/filesystem commands before they execute (Codex, Claude Code, more).  
  <sub>topics: claude, claude-code, claude-code-plugin, security, codex, pi-extension, ai-agents, ai-safety</sub>
- **[affaan-m/agentshield](https://github.com/affaan-m/agentshield)** · 1,254★ · TypeScript · Hot  
  Scanner for agent configs, MCP servers, and tool permissions — CLI and CI modes.  
  <sub>topics: ai-agent, anthropic, claude-code, hackathon, mcp, opus, security</sub>

### Multi-CLI glue

_Most people end up running several agents; these switch between, combine, and provision them._

- **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** · 140,188★ · Rust · Hot  
  All-in-one switcher for Claude Code, Codex, OpenCode, OpenClaw, Gemini CLI & Hermes Agent.  
  <sub>topics: ai-tools, claude-code, desktop-app, open-source, rust, tauri, codex, mcp</sub>
- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** · 56,692★ · Python · Hot  
  Run claude code, codex or pi free in terminal/VSCode/discord — proxy-style access layer.  
  <sub>topics: —</sub>
- **[UfoMiao/zcf](https://github.com/UfoMiao/zcf)** · 6,081★ · TypeScript · Hot  
  Zero-Config Code Flow — one-command setup for Claude Code & Codex.  
  <sub>topics: ai, ccr, claude, claude-ai, claude-code, cli, nodejs, typescript</sub>
- **[zamalali/langchain-code](https://github.com/zamalali/langchain-code)** · 439★ · Python · Declining  
  LangCode — combines gemini-cli and claude-code capabilities under one CLI; now declining.  
  <sub>topics: —</sub>
- **[BA-CalderonMorales/terminal-jarvis](https://github.com/BA-CalderonMorales/terminal-jarvis)** · 136★ · Rust · Hot  
  A 'shovel' to install and try every terminal coding tool from one place.  
  <sub>topics: cli, terminal, context-engineering, meta-prompting, agents, ai, framework, governance</sub>

### TUI building blocks

_The frameworks the agents' interfaces are built from — relevant if you build rather than buy._

- **[charmbracelet/bubbletea](https://github.com/charmbracelet/bubbletea)** · 45,279★ · Go · Classic  
  The Go TUI framework — the substrate under crush and much of the modern terminal-app wave.  
  <sub>topics: cli, framework, elm-architecture, tui, functional, golang, go, hacktoberfest</sub>
- **[charmbracelet/bubbles](https://github.com/charmbracelet/bubbles)** · 8,969★ · Go · Classic  
  Ready-made TUI components for Bubble Tea.  
  <sub>topics: elm-architecture, tui, terminal, cli, hacktoberfest</sub>

## Spotlight: the harness matters more than the model

The June 2026 Terminal-Bench 2.1 snapshot makes one thing unambiguous — the agent loop wrapping the model is worth real percentage points:

- Same GPT-5.5 model: **83.4%** inside Codex CLI vs **76.4%** inside the generic Terminus 2 harness — a 7-point gap that is pure harness engineering.
- Claude Code posts **83.1%** with Fable 5 and **78.9%** with Opus 4.8 — the model swap moves it more than most competitor-harness swaps do.
- Consequence for choosing: pick the *harness* whose ecosystem you can invest in (hooks, skills, MCP servers, safety nets), because vendor-tuned harness+model pairs beat mix-and-match on agentic work — while `opencode`/`goose` hedge the platform risk the Gemini CLI deprecation just demonstrated.

## Graph analysis — how they relate

**Community clustering.** These 31 tools span **13 of the graph's 40 communities**.

- **Community 13** (5): `earendil-works/pi`, `CodebuffAI/freebuff`, `mksglu/context-mode`, `sheeki03/tirith`, `kenryu42/cc-safety-net`
- **Community 5** (5): `code-yeongyu/oh-my-openagent`, `ctxrs/ctx`, `opalinehq/cli`, `aniketkarne/ClaudeNightsWatch`, `BA-CalderonMorales/terminal-jarvis`
- **Community 21** (4): `anomalyco/opencode`, `google-gemini/gemini-cli`, `aaif-goose/goose`, `github/copilot-cli`
- **Community 0** (3): `Aider-AI/aider`, `dagger/container-use`, `affaan-m/agentshield`
- **Community 16** (3): `charmbracelet/crush`, `charmbracelet/bubbletea`, `charmbracelet/bubbles`
- **Community 6** (3): `rtk-ai/rtk`, `terryso/claude-auto-resume`, `farion1231/cc-switch`
- **Community 7** (2): `getagentseal/codeburn`, `Alishahryar1/free-claude-code`

**Centrality (PageRank in the full 2,304-repo graph)** — most 'hub-like' terminal-coding tools in your ecosystem:

- `mksglu/context-mode` — PageRank 0.0031
- `CodebuffAI/freebuff` — PageRank 0.0022
- `kenryu42/cc-safety-net` — PageRank 0.0010
- `charmbracelet/bubbles` — PageRank 0.0009
- `sheeki03/tirith` — PageRank 0.0008
- `QwenLM/qwen-code` — PageRank 0.0008
- `code-yeongyu/oh-my-openagent` — PageRank 0.0008
- `UfoMiao/zcf` — PageRank 0.0007
- `aaif-goose/goose` — PageRank 0.0006
- `opalinehq/cli` — PageRank 0.0006

**Direct links between these tools** (top similarity edges where both endpoints are in this report):

- `mksglu/context-mode` ⇄ `CodebuffAI/freebuff` (w=2.050) — authors: github-actions[bot]
- `charmbracelet/bubbles` ⇄ `charmbracelet/bubbletea` (w=1.310) — topics: elm-architecture, tui, cli, hacktoberfest; authors: andrinoff, meowgorithm, charmcli
- `mksglu/context-mode` ⇄ `kenryu42/cc-safety-net` (w=1.262) — topics: claude, claude-code, codex, opencode; authors: github-actions[bot]
- `kenryu42/cc-safety-net` ⇄ `CodebuffAI/freebuff` (w=1.050) — authors: github-actions[bot]
- `mksglu/context-mode` ⇄ `sheeki03/tirith` (w=1.000) — authors: github-actions[bot]
- `sheeki03/tirith` ⇄ `CodebuffAI/freebuff` (w=1.000) — authors: github-actions[bot]
- `charmbracelet/bubbles` ⇄ `charmbracelet/crush` (w=0.903) — authors: andrinoff, meowgorithm, charmcli
- `charmbracelet/bubbletea` ⇄ `charmbracelet/crush` (w=0.790) — authors: andrinoff, charmcli, meowgorithm
- `code-yeongyu/oh-my-openagent` ⇄ `kenryu42/cc-safety-net` (w=0.502) — topics: opencode, claude, cursor, ai-agents; authors: github-actions[bot]
- `mksglu/context-mode` ⇄ `code-yeongyu/oh-my-openagent` (w=0.477) — topics: claude, codex, opencode; authors: github-actions[bot]
- `opalinehq/cli` ⇄ `getagentseal/codeburn` (w=0.336) — topics: claude-code, cli, codex, developer-tools
- `mksglu/context-mode` ⇄ `earendil-works/pi` (w=0.193) — authors: github-actions[bot]
- `farion1231/cc-switch` ⇄ `mksglu/context-mode` (w=0.176) — topics: claude-code, codex, mcp, opencode

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| aaif-goose/goose | 99 | Mature | very active | 7 | 10% | 154 |
| google-gemini/gemini-cli | 95 | Hot | very active | 4 | 19% | 649 |
| anomalyco/opencode | 88 | Hot | very active | 3 | 26% | 876 |
| charmbracelet/bubbletea | 88 | Classic | active | 6 | 26% | 81 |
| openai/codex | 84 | Hot | very active | 3 | 29% | 1204 |
| getagentseal/codeburn | 84 | Hot | very active | 2 | 45% | 71 |
| QwenLM/qwen-code | 83 | Hot | very active | 2 | 36% | 753 |
| charmbracelet/crush | 81 | Hot | very active | 2 | 32% | 193 |
| earendil-works/pi | 80 | Hot | very active | 1 | 51% | 270 |
| ctxrs/ctx | 80 | Hot | very active | 1 | 92% | 72 |
| kenryu42/cc-safety-net | 80 | Rising | very active | 1 | 93% | 65 |
| anthropics/claude-code | 79 | Hot | very active | 1 | 65% | 234 |
| sheeki03/tirith | 79 | Rising | very active | 1 | 54% | 90 |
| code-yeongyu/oh-my-openagent | 78 | Hot | very active | 1 | 82% | 329 |
| CodebuffAI/freebuff | 77 | Mature | very active | 1 | 100% | 9 |
| mksglu/context-mode | 77 | Rising | very active | 1 | 100% | 195 |
| Alishahryar1/free-claude-code | 77 | Hot | very active | 1 | 86% | 47 |
| BA-CalderonMorales/terminal-jarvis | 77 | Hot | very active | 1 | 73% | 53 |
| opalinehq/cli | 76 | Rising | very active | 1 | 99% | 25 |
| farion1231/cc-switch | 76 | Hot | very active | 1 | 85% | 57 |
| rtk-ai/rtk | 75 | Hot | very active | 1 | 58% | 390 |
| charmbracelet/bubbles | 70 | Classic | active | 2 | 38% | 38 |
| github/copilot-cli | 69 | Classic | very active | 1 | 59% | 464 |
| UfoMiao/zcf | 68 | Hot | active | 1 | 68% | 96 |
| affaan-m/agentshield | 64 | Hot | very active | 1 | 80% | 6 |
| dagger/container-use | 45 | Mature | active | 1 | 86% | 14 |
| aniketkarne/ClaudeNightsWatch | 41 | Declining | active | 1 | 100% | 0 |
| Aider-AI/aider | 26 | Mature | slowing | 0 | 0% | 93 |
| terryso/claude-auto-resume | 22 | Declining | slowing | 0 | 0% | 0 |
| zamalali/langchain-code | 7 | Declining | stale | 0 | 0% | 0 |
| rsrohan99/tig | 5 | Abandoned | stale | 0 | 0% | 0 |

Watch items: `gemini-cli` is deprecated upstream (Antigravity CLI replaced it, June 2026) despite healthy-looking repo metrics; `aider` is slowing (52d since push in this snapshot); `tig` and `langchain-code` are effectively dead; `claude-auto-resume` and `ClaudeNightsWatch` are declining single-maintainer shell utilities.

## Adjacent (deliberately not listed as terminal coding agents)

- **cline/cline** (69,871★) — primarily an IDE extension (CLI mode is secondary) — not a TUI-first agent
- **continuedev/continue** (36,113★) — same: IDE-first open-source coding agent
- **OpenHands/OpenHands** (90,020★) — AI-dev *platform* (web/headless), not a terminal UI
- **langchain-ai/open-swe** (10,803★) — asynchronous *cloud* coding agent — no terminal in the loop
- **NousResearch/hermes-agent** (251,309★) — covered in the *hermes-vs-openclaw* and *agent-harnesses* reports
- **affaan-m/ECC** (273,296★) — harness/config framework on top of coding TUIs — see *claude-code-setups*
- **SuperClaude-Org/SuperClaude_Framework** (23,907★) — config framework — see *claude-code-setups* (retired upstream 2026-07)
- **BloopAI/vibe-kanban** (28,261★) — GUI orchestrator *over* coding agents, not a TUI
- **iOfficeAI/AionUi** (33,319★) — GUI wrapper over the CLIs, not a TUI
- **winfunc/opcode** (22,419★) — GUI toolkit for Claude Code
- **jesseduffield/lazygit** (82,901★) — beloved git TUI, but no AI

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json` for all repo metrics and graph structure. No API calls at generation time; fully reproducible.
- **Selection**: keyword scan (terminal / tui / cli / coding agent / pair programming) + manual curation. IDE-first agents, GUI wrappers, cloud agents, and config frameworks were routed to adjacent reports (see above).
- **Pros/cons & task rankings** cite external evidence gathered 2026-07: the [Terminal-Bench](https://www.tbench.ai/) 2.1 public leaderboard (June 2026 snapshot: Codex CLI 83.4% w/ GPT-5.5, Claude Code 83.1% w/ Fable 5 / 78.9% w/ Opus 4.8; same GPT-5.5 at 76.4% in the Terminus 2 harness), 2026 head-to-head comparisons ([tembo.io](https://www.tembo.io/blog/coding-cli-tools-comparison), [morphllm.com](https://www.morphllm.com/ai-coding-agent), [kilo.ai](https://kilo.ai/articles/best-cli-coding-agents)), and vendor announcements (Gemini CLI → Antigravity deprecation, qwen-code free-tier retirement). Benchmark numbers are point-in-time — treat rankings as defaults, not verdicts.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity; frozen benchmark citations need manual review as new models/agents ship.

<sub>Tools covered: 31 · Snapshot: 2026-10-05T13:01:39.533Z</sub>
