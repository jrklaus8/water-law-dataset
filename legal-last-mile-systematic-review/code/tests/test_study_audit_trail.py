#!/usr/bin/env python3
"""00_admin/STUDY_AUDIT_TRAIL.csv is derived from the databases and must agree with them and with current_figures.py.

Checks: the files equal what the generator writes today; one row per extracted study, ids unique; the human/AI split of inclusion decisions, extraction depth, risk-of-bias tool counts and the synthesis
statuses equal the computed figures; no row claims a human check of extraction, risk of bias or direction coding (none exists). Run from legal-last-mile-systematic-review/."""
import csv
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/analysis'))
import current_figures as cf  # noqa: E402
import build_study_audit_trail as bsat  # noqa: E402


class TestAuditTrail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.F = cf.compute()
        with open(bsat.OUT_CSV, newline='', encoding='utf-8') as f:
            cls.rows = list(csv.DictReader(f))

    def test_files_are_what_the_generator_writes_today(self):
        csv_text, md_text = bsat.render()
        self.assertEqual(bsat.OUT_CSV.read_bytes().decode('utf-8'), csv_text)
        self.assertEqual(bsat.OUT_MD.read_text(encoding='utf-8'), md_text)

    def test_one_row_per_study(self):
        ids = [r['study_id'] for r in self.rows]
        self.assertEqual(len(ids), self.F['extraction_rows'])
        self.assertEqual(len(set(ids)), len(ids))
        self.assertEqual(list(self.rows[0].keys()), bsat.COLUMNS)

    def test_verification_split_matches_the_computed_figures(self):
        v = Counter(r['inclusion_verified_by'] for r in self.rows)
        self.assertEqual(v['human second reviewer'], self.F['reviewer_2_confirmed_includes'])
        self.assertEqual(v['principal investigator ruling'], self.F['human_adjudicated_includes'])
        self.assertEqual(v['none (AI only)'], self.F['full_text_include'] - self.F['reviewer_2_confirmed_includes'] - self.F['human_adjudicated_includes'])
        self.assertEqual(sum(r['borderline_include'] == 'yes' for r in self.rows), self.F['borderline_includes'])

    def test_extraction_and_appraisal_figures(self):
        self.assertEqual(sum(r['extraction_depth'] == 'abstract or metadata only' for r in self.rows), self.F['abstract_only_extractions'])
        self.assertEqual(dict(Counter(r['rob_tool'] for r in self.rows)), self.F['tools'])
        self.assertEqual({r['extracted_by'] for r in self.rows}, {'AI (Claude)'})
        self.assertEqual({r['ft_reviewer_1'] for r in self.rows}, {'AI (Claude)'})

    def test_no_row_claims_a_check_that_does_not_exist(self):
        self.assertEqual({r['second_extractor_checked'] for r in self.rows}, {'no'})
        self.assertEqual({r['rob_human_checked'] for r in self.rows}, {'no'})
        self.assertEqual(sum(r['direction_coding_confirmed_by_author'] == 'yes' for r in self.rows), self.F['swim_core_direction_ck_confirmed'])

    def test_synthesis_statuses(self):
        s = Counter(r['swim_inclusion_status'] for r in self.rows if r['synthesis_family'])
        self.assertEqual(s['human-verified inclusion'], self.F['swim_core_inclusion_human_verified'])
        self.assertEqual(s['AI-checked only'], self.F['swim_core_ai_checked_not_human'])
        self.assertEqual(sum(s.values()), self.F['swim_core_studies'])
        self.assertEqual(sum(int(r['effect_rows']) for r in self.rows), self.F['effect_size_rows'])


if __name__ == '__main__':
    unittest.main(verbosity=1)
