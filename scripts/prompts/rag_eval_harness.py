#!/usr/bin/env python3
"""Prompt: a retrieval-evaluation harness, built with the rag-tooling stack.

Run: python3 scripts/prompts/rag_eval_harness.py
"""
import json
import os
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts", "reports"))

from promptlib import CLASSIFIED, render_stack_table, resolve_stack  # noqa: E402

SLUG = "rag-eval-harness"
TITLE = "Retrieval-evaluation harness"
REPORT = "rag-tooling"
SUMMARY = ("A retrieval-evaluation harness that scores recall@k and MRR against a fixed "
           "question set, with a keyword-only baseline so every number has a floor.")

STACK = [
    ("Retrieve", "deepset-ai/haystack"),
    ("Index", "qdrant/qdrant"),
    ("Embed", "huggingface/sentence-transformers"),
    ("Judge", "KRLabsOrg/LettuceDetect"),
]

# Per-generator heading + health caveat (promptlib intentionally has no shared
# renderer for these — see the TODO there). The "low health usually means
# finished" caveat was earned for geometry/algorithm libraries in the
# 3d-printing-stack report; staleness is a real liability in retrieval
# libraries, and this table has nothing unhealthy in it anyway, so it stays off.
VERIFY_HEADING = "## Verify before you trust the numbers"
HEALTH_CAVEAT = ""

WHY = ("A home-made RAG eval is the easiest place in the whole stack to fool yourself: it is "
       "trivial to get a single number out, and almost as trivial for that number to be "
       "meaningless because it blends retrieval and generation into one score. This harness "
       "keeps the two apart on purpose and gives retrieval a keyword-only floor to be read "
       "against, so a change in generation prompt can never masquerade as better retrieval.")

INPUTS = None

BRIEF = """You are writing Python that builds a retrieval-evaluation harness for a
retrieval-augmented-generation pipeline. Output a single script plus one data file,
nothing else.

**Deliverable:** a harness that loads a document set, builds an index over it, runs a
fixed question set against that index, and writes per-question results to a CSV — one
row per question, never an aggregate-only summary. The CSV is the artifact; the console
report is derived from it, not the other way round.

**Keep retrieval quality and generation quality in separate columns, and never blend
them into one number.** Recall@k and MRR (mean reciprocal rank) are retrieval metrics —
they ask only whether the right chunk was fetched, and at what rank. Faithfulness is a
generation metric — it asks whether the model's final answer is supported by and
consistent with what was fetched. These measure different failure modes: a retrieval
miss and a generation hallucination look identical in a single blended score but need
opposite fixes. The CSV must carry `recall_at_k`, `mrr`, and `faithfulness` as three
distinct columns, and the script must refuse to print or write any single score that
averages across that boundary. Score a run as "retrieval failed" or "generation failed"
separately — never as one number that hides which stage broke.

Deliberately absent: answer-correctness. Scoring it needs a gold answer to compare the
model's answer against, and `questions.jsonl` below carries only a gold document id or
span — no gold answer exists to score against. A number nothing here can ground is
worse than no number, so this harness reports faithfulness only.

**Reproducibility:** fix the random seed as a top-level constant, `SEED = 42`, and pass
it to every stochastic step — negative sampling for the question set, any shuffling of
the document set, and any sampling used by the embedding or index step. Two runs on the
same corpus and question set must produce byte-identical `recall_at_k` and `mrr`
columns — the retrieval half of the pipeline has no stochastic step it doesn't control,
so it has no excuse not to be deterministic. `faithfulness` depends on the generation
step below and is *not* covered by this guarantee: LLM output is not reliably
byte-identical run to run, even at temperature 0, across providers or model versions.
Do not claim byte-identical generation metrics — only the two retrieval columns carry
that promise.

**Baseline flag:** add a `--baseline` command-line flag that runs the retrieval step
with embeddings disabled, falling back to plain keyword (BM25-style) matching only. A
recall@k of 0.9 means nothing on its own — it means something only next to what
keyword-only retrieval gets on the same questions. Running with `--baseline` must
produce a second, clearly-labelled CSV (`results_baseline.csv`) alongside the normal
one (`results.csv`), and the harness must refuse to claim an improvement unless the
embedding-based run is compared against its own baseline run, not a baseline from a
different corpus.

**Question set:** the fixed question set (question text plus the expected/gold document
id or span) must live in its own file, `questions.jsonl`, one JSON object per line —
never embedded as a Python literal inside the script. The script loads this file at
run time; changing the eval set must never require touching the harness code.

**Pipeline, naming each tool where it is used:**

1. **Embed** — use `huggingface/sentence-transformers` to embed both the document
   chunks and the incoming questions into the same vector space.
2. **Index** — use `qdrant/qdrant` as the vector index: upsert the embedded chunks with
   their source document id as payload, and query it for the top-k nearest neighbours
   per question.
3. **Retrieve** — use `deepset-ai/haystack` to wire the embedding and index steps into
   a retrieval pipeline object, so the retrieval stage is a single composable component
   rather than hand-rolled glue code, and so `--baseline` can swap in a keyword
   retriever at exactly this seam.
4. **Generate** — produce the answer that step 5 judges; without this step nothing
   exists for the judge to score. There is no curated generation tool in this stack, so
   use whatever model you have on hand — a local model, a hosted API, even the same
   model you are using to write this harness — and record which one as a comment at
   the top of the script. Feed it only the question plus the top-k retrieved chunks, so
   a bad answer traces back to bad retrieval rather than the model ignoring the context
   it was given.
5. **Judge** — use `KRLabsOrg/LettuceDetect` as the faithfulness/hallucination judge
   over the generated answer against the retrieved context, to produce the
   `faithfulness` column. Do not let this judge see or influence the retrieval-metric
   columns; it only ever scores the generation half.

Chunk documents at a fixed size (state it as a constant, e.g. `CHUNK_SIZE = 400` tokens)
with a fixed overlap, so chunk boundaries are reproducible run to run.

Print a short console summary at the end: mean recall@k, mean MRR, mean faithfulness,
and — only when `--baseline` was used — the delta between the embedding run and the
baseline run for each retrieval metric, never for the generation metric (a
keyword-only baseline has no generation stage to compare)."""

