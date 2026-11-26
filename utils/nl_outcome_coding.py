"""Outcome coding for Dutch administrative decisions (FUTURE_WORK.md, Priority 1).

Offline, standard-library only. Works on the operative part ("Beslissing") of a
decision, supplied either as plain text (as served by Legal Data Hunter, where
the body is one flat string) or as rechtspraak.nl XML.

Codes: WIN, LOSS, PARTIAL, INADMISSIBLE, REMAND, UNCLASSIFIED.
WIN means the appeal/claim was upheld from the appellant's side. Whether the
appellant is an individual, a municipality or a utility is NOT coded here
(see "Appellant Identity Coding" in FUTURE_WORK.md).

Design notes
- Only the Beslissing segment is classified. Words such as "vernietigt" occur
  throughout reasoning sections and would produce false WINs.
- Precedence is explicit and most specific first: PARTIAL, INADMISSIBLE,
  REMAND, WIN, LOSS. A decision that annuls AND dismisses elsewhere is
  PARTIAL only if the text says "gedeeltelijk"; otherwise multiple distinct
  labels are reported in `outcome_flags` and the primary code is WIN, with
  LOSS-only decisions requiring no WIN marker.
- Regex output is a first pass. UNCLASSIFIED rows should go to a human or LLM
  pass, and a manual sample must be validated before analysis.
"""
import re
from typing import Dict, List, Optional, Tuple

_FLAGS = re.IGNORECASE

PATTERNS: Dict[str, re.Pattern] = {
    "PARTIAL": re.compile(
        r"gedeeltelijk\s+gegrond|deels\s+gegrond|gegrond\s+voor\s+zover", _FLAGS),
    "INADMISSIBLE": re.compile(
        r"niet[\s-]*ontvankelijk|onbevoegd|verklaart\s+zich\s+onbevoegd", _FLAGS),
    "REMAND": re.compile(
        r"verwijst\s+(?:de\s+zaak|het\s+geding)\s+(?:terug|naar)|"
        r"draagt\s+(?:het\s+bestuursorgaan|verweerder|de\s+\w+)\s+op\s+.{0,80}"
        r"(?:nieuw\s+besluit|opnieuw)", _FLAGS),
    # "ongegrond" must be excluded from the gegrond match
    "WIN": re.compile(
        r"(?<!on)gegrond\b|vernietigt\b|herroept\b|"
        r"(?:verklaart|acht)\s+het\s+bezwaar\s+(?<!on)gegrond|"
        r"wijst\s+(?:het\s+verzoek|de\s+vordering)\s+toe", _FLAGS),
    "LOSS": re.compile(
        r"ongegrond\b|bevestigt\s+de\s+(?:aangevallen|bestreden)|"
        r"wijst\s+(?:het\s+verzoek|de\s+vordering)\s+af|verwerpt\s+het\s+beroep|"
        r"laat\s+het\s+bestreden\s+besluit\s+in\s+stand", _FLAGS),
}
PRECEDENCE = ["PARTIAL", "INADMISSIBLE", "REMAND", "WIN", "LOSS"]

_START = re.compile(r"(?:^|\s|\n)(?:\d+\.\s*)?(?:Beslissing|BESLISSING|Beslissing\s+van\s+de\s+\w+)\b")
_END = re.compile(
    r"Deze\s+uitspraak\s+is\s+gedaan\s+door|Aldus\s+(?:vastgesteld|gedaan|gewezen)|"
    r"Uitgesproken\s+in\s+het\s+openbaar|Deze\s+beslissing\s+is\s+gegeven\s+door", _FLAGS)


def extract_beslissing(text: str, max_chars: int = 3000) -> str:
    """Return the operative part of a decision given as flat text.

    Uses the LAST 'Beslissing' heading (headings may also appear in
    "Procesverloop" cross-references) and cuts at the signature block.
    Returns '' when no heading is found.
    """
    if not text:
        return ""
    starts = [m.end() for m in _START.finditer(text)]
    if not starts:
        return ""
    seg = text[starts[-1]:]
    m = _END.search(seg)
    if m:
        seg = seg[:m.start()]
    return seg.strip()[:max_chars]


def extract_beslissing_xml(xml_text: str) -> str:
    """Best-effort extraction from rechtspraak.nl XML.

    UNVERIFIED against the live API (not reachable when written): section
    roles and namespaces are matched loosely. Falls back to flat-text logic.
    """
    from xml.etree import ElementTree as ET
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return extract_beslissing(re.sub(r"<[^>]+>", " ", xml_text))
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag == "section":
            role = (el.get("role") or "").lower()
            title = " ".join(
                " ".join(t.itertext()) for t in el if t.tag.split("}")[-1] in ("title", "kop"))
            if "beslissing" in role or "beslissing" in title.lower():
                return " ".join(" ".join(el.itertext()).split())[:3000]
    flat = " ".join(" ".join(root.itertext()).split())
    return extract_beslissing(flat)


def classify_outcome(beslissing: str) -> Tuple[str, List[str]]:
    """Return (primary_code, all_matched_codes)."""
    if not beslissing or not beslissing.strip():
        return "UNCLASSIFIED", []
    hits = [k for k in PRECEDENCE if PATTERNS[k].search(beslissing)]
    if not hits:
        return "UNCLASSIFIED", []
    return hits[0], hits


def code_decision(text: str, is_xml: bool = False) -> Dict[str, Optional[str]]:
    seg = extract_beslissing_xml(text) if is_xml else extract_beslissing(text)
    primary, hits = classify_outcome(seg)
    if not seg:
        primary = "UNCLASSIFIED"
    return {
        "outcome": primary,
        "outcome_flags": "|".join(hits),
        "outcome_multi": str(len(hits) > 1),
        "beslissing_excerpt": seg[:300],
    }
