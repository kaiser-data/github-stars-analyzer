"""Score repos against a report's category labels with GLiClass.

Called by model.mjs. Reads {"model", "labels", "items": [{"full_name", "text"}]}
as JSON on stdin and writes {"model", "scores": {full_name: probability}} on
stdout. Library chatter is redirected to stderr so stdout stays parseable.
"""
import contextlib
import json
import sys

BATCH = 16


def main():
    req = json.load(sys.stdin)
    labels, items = req["labels"], req["items"]
    scores = {}
    with contextlib.redirect_stdout(sys.stderr):
        from gliclass import GLiClassModel, ZeroShotClassificationPipeline
        from transformers import AutoTokenizer

        model = GLiClassModel.from_pretrained(req["model"])
        tok = AutoTokenizer.from_pretrained(req["model"], add_prefix_space=True)
        pipe = ZeroShotClassificationPipeline(model, tok, classification_type="multi-label", device="cpu")
        for i in range(0, len(items), BATCH):
            batch = items[i:i + BATCH]
            results = pipe([it["text"] for it in batch], labels, threshold=0.0, batch_size=BATCH)
            for it, res in zip(batch, results):
                scores[it["full_name"]] = max((r["score"] for r in res), default=0.0)
    json.dump({"model": req["model"], "scores": scores}, sys.stdout)


if __name__ == "__main__":
    main()
