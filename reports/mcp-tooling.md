# MCP (Model Context Protocol) Tooling — Landscape Report

> Derived from **kaiser-data**'s 1,327 starred repos (snapshot `2026-07-13T08:42:30.177Z`), cross-referenced with the repo-similarity graph (1,327 nodes / 4,302 edges, 27 communities).
>
> Generated 2026-07-13 by `scripts/reports/mcp_tooling.py` (regenerate any time — no API cost).

![Top tools by stars](assets/mcp-tooling-top-tools.svg)

![Tools per category](assets/mcp-tooling-categories.svg)


> **What is MCP?** The Model Context Protocol is an open standard (Anthropic, late 2024) that lets LLM apps talk to external tools/data through a uniform interface — the 'USB-C port' for AI. **Servers** expose capabilities; **clients/hosts** (Claude Desktop, Cursor, editors) consume them; **gateways** govern them at scale.

## Executive summary

- **37 MCP projects** in your stars (**533,744★** combined) — spanning the whole stack: SDKs, clients, gateways, and **23 domain servers**.
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
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Learning / reference | — | MIT | 90,672 (▲1,785) | Hot | 65 | very active | 0d ago | 1.6y | 3 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | SDK / framework | TypeScript | NOASSERTION | 88,390 (▲1,320) | Hot | 77 | very active | 3d ago | 1.6y | 15 |
| [upstash/context7](https://github.com/upstash/context7) | Server · code intelligence | TypeScript | MIT | 59,013 (▲1,824) | Hot | 84 | very active | 3d ago | 1.3y | 17 |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Server · browser/web | TypeScript | Apache-2.0 | 35,009 (▲1,226) | Hot | 74 | very active | 4d ago | 1.3y | 7 |
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | Server · dev-tooling | Go | MIT | 31,399 (▲816) | Hot | 93 | very active | 3d ago | 1.4y | 35 |
| [oraios/serena](https://github.com/oraios/serena) | Server · code intelligence | Python | MIT | 26,385 (▲1,133) | Hot | 84 | very active | 1d ago | 1.3y | 16 |
| [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | SDK / framework | Python | Apache-2.0 | 26,168 (▲571) | Hot | 78 | very active | 4d ago | 1.6y | 17 |
| [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | Server · dev-tooling | TypeScript | MIT | 22,265 (▲585) | Hot | 79 | very active | 1d ago | 1.1y | 9 |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | Server · code intelligence | TypeScript | NOASSERTION | 18,861 (▲1,715) | Hot | 79 | very active | 0d ago | 4mo | 5 |
| [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | Learning / reference | Jupyter Notebook | MIT | 16,742 (▲234) | Hot | 70 | very active | 4d ago | 1.3y | 6 |
| [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | Gateway / control plane | Go | Apache-2.0 | 15,944 (▲356) | Mature | 98 | very active | 0d ago | 2.1y | 29 |
| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | SDK / framework | TypeScript | NOASSERTION | 12,839 (▲193) | Hot | 76 | very active | 0d ago | 1.8y | 9 |
| [hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome) | Server · browser/web | TypeScript | MIT | 12,099 (▲200) | Declining | 19 | stale | 6mo ago | 1.1y | 0 |
| [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | SDK / framework | Python | MIT | 11,941 (▲30) | Declining | 19 | stale | 7mo ago | 1.3y | 0 |
| [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) | Client / host | TypeScript | NOASSERTION | 10,354 (▲302) | Mature | 66 | active | 1d ago | 1.8y | 6 |
| [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) | SDK / framework | TypeScript | MIT | 10,283 (▲194) | Hot | 82 | very active | 0d ago | 1.3y | 10 |
| [Klavis-AI/klavis](https://github.com/Klavis-AI/klavis) | Gateway / control plane | Python | Apache-2.0 | 5,768 (▲21) | Mature | 61 | active | 1mo ago | 1.2y | 3 |
| [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) | Server · game/platform | TypeScript | Apache-2.0 | 5,432 (▲251) | Hot | 71 | very active | 1d ago | 1.3y | 4 |
| [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) | Server · game/platform | JavaScript | MIT | 4,678 (▲558) | Declining | 35 | slowing | 2mo ago | 1.4y | 1 |
| [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) | Learning / reference | — | MIT | 4,203 (▲53) | Mature | 48 | active | 10d ago | 1.6y | 1 |
| [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) | Server · browser/web | TypeScript | Apache-2.0 | 3,402 (▲33) | Declining | 42 | active | 6d ago | 1.6y | 1 |
| [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx) | Server · code intelligence | Rust | Apache-2.0 | 3,229 (▲598) | Hot | 80 | very active | 1d ago | 3mo | 6 |
| [bytebase/dbhub](https://github.com/bytebase/dbhub) | Server · database/data | TypeScript | MIT | 3,149 (▲196) | Hot | 62 | very active | 3d ago | 1.3y | 6 |
| [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | Server · docs/research | Python | Apache-2.0 | 2,953 (▲107) | Mature | 53 | active | 1mo ago | 1.6y | 5 |
| [brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | Server · browser/web | JavaScript | MIT | 2,495 (▲49) | Mature | 67 | very active | 22d ago | 1.2y | 3 |
| [Kochava-Studios/witsy](https://github.com/Kochava-Studios/witsy) | Client / host | TypeScript | AGPL-3.0 | 1,991 (▲11) | Mature | 47 | slowing | 2mo ago | 2.2y | 0 |
| [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) | Server · game/platform | C# | MIT | 1,827 (▲60) | Mature | 59 | very active | 9d ago | 1.3y | 5 |
| [ravitemer/mcphub.nvim](https://github.com/ravitemer/mcphub.nvim) | Client / host | Lua | MIT | 1,781 (▲2) | Declining | 30 | slowing | 5mo ago | 1.4y | 0 |
| [shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) | Server · code intelligence | JavaScript | MIT | 875 (▲11) | Declining | 59 | active | 1mo ago | 1.6y | 1 |
| [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) | Server · dev-tooling | TypeScript | NOASSERTION | 769 (▲45) | Hot | 77 | very active | 2d ago | 1.3y | 23 |
| [hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid) | Server · docs/research | TypeScript | MIT | 607 (▲27) | Declining | 53 | active | 1mo ago | 1.1y | 2 |
| [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) | Server · dev-tooling | Java | NOASSERTION | 594 (▲23) | Hot | 77 | very active | 3d ago | 1.2y | 17 |
| [reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) | Server · database/data | Python | MIT | 545 (▲3) | Abandoned | 1 | stale | 1.3y ago | 1.6y | 0 |
| [VectifyAI/pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp) | Server · docs/research | TypeScript | MIT | 374 (▲16) | Rising | 54 | active | 1mo ago | 10mo | 2 |
| [neo4j/mcp](https://github.com/neo4j/mcp) | Server · database/data | Go | NOASSERTION | 269 (▲12) | Hot | 85 | very active | 1d ago | 10mo | 8 |
| [storybookjs/mcp](https://github.com/storybookjs/mcp) | Server · dev-tooling | TypeScript | MIT | 262 (▲11) | Hot | 75 | very active | 3d ago | 10mo | 7 |
| [aipotheosis-labs/gate22](https://github.com/aipotheosis-labs/gate22) | Gateway / control plane | TypeScript | Apache-2.0 | 177 | Declining | 28 | stale | 7mo ago | 10mo | 0 |

## By category

### SDK / framework

_The layer you reach for to *author* an MCP server or client._

- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 88,390★ · TypeScript · Hot  
  Official reference-server monorepo — canonical examples for filesystem, git, fetch, etc.  
  <sub>topics: —</sub>
- **[PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)** · 26,168★ · Python · Hot  
  The fast, Pythonic way to build MCP servers & clients; the de-facto Python framework.  
  <sub>topics: model-context-protocol, fastmcp, mcp, agents, llms, mcp-clients, mcp-servers, mcp-tools</sub>
- **[modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** · 12,839★ · TypeScript · Hot  
  Official TypeScript SDK for building MCP servers & clients.  
  <sub>topics: —</sub>
- **[tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** · 11,941★ · Python · Declining  
  Expose existing FastAPI endpoints as MCP tools, with auth — zero-rewrite server creation.  
  <sub>topics: ai, claude, cursor, fastapi, llm, mcp, mcp-server, mcp-servers</sub>
- **[mcp-use/mcp-use](https://github.com/mcp-use/mcp-use)** · 10,283★ · TypeScript · Hot  
  Fullstack MCP framework — build MCP apps for ChatGPT/Claude and MCP servers for agents.  
  <sub>topics: mcp, model-context-protocol, apps-sdk, mcp-apps, mcp-inspector, mcp-servers, mcp-ui, agentic-framework</sub>

### Client / host

_Apps/editors that connect to servers and surface their tools to the user._

- **[modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)** · 10,354★ · TypeScript · Mature  
  Official visual debugger/inspector for testing MCP servers.  
  <sub>topics: —</sub>
- **[Kochava-Studios/witsy](https://github.com/Kochava-Studios/witsy)** · 1,991★ · TypeScript · Mature  
  Desktop AI assistant doubling as a universal MCP client.  
  <sub>topics: anthropic, genai, groq, ollama, ollama-gui, openai, electron-app, electronjs</sub>
- **[ravitemer/mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** · 1,781★ · Lua · Declining  
  MCP client for Neovim — integrates MCP servers into the editing workflow.  
  <sub>topics: avante, chatgpt, chatplugin, claude-ai, llm, mcp, mcp-client, mcp-hub</sub>

### Gateway / control plane

_Front many servers behind one endpoint; add auth, routing, and policy — the enterprise-readiness layer._

- **[googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox)** · 15,944★ · Go · Mature  
  Google's open MCP server for databases — one gateway fronting many DBs.  
  <sub>topics: genai, mcp, agent, ai, database, llm, server, agents</sub>
- **[Klavis-AI/klavis](https://github.com/Klavis-AI/klavis)** · 5,768★ · Python · Mature  
  MCP integration platform so agents use tools reliably at scale.  
  <sub>topics: ai, discord, llm, mcp, mcp-client, mcp-server, open-source, agents</sub>
- **[aipotheosis-labs/gate22](https://github.com/aipotheosis-labs/gate22)** · 177★ · TypeScript · Declining  
  Open-source MCP gateway & control plane to govern which tools agents may use.  
  <sub>topics: agents, ai, ai-agents, control-plane, gateway, guardrails, llm, mcp</sub>

### Server · browser/web

_Give agents a browser or the open web._

- **[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)** · 35,009★ · TypeScript · Hot  
  Microsoft's Playwright MCP server — drive a real browser from an agent.  
  <sub>topics: mcp, playwright</sub>
- **[hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome)** · 12,099★ · TypeScript · Declining  
  Chrome-extension-based MCP server exposing the user's actual browser.  
  <sub>topics: —</sub>
- **[browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase)** · 3,402★ · TypeScript · Declining  
  Let LLMs control a cloud browser via Browserbase + Stagehand.  
  <sub>topics: ai, browser, chrome, chromium, mcp, playwright, puppeteer</sub>
- **[brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** · 2,495★ · JavaScript · Mature  
  All-in-one MCP server for public web data access / scraping at scale.  
  <sub>topics: llm, mcp, modelcontextprotocol, scraping, ai-agents, ai-integrations, anti-bot-detection, browser-automation</sub>

### Server · database/data

_Expose databases and datasets as agent-queryable tools._

- **[bytebase/dbhub](https://github.com/bytebase/dbhub)** · 3,149★ · TypeScript · Hot  
  Zero-dependency, token-efficient database MCP server (Postgres, MySQL, SQL Server, …).  
  <sub>topics: ai, anthropic, claude, database, mcp, mcp-server, claude-ai, mysql</sub>
- **[reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** · 545★ · Python · Abandoned  
  MCP server for interactive data exploration.  
  <sub>topics: —</sub>
- **[neo4j/mcp](https://github.com/neo4j/mcp)** · 269★ · Go · Hot  
  Neo4j's official MCP server for graph-database access.  
  <sub>topics: —</sub>

### Server · dev-tooling

_Wire agents into the software-delivery toolchain (VCS, CI, quality, errors)._

- **[github/github-mcp-server](https://github.com/github/github-mcp-server)** · 31,399★ · Go · Hot  
  GitHub's official MCP server — issues, PRs, repos as agent tools.  
  <sub>topics: github, mcp, mcp-server</sub>
- **[czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** · 22,265★ · TypeScript · Hot  
  MCP server that helps agents build n8n workflows.  
  <sub>topics: mcp, mcp-server, n8n, workflows</sub>
- **[getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp)** · 769★ · TypeScript · Hot  
  Interact with Sentry (errors/issues) via LLMs.  
  <sub>topics: mcp-server, tag-production</sub>
- **[SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** · 594★ · Java · Hot  
  Official SonarQube MCP server — code quality & security in agents.  
  <sub>topics: agent, ai, mcp, mcp-server, sonarqube, code-quality, security, static-analysis</sub>
- **[storybookjs/mcp](https://github.com/storybookjs/mcp)** · 262★ · TypeScript · Hot  
  Storybook's MCP server for component-driven workflows.  
  <sub>topics: —</sub>

### Server · code intelligence

_Feed agents accurate code/library context — the antidote to hallucinated APIs._

- **[upstash/context7](https://github.com/upstash/context7)** · 59,013★ · TypeScript · Hot  
  Up-to-date library docs piped to LLMs/editors via MCP — kills version drift.  
  <sub>topics: llm, mcp, mcp-server, vibe-coding</sub>
- **[oraios/serena](https://github.com/oraios/serena)** · 26,385★ · Python · Hot  
  Powerful MCP coding toolkit — semantic retrieval & editing (LSP-backed).  
  <sub>topics: agent, ai, vibe-coding, mcp-server, ai-coding, language-server, programming, claude</sub>
- **[mksglu/context-mode](https://github.com/mksglu/context-mode)** · 18,861★ · TypeScript · Hot  
  Context-window optimization for coding agents; sandboxes tool output (~98% reduction).  
  <sub>topics: claude, claude-code, claude-code-plugins, mcp, skills, codex, copilot, opencode</sub>
- **[yvgude/lean-ctx](https://github.com/yvgude/lean-ctx)** · 3,229★ · Rust · Hot  
  Cognitive context layer — 51+ MCP tools, multiple read modes for agentic systems.  
  <sub>topics: ai, cursor, llm, mcp, rust, token-optimization, agentic-coding, claude-code</sub>
- **[shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** · 875★ · JavaScript · Declining  
  Persistent memory for Claude via a local knowledge graph (also in the memory report).  
  <sub>topics: ai-memory, claude-ai, knowledge-graph, mcp, memory-server, typescript</sub>

### Server · docs/research

_Documents, papers, and diagram generation._

- **[blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** · 2,953★ · Python · Mature  
  Search & analyze arXiv papers through MCP.  
  <sub>topics: ai, claude-ai, gpt, mcp-server, arxiv, papers, research, llm</sub>
- **[hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** · 607★ · TypeScript · Declining  
  Generate Mermaid diagrams/charts dynamically via MCP.  
  <sub>topics: mcp, mcp-server, mermaid, mermaidjs</sub>
- **[VectifyAI/pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp)** · 374★ · TypeScript · Rising  
  MCP front-end to PageIndex's vectorless reasoning-based RAG.  
  <sub>topics: —</sub>

### Server · game/platform

_Drive game engines and mobile/desktop platforms._

- **[mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp)** · 5,432★ · TypeScript · Hot  
  MCP server for mobile automation/scraping (iOS, Android, emulators).  
  <sub>topics: android, ios, mcp, mobile, agent, emulator, physical, real</sub>
- **[Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp)** · 4,678★ · JavaScript · Declining  
  MCP server to drive the Godot game engine (launch editor, run scenes).  
  <sub>topics: ai, godot, mcp</sub>
- **[CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity)** · 1,827★ · C# · Mature  
  MCP plugin connecting agents (Cursor/Claude) to the Unity editor.  
  <sub>topics: cursor, unity, unity-package, mcp, copilot, game-development, model-context-protocol, openai</sub>

### Learning / reference

_Where the ecosystem is catalogued and taught._

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 90,672★ · — · Hot  
  The flagship awesome-list of MCP servers (88k★).  
  <sub>topics: ai, mcp</sub>
- **[microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** · 16,742★ · Jupyter Notebook · Hot  
  Microsoft's open curriculum teaching MCP fundamentals.  
  <sub>topics: csharp, java, javascript, mcp, mcp-client, mcp-security, mcp-server, model</sub>
- **[wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** · 4,203★ · — · Mature  
  Curated list of MCP servers.  
  <sub>topics: —</sub>

## Spotlight: official vendor servers

A maturity signal — major vendors shipping **first-party** MCP servers in your stars:

- **Upstash** — [upstash/context7](https://github.com/upstash/context7) · 59,013★ · health 84
- **Microsoft** — [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) · 35,009★ · health 74
- **GitHub** — [github/github-mcp-server](https://github.com/github/github-mcp-server) · 31,399★ · health 93
- **Microsoft (edu)** — [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) · 16,742★ · health 70
- **Google** — [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) · 15,944★ · health 98
- **Sentry** — [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) · 769★ · health 77
- **SonarSource** — [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) · 594★ · health 77
- **Neo4j** — [neo4j/mcp](https://github.com/neo4j/mcp) · 269★ · health 85
- **Storybook** — [storybookjs/mcp](https://github.com/storybookjs/mcp) · 262★ · health 75

## Graph analysis — how they relate

**Community clustering.** These 37 projects span **14 of the graph's 27 communities** — MCP tooling is woven through the whole agent-infra landscape rather than sitting in one bucket.

- **Community 14** (11): `tadata-org/fastapi_mcp`, `brightdata/brightdata-mcp`, `bytebase/dbhub`, `github/github-mcp-server`, `getsentry/sentry-mcp`, `SonarSource/sonarqube-mcp-server`, `czlonkowski/n8n-mcp`, `upstash/context7`, `hustcc/mcp-mermaid`, `Coding-Solo/godot-mcp`, `punkpeye/awesome-mcp-servers`
- **Community 5** (4): `mcp-use/mcp-use`, `ravitemer/mcphub.nvim`, `mksglu/context-mode`, `mobile-next/mobile-mcp`
- **Community 1** (4): `Klavis-AI/klavis`, `aipotheosis-labs/gate22`, `browserbase/mcp-server-browserbase`, `blazickjp/arxiv-mcp-server`
- **Community 23** (4): `shaneholloman/mcp-knowledge-graph`, `modelcontextprotocol/servers`, `modelcontextprotocol/typescript-sdk`, `modelcontextprotocol/inspector`
- **Community 2** (3): `hangwin/mcp-chrome`, `oraios/serena`, `yvgude/lean-ctx`
- **Community 17** (2): `Kochava-Studios/witsy`, `CoderGamester/mcp-unity`
- **Community 18** (2): `microsoft/playwright-mcp`, `microsoft/mcp-for-beginners`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' MCP projects in your ecosystem:

- `microsoft/mcp-for-beginners` — PageRank 0.0031
- `github/github-mcp-server` — PageRank 0.0017
- `hustcc/mcp-mermaid` — PageRank 0.0015
- `mksglu/context-mode` — PageRank 0.0014
- `punkpeye/awesome-mcp-servers` — PageRank 0.0014
- `czlonkowski/n8n-mcp` — PageRank 0.0012
- `microsoft/playwright-mcp` — PageRank 0.0012
- `browserbase/mcp-server-browserbase` — PageRank 0.0011
- `modelcontextprotocol/typescript-sdk` — PageRank 0.0011
- `upstash/context7` — PageRank 0.0010

**Direct links between MCP projects** (top similarity edges where both endpoints are in this report):

- `modelcontextprotocol/inspector` ⇄ `modelcontextprotocol/servers` (w=0.883) — authors: cliffhall, olaservo, galagaevdc
- `microsoft/playwright-mcp` ⇄ `microsoft/mcp-for-beginners` (w=0.733) — topics: mcp; authors: dependabot[bot]
- `modelcontextprotocol/typescript-sdk` ⇄ `modelcontextprotocol/servers` (w=0.732) — authors: KKonstantinov, dependabot[bot]
- `Coding-Solo/godot-mcp` ⇄ `punkpeye/awesome-mcp-servers` (w=0.667) — topics: ai, mcp
- `hustcc/mcp-mermaid` ⇄ `czlonkowski/n8n-mcp` (w=0.583) — topics: mcp, mcp-server; authors: Copilot
- `czlonkowski/n8n-mcp` ⇄ `github/github-mcp-server` (w=0.495) — topics: mcp, mcp-server; authors: dependabot[bot], Copilot
- `github/github-mcp-server` ⇄ `upstash/context7` (w=0.480) — topics: mcp, mcp-server; authors: syf2211, github-actions[bot]
- `hustcc/mcp-mermaid` ⇄ `github/github-mcp-server` (w=0.456) — topics: mcp, mcp-server; authors: Copilot
- `microsoft/mcp-for-beginners` ⇄ `czlonkowski/n8n-mcp` (w=0.433) — topics: mcp, mcp-server; authors: dependabot[bot], Copilot
- `mksglu/context-mode` ⇄ `mcp-use/mcp-use` (w=0.369) — topics: claude-code, mcp, skills, openclaw; authors: github-actions[bot]
- `microsoft/playwright-mcp` ⇄ `browserbase/mcp-server-browserbase` (w=0.336) — topics: mcp, playwright
- `Klavis-AI/klavis` ⇄ `aipotheosis-labs/gate22` (w=0.333) — topics: ai, llm, mcp, open-source
- `getsentry/sentry-mcp` ⇄ `upstash/context7` (w=0.301) — topics: mcp-server; authors: syf2211
- `browserbase/mcp-server-browserbase` ⇄ `punkpeye/awesome-mcp-servers` (w=0.286) — topics: ai, mcp
- `getsentry/sentry-mcp` ⇄ `github/github-mcp-server` (w=0.285) — topics: mcp-server; authors: syf2211
- …and 9 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). MCP servers are often weekend projects — check this before wiring one into production agents.

| Project | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| googleapis/mcp-toolbox | 98 | Mature | very active | 5 | 14% | 45 |
| github/github-mcp-server | 93 | Hot | very active | 4 | 22% | 70 |
| neo4j/mcp | 85 | Hot | very active | 3 | 24% | 28 |
| oraios/serena | 84 | Hot | very active | 2 | 47% | 13 |
| upstash/context7 | 84 | Hot | very active | 2 | 39% | 93 |
| mcp-use/mcp-use | 82 | Hot | very active | 2 | 28% | 1149 |
| yvgude/lean-ctx | 80 | Hot | very active | 1 | 58% | 234 |
| czlonkowski/n8n-mcp | 79 | Hot | very active | 1 | 73% | 235 |
| mksglu/context-mode | 79 | Hot | very active | 1 | 56% | 195 |
| PrefectHQ/fastmcp | 78 | Hot | very active | 1 | 79% | 106 |
| getsentry/sentry-mcp | 77 | Hot | very active | 1 | 50% | 41 |
| SonarSource/sonarqube-mcp-server | 77 | Hot | very active | 2 | 38% | 34 |
| modelcontextprotocol/servers | 77 | Hot | very active | 2 | 47% | 26 |
| modelcontextprotocol/typescript-sdk | 76 | Hot | very active | 1 | 65% | 131 |
| storybookjs/mcp | 75 | Hot | very active | 1 | 84% | 55 |
| microsoft/playwright-mcp | 74 | Hot | very active | 1 | 68% | 68 |
| mobile-next/mobile-mcp | 71 | Hot | very active | 1 | 92% | 49 |
| microsoft/mcp-for-beginners | 70 | Hot | very active | 2 | 45% | 0 |
| brightdata/brightdata-mcp | 67 | Mature | very active | 1 | 71% | 11 |
| modelcontextprotocol/inspector | 66 | Mature | active | 1 | 50% | 51 |
| punkpeye/awesome-mcp-servers | 65 | Hot | very active | 1 | 98% | 0 |
| bytebase/dbhub | 62 | Hot | very active | 1 | 83% | 2 |
| Klavis-AI/klavis | 61 | Mature | active | 1 | 85% | 79 |
| shaneholloman/mcp-knowledge-graph | 59 | Declining | active | 1 | 100% | 8 |
| CoderGamester/mcp-unity | 59 | Mature | very active | 1 | 83% | 8 |
| VectifyAI/pageindex-mcp | 54 | Rising | active | 1 | 70% | 19 |
| blazickjp/arxiv-mcp-server | 53 | Mature | active | 1 | 78% | 2 |
| hustcc/mcp-mermaid | 53 | Declining | active | 1 | 50% | 6 |
| wong2/awesome-mcp-servers | 48 | Mature | active | 1 | 100% | 0 |
| Kochava-Studios/witsy | 47 | Mature | slowing | 0 | 0% | 173 |
| browserbase/mcp-server-browserbase | 42 | Declining | active | 1 | 100% | 1 |
| Coding-Solo/godot-mcp | 35 | Declining | slowing | 1 | 100% | 0 |
| ravitemer/mcphub.nvim | 30 | Declining | slowing | 0 | 0% | 59 |
| aipotheosis-labs/gate22 | 28 | Declining | stale | 0 | 0% | 8 |
| tadata-org/fastapi_mcp | 19 | Declining | stale | 0 | 0% | 10 |
| hangwin/mcp-chrome | 19 | Declining | stale | 0 | 0% | 7 |
| reading-plus-ai/mcp-server-data-exploration | 1 | Abandoned | stale | 0 | 0% | 0 |

⚠️ **Adopt with caution** (low health and/or declining): `reading-plus-ai/mcp-server-data-exploration`, `tadata-org/fastapi_mcp`, `hangwin/mcp-chrome`, `aipotheosis-labs/gate22`, `ravitemer/mcphub.nvim`, `Coding-Solo/godot-mcp`, `browserbase/mcp-server-browserbase`, `hustcc/mcp-mermaid`, `shaneholloman/mcp-knowledge-graph`.

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

<sub>Projects covered: 37 (23 servers) · Snapshot: 2026-07-13T08:42:30.177Z</sub>
