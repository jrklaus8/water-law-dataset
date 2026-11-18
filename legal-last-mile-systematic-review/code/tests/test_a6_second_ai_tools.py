#!/usr/bin/env python3
"""Tests for compare_a6_reviews.py and verify_second_ai_quotes.py on small synthetic inputs (no real papers, no real decisions).
Run from legal-last-mile-systematic-review/."""
import json, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/screening'))
import compare_a6_reviews as cmp  # noqa: E402
import verify_second_ai_quotes as vq  # noqa: E402

H = 'reviewer_decision (include/exclude/cannot_tell)'


class TestCompare(unittest.TestCase):
    def test_statuses(self):
        queue = [{'record_id': f'R{i}', 'ai_decision': 'include'} for i in range(5)]
        human = [{'record_id': 'R0', 'study_id': 'S0', H: 'include'}, {'record_id': 'R1', 'study_id': 'S1', H: 'exclude'},
                 {'record_id': 'R2', 'study_id': 'S2', H: ''}, {'record_id': 'R3', 'study_id': 'S3', H: 'cannot_tell'},
                 {'record_id': 'R4', 'study_id': 'S4', H: 'include'}]
        second = [{'record_id': 'R0', 'decision': 'include'}, {'record_id': 'R1', 'decision': 'include'}, {'record_id': 'R2', 'decision': 'include'},
                  {'record_id': 'R3', 'decision': 'include'}]
        st = {r['record_id']: r['status'] for r in cmp.compare(human, second, queue)}
        self.assertEqual(st['R0'], 'all three agree')
        self.assertTrue(st['R1'].startswith('DISAGREEMENT'))
        self.assertEqual(st['R2'], 'human not yet decided')
        self.assertEqual(st['R3'], 'cannot_tell involved')
        self.assertEqual(st['R4'], 'second AI missing')

    def test_human_columns_untouched_and_report_runs(self):
        rows = cmp.compare([{'record_id': 'R0', 'study_id': 'S0', H: 'exclude', 'saw_AI_reasoning_before_deciding (Y/N)': 'Y'}],
                           [{'record_id': 'R0', 'decision': 'include', 'confidence': 'high'}], [{'record_id': 'R0', 'ai_decision': 'include'}])
        txt = cmp.report(rows)
        self.assertIn('DISAGREEMENT', txt)
        self.assertIn('Anchoring flags: 1', txt)


class TestQuotes(unittest.TestCase):
    def test_verification(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            (t / 'R1.txt').write_text('Households were disconnected after\nthree months of non-pay-\nment, according to the utility’s rules.', encoding='utf-8')
            j = t / 'j'; j.mkdir()
            (j / 'R1.json').write_text(json.dumps({'record_id': 'R1', 'evidence_quotes': [
                {'criterion': 'c2', 'page': '3', 'quote': "disconnected after three months of non-payment, according to the utility's rules"},
                {'criterion': 'c4', 'page': '4', 'quote': 'this sentence is invented and does not occur anywhere'}]}), encoding='utf-8')
            (j / 'R2.json').write_text(json.dumps({'record_id': 'R2'}), encoding='utf-8')
            res = {(r['record_id'], r['criterion']): r['result'] for r in vq.check(j, t)}
            self.assertEqual(res[('R1', 'c2')], 'verified')
            self.assertEqual(res[('R1', 'c4')], 'NOT FOUND IN TEXT')
            self.assertEqual(res[('R2', '')], 'NO QUOTES GIVEN')


if __name__ == '__main__':
    unittest.main()
