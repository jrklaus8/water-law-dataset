#!/usr/bin/env python3
"""The two-column direction coding of the family-assigned effect rows (39 after the author's A26 rulings, 37 after the A29 ruling and 31 after the A28 rulings, all of 2026-10-14) (05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv).

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
        self.assertEqual(Counter(fam.values()), Counter({'A': 13, 'B': 3, 'C': 15}))
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

    def test_a26_and_a29_rulings(self):
        """The author's A26 rulings: S358, S590 and S606 are reasoned non-fits; S1121 and S1143 left the review; S1038 carries state regulation as the exposure; S879 stays Mixed.
        The A29 ruling: S1140 and S1136 are reasoned non-fits too (no household water or sanitation access outcome), so no study in the three families is flagged as an indirect outcome."""
        for s in ('S358', 'S590', 'S606', 'S1140', 'S1136'):
            self.assertEqual(self.es[s]['synthesis_family'], '', s)
            self.assertIn('reasoned non-fit', self.es[s]['exclusion_from_pooling_reason'], s)
            self.assertNotIn(s, self.c)
        self.assertIn('A29 ruling 2026-10-14 by CK', self.es['S1140']['provenance_note'])
        self.assertIn('A29 ruling 2026-10-14 by CK', self.es['S1136']['provenance_note'])
        self.assertEqual(sum(1 for r in self.es.values() if r['synthesis_family'] == ''), 21)   # the reasoned non-fits, 19 before A29
        for s in ('S1121', 'S1143'):
            self.assertNotIn(s, self.es, s)
            self.assertNotIn(s, self.c)
        self.assertEqual({s for s, r in self.c.items() if r['outcome_directness_check'].startswith('checked')}, set())
        self.assertTrue(self.es['S1038']['exposure_definition'].startswith('Residential customers of a municipally-owned water utility subject to state public utility commission'))
        self.assertIn('local-only', self.es['S1038']['comparator_definition'])
        self.assertEqual((self.c['S879']['raw_coefficient_sign'], self.c['S879']['substantive_direction']), ('mixed', 'Mixed'))
        self.assertEqual((self.c['S471']['raw_coefficient_sign'], self.c['S471']['substantive_direction'], self.c['S471']['alternative_substantive_direction']), ('-', 'Favourable', 'Null'))

    def test_ai_scope_checks_cover_twenty_eight_studies_and_the_table_follows_them(self):
        """18 passed the AI's scope check and are AI-checked only (no human confirmation, no direction confirmation); the 10 the AI flagged carry the author's A28 ruling (4 kept, 6 excluded); the verification table carries exactly that."""
        chk = {r['study_id']: r for r in rows('05_analysis/effect_sizes/SWIM_AI_SCOPE_CHECKS_2026-10-14.csv')}
        self.assertEqual(len(chk), 28)
        passed = {s for s, r in chk.items() if r['ai_scope_check'] == 'passed'}
        flagged = {s for s, r in chk.items() if r['ai_scope_check'] == 'flagged'}
        self.assertEqual((len(passed), len(flagged)), (18, 10))
        self.assertTrue(all(chk[s]['a28_outcome'] == '' for s in passed))
        self.assertEqual({s for s in flagged if chk[s]['a28_outcome'].startswith('include')}, {'S920', 'S1102', 'S1146', 'S294'})
        self.assertEqual({s for s in flagged if chk[s]['a28_outcome'].startswith('exclude')}, {'S1020', 'S1042', 'S1057', 'S1144', 'S1163', 'S947'})
        self.assertTrue(all(r['ck_raw_sign_agrees (Y/N)'] == '' and r['ck_substantive_direction_agrees (Y/N)'] == '' for r in chk.values()))   # the author has not confirmed any direction coding
        tab = {r['study_id']: r for r in rows('05_analysis/effect_sizes/SWIM_CORE_VERIFICATION_TABLE_2026-10-14.csv')}
        self.assertEqual(set(chk) & set(self.c), passed | {'S920', 'S1102', 'S1146'})
        for s in passed:
            self.assertEqual((tab[s]['ck_raw_sign_agrees (Y/N)'], tab[s]['inclusion_decision_human_verified']), ('', 'N (AI-checked only)'), s)
        for s in ('S920', 'S1102', 'S1146'):
            self.assertEqual(tab[s]['inclusion_decision_human_verified'], 'Y (CK ruling)', s)
        self.assertEqual(tab['S366']['inclusion_decision_human_verified'][:1], 'Y')

    def test_a28_rulings(self):
        """The author's A28 rulings of 2026-10-14: six studies left the review (their effect rows are archived), the Family B row moved from S294 to S366, S920's mechanism is recorded."""
        for s in ('S1020', 'S1042', 'S1057', 'S1144', 'S1163', 'S947'):
            self.assertNotIn(s, self.es, s)
            self.assertNotIn(s, self.c, s)
        archived = {r['study_id'] for r in rows('11_archive/effect_sizes_removed_2026-10-13.csv')}
        self.assertTrue({'S1020', 'S1042', 'S1057', 'S1144', 'S1163', 'S947', 'S294'} <= archived)
        self.assertNotIn('S294', self.es)
        self.assertEqual((self.es['S366']['synthesis_family'], self.es['S366']['effect_estimate'][:4], self.es['S366']['lower_CI'], self.es['S366']['upper_CI']), ('B', '0.33', '0.22', '0.45'))
        self.assertEqual((self.c['S366']['raw_coefficient_sign'], self.c['S366']['substantive_direction']), ('+', 'Favourable'))
        self.assertIn('regulatory_model_ownership', self.es['S920']['provenance_note'])
        links = {r['link_id']: r for r in rows('03_extraction/extracted_data/linked_reports_2026-09-28.csv')}
        self.assertEqual(links['LR01']['in_effect_sizes'], 'second only')

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
