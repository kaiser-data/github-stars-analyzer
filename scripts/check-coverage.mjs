// Coverage gate: find starred repos a report already wants but never curated.
//
// Drift detection runs in exactly one direction. Each generator warns when a
// curated entry is no longer in the dataset — a repo renamed, archived or
// unstarred. That direction is well covered and stays with the generators,
// which are the only thing that knows which absences are deliberate (e.g.
// blockchain_essentials.py's EXTERNAL entries are archived on purpose).
//
// The other direction has nothing watching it. `discover.mjs` surfaces repos
// that belong in a landscape but are not starred; when one is then starred it
// enters the dataset, and if nobody edits the generator it lands in no curated
// list. It is now on-topic, owned, and invisible: no report mentions it, so no
// warning can ever fire for it. Measured 2026-09-07: 0 entries drifting,
// 70 repos sitting in that blind spot.
//
// This is the missing half, and only that half. It exits non-zero when the
// backlog grows past a threshold, so "we starred it and forgot" stops being a
// silent state.
//
// Usage: node scripts/check-coverage.mjs [--max-blind=70] [--min-stars=0]
//                                        [--json] [--quiet]

import { readFileSync, readdirSync, existsSync } from 'node:fs';
import path from 'node:path';

const args = process.argv.slice(2);
const arg = (name, fallback) => {
  const a = args.find((x) => x.startsWith(`--${name}=`));
  if (a) return a.split('=').slice(1).join('=');
  const i = args.indexOf(`--${name}`);
  return i > -1 && args[i + 1] && !args[i + 1].startsWith('--') ? args[i + 1] : fallback;
};
const flag = (n) => args.includes(`--${n}`);

const ROOT = path.resolve(import.meta.dirname, '..');
const REPORTS = path.join(ROOT, 'reports');
const GENERATORS = path.join(ROOT, 'scripts', 'reports');
const MAX_BLIND = Number(arg('max-blind', 70));
const MIN_STARS = Number(arg('min-stars', 0));

const classified = path.join(ROOT, arg('classified', 'data/classified.json'));
if (!existsSync(classified)) {
  console.error(`✗ Coverage check failed: ${classified} not found — run npm run refresh:classify first.`);
  process.exit(1);
}

const dataset = new Map(
  JSON.parse(readFileSync(classified, 'utf8')).repos.map((r) => [r.full_name.toLowerCase(), r]),
);

// "Curated" means a generator names the repo in a module-level constant, which
// is what makes drift detection able to see it. Do NOT key this on the name
// TAXONOMY: 21 generators use it, but which_claw.py curates into CANDIDATES and
// SHINES, hermes_vs_openclaw.py into FIELD, trending_now.py into THEMES, and
// blockchain_claws.py into CLAWS and SKILLS. Keying on one name would report
// those entries as a blind spot they are not in.
//
// Scanned as text rather than imported: 21 of the 26 generators write their
// report as an import side effect, so importing to introspect would rebuild the
// repo. Scanning is therefore loose, and picks up prose ("mac/linux"), paths
// ("reports/foo.md") and other one-slash strings — so a scanned slug only
// counts once the dataset confirms it is a real starred repo. That filter is
// exact for the question asked here, which is only ever whether a repo already
// in the dataset is curated.
const NOT_A_GENERATOR = new Set(['lib.py', 'build_index.py', 'snapshot.py', 'render_html.py']);
const generators = readdirSync(GENERATORS).filter((f) => f.endsWith('.py') && !NOT_A_GENERATOR.has(f));
const curated = new Set();
let generatorsWithCuration = 0;

for (const g of generators) {
  const src = readFileSync(path.join(GENERATORS, g), 'utf8');
  let found = false;
  for (const m of src.matchAll(/^([A-Z][A-Z0-9_]*)\s*(?::[^=\n]+)?=/gm)) {
    const rest = src.slice(m.index);
    const end = rest.search(/\n(?=[A-Za-z_#@])/);
    const body = end === -1 ? rest : rest.slice(0, end);
    // Slugs appear as dict keys and as tuple/list members, so match the string
    // itself rather than a trailing colon.
    for (const q of body.matchAll(/["']([A-Za-z0-9._-]+\/[A-Za-z0-9._-]+)["']/g)) {
      const slug = q[1].toLowerCase();
      if (!dataset.has(slug)) continue;
      curated.add(slug);
      found = true;
    }
  }
  if (found) generatorsWithCuration += 1;
}

// A repo is "on topic" because a report's own discovery pass said so.
const wanted = new Map();
for (const f of readdirSync(REPORTS).filter((f) => f.endsWith('.candidates.json'))) {
  const d = JSON.parse(readFileSync(path.join(REPORTS, f), 'utf8'));
  for (const c of d.candidates) {
    const k = c.full_name.toLowerCase();
    if (!wanted.has(k)) wanted.set(k, new Set());
    wanted.get(k).add(d.slug);
  }
}

const blind = [];
for (const [k, reports] of wanted) {
  const r = dataset.get(k);
  if (!r || curated.has(k)) continue;
  if ((r.stars ?? 0) < MIN_STARS) continue;
  blind.push({
    full_name: r.full_name,
    stars: r.stars ?? 0,
    health_score: r.health_score ?? null,
    lifecycle_stage: r.lifecycle_stage ?? null,
    reports: [...reports].sort(),
  });
}
// Repos several landscapes wanted rank first — that overlap is a relevance
// signal, and it is also the strongest evidence the omission was an oversight.
blind.sort((a, b) => b.reports.length - a.reports.length || b.stars - a.stars);

if (flag('json')) {
  console.log(JSON.stringify({ blind, curated: curated.size, generatorsWithCuration }, null, 2));
} else if (!flag('quiet')) {
  console.error(
    `Coverage: ${curated.size} curated entries across ${generatorsWithCuration}/${generators.length} ` +
    `generators; ${blind.length} starred and on-topic but uncurated.`,
  );
  if (blind.length) {
    console.error('');
    console.error('  Starred, wanted by a report, in no curated list — nothing watches these:');
    for (const b of blind.slice(0, 25)) {
      console.error(
        `    ${b.full_name.padEnd(44)} ${String(b.stars).padStart(7)}★  ` +
        `${b.reports.length > 1 ? `${b.reports.length} reports: ` : ''}${b.reports.join(', ')}`,
      );
    }
    if (blind.length > 25) console.error(`    … and ${blind.length - 25} more (--json for all)`);
  }
}

if (blind.length > MAX_BLIND) {
  console.error('');
  console.error(`✗ Coverage check failed: ${blind.length} uncurated on-topic repos (limit ${MAX_BLIND}).`);
  console.error("  Curate them into the listed report's generator, or raise --max-blind deliberately.");
  process.exit(1);
}

if (!flag('quiet') && !flag('json')) {
  console.error('');
  console.error(`✓ Coverage check: ${blind.length} uncurated (limit ${MAX_BLIND}).`);
}
