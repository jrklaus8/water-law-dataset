#!/usr/bin/env python3
"""Unit tests for small pure helpers added in the 2026-10-04 session: the A16 Wilson interval and projection and the design-label classifier.
Run from legal-last-mile-systematic-review/:  python3 code/tests/test_analysis_helpers.py"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/analysis'))
import build_a16_adjudication_sheet as baa  # noqa: E402
import propose_design_vocabulary as pdv  # noqa: E402


class TestWilson(unittest.TestCase):
    def test_reference_values(self):
        for (k, n), (lo, hi) in {(3, 18): (0.0584, 0.3922), (19, 37): (0.3589, 0.6655), (6, 9): (0.3542, 0.8794), (0, 10): (0.0, 0.2775), (1, 1): (0.2065, 1.0)}.items():
            a, b = baa._wilson(k, n)
            self.assertAlmostEqual(a, lo, places=3); self.assertAlmostEqual(b, hi, places=3)

    def test_bounds_and_empty(self):
        for k, n in [(0, 1), (0, 50), (50, 50), (1, 2)]:
            lo, hi = baa._wilson(k, n)
            self.assertTrue(0.0 <= lo <= k / n <= hi <= 1.0, (k, n, lo, hi))
        self.assertEqual(baa._wilson(0, 0), (0.0, 1.0))

    def test_projection_ordering_on_real_data(self):
        total, narrow, literal = baa.implied_total()
        self.assertLessEqual(narrow, literal); self.assertLessEqual(literal, total + 1)  # narrow reading <= literal reading <= the models' rate (up to rounding)
        self.assertGreater(narrow, 0)


class TestDesignClassifier(unittest.TestCase):
    def test_cases(self):
        c = lambda s: pdv.classify(s)[0]
        self.assertEqual(c('systematic literature review (185 articles)'), 'systematic_review_secondary')
        self.assertEqual(c('comparative natural-experiment case study'), 'quasi_experimental')
        self.assertEqual(c('legal-doctrinal analysis'), 'doctrinal')
        self.assertEqual(c('institutional/legal case study'), 'qualitative')               # a bare 'legal' is not enough
        self.assertEqual(c('qualitative case study (institutional theory + legal analysis)'), 'qualitative')
        self.assertEqual(c('historical econometric case study'), 'mixed_methods')           # quantitative and qualitative cues
        self.assertEqual(c('econometric tariff-differential analysis of municipal water pricing'), 'observational')
        self.assertEqual(c('ethnographic case study'), 'qualitative')
        self.assertEqual(c('critical policy-analysis essay'), 'unmapped_needs_review')

    def test_build_only_covers_non_enum_labels_and_is_deterministic(self):
        rows = pdv.build()
        self.assertTrue(all(r['free_text_label'] not in pdv.ENUM for r in rows))
        self.assertTrue(all(r['proposed_class'] in pdv.ENUM | {'unmapped_needs_review'} for r in rows))
        self.assertEqual(rows, pdv.build())


if __name__ == '__main__':
    unittest.main(verbosity=1)
