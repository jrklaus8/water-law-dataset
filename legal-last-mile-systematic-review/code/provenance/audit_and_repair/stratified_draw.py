import csv, random
from collections import Counter, defaultdict

REGION_MAP = {
 'Brazil':'Latin America & Caribbean','India':'South Asia','South Africa':'Sub-Saharan Africa',
 'United States':'North America','Kenya':'Sub-Saharan Africa','Ghana':'Sub-Saharan Africa',
 'Mexico':'Latin America & Caribbean','Indonesia':'East Asia & Pacific','Uganda':'Sub-Saharan Africa',
 'Nigeria':'Sub-Saharan Africa','Bangladesh':'South Asia','Ethiopia':'Sub-Saharan Africa',
 'Tanzania':'Sub-Saharan Africa','Peru':'Latin America & Caribbean','Colombia':'Latin America & Caribbean',
 'Malawi':'Sub-Saharan Africa','Nepal':'South Asia','Argentina':'Latin America & Caribbean',
 'Zimbabwe':'Sub-Saharan Africa','Cameroon':'Sub-Saharan Africa','Canada':'North America',
 'Pakistan':'South Asia','Chile':'Latin America & Caribbean','Philippines':'East Asia & Pacific',
 'Costa Rica':'Latin America & Caribbean','Zambia':'Sub-Saharan Africa','United Kingdom':'Europe & Central Asia',
 'Democratic Republic of Congo':'Sub-Saharan Africa','Burkina Faso':'Sub-Saharan Africa',
 'Nicaragua':'Latin America & Caribbean','Ecuador':'Latin America & Caribbean','Bolivia':'Latin America & Caribbean',
 'Vietnam':'East Asia & Pacific','Slovakia':'Europe & Central Asia','Namibia':'Sub-Saharan Africa',
 'Portugal':'Europe & Central Asia','Spain':'Europe & Central Asia','Sweden':'Europe & Central Asia',
 'China':'East Asia & Pacific','Democratic Republic of the Congo':'Sub-Saharan Africa','Mali':'Sub-Saharan Africa',
 'Germany':'Europe & Central Asia','Trinidad and Tobago':'Latin America & Caribbean','Hungary':'Europe & Central Asia',
 'France':'Europe & Central Asia','Senegal':'Sub-Saharan Africa','Iraq':'Middle East & North Africa',
 'Australia':'East Asia & Pacific','Sri Lanka':'South Asia','Rwanda':'Sub-Saharan Africa',
 'Mozambique':'Sub-Saharan Africa','Oman':'Middle East & North Africa','Myanmar':'East Asia & Pacific',
}

def region_of(country):
    c = country.strip()
    if not c:
        return 'Other/unmapped'
    if ';' in c or '/' in c or 'multi-country' in c.lower() or 'global' in c.lower():
        return 'Multi-country / global'
    return REGION_MAP.get(c, 'Other/unmapped')

def design_class_of(s):
    s = s.lower()
    if 'doctrinal' in s: return 'doctrinal'
    if 'jurimetric' in s: return 'jurimetric'
    if 'systematic_review' in s or 'systematic review' in s or 'secondary' in s: return 'systematic_review_secondary'
    if 'quasi' in s or 'experimental' in s: return 'quasi_experimental'
    if 'mixed' in s: return 'mixed_methods'
    if 'qualitative' in s: return 'qualitative'
    if 'observational' in s or 'cross-sectional' in s or 'cross_sectional' in s or 'survey' in s or 'longitudinal' in s or 'quantitative' in s: return 'observational'
    return 'other'

CANON_MECH = {'DISCRETION_ACCOMMODATION','ENFORCEMENT','ELIGIBILITY','BURDEN'}
CANON_OUTCOME = {'effective_access','primary_connection','administrative_outcome','economic_access',
                 'water_access','service_reliability','affordability','service_coverage',
                 'service_quantity','sanitation_access','service_quality'}

def mech_code(m):
    m = m.strip()
    return m if m in CANON_MECH else ('MULTIPLE' if m == 'MULTIPLE' else 'OTHER_BESPOKE')

def outcome_code(o):
    o = o.strip()
    return o if o in CANON_OUTCOME else 'OTHER_COMPOSITE'

# load extraction db for country
with open('03_extraction/extracted_data/extraction_database.csv') as f:
    ext = {r['study_id']: r for r in csv.DictReader(f)}

# load evidence map for design class / mechanism / outcome
with open('05_analysis/descriptive/evidence_map.csv') as f:
    em = {r['study_id']: r for r in csv.DictReader(f)}

study_ids = sorted(set(ext) & set(em))
print(f'Studies with both extraction + evidence_map rows: {len(study_ids)}')

