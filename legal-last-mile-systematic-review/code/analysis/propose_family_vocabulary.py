#!/usr/bin/env python3
"""Controlled vocabulary for evidence_map.csv's `mechanism_family` and `outcome_family`. ADOPTED 2026-10-14 (open item A5).

The PI adopted the mapping this script derives. `evidence_map.csv` now carries the single-label family in both columns (9 mechanism families + `multiple`, 4 outcome families + `multiple`),
and the 5 studies the rules and the 2026-10-14 resolutions could not place keep `unmapped_needs_review`. The original free-text labels are preserved in
05_analysis/descriptive/evidence_map_original_labels_2026-10-14.csv (written by code/provenance/audit_and_repair/adopt_a5_a20_vocabularies_2026-10-14.py) and this script reads them from there, so the files
it writes stay reproducible. Resolutions of the rows the keyword rules could not place are in 05_analysis/descriptive/family_vocabulary_overrides_2026-10-14.csv (AI resolutions the PI can veto).
The files keep their 2026-09-28 names. Written files:
    05_analysis/descriptive/family_vocabulary_mapping_DRAFT_2026-09-28.csv   one row per study
    05_analysis/descriptive/FAMILY_VOCABULARY_PROPOSAL_2026-09-28.md          the vocabulary, rules, coverage and caveats

Run from the project root:  python3 code/analysis/propose_family_vocabulary.py   (rewrites both files; deterministic)

How the proposal is built (every rule is in this file, so it can be challenged):
  * MECHANISM — single-label column: keywords in the free-text `mechanism_family` label decide (one family -> that family; the
    label `MULTIPLE` or several families -> `multiple`); if the label is blank, the four TOP-LEVEL extraction booleans
    (eligibility, burden, discretion_accommodation, enforcement — the same ones build_evidence_map.py uses) decide; else
    `unmapped_needs_review`. Multi-label column `mechanism_families_all`: union of ALL extraction booleans (CODEBOOK section 4)
    and the label's families — a breadth measure, not a primary mechanism.
  * OUTCOME — each comma/`and`-separated token of the free-text label is mapped, by ordered keyword rules, to the four families
    already documented in DATA_DICTIONARY.md / PROJECT_SPEC.md section 7 (primary_connection, effective_access, economic_access,
    administrative_outcome). Several -> `multiple`; none -> `unmapped_needs_review`.
This is a mechanical, keyword-based draft, not a validated coding: a human must accept or edit it before it replaces anything.
"""
import csv, re, sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402

ROOT = cf.ROOT
OUT_CSV = ROOT / '05_analysis/descriptive/family_vocabulary_mapping_DRAFT_2026-09-28.csv'
OUT_MD = ROOT / '05_analysis/descriptive/FAMILY_VOCABULARY_PROPOSAL_2026-09-28.md'
OVERRIDES = ROOT / '05_analysis/descriptive/family_vocabulary_overrides_2026-10-14.csv'

