#!/usr/bin/env python3
"""The executive summary (06_outputs/EXECUTIVE_SUMMARY_2026-10-14.docx) quotes the current figures.

Checks, against figures recomputed from the databases rather than read back from the builder's own output: (1) the headline screening and verification numbers appear in the text;
(2) the family table matches the baseline sensitivity scenario and the three family sizes add up to the studies in the coding file (37 after the A29 ruling); (3) the flagged / confirmed / not-yet split equals the
counts in current_figures; (4) no template placeholder, "None" or "nan" leaked into the text; (5) the picture has alt text; (6) the document makes no claim to a pooled effect or to full human review.
Run from legal-last-mile-systematic-review/:  python3 code/tests/test_executive_summary.py"""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/analysis'))
import build_executive_summary as bes  # noqa: E402
from docx import Document  # noqa: E402

DOC = ROOT / '06_outputs/EXECUTIVE_SUMMARY_2026-10-14.docx'


class TestExecutiveSummary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.D = bes.gather()
        d = Document(DOC)
        cls.paras = [p.text for p in d.paragraphs]
        cls.tables = [[[c.text for c in r.cells] for r in t.rows] for t in d.tables]
        cls.text = '\n'.join(cls.paras + [c for t in cls.tables for r in t for c in r])
        cls.doc = d

    def test_headline_numbers(self):
        F = self.D['F']
        for needle in (f"{F['human_verified_rows']:,} of {F['full_text_decided']:,}", f"{F['full_text_include']:,} included", f"{F['full_text_exclude']:,} excluded",
                       f"{F['effect_size_rows']} effect-size rows", f"{F['swim_core_flagged_for_author']} flagged core studies", f"{F['causal_capable_designs']} "):
            self.assertIn(needle, self.text, needle)

    def test_family_table_matches_baseline(self):
        b = self.D['base']
        t = next(x for x in self.tables if x[0][0] == 'Family')
        self.assertEqual(len(t), 4)
        total = 0
        for row, f in zip(t[1:], 'ABC'):
            self.assertEqual(int(row[1]), b[f'{f}_k'])
            self.assertEqual(row[2], f"{b[f'{f}_positive']} / {b[f'{f}_negative']} / {b[f'{f}_null']} / {b[f'{f}_mixed']}")
            self.assertEqual(row[3], f"{b[f'{f}_favourable']} / {b[f'{f}_unfavourable']} / {b[f'{f}_subst_null']} / {b[f'{f}_subst_mixed']}")
            self.assertEqual(sum(int(x) for x in row[4].split(' / ')), b[f'{f}_k'])
            total += int(row[1])
        self.assertEqual(total, self.D['F']['swim_core_studies'])
        self.assertEqual(total, len(self.D['code']))

    def test_check_split_equals_current_figures(self):
        F, t = self.D['F'], next(x for x in self.tables if x[0][0] == 'Family')
        conf = sum(int(r[4].split(' / ')[0]) for r in t[1:])
        flag = sum(int(r[4].split(' / ')[1]) for r in t[1:])
        self.assertEqual((conf, flag), (F['swim_core_direction_ck_confirmed'], F['swim_core_flagged_for_author']))

    def test_no_template_leaks(self):
        for bad in ('{', '}', '%%', '  .'):
            self.assertNotIn(bad, self.text, bad)
        self.assertIsNone(re.search(r'\bnan\b', self.text, re.I))
        self.assertIsNone(re.search(r'\bNone\b(?! is pooled)', self.text))   # a literal Python None; "None is pooled" is the table's own wording

    def test_picture_has_alt_text(self):
        shapes = self.doc.inline_shapes
        self.assertEqual(len(shapes), 1)
        self.assertGreater(len(shapes[0]._inline.docPr.get('descr', '')), 40)

    def test_no_overclaim(self):
        low = self.text.lower()
        self.assertIn('nothing is pooled', low)
        self.assertNotIn('100% of the', low)
        self.assertNotIn('fully verified', low)
        self.assertIn('flagged', low)

    def test_standalone_geography_framing(self):
        """The summary and the manuscript describe what the geographic distribution shows, without reference to the dissertation's comparison countries; the counts come from the extraction database."""
        low = self.text.lower()
        self.assertNotIn('dissertation', low)
        self.assertNotIn('comparative frame', low)
        import build_manuscript_pieces as bmp
        g = bmp.geography_framing(self.D['F'])
        self.assertEqual((g['canada'], g['netherlands']), (15, 1))
        self.assertEqual(g['canada_fn'], 12)                                   # the Canadian studies that concern First Nations or other Indigenous communities (checked by reading their titles, 2026-10-14)
        self.assertIn(f"{g['canada']} single-country studies in Canada", self.text)
        ms = (ROOT / '07_manuscript/draft/MANUSCRIPT_DRAFT_2026-10-04.md').read_text(encoding='utf-8').lower()
        self.assertNotIn('comparative frame', ms)
        self.assertEqual(ms.count('dissertation'), 1)                          # only the declaration of the companion PhD project
        self.assertIn('universal-network systems', ms)
        self.assertNotIn('municipal discretion', g['full'].lower())            # discretion is the second most coded mechanism in the corpus, so it is not called under-examined


if __name__ == '__main__':
    unittest.main(verbosity=1)
