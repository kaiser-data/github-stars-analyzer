# LLM Evaluation Tooling — Landscape Report

> Derived from **kaiser-data**'s 2,398 starred repos (snapshot `2026-10-19T11:27:31.266Z`), cross-referenced with the repo-similarity graph (2,398 nodes / 8,025 edges, 39 communities).
>
> Generated 2026-10-19 by `scripts/reports/llm_evaluation.py` (regenerate any time — no API cost).

![Top tools by stars](assets/llm-evaluation-tooling-top-tools.svg)

![Tools per category](assets/llm-evaluation-tooling-categories.svg)


## Executive summary

- **29 evaluation-focused tools** found in your stars (**224,548★** combined), spanning four categories:
  - **Observability + eval platform** (6): `langfuse`, `mlflow`, `opik`, `openllmetry`, `langwatch`, `opik-openclaw`
  - **Evaluation framework** (10): `promptfoo`, `evals`, `deepeval`, `phoenix`, `trulens`, `inspect_ai`, `openevals`, `agentevals`, `rhesis`, `evals`
  - **Benchmark / leaderboard** (9): `lm-evaluation-harness`, `lighteval`, `AssetOpsBench`, `guidellm`, `skill`, `LiveBench`, `evals`, `Open-Financial-LLMs-Leaderboard`, `RACE`
  - **Safety / red-team** (4): `garak`, `deepteam`, `uqlm`, `LettuceDetect`
