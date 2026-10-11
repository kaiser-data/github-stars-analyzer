# LLM Evaluation Tooling — Landscape Report

> Derived from **kaiser-data**'s 2,322 starred repos (snapshot `2026-10-10T15:21:10.911Z`), cross-referenced with the repo-similarity graph (2,322 nodes / 7,718 edges, 43 communities).
>
> Generated 2026-10-10 by `scripts/reports/llm_evaluation.py` (regenerate any time — no API cost).

![Top tools by stars](assets/llm-evaluation-tooling-top-tools.svg)

![Tools per category](assets/llm-evaluation-tooling-categories.svg)


## Executive summary

- **26 evaluation-focused tools** found in your stars (**217,209★** combined), spanning four categories:
  - **Observability + eval platform** (6): `langfuse`, `mlflow`, `opik`, `openllmetry`, `langwatch`, `opik-openclaw`
  - **Evaluation framework** (9): `promptfoo`, `evals`, `deepeval`, `phoenix`, `trulens`, `openevals`, `agentevals`, `rhesis`, `evals`
  - **Benchmark / leaderboard** (7): `lm-evaluation-harness`, `lighteval`, `guidellm`, `skill`, `LiveBench`, `Open-Financial-LLMs-Leaderboard`, `RACE`
  - **Safety / red-team** (4): `garak`, `deepteam`, `uqlm`, `LettuceDetect`
- The field splits cleanly into **online** evaluation (tracing/observability in production) and **offline** evaluation (datasets, metrics, benchmarks before ship). Platforms increasingly do both.
- Evaluation method has converged on **LLM-as-a-judge** (deepeval, openevals) alongside classic reference metrics, plus a fast-growing **safety/red-team** wing (garak, deepteam) and **hallucination detection** (uqlm, LettuceDetect).
- Python dominates (21/26); the lone TypeScript-first platform is Langfuse.

## Master comparison

Sorted by stars. `Health`/`Lifecycle` are the dataset's computed metrics; `Activity` is derived from days-since-push + 90-day commits.

