"""2026-10-04 (evening): the researcher put seven full texts in the Drive inbox folder 'Sep 26 2026' (S015, S037, S104, S142, S270, S294, S388) and asked for them to be analysed
and moved to the 'Processed' folder. What this dated script records (the PDFs were read in the session; nothing is copied into the repository):
  * S270 (Rivera-Contreras 2018): re-extracted from the full text by reextract_2026-10-04/S270.json (run_reextract_2026-10-04.py); here only the note sentence about the
    appraisal rating is corrected (the Legal Framework tool is not misfitted; the 2026-09-28 condensed rating simply was not re-answered).
  * S015 (Basnet & Sherchan 2026, Water 18(12):1514): AMSTAR 2 appraised on the full text -> Critically Low (critical items 2, 7, 9, 13 flawed); extraction fields upgraded from the
    abstract-level entry; item-level answers in 04_quality/appraisal_forms/S015_AMSTAR2.md (supersedes the 2026-09-16 pilot).
  * S142 (Allaire et al. 2024): effect-size row enriched with the incidence rate ratios printed in the main text (3.54, 17.8, 1.48, >4.0, 0.91); the confidence intervals are in
    Supplementary Tables 5-6, which are not in the PDF, so the row stays unpooled.
  * FULLTEXT_VERIFICATION_2026-10-04.csv: S037, S104, S294, S388 verified, S142 verified and enriched (5 of the 15 rows that had no full text).
Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
DATE = '2026-10-04'
ED = '03_extraction/extracted_data/extraction_database.csv'
ES = '05_analysis/effect_sizes/effect_sizes.csv'
VER = '05_analysis/effect_sizes/FULLTEXT_VERIFICATION_2026-10-04.csv'


def rw(path, fn):
    raw = open(path, newline='', encoding='utf-8').read(); crlf = '\r\n' in raw[:5000]
    with open(path, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
    n = len(rows); out = fn(rows); assert len(rows) == n
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
    os.replace(tmp, path)
    return out


# ---------------------------------------------------------------- S015 AMSTAR 2
ITEMS = {1: 'PICO components in the research questions and inclusion criteria', 2: 'Review methods established prior to the review (protocol); deviations justified',
         3: 'Selection of study designs explained', 4: 'Comprehensive literature search strategy', 5: 'Study selection in duplicate', 6: 'Data extraction in duplicate',
         7: 'List of excluded studies with justification', 8: 'Included studies described in adequate detail', 9: 'Satisfactory technique for risk of bias in included studies',
         10: 'Funding sources of included studies reported', 11: 'Appropriate meta-analytic methods', 12: 'Impact of risk of bias on meta-analysis results',
         13: 'Risk of bias accounted for when interpreting results', 14: 'Heterogeneity explained and discussed', 15: 'Publication bias investigated (quantitative synthesis)',
         16: 'Conflicts of interest and funding of the review reported'}
CRIT = {2, 4, 7, 9, 11, 13, 15}
ANS = {
    1: ('Partial Yes', 'project convention: three research questions with population (Kathmandu Valley), exposure (water contamination, governance) and outcomes (health risks) and eligibility domains are stated; there is no comparator group'),
    2: ('No', 'CRITICAL FLAW: the eligibility criteria are called a priori, but the review was registered retrospectively on OSF during manuscript revision (osf.io/w94yr, accessed 10 June 2026), so no protocol existed before the review'),
    3: ('Yes', 'BORDERLINE: the text accepts all empirical designs (laboratory testing, epidemiological and household surveys, hydrogeochemical studies, governance literature) and says the diversity strengthens breadth, while limiting comparability; no further justification'),
    4: ('Partial Yes', 'five databases (PubMed, ProQuest, SpringerLink, Google Scholar, NepJOL) plus named grey-literature sources; example Boolean strings given; English only, 2000-July 2025 (limits stated, not justified); no reference-list searching, expert consultation or full strategy; a single search in July 2025'),
    5: ('No', 'who screened is not stated; the author-contribution statement assigns investigation to one author, so duplicate selection is not shown'),
    6: ('No', 'a structured extraction matrix is described; duplicate extraction is not stated'),
    7: ('No', 'CRITICAL FLAW: PRISMA counts and grouped reasons are given (70 records, 4 duplicates, 11 excluded on title/abstract, 55 full texts, 10 excluded: 2 limited rigour, 3 not relevant to health or governance, 5 not urban Kathmandu) but the 10 excluded studies are not listed'),
    8: ('No', 'Table 1 is a representative domain-level summary of the 45 sources (counts per domain, example findings, bracketed reference numbers), not a per-study description of populations, designs and outcomes'),
    9: ('No', 'CRITICAL FLAW: section 2.7 states that no formal quality appraisal tool was applied (heterogeneity; broad scope); methodological clarity was only noted informally during extraction'),
    10: ('No', 'funding sources of the included studies are not reported'),
    11: ('No', 'not applicable: no meta-analysis was done (narrative thematic synthesis; stated as inappropriate given heterogeneity); not counted as a flaw'),
    12: ('No', 'not applicable: no meta-analysis'),
    13: ('No', 'CRITICAL FLAW: with no risk-of-bias assessment, nothing is accounted for in interpreting the findings; the review only says studies with limited transparency were interpreted cautiously and lists the reliance on cross-sectional designs and grey literature as limitations'),
    14: ('Yes', 'heterogeneity of designs, sampling, geography, methods and reporting is discussed (4.6 and 2.7) and used to justify narrative synthesis; patterns are explained by source, season and system level'),
    15: ('No', 'not applicable: no quantitative synthesis; publication bias is not discussed (English-only and grey literature noted as limitations)'),
    16: ('Yes', 'no external funding; authors declare no conflicts of interest; an NSF IRES programme is acknowledged for the Nepal research experience')}
NA_ITEMS = {11, 12, 15}
RATING = 'Critically Low'
BASIS = 'critical items 2 (retrospective registration, so no protocol), 7 (no list of excluded studies), 9 (no risk-of-bias technique) and 13 (risk of bias not accounted for) are flawed; items 11 and 15 do not apply (no meta-analysis)'
S015 = dict(
    publication_type='journal article (systematic review, Water 18(12):1514, MDPI)',
    population='peer-reviewed and selected grey literature on drinking-water contamination, public-health risk and governance in Kathmandu Valley, Nepal (45 sources, 2000-2025)',
    sample_size='70 records identified (62 databases, 8 grey), 4 duplicates, 66 screened, 11 excluded, 55 full texts, 10 excluded (2 limited rigour, 3 not relevant, 5 not urban), 45 included; no meta-analysis',
    effect_measure='narrative thematic synthesis in three domains (water quality and contamination 28 sources, public-health risk 10, governance and infrastructure 8; household treatment 5 and surface water 7 overlap); no pooled estimate',
    effect_estimate=('Reported findings (not appraised): microbial and chemical contamination across municipal supply, groundwater, tanker water, traditional stone spouts and stored water, with some studies reporting contamination above 80% of samples; '
                     'groundwater maxima ammonia 3.0 mg/L, arsenic 1.5 mg/L, iron 7.5 mg/L, nitrate 37 mg/L, Water Quality Index up to 442.11; wastewater and river pathogens up to 8.1 log10 copies/L; resistance genes sul1 94%, intI1 83%, tet(A) 60%. '
                     'Governance: overlapping institutional mandates, weak enforcement and monitoring, delays in the Melamchi Water Supply Project sustaining vendor, tanker and unregulated groundwater dependence, and a hybrid formal-informal system; peri-urban and marginalised households bear the greatest exposure. No quantitative legal-institutional effect is estimated.'),
    study_design='systematic review (PRISMA 2020; narrative thematic synthesis of 45 sources; retrospectively registered on OSF; no quality appraisal tool applied)',
    model_type='systematic review with narrative thematic synthesis (no meta-analysis)',
    section='Abstract; Methods 2.1-2.7; Results 3.1-3.6 and Table 1; Discussion 4.1-4.6 (governance fragmentation in 4.3); Conclusions (full text)',
    exact_location='Methods 2.2-2.7 pp. 4-6 (search, eligibility, selection counts, extraction, synthesis, no appraisal); Results 3.5 governance and infrastructure challenges; Discussion 4.3 p. 14 (governance fragmentation and hybrid systems); Table 1 p. 8')
S015_NOTE = ("Full-text appraisal 2026-10-04 from the PDF in the researcher's Drive inbox (MDPI Water 18(12):1514, 20 pages read; figures not read; Table 1 is a representative domain-level summary, not a per-study table). "
             "Replaces the abstract-level entry of 2026-09-12 and the 3-of-16-item pilot of 2026-09-16. Registered retrospectively on OSF (osf.io/w94yr) during manuscript revision; no quality appraisal of the 45 included sources; no list of the 10 full-text exclusions. "
             "Legal/institutional content: governance fragmentation, overlapping mandates, weak enforcement and informal supply markets are narrative findings, not estimated effects.")
NA = 'Not applicable to AMSTAR 2 domains; item-level appraisal in 04_quality/appraisal_forms/S015_AMSTAR2.md (full text, ' + DATE + ')'


def m_ed(rows):
    done = []
    for r in rows:
        sid = r['study_id']
        if sid == 'S270':
            old = ("The old risk_of_bias_rating was NOT re-answered here because the full text shows the appraisal tool does not fit the design (see CAMPAIGN_NOTES.md); it is left for the reclassification step. ")
            if old in r['extraction_note']:
                r['extraction_note'] = r['extraction_note'].replace(old, "The condensed Legal Institutional Evidence Appraisal Framework rating of 2026-09-28 (extraction depth) was not re-answered in this pass; the tool fits the design. ")
                done.append('S270 note')
        if sid == 'S015':
            if r['risk_of_bias_rating'].startswith(RATING + ' (appraised ' + DATE):
                continue
            assert r['risk_of_bias_rating'].startswith('Not ratable') and r['risk_of_bias_tool'].replace(' ', '').startswith('AMSTAR2'), sid
            for k, v in S015.items():
                assert k in r, k
                r[k] = v
            r['risk_of_bias_rating'] = (f"{RATING} (appraised {DATE} against the official AMSTAR 2 checklist on the full text; item-level answers in 04_quality/appraisal_forms/S015_AMSTAR2.md; {BASIS}). "
                                        "Supersedes the earlier 'Not ratable' entry; eligibility as a systematic review confirmed from the methods text.")
            for k in ('selection_bias', 'measurement_bias', 'confounding', 'attrition', 'reporting_bias'):
                r[k] = NA
            r['extraction_note'] = S015_NOTE + ' record_id ' + r['record_id'] + '.'
            r['researcher'] = 'Claude-AI-extraction-2026-10-04 (full-text appraisal)'; r['date_extracted'] = DATE
            done.append('S015')
            cit = r['citation']
            L = [f"# AMSTAR 2 appraisal (full text) — S015", "", f"**Citation:** {cit}", "",
                 f"**Date appraised:** {DATE} · **Appraiser:** Claude-AI-appraisal-{DATE} · **Basis:** the full-text PDF in the researcher's Drive inbox (not committed). Figures and supplementary files were **not read**. Supersedes the 2026-09-16 abstract-level pilot. Appraised by the AI; not independently verified.", "",
                 f"**Overall confidence: {RATING}** — {BASIS}. Critical items: 2, 4, 7, 9, 11, 13, 15.", "",
                 "| # | Critical? | Item | Answer | Basis (from the text read) |", "|---|---|---|---|---|"]
            for i, name in ITEMS.items():
                a, b = ANS[i]
                L.append(f"| {i} | {'**Yes**' if i in CRIT else 'No'} | {name} | {a}{' (n/a)' if i in NA_ITEMS else ''} | {b} |")
            L += ["", "Method note: where the text is silent the answer is No (AMSTAR 2's own convention). AMSTAR 2 rating rule: no critical flaw = High or Moderate; one critical flaw = Low; more than one = Critically Low. A 'Partial Yes' is not a flaw; items 11, 12 and 15 do not apply to a review without meta-analysis and are not counted."]
            open('04_quality/appraisal_forms/S015_AMSTAR2.md', 'w', encoding='utf-8').write("\n".join(L) + "\n")
    return done


# ---------------------------------------------------------------- S142 effect-size row
S142_ADD = (" Full-text check 2026-10-04 (main text; the confidence intervals are in Supplementary Tables 5-6, which are not in the PDF): among high-poverty block groups, unincorporated status is associated with "
            "3.54 times the unsewered land area and 17.8 times the area unserved by centralized water (incidence rate ratios); among block groups without high poverty, 1.48 times the unsewered area; "
            "for high-poverty Outlying and Island communities the IRR for unsewered area exceeds 4.0, while Outlying communities without high poverty have IRR 0.91.")
S142_REASON = ("ANALYSIS_PLAN.md S2 -- single study; the incidence rate ratios printed in the main text (3.54, 17.8, 1.48) were recorded on 2026-10-04 from the full text, but their confidence intervals are in supplementary tables that were not "
               "available, the outcomes are land-area ratios (not odds ratios or percentage differences), and S037/S084/S057 measure different estimands, so no common metric exists -- left unpooled rather than approximated, per PROJECT_SPEC.md S14.")


def m_es(rows):
    for r in rows:
        if r['study_id'] == 'S142':
            if 'Full-text check 2026-10-04' in r['effect_estimate']:
                return 'S142 already enriched'
            assert r['exclusion_from_pooling_reason'].startswith('ANALYSIS_PLAN.md S2 -- exact incidence-rate-ratio effect size not reported'), r['exclusion_from_pooling_reason'][:60]
            r['effect_estimate'] += S142_ADD
            r['exclusion_from_pooling_reason'] = S142_REASON
            r['provenance_note'] += ' Full text read 2026-10-04 (npj Clean Water 7:125): sample 31,383 block groups in nine states confirmed; narrative direction confirmed; IRRs added from the main text (process_drive_inbox_2026-10-04.py).'
            return 'S142 enriched'
    raise AssertionError('S142 missing')


# ---------------------------------------------------------------- verification table
VERIFIED = {
    'S037': ('11', '11', '', 'verified', 'Table 2 in the full text: poor drinking-water exposure 83% vs 79% (p = 0.1363), overall DAC vulnerability 83% vs 81% (p = 0.3147), median household income $34,276 vs $36,450 (p = 0.7893), n = 97 ID-DAC and 56 GDC places; direction and labelling consistent'),
    'S104': ('7', '7', '', 'verified', 'abstract and Table 4: 47% (95% CI 45-49) reported at least one full day without water, provider range 18-76%, adjusted OR 1.31 for at least partly owning the home (flagged *** in Table 4, which the table legend defines as p < 0.01; the body text says p < 0.001; abstract p < 0.01), n = 3,047 households in 177 clusters; the body text gives 44-49% and 19-77% for the same quantities (the paper is internally slightly inconsistent)'),
    'S142': ('1', '1', '', 'verified_and_enriched', 'abstract: 31,383 block groups in nine states, negative binomial regression, unincorporated status and poverty associated with unserved area; IRRs (3.54, 17.8, 1.48, >4.0, 0.91) from the main text added 2026-10-04 (process_drive_inbox_2026-10-04.py); confidence intervals are in supplementary tables not supplied'),
    'S294': ('9', '9', '', 'verified', 'Table 3: diarrhea adjusted difference -0.01 (-0.05 to 0.03), length-for-age Z -0.01 (-0.15 to 0.12), WASH institutions index 0.40 (0.16 to 0.65); 332 villages in 121 clusters, 3,283 households (Table 2 denominators)'),
    'S388': ('5', '5', '', 'verified', 'Table 5 adjusted model: local management vs no management OR 3.733 (95% CI 2.993-4.657, p < 0.0001); 11,065 Afridev hand pumps analysed (the prose "about four times, 3.95-5.67" quotes the unadjusted 4.730)')}


def m_ver(rows):
    n = 0
    for r in rows:
        if r['study_id'] in VERIFIED and r['verdict'] == 'not_checked':
            a, b, c, v, note = VERIFIED[r['study_id']]
            r['numbers_in_row'], r['numbers_found_in_text'], r['numbers_not_found'] = a, b, c
            r['source_text'] = 'Drive inbox full text (2026-10-04 evening)'; r['verdict'] = v; r['note'] = note
            n += 1
    return n


print('extraction:', rw(ED, m_ed) or 'nothing new')
print('effect sizes:', rw(ES, m_es))
print('verification rows updated:', rw(VER, m_ver))


def m_fix(rows):
    n = 0
    for r in rows:
        if r['study_id'] == 'S104' and '(p < 0.001 in Table 4; abstract p < 0.01)' in r['note']:
            r['note'] = r['note'].replace('(p < 0.001 in Table 4; abstract p < 0.01)', '(flagged *** in Table 4, which the table legend defines as p < 0.01; the body text says p < 0.001; abstract p < 0.01)'); n += 1
    return n


print('verification note fixes:', rw(VER, m_fix))
