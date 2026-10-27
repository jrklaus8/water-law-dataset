#!/usr/bin/env python3
"""00_admin/AI_USE_LEDGER.* is derived from the reviewer and researcher labels in the databases and must agree with current_figures.py.

Checks: the files equal what the generator writes today; every archived instruction file it cites exists; the AI first-decision rows add up to the decided full-text records and their
human-checked counts add up to the computed human-verified total; the second-model and human rows match the computed figures; and the ledger states what is not archived.
Run from legal-last-mile-systematic-review/."""
import csv
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/analysis'))
import current_figures as cf  # noqa: E402
import build_ai_use_ledger as bal  # noqa: E402


class TestAiUseLedger(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.F = cf.compute()
        with open(bal.OUT_CSV, newline='', encoding='utf-8') as f:
            cls.rows = list(csv.DictReader(f))

    def test_files_are_what_the_generator_writes_today(self):
        csv_text, md_text = bal.render()
        self.assertEqual(bal.OUT_CSV.read_bytes().decode('utf-8'), csv_text)
        self.assertEqual(bal.OUT_MD.read_text(encoding='utf-8'), md_text)

    def test_every_cited_instruction_file_exists(self):
        for path, _ in bal.ARCHIVED:
            self.assertTrue((ROOT / path).exists(), path)

    def test_full_text_first_decisions_add_up(self):
        first = [r for r in self.rows if r['stage'] == 'Full-text screening' and r['activity'].startswith('First decision')]
        self.assertEqual(sum(int(r['units']) for r in first), self.F['full_text_decided'])
        self.assertEqual(sum(int(r['human_checked']) for r in first), self.F['human_verified_rows'])

    def test_second_reviewer_rows(self):
        second = [int(r['units']) for r in self.rows if r['activity'] == 'Independent second review']
        self.assertEqual(sum(second), self.F['reviewer_2_confirmed_includes'] + self.F['reviewer_2_second_model_rows'])
        pi = next(r for r in self.rows if r['actor'].startswith('principal investigator'))
        self.assertEqual(int(pi['units']), self.F['human_adjudicated_rows'])

    def test_title_abstract_and_extraction_counts(self):
        ta = next(r for r in self.rows if r['activity'].startswith('First-pass'))
        self.assertEqual(int(ta['units']), sum(1 for r in cf.read('ta') if r['reviewer_1']))
        ex = next(r for r in self.rows if r['stage'].startswith('Data extraction'))
        self.assertEqual(int(ex['units']), self.F['extraction_rows'])
        self.assertEqual(ex['human_checked'], '0')

    def test_states_what_is_not_archived(self):
        text = bal.OUT_MD.read_text(encoding='utf-8')
        for needle in ('What is NOT archived', 'exact model version', 'Sampling settings and seeds', 'not deterministic', 'No second AI model repeated the whole first pass'):
            self.assertIn(needle, text, needle)


if __name__ == '__main__':
    unittest.main(verbosity=1)
