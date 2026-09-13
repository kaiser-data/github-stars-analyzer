import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED_META_KEYS = {
    "slug", "title", "file", "report", "summary", "stack", "brief", "generated", "generator",
}


def run_generator(name):
    proc = subprocess.run(
        [sys.executable, os.path.join(ROOT, "scripts", "prompts", name)],
        cwd=ROOT, capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stderr
    return proc.stdout


def table_columns_match(md_text):
    lines = md_text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        is_sep = (
            i + 1 < len(lines)
            and lines[i + 1].startswith("|")
            and set(lines[i + 1].replace("|", "").replace(" ", "")) <= {"-", ":"}
            and lines[i + 1].replace("|", "").strip() != ""
        )
        if line.startswith("|") and is_sep:
            n = len(line.strip("|").split("|"))
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                if len(lines[i].strip("|").split("|")) != n:
                    return False
                i += 1
        else:
            i += 1
    return True


def test_stump_base_generates_without_drift():
    out = run_generator("stump_base.py")
    assert "WARNING missing:" not in out
    assert "stack: " in out


def test_stump_base_meta_has_required_keys_and_nonempty_brief():
    run_generator("stump_base.py")
    with open(os.path.join(ROOT, "prompts", "stump-base.meta.json")) as f:
        meta = json.load(f)
    assert REQUIRED_META_KEYS <= set(meta)
    assert meta["report"] == "3d-printing-stack"
    assert len(meta["brief"].strip()) > 500
    assert len(meta["stack"]) >= 3


def test_stump_base_markdown_tables_are_well_formed():
    run_generator("stump_base.py")
    with open(os.path.join(ROOT, "prompts", "stump-base.md")) as f:
        assert table_columns_match(f.read())


import pytest


@pytest.mark.parametrize("gen,slug,report", [
    ("rag_eval_harness.py", "rag-eval-harness", "rag-tooling"),
    ("trading_dashboard.py", "trading-dashboard", "charting-stack"),
])
def test_additional_prompts_generate_cleanly(gen, slug, report):
    out = run_generator(gen)
    assert "WARNING missing:" not in out
    with open(os.path.join(ROOT, "prompts", f"{slug}.meta.json")) as f:
        meta = json.load(f)
    assert REQUIRED_META_KEYS <= set(meta)
    assert meta["report"] == report
    assert len(meta["brief"].strip()) > 500
    with open(os.path.join(ROOT, "prompts", f"{slug}.md")) as f:
        assert table_columns_match(f.read())


def test_rag_prompt_has_no_inputs_table():
    """INPUTS=None must render no 'Measure these first' section."""
    run_generator("rag_eval_harness.py")
    with open(os.path.join(ROOT, "prompts", "rag-eval-harness.md")) as f:
        assert "Measure these first" not in f.read()
