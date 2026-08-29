// The dataset's exclusion list. See data/ignore-repos.txt for what is on it
// and why — the reasons matter more than the names, since a bare list rots.

import { readFileSync } from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '../..');

/** Parse the ignore file into a lower-cased Set. Missing file means ignore nothing. */
export function loadIgnored({ root = ROOT } = {}) {
  let raw;
  try {
    raw = readFileSync(path.join(root, 'data/ignore-repos.txt'), 'utf8');
  } catch {
    return new Set();
  }
  return new Set(
    raw
      .split('\n')
      .map((l) => l.replace(/#.*$/, '').trim())
      .filter((l) => /^[^/\s]+\/[^/\s]+$/.test(l))
      .map((l) => l.toLowerCase()),
  );
}
