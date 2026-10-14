#!/usr/bin/env python3
"""The two-column direction coding of the 44 family-assigned effect rows (05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv).

Checks, independently of the script that writes the file: (1) it covers exactly the studies that effect_sizes.csv assigns to Families A, B and C; (2) the substantive direction follows from the raw sign, the outcome polarity and the exposure
orientation by one rule (the product of three signs; null and mixed pass through); (3) the cases the author named on 2026-10-14 come out as instructed; (4) the three family documents and the verification table carry the same two codings.
Run from legal-last-mile-systematic-review/:  python3 code/tests/test_swim_direction_coding.py"""
import csv
import re
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
csv.field_size_limit(sys.maxsize)
HB, AR = 'higher = better', 'as reported'


def rows(rel):
    with open(ROOT / rel, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


class TestDirectionCoding(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = {r['study_id']: r for r in rows('05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv')}
        cls.es = {r['study_id']: r for r in rows('05_analysis/effect_sizes/effect_sizes.csv')}

    def test_covers_exactly_the_family_assigned_studies(self):
        fam = {s: r['synthesis_family'] for s, r in self.es.items() if r['synthesis_family'] in ('A', 'B', 'C')}
        self.assertEqual(set(self.c), set(fam))
        self.assertEqual(Counter(fam.values()), Counter({'A': 18, 'B': 6, 'C': 20}))
        self.assertEqual({s: r['family'] for s, r in self.c.items()}, fam)

    def test_substantive_direction_follows_from_the_three_coded_fields(self):
        for s, r in self.c.items():
            raw = r['raw_coefficient_sign']
            self.assertIn(raw, ('+', '-', 'null', 'mixed'), s)
            if raw in ('null', 'mixed'):
                expect = raw.capitalize()
            else:
                sign = (1 if raw == '+' else -1) * (1 if r['outcome_polarity'] == HB else -1) * (1 if r['exposure_orientation'] == AR else -1)
                expect = 'Favourable' if sign > 0 else 'Unfavourable'
            self.assertEqual(r['substantive_direction'], expect, s)

    def test_the_cases_named_by_the_author(self):
        c = self.c
        self.assertEqual((c['S104']['raw_coefficient_sign'], c['S104']['substantive_direction']), ('+', 'Unfavourable'))    # home ownership, more interruptions (OR 1.31)
        self.assertEqual((c['S404']['raw_coefficient_sign'], c['S404']['substantive_direction']), ('-', 'Favourable'))      # WRUA membership, less water poverty
        for s in ('S084', 'S142'):                                                                                           # deprived status with a negative coefficient: concordant with recognition
            self.assertEqual((c[s]['raw_coefficient_sign'], c[s]['substantive_direction']), ('-', 'Favourable'), s)
        self.assertEqual(c['S526']['raw_coefficient_sign'], '-')                                                             # progressivity ratio down
        self.assertEqual(c['S539']['raw_coefficient_sign'], '+')                                                             # bill and burden up
        self.assertEqual(c['S749']['raw_coefficient_sign'], '+')                                                             # tariff up
        self.assertEqual({c[s]['substantive_direction'] for s in ('S526', 'S539', 'S749')}, {'Unfavourable'})               # the same substantive direction despite opposite raw signs
        self.assertEqual((c['S471']['raw_coefficient_sign'], c['S471']['alternative_substantive_direction']), ('-', 'Null'))  # unadjusted sign -, fully adjusted direction Null

    def test_the_five_indirect_outcome_studies_are_the_ones_flagged(self):
        flagged = {s for s, r in self.c.items() if r['outcome_directness_check'].startswith('checked')}
        self.assertEqual(flagged, {'S358', 'S1121', 'S1140', 'S590', 'S1136'})
        self.assertTrue(all(self.c[s]['ai_recommendation_for_author'] for s in flagged))

    def test_family_documents_and_table_carry_the_same_codings(self):
        sys.path.insert(0, str(ROOT / 'code/analysis'))
        import sensitivity_analysis as sa
        word = {'+': 'positive', '-': 'negative', 'null': 'null', 'mixed': 'mixed'}
        for f in 'ABC':
            raw, sub = sa.parse_signs(f), sa.parse_substantive(f)
            fam_c = {s: r for s, r in self.c.items() if r['family'] == f}
            self.assertEqual(raw, {s: word[r['raw_coefficient_sign']] for s, r in fam_c.items()}, f)
            self.assertEqual(sub, {s: r['substantive_direction'].lower() for s, r in fam_c.items()}, f)
        tab = {r['study_id']: r for r in rows('05_analysis/effect_sizes/SWIM_CORE_VERIFICATION_TABLE_2026-10-14.csv')}
        self.assertEqual(set(tab), set(self.c))
        for s, r in tab.items():
            self.assertEqual((r['raw_coefficient_sign'], r['substantive_direction']), (self.c[s]['raw_coefficient_sign'], self.c[s]['substantive_direction']), s)


if __name__ == '__main__':
    unittest.main(verbosity=1)
