import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts", "prompts"))


def run_build():
    proc = subprocess.run(
        [sys.executable, os.path.join(ROOT, "scripts", "prompts", "build_prompts.py")],
        cwd=ROOT, capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    return proc.stdout


def test_build_writes_public_index_with_briefs():
    run_build()
    with open(os.path.join(ROOT, "public", "prompts", "index.json")) as f:
        index = json.load(f)
    assert index["count"] >= 1
    assert index["count"] == len(index["prompts"])
    for p in index["prompts"]:
        assert p["brief"].strip()
        assert p["report"]


def test_build_copies_markdown_to_public():
    run_build()
    with open(os.path.join(ROOT, "public", "prompts", "index.json")) as f:
        index = json.load(f)
    for p in index["prompts"]:
        assert os.path.exists(os.path.join(ROOT, "public", "prompts", p["file"]))


def test_cross_link_appears_once_after_two_consecutive_runs():
    from promptlib import PROMPT_SECTION
    run_build()
    run_build()
    with open(os.path.join(ROOT, "reports", "3d-printing-stack.md")) as f:
        text = f.read()
    assert text.count(PROMPT_SECTION) == 1


def test_full_build_leaves_public_report_and_repo_report_identical():
    """The cross-link must reach public/reports/, not just reports/."""
    proc = subprocess.run(
        [sys.executable, os.path.join(ROOT, "scripts", "reports", "build_index.py")],
        cwd=ROOT, capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    with open(os.path.join(ROOT, "reports", "3d-printing-stack.md")) as f:
        repo_copy = f.read()
    with open(os.path.join(ROOT, "public", "reports", "3d-printing-stack.md")) as f:
        public_copy = f.read()
    assert repo_copy == public_copy
    from promptlib import PROMPT_SECTION
    assert PROMPT_SECTION in public_copy
