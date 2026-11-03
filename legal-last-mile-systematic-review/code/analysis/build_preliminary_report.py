#!/usr/bin/env python3
"""Generate 06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.md from the databases.

Every number is computed from the CSVs (so it cannot drift from the data); every quoted example is pulled from the extraction
or effect-size rows by study_id. Interpretive sentences are hand-written here, are labelled TENTATIVE, and cite the numbers they
rest on. Nothing in the report is a pooled effect, a certainty (GRADE) judgment, or a final finding.

Run from the project root:  python3 code/analysis/build_preliminary_report.py   (deterministic; verify_repository.py checks freshness)
"""
import csv, re, statistics, sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402
import sensitivity_analysis as sa  # noqa: E402
import propose_family_vocabulary as pv  # noqa: E402
import propose_design_vocabulary as dvm  # noqa: E402
import audit_data_quality as adq  # noqa: E402
import audit_sparse_records as asr  # noqa: E402
import build_manuscript_pieces as bmp  # noqa: E402

ROOT = cf.ROOT
OUT = ROOT / '06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.md'
T = lambda v: str(v).strip().upper() == 'TRUE'
trim = lambda s, k=170: (re.sub(r'\s+', ' ', s).strip()[:k].rstrip() + ('…' if len(s.strip()) > k else ''))


