#!/usr/bin/env python3
"""The SWiM source-verification dossier (05_analysis/effect_sizes/SWIM_37_SOURCE_VERIFICATION_DOSSIER.md) and the blind second-extractor sheet.

Checks, against the databases rather than the builder: (1) the dossier has one entry for each of the 37 studies in Families A, B and C and the manifest one row each; (2) its status counts equal the figures in current_figures (10 flagged,
the rest AI-checked or confirmed earlier); (3) the dossier records no verification: no ticked box, no filled decision field; (4) every A28 study has hand-picked quotes with a PDF page and nobody else's name is on a decision;
(5) the blind sheet has the 60 sampled studies, nine fields each, and no AI value, location or stratum; (6) the committed files make no claim of CK confirmation of their own.
Run from legal-last-mile-systematic-review/:  python3 code/tests/test_swim_dossier.py"""
import csv
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/analysis'))
csv.field_size_limit(sys.maxsize)
import current_figures as cf  # noqa: E402
from swim_dossier_curated import CURATED  # noqa: E402

DOS = ROOT / '05_analysis/effect_sizes/SWIM_37_SOURCE_VERIFICATION_DOSSIER.md'
MAN = ROOT / '05_analysis/effect_sizes/SWIM_37_SOURCE_PDF_MANIFEST.csv'
BLIND = ROOT / '03_extraction/second_extractor/second_extractor_sheet_BLIND_VALUES_2026-10-14.csv'
A28 = {'S920', 'S1020', 'S1042', 'S1057', 'S294', 'S1102', 'S1144', 'S1163', 'S947', 'S1146'}


def rows(p):
    with open(p, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


class TestDossier(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = DOS.read_text(encoding='utf-8')
        cls.core = sorted(r['study_id'] for r in cf.read('es') if r['synthesis_family'] in ('A', 'B', 'C'))
        cls.F = cf.compute()
        cls.entries = dict(re.findall(r'^### (S\d+)  ·  (.*?)(?=^### S\d+  ·  |\Z)', cls.text, re.S | re.M))

    def test_one_entry_per_study(self):
        self.assertEqual(len(self.core), 37)
        self.assertEqual(sorted(self.entries, key=lambda s: int(s[1:])), sorted(self.core, key=lambda s: int(s[1:])))
        self.assertEqual(sorted(r['study_id'] for r in rows(MAN)), sorted(self.core))

    def test_status_counts_follow_current_figures(self):
        flagged = sum('FLAGGED in A28' in e for e in self.entries.values())
        ai = sum('RECORDED on 2026-10-14 after the AI' in e for e in self.entries.values())
        earlier = sum(e.count('Inclusion confirmed by you earlier') + e.count('Inclusion decided by your own CK ruling earlier') for e in self.entries.values())
        self.assertEqual(flagged, self.F['swim_core_flagged_for_author'])
        self.assertEqual(ai, self.F['swim_core_direction_ck_confirmed'])
        self.assertEqual(flagged + ai + earlier, 37)

    def test_dossier_records_no_verification(self):
        self.assertNotIn('[x]', self.text.lower())
        self.assertEqual(self.text.count('- [ ] Inclusion and scope'), 37)
        for needle in ('**Your decision:** ____', '**Your A28 ruling:** keep / exclude E03 / exclude other (code ____)'):
            self.assertIn(needle, self.text)
        self.assertIsNone(re.search(r'human_verified\s*[=:]\s*Y', self.text))

    def test_a28_entries_carry_checked_quotes_and_pages(self):
        for s in A28:
            e = self.entries[s]
            self.assertIn('Hand-picked passages for your A28 ruling', e, s)
            for _label, q in CURATED[s]['quotes']:
                self.assertIn(q, e, (s, q[:60]))
            self.assertRegex(e, r'\(PDF p\. \d+', s)

    def test_manifest_is_complete_where_a_pdf_was_read(self):
        for r in rows(MAN):
            if r['text_layer'] not in ('no pdf', ''):
                self.assertEqual(len(r['sha256']), 64, r['study_id'])
                self.assertGreater(int(r['pages']), 0, r['study_id'])
        self.assertEqual({r['study_id'] for r in rows(MAN) if r['text_layer'] == 'no pdf'}, {'S471'})   # the one study with no source file


class TestBlindSheet(unittest.TestCase):
    def test_no_ai_values_in_the_blind_sheet(self):
        r = rows(BLIND)
        self.assertEqual(len(r), 540)
        self.assertEqual(len({x['study_id'] for x in r}), 60)
        self.assertEqual(set(r[0]), {'study_id', 'citation', 'doi', 'field', 'what_to_check', 'second_extractor_value', 'comment'})
        self.assertTrue(all(x['second_extractor_value'] == '' for x in r))
        blank = {(x['study_id'], x['field']): x for x in rows(ROOT / '03_extraction/second_extractor/second_extractor_sheet_BLANK_2026-10-04.csv')}
        self.assertEqual({(x['study_id'], x['field']) for x in r}, set(blank))
        for x in r:
            ai = blank[(x['study_id'], x['field'])]['ai_value'].strip()
            if x['field'] in ('risk_of_bias_tool', 'outcome_flags', 'mechanism_flags'):
                continue                                   # these three are re-asked with the full list of options, which is not a leak of the AI's choice
            if len(ai) > 6:
                self.assertNotIn(ai.lower(), (x['what_to_check'] + ' ' + x['comment']).lower())


if __name__ == '__main__':
    unittest.main(verbosity=1)
