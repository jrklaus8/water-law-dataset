#!/usr/bin/env python3
"""Generate 07_manuscript/draft/GENERATED_MANUSCRIPT_PIECES_2026-09-29.md: draft methods/AI-disclosure, PRISMA-flow and limitations text.

Every number comes from current_figures.compute() (the verifier-confirmed figures) or from the constants below, which
verify_repository.py checks against the README. No result is stated; no wording here has been reviewed by a human author.
Run from the project root:  python3 code/analysis/build_manuscript_pieces.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402

ROOT = cf.ROOT
OUT = ROOT / '07_manuscript/draft/GENERATED_MANUSCRIPT_PIECES_2026-09-29.md'
import json as _json  # noqa: E402


def reextraction_counts():
    """(re-extracted from full text in the 2026-10-04 campaigns, of which sparse-audit rows, with a recorded material correction) from the campaign JSONs."""
    ds = [_json.load(open(p, encoding='utf-8')) for p in sorted((ROOT / 'code/provenance/audit_and_repair/reextract_2026-10-04').glob('S*.json'))]
    return len(ds), sum(1 for d in ds if d.get('nonprefix')), sum(1 for d in ds if d.get('material_correction'))


def ai_provenance_clause():
    """Computed sentence: the AI models and tools, and the dates of use, exactly as the repository logs them (reviewer and researcher labels in the screening and extraction databases, plus the
    second-reviewer tools disclosure). No version string is added that the data do not carry: for most Claude decisions only the stage and the date are logged."""
    import re
    dt = lambda labels: sorted({m.group(0) for x in labels for m in [re.search(r'\d{4}-\d{2}-\d{2}', x)] if m})
    ta, ft, ed = cf.read('ta'), cf.read('ft'), cf.read('ed')
    ta_d = dt(r['reviewer_1'] for r in ta if r['reviewer_1'].startswith('Claude-AI-1stpass'))
    ft_d = dt(r['reviewer_1'] for r in ft if r['reviewer_1'].startswith('Claude-AI-fulltext'))
    ex_d = dt(r['researcher'] for r in ed)
    n_sn = sum(r['reviewer_1'] == 'claude_sonnet_5' for r in ft)
    n_lg = sum(r['reviewer_1'] in ('Claude', 'claude') for r in ft)
    sec = {}
    for r in ft:
        m = re.match(r'(Codex|Gemini)-(.+)-reviewer2-fulltext-(\d{4}-\d{2}-\d{2})$', r['reviewer_2'])
        if m:
            sec.setdefault(m.group(1), (set(), set()))
            sec[m.group(1)][0].add(m.group(2))
            sec[m.group(1)][1].add(m.group(3))
    disc = (ROOT / '_reviewer2_codex/AI_USE_AND_TOOLS_DISCLOSURE.md').read_text(encoding='utf-8')
    assert set(sec) == {'Codex', 'Gemini'} and 'codex-cli` 0.160.0' in disc and 'Claude Sonnet 5' in disc and 'gemini-2.5-flash' in disc, 'second-reviewer provenance changed: update ai_provenance_clause'
    cx, gm = sorted(sec['Codex'][0]), sorted(sec['Gemini'][0])
    return (f"Model and tool provenance, as logged in the repository: Claude (Anthropic) made the title/abstract first-pass decisions (labels `Claude-AI-1stpass-{ta_d[0]}` and `-{ta_d[-1]}`), "
            f"the full-text decisions (labels `Claude-AI-fulltext-{ft_d[0]}` to `Claude-AI-fulltext-{ft_d[-1]}`, plus {n_sn} early rows labelled `claude_sonnet_5` and {n_lg} legacy rows labelled `Claude` or `claude`) "
            f"and the extraction and appraisal records (labels dated {ex_d[0]} to {ex_d[-1]}). The repository records a Claude model version only as the label `claude_sonnet_5` on those {n_sn} rows and as \"Claude Sonnet 5\" "
            "in the second-reviewer tools disclosure for 2026-10-03 and 2026-10-04; for the other decisions only the stage and the date are logged, so the exact Claude model version behind them is not recorded. "
            f"The blind second reviewers (full-text re-screening, {min(sec['Codex'][1] | sec['Gemini'][1])} to {max(sec['Codex'][1] | sec['Gemini'][1])}) were OpenAI Codex CLI 0.160.0 with model `{cx[0]}` (reasoning effort high) "
            f"and Google Gemini CLI with model `{gm[0]}` (`gemini-2.5-flash` was tried first and dropped when its daily quota ran out); their labels are in `reviewer_2` of the full-text database "
            "and the tools are described in `_reviewer2_codex/AI_USE_AND_TOOLS_DISCLOSURE.md`.")


def human_verification(F):
    """Computed human-verification figures for the prose (current_figures keys): confirmed includes, further rows ruled on by the PI under reviewer CK, their split, the total and its share of the decided rows."""
    conf, adj = F['reviewer_2_confirmed_includes'], F['human_adjudicated_rows']
    tot, dec = F['human_verified_rows'], F['full_text_decided']
    return {'conf': conf, 'retired': 200 - conf, 'adj': adj, 'adj_exc': F['human_adjudicated_excludes'], 'adj_inc': F['human_adjudicated_includes'], 'tot': tot, 'dec': dec, 'pct': 100 * tot / dec}


def human_verification_clause(F):
    """The sentence of the Abstract that reports how much of the full-text screening a human has verified."""
    h = human_verification(F)
    return (f"The author independently confirmed {h['conf']} chronological full-text inclusions (S001–S200 net of {h['retired']} later retirements) and adjudicated a further {h['adj']} full-text records ({h['adj_exc']} exclusions, {h['adj_inc']} inclusions) "
            f"in the scope, consistency and audit passes and the rulings on the SWiM core (A6, A16, A19, A22–A26, A28), so {h['tot']:,} of the {h['dec']:,} full-text decisions ({h['pct']:.1f}%) carry human verification or adjudication; no extracted value has been independently verified.")


def swim_family_counts():
    """Per family, how many studies carry each raw sign and each substantive direction, from SWIM_DIRECTION_CODING_2026-10-14.csv: {'A': {'k': 13, 'raw': Counter, 'sub': Counter}, ...}."""
    import csv as _csv
    from collections import Counter as _C
    out = {f: {'k': 0, 'raw': _C(), 'sub': _C()} for f in 'ABC'}
    with open(cf.ROOT / '05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv', newline='', encoding='utf-8') as fh:
        for r in _csv.DictReader(fh):
            o = out[r['family']]
            o['k'] += 1
            o['raw'][r['raw_coefficient_sign']] += 1
            o['sub'][r['substantive_direction']] += 1
    return out


def swim_core_clause(F):
    """Computed sentence: how much of the SWiM core the author has verified (inclusion decision, direction codings), how much is AI-checked only, and what is flagged and still open."""
    n, hv, ai, ck, fl = F['swim_core_studies'], F['swim_core_inclusion_human_verified'], F['swim_core_ai_checked_not_human'], F['swim_core_direction_ck_confirmed'], F['swim_core_flagged_for_author']
    other = n - hv - ai
    return (f"Of the {n} studies in the three SWiM families, {hv} ({100 * hv / n:.0f}%) carry a recorded human verification of the inclusion decision (the author's own confirmations and rulings, among them the rulings of 2026-10-14 in which the author read the verbatim passages of the papers); "
            f"{ai} ({100 * ai / n:.0f}%) were checked only by the AI against the narrow reading of criteria 2 and 4 and are recorded as AI-checked, not as human confirmations, until the author reviews the source passages (a source-verification dossier has been prepared for that review)"
            + (f"; {other} have neither" if other else "") + f". The author has confirmed the two-column direction coding (raw sign and substantive direction) for {ck} of the {n}"
            + (f", and {fl} are flagged and await a ruling" if fl else "") + ". The effect estimates themselves were extracted and checked against the full texts by the AI, not by a human.")


def geography_framing(F):
    """Computed standalone wording for what the geographic distribution shows (replaces the earlier references to the dissertation's comparison countries). Returns the full paragraph (for the gaps section),
    a one-sentence discussion point and a short summary, all from the extraction database: the four commonest middle-income countries, the United States, Canada (and how many of its studies concern First Nations or other
    Indigenous communities) and the Netherlands. The claim about under-examined mechanisms is worded as a statement about the evidence this review identified, because a review can speak only for the evidence it found;
    municipal discretion is deliberately not in the list of under-examined mechanisms, since it is the second most frequently coded mechanism in the whole corpus."""
    import re as _re
    ed = cf.read('ed')
    T_ = lambda v: str(v).strip().upper() == 'TRUE'
    one = lambda name: sum(1 for r in ed if r['country'].strip() == name)
    four = [r for r in ed if r['country'].strip() in ('India', 'Brazil', 'South Africa', 'Ghana')]
    fc, el = sum(T_(r['formal_connection']) for r in four), sum(T_(r['eligibility']) for r in four)
    canada = [r for r in ed if r['country'].strip() == 'Canada']
    fn = sum(bool(_re.search(r'first nation|indigenous|aboriginal|inuit|m[eé]tis', ' '.join([r['citation'], r.get('population', ''), r.get('subnational_unit', ''), r.get('extraction_note', '')]), _re.I)) for r in canada)
    c = {k: one(k) for k in ('India', 'Brazil', 'South Africa', 'Ghana', 'United States', 'Canada', 'Netherlands')}
    full = (f"Empirical research on the legal last mile is heavily concentrated in middle-income urbanising jurisdictions (India {c['India']}, Brazil {c['Brazil']}, South Africa {c['South Africa']}, Ghana {c['Ghana']}) and the United States ({c['United States']}), "
            f"where last-mile exclusion is studied primarily at the informal-settlement tenure, municipal incorporation and utility-connection boundary: in the four middle-income countries, {fc} of {len(four)} studies ({100 * fc / len(four):.0f}%) code a formal-connection outcome and {el} ({100 * el / len(four):.0f}%) an eligibility mechanism. "
            f"By contrast, high-coverage welfare states with near-universal physical networks are sparsely represented (for example, {c['Canada']} single-country studies in Canada, {fn} of them concerning the drinking water of First Nations and other Indigenous communities (advisories, infrastructure, regulation and jurisdictional gaps), "
            f"and {c['Netherlands']} in the Netherlands), leaving administrative exclusion mechanisms within universal-network systems, such as tariff hardship exemptions, tenant billing rules and administrative redress, comparatively under-examined in the evidence this review identified.")
    point = (f"**The evidence is concentrated where networks are incomplete and thin where they are near-universal.** Middle-income urbanising countries and the United States dominate, and high-coverage welfare states are represented by few studies ({c['Canada']} single-country studies in Canada, mostly on First Nations drinking water, and {c['Netherlands']} in the Netherlands), "
             "so how administrative exclusion operates inside universal-network systems (tariff hardship exemptions, tenant billing rules, administrative redress) cannot be assessed from this evidence base.")
    short = (f"high-coverage welfare states with near-universal networks are sparsely represented ({c['Canada']} single-country studies in Canada, {fn} of them on First Nations and other Indigenous communities' drinking water, and {c['Netherlands']} in the Netherlands), "
             "so administrative exclusion within universal-network systems is comparatively under-examined in this evidence base.")
    return {'full': full, 'point': point, 'short': short, 'canada': c['Canada'], 'canada_fn': fn, 'netherlands': c['Netherlands'], 'four_n': len(four), 'four_formal': fc, 'four_elig': el}


def family_fit_clause():
    """Computed sentence: how many family-assigned effect-size rows sit outside their family's own wording (keyword audit, audit_effect_size_families.py)."""
    import audit_effect_size_families as _aef
    rows = _aef.build()
    out = sum(1 for r in rows if r['fit'].startswith('outside'))
    return (f"The family assignments were made by judgement and organise the write-up only: on a keyword reading of the exposure definitions, {out} of {len(rows)} family-assigned rows "
            "sit outside the wording of the family they were placed in (`05_analysis/effect_sizes/FAMILY_FIT_AUDIT_2026-10-04.md`), so the families are loose groupings, not tests of the specified constructs. "
            "Families A, B and C are therefore reported as thematic mechanism groupings used to organise structured vote counting (SWiM), not as homogeneous exposure–outcome pairs, and their headings describe the clusters actually synthesised "
            "(legal status, tenure, recognition and governance arrangements; assistance, participation, trust and external support; ownership, regulation, institutional capacity and administrative structure), which is also why pooling was rejected.")


def reviewer2_ai_counts():
    """(AI full-text excludes re-read blind by the non-Claude models, of which judged include, records reviewed in all) from the reviewer-2 queue file; AI-versus-AI, not human."""
    import csv as _csv
    rows = list(_csv.DictReader(open(sorted((ROOT / '_reviewer2_codex').glob('full_text_reviewer_2_FILLED_*.csv'))[-1], encoding='utf-8', newline='')))  # newest dated pass
    ex = [r for r in rows if r['ai_decision'] == 'exclude']
    return len(ex), sum(1 for r in ex if r['reviewer_2_decision (include/exclude/cannot_tell)'] == 'include'), len(rows)



def _a16_inc():
    import build_a16_adjudication_sheet as _baa
    return _baa.includes_side()


def _a16_outcome():
    import build_a16_adjudication_sheet as _baa
    return _baa.adjudication_outcome()


def _a16_total():
    import build_a16_adjudication_sheet as _baa
    return _baa.implied_total()

RAW, UNIQUE, TA_SCREENED, TA_NO_ABSTRACT, TA_HUMAN_PASS = 34594, 27481, 26222, 1259, 3665  # README "Chronological workflow"; verifier-checked
SEARCH_CLOSED = '2026-09-11'


def build():
    F = cf.compute()
    A16 = _a16_outcome()
    n = F['extraction_rows']
    tools = F['tools']
    fam = F['effect_size_by_family']
    inc, exc, und, rec = F['full_text_include'], F['full_text_exclude'], F['full_text_undecided'], F['full_text_records']
    dec = F['full_text_decided']
    e10 = F['exclusion_by_code'].get('E10', 0)
    n_rated_am = sum(1 for r in cf.read('ed') if cf.tool_of(r['risk_of_bias_tool']) == 'AMSTAR 2' and not r['risk_of_bias_rating'].startswith('Not ratable'))
    n_cl_am = sum(1 for r in cf.read('ed') if cf.tool_of(r['risk_of_bias_tool']) == 'AMSTAR 2' and r['risk_of_bias_rating'].startswith('Critically Low'))
    am_clause = 'all Critically Low' if n_cl_am == n_rated_am else f'{n_cl_am} Critically Low and {n_rated_am - n_cl_am} Low'  # was hard-coded "all Critically Low" and went stale when S327 was rated Low
    L = ["# Generated manuscript pieces — DRAFT (2026-09-29)", "",
         "> Auto-generated by `code/analysis/build_manuscript_pieces.py` from the verifier-confirmed figures (`00_admin/CURRENT_FIGURES.md`). Text is a starting point for the human authors, not reviewed prose. Bracketed items [ ] need the author's input. Regenerate after any data change.", "",
         "## 1. Methods — AI-assisted conduct and disclosure", "",
         "This is an AI-assisted systematic review. A large language model (Claude, Anthropic) performed most of the title/abstract first-pass screening, full-text screening, data extraction, risk-of-bias appraisal and synthesis drafting, under the direction of the human researcher, who defined the question, protocol and eligibility criteria, ran the database searches, supplied the full texts and made the closing and scoping decisions. "
         f"Independent human verification was partial: a human second reviewer covered the {TA_HUMAN_PASS:,} title/abstract records the AI marked include or unsure (not the AI's exclusions), and confirmed {F['reviewer_2_confirmed_includes']} of the {inc:,} full-text includes; no extracted value or risk-of-bias rating has been independently verified against source papers, and the researcher adjudicated {F['human_adjudicated_rows']} further full-text decisions ({F['human_adjudicated_excludes']} exclusions, {F['human_adjudicated_includes']} inclusions; open items A16, A19, A22 to A25 and A6), so {F['human_verified_rows']:,} of the {F['full_text_decided']:,} full-text decisions ({100 * F['human_verified_rows'] / F['full_text_decided']:.1f}%) carry human verification or adjudication, but the remaining AI full-text decisions have not been checked by a human. " +
         ai_provenance_clause() + " The stage-by-stage division of labour is tabulated in `AI_USE_STATEMENT.md`.", "",
         "The review was conducted according to a written protocol (`PROTOCOL.md`) [registration: retrospective OSF registration frozen at release 0.2.0-interim, 2026-10-14; add the identifier once submitted]. Searches closed on " + SEARCH_CLOSED + f" and identified {RAW:,} records ({UNIQUE:,} after deduplication). Risk of bias was assessed with the instrument matching each study's design — RoB 2 (cluster variant) {tools['RoB 2']}, ROBINS-I {tools['ROBINS-I']}, JBI cross-sectional {tools['JBI Cross-Sectional']}, MMAT {tools['MMAT']}, CASP qualitative {tools['CASP Qualitative']}, AMSTAR 2 {tools['AMSTAR 2']} — and, for {tools['Legal Framework']} studies for which no published instrument fits, this project's own non-validated Legal Institutional Evidence Appraisal Framework; {('no study was judged not appraisable' if not tools.get('NONE', 0) else str(tools.get('NONE', 0)) + ' studies were judged not appraisable')}. "
         "Ratings were assigned by rule from the extracted fields rather than by signalling-question reading of each paper. "
         f"Synthesis followed SWiM guidance without meta-analysis: {F['effect_size_rows']} effect-size rows (Family A {fam['A']}, B {fam['B']}, C {fam['C']}, {fam['(none: reasoned non-fit)']} reasoned non-fits) were compiled and none was pooled. " + family_fit_clause(), "",
         "## 2. Results — PRISMA flow paragraph", "",
         f"The database and grey-literature searches identified {RAW:,} records; {UNIQUE:,} remained after deduplication. {TA_SCREENED:,} had an abstract and were screened at title/abstract level ({TA_NO_ABSTRACT:,} without an abstract were not decided); {F['title_abstract_include']:,} were retained for full-text assessment. "
         f"Full-text retrieval was closed by the researcher's decision: {dec:,} of {rec:,} records were assessed and {und:,} were never assessed ({F['unretrieved_not_retrievable']:,} not retrievable, {F['unretrieved_wrong_file']} for which the wrong file was obtained). "
         f"Of the {dec:,} assessed, {exc:,} were excluded ({e10} because the full text was inaccessible; reasons for the others are in `exclusion_log.csv`) and {inc:,} were included ({n:,} extraction rows, one per included report). The {n:,} reports describe {F['distinct_studies_definite_links']:,} distinct studies on the two definite same-data links (S294/S366, S097/S098) and {F['distinct_studies_incl_partial_links']:,} counting the two partial-overlap links (S681/S682, S357/S369). No pair was collapsed, because companion reports carry distinct outcome-specific extractions and risk-of-bias ratings; the five RoB 2 report rows are four distinct cluster-randomised trials, and S526/S539 are flagged for verification of sample overlap before any future pooling.", "",
         "## 3. Limitations (draft)", "",
         f"- **Incomplete full-text screening.** {und:,} of {rec:,} records ({100 * und / rec:.1f}%) were not assessed, and those not assessed are older on average; the review is not exhaustive and may under-represent earlier literature.",
         f"- **AI-conducted judgments with partial verification.** Screening decisions, extraction, appraisal and coding of direction of association were made by the same AI system. The author confirmed {F['reviewer_2_confirmed_includes']} full-text includes (S001–S200) and adjudicated {F['human_adjudicated_rows']} further full-text decisions, so {F['human_verified_rows']:,} of the {F['full_text_decided']:,} decisions ({100 * F['human_verified_rows'] / F['full_text_decided']:.1f}%) carry human verification or adjudication ({F['reviewer_2_confirmed_includes'] + F['human_adjudicated_includes']} includes and {F['human_adjudicated_excludes']} excludes); {F['decided_blank_reviewer_1'] + F['decided_inferred_reviewer_1']} decided rows had no reviewer recorded at the time (the label was inferred afterwards, and the author has since ruled on all of them), and the title/abstract exclusions were not human-checked. "
         + swim_core_clause(F) + " "
         f"A blind re-read of {A16['reread_excludes']} full-text exclusions with an available PDF ({A16['sample']} of them a random sample stratified by exclusion code) by two non-Claude models (Codex, Gemini) flagged {A16['flagged']}; the author adjudicated all {A16['flagged']}, confirming {A16['upheld']} exclusions and reversing {A16['reversed']} to inclusion ({', '.join(A16['reversed_ids'])}). That is {A16['reversed_in_sample']} of the {A16['sample']} sampled exclusions ({100 * A16['rate']:.1f}%; 95% Wilson interval {100 * A16['rate_lo']:.1f}–{100 * A16['rate_hi']:.1f}%), or about {A16['scaled']} of the {A16['pool']:,} content-based exclusions if the rate held (interval {A16['scaled_lo']}–{A16['scaled_hi']}; about {A16['scaled_by_code']} when scaled within exclusion code). It counts only the exclusions the models flagged and rests on the narrow reading of eligibility criterion 2 adopted after the disagreement was seen, so it is an estimate and not a verified count; it replaces an earlier unadjudicated extrapolation that took the models' verdicts at face value.",
         f"- **Thin extraction for some studies.** {F['abstract_only_extractions']} studies were extracted from abstract or metadata only; there was no second extractor. The AI re-read {reextraction_counts()[0]} studies from full texts after the first extraction (an AI check of AI work, not independent verification); in {reextraction_counts()[2]} of the {reextraction_counts()[1]} sparse-audit rows among them the abstract-level extraction was materially wrong or incomplete (`CAMPAIGN_NOTES.md`).",
         f"- **Appraisal validity.** Ratings are rule-based; {tools['Legal Framework']} studies were appraised with a non-validated project instrument; {F['jbi_high_concern']} of {tools['JBI Cross-Sectional']} JBI ratings are 'high concern' largely reflecting sparse extraction; {('all ' + str(tools['AMSTAR 2']) + ' AMSTAR 2 reviews received a confidence rating') if n_rated_am == tools['AMSTAR 2'] else ('only ' + str(n_rated_am) + ' of ' + str(tools['AMSTAR 2']) + ' AMSTAR 2 reviews could be given a confidence rating')} ({am_clause}).",
         f"- **No pooled estimate.** Direction-of-association syntheses rest on {F['effect_size_rows']} effect-size rows and are neither effect estimates nor certainty-graded (GRADE).",
         "- **Classifications.** Mechanism, outcome and study-design labels were mapped to controlled vocabularies by keyword rules on 2026-10-14 (original labels preserved); the mapping is mechanical and unvalidated, and country and legal-system fields remain free text.",
        f"- **A post-hoc scope reading.** Eligibility criterion 2 was applied under a narrow, rule-type reading adopted on 2026-10-13, after an AI-versus-AI disagreement about the exclusions had been seen. The adjudication and consistency passes that followed moved {A16['moved_to_exclusion']} included reports to the exclusions (the {A16['p4_flagged']} inclusions that the models had also questioned, all excluded by the author, and {A16['moved_to_exclusion_after_p4']} others) and {A16['moved_to_inclusion']} exclusions to the inclusions. It is a post-hoc clarification, not an a priori rule; the wording of the criterion is unchanged, and a different reading would change the included set (`INCLUSION_EXCLUSION.md`, `CHANGELOG.md`).",
        f"- **Counts are of reports.** The {n:,} included items are reports: they describe {F['distinct_studies_definite_links']:,} distinct studies on the definite same-data links ({F['distinct_studies_incl_partial_links']:,} counting the partial overlaps), the five RoB 2 report rows are four trials, and S526 and S539 (two US utility studies) are flagged for verification of sample overlap before any pooling.",
         "- **Search scope.** SSRN and Westlaw/Lexis were not searched (`README.md`, Known limitations).", "",
         "*Source of every figure: `00_admin/CURRENT_FIGURES.md`; checked by `python3 code/analysis/verify_repository.py`.*"]
    return "\n".join(L) + "\n"


if __name__ == '__main__':
    OUT.write_text(build(), encoding='utf-8')
    print('wrote', OUT.relative_to(ROOT))
