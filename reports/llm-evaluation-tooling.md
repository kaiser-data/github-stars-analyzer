# LLM Evaluation Tooling — Landscape Report

> Derived from **kaiser-data**'s 1,752 starred repos (snapshot `2026-08-28T01:21:50.535Z`), cross-referenced with the repo-similarity graph (1,752 nodes / 5,707 edges, 35 communities).
>
> Generated 2026-08-28 by `scripts/reports/llm_evaluation.py` (regenerate any time — no API cost).

![Top tools by stars](assets/llm-evaluation-tooling-top-tools.svg)

![Tools per category](assets/llm-evaluation-tooling-categories.svg)


## Executive summary

- **24 evaluation-focused tools** found in your stars (**204,169★** combined), spanning four categories:
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
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Observability + eval platform | TypeScript | NOASSERTION | 33,820 (▲1,112) | Classic | 94 | very active | 0d ago | 3.3y | 16 |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | Observability + eval platform | Python | Apache-2.0 | 27,698 (▲287) | Classic | 92 | very active | 0d ago | 8.2y | 36 |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | Evaluation framework | TypeScript | MIT | 24,623 (▲567) | Classic | 84 | very active | 0d ago | 3.3y | 10 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Observability + eval platform | Python | Apache-2.0 | 21,642 (▲445) | Classic | 93 | very active | 0d ago | 3.3y | 23 |
| [openai/evals](https://github.com/openai/evals) | Evaluation framework | Python | NOASSERTION | 19,288 (▲161) | Mature | 23 | slowing | 4mo ago | 3.6y | 0 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | Evaluation framework | Python | Apache-2.0 | 17,914 (▲446) | Classic | 81 | very active | 2d ago | 3.1y | 13 |
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | Benchmark / leaderboard | Python | MIT | 13,814 (▲245) | Classic | 86 | very active | 0d ago | 6.0y | 48 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Evaluation framework | Python | NOASSERTION | 11,218 (▲281) | Classic | 84 | very active | 0d ago | 3.8y | 19 |
| [NVIDIA/garak](https://github.com/NVIDIA/garak) | Safety / red-team | Python | Apache-2.0 | 9,048 (▲319) | Classic | 77 | very active | 2d ago | 3.3y | 15 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Observability + eval platform | Python | Apache-2.0 | 7,404 (▲44) | Mature | 66 | active | 18d ago | 3.0y | 4 |
| [truera/trulens](https://github.com/truera/trulens) | Evaluation framework | Python | MIT | 3,526 (▲36) | Classic | 98 | very active | 0d ago | 5.8y | 37 |
| [confident-ai/deepteam](https://github.com/confident-ai/deepteam) | Safety / red-team | Python | Apache-2.0 | 2,625 (▲269) | Hot | 63 | very active | 7d ago | 1.5y | 5 |
| [huggingface/lighteval](https://github.com/huggingface/lighteval) | Benchmark / leaderboard | Python | MIT | 2,530 (▲22) | Mature | 53 | active | 17d ago | 2.6y | 3 |
| [vllm-project/guidellm](https://github.com/vllm-project/guidellm) | Benchmark / leaderboard | Python | Apache-2.0 | 1,551 (▲67) | Mature | 93 | very active | 0d ago | 2.2y | 25 |
| [pinchbench/skill](https://github.com/pinchbench/skill) | Benchmark / leaderboard | Python | MIT | 1,327 (▲21) | Declining | 49 | active | 1mo ago | 6mo | 0 |
| [LiveBench/LiveBench](https://github.com/LiveBench/LiveBench) | Benchmark / leaderboard | Python | NOASSERTION | 1,295 (▲21) | Mature | 66 | very active | 1d ago | 2.2y | 6 |
| [cvs-health/uqlm](https://github.com/cvs-health/uqlm) | Safety / red-team | Python | Apache-2.0 | 1,192 (▲4) | Hot | 76 | very active | 2d ago | 1.4y | 6 |
| [langchain-ai/openevals](https://github.com/langchain-ai/openevals) | Evaluation framework | Python | MIT | 1,181 (▲25) | Hot | 79 | very active | 8d ago | 1.6y | 4 |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | Observability + eval platform | TypeScript | Apache-2.0 | 725 (▲14) | Declining | 59 | active | 0d ago | 5mo | 1 |
| [langchain-ai/agentevals](https://github.com/langchain-ai/agentevals) | Evaluation framework | Python | MIT | 708 (▲23) | Mature | 54 | active | 1mo ago | 1.5y | 4 |
| [KRLabsOrg/LettuceDetect](https://github.com/KRLabsOrg/LettuceDetect) | Safety / red-team | Python | MIT | 601 (▲10) | Hot | 70 | very active | 15d ago | 1.6y | 11 |
| [rhesis-ai/rhesis](https://github.com/rhesis-ai/rhesis) | Evaluation framework | Python | NOASSERTION | 390 (▲4) | Hot | 89 | very active | 0d ago | 1.9y | 9 |
| [finos-labs/Open-Financial-LLMs-Leaderboard](https://github.com/finos-labs/Open-Financial-LLMs-Leaderboard) | Benchmark / leaderboard | JavaScript | — | 35 (▲2) | Declining | 8 | stale | 8mo ago | 2.0y | 0 |
| [jszheng21/RACE](https://github.com/jszheng21/RACE) | Benchmark / leaderboard | Python | Apache-2.0 | 14 | Abandoned | 10 | stale | 1.9y ago | 2.1y | 0 |

## By category

### Observability + eval platform

_Capture traces from live LLM apps, attach scores, manage prompts & datasets. Online-first, but most now run offline eval suites too._

- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 33,820★ · TypeScript · Classic  
  LLM observability, metrics, evals, prompt management, datasets & playground; the most-adopted OSS platform here.  
  <sub>topics: analytics, llm, llmops, large-language-models, openai, self-hosted, ycombinator, monitoring</sub>
- **[mlflow/mlflow](https://github.com/mlflow/mlflow)** · 27,698★ · Python · Classic  
  Broad AI engineering platform; LLM tracing + evaluate + experiment tracking on top of classic MLOps.  
  <sub>topics: machine-learning, ai, ml, mlflow, apache-spark, model-management, agentops, agents</sub>
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 21,642★ · Python · Classic  
  Debug / evaluate / monitor LLM, RAG & agentic apps with tracing + automated scoring.  
  <sub>topics: open-source, langchain, openai, playground, prompt-engineering, llama-index, llm, llm-evaluation</sub>
- **[traceloop/openllmetry](https://github.com/traceloop/openllmetry)** · 7,404★ · Python · Mature  
  OpenTelemetry-native GenAI observability; standards-based traces & metrics.  
  <sub>topics: llmops, observability, open-telemetry, metrics, monitoring, opentelemetry, datascience, ml</sub>
- **[comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw)** · 725★ · TypeScript · Declining  
  Opik plugin that exports OpenClaw agent traces (cost/tokens/errors) for monitoring.  
  <sub>topics: clawdbot, evaluation, moltbot, observability, openclaw, testing, ai-agents, llm-observability</sub>

### Evaluation framework

_Libraries to score outputs offline — reference metrics + LLM-as-a-judge — wired into CI like unit tests._

- **[promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)** · 24,623★ · TypeScript · Classic  
  Declarative prompt/eval testing + red-teaming CLI; config-driven test matrices in CI.  
  <sub>topics: llm, prompt-engineering, prompts, llmops, prompt-testing, testing, rag, evaluation</sub>
- **[openai/evals](https://github.com/openai/evals)** · 19,288★ · Python · Mature  
  OpenAI's eval registry/framework — write & share evals against a standard harness.  
  <sub>topics: —</sub>
- **[confident-ai/deepeval](https://github.com/confident-ai/deepeval)** · 17,914★ · Python · Classic  
  'The LLM eval framework' — pytest-style unit tests with metrics (faithfulness, relevancy, G-Eval/LLM-as-judge).  
  <sub>topics: evaluation-metrics, evaluation-framework, llm-evaluation, llm-evaluation-framework, llm-evaluation-metrics, python</sub>
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 11,218★ · Python · Classic  
  Open-source LLM tracing + eval; notebook-friendly, OTel-based.  
  <sub>topics: llmops, ai-monitoring, ai-observability, llm-eval, aiengineering, datasets, agents, llms</sub>
- **[truera/trulens](https://github.com/truera/trulens)** · 3,526★ · Python · Classic  
  Feedback-function evaluation — programmatic scorers for groundedness/relevance.  
  <sub>topics: machine-learning, neural-networks, explainable-ml, llmops, ai-monitoring, ai-observability, evals, llm-evaluation</sub>
- **[langchain-ai/openevals](https://github.com/langchain-ai/openevals)** · 1,181★ · Python · Hot  
  Readymade evaluators (prebuilt prompts + scorers) for LLM apps.  
  <sub>topics: —</sub>
- **[langchain-ai/agentevals](https://github.com/langchain-ai/agentevals)** · 708★ · Python · Mature  
  Evaluators specialized for agent *trajectories* (tool-call sequences, not just final output).  
  <sub>topics: —</sub>
- **[rhesis-ai/rhesis](https://github.com/rhesis-ai/rhesis)** · 390★ · Python · Hot  
  Testing platform that lets engineers + PMs + domain experts generate and run test suites.  
  <sub>topics: llmops, annotations, feedback-loop, hypothesis-testing, regression-testing, systematic-evaluation</sub>

### Benchmark / leaderboard

_Fixed task sets that rank models/agents. Watch for contamination (LiveBench is explicitly designed against it)._

- **[EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)** · 13,814★ · Python · Classic  
  The de-facto academic harness — 100+ standardized benchmarks behind the HF leaderboard.  
  <sub>topics: evaluation-framework, language-model, transformer</sub>
- **[huggingface/lighteval](https://github.com/huggingface/lighteval)** · 2,530★ · Python · Mature  
  Hugging Face's lightweight, all-in-one eval suite for fast benchmark runs.  
  <sub>topics: evaluation, evaluation-framework, evaluation-metrics, huggingface</sub>
- **[vllm-project/guidellm](https://github.com/vllm-project/guidellm)** · 1,551★ · Python · Mature  
  Performance/inference benchmark: evaluate LLM *deployments* for real-world throughput/latency.  
  <sub>topics: —</sub>
- **[pinchbench/skill](https://github.com/pinchbench/skill)** · 1,327★ · Python · Declining  
  Benchmarks LLMs as OpenClaw *coding agents* on real tasks.  
  <sub>topics: —</sub>
- **[LiveBench/LiveBench](https://github.com/LiveBench/LiveBench)** · 1,295★ · Python · Mature  
  Challenging, contamination-free benchmark refreshed over time to resist training-set leakage.  
  <sub>topics: —</sub>
- **[finos-labs/Open-Financial-LLMs-Leaderboard](https://github.com/finos-labs/Open-Financial-LLMs-Leaderboard)** · 35★ · JavaScript · Declining  
  Domain leaderboard ranking LLMs on financial tasks.  
  <sub>topics: —</sub>
- **[jszheng21/RACE](https://github.com/jszheng21/RACE)** · 14★ · Python · Abandoned  
  Multi-dimensional code-generation benchmark (Readability, Maintainability, Correctness, Efficiency).  
  <sub>topics: benchmark, code-generation, multidimensional, llm</sub>

### Safety / red-team

_Adversarial testing, vulnerability scanning, and hallucination / uncertainty detection — evaluating *failure modes* rather than task accuracy._

- **[NVIDIA/garak](https://github.com/NVIDIA/garak)** · 9,048★ · Python · Classic  
  LLM vulnerability scanner — probes for jailbreaks, prompt injection, toxicity, data leakage.  
  <sub>topics: ai, llm-evaluation, llm-security, security-scanners, vulnerability-assessment</sub>
- **[confident-ai/deepteam](https://github.com/confident-ai/deepteam)** · 2,625★ · Python · Hot  
  Framework to red-team LLMs & LLM systems (adversarial attack suites, from the DeepEval team).  
  <sub>topics: llm-guardrails, llm-red-teaming, llm-safety, python, llm-seecurity</sub>
- **[cvs-health/uqlm](https://github.com/cvs-health/uqlm)** · 1,192★ · Python · Hot  
  Uncertainty quantification for LLMs; UQ-based hallucination detection.  
  <sub>topics: ai-evaluation, ai-safety, hallucination, hallucination-detection, hallucination-evaluation, hallucination-mitigation, llm, llm-evaluation</sub>
- **[KRLabsOrg/LettuceDetect](https://github.com/KRLabsOrg/LettuceDetect)** · 601★ · Python · Hot  
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

- **Community 10** (8): `langfuse/langfuse`, `mlflow/mlflow`, `comet-ml/opik`, `comet-ml/opik-openclaw`, `rhesis-ai/rhesis`, `promptfoo/promptfoo`, `Arize-ai/phoenix`, `truera/trulens`
- **Community 21** (5): `confident-ai/deepeval`, `vllm-project/guidellm`, `EleutherAI/lm-evaluation-harness`, `huggingface/lighteval`, `confident-ai/deepteam`
- **Community 8** (2): `langchain-ai/openevals`, `langchain-ai/agentevals`
- **Community 0** (2): `LiveBench/LiveBench`, `pinchbench/skill`

**Centrality (PageRank in the full 1,071-repo graph)** — how 'hub-like' each tool is within your starred ecosystem:

- `comet-ml/opik` — PageRank 0.0011
- `langchain-ai/agentevals` — PageRank 0.0009
- `langchain-ai/openevals` — PageRank 0.0008
- `huggingface/lighteval` — PageRank 0.0008
- `NVIDIA/garak` — PageRank 0.0006
- `vllm-project/guidellm` — PageRank 0.0006
- `confident-ai/deepeval` — PageRank 0.0006
- `KRLabsOrg/LettuceDetect` — PageRank 0.0006

**Direct links between eval tools** (similarity edges where both endpoints are in this report):

- `langchain-ai/agentevals` ⇄ `langchain-ai/openevals` (w=1.750) — authors: jkennedyvz, dependabot[bot], jacoblee93
- `confident-ai/deepteam` ⇄ `confident-ai/deepeval` (w=1.221) — topics: python; authors: A-Vamshi, tanayvaswani, penguine-ip
- `comet-ml/opik-openclaw` ⇄ `comet-ml/opik` (w=0.600) — topics: evaluation, llm-observability
- `langfuse/langfuse` ⇄ `comet-ml/opik` (w=0.524) — topics: llm, llmops, openai, open-source
- `truera/trulens` ⇄ `Arize-ai/phoenix` (w=0.405) — topics: llmops, ai-monitoring, ai-observability, evals; authors: BetterAndBetterII
- `mlflow/mlflow` ⇄ `comet-ml/opik` (w=0.342) — topics: evaluation, langchain, llm-evaluation, llmops
- `Arize-ai/phoenix` ⇄ `comet-ml/opik` (w=0.307) — topics: llmops, prompt-engineering, llm-evaluation, openai; authors: Anuj7411
- `huggingface/lighteval` ⇄ `confident-ai/deepeval` (w=0.300) — topics: evaluation-framework, evaluation-metrics
- `langfuse/langfuse` ⇄ `mlflow/mlflow` (w=0.276) — topics: llmops, openai, observability, open-source
- `Arize-ai/phoenix` ⇄ `mlflow/mlflow` (w=0.264) — topics: llmops, agents, prompt-engineering, llm-evaluation
- `promptfoo/promptfoo` ⇄ `comet-ml/opik` (w=0.255) — topics: llm, prompt-engineering, llmops, evaluation; authors: dependabot[bot]
- `huggingface/lighteval` ⇄ `EleutherAI/lm-evaluation-harness` (w=0.217) — topics: evaluation-framework
- `EleutherAI/lm-evaluation-harness` ⇄ `confident-ai/deepeval` (w=0.208) — topics: evaluation-framework; authors: Anai-Guo
- `truera/trulens` ⇄ `comet-ml/opik` (w=0.202) — topics: llmops, llm-evaluation; authors: dependabot[bot], feiiiiii5
- `truera/trulens` ⇄ `mlflow/mlflow` (w=0.198) — topics: machine-learning, llmops, llm-evaluation, agentops
- `rhesis-ai/rhesis` ⇄ `cvs-health/uqlm` (w=0.193) — authors: feiiiiii5
- `rhesis-ai/rhesis` ⇄ `comet-ml/opik` (w=0.170) — topics: llmops; authors: feiiiiii5
- `truera/trulens` ⇄ `rhesis-ai/rhesis` (w=0.150) — topics: llmops; authors: feiiiiii5

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| truera/trulens | 98 | Classic | very active | 6 | 17% | 125 |
| langfuse/langfuse | 94 | Classic | very active | 4 | 23% | 666 |
| comet-ml/opik | 93 | Classic | very active | 4 | 19% | 561 |
| vllm-project/guidellm | 93 | Mature | very active | 4 | 18% | 17 |
| mlflow/mlflow | 92 | Classic | very active | 4 | 24% | 174 |
| rhesis-ai/rhesis | 89 | Hot | very active | 3 | 23% | 158 |
| EleutherAI/lm-evaluation-harness | 86 | Classic | very active | 11 | 11% | 18 |
| promptfoo/promptfoo | 84 | Classic | very active | 2 | 49% | 422 |
| Arize-ai/phoenix | 84 | Classic | very active | 2 | 38% | 793 |
| confident-ai/deepeval | 81 | Classic | very active | 2 | 39% | 62 |
| langchain-ai/openevals | 79 | Hot | very active | 2 | 46% | 44 |
| NVIDIA/garak | 77 | Classic | very active | 1 | 50% | 32 |
| cvs-health/uqlm | 76 | Hot | very active | 1 | 60% | 44 |
| KRLabsOrg/LettuceDetect | 70 | Hot | very active | 1 | 80% | 13 |
| traceloop/openllmetry | 66 | Mature | active | 1 | 58% | 262 |
| LiveBench/LiveBench | 66 | Mature | very active | 2 | 34% | 0 |
| confident-ai/deepteam | 63 | Hot | very active | 2 | 49% | 3 |
| comet-ml/opik-openclaw | 59 | Declining | active | 1 | 100% | 25 |
| langchain-ai/agentevals | 54 | Mature | active | 2 | 45% | 12 |
| huggingface/lighteval | 53 | Mature | active | 1 | 50% | 15 |
| pinchbench/skill | 49 | Declining | active | 0 | 0% | 14 |
| openai/evals | 23 | Mature | slowing | 0 | 0% | 0 |
| jszheng21/RACE | 10 | Abandoned | stale | 0 | 0% | 0 |
| finos-labs/Open-Financial-LLMs-Leaderboard | 8 | Declining | stale | 0 | 0% | 0 |

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

<sub>Tools covered: 24 · Snapshot: 2026-08-28T01:21:50.535Z</sub>
