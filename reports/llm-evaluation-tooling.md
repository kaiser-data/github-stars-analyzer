# LLM Evaluation Tooling — Landscape Report

> Derived from **kaiser-data**'s 1,327 starred repos (snapshot `2026-07-13T08:42:30.177Z`), cross-referenced with the repo-similarity graph (1,327 nodes / 4,302 edges, 27 communities).
>
> Generated 2026-07-13 by `scripts/reports/llm_evaluation.py` (regenerate any time — no API cost).

![Top tools by stars](assets/llm-evaluation-tooling-top-tools.svg)

![Tools per category](assets/llm-evaluation-tooling-categories.svg)


## Executive summary

- **24 evaluation-focused tools** found in your stars (**193,521★** combined), spanning four categories:
  - **Observability + eval platform** (5): `langfuse`, `mlflow`, `opik`, `openllmetry`, `opik-openclaw`
  - **Evaluation framework** (8): `promptfoo`, `evals`, `deepeval`, `phoenix`, `trulens`, `openevals`, `agentevals`, `rhesis`
  - **Benchmark / leaderboard** (7): `lm-evaluation-harness`, `lighteval`, `guidellm`, `skill`, `LiveBench`, `Open-Financial-LLMs-Leaderboard`, `RACE`
  - **Safety / red-team** (4): `garak`, `deepteam`, `uqlm`, `LettuceDetect`
