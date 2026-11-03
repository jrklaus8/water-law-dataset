#!/usr/bin/env python3
"""source_text_tools.py: the text clean-up and number matching behind the SWiM source-verification dossier and the second-extractor packet (no PDF needed).

Run from legal-last-mile-systematic-review/:  python3 code/tests/test_source_text_tools.py"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/analysis'))
import source_text_tools as T  # noqa: E402


class TestClean(unittest.TestCase):
    def test_ligatures_hyphens_and_whitespace(self):
        self.assertEqual(T.clean('the diﬀerence in  ­\nsigniﬁcant'), 'the difference in significant')
        self.assertEqual(T.clean('market-\nbased  sanitation'), 'marketbased sanitation')       # a hyphen at a line break inside a word is joined
        self.assertEqual(T.clean('well-\nKnown'), 'well- Known')                                  # but not before a capital letter

    def test_sentences_keep_abbreviations_and_decimals_together(self):
        class D(T.Doc):
            def __init__(self):
                self.pages = ['We follow Smith et al. (2010) and find 3.54 times more area. A second sentence follows here, long enough. The third one is also long enough to keep.']
        sents = D().sentences(1)
        self.assertEqual(len(sents), 3)
        self.assertIn('3.54 times', sents[0])
        self.assertIn('et al.', sents[0])


class TestNumbers(unittest.TestCase):
    def test_estimate_tokens(self):
        toks = T.number_tokens('coefficient -1.1858 (SE 0.4163, p = 0.004); 95% CI 0.05 to 0.10; -41,810.91 (SE 25,959.55)', 'estimate')
        self.assertEqual(toks, ['1.1858', '0.4163', '0.004', '41810.91', '25959.55'])   # weak numbers (0.05, 0.10) and the sign are dropped, thousands commas removed
        self.assertEqual(T.number_tokens('an increase of 32 percentage points', 'estimate'), ['32'])

    def test_sample_tokens(self):
        self.assertEqual(T.number_tokens('5,276 villages; 10,408 roads; 2,677 schools in 2019', 'n'), ['5276', '10408', '2677'])   # the year is not a sample size
        self.assertEqual(T.number_tokens('37 clusters and 7 villages', 'n'), ['37'])

    def test_printed_forms(self):
        self.assertTrue(T.present(['3283'], 'in 3,283 households'))
        self.assertTrue(T.present(['0.55'], 'a coefficient of 0.55***'))
        self.assertTrue(T.present(['0.55'], 'a coefficient of 0,55'))                            # decimal comma
        self.assertTrue(T.present(['0.55'], 'coefficient .55'))                                  # dropped leading zero
        self.assertFalse(T.present(['0.55'], 'the value 10.55 is unrelated'))                    # not inside a longer number
        self.assertFalse(T.present(['470'], 'n = 4705'))
        self.assertTrue(T.present(['41810.91'], 'a coefficient of -41,810.91 (SE'))

    def test_rounded_forms(self):
        self.assertEqual(T.present_rounded(['0.14', '19.21'], 'Water poverty -0.140*** and REGU 19.2078***'), ['0.14', '19.21'])
        self.assertEqual(T.present_rounded(['0.15'], 'only -0.140 here'), [])
        self.assertEqual(T.present_rounded(['1.89'], 'Capacidade_Politica -1,890 0,883'), ['1.89'])


class TestFilters(unittest.TestCase):
    def test_equation_debris_is_garbled(self):
        self.assertTrue(T._garbled('y it ¼ a þ b1 D:ruralassocit þ Xit 0b ð 1 Þ'))
        self.assertFalse(T._garbled('Municipalities with association projects realized increases of about six percentage points.'))


if __name__ == '__main__':
    unittest.main(verbosity=1)
