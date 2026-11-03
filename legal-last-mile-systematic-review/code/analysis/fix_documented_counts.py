#!/usr/bin/env python3
"""Propose (and optionally apply) the number edits the verifier asks for after a real screening or extraction change.

After an A16 resolution, a criterion-3 exclusion or any dated data script, `verify_repository.py` reports hand-written figures that no longer match the data,
as lines like  "README.md: expected to contain '1,154 studies extracted' (extraction row)". The expected phrase is computed from the databases, so the fix is
mechanical: find the old phrase in that file (the same text with different numbers) and replace it. This script does exactly that and nothing cleverer:
  * it runs the verifier and parses every "expected to contain '...'" and "A16 figure out of date, expected the phrase '...'" failure;
  * FIRST it tries an exact mapping: the verifier can list every phrase it looks for (VERIFY_EMIT_EXPECTED=file), so the script runs it on the last commit
    (`--old-ref`, default HEAD, in a temporary git worktree) and on the working tree, pairs the phrases by file, label and position, and replaces the old
    phrase by the new one when the old one occurs exactly once in the file (this resolves cases where several different numbers would match the pattern);
  * otherwise it turns the expected phrase into a regular expression (digit groups become wildcards, whitespace is flexible) and searches the named file;
  * it edits only when exactly one distinct old text matches and differs from the expected phrase; otherwise it reports the failure as MANUAL;
  * failures of any other kind (per-code breakdown sentences, stale generated files, the known-year list) are listed as MANUAL.
Dry run by default (prints each proposed replacement); --apply writes. Re-run the verifier afterwards; repeat until it passes or only MANUAL items remain.
Always read the diff (`git diff`) before committing: a replacement is only as right as the verifier's phrase, and a changed number in a dated historical document is
wrong even when the verifier asks for it (dated documents are deliberately not in the verifier's list).
Usage (from legal-last-mile-systematic-review/):  python3 code/analysis/fix_documented_counts.py [--apply] [--root PATH]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
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


def _read(path: Path):
    """Return (text with LF endings, whether the file uses CRLF); the verifier reads files in text mode, so needles never contain a carriage return."""
    raw = path.read_bytes().decode('utf-8')
    return raw.replace('\r\n', '\n'), '\r\n' in raw


def _write(path: Path, text: str, crlf: bool):
    path.write_bytes((text.replace('\n', '\r\n') if crlf else text).encode('utf-8'))


def _keyed(expected):
    """[(file, phrase, label), ...] -> {(file, label, k): phrase} plus the number of phrases per (file, label)."""
    keyed, seen = {}, {}
    for rel, phrase, label in expected:
        k = seen.get((rel, label), 0)
        seen[(rel, label)] = k + 1
        keyed[(rel, label, k)] = phrase
    return keyed, seen


def exact_pairs(old_expected, new_expected):
    """{(file, new_phrase): old_phrase} for phrases whose (file, label, position) exists in both runs with the same number of phrases per (file, label)."""
    ok, oc = _keyed(old_expected)
    nk, nc = _keyed(new_expected)
    pairs = {}
    for (rel, label, k), new in nk.items():
        if oc.get((rel, label)) == nc.get((rel, label)) and (rel, label, k) in ok and ok[(rel, label, k)] != new:
            pairs[(rel, new)] = ok[(rel, label, k)]
    return pairs


def propose(root: Path, verifier_output: str, old_expected=None, new_expected=None):
    """Return (edits, manual): edits are (path, old_text, new_text); manual are failure lines the script will not touch.
    old_expected / new_expected (optional): the verifier's phrase lists at the old and the new state; when given, an old phrase that occurs exactly once is
    used in preference to the pattern search."""
    pairs = exact_pairs(old_expected, new_expected) if old_expected and new_expected else {}
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
        text, _ = _read(path)
        old = pairs.get((m['file'], phrase))
        if old is not None and text.count(old) == 1:
            edits.append((path, old, phrase)); continue
        found = {x.group(0) for x in phrase_regex(phrase).finditer(text)}
        found.discard(phrase)
        if len(found) == 1:
            edits.append((path, next(iter(found)), phrase))
        else:
            manual.append(line.strip() + ('  [no matching old text]' if not found else f'  [{len(found)} different old texts, e.g. ' + '; '.join(repr(x[:50]) for x in sorted(found)[:3]) + ']'))
    return edits, manual


def emit_expected(project: Path):
    """Run the verifier of `project` and return the phrase list it dumps (None if that verifier cannot)."""
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / 'expected.json'
        r = subprocess.run([sys.executable, str(project / 'code/analysis/verify_repository.py')], cwd=project, capture_output=True, text=True,
                           env={**os.environ, 'VERIFY_EMIT_EXPECTED': str(out)})
        if not out.exists():
            return None, r.stdout + r.stderr
        return [tuple(x) for x in json.loads(out.read_text(encoding='utf-8'))], r.stdout + r.stderr


def old_state_expected(root: Path, ref: str):
    """The phrase list of the project as committed at `ref`, from a temporary detached worktree; None when that is not possible."""
    try:
        top = Path(subprocess.run(['git', '-C', str(root), 'rev-parse', '--show-toplevel'], capture_output=True, text=True, check=True).stdout.strip())
        rel = root.resolve().relative_to(top.resolve())
        with tempfile.TemporaryDirectory() as d:
            wt = Path(d) / 'wt'
            subprocess.run(['git', '-C', str(top), 'worktree', 'add', '--detach', str(wt), ref], capture_output=True, text=True, check=True)
            try:
                return emit_expected(wt / rel)[0]
            finally:
                subprocess.run(['git', '-C', str(top), 'worktree', 'remove', '--force', str(wt)], capture_output=True, text=True)
    except (OSError, ValueError, subprocess.CalledProcessError):
        return None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    ap.add_argument('--old-ref', default='HEAD', help='git ref holding the state the documents were last consistent with (default HEAD)')
    ap.add_argument('--no-exact', action='store_true', help='skip the exact old-to-new phrase mapping and use only the pattern search')
    a = ap.parse_args(argv)
    new_expected, out = emit_expected(a.root)
    old_expected = None if a.no_exact or new_expected is None else old_state_expected(a.root, a.old_ref)
    print('exact old-to-new phrase mapping:', 'available' if old_expected else 'not available (pattern search only)')
    edits, manual = propose(a.root, out, old_expected, new_expected)
    for path, old, new in edits:
        print(f"{path.relative_to(a.root.parent) if a.root.parent in path.parents else path}:\n   - {old!r}\n   + {new!r}")
    done = 0
    if a.apply:
        for path, old, new in edits:
            t, crlf = _read(path)
            if old in t:
                _write(path, t.replace(old, new), crlf); done += 1
    print(f"\n{len(edits)} replacement(s) proposed{f', {done} applied' if a.apply else ' (dry run: nothing written; pass --apply)'}; {len(manual)} item(s) need a person:")
    for x in manual:
        print('  MANUAL:', x[:200])
    return 0


if __name__ == '__main__':
    sys.exit(main())