MECH = {  # proposed family -> (definition, extraction booleans (CODEBOOK s.4), label keywords)
    'eligibility_status_documentation': ('Who qualifies: legal recognition, tenure/property status, required documents',
        ['eligibility', 'documentation', 'tenure', 'property'], ['eligib', 'legal_status', 'tenure', 'property', 'document', 'recogni', 'formal_connection', 'title', 'landlord', 'informal']),
    'procedural_burden': ('Cost of getting through the process: steps, delay, permits',
        ['burden', 'procedural_steps', 'delay', 'building_permit'], ['burden', 'procedur', 'delay', 'permit']),
    'fees_tariffs_subsidies': ('Money rules: connection fees, tariff design, subsidies, price regulation',
        ['fees'], ['fee', 'tariff', 'subsid', 'pricing', 'price']),
    'discretion_accommodation': ('Official discretion, hardship exceptions and accommodation',
        ['discretion_accommodation', 'discretion', 'hardship_exception'], ['discretion', 'accommodat', 'hardship', 'favour', 'favor', 'corrupt']),
    'enforcement_sanctions': ('Enforcement, disconnection, reconnection, sanctions',
        ['enforcement', 'disconnection', 'reconnection', 'sanction'], ['enforce', 'sanction', 'disconnect', 'reconnect', 'illegal', 'penal']),
    'review_redress': ('Administrative review, complaints, judicial review',
        ['administrative_review', 'complaint', 'judicial_review'], ['review', 'redress', 'complaint', 'judicial', 'court', 'litigat']),
    'institutional_structure_coordination': ('Fragmented or decentralised institutions, service-area and planning boundaries, political coordination',
        ['institutional_fragmentation', 'political_coordination', 'service_area', 'planning', 'zoning'], ['fragment', 'coordinat', 'boundary', 'decentrali', 'planning', 'zoning', 'service_area', 'jurisdiction']),
    'participation_assistance': ('Community participation and bureaucratic assistance to applicants',
        ['participation', 'bureaucratic_assistance'], ['particip', 'assistance', 'community']),
    'regulatory_model_ownership': ('Who owns/runs/regulates the service: regulatory model, ownership, concession, reform',
        [], ['regulatory', 'ownership', 'concession', 'ppp', 'private', 'public_private', 'governance', 'reform', 'regulator']),
}
OUT = {  # ordered: first matching rule wins for a token
    'administrative_outcome': ['administrative', 'approval', 'refusal', 'application_success', 'appeal', 'complaint', 'delay'],
    'primary_connection': ['primary', 'formal', 'connection'],
    'economic_access': ['economic', 'afford', 'cost', 'tariff', 'price', 'expenditure', 'burden'],
    'effective_access': ['effective', 'access', 'coverage', 'reliab', 'quantity', 'quality', 'continuity', 'service', 'water', 'sanitation'],
}
TOP_LEVEL = ['eligibility', 'burden', 'discretion_accommodation', 'enforcement']
BOOL_TO_FAMILY = {b: fam for fam, (_, bools, _) in MECH.items() for b in bools}
NEEDS = 'unmapped_needs_review'


def mech_from_label(label):
    l = label.lower()
    return {fam for fam, (_, _, kws) in MECH.items() if any(k in l for k in kws)}


def outcome_from_label(label):
    fams = set(); unmatched = []
    for tok in [t.strip().lower() for t in re.split(r'[,;]| and ', label) if t.strip()]:
        for fam, kws in OUT.items():
            if any(k in tok for k in kws):
                fams.add(fam); break
        else:
            unmatched.append(tok)
    return fams, unmatched


def overrides():
    """study_id -> {'mechanism_family', 'outcome_family', 'basis'} from the 2026-10-14 resolutions of the flagged rows (blank = no override of that field)."""
    if not OVERRIDES.exists():
        return {}
    with open(OVERRIDES, newline='', encoding='utf-8') as f:
        return {r['study_id']: r for r in csv.DictReader(f)}


CONTROLLED_MECH = set(MECH) | {'multiple', NEEDS}
CONTROLLED_OUT = set(OUT) | {'multiple', NEEDS}


