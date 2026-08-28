// Output. The score is always shown decomposed — a total alone gives the
// reader nothing to overrule.

function cell(s) {
  return String(s ?? '').replace(/\|/g, '\\|').replace(/\n/g, ' ');
}

function pct(n) {
  return `${Math.round((n ?? 0) * 100)}`;
}

export function renderMarkdown(result) {
  const { slug, generated, heldCount, candidates, renamed, unresolved } = result;
  const gaps = candidates.filter((c) => c.state === 'known-gap');
  const fresh = candidates.filter((c) => c.state === 'new');

  const lines = [];
  lines.push(`# Candidates for \`${slug}\``);
  lines.push('');
  lines.push(`Generated ${generated}. ${heldCount} repos in this landscape are already starred; `
    + `${gaps.length} are named by the report but unstarred (\`known-gap\`), and ${fresh.length} are new finds.`);
  lines.push('');
  lines.push('`known-gap` means the report already judged it in-scope — the only open question is whether to star it.');
  lines.push('');
  lines.push('| # | Repo | State | Kind | ★ | Lang | Licence | Stage | Health | Pushed | Bus | Fit | rel/std/hlt/rec | What it is |');
  lines.push('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|');

  candidates.forEach((c, i) => {
    const p = c.score.parts;
    lines.push('| ' + [
      i + 1,
      `[${cell(c.full_name)}](https://github.com/${c.full_name})`,
      c.state,
      c.kind,
      (c.stars ?? 0).toLocaleString('en-US'),
      cell(c.primary_language ?? '—'),
      cell(c.license ?? 'none'),
      c.lifecycle_stage,
      c.health_score,
      `${c.days_since_push}d`,
      c.bus_factor,
      `**${c.score.total}**`,
      `${pct(p.relevance)}/${pct(p.standing)}/${pct(p.health)}/${pct(p.recency)}`,
      cell((c.description ?? '').slice(0, 110)),
    ].join(' | ') + ' |');
  });

  if (renamed.length) {
    lines.push('', '## Renames followed', '');
    lines.push('The API resolved these to a different name. The set-diff used the resolved one.', '');
    for (const r of renamed) lines.push(`- \`${r.from}\` → \`${r.to}\``);
  }

  if (unresolved.length) {
    lines.push('', '## Unresolved', '');
    lines.push('Names that did not resolve to a repo. A name supplied via `--extra` landing here '
      + 'means it was misremembered, not that the repo is obscure.', '');
    for (const u of unresolved) lines.push(`- \`${u}\``);
  }

  lines.push('');
  return lines.join('\n');
}

export function renderJson(result) {
  return {
    slug: result.slug,
    generated: result.generated,
    held_count: result.heldCount,
    counts: {
      known_gap: result.candidates.filter((c) => c.state === 'known-gap').length,
      new: result.candidates.filter((c) => c.state === 'new').length,
      renamed: result.renamed.length,
      unresolved: result.unresolved.length,
    },
    candidates: result.candidates,
    renamed: result.renamed,
    unresolved: result.unresolved,
  };
}
