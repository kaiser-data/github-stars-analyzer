# LLM Evaluation Tooling — Landscape Report

> Derived from **kaiser-data**'s 2,243 starred repos (snapshot `2026-09-25T10:37:19.717Z`), cross-referenced with the repo-similarity graph (2,243 nodes / 7,393 edges, 35 communities).
>
> Generated 2026-09-25 by `scripts/reports/llm_evaluation.py` (regenerate any time — no API cost).

![Top tools by stars](assets/llm-evaluation-tooling-top-tools.svg)

![Tools per category](assets/llm-evaluation-tooling-categories.svg)


## Executive summary

- **24 evaluation-focused tools** found in your stars (**209,569★** combined), spanning four categories:
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
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Observability + eval platform | TypeScript | NOASSERTION | 35,033 (▲150) | Classic | 89 | very active | 0d ago | 3.4y | 21 |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | Observability + eval platform | Python | Apache-2.0 | 28,133 (▲61) | Classic | 92 | very active | 0d ago | 8.3y | 28 |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | Evaluation framework | TypeScript | MIT | 25,439 (▲109) | Classic | 89 | very active | 0d ago | 3.4y | 28 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Observability + eval platform | Python | Apache-2.0 | 22,230 (▲51) | Classic | 93 | very active | 0d ago | 3.4y | 22 |
| [openai/evals](https://github.com/openai/evals) | Evaluation framework | Python | NOASSERTION | 19,505 (▲17) | Mature | 21 | slowing | 5mo ago | 3.7y | 0 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | Evaluation framework | Python | Apache-2.0 | 18,437 (▲72) | Classic | 76 | very active | 1d ago | 3.1y | 8 |
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | Benchmark / leaderboard | Python | MIT | 14,073 (▲30) | Classic | 88 | very active | 11d ago | 6.1y | 54 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Evaluation framework | Python | NOASSERTION | 11,609 (▲48) | Classic | 79 | very active | 0d ago | 3.9y | 17 |
| [NVIDIA/garak](https://github.com/NVIDIA/garak) | Safety / red-team | Python | Apache-2.0 | 9,351 (▲29) | Classic | 81 | very active | 9d ago | 3.4y | 21 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Observability + eval platform | Python | Apache-2.0 | 7,447 (▲6) | Classic | 70 | active | 1d ago | 3.1y | 7 |
| [truera/trulens](https://github.com/truera/trulens) | Evaluation framework | Python | MIT | 3,571 (▲3) | Classic | 100 | very active | 0d ago | 5.9y | 36 |
| [confident-ai/deepteam](https://github.com/confident-ai/deepteam) | Safety / red-team | Python | Apache-2.0 | 2,949 (▲51) | Hot | 55 | very active | 4d ago | 1.6y | 5 |
| [huggingface/lighteval](https://github.com/huggingface/lighteval) | Benchmark / leaderboard | Python | MIT | 2,549 (▲2) | Mature | 59 | active | 2d ago | 2.7y | 5 |
| [vllm-project/guidellm](https://github.com/vllm-project/guidellm) | Benchmark / leaderboard | Python | Apache-2.0 | 1,642 (▲11) | Mature | 93 | very active | 0d ago | 2.3y | 28 |
| [pinchbench/skill](https://github.com/pinchbench/skill) | Benchmark / leaderboard | Python | MIT | 1,350 (▲1) | Declining | 47 | slowing | 2mo ago | 7mo | 0 |
| [LiveBench/LiveBench](https://github.com/LiveBench/LiveBench) | Benchmark / leaderboard | Python | NOASSERTION | 1,329 (▲4) | Mature | 65 | very active | 3d ago | 2.3y | 5 |
| [langchain-ai/openevals](https://github.com/langchain-ai/openevals) | Evaluation framework | Python | MIT | 1,207 (▲1) | Hot | 77 | very active | 6d ago | 1.6y | 5 |
| [cvs-health/uqlm](https://github.com/cvs-health/uqlm) | Safety / red-team | Python | Apache-2.0 | 1,202 (▲1) | Hot | 76 | very active | 4d ago | 1.4y | 7 |
| [langchain-ai/agentevals](https://github.com/langchain-ai/agentevals) | Evaluation framework | Python | MIT | 732 (▲5) | Declining | 37 | slowing | 2mo ago | 1.6y | 2 |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | Observability + eval platform | TypeScript | Apache-2.0 | 724 (▼1) | Declining | 60 | active | 10d ago | 6mo | 2 |
| [KRLabsOrg/LettuceDetect](https://github.com/KRLabsOrg/LettuceDetect) | Safety / red-team | Python | MIT | 611 | Mature | 59 | very active | 18d ago | 1.6y | 8 |
| [rhesis-ai/rhesis](https://github.com/rhesis-ai/rhesis) | Evaluation framework | Python | NOASSERTION | 395 (▲3) | Hot | 79 | very active | 0d ago | 2.0y | 5 |
| [finos-labs/Open-Financial-LLMs-Leaderboard](https://github.com/finos-labs/Open-Financial-LLMs-Leaderboard) | Benchmark / leaderboard | JavaScript | — | 37 | Declining | 6 | stale | 9mo ago | 2.1y | 0 |
| [jszheng21/RACE](https://github.com/jszheng21/RACE) | Benchmark / leaderboard | Python | Apache-2.0 | 14 | Abandoned | 10 | stale | 2.0y ago | 2.2y | 0 |

## By category

### Observability + eval platform

_Capture traces from live LLM apps, attach scores, manage prompts & datasets. Online-first, but most now run offline eval suites too._

- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 35,033★ · TypeScript · Classic  
  LLM observability, metrics, evals, prompt management, datasets & playground; the most-adopted OSS platform here.  
  <sub>topics: analytics, llm, llmops, large-language-models, openai, self-hosted, ycombinator, monitoring</sub>
- **[mlflow/mlflow](https://github.com/mlflow/mlflow)** · 28,133★ · Python · Classic  
  Broad AI engineering platform; LLM tracing + evaluate + experiment tracking on top of classic MLOps.  
  <sub>topics: machine-learning, ai, ml, mlflow, apache-spark, model-management, agentops, agents</sub>
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 22,230★ · Python · Classic  
  Debug / evaluate / monitor LLM, RAG & agentic apps with tracing + automated scoring.  
  <sub>topics: open-source, langchain, openai, playground, prompt-engineering, llama-index, llm, llm-evaluation</sub>
- **[traceloop/openllmetry](https://github.com/traceloop/openllmetry)** · 7,447★ · Python · Classic  
  OpenTelemetry-native GenAI observability; standards-based traces & metrics.  
  <sub>topics: llmops, observability, open-telemetry, metrics, monitoring, opentelemetry, datascience, ml</sub>
- **[comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw)** · 724★ · TypeScript · Declining  
  Opik plugin that exports OpenClaw agent traces (cost/tokens/errors) for monitoring.  
  <sub>topics: clawdbot, evaluation, moltbot, observability, openclaw, testing, ai-agents, llm-observability</sub>

### Evaluation framework

_Libraries to score outputs offline — reference metrics + LLM-as-a-judge — wired into CI like unit tests._

- **[promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)** · 25,439★ · TypeScript · Classic  
  Declarative prompt/eval testing + red-teaming CLI; config-driven test matrices in CI.  
  <sub>topics: llm, prompt-engineering, prompts, llmops, prompt-testing, testing, rag, evaluation</sub>
- **[openai/evals](https://github.com/openai/evals)** · 19,505★ · Python · Mature  
  OpenAI's eval registry/framework — write & share evals against a standard harness.  
  <sub>topics: —</sub>
- **[confident-ai/deepeval](https://github.com/confident-ai/deepeval)** · 18,437★ · Python · Classic  
  'The LLM eval framework' — pytest-style unit tests with metrics (faithfulness, relevancy, G-Eval/LLM-as-judge).  
  <sub>topics: evaluation-metrics, evaluation-framework, llm-evaluation, llm-evaluation-framework, llm-evaluation-metrics, python</sub>
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 11,609★ · Python · Classic  
  Open-source LLM tracing + eval; notebook-friendly, OTel-based.  
  <sub>topics: llmops, ai-monitoring, ai-observability, llm-eval, aiengineering, datasets, agents, llms</sub>
- **[truera/trulens](https://github.com/truera/trulens)** · 3,571★ · Python · Classic  
  Feedback-function evaluation — programmatic scorers for groundedness/relevance.  
  <sub>topics: machine-learning, neural-networks, explainable-ml, llmops, ai-monitoring, ai-observability, evals, llm-evaluation</sub>
- **[langchain-ai/openevals](https://github.com/langchain-ai/openevals)** · 1,207★ · Python · Hot  
  Readymade evaluators (prebuilt prompts + scorers) for LLM apps.  
  <sub>topics: —</sub>
- **[langchain-ai/agentevals](https://github.com/langchain-ai/agentevals)** · 732★ · Python · Declining  
  Evaluators specialized for agent *trajectories* (tool-call sequences, not just final output).  
  <sub>topics: —</sub>
- **[rhesis-ai/rhesis](https://github.com/rhesis-ai/rhesis)** · 395★ · Python · Hot  
  Testing platform that lets engineers + PMs + domain experts generate and run test suites.  
  <sub>topics: llmops, annotations, feedback-loop, hypothesis-testing, regression-testing, systematic-evaluation</sub>

### Benchmark / leaderboard

_Fixed task sets that rank models/agents. Watch for contamination (LiveBench is explicitly designed against it)._

- **[EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)** · 14,073★ · Python · Classic  
  The de-facto academic harness — 100+ standardized benchmarks behind the HF leaderboard.  
  <sub>topics: evaluation-framework, language-model, transformer</sub>
- **[huggingface/lighteval](https://github.com/huggingface/lighteval)** · 2,549★ · Python · Mature  
  Hugging Face's lightweight, all-in-one eval suite for fast benchmark runs.  
  <sub>topics: evaluation, evaluation-framework, evaluation-metrics, huggingface</sub>
- **[vllm-project/guidellm](https://github.com/vllm-project/guidellm)** · 1,642★ · Python · Mature  
  Performance/inference benchmark: evaluate LLM *deployments* for real-world throughput/latency.  
  <sub>topics: —</sub>
- **[pinchbench/skill](https://github.com/pinchbench/skill)** · 1,350★ · Python · Declining  
  Benchmarks LLMs as OpenClaw *coding agents* on real tasks.  
  <sub>topics: —</sub>
- **[LiveBench/LiveBench](https://github.com/LiveBench/LiveBench)** · 1,329★ · Python · Mature  
  Challenging, contamination-free benchmark refreshed over time to resist training-set leakage.  
  <sub>topics: —</sub>
- **[finos-labs/Open-Financial-LLMs-Leaderboard](https://github.com/finos-labs/Open-Financial-LLMs-Leaderboard)** · 37★ · JavaScript · Declining  
  Domain leaderboard ranking LLMs on financial tasks.  
  <sub>topics: —</sub>
- **[jszheng21/RACE](https://github.com/jszheng21/RACE)** · 14★ · Python · Abandoned  
  Multi-dimensional code-generation benchmark (Readability, Maintainability, Correctness, Efficiency).  
  <sub>topics: benchmark, code-generation, multidimensional, llm</sub>

### Safety / red-team

_Adversarial testing, vulnerability scanning, and hallucination / uncertainty detection — evaluating *failure modes* rather than task accuracy._

- **[NVIDIA/garak](https://github.com/NVIDIA/garak)** · 9,351★ · Python · Classic  
  LLM vulnerability scanner — probes for jailbreaks, prompt injection, toxicity, data leakage.  
  <sub>topics: ai, llm-evaluation, llm-security, security-scanners, vulnerability-assessment</sub>
- **[confident-ai/deepteam](https://github.com/confident-ai/deepteam)** · 2,949★ · Python · Hot  
  Framework to red-team LLMs & LLM systems (adversarial attack suites, from the DeepEval team).  
  <sub>topics: llm-guardrails, llm-red-teaming, llm-safety, python, llm-seecurity</sub>
- **[cvs-health/uqlm](https://github.com/cvs-health/uqlm)** · 1,202★ · Python · Hot  
  Uncertainty quantification for LLMs; UQ-based hallucination detection.  
  <sub>topics: ai-evaluation, ai-safety, hallucination, hallucination-detection, hallucination-evaluation, hallucination-mitigation, llm, llm-evaluation</sub>
- **[KRLabsOrg/LettuceDetect](https://github.com/KRLabsOrg/LettuceDetect)** · 611★ · Python · Mature  
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

**Community clustering.** These 24 tools span **11 of the graph's 35 communities** — evaluation tooling co-locates with the broader LLM-app / agent-infra clusters rather than forming an isolated island.

- **Community 21** (7): `langfuse/langfuse`, `mlflow/mlflow`, `comet-ml/opik`, `comet-ml/opik-openclaw`, `promptfoo/promptfoo`, `Arize-ai/phoenix`, `truera/trulens`
- **Community 20** (4): `confident-ai/deepeval`, `openai/evals`, `confident-ai/deepteam`, `KRLabsOrg/LettuceDetect`
- **Community 5** (3): `rhesis-ai/rhesis`, `jszheng21/RACE`, `EleutherAI/lm-evaluation-harness`
- **Community 13** (2): `langchain-ai/agentevals`, `cvs-health/uqlm`
- **Community 2** (2): `LiveBench/LiveBench`, `pinchbench/skill`

**Centrality (PageRank in the full 1,071-repo graph)** — how 'hub-like' each tool is within your starred ecosystem:

- `huggingface/lighteval` — PageRank 0.0010
- `comet-ml/opik` — PageRank 0.0009
- `langchain-ai/agentevals` — PageRank 0.0007
- `langchain-ai/openevals` — PageRank 0.0006
- `NVIDIA/garak` — PageRank 0.0006
- `vllm-project/guidellm` — PageRank 0.0005
- `confident-ai/deepeval` — PageRank 0.0005
- `langfuse/langfuse` — PageRank 0.0005

**Direct links between eval tools** (similarity edges where both endpoints are in this report):

- `confident-ai/deepteam` ⇄ `confident-ai/deepeval` (w=1.539) — topics: python; authors: A-Vamshi, tanayvaswani, kritinv
- `langchain-ai/agentevals` ⇄ `langchain-ai/openevals` (w=1.350) — authors: jkennedyvz, dependabot[bot]
- `comet-ml/opik-openclaw` ⇄ `comet-ml/opik` (w=0.687) — topics: evaluation, llm-observability; authors: GuySaar8
- `langfuse/langfuse` ⇄ `comet-ml/opik` (w=0.524) — topics: llm, llmops, openai, open-source
- `mlflow/mlflow` ⇄ `comet-ml/opik` (w=0.425) — topics: evaluation, langchain, llm-evaluation, llmops; authors: anishmehta24, dependabot[bot]
- `truera/trulens` ⇄ `Arize-ai/phoenix` (w=0.368) — topics: llmops, ai-monitoring, ai-observability, evals
- `promptfoo/promptfoo` ⇄ `comet-ml/opik` (w=0.320) — topics: llm, prompt-engineering, llmops, evaluation; authors: chuenchen309, dependabot[bot], kimnamu
- `huggingface/lighteval` ⇄ `confident-ai/deepeval` (w=0.300) — topics: evaluation-framework, evaluation-metrics
- `truera/trulens` ⇄ `comet-ml/opik` (w=0.281) — topics: llmops, llm-evaluation; authors: kimnamu, feiiiiii5, sbguangha
- `langfuse/langfuse` ⇄ `mlflow/mlflow` (w=0.276) — topics: llmops, openai, observability, open-source
- `Arize-ai/phoenix` ⇄ `mlflow/mlflow` (w=0.264) — topics: llmops, agents, prompt-engineering, llm-evaluation
- `Arize-ai/phoenix` ⇄ `comet-ml/opik` (w=0.258) — topics: llmops, prompt-engineering, llm-evaluation, openai
- `huggingface/lighteval` ⇄ `EleutherAI/lm-evaluation-harness` (w=0.217) — topics: evaluation-framework
- `promptfoo/promptfoo` ⇄ `langfuse/langfuse` (w=0.206) — topics: llm, prompt-engineering, llmops, evaluation
- `EleutherAI/lm-evaluation-harness` ⇄ `confident-ai/deepeval` (w=0.175) — topics: evaluation-framework

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| truera/trulens | 100 | Classic | very active | 5 | 21% | 126 |
| comet-ml/opik | 93 | Classic | very active | 4 | 21% | 597 |
| vllm-project/guidellm | 93 | Mature | very active | 4 | 17% | 18 |
| mlflow/mlflow | 92 | Classic | very active | 4 | 29% | 177 |
| langfuse/langfuse | 89 | Classic | very active | 3 | 23% | 700 |
| promptfoo/promptfoo | 89 | Classic | very active | 3 | 29% | 426 |
| EleutherAI/lm-evaluation-harness | 88 | Classic | very active | 11 | 10% | 19 |
| NVIDIA/garak | 81 | Classic | very active | 2 | 45% | 33 |
| rhesis-ai/rhesis | 79 | Hot | very active | 1 | 74% | 173 |
| Arize-ai/phoenix | 79 | Classic | very active | 1 | 57% | 845 |
| langchain-ai/openevals | 77 | Hot | very active | 2 | 44% | 44 |
| confident-ai/deepeval | 76 | Classic | very active | 1 | 68% | 63 |
| cvs-health/uqlm | 76 | Hot | very active | 1 | 52% | 45 |
| traceloop/openllmetry | 70 | Classic | active | 2 | 33% | 262 |
| LiveBench/LiveBench | 65 | Mature | very active | 2 | 47% | 0 |
| comet-ml/opik-openclaw | 60 | Declining | active | 1 | 50% | 25 |
| huggingface/lighteval | 59 | Mature | active | 2 | 33% | 15 |
| KRLabsOrg/LettuceDetect | 59 | Mature | very active | 1 | 68% | 13 |
| confident-ai/deepteam | 55 | Hot | very active | 1 | 56% | 3 |
| pinchbench/skill | 47 | Declining | slowing | 0 | 0% | 14 |
| langchain-ai/agentevals | 37 | Declining | slowing | 1 | 67% | 12 |
| openai/evals | 21 | Mature | slowing | 0 | 0% | 0 |
| jszheng21/RACE | 10 | Abandoned | stale | 0 | 0% | 0 |
| finos-labs/Open-Financial-LLMs-Leaderboard | 6 | Declining | stale | 0 | 0% | 0 |

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

<sub>Tools covered: 24 · Snapshot: 2026-09-25T10:37:19.717Z</sub>
