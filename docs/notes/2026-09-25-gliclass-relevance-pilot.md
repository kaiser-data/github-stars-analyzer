# GLiClass as a discovery relevance signal — pilot, 2026-09-25

Question: can a local zero-shot classifier replace or improve the keyword
relevance (`rel`) in `discover.mjs`? This came up because hosted Jev is blocked
(TypeSafe signups paused), and GLiClass is the local option already covered in
the decision-classifiers report.

Model: `knowledgator/gliclass-modern-base-v3.0`, CPU, Apple M2 with 8 GB of RAM. Input:
`owner/repo: description Topics: …` plus the first 1,200 characters of the README.
Labels: the report's category names. Score: the highest probability over all labels.

## Resources

| | |
|---|---|
| Peak RAM | 1.27 GB |
| Load | 216 s the first time (includes the ~600 MB download), 1.3 s when cached |
| Description + topics only | 63–104 ms per repo |
| With README | 330–440 ms per repo |

## Offline test: labelled report members

- Positives: repos a report covers that are already starred (27–52 per report).
- Negatives: repos held by other reports. "Far" negatives come from 3D printing,
  blockchain and charting. "Near" negatives come from other AI reports, excluding
  any report whose scope overlaps the target.
- Threshold: set at 10% FPR on half the negatives, then read off the rest.
  Averaged over 20 splits.
- Self-check: shuffling the labels gives AUROC 0.43–0.55.

| Report | Scorer | AUROC (near) | TPR | FPR (near) |
|---|---|---|---|---|
| rag-tooling | keyword | 0.97 | 1.00 | 0.26 |
| | GLiClass + README | 0.88 | 0.68 | 0.13 |
| | 50/50 raw average | **0.99** | 1.00 | 0.12 |
| agentic-terminals | keyword | 0.86 | 0.72 | 0.15 |
| | GLiClass + README | 0.91 | 0.80 | 0.14 |
| | 50/50 raw average | **0.94** | 0.86 | 0.12 |
| voice-agents | keyword | 0.78 | 0.50 | 0.16 |
| | GLiClass + README | 0.90 | 0.82 | 0.11 |
| | 50/50 raw average | **0.90** | 0.74 | 0.14 |

What this showed:

- Using the description and topics alone lost to keywords. The README carries the gain.
- The keyword score takes only a few distinct values, so at a nominal 10% threshold its
  real FPR is 15–26%.
- A raw average ranked as well as a rank average. It was chosen because its value
  does not depend on how big the candidate pool is.

## Live test: search hits (`agentic-terminals`, 47 candidates)

The offline gain **did not transfer**.

- Every candidate scored between 0.63 and 1.00.
- Game emulators (`mgba-emu/mgba`, `cemu-project/Cemu`) scored 0.99 against the
  category "Emulator".
- Ranking known-gaps (which the report itself named) above new finds gave AUROC 0.34
  for keyword, 0.27 for the model and 0.30 combined.

That check is weak: only 7 gaps, and some of the new finds are real positives. It
still gives no support for the model. Search picks repos by the category words, so
bare category labels cannot tell a search hit apart from an in-scope repo.

## Live test 2: hand-labelled search hits (`agentic-terminals`, 47 candidates)

The same 47 search hits were labelled y/n in `data/labels-agentic-terminals.txt`
(34 y / 13 n). **The labels are Claude's**, made from descriptions and the report's
categories, and have not been reviewed by the owner yet.

Three label sets were compared:

- **A:** bare category names.
- **B:** category name plus the report title. This one is automatic.
- **C:** hand-written descriptions. These were written *after* seeing the labels,
  so C is optimistic and counts as an upper bound.

| Scorer | AUROC y>n | Off-topic in top 23 |
|---|---|---|
| keyword (current) | 0.66 | 4 |
| model, A bare | 0.70 | 3 |
| **combined, A bare** | **0.76** | 3 |
| model, B +title | 0.60 | 4 |
| combined, B +title | 0.71 | 3 |
| model, C hand-written | 0.71 | 5 |
| combined, C hand-written | 0.77 | 2 |

What this showed:

- Against real labels, the combined score beats keyword alone: 0.76 vs 0.66.
  Live test 1's known-gap proxy understated the model.
- Descriptive labels do not help. The automatic B is worse than A, and the tuned C
  barely beats A. Keep the bare category names.
- With only 13 negatives, the AUROC standard error is about ±0.08, so the gain is
  suggestive, not established. It needs the owner's labels and a second report.
- Offline mode, now automatic once the model is cached, cut a 47-repo pass from
  87 s to 26 s.

## Where it stands

- `--model` is opt-in and off by default. With it on, `rel` becomes the average of the
  keyword and model scores. The output always states which relevance was used.
- **Next step:** the owner corrects the labels in `data/labels-agentic-terminals.txt`
  and labels a second report. If the combined score still wins, make `--model` the
  default.
- Scratch pilot code (not committed): `export.mjs`, `score.py`, `dump.py`,
  `combine.py` and `live_eval.mjs`.
