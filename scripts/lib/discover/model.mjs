// Optional semantic relevance from a local GLiClass zero-shot classifier.
// Keyword overlap cannot tell "agent runtime" from dotnet/runtime; a model
// reading the README can. Python runs out of process via uv, so discovery keeps
// working (keyword-only) on a machine without uv or the model.

import { spawnSync } from 'node:child_process';
import path from 'node:path';

export const MODEL = 'knowledgator/gliclass-modern-base-v3.0';
// What the pilot measured with; longer excerpts are untested and ~4x slower per 1k chars.
export const README_CHARS = 1200;

const SCRIPT = path.join(import.meta.dirname, 'gliclass_score.py');

/** The text the model reads. Must match the pilot's inputs for its numbers to hold. */
export function modelText(repo) {
  const head = `${repo.full_name}: ${repo.description ?? ''} Topics: ${(repo.topics ?? []).join(', ')}`;
  return `${head}\n${(repo.readme_excerpt ?? '').slice(0, README_CHARS)}`;
}

/** Run gliclass_score.py under uv. Throws with the script's last stderr line on failure. */
export function runPython(request) {
  const r = spawnSync('uv', ['run', '-q', '--python', '3.12', '--with', 'gliclass', 'python', SCRIPT], {
    input: JSON.stringify(request),
    encoding: 'utf8',
    maxBuffer: 64 * 1024 * 1024,
  });
  if (r.error) throw r.error;
  if (r.status !== 0) {
    const last = (r.stderr ?? '').trim().split('\n').pop() || `exit ${r.status}`;
    throw new Error(last);
  }
  return JSON.parse(r.stdout);
}

/**
 * Model relevance per repo, as the max probability over the report's category
 * labels. Returns `{ scores: Map | null, error }`; null scores mean "fall back
 * to keyword relevance", and `error` says why.
 */
export function modelRelevance(repos, labels, { run = runPython } = {}) {
  if (!repos.length || !labels.length) return { scores: new Map(), error: null };
  try {
    const out = run({
      model: MODEL,
      labels,
      items: repos.map((r) => ({ full_name: r.full_name, text: modelText(r) })),
    });
    return { scores: new Map(Object.entries(out.scores)), error: null };
  } catch (err) {
    return { scores: null, error: err.message };
  }
}
