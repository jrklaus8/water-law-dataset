#!/usr/bin/env python3
"""The interactive evidence atlas (06_outputs/EVIDENCE_ATLAS_INTERACTIVE.html) embeds the project's computed data as JSON and only filters and re-counts it in the browser.

Checks that the embedded data equal what the databases say now (so the page cannot drift from them): study counts and design mix, the PRISMA stages, the human-verification split, the 31 SWiM studies
with their statuses (13 human-verified, 18 AI-checked), the sensitivity scenarios, and that the file is what the generator writes today. Run from legal-last-mile-systematic-review/."""
import json
import re
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/analysis'))
import current_figures as cf  # noqa: E402
import build_evidence_atlas as bea  # noqa: E402

PAGE = ROOT / '06_outputs/EVIDENCE_ATLAS_INTERACTIVE.html'


class TestAtlas(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = PAGE.read_text(encoding='utf-8')
        m = re.search(r'^const D = (\{.*\});$', cls.text, re.M)
        assert m, 'no embedded data'
        cls.D = json.loads(m.group(1))
        cls.F = cf.compute()

    def test_page_is_what_the_generator_writes_today(self):
        self.assertEqual(self.D, json.loads(json.dumps(bea.gather(), ensure_ascii=False)))
        self.assertNotIn('</script', json.dumps(self.D).lower())   # embedded text must not close the script element

    def test_study_counts_and_design_mix(self):
        D, F = self.D, self.F
        self.assertEqual(len(D['studies']), F['extraction_rows'])
        em = Counter(r['study_design_class'] for r in cf.read('em'))
        self.assertEqual(Counter(s['d'] for s in D['studies']), em)
        self.assertEqual(sum(s['q'] for s in D['studies']), F['quantitative_synthesis_eligible'])
        self.assertEqual(Counter(s['t'] for s in D['studies']), Counter(F['tools']))
        self.assertEqual(len({s['id'] for s in D['studies']}), len(D['studies']))

    def test_flow_and_verification(self):
        D, F = self.D, self.F
        by = {f['k']: f['n'] for f in D['flow']}
        self.assertEqual((by['inc'], by['ft'], by['es'], by['swim'], by['hv']), (F['full_text_include'], F['full_text_decided'], F['effect_size_rows'], F['swim_core_studies'], F['swim_core_inclusion_human_verified']))
        hv = D['hv']
        self.assertEqual(hv['confirmed_includes'] + hv['adj_includes'] + hv['adj_excludes'], F['human_verified_rows'])
        self.assertEqual(sum(hv[k] for k in ('confirmed_includes', 'adj_includes', 'adj_excludes', 'ai_includes', 'ai_excludes')), F['full_text_decided'])
        self.assertEqual(sum(e['n'] for e in D['excl']), F['exclusion_log_rows'])

    def test_swim_studies_and_status(self):
        D, F = self.D, self.F
        sw = D['swim']
        self.assertEqual(len(sw), F['swim_core_studies'])
        self.assertEqual(sum(w['status'] == 'human' for w in sw), F['swim_core_inclusion_human_verified'])
        self.assertEqual(sum(w['status'] == 'ai' for w in sw), F['swim_core_ai_checked_not_human'])
        self.assertEqual(Counter(w['fam'] for w in sw), Counter({k: v for k, v in F['effect_size_by_family'].items() if k in 'ABC'}))
        self.assertEqual(D['direction_confirmed'], 0)
        coding = {r['study_id']: r for r in cf.read('es') if r['synthesis_family'] in ('A', 'B', 'C')}
        self.assertEqual({w['id'] for w in sw}, set(coding))
        for w in sw:                       # an AI-checked study never carries a human-verification detail
            if w['status'] == 'ai':
                self.assertIn('not a human confirmation', w['detail'])

    def test_scenarios_match_the_sensitivity_analysis(self):
        import sensitivity_analysis as sa
        rows = sa.scenarios()[0]
        base = self.D['scen'][0]
        self.assertEqual(len(self.D['scen']), len(rows))
        for f in 'ABC':
            self.assertEqual(base[f][0], rows[0][f'{f}_k'])
            self.assertEqual(base[f][1], rows[0][f'{f}_favourable'])

    def test_page_states_its_limits(self):
        low = self.text.lower()
        for needle in ('preliminary', 'ai-checked', 'human-verified', 'cannot tell us', 'nothing here is pooled'):
            self.assertIn(needle, low, needle)
        self.assertNotIn('lorem', low)


if __name__ == '__main__':
    unittest.main(verbosity=1)
