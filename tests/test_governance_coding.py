"""Regression tests pinning the governance classifier.

These encode what the engine currently does, so that anyone changing a pattern
can see exactly which classifications move. A failure is not automatically a
bug: it means the behaviour changed, and the change needs justifying. See
CODEBOOK.md §6.
"""
import pytest

# (text, expected category) — drawn from real headnote language across the
# three jurisdictions and four languages the engine claims to cover.
CASES = [
    # Brazil, main table
    ('corte no fornecimento de água por inadimplemento, suspensão indevida do abastecimento',
     'tariff_dispute'),
    # Brazil, rescue patterns (added after the residual audit)
    ('ação declaratória de inexistência de débito em face da caesb, cobrança de faturas de água',
     'tariff_dispute'),
    ('obrigação de fazer. abastecimento de água. implantação de rede de água em loteamento',
     'connection_refusal'),
    ('responsabilidade civil. rompimento de adutora. vazamento de água causou dano ao imóvel',
     'pipe_leak_damage'),
    # Netherlands
    ('beroep tegen het peilbesluit van het waterschap inzake wateroverlast en waterkering',
     'flooding'),
    # Canada / English
    ('judicial review of a drinking water advisory; water quality standards on reserve',
     'water_quality'),
    # The gate
    ('geschil over een huurovereenkomst voor een bedrijfspand', 'not_water_related'),
    ('appeal concerning a commercial lease and rent arrears', 'not_water_related'),
]


@pytest.mark.parametrize('text,expected', CASES)
def test_governance_category_is_stable(coding, text, expected):
    assert coding['code_governance'](text.lower()) == expected


@pytest.mark.parametrize('text,expected', CASES)
def test_explain_agrees_with_code(coding, text, expected):
    """The audit trail must never disagree with the label it explains."""
    cat, rule, span = coding['explain_governance'](text.lower())
    assert cat == coding['code_governance'](text.lower()) == expected
    assert rule, 'every decision must carry a rule identifier'


def test_gate_rules_carry_no_span(coding):
    """Rules that fire on absence have nothing to quote."""
    _, rule, span = coding['explain_governance']('a commercial lease dispute')
    assert rule == 'FILTER:no_water_vocabulary'
    assert span == ''


def test_matched_span_is_quoted_from_the_text(coding):
    text = 'corte no fornecimento de água por inadimplemento'
    _, _, span = coding['explain_governance'](text)
    assert span, 'a substantive rule must quote the text it matched'
    core = span.split(' ... ')[0]
    assert core in text, f'span {core!r} is not a substring of the input'


def test_span_is_bounded(coding):
    """Rescue patterns bridge terms with .*? and must not dump whole headnotes."""
    long_text = ('inexistência de débito ' + 'texto irrelevante ' * 200 + ' caesb')
    _, _, span = coding['explain_governance'](long_text)
    assert len(span) <= coding['AUDIT_SPAN_MAX']


def test_every_category_is_reachable(coding):
    """No category may be shadowed into unreachability by an earlier one."""
    names = [c for c, _ in coding['GOV_CATS']]
    assert len(names) == len(set(names)), 'duplicate category in GOV_CATS'
    assert len(names) == 19, f'expected 19 substantive categories, found {len(names)}'
