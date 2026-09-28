import csv, sys, re
csv.field_size_limit(sys.maxsize)

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"

with open(f"{BASE}/01_search/deduplicated/deduplicated_records.csv") as f:
    dedup = list(csv.DictReader(f))
with open(f"{BASE}/02_screening/title_abstract/screening_database.csv") as f:
    scr = {r['record_id']: r for r in csv.DictReader(f)}
with open(f"{BASE}/02_screening/full_text/full_text_screening_database.csv") as f:
    ft = {r['record_id']: r for r in csv.DictReader(f)}

STOPWORDS = {
    "a","an","the","of","in","and","for","to","on","with","from","by","at",
    "is","are","as","this","that","study","evidence","case","analysis",
    "review","water","sanitation","access","paper","towards","into","under",
    "between","among","its","their","new",
}

def normalize(title):
    t = title.lower()
    t = re.sub(r'[^a-z0-9\s]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    tokens = [w for w in t.split() if w not in STOPWORDS and len(w) > 2]
    return t, tokens

recs = []
for row in dedup:
    title = row['title'].strip()
    if not title:
        continue
    norm_str, tokens = normalize(title)
    recs.append({
        'rid': row['record_id'], 'title': title, 'year': row['year'],
        'authors': row['authors'], 'db': row['database'],
        'norm': norm_str, 'tokens': frozenset(tokens),
    })

from collections import defaultdict
by_norm = defaultdict(list)
for r in recs:
    if r['norm']:
        by_norm[r['norm']].append(r)
exact_groups = {k: v for k, v in by_norm.items() if len(v) > 1}

def status(rid):
    s = scr.get(rid, {})
    tad = s.get('title_abstract_decision', '')
    fd_screen = s.get('final_decision', '')
    f = ft.get(rid, {})
    fulltext_decision = f.get('full_text_decision', '')
    fd_full = f.get('final_decision', '')
    return {
        'title_abstract_decision': tad,
        'ta_final_decision': fd_screen,
        'in_full_text_stage': rid in ft,
        'full_text_decision': fulltext_decision,
        'ft_final_decision': fd_full,
    }

def first_name_token(authors):
    a = authors.lower()
    a = re.sub(r'[^a-z\s]', ' ', a)
    toks = a.split()
    return toks[0] if toks else ''

live_both_included = []
generic_titles = []
other_groups = []

GENERIC = {
    "introduction","conclusion","discussion","editorial","bibliography",
    "reviews","review","who s who","news briefs","rating changes",
    "editorial foreword","editor s note","publications received",
    "washington news", "water", "water and life", "keepers of the water",
}

for norm, group in exact_groups.items():
    statuses = [(r, status(r['rid'])) for r in group]
    both_included = [r for r, s in statuses if s['title_abstract_decision'] == 'include']
    if norm in GENERIC or (len(group) >= 2 and len(set(first_name_token(r['authors']) for r in group)) == len(group) and norm in GENERIC):
        generic_titles.append((norm, group, statuses))
    elif len(both_included) >= 2:
        live_both_included.append((norm, group, statuses))
    else:
        other_groups.append((norm, group, statuses))

print(f"Total exact-title groups: {len(exact_groups)}")
print(f"  Generic/recurring section-header titles (flagged, not counted as candidates): {len(generic_titles)}")
print(f"  LIVE: 2+ members both title_abstract 'include': {len(live_both_included)}")
print(f"  Other (at least one side not included, or singly included): {len(other_groups)}")

print("\n" + "="*100)
print("LIVE-BOTH-INCLUDED groups (both sides currently marked include at title/abstract stage):")
print("="*100)
for norm, group, statuses in live_both_included:
    print(f"\n-- {norm!r}")
    for r, s in statuses:
        print(f"   {r['rid']} | {r['year']} | {r['db']} | {r['authors'][:50]} | ta_decision={s['title_abstract_decision']} | ft_stage={s['in_full_text_stage']} | ft_decision={s['full_text_decision']} | ft_final={s['ft_final_decision']}")
