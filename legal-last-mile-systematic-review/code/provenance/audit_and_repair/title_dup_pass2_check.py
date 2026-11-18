import csv, sys, re, time
csv.field_size_limit(sys.maxsize)
BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"

with open(f"{BASE}/01_search/deduplicated/deduplicated_records.csv") as f:
    dedup = list(csv.DictReader(f))
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
    recs.append({'rid': row['record_id'], 'title': title, 'year': row['year'], 'db': row['database'], 'norm': norm_str, 'tokens': frozenset(tokens)})

def jaccard(a, b):
    if not a or not b:
        return 0.0
    inter = len(a & b); union = len(a | b)
    return inter/union if union else 0.0

from collections import defaultdict
blocks = defaultdict(list)
for r in recs:
    if not r['tokens']:
        continue
    mt = min(r['tokens'])
    blocks[(r['year'], mt)].append(r)
    try:
        y = int(r['year'])
        blocks[(str(y-1), mt)].append(r)
        blocks[(str(y+1), mt)].append(r)
    except ValueError:
        pass

seen = set()
near_dupes = []
THRESHOLD = 0.75
for key, group in blocks.items():
    if len(group) < 2 or len(group) > 60:
        continue
    n = len(group)
    for i in range(n):
        for j in range(i+1, n):
            a, b = group[i], group[j]
            if a['rid'] == b['rid']:
                continue
            pk = tuple(sorted([a['rid'], b['rid']]))
            if pk in seen:
                continue
            sim = jaccard(a['tokens'], b['tokens'])
            if sim >= THRESHOLD and a['norm'] != b['norm']:
                seen.add(pk)
                near_dupes.append((sim, a, b))

print("Near-duplicate pairs (Pass 2):", len(near_dupes))

both_include = 0
one_include_other_unretrieved = 0
for sim, a, b in near_dupes:
    fa = ft.get(a['rid'], {})
    fb = ft.get(b['rid'], {})
    da, db = fa.get('final_decision',''), fb.get('final_decision','')
    if da == 'include' and db == 'include':
        both_include += 1
        print(f"DOUBLE-COUNT RISK: sim={sim:.2f} | {a['rid']} ({a['title']}) | {b['rid']} ({b['title']})")
    elif (da=='include') != (db=='include'):
        # exactly one included
        other_status = fb.get('full_text_status','') if da=='include' else fa.get('full_text_status','')
        if other_status in ('not_retrievable','wrong_file_retrieved'):
            one_include_other_unretrieved += 1

print("Both sides 'include' (double-count risk):", both_include)
print("One side include, other unretrieved/wrong-file (latent, already resolved by non-retrieval):", one_include_other_unretrieved)