- The field splits cleanly into **online** evaluation (tracing/observability in production) and **offline** evaluation (datasets, metrics, benchmarks before ship). Platforms increasingly do both.
- Evaluation method has converged on **LLM-as-a-judge** (deepeval, openevals) alongside classic reference metrics, plus a fast-growing **safety/red-team** wing (garak, deepteam) and **hallucination detection** (uqlm, LettuceDetect).
- Python dominates (20/24); the lone TypeScript-first platform is Langfuse.

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Observability + eval platform | TypeScript | NOASSERTION | 31,012 (▲2,083) | Classic | 94 | very active | 0d ago | 3.2y | 19 |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | Observability + eval platform | Python | Apache-2.0 | 26,998 (▲556) | Classic | 92 | very active | 0d ago | 8.1y | 29 |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | Evaluation framework | TypeScript | MIT | 23,183 (▲1,061) | Classic | 84 | very active | 0d ago | 3.2y | 16 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Observability + eval platform | Python | Apache-2.0 | 20,575 (▲996) | Classic | 94 | very active | 0d ago | 3.2y | 22 |
| [openai/evals](https://github.com/openai/evals) | Evaluation framework | Python | NOASSERTION | 18,906 (▲236) | Mature | 34 | slowing | 3mo ago | 3.5y | 1 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | Evaluation framework | Python | Apache-2.0 | 16,795 (▲685) | Mature | 76 | very active | 1d ago | 2.9y | 18 |
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | Benchmark / leaderboard | Python | MIT | 13,267 (▲346) | Classic | 80 | very active | 19d ago | 5.9y | 28 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Evaluation framework | Python | NOASSERTION | 10,528 (▲428) | Classic | 79 | very active | 0d ago | 3.7y | 13 |
| [NVIDIA/garak](https://github.com/NVIDIA/garak) | Safety / red-team | Python | Apache-2.0 | 8,406 (▲324) | Classic | 82 | very active | 3d ago | 3.2y | 22 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Observability + eval platform | Python | Apache-2.0 | 7,293 (▲103) | Mature | 72 | very active | 2d ago | 2.9y | 11 |
| [truera/trulens](https://github.com/truera/trulens) | Evaluation framework | Python | MIT | 3,436 (▲63) | Classic | 84 | very active | 2d ago | 5.7y | 17 |
| [huggingface/lighteval](https://github.com/huggingface/lighteval) | Benchmark / leaderboard | Python | MIT | 2,473 (▲31) | Mature | 60 | active | 14d ago | 2.5y | 6 |
| [confident-ai/deepteam](https://github.com/confident-ai/deepteam) | Safety / red-team | Python | Apache-2.0 | 2,131 (▲251) | Hot | 60 | very active | 5d ago | 1.4y | 4 |
| [vllm-project/guidellm](https://github.com/vllm-project/guidellm) | Benchmark / leaderboard | Python | Apache-2.0 | 1,386 (▲138) | Mature | 83 | very active | 0d ago | 2.1y | 14 |
| [pinchbench/skill](https://github.com/pinchbench/skill) | Benchmark / leaderboard | Python | MIT | 1,275 (▲48) | Hot | 78 | very active | 11d ago | 5mo | 6 |
| [LiveBench/LiveBench](https://github.com/LiveBench/LiveBench) | Benchmark / leaderboard | Python | NOASSERTION | 1,235 (▲40) | Mature | 60 | very active | 3d ago | 2.1y | 3 |
| [cvs-health/uqlm](https://github.com/cvs-health/uqlm) | Safety / red-team | Python | Apache-2.0 | 1,184 (▲18) | Hot | 73 | very active | 4d ago | 1.2y | 5 |
| [langchain-ai/openevals](https://github.com/langchain-ai/openevals) | Evaluation framework | Python | MIT | 1,114 (▲44) | Mature | 69 | very active | 11d ago | 1.4y | 2 |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | Observability + eval platform | TypeScript | Apache-2.0 | 670 (▲50) | Hot | 72 | very active | 7d ago | 4mo | 6 |
| [langchain-ai/agentevals](https://github.com/langchain-ai/agentevals) | Evaluation framework | Python | MIT | 644 (▲29) | Mature | 61 | very active | 2d ago | 1.4y | 4 |
| [KRLabsOrg/LettuceDetect](https://github.com/KRLabsOrg/LettuceDetect) | Safety / red-team | Python | MIT | 584 (▲7) | Hot | 67 | very active | 2d ago | 1.4y | 7 |
| [rhesis-ai/rhesis](https://github.com/rhesis-ai/rhesis) | Evaluation framework | Python | NOASSERTION | 379 (▲17) | Hot | 88 | very active | 0d ago | 1.8y | 11 |
| [finos-labs/Open-Financial-LLMs-Leaderboard](https://github.com/finos-labs/Open-Financial-LLMs-Leaderboard) | Benchmark / leaderboard | JavaScript | — | 33 (▲1) | Declining | 12 | stale | 7mo ago | 1.9y | 0 |
| [jszheng21/RACE](https://github.com/jszheng21/RACE) | Benchmark / leaderboard | Python | Apache-2.0 | 14 | Abandoned | 10 | stale | 1.8y ago | 2.0y | 0 |

## By category

### Observability + eval platform

_Capture traces from live LLM apps, attach scores, manage prompts & datasets. Online-first, but most now run offline eval suites too._

- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 31,012★ · TypeScript · Classic  
  LLM observability, metrics, evals, prompt management, datasets & playground; the most-adopted OSS platform here.  
  <sub>topics: analytics, llm, llmops, large-language-models, openai, self-hosted, ycombinator, monitoring</sub>
- **[mlflow/mlflow](https://github.com/mlflow/mlflow)** · 26,998★ · Python · Classic  
  Broad AI engineering platform; LLM tracing + evaluate + experiment tracking on top of classic MLOps.  
  <sub>topics: machine-learning, ai, ml, mlflow, apache-spark, model-management, agentops, agents</sub>
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 20,575★ · Python · Classic  
  Debug / evaluate / monitor LLM, RAG & agentic apps with tracing + automated scoring.  
  <sub>topics: open-source, langchain, openai, playground, prompt-engineering, llama-index, llm, llm-evaluation</sub>
- **[traceloop/openllmetry](https://github.com/traceloop/openllmetry)** · 7,293★ · Python · Mature  
  OpenTelemetry-native GenAI observability; standards-based traces & metrics.  
  <sub>topics: llmops, observability, open-telemetry, metrics, monitoring, opentelemetry, datascience, ml</sub>
- **[comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw)** · 670★ · TypeScript · Hot  
  Opik plugin that exports OpenClaw agent traces (cost/tokens/errors) for monitoring.  
  <sub>topics: clawdbot, evaluation, moltbot, observability, openclaw, testing</sub>

### Evaluation framework

_Libraries to score outputs offline — reference metrics + LLM-as-a-judge — wired into CI like unit tests._

- **[promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)** · 23,183★ · TypeScript · Classic  
  Declarative prompt/eval testing + red-teaming CLI; config-driven test matrices in CI.  
  <sub>topics: llm, prompt-engineering, prompts, llmops, prompt-testing, testing, rag, evaluation</sub>
- **[openai/evals](https://github.com/openai/evals)** · 18,906★ · Python · Mature  
  OpenAI's eval registry/framework — write & share evals against a standard harness.  
  <sub>topics: —</sub>
- **[confident-ai/deepeval](https://github.com/confident-ai/deepeval)** · 16,795★ · Python · Mature  
  'The LLM eval framework' — pytest-style unit tests with metrics (faithfulness, relevancy, G-Eval/LLM-as-judge).  
  <sub>topics: evaluation-metrics, evaluation-framework, llm-evaluation, llm-evaluation-framework, llm-evaluation-metrics, python</sub>
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 10,528★ · Python · Classic  
  Open-source LLM tracing + eval; notebook-friendly, OTel-based.  
  <sub>topics: llmops, ai-monitoring, ai-observability, llm-eval, aiengineering, datasets, agents, llms</sub>
- **[truera/trulens](https://github.com/truera/trulens)** · 3,436★ · Python · Classic  
  Feedback-function evaluation — programmatic scorers for groundedness/relevance.  
  <sub>topics: machine-learning, neural-networks, explainable-ml, llmops, ai-monitoring, ai-observability, evals, llm-evaluation</sub>
- **[langchain-ai/openevals](https://github.com/langchain-ai/openevals)** · 1,114★ · Python · Mature  
  Readymade evaluators (prebuilt prompts + scorers) for LLM apps.  
  <sub>topics: —</sub>
- **[langchain-ai/agentevals](https://github.com/langchain-ai/agentevals)** · 644★ · Python · Mature  
  Evaluators specialized for agent *trajectories* (tool-call sequences, not just final output).  
  <sub>topics: —</sub>
- **[rhesis-ai/rhesis](https://github.com/rhesis-ai/rhesis)** · 379★ · Python · Hot  
  Testing platform that lets engineers + PMs + domain experts generate and run test suites.  
  <sub>topics: llm-evaluation, open-source, quality-assessment, responsible-ai, test-execution, test-generation, test-management, generative-ai</sub>

### Benchmark / leaderboard

_Fixed task sets that rank models/agents. Watch for contamination (LiveBench is explicitly designed against it)._

- **[EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)** · 13,267★ · Python · Classic  
  The de-facto academic harness — 100+ standardized benchmarks behind the HF leaderboard.  
  <sub>topics: evaluation-framework, language-model, transformer</sub>
- **[huggingface/lighteval](https://github.com/huggingface/lighteval)** · 2,473★ · Python · Mature  
  Hugging Face's lightweight, all-in-one eval suite for fast benchmark runs.  
  <sub>topics: evaluation, evaluation-framework, evaluation-metrics, huggingface</sub>
- **[vllm-project/guidellm](https://github.com/vllm-project/guidellm)** · 1,386★ · Python · Mature  
  Performance/inference benchmark: evaluate LLM *deployments* for real-world throughput/latency.  
  <sub>topics: —</sub>
- **[pinchbench/skill](https://github.com/pinchbench/skill)** · 1,275★ · Python · Hot  
  Benchmarks LLMs as OpenClaw *coding agents* on real tasks.  
  <sub>topics: —</sub>
- **[LiveBench/LiveBench](https://github.com/LiveBench/LiveBench)** · 1,235★ · Python · Mature  
  Challenging, contamination-free benchmark refreshed over time to resist training-set leakage.  
  <sub>topics: —</sub>
- **[finos-labs/Open-Financial-LLMs-Leaderboard](https://github.com/finos-labs/Open-Financial-LLMs-Leaderboard)** · 33★ · JavaScript · Declining  
  Domain leaderboard ranking LLMs on financial tasks.  
  <sub>topics: —</sub>
- **[jszheng21/RACE](https://github.com/jszheng21/RACE)** · 14★ · Python · Abandoned  
  Multi-dimensional code-generation benchmark (Readability, Maintainability, Correctness, Efficiency).  
  <sub>topics: benchmark, code-generation, multidimensional, llm</sub>

### Safety / red-team

_Adversarial testing, vulnerability scanning, and hallucination / uncertainty detection — evaluating *failure modes* rather than task accuracy._

- **[NVIDIA/garak](https://github.com/NVIDIA/garak)** · 8,406★ · Python · Classic  
  LLM vulnerability scanner — probes for jailbreaks, prompt injection, toxicity, data leakage.  
  <sub>topics: ai, llm-evaluation, llm-security, security-scanners, vulnerability-assessment</sub>
- **[confident-ai/deepteam](https://github.com/confident-ai/deepteam)** · 2,131★ · Python · Hot  
  Framework to red-team LLMs & LLM systems (adversarial attack suites, from the DeepEval team).  
  <sub>topics: llm-guardrails, llm-red-teaming, llm-safety, python, llm-seecurity</sub>
- **[cvs-health/uqlm](https://github.com/cvs-health/uqlm)** · 1,184★ · Python · Hot  
  Uncertainty quantification for LLMs; UQ-based hallucination detection.  
  <sub>topics: ai-evaluation, ai-safety, hallucination, hallucination-detection, hallucination-evaluation, hallucination-mitigation, llm, llm-evaluation</sub>
- **[KRLabsOrg/LettuceDetect](https://github.com/KRLabsOrg/LettuceDetect)** · 584★ · Python · Hot  
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

**Community clustering.** These 24 tools span **9 of the graph's 27 communities** — evaluation tooling co-locates with the broader LLM-app / agent-infra clusters rather than forming an isolated island.

- **Community 22** (7): `langfuse/langfuse`, `mlflow/mlflow`, `comet-ml/opik`, `comet-ml/opik-openclaw`, `promptfoo/promptfoo`, `Arize-ai/phoenix`, `truera/trulens`
- **Community 19** (7): `confident-ai/deepeval`, `vllm-project/guidellm`, `jszheng21/RACE`, `EleutherAI/lm-evaluation-harness`, `huggingface/lighteval`, `confident-ai/deepteam`, `cvs-health/uqlm`
- **Community 7** (2): `langchain-ai/openevals`, `langchain-ai/agentevals`
- **Community 12** (2): `openai/evals`, `KRLabsOrg/LettuceDetect`
- **Community 0** (2): `LiveBench/LiveBench`, `pinchbench/skill`

**Centrality (PageRank in the full 1,071-repo graph)** — how 'hub-like' each tool is within your starred ecosystem:

- `NVIDIA/garak` — PageRank 0.0018
- `comet-ml/opik` — PageRank 0.0015
- `openai/evals` — PageRank 0.0012
- `langchain-ai/openevals` — PageRank 0.0012
- `langchain-ai/agentevals` — PageRank 0.0011
- `comet-ml/opik-openclaw` — PageRank 0.0011
- `huggingface/lighteval` — PageRank 0.0011
- `langfuse/langfuse` — PageRank 0.0009

**Direct links between eval tools** (similarity edges where both endpoints are in this report):

- `langchain-ai/agentevals` ⇄ `langchain-ai/openevals` (w=1.550) — authors: jkennedyvz, dependabot[bot]
- `confident-ai/deepteam` ⇄ `confident-ai/deepeval` (w=0.966) — topics: python; authors: A-Vamshi, penguine-ip, kritinv
- `comet-ml/opik-openclaw` ⇄ `comet-ml/opik` (w=0.709) — topics: evaluation; authors: YarivHashaiComet, dependabot[bot]
- `langfuse/langfuse` ⇄ `comet-ml/opik` (w=0.574) — topics: llm, llmops, openai, open-source; authors: dependabot[bot]
- `truera/trulens` ⇄ `Arize-ai/phoenix` (w=0.368) — topics: llmops, ai-monitoring, ai-observability, evals
- `mlflow/mlflow` ⇄ `comet-ml/opik` (w=0.342) — topics: evaluation, langchain, llm-evaluation, llmops
- `huggingface/lighteval` ⇄ `confident-ai/deepeval` (w=0.300) — topics: evaluation-framework, evaluation-metrics
- `langfuse/langfuse` ⇄ `mlflow/mlflow` (w=0.276) — topics: llmops, openai, observability, open-source
- `Arize-ai/phoenix` ⇄ `mlflow/mlflow` (w=0.264) — topics: llmops, agents, prompt-engineering, llm-evaluation
- `promptfoo/promptfoo` ⇄ `comet-ml/opik` (w=0.246) — topics: llm, prompt-engineering, llmops, evaluation; authors: anxkhn
- `langfuse/langfuse` ⇄ `traceloop/openllmetry` (w=0.225) — topics: llm, llmops, monitoring, observability; authors: dependabot[bot]
- `EleutherAI/lm-evaluation-harness` ⇄ `confident-ai/deepeval` (w=0.219) — topics: evaluation-framework; authors: bongho
- `huggingface/lighteval` ⇄ `EleutherAI/lm-evaluation-harness` (w=0.217) — topics: evaluation-framework
- `promptfoo/promptfoo` ⇄ `langfuse/langfuse` (w=0.206) — topics: llm, prompt-engineering, llmops, evaluation
- `rhesis-ai/rhesis` ⇄ `comet-ml/opik` (w=0.193) — topics: llm-evaluation, open-source, llmops
- `rhesis-ai/rhesis` ⇄ `confident-ai/deepeval` (w=0.183) — topics: llm-evaluation, llm-evaluation-framework
- `cvs-health/uqlm` ⇄ `KRLabsOrg/LettuceDetect` (w=0.150) — topics: hallucination-detection, hallucination-evaluation
- `cvs-health/uqlm` ⇄ `comet-ml/opik` (w=0.130) — topics: llm, llm-evaluation

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| langfuse/langfuse | 94 | Classic | very active | 4 | 17% | 614 |
| comet-ml/opik | 94 | Classic | very active | 4 | 19% | 517 |
| mlflow/mlflow | 92 | Classic | very active | 4 | 20% | 171 |
| rhesis-ai/rhesis | 88 | Hot | very active | 3 | 25% | 140 |
| promptfoo/promptfoo | 84 | Classic | very active | 2 | 41% | 418 |
| truera/trulens | 84 | Classic | very active | 3 | 28% | 119 |
| vllm-project/guidellm | 83 | Mature | very active | 2 | 38% | 15 |
| NVIDIA/garak | 82 | Classic | very active | 2 | 46% | 31 |
| EleutherAI/lm-evaluation-harness | 80 | Classic | very active | 4 | 26% | 18 |
| Arize-ai/phoenix | 79 | Classic | very active | 1 | 68% | 745 |
| pinchbench/skill | 78 | Hot | very active | 1 | 88% | 14 |
| confident-ai/deepeval | 76 | Mature | very active | 1 | 50% | 57 |
| cvs-health/uqlm | 73 | Hot | very active | 1 | 73% | 41 |
| traceloop/openllmetry | 72 | Mature | very active | 1 | 50% | 260 |
| comet-ml/opik-openclaw | 72 | Hot | very active | 1 | 67% | 25 |
| langchain-ai/openevals | 69 | Mature | very active | 1 | 54% | 41 |
| KRLabsOrg/LettuceDetect | 67 | Hot | very active | 1 | 86% | 12 |
| langchain-ai/agentevals | 61 | Mature | very active | 2 | 48% | 12 |
| LiveBench/LiveBench | 60 | Mature | very active | 1 | 57% | 0 |
| huggingface/lighteval | 60 | Mature | active | 1 | 58% | 15 |
| confident-ai/deepteam | 60 | Hot | very active | 1 | 62% | 3 |
| openai/evals | 34 | Mature | slowing | 1 | 100% | 0 |
| finos-labs/Open-Financial-LLMs-Leaderboard | 12 | Declining | stale | 0 | 0% | 0 |
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

- **explodinggradients/ragas** — the standard RAG eval metric library (you hold the fork `vibrantlabsai/ragas`)
- **stanford-crfm/helm** — holistic benchmark from Stanford

## Methodology & caveats

- **Source**: `data/classified.json` + `public/data/graph.json`. No external calls; fully reproducible via the generator script.
- **Selection**: keyword scan (eval/benchmark/leaderboard/red-team/guardrail/observability/hallucination + LLM/agent signals) across name/description/topics/README, then manual curation. Adjacent-but-excluded: RAG engines, vector DBs, LLM gateways (e.g. `litellm`), and agent frameworks that merely *embed* an eval module.
- **Metrics** (health, lifecycle, bus_factor) are precomputed at snapshot time and may lag GitHub's current state.
- Re-run after a fresh `classified.json` to refresh stars/activity.

<sub>Tools covered: 24 · Snapshot: 2026-07-13T08:42:30.177Z</sub>
