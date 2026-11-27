#!/usr/bin/env python3
"""Rule-based coding of WHO brought the challenge (appellant identity) in Dutch Rechtspraak.nl decisions.

Input: the `opening` text kept by utils/nl_text_features.py (caption and procedural history).
Method: find the first party-role word (appellant, eiser, verzoeker, ...) in the caption, take the party description that
precedes it (back to the last 'tussen', 'beroep van' or 'verzoek van' marker), and match entity patterns.

Types: MUNICIPALITY, WATER_BOARD, PROVINCE, STATE_BODY, UTILITY, COMPANY, NGO_ASSOCIATION, PRIVATE_ANONYMISED, UNKNOWN, MIXED(a+b).
IMPORTANT LIMIT: Rechtspraak.nl anonymises natural persons as "[naam]", and often companies too. PRIVATE_ANONYMISED therefore
means "a party shown only as a placeholder": a natural person, or an entity whose name was removed. It must NOT be read as
"household" or "individual". Only an explicit legal-form word (B.V., V.O.F., Maatschap, Stichting, ...) identifies an entity.
"""
import re

ROLE = re.compile(r"\b(appellant(?:e|en|es)?|eiser(?:es|s)?|eisers|verzoek(?:er|ster|ers|sters)|klager(?:s|es)?|reclamant(?:e|en)?|"
                  r"belanghebbende(?:n)?|indiener(?:s)?|verweerder(?:s)?)\b", re.I)
MARK = re.compile(r"(?:in\s+de\s+zaken?\s+tussen|in\s+de\s+zaak\s+van|tussen|hoger\s+beroep\s+van:?|beroep\s+van:?|verzoek\s+van:?|bezwaar\s+van:?|op\s+het\s+(?:hoger\s+)?beroep\s+van:?|van:)", re.I)

PATTERNS = [
    ("WATER_BOARD", re.compile(r"waterschap|hoogheemraadschap|dijkgraaf|water\s*board", re.I)),
    ("MUNICIPALITY", re.compile(r"college\s+van\s+burgemeester|burgemeester\s+en\s+wethouders|\bburgemeester\b|\bgemeenteraad\b|\braad\s+van\s+de\s+gemeente|^\s*(?:\d\.\s*)?(?:de\s+)?gemeente\b", re.I)),
    ("PROVINCE", re.compile(r"gedeputeerde\s+staten|\bprovincie\b|provinciale\s+staten", re.I)),
    ("STATE_BODY", re.compile(r"\bminister\b|\bdienst\b|\bdirectie\b|agentschap|\bcbr\b|\bnvwa\b|staatssecretaris|\bstaat\s+der\s+nederlanden\b|\bde\s+staat\b|belastingdienst|rijkswaterstaat|\bctgb\b|nederlandse\s+voedsel|autoriteit|inspectie|\bcollege\s+van\s+beroep|\bUWV\b|\bRVO\b|raad\s+voor", re.I)),
    ("UTILITY", re.compile(r"\bvitens\b|dunea|evides|\bpwn\b|waternet|brabant\s*water|\boasen\b|waterleiding|waterbedrijf|drinkwaterbedrijf|netbeheerder|liander|stedin|enexis|\bwml\b|waterbedrijf|\bwbl\b", re.I)),
    ("NGO_ASSOCIATION", re.compile(r"stichting|vereniging|\bfederatie\b|\bbond\b|\bcomit[eé]\b|\bbelangen\w*\b|\bvve\b|\bmilieu\w*\s+(?:defensie|federatie)|\bgreenpeace\b|\bnatuur\w*\b(?=.*\bvereniging)", re.I)),
    ("COMPANY", re.compile(r"\bb\.?v\.?\b|\bn\.?v\.?\b|\bv\.?o\.?f\.?\b|\bmaatschap\b|\bc\.?v\.?\b|\bholding\b|\bcoöperatie\b|\bcooperatie\b|\bvennootschap\b|\bonderneming\b|\bgroep\b|\bgmbh\b|\bltd\b|\bfirma\b|\bhandelsnaam\b|\bmanagement\b|\bexploitatie\b", re.I)),
]
RESIDENCE = re.compile(r"(?:wonend|woonachtig|gewoond\s+hebbend|gevestigd|uit|te)\s+(?:te|in)?\s*[^,;]{0,60}(?:,\s*gemeente\s+[^,;]{1,40})", re.I)
PLACEHOLDER = re.compile(r"\[[^\]]{1,40}\]")


def party_segment(opening):
    """Return the text describing the first appellant/applicant-type party, or ''.
    Placeholders such as [verzoeker] are masked first so that a role word inside a placeholder is not mistaken for a caption role."""
    head = PLACEHOLDER.sub("[X]", opening[:2200])[:1800]
    # Raad van State appeal captions: "Uitspraak op het hoger beroep van: <party>, wonend te Y, tegen de uitspraak van ..."
    m = re.search(r"(?:hoger\s+beroep|beroep|verzoek)\s+van:\s+(.{3,350}?)(?:,\s*(?:tegen|gemachtigde)|\s+tegen\s+de\s+uitspraak|\s+in\s+het\s+geding)", head[:900], re.I)
    if m:
        return m.group(1).strip(" ,;:()")
    # Caption with an explicit role word near the top: "in de zaak tussen <party>, appellant, en <party>, verweerder"
    for m in ROLE.finditer(head[:900]):
        if m.group(1).lower().startswith("verweerder"):
            continue
        before = head[max(0, m.start() - 450):m.start()]
        marks = list(MARK.finditer(before))
        seg = before[marks[-1].end():] if marks else before[-200:]
        return seg.strip(" ,;:()")
    return ""


def code_party(seg):
    seg = seg if "[X]" not in seg else seg
    if not seg:
        return "UNKNOWN", "no appellant role word in caption"
    seg = RESIDENCE.sub("", seg)
    found = []
    for label, rx in PATTERNS:
        if rx.search(seg):
            found.append(label)
    if found:
        # public-law bodies outrank generic company/NGO words when both occur only because of a long segment
        uniq = []
        for f in found:
            if f not in uniq:
                uniq.append(f)
        if len(uniq) == 1:
            return uniq[0], "pattern: " + uniq[0]
        # several types in one party group: report them in a fixed order
        order = ["WATER_BOARD", "MUNICIPALITY", "PROVINCE", "STATE_BODY", "UTILITY", "NGO_ASSOCIATION", "COMPANY"]
        uniq.sort(key=order.index)
        return "MIXED(" + "+".join(uniq) + ")", "several patterns in the party group"
    if PLACEHOLDER.search(seg) or seg.strip() == "[X]":
        return "PRIVATE_ANONYMISED", "placeholder only"
    return "UNKNOWN", "no pattern matched"


def code_opening(opening):
    seg = party_segment(opening)
    label, rule = code_party(seg)
    return {"appellant_type": label, "appellant_rule": rule, "appellant_segment": seg[:300]}
