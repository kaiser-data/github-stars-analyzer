# LLM Evaluation Tooling — Landscape Report

> Derived from **kaiser-data**'s 1,071 starred repos (snapshot `2026-05-24T19:57:47.245Z`), cross-referenced with the repo-similarity graph (1,071 nodes / 3,486 edges, 23 communities).
>
> Generated 2026-05-31 by `scripts/reports/llm_evaluation.py` (regenerate any time — no API cost).

## Executive summary

- **18 evaluation-focused tools** found in your stars (**113,734★** combined), spanning four categories:
  - **Observability + eval platform** (5): `langfuse`, `mlflow`, `opik`, `openllmetry`, `opik-openclaw`
  - **Evaluation framework** (4): `deepeval`, `openevals`, `agentevals`, `rhesis`
  - **Benchmark / leaderboard** (5): `skill`, `LiveBench`, `guidellm`, `Open-Financial-LLMs-Leaderboard`, `RACE`
  - **Safety / red-team** (4): `garak`, `deepteam`, `uqlm`, `LettuceDetect`
- The field splits cleanly into **online** evaluation (tracing/observability in production) and **offline** evaluation (datasets, metrics, benchmarks before ship). Platforms increasingly do both.
- Evaluation method has converged on **LLM-as-a-judge** (deepeval, openevals) alongside classic reference metrics, plus a fast-growing **safety/red-team** wing (garak, deepteam) and **hallucination detection** (uqlm, LettuceDetect).
- Python dominates (15/18); the lone TypeScript-first platform is Langfuse.

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Observability + eval platform | TypeScript | NOASSERTION | 27,824 | Classic | 89 | very active | 1d ago | 3.0y | 17 |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | Observability + eval platform | Python | Apache-2.0 | 26,085 | Classic | 82 | very active | 0d ago | 8.0y | 21 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Observability + eval platform | Python | Apache-2.0 | 19,366 | Classic | 94 | very active | 0d ago | 3.0y | 25 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | Evaluation framework | Python | Apache-2.0 | 15,669 | Mature | 77 | very active | 1d ago | 2.8y | 3 |
| [NVIDIA/garak](https://github.com/NVIDIA/garak) | Safety / red-team | Python | Apache-2.0 | 7,896 | Classic | 77 | very active | 3d ago | 3.0y | 10 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Observability + eval platform | Python | Apache-2.0 | 7,139 | Mature | 85 | very active | 5d ago | 2.7y | 17 |
| [confident-ai/deepteam](https://github.com/confident-ai/deepteam) | Safety / red-team | Python | Apache-2.0 | 1,816 | Hot | 59 | very active | 27d ago | 1.2y | 4 |
| [pinchbench/skill](https://github.com/pinchbench/skill) | Benchmark / leaderboard | Python | MIT | 1,195 | Hot | 79 | very active | 2d ago | 3mo | 6 |
| [LiveBench/LiveBench](https://github.com/LiveBench/LiveBench) | Benchmark / leaderboard | Python | NOASSERTION | 1,178 | Mature | 55 | very active | 3d ago | 1.9y | 2 |
| [vllm-project/guidellm](https://github.com/vllm-project/guidellm) | Benchmark / leaderboard | Python | Apache-2.0 | 1,163 | Hot | 82 | very active | 2d ago | 2.0y | 6 |
| [cvs-health/uqlm](https://github.com/cvs-health/uqlm) | Safety / red-team | Python | Apache-2.0 | 1,157 | Hot | 74 | very active | 2d ago | 1.1y | 5 |
| [langchain-ai/openevals](https://github.com/langchain-ai/openevals) | Evaluation framework | Python | MIT | 1,062 | Hot | 80 | very active | 5d ago | 1.3y | 3 |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | Observability + eval platform | TypeScript | Apache-2.0 | 615 | Hot | 78 | very active | 2d ago | 2mo | 9 |
| [langchain-ai/agentevals](https://github.com/langchain-ai/agentevals) | Evaluation framework | Python | MIT | 600 | Hot | 58 | very active | 11d ago | 1.3y | 3 |
| [KRLabsOrg/LettuceDetect](https://github.com/KRLabsOrg/LettuceDetect) | Safety / red-team | Python | MIT | 576 | Mature | 48 | active | 4d ago | 1.3y | 1 |
| [rhesis-ai/rhesis](https://github.com/rhesis-ai/rhesis) | Evaluation framework | Python | NOASSERTION | 347 | Hot | 83 | very active | 1d ago | 1.6y | 10 |
| [finos-labs/Open-Financial-LLMs-Leaderboard](https://github.com/finos-labs/Open-Financial-LLMs-Leaderboard) | Benchmark / leaderboard | JavaScript | — | 32 | Declining | 16 | slowing | 5mo ago | 1.8y | 0 |
| [jszheng21/RACE](https://github.com/jszheng21/RACE) | Benchmark / leaderboard | Python | Apache-2.0 | 14 | Abandoned | 10 | stale | 1.6y ago | 1.9y | 0 |

## By category

### Observability + eval platform

_Capture traces from live LLM apps, attach scores, manage prompts & datasets. Online-first, but most now run offline eval suites too._

- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 27,824★ · TypeScript · Classic  
  LLM observability, metrics, evals, prompt management, datasets & playground; the most-adopted OSS platform here.  
  <sub>topics: analytics, llm, llmops, large-language-models, openai, self-hosted, ycombinator, monitoring</sub>
- **[mlflow/mlflow](https://github.com/mlflow/mlflow)** · 26,085★ · Python · Classic  
  Broad AI engineering platform; LLM tracing + evaluate + experiment tracking on top of classic MLOps.  
  <sub>topics: machine-learning, ai, ml, mlflow, apache-spark, model-management, agentops, agents</sub>
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 19,366★ · Python · Classic  
  Debug / evaluate / monitor LLM, RAG & agentic apps with tracing + automated scoring.  
  <sub>topics: open-source, langchain, openai, playground, prompt-engineering, llama-index, llm, llm-evaluation</sub>
- **[traceloop/openllmetry](https://github.com/traceloop/openllmetry)** · 7,139★ · Python · Mature  
  OpenTelemetry-native GenAI observability; standards-based traces & metrics.  
  <sub>topics: llmops, observability, open-telemetry, metrics, monitoring, opentelemetry, datascience, ml</sub>
- **[comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw)** · 615★ · TypeScript · Hot  
  Opik plugin that exports OpenClaw agent traces (cost/tokens/errors) for monitoring.  
  <sub>topics: clawdbot, evaluation, moltbot, observability, openclaw, testing</sub>

### Evaluation framework

_Libraries to score outputs offline — reference metrics + LLM-as-a-judge — wired into CI like unit tests._

- **[confident-ai/deepeval](https://github.com/confident-ai/deepeval)** · 15,669★ · Python · Mature  
  'The LLM eval framework' — pytest-style unit tests with metrics (faithfulness, relevancy, G-Eval/LLM-as-judge).  
  <sub>topics: evaluation-metrics, evaluation-framework, llm-evaluation, llm-evaluation-framework, llm-evaluation-metrics, python</sub>
- **[langchain-ai/openevals](https://github.com/langchain-ai/openevals)** · 1,062★ · Python · Hot  
  Readymade evaluators (prebuilt prompts + scorers) for LLM apps.  
  <sub>topics: —</sub>
- **[langchain-ai/agentevals](https://github.com/langchain-ai/agentevals)** · 600★ · Python · Hot  
  Evaluators specialized for agent *trajectories* (tool-call sequences, not just final output).  
  <sub>topics: —</sub>
- **[rhesis-ai/rhesis](https://github.com/rhesis-ai/rhesis)** · 347★ · Python · Hot  
  Testing platform that lets engineers + PMs + domain experts generate and run test suites.  
  <sub>topics: llm-evaluation, open-source, quality-assessment, responsible-ai, test-execution, test-generation, test-management, generative-ai</sub>

### Benchmark / leaderboard

_Fixed task sets that rank models/agents. Watch for contamination (LiveBench is explicitly designed against it)._

- **[pinchbench/skill](https://github.com/pinchbench/skill)** · 1,195★ · Python · Hot  
  Benchmarks LLMs as OpenClaw *coding agents* on real tasks.  
  <sub>topics: —</sub>
- **[LiveBench/LiveBench](https://github.com/LiveBench/LiveBench)** · 1,178★ · Python · Mature  
  Challenging, contamination-free benchmark refreshed over time to resist training-set leakage.  
  <sub>topics: —</sub>
- **[vllm-project/guidellm](https://github.com/vllm-project/guidellm)** · 1,163★ · Python · Hot  
  Performance/inference benchmark: evaluate LLM *deployments* for real-world throughput/latency.  
  <sub>topics: —</sub>
- **[finos-labs/Open-Financial-LLMs-Leaderboard](https://github.com/finos-labs/Open-Financial-LLMs-Leaderboard)** · 32★ · JavaScript · Declining  
  Domain leaderboard ranking LLMs on financial tasks.  
  <sub>topics: —</sub>
- **[jszheng21/RACE](https://github.com/jszheng21/RACE)** · 14★ · Python · Abandoned  
  Multi-dimensional code-generation benchmark (Readability, Maintainability, Correctness, Efficiency).  
  <sub>topics: benchmark, code-generation, multidimensional, llm</sub>

### Safety / red-team

_Adversarial testing, vulnerability scanning, and hallucination / uncertainty detection — evaluating *failure modes* rather than task accuracy._

- **[NVIDIA/garak](https://github.com/NVIDIA/garak)** · 7,896★ · Python · Classic  
  LLM vulnerability scanner — probes for jailbreaks, prompt injection, toxicity, data leakage.  
  <sub>topics: ai, llm-evaluation, llm-security, security-scanners, vulnerability-assessment</sub>
- **[confident-ai/deepteam](https://github.com/confident-ai/deepteam)** · 1,816★ · Python · Hot  
  Framework to red-team LLMs & LLM systems (adversarial attack suites, from the DeepEval team).  
  <sub>topics: llm-guardrails, llm-red-teaming, llm-safety, hacktoberfest, python</sub>
- **[cvs-health/uqlm](https://github.com/cvs-health/uqlm)** · 1,157★ · Python · Hot  
  Uncertainty quantification for LLMs; UQ-based hallucination detection.  
  <sub>topics: ai-evaluation, ai-safety, hallucination, hallucination-detection, hallucination-evaluation, hallucination-mitigation, llm, llm-evaluation</sub>
- **[KRLabsOrg/LettuceDetect](https://github.com/KRLabsOrg/LettuceDetect)** · 576★ · Python · Mature  
  Lightweight hallucination-detection framework for RAG outputs.  
  <sub>topics: bert, hallucination-detection, hallucination-evaluation, information-extraction, nlp, python, pytorch, token-classification</sub>

## Online vs. offline evaluation

| | What it measures | Tools in your stars |
|---|---|---|
| **Online** (production) | Live traces, cost/latency, drift, real-user feedback | `langfuse`, `mlflow`, `opik`, `openllmetry`, `opik-openclaw` |
| **Offline** (pre-ship) | Metric scores on datasets, regression gates in CI | `deepeval`, `openevals`, `agentevals`, `rhesis` |
| **Comparative** (ranking) | Model/agent leaderboards on fixed tasks | `LiveBench`, `pinchbench`, `guidellm`, `RACE`, `Open-Financial-LLMs-Leaderboard` |
| **Adversarial** (safety) | Jailbreaks, injection, hallucination, uncertainty | `garak`, `deepteam`, `uqlm`, `LettuceDetect` |

## Graph analysis — how they relate

**Community clustering.** These 18 tools span **11 of the graph's 23 communities** — evaluation tooling co-locates with the broader LLM-app / agent-infra clusters rather than forming an isolated island.

- **Community 18** (4): `langfuse/langfuse`, `mlflow/mlflow`, `comet-ml/opik`, `comet-ml/opik-openclaw`
- **Community 2** (2): `confident-ai/deepeval`, `confident-ai/deepteam`
- **Community 12** (2): `langchain-ai/openevals`, `langchain-ai/agentevals`
- **Community 5** (2): `LiveBench/LiveBench`, `pinchbench/skill`
- **Community 15** (2): `vllm-project/guidellm`, `jszheng21/RACE`

**Centrality (PageRank in the full 1,071-repo graph)** — how 'hub-like' each tool is within your starred ecosystem:

- `NVIDIA/garak` — PageRank 0.0023
- `comet-ml/opik` — PageRank 0.0014
- `comet-ml/opik-openclaw` — PageRank 0.0014
- `langchain-ai/openevals` — PageRank 0.0012
- `langchain-ai/agentevals` — PageRank 0.0012
- `confident-ai/deepteam` — PageRank 0.0011
- `confident-ai/deepeval` — PageRank 0.0011
- `vllm-project/guidellm` — PageRank 0.0010

**Direct links between eval tools** (similarity edges where both endpoints are in this report):

- `langchain-ai/agentevals` ⇄ `langchain-ai/openevals` (w=1.550) — authors: jkennedyvz, dependabot[bot]
- `confident-ai/deepteam` ⇄ `confident-ai/deepeval` (w=1.450) — topics: python; authors: A-Vamshi, penguine-ip
- `comet-ml/opik-openclaw` ⇄ `comet-ml/opik` (w=0.822) — topics: evaluation; authors: YarivHashaiComet, dependabot[bot], Nimrod007
- `langfuse/langfuse` ⇄ `comet-ml/opik` (w=0.573) — topics: llm, llmops, openai, open-source; authors: dependabot[bot]
- `mlflow/mlflow` ⇄ `comet-ml/opik` (w=0.342) — topics: evaluation, langchain, llm-evaluation, llmops
- `langfuse/langfuse` ⇄ `mlflow/mlflow` (w=0.276) — topics: llmops, openai, observability, open-source
- `langfuse/langfuse` ⇄ `comet-ml/opik-openclaw` (w=0.217) — topics: observability, evaluation; authors: dependabot[bot]
- `langfuse/langfuse` ⇄ `traceloop/openllmetry` (w=0.217) — topics: llm, llmops, monitoring, observability; authors: dependabot[bot]
- `rhesis-ai/rhesis` ⇄ `comet-ml/opik` (w=0.193) — topics: llm-evaluation, open-source, llmops
- `rhesis-ai/rhesis` ⇄ `confident-ai/deepeval` (w=0.183) — topics: llm-evaluation, llm-evaluation-framework

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| comet-ml/opik | 94 | Classic | very active | 4 | 24% | 466 |
| langfuse/langfuse | 89 | Classic | very active | 3 | 20% | 563 |
| traceloop/openllmetry | 85 | Mature | very active | 3 | 22% | 257 |
| rhesis-ai/rhesis | 83 | Hot | very active | 2 | 30% | 132 |
| mlflow/mlflow | 82 | Classic | very active | 2 | 38% | 169 |
| vllm-project/guidellm | 82 | Hot | very active | 2 | 32% | 12 |
| langchain-ai/openevals | 80 | Hot | very active | 2 | 36% | 41 |
| pinchbench/skill | 79 | Hot | very active | 1 | 88% | 14 |
| comet-ml/opik-openclaw | 78 | Hot | very active | 1 | 80% | 25 |
| confident-ai/deepeval | 77 | Mature | very active | 1 | 54% | 55 |
| NVIDIA/garak | 77 | Classic | very active | 1 | 58% | 30 |
| cvs-health/uqlm | 74 | Hot | very active | 1 | 79% | 38 |
| confident-ai/deepteam | 59 | Hot | very active | 1 | 57% | 3 |
| langchain-ai/agentevals | 58 | Hot | very active | 1 | 58% | 12 |
| LiveBench/LiveBench | 55 | Mature | very active | 1 | 75% | 0 |
| KRLabsOrg/LettuceDetect | 48 | Mature | active | 1 | 100% | 9 |
| finos-labs/Open-Financial-LLMs-Leaderboard | 16 | Declining | slowing | 0 | 0% | 0 |
| jszheng21/RACE | 10 | Abandoned | stale | 0 | 0% | 0 |

## Which one should you use?

| If you want… | Start with | Why |
|---|---|---|
| End-to-end observability + evals for a production app | `langfuse/langfuse` | Most-starred OSS platform here; tracing + evals + prompt mgmt + datasets, TS-friendly. |
| Offline eval as CI unit tests (LLM-as-judge) | `confident-ai/deepeval` | Pytest-style metrics (faithfulness, relevancy, G-Eval); largest dedicated framework. |
| To evaluate agent *trajectories*, not just answers | `langchain-ai/agentevals` | Scores tool-call sequences / multi-step behavior. |
| Standards-based tracing (vendor-neutral) | `traceloop/openllmetry` | Built on OpenTelemetry; plugs into existing observability stacks. |
| To red-team / security-scan a model | `NVIDIA/garak` + `confident-ai/deepteam` | garak = vulnerability scanner; deepteam = adversarial attack framework. |
| Hallucination / uncertainty detection | `cvs-health/uqlm` or `KRLabsOrg/LettuceDetect` | UQ-based detection; LettuceDetect targets RAG outputs specifically. |
| A contamination-resistant model leaderboard | `LiveBench/LiveBench` | Refreshed tasks designed to resist training-set leakage. |
| To benchmark coding agents | `pinchbench/skill` | Runs LLMs as coding agents on real tasks. |

## Notably absent from your stars

Several widely-used evaluation tools are **not** in this dataset — worth knowing when treating the above as a complete picture:

- **explodinggradients/ragas** — the standard RAG evaluation metric library
- **promptfoo/promptfoo** — popular CLI for prompt/eval testing & red-teaming
- **openai/evals** — OpenAI's eval registry/framework
- **EleutherAI/lm-evaluation-harness** — de-facto academic benchmark harness
- **Arize-ai/phoenix** — open-source LLM tracing & eval
- **huggingface/lighteval** — HF's lightweight eval suite
- **stanford-crfm/helm** — holistic benchmark from Stanford
- **truera/trulens** — feedback-function evaluation

## Methodology & caveats

- **Source**: `public/data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible via the generator script.
- **Selection**: keyword scan (eval/benchmark/leaderboard/red-team/guardrail/observability/hallucination + LLM/agent signals) across name/description/topics/README, then manual curation. Adjacent-but-excluded: RAG engines, vector DBs, LLM gateways (e.g. `litellm`), and agent frameworks that merely *embed* an eval module.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 18 · Snapshot: 2026-05-24T19:57:47.245Z</sub>
