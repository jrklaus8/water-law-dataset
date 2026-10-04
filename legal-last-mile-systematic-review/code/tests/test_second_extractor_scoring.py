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
        R = sc.score([row('S1', 'A', 'country', 'maybe'), row('S1', 'A', 'sample_size', '', value='12'), row('S1', 'A', 'study_design', 'Y')])
        self.assertEqual(sum(R['tot'].values()), 1)
        self.assertEqual([x[3] for x in R['invalid']], ['maybe']); self.assertEqual(R['filled_unjudged'][0][1:], ('S1', 'sample_size'))

    def test_everyday_spellings_and_padded_ids(self):
        R = sc.score([row('S1', 'A', 'country', 'Yes'), row('S1 ', 'A', 'sample_size', ' no '), row('S2', 'A', 'country', "Can't tell"), row('S2', 'A', 'sample_size', 'cannot tell')])
        self.assertEqual((sum(R['tot'].values()), sum(R['bad'].values())), (2, 1)); self.assertEqual(R['invalid'], [])
        self.assertEqual(sorted(R['per_study']), ['S1'])  # 'S1 ' counts as S1
        self.assertEqual([x[3] for x in sc.score([row('S1', 'A', 'country', 'maybe')])['invalid']], ['maybe'])

    def test_wilson_matches_reference_values(self):
        # reference values from the closed-form Wilson score interval (z = 1.96), e.g. as printed by standard statistics packages
        for (k, n), (lo, hi) in {(5, 10): (0.2366, 0.7634), (0, 10): (0.0, 0.2775), (10, 10): (0.7225, 1.0), (1, 20): (0.0089, 0.2361)}.items():
            got = sc.wilson(k, n)
            self.assertAlmostEqual(got[0], lo, places=4, msg=(k, n)); self.assertAlmostEqual(got[1], hi, places=4, msg=(k, n))
            self.assertTrue(0.0 <= got[0] <= got[1] <= 1.0)

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

    def test_edge_cases_all_disagree_all_missing_single_study(self):
        import contextlib
        import io
        import tempfile
        def run_main(rows):
            with tempfile.TemporaryDirectory() as d:
                p = Path(d) / 's.csv'
                with open(p, 'w', encoding='utf-8', newline='') as f:
                    w = csv.DictWriter(f, fieldnames=['study_id', 'stratum', 'field', 'second_extractor_value', V]); w.writeheader(); w.writerows(rows)
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    rc = sc.main(str(p))
                return rc, buf.getvalue()
        # everything disagrees: rate 100%, interval upper bound 100%, one study, no crash
        rc, out = run_main([row('S1', 'A', f, 'N') for f in ('country', 'sample_size', 'study_design')])
        self.assertEqual(rc, 0); self.assertIn('100.0%', out); self.assertIn('1 of 1', out)
        # nothing judged (all blank or cannot_tell): no division by zero, nothing scored
        rc, out = run_main([row('S1', 'A', 'country', ''), row('S2', 'A', 'country', 'cannot_tell')])
        self.assertEqual(rc, 0); self.assertNotIn('ALL FIELDS', out); self.assertIn('0 of 2', out)
        # a single agreeing row: 0% with a sensible interval
        rc, out = run_main([row('S1', 'A', 'country', 'Y')])
        self.assertEqual(rc, 0); self.assertIn('0.0%', out)


class TestStickySample(unittest.TestCase):
    """build_second_extractor_sample keeps an issued sheet stable: a pool change replaces only the studies that became ineligible (it once swapped 21 of 60)."""
    @classmethod
    def setUpClass(cls):
        import build_second_extractor_sample as bse
        cls.bse = bse

    def ids(self, rows):
        return {r['study_id'] for r in rows}

    def test_the_committed_sheet_is_a_fixed_point(self):
        rows = self.bse.draw()
        with open(self.bse.OUT, encoding='utf-8', newline='') as f:
            committed = list(csv.DictReader(f))
        self.assertEqual(self.ids(rows), self.ids(committed)); self.assertEqual(len(self.ids(rows)), 60)

    def test_an_ineligible_study_is_replaced_and_nothing_else_moves(self):
        import audit_sparse_records as asr
        before = self.ids(self.bse.draw())
        victim = sorted(before)[10]
        orig = asr.audit
        def fake():
            return orig() + [{'study_id': victim, 'strength': 'strong'}]
        asr.audit = fake
        self.addCleanup(setattr, asr, 'audit', orig)
        after = self.ids(self.bse.draw())
        self.assertEqual(len(after), 60); self.assertNotIn(victim, after)
        self.assertEqual(len(before - after), 1); self.assertEqual(len(after - before), 1)

    def test_without_an_earlier_sheet_the_seeded_draw_is_reproducible(self):
        import tempfile
        orig = self.bse.OUT
        with tempfile.TemporaryDirectory() as d:
            self.bse.OUT = Path(d) / 'none.csv'
            self.addCleanup(setattr, self.bse, 'OUT', orig)
            a, b = self.ids(self.bse.draw()), self.ids(self.bse.draw())
        self.assertEqual(a, b); self.assertEqual(len(a), 60)


if __name__ == '__main__':
    unittest.main(verbosity=1)
