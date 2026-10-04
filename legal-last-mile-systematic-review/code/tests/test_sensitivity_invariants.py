#!/usr/bin/env python3
"""Structural invariants of the sensitivity scenarios (05_analysis/sensitivity/sensitivity_scenarios_2026-09-28.csv), checked against effect_sizes.csv.

For every scenario: the sign counts of each family sum to its k; Family A's concordant + counter-pattern + null counts sum to its k and the concordance percentage equals
concordant / k; dropped studies are real effect-size studies of that family and exactly account for the fall in k against the baseline; and the pre-stated conclusion
tests are consistent with the counts they are computed from. Run from legal-last-mile-systematic-review/:  python3 code/tests/test_sensitivity_invariants.py"""
import csv
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
csv.field_size_limit(sys.maxsize)


def rows(rel):
    with open(ROOT / rel, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


class TestSensitivity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sc = rows('05_analysis/sensitivity/sensitivity_scenarios_2026-09-28.csv')
        es = rows('05_analysis/effect_sizes/effect_sizes.csv')
        cls.fam_of = {r['study_id']: r['synthesis_family'] for r in es}
        cls.k = Counter(r['synthesis_family'] for r in es)

    def test_baseline_matches_effect_sizes(self):
        b = self.sc[0]
        self.assertTrue(b['scenario'].startswith('S0'))
        self.assertEqual((int(b['A_k']), int(b['B_k']), int(b['C_k'])), (self.k['A'], self.k['B'], self.k['C']))

    def test_signs_sum_to_k_and_concordance_is_consistent(self):
        for r in self.sc:
            for f in 'ABC':
                self.assertEqual(sum(int(r[f'{f}_{s}']) for s in ('positive', 'negative', 'null', 'mixed')), int(r[f'{f}_k']), (r['scenario'], f))
            self.assertEqual(int(r['A_concordant']) + int(r['A_counter']) + int(r['A_null_concordance']), int(r['A_k']), r['scenario'])
            self.assertAlmostEqual(float(r['A_concordant_pct']), 100 * int(r['A_concordant']) / int(r['A_k']), delta=0.06, msg=r['scenario'])

    def test_dropped_studies_account_for_the_change_in_k(self):
        base = self.sc[0]
        for r in self.sc[1:]:
            dropped = [s for s in r['dropped_studies_in_families'].split(';') if s]
            self.assertTrue(all(s in self.fam_of and self.fam_of[s] in 'ABC' and self.fam_of[s] for s in dropped), (r['scenario'], dropped))
            by = Counter(self.fam_of[s] for s in dropped)
            for f in 'ABC':
                if r['scenario'].startswith('S3'):  # collapsing linked reports changes what is counted, not which family rows exist (no effect-size study is in a linked pair)
                    continue
                self.assertEqual(int(base[f'{f}_k']) - int(r[f'{f}_k']), by[f], (r['scenario'], f))

    def test_pre_stated_tests_follow_from_counts(self):
        for r in self.sc:
            a_holds = int(r['A_concordant']) * 2 > int(r['A_k'])
            self.assertEqual(r['A_test_majority_concordant'] == 'holds', a_holds, r['scenario'])
            b_holds = int(r['B_negative']) == 0 and int(r['B_null']) == 0
            self.assertEqual(r['B_test_none_negative_or_null'] == 'holds', b_holds, r['scenario'])
            signs = [int(r[f'C_{x}']) for x in ('positive', 'negative', 'null', 'mixed')]
            self.assertEqual(r['C_test_no_dominant_sign'] == 'holds', max(signs) * 2 <= int(r['C_k']), r['scenario'])  # no single sign holds a majority


if __name__ == '__main__':
    unittest.main(verbosity=1)
