#!/usr/bin/env python3
"""Compute every headline figure this project quotes, directly from the CSV databases.

Why this exists: figures were originally typed by hand into a dozen documents and repeatedly went stale (see
00_admin/audits/2026-09-28_repository_audit.md). This module is the single, reproducible source of the numbers; the
documents are checked against it by verify_repository.py.

Usage (from the project root, legal-last-mile-systematic-review/):
    python3 code/analysis/current_figures.py            # print figures
    python3 code/analysis/current_figures.py --write    # also (re)write 00_admin/CURRENT_FIGURES.md and current_figures.json

No third-party dependencies. Read-only except for the two output files under 00_admin/ when --write is given.
"""
import csv, json, re, sys
from collections import Counter
from pathlib import Path

csv.field_size_limit(sys.maxsize)
ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    'ft': ROOT / '02_screening/full_text/full_text_screening_database.csv',
    'el': ROOT / '02_screening/exclusion_log/exclusion_log.csv',
    'ed': ROOT / '03_extraction/extracted_data/extraction_database.csv',
    'em': ROOT / '05_analysis/descriptive/evidence_map.csv',
    'es': ROOT / '05_analysis/effect_sizes/effect_sizes.csv',
    'map': ROOT / '03_extraction/extracted_data/study_record_map.csv',
    'links': ROOT / '03_extraction/extracted_data/linked_reports_2026-09-28.csv',
    'ta': ROOT / '02_screening/title_abstract/screening_database.csv',
}

# Tool classification: the EARLIEST tool keyword in `risk_of_bias_tool` wins. Substring matching anywhere in the string
# mis-buckets rows whose annotation text mentions a second tool (an error this project made and corrected on 2026-09-28).
TOOL_KEYS = [('RoB 2', 'RoB 2'), ('ROBINS-I', 'ROBINS-I'), ('JBI', 'JBI Cross-Sectional'), ('MMAT', 'MMAT'),
             ('CASP', 'CASP Qualitative'), ('AMSTAR', 'AMSTAR 2'), ('Legal Institutional', 'Legal Framework'), ('NONE', 'NONE')]
ABSTRACT_ONLY_PREFIXES = ('Extracted from published abstract', 'Extracted from abstract')