def build():
    em = {r['study_id']: dict(r) for r in cf.read('em')}
    ed = {r['study_id']: r for r in cf.read('ed')}
    orig, ov = cf.original_labels(), overrides()
    for sid, r in em.items():  # the labels as they stood before adoption (a study added later has its current labels as originals)
        r.update({k: v for k, v in orig.get(sid, {}).items() if k in ('mechanism_family', 'outcome_family')})
    rows = []
    for sid in sorted(em, key=lambda s: int(s[1:])):
        e, x = em[sid], ed[sid]
        from_bool = {BOOL_TO_FAMILY[b] for b in BOOL_TO_FAMILY if x.get(b, '').strip().upper() == 'TRUE'}
        from_label = mech_from_label(e['mechanism_family']) if e['mechanism_family'].upper() not in ('MULTIPLE', '') else set()
        allm = from_bool | from_label
        lab = e['mechanism_family'].strip()
        top = {BOOL_TO_FAMILY[b] for b in TOP_LEVEL if x.get(b, '').strip().upper() == 'TRUE'}
        if lab.upper() == 'MULTIPLE':
            mech, basis = 'multiple', 'label says MULTIPLE'
        elif from_label:
            mech, basis = (next(iter(from_label)) if len(from_label) == 1 else 'multiple'), 'label keywords'
        elif not lab and top:
            mech, basis = (next(iter(top)) if len(top) == 1 else 'multiple'), 'top-level booleans (blank label)'
        else:
            mech, basis = NEEDS, 'none'
        if sid not in orig and lab in CONTROLLED_MECH:  # already a controlled value (a study added after the adoption)
            mech, basis = lab, 'already a controlled value'
        ofams, unm = outcome_from_label(e['outcome_family'])
        out = next(iter(ofams)) if len(ofams) == 1 else ('multiple' if ofams else NEEDS)
        if sid not in orig and e['outcome_family'].strip() in CONTROLLED_OUT:
            out, ofams, unm = e['outcome_family'].strip(), {e['outcome_family'].strip()} - {'multiple', NEEDS}, []
        o = ov.get(sid)
        if o and o['mechanism_family']:
            mech, basis = o['mechanism_family'], 'A5 resolution 2026-10-14: ' + o['basis']
        if o and o['outcome_family']:
            out, unm = o['outcome_family'], []
        rows.append({'study_id': sid, 'mechanism_family_original': e['mechanism_family'], 'mechanism_family_proposed': mech,
                     'mechanism_families_all': ';'.join(sorted(allm)), 'mechanism_basis': basis,
                     'outcome_family_original': e['outcome_family'], 'outcome_family_proposed': out,
                     'outcome_families_all': ';'.join(sorted(ofams)), 'outcome_tokens_unmatched': ';'.join(unm),
                     'needs_review': 'TRUE' if NEEDS in (mech, out) or unm else 'FALSE', 'resolution_2026-10-14': o['basis'] if o else ''})
    return rows


