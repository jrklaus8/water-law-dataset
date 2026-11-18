#!/usr/bin/env python3
"""Tests for code/screening/bulk_import_full_text_results.py: all-or-nothing validation, decided records and unknown ids are skipped and reported, only the columns present
in the results file are touched, dry runs write nothing, and padded enum values are stored clean (a trailing space passed validation but was once written as typed,
leaving ' retrieved' in the database). Works on temp copies of the real database.
Run from legal-last-mile-systematic-review/:  python3 code/tests/test_bulk_import_full_text.py"""
import csv
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'code/screening/bulk_import_full_text_results.py'
REAL = ROOT / '02_screening/full_text/full_text_screening_database.csv'
csv.field_size_limit(sys.maxsize)


class TestBulkImport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(REAL, encoding='utf-8', newline='') as f:
            rows = list(csv.DictReader(f))
        cls.undecided = [r['record_id'] for r in rows if not r['final_decision'].strip()][:3]
        cls.decided = next(r['record_id'] for r in rows if r['final_decision'].strip())
        assert len(cls.undecided) == 3

    def setUp(self):
        self._t = tempfile.TemporaryDirectory(); self.addCleanup(self._t.cleanup)
        self.d = Path(self._t.name)
        self.db = self.d / 'ft.csv'; shutil.copy(REAL, self.db)

    def results(self, rows, fields=('record_id', 'full_text_status', 'full_text_location', 'notes')):
        p = self.d / 'results.csv'
        with open(p, 'w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(fields)); w.writeheader(); w.writerows(rows)
        return p

    def run_import(self, results, *extra):
        return subprocess.run([sys.executable, str(SCRIPT), '--full-text-db', str(self.db), '--results', str(results), *extra], capture_output=True, text=True)

    def row(self, rid):
        with open(self.db, encoding='utf-8', newline='') as f:
            return next(r for r in csv.DictReader(f) if r['record_id'] == rid)

    def test_applies_only_present_columns_and_skips_decided_and_unknown(self):
        a = self.undecided[0]; before = self.row(a)
        res = self.results([dict(record_id=a, full_text_status='retrieved', full_text_location='x.pdf', notes='n1'),
                            dict(record_id=self.decided, full_text_status='retrieved', full_text_location='y', notes='n2'),
                            dict(record_id='RNOPE', full_text_status='retrieved', full_text_location='z', notes='n3')])
        r = self.run_import(res); self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn('1 to apply', r.stdout); self.assertIn('RNOPE', r.stdout); self.assertIn(self.decided, r.stdout)
        after = self.row(a)
        self.assertEqual((after['full_text_status'], after['full_text_location'], after['notes']), ('retrieved', 'x.pdf', 'n1'))
        for k in before:
            if k not in ('full_text_status', 'full_text_location', 'notes'):
                self.assertEqual(after[k], before[k], k)
        self.assertNotEqual(self.row(self.decided)['notes'], 'n2')

    def test_one_bad_row_rejects_the_whole_batch(self):
        before = self.db.read_bytes()
        res = self.results([dict(record_id=self.undecided[0], full_text_status='retrieved', full_text_location='', notes='ok'),
                            dict(record_id=self.undecided[1], full_text_status='got it', full_text_location='', notes='typo')])
        r = self.run_import(res); self.assertEqual(r.returncode, 1); self.assertIn('REJECTING ENTIRE IMPORT', r.stdout)
        self.assertEqual(self.db.read_bytes(), before)

    def test_dry_run_writes_nothing(self):
        before = self.db.read_bytes()
        r = self.run_import(self.results([dict(record_id=self.undecided[0], full_text_status='retrieved', full_text_location='', notes='x')]), '--dry-run')
        self.assertEqual(r.returncode, 0); self.assertIn('dry-run', r.stdout); self.assertEqual(self.db.read_bytes(), before)

    def test_padded_enum_values_are_stored_clean(self):
        a = self.undecided[2]
        res = self.results([dict(record_id=a, full_text_status=' retrieved ', full_text_location='', notes='')])
        r = self.run_import(res); self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.row(a)['full_text_status'], 'retrieved')

    def test_blank_record_id_is_an_error(self):
        r = self.run_import(self.results([dict(record_id='', full_text_status='retrieved', full_text_location='', notes='')]))
        self.assertEqual(r.returncode, 1); self.assertIn('blank record_id', r.stdout)


if __name__ == '__main__':
    unittest.main(verbosity=1)
