#!/usr/bin/env python3
"""
Archive a compact snapshot of the current classified.json so reports can show
trends (star velocity, newly-archived repos, lifecycle moves) across refreshes.

Writes data/snapshots/<YYYY-MM-DD>.json keyed by the dataset's generatedAt
date — not today's date — so re-running against the same data vintage is
idempotent and snapshots line up with when the data was actually fetched.

Run: python3 scripts/reports/snapshot.py   (build_index.py runs it first)
"""
import json
import os

from lib import CLASSIFIED, SNAPSHOT_DIR, SNAPSHOT_FIELDS


def main():
    with open(CLASSIFIED) as f:
        cl = json.load(f)
    date = (cl.get("generatedAt") or "")[:10]
    if not date:
        raise SystemExit("classified.json has no generatedAt — refusing to snapshot")

    snap = {
        "date": date,
        "generatedAt": cl.get("generatedAt"),
        "total": cl.get("total"),
        "repos": {
            r["full_name"]: {k: r.get(k) for k in SNAPSHOT_FIELDS}
            for r in cl["repos"]
        },
    }
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    out = os.path.join(SNAPSHOT_DIR, f"{date}.json")
    with open(out, "w") as f:
        json.dump(snap, f, separators=(",", ":"))
    print(f"Wrote {out} ({len(snap['repos'])} repos)")


if __name__ == "__main__":
    main()
