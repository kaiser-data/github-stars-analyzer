import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts", "prompts"))

from promptlib import PROMPT_SECTION, inject_prompt_links, render_stack_table, resolve_stack  # noqa: E402

REPO_A = {"full_name": "fogleman/sdf", "stars": 2001, "health_score": 4, "lifecycle_stage": "Abandoned"}
REPO_B = {"full_name": "mikedh/trimesh", "stars": 3678, "health_score": 74, "lifecycle_stage": "Classic"}
BY_NAME = {"fogleman/sdf": REPO_A, "mikedh/trimesh": REPO_B}


def test_resolve_stack_returns_repos_in_declared_order():
    stack = [("Author", "fogleman/sdf"), ("Validate", "mikedh/trimesh")]
    resolved, missing = resolve_stack(stack, BY_NAME)
    assert missing == []
    assert [r[0] for r in resolved] == ["Author", "Validate"]
    assert resolved[0][2]["stars"] == 2001


def test_resolve_stack_reports_unresolved_entries():
    stack = [("Author", "fogleman/sdf"), ("Slice", "ghost/nope")]
    resolved, missing = resolve_stack(stack, BY_NAME)
    assert missing == ["ghost/nope"]
    assert len(resolved) == 1


def test_render_stack_table_rows_match_header_column_count():
    resolved, _ = resolve_stack([("Author", "fogleman/sdf"), ("Validate", "mikedh/trimesh")], BY_NAME)
    lines = render_stack_table(resolved)
    header_cols = len(lines[0].strip("|").split("|"))
    for row in lines[2:]:
        assert len(row.strip("|").split("|")) == header_cols


def test_inject_prompt_links_inserts_before_methodology(tmp_path):
    md = tmp_path / "r.md"
    md.write_text("# Title\n\n## Which one?\n\nbody\n\n## Methodology & caveats\n\nnotes\n")
    assert inject_prompt_links(str(md), [("Stump base", "stump-base", "A trophy base.")]) is True
    text = md.read_text()
    assert PROMPT_SECTION in text
    assert text.index(PROMPT_SECTION) < text.index("## Methodology & caveats")


def test_inject_prompt_links_appends_when_no_methodology(tmp_path):
    md = tmp_path / "r.md"
    md.write_text("# Title\n\nbody\n")
    assert inject_prompt_links(str(md), [("Stump base", "stump-base", "A trophy base.")]) is True
    assert PROMPT_SECTION in md.read_text()


def test_inject_prompt_links_is_idempotent(tmp_path):
    md = tmp_path / "r.md"
    md.write_text("# Title\n\nbody\n")
    inject_prompt_links(str(md), [("Stump base", "stump-base", "A trophy base.")])
    assert inject_prompt_links(str(md), [("Stump base", "stump-base", "A trophy base.")]) is False
    assert md.read_text().count(PROMPT_SECTION) == 1


def test_inject_prompt_links_noop_on_empty_list(tmp_path):
    md = tmp_path / "r.md"
    md.write_text("# Title\n\nbody\n")
    assert inject_prompt_links(str(md), []) is False
    assert PROMPT_SECTION not in md.read_text()