def render(rows):
    n = len(rows)
    om, oo = Counter(r['mechanism_family_original'] for r in rows), Counter(r['outcome_family_original'] for r in rows)
    pm, po = Counter(r['mechanism_family_proposed'] for r in rows), Counter(r['outcome_family_proposed'] for r in rows)
    allm = Counter(f for r in rows for f in r['mechanism_families_all'].split(';') if f)
    n_ov = sum(1 for r in rows if r['resolution_2026-10-14'])
    L = ["# Controlled vocabulary for `mechanism_family` and `outcome_family` (drafted 2026-09-28, adopted 2026-10-14)", "",
         "**Status: ADOPTED by the PI on 2026-10-14 (open item A5).** `evidence_map.csv` now carries the single-label family below in both columns; the original free-text labels are preserved in",
         "`evidence_map_original_labels_2026-10-14.csv`. Generated by `code/analysis/propose_family_vocabulary.py` (deterministic; every rule is in that file). The mapping is mechanical and",
         f"keyword-based, not a validated coding; the AI that produced the original labels also produced it, so a human should still spot-check a sample. {n_ov} rows the keyword rules could not place, or placed doubtfully, were resolved by the AI on 2026-10-14 in",
         "`family_vocabulary_overrides_2026-10-14.csv` (one-line basis each; the PI can veto any of them). The studies still `unmapped_needs_review` are the genuine edge cases listed at the end.", "",
         "## The problem", "",
         f"`mechanism_family` holds {len(om)} distinct labels and `outcome_family` {len(oo)} across {n:,} studies. The documented enum",
         "(`DATA_DICTIONARY.md`) has 5 and 4 values; in practice the fields mix the enum, upper- and lower-case variants, comma-separated",
         "lists and one-off free-text descriptions. Any tabulation by family is therefore unreliable as it stands.", "",
         "## Proposed vocabulary", "", "### Mechanism families (multi-label allowed)", "",
         "| Family | Meaning | Extraction booleans that map to it |", "|---|---|---|"]
    L += [f"| `{f}` | {d} | {', '.join('`'+b+'`' for b in bools) or '(label keywords only — no boolean exists)'} |" for f, (d, bools, _) in MECH.items()]
    L += ["", "Studies with more than one family are `multiple` in the single-label column and list every family in `mechanism_families_all`.", "",
          "### Outcome families", "",
          "The four already documented in `PROJECT_SPEC.md` §7 / `DATA_DICTIONARY.md`: `primary_connection` (formal connection),",
          "`effective_access` (quantity, reliability, continuity, quality, coverage, water/sanitation access), `economic_access`",
          "(cost, affordability, tariff burden) and `administrative_outcome` (approval, refusal, delay, appeal, complaint). Labels such as",
          "`water_access`, `sanitation_access`, `service_coverage`, `affordability` and `formal_connection` are treated as refinements",
          "and folded into these four; `PROJECT_SPEC.md` §7 warns not to pool them merely because they share the word \"access\".", "",
          "## Coverage of the draft", "",
          "| | Mechanism | Outcome |", "|---|---|---|",
          f"| Original distinct labels | {len(om)} | {len(oo)} |",
          f"| Proposed single-label values (incl. `multiple`, `{NEEDS}`) | {len(pm)} | {len(po)} |",
          f"| Studies mapped to exactly one family | {sum(v for k, v in pm.items() if k not in ('multiple', NEEDS)):,} | {sum(v for k, v in po.items() if k not in ('multiple', NEEDS)):,} |",
          f"| Studies mapped to `multiple` | {pm['multiple']:,} | {po['multiple']:,} |",
          f"| Studies `{NEEDS}` | {pm[NEEDS]:,} | {po[NEEDS]:,} |",
          f"| Studies flagged `needs_review` (either field, or an unmatched outcome token) | {sum(r['needs_review'] == 'TRUE' for r in rows):,} | |", "",
          "### Proposed mechanism value counts (single-label column)", "", "| Value | Studies |", "|---|---|"]
    L += [f"| `{k}` | {v:,} |" for k, v in cf.ranked(pm)]
    L += ["", "### Studies touching each mechanism family (multi-label)", "", "| Family | Studies |", "|---|---|"]
    L += [f"| `{k}` | {v:,} |" for k, v in cf.ranked(allm)]
    L += ["", "### Proposed outcome value counts", "", "| Value | Studies |", "|---|---|"]
    L += [f"| `{k}` | {v:,} |" for k, v in cf.ranked(po)]
    L += ["", "## Known weaknesses of this draft", "",
          "- Keyword rules can mis-assign a one-off label (e.g. a label containing \"community\" is sent to `participation_assistance`).",
          f"- `multiple` is large because {sum(1 for r in rows if r['mechanism_family_original'].strip().upper() == 'MULTIPLE'):,} studies already carry the label `MULTIPLE` (more than one of the four top-level booleans TRUE) and specific labels that name several families also land there; use `mechanism_families_all` for breadth.",
          "- The multi-label counts are broad because the extraction booleans are TRUE for most studies (e.g. institutional fragmentation for about three quarters); they show low discriminating power of the booleans — itself a finding for the taxonomy decision, not a clean count of \"studies about X\".",
          "- Extraction booleans are sparse-to-noisy (blank is not FALSE), so a study with few TRUE booleans may be under-labelled.",
          "- `effective_access` is broad by design (it absorbs coverage, reliability, quantity, quality, continuity); a finer split may be wanted.",
          "- No inter-rater check exists. The PI adopted the vocabulary on 2026-10-14 (`00_admin/DECISIONS_AND_OPEN_ITEMS.md` A5) knowing this.", "",
          "## Edge cases still `unmapped_needs_review`", "",
          "These studies' recorded mechanism is a broad determinant or an external macro-policy, not a legal or administrative rule that fits one of the nine families; they keep the value `unmapped_needs_review` rather than a forced label.", ""]
    L += [f"- {r['study_id']}: {r['mechanism_family_original'][:120]!r} (outcome: {r['outcome_family_proposed']})" for r in rows if r['mechanism_family_proposed'] == NEEDS] or ["(none)"]
    L += ["", "## How it was adopted", "",
          "`code/provenance/audit_and_repair/adopt_a5_a20_vocabularies_2026-10-14.py` saved the original labels, then wrote `mechanism_family_proposed` and `outcome_family_proposed` into `evidence_map.csv`. "
          "`family_vocabulary_mapping_DRAFT_2026-09-28.csv` (name kept) lists, per study, the original label, the adopted value, the multi-label breadth and the basis."]
    return "\n".join(L) + "\n"


if __name__ == '__main__':
    rows = build()
    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\r\n'); w.writeheader(); w.writerows(rows)
    OUT_MD.write_text(render(rows), encoding='utf-8')
    print(f'wrote {OUT_CSV.name} ({len(rows)} rows) and {OUT_MD.name}')