records = []
for sid in study_ids:
    e, m = ext[sid], em[sid]
    region = region_of(e['country'])
    design = design_class_of(m['study_design_class'])
    code = (mech_code(m['mechanism_family']), outcome_code(m['outcome_family']))
    records.append({'study_id': sid, 'region': region, 'design': design, 'code': code})

# region totals -> proportional quota, target N=120, floor 3
TARGET_N = 120
FLOOR = 3
region_counts = Counter(r['region'] for r in records)
total = sum(region_counts.values())
raw_quota = {reg: TARGET_N * cnt / total for reg, cnt in region_counts.items()}
quota = {reg: max(FLOOR, round(q)) for reg, q in raw_quota.items()}
# cap quota at available count in region
quota = {reg: min(quota[reg], region_counts[reg]) for reg in quota}

print()
print('Region quotas (target N=120, floor=3, capped at availability):')
for reg in sorted(quota, key=lambda r: -region_counts[r]):
    print(f'  {reg:35s} available={region_counts[reg]:4d}  quota={quota[reg]:4d}')
print(f'  {"TOTAL":35s} available={total:4d}  quota={sum(quota.values()):4d}')

# saturation-based stratified draw within region, sub-stratified by design class order (rotate through design classes present)
random.seed(42)
by_region = defaultdict(list)
for r in records:
    by_region[r['region']].append(r)

IN, OUT = [], []
stratum_report = []

for reg, recs in by_region.items():
    q = quota[reg]
    # group by design within region, shuffle each group, then round-robin across design groups
    by_design = defaultdict(list)
    for r in recs:
        by_design[r['design']].append(r)
    for d in by_design:
        random.shuffle(by_design[d])
    design_order = sorted(by_design, key=lambda d: -len(by_design[d]))

    seen_codes = set()
    drawn = []
    consecutive_no_new = 0
    stop_reason = None
    pools = {d: list(by_design[d]) for d in design_order}
    # ensure floor 1 for doctrinal/jurimetric if present, drawn first
    priority = [d for d in ('doctrinal','jurimetric') if pools.get(d)]
    draw_order = []
    for d in priority:
        if pools[d]:
            draw_order.append(pools[d].pop(0))
    # round robin remaining
    idx = 0
    active = [d for d in design_order]
    while any(pools[d] for d in active):
        d = active[idx % len(active)]
        if pools[d]:
            draw_order.append(pools[d].pop(0))
        idx += 1

    for rec in draw_order:
        if len(drawn) >= q:
            stop_reason = 'quota_reached'
            break
        is_new = rec['code'] not in seen_codes
        seen_codes.add(rec['code'])
        drawn.append(rec)
        consecutive_no_new = 0 if is_new else consecutive_no_new + 1
        if consecutive_no_new >= 4:  # 4 consecutive = "5th+ in a row adds nothing new" -> saturation after this point
            stop_reason = 'saturation'
            break
    else:
        if stop_reason is None:
            stop_reason = 'stratum_exhausted'

    drawn_ids = {r['study_id'] for r in drawn}
    IN.extend(drawn)
    OUT.extend(r for r in recs if r['study_id'] not in drawn_ids)
    stratum_report.append((reg, len(recs), q, len(drawn), len(seen_codes), stop_reason))

print()
print(f'{"Region":35s} {"avail":>6s} {"quota":>6s} {"drawn":>6s} {"codes":>6s}  stop_reason')
for reg, avail, q, drawn_n, codes_n, reason in sorted(stratum_report, key=lambda x: -x[1]):
    print(f'{reg:35s} {avail:6d} {q:6d} {drawn_n:6d} {codes_n:6d}  {reason}')

print()
print(f'TOTAL IN (deep-extraction subsample): {len(IN)}')
print(f'TOTAL OUT (eligibility-only / not resampled): {len(OUT)}')
print()

reason_counts = Counter(r for *_, r in stratum_report)
print('Stop-reason summary across regions:', dict(reason_counts))

with open('/tmp/claude-0/-home-user-water-law-dataset/13a4d716-bf67-5f8e-b123-127698a45259/scratchpad/subsample_in.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['study_id','region','design','mechanism_code','outcome_code'])
    for r in sorted(IN, key=lambda x: x['study_id']):
        w.writerow([r['study_id'], r['region'], r['design'], r['code'][0], r['code'][1]])

with open('/tmp/claude-0/-home-user-water-law-dataset/13a4d716-bf67-5f8e-b123-127698a45259/scratchpad/subsample_out.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['study_id','region','design','mechanism_code','outcome_code'])
    for r in sorted(OUT, key=lambda x: x['study_id']):
        w.writerow([r['study_id'], r['region'], r['design'], r['code'][0], r['code'][1]])
