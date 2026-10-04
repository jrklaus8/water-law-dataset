#!/usr/bin/env python3
"""DRAFT mapping of the free-text `study_design_class` labels in evidence_map.csv onto the documented 8-value enum.

The originals are NEVER modified. DATA_DICTIONARY.md records that the studies appraised with the project's own Legal Institutional Evidence Appraisal
Framework (or no tool) kept free-text design labels because their methods do not reduce to `doctrinal`/`jurimetric` without a false binary. This derives a
*proposal* for the researcher to accept, edit or reject (and, if the enum is to be extended, to see which labels would need a new value). Mechanical keyword
rules, all in this file, applied in this order:
  1. systematic/literature review or meta-analysis                      -> systematic_review_secondary
  2. natural experiment, difference-in-differences, counterfactual      -> quasi_experimental
  3. legal-only: an explicit doctrinal/statutory/legal-analysis/case-law cue and no field, survey or quantitative cue -> doctrinal
     (a bare 'legal' or 'institutional/legal case study' is NOT enough: those fall through to qualitative)
  4. quantitative cue AND qualitative cue                               -> mixed_methods
  5. quantitative cue only                                              -> observational
  6. qualitative cue only (interview, ethnography, fieldwork, case study, historical, documentary ...) -> qualitative
  7. otherwise (essay, theory, model, policy analysis with no method cue) -> unmapped_needs_review
Writes 05_analysis/descriptive/design_class_mapping_DRAFT_2026-10-04.csv (one row per free-text study) and DESIGN_CLASS_PROPOSAL_2026-10-04.md.
Run from the project root. No ground truth exists for these labels, so the proposal is not validated; it shows the scale and where judgement is needed."""
import csv
import re
import sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402

OUT_CSV = cf.ROOT / '05_analysis/descriptive/design_class_mapping_DRAFT_2026-10-04.csv'
OUT_MD = cf.ROOT / '05_analysis/descriptive/DESIGN_CLASS_PROPOSAL_2026-10-04.md'
ENUM = {'experimental', 'quasi_experimental', 'observational', 'qualitative', 'doctrinal', 'jurimetric', 'systematic_review_secondary', 'mixed_methods'}
SR = re.compile(r'systematic (literature )?review|meta-analysis|research synthesis|literature review', re.I)
QUASI = re.compile(r'natural[- ]experiment|difference-in-differences|counterfactual', re.I)
LEGAL = re.compile(r'doctrinal|statutory|legal[- ]text|legal[- ]policy analysis|legal analysis|legal/documentary analysis|legal/policy review|constitutional/legal-doctrinal|case[- ]law|legal-doctrinal|constitutional (analysis|review)', re.I)
FIELD = re.compile(r'interview|ethnograph|fieldwork|field study|survey|focus group|participant|observation', re.I)
QUANT = re.compile(r'econometric|quantitative|statistic|regression|decomposition|GIS|census|household survey|numerical|numbers|coverage data|administrative data|national coverage|modell?ing', re.I)
QUAL = re.compile(r'ethnograph|interview|qualitative|case[- ]study|case analysis|fieldwork|field research|participant|focus group|historical|archival|genealog|discourse|process[- ]tracing|political[- ]ecology|political[- ]economy|action[- ]research|documentary|documentation|institutional|comparative|narrative|anthropolog', re.I)
FIELDS = ['study_id', 'record_id', 'risk_of_bias_tool', 'free_text_label', 'proposed_class', 'rule']


def classify(label):
    if SR.search(label):
        return 'systematic_review_secondary', '1 review/synthesis'
    if QUASI.search(label):
        return 'quasi_experimental', '2 natural experiment / counterfactual'
    if re.search(r'mixed[- ]methods?', label, re.I):
        return 'mixed_methods', '3b label says mixed methods'
    legal, field, quant, qual = (bool(x.search(label)) for x in (LEGAL, FIELD, QUANT, QUAL))
    if legal and not field and not quant and 'qualitative' not in label.lower():
        return 'doctrinal', '3 explicit doctrinal cue, no field or quantitative cue'
    if quant and (qual or field):
        return 'mixed_methods', '4 quantitative and qualitative cues'
    if quant:
        return 'observational', '5 quantitative cue only'
    if qual or field:
        return 'qualitative', '6 qualitative cue only'
    return 'unmapped_needs_review', '7 no method cue'


def build():
    ed = {r['study_id']: r for r in cf.read('ed')}
    rows = []
    for r in cf.read('em'):
        lab = r['study_design_class']
        if lab in ENUM:
            continue
        cls, rule = classify(lab)
        e = ed[r['study_id']]
        rows.append({'study_id': r['study_id'], 'record_id': e['record_id'], 'risk_of_bias_tool': e['risk_of_bias_tool'][:40], 'free_text_label': lab, 'proposed_class': cls, 'rule': rule})
    rows.sort(key=lambda x: (x['proposed_class'], int(x['study_id'][1:])))
    return rows


def render(rows):
    n_all = len(cf.read('em'))
    c = Counter(r['proposed_class'] for r in rows)
    L = ['# Draft mapping of free-text study design labels to the 8-value enum', '',
         f"Generated by `code/analysis/propose_design_vocabulary.py`. {len(rows)} of {n_all:,} studies in `evidence_map.csv` carry a free-text `study_design_class` (the Legal Institutional Evidence Appraisal Framework and no-tool studies; see `DATA_DICTIONARY.md` and `study_design_class_normalization_2026-09-28.md`). "
         "This is a **proposal only**: nothing in `evidence_map.csv` changes, and the keyword rules have no ground truth.", '',
         "| Proposed class | Studies |", "|---|---|"]
    L += [f"| {k} | {v} |" for k, v in c.most_common()]
    L += ['', "How to read it: the enum has no value for what most of these studies are (institutional, historical, documentary or ethnographic case studies). The `qualitative` bucket therefore lumps together designs `RISK_OF_BIAS.md` section 2 treats as different; "
          "`doctrinal` catches only legal-only labels; `unmapped_needs_review` are essays, theory or models. If the researcher wants the field fully normalised, the choice is between (a) accept this mapping, (b) extend the enum with a value such as `qualitative_institutional_case_study`, or (c) leave the free text (current state). "
          "The rules are in the script's docstring; each row of the CSV names the rule that fired.", '',
          "## Rule hits", "", "| Rule | Studies |", "|---|---|"]
    L += [f"| {k} | {v} |" for k, v in sorted(Counter(r['rule'] for r in rows).items())]
    L += ['', "## Unmapped labels (need a human)", ""]
    L += [f"- {r['study_id']}: {r['free_text_label']}" for r in rows if r['proposed_class'] == 'unmapped_needs_review'] or ['(none)']
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    rows = build()
    with open(OUT_CSV, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n'); w.writeheader(); w.writerows(rows)
    OUT_MD.write_text(render(rows), encoding='utf-8')
    print(f'wrote {OUT_CSV.relative_to(cf.ROOT)} ({len(rows)} rows) and {OUT_MD.name}')
