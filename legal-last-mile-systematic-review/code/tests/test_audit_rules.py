#!/usr/bin/env python3
"""Pins the behaviour of the rule-based audit scripts on small synthetic inputs, so a later edit to a regular expression cannot silently change which studies the
researcher is told to look at: the design-class proposal (A20), the thin-basis exclusion phrase match (A19) and the criterion-3 cues (A22). The scripts' outputs on the
real data are covered by the verifier's freshness checks; these tests cover the rules themselves. Run from legal-last-mile-systematic-review/:
python3 code/tests/test_audit_rules.py"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/analysis'))
import audit_effect_size_families as aef  # noqa: E402
import audit_exclusion_basis as aeb  # noqa: E402
import audit_includes_criterion3 as aic  # noqa: E402
import propose_design_vocabulary as pdv  # noqa: E402


class TestDesignClass(unittest.TestCase):
    def cls(self, label):
        return pdv.classify(label)[0]

    def test_precedence_and_cues(self):
        cases = {
            'Systematic review of tenure studies': 'systematic_review_secondary',
            'Narrative literature review': 'systematic_review_secondary',
            'Natural experiment using difference-in-differences': 'quasi_experimental',
            'Doctrinal analysis of statutory text': 'doctrinal',
            'Ethnographic fieldwork': 'qualitative',
            'Semi-structured interviews and regression': 'mixed_methods',
            'Regression on census coverage data': 'observational',
            'Mixed methods: survey and focus groups': 'mixed_methods',  # an explicit label wins over the cue counts
            'Cross-sectional': 'unmapped_needs_review',
            '': 'unmapped_needs_review',
        }
        for label, want in cases.items():
            self.assertEqual(self.cls(label), want, label)

    def test_a_review_beats_a_method_cue(self):
        self.assertEqual(self.cls('Systematic review of household survey regression studies'), 'systematic_review_secondary')

    def test_every_proposed_class_is_in_the_enumeration_or_unmapped(self):
        for label in ('x', 'case study', 'econometric panel regression', 'legal analysis of statutes'):
            self.assertIn(self.cls(label), pdv.ENUM | {'unmapped_needs_review'}, label)


class TestThinBasisPhrase(unittest.TestCase):
    def test_phrases_that_say_the_basis_was_thin(self):
        for s in ('decided on the abstract only', 'landing page only', 'paywalled abstract', 'No abstract available', 'only the abstract was available', 'bibliographic metadata record',
                  'Abstract is available but the full text is not'):
            self.assertTrue(aeb.PAT.search(s), s)

    def test_phrases_that_do_not(self):
        for s in ('the PDF was read in full', 'excluded: wrong population', 'full text confirms the study is a policy essay', ''):
            self.assertFalse(aeb.PAT.search(s), s)


class TestCriterion3Cues(unittest.TestCase):
    def test_cues_for_studies_without_empirical_data(self):
        for s in ('conceptual essay', 'Theoretical model', 'game-theoretic model', 'simulation study', 'normative analysis'):
            self.assertTrue(aic.CUE.search(s), s)
        self.assertFalse(aic.CUE.search('Randomized controlled trial'))

    def test_no_sample_patterns(self):
        for s in ('', 'not stated', 'None', 'n/a', 'no primary data'):
            self.assertTrue(aic.NO_SAMPLE.search(s), s)
        for s in ('1,200 households', '57 interviews'):
            self.assertFalse(aic.NO_SAMPLE.search(s), s)


class TestFamilyFit(unittest.TestCase):
    def test_cues(self):
        yes = {'A': ['Legal recognition of informal settlements', 'Land title formalisation', 'Home-ownership vs rental', 'Eligibility for a formal water connection', 'zoned as residential'],
               'B': ['Assistance completing the application', 'Simplified procedures', 'Bureaucratic facilitation'],
               'C': ['Documentation requirement as a barrier', 'Disconnection enforcement', 'Hukou restrictions']}
        for fam, labels in yes.items():
            for s in labels:
                self.assertTrue(aef.CUES[fam].search(s), (fam, s))
        self.assertFalse(aef.CUES['A'].search('Rainfall variability'))
        self.assertFalse(aef.CUES['B'].search('Average household income'))

    def test_build_flags_rows_outside_the_wording_and_sorts_them_first(self):
        fake = [dict(study_id='S010', synthesis_family='A', outcome_family='x', exposure_definition='Legal recognition of the settlement'),
                dict(study_id='S002', synthesis_family='A', outcome_family='x', exposure_definition='Rainfall variability'),
                dict(study_id='S003', synthesis_family='B', outcome_family='x', exposure_definition='Rainfall'),
                dict(study_id='S004', synthesis_family='', outcome_family='x', exposure_definition='anything')]  # a non-fit row (no family) is skipped
        orig = aef.cf.read
        aef.cf.read = lambda name: fake if name == 'es' else orig(name)
        self.addCleanup(setattr, aef.cf, 'read', orig)
        rows = aef.build()
        self.assertEqual([(r['study_id'], r['fit']) for r in rows], [('S002', 'outside the definition wording'), ('S010', 'cue in definition wording'), ('S003', 'outside the definition wording')])
        self.assertEqual(rows[1]['cue_found'], 'recogni')


if __name__ == '__main__':
    unittest.main(verbosity=1)
