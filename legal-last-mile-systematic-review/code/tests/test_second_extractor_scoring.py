#!/usr/bin/env python3
"""Tests for code/analysis/score_second_extractor_sheet.py, so the one independent check in the project is known to score correctly before a human's
filled sheet arrives. Run from legal-last-mile-systematic-review/:  python3 code/tests/test_second_extractor_scoring.py"""
import csv
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/analysis'))
import score_second_extractor_sheet as sc  # noqa: E402

V = sc.VERDICT


def row(study, stratum, field, verdict, value='x'):
    return {'study_id': study, 'stratum': stratum, 'field': field, V: verdict, 'second_extractor_value': value}


class TestScore(unittest.TestCase):
    def test_counts_and_strata(self):
        R = sc.score([row('S1', 'A', 'country', 'Y'), row('S1', 'A', 'sample_size', 'N'), row('S2', 'B', 'country', 'n'),
                      row('S2', 'B', 'sample_size', 'cannot_tell'), row('S3', 'B', 'country', '', value='')])
        self.assertEqual((sum(R["tot"].values()), sum(R["bad"].values())), (3, 2))
        self.assertEqual(dict(R['st_tot']), {'A': 2, 'B': 1}); self.assertEqual(dict(R['st_bad']), {'A': 1, 'B': 1})
        self.assertEqual(sorted(R['per_study']), ['S1', 'S2']); self.assertEqual(R['n_studies'], 3)
        self.assertEqual(R['invalid'], []); self.assertEqual(R['filled_unjudged'], [])  # 'n' lower case and 'cannot_tell' are accepted; a blank with no value is not a warning

    def test_invalid_and_unjudged_are_flagged_not_scored(self):
        R = sc.score([row('S1', 'A', 'country', 'yes'), row('S1', 'A', 'sample_size', '', value='12'), row('S1', 'A', 'study_design', 'Y')])
        self.assertEqual(sum(R['tot'].values()), 1)
        self.assertEqual([x[3] for x in R['invalid']], ['yes']); self.assertEqual(R['filled_unjudged'][0][1:], ('S1', 'sample_size'))

    def test_wilson_interval(self):
        lo, hi = sc.wilson(0, 10); self.assertEqual(lo, 0.0 if lo == 0 else lo); self.assertLess(hi, 0.31)
        lo, hi = sc.wilson(5, 10); self.assertAlmostEqual((lo + hi) / 2, 0.5, places=1)
        self.assertTrue(all(x != x for x in sc.wilson(0, 0)))  # nan

    def test_blank_sheet_scores_nothing(self):
        blank = ROOT / '03_extraction/second_extractor/second_extractor_sheet_BLANK_2026-10-04.csv'
        rows = list(csv.DictReader(open(blank, encoding='utf-8', newline='')))
        self.assertGreater(len(rows), 100)
        R = sc.score(rows)
        self.assertEqual(sum(R['tot'].values()), 0); self.assertEqual(R['invalid'], []); self.assertEqual(R['filled_unjudged'], [])

    def test_tolerant_reading(self):
        import tempfile
        head = f'study_id,stratum,field,second_extractor_value,{V}\n'
        with tempfile.TemporaryDirectory() as d:
            for name, data in {'bom': ('\ufeff' + head + 'S1,A,country,caf\u00e9,Y\n').encode('utf-8'), 'cp': (head + 'S1,A,country,caf\u00e9,N\n').encode('cp1252'),
                               'semi': head.replace(',', ';').encode() + b'S1;A;country;x;Y\n;;;;\n'}.items():
                p = Path(d) / name; p.write_bytes(data)
                rows = sc.read_rows(str(p)); self.assertEqual(len(rows), 1); self.assertEqual(rows[0]['field'], 'country')
            (Path(d) / 'bad').write_bytes(b'a,b\n1,2\n')
            with self.assertRaises(SystemExit):
                sc.read_rows(str(Path(d) / 'bad'))


if __name__ == '__main__':
    unittest.main(verbosity=1)
