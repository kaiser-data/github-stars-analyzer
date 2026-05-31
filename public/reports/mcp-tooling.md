# MCP (Model Context Protocol) Tooling — Landscape Report

> Derived from **kaiser-data**'s 1,071 starred repos (snapshot `2026-05-24T19:57:47.245Z`), cross-referenced with the repo-similarity graph (1,071 nodes / 3,486 edges, 23 communities).
>
> Generated 2026-05-31 by `scripts/reports/mcp_tooling.py` (regenerate any time — no API cost).

> **What is MCP?** The Model Context Protocol is an open standard (Anthropic, late 2024) that lets LLM apps talk to external tools/data through a uniform interface — the 'USB-C port' for AI. **Servers** expose capabilities; **clients/hosts** (Claude Desktop, Cursor, editors) consume them; **gateways** govern them at scale.

## Executive summary

- **34 MCP projects** in your stars (**400,473★** combined) — spanning the whole stack: SDKs, clients, gateways, and **23 domain servers**.
- The architecture has three roles — and your stars cover all of them:
  - **Build** (SDKs/frameworks): `fastmcp`, `fastapi_mcp`, `mcp-use`
  - **Consume** (clients/hosts): `witsy`, `mcphub.nvim`
  - **Govern** (gateways/control planes): `mcp-toolbox`, `klavis`, `gate22`
- **Official vendor servers dominate the top** — GitHub, Microsoft (Playwright), Google (mcp-toolbox), Neo4j, Sentry, SonarSource all ship first-party MCP servers, a strong signal the protocol has crossed into mainstream adoption.
- TypeScript is the lingua franca of MCP servers; Python leads the SDK/framework layer (fastmcp, fastapi_mcp).

## The MCP stack at a glance

