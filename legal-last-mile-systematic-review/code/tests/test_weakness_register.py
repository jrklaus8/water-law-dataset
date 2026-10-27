#!/usr/bin/env python3
"""The weakness register (00_admin/WEAKNESS_REGISTER.csv, WEAKNESSES.md) is generated from a hand-written source; this checks it cannot rot.

Checks: the outputs equal what the generator writes today; ids are unique and well-formed; every cell is filled and every {token} was resolved; severities are valid; every evidence path exists in
the repository (so a cited file cannot be renamed or deleted without the test failing); and the page says that the severity ratings are the AI's. Run from legal-last-mile-systematic-review/."""
import csv
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/analysis'))
import build_weakness_register as bwr  # noqa: E402


class TestWeaknessRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(bwr.OUT_CSV, newline='', encoding='utf-8') as f:
            cls.rows = list(csv.DictReader(f))

    def test_files_are_what_the_generator_writes_today(self):
        csv_text, md_text = bwr.render()
        self.assertEqual(bwr.OUT_CSV.read_bytes().decode('utf-8'), csv_text)
        self.assertEqual(bwr.OUT_MD.read_text(encoding='utf-8'), md_text)

    def test_ids_and_fields(self):
        ids = [r['id'] for r in self.rows]
        self.assertEqual(len(ids), len(set(ids)))
        for r in self.rows:
            self.assertRegex(r['id'], r'^W\d\d$')
            self.assertIn(r['severity_ai_judgment'], ('high', 'medium', 'low'))
            for k, v in r.items():
                self.assertTrue(v.strip(), (r['id'], k))
                self.assertNotRegex(v, r'\{\w+\}', (r['id'], k))

    def test_every_evidence_path_exists(self):
        missing = []
        for r in self.rows:
            for p in r['evidence'].split(';'):
                p = p.strip()
                if p and not (ROOT / p).exists():
                    missing.append((r['id'], p))
        self.assertEqual(missing, [])

    def test_page_says_the_ratings_are_the_ais(self):
        text = bwr.OUT_MD.read_text(encoding='utf-8')
        for needle in ("the AI's judgment", 'has not yet rated it', 'Where I would attack first', 'How to challenge or extend it'):
            self.assertIn(needle, text, needle)

    def test_covers_every_stage_of_the_review(self):
        stages = {r['stage'] for r in self.rows}
        for needed in ('Search', 'Title/abstract screening', 'Full-text screening', 'Extraction', 'Risk of bias', 'Synthesis', 'AI use', 'Governance', 'Verification'):
            self.assertIn(needed, stages, needed)


if __name__ == '__main__':
    unittest.main(verbosity=1)