VARIANTS = [
    ("Multi-hop questions", "Extend the question set format with a list of gold document "
                            "ids instead of one, and change recall@k to require all of them."),
    ("Chunking sweep", "Wrap the harness in an outer loop over a list of CHUNK_SIZE values "
                       "and append the chunk size as a column, so the CSV can answer "
                       "'what chunk size maximises recall@k' directly."),
    ("Cross-encoder rerank", "Add an optional rerank stage after retrieval and before Judge, "
                             "and add a `reranked` boolean column so its effect is isolated "
                             "rather than folded into the base recall@k numbers."),
]

VERIFY = [
    ("generate on a tiny corpus", "python3 rag_eval_harness.py --corpus tiny_corpus/ "
                                  "--questions questions.jsonl"),
    ("assert one row per question", """python3 -c "
import csv
rows = list(csv.DictReader(open('results.csv')))
questions = sum(1 for _ in open('questions.jsonl'))
assert len(rows) == questions, (len(rows), questions)
print('rows == questions:', len(rows))
\""""),
    ("re-run with the baseline and confirm scores drop",
     "python3 rag_eval_harness.py --corpus tiny_corpus/ --questions questions.jsonl --baseline"),
]

CLOSING = """If `results_baseline.csv` scores as high as `results.csv`, the embedding step is
not adding anything on this question set — that is a real finding about the corpus, not a
bug in the harness. Look at which questions the baseline gets right: keyword search wins
on exact-term lookups, and only loses once questions paraphrase away from the source
vocabulary. That gap is what the embedding step is buying you, and it should be visible
question-by-question in the CSV, not just in the mean.

Never let a good faithfulness score paper over a bad recall@k — a generator can sound
faithful to context that was the wrong context. Read the two metrics together before
trusting either alone."""


def main():
    with open(CLASSIFIED) as f:
        cl = json.load(f)
    by_name = {r["full_name"]: r for r in cl["repos"]}
    resolved, missing = resolve_stack(STACK, by_name)

    out_md = os.path.join(ROOT, f"prompts/{SLUG}.md")
    out_meta = os.path.join(ROOT, f"prompts/{SLUG}.meta.json")
    os.makedirs(os.path.join(ROOT, "prompts"), exist_ok=True)

    L = []
    L.append(f"# {TITLE}")
    L.append("")
    if missing:
        # Drift is non-fatal at the build level, so the prompt itself has to say
        # so — otherwise a reader pastes a prompt naming a tool that is gone.
        L.append(f"> ⚠ **{len(missing)} tool(s) in this stack no longer resolve in the dataset:** "
                 + ", ".join(f"`{m}`" for m in missing)
                 + ". They were archived, renamed or unstarred. Re-point them in "
                 + f"`scripts/prompts/{os.path.basename(__file__)}` before relying on this prompt.")
        L.append("")
    L.append(f"> Built from the **{REPORT}** report, against {cl['total']:,} starred repos "
             f"(snapshot `{cl.get('generatedAt','')}`). Regenerate any time — no API cost.")
    L.append("")
    L.append(WHY)
    L.append("")
    L.append("## The stack this uses")
    L.append("")
    L.extend(render_stack_table(resolved))
    L.append("")
    L.append(("Metrics are live from the dataset." + HEALTH_CAVEAT).strip())
    L.append("")
    if INPUTS:
        L.append("## Measure these first")
        L.append("")
        L.append("| Input | What to measure | Why it drives the shape |")
        L.append("|---|---|---|")
        for name, what, why in INPUTS:
            L.append(f"| `{name}` | {what} | {why} |")
        L.append("")
    L.append("## The prompt")
    L.append("")
    for line in BRIEF.split("\n"):
        L.append(f"> {line}" if line else ">")
    L.append("")
    L.append("## Variants")
    L.append("")
    L.append("Append one of these:")
    L.append("")
    for label, text in VARIANTS:
        L.append(f"- **{label}** — \"{text}\"")
    L.append("")
    L.append(VERIFY_HEADING)
    L.append("")
    for comment, cmd in VERIFY:
        L.append(f"```bash")
        L.append(f"# {comment}")
        L.append(cmd)
        L.append("```")
        L.append("")
    L.append(CLOSING)
    L.append("")
    L.append(f"<sub>Generated by `scripts/prompts/{os.path.basename(__file__)}` · "
             f"parent report: `{REPORT}`</sub>")

    with open(out_md, "w") as f:
        f.write("\n".join(L) + "\n")

    meta = {
        "slug": SLUG,
        "title": TITLE,
        "file": f"{SLUG}.md",
        "report": REPORT,
        "summary": SUMMARY,
        "stack": [
            {"stage": s, "name": n, "stars": r.get("stars"),
             "health": r.get("health_score"), "lifecycle": r.get("lifecycle_stage")}
            for s, n, r in resolved
        ],
        "brief": BRIEF,
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "generator": f"scripts/prompts/{os.path.basename(__file__)}",
    }
    with open(out_meta, "w") as f:
        json.dump(meta, f, indent=2)

    print(f"Wrote {out_md}")
    print(f"Wrote {out_meta}")
    print(f"  stack: {len(resolved)} / {len(STACK)} resolved")
    if missing:
        print("  WARNING missing:", missing)


if __name__ == "__main__":
    main()
