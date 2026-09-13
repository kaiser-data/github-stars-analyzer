# Retrieval-evaluation harness

> Built from the **rag-tooling** report, against 2,140 starred repos (snapshot `2026-09-12T16:25:05.965Z`). Regenerate any time — no API cost.

A home-made RAG eval is the easiest place in the whole stack to fool yourself: it is trivial to get a single number out, and almost as trivial for that number to be meaningless because it blends retrieval and generation into one score. This harness keeps the two apart on purpose and gives retrieval a keyword-only floor to be read against, so a change in generation prompt can never masquerade as better retrieval.

## The stack this uses

| Stage | Tool | Stars | Health | Lifecycle |
|---|---|---|---|---|
| Retrieve | [`deepset-ai/haystack`](https://github.com/deepset-ai/haystack) | 26,430 | 79 | Classic |
| Index | [`qdrant/qdrant`](https://github.com/qdrant/qdrant) | 34,404 | 92 | Classic |
| Embed | [`huggingface/sentence-transformers`](https://github.com/huggingface/sentence-transformers) | 19,074 | 74 | Classic |
| Judge | [`KRLabsOrg/LettuceDetect`](https://github.com/KRLabsOrg/LettuceDetect) | 602 | 66 | Hot |

Metrics are live from the dataset. A low health score in retrieval libraries usually means *finished*, not dead — see the parent report's maintenance section.

## The prompt

> You are writing Python that builds a retrieval-evaluation harness for a
> retrieval-augmented-generation pipeline. Output a single script plus one data file,
> nothing else.
>
> **Deliverable:** a harness that loads a document set, builds an index over it, runs a
> fixed question set against that index, and writes per-question results to a CSV — one
> row per question, never an aggregate-only summary. The CSV is the artifact; the console
> report is derived from it, not the other way round.
>
> **Keep retrieval quality and generation quality in separate columns, and never blend
> them into one number.** Recall@k and MRR (mean reciprocal rank) are retrieval metrics —
> they ask only whether the right chunk was fetched, and at what rank. Faithfulness and
> answer-correctness are generation metrics — they ask whether the model's final answer is
> supported by and consistent with what was fetched. These measure different failure
> modes: a retrieval miss and a generation hallucination look identical in a single
> blended score but need opposite fixes. The CSV must carry `recall_at_k`, `mrr`,
> `faithfulness`, and `answer_correctness` as four distinct columns, and the script must
> refuse to print or write any single score that averages across that boundary. Score a
> run as "retrieval failed" or "generation failed" separately — never as one number that
> hides which stage broke.
>
> **Reproducibility:** fix the random seed as a top-level constant, `SEED = 42`, and pass
> it to every stochastic step — negative sampling for the question set, any shuffling of
> the document set, and any sampling used by the embedding or index step. Two runs on the
> same corpus and question set must produce byte-identical CSVs.
>
> **Baseline flag:** add a `--baseline` command-line flag that runs the retrieval step
> with embeddings disabled, falling back to plain keyword (BM25-style) matching only. A
> recall@k of 0.9 means nothing on its own — it means something only next to what
> keyword-only retrieval gets on the same questions. Running with `--baseline` must
> produce a second, clearly-labelled CSV (`results_baseline.csv`) alongside the normal
> one (`results.csv`), and the harness must refuse to claim an improvement unless the
> embedding-based run is compared against its own baseline run, not a baseline from a
> different corpus.
>
> **Question set:** the fixed question set (question text plus the expected/gold document
> id or span) must live in its own file, `questions.jsonl`, one JSON object per line —
> never embedded as a Python literal inside the script. The script loads this file at
> run time; changing the eval set must never require touching the harness code.
>
> **Pipeline, naming each tool where it is used:**
>
> 1. **Embed** — use `huggingface/sentence-transformers` to embed both the document
>    chunks and the incoming questions into the same vector space.
> 2. **Index** — use `qdrant/qdrant` as the vector index: upsert the embedded chunks with
>    their source document id as payload, and query it for the top-k nearest neighbours
>    per question.
> 3. **Retrieve** — use `deepset-ai/haystack` to wire the embedding and index steps into
>    a retrieval pipeline object, so the retrieval stage is a single composable component
>    rather than hand-rolled glue code, and so `--baseline` can swap in a keyword
>    retriever at exactly this seam.
> 4. **Judge** — use `KRLabsOrg/LettuceDetect` as the faithfulness/hallucination judge
>    over the generated answer against the retrieved context, to produce the
>    `faithfulness` column. Do not let this judge see or influence the retrieval-metric
>    columns; it only ever scores the generation half.
>
> Chunk documents at a fixed size (state it as a constant, e.g. `CHUNK_SIZE = 400` tokens)
> with a fixed overlap, so chunk boundaries are reproducible run to run.
>
> Print a short console summary at the end: mean recall@k, mean MRR, mean faithfulness,
> mean answer-correctness, and — only when `--baseline` was used — the delta between the
> embedding run and the baseline run for each retrieval metric, never for the generation
> metrics (a keyword-only baseline has no generation stage to compare).

## Variants

Append one of these:

- **Multi-hop questions** — "Extend the question set format with a list of gold document ids instead of one, and change recall@k to require all of them."
- **Chunking sweep** — "Wrap the harness in an outer loop over a list of CHUNK_SIZE values and append the chunk size as a column, so the CSV can answer 'what chunk size maximises recall@k' directly."
- **Cross-encoder rerank** — "Add an optional rerank stage after retrieval and before Judge, and add a `reranked` boolean column so its effect is isolated rather than folded into the base recall@k numbers."

## Verify before you print

```bash
# generate on a tiny corpus
python3 rag_eval_harness.py --corpus tiny_corpus/ --questions questions.jsonl
```

```bash
# assert one row per question
python3 -c "
import csv
rows = list(csv.DictReader(open('results.csv')))
questions = sum(1 for _ in open('questions.jsonl'))
assert len(rows) == questions, (len(rows), questions)
print('rows == questions:', len(rows))
"
```

```bash
# re-run with the baseline and confirm scores drop
python3 rag_eval_harness.py --corpus tiny_corpus/ --questions questions.jsonl --baseline
```

If `results_baseline.csv` scores as high as `results.csv`, the embedding step is
not adding anything on this question set — that is a real finding about the corpus, not a
bug in the harness. Look at which questions the baseline gets right: keyword search wins
on exact-term lookups, and only loses once questions paraphrase away from the source
vocabulary. That gap is what the embedding step is buying you, and it should be visible
question-by-question in the CSV, not just in the mean.

Never let a good faithfulness score paper over a bad recall@k — a generator can sound
faithful to context that was the wrong context. Read the two metrics together before
trusting either alone.

<sub>Generated by `scripts/prompts/rag_eval_harness.py` · parent report: `rag-tooling`</sub>