| Role | What it does | Tools in your stars |
|---|---|---|
| **SDK / framework** | Build servers/clients | `fastmcp`, `mcp-use`, `fastapi_mcp` |
| **Client / host** | Apps that consume servers | `mcphub.nvim`, `witsy` |
| **Gateway / control plane** | Route, secure & govern servers | `klavis`, `gate22`, `mcp-toolbox` |
| **Servers** | Expose a capability to agents | 23 across browser, DB, dev-tools, code-intel, docs, game engines |
| **Learning** | Lists & curricula | `awesome-mcp-servers` (×2), `mcp-for-beginners` |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Project | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Learning / reference | — | MIT | 87,798 | Hot | 62 | very active | 22d ago | 1.5y | 19 |
| [upstash/context7](https://github.com/upstash/context7) | Server · code intelligence | TypeScript | MIT | 56,002 | Hot | 84 | very active | 2d ago | 1.2y | 14 |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Server · browser/web | TypeScript | Apache-2.0 | 32,957 | Hot | 76 | very active | 1d ago | 1.2y | 11 |
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | Server · dev-tooling | Go | MIT | 30,138 | Hot | 88 | very active | 2d ago | 1.2y | 25 |
| [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | SDK / framework | Python | Apache-2.0 | 25,293 | Hot | 84 | very active | 0d ago | 1.5y | 29 |
| [oraios/serena](https://github.com/oraios/serena) | Server · code intelligence | Python | MIT | 24,566 | Hot | 84 | very active | 1d ago | 1.2y | 18 |
| [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | Server · dev-tooling | TypeScript | MIT | 21,226 | Hot | 77 | very active | 1d ago | 11mo | 6 |
| [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | Learning / reference | Jupyter Notebook | MIT | 16,186 | Hot | 70 | very active | 1d ago | 1.1y | 5 |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | Server · code intelligence | TypeScript | NOASSERTION | 15,558 | Hot | 80 | very active | 0d ago | 3mo | 16 |
| [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | Gateway / control plane | Go | Apache-2.0 | 15,326 | Hot | 92 | very active | 1d ago | 2.0y | 21 |
| [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | SDK / framework | Python | MIT | 11,877 | Declining | 25 | stale | 6mo ago | 1.2y | 0 |
| [hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome) | Server · browser/web | TypeScript | MIT | 11,707 | Declining | 35 | slowing | 4mo ago | 11mo | 0 |
| [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) | SDK / framework | TypeScript | MIT | 9,995 | Hot | 81 | very active | 1d ago | 1.2y | 15 |
| [Klavis-AI/klavis](https://github.com/Klavis-AI/klavis) | Gateway / control plane | Python | Apache-2.0 | 5,743 | Hot | 79 | very active | 5d ago | 1.1y | 3 |
| [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) | Server · game/platform | TypeScript | Apache-2.0 | 5,004 | Hot | 73 | very active | 7d ago | 1.2y | 4 |
| [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) | Learning / reference | — | MIT | 4,102 | Mature | 43 | active | 24d ago | 1.5y | 1 |
| [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) | Server · game/platform | JavaScript | MIT | 3,815 | Mature | 43 | active | 1mo ago | 1.2y | 2 |
| [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) | Server · browser/web | TypeScript | Apache-2.0 | 3,351 | Mature | 46 | active | 17d ago | 1.5y | 4 |
| [bytebase/dbhub](https://github.com/bytebase/dbhub) | Server · database/data | TypeScript | MIT | 2,824 | Hot | 57 | active | 1mo ago | 1.2y | 7 |
| [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | Server · docs/research | Python | Apache-2.0 | 2,767 | Hot | 63 | very active | 6d ago | 1.5y | 6 |
| [brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | Server · browser/web | JavaScript | MIT | 2,405 | Mature | 69 | active | 1mo ago | 1.1y | 2 |
| [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx) | Server · code intelligence | Rust | Apache-2.0 | 2,146 | Hot | 79 | very active | 0d ago | 2mo | 9 |
| [Kochava-Studios/witsy](https://github.com/Kochava-Studios/witsy) | Client / host | TypeScript | AGPL-3.0 | 1,973 | Mature | 73 | active | 1mo ago | 2.1y | 2 |
| [ravitemer/mcphub.nvim](https://github.com/ravitemer/mcphub.nvim) | Client / host | Lua | MIT | 1,768 | Declining | 43 | slowing | 4mo ago | 1.3y | 0 |
| [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) | Server · game/platform | C# | MIT | 1,717 | Mature | 63 | very active | 7d ago | 1.2y | 7 |
| [shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) | Server · code intelligence | JavaScript | MIT | 862 | Declining | 41 | slowing | 5mo ago | 1.5y | 0 |
| [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) | Server · dev-tooling | TypeScript | NOASSERTION | 702 | Hot | 76 | very active | 1d ago | 1.2y | 15 |
| [hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid) | Server · docs/research | TypeScript | MIT | 564 | Mature | 61 | active | 9d ago | 1.0y | 4 |
| [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) | Server · dev-tooling | Java | NOASSERTION | 556 | Hot | 75 | very active | 0d ago | 1.1y | 15 |
| [reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) | Server · database/data | Python | MIT | 538 | Abandoned | 1 | stale | 1.2y ago | 1.5y | 0 |
| [VectifyAI/pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp) | Server · docs/research | TypeScript | MIT | 345 | Declining | 42 | slowing | 3mo ago | 9mo | 0 |
| [neo4j/mcp](https://github.com/neo4j/mcp) | Server · database/data | Go | NOASSERTION | 243 | Hot | 87 | very active | 4d ago | 9mo | 8 |
| [storybookjs/mcp](https://github.com/storybookjs/mcp) | Server · dev-tooling | TypeScript | MIT | 243 | Hot | 80 | very active | 1d ago | 9mo | 4 |
| [aipotheosis-labs/gate22](https://github.com/aipotheosis-labs/gate22) | Gateway / control plane | TypeScript | Apache-2.0 | 176 | Declining | 32 | slowing | 5mo ago | 9mo | 0 |

## By category

### SDK / framework

_The layer you reach for to *author* an MCP server or client._

- **[PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)** · 25,293★ · Python · Hot  
  The fast, Pythonic way to build MCP servers & clients; the de-facto Python framework.  
  <sub>topics: model-context-protocol, fastmcp, mcp, agents, llms, mcp-clients, mcp-servers, mcp-tools</sub>
- **[tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** · 11,877★ · Python · Declining  
  Expose existing FastAPI endpoints as MCP tools, with auth — zero-rewrite server creation.  
  <sub>topics: ai, claude, cursor, fastapi, llm, mcp, mcp-server, mcp-servers</sub>
- **[mcp-use/mcp-use](https://github.com/mcp-use/mcp-use)** · 9,995★ · TypeScript · Hot  
  Fullstack MCP framework — build MCP apps for ChatGPT/Claude and MCP servers for agents.  
  <sub>topics: mcp, model-context-protocol, apps-sdk, mcp-apps, mcp-inspector, mcp-servers, mcp-ui, agentic-framework</sub>

### Client / host

_Apps/editors that connect to servers and surface their tools to the user._

- **[Kochava-Studios/witsy](https://github.com/Kochava-Studios/witsy)** · 1,973★ · TypeScript · Mature  
  Desktop AI assistant doubling as a universal MCP client.  
  <sub>topics: anthropic, genai, groq, ollama, ollama-gui, openai, electron-app, electronjs</sub>
- **[ravitemer/mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** · 1,768★ · Lua · Declining  
  MCP client for Neovim — integrates MCP servers into the editing workflow.  
  <sub>topics: avante, chatgpt, chatplugin, claude-ai, llm, mcp, mcp-client, mcp-hub</sub>

### Gateway / control plane

_Front many servers behind one endpoint; add auth, routing, and policy — the enterprise-readiness layer._

- **[googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox)** · 15,326★ · Go · Hot  
  Google's open MCP server for databases — one gateway fronting many DBs.  
  <sub>topics: genai, mcp, agent, ai, database, llm, server, agents</sub>
- **[Klavis-AI/klavis](https://github.com/Klavis-AI/klavis)** · 5,743★ · Python · Hot  
  MCP integration platform so agents use tools reliably at scale.  
  <sub>topics: ai, discord, llm, mcp, mcp-client, mcp-server, open-source, agents</sub>
- **[aipotheosis-labs/gate22](https://github.com/aipotheosis-labs/gate22)** · 176★ · TypeScript · Declining  
  Open-source MCP gateway & control plane to govern which tools agents may use.  
  <sub>topics: agents, ai, ai-agents, control-plane, gateway, guardrails, llm, mcp</sub>

### Server · browser/web

_Give agents a browser or the open web._

- **[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)** · 32,957★ · TypeScript · Hot  
  Microsoft's Playwright MCP server — drive a real browser from an agent.  
  <sub>topics: mcp, playwright</sub>
- **[hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome)** · 11,707★ · TypeScript · Declining  
  Chrome-extension-based MCP server exposing the user's actual browser.  
  <sub>topics: —</sub>
- **[browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase)** · 3,351★ · TypeScript · Mature  
  Let LLMs control a cloud browser via Browserbase + Stagehand.  
  <sub>topics: ai, browser, chrome, chromium, mcp, playwright, puppeteer</sub>
- **[brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** · 2,405★ · JavaScript · Mature  
  All-in-one MCP server for public web data access / scraping at scale.  
  <sub>topics: llm, mcp, modelcontextprotocol, scraping, ai-agents, ai-integrations, anti-bot-detection, browser-automation</sub>

### Server · database/data

_Expose databases and datasets as agent-queryable tools._

- **[bytebase/dbhub](https://github.com/bytebase/dbhub)** · 2,824★ · TypeScript · Hot  
  Zero-dependency, token-efficient database MCP server (Postgres, MySQL, SQL Server, …).  
  <sub>topics: ai, anthropic, claude, database, mcp, mcp-server, claude-ai, mysql</sub>
- **[reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** · 538★ · Python · Abandoned  
  MCP server for interactive data exploration.  
  <sub>topics: —</sub>
- **[neo4j/mcp](https://github.com/neo4j/mcp)** · 243★ · Go · Hot  
  Neo4j's official MCP server for graph-database access.  
  <sub>topics: —</sub>

### Server · dev-tooling

_Wire agents into the software-delivery toolchain (VCS, CI, quality, errors)._

- **[github/github-mcp-server](https://github.com/github/github-mcp-server)** · 30,138★ · Go · Hot  
  GitHub's official MCP server — issues, PRs, repos as agent tools.  
  <sub>topics: github, mcp, mcp-server</sub>
- **[czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** · 21,226★ · TypeScript · Hot  
  MCP server that helps agents build n8n workflows.  
  <sub>topics: mcp, mcp-server, n8n, workflows</sub>
- **[getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp)** · 702★ · TypeScript · Hot  
  Interact with Sentry (errors/issues) via LLMs.  
  <sub>topics: mcp-server, tag-production</sub>
- **[SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** · 556★ · Java · Hot  
  Official SonarQube MCP server — code quality & security in agents.  
  <sub>topics: agent, ai, mcp, mcp-server, sonarqube, code-quality, security, static-analysis</sub>
- **[storybookjs/mcp](https://github.com/storybookjs/mcp)** · 243★ · TypeScript · Hot  
  Storybook's MCP server for component-driven workflows.  
  <sub>topics: —</sub>

### Server · code intelligence

_Feed agents accurate code/library context — the antidote to hallucinated APIs._

- **[upstash/context7](https://github.com/upstash/context7)** · 56,002★ · TypeScript · Hot  
  Up-to-date library docs piped to LLMs/editors via MCP — kills version drift.  
  <sub>topics: llm, mcp, mcp-server, vibe-coding</sub>
- **[oraios/serena](https://github.com/oraios/serena)** · 24,566★ · Python · Hot  
  Powerful MCP coding toolkit — semantic retrieval & editing (LSP-backed).  
  <sub>topics: agent, ai, vibe-coding, mcp-server, ai-coding, language-server, programming, claude</sub>
- **[mksglu/context-mode](https://github.com/mksglu/context-mode)** · 15,558★ · TypeScript · Hot  
  Context-window optimization for coding agents; sandboxes tool output (~98% reduction).  
  <sub>topics: claude, claude-code, claude-code-plugins, mcp, skills, codex, copilot, opencode</sub>
- **[yvgude/lean-ctx](https://github.com/yvgude/lean-ctx)** · 2,146★ · Rust · Hot  
  Cognitive context layer — 51+ MCP tools, multiple read modes for agentic systems.  
  <sub>topics: ai, cursor, llm, mcp, rust, token-optimization, agentic-coding, claude-code</sub>
- **[shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** · 862★ · JavaScript · Declining  
  Persistent memory for Claude via a local knowledge graph (also in the memory report).  
  <sub>topics: ai-memory, claude-ai, knowledge-graph, mcp, memory-server, typescript</sub>

### Server · docs/research

_Documents, papers, and diagram generation._

- **[blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** · 2,767★ · Python · Hot  
  Search & analyze arXiv papers through MCP.  
  <sub>topics: ai, claude-ai, gpt, mcp-server, arxiv, papers, research, llm</sub>
- **[hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** · 564★ · TypeScript · Mature  
  Generate Mermaid diagrams/charts dynamically via MCP.  
  <sub>topics: mcp, mcp-server, mermaid, mermaidjs</sub>
- **[VectifyAI/pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp)** · 345★ · TypeScript · Declining  
  MCP front-end to PageIndex's vectorless reasoning-based RAG.  
  <sub>topics: —</sub>

### Server · game/platform

_Drive game engines and mobile/desktop platforms._

- **[mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp)** · 5,004★ · TypeScript · Hot  
  MCP server for mobile automation/scraping (iOS, Android, emulators).  
  <sub>topics: android, ios, mcp, mobile, agent, emulator, physical, real</sub>
- **[Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp)** · 3,815★ · JavaScript · Mature  
  MCP server to drive the Godot game engine (launch editor, run scenes).  
  <sub>topics: ai, godot, mcp</sub>
- **[CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity)** · 1,717★ · C# · Mature  
  MCP plugin connecting agents (Cursor/Claude) to the Unity editor.  
  <sub>topics: cursor, unity, unity-package, mcp, copilot, game-development, model-context-protocol, openai</sub>

### Learning / reference

_Where the ecosystem is catalogued and taught._

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 87,798★ · — · Hot  
  The flagship awesome-list of MCP servers (88k★).  
  <sub>topics: ai, mcp</sub>
- **[microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** · 16,186★ · Jupyter Notebook · Hot  
  Microsoft's open curriculum teaching MCP fundamentals.  
  <sub>topics: csharp, java, javascript, mcp, mcp-client, mcp-security, mcp-server, model</sub>
- **[wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** · 4,102★ · — · Mature  
  Curated list of MCP servers.  
  <sub>topics: —</sub>

## Spotlight: official vendor servers

A maturity signal — major vendors shipping **first-party** MCP servers in your stars:

- **Upstash** — [upstash/context7](https://github.com/upstash/context7) · 56,002★ · health 84
- **Microsoft** — [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) · 32,957★ · health 76
- **GitHub** — [github/github-mcp-server](https://github.com/github/github-mcp-server) · 30,138★ · health 88
- **Microsoft (edu)** — [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) · 16,186★ · health 70
- **Google** — [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) · 15,326★ · health 92
- **Sentry** — [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) · 702★ · health 76
- **SonarSource** — [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) · 556★ · health 75
- **Neo4j** — [neo4j/mcp](https://github.com/neo4j/mcp) · 243★ · health 87
- **Storybook** — [storybookjs/mcp](https://github.com/storybookjs/mcp) · 243★ · health 80

## Graph analysis — how they relate

**Community clustering.** These 34 projects span **13 of the graph's 23 communities** — MCP tooling is woven through the whole agent-infra landscape rather than sitting in one bucket.

- **Community 12** (10): `tadata-org/fastapi_mcp`, `Kochava-Studios/witsy`, `Klavis-AI/klavis`, `aipotheosis-labs/gate22`, `bytebase/dbhub`, `SonarSource/sonarqube-mcp-server`, `shaneholloman/mcp-knowledge-graph`, `VectifyAI/pageindex-mcp`, `Coding-Solo/godot-mcp`, `punkpeye/awesome-mcp-servers`
- **Community 6** (5): `mcp-use/mcp-use`, `ravitemer/mcphub.nvim`, `browserbase/mcp-server-browserbase`, `mksglu/context-mode`, `blazickjp/arxiv-mcp-server`
- **Community 13** (5): `github/github-mcp-server`, `getsentry/sentry-mcp`, `czlonkowski/n8n-mcp`, `upstash/context7`, `hustcc/mcp-mermaid`
- **Community 3** (3): `PrefectHQ/fastmcp`, `googleapis/mcp-toolbox`, `yvgude/lean-ctx`
- **Community 16** (2): `microsoft/playwright-mcp`, `microsoft/mcp-for-beginners`
- **Community 0** (2): `hangwin/mcp-chrome`, `mobile-next/mobile-mcp`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' MCP projects in your ecosystem:

- `browserbase/mcp-server-browserbase` — PageRank 0.0024
- `microsoft/mcp-for-beginners` — PageRank 0.0023
- `github/github-mcp-server` — PageRank 0.0022
- `upstash/context7` — PageRank 0.0018
- `punkpeye/awesome-mcp-servers` — PageRank 0.0018
- `hustcc/mcp-mermaid` — PageRank 0.0016
- `microsoft/playwright-mcp` — PageRank 0.0015
- `yvgude/lean-ctx` — PageRank 0.0015
- `mksglu/context-mode` — PageRank 0.0014
- `czlonkowski/n8n-mcp` — PageRank 0.0014

**Direct links between MCP projects** (top similarity edges where both endpoints are in this report):

- `microsoft/playwright-mcp` ⇄ `microsoft/mcp-for-beginners` (w=0.700) — topics: mcp; authors: dependabot[bot]
- `Coding-Solo/godot-mcp` ⇄ `punkpeye/awesome-mcp-servers` (w=0.667) — topics: ai, mcp
- `hustcc/mcp-mermaid` ⇄ `czlonkowski/n8n-mcp` (w=0.606) — topics: mcp, mcp-server; authors: Copilot
- `github/github-mcp-server` ⇄ `upstash/context7` (w=0.508) — topics: mcp, mcp-server; authors: dependabot[bot], github-actions[bot]
- `hustcc/mcp-mermaid` ⇄ `github/github-mcp-server` (w=0.471) — topics: mcp, mcp-server; authors: Copilot
- `czlonkowski/n8n-mcp` ⇄ `github/github-mcp-server` (w=0.467) — topics: mcp, mcp-server; authors: Copilot
- `hustcc/mcp-mermaid` ⇄ `upstash/context7` (w=0.383) — topics: mcp, mcp-server
- `Klavis-AI/klavis` ⇄ `aipotheosis-labs/gate22` (w=0.333) — topics: ai, llm, mcp, open-source
- `getsentry/sentry-mcp` ⇄ `upstash/context7` (w=0.321) — topics: mcp-server; authors: dependabot[bot]
- `getsentry/sentry-mcp` ⇄ `github/github-mcp-server` (w=0.301) — topics: mcp-server; authors: dependabot[bot]
- `mksglu/context-mode` ⇄ `mcp-use/mcp-use` (w=0.293) — topics: claude-code, mcp, skills, openclaw; authors: github-actions[bot]
- `getsentry/sentry-mcp` ⇄ `hustcc/mcp-mermaid` (w=0.250) — topics: mcp-server
- `SonarSource/sonarqube-mcp-server` ⇄ `punkpeye/awesome-mcp-servers` (w=0.250) — topics: ai, mcp
- `browserbase/mcp-server-browserbase` ⇄ `mcp-use/mcp-use` (w=0.241) — topics: ai, mcp; authors: github-actions[bot]
- `Coding-Solo/godot-mcp` ⇄ `SonarSource/sonarqube-mcp-server` (w=0.222) — topics: ai, mcp
- …and 10 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). MCP servers are often weekend projects — check this before wiring one into production agents.

| Project | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| googleapis/mcp-toolbox | 92 | Hot | very active | 4 | 25% | 42 |
| github/github-mcp-server | 88 | Hot | very active | 3 | 23% | 63 |
| neo4j/mcp | 87 | Hot | very active | 3 | 21% | 27 |
| PrefectHQ/fastmcp | 84 | Hot | very active | 2 | 45% | 101 |
| oraios/serena | 84 | Hot | very active | 2 | 42% | 11 |
| upstash/context7 | 84 | Hot | very active | 2 | 34% | 78 |
| mcp-use/mcp-use | 81 | Hot | very active | 2 | 28% | 928 |
| storybookjs/mcp | 80 | Hot | very active | 2 | 42% | 53 |
| mksglu/context-mode | 80 | Hot | very active | 1 | 59% | 177 |
| Klavis-AI/klavis | 79 | Hot | very active | 2 | 41% | 79 |
| yvgude/lean-ctx | 79 | Hot | very active | 1 | 88% | 189 |
| czlonkowski/n8n-mcp | 77 | Hot | very active | 1 | 91% | 217 |
| microsoft/playwright-mcp | 76 | Hot | very active | 1 | 67% | 65 |
| getsentry/sentry-mcp | 76 | Hot | very active | 1 | 65% | 39 |
| SonarSource/sonarqube-mcp-server | 75 | Hot | very active | 2 | 34% | 30 |
| Kochava-Studios/witsy | 73 | Mature | active | 1 | 97% | 173 |
| mobile-next/mobile-mcp | 73 | Hot | very active | 1 | 96% | 45 |
| microsoft/mcp-for-beginners | 70 | Hot | very active | 2 | 37% | 0 |
| brightdata/brightdata-mcp | 69 | Mature | active | 1 | 95% | 10 |
| blazickjp/arxiv-mcp-server | 63 | Hot | very active | 1 | 89% | 2 |
| CoderGamester/mcp-unity | 63 | Mature | very active | 1 | 63% | 8 |
| punkpeye/awesome-mcp-servers | 62 | Hot | very active | 1 | 70% | 0 |
| hustcc/mcp-mermaid | 61 | Mature | active | 1 | 50% | 6 |
| bytebase/dbhub | 57 | Hot | active | 1 | 88% | 0 |
| browserbase/mcp-server-browserbase | 46 | Mature | active | 1 | 57% | 1 |
| ravitemer/mcphub.nvim | 43 | Declining | slowing | 0 | 0% | 59 |
| Coding-Solo/godot-mcp | 43 | Mature | active | 1 | 83% | 0 |
| wong2/awesome-mcp-servers | 43 | Mature | active | 1 | 100% | 0 |
| VectifyAI/pageindex-mcp | 42 | Declining | slowing | 0 | 0% | 17 |
| shaneholloman/mcp-knowledge-graph | 41 | Declining | slowing | 0 | 0% | 8 |
| hangwin/mcp-chrome | 35 | Declining | slowing | 0 | 0% | 7 |
| aipotheosis-labs/gate22 | 32 | Declining | slowing | 0 | 0% | 8 |
| tadata-org/fastapi_mcp | 25 | Declining | stale | 0 | 0% | 10 |
| reading-plus-ai/mcp-server-data-exploration | 1 | Abandoned | stale | 0 | 0% | 0 |

⚠️ **Adopt with caution** (low health and/or declining): `reading-plus-ai/mcp-server-data-exploration`, `tadata-org/fastapi_mcp`, `aipotheosis-labs/gate22`, `hangwin/mcp-chrome`, `shaneholloman/mcp-knowledge-graph`, `VectifyAI/pageindex-mcp`, `ravitemer/mcphub.nvim`, `Coding-Solo/godot-mcp`, `wong2/awesome-mcp-servers`.

## Which one should you use?

| If you want… | Start with | Why |
|---|---|---|
| To build an MCP server in Python | `PrefectHQ/fastmcp` | The standard Pythonic framework; health 84, very active. |
| To expose an existing FastAPI app as MCP | `tadata-org/fastapi_mcp` | No rewrite — but note declining health (25); verify before relying on it. |
| A fullstack/TS way to build MCP apps | `mcp-use/mcp-use` | Build both servers and ChatGPT/Claude MCP apps. |
| To give an agent a real browser | `microsoft/playwright-mcp` | First-party Microsoft server; most-starred browser MCP here. |
| Database access for agents | `googleapis/mcp-toolbox` or `bytebase/dbhub` | Google's multi-DB gateway (health 92) or a zero-dep single server. |
| GitHub as agent tools | `github/github-mcp-server` | Official, Go, health 88 — issues/PRs/repos out of the box. |
| Accurate, current library docs in your editor | `upstash/context7` | 56k★; pipes up-to-date docs to LLMs, killing version drift. |
| Semantic code editing for a coding agent | `oraios/serena` | LSP-backed semantic retrieval & editing toolkit; health 84. |
| To govern which tools agents can use | `aipotheosis-labs/gate22` or `Klavis-AI/klavis` | Gateway/control-plane layer for policy & scale. |

## Methodology & caveats

- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: word-boundary scan for `mcp` / 'model context protocol' across name/description/topics/README, then manual curation into roles + server domains. Many repos *mention* MCP support (agents, IDEs, gateways like litellm/Portkey) but aren't MCP-specific tools — those were excluded to keep the list about MCP itself.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state. MCP moves *very* fast — treat ages/stars as a May-2026 snapshot.
- Re-run after a fresh `classified.json` to refresh.

<sub>Projects covered: 34 (23 servers) · Snapshot: 2026-05-24T19:57:47.245Z</sub>
