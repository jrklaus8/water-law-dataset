#!/usr/bin/env python3
"""Tests for code/analysis/fix_documented_counts.py: the phrase-to-regex step and the propose() rules (unique match edits, ambiguous or missing matches stay manual,
the '(repository root)' suffix of a verifier path is understood). Uses temp files and synthetic verifier output; touches no real document.
Run from legal-last-mile-systematic-review/:  python3 code/tests/test_fix_documented_counts.py"""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/analysis'))
import fix_documented_counts as fx  # noqa: E402


class TestRegex(unittest.TestCase):
    def test_digits_are_wildcards_and_whitespace_flexible(self):
        rx = fx.phrase_regex('1,161 studies extracted')
        self.assertTrue(rx.search('now 1,159 studies extracted here'))
        self.assertTrue(rx.search('1,159 studies\nextracted'))
        self.assertFalse(rx.search('1,159 studies indexed'))
        self.assertTrue(fx.phrase_regex('**1,154 include / 1,122 exclude**').search('**1,159 include / 1,117 exclude**'))


class TestPropose(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory(); self.addCleanup(self._t.cleanup)
        self.root = Path(self._t.name) / 'proj'; self.root.mkdir()
        (self.root / 'doc.md').write_text('We extracted 1,159 studies extracted in all; E01 is 496.\nOne more: 10 of 20 sampled.\nAlso 11 of 21 sampled.\n', encoding='utf-8')
        (Path(self._t.name) / 'README.md').write_text('Root says 1,159 studies extracted.\n', encoding='utf-8')

    def out(self, *lines):
        return '\n'.join('  FAIL: ' + x for x in lines)

    def test_unique_match_becomes_an_edit(self):
        edits, manual = fx.propose(self.root, self.out("doc.md: expected to contain '1,161 studies extracted' (extraction row)"))
        self.assertEqual([(e[1], e[2]) for e in edits], [('1,159 studies extracted', '1,161 studies extracted')]); self.assertEqual(manual, [])

    def test_repository_root_suffix(self):
        edits, manual = fx.propose(self.root, self.out("../README.md (repository root): expected to contain '1,161 studies extracted'"))
        self.assertEqual(len(edits), 1); self.assertEqual(manual, [])

    def test_ambiguous_and_missing_stay_manual(self):
        edits, manual = fx.propose(self.root, self.out("doc.md: expected to contain '12 of 22 sampled'", "doc.md: expected to contain 'nothing like this 5'", "README exclusion breakdown: E01 is 496, data says 493"))
        self.assertEqual(edits, []); self.assertEqual(len(manual), 3)
        self.assertIn('2 different old texts', manual[0]); self.assertIn('no matching old text', manual[1])

    def test_a16_phrase_failures_are_handled(self):
        (self.root / 'doc.md').write_text('about 468 implied further includes\n', encoding='utf-8')
        edits, _ = fx.propose(self.root, self.out("doc.md: A16 figure out of date, expected the phrase 'about 466 implied further includes' (computed by x.py)"))
        self.assertEqual(edits[0][2], 'about 466 implied further includes')


if __name__ == '__main__':
    unittest.main(verbosity=1)