- The field splits cleanly into **online** evaluation (tracing/observability in production) and **offline** evaluation (datasets, metrics, benchmarks before ship). Platforms increasingly do both.
- Evaluation method has converged on **LLM-as-a-judge** (deepeval, openevals) alongside classic reference metrics, plus a fast-growing **safety/red-team** wing (garak, deepteam) and **hallucination detection** (uqlm, LettuceDetect).
- Python dominates (23/29); the lone TypeScript-first platform is Langfuse.

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Observability + eval platform | TypeScript | NOASSERTION | 36,015 (▲415) | Classic | 94 | very active | 0d ago | 3.4y | 21 |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | Observability + eval platform | Python | Apache-2.0 | 28,446 (▲110) | Classic | 87 | very active | 0d ago | 8.4y | 24 |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | Evaluation framework | TypeScript | MIT | 26,135 (▲266) | Classic | 84 | very active | 0d ago | 3.5y | 12 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Observability + eval platform | Python | Apache-2.0 | 22,734 (▲247) | Classic | 94 | very active | 0d ago | 3.4y | 22 |
| [openai/evals](https://github.com/openai/evals) | Evaluation framework | Python | NOASSERTION | 19,619 (▲36) | Declining | 18 | stale | 6mo ago | 3.7y | 0 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | Evaluation framework | Python | Apache-2.0 | 18,955 (▲224) | Classic | 81 | very active | 0d ago | 3.2y | 5 |
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | Benchmark / leaderboard | Python | MIT | 14,266 (▲90) | Classic | 86 | active | 1mo ago | 6.1y | 52 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Evaluation framework | Python | NOASSERTION | 11,907 (▲133) | Classic | 84 | very active | 0d ago | 3.9y | 22 |
| [NVIDIA/garak](https://github.com/NVIDIA/garak) | Safety / red-team | Python | Apache-2.0 | 9,613 (▲95) | Classic | 77 | very active | 3d ago | 3.4y | 21 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Observability + eval platform | Python | Apache-2.0 | 7,501 (▲20) | Classic | 73 | very active | 0d ago | 3.1y | 10 |
| [langwatch/langwatch](https://github.com/langwatch/langwatch) | Observability + eval platform | TypeScript | Apache-2.0 | 4,981 (▲48) | Classic | 79 | very active | 0d ago | 3.1y | 6 |
| [truera/trulens](https://github.com/truera/trulens) | Evaluation framework | Python | MIT | 3,602 (▲6) | Classic | 94 | very active | 0d ago | 6.0y | 29 |
| [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | Evaluation framework | Python | MIT | 3,042 (▲58) | Mature | 75 | very active | 2d ago | 2.9y | 17 |
| [confident-ai/deepteam](https://github.com/confident-ai/deepteam) | Safety / red-team | Python | Apache-2.0 | 3,028 (▲23) | Hot | 56 | very active | 3d ago | 1.6y | 3 |
| [huggingface/lighteval](https://github.com/huggingface/lighteval) | Benchmark / leaderboard | Python | MIT | 2,564 (▲11) | Mature | 59 | active | 13d ago | 2.7y | 5 |
| [IBM/AssetOpsBench](https://github.com/IBM/AssetOpsBench) | Benchmark / leaderboard | Python | Apache-2.0 | 2,365 (▲24) | Hot | 70 | very active | 0d ago | 1.5y | 8 |
| [vllm-project/guidellm](https://github.com/vllm-project/guidellm) | Benchmark / leaderboard | Python | Apache-2.0 | 1,702 (▲23) | Mature | 88 | very active | 0d ago | 2.4y | 24 |
| [pinchbench/skill](https://github.com/pinchbench/skill) | Benchmark / leaderboard | Python | MIT | 1,366 (▲7) | Declining | 45 | slowing | 3mo ago | 8mo | 0 |
| [LiveBench/LiveBench](https://github.com/LiveBench/LiveBench) | Benchmark / leaderboard | Python | NOASSERTION | 1,343 (▲2) | Mature | 60 | very active | 1d ago | 2.4y | 4 |
| [langchain-ai/openevals](https://github.com/langchain-ai/openevals) | Evaluation framework | Python | MIT | 1,226 (▲10) | Hot | 78 | very active | 0d ago | 1.7y | 6 |
| [cvs-health/uqlm](https://github.com/cvs-health/uqlm) | Safety / red-team | Python | Apache-2.0 | 1,210 (▲3) | Hot | 76 | very active | 6d ago | 1.5y | 7 |
| [langchain-ai/agentevals](https://github.com/langchain-ai/agentevals) | Evaluation framework | Python | MIT | 752 (▲10) | Declining | 27 | slowing | 3mo ago | 1.7y | 0 |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | Observability + eval platform | TypeScript | Apache-2.0 | 726 (▲2) | Rising | 63 | active | 14d ago | 7mo | 4 |
| [KRLabsOrg/LettuceDetect](https://github.com/KRLabsOrg/LettuceDetect) | Safety / red-team | Python | MIT | 617 (▲2) | Mature | 57 | active | 10d ago | 1.7y | 4 |
| [rhesis-ai/rhesis](https://github.com/rhesis-ai/rhesis) | Evaluation framework | Python | NOASSERTION | 398 (▲1) | Mature | 79 | very active | 4d ago | 2.0y | 7 |
| [strands-agents/evals](https://github.com/strands-agents/evals) | Evaluation framework | Python | Apache-2.0 | 238 (▲3) | Hot | 78 | very active | 5d ago | 1.2y | 15 |
| [supabase/evals](https://github.com/supabase/evals) | Benchmark / leaderboard | TypeScript | Apache-2.0 | 145 | Hot | 67 | very active | 0d ago | 5mo | 12 |
| [finos-labs/Open-Financial-LLMs-Leaderboard](https://github.com/finos-labs/Open-Financial-LLMs-Leaderboard) | Benchmark / leaderboard | JavaScript | — | 37 | Declining | 4 | stale | 10mo ago | 2.2y | 0 |
| [jszheng21/RACE](https://github.com/jszheng21/RACE) | Benchmark / leaderboard | Python | Apache-2.0 | 15 | Abandoned | 10 | stale | 2.0y ago | 2.3y | 0 |

## By category

### Observability + eval platform

_Capture traces from live LLM apps, attach scores, manage prompts & datasets. Online-first, but most now run offline eval suites too._

- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 36,015★ · TypeScript · Classic  
  LLM observability, metrics, evals, prompt management, datasets & playground; the most-adopted OSS platform here.  
  <sub>topics: analytics, llm, llmops, large-language-models, openai, self-hosted, ycombinator, monitoring</sub>
- **[mlflow/mlflow](https://github.com/mlflow/mlflow)** · 28,446★ · Python · Classic  
  Broad AI engineering platform; LLM tracing + evaluate + experiment tracking on top of classic MLOps.  
  <sub>topics: machine-learning, ai, ml, mlflow, apache-spark, model-management, agentops, agents</sub>
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 22,734★ · Python · Classic  
  Debug / evaluate / monitor LLM, RAG & agentic apps with tracing + automated scoring.  
  <sub>topics: open-source, langchain, openai, playground, prompt-engineering, llama-index, llm, llm-evaluation</sub>
- **[traceloop/openllmetry](https://github.com/traceloop/openllmetry)** · 7,501★ · Python · Classic  
  OpenTelemetry-native GenAI observability; standards-based traces & metrics.  
  <sub>topics: llmops, observability, open-telemetry, metrics, monitoring, opentelemetry, datascience, ml</sub>
- **[langwatch/langwatch](https://github.com/langwatch/langwatch)** · 4,981★ · TypeScript · Classic  
  Agent observability plus evals, simulations and guardrails — OTel-based tracing with an agent-testing focus.  
  <sub>topics: ai, analytics, datasets, evaluation, gpt, llm, observability, openai</sub>
- **[comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw)** · 726★ · TypeScript · Rising  
  Opik plugin that exports OpenClaw agent traces (cost/tokens/errors) for monitoring.  
  <sub>topics: clawdbot, evaluation, moltbot, observability, openclaw, testing, ai-agents, llm-observability</sub>

### Evaluation framework

_Libraries to score outputs offline — reference metrics + LLM-as-a-judge — wired into CI like unit tests._

- **[promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)** · 26,135★ · TypeScript · Classic  
  Declarative prompt/eval testing + red-teaming CLI; config-driven test matrices in CI.  
  <sub>topics: llm, prompt-engineering, prompts, llmops, prompt-testing, testing, rag, evaluation</sub>
- **[openai/evals](https://github.com/openai/evals)** · 19,619★ · Python · Declining  
  OpenAI's eval registry/framework — write & share evals against a standard harness.  
  <sub>topics: —</sub>
- **[confident-ai/deepeval](https://github.com/confident-ai/deepeval)** · 18,955★ · Python · Classic  
  'The LLM eval framework' — pytest-style unit tests with metrics (faithfulness, relevancy, G-Eval/LLM-as-judge).  
  <sub>topics: evaluation-metrics, evaluation-framework, llm-evaluation, llm-evaluation-framework, llm-evaluation-metrics, python</sub>
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 11,907★ · Python · Classic  
  Open-source LLM tracing + eval; notebook-friendly, OTel-based.  
  <sub>topics: llmops, ai-monitoring, ai-observability, llm-eval, aiengineering, datasets, agents, llms</sub>
- **[truera/trulens](https://github.com/truera/trulens)** · 3,602★ · Python · Classic  
  Feedback-function evaluation — programmatic scorers for groundedness/relevance.  
  <sub>topics: machine-learning, neural-networks, explainable-ml, llmops, ai-monitoring, ai-observability, evals, llm-evaluation</sub>
- **[UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai)** · 3,042★ · Python · Mature  
  UK AI Security Institute's eval framework — composable tasks, solvers and scorers with sandboxed agent evals; widely used for safety and capability evals.  
  <sub>topics: —</sub>
- **[langchain-ai/openevals](https://github.com/langchain-ai/openevals)** · 1,226★ · Python · Hot  
  Readymade evaluators (prebuilt prompts + scorers) for LLM apps.  
  <sub>topics: —</sub>
- **[langchain-ai/agentevals](https://github.com/langchain-ai/agentevals)** · 752★ · Python · Declining  
  Evaluators specialized for agent *trajectories* (tool-call sequences, not just final output).  
  <sub>topics: —</sub>
- **[rhesis-ai/rhesis](https://github.com/rhesis-ai/rhesis)** · 398★ · Python · Mature  
  Testing platform that lets engineers + PMs + domain experts generate and run test suites.  
  <sub>topics: llmops, annotations, feedback-loop, hypothesis-testing, regression-testing, systematic-evaluation</sub>
- **[strands-agents/evals](https://github.com/strands-agents/evals)** · 238★ · Python · Hot  
  Strands' eval framework for agents and LLM apps — output and trajectory evaluators plus simulated users.  
  <sub>topics: agentic, agentic-ai, ai, machine-learning, python, evaluation, strands-agents</sub>

### Benchmark / leaderboard

_Fixed task sets that rank models/agents. Watch for contamination (LiveBench is explicitly designed against it)._

- **[EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)** · 14,266★ · Python · Classic  
  The de-facto academic harness — 100+ standardized benchmarks behind the HF leaderboard.  
  <sub>topics: evaluation-framework, language-model, transformer</sub>
- **[huggingface/lighteval](https://github.com/huggingface/lighteval)** · 2,564★ · Python · Mature  
  Hugging Face's lightweight, all-in-one eval suite for fast benchmark runs.  
  <sub>topics: evaluation, evaluation-framework, evaluation-metrics, huggingface</sub>
- **[IBM/AssetOpsBench](https://github.com/IBM/AssetOpsBench)** · 2,365★ · Python · Hot  
  IBM's Industry 4.0 benchmark for multi-agent asset-operations tasks — a domain benchmark with its own agent framework.  
  <sub>topics: llm-agents, model-context-protocol, time-series-forecasting, condition-based-maintenance, hvac-maintenance, iot, predictive-maintenance, ai-for-physical-assets</sub>
- **[vllm-project/guidellm](https://github.com/vllm-project/guidellm)** · 1,702★ · Python · Mature  
  Performance/inference benchmark: evaluate LLM *deployments* for real-world throughput/latency.  
  <sub>topics: —</sub>
- **[pinchbench/skill](https://github.com/pinchbench/skill)** · 1,366★ · Python · Declining  
  Benchmarks LLMs as OpenClaw *coding agents* on real tasks.  
  <sub>topics: —</sub>
- **[LiveBench/LiveBench](https://github.com/LiveBench/LiveBench)** · 1,343★ · Python · Mature  
  Challenging, contamination-free benchmark refreshed over time to resist training-set leakage.  
  <sub>topics: —</sub>
- **[supabase/evals](https://github.com/supabase/evals)** · 145★ · TypeScript · Hot  
  Supabase's evals of coding agents doing Supabase work — a vendor benchmark of agent competence on one platform.  
  <sub>topics: —</sub>
- **[finos-labs/Open-Financial-LLMs-Leaderboard](https://github.com/finos-labs/Open-Financial-LLMs-Leaderboard)** · 37★ · JavaScript · Declining  
  Domain leaderboard ranking LLMs on financial tasks.  
  <sub>topics: —</sub>
- **[jszheng21/RACE](https://github.com/jszheng21/RACE)** · 15★ · Python · Abandoned  
  Multi-dimensional code-generation benchmark (Readability, Maintainability, Correctness, Efficiency).  
  <sub>topics: benchmark, code-generation, multidimensional, llm</sub>

### Safety / red-team

_Adversarial testing, vulnerability scanning, and hallucination / uncertainty detection — evaluating *failure modes* rather than task accuracy._

- **[NVIDIA/garak](https://github.com/NVIDIA/garak)** · 9,613★ · Python · Classic  
  LLM vulnerability scanner — probes for jailbreaks, prompt injection, toxicity, data leakage.  
  <sub>topics: ai, llm-evaluation, llm-security, security-scanners, vulnerability-assessment</sub>
- **[confident-ai/deepteam](https://github.com/confident-ai/deepteam)** · 3,028★ · Python · Hot  
  Framework to red-team LLMs & LLM systems (adversarial attack suites, from the DeepEval team).  
  <sub>topics: llm-guardrails, llm-red-teaming, llm-safety, python, llm-seecurity</sub>
- **[cvs-health/uqlm](https://github.com/cvs-health/uqlm)** · 1,210★ · Python · Hot  
  Uncertainty quantification for LLMs; UQ-based hallucination detection.  
  <sub>topics: ai-evaluation, ai-safety, hallucination, hallucination-detection, hallucination-evaluation, hallucination-mitigation, llm, llm-evaluation</sub>
- **[KRLabsOrg/LettuceDetect](https://github.com/KRLabsOrg/LettuceDetect)** · 617★ · Python · Mature  
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

**Community clustering.** These 29 tools span **15 of the graph's 39 communities** — evaluation tooling co-locates with the broader LLM-app / agent-infra clusters rather than forming an isolated island.

- **Community 17** (8): `langfuse/langfuse`, `mlflow/mlflow`, `comet-ml/opik`, `comet-ml/opik-openclaw`, `langwatch/langwatch`, `promptfoo/promptfoo`, `Arize-ai/phoenix`, `truera/trulens`
- **Community 21** (3): `confident-ai/deepeval`, `openai/evals`, `confident-ai/deepteam`
- **Community 13** (2): `traceloop/openllmetry`, `UKGovernmentBEIS/inspect_ai`
- **Community 24** (2): `langchain-ai/openevals`, `langchain-ai/agentevals`
- **Community 0** (2): `LiveBench/LiveBench`, `pinchbench/skill`
- **Community 20** (2): `vllm-project/guidellm`, `EleutherAI/lm-evaluation-harness`
- **Community 22** (2): `NVIDIA/garak`, `KRLabsOrg/LettuceDetect`

**Centrality (PageRank in the full 1,071-repo graph)** — how 'hub-like' each tool is within your starred ecosystem:

- `huggingface/lighteval` — PageRank 0.0010
- `strands-agents/evals` — PageRank 0.0009
- `comet-ml/opik` — PageRank 0.0007
- `IBM/AssetOpsBench` — PageRank 0.0005
- `langfuse/langfuse` — PageRank 0.0005
- `mlflow/mlflow` — PageRank 0.0005
- `confident-ai/deepeval` — PageRank 0.0005
- `NVIDIA/garak` — PageRank 0.0004

**Direct links between eval tools** (similarity edges where both endpoints are in this report):

- `confident-ai/deepteam` ⇄ `confident-ai/deepeval` (w=1.850) — topics: python; authors: A-Vamshi, penguine-ip, kritinv
- `comet-ml/opik-openclaw` ⇄ `comet-ml/opik` (w=0.767) — topics: evaluation, llm-observability; authors: awkoy, GuySaar8
- `langfuse/langfuse` ⇄ `comet-ml/opik` (w=0.571) — topics: llm, llmops, openai, open-source; authors: dependabot[bot]
- `mlflow/mlflow` ⇄ `comet-ml/opik` (w=0.386) — topics: evaluation, langchain, llm-evaluation, llmops; authors: dependabot[bot]
- `truera/trulens` ⇄ `Arize-ai/phoenix` (w=0.368) — topics: llmops, ai-monitoring, ai-observability, evals
- `langfuse/langfuse` ⇄ `mlflow/mlflow` (w=0.321) — topics: llmops, openai, observability, open-source; authors: dependabot[bot]
- `Arize-ai/phoenix` ⇄ `mlflow/mlflow` (w=0.309) — topics: llmops, agents, prompt-engineering, llm-evaluation; authors: dependabot[bot]
- `Arize-ai/phoenix` ⇄ `comet-ml/opik` (w=0.305) — topics: llmops, prompt-engineering, llm-evaluation, openai; authors: dependabot[bot]
- `langwatch/langwatch` ⇄ `langfuse/langfuse` (w=0.300) — topics: analytics, evaluation, llm, observability
- `huggingface/lighteval` ⇄ `confident-ai/deepeval` (w=0.300) — topics: evaluation-framework, evaluation-metrics
- `promptfoo/promptfoo` ⇄ `langfuse/langfuse` (w=0.269) — topics: llm, prompt-engineering, llmops, evaluation; authors: kumarpriyanshu09
- `promptfoo/promptfoo` ⇄ `comet-ml/opik` (w=0.253) — topics: llm, prompt-engineering, llmops, evaluation; authors: feiiiiii5
- `truera/trulens` ⇄ `mlflow/mlflow` (w=0.237) — topics: machine-learning, llmops, llm-evaluation, agentops; authors: kimnamu
- `huggingface/lighteval` ⇄ `EleutherAI/lm-evaluation-harness` (w=0.217) — topics: evaluation-framework
- `EleutherAI/lm-evaluation-harness` ⇄ `confident-ai/deepeval` (w=0.175) — topics: evaluation-framework

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| langfuse/langfuse | 94 | Classic | very active | 4 | 24% | 719 |
| comet-ml/opik | 94 | Classic | very active | 4 | 24% | 620 |
| truera/trulens | 94 | Classic | very active | 4 | 19% | 127 |
| vllm-project/guidellm | 88 | Mature | very active | 3 | 23% | 20 |
| mlflow/mlflow | 87 | Classic | very active | 3 | 30% | 179 |
| EleutherAI/lm-evaluation-harness | 86 | Classic | active | 11 | 11% | 19 |
| promptfoo/promptfoo | 84 | Classic | very active | 2 | 40% | 430 |
| Arize-ai/phoenix | 84 | Classic | very active | 2 | 48% | 869 |
| confident-ai/deepeval | 81 | Classic | very active | 2 | 43% | 64 |
| langwatch/langwatch | 79 | Classic | very active | 1 | 64% | 409 |
| rhesis-ai/rhesis | 79 | Mature | very active | 1 | 85% | 177 |
| langchain-ai/openevals | 78 | Hot | very active | 2 | 42% | 44 |
| strands-agents/evals | 78 | Hot | very active | 3 | 35% | 32 |
| NVIDIA/garak | 77 | Classic | very active | 1 | 50% | 34 |
| cvs-health/uqlm | 76 | Hot | very active | 1 | 63% | 46 |
| UKGovernmentBEIS/inspect_ai | 75 | Mature | very active | 2 | 38% | 4 |
| traceloop/openllmetry | 73 | Classic | very active | 2 | 35% | 263 |
| IBM/AssetOpsBench | 70 | Hot | very active | 2 | 48% | 0 |
| supabase/evals | 67 | Hot | very active | 2 | 41% | 0 |
| comet-ml/opik-openclaw | 63 | Rising | active | 1 | 60% | 26 |
| LiveBench/LiveBench | 60 | Mature | very active | 1 | 55% | 0 |
| huggingface/lighteval | 59 | Mature | active | 2 | 38% | 15 |
| KRLabsOrg/LettuceDetect | 57 | Mature | active | 1 | 81% | 13 |
| confident-ai/deepteam | 56 | Hot | very active | 1 | 78% | 3 |
| pinchbench/skill | 45 | Declining | slowing | 0 | 0% | 14 |
| langchain-ai/agentevals | 27 | Declining | slowing | 0 | 0% | 12 |
| openai/evals | 18 | Declining | stale | 0 | 0% | 0 |
| jszheng21/RACE | 10 | Abandoned | stale | 0 | 0% | 0 |
| finos-labs/Open-Financial-LLMs-Leaderboard | 4 | Declining | stale | 0 | 0% | 0 |

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

<sub>Tools covered: 29 · Snapshot: 2026-10-19T11:27:31.266Z</sub>