def read(key):
    with open(PATHS[key], newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def tool_of(text):
    best = None
    for kw, name in TOOL_KEYS:
        i = text.find(kw)
        if i >= 0 and (best is None or i < best[0]):
            best = (i, name)
    return best[1] if best else 'UNCLASSIFIED'


def compute():
    ft, el, ed, em, es, mp, links = (read(k) for k in ('ft', 'el', 'ed', 'em', 'es', 'map', 'links'))
    ta = read('ta')
    F = {}
    F['title_abstract_include'] = sum(r['final_decision'] == 'include' for r in ta)
    F['title_abstract_exclude'] = sum(r['final_decision'] == 'exclude' for r in ta)
    dec = Counter(r['final_decision'] or 'undecided' for r in ft)
    F['full_text_records'] = len(ft)
    F['full_text_include'], F['full_text_exclude'], F['full_text_undecided'] = dec['include'], dec['exclude'], dec['undecided']
    F['full_text_decided'] = dec['include'] + dec['exclude']
    und = Counter(r['full_text_status'] for r in ft if not r['final_decision'])
    F['unretrieved_not_retrievable'], F['unretrieved_wrong_file'] = und['not_retrievable'], und['wrong_file_retrieved']
    F['exclusion_log_rows'] = len(el)
    F['exclusion_by_code'] = dict(sorted(Counter(r['exclusion_code'] for r in el).items()))
    dec_rows = [r for r in ft if r['final_decision']]
    F['decided_blank_reviewer_1'] = sum(not r['reviewer_1'] for r in dec_rows)
    # Human confirmations only (labels `Human-reviewer2-...`); a second AI model's blind pass is counted separately.
    F['reviewer_2_confirmed_includes'] = sum(r['reviewer_2'].startswith('Human-') and r['final_decision'] == 'include' for r in ft)
    F['reviewer_2_second_model_rows'] = sum(r['reviewer_2'].startswith(('Codex-', 'Gemini-')) for r in ft)
    F['reviewer_2_second_model_conflicts'] = sum(r['reviewer_2'].startswith(('Codex-', 'Gemini-')) and r['conflict'].lower() == 'true' for r in ft)
    F['extraction_rows'] = len(ed)
    F['evidence_map_rows'] = len(em)
    ids = sorted(int(r['study_id'][1:]) for r in ed)
    F['study_id_max'] = f"S{ids[-1]}"
    present = set(ids)
    F['study_id_gaps'] = [f"S{i:03d}" for i in range(1, ids[-1] + 1) if i not in present]
    tools = Counter(tool_of(r['risk_of_bias_tool']) for r in ed)
    F['tools'] = {k: tools[k] for k in [n for _, n in TOOL_KEYS] if tools[k]}
    F['tool_unclassified'] = tools['UNCLASSIFIED']
    F['tool_applicable'] = len(ed) - tools['NONE']
    F['tool_applicable_unrated'] = sum(1 for r in ed if tool_of(r['risk_of_bias_tool']) != 'NONE' and not r['risk_of_bias_rating'].strip())
    F['none_blank_rating'] = sum(1 for r in ed if tool_of(r['risk_of_bias_tool']) == 'NONE' and not r['risk_of_bias_rating'].strip())
    F['none_not_applicable_note'] = sum(1 for r in ed if tool_of(r['risk_of_bias_tool']) == 'NONE' and r['risk_of_bias_rating'].startswith('NOT APPLICABLE'))
    F['causal_capable_designs'] = tools['ROBINS-I'] + tools['RoB 2']
    F['casp_plus_mmat'] = tools['CASP Qualitative'] + tools['MMAT']
    F['casp_mmat_legal_framework'] = F['casp_plus_mmat'] + tools['Legal Framework']
    jbi = [r for r in ed if tool_of(r['risk_of_bias_tool']) == 'JBI Cross-Sectional']
    F['jbi_high_concern'] = sum(r['risk_of_bias_rating'].startswith('High concern') for r in jbi)
    lf = [r for r in ed if tool_of(r['risk_of_bias_tool']) == 'Legal Framework']
    F['legal_framework_measurement_quality_populated'] = sum(bool(r['legal_measurement_quality'].strip()) for r in lf)
    F['abstract_only_extractions'] = sum(r['extraction_note'].startswith(ABSTRACT_ONLY_PREFIXES) for r in ed)
    F['quantitative_synthesis_eligible'] = sum(r['quantitative_synthesis_eligible'] == 'TRUE' for r in em)
    F['qualitative_synthesis_eligible'] = sum(r['qualitative_synthesis_eligible'] == 'TRUE' for r in em)
    F['effect_size_rows'] = len(es)
    F['effect_size_by_family'] = dict(sorted(Counter(r['synthesis_family'] or '(none: reasoned non-fit)' for r in es).items()))
    F['effect_size_rows_pooled'] = sum(r['included_in_pooled_estimate'] == 'TRUE' for r in es)
    elig = {r['study_id'] for r in em if r['quantitative_synthesis_eligible'] == 'TRUE'}
    F['effect_size_rows_from_eligible_studies'] = sum(r['study_id'] in elig for r in es)
    F['effect_size_rows_from_ineligible_studies'] = sum(r['study_id'] not in elig for r in es)
    F['linked_report_links'] = len(links)
    F['linked_same_underlying_data_yes'] = sum(r['same_underlying_data'] == 'yes' for r in links)
    F['linked_partial'] = sum(r['same_underlying_data'] == 'partial' for r in links)
    F['distinct_studies_definite_links'] = len(ed) - F['linked_same_underlying_data_yes']
    F['distinct_studies_incl_partial_links'] = len(ed) - F['linked_same_underlying_data_yes'] - F['linked_partial']
    # Jurisdiction coverage. `country` and `legal_system` are FREE TEXT, not controlled vocabularies (see DATA_DICTIONARY.md),
    # so these are rule-based buckets, stated here so they can be challenged.
    multi_re = re.compile(r'[;/&,]| and |multi|global|various|several|worldwide|international', re.I)
    # single countries whose official names contain " and " must not be read as two countries (found in the 2026-10-04 code review: Trinidad and Tobago was bucketed as multi-country)
    and_names = re.compile(r'trinidad and tobago|bosnia and herzegovina|antigua and barbuda|saint kitts and nevis|st\.? kitts and nevis|saint vincent and the grenadines|sao tome and principe|s[aã]o tom[eé] and pr[ií]ncipe|turks and caicos', re.I)
    countries = [r['country'].strip() for r in ed]
    is_multi = lambda c: bool(multi_re.search(and_names.sub('', c)))
    single = Counter(c for c in countries if c and not is_multi(c))
    F['country_single_name_studies'] = sum(single.values())
    F['country_multi_or_regional_studies'] = sum(1 for c in countries if c and is_multi(c))
    F['country_blank_studies'] = sum(1 for c in countries if not c)
    F['country_top10_single_name'] = single.most_common(10)
    F['country_distinct_single_name_values'] = len(single)
    def legal_bucket(v):
        v = v.strip().lower()
        if not v:
            return 'blank'
        has_c, has_v = 'common' in v, 'civil' in v
        if (has_c and has_v) or any(k in v for k in ('mixed', 'hybrid', 'pluralis', 'customary')):
            return 'mixed / both / customary'
        return 'common law' if has_c else 'civil law' if has_v else 'other'
    F['legal_system_buckets'] = dict(sorted(Counter(legal_bucket(r['legal_system']) for r in ed).items()))
    mc = Counter(r['mechanism_certainty'].strip() for r in ed)
    numeric = {k: mc.get(k, 0) for k in ('0', '1', '2', '3', '4')}
    F['mechanism_certainty_numeric'] = numeric
    F['mechanism_certainty_narrative_text'] = len(ed) - sum(numeric.values())
    rob = Counter(re.split(r'[ (,]', r['risk_of_bias_rating'].strip())[0] for r in ed if tool_of(r['risk_of_bias_tool']) == 'ROBINS-I')
    F['robins_i_ratings'] = dict(rob)
    F['rob2_ratings'] = dict(Counter(re.split(r'[(,]', r['risk_of_bias_rating'])[0].strip() for r in ed if tool_of(r['risk_of_bias_tool']) == 'RoB 2'))
    n = len(ed)
    F['tool_share_pct'] = {k: round(100 * v / n, 1) for k, v in F['tools'].items()}
    return F


def render(F):
    T = F['tools']
    lines = ["# Current figures (generated — do not edit by hand)", "",
             "Produced by `code/analysis/current_figures.py --write` from the CSV databases; `code/analysis/verify_repository.py`",
             "checks that the current-status documents quote these values. If a document disagrees with this file, this file is right",
             "(or the databases changed and this file needs regenerating — run the script). Historical, dated documents",
             "(`CHANGELOG.md` entries, audit reports, `preliminary_*` logs) intentionally keep the figures that were true when written.", "",
             "## Screening", "",
             "| Stage | Figure |", "|---|---|",
             f"| Title/abstract | {F['title_abstract_include']:,} include / {F['title_abstract_exclude']:,} exclude |",
             f"| Full-text records tracked | {F['full_text_records']:,} |",
             f"| Full-text decided | {F['full_text_decided']:,} ({F['full_text_include']:,} include / {F['full_text_exclude']:,} exclude) |",
             f"| Never decided (retrieval closed) | {F['full_text_undecided']:,} ({F['unretrieved_not_retrievable']:,} not_retrievable, {F['unretrieved_wrong_file']:,} wrong_file_retrieved) |",
             f"| Exclusion-log rows | {F['exclusion_log_rows']:,} — by code: " + ", ".join(f"{k} {v}" for k, v in F['exclusion_by_code'].items()) + " |",
             f"| Decided rows with blank reviewer_1 | {F['decided_blank_reviewer_1']} |",
             f"| Includes confirmed by a human reviewer_2 | {F['reviewer_2_confirmed_includes']} |",
             f"| Decided rows blind-re-screened by a second AI model (reviewer_2 `Codex-…`) / conflicts | {F['reviewer_2_second_model_rows']} / {F['reviewer_2_second_model_conflicts']} |", "",
             "## Extraction and classification", "",
             "| Item | Figure |", "|---|---|",
             f"| Extraction rows / evidence-map rows | {F['extraction_rows']:,} / {F['evidence_map_rows']:,} |",
             f"| Highest study ID; retired-ID gaps | {F['study_id_max']}; " + ", ".join(F['study_id_gaps']) + " |",
             f"| Quantitative-synthesis-eligible / qualitative-synthesis-eligible | {F['quantitative_synthesis_eligible']} / {F['qualitative_synthesis_eligible']:,} |",
             f"| Abstract/metadata-only extractions | {F['abstract_only_extractions']} |",
             f"| Linked-report links (same data yes / partial) | {F['linked_report_links']} ({F['linked_same_underlying_data_yes']} / {F['linked_partial']}) |",
             f"| Distinct studies (definite links / incl. partial) | {F['distinct_studies_definite_links']:,} / {F['distinct_studies_incl_partial_links']:,} |", "",
             "## Risk-of-bias tool distribution", "",
             "Method: the *earliest* tool keyword in `risk_of_bias_tool` decides (substring matching anywhere mis-buckets annotated rows).", "",
             "| Tool | Studies | % |", "|---|---|---|"]
    lines += [f"| {k} | {v:,} | {F['tool_share_pct'][k]} |" for k, v in T.items()]
    lines += ["", f"Tool-applicable studies (all tools except NONE): {F['tool_applicable']:,}; unrated among them: {F['tool_applicable_unrated']}. "
              f"NONE studies: {T.get('NONE', 0)} ({F['none_not_applicable_note']} with an explicit NOT APPLICABLE note, {F['none_blank_rating']} blank by design). "
              f"Causal-capable designs (ROBINS-I + RoB 2): {F['causal_capable_designs']}. CASP + MMAT: {F['casp_plus_mmat']}; with Legal Framework: {F['casp_mmat_legal_framework']}. "
              f"JBI \"High concern\" (sparse extraction): {F['jbi_high_concern']} of {T.get('JBI Cross-Sectional', 0)}. "
              f"Legal Framework studies with legal_measurement_quality populated: {F['legal_framework_measurement_quality_populated']} of {T.get('Legal Framework', 0)}.",
              "", "## Jurisdiction coverage (free-text fields; rule-based buckets, see current_figures.py)", "",
              f"`country`: {F['country_single_name_studies']:,} studies name exactly one country, {F['country_multi_or_regional_studies']} name several countries or a region, "
              f"{F['country_blank_studies']} are blank. Top single-country values: " + ", ".join(f"{k} {v}" for k, v in F['country_top10_single_name']) + ". "
              "`legal_system` buckets: " + ", ".join(f"{k} {v}" for k, v in F['legal_system_buckets'].items()) + ".",
              "", "## Certainty scale and ratings", "",
              "`mechanism_certainty` numeric levels: " + ", ".join(f"{k}: {v}" for k, v in F['mechanism_certainty_numeric'].items()) +
              f"; {F['mechanism_certainty_narrative_text']} studies carry narrative text instead of a 0-4 code. ROBINS-I ratings: " +
              ", ".join(f"{k} {v}" for k, v in F['robins_i_ratings'].items()) + ". RoB 2 ratings: " + ", ".join(f"{k.strip()} {v}" for k, v in F['rob2_ratings'].items()) + ".",
              "", "## Effect sizes", "",
              f"{F['effect_size_rows']} rows ({F['effect_size_rows_from_eligible_studies']} from quantitative-synthesis-eligible studies, "
              f"{F['effect_size_rows_from_ineligible_studies']} from a study not flagged eligible); by family: " +
              ", ".join(f"{k} {v}" for k, v in F['effect_size_by_family'].items()) + f"; rows pooled: {F['effect_size_rows_pooled']}.", ""]
    return "\n".join(lines)


if __name__ == '__main__':
    F = compute()
    if '--write' in sys.argv:
        (ROOT / '00_admin/current_figures.json').write_text(json.dumps(F, indent=2, ensure_ascii=False) + "\n", encoding='utf-8')
        (ROOT / '00_admin/CURRENT_FIGURES.md').write_text(render(F) + "\n", encoding='utf-8')
        print('wrote 00_admin/CURRENT_FIGURES.md and 00_admin/current_figures.json')
    else:
        print(render(F))
