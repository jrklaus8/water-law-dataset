"""Offline tests for utils/nl_outcome_coding.py. Fixture 1 is the operative
part of a real public decision (ECLI:NL:RBROT:2026:1954); others are synthetic."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils.nl_outcome_coding import code_decision, classify_outcome, extract_beslissing

REAL = ("Conclusie en gevolgen 7. Het beroep is ongegrond. Beslissing De rechtbank "
        "verklaart het beroep ongegrond. Deze uitspraak is gedaan door mr. J.C. de Vries, rechter.")

def test_real_loss():
    assert code_decision(REAL)["outcome"] == "LOSS"

def test_ongegrond_not_win():
    assert classify_outcome("verklaart het beroep ongegrond")[0] == "LOSS"

def test_win():
    assert classify_outcome("verklaart het beroep gegrond en vernietigt het besluit")[0] == "WIN"

def test_partial_precedence():
    assert classify_outcome("verklaart het beroep gedeeltelijk gegrond, vernietigt het besluit")[0] == "PARTIAL"

def test_inadmissible():
    assert classify_outcome("verklaart het beroep niet-ontvankelijk")[0] == "INADMISSIBLE"

def test_remand():
    assert classify_outcome("verwijst de zaak terug naar de rechtbank")[0] == "REMAND"

def test_reasoning_not_classified():
    t = "De rechtbank vernietigt dit niet. Beslissing De rechtbank verklaart het beroep ongegrond. Deze uitspraak is gedaan door X"
    assert code_decision(t)["outcome"] == "LOSS"

def test_no_heading_unclassified():
    assert code_decision("geen operatief deel hier")["outcome"] == "UNCLASSIFIED"

def test_stops_at_signature():
    seg = extract_beslissing("Beslissing De rechtbank verklaart het beroep gegrond. Deze uitspraak is gedaan door X vernietigt")
    assert "vernietigt" not in seg