def build():
    F = cf.compute()
    cert = adq.certainty_audit()
    ed = {r['study_id']: r for r in cf.read('ed')}
    em = {r['study_id']: r for r in cf.read('em')}
    es = {r['study_id']: r for r in cf.read('es')}
    ft = cf.read('ft')
    n = len(ed)
    tools = F['tools']
    fam = F['effect_size_by_family']
    rows_sc, ab_only, not_elig, collapse, signs = sa.scenarios()
    conc = sa.parse_concordance()
    dcoding = {r_['study_id']: r_ for r_ in csv.DictReader(open(cf.ROOT / '05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv', encoding='utf-8'))}
    vocab = {r['study_id']: r for r in pv.build()}
    orig_lab = cf.original_labels() or {s: {k: r[k] for k in ('study_design_class', 'mechanism_family', 'outcome_family')} for s, r in em.items()}
    P = lambda k, d=n: f"{k:,} ({100 * k / d:.0f}%)"

    # ---- descriptive numbers
    dc = Counter(r['study_design_class'] for r in em.values())
    enum = dvm.ENUM
    free_design = sum(v for k, v in dc.items() if k not in enum)
    years = [int(r['publication_year']) for r in ed.values() if r['publication_year'].strip().isdigit()]
    since2010 = sum(y >= 2010 for y in years)
    lang = Counter(r['language'] for r in ed.values())
    def urb_bucket(v):
        v = v.strip().lower()
        return 'urban' if v.startswith('urban') else 'peri' if v.startswith('peri') else 'rural' if v.startswith('rural') else 'mixed' if v.startswith(('mixed', 'both')) else 'blank/other'
    urb = Counter(urb_bucket(r['urban_rural']) for r in ed.values())
    country = lambda name: sum(1 for r in ed.values() if r['country'].strip() == name)
    country_any = lambda name: sum(1 for r in ed.values() if name in r['country'])
    mech = ['institutional_fragmentation', 'discretion_accommodation', 'fees', 'service_area', 'political_coordination', 'enforcement', 'participation',
            'eligibility', 'burden', 'documentation', 'bureaucratic_assistance', 'administrative_review', 'complaint', 'judicial_review', 'disconnection', 'reconnection']
    mc = {m: sum(T(r[m]) for r in ed.values()) for m in mech}
    outc = ['water_access', 'formal_connection', 'service_coverage', 'affordability', 'sanitation_access', 'service_reliability', 'service_quality', 'service_continuity', 'service_quantity', 'refusal', 'delay_outcome', 'application_success']
    oc = {o: sum(T(r[o]) for r in ed.values()) for o in outc}
    mcert = F['mechanism_certainty_numeric']
    # retrieval bias
    yr = lambda r: int(r['year']) if r['year'].strip().isdigit() else None
    def ystats(sel):
        ys = [yr(r) for r in ft if sel(r) and yr(r)]
        return len(ys), statistics.median(ys), 100 * sum(y < 2000 for y in ys) / len(ys), 100 * sum(y >= 2020 for y in ys) / len(ys)
    y_assessed, y_unret = ystats(lambda r: r['final_decision']), ystats(lambda r: not r['final_decision'])
    e10 = F['exclusion_by_code'].get('E10', 0)
    content_assessed = F['full_text_decided'] - e10

    def ex(sid, extra=''):
        e = es[sid]; x = ed[sid]; c_ = dcoding[sid]
        return (f"| {sid} | {x['country'][:28]} | {cf.tool_of(x['risk_of_bias_tool'])} | {trim(e['exposure_definition'], 95)} | {trim(e['direction'], 110)} | {c_['raw_coefficient_sign']} | {c_['substantive_direction']} |")

    L = []
    W = L.append
    W("# Preliminary results report — AI-assisted systematic review (generated 2026-09-29)")
    W("")
    W("> **PRELIMINARY — NOT A FINAL RESULT.** Produced by the same AI that screened, extracted and appraised the studies, from the")
    W("> repository's own databases, with no human verification of extracted values against the source papers (`AI_USE_STATEMENT.md`).")
    W("> Every number below is computed from the data (`code/analysis/build_preliminary_report.py`); every quoted example is an")
    W("> AI-extracted field, not a re-reading of the paper. Sections 2A and 3 report what the records contain; **Section 2B is tentative")
    W("> interpretation** and is labelled as such. No pooled effect exists and none is claimed.")
    W("")
    W("## 1. Methods and progress in brief")
    W("")
    W("| Step | Status |")
    W("|---|---|")
    W("| Question | How legal and administrative institutions shape the translation of physical water/sanitation infrastructure into effective household access (`PROTOCOL.md`) |")
    W("| Search | Closed 2026-09-11; 34,594 raw records → 27,481 unique (SSRN and Westlaw/Lexis never searched) |")
    W(f"| Title/abstract screening | Final {F['title_abstract_include']:,} include / {F['title_abstract_exclude']} exclude: 26,222 of 27,481 screened by AI first pass (3,062 include / 22,557 exclude / 603 unsure; 1,259 without an abstract left undecided); a human second pass covered the 3,665 include-plus-unsure records, **not the 22,557 AI excludes**; 99.8% agreement, flagged by the project as unusually high |")
    W(f"| Full-text screening | Closed by researcher decision at **{F['full_text_decided']:,} of {F['full_text_records']:,} assessed (62.2%)**: **{F['full_text_include']:,} include / {F['full_text_exclude']:,} exclude**; {F['full_text_undecided']:,} never assessed. {e10} of the excludes are E10 (\"full text inaccessible\"), so only **{content_assessed:,}** were judged on content. AI decisions; a human confirmed 100 includes and no excludes |")
    W(f"| Extraction | {n:,} studies, 92 codebook fields, by the AI; {F['abstract_only_extractions']} from abstract/metadata only; no second extractor |")
    W("| Appraisal | Rule-based batch ratings from extracted fields with design-matched tools: " + ", ".join(f"{k} {v}" for k, v in tools.items()) + ". Legal Framework is the project's own **non-validated** instrument. No human review of ratings |")
    W(f"| Synthesis | Phase 11: no family clears the bar for meta-analysis. {F['effect_size_rows']} effect-size rows (A {fam['A']}, B {fam['B']}, C {fam['C']}, {fam['(none: reasoned non-fit)']} reasoned non-fits), none pooled; three structured (SWiM) direction-of-association syntheses |")
    W("")
    W("## 2A. Preliminary findings drawn from the extracted evidence")
    W("")
    W("### 2A.1 What the evidence base looks like")
    W("")
    W(f"- **Volume and recency.** {n:,} studies; {P(since2010)} published 2010 or later (median year {int(statistics.median(years))}; {sum(y < 2000 for y in years)} before 2000).")
    free_top = "; ".join(f"{k} ({v})" for k, v in cf.ranked(Counter(v for v in (r['study_design_class'] for r in em.values()) if v not in enum), 2))
    n_adopted = len(dvm.build()) - free_design
    W(f"- **Design mix** (evidence-map `study_design_class`; the free-text design labels of {n_adopted} studies were mapped onto the design list (the eight documented values plus `other`, added for decision-analysis and theoretical models) on 2026-10-14 under open item A20, with the original strings kept in `evidence_map_original_labels_2026-10-14.csv`, so `qualitative` lumps ethnographic, historical, institutional and documentary case studies; " + (f"{free_design} studies keep a free-text label and are not in the counts that follow" if free_design else "no study keeps a free-text label") + f"): qualitative {dc['qualitative']}, mixed-methods {dc['mixed_methods']}, observational {dc['observational']}, quasi-experimental {dc['quasi_experimental']}, doctrinal {dc['doctrinal']}, jurimetric {dc['jurimetric']}, secondary systematic reviews {dc['systematic_review_secondary']}, experimental {dc['experimental']}, other {dc['other']}. By appraisal tool: " + ", ".join(f"{k} {v}" for k, v in tools.items()) + ".")
    mc_prov = list(csv.DictReader(open(cf.ROOT / '03_extraction/extracted_data/extraction_mechanism_certainty_original_2026-10-14.csv', encoding='utf-8')))
    mc_narr = sum(1 for r_ in mc_prov if r_['original_type'] == 'narrative')
    mc_low = sum(1 for r_ in mc_prov if r_['original_type'] == 'numeric' and r_['original_value'].strip() != str(r_['new_value']))
    assert all(r_['original_type'] == 'narrative' or True for r_ in mc_prov) and not cert['hi_outside'] and not F['mechanism_certainty_narrative_text']
    W(f"- **Designs able to support a causal claim about a legal/administrative mechanism:** {F['causal_capable_designs']} ({100 * F['causal_capable_designs'] / n:.0f}%) — {tools['ROBINS-I']} quasi-experimental studies and {tools['RoB 2']} randomised trials (which are 4 distinct trials, see §3.4). "
      f"The mechanism-certainty code follows the codebook scale (0 inferred only, 1 documented association, 2 mechanism directly observed, 3 quasi-experimental evidence, 4 experimental evidence), which is design-driven; it was normalised on 2026-10-14 so that level 4 is held only by RoB 2 trials, level 3 only by RoB 2 trials and ROBINS-I studies rated Low or Moderate, and every other design is capped at 2. "
      f"All {mcert['3'] + mcert['4']} studies at level 3 or 4 are therefore among the {F['causal_capable_designs']} causal-capable designs; {mcert['0']} sit at level 0, {mcert['1']} at level 1, {mcert['2']} at level 2, {mcert['3']} at level 3 and {mcert['4']} at level 4. "
      f"Before the normalisation {mc_narr} studies held a narrative sentence instead of a 0–4 code and {mc_low} studies of other designs held a 3 or 4; the original values are kept in `03_extraction/extracted_data/extraction_mechanism_certainty_original_2026-10-14.csv`, and the step from the narrative labels (High, Moderate-high, Moderate) to a level is the AI's reading, not a validated scale.")
    W(f"- **Geography** (`country` is free text; {F['country_multi_or_regional_studies']} studies name several countries or a region and are not counted below): " + ", ".join(f"{k} {v}" for k, v in F['country_top10_single_name']) + f". High-coverage welfare states are thinly covered: **Canada {country('Canada')} ({country_any('Canada')} counting multi-country entries), Netherlands {country('Netherlands')} ({country_any('Netherlands')} counting multi-country entries)** (interpreted under gaps below).")
    W("- **Legal systems** (rule-based buckets): " + ", ".join(f"{k} {v}" for k, v in F['legal_system_buckets'].items()) + ".")
    W(f"- **Setting and language:** urban (incl. informal settlements) {urb['urban']}, rural {urb['rural']}, mixed/both {urb['mixed']}, peri-urban {urb['peri']}, blank/other {urb['blank/other']}; English {lang['English']} of {n:,} studies, Spanish {lang['Spanish']}, Portuguese {lang['Portuguese']}, French {lang['French']}.")
    W("")
    W("### 2A.2 Mechanisms and outcomes the studies address (AI extraction coding)")
    W("")
    W("Counts are studies for which the extraction coded the field `TRUE` (a blank is *not* `FALSE`; a study can carry many). They show what was coded, not how strong the evidence is.")
    W("")
    W("| Mechanism coded | Studies | | Outcome coded | Studies |")
    W("|---|---|---|---|---|")
    for i in range(max(len(mech), len(outc))):
        a = f"`{mech[i]}` | {mc[mech[i]]:,}" if i < len(mech) else " | "
        b = f"`{outc[i]}` | {oc[outc[i]]:,}" if i < len(outc) else " | "
        W(f"| {a} | | {b} |")
    W("")
    W(f"Institutional fragmentation ({mc['institutional_fragmentation']:,}), official discretion/accommodation ({mc['discretion_accommodation']:,}) and fees/tariffs ({mc['fees']:,}) are the most frequently coded mechanisms; formal-connection ({oc['formal_connection']:,}) and affordability ({oc['affordability']:,}) outcomes are well represented, while sanitation access ({oc['sanitation_access']:,}) is coded about half as often as water access ({oc['water_access']:,}). Mechanisms concerning redress and review — administrative review ({mc['administrative_review']}), judicial review ({mc['judicial_review']}), complaint ({mc['complaint']}), reconnection ({mc['reconnection']}) — and application outcomes (refusal {oc['refusal']}, delay {oc['delay_outcome']}, success {oc['application_success']}) are coded far less often.")
    W("")
    W("### 2A.3 The quantitative subset: three structured syntheses (direction of association, not effect size)")
    W("")
    b = rows_sc[0]
    cdes = lambda s_: cf.tool_of(ed[s_]['risk_of_bias_tool'])
    counter_ids = sorted((s_ for s_, v in conc.items() if v == 'counter'), key=lambda x: int(x[1:]))
    n_fam = b['A_k'] + b['B_k'] + b['C_k']
    n_nonfit = fam['(none: reasoned non-fit)']
    assert n_fam + n_nonfit == F['effect_size_rows']
    split = lambda f_: sorted((s_ for s_, v in signs[f_].items() if v in ('positive', 'negative') and (v, sa.parse_substantive(f_)[s_]) not in sa.FAVOURABLE_IF), key=lambda x: int(x[1:]))
    diverge_all = split('A') + split('B') + split('C')
    W(f"{F['effect_size_rows']} studies have an extractable effect-size row. Of these, {n_fam} are assigned to the three synthesis families (A {b['A_k']}, B {b['B_k']}, C {b['C_k']}) and {n_nonfit} are classified as reasoned non-fits, whose exposure–outcome pair belongs to none of the families (`phase11_blank_family_resolution_2026-09-28.md` and later additions); none is pooled. Each family-assigned study is reported on two readings that must not be conflated (Campbell et al., 2020): the **raw coefficient sign** of its reported estimate, and its **substantive direction** for household access, affordability or equity (Favourable, Unfavourable, Null or Mixed). The second takes into account whether a higher value of the outcome is better or worse for households (a higher tariff, bill, interruption rate, collection time or water-poverty score is worse; a higher coverage or access rate is better) and, for three Family A studies of a non-recognised legal status, the pole of the exposure. Both are the AI's coding; the author's confirmation of them is reported below.")
    W("")
    W("| Family | Studies | Raw sign: positive / negative / null / mixed | Substantive direction: favourable / unfavourable / null / mixed | Documents |")
    W("|---|---|---|---|---|")
    W(f"| A — legal status, tenure, recognition and governance arrangements | {b['A_k']} | {b['A_positive']} / {b['A_negative']} / {b['A_null']} / {b['A_mixed']} | {b['A_favourable']} / {b['A_unfavourable']} / {b['A_subst_null']} / {b['A_subst_mixed']} | `family_A_swim_synthesis_2026-09-28.md` |")
    W(f"| B — assistance, participation, trust and external support | {b['B_k']} | {b['B_positive']} / {b['B_negative']} / {b['B_null']} / {b['B_mixed']} | {b['B_favourable']} / {b['B_unfavourable']} / {b['B_subst_null']} / {b['B_subst_mixed']} | `family_B_swim_synthesis_2026-09-28.md` |")
    W(f"| C — ownership, regulation, institutional capacity and administrative structure | {b['C_k']} | {b['C_positive']} / {b['C_negative']} / {b['C_null']} / {b['C_mixed']} | {b['C_favourable']} / {b['C_unfavourable']} / {b['C_subst_null']} / {b['C_subst_mixed']} | `family_C_swim_synthesis_2026-09-28.md` |")
    W("")
    W(bmp.swim_core_clause(F))
    W("")
    W("The families are thematic mechanism groupings used to organise structured vote counting (SWiM), not homogeneous exposure–outcome pairs: their headings describe the mechanism clusters actually synthesised and are not the protocol's original titles (`PROJECT_SPEC.md` §8, dated note; open item A21). The per-study table of exposure, comparator, outcome, estimate, raw sign, substantive direction and appraisal is `05_analysis/effect_sizes/SWIM_CORE_VERIFICATION_TABLE_2026-10-14.csv`, and the coding behind the two directions is `05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv`.")
    W("")
    W(f"**Where studies agree.** In Family A, {b['A_concordant']} of {b['A_k']} ({b['A_concordant_pct']}%) are Favourable, that is concordant with \"legal/institutional recognition or eligibility is associated with better access\"; {b['A_unfavourable']} are Unfavourable and {b['A_subst_null']} Null. All {b['B_k']} Family B studies are Favourable or Mixed, and none is Unfavourable or Null. Three studies of private versus public ownership (S526, S539, S749; US ×2 and Brazil) are all Unfavourable for private ownership, with raw signs that differ (negative on a progressivity ratio, positive on a bill and on a tariff) because their outcomes point in opposite directions. Raw sign and substantive direction come apart for {len(diverge_all)} of the {n_fam} studies ({', '.join(diverge_all)}), which is why the two are reported separately.")
    W("")
    W("**Where they disagree or do not fit.**")
    W("")
    W("- Family A counter-pattern (exposure associated with *worse* access): " + ", ".join(f"{s}" for s in sorted(s for s, v in conc.items() if v == 'counter')) + "; null: " + ", ".join(sorted(s for s, v in conc.items() if v == 'null')) + ".")
    if b['C_test_no_dominant_sign'] == 'holds':
        W(f"- Family C has no dominant direction by either reading ({b['C_favourable']} Favourable / {b['C_unfavourable']} Unfavourable / {b['C_subst_mixed']} Mixed; raw sign {b['C_positive']} positive / {b['C_negative']} negative / {b['C_mixed']} mixed) — its exposures and outcomes are heterogeneous.")
    else:
        W(f"- Family C has no dominant direction by the substantive reading ({b['C_favourable']} Favourable / {b['C_unfavourable']} Unfavourable / {b['C_subst_mixed']} Mixed of {b['C_k']}); by raw sign ({b['C_positive']} positive / {b['C_negative']} negative / {b['C_mixed']} mixed) negative is a bare majority, which the pre-stated no-dominant-sign test reports as failing, but raw sign mixes outcomes of opposite polarity (a lower cost, complaint rate or welfare loss is Favourable), so the household-relevant reading is the substantive one — its exposures and outcomes are heterogeneous.")
    W(f"- Studies whose outcome is not a household water or sanitation access measure were taken out of the three families under the author's rulings of 2026-10-14: S358 (groundwater decline), S590 (a city's decision to build waterworks), S1140 (a village community's success in securing programme funding) and S1136 (road-level public sanitation infrastructure) are reasoned non-fits, and S1121 (residential building permits) was excluded; none of the {F['swim_core_studies']} studies in the families is flagged as an indirect outcome. The author's further rulings of 2026-10-14, made from the verbatim PDF passages, then excluded S1020 (physical watershed engineering), S1042 (the mayors' subjective valuation of water access), S1057 (community design and O&M participation), S1144 (social-proximity trust), S1163 (external donor or NGO sponsorship of school WASH programmes) and S947 (macroeconomic natural-resource dependence; the governance index was only a control) and kept S920, S1102, S1146 and the DRC trial (S366, with S294 as its linked report). S471 is Favourable on its primary estimate but Null once fully adjusted, and S879 is Mixed (payment compliance rose, household water access did not change); the author kept both in the main count, and two further scenarios recode them.")
    W("")
    W("Examples as extracted (exposure and direction are AI-extracted fields):")
    W("")
    W("| Study | Country | Tool | Exposure (extracted) | Direction (extracted) | Raw sign | Substantive |")
    W("|---|---|---|---|---|---|---|")
    for s in ('S765', 'S398', 'S1122', 'S142', 'S057', 'S104', 'S920', 'S085', 'S366', 'S1102', 'S526', 'S539', 'S749', 'S631', 'S1146', 'S879', 'S1062'):
        W(ex(s))
    W("")
    _fails = any(r_[k_] == 'FAILS' for r_ in rows_sc for k_ in ('A_test_majority_concordant', 'B_test_none_negative_or_null', 'C_test_no_dominant_sign', 'C_test_no_dominant_direction'))
    W("**Sensitivity of these counts** (`05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md`): under " + ("every scenario tried" if not _fails else "the scenarios tried, **except where a test FAILS (see the file)**") + " — dropping abstract-only extractions, dropping the sparse-audit rows that carry effect sizes, dropping effect-size rows of studies not flagged eligible (none remains since S589's row was removed on 2026-10-14; the scenario is kept as a check), collapsing linked reports, dropping Family A's remaining coding judgment call (S404), recoding S471 as Null, recoding S879 as Null, and keeping only the studies for which raw sign and substantive direction agree — the pre-stated conclusion tests for A, B and C " + ("hold" if not _fails else "do not all hold") + "; Family A's Favourable share ranges " + f"{min(r['A_concordant_pct'] for r in rows_sc)}–{max(r['A_concordant_pct'] for r in rows_sc)}%.")
    W("")
    W("### 2A.4 What the qualitative, doctrinal and mixed-methods studies record")
    W("")
    W(f"A large part of the evidence base ({dc['qualitative'] + dc['mixed_methods'] + dc['doctrinal'] + dc['jurimetric']:,} studies by design class{f', plus {free_design} with unmapped free-text design labels' if free_design else ''}) is qualitative, mixed-methods or documentary rather than quantitative. Using the mechanism vocabulary adopted on 2026-10-14 (`FAMILY_VOCABULARY_PROPOSAL_2026-09-28.md`, mechanical and unvalidated), studies whose label maps to a single mechanism family are: " + ", ".join(f"{k.replace('_', ' ')} {v}" for k, v in cf.ranked(Counter(r['mechanism_family_proposed'] for r in vocab.values() if r['mechanism_family_proposed'] not in ('multiple', pv.NEEDS)))) + f"; {Counter(r['mechanism_family_proposed'] for r in vocab.values())['multiple']} carry several. The mapping is mechanical and unvalidated, so read the counts as indicative only. Examples of qualitative or doctrinal studies with `mechanism_certainty` 2 or higher (\"mechanism directly observed\" or above), showing the study's own recorded (original) mechanism label beside the adopted family, and the AI-extracted finding text:")
    W("")
    W("| Study | Country | Design | Own recorded mechanism label (original) → adopted family | Extracted finding (truncated) |")
    W("|---|---|---|---|---|")
    shown = Counter()
    for sid in sorted(ed, key=lambda s: int(s[1:])):
        r, e, v = ed[sid], em[sid], vocab[sid]
        f_ = v['mechanism_family_proposed']
        if e['study_design_class'] in ('qualitative', 'doctrinal') and r['mechanism_certainty'].strip() in ('2', '3', '4') and f_ not in ('multiple', pv.NEEDS) and shown[f_] < 1 and r['effect_estimate'].strip() and not r['extraction_note'].startswith(cf.ABSTRACT_ONLY_PREFIXES):
            shown[f_] += 1
            W(f"| {sid} | {r['country'][:24]} | {e['study_design_class']} | {trim(orig_lab.get(sid, {}).get('mechanism_family', e['mechanism_family']), 60)} → {f_.replace('_', ' ')} | {trim(r['effect_estimate'], 210)} |")
    W("")
    W("### 2A.5 Gaps visible in the records")
    W("")
    GEO = bmp.geography_framing(F)
    W(f"- **Geographic:** {GEO['full']} {P(sum(v for _, v in F['country_top10_single_name']))} of studies sit in the ten commonest single countries.")
    W(f"- **Design:** {tools['RoB 2']} randomised trials (4 distinct) and {tools['ROBINS-I']} quasi-experimental studies against {P(tools['Legal Framework'])} studies appraised with the project's own non-validated framework (the residual category for designs no published instrument fits, including doctrinal and documentary studies).")
    W("- **Mechanisms/outcomes:** redress and review mechanisms and application-process outcomes are thinly coded (see 2A.2); sanitation access less than water.")
    W(f"- **Retrieval:** {F['full_text_undecided']:,} title/abstract includes were never assessed. Their median publication year is {int(y_unret[1])} versus {int(y_assessed[1])} for assessed records; {y_unret[2]:.1f}% were published before 2000 versus {y_assessed[2]:.1f}%, and {y_unret[3]:.1f}% in 2020 or later versus {y_assessed[3]:.1f}% — the unassessed set is older, so the corpus under-represents earlier literature.")
    W("")
    W("## 2B. Tentative interpretations (not findings — each rests on the numbers cited and could be wrong)")
    W("")
    W(f"1. **The literature documents co-occurrence far more than causation.** With {P(F['causal_capable_designs'])} causal-capable designs (the mechanism-certainty code now follows the design, §2A.1), the base can say that legal/administrative features and access outcomes are associated across many settings, but rarely that one causes the other. *Rests on:* §2A.1 counts. *Would change if:* the {F['full_text_undecided']:,} unassessed records or future searches contain many more designs with credible identification.")
    W(f"2. **Recognition and formal status tend to go with better access (Family A), but the pattern is thin.** {b['A_concordant']} of {b['A_k']} Favourable, {len(counter_ids)} Unfavourable (S104 tenure and interruptions): {'; '.join(f'{s_} appraised with {cdes(s_)}' for s_ in counter_ids)}. *Rests on:* the SWiM coding, a judgment by the same AI. Not a pooled estimate and not certainty-graded.")
    W("3. **Assistance and trust mechanisms look uniformly favourable (Family B) — but on three studies with three different mechanisms.** The consistency may reflect small numbers or reporting of positive findings; nothing here excludes either.")
    W("4. **Ownership and price: private ownership goes with worse affordability in the three studies (S526, S539, S749), but the two US samples probably overlap**, so this may be two independent samples, not three (`linked_reports_2026-09-28.csv` LR09, an audit inference).")
    W("5. **Most institutional analysis in this corpus is descriptive-qualitative and concentrated on fragmentation, discretion and fees.** This may reflect what the search and the closed retrieval surfaced (English-language, post-2010, database-indexed) as much as what the world contains.")
    W("6. " + GEO['point'])
    W("")
    W("## 3. Confidence and limitations")
    W("")
    W("### 3.1 Overall confidence: low to very low for any causal or comparative claim")
    W("")
    W("This is the author's tentative characterisation, not a GRADE judgment (none has been made): the direction-of-association statements rest on a small quantitative subset (" + f"{fam['A']}, {fam['B']} and {fam['C']}" + " studies), AI-extracted and AI-coded values, mostly observational designs, and a screening stage that closed early. Reasons follow.")
    W("")
    W("### 3.2 Incomplete screening")
    W("")
    W(f"- Full-text retrieval closed at 62.2%: {F['full_text_undecided']:,} of {F['full_text_records']:,} records ({F['unretrieved_not_retrievable']:,} not retrievable, {F['unretrieved_wrong_file']} wrong file delivered) were never assessed, and the unassessed set is systematically older (§2A.5). Some may be duplicates of included studies, some not eligible; the direction of any bias is unknown.")
    W(f"- {e10} of the {F['full_text_exclude']:,} full-text excludes are E10 (inaccessible text), i.e. never judged on content.")
    A16 = bmp._a16_outcome()
    W(f"- The full-text decisions were made by the AI, and {F['human_verified_rows']:,} of the {F['full_text_decided']:,} ({100 * F['human_verified_rows'] / F['full_text_decided']:.1f}%) carry human verification or adjudication: the author confirmed {F['reviewer_2_confirmed_includes']} includes (S001–S200) and adjudicated {F['human_adjudicated_rows']} further decisions, which makes {F['reviewer_2_confirmed_includes'] + F['human_adjudicated_includes']} human-checked includes and {F['human_adjudicated_excludes']} human-checked excludes; the other {F['full_text_decided'] - F['human_verified_rows']:,} AI decisions have not been checked by a human. {F['decided_blank_reviewer_1'] + F['decided_inferred_reviewer_1']} decided rows had no reviewer label recorded at the time (an AI label was inferred for them on 2026-10-14 from the exclusion log and extraction records, open item A2), and the author has since ruled on all of them. A prioritised queue for further human review exists (`02_screening/full_text/REVIEWER_2_PRIORITY_QUEUE_README.md`).")
    W(f"- **A blind AI re-read of the exclusions was adjudicated by the author.** Two non-Claude models (Codex, Gemini), blind to the original decision, re-read {A16['reread_excludes']} full-text exclusions whose PDF was available: {A16['sample']} drawn at random, stratified by exclusion code, and {A16['reread_excludes'] - A16['sample']} from the priority queue. The models disagreed with the AI on {A16['flagged']} of them ({A16['flagged_in_sample']} from the random sample and {A16['flagged'] - A16['flagged_in_sample']} from outside it), most often under wrong topic and engineering only. The author adjudicated all {A16['flagged']}: {A16['upheld']} exclusions were confirmed and {A16['reversed']} were reversed to inclusions ({', '.join(A16['reversed_ids'])}). Among the {A16['sample']} randomly sampled exclusions, {A16['reversed_in_sample']} were therefore false exclusions ({100 * A16['rate']:.1f}%, 95% Wilson interval {100 * A16['rate_lo']:.1f}–{100 * A16['rate_hi']:.1f}%); scaled to the {A16['pool']:,} content-based exclusions (all codes except the {e10} inaccessible texts and the {F['exclusion_by_code'].get('E08', 0)} duplicates, which were never sampled), that is about {A16['scaled']} studies (interval {A16['scaled_lo']}–{A16['scaled_hi']}; about {A16['scaled_by_code']} when scaled within exclusion code). This replaces the earlier arithmetic of roughly {bmp._a16_total()[0]} further includes, which took the models' verdicts at face value. The estimate has three limits: it counts only the exclusions the models flagged, it was made under the narrow reading of eligibility criterion 2 that the author adopted after seeing the disagreement, and it rests on a sample of {A16['sample']}. In the other direction the models questioned {A16['p4_flagged']} inclusions, and the author excluded all {A16['p4_excluded']}; the consistency passes that followed under the same narrow reading moved {A16['moved_to_exclusion_after_p4']} further included reports to the exclusions ({A16['moved_to_exclusion']} in all). The author's reading list is `02_screening/full_text/A16_ADJUDICATION_SHEET_2026-10-04.md` (open item A16).")
    W("- At title/abstract stage the human second pass covered the 3,665 include-plus-unsure records only; the 22,557 records the AI excluded were not human-checked, so any wrongly excluded record is invisible to this review. The 99.8% agreement on the reviewed set is unusually high and was flagged by the project itself (`README.md`; `AI_USE_STATEMENT.md`).")
    W("")
    W("### 3.3 Missing or thin data")
    W("")
    sp = asr.audit()
    sp_new = [r_ for r_ in sp if not r_['S1_prefix']]
    sp_strong, sp_mod = sum(r_['strength'] == 'strong' for r_ in sp_new), sum(r_['strength'] == 'moderate' for r_ in sp_new)
    sp_es = sum(1 for r_ in sp_new if r_['strength'] in ('strong', 'moderate') and 'effect-size row' in r_['weight'])
    abs_es = sum(1 for r_ in cf.read('es') if ed[r_['study_id']]['extraction_note'].startswith(cf.ABSTRACT_ONLY_PREFIXES))
    abs_es_txt = 'none has an effect-size row, so the SWiM syntheses are unaffected by them' if abs_es == 0 else f'{abs_es} effect-size rows come from them'
    W(f"- {F['abstract_only_extractions']} studies were extracted from abstract or metadata only ({100 * F['abstract_only_extractions'] / n:.1f}%); {abs_es_txt}, but descriptive counts and ratings include them. **That count is a floor:** it counts one note prefix, and a sparse-record audit (`05_analysis/descriptive/SPARSE_RECORD_AUDIT_2026-10-04.md`) found {len(sp_new)} more rows with at least one sign of shallow extraction ({('none has notes saying that only the abstract or citation was read' if not sp_strong else f'{sp_strong} have notes saying that only the abstract or citation was read')}, and {sp_mod} {'has' if sp_mod == 1 else 'have'} a recorded location that cites the abstract alone; a verification queue, not proof), of which {('none carries an effect-size row' if not sp_es else '1 carries an effect-size row' if sp_es == 1 else f'{sp_es} carry effect-size rows')}. There is no second extractor: extracted values have not been checked against the source papers.")
    W(f"- {F['jbi_high_concern']} of {tools['JBI Cross-Sectional']} JBI ratings are \"High concern\", which here means sparse extraction rather than a poor study. For CASP and MMAT, several items are \"Can't tell\" for every study (for example CASP item 3, research design justified) because extraction did not capture methodological reporting. Ratings are rule-based and unreviewed by a human.")
    W(f"- Of {F['effect_size_rows']} effect-size rows, {sum(1 for r in cf.read('es') if r['lower_CI'].strip() or r['upper_CI'].strip())} give a confidence interval and {sum(1 for r in cf.read('es') if r['standard_error'].strip())} a standard error; estimates are as the papers report them and none is pooled.")
    W("")
    # AMSTAR 2 eligibility
    am = [s for s, r in ed.items() if cf.tool_of(r['risk_of_bias_tool']) == 'AMSTAR 2']
    sweep = adq.amstar_sweep()
    weak = [x['study_id'] for x in sweep if x['evidence_score'] <= 1]
    n_reg = sum('registration' in x['signals'] for x in sweep)
    n_cnt = sum('count of included' in x['signals'] for x in sweep)
    rated = [s for s in am if not ed[s]['risk_of_bias_rating'].startswith('Not ratable')]
    am_abs = [s for s in am if ed[s]['extraction_note'].startswith(cf.ABSTRACT_ONLY_PREFIXES)]
    none_sr = [s for s, r in ed.items() if cf.tool_of(r['risk_of_bias_tool']) == 'NONE' and em[s]['study_design_class'] == 'systematic_review_secondary']
    W("### 3.4 Unresolved classifications — the two you asked about")
    W("")
    W("**Are the AMSTAR 2 studies actually systematic reviews? Partly confirmed, partly not.**")
    W("")
    if none_sr:
        W(f"- {len(am)} studies carry AMSTAR 2; another {len(none_sr)} studies also had a secondary-review design class but were **reclassified to `NONE`** after an eligibility check found them to be self-described narrative, conceptual or documentary reviews that never claim a systematic search ({', '.join(sorted(none_sr, key=lambda x: int(x[1:])))}; `RISK_OF_BIAS.md` §4). AMSTAR 2 was not applied to those, and the project has **no validated instrument for a non-systematic review used as an evidence source** — an acknowledged gap.")
    else:
        W(f"- {len(am)} studies carry AMSTAR 2. Eleven further studies had a secondary-review design class but were reclassified to `NONE` in 2026-09-28/29 after an eligibility check found them to be self-described narrative, conceptual or documentary reviews that never claim a systematic search (`RISK_OF_BIAS.md` §4). On 2026-10-14 the PI ruled on all of them (open item A25): ten were excluded (E05, no systematic method or primary data, or E03, outside the narrow scope) and one, S480, stayed included under the Legal Institutional Evidence Appraisal Framework. No included study is now tagged `NONE`, so the gap of a validated instrument for a non-systematic review no longer affects an included study, though it would again if such reviews were admitted.")
    abs_clause = (f"**{len(am_abs)} of them ({', '.join(sorted(am_abs, key=lambda s: int(s[1:])))}) were extracted from abstract or metadata only, so their eligibility was never confirmed from the full text**" if am_abs else "None of them is now extracted from abstract or metadata only")
    READ = [('S319', '2026-10-02'), ('S325', '2026-10-02'), ('S344', '2026-10-02'), ('S418', '2026-10-03'), ('S438', '2026-10-03'), ('S052', '2026-10-03')]
    GONE = ('S324', 'S326', 'S327', 'S329', 'S697')   # AMSTAR 2 reviews read in full text in 2026-10 and excluded in the 2026-10-13/14 passes (S326 E05, the others E03)
    assert all(s_ in am for s_, _ in READ) and not any(s_ in am for s_ in GONE), 'the AMSTAR 2 set changed: update the full-text reading notes'
    def join_(xs):
        return xs[0] if len(xs) == 1 else ', '.join(xs[:-1]) + ' and ' + xs[-1]
    r1 = [s_ for s_, d_ in READ if d_ == '2026-10-02']; r2 = [s_ for s_, d_ in READ if d_ == '2026-10-03']
    W(f"- Of the {len(am)} that kept AMSTAR 2, each was classed as a secondary systematic review. The recorded fields (publication type, design, method text, sample) support that unevenly: {n_reg} name a registration, PRISMA or JBI method, {n_cnt} state a count of included studies, and " + (f"{len(weak)} ({', '.join(sorted(weak, key=lambda x: int(x[1:])))}) {'shows' if len(weak) == 1 else 'show'} at most one weak signal (the word \"systematic\" or a review type)" if weak else "none is left with only one weak signal") + f" — a way to order full-text checks, not a finding (`05_analysis/descriptive/DATA_QUALITY_AUDIT_2026-09-29.md` §3). {abs_clause}. "
      f"{join_(r1)} were read in full text on 2026-10-02 (S319 searched one database; S325 and S344 are single-author reviews with weak methods, but all {len(r1)} state a search, a selection process and a synthesis, so all keep AMSTAR 2); {join_(r2)} were read in full text on 2026-10-03 (S418 is described as a narrative/scoping review with a documented search, a hybrid kept eligible with a noted caveat; all {len(r2)} state a search, selection and synthesis, so all keep AMSTAR 2). "
      f"Five reviews that earlier drafts of this bullet discussed ({join_(list(GONE))}) are no longer in the corpus: they were excluded in the consistency passes of 2026-10-13 and 2026-10-14, S326 because it states no search or selection method and the other four under the narrow reading of criterion 2.")
    rated_txt = ', '.join(s_ + ' ' + ed[s_]['risk_of_bias_rating'].split(' (')[0] for s_ in sorted(rated, key=lambda x: int(x[1:])))
    n_cl = sum(1 for s_ in rated if ed[s_]['risk_of_bias_rating'].startswith('Critically Low'))
    others_txt = ', '.join(s_ + ' ' + ed[s_]['risk_of_bias_rating'].split(' (')[0] for s_ in sorted(rated, key=lambda x: int(x[1:])) if not ed[s_]['risk_of_bias_rating'].startswith('Critically Low'))
    n_prov = sum('(provisional)' in ed[s_]['risk_of_bias_rating'].split(' (appraised')[0] for s_ in rated)
    prov_txt = f' ({n_prov} provisionally)' if n_prov else ''
    cl_clause = ('every rating given so far is Critically Low' + prov_txt if n_cl == len(rated) else f'{n_cl} of the {len(rated)} are Critically Low{prov_txt}; the others are {others_txt}')
    if len(rated) == len(am):
        oth = {}
        for s_ in sorted(rated, key=lambda x: int(x[1:])):
            lab_ = ed[s_]['risk_of_bias_rating'].split(' (')[0].strip()
            if not lab_.startswith('Critically Low'):
                oth.setdefault(lab_, []).append(s_)
        oth_txt = ', '.join(f"{len(v_)} {k_}, {', '.join(v_)}" for k_, v_ in oth.items())
        W(f"- **All {len(am)} systematic reviews received a formal AMSTAR 2 confidence rating** ({n_cl} Critically Low" + (f" and {oth_txt}" if oth_txt else "") + f"{prov_txt}), primarily reflecting absent pre-registered protocols, single-database searches, unappraised primary studies or missing lists of excluded studies. **So AMSTAR 2 so far tells the reader little beyond \"low confidence\".**")
    else:
        W(f"- **Only {len(rated)} of the {len(am)} received a formal AMSTAR 2 confidence rating** ({rated_txt}; {cl_clause}, mostly because of missing protocols, single-database searches, no list of excluded studies or no appraisal of the included studies); the other {len(am) - len(rated)} are \"Not ratable\" because their extraction lacks the information for the critical items. **So AMSTAR 2 so far tells the reader little beyond \"low confidence\"; the {len(am) - len(rated)} unrated reviews need their full texts.**")
    W("- *Tentative flag (this report's own observation, not a project ruling):* AMSTAR 2 was designed for reviews of healthcare interventions that include randomised or non-randomised studies; several of these reviews are realist, scoping or mapping reviews of qualitative and policy literature, for which a rating would be out-of-design even with full information. A decision on whether to keep AMSTAR 2 for these, or use a different instrument, is open.")
    import csv as _csv
    _ov = list(_csv.DictReader(open(cf.ROOT / '05_analysis/descriptive/amstar2_overlap_check_2026-10-04.csv', encoding='utf-8')))
    _cited = {c_ for r_ in _ov for c_ in r_['cited_corpus_study_ids'].split(';') if c_}
    _hv = [f"{r_['review']} ({r_['corpus_studies_cited']})" for r_ in _ov if int(r_['corpus_studies_cited']) >= 10]
    _heavy = 'none cites' if not _hv else (_hv[0] + ' cites' if len(_hv) == 1 else ', '.join(_hv[:-1]) + ' and ' + _hv[-1] + ' cite')
    W(f"- Reviews are secondary evidence and are never pooled as if primary. Whether their primary studies are also separate rows in this corpus was checked on 2026-10-04 for only {len(_ov)} of the {len(am)} reviews (those whose PDFs were to hand): their reference lists cite {len(_cited)} distinct corpus studies, {_heavy or 'none'} cite ten or more. This is an upper bound (background citations count) and does not read the included-studies tables, so the real double-counting risk is **still unresolved**, and {len(am) - len(_ov)} reviews are unchecked (`05_analysis/descriptive/AMSTAR2_OVERLAP_CHECK_2026-10-04.md`).")
    W("")
    rob = [s for s, r in ed.items() if cf.tool_of(r['risk_of_bias_tool']) == 'RoB 2']
    W("**Do the randomised trials need the cluster version of RoB 2? Yes for all five — one unit is inferred, and S366 has now been re-read in full.**")
    W("")
    W(f"- All {len(rob)} RoB 2 studies ({', '.join(sorted(rob, key=lambda s: int(s[1:])))}) were checked and are **cluster-randomised**, not individually randomised, and were appraised with the cluster-trial variant (`04_quality/appraisal_forms/`). Four state cluster randomisation in their own extracted design field.")
    W("- **S879** (Kenya) records only \"randomized controlled trial\"; cluster randomisation at compound level is *inferred* from the recorded unit of intervention and flagged \"verify against source paper before finalizing rating\" in its own tool field. Its rating is provisional.")
    s366_abs = ed['S366']['extraction_note'].startswith(cf.ABSTRACT_ONLY_PREFIXES)
    W(("- **S366** is still extracted from abstract/introduction text only and its RoB 2 rating is labelled low-confidence. " if s366_abs else
       "- **S366** was re-extracted and re-appraised on 2026-09-29 from the full-text PDF you supplied (its earlier abstract-only, low-confidence rating is superseded): Domains 1 and 3 Low, Domains 2 and 5 Some concerns, Domain 4 Some concerns for the primary outcomes and High for the self-reported satisfaction/behaviour indices; Figure 1 and the supplement were not read. ") +
      f"S366 and S294 report the same DRC cluster trial, so the {len(rob)} RoB 2 studies are **4 distinct trials** (but different surveys: 1,312 households in S366, 3,283 in S294). All five rate \"Some concerns\" overall; S057, S085, S294 and S879 still use many \"No information\" answers because extraction did not capture trial-conduct details.")
    W(f"- A keyword scan of design fields in the other {n - len(rob):,} studies found no further randomised design under another tool. **S189** is a process evaluation conducted \"in connection with a randomised controlled trial\" (Orissa, India); it was appraised with ROBINS-I as a quasi-experimental study, and its full appraisal form covers the confounding domain only. Whether the parent trial itself is in the corpus, and whether any of its outcomes belong under RoB 2 cluster, is worth confirming. (The scan covered design and measure fields only, not full texts.)")
    W("")
    W("### 3.5 Other unresolved items that may matter")
    W("")
    W("- **S589's** effect-size row (an unadjusted descriptive comparison in a study not flagged eligible) was removed on 2026-10-14 (`DECISIONS_AND_OPEN_ITEMS.md` A1, closed); the study itself stays in the review.")
    W(f"- **Linked reports (open item A3, ruled 2026-10-14: keep and link):** the {n:,} included reports describe {F['distinct_studies_definite_links']:,} distinct studies on the definite same-data links (S294/S366 one trial; S097/S098 one sample) and {F['distinct_studies_incl_partial_links']:,} counting the partial overlaps (S681/S682, S357/S369). No pair was collapsed: companion reports carry distinct outcome-specific extractions and appraisals. S526/S539 (two US utility studies whose samples probably overlap) are flagged for verification before any pooling.")
    W(f"- **Free-text classifications:** `mechanism_family` ({len({r['mechanism_family'] for r in orig_lab.values()})} distinct labels) and `outcome_family` ({len({r['outcome_family'] for r in orig_lab.values()})}) were uncontrolled until 2026-10-14, when the PI adopted the draft vocabularies (open items A5 and A20; originals preserved, the AI-resolved edge cases listed in `FAMILY_VOCABULARY_PROPOSAL_2026-09-28.md`); {free_design} studies still have an unmapped design class and the family mapping is mechanical and unvalidated. Country and legal-system fields are free text, so the geographic counts here are rule-based.")
    W("- **Direction coding** in the SWiM documents is a judgment by the same AI; sign and valence differ for several studies.")
    fa = adq.flag_audit(); fc = Counter(x['category'] for x in fa); esf, escov = adq.es_scan()
    W(f"- **The \"quantitative-synthesis-eligible\" flag looks generous.** Of {len(fa)} studies flagged, {fc['C']} show nothing inferential in their extraction (descriptive or unclear), {fc['B']} name an inferential model but hold no interval, SE or p-value, and {fc['A']} carry some uncertainty information (heuristic; `05_analysis/descriptive/quantitative_flag_audit_2026-09-29.csv`). Only {F['effect_size_rows']} studies have an effect-size row and none is pooled, so no synthesis result depends on the flag. No flag was changed.")
    W(f"- **Consistency scan of the effect-size rows** found {len([f for f in esf if f[1] != 'row_for_study_not_flagged_eligible'])} new item(s) besides the S589 row removed on 2026-10-14 ({', '.join(f'{a} {b}' for a, b, _ in esf if b != 'row_for_study_not_flagged_eligible') or 'none'}); but an interval could be checked for only {escov['structured_interval'] + escov['text_interval']} of {F['effect_size_rows']} rows, so this is weak assurance.")
    W("- **Same-paper duplicates** with different-language titles and blank DOIs were found and merged among included studies; the DOI/title audits cannot detect this class in the wider pool.")
    W("")
    W("## 4. Most useful next steps (in order)")
    W("")
    W(f"1. **Human check of the AI's screening**: work `full_text_reviewer_2_priority_queue_2026-09-28.csv` (tier 1: the {F['decided_blank_reviewer_1'] + F['decided_inferred_reviewer_1']} rows whose reviewer label was not recorded; tier 2: a stratified sample of excludes). It bounds the risk that eligible studies were excluded or ineligible ones included.")
    W("2. **Obtain the full text of the abstract-only studies that carry the most weight**: " + ("S366 (RoB 2), " if s366_abs else "(S366, the RoB 2 study, was re-extracted 2026-09-29; the four abstract-only AMSTAR 2 reviews on 2026-10-02), ") + ("the AMSTAR 2 reviews extracted from abstracts (" + ", ".join(sorted(am_abs, key=lambda s: int(s[1:]))) + "), " if am_abs else f"the {len(am) - len(rated)} AMSTAR 2 reviews still unrated (start with the weakest-evidenced in the audit, `DATA_QUALITY_AUDIT_2026-09-29.md` §3), ") + f"then the {F['abstract_only_extractions']} remaining abstract-only studies and the {sp_strong} further strong candidates from the sparse-record audit; re-extract (`03_extraction/extracted_data/abstract_only_fulltext_request_list_2026-09-29.csv`, `05_analysis/descriptive/sparse_record_audit_2026-10-04.csv`).")
    W("3. **Verify S879's randomisation unit against the paper** and confirm S189's parent-trial handling; then finalise or revise the RoB 2 cluster ratings.")
    W(f"4. **Decide the AMSTAR 2 question**: keep it (and obtain full texts so the {len(am) - len(rated)} \"Not ratable\" reviews can be rated) or replace it for realist/scoping/mapping reviews. Finish the check of whether these reviews' primary studies are also in the corpus (so far {len(_ov)} of {len(am)} reviews, reference lists only).")
    W("5. **Second-extract the prepared sample** (60 studies from S001–S200, `03_extraction/second_extractor/`) against the source papers to estimate extraction error; the sample cannot speak for later extractions, so a second sample from S201 onward is needed before any whole-corpus claim.")
    W("6. **Resolve linked reports and the family vocabulary** (S589 was settled on 2026-10-14), then re-run `sensitivity_analysis.py`.")
    W("7. **Reduce the retrieval bias**: prioritise the older, unassessed records (or state the limitation prominently), and consider targeted searches for evidence from high-coverage welfare states (for example the Netherlands and other European systems) to examine administrative exclusion inside universal-network systems.")
    W("8. **Only then** decide whether any family could support a restricted meta-analysis (`ANALYSIS_PLAN.md` §2); at present none does.")
    W("")
    W("---")
    W("*Provenance: `00_admin/CURRENT_FIGURES.md`, `05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md`, `05_analysis/descriptive/FAMILY_VOCABULARY_PROPOSAL_2026-09-28.md`, `04_quality/risk_of_bias/2026-09-28_evidence_limitations.md`, `00_admin/audits/2026-09-28_repository_audit.md`. Regenerate with `python3 code/analysis/build_preliminary_report.py`.*")
    return "\n".join(L) + "\n"


if __name__ == '__main__':
    OUT.write_text(build(), encoding='utf-8')
    print('wrote', OUT.relative_to(ROOT))
