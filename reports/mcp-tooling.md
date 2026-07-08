# MCP (Model Context Protocol) Tooling — Landscape Report

> Derived from **kaiser-data**'s 1,243 starred repos (snapshot `2026-06-11T21:58:33.384Z`), cross-referenced with the repo-similarity graph (1,243 nodes / 4,017 edges, 31 communities).
>
> Generated 2026-07-08 by `scripts/reports/mcp_tooling.py` (regenerate any time — no API cost).

![Top tools by stars](assets/mcp-tooling-top-tools.svg)

![Tools per category](assets/mcp-tooling-categories.svg)


> **What is MCP?** The Model Context Protocol is an open standard (Anthropic, late 2024) that lets LLM apps talk to external tools/data through a uniform interface — the 'USB-C port' for AI. **Servers** expose capabilities; **clients/hosts** (Claude Desktop, Cursor, editors) consume them; **gateways** govern them at scale.

## Executive summary

- **37 MCP projects** in your stars (**519,173★** combined) — spanning the whole stack: SDKs, clients, gateways, and **23 domain servers**.
- The architecture has three roles — and your stars cover all of them:
  - **Build** (SDKs/frameworks): `servers`, `fastmcp`, `typescript-sdk`, `fastapi_mcp`, `mcp-use`
  - **Consume** (clients/hosts): `inspector`, `witsy`, `mcphub.nvim`
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
|---|---|---|---|---|---|---|---|---|---|---|
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Learning / reference | — | MIT | 88,887 | Hot | 65 | very active | 0d ago | 1.5y | 7 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | SDK / framework | TypeScript | NOASSERTION | 87,070 | Hot | 85 | very active | 4d ago | 1.6y | 17 |
| [upstash/context7](https://github.com/upstash/context7) | Server · code intelligence | TypeScript | MIT | 57,189 | Hot | 85 | very active | 0d ago | 1.2y | 15 |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Server · browser/web | TypeScript | Apache-2.0 | 33,783 | Hot | 76 | very active | 2d ago | 1.2y | 8 |
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | Server · dev-tooling | Go | MIT | 30,583 | Hot | 88 | very active | 0d ago | 1.3y | 29 |
| [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | SDK / framework | Python | Apache-2.0 | 25,597 | Hot | 83 | very active | 6d ago | 1.5y | 31 |
| [oraios/serena](https://github.com/oraios/serena) | Server · code intelligence | Python | MIT | 25,252 | Hot | 79 | very active | 0d ago | 1.2y | 16 |
| [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | Server · dev-tooling | TypeScript | MIT | 21,680 | Hot | 78 | very active | 1d ago | 1.0y | 7 |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | Server · code intelligence | TypeScript | NOASSERTION | 17,146 | Hot | 79 | very active | 0d ago | 3mo | 4 |
| [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | Learning / reference | Jupyter Notebook | MIT | 16,508 | Hot | 70 | very active | 1d ago | 1.2y | 7 |
| [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | Gateway / control plane | Go | Apache-2.0 | 15,588 | Mature | 88 | very active | 0d ago | 2.0y | 25 |
| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | SDK / framework | TypeScript | NOASSERTION | 12,646 | Hot | 80 | very active | 0d ago | 1.7y | 23 |
| [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | SDK / framework | Python | MIT | 11,911 | Declining | 24 | stale | 6mo ago | 1.3y | 0 |
| [hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome) | Server · browser/web | TypeScript | MIT | 11,899 | Declining | 30 | slowing | 5mo ago | 1.0y | 0 |
| [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) | SDK / framework | TypeScript | MIT | 10,089 | Hot | 82 | very active | 0d ago | 1.2y | 12 |
| [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) | Client / host | TypeScript | NOASSERTION | 10,052 | Hot | 71 | very active | 1d ago | 1.7y | 8 |
| [Klavis-AI/klavis](https://github.com/Klavis-AI/klavis) | Gateway / control plane | Python | Apache-2.0 | 5,747 | Hot | 74 | very active | 10d ago | 1.2y | 3 |
| [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) | Server · game/platform | TypeScript | Apache-2.0 | 5,181 | Mature | 72 | very active | 2d ago | 1.2y | 2 |
| [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) | Learning / reference | — | MIT | 4,150 | Mature | 46 | active | 9d ago | 1.5y | 1 |
| [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) | Server · game/platform | JavaScript | MIT | 4,120 | Mature | 41 | active | 1mo ago | 1.3y | 2 |
| [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) | Server · browser/web | TypeScript | Apache-2.0 | 3,369 | Mature | 44 | active | 1mo ago | 1.5y | 3 |
| [bytebase/dbhub](https://github.com/bytebase/dbhub) | Server · database/data | TypeScript | MIT | 2,953 | Hot | 59 | very active | 2d ago | 1.3y | 7 |
| [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | Server · docs/research | Python | Apache-2.0 | 2,846 | Hot | 61 | very active | 24d ago | 1.5y | 6 |
| [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx) | Server · code intelligence | Rust | Apache-2.0 | 2,631 | Hot | 80 | very active | 0d ago | 2mo | 4 |
| [brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | Server · browser/web | JavaScript | MIT | 2,446 | Hot | 70 | very active | 0d ago | 1.2y | 3 |
| [Kochava-Studios/witsy](https://github.com/Kochava-Studios/witsy) | Client / host | TypeScript | AGPL-3.0 | 1,980 | Mature | 67 | active | 1mo ago | 2.1y | 1 |
| [ravitemer/mcphub.nvim](https://github.com/ravitemer/mcphub.nvim) | Client / host | Lua | MIT | 1,779 | Declining | 41 | slowing | 4mo ago | 1.3y | 0 |
| [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) | Server · game/platform | C# | MIT | 1,767 | Mature | 62 | active | 4d ago | 1.2y | 6 |
| [shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) | Server · code intelligence | JavaScript | MIT | 864 | Declining | 62 | active | 13d ago | 1.5y | 1 |
| [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) | Server · dev-tooling | TypeScript | NOASSERTION | 724 | Hot | 82 | very active | 0d ago | 1.2y | 18 |
| [hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid) | Server · docs/research | TypeScript | MIT | 580 | Mature | 59 | active | 27d ago | 1.1y | 4 |
| [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) | Server · dev-tooling | Java | NOASSERTION | 571 | Hot | 76 | very active | 1d ago | 1.1y | 17 |
| [reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) | Server · database/data | Python | MIT | 542 | Abandoned | 1 | stale | 1.2y ago | 1.5y | 0 |
| [VectifyAI/pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp) | Server · docs/research | TypeScript | MIT | 358 | Rising | 61 | active | 15d ago | 9mo | 2 |
| [neo4j/mcp](https://github.com/neo4j/mcp) | Server · database/data | Go | NOASSERTION | 257 | Hot | 88 | very active | 0d ago | 9mo | 8 |
| [storybookjs/mcp](https://github.com/storybookjs/mcp) | Server · dev-tooling | TypeScript | MIT | 251 | Rising | 75 | very active | 0d ago | 9mo | 2 |
| [aipotheosis-labs/gate22](https://github.com/aipotheosis-labs/gate22) | Gateway / control plane | TypeScript | Apache-2.0 | 177 | Declining | 31 | stale | 6mo ago | 9mo | 0 |

## By category

### SDK / framework

_The layer you reach for to *author* an MCP server or client._

- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 87,070★ · TypeScript · Hot  
  Official reference-server monorepo — canonical examples for filesystem, git, fetch, etc.  
  <sub>topics: —</sub>
- **[PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)** · 25,597★ · Python · Hot  
  The fast, Pythonic way to build MCP servers & clients; the de-facto Python framework.  
  <sub>topics: model-context-protocol, fastmcp, mcp, agents, llms, mcp-clients, mcp-servers, mcp-tools</sub>
- **[modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** · 12,646★ · TypeScript · Hot  
  Official TypeScript SDK for building MCP servers & clients.  
  <sub>topics: —</sub>
- **[tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** · 11,911★ · Python · Declining  
  Expose existing FastAPI endpoints as MCP tools, with auth — zero-rewrite server creation.  
  <sub>topics: ai, claude, cursor, fastapi, llm, mcp, mcp-server, mcp-servers</sub>
- **[mcp-use/mcp-use](https://github.com/mcp-use/mcp-use)** · 10,089★ · TypeScript · Hot  
  Fullstack MCP framework — build MCP apps for ChatGPT/Claude and MCP servers for agents.  
  <sub>topics: mcp, model-context-protocol, apps-sdk, mcp-apps, mcp-inspector, mcp-servers, mcp-ui, agentic-framework</sub>

### Client / host

_Apps/editors that connect to servers and surface their tools to the user._

- **[modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)** · 10,052★ · TypeScript · Hot  
  Official visual debugger/inspector for testing MCP servers.  
  <sub>topics: —</sub>
- **[Kochava-Studios/witsy](https://github.com/Kochava-Studios/witsy)** · 1,980★ · TypeScript · Mature  
  Desktop AI assistant doubling as a universal MCP client.  
  <sub>topics: anthropic, genai, groq, ollama, ollama-gui, openai, electron-app, electronjs</sub>
- **[ravitemer/mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** · 1,779★ · Lua · Declining  
  MCP client for Neovim — integrates MCP servers into the editing workflow.  
  <sub>topics: avante, chatgpt, chatplugin, claude-ai, llm, mcp, mcp-client, mcp-hub</sub>

### Gateway / control plane

_Front many servers behind one endpoint; add auth, routing, and policy — the enterprise-readiness layer._

- **[googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox)** · 15,588★ · Go · Mature  
  Google's open MCP server for databases — one gateway fronting many DBs.  
  <sub>topics: genai, mcp, agent, ai, database, llm, server, agents</sub>
- **[Klavis-AI/klavis](https://github.com/Klavis-AI/klavis)** · 5,747★ · Python · Hot  
  MCP integration platform so agents use tools reliably at scale.  
  <sub>topics: ai, discord, llm, mcp, mcp-client, mcp-server, open-source, agents</sub>
- **[aipotheosis-labs/gate22](https://github.com/aipotheosis-labs/gate22)** · 177★ · TypeScript · Declining  
  Open-source MCP gateway & control plane to govern which tools agents may use.  
  <sub>topics: agents, ai, ai-agents, control-plane, gateway, guardrails, llm, mcp</sub>

### Server · browser/web

_Give agents a browser or the open web._

- **[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)** · 33,783★ · TypeScript · Hot  
  Microsoft's Playwright MCP server — drive a real browser from an agent.  
  <sub>topics: mcp, playwright</sub>
- **[hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome)** · 11,899★ · TypeScript · Declining  
  Chrome-extension-based MCP server exposing the user's actual browser.  
  <sub>topics: —</sub>
- **[browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase)** · 3,369★ · TypeScript · Mature  
  Let LLMs control a cloud browser via Browserbase + Stagehand.  
  <sub>topics: ai, browser, chrome, chromium, mcp, playwright, puppeteer</sub>
- **[brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** · 2,446★ · JavaScript · Hot  
  All-in-one MCP server for public web data access / scraping at scale.  
  <sub>topics: llm, mcp, modelcontextprotocol, scraping, ai-agents, ai-integrations, anti-bot-detection, browser-automation</sub>

### Server · database/data

_Expose databases and datasets as agent-queryable tools._

- **[bytebase/dbhub](https://github.com/bytebase/dbhub)** · 2,953★ · TypeScript · Hot  
  Zero-dependency, token-efficient database MCP server (Postgres, MySQL, SQL Server, …).  
  <sub>topics: ai, anthropic, claude, database, mcp, mcp-server, claude-ai, mysql</sub>
- **[reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** · 542★ · Python · Abandoned  
  MCP server for interactive data exploration.  
  <sub>topics: —</sub>
- **[neo4j/mcp](https://github.com/neo4j/mcp)** · 257★ · Go · Hot  
  Neo4j's official MCP server for graph-database access.  
  <sub>topics: —</sub>

### Server · dev-tooling

_Wire agents into the software-delivery toolchain (VCS, CI, quality, errors)._

- **[github/github-mcp-server](https://github.com/github/github-mcp-server)** · 30,583★ · Go · Hot  
  GitHub's official MCP server — issues, PRs, repos as agent tools.  
  <sub>topics: github, mcp, mcp-server</sub>
- **[czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** · 21,680★ · TypeScript · Hot  
  MCP server that helps agents build n8n workflows.  
  <sub>topics: mcp, mcp-server, n8n, workflows</sub>
- **[getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp)** · 724★ · TypeScript · Hot  
  Interact with Sentry (errors/issues) via LLMs.  
  <sub>topics: mcp-server, tag-production</sub>
- **[SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** · 571★ · Java · Hot  
  Official SonarQube MCP server — code quality & security in agents.  
  <sub>topics: agent, ai, mcp, mcp-server, sonarqube, code-quality, security, static-analysis</sub>
- **[storybookjs/mcp](https://github.com/storybookjs/mcp)** · 251★ · TypeScript · Rising  
  Storybook's MCP server for component-driven workflows.  
  <sub>topics: —</sub>

### Server · code intelligence

_Feed agents accurate code/library context — the antidote to hallucinated APIs._

- **[upstash/context7](https://github.com/upstash/context7)** · 57,189★ · TypeScript · Hot  
  Up-to-date library docs piped to LLMs/editors via MCP — kills version drift.  
  <sub>topics: llm, mcp, mcp-server, vibe-coding</sub>
- **[oraios/serena](https://github.com/oraios/serena)** · 25,252★ · Python · Hot  
  Powerful MCP coding toolkit — semantic retrieval & editing (LSP-backed).  
  <sub>topics: agent, ai, vibe-coding, mcp-server, ai-coding, language-server, programming, claude</sub>
- **[mksglu/context-mode](https://github.com/mksglu/context-mode)** · 17,146★ · TypeScript · Hot  
  Context-window optimization for coding agents; sandboxes tool output (~98% reduction).  
  <sub>topics: claude, claude-code, claude-code-plugins, mcp, skills, codex, copilot, opencode</sub>
- **[yvgude/lean-ctx](https://github.com/yvgude/lean-ctx)** · 2,631★ · Rust · Hot  
  Cognitive context layer — 51+ MCP tools, multiple read modes for agentic systems.  
  <sub>topics: ai, cursor, llm, mcp, rust, token-optimization, agentic-coding, claude-code</sub>
- **[shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** · 864★ · JavaScript · Declining  
  Persistent memory for Claude via a local knowledge graph (also in the memory report).  
  <sub>topics: ai-memory, claude-ai, knowledge-graph, mcp, memory-server, typescript</sub>

### Server · docs/research

_Documents, papers, and diagram generation._

- **[blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** · 2,846★ · Python · Hot  
  Search & analyze arXiv papers through MCP.  
  <sub>topics: ai, claude-ai, gpt, mcp-server, arxiv, papers, research, llm</sub>
- **[hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** · 580★ · TypeScript · Mature  
  Generate Mermaid diagrams/charts dynamically via MCP.  
  <sub>topics: mcp, mcp-server, mermaid, mermaidjs</sub>
- **[VectifyAI/pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp)** · 358★ · TypeScript · Rising  
  MCP front-end to PageIndex's vectorless reasoning-based RAG.  
  <sub>topics: —</sub>

### Server · game/platform

_Drive game engines and mobile/desktop platforms._

- **[mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp)** · 5,181★ · TypeScript · Mature  
  MCP server for mobile automation/scraping (iOS, Android, emulators).  
  <sub>topics: android, ios, mcp, mobile, agent, emulator, physical, real</sub>
- **[Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp)** · 4,120★ · JavaScript · Mature  
  MCP server to drive the Godot game engine (launch editor, run scenes).  
  <sub>topics: ai, godot, mcp</sub>
- **[CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity)** · 1,767★ · C# · Mature  
  MCP plugin connecting agents (Cursor/Claude) to the Unity editor.  
  <sub>topics: cursor, unity, unity-package, mcp, copilot, game-development, model-context-protocol, openai</sub>

### Learning / reference

_Where the ecosystem is catalogued and taught._

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 88,887★ · — · Hot  
  The flagship awesome-list of MCP servers (88k★).  
  <sub>topics: ai, mcp</sub>
- **[microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** · 16,508★ · Jupyter Notebook · Hot  
  Microsoft's open curriculum teaching MCP fundamentals.  
  <sub>topics: csharp, java, javascript, mcp, mcp-client, mcp-security, mcp-server, model</sub>
- **[wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** · 4,150★ · — · Mature  
  Curated list of MCP servers.  
  <sub>topics: —</sub>

## Spotlight: official vendor servers

A maturity signal — major vendors shipping **first-party** MCP servers in your stars:

- **Upstash** — [upstash/context7](https://github.com/upstash/context7) · 57,189★ · health 85
- **Microsoft** — [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) · 33,783★ · health 76
- **GitHub** — [github/github-mcp-server](https://github.com/github/github-mcp-server) · 30,583★ · health 88
- **Microsoft (edu)** — [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) · 16,508★ · health 70
- **Google** — [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) · 15,588★ · health 88
- **Sentry** — [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) · 724★ · health 82
- **SonarSource** — [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) · 571★ · health 76
- **Neo4j** — [neo4j/mcp](https://github.com/neo4j/mcp) · 257★ · health 88
- **Storybook** — [storybookjs/mcp](https://github.com/storybookjs/mcp) · 251★ · health 75

## Graph analysis — how they relate

**Community clustering.** These 37 projects span **13 of the graph's 31 communities** — MCP tooling is woven through the whole agent-infra landscape rather than sitting in one bucket.

- **Community 10** (8): `mcp-use/mcp-use`, `github/github-mcp-server`, `getsentry/sentry-mcp`, `SonarSource/sonarqube-mcp-server`, `czlonkowski/n8n-mcp`, `storybookjs/mcp`, `upstash/context7`, `hustcc/mcp-mermaid`
- **Community 1** (7): `PrefectHQ/fastmcp`, `tadata-org/fastapi_mcp`, `Klavis-AI/klavis`, `aipotheosis-labs/gate22`, `bytebase/dbhub`, `Coding-Solo/godot-mcp`, `punkpeye/awesome-mcp-servers`
- **Community 11** (4): `ravitemer/mcphub.nvim`, `browserbase/mcp-server-browserbase`, `mksglu/context-mode`, `blazickjp/arxiv-mcp-server`
- **Community 21** (4): `shaneholloman/mcp-knowledge-graph`, `modelcontextprotocol/servers`, `modelcontextprotocol/typescript-sdk`, `modelcontextprotocol/inspector`
- **Community 7** (2): `Kochava-Studios/witsy`, `neo4j/mcp`
- **Community 13** (2): `microsoft/playwright-mcp`, `microsoft/mcp-for-beginners`
- **Community 19** (2): `brightdata/brightdata-mcp`, `mobile-next/mobile-mcp`
- **Community 0** (2): `reading-plus-ai/mcp-server-data-exploration`, `CoderGamester/mcp-unity`
- **Community 18** (2): `oraios/serena`, `yvgude/lean-ctx`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' MCP projects in your ecosystem:

- `microsoft/mcp-for-beginners` — PageRank 0.0029
- `github/github-mcp-server` — PageRank 0.0019
- `mksglu/context-mode` — PageRank 0.0018
- `browserbase/mcp-server-browserbase` — PageRank 0.0018
- `czlonkowski/n8n-mcp` — PageRank 0.0016
- `punkpeye/awesome-mcp-servers` — PageRank 0.0013
- `hustcc/mcp-mermaid` — PageRank 0.0012
- `modelcontextprotocol/typescript-sdk` — PageRank 0.0011
- `blazickjp/arxiv-mcp-server` — PageRank 0.0011
- `upstash/context7` — PageRank 0.0010

**Direct links between MCP projects** (top similarity edges where both endpoints are in this report):

- `modelcontextprotocol/inspector` ⇄ `modelcontextprotocol/servers` (w=0.823) — authors: cliffhall, olaservo, galagaevdc
- `modelcontextprotocol/typescript-sdk` ⇄ `modelcontextprotocol/servers` (w=0.712) — authors: KKonstantinov, nielskaspers, olaservo
- `microsoft/playwright-mcp` ⇄ `microsoft/mcp-for-beginners` (w=0.710) — topics: mcp; authors: dependabot[bot]
- `Coding-Solo/godot-mcp` ⇄ `punkpeye/awesome-mcp-servers` (w=0.667) — topics: ai, mcp
- `modelcontextprotocol/typescript-sdk` ⇄ `modelcontextprotocol/inspector` (w=0.617) — authors: olaservo
- `hustcc/mcp-mermaid` ⇄ `czlonkowski/n8n-mcp` (w=0.583) — topics: mcp, mcp-server; authors: Copilot
- `czlonkowski/n8n-mcp` ⇄ `upstash/context7` (w=0.479) — topics: mcp, mcp-server; authors: cnYui
- `hustcc/mcp-mermaid` ⇄ `github/github-mcp-server` (w=0.463) — topics: mcp, mcp-server; authors: Copilot
- `czlonkowski/n8n-mcp` ⇄ `github/github-mcp-server` (w=0.457) — topics: mcp, mcp-server; authors: Copilot
- `github/github-mcp-server` ⇄ `upstash/context7` (w=0.447) — topics: mcp, mcp-server; authors: github-actions[bot]
- `mksglu/context-mode` ⇄ `mcp-use/mcp-use` (w=0.360) — topics: claude-code, mcp, skills, openclaw; authors: github-actions[bot]
- `Klavis-AI/klavis` ⇄ `aipotheosis-labs/gate22` (w=0.333) — topics: ai, llm, mcp, open-source
- `browserbase/mcp-server-browserbase` ⇄ `mcp-use/mcp-use` (w=0.273) — topics: ai, mcp; authors: github-actions[bot]
- `SonarSource/sonarqube-mcp-server` ⇄ `github/github-mcp-server` (w=0.267) — topics: mcp, mcp-server; authors: github-actions[bot]
- `SonarSource/sonarqube-mcp-server` ⇄ `upstash/context7` (w=0.265) — topics: mcp, mcp-server; authors: github-actions[bot]
- …and 10 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). MCP servers are often weekend projects — check this before wiring one into production agents.

| Project | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| googleapis/mcp-toolbox | 88 | Mature | very active | 3 | 20% | 43 |
| neo4j/mcp | 88 | Hot | very active | 3 | 22% | 28 |
| github/github-mcp-server | 88 | Hot | very active | 3 | 24% | 68 |
| upstash/context7 | 85 | Hot | very active | 2 | 36% | 86 |
| modelcontextprotocol/servers | 85 | Hot | very active | 4 | 24% | 24 |
| PrefectHQ/fastmcp | 83 | Hot | very active | 2 | 45% | 104 |
| mcp-use/mcp-use | 82 | Hot | very active | 2 | 30% | 1028 |
| getsentry/sentry-mcp | 82 | Hot | very active | 2 | 46% | 40 |
| yvgude/lean-ctx | 80 | Hot | very active | 1 | 89% | 205 |
| modelcontextprotocol/typescript-sdk | 80 | Hot | very active | 2 | 49% | 94 |
| oraios/serena | 79 | Hot | very active | 1 | 51% | 13 |
| mksglu/context-mode | 79 | Hot | very active | 1 | 73% | 188 |
| czlonkowski/n8n-mcp | 78 | Hot | very active | 1 | 90% | 222 |
| microsoft/playwright-mcp | 76 | Hot | very active | 1 | 71% | 66 |
| SonarSource/sonarqube-mcp-server | 76 | Hot | very active | 2 | 34% | 31 |
| storybookjs/mcp | 75 | Rising | very active | 1 | 58% | 53 |
| Klavis-AI/klavis | 74 | Hot | very active | 2 | 43% | 79 |
| mobile-next/mobile-mcp | 72 | Mature | very active | 1 | 98% | 49 |
| modelcontextprotocol/inspector | 71 | Hot | very active | 1 | 56% | 51 |
| brightdata/brightdata-mcp | 70 | Hot | very active | 1 | 86% | 10 |
| microsoft/mcp-for-beginners | 70 | Hot | very active | 2 | 42% | 0 |
| Kochava-Studios/witsy | 67 | Mature | active | 1 | 100% | 173 |
| punkpeye/awesome-mcp-servers | 65 | Hot | very active | 1 | 86% | 0 |
| shaneholloman/mcp-knowledge-graph | 62 | Declining | active | 1 | 100% | 8 |
| CoderGamester/mcp-unity | 62 | Mature | active | 1 | 74% | 8 |
| blazickjp/arxiv-mcp-server | 61 | Hot | very active | 1 | 89% | 2 |
| VectifyAI/pageindex-mcp | 61 | Rising | active | 1 | 70% | 19 |
| bytebase/dbhub | 59 | Hot | very active | 1 | 86% | 0 |
| hustcc/mcp-mermaid | 59 | Mature | active | 1 | 50% | 6 |
| wong2/awesome-mcp-servers | 46 | Mature | active | 1 | 100% | 0 |
| browserbase/mcp-server-browserbase | 44 | Mature | active | 1 | 67% | 1 |
| ravitemer/mcphub.nvim | 41 | Declining | slowing | 0 | 0% | 59 |
| Coding-Solo/godot-mcp | 41 | Mature | active | 1 | 83% | 0 |
| aipotheosis-labs/gate22 | 31 | Declining | stale | 0 | 0% | 8 |
| hangwin/mcp-chrome | 30 | Declining | slowing | 0 | 0% | 7 |
| tadata-org/fastapi_mcp | 24 | Declining | stale | 0 | 0% | 10 |
| reading-plus-ai/mcp-server-data-exploration | 1 | Abandoned | stale | 0 | 0% | 0 |

⚠️ **Adopt with caution** (low health and/or declining): `reading-plus-ai/mcp-server-data-exploration`, `tadata-org/fastapi_mcp`, `hangwin/mcp-chrome`, `aipotheosis-labs/gate22`, `ravitemer/mcphub.nvim`, `Coding-Solo/godot-mcp`, `browserbase/mcp-server-browserbase`, `shaneholloman/mcp-knowledge-graph`.

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

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible.
- **Selection**: word-boundary scan for `mcp` / 'model context protocol' across name/description/topics/README, then manual curation into roles + server domains. Many repos *mention* MCP support (agents, IDEs, gateways like litellm/Portkey) but aren't MCP-specific tools — those were excluded to keep the list about MCP itself.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state. MCP moves *very* fast — treat ages/stars as a May-2026 snapshot.
- Re-run after a fresh `classified.json` to refresh.

<sub>Projects covered: 37 (23 servers) · Snapshot: 2026-06-11T21:58:33.384Z</sub>
