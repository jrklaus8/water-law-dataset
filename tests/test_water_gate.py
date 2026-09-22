"""Tests documenting the Dutch compound defect in the water-vocabulary gate.

The gate decides, before any category is considered, whether a decision is a
water case at all. It uses `\\b` word boundaries, which Dutch compounding
defeats. These tests pin the CURRENT behaviour and mark the known-wrong cases
with xfail, so that whoever fixes the gate sees the tests flip to xpass rather
than discovering the problem by accident.

See CODEBOOK.md §4.1 and DATA_ACCESS.md §6.2.
"""
import pytest

# Terms the gate correctly recognises.
SEEN = ['water', 'waterschap', 'drinkwater', 'grondwater', 'riolering',
        'wateroverlast', 'dijk', 'peilbesluit']

# Dutch compounds the gate cannot see. Each is unambiguously a water term.
UNSEEN = ['waterwet', 'watervergunning', 'grondwateronttrekking',
          'drinkwatervoorziening', 'afvalwater', 'oppervlaktewater',
          'hemelwater', 'rioolwater', 'waterhuishouding', 'waterbodem',
          'zwemwater', 'waterschapsbelasting']


@pytest.mark.parametrize('term', SEEN)
def test_gate_recognises_simple_terms(coding, term):
    assert coding['_WATER_CORE_RE'].search(term), f'{term} should pass the gate'


@pytest.mark.parametrize('term', UNSEEN)
@pytest.mark.xfail(strict=True, reason='KNOWN DEFECT: \\b boundaries vs Dutch '
                                       'compounding. See CODEBOOK.md 4.1.')
def test_gate_recognises_compounds(coding, term):
    assert coding['_WATER_CORE_RE'].search(term), f'{term} should pass the gate'


def test_compound_decision_is_gated_out(coding):
    """End-to-end consequence: a plain water-permit case is called not-water."""
    text = 'vergunning voor grondwateronttrekking ten behoeve van drinkwaterwinning'
    assert coding['code_governance'](text) == 'not_water_related'
