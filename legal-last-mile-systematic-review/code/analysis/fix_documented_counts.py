#!/usr/bin/env python3
"""Propose (and optionally apply) the number edits the verifier asks for after a real screening or extraction change.

After an A16 resolution, a criterion-3 exclusion or any dated data script, `verify_repository.py` reports hand-written figures that no longer match the data,
as lines like  "README.md: expected to contain '1,154 studies extracted' (extraction row)". The expected phrase is computed from the databases, so the fix is
mechanical: find the old phrase in that file (the same text with different numbers) and replace it. This script does exactly that and nothing cleverer:
  * it runs the verifier and parses every "expected to contain '...'" and "A16 figure out of date, expected the phrase '...'" failure;
  * it turns the expected phrase into a regular expression (digit groups become wildcards, whitespace is flexible) and searches the named file;
  * it edits only when exactly one distinct old text matches and differs from the expected phrase; otherwise it reports the failure as MANUAL;
  * failures of any other kind (per-code breakdown sentences, stale generated files, the known-year list) are listed as MANUAL.
Dry run by default (prints each proposed replacement); --apply writes. Re-run the verifier afterwards; repeat until it passes or only MANUAL items remain.
Always read the diff (`git diff`) before committing: a replacement is only as right as the verifier's phrase, and a changed number in a dated historical document is
wrong even when the verifier asks for it (dated documents are deliberately not in the verifier's list).
Usage (from legal-last-mile-systematic-review/):  python3 code/analysis/fix_documented_counts.py [--apply] [--root PATH]
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

PAT = re.compile(r"^\s*FAIL: (?P<file>.+?): (?:expected to contain|A16 figure out of date, expected the phrase) '(?P<phrase>.+?)'(?: \(.*\))?\s*$")


def phrase_regex(phrase: str) -> re.Pattern:
    """Digits become wildcards, whitespace flexible: '1,161 studies extracted' matches '1,159 studies extracted'."""
    parts = re.split(r'(\d[\d,.]*\d|\d)', phrase)
    out = []
    for i, part in enumerate(parts):
        if i % 2:
            out.append(r'\d[\d,.]*')
        else:
            out.append(r'\s+'.join(re.escape(w) for w in part.split()) if part.strip() else (r'\s+' if part else ''))
            if part and part[0].isspace():
                out[-1] = r'\s*' + out[-1]
            if part and part[-1].isspace():
                out[-1] = out[-1] + r'\s*'
    return re.compile(''.join(out))


def propose(root: Path, verifier_output: str):
    """Return (edits, manual): edits are (path, old_text, new_text); manual are failure lines the script will not touch."""
    edits, manual = [], []
    for line in verifier_output.splitlines():
        if 'FAIL:' not in line:
            continue
        m = PAT.match(line)
        if not m:
            manual.append(line.strip()); continue
        rel, phrase = re.sub(r' \(repository root\)$', '', m['file']), m['phrase'].replace('\\n', '\n')
        path = (root / rel).resolve()
        if not path.exists():
            manual.append(line.strip() + '  [file not found]'); continue
        text = path.read_text(encoding='utf-8')
        found = {x.group(0) for x in phrase_regex(phrase).finditer(text)}
        found.discard(phrase)
        if len(found) == 1:
            edits.append((path, next(iter(found)), phrase))
        else:
            manual.append(line.strip() + ('  [no matching old text]' if not found else f'  [{len(found)} different old texts, e.g. ' + '; '.join(repr(x[:50]) for x in sorted(found)[:3]) + ']'))
    return edits, manual


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    a = ap.parse_args(argv)
    r = subprocess.run([sys.executable, str(a.root / 'code/analysis/verify_repository.py')], cwd=a.root, capture_output=True, text=True)
    edits, manual = propose(a.root, r.stdout + r.stderr)
    for path, old, new in edits:
        print(f"{path.relative_to(a.root.parent) if a.root.parent in path.parents else path}:\n   - {old!r}\n   + {new!r}")
    done = 0
    if a.apply:
        for path, old, new in edits:
            t = path.read_text(encoding='utf-8')
            if old in t:
                path.write_text(t.replace(old, new), encoding='utf-8'); done += 1
    print(f"\n{len(edits)} replacement(s) proposed{f', {done} applied' if a.apply else ' (dry run: nothing written; pass --apply)'}; {len(manual)} item(s) need a person:")
    for x in manual:
        print('  MANUAL:', x[:200])
    return 0


if __name__ == '__main__':
    sys.exit(main())
