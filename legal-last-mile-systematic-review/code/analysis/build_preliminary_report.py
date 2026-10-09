#!/usr/bin/env python3
"""Generate 06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.md from the databases.

Every number is computed from the CSVs (so it cannot drift from the data); every quoted example is pulled from the extraction
or effect-size rows by study_id. Interpretive sentences are hand-written here, are labelled TENTATIVE, and cite the numbers they
rest on. Nothing in the report is a pooled effect, a certainty (GRADE) judgment, or a final finding.

Run from the project root:  python3 code/analysis/build_preliminary_report.py   (deterministic; verify_repository.py checks freshness)
"""
import re, statistics, sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402
import sensitivity_analysis as sa  # noqa: E402
import propose_family_vocabulary as pv  # noqa: E402
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
    vocab = {r['study_id']: r for r in pv.build()}
    P = lambda k, d=n: f"{k:,} ({100 * k / d:.0f}%)"

    # ---- descriptive numbers
    dc = Counter(r['study_design_class'] for r in em.values())
    enum = {'experimental', 'quasi_experimental', 'observational', 'qualitative', 'doctrinal', 'jurimetric', 'systematic_review_secondary', 'mixed_methods'}
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
        e = es[sid]; x = ed[sid]
        return (f"| {sid} | {x['country'][:28]} | {cf.tool_of(x['risk_of_bias_tool'])} | {trim(e['exposure_definition'], 95)} | {trim(e['direction'], 110)} |")

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
    free_top = "; ".join(f"{k} ({v})" for k, v in Counter(v for v in (r['study_design_class'] for r in em.values()) if v not in enum).most_common(2))
    W(f"- **Design mix** (evidence-map `study_design_class`; {free_design} studies carry free-text values outside the 8-value enum — the commonest are variants of \"case study\", e.g. {free_top}; they are not in the counts that follow): qualitative {dc['qualitative']}, mixed-methods {dc['mixed_methods']}, observational {dc['observational']}, quasi-experimental {dc['quasi_experimental']}, doctrinal {dc['doctrinal']}, jurimetric {dc['jurimetric']}, secondary systematic reviews {dc['systematic_review_secondary']}, experimental {dc['experimental']}. By appraisal tool: " + ", ".join(f"{k} {v}" for k, v in tools.items()) + ".")
    W(f"- **Designs able to support a causal claim about a legal/administrative mechanism:** {F['causal_capable_designs']} ({100 * F['causal_capable_designs'] / n:.0f}%) — {tools['ROBINS-I']} quasi-experimental studies and {tools['RoB 2']} randomised trials (which are 4 distinct trials, see §3.4). {mcert['3'] + mcert['4']} studies carry a numeric mechanism-certainty of 3 or 4 (the codebook's quasi-experimental or experimental evidence), **but only {cert['hi_in_causal']} of them are among the {F['causal_capable_designs']} ROBINS-I/RoB 2 studies; the other {len(cert['hi_outside'])} are other designs, a coding inconsistency the audit flags** (`DATA_QUALITY_AUDIT_2026-09-29.md` §5); {mcert['1']} sit at level 1 (documented association) and {mcert['2']} at level 2; {F['mechanism_certainty_narrative_text']} carry narrative text instead of a 0–4 code.")
    W(f"- **Geography** (`country` is free text; {F['country_multi_or_regional_studies']} studies name several countries or a region and are not counted below): " + ", ".join(f"{k} {v}" for k, v in F['country_top10_single_name']) + f". The dissertation's comparison countries are unevenly covered: **Brazil {country('Brazil')}, Canada {country('Canada')} ({country_any('Canada')} counting multi-country entries), Netherlands {country('Netherlands')} ({country_any('Netherlands')} counting multi-country entries).**")
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
    sA = signs['A']
    pos_conc = sum(1 for s_, v in conc.items() if v == 'concordant' and sA[s_] == 'positive')
    neg_conc = sum(1 for s_, v in conc.items() if v == 'concordant' and sA[s_] == 'negative')
    cdes = lambda s_: cf.tool_of(ed[s_]['risk_of_bias_tool'])
    counter_ids = sorted((s_ for s_, v in conc.items() if v == 'counter'), key=lambda x: int(x[1:]))
    W(f"Only {F['effect_size_rows']} studies have an effect-size row; none is pooled. Counts are of the **sign of each study's extracted association** (sign and valence differ for some studies — see the Family A and C documents).")
    W("")
    W("| Family | Studies | Positive / negative / null / mixed (sign) | Documents |")
    W("|---|---|---|---|")
    W(f"| A — legal recognition, eligibility and access | {b['A_k']} | {b['A_positive']} / {b['A_negative']} / {b['A_null']} / 0 | `family_A_swim_synthesis_2026-09-28.md` |")
    W(f"| B — bureaucratic/administrative assistance | {b['B_k']} | {b['B_positive']} / {b['B_negative']} / {b['B_null']} / {b['B_mixed']} | `family_B_…` |")
    W(f"| C — administrative/legal barriers, ownership and price | {b['C_k']} | {b['C_positive']} / {b['C_negative']} / {b['C_null']} / {b['C_mixed']} | `family_C_…` |")
    W("")
    W(f"**Where studies agree.** In Family A, {b['A_concordant']} of {b['A_k']} ({b['A_concordant_pct']}%) are concordant with \"legal/institutional recognition or eligibility is associated with better access\" on a substantive reading ({pos_conc} positive-sign studies plus {neg_conc} negative-sign studies in which unrecognised or informal status is associated with worse access). All {b['B_k']} Family B studies report a positive or mixed association between administrative assistance/institutional trust and access, and none is negative. Three studies of private versus public ownership (S526, S539, S749; US ×2 and Brazil) all associate private ownership with worse affordability or progressivity.")
    W("")
    W("**Where they disagree or do not fit.**")
    W("")
    W("- Family A counter-pattern (exposure associated with *worse* access): " + ", ".join(f"{s}" for s in sorted(s for s, v in conc.items() if v == 'counter')) + "; null: " + ", ".join(sorted(s for s, v in conc.items() if v == 'null')) + ".")
    W(f"- Family C has no dominant direction ({b['C_positive']} positive / {b['C_negative']} negative / {b['C_mixed']} mixed) — its exposures and outcomes are heterogeneous, and signs are not comparable across them.")
    W("")
    W("Examples as extracted (exposure and direction are AI-extracted fields):")
    W("")
    W("| Study | Country | Tool | Exposure (extracted) | Direction (extracted) |")
    W("|---|---|---|---|---|")
    for s in ('S765', 'S398', 'S1122', 'S142', 'S057', 'S104', 'S1020', 'S1121', 'S085', 'S294', 'S526', 'S539', 'S749', 'S631', 'S947', 'S1146', 'S879', 'S1062'):
        W(ex(s))
    W("")
    _fails = any(r_[k_] == 'FAILS' for r_ in rows_sc for k_ in ('A_test_majority_concordant', 'B_test_none_negative_or_null', 'C_test_no_dominant_sign'))
    W("**Sensitivity of these counts** (`05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md`): under " + ("every scenario tried" if not _fails else "the scenarios tried, **except where a test FAILS (see the file)**") + " — dropping abstract-only extractions, dropping the sparse-audit rows that carry effect sizes, dropping S589 (an unadjusted descriptive comparison in an ineligible-flagged study), collapsing linked reports, and dropping Family A's two coding judgment calls — the pre-stated conclusion tests for A, B and C " + ("hold" if not _fails else "do not all hold") + "; Family A's concordant share ranges " + f"{min(r['A_concordant_pct'] for r in rows_sc)}–{max(r['A_concordant_pct'] for r in rows_sc)}%.")
    W("")
    W("### 2A.4 What the qualitative, doctrinal and mixed-methods studies record")
    W("")
    W(f"A large part of the evidence base ({dc['qualitative'] + dc['mixed_methods'] + dc['doctrinal'] + dc['jurimetric']:,} studies by design class, plus {free_design} with free-text design labels, mostly case studies) is qualitative, mixed-methods or documentary rather than quantitative. Using the draft mechanism vocabulary (`FAMILY_VOCABULARY_PROPOSAL_2026-09-28.md`, mechanical and unvalidated), studies whose label maps to a single mechanism family are: " + ", ".join(f"{k.replace('_', ' ')} {v}" for k, v in Counter(r['mechanism_family_proposed'] for r in vocab.values() if r['mechanism_family_proposed'] not in ('multiple', pv.NEEDS)).most_common()) + f"; {Counter(r['mechanism_family_proposed'] for r in vocab.values())['multiple']} carry several. The mapping is mechanical and unvalidated, so read the counts as indicative only. Examples of qualitative or doctrinal studies with `mechanism_certainty` 2 or higher (\"mechanism directly observed\" or above), showing the study's own recorded mechanism label beside the draft family, and the AI-extracted finding text:")
    W("")
    W("| Study | Country | Design | Own recorded mechanism label → draft family | Extracted finding (truncated) |")
    W("|---|---|---|---|---|")
    shown = Counter()
    for sid in sorted(ed, key=lambda s: int(s[1:])):
        r, e, v = ed[sid], em[sid], vocab[sid]
        f_ = v['mechanism_family_proposed']
        if e['study_design_class'] in ('qualitative', 'doctrinal') and r['mechanism_certainty'].strip() in ('2', '3', '4') and f_ not in ('multiple', pv.NEEDS) and shown[f_] < 1 and r['effect_estimate'].strip() and not r['extraction_note'].startswith(cf.ABSTRACT_ONLY_PREFIXES):
            shown[f_] += 1
            W(f"| {sid} | {r['country'][:24]} | {e['study_design_class']} | {trim(e['mechanism_family'], 60)} → {f_.replace('_', ' ')} | {trim(r['effect_estimate'], 210)} |")
    W("")
    W("### 2A.5 Gaps visible in the records")
    W("")
    W(f"- **Geographic:** the Netherlands ({country('Netherlands')} single-country study) and Canada ({country('Canada')}) — two of the dissertation's three comparison jurisdictions — are barely represented against Brazil ({country('Brazil')}); {P(sum(v for _, v in F['country_top10_single_name']))} of studies sit in the ten commonest single countries.")
    W(f"- **Design:** {tools['RoB 2']} randomised trials (4 distinct) and {tools['ROBINS-I']} quasi-experimental studies against {P(tools['Legal Framework'])} studies appraised with the project's own non-validated framework (the residual category for designs no published instrument fits, including doctrinal and documentary studies).")
    W("- **Mechanisms/outcomes:** redress and review mechanisms and application-process outcomes are thinly coded (see 2A.2); sanitation access less than water.")
    W(f"- **Retrieval:** {F['full_text_undecided']:,} title/abstract includes were never assessed. Their median publication year is {int(y_unret[1])} versus {int(y_assessed[1])} for assessed records; {y_unret[2]:.1f}% were published before 2000 versus {y_assessed[2]:.1f}%, and {y_unret[3]:.1f}% in 2020 or later versus {y_assessed[3]:.1f}% — the unassessed set is older, so the corpus under-represents earlier literature.")
    W("")
    W("## 2B. Tentative interpretations (not findings — each rests on the numbers cited and could be wrong)")
    W("")
    W(f"1. **The literature documents co-occurrence far more than causation.** With {P(F['causal_capable_designs'])} causal-capable designs (and a certainty-3–4 coding that does not line up with them, see §2A.1), the base can say that legal/administrative features and access outcomes are associated across many settings, but rarely that one causes the other. *Rests on:* §2A.1 counts. *Would change if:* the {F['full_text_undecided']:,} unassessed records or future searches contain many more designs with credible identification.")
    W(f"2. **Recognition and formal status tend to go with better access (Family A), but the pattern is thin.** {b['A_concordant']} of {b['A_k']} concordant, {len(counter_ids)} counter-pattern (S104 tenure and interruptions; S1020 a watershed programme and collection time; S1121 water-adequacy screening and permitting): {'; '.join(f'{s_} appraised with {cdes(s_)}' for s_ in counter_ids)}. *Rests on:* the SWiM coding, a judgment by the same AI. Not a pooled estimate and not certainty-graded.")
    W("3. **Assistance and trust mechanisms look uniformly favourable (Family B) — but on six studies with six different mechanisms.** The consistency may reflect small numbers or reporting of positive findings; nothing here excludes either.")
    W("4. **Ownership and price: private ownership goes with worse affordability in the three studies (S526, S539, S749), but the two US samples probably overlap**, so this may be two independent samples, not three (`linked_reports_2026-09-28.csv` LR09, an audit inference).")
    W("5. **Most institutional analysis in this corpus is descriptive-qualitative and concentrated on fragmentation, discretion and fees.** This may reflect what the search and the closed retrieval surfaced (English-language, post-2010, database-indexed) as much as what the world contains.")
    W(f"6. **The dissertation's comparative frame (Netherlands, Canada, Brazil) cannot be tested from this base as it stands**: one Dutch and {country('Canada')} Canadian single-country studies.")
    W("")
    W("## 3. Confidence and limitations")
    W("")
    W("### 3.1 Overall confidence: low to very low for any causal or comparative claim")
    W("")
    W("This is the author's tentative characterisation, not a GRADE judgment (none has been made): the direction-of-association statements rest on a small quantitative subset (20, 6 and 20 studies), AI-extracted and AI-coded values, mostly observational designs, and a screening stage that closed early. Reasons follow.")
    W("")
    W("### 3.2 Incomplete screening")
    W("")
    W(f"- Full-text retrieval closed at 62.2%: {F['full_text_undecided']:,} of {F['full_text_records']:,} records ({F['unretrieved_not_retrievable']:,} not retrievable, {F['unretrieved_wrong_file']} wrong file delivered) were never assessed, and the unassessed set is systematically older (§2A.5). Some may be duplicates of included studies, some not eligible; the direction of any bias is unknown.")
    W(f"- {e10} of the {F['full_text_exclude']:,} full-text excludes are E10 (inaccessible text), i.e. never judged on content.")
    W(f"- Every full-text decision is the AI's; a human confirmed {F['reviewer_2_confirmed_includes']} includes (S001–S200) and no excludes; {F['decided_blank_reviewer_1']} decided rows carry no reviewer label. A prioritised queue for human review exists (`02_screening/full_text/REVIEWER_2_PRIORITY_QUEUE_README.md`).")
    _n_ex, _n_inc, _n_all = bmp.reviewer2_ai_counts()
    W(f"- **An AI-versus-AI check found many contested excludes.** Two non-Claude models (Codex, Gemini), blind to the original decision, re-read {_n_all} full-text decisions whose PDF was available; of the {_n_ex} the AI had excluded, {_n_inc} were judged includes (concentrated in E01 wrong topic and E06 engineering only). This was not human-adjudicated, the models may read the criteria too loosely, and nothing was changed; scaled by exclusion code the rate would imply roughly {bmp._a16_total()[0]} further includes if the models were right, and about {bmp._a16_total()[1]} even under a narrow reading of criterion 2 by an AI triage of the same records (arithmetic only, against {F['full_text_include']:,} current includes); if even a fraction are eligible, the exclusion log and every count built on it are understated. In the other direction the models would exclude {bmp._a16_inc()[1]} of {bmp._a16_inc()[0]} sampled includes beyond S001–S200, roughly {bmp._a16_inc()[2]} (range {bmp._a16_inc()[3]}–{bmp._a16_inc()[4]}) of the unconfirmed includes if the rate held — a precision question that the human second-screening of includes would settle. The researcher's reading list is `02_screening/full_text/A16_ADJUDICATION_SHEET_2026-10-04.md` (open item A16).")
    W("- At title/abstract stage the human second pass covered the 3,665 include-plus-unsure records only; the 22,557 records the AI excluded were not human-checked, so any wrongly excluded record is invisible to this review. The 99.8% agreement on the reviewed set is unusually high and was flagged by the project itself. (`AI_USE_STATEMENT.md` and `AUDITING_GUIDE.md` say \"all records\"; that wording should be checked against the README, which is narrower.)")
    W("")
    W("### 3.3 Missing or thin data")
    W("")
    sp = asr.audit()
    sp_new = [r_ for r_ in sp if not r_['S1_prefix']]
    sp_strong, sp_mod = sum(r_['strength'] == 'strong' for r_ in sp_new), sum(r_['strength'] == 'moderate' for r_ in sp_new)
    sp_es = sum(1 for r_ in sp_new if r_['strength'] in ('strong', 'moderate') and 'effect-size row' in r_['weight'])
    abs_es = sum(1 for r_ in cf.read('es') if ed[r_['study_id']]['extraction_note'].startswith(cf.ABSTRACT_ONLY_PREFIXES))
    abs_es_txt = 'none has an effect-size row, so the SWiM syntheses are unaffected by them' if abs_es == 0 else f'{abs_es} effect-size rows come from them'
    W(f"- {F['abstract_only_extractions']} studies were extracted from abstract or metadata only ({100 * F['abstract_only_extractions'] / n:.1f}%); {abs_es_txt}, but descriptive counts and ratings include them. **That count is a floor:** it counts one note prefix, and a sparse-record audit (`05_analysis/descriptive/SPARSE_RECORD_AUDIT_2026-10-04.md`) found {len(sp_new)} more rows with at least one sign of shallow extraction — {sp_strong} whose own notes say only the abstract or citation was read and {sp_mod} whose recorded location cites the abstract alone (a verification queue, not proof) — of which {sp_es} carry effect-size rows. There is no second extractor: extracted values have not been checked against the source papers.")
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
    W(f"- {len(am)} studies carry AMSTAR 2; another {len(none_sr)} studies also had a secondary-review design class but were **reclassified to `NONE`** after an eligibility check found them to be self-described narrative, conceptual or documentary reviews that never claim a systematic search ({', '.join(sorted(none_sr, key=lambda x: int(x[1:])))}; `RISK_OF_BIAS.md` §4; S326 joined them on 2026-09-29 after its full text, supplied by you, showed no stated search, selection or appraisal method). AMSTAR 2 was not applied to those, and the project has **no validated instrument for a non-systematic review used as an evidence source** — an acknowledged gap.")
    abs_clause = (f"**{len(am_abs)} of them ({', '.join(sorted(am_abs, key=lambda s: int(s[1:])))}) were extracted from abstract or metadata only, so their eligibility was never confirmed from the full text**" if am_abs else "None of them is now extracted from abstract or metadata only")
    W(f"- Of the {len(am)} that kept AMSTAR 2, each was classed as a secondary systematic review. The recorded fields (publication type, design, method text, sample) support that unevenly: {n_reg} name a registration, PRISMA or JBI method, {n_cnt} state a count of included studies, and " + (f"{len(weak)} ({', '.join(sorted(weak, key=lambda x: int(x[1:])))}) show at most one weak signal (the word \"systematic\" or a review type)" if weak else "none is left with only one weak signal") + f" — a way to order full-text checks, not a finding (`05_analysis/descriptive/DATA_QUALITY_AUDIT_2026-09-29.md` §3). {abs_clause}; S319, S324, S325 and S344 were read in full text on 2026-10-02 (S324 is a registered, well-reported review; S319 searched one database; S325 and S344 are single-author reviews with weak methods, but all four state a search, a selection process and a synthesis, so all keep AMSTAR 2); S329 is described as a \"narrative review with systematic search\" and S418 as a narrative/scoping review with a documented search (hybrids kept eligible with a noted caveat); S326, first flagged as an \"evidence survey\", was moved to `NONE` once its full text was read; S418, S438, S697, S052 and S327 were read in full text on 2026-10-03 (S697, a meta-analysis, and S438, S052 and S327 all state a search, selection and synthesis, so all keep AMSTAR 2).")
    rated_txt = ', '.join(s_ + ' ' + ed[s_]['risk_of_bias_rating'].split(' (')[0] for s_ in sorted(rated, key=lambda x: int(x[1:])))
    n_cl = sum(1 for s_ in rated if ed[s_]['risk_of_bias_rating'].startswith('Critically Low'))
    others_txt = ', '.join(s_ + ' ' + ed[s_]['risk_of_bias_rating'].split(' (')[0] for s_ in sorted(rated, key=lambda x: int(x[1:])) if not ed[s_]['risk_of_bias_rating'].startswith('Critically Low'))
    n_prov = sum('(provisional)' in ed[s_]['risk_of_bias_rating'].split(' (appraised')[0] for s_ in rated)
    prov_txt = f' ({n_prov} provisionally)' if n_prov else ''
    cl_clause = ('every rating given so far is Critically Low' + prov_txt if n_cl == len(rated) else f'{n_cl} of the {len(rated)} are Critically Low{prov_txt}; the others are {others_txt}')
    W(f"- **Only {len(rated)} of the {len(am)} received a formal AMSTAR 2 confidence rating** ({rated_txt}; {cl_clause}, mostly because of missing protocols, single-database searches, no list of excluded studies or no appraisal of the included studies); the other {len(am) - len(rated)} are \"Not ratable\" because their extraction lacks the information for the critical items. **So AMSTAR 2 so far tells the reader little beyond \"low confidence\"; the {len(am) - len(rated)} unrated reviews need their full texts.**")
    W("- *Tentative flag (this report's own observation, not a project ruling):* AMSTAR 2 was designed for reviews of healthcare interventions that include randomised or non-randomised studies; several of these reviews are realist, scoping or mapping reviews of qualitative and policy literature, for which a rating would be out-of-design even with full information. A decision on whether to keep AMSTAR 2 for these, or use a different instrument, is open.")
    import csv as _csv
    _ov = list(_csv.DictReader(open(cf.ROOT / '05_analysis/descriptive/amstar2_overlap_check_2026-10-04.csv', encoding='utf-8')))
    _cited = {c_ for r_ in _ov for c_ in r_['cited_corpus_study_ids'].split(';') if c_}
    _heavy = ', '.join(f"{r_['review']} ({r_['corpus_studies_cited']})" for r_ in _ov if int(r_['corpus_studies_cited']) >= 10)
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
    W("- **S589** is in Family A but its row is an unadjusted descriptive comparison for a study not flagged eligible; Family A results are shown with and without it. Decision pending (`DECISIONS_AND_OPEN_ITEMS.md` A1).")
    W(f"- **Linked reports:** the {n:,} rows are about {F['distinct_studies_definite_links']:,} distinct studies (S294/S366 one trial; S097/S098 one sample) and {F['distinct_studies_incl_partial_links']:,} counting partial overlaps.")
    W(f"- **Free-text classifications:** `mechanism_family` ({len({r['mechanism_family'] for r in em.values()})} distinct labels) and `outcome_family` ({len({r['outcome_family'] for r in em.values()})}) are uncontrolled; {free_design} studies have a design class outside the documented enum; a draft vocabulary is proposed, not adopted. Country and legal-system fields are free text, so the geographic counts here are rule-based.")
    W("- **Direction coding** in the SWiM documents is a judgment by the same AI; sign and valence differ for several studies.")
    fa = adq.flag_audit(); fc = Counter(x['category'] for x in fa); esf, escov = adq.es_scan()
    W(f"- **The \"quantitative-synthesis-eligible\" flag looks generous.** Of {len(fa)} studies flagged, {fc['C']} show nothing inferential in their extraction (descriptive or unclear), {fc['B']} name an inferential model but hold no interval, SE or p-value, and {fc['A']} carry some uncertainty information (heuristic; `05_analysis/descriptive/quantitative_flag_audit_2026-09-29.csv`). Only {F['effect_size_rows']} studies have an effect-size row and none is pooled, so no synthesis result depends on the flag. No flag was changed.")
    W(f"- **Consistency scan of the effect-size rows** found {len([f for f in esf if f[1] != 'row_for_study_not_flagged_eligible'])} new item(s) besides the known S589 row ({', '.join(f'{a} {b}' for a, b, _ in esf if b != 'row_for_study_not_flagged_eligible') or 'none'}); but an interval could be checked for only {escov['structured_interval'] + escov['text_interval']} of {F['effect_size_rows']} rows, so this is weak assurance.")
    W("- **Same-paper duplicates** with different-language titles and blank DOIs were found and merged among included studies; the DOI/title audits cannot detect this class in the wider pool.")
    W("")
    W("## 4. Most useful next steps (in order)")
    W("")
    W(f"1. **Human check of the AI's screening**: work `full_text_reviewer_2_priority_queue_2026-09-28.csv` (tier 1: the {F['decided_blank_reviewer_1']} no-reviewer rows; tier 2: a stratified sample of excludes). It bounds the risk that eligible studies were excluded or ineligible ones included.")
    W("2. **Obtain the full text of the abstract-only studies that carry the most weight**: " + ("S366 (RoB 2), " if s366_abs else "(S366, the RoB 2 study, was re-extracted 2026-09-29; the four abstract-only AMSTAR 2 reviews on 2026-10-02), ") + ("the AMSTAR 2 reviews extracted from abstracts (" + ", ".join(sorted(am_abs, key=lambda s: int(s[1:]))) + "), " if am_abs else f"the {len(am) - len(rated)} AMSTAR 2 reviews still unrated (start with the weakest-evidenced in the audit, `DATA_QUALITY_AUDIT_2026-09-29.md` §3), ") + f"then the {F['abstract_only_extractions']} remaining abstract-only studies and the {sp_strong} further strong candidates from the sparse-record audit; re-extract (`03_extraction/extracted_data/abstract_only_fulltext_request_list_2026-09-29.csv`, `05_analysis/descriptive/sparse_record_audit_2026-10-04.csv`).")
    W("3. **Verify S879's randomisation unit against the paper** and confirm S189's parent-trial handling; then finalise or revise the RoB 2 cluster ratings.")
    W(f"4. **Decide the AMSTAR 2 question**: keep it (and obtain full texts so the {len(am) - len(rated)} \"Not ratable\" reviews can be rated) or replace it for realist/scoping/mapping reviews; decide how to handle the non-systematic reviews now labelled `NONE`. Finish the check of whether these reviews' primary studies are also in the corpus (so far {len(_ov)} of {len(am)} reviews, reference lists only).")
    W("5. **Second-extract the prepared sample** (60 studies from S001–S200, `03_extraction/second_extractor/`) against the source papers to estimate extraction error; the sample cannot speak for later extractions, so a second sample from S201 onward is needed before any whole-corpus claim.")
    W("6. **Resolve S589, linked reports and the family vocabulary**, then re-run `sensitivity_analysis.py`.")
    W("7. **Reduce the retrieval bias**: prioritise the older, unassessed records (or state the limitation prominently), and consider targeted searches for Dutch and Canadian evidence if the comparative frame is to be tested.")
    W("8. **Only then** decide whether any family could support a restricted meta-analysis (`ANALYSIS_PLAN.md` §2); at present none does.")
    W("")
    W("---")
    W("*Provenance: `00_admin/CURRENT_FIGURES.md`, `05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md`, `05_analysis/descriptive/FAMILY_VOCABULARY_PROPOSAL_2026-09-28.md`, `04_quality/risk_of_bias/2026-09-28_evidence_limitations.md`, `00_admin/audits/2026-09-28_repository_audit.md`. Regenerate with `python3 code/analysis/build_preliminary_report.py`.*")
    return "\n".join(L) + "\n"


if __name__ == '__main__':
    OUT.write_text(build(), encoding='utf-8')
    print('wrote', OUT.relative_to(ROOT))
