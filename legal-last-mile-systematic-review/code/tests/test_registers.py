#!/usr/bin/env python3
"""The deviations and errors-found registers are hand-maintained data files; this checks they stay well formed and that the readable view matches them.

Checks: unique ids; ISO dates; allowed values for kind-independent fields (after-seeing-results, status); every cited file exists; the rendered page equals the generator's output; and the entries the
project most needs to keep (the criterion-2 narrowing, the A26/A28 rulings, the retrospective registration, the 39-batch corruption) are present. Run from legal-last-mile-systematic-review/."""
import csv
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/analysis'))
import build_deviation_error_registers as bder  # noqa: E402

ISO = re.compile(r'^\d{4}-\d{2}-\d{2}$')
PATH = re.compile(r'[\w./-]+\.(?:md|csv|py|json|html|yml|cff)')


def paths(cell):
    for part in re.split(r'[;]', cell):
        m = PATH.search(part)
        if m:
            yield m.group(0)


class TestRegisters(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dev, cls.err = bder.read(bder.DEV), bder.read(bder.ERR)

    def test_view_matches_the_registers(self):
        self.assertEqual(bder.OUT.read_text(encoding='utf-8'), bder.render())

    def test_ids_dates_and_values(self):
        for rows, key in ((self.dev, 'date_recorded'), (self.err, 'date_found')):
            ids = [r['id'] for r in rows]
            self.assertEqual(len(ids), len(set(ids)))
            for r in rows:
                self.assertRegex(r[key], ISO, r['id'])
                self.assertTrue(all(v.strip() for v in r.values()), r['id'])
        for r in self.dev:
            self.assertIn(r['decided_after_seeing_results'], ('yes', 'no', 'partly', 'not applicable'), r['id'])
        for r in self.err:
            self.assertRegex(r['status'], r'^(fixed|disclosed|mitigated|open)', r['id'])

    def test_cited_files_exist(self):
        missing = []
        for rows, col in ((self.dev, 'documented_in'), (self.err, 'documented_in')):
            for r in rows:
                for p in paths(r[col]):
                    if not (ROOT / p).exists() and not (ROOT.parent / p).exists():
                        missing.append((r['id'], p))
        self.assertEqual(missing, [])

    def test_key_entries_are_present(self):
        text = ' '.join(r['deviation'] for r in self.dev)
        for needle in ('Criterion 2 read narrowly', 'A26 rulings', 'A28', 'Protocol not registered', 'Search closed'):
            self.assertIn(needle, text, needle)
        self.assertIn('39 parallel batches', ' '.join(r['error'] for r in self.err))


if __name__ == '__main__':
    unittest.main(verbosity=1)
