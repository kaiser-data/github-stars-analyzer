# MCP (Model Context Protocol) Tooling — Landscape Report

> Derived from **kaiser-data**'s 1,341 starred repos (snapshot `2026-07-19T22:39:07.967Z`), cross-referenced with the repo-similarity graph (1,341 nodes / 4,341 edges, 28 communities).
>
> Generated 2026-07-19 by `scripts/reports/mcp_tooling.py` (regenerate any time — no API cost).

![Top tools by stars](assets/mcp-tooling-top-tools.svg)

![Tools per category](assets/mcp-tooling-categories.svg)


> **What is MCP?** The Model Context Protocol is an open standard (Anthropic, late 2024) that lets LLM apps talk to external tools/data through a uniform interface — the 'USB-C port' for AI. **Servers** expose capabilities; **clients/hosts** (Claude Desktop, Cursor, editors) consume them; **gateways** govern them at scale.

## Executive summary

- **41 MCP projects** in your stars (**541,376★** combined) — spanning the whole stack: SDKs, clients, gateways, and **26 domain servers**.
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
| **Servers** | Expose a capability to agents | 26 across browser, DB, dev-tools, code-intel, docs, game engines |
| **Learning** | Lists & curricula | `awesome-mcp-servers` (×2), `mcp-for-beginners` |

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Project | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Learning / reference | — | MIT | 90,968 (▲296) | Hot | 64 | very active | 6d ago | 1.6y | 4 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | SDK / framework | TypeScript | NOASSERTION | 88,639 (▲249) | Hot | 75 | very active | 10d ago | 1.7y | 14 |
| [upstash/context7](https://github.com/upstash/context7) | Server · code intelligence | TypeScript | MIT | 59,432 (▲419) | Hot | 84 | very active | 0d ago | 1.3y | 18 |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Server · browser/web | TypeScript | Apache-2.0 | 35,270 (▲261) | Hot | 73 | very active | 5d ago | 1.3y | 8 |
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | Server · dev-tooling | Go | MIT | 31,557 (▲158) | Hot | 93 | very active | 0d ago | 1.4y | 35 |
| [oraios/serena](https://github.com/oraios/serena) | Server · code intelligence | Python | MIT | 26,586 (▲201) | Hot | 79 | very active | 0d ago | 1.3y | 13 |
| [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | SDK / framework | Python | Apache-2.0 | 26,296 (▲128) | Hot | 79 | very active | 0d ago | 1.6y | 16 |
| [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | Server · dev-tooling | TypeScript | MIT | 22,348 (▲83) | Hot | 79 | very active | 3d ago | 1.1y | 9 |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | Server · code intelligence | TypeScript | NOASSERTION | 19,094 (▲233) | Hot | 84 | very active | 0d ago | 4mo | 5 |
| [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | Learning / reference | Jupyter Notebook | MIT | 16,781 (▲39) | Hot | 65 | very active | 2d ago | 1.3y | 7 |
| [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) | Gateway / control plane | Go | Apache-2.0 | 15,980 (▲36) | Mature | 98 | very active | 0d ago | 2.1y | 29 |
| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | SDK / framework | TypeScript | NOASSERTION | 12,892 (▲53) | Hot | 76 | very active | 1d ago | 1.8y | 8 |
| [hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome) | Server · browser/web | TypeScript | MIT | 12,153 (▲54) | Declining | 19 | stale | 6mo ago | 1.1y | 0 |
| [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | SDK / framework | Python | MIT | 11,949 (▲8) | Declining | 16 | stale | 7mo ago | 1.4y | 0 |
| [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) | Client / host | TypeScript | NOASSERTION | 10,406 (▲52) | Mature | 68 | active | 0d ago | 1.8y | 5 |
| [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) | SDK / framework | TypeScript | MIT | 10,331 (▲48) | Hot | 81 | very active | 0d ago | 1.3y | 11 |
| [Klavis-AI/klavis](https://github.com/Klavis-AI/klavis) | Gateway / control plane | Python | Apache-2.0 | 5,771 (▲3) | Mature | 60 | active | 1mo ago | 1.3y | 2 |
| [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) | Server · game/platform | TypeScript | Apache-2.0 | 5,494 (▲62) | Hot | 70 | very active | 7d ago | 1.3y | 4 |
| [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) | Server · game/platform | JavaScript | MIT | 4,799 (▲121) | Declining | 27 | slowing | 3mo ago | 1.4y | 0 |
| [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) | Learning / reference | — | MIT | 4,217 (▲14) | Mature | 49 | active | 6d ago | 1.6y | 1 |
| [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) | Server · browser/web | TypeScript | Apache-2.0 | 3,408 (▲6) | Declining | 41 | active | 13d ago | 1.6y | 1 |
| [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx) | Server · code intelligence | Rust | Apache-2.0 | 3,298 (▲69) | Hot | 80 | very active | 0d ago | 3mo | 5 |
| [bytebase/dbhub](https://github.com/bytebase/dbhub) | Server · database/data | TypeScript | MIT | 3,182 (▲33) | Hot | 63 | very active | 0d ago | 1.4y | 6 |
| [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | Gateway / control plane | TypeScript | Apache-2.0 | 2,997 | Hot | 92 | very active | 0d ago | 20d | 27 |
| [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | Server · docs/research | Python | Apache-2.0 | 2,969 (▲16) | Mature | 52 | slowing | 2mo ago | 1.6y | 5 |
| [brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | Server · browser/web | JavaScript | MIT | 2,516 (▲21) | Mature | 65 | active | 29d ago | 1.3y | 2 |
| [Kochava-Studios/witsy](https://github.com/Kochava-Studios/witsy) | Client / host | TypeScript | AGPL-3.0 | 2,005 (▲14) | Mature | 47 | slowing | 2mo ago | 2.2y | 0 |
| [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) | Server · game/platform | C# | MIT | 1,833 (▲6) | Mature | 58 | very active | 15d ago | 1.4y | 5 |
| [ravitemer/mcphub.nvim](https://github.com/ravitemer/mcphub.nvim) | Client / host | Lua | MIT | 1,782 (▲1) | Declining | 25 | stale | 6mo ago | 1.4y | 0 |
| [hi-godot/godot-ai](https://github.com/hi-godot/godot-ai) | Server · game/platform | GDScript | MIT | 1,065 | Hot | 79 | very active | 1d ago | 3mo | 9 |
| [shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) | Server · code intelligence | JavaScript | MIT | 877 (▲2) | Declining | 59 | active | 1mo ago | 1.6y | 1 |
| [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) | Server · dev-tooling | TypeScript | NOASSERTION | 781 (▲12) | Hot | 77 | very active | 1d ago | 1.3y | 21 |
| [hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid) | Server · docs/research | TypeScript | MIT | 611 (▲4) | Declining | 52 | slowing | 2mo ago | 1.2y | 2 |
| [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) | Server · dev-tooling | Java | NOASSERTION | 599 (▲5) | Hot | 77 | very active | 2d ago | 1.2y | 16 |
| [reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) | Server · database/data | Python | MIT | 545 | Abandoned | 1 | stale | 1.3y ago | 1.6y | 0 |
| [youichi-uda/godot-mcp-pro](https://github.com/youichi-uda/godot-mcp-pro) | Server · game/platform | GDScript | NOASSERTION | 515 | Rising | 70 | very active | 0d ago | 4mo | 3 |
| [VectifyAI/pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp) | Server · docs/research | TypeScript | MIT | 372 (▼2) | Rising | 63 | active | 1mo ago | 10mo | 2 |
| [tugcantopaloglu/godot-mcp](https://github.com/tugcantopaloglu/godot-mcp) | Server · game/platform | JavaScript | MIT | 345 | Rising | 58 | active | 7d ago | 5mo | 2 |
| [neo4j/mcp](https://github.com/neo4j/mcp) | Server · database/data | Go | NOASSERTION | 273 (▲4) | Hot | 79 | very active | 2d ago | 11mo | 8 |
| [storybookjs/mcp](https://github.com/storybookjs/mcp) | Server · dev-tooling | TypeScript | MIT | 263 (▲1) | Hot | 75 | very active | 5d ago | 11mo | 7 |
| [aipotheosis-labs/gate22](https://github.com/aipotheosis-labs/gate22) | Gateway / control plane | TypeScript | Apache-2.0 | 177 | Declining | 28 | stale | 7mo ago | 11mo | 0 |

## By category

### SDK / framework

_The layer you reach for to *author* an MCP server or client._

- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** · 88,639★ · TypeScript · Hot  
  Official reference-server monorepo — canonical examples for filesystem, git, fetch, etc.  
  <sub>topics: —</sub>
- **[PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)** · 26,296★ · Python · Hot  
  The fast, Pythonic way to build MCP servers & clients; the de-facto Python framework.  
  <sub>topics: model-context-protocol, fastmcp, mcp, agents, llms, mcp-clients, mcp-servers, mcp-tools</sub>
- **[modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** · 12,892★ · TypeScript · Hot  
  Official TypeScript SDK for building MCP servers & clients.  
  <sub>topics: —</sub>
- **[tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** · 11,949★ · Python · Declining  
  Expose existing FastAPI endpoints as MCP tools, with auth — zero-rewrite server creation.  
  <sub>topics: ai, claude, cursor, fastapi, llm, mcp, mcp-server, mcp-servers</sub>
- **[mcp-use/mcp-use](https://github.com/mcp-use/mcp-use)** · 10,331★ · TypeScript · Hot  
  Fullstack MCP framework — build MCP apps for ChatGPT/Claude and MCP servers for agents.  
  <sub>topics: mcp, model-context-protocol, apps-sdk, mcp-apps, mcp-inspector, mcp-servers, mcp-ui, agentic-framework</sub>

### Client / host

_Apps/editors that connect to servers and surface their tools to the user._

- **[modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)** · 10,406★ · TypeScript · Mature  
  Official visual debugger/inspector for testing MCP servers.  
  <sub>topics: —</sub>
- **[Kochava-Studios/witsy](https://github.com/Kochava-Studios/witsy)** · 2,005★ · TypeScript · Mature  
  Desktop AI assistant doubling as a universal MCP client.  
  <sub>topics: anthropic, genai, groq, ollama, ollama-gui, openai, electron-app, electronjs</sub>
- **[ravitemer/mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** · 1,782★ · Lua · Declining  
  MCP client for Neovim — integrates MCP servers into the editing workflow.  
  <sub>topics: avante, chatgpt, chatplugin, claude-ai, llm, mcp, mcp-client, mcp-hub</sub>

### Gateway / control plane

_Front many servers behind one endpoint; add auth, routing, and policy — the enterprise-readiness layer._

- **[googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox)** · 15,980★ · Go · Mature  
  Google's open MCP server for databases — one gateway fronting many DBs.  
  <sub>topics: genai, mcp, agent, ai, database, llm, server, agents</sub>
- **[Klavis-AI/klavis](https://github.com/Klavis-AI/klavis)** · 5,771★ · Python · Mature  
  MCP integration platform so agents use tools reliably at scale.  
  <sub>topics: ai, discord, llm, mcp, mcp-client, mcp-server, open-source, agents</sub>
- **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** · 2,997★ · TypeScript · Hot  
  Open-source auth gateway connecting 1000+ SaaS providers to agents via MCP, SDK & HTTP.  
  <sub>topics: agent-tools, ai-agents, api-gateway, automation, cli, cloudflare-workers, connectors, integration-platform</sub>
- **[aipotheosis-labs/gate22](https://github.com/aipotheosis-labs/gate22)** · 177★ · TypeScript · Declining  
  Open-source MCP gateway & control plane to govern which tools agents may use.  
  <sub>topics: agents, ai, ai-agents, control-plane, gateway, guardrails, llm, mcp</sub>

### Server · browser/web

_Give agents a browser or the open web._

- **[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)** · 35,270★ · TypeScript · Hot  
  Microsoft's Playwright MCP server — drive a real browser from an agent.  
  <sub>topics: mcp, playwright</sub>
- **[hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome)** · 12,153★ · TypeScript · Declining  
  Chrome-extension-based MCP server exposing the user's actual browser.  
  <sub>topics: —</sub>
- **[browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase)** · 3,408★ · TypeScript · Declining  
  Let LLMs control a cloud browser via Browserbase + Stagehand.  
  <sub>topics: ai, browser, chrome, chromium, mcp, playwright, puppeteer</sub>
- **[brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** · 2,516★ · JavaScript · Mature  
  All-in-one MCP server for public web data access / scraping at scale.  
  <sub>topics: llm, mcp, modelcontextprotocol, scraping, ai-agents, ai-integrations, anti-bot-detection, browser-automation</sub>

### Server · database/data

_Expose databases and datasets as agent-queryable tools._

- **[bytebase/dbhub](https://github.com/bytebase/dbhub)** · 3,182★ · TypeScript · Hot  
  Zero-dependency, token-efficient database MCP server (Postgres, MySQL, SQL Server, …).  
  <sub>topics: ai, anthropic, claude, database, mcp, mcp-server, claude-ai, mysql</sub>
- **[reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** · 545★ · Python · Abandoned  
  MCP server for interactive data exploration.  
  <sub>topics: —</sub>
- **[neo4j/mcp](https://github.com/neo4j/mcp)** · 273★ · Go · Hot  
  Neo4j's official MCP server for graph-database access.  
  <sub>topics: —</sub>

### Server · dev-tooling

_Wire agents into the software-delivery toolchain (VCS, CI, quality, errors)._

- **[github/github-mcp-server](https://github.com/github/github-mcp-server)** · 31,557★ · Go · Hot  
  GitHub's official MCP server — issues, PRs, repos as agent tools.  
  <sub>topics: github, mcp, mcp-server</sub>
- **[czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** · 22,348★ · TypeScript · Hot  
  MCP server that helps agents build n8n workflows.  
  <sub>topics: mcp, mcp-server, n8n, workflows</sub>
- **[getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp)** · 781★ · TypeScript · Hot  
  Interact with Sentry (errors/issues) via LLMs.  
  <sub>topics: mcp-server, tag-production</sub>
- **[SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** · 599★ · Java · Hot  
  Official SonarQube MCP server — code quality & security in agents.  
  <sub>topics: agent, ai, mcp, mcp-server, sonarqube, code-quality, security, static-analysis</sub>
- **[storybookjs/mcp](https://github.com/storybookjs/mcp)** · 263★ · TypeScript · Hot  
  Storybook's MCP server for component-driven workflows.  
  <sub>topics: —</sub>

### Server · code intelligence

_Feed agents accurate code/library context — the antidote to hallucinated APIs._

- **[upstash/context7](https://github.com/upstash/context7)** · 59,432★ · TypeScript · Hot  
  Up-to-date library docs piped to LLMs/editors via MCP — kills version drift.  
  <sub>topics: llm, mcp, mcp-server, vibe-coding</sub>
- **[oraios/serena](https://github.com/oraios/serena)** · 26,586★ · Python · Hot  
  Powerful MCP coding toolkit — semantic retrieval & editing (LSP-backed).  
  <sub>topics: agent, ai, vibe-coding, mcp-server, ai-coding, language-server, programming, claude</sub>
- **[mksglu/context-mode](https://github.com/mksglu/context-mode)** · 19,094★ · TypeScript · Hot  
  Context-window optimization for coding agents; sandboxes tool output (~98% reduction).  
  <sub>topics: claude, claude-code, claude-code-plugins, mcp, skills, codex, copilot, opencode</sub>
- **[yvgude/lean-ctx](https://github.com/yvgude/lean-ctx)** · 3,298★ · Rust · Hot  
  Cognitive context layer — 51+ MCP tools, multiple read modes for agentic systems.  
  <sub>topics: ai, cursor, llm, mcp, rust, token-optimization, agentic-coding, claude-code</sub>
- **[shaneholloman/mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** · 877★ · JavaScript · Declining  
  Persistent memory for Claude via a local knowledge graph (also in the memory report).  
  <sub>topics: ai-memory, claude-ai, knowledge-graph, mcp, memory-server, typescript</sub>

### Server · docs/research

_Documents, papers, and diagram generation._

- **[blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** · 2,969★ · Python · Mature  
  Search & analyze arXiv papers through MCP.  
  <sub>topics: ai, claude-ai, gpt, mcp-server, arxiv, papers, research, llm</sub>
- **[hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** · 611★ · TypeScript · Declining  
  Generate Mermaid diagrams/charts dynamically via MCP.  
  <sub>topics: mcp, mcp-server, mermaid, mermaidjs</sub>
- **[VectifyAI/pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp)** · 372★ · TypeScript · Rising  
  MCP front-end to PageIndex's vectorless reasoning-based RAG.  
  <sub>topics: —</sub>

### Server · game/platform

_Drive game engines and mobile/desktop platforms._

- **[mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp)** · 5,494★ · TypeScript · Hot  
  MCP server for mobile automation/scraping (iOS, Android, emulators).  
  <sub>topics: android, ios, mcp, mobile, agent, emulator, physical, real</sub>
- **[Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp)** · 4,799★ · JavaScript · Declining  
  MCP server to drive the Godot game engine (launch editor, run scenes).  
  <sub>topics: ai, godot, mcp</sub>
- **[CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity)** · 1,833★ · C# · Mature  
  MCP plugin connecting agents (Cursor/Claude) to the Unity editor.  
  <sub>topics: cursor, unity, unity-package, mcp, copilot, game-development, model-context-protocol, openai</sub>
- **[hi-godot/godot-ai](https://github.com/hi-godot/godot-ai)** · 1,065★ · GDScript · Hot  
  Production-grade MCP server and AI tools for the Godot engine.  
  <sub>topics: ai, game-development, godot, godot-plugin, mcp</sub>
- **[youichi-uda/godot-mcp-pro](https://github.com/youichi-uda/godot-mcp-pro)** · 515★ · GDScript · Rising  
  162 MCP tools for AI-powered Godot 4 development — scene, animation, 3D, physics.  
  <sub>topics: ai, claude, cursor, game-development, godot, godot-engine, mcp, model-context-protocol</sub>
- **[tugcantopaloglu/godot-mcp](https://github.com/tugcantopaloglu/godot-mcp)** · 345★ · JavaScript · Rising  
  Full Godot 4.x engine control via MCP: 157 tools for AI-driven game development.  
  <sub>topics: game-development, gdscript, godot, mcp, model-context-protocol, ai, automation, godot-engine</sub>

### Learning / reference

_Where the ecosystem is catalogued and taught._

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · 90,968★ · — · Hot  
  The flagship awesome-list of MCP servers (88k★).  
  <sub>topics: ai, mcp</sub>
- **[microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** · 16,781★ · Jupyter Notebook · Hot  
  Microsoft's open curriculum teaching MCP fundamentals.  
  <sub>topics: csharp, java, javascript, mcp, mcp-client, mcp-security, mcp-server, model</sub>
- **[wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** · 4,217★ · — · Mature  
  Curated list of MCP servers.  
  <sub>topics: —</sub>

## Spotlight: official vendor servers

A maturity signal — major vendors shipping **first-party** MCP servers in your stars:

- **Upstash** — [upstash/context7](https://github.com/upstash/context7) · 59,432★ · health 84
- **Microsoft** — [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) · 35,270★ · health 73
- **GitHub** — [github/github-mcp-server](https://github.com/github/github-mcp-server) · 31,557★ · health 93
- **Microsoft (edu)** — [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) · 16,781★ · health 65
- **Google** — [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) · 15,980★ · health 98
- **Sentry** — [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) · 781★ · health 77
- **SonarSource** — [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) · 599★ · health 77
- **Neo4j** — [neo4j/mcp](https://github.com/neo4j/mcp) · 273★ · health 79
- **Storybook** — [storybookjs/mcp](https://github.com/storybookjs/mcp) · 263★ · health 75

## Graph analysis — how they relate

**Community clustering.** These 41 projects span **14 of the graph's 28 communities** — MCP tooling is woven through the whole agent-infra landscape rather than sitting in one bucket.

- **Community 1** (16): `tadata-org/fastapi_mcp`, `brightdata/brightdata-mcp`, `bytebase/dbhub`, `github/github-mcp-server`, `getsentry/sentry-mcp`, `SonarSource/sonarqube-mcp-server`, `czlonkowski/n8n-mcp`, `upstash/context7`, `shaneholloman/mcp-knowledge-graph`, `hustcc/mcp-mermaid`, `Coding-Solo/godot-mcp`, `hi-godot/godot-ai`, `youichi-uda/godot-mcp-pro`, `tugcantopaloglu/godot-mcp`, `CoderGamester/mcp-unity`, `punkpeye/awesome-mcp-servers`
- **Community 2** (5): `oomol-lab/open-connector`, `hangwin/mcp-chrome`, `oraios/serena`, `yvgude/lean-ctx`, `mobile-next/mobile-mcp`
- **Community 9** (4): `Klavis-AI/klavis`, `aipotheosis-labs/gate22`, `browserbase/mcp-server-browserbase`, `blazickjp/arxiv-mcp-server`
- **Community 8** (3): `mcp-use/mcp-use`, `ravitemer/mcphub.nvim`, `mksglu/context-mode`
- **Community 24** (3): `modelcontextprotocol/servers`, `modelcontextprotocol/typescript-sdk`, `modelcontextprotocol/inspector`
- **Community 21** (2): `microsoft/playwright-mcp`, `microsoft/mcp-for-beginners`

**Centrality (PageRank in the full 1,071-repo graph)** — most 'hub-like' MCP projects in your ecosystem:

- `microsoft/mcp-for-beginners` — PageRank 0.0027
- `oomol-lab/open-connector` — PageRank 0.0021
- `github/github-mcp-server` — PageRank 0.0016
- `punkpeye/awesome-mcp-servers` — PageRank 0.0015
- `hi-godot/godot-ai` — PageRank 0.0014
- `microsoft/playwright-mcp` — PageRank 0.0014
- `hustcc/mcp-mermaid` — PageRank 0.0014
- `mksglu/context-mode` — PageRank 0.0013
- `czlonkowski/n8n-mcp` — PageRank 0.0013
- `Coding-Solo/godot-mcp` — PageRank 0.0012

**Direct links between MCP projects** (top similarity edges where both endpoints are in this report):

- `modelcontextprotocol/inspector` ⇄ `modelcontextprotocol/servers` (w=0.925) — authors: cliffhall, olaservo, galagaevdc
- `modelcontextprotocol/typescript-sdk` ⇄ `modelcontextprotocol/servers` (w=0.750) — authors: KKonstantinov, dependabot[bot]
- `microsoft/playwright-mcp` ⇄ `microsoft/mcp-for-beginners` (w=0.710) — topics: mcp; authors: dependabot[bot]
- `Coding-Solo/godot-mcp` ⇄ `punkpeye/awesome-mcp-servers` (w=0.667) — topics: ai, mcp
- `hi-godot/godot-ai` ⇄ `Coding-Solo/godot-mcp` (w=0.600) — topics: ai, godot, mcp
- `hustcc/mcp-mermaid` ⇄ `czlonkowski/n8n-mcp` (w=0.583) — topics: mcp, mcp-server; authors: Copilot
- `czlonkowski/n8n-mcp` ⇄ `github/github-mcp-server` (w=0.495) — topics: mcp, mcp-server; authors: dependabot[bot], Copilot
- `github/github-mcp-server` ⇄ `upstash/context7` (w=0.478) — topics: mcp, mcp-server; authors: syf2211, github-actions[bot]
- `hustcc/mcp-mermaid` ⇄ `github/github-mcp-server` (w=0.456) — topics: mcp, mcp-server; authors: Copilot
- `youichi-uda/godot-mcp-pro` ⇄ `hi-godot/godot-ai` (w=0.435) — topics: ai, game-development, godot, mcp
- `microsoft/mcp-for-beginners` ⇄ `czlonkowski/n8n-mcp` (w=0.411) — topics: mcp, mcp-server; authors: Copilot, dependabot[bot]
- `hi-godot/godot-ai` ⇄ `punkpeye/awesome-mcp-servers` (w=0.400) — topics: ai, mcp
- `youichi-uda/godot-mcp-pro` ⇄ `tugcantopaloglu/godot-mcp` (w=0.389) — topics: ai, game-development, godot, godot-engine
- `mksglu/context-mode` ⇄ `mcp-use/mcp-use` (w=0.360) — topics: claude-code, mcp, skills, openclaw; authors: github-actions[bot]
- `microsoft/playwright-mcp` ⇄ `browserbase/mcp-server-browserbase` (w=0.336) — topics: mcp, playwright
- …and 20 more.

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). MCP servers are often weekend projects — check this before wiring one into production agents.

| Project | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| googleapis/mcp-toolbox | 98 | Mature | very active | 6 | 13% | 46 |
| github/github-mcp-server | 93 | Hot | very active | 4 | 23% | 71 |
| oomol-lab/open-connector | 92 | Hot | very active | 4 | 26% | 7 |
| upstash/context7 | 84 | Hot | very active | 2 | 39% | 95 |
| mksglu/context-mode | 84 | Hot | very active | 2 | 49% | 195 |
| mcp-use/mcp-use | 81 | Hot | very active | 2 | 27% | 1149 |
| yvgude/lean-ctx | 80 | Hot | very active | 1 | 67% | 238 |
| PrefectHQ/fastmcp | 79 | Hot | very active | 1 | 79% | 106 |
| neo4j/mcp | 79 | Hot | very active | 2 | 28% | 28 |
| czlonkowski/n8n-mcp | 79 | Hot | very active | 1 | 73% | 238 |
| oraios/serena | 79 | Hot | very active | 1 | 66% | 14 |
| hi-godot/godot-ai | 79 | Hot | very active | 1 | 62% | 87 |
| getsentry/sentry-mcp | 77 | Hot | very active | 1 | 51% | 41 |
| SonarSource/sonarqube-mcp-server | 77 | Hot | very active | 2 | 39% | 34 |
| modelcontextprotocol/typescript-sdk | 76 | Hot | very active | 1 | 66% | 140 |
| storybookjs/mcp | 75 | Hot | very active | 1 | 84% | 55 |
| modelcontextprotocol/servers | 75 | Hot | very active | 2 | 41% | 26 |
| microsoft/playwright-mcp | 73 | Hot | very active | 1 | 62% | 68 |
| youichi-uda/godot-mcp-pro | 70 | Rising | very active | 1 | 52% | 18 |
| mobile-next/mobile-mcp | 70 | Hot | very active | 1 | 92% | 49 |
| modelcontextprotocol/inspector | 68 | Mature | active | 1 | 72% | 52 |
| brightdata/brightdata-mcp | 65 | Mature | active | 1 | 73% | 11 |
| microsoft/mcp-for-beginners | 65 | Hot | very active | 1 | 57% | 0 |
| punkpeye/awesome-mcp-servers | 64 | Hot | very active | 1 | 96% | 0 |
| bytebase/dbhub | 63 | Hot | very active | 1 | 86% | 2 |
| VectifyAI/pageindex-mcp | 63 | Rising | active | 1 | 70% | 19 |
| Klavis-AI/klavis | 60 | Mature | active | 1 | 92% | 79 |
| shaneholloman/mcp-knowledge-graph | 59 | Declining | active | 1 | 100% | 8 |
| tugcantopaloglu/godot-mcp | 58 | Rising | active | 1 | 91% | 3 |
| CoderGamester/mcp-unity | 58 | Mature | very active | 1 | 83% | 8 |
| blazickjp/arxiv-mcp-server | 52 | Mature | slowing | 1 | 78% | 2 |
| hustcc/mcp-mermaid | 52 | Declining | slowing | 1 | 50% | 6 |
| wong2/awesome-mcp-servers | 49 | Mature | active | 1 | 100% | 0 |
| Kochava-Studios/witsy | 47 | Mature | slowing | 0 | 0% | 173 |
| browserbase/mcp-server-browserbase | 41 | Declining | active | 1 | 100% | 1 |
| aipotheosis-labs/gate22 | 28 | Declining | stale | 0 | 0% | 8 |
| Coding-Solo/godot-mcp | 27 | Declining | slowing | 0 | 0% | 0 |
| ravitemer/mcphub.nvim | 25 | Declining | stale | 0 | 0% | 59 |
| hangwin/mcp-chrome | 19 | Declining | stale | 0 | 0% | 7 |
| tadata-org/fastapi_mcp | 16 | Declining | stale | 0 | 0% | 10 |
| reading-plus-ai/mcp-server-data-exploration | 1 | Abandoned | stale | 0 | 0% | 0 |

⚠️ **Adopt with caution** (low health and/or declining): `reading-plus-ai/mcp-server-data-exploration`, `tadata-org/fastapi_mcp`, `hangwin/mcp-chrome`, `ravitemer/mcphub.nvim`, `Coding-Solo/godot-mcp`, `aipotheosis-labs/gate22`, `browserbase/mcp-server-browserbase`, `hustcc/mcp-mermaid`, `shaneholloman/mcp-knowledge-graph`.

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

<sub>Projects covered: 41 (26 servers) · Snapshot: 2026-07-19T22:39:07.967Z</sub>
