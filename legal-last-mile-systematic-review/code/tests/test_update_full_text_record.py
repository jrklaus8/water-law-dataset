#!/usr/bin/env python3
"""Tests for code/screening/update_full_text_record.py, the one-record command-line editor of the full-text screening database: a no-op update leaves the real file
byte-identical (CRLF kept), a change touches only the named fields, an unknown record or an invalid code writes nothing. Works on temp copies.
Run from legal-last-mile-systematic-review/:  python3 code/tests/test_update_full_text_record.py"""
import csv
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'code/screening/update_full_text_record.py'
REAL = ROOT / '02_screening/full_text/full_text_screening_database.csv'
csv.field_size_limit(sys.maxsize)


def run(db, *args):
    return subprocess.run([sys.executable, str(SCRIPT), '--full-text-db', str(db), *args], capture_output=True, text=True)


class TestUpdate(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory(); self.addCleanup(self._t.cleanup)
        self.db = Path(self._t.name) / 'ft.csv'
        shutil.copy(REAL, self.db)
        with open(REAL, encoding='utf-8', newline='') as f:
            self.first = next(csv.DictReader(f))

    def rows(self):
        with open(self.db, encoding='utf-8', newline='') as f:
            return list(csv.DictReader(f))

    def test_noop_update_is_byte_identical(self):
        r = run(self.db, '--record-id', self.first['record_id'], '--notes', self.first['notes'])
        self.assertEqual(r.returncode, 0); self.assertIn('notes', r.stdout)
        self.assertEqual(self.db.read_bytes(), REAL.read_bytes())

    def test_only_named_fields_change(self):
        rid = self.first['record_id']
        r = run(self.db, '--record-id', rid, '--notes', 'checked by test', '--location', 'somewhere')
        self.assertEqual(r.returncode, 0)
        new = {x['record_id']: x for x in self.rows()}[rid]
        for k, v in self.first.items():
            if k in ('notes', 'full_text_location'):
                continue
            self.assertEqual(new[k], v, k)
        self.assertEqual((new['notes'], new['full_text_location']), ('checked by test', 'somewhere'))

    def test_unknown_record_and_no_fields_write_nothing(self):
        before = self.db.read_bytes()
        r = run(self.db, '--record-id', 'RNOPE', '--notes', 'x'); self.assertEqual(r.returncode, 1); self.assertIn('not found', r.stdout)
        r = run(self.db, '--record-id', self.first['record_id']); self.assertEqual(r.returncode, 0); self.assertIn('nothing written', r.stdout)
        self.assertEqual(self.db.read_bytes(), before)

    def test_invalid_code_is_refused_by_the_parser(self):
        before = self.db.read_bytes()
        r = run(self.db, '--record-id', self.first['record_id'], '--exclusion-reason', 'E13')
        self.assertEqual(r.returncode, 2); self.assertEqual(self.db.read_bytes(), before)

    def test_exclude_without_a_code_warns(self):
        rid = next(x['record_id'] for x in self.rows() if not x['exclusion_reason'])
        r = run(self.db, '--record-id', rid, '--decision', 'exclude')
        self.assertIn('WARNING', r.stdout)


if __name__ == '__main__':
    unittest.main(verbosity=1)
