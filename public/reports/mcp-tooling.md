# MCP (Model Context Protocol) Tooling — Landscape Report

> Derived from **kaiser-data**'s 1,752 starred repos (snapshot `2026-08-28T01:21:50.535Z`), cross-referenced with the repo-similarity graph (1,752 nodes / 5,707 edges, 35 communities).
>
> Generated 2026-08-28 by `scripts/reports/mcp_tooling.py` (regenerate any time — no API cost).

![Top tools by stars](assets/mcp-tooling-top-tools.svg)

![Tools per category](assets/mcp-tooling-categories.svg)


> **What is MCP?** The Model Context Protocol is an open standard (Anthropic, late 2024) that lets LLM apps talk to external tools/data through a uniform interface — the 'USB-C port' for AI. **Servers** expose capabilities; **clients/hosts** (Claude Desktop, Cursor, editors) consume them; **gateways** govern them at scale.

## Executive summary

- **40 MCP projects** in your stars (**557,399★** combined) — spanning the whole stack: SDKs, clients, gateways, and **25 domain servers**.
- The architecture has three roles — and your stars cover all of them:
  - **Build** (SDKs/frameworks): `servers`, `fastmcp`, `typescript-sdk`, `fastapi_mcp`, `mcp-use`
  - **Consume** (clients/hosts): `inspector`, `witsy`, `mcphub.nvim`
  - **Govern** (gateways/control planes): `mcp-toolbox`, `klavis`, `open-connector`, `gate22`
- **Official vendor servers dominate the top** — GitHub, Microsoft (Playwright), Google (mcp-toolbox), Neo4j, Sentry, SonarSource all ship first-party MCP servers, a strong signal the protocol has crossed into mainstream adoption.
- TypeScript is the lingua franca of MCP servers; Python leads the SDK/framework layer (fastmcp, fastapi_mcp).

## The MCP stack at a glance

