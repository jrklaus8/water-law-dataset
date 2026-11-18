"""2026-10-13: effect_sizes.csv row for S1166 (Jiang & Zheng 2014, Economic Development and Cultural Change 63(1):155-189), which the PI's A16 adjudication of 2026-10-13
reversed from exclude (E06) to include (record R69F53378C8F2). The study was read in full text (Drive inbox, 35 pages). The row records the study's one access-relevant estimate: Table 8, column 4 of the
domestic water supply population regression (log), PSP-majority coefficient in the corrective recoding, 0.046 (SE 0.026), significant at 10% only, N = 814 utility-years. The exposure (private ownership
of a water utility) does not map to Family A, B or C (PROJECT_SPEC section 8), so synthesis_family is left blank as a reasoned non-fit, the same treatment as S869 and the other ownership/PSP rows, and the row is not pooled.
A FULLTEXT_VERIFICATION row is added with the numbers checked against the text. Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
EP = '05_analysis/effect_sizes/effect_sizes.csv'
VP = '05_analysis/effect_sizes/FULLTEXT_VERIFICATION_2026-10-04.csv'
SID = 'S1166'


def read(p):
    raw = open(p, newline='', encoding='utf-8').read()
    crlf = '\r\n' in raw[:5000]
    with open(p, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f)
        return rd.fieldnames, list(rd), crlf


def write(p, fields, rows, crlf):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n')
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, p)


fields, rows, crlf = read(EP)
if any(r['study_id'] == SID for r in rows):
    print('effect row already present')
else:
    new = {k: '' for k in fields}
    new.update(
        study_id=SID,
        outcome_family='service_coverage',
        synthesis_family='',
        exposure_definition=("Majority private (nonstate) capital in a Chinese urban water utility ('PSP majority': nonstate sources hold more than 50% of the utility's capital; private sector participation "
                             "was opened to private investors on a pilot basis in 1992 and nationwide in 2002), measured from the capital-source codes of the National Bureau of Statistics industrial firm survey "
                             "with 27 corrective recodings, vs. state-owned utilities."),
        comparator_definition='The same utilities in years before private participation, and state-owned utilities (fixed-effects panel, 208 utilities in 192 cities, 1998-2007).',
        effect_measure='fixed-effects panel regression coefficient on the log domestic water supply population (Table 8, column 4, corrective PSP recoding, lagged utility variables and city controls)',
        effect_estimate=("PSP majority coefficient 0.046 (SE 0.026, significant at 10% only): about 4.6% more domestic water-service population under majority private ownership than under state ownership, N = 814. "
                         "Other Table 8 columns: PSP 0.026 (0.025) original and 0.037 (0.026) corrective; PSP minority 0.006 (0.034) and 0.015 (0.038); PSP-majority original coding 0.032 (0.026). "
                         "Domestic water supply (log): PSP majority -0.071 (0.038, 10%) original, -0.062 (0.047) corrective. Total urban water supply (log), N = 1,752: PSP majority -0.040 (0.030) and -0.055 (0.035). "
                         "The authors call the effects 'either statistically insignificant or marginally significant' and read the supply declines as possible leakage reduction."),
        standard_error='0.026',
        sample_size='814 utility-year observations (domestic water supply population); 208 utilities in 192 cities, 1998-2007',
        direction='positive (marginal: 10% level in one coding of PSP majority, not in the original coding or for PSP overall)',
        adjusted='TRUE (utility fixed effects, lagged utility variables, city controls)',
        evidence_status='OBSERVED',
        provenance_note=("extraction_database.csv S1166; source Jiang & Zheng 2014, Economic Development and Cultural Change 63(1):155-189, Table 8 (pp. 183-184). New inclusion by the PI's A16 adjudication of "
                         "2026-10-13; the original E06 exclusion had partly rested on the estimate being non-significant, which is not an exclusion criterion (open item A18). The abstract and introduction say 200 cities; "
                         "the Data section gives 208 utilities in 192 cities. The domestic service population is derived from industrial-survey variables, not from a household coverage or connection measure, which is why "
                         "the outcome measurement is rated low and ROBINS-I is Serious for this outcome. Only one estimate is recorded for the family (CODEBOOK section 12); the corrective-recoding PSP-majority coefficient was chosen "
                         "because the authors use it for the 4.6% reading, and the other columns are in effect_estimate."),
        included_in_pooled_estimate='FALSE',
        exclusion_from_pooling_reason=("ANALYSIS_PLAN.md section 2 decision tree: the exposure (majority private ownership of a utility) is an ownership and regulatory-structure variable that does not cleanly map to "
                                       "Family A (legal recognition), B (administrative assistance) or C (legal/administrative barriers), so synthesis_family is left blank as a reasoned non-fit, consistent with the S749/S795/S869 "
                                       "precedent; the outcome is a utility-level service population, not a household access measure; single study with this exposure-comparator, so pooling is not possible or meaningful "
                                       "(PROJECT_SPEC.md section 8)."),
    )
    rows.append(new)
    write(EP, fields, rows, crlf)
    print('effect row added for', SID, '(', len(rows), 'rows )')

vf, vrows, vcrlf = read(VP)
if any(r['study_id'] == SID for r in vrows):
    print('verification row already present')
else:
    v = {k: '' for k in vf}
    v.update(study_id=SID, synthesis_family='', numbers_in_row='9', numbers_found_in_text='9', numbers_not_found='',
             source_text='Drive inbox full text (2026-10-13)', verdict='verified',
             note=("Table 8 in the full text: domestic water supply population (log), N = 814, PSP 0.026 (0.025) and 0.037 (0.026), PSP majority 0.032 (0.026) and 0.046 (0.026, p < 0.10), PSP minority 0.006 (0.034) and 0.015 (0.038); "
                   "208 utilities in 192 cities in the Data section (abstract and introduction say 200 cities)"))
    vrows.append(v)
    write(VP, vf, vrows, vcrlf)
    print('verification row added')
