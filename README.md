# GitHub Stars Analyzer

A 3D knowledge graph of your GitHub starred repositories — communities, relationships, lifecycle, and AI-powered exploration.

**Live:** [your-netlify-url.netlify.app](https://your-netlify-url.netlify.app)

---

## What it does

Fetches all your GitHub stars, builds a knowledge graph from shared topics, authors, and ownership, then lets you explore it in 3D:

- **Map** — interactive 3D force graph, nodes colored by community, sized by stars + PageRank
- **Topics** — co-occurrence graph of tags across your starred repos
- **Insights** — named queries: where devs actually work, hidden gems, rising stars
- **Browse** — searchable, filterable list of all repos
- **Compare** — side-by-side metrics + shortest graph path between two repos
- **Ask AI** — natural language questions answered using the knowledge graph as context

---

## Architecture

```
GitHub API
    ↓
scripts/ingest.mjs       # fetch raw repo + author data
scripts/classify.mjs     # lifecycle stage + health score (no LLM)
scripts/precompute.mjs   # kNN graph + Louvain communities + PageRank
                         # + 300-tick force simulation → positions
    ↓
public/data/
  graph.json             # 1.2 MB — nodes/links ready for the browser
  graph-context.json     # compact community summary for LLM context

Browser (React + Three.js)
  → loads graph.json, renders immediately (zero graph math in browser)
  → ForceGraph3D with pre-computed node positions

Netlify Function /api/ask
  → loads graph-context.json, calls any OpenAI-compatible LLM endpoint
    (default: Z.AI GLM-4.6 Coding Plan)
```

---

## Quick start

```bash
npm install
cp .env.example .env          # add GITHUB_TOKEN
npm run refresh               # fetch → classify → precompute
npm run dev
```

Open http://localhost:5173

---

## Data pipeline

```bash
npm run refresh               # full pipeline (sample → ingest → classify → precompute)
npm run precompute            # rebuild graph.json from existing classified.json
```

`refresh` requires `GITHUB_TOKEN` in `.env`. The precompute step runs entirely offline.

### What each script does

| Script | Input | Output |
|--------|-------|--------|
| `scripts/sample.mjs` | GitHub username | `src/data/sample-all.json` (star list) |
| `scripts/ingest.mjs` | sample + `--max-age` | `src/data/raw-all.json` (full repo data) |
| `scripts/classify.mjs` | raw JSON | `classified-all.json` (lifecycle + health) |
| `scripts/precompute.mjs` | classified JSON | `graph.json` + `graph-context.json` |

---

## Ask AI setup

The **Ask AI** tab calls a provider-agnostic Netlify Function that talks to any **OpenAI-compatible** chat-completions endpoint. Three env vars configure it:

| Var            | Required | Default                                      |
|----------------|----------|----------------------------------------------|
| `LLM_API_KEY`  | yes      | —                                            |
| `LLM_BASE_URL` | no       | `https://api.z.ai/api/coding/paas/v4`        |
| `LLM_MODEL`    | no       | `glm-4.6`                                    |

In Netlify: **Site settings → Environment variables → Add**, then redeploy. Locally, drop them into `.env` (see `.env.example`). Legacy `ZAI_API_KEY` / `ZAI_BASE_URL` / `ZAI_MODEL` are still honored as fallbacks.

### Provider recipes

| Provider                | `LLM_BASE_URL`                                | Example `LLM_MODEL`                                  |
|-------------------------|-----------------------------------------------|------------------------------------------------------|
| **Z.AI Coding Plan**    | `https://api.z.ai/api/coding/paas/v4`         | `glm-4.6`                                            |
| Z.AI pay-as-you-go      | `https://api.z.ai/api/paas/v4`                | `glm-4.6`                                            |
| OpenAI                  | `https://api.openai.com/v1`                   | `gpt-4o-mini`                                        |
| Groq                    | `https://api.groq.com/openai/v1`              | `llama-3.3-70b-versatile`                            |
| Together                | `https://api.together.xyz/v1`                 | `meta-llama/Llama-3.3-70B-Instruct-Turbo`            |
| DeepSeek                | `https://api.deepseek.com/v1`                 | `deepseek-chat`                                      |
| Mistral                 | `https://api.mistral.ai/v1`                   | `mistral-small-latest`                               |
| OpenRouter (→ anything) | `https://openrouter.ai/api/v1`                | `anthropic/claude-sonnet-4-5`                        |
| Fireworks               | `https://api.fireworks.ai/inference/v1`       | `accounts/fireworks/models/llama-v3p3-70b-instruct`  |
| Local Ollama            | `http://localhost:11434/v1`                   | `llama3.2`                                           |

Without `LLM_API_KEY` the tab shows a configuration notice; every other tab works normally. Billing / quota errors are detected generically and surfaced as a friendly notice rather than a stack trace.

---

## Deploy to Netlify

1. Push to GitHub
2. Connect repo in Netlify — auto-detects `netlify.toml`
3. Build command: `npm run build` · Publish: `dist`
4. Add `LLM_API_KEY` (and optionally `LLM_BASE_URL` / `LLM_MODEL`) environment variables for Ask AI

`graph.json` is committed so Netlify serves it without running the data pipeline at build time. Re-run `npm run refresh` locally when you want fresh data, then push.

---

## Tech stack

| Layer | Libraries |
|-------|-----------|
| UI | React 18, Tailwind CSS, Lucide |
| 3D graph | react-force-graph-3d, Three.js, d3-force-3d |
| Graph algorithms | graphology, graphology-communities-louvain, graphology-metrics |
| Data pipeline | Node.js ESM scripts, GitHub REST API |
| LLM | Any OpenAI-compatible API (default: Z.AI GLM-4.6 Coding Plan) |
| Hosting | Netlify (static + Functions) |

---

## Project structure

```
scripts/
  ingest.mjs          fetch repo data from GitHub
  classify.mjs        lifecycle + health scoring
  precompute.mjs      graph build, simulation, LLM context

public/data/
  classified.json     raw classified data (committed)
  graph.json          pre-computed graph (committed)
  graph-context.json  LLM grounding context (committed)

src/lab/
  GraphProvider.jsx   loads graph.json, provides nodes/links via context
  MapView.jsx         3D force graph
  TopicMap.jsx        topic co-occurrence graph
  InsightFeed.jsx     named analytical queries
  AllRepos.jsx        searchable repo list
  Comparator.jsx      side-by-side comparison + path finding
  LabApp.jsx          tab routing + Ask AI UI

netlify/functions/
  ask.mjs             POST /api/ask → Claude
```

---

## License

MIT © Martin Kaiser
