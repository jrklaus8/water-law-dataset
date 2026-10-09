#!/usr/bin/env python3
"""Independent re-derivation of the headline figures straight from the CSVs, compared with 00_admin/current_figures.json.

current_figures.py feeds the verifier, the README checks and every generated text, so a bug in it would be self-confirming. This test recomputes the headline
numbers with deliberately separate, simple code (plain csv, its own tool-name normalisation) and fails if they disagree. Run from legal-last-mile-systematic-review/:
python3 code/tests/test_current_figures_independent.py"""
import csv
import json
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
csv.field_size_limit(sys.maxsize)


def rows(rel):
    with open(ROOT / rel, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def tool(raw):
    """Prefix-based normalisation of the risk_of_bias_tool text (free text that often goes on to explain a reclassification, so a substring match would misfile rows)."""
    t = raw.strip().lower()
    for prefix, name in (('rob 2', 'RoB 2'), ('robins-i', 'ROBINS-I'), ('amstar', 'AMSTAR 2'), ('jbi', 'JBI Cross-Sectional'), ('a jbi', 'JBI Cross-Sectional'), ('mmat', 'MMAT'),
                         ('mixed methods appraisal', 'MMAT'), ('casp', 'CASP Qualitative'), ('legal institutional', 'Legal Framework'), ('none', 'NONE')):
        if t.startswith(prefix):
            return name
    return 'other'


class TestHeadlineFigures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.F = json.loads((ROOT / '00_admin/current_figures.json').read_text(encoding='utf-8'))
        cls.ft = rows('02_screening/full_text/full_text_screening_database.csv')
        cls.ed = rows('03_extraction/extracted_data/extraction_database.csv')
        cls.es = rows('05_analysis/effect_sizes/effect_sizes.csv')
        cls.el = rows('02_screening/exclusion_log/exclusion_log.csv')
        cls.ta = rows('02_screening/title_abstract/screening_database.csv')

    def test_screening_counts(self):
        F, ft = self.F, self.ft
        self.assertEqual(F['full_text_records'], len(ft))
        self.assertEqual(F['full_text_include'], sum(r['final_decision'] == 'include' for r in ft))
        self.assertEqual(F['full_text_exclude'], sum(r['final_decision'] == 'exclude' for r in ft))
        self.assertEqual(F['full_text_undecided'], sum(r['final_decision'] not in ('include', 'exclude') for r in ft))
        self.assertEqual(F['decided_blank_reviewer_1'], sum(1 for r in ft if r['final_decision'] in ('include', 'exclude') and not r['reviewer_1'].strip()))
        self.assertEqual(F['exclusion_log_rows'], len(self.el))
        self.assertEqual(F['exclusion_by_code'], dict(Counter(r['exclusion_code'] for r in self.el)))
        self.assertEqual(F['title_abstract_include'], sum(r['final_decision'] == 'include' for r in self.ta))
        self.assertEqual(F['title_abstract_exclude'], sum(r['final_decision'] == 'exclude' for r in self.ta))

    def test_extraction_counts(self):
        F, ed = self.F, self.ed
        self.assertEqual(F['extraction_rows'], len(ed)); self.assertEqual(F['extraction_rows'], F['full_text_include'])
        tools = Counter(tool(r['risk_of_bias_tool']) for r in ed)
        self.assertNotIn('other', tools)
        self.assertEqual(F['tools'], dict(tools))
        self.assertEqual(F['causal_capable_designs'], tools['RoB 2'] + tools['ROBINS-I'])
        self.assertEqual(F['country_blank_studies'], sum(1 for r in ed if not r['country'].strip()))

    def test_effect_size_counts(self):
        F, es = self.F, self.es
        self.assertEqual(F['effect_size_rows'], len(es))
        fam = Counter(r['synthesis_family'] or '(none: reasoned non-fit)' for r in es)
        self.assertEqual({k: v for k, v in F['effect_size_by_family'].items() if v}, dict(fam))
        self.assertEqual(F['effect_size_rows_pooled'], sum(r['included_in_pooled_estimate'].strip().upper() == 'TRUE' for r in es))
        self.assertEqual(len({r['study_id'] for r in es}), len(es))  # one prespecified effect per study


if __name__ == '__main__':
    unittest.main(verbosity=1)
