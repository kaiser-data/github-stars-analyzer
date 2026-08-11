# MCP (Model Context Protocol) Tooling — Landscape Report

> Derived from **kaiser-data**'s 1,596 starred repos (snapshot `2026-08-11T18:59:16.380Z`), cross-referenced with the repo-similarity graph (1,596 nodes / 5,170 edges, 31 communities).
>
> Generated 2026-08-11 by `scripts/reports/mcp_tooling.py` (regenerate any time — no API cost).

![Top tools by stars](assets/mcp-tooling-top-tools.svg)

![Tools per category](assets/mcp-tooling-categories.svg)


> **What is MCP?** The Model Context Protocol is an open standard (Anthropic, late 2024) that lets LLM apps talk to external tools/data through a uniform interface — the 'USB-C port' for AI. **Servers** expose capabilities; **clients/hosts** (Claude Desktop, Cursor, editors) consume them; **gateways** govern them at scale.

## Executive summary

- **40 MCP projects** in your stars (**548,731★** combined) — spanning the whole stack: SDKs, clients, gateways, and **25 domain servers**.
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
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Learning / reference | — | MIT | 91,941 | Hot | 64 | very active | 9d ago | 1.7y | 16 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | SDK / framework | TypeScript | NOASSERTION | 89,327 | Hot | 82 | very active | 6d ago | 1.7y | 15 |
| [upstash/context7](https://github.com/upstash/context7) | Server · code intelligence | TypeScript | MIT | 60,396 | Hot | 83 | very active | 4d ago | 1.4y | 18 |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Server · browser/web | TypeScript | Apache-2.0 | 35,895 | Mature | 76 | very active | 4d ago | 1.4y | 6 |
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | Server · dev-tooling | Go | MIT | 32,035 | Hot | 88 | very active | 4d ago | 1.4y | 29 |
| [oraios/serena](https://github.com/oraios/serena) | Server · code intelligence | Python | MIT | 27,719 | Hot | 79 | very active | 6d ago | 1.4y | 14 |
| [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | SDK / framework | Python | Apache-2.0 | 27,103 | Hot | 78 | very active | 4d ago | 1.7y | 16 |
| [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | Server · dev-tooling | TypeScript | MIT | 22,630 | Hot | 79 | very active | 4d ago | 1.2y | 9 |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | Server · code intelligence | TypeScript | NOASSERTION | 19,694 | Rising | 78 | very active | 4d ago | 5mo | 2 |
| [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | Learning / reference | Jupyter Notebook | MIT | 16,938 | Hot | 69 | very active | 6d ago | 1.4y | 6 |
| [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | Gateway / control plane | Go | Apache-2.0 | 16,137 | Mature | 93 | very active | 4d ago | 2.2y | 27 |
| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | SDK / framework | TypeScript | NOASSERTION | 13,095 | Hot | 75 | very active | 5d ago | 1.9y | 9 |
| [hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome) | Server · browser/web | TypeScript | MIT | 12,270 | Declining | 17 | stale | 7mo ago | 1.2y | 0 |
| [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | SDK / framework | Python | MIT | 11,977 | Declining | 13 | stale | 8mo ago | 1.4y | 0 |
| [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) | Client / host | TypeScript | — | 10,615 | Hot | 79 | very active | 4d ago | 1.9y | 3 |
| [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) | SDK / framework | TypeScript | MIT | 10,457 | Hot | 84 | very active | 4d ago | 1.4y | 5 |
| [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) | Server · game/platform | TypeScript | Apache-2.0 | 5,835 | Hot | 71 | very active | 5d ago | 1.4y | 5 |
| [Klavis-AI/klavis](https://github.com/Klavis-AI/klavis) | Gateway / control plane | Python | Apache-2.0 | 5,786 | Declining | 52 | slowing | 2mo ago | 1.3y | 1 |
| [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) | Server · game/platform | JavaScript | MIT | 5,112 | Declining | 25 | slowing | 3mo ago | 1.5y | 0 |
| [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | Gateway / control plane | TypeScript | Apache-2.0 | 4,425 | Hot | 99 | very active | 4d ago | 1mo | 29 |
| [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) | Learning / reference | — | MIT | 4,252 | Mature | 46 | active | 29d ago | 1.7y | 1 |
| [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx) | Server · code intelligence | Rust | Apache-2.0 | 3,540 | Hot | 79 | very active | 4d ago | 4mo | 3 |
| [bytebase/dbhub](https://github.com/bytebase/dbhub) | Server · database/data | TypeScript | MIT | 3,301 | Hot | 74 | very active | 6d ago | 1.4y | 7 |
| [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | Server · docs/research | Python | Apache-2.0 | 3,029 | Mature | 66 | very active | 14d ago | 1.7y | 6 |
| [brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | Server · browser/web | JavaScript | MIT | 2,566 | Mature | 68 | very active | 15d ago | 1.3y | 3 |
| [Kochava-Studios/witsy](https://github.com/Kochava-Studios/witsy) | Client / host | TypeScript | AGPL-3.0 | 2,014 | Mature | 45 | slowing | 3mo ago | 2.3y | 0 |
| [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) | Server · game/platform | C# | MIT | 1,859 | Hot | 63 | very active | 7d ago | 1.4y | 8 |
| [ravitemer/mcphub.nvim](https://github.com/ravitemer/mcphub.nvim) | Client / host | Lua | MIT | 1,783 | Declining | 22 | stale | 6mo ago | 1.5y | 0 |
| [hi-godot/godot-ai](https://github.com/hi-godot/godot-ai) | Server · game/platform | GDScript | MIT | 1,488 | Hot | 79 | very active | 4d ago | 4mo | 11 |
| [shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) | Server · code intelligence | JavaScript | MIT | 882 | Declining | 57 | slowing | 2mo ago | 1.7y | 1 |
| [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) | Server · dev-tooling | TypeScript | NOASSERTION | 808 | Hot | 82 | very active | 4d ago | 1.4y | 16 |
| [hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid) | Server · docs/research | TypeScript | MIT | 621 | Declining | 49 | slowing | 2mo ago | 1.2y | 1 |
| [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) | Server · dev-tooling | Java | NOASSERTION | 617 | Hot | 76 | very active | 5d ago | 1.3y | 17 |
| [youichi-uda/godot-mcp-pro](https://github.com/youichi-uda/godot-mcp-pro) | Server · game/platform | GDScript | NOASSERTION | 553 | Rising | 68 | very active | 10d ago | 5mo | 2 |
| [reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) | Server · database/data | Python | MIT | 545 | Abandoned | 1 | stale | 1.4y ago | 1.7y | 0 |
| [tugcantopaloglu/godot-mcp](https://github.com/tugcantopaloglu/godot-mcp) | Server · game/platform | JavaScript | MIT | 390 | Rising | 53 | active | 29d ago | 6mo | 2 |
| [VectifyAI/pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp) | Server · docs/research | TypeScript | MIT | 378 | Rising | 68 | active | 17d ago | 11mo | 2 |
| [neo4j/mcp](https://github.com/neo4j/mcp) | Server · database/data | Go | NOASSERTION | 278 | Hot | 75 | very active | 11d ago | 11mo | 5 |
| [storybookjs/mcp](https://github.com/storybookjs/mcp) | Server · dev-tooling | TypeScript | MIT | 265 | Hot | 74 | very active | 4d ago | 11mo | 8 |
| [aipotheosis-labs/gate22](https://github.com/aipotheosis-labs/gate22) | Gateway / control plane | TypeScript | Apache-2.0 | 175 | Declining | 26 | stale | 8mo ago | 11mo | 0 |

## By category

### SDK / framework

_The layer you reach for to *author* an MCP server or client._

- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 89,327★ · TypeScript · Hot  
  Official reference-server monorepo — canonical examples for filesystem, git, fetch, etc.  
  <sub>topics: —</sub>
- **[PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)** · 27,103★ · Python · Hot  
  The fast, Pythonic way to build MCP servers & clients; the de-facto Python framework.  
  <sub>topics: model-context-protocol, fastmcp, mcp, agents, llms, mcp-clients, mcp-servers, mcp-tools</sub>
- **[modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** · 13,095★ · TypeScript · Hot  
  Official TypeScript SDK for building MCP servers & clients.  
  <sub>topics: typescript, mcp, mcp-server, mcp-client</sub>
- **[tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** · 11,977★ · Python · Declining  
  Expose existing FastAPI endpoints as MCP tools, with auth — zero-rewrite server creation.  
  <sub>topics: ai, claude, cursor, fastapi, llm, mcp, mcp-server, mcp-servers</sub>
- **[mcp-use/mcp-use](https://github.com/mcp-use/mcp-use)** · 10,457★ · TypeScript · Hot  
  Fullstack MCP framework — build MCP apps for ChatGPT/Claude and MCP servers for agents.  
  <sub>topics: mcp, model-context-protocol, apps-sdk, mcp-apps, mcp-inspector, mcp-servers, mcp-ui, agentic-framework</sub>

### Client / host

_Apps/editors that connect to servers and surface their tools to the user._

- **[modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)** · 10,615★ · TypeScript · Hot  
  Official visual debugger/inspector for testing MCP servers.  
  <sub>topics: tool, debug, mcp</sub>
- **[Kochava-Studios/witsy](https://github.com/Kochava-Studios/witsy)** · 2,014★ · TypeScript · Mature  
  Desktop AI assistant doubling as a universal MCP client.  
  <sub>topics: anthropic, genai, groq, ollama, ollama-gui, openai, electron-app, electronjs</sub>
- **[ravitemer/mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** · 1,783★ · Lua · Declining  
  MCP client for Neovim — integrates MCP servers into the editing workflow.  
  <sub>topics: avante, chatgpt, chatplugin, claude-ai, llm, mcp, mcp-client, mcp-hub</sub>

### Gateway / control plane

_Front many servers behind one endpoint; add auth, routing, and policy — the enterprise-readiness layer._

- **[googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox)** · 16,137★ · Go · Mature  
  Google's open MCP server for databases — one gateway fronting many DBs.  
  <sub>topics: genai, mcp, agent, ai, database, llm, server, agents</sub>
- **[Klavis-AI/klavis](https://github.com/Klavis-AI/klavis)** · 5,786★ · Python · Declining  
  MCP integration platform so agents use tools reliably at scale.  
  <sub>topics: ai, discord, llm, mcp, mcp-client, mcp-server, open-source, agents</sub>
- **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** · 4,425★ · TypeScript · Hot  
  Open-source auth gateway connecting 1000+ SaaS providers to agents via MCP, SDK & HTTP.  
  <sub>topics: agent-tools, ai-agents, api-gateway, automation, cli, cloudflare-workers, connectors, integration-platform</sub>
- **[aipotheosis-labs/gate22](https://github.com/aipotheosis-labs/gate22)** · 175★ · TypeScript · Declining  
  Open-source MCP gateway & control plane to govern which tools agents may use.  
  <sub>topics: agents, ai, ai-agents, control-plane, gateway, guardrails, llm, mcp</sub>

### Server · browser/web

_Give agents a browser or the open web._

- **[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)** · 35,895★ · TypeScript · Mature  
  Microsoft's Playwright MCP server — drive a real browser from an agent.  
  <sub>topics: mcp, playwright</sub>
- **[hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome)** · 12,270★ · TypeScript · Declining  
  Chrome-extension-based MCP server exposing the user's actual browser.  
  <sub>topics: —</sub>
- **[brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** · 2,566★ · JavaScript · Mature  
  All-in-one MCP server for public web data access / scraping at scale.  
  <sub>topics: llm, mcp, modelcontextprotocol, scraping, ai-agents, ai-integrations, anti-bot-detection, browser-automation</sub>

### Server · database/data

_Expose databases and datasets as agent-queryable tools._

- **[bytebase/dbhub](https://github.com/bytebase/dbhub)** · 3,301★ · TypeScript · Hot  
  Zero-dependency, token-efficient database MCP server (Postgres, MySQL, SQL Server, …).  
  <sub>topics: ai, anthropic, claude, database, mcp, mcp-server, claude-ai, mysql</sub>
- **[reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** · 545★ · Python · Abandoned  
  MCP server for interactive data exploration.  
  <sub>topics: —</sub>
- **[neo4j/mcp](https://github.com/neo4j/mcp)** · 278★ · Go · Hot  
  Neo4j's official MCP server for graph-database access.  
  <sub>topics: —</sub>

### Server · dev-tooling

_Wire agents into the software-delivery toolchain (VCS, CI, quality, errors)._

- **[github/github-mcp-server](https://github.com/github/github-mcp-server)** · 32,035★ · Go · Hot  
  GitHub's official MCP server — issues, PRs, repos as agent tools.  
  <sub>topics: github, mcp, mcp-server</sub>
- **[czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** · 22,630★ · TypeScript · Hot  
  MCP server that helps agents build n8n workflows.  
  <sub>topics: mcp, mcp-server, n8n, workflows</sub>
- **[getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp)** · 808★ · TypeScript · Hot  
  Interact with Sentry (errors/issues) via LLMs.  
  <sub>topics: mcp-server, tag-production</sub>
- **[SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** · 617★ · Java · Hot  
  Official SonarQube MCP server — code quality & security in agents.  
  <sub>topics: agent, ai, mcp, mcp-server, sonarqube, code-quality, security, static-analysis</sub>
- **[storybookjs/mcp](https://github.com/storybookjs/mcp)** · 265★ · TypeScript · Hot  
  Storybook's MCP server for component-driven workflows.  
  <sub>topics: —</sub>

### Server · code intelligence

_Feed agents accurate code/library context — the antidote to hallucinated APIs._

- **[upstash/context7](https://github.com/upstash/context7)** · 60,396★ · TypeScript · Hot  
  Up-to-date library docs piped to LLMs/editors via MCP — kills version drift.  
  <sub>topics: llm, mcp, mcp-server, vibe-coding</sub>
- **[oraios/serena](https://github.com/oraios/serena)** · 27,719★ · Python · Hot  
  Powerful MCP coding toolkit — semantic retrieval & editing (LSP-backed).  
  <sub>topics: agent, ai, vibe-coding, mcp-server, ai-coding, language-server, programming, claude</sub>
- **[mksglu/context-mode](https://github.com/mksglu/context-mode)** · 19,694★ · TypeScript · Rising  
  Context-window optimization for coding agents; sandboxes tool output (~98% reduction).  
  <sub>topics: claude, claude-code, claude-code-plugins, mcp, skills, codex, copilot, opencode</sub>
- **[yvgude/lean-ctx](https://github.com/yvgude/lean-ctx)** · 3,540★ · Rust · Hot  
  Cognitive context layer — 51+ MCP tools, multiple read modes for agentic systems.  
  <sub>topics: ai, cursor, llm, mcp, rust, token-optimization, agentic-coding, claude-code</sub>
- **[shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** · 882★ · JavaScript · Declining  
  Persistent memory for Claude via a local knowledge graph (also in the memory report).  
  <sub>topics: ai-memory, claude-ai, knowledge-graph, mcp, memory-server, typescript</sub>

### Server · docs/research

_Documents, papers, and diagram generation._

- **[blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** · 3,029★ · Python · Mature  
  Search & analyze arXiv papers through MCP.  
  <sub>topics: ai, claude-ai, gpt, mcp-server, arxiv, papers, research, llm</sub>
- **[hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** · 621★ · TypeScript · Declining  
  Generate Mermaid diagrams/charts dynamically via MCP.  
  <sub>topics: mcp, mcp-server, mermaid, mermaidjs</sub>
- **[VectifyAI/pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp)** · 378★ · TypeScript · Rising  
  MCP front-end to PageIndex's vectorless reasoning-based RAG.  
  <sub>topics: —</sub>

### Server · game/platform

_Drive game engines and mobile/desktop platforms._

- **[mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp)** · 5,835★ · TypeScript · Hot  
  MCP server for mobile automation/scraping (iOS, Android, emulators).  
  <sub>topics: android, ios, mcp, mobile, agent, emulator, physical, real</sub>
- **[Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp)** · 5,112★ · JavaScript · Declining  
  MCP server to drive the Godot game engine (launch editor, run scenes).  
  <sub>topics: ai, godot, mcp</sub>
- **[CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity)** · 1,859★ · C# · Hot  
  MCP plugin connecting agents (Cursor/Claude) to the Unity editor.  
  <sub>topics: cursor, unity, unity-package, mcp, copilot, game-development, model-context-protocol, openai</sub>
- **[hi-godot/godot-ai](https://github.com/hi-godot/godot-ai)** · 1,488★ · GDScript · Hot  
  Production-grade MCP server and AI tools for the Godot engine.  
  <sub>topics: ai, game-development, godot, godot-plugin, mcp</sub>
- **[youichi-uda/godot-mcp-pro](https://github.com/youichi-uda/godot-mcp-pro)** · 553★ · GDScript · Rising  
  162 MCP tools for AI-powered Godot 4 development — scene, animation, 3D, physics.  
  <sub>topics: ai, claude, cursor, game-development, godot, godot-engine, mcp, model-context-protocol</sub>
- **[tugcantopaloglu/godot-mcp](https://github.com/tugcantopaloglu/godot-mcp)** · 390★ · JavaScript · Rising  
  Full Godot 4.x engine control via MCP: 157 tools for AI-driven game development.  
  <sub>topics: game-development, gdscript, godot, mcp, model-context-protocol, ai, automation, godot-engine</sub>

### Learning / reference

_Where the ecosystem is catalogued and taught._

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 91,941★ · — · Hot  
  The flagship awesome-list of MCP servers (88k★).  
  <sub>topics: ai, mcp</sub>
- **[microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** · 16,938★ · Jupyter Notebook · Hot  
  Microsoft's open curriculum teaching MCP fundamentals.  
  <sub>topics: csharp, java, javascript, mcp, mcp-client, mcp-security, mcp-server, model</sub>
- **[wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** · 4,252★ · — · Mature  
  Curated list of MCP servers.  
  <sub>topics: —</sub>

## Spotlight: official vendor servers

A maturity signal — major vendors shipping **first-party** MCP servers in your stars:

- **Upstash** — [upstash/context7](https://github.com/upstash/context7) · 60,396★ · health 83
- **Microsoft** — [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) · 35,895★ · health 76
- **GitHub** — [github/github-mcp-server](https://github.com/github/github-mcp-server) · 32,035★ · health 88
- **Microsoft (edu)** — [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) · 16,938★ · health 69
- **Google** — [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) · 16,137★ · health 93
- **Sentry** — [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) · 808★ · health 82
- **SonarSource** — [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) · 617★ · health 76
- **Neo4j** — [neo4j/mcp](https://github.com/neo4j/mcp) · 278★ · health 75
- **Storybook** — [storybookjs/mcp](https://github.com/storybookjs/mcp) · 265★ · health 74

## Graph analysis — how they relate

**Community clustering.** These 40 projects span **14 of the graph's 31 communities** — MCP tooling is woven through the whole agent-infra landscape rather than sitting in one bucket.

- **Community 12** (13): `PrefectHQ/fastmcp`, `tadata-org/fastapi_mcp`, `Klavis-AI/klavis`, `aipotheosis-labs/gate22`, `bytebase/dbhub`, `shaneholloman/mcp-knowledge-graph`, `blazickjp/arxiv-mcp-server`, `Coding-Solo/godot-mcp`, `hi-godot/godot-ai`, `youichi-uda/godot-mcp-pro`, `tugcantopaloglu/godot-mcp`, `CoderGamester/mcp-unity`, `punkpeye/awesome-mcp-servers`
- **Community 10** (10): `oomol-lab/open-connector`, `brightdata/brightdata-mcp`, `github/github-mcp-server`, `getsentry/sentry-mcp`, `czlonkowski/n8n-mcp`, `upstash/context7`, `modelcontextprotocol/servers`, `modelcontextprotocol/typescript-sdk`, `modelcontextprotocol/inspector`, `hustcc/mcp-mermaid`
- **Community 14** (3): `mcp-use/mcp-use`, `ravitemer/mcphub.nvim`, `mksglu/context-mode`
- **Community 0** (3): `hangwin/mcp-chrome`, `storybookjs/mcp`, `mobile-next/mobile-mcp`
- **Community 20** (2): `microsoft/playwright-mcp`, `microsoft/mcp-for-beginners`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' MCP projects in your ecosystem:

- `microsoft/mcp-for-beginners` — PageRank 0.0032
- `modelcontextprotocol/typescript-sdk` — PageRank 0.0031
- `mksglu/context-mode` — PageRank 0.0027
- `yvgude/lean-ctx` — PageRank 0.0015
- `punkpeye/awesome-mcp-servers` — PageRank 0.0014
- `github/github-mcp-server` — PageRank 0.0013
- `Coding-Solo/godot-mcp` — PageRank 0.0011
- `blazickjp/arxiv-mcp-server` — PageRank 0.0011
- `microsoft/playwright-mcp` — PageRank 0.0010
- `SonarSource/sonarqube-mcp-server` — PageRank 0.0010

**Direct links between MCP projects** (top similarity edges where both endpoints are in this report):

- `microsoft/playwright-mcp` ⇄ `microsoft/mcp-for-beginners` (w=0.748) — topics: mcp; authors: dependabot[bot]
- `modelcontextprotocol/typescript-sdk` ⇄ `modelcontextprotocol/servers` (w=0.732) — authors: KKonstantinov, dependabot[bot]
- `modelcontextprotocol/typescript-sdk` ⇄ `modelcontextprotocol/inspector` (w=0.717) — topics: mcp
- `modelcontextprotocol/inspector` ⇄ `modelcontextprotocol/servers` (w=0.668) — authors: cliffhall
- `Coding-Solo/godot-mcp` ⇄ `punkpeye/awesome-mcp-servers` (w=0.667) — topics: ai, mcp
- `hi-godot/godot-ai` ⇄ `Coding-Solo/godot-mcp` (w=0.600) — topics: ai, godot, mcp
- `mksglu/context-mode` ⇄ `mcp-use/mcp-use` (w=0.560) — topics: claude-code, mcp, skills, openclaw; authors: github-actions[bot]
- `modelcontextprotocol/typescript-sdk` ⇄ `upstash/context7` (w=0.543) — topics: mcp, mcp-server; authors: github-actions[bot], KKonstantinov
- `czlonkowski/n8n-mcp` ⇄ `github/github-mcp-server` (w=0.511) — topics: mcp, mcp-server; authors: dependabot[bot], Copilot
- `modelcontextprotocol/typescript-sdk` ⇄ `czlonkowski/n8n-mcp` (w=0.501) — topics: mcp, mcp-server; authors: dependabot[bot]
- `github/github-mcp-server` ⇄ `upstash/context7` (w=0.489) — topics: mcp, mcp-server; authors: github-actions[bot], syf2211
- `youichi-uda/godot-mcp-pro` ⇄ `hi-godot/godot-ai` (w=0.435) — topics: ai, game-development, godot, mcp
- `microsoft/mcp-for-beginners` ⇄ `czlonkowski/n8n-mcp` (w=0.433) — topics: mcp, mcp-server; authors: dependabot[bot], Copilot
- `hi-godot/godot-ai` ⇄ `punkpeye/awesome-mcp-servers` (w=0.400) — topics: ai, mcp
- `hustcc/mcp-mermaid` ⇄ `github/github-mcp-server` (w=0.400) — topics: mcp, mcp-server
- …and 21 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). MCP servers are often weekend projects — check this before wiring one into production agents.

| Project | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| oomol-lab/open-connector | 99 | Hot | very active | 5 | 13% | 12 |
| googleapis/mcp-toolbox | 93 | Mature | very active | 4 | 19% | 47 |
| github/github-mcp-server | 88 | Hot | very active | 3 | 28% | 73 |
| mcp-use/mcp-use | 84 | Hot | very active | 2 | 42% | 1203 |
| upstash/context7 | 83 | Hot | very active | 2 | 42% | 101 |
| getsentry/sentry-mcp | 82 | Hot | very active | 2 | 48% | 41 |
| modelcontextprotocol/servers | 82 | Hot | very active | 3 | 30% | 26 |
| czlonkowski/n8n-mcp | 79 | Hot | very active | 1 | 73% | 251 |
| oraios/serena | 79 | Hot | very active | 1 | 64% | 15 |
| yvgude/lean-ctx | 79 | Hot | very active | 1 | 95% | 243 |
| modelcontextprotocol/inspector | 79 | Hot | very active | 1 | 96% | 58 |
| hi-godot/godot-ai | 79 | Hot | very active | 1 | 53% | 94 |
| PrefectHQ/fastmcp | 78 | Hot | very active | 1 | 77% | 112 |
| mksglu/context-mode | 78 | Rising | very active | 1 | 71% | 195 |
| microsoft/playwright-mcp | 76 | Mature | very active | 2 | 36% | 69 |
| SonarSource/sonarqube-mcp-server | 76 | Hot | very active | 2 | 33% | 36 |
| neo4j/mcp | 75 | Hot | very active | 2 | 28% | 28 |
| modelcontextprotocol/typescript-sdk | 75 | Hot | very active | 1 | 67% | 159 |
| bytebase/dbhub | 74 | Hot | very active | 1 | 90% | 6 |
| storybookjs/mcp | 74 | Hot | very active | 1 | 81% | 55 |
| mobile-next/mobile-mcp | 71 | Hot | very active | 1 | 90% | 50 |
| microsoft/mcp-for-beginners | 69 | Hot | very active | 2 | 43% | 0 |
| brightdata/brightdata-mcp | 68 | Mature | very active | 1 | 55% | 12 |
| VectifyAI/pageindex-mcp | 68 | Rising | active | 1 | 75% | 20 |
| youichi-uda/godot-mcp-pro | 68 | Rising | very active | 1 | 55% | 19 |
| blazickjp/arxiv-mcp-server | 66 | Mature | very active | 1 | 77% | 6 |
| punkpeye/awesome-mcp-servers | 64 | Hot | very active | 1 | 79% | 0 |
| CoderGamester/mcp-unity | 63 | Hot | very active | 1 | 75% | 9 |
| shaneholloman/mcp-knowledge-graph | 57 | Declining | slowing | 1 | 100% | 8 |
| tugcantopaloglu/godot-mcp | 53 | Rising | active | 1 | 91% | 3 |
| Klavis-AI/klavis | 52 | Declining | slowing | 1 | 100% | 79 |
| hustcc/mcp-mermaid | 49 | Declining | slowing | 1 | 100% | 6 |
| wong2/awesome-mcp-servers | 46 | Mature | active | 1 | 100% | 0 |
| Kochava-Studios/witsy | 45 | Mature | slowing | 0 | 0% | 173 |
| aipotheosis-labs/gate22 | 26 | Declining | stale | 0 | 0% | 8 |
| Coding-Solo/godot-mcp | 25 | Declining | slowing | 0 | 0% | 0 |
| ravitemer/mcphub.nvim | 22 | Declining | stale | 0 | 0% | 59 |
| hangwin/mcp-chrome | 17 | Declining | stale | 0 | 0% | 7 |
| tadata-org/fastapi_mcp | 13 | Declining | stale | 0 | 0% | 10 |
| reading-plus-ai/mcp-server-data-exploration | 1 | Abandoned | stale | 0 | 0% | 0 |

⚠️ **Adopt with caution** (low health and/or declining): `reading-plus-ai/mcp-server-data-exploration`, `tadata-org/fastapi_mcp`, `hangwin/mcp-chrome`, `ravitemer/mcphub.nvim`, `Coding-Solo/godot-mcp`, `aipotheosis-labs/gate22`, `hustcc/mcp-mermaid`, `Klavis-AI/klavis`, `shaneholloman/mcp-knowledge-graph`.

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

<sub>Projects covered: 40 (25 servers) · Snapshot: 2026-08-11T18:59:16.380Z</sub>