| Tool | Category | Lang | License | ★ Stars | Lifecycle | Health | Activity | Last push | Age | Contrib(90d) |
|---|---|---|---|---|---|---|---|---|---|---|
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Observability + eval platform | TypeScript | NOASSERTION | 35,600 (▲567) | Classic | 94 | very active | 0d ago | 3.4y | 19 |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | Observability + eval platform | Python | Apache-2.0 | 28,336 (▲203) | Classic | 82 | very active | 0d ago | 8.4y | 21 |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | Evaluation framework | TypeScript | MIT | 25,869 (▲430) | Classic | 79 | very active | 0d ago | 3.5y | 20 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | Observability + eval platform | Python | Apache-2.0 | 22,487 (▲257) | Classic | 89 | very active | 1d ago | 3.4y | 18 |
| [openai/evals](https://github.com/openai/evals) | Evaluation framework | Python | NOASSERTION | 19,583 (▲78) | Mature | 19 | slowing | 5mo ago | 3.7y | 0 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | Evaluation framework | Python | Apache-2.0 | 18,731 (▲294) | Classic | 76 | very active | 1d ago | 3.2y | 7 |
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | Benchmark / leaderboard | Python | MIT | 14,176 (▲103) | Classic | 87 | very active | 26d ago | 6.1y | 54 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Evaluation framework | Python | NOASSERTION | 11,774 (▲165) | Classic | 84 | very active | 0d ago | 3.9y | 22 |
| [NVIDIA/garak](https://github.com/NVIDIA/garak) | Safety / red-team | Python | Apache-2.0 | 9,518 (▲167) | Classic | 82 | very active | 0d ago | 3.4y | 25 |
| [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Observability + eval platform | Python | Apache-2.0 | 7,481 (▲34) | Classic | 71 | active | 4d ago | 3.1y | 8 |
| [langwatch/langwatch](https://github.com/langwatch/langwatch) | Observability + eval platform | TypeScript | Apache-2.0 | 4,933 | Classic | 85 | very active | 0d ago | 3.1y | 7 |
| [truera/trulens](https://github.com/truera/trulens) | Evaluation framework | Python | MIT | 3,596 (▲25) | Classic | 89 | very active | 1d ago | 5.9y | 26 |
| [confident-ai/deepteam](https://github.com/confident-ai/deepteam) | Safety / red-team | Python | Apache-2.0 | 3,005 (▲56) | Hot | 55 | very active | 9d ago | 1.6y | 5 |
| [huggingface/lighteval](https://github.com/huggingface/lighteval) | Benchmark / leaderboard | Python | MIT | 2,553 (▲4) | Mature | 60 | active | 4d ago | 2.7y | 5 |
| [vllm-project/guidellm](https://github.com/vllm-project/guidellm) | Benchmark / leaderboard | Python | Apache-2.0 | 1,679 (▲37) | Mature | 88 | very active | 0d ago | 2.4y | 23 |
| [pinchbench/skill](https://github.com/pinchbench/skill) | Benchmark / leaderboard | Python | MIT | 1,359 (▲9) | Declining | 46 | slowing | 3mo ago | 8mo | 0 |
| [LiveBench/LiveBench](https://github.com/LiveBench/LiveBench) | Benchmark / leaderboard | Python | NOASSERTION | 1,341 (▲12) | Mature | 65 | very active | 3d ago | 2.3y | 4 |
| [langchain-ai/openevals](https://github.com/langchain-ai/openevals) | Evaluation framework | Python | MIT | 1,216 (▲9) | Hot | 77 | very active | 8d ago | 1.7y | 5 |
| [cvs-health/uqlm](https://github.com/cvs-health/uqlm) | Safety / red-team | Python | Apache-2.0 | 1,207 (▲5) | Hot | 76 | very active | 2d ago | 1.5y | 7 |
| [langchain-ai/agentevals](https://github.com/langchain-ai/agentevals) | Evaluation framework | Python | MIT | 742 (▲10) | Declining | 34 | slowing | 2mo ago | 1.6y | 1 |
| [comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw) | Observability + eval platform | TypeScript | Apache-2.0 | 724 | Rising | 64 | active | 5d ago | 7mo | 4 |
| [KRLabsOrg/LettuceDetect](https://github.com/KRLabsOrg/LettuceDetect) | Safety / red-team | Python | MIT | 615 (▲4) | Mature | 59 | very active | 1d ago | 1.7y | 8 |
| [rhesis-ai/rhesis](https://github.com/rhesis-ai/rhesis) | Evaluation framework | Python | NOASSERTION | 397 (▲2) | Mature | 79 | very active | 2d ago | 2.0y | 8 |
| [strands-agents/evals](https://github.com/strands-agents/evals) | Evaluation framework | Python | Apache-2.0 | 235 | Hot | 79 | very active | 2d ago | 1.2y | 16 |
| [finos-labs/Open-Financial-LLMs-Leaderboard](https://github.com/finos-labs/Open-Financial-LLMs-Leaderboard) | Benchmark / leaderboard | JavaScript | — | 37 | Declining | 5 | stale | 10mo ago | 2.1y | 0 |
| [jszheng21/RACE](https://github.com/jszheng21/RACE) | Benchmark / leaderboard | Python | Apache-2.0 | 15 (▲1) | Abandoned | 10 | stale | 2.0y ago | 2.2y | 0 |

## By category

### Observability + eval platform

_Capture traces from live LLM apps, attach scores, manage prompts & datasets. Online-first, but most now run offline eval suites too._

- **[langfuse/langfuse](https://github.com/langfuse/langfuse)** · 35,600★ · TypeScript · Classic  
  LLM observability, metrics, evals, prompt management, datasets & playground; the most-adopted OSS platform here.  
  <sub>topics: analytics, llm, llmops, large-language-models, openai, self-hosted, ycombinator, monitoring</sub>
- **[mlflow/mlflow](https://github.com/mlflow/mlflow)** · 28,336★ · Python · Classic  
  Broad AI engineering platform; LLM tracing + evaluate + experiment tracking on top of classic MLOps.  
  <sub>topics: machine-learning, ai, ml, mlflow, apache-spark, model-management, agentops, agents</sub>
- **[comet-ml/opik](https://github.com/comet-ml/opik)** · 22,487★ · Python · Classic  
  Debug / evaluate / monitor LLM, RAG & agentic apps with tracing + automated scoring.  
  <sub>topics: open-source, langchain, openai, playground, prompt-engineering, llama-index, llm, llm-evaluation</sub>
- **[traceloop/openllmetry](https://github.com/traceloop/openllmetry)** · 7,481★ · Python · Classic  
  OpenTelemetry-native GenAI observability; standards-based traces & metrics.  
  <sub>topics: llmops, observability, open-telemetry, metrics, monitoring, opentelemetry, datascience, ml</sub>
- **[langwatch/langwatch](https://github.com/langwatch/langwatch)** · 4,933★ · TypeScript · Classic  
  Agent observability plus evals, simulations and guardrails — OTel-based tracing with an agent-testing focus.  
  <sub>topics: ai, analytics, datasets, evaluation, gpt, llm, observability, openai</sub>
- **[comet-ml/opik-openclaw](https://github.com/comet-ml/opik-openclaw)** · 724★ · TypeScript · Rising  
  Opik plugin that exports OpenClaw agent traces (cost/tokens/errors) for monitoring.  
  <sub>topics: clawdbot, evaluation, moltbot, observability, openclaw, testing, ai-agents, llm-observability</sub>

### Evaluation framework

_Libraries to score outputs offline — reference metrics + LLM-as-a-judge — wired into CI like unit tests._

- **[promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)** · 25,869★ · TypeScript · Classic  
  Declarative prompt/eval testing + red-teaming CLI; config-driven test matrices in CI.  
  <sub>topics: llm, prompt-engineering, prompts, llmops, prompt-testing, testing, rag, evaluation</sub>
- **[openai/evals](https://github.com/openai/evals)** · 19,583★ · Python · Mature  
  OpenAI's eval registry/framework — write & share evals against a standard harness.  
  <sub>topics: —</sub>
- **[confident-ai/deepeval](https://github.com/confident-ai/deepeval)** · 18,731★ · Python · Classic  
  'The LLM eval framework' — pytest-style unit tests with metrics (faithfulness, relevancy, G-Eval/LLM-as-judge).  
  <sub>topics: evaluation-metrics, evaluation-framework, llm-evaluation, llm-evaluation-framework, llm-evaluation-metrics, python</sub>
- **[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)** · 11,774★ · Python · Classic  
  Open-source LLM tracing + eval; notebook-friendly, OTel-based.  
  <sub>topics: llmops, ai-monitoring, ai-observability, llm-eval, aiengineering, datasets, agents, llms</sub>
- **[truera/trulens](https://github.com/truera/trulens)** · 3,596★ · Python · Classic  
  Feedback-function evaluation — programmatic scorers for groundedness/relevance.  
  <sub>topics: machine-learning, neural-networks, explainable-ml, llmops, ai-monitoring, ai-observability, evals, llm-evaluation</sub>
- **[langchain-ai/openevals](https://github.com/langchain-ai/openevals)** · 1,216★ · Python · Hot  
  Readymade evaluators (prebuilt prompts + scorers) for LLM apps.  
  <sub>topics: —</sub>
- **[langchain-ai/agentevals](https://github.com/langchain-ai/agentevals)** · 742★ · Python · Declining  
  Evaluators specialized for agent *trajectories* (tool-call sequences, not just final output).  
  <sub>topics: —</sub>
- **[rhesis-ai/rhesis](https://github.com/rhesis-ai/rhesis)** · 397★ · Python · Mature  
  Testing platform that lets engineers + PMs + domain experts generate and run test suites.  
  <sub>topics: llmops, annotations, feedback-loop, hypothesis-testing, regression-testing, systematic-evaluation</sub>
- **[strands-agents/evals](https://github.com/strands-agents/evals)** · 235★ · Python · Hot  
  Strands' eval framework for agents and LLM apps — output and trajectory evaluators plus simulated users.  
  <sub>topics: agentic, agentic-ai, ai, machine-learning, python, evaluation, strands-agents</sub>

### Benchmark / leaderboard

_Fixed task sets that rank models/agents. Watch for contamination (LiveBench is explicitly designed against it)._

- **[EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)** · 14,176★ · Python · Classic  
  The de-facto academic harness — 100+ standardized benchmarks behind the HF leaderboard.  
  <sub>topics: evaluation-framework, language-model, transformer</sub>
- **[huggingface/lighteval](https://github.com/huggingface/lighteval)** · 2,553★ · Python · Mature  
  Hugging Face's lightweight, all-in-one eval suite for fast benchmark runs.  
  <sub>topics: evaluation, evaluation-framework, evaluation-metrics, huggingface</sub>
- **[vllm-project/guidellm](https://github.com/vllm-project/guidellm)** · 1,679★ · Python · Mature  
  Performance/inference benchmark: evaluate LLM *deployments* for real-world throughput/latency.  
  <sub>topics: —</sub>
- **[pinchbench/skill](https://github.com/pinchbench/skill)** · 1,359★ · Python · Declining  
  Benchmarks LLMs as OpenClaw *coding agents* on real tasks.  
  <sub>topics: —</sub>
- **[LiveBench/LiveBench](https://github.com/LiveBench/LiveBench)** · 1,341★ · Python · Mature  
  Challenging, contamination-free benchmark refreshed over time to resist training-set leakage.  
  <sub>topics: —</sub>
- **[finos-labs/Open-Financial-LLMs-Leaderboard](https://github.com/finos-labs/Open-Financial-LLMs-Leaderboard)** · 37★ · JavaScript · Declining  
  Domain leaderboard ranking LLMs on financial tasks.  
  <sub>topics: —</sub>
- **[jszheng21/RACE](https://github.com/jszheng21/RACE)** · 15★ · Python · Abandoned  
  Multi-dimensional code-generation benchmark (Readability, Maintainability, Correctness, Efficiency).  
  <sub>topics: benchmark, code-generation, multidimensional, llm</sub>

### Safety / red-team

_Adversarial testing, vulnerability scanning, and hallucination / uncertainty detection — evaluating *failure modes* rather than task accuracy._

- **[NVIDIA/garak](https://github.com/NVIDIA/garak)** · 9,518★ · Python · Classic  
  LLM vulnerability scanner — probes for jailbreaks, prompt injection, toxicity, data leakage.  
  <sub>topics: ai, llm-evaluation, llm-security, security-scanners, vulnerability-assessment</sub>
- **[confident-ai/deepteam](https://github.com/confident-ai/deepteam)** · 3,005★ · Python · Hot  
  Framework to red-team LLMs & LLM systems (adversarial attack suites, from the DeepEval team).  
  <sub>topics: llm-guardrails, llm-red-teaming, llm-safety, python, llm-seecurity</sub>
- **[cvs-health/uqlm](https://github.com/cvs-health/uqlm)** · 1,207★ · Python · Hot  
  Uncertainty quantification for LLMs; UQ-based hallucination detection.  
  <sub>topics: ai-evaluation, ai-safety, hallucination, hallucination-detection, hallucination-evaluation, hallucination-mitigation, llm, llm-evaluation</sub>
- **[KRLabsOrg/LettuceDetect](https://github.com/KRLabsOrg/LettuceDetect)** · 615★ · Python · Mature  
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

**Community clustering.** These 26 tools span **13 of the graph's 43 communities** — evaluation tooling co-locates with the broader LLM-app / agent-infra clusters rather than forming an isolated island.

- **Community 18** (7): `langfuse/langfuse`, `mlflow/mlflow`, `comet-ml/opik`, `comet-ml/opik-openclaw`, `promptfoo/promptfoo`, `Arize-ai/phoenix`, `truera/trulens`
- **Community 17** (4): `confident-ai/deepeval`, `langchain-ai/openevals`, `langchain-ai/agentevals`, `confident-ai/deepteam`
- **Community 3** (3): `LiveBench/LiveBench`, `pinchbench/skill`, `NVIDIA/garak`
- **Community 1** (2): `langwatch/langwatch`, `finos-labs/Open-Financial-LLMs-Leaderboard`
- **Community 8** (2): `rhesis-ai/rhesis`, `EleutherAI/lm-evaluation-harness`

**Centrality (PageRank in the full 1,071-repo graph)** — how 'hub-like' each tool is within your starred ecosystem:

- `langwatch/langwatch` — PageRank 0.0020
- `huggingface/lighteval` — PageRank 0.0011
- `strands-agents/evals` — PageRank 0.0010
- `comet-ml/opik` — PageRank 0.0007
- `langfuse/langfuse` — PageRank 0.0006
- `NVIDIA/garak` — PageRank 0.0006
- `vllm-project/guidellm` — PageRank 0.0005
- `langchain-ai/openevals` — PageRank 0.0005

**Direct links between eval tools** (similarity edges where both endpoints are in this report):

- `confident-ai/deepteam` ⇄ `confident-ai/deepeval` (w=1.650) — topics: python; authors: A-Vamshi, kritinv, penguine-ip
- `langchain-ai/agentevals` ⇄ `langchain-ai/openevals` (w=0.950) — authors: jkennedyvz
- `comet-ml/opik-openclaw` ⇄ `comet-ml/opik` (w=0.800) — topics: evaluation, llm-observability; authors: awkoy, GuySaar8
- `langfuse/langfuse` ⇄ `comet-ml/opik` (w=0.524) — topics: llm, llmops, openai, open-source
- `truera/trulens` ⇄ `Arize-ai/phoenix` (w=0.368) — topics: llmops, ai-monitoring, ai-observability, evals
- `mlflow/mlflow` ⇄ `comet-ml/opik` (w=0.342) — topics: evaluation, langchain, llm-evaluation, llmops
- `langfuse/langfuse` ⇄ `mlflow/mlflow` (w=0.327) — topics: llmops, openai, observability, open-source; authors: github-actions[bot]
- `Arize-ai/phoenix` ⇄ `mlflow/mlflow` (w=0.312) — topics: llmops, agents, prompt-engineering, llm-evaluation; authors: github-actions[bot]
- `langwatch/langwatch` ⇄ `langfuse/langfuse` (w=0.300) — topics: analytics, evaluation, llm, observability
- `huggingface/lighteval` ⇄ `confident-ai/deepeval` (w=0.300) — topics: evaluation-framework, evaluation-metrics
- `truera/trulens` ⇄ `cvs-health/uqlm` (w=0.217) — topics: llm-evaluation; authors: feiiiiii5, Garyouki
- `huggingface/lighteval` ⇄ `EleutherAI/lm-evaluation-harness` (w=0.217) — topics: evaluation-framework
- `promptfoo/promptfoo` ⇄ `langfuse/langfuse` (w=0.206) — topics: llm, prompt-engineering, llmops, evaluation
- `rhesis-ai/rhesis` ⇄ `cvs-health/uqlm` (w=0.193) — authors: feiiiiii5
- `promptfoo/promptfoo` ⇄ `comet-ml/opik` (w=0.192) — topics: llm, prompt-engineering, llmops, evaluation
- `EleutherAI/lm-evaluation-harness` ⇄ `confident-ai/deepeval` (w=0.175) — topics: evaluation-framework

## Maintenance & risk signal

Bus factor = commit concentration (1 = single-maintainer risk). Pair with lifecycle + activity before adopting.

| Tool | Health | Lifecycle | Activity | Bus factor | Top-author share | Releases |
|---|---|---|---|---|---|---|
| langfuse/langfuse | 94 | Classic | very active | 4 | 24% | 711 |
| comet-ml/opik | 89 | Classic | very active | 3 | 26% | 613 |
| truera/trulens | 89 | Classic | very active | 3 | 21% | 127 |
| vllm-project/guidellm | 88 | Mature | very active | 3 | 22% | 20 |
| EleutherAI/lm-evaluation-harness | 87 | Classic | very active | 11 | 10% | 19 |
| langwatch/langwatch | 85 | Classic | very active | 2 | 35% | 409 |
| Arize-ai/phoenix | 84 | Classic | very active | 2 | 48% | 861 |
| mlflow/mlflow | 82 | Classic | very active | 2 | 47% | 178 |
| NVIDIA/garak | 82 | Classic | very active | 2 | 42% | 33 |
| rhesis-ai/rhesis | 79 | Mature | very active | 1 | 64% | 177 |
| promptfoo/promptfoo | 79 | Classic | very active | 1 | 69% | 430 |
| strands-agents/evals | 79 | Hot | very active | 3 | 32% | 31 |
| langchain-ai/openevals | 77 | Hot | very active | 2 | 42% | 44 |
| confident-ai/deepeval | 76 | Classic | very active | 1 | 50% | 63 |
| cvs-health/uqlm | 76 | Hot | very active | 1 | 63% | 46 |
| traceloop/openllmetry | 71 | Classic | active | 2 | 29% | 263 |
| LiveBench/LiveBench | 65 | Mature | very active | 2 | 48% | 0 |
| comet-ml/opik-openclaw | 64 | Rising | active | 1 | 60% | 26 |
| huggingface/lighteval | 60 | Mature | active | 2 | 38% | 15 |
| KRLabsOrg/LettuceDetect | 59 | Mature | very active | 1 | 64% | 13 |
| confident-ai/deepteam | 55 | Hot | very active | 1 | 84% | 3 |
| pinchbench/skill | 46 | Declining | slowing | 0 | 0% | 14 |
| langchain-ai/agentevals | 34 | Declining | slowing | 1 | 100% | 12 |
| openai/evals | 19 | Mature | slowing | 0 | 0% | 0 |
| jszheng21/RACE | 10 | Abandoned | stale | 0 | 0% | 0 |
| finos-labs/Open-Financial-LLMs-Leaderboard | 5 | Declining | stale | 0 | 0% | 0 |

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

<sub>Tools covered: 26 · Snapshot: 2026-10-10T15:21:10.911Z</sub>