| Role | What it does | Tools in your stars |
|---|---|---|
| **SDK / framework** | Build servers/clients | `fastmcp`, `mcp-use`, `fastapi_mcp` |
| **Client / host** | Apps that consume servers | `mcphub.nvim`, `witsy` |
| **Gateway / control plane** | Route, secure & govern servers | `klavis`, `gate22`, `mcp-toolbox` |
| **Servers** | Expose a capability to agents | 25 across browser, DB, dev-tools, code-intel, docs, game engines |
| **Learning** | Lists & curricula | `awesome-mcp-servers` (×2), `mcp-for-beginners` |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Project | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Learning / reference | — | MIT | 92,895 (▲954) | Hot | 65 | very active | 0d ago | 1.7y | 19 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | SDK / framework | TypeScript | NOASSERTION | 89,915 (▲588) | Hot | 78 | very active | 8d ago | 1.8y | 13 |
| [upstash/context7](https://github.com/upstash/context7) | Server · code intelligence | TypeScript | MIT | 61,309 (▲913) | Hot | 79 | very active | 1d ago | 1.4y | 13 |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Server · browser/web | TypeScript | Apache-2.0 | 36,552 (▲657) | Mature | 76 | very active | 0d ago | 1.4y | 7 |
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | Server · dev-tooling | Go | MIT | 32,565 (▲530) | Hot | 78 | very active | 0d ago | 1.5y | 18 |
| [oraios/serena](https://github.com/oraios/serena) | Server · code intelligence | Python | MIT | 28,545 (▲826) | Hot | 78 | very active | 8d ago | 1.4y | 20 |
| [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | SDK / framework | Python | Apache-2.0 | 27,406 (▲303) | Hot | 84 | very active | 0d ago | 1.7y | 24 |
| [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | Server · dev-tooling | TypeScript | MIT | 22,798 (▲168) | Hot | 79 | very active | 0d ago | 1.2y | 5 |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | Server · code intelligence | TypeScript | NOASSERTION | 20,195 (▲501) | Rising | 78 | very active | 0d ago | 6mo | 1 |
| [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | Learning / reference | Jupyter Notebook | MIT | 17,095 (▲157) | Hot | 70 | very active | 1d ago | 1.4y | 6 |
| [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | Gateway / control plane | Go | Apache-2.0 | 16,268 (▲131) | Mature | 93 | very active | 0d ago | 2.2y | 31 |
| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | SDK / framework | TypeScript | NOASSERTION | 13,262 (▲167) | Hot | 76 | very active | 1d ago | 1.9y | 12 |
| [hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome) | Server · browser/web | TypeScript | MIT | 12,357 (▲87) | Declining | 15 | stale | 7mo ago | 1.2y | 0 |
| [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | SDK / framework | Python | MIT | 11,987 (▲10) | Declining | 11 | stale | 9mo ago | 1.5y | 0 |
| [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) | Client / host | TypeScript | — | 10,769 (▲154) | Mature | 80 | very active | 0d ago | 1.9y | 1 |
| [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) | SDK / framework | TypeScript | MIT | 10,531 (▲74) | Hot | 85 | very active | 0d ago | 1.4y | 8 |
| [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) | Server · game/platform | TypeScript | Apache-2.0 | 6,045 (▲210) | Hot | 71 | very active | 1d ago | 1.4y | 6 |
| [Klavis-AI/klavis](https://github.com/Klavis-AI/klavis) | Gateway / control plane | Python | Apache-2.0 | 5,795 (▲9) | Declining | 49 | slowing | 2mo ago | 1.4y | 1 |
| [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) | Server · game/platform | JavaScript | MIT | 5,400 (▲288) | Declining | 23 | slowing | 4mo ago | 1.5y | 0 |
| [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | Gateway / control plane | TypeScript | Apache-2.0 | 5,362 (▲937) | Hot | 89 | very active | 1d ago | 2mo | 21 |
| [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) | Learning / reference | — | MIT | 4,280 (▲28) | Mature | 44 | active | 1mo ago | 1.7y | 1 |
| [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx) | Server · code intelligence | Rust | Apache-2.0 | 3,662 (▲122) | Rising | 80 | very active | 2d ago | 5mo | 1 |
| [bytebase/dbhub](https://github.com/bytebase/dbhub) | Server · database/data | TypeScript | MIT | 3,417 (▲116) | Hot | 76 | very active | 7d ago | 1.5y | 10 |
| [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | Server · docs/research | Python | Apache-2.0 | 3,084 (▲55) | Hot | 77 | very active | 1d ago | 1.7y | 5 |
| [brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | Server · browser/web | JavaScript | MIT | 2,614 (▲48) | Mature | 67 | very active | 16d ago | 1.4y | 4 |
| [Kochava-Studios/witsy](https://github.com/Kochava-Studios/witsy) | Client / host | TypeScript | AGPL-3.0 | 2,024 (▲10) | Mature | 43 | slowing | 4mo ago | 2.3y | 0 |
| [hi-godot/godot-ai](https://github.com/hi-godot/godot-ai) | Server · game/platform | GDScript | MIT | 1,954 (▲466) | Hot | 80 | very active | 0d ago | 4mo | 12 |
| [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) | Server · game/platform | C# | MIT | 1,877 (▲18) | Hot | 61 | very active | 1d ago | 1.5y | 7 |
| [ravitemer/mcphub.nvim](https://github.com/ravitemer/mcphub.nvim) | Client / host | Lua | MIT | 1,783 | Declining | 20 | stale | 7mo ago | 1.5y | 0 |
| [shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) | Server · code intelligence | JavaScript | MIT | 886 (▲4) | Declining | 43 | slowing | 3mo ago | 1.7y | 0 |
| [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) | Server · dev-tooling | TypeScript | NOASSERTION | 830 (▲22) | Hot | 83 | very active | 0d ago | 1.4y | 23 |
| [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) | Server · dev-tooling | Java | NOASSERTION | 633 (▲16) | Hot | 76 | very active | 0d ago | 1.3y | 15 |
| [hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid) | Server · docs/research | TypeScript | MIT | 628 (▲7) | Declining | 41 | slowing | 3mo ago | 1.3y | 0 |
| [youichi-uda/godot-mcp-pro](https://github.com/youichi-uda/godot-mcp-pro) | Server · game/platform | GDScript | NOASSERTION | 580 (▲27) | Mature | 62 | active | 26d ago | 6mo | 2 |
| [reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) | Server · database/data | Python | MIT | 544 (▼1) | Abandoned | 1 | stale | 1.4y ago | 1.7y | 0 |
| [tugcantopaloglu/godot-mcp](https://github.com/tugcantopaloglu/godot-mcp) | Server · game/platform | JavaScript | MIT | 439 (▲49) | Rising | 52 | active | 1mo ago | 6mo | 2 |
| [VectifyAI/pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp) | Server · docs/research | TypeScript | MIT | 381 (▲3) | Mature | 63 | active | 1mo ago | 1.0y | 2 |
| [neo4j/mcp](https://github.com/neo4j/mcp) | Server · database/data | Go | NOASSERTION | 285 (▲7) | Hot | 71 | very active | 1d ago | 1.0y | 5 |
| [storybookjs/mcp](https://github.com/storybookjs/mcp) | Server · dev-tooling | TypeScript | MIT | 269 (▲4) | Hot | 74 | very active | 7d ago | 1.0y | 8 |
| [aipotheosis-labs/gate22](https://github.com/aipotheosis-labs/gate22) | Gateway / control plane | TypeScript | Apache-2.0 | 178 (▲3) | Declining | 24 | stale | 8mo ago | 1.0y | 0 |

## By category

### SDK / framework

_The layer you reach for to *author* an MCP server or client._

- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 89,915★ · TypeScript · Hot  
  Official reference-server monorepo — canonical examples for filesystem, git, fetch, etc.  
  <sub>topics: —</sub>
- **[PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)** · 27,406★ · Python · Hot  
  The fast, Pythonic way to build MCP servers & clients; the de-facto Python framework.  
  <sub>topics: model-context-protocol, fastmcp, mcp, agents, llms, mcp-clients, mcp-servers, mcp-tools</sub>
- **[modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** · 13,262★ · TypeScript · Hot  
  Official TypeScript SDK for building MCP servers & clients.  
  <sub>topics: typescript, mcp, mcp-server, mcp-client</sub>
- **[tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** · 11,987★ · Python · Declining  
  Expose existing FastAPI endpoints as MCP tools, with auth — zero-rewrite server creation.  
  <sub>topics: ai, claude, cursor, fastapi, llm, mcp, mcp-server, mcp-servers</sub>
- **[mcp-use/mcp-use](https://github.com/mcp-use/mcp-use)** · 10,531★ · TypeScript · Hot  
  Fullstack MCP framework — build MCP apps for ChatGPT/Claude and MCP servers for agents.  
  <sub>topics: mcp, model-context-protocol, apps-sdk, mcp-apps, mcp-inspector, mcp-servers, mcp-ui, agentic-framework</sub>

### Client / host

_Apps/editors that connect to servers and surface their tools to the user._

- **[modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)** · 10,769★ · TypeScript · Mature  
  Official visual debugger/inspector for testing MCP servers.  
  <sub>topics: tool, debug, mcp, cli, tui, web</sub>
- **[Kochava-Studios/witsy](https://github.com/Kochava-Studios/witsy)** · 2,024★ · TypeScript · Mature  
  Desktop AI assistant doubling as a universal MCP client.  
  <sub>topics: anthropic, genai, groq, ollama, ollama-gui, openai, electron-app, electronjs</sub>
- **[ravitemer/mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** · 1,783★ · Lua · Declining  
  MCP client for Neovim — integrates MCP servers into the editing workflow.  
  <sub>topics: avante, chatgpt, chatplugin, claude-ai, llm, mcp, mcp-client, mcp-hub</sub>

### Gateway / control plane

_Front many servers behind one endpoint; add auth, routing, and policy — the enterprise-readiness layer._

- **[googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox)** · 16,268★ · Go · Mature  
  Google's open MCP server for databases — one gateway fronting many DBs.  
  <sub>topics: genai, mcp, agent, ai, database, llm, server, agents</sub>
- **[Klavis-AI/klavis](https://github.com/Klavis-AI/klavis)** · 5,795★ · Python · Declining  
  MCP integration platform so agents use tools reliably at scale.  
  <sub>topics: ai, discord, llm, mcp, mcp-client, mcp-server, open-source, agents</sub>
- **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** · 5,362★ · TypeScript · Hot  
  Open-source auth gateway connecting 1000+ SaaS providers to agents via MCP, SDK & HTTP.  
  <sub>topics: agent-tools, ai-agents, api-gateway, automation, cli, cloudflare-workers, connectors, integration-platform</sub>
- **[aipotheosis-labs/gate22](https://github.com/aipotheosis-labs/gate22)** · 178★ · TypeScript · Declining  
  Open-source MCP gateway & control plane to govern which tools agents may use.  
  <sub>topics: agents, ai, ai-agents, control-plane, gateway, guardrails, llm, mcp</sub>

### Server · browser/web

_Give agents a browser or the open web._

- **[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)** · 36,552★ · TypeScript · Mature  
  Microsoft's Playwright MCP server — drive a real browser from an agent.  
  <sub>topics: mcp, playwright</sub>
- **[hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome)** · 12,357★ · TypeScript · Declining  
  Chrome-extension-based MCP server exposing the user's actual browser.  
  <sub>topics: —</sub>
- **[brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** · 2,614★ · JavaScript · Mature  
  All-in-one MCP server for public web data access / scraping at scale.  
  <sub>topics: llm, mcp, modelcontextprotocol, scraping, ai-agents, ai-integrations, anti-bot-detection, browser-automation</sub>

### Server · database/data

_Expose databases and datasets as agent-queryable tools._

- **[bytebase/dbhub](https://github.com/bytebase/dbhub)** · 3,417★ · TypeScript · Hot  
  Zero-dependency, token-efficient database MCP server (Postgres, MySQL, SQL Server, …).  
  <sub>topics: ai, anthropic, claude, database, mcp, mcp-server, claude-ai, mysql</sub>
- **[reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** · 544★ · Python · Abandoned  
  MCP server for interactive data exploration.  
  <sub>topics: —</sub>
- **[neo4j/mcp](https://github.com/neo4j/mcp)** · 285★ · Go · Hot  
  Neo4j's official MCP server for graph-database access.  
  <sub>topics: —</sub>

### Server · dev-tooling

_Wire agents into the software-delivery toolchain (VCS, CI, quality, errors)._

- **[github/github-mcp-server](https://github.com/github/github-mcp-server)** · 32,565★ · Go · Hot  
  GitHub's official MCP server — issues, PRs, repos as agent tools.  
  <sub>topics: github, mcp, mcp-server</sub>
- **[czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** · 22,798★ · TypeScript · Hot  
  MCP server that helps agents build n8n workflows.  
  <sub>topics: mcp, mcp-server, n8n, workflows</sub>
- **[getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp)** · 830★ · TypeScript · Hot  
  Interact with Sentry (errors/issues) via LLMs.  
  <sub>topics: mcp-server, tag-production</sub>
- **[SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** · 633★ · Java · Hot  
  Official SonarQube MCP server — code quality & security in agents.  
  <sub>topics: agent, ai, mcp, mcp-server, sonarqube, code-quality, security, static-analysis</sub>
- **[storybookjs/mcp](https://github.com/storybookjs/mcp)** · 269★ · TypeScript · Hot  
  Storybook's MCP server for component-driven workflows.  
  <sub>topics: —</sub>

### Server · code intelligence

_Feed agents accurate code/library context — the antidote to hallucinated APIs._

- **[upstash/context7](https://github.com/upstash/context7)** · 61,309★ · TypeScript · Hot  
  Up-to-date library docs piped to LLMs/editors via MCP — kills version drift.  
  <sub>topics: llm, mcp, mcp-server, vibe-coding</sub>
- **[oraios/serena](https://github.com/oraios/serena)** · 28,545★ · Python · Hot  
  Powerful MCP coding toolkit — semantic retrieval & editing (LSP-backed).  
  <sub>topics: agent, ai, vibe-coding, mcp-server, ai-coding, language-server, programming, claude</sub>
- **[mksglu/context-mode](https://github.com/mksglu/context-mode)** · 20,195★ · TypeScript · Rising  
  Context-window optimization for coding agents; sandboxes tool output (~98% reduction).  
  <sub>topics: claude, claude-code, claude-code-plugins, mcp, skills, codex, copilot, opencode</sub>
- **[yvgude/lean-ctx](https://github.com/yvgude/lean-ctx)** · 3,662★ · Rust · Rising  
  Cognitive context layer — 51+ MCP tools, multiple read modes for agentic systems.  
  <sub>topics: ai, cursor, llm, mcp, rust, token-optimization, agentic-coding, claude-code</sub>
- **[shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** · 886★ · JavaScript · Declining  
  Persistent memory for Claude via a local knowledge graph (also in the memory report).  
  <sub>topics: ai-memory, claude-ai, knowledge-graph, mcp, memory-server, typescript</sub>

### Server · docs/research

_Documents, papers, and diagram generation._

- **[blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** · 3,084★ · Python · Hot  
  Search & analyze arXiv papers through MCP.  
  <sub>topics: ai, claude-ai, gpt, mcp-server, arxiv, papers, research, llm</sub>
- **[hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** · 628★ · TypeScript · Declining  
  Generate Mermaid diagrams/charts dynamically via MCP.  
  <sub>topics: mcp, mcp-server, mermaid, mermaidjs</sub>
- **[VectifyAI/pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp)** · 381★ · TypeScript · Mature  
  MCP front-end to PageIndex's vectorless reasoning-based RAG.  
  <sub>topics: —</sub>

### Server · game/platform

_Drive game engines and mobile/desktop platforms._

- **[mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp)** · 6,045★ · TypeScript · Hot  
  MCP server for mobile automation/scraping (iOS, Android, emulators).  
  <sub>topics: android, ios, mcp, mobile, agent, emulator, physical, real</sub>
- **[Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp)** · 5,400★ · JavaScript · Declining  
  MCP server to drive the Godot game engine (launch editor, run scenes).  
  <sub>topics: ai, godot, mcp</sub>
- **[hi-godot/godot-ai](https://github.com/hi-godot/godot-ai)** · 1,954★ · GDScript · Hot  
  Production-grade MCP server and AI tools for the Godot engine.  
  <sub>topics: ai, game-development, godot, godot-plugin, mcp</sub>
- **[CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity)** · 1,877★ · C# · Hot  
  MCP plugin connecting agents (Cursor/Claude) to the Unity editor.  
  <sub>topics: cursor, unity, unity-package, mcp, copilot, game-development, model-context-protocol, openai</sub>
- **[youichi-uda/godot-mcp-pro](https://github.com/youichi-uda/godot-mcp-pro)** · 580★ · GDScript · Mature  
  162 MCP tools for AI-powered Godot 4 development — scene, animation, 3D, physics.  
  <sub>topics: ai, claude, cursor, game-development, godot, godot-engine, mcp, model-context-protocol</sub>
- **[tugcantopaloglu/godot-mcp](https://github.com/tugcantopaloglu/godot-mcp)** · 439★ · JavaScript · Rising  
  Full Godot 4.x engine control via MCP: 157 tools for AI-driven game development.  
  <sub>topics: game-development, gdscript, godot, mcp, model-context-protocol, ai, automation, godot-engine</sub>

### Learning / reference

_Where the ecosystem is catalogued and taught._

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 92,895★ · — · Hot  
  The flagship awesome-list of MCP servers (88k★).  
  <sub>topics: ai, mcp</sub>
- **[microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** · 17,095★ · Jupyter Notebook · Hot  
  Microsoft's open curriculum teaching MCP fundamentals.  
  <sub>topics: csharp, java, javascript, mcp, mcp-client, mcp-security, mcp-server, model</sub>
- **[wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** · 4,280★ · — · Mature  
  Curated list of MCP servers.  
  <sub>topics: —</sub>

## Spotlight: official vendor servers

A maturity signal — major vendors shipping **first-party** MCP servers in your stars:

- **Upstash** — [upstash/context7](https://github.com/upstash/context7) · 61,309★ · health 79
- **Microsoft** — [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) · 36,552★ · health 76
- **GitHub** — [github/github-mcp-server](https://github.com/github/github-mcp-server) · 32,565★ · health 78
- **Microsoft (edu)** — [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) · 17,095★ · health 70
- **Google** — [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) · 16,268★ · health 93
- **Sentry** — [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) · 830★ · health 83
- **SonarSource** — [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) · 633★ · health 76
- **Neo4j** — [neo4j/mcp](https://github.com/neo4j/mcp) · 285★ · health 71
- **Storybook** — [storybookjs/mcp](https://github.com/storybookjs/mcp) · 269★ · health 74

## Graph analysis — how they relate

**Community clustering.** These 40 projects span **12 of the graph's 35 communities** — MCP tooling is woven through the whole agent-infra landscape rather than sitting in one bucket.

- **Community 26** (16): `tadata-org/fastapi_mcp`, `brightdata/brightdata-mcp`, `github/github-mcp-server`, `getsentry/sentry-mcp`, `upstash/context7`, `shaneholloman/mcp-knowledge-graph`, `modelcontextprotocol/servers`, `modelcontextprotocol/typescript-sdk`, `modelcontextprotocol/inspector`, `hustcc/mcp-mermaid`, `Coding-Solo/godot-mcp`, `hi-godot/godot-ai`, `youichi-uda/godot-mcp-pro`, `tugcantopaloglu/godot-mcp`, `CoderGamester/mcp-unity`, `punkpeye/awesome-mcp-servers`
- **Community 11** (5): `mcp-use/mcp-use`, `ravitemer/mcphub.nvim`, `oomol-lab/open-connector`, `mksglu/context-mode`, `blazickjp/arxiv-mcp-server`
- **Community 6** (4): `PrefectHQ/fastmcp`, `Klavis-AI/klavis`, `aipotheosis-labs/gate22`, `oraios/serena`
- **Community 10** (4): `Kochava-Studios/witsy`, `googleapis/mcp-toolbox`, `bytebase/dbhub`, `neo4j/mcp`
- **Community 15** (3): `microsoft/playwright-mcp`, `czlonkowski/n8n-mcp`, `microsoft/mcp-for-beginners`
- **Community 4** (2): `hangwin/mcp-chrome`, `storybookjs/mcp`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' MCP projects in your ecosystem:

- `mksglu/context-mode` — PageRank 0.0057
- `modelcontextprotocol/typescript-sdk` — PageRank 0.0027
- `microsoft/mcp-for-beginners` — PageRank 0.0022
- `github/github-mcp-server` — PageRank 0.0011
- `punkpeye/awesome-mcp-servers` — PageRank 0.0010
- `Coding-Solo/godot-mcp` — PageRank 0.0010
- `blazickjp/arxiv-mcp-server` — PageRank 0.0010
- `czlonkowski/n8n-mcp` — PageRank 0.0009
- `microsoft/playwright-mcp` — PageRank 0.0009
- `SonarSource/sonarqube-mcp-server` — PageRank 0.0009

**Direct links between MCP projects** (top similarity edges where both endpoints are in this report):

- `microsoft/playwright-mcp` ⇄ `microsoft/mcp-for-beginners` (w=0.733) — topics: mcp; authors: dependabot[bot]
- `modelcontextprotocol/inspector` ⇄ `modelcontextprotocol/servers` (w=0.704) — authors: cliffhall
- `Coding-Solo/godot-mcp` ⇄ `punkpeye/awesome-mcp-servers` (w=0.667) — topics: ai, mcp
- `modelcontextprotocol/typescript-sdk` ⇄ `modelcontextprotocol/inspector` (w=0.661) — topics: mcp
- `modelcontextprotocol/typescript-sdk` ⇄ `modelcontextprotocol/servers` (w=0.633) — authors: dependabot[bot]
- `hi-godot/godot-ai` ⇄ `Coding-Solo/godot-mcp` (w=0.600) — topics: ai, godot, mcp
- `microsoft/mcp-for-beginners` ⇄ `czlonkowski/n8n-mcp` (w=0.569) — topics: mcp, mcp-server; authors: dependabot[bot], Copilot
- `modelcontextprotocol/typescript-sdk` ⇄ `upstash/context7` (w=0.557) — topics: mcp, mcp-server; authors: github-actions[bot], KKonstantinov
- `modelcontextprotocol/typescript-sdk` ⇄ `czlonkowski/n8n-mcp` (w=0.508) — topics: mcp, mcp-server; authors: dependabot[bot]
- `github/github-mcp-server` ⇄ `upstash/context7` (w=0.467) — topics: mcp, mcp-server; authors: github-actions[bot]
- `mksglu/context-mode` ⇄ `mcp-use/mcp-use` (w=0.443) — topics: claude-code, mcp, skills, mcp-server; authors: github-actions[bot]
- `youichi-uda/godot-mcp-pro` ⇄ `hi-godot/godot-ai` (w=0.435) — topics: ai, game-development, godot, mcp
- `hi-godot/godot-ai` ⇄ `punkpeye/awesome-mcp-servers` (w=0.400) — topics: ai, mcp
- `hustcc/mcp-mermaid` ⇄ `github/github-mcp-server` (w=0.400) — topics: mcp, mcp-server
- `youichi-uda/godot-mcp-pro` ⇄ `tugcantopaloglu/godot-mcp` (w=0.389) — topics: ai, game-development, godot, godot-engine
- …and 19 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). MCP servers are often weekend projects — check this before wiring one into production agents.

| Project | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| googleapis/mcp-toolbox | 93 | Mature | very active | 4 | 17% | 49 |
| oomol-lab/open-connector | 89 | Hot | very active | 3 | 23% | 13 |
| mcp-use/mcp-use | 85 | Hot | very active | 2 | 34% | 1361 |
| PrefectHQ/fastmcp | 84 | Hot | very active | 2 | 45% | 115 |
| getsentry/sentry-mcp | 83 | Hot | very active | 2 | 34% | 43 |
| yvgude/lean-ctx | 80 | Rising | very active | 1 | 100% | 246 |
| modelcontextprotocol/inspector | 80 | Mature | very active | 1 | 100% | 62 |
| hi-godot/godot-ai | 80 | Hot | very active | 1 | 57% | 101 |
| czlonkowski/n8n-mcp | 79 | Hot | very active | 1 | 83% | 266 |
| upstash/context7 | 79 | Hot | very active | 1 | 53% | 107 |
| github/github-mcp-server | 78 | Hot | very active | 1 | 55% | 77 |
| oraios/serena | 78 | Hot | very active | 1 | 60% | 16 |
| mksglu/context-mode | 78 | Rising | very active | 1 | 100% | 195 |
| modelcontextprotocol/servers | 78 | Hot | very active | 2 | 31% | 27 |
| blazickjp/arxiv-mcp-server | 77 | Hot | very active | 1 | 94% | 10 |
| microsoft/playwright-mcp | 76 | Mature | very active | 2 | 43% | 69 |
| bytebase/dbhub | 76 | Hot | very active | 1 | 88% | 7 |
| SonarSource/sonarqube-mcp-server | 76 | Hot | very active | 2 | 31% | 37 |
| modelcontextprotocol/typescript-sdk | 76 | Hot | very active | 1 | 65% | 159 |
| storybookjs/mcp | 74 | Hot | very active | 1 | 73% | 55 |
| neo4j/mcp | 71 | Hot | very active | 1 | 56% | 28 |
| mobile-next/mobile-mcp | 71 | Hot | very active | 1 | 86% | 52 |
| microsoft/mcp-for-beginners | 70 | Hot | very active | 2 | 35% | 0 |
| brightdata/brightdata-mcp | 67 | Mature | very active | 1 | 52% | 12 |
| punkpeye/awesome-mcp-servers | 65 | Hot | very active | 1 | 74% | 0 |
| VectifyAI/pageindex-mcp | 63 | Mature | active | 1 | 83% | 20 |
| youichi-uda/godot-mcp-pro | 62 | Mature | active | 1 | 75% | 19 |
| CoderGamester/mcp-unity | 61 | Hot | very active | 1 | 73% | 9 |
| tugcantopaloglu/godot-mcp | 52 | Rising | active | 1 | 91% | 3 |
| Klavis-AI/klavis | 49 | Declining | slowing | 1 | 100% | 79 |
| wong2/awesome-mcp-servers | 44 | Mature | active | 1 | 100% | 0 |
| Kochava-Studios/witsy | 43 | Mature | slowing | 0 | 0% | 173 |
| shaneholloman/mcp-knowledge-graph | 43 | Declining | slowing | 0 | 0% | 8 |
| hustcc/mcp-mermaid | 41 | Declining | slowing | 0 | 0% | 6 |
| aipotheosis-labs/gate22 | 24 | Declining | stale | 0 | 0% | 8 |
| Coding-Solo/godot-mcp | 23 | Declining | slowing | 0 | 0% | 0 |
| ravitemer/mcphub.nvim | 20 | Declining | stale | 0 | 0% | 59 |
| hangwin/mcp-chrome | 15 | Declining | stale | 0 | 0% | 7 |
| tadata-org/fastapi_mcp | 11 | Declining | stale | 0 | 0% | 10 |
| reading-plus-ai/mcp-server-data-exploration | 1 | Abandoned | stale | 0 | 0% | 0 |

⚠️ **Adopt with caution** (low health and/or declining): `reading-plus-ai/mcp-server-data-exploration`, `tadata-org/fastapi_mcp`, `hangwin/mcp-chrome`, `ravitemer/mcphub.nvim`, `Coding-Solo/godot-mcp`, `aipotheosis-labs/gate22`, `hustcc/mcp-mermaid`, `Kochava-Studios/witsy`, `shaneholloman/mcp-knowledge-graph`, `wong2/awesome-mcp-servers`, `Klavis-AI/klavis`.

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

<sub>Projects covered: 40 (25 servers) · Snapshot: 2026-08-28T01:21:50.535Z</sub>
