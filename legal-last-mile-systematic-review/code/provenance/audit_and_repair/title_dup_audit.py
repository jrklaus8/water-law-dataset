import csv, sys, re, time
csv.field_size_limit(sys.maxsize)

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/01_search/deduplicated/deduplicated_records.csv"

STOPWORDS = {
    "a","an","the","of","in","and","for","to","on","with","from","by","at",
    "is","are","as","this","that","study","evidence","case","an","analysis",
    "review","water","sanitation","access","paper","towards","into","under",
    "between","among","its","their","new","study:"
}

def normalize(title):
    t = title.lower()
    t = re.sub(r'[^a-z0-9\s]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    tokens = [w for w in t.split() if w not in STOPWORDS and len(w) > 2]
    return t, tokens

with open(PATH) as f:
    rows = list(csv.DictReader(f))

print("total records:", len(rows))

recs = []
for row in rows:
    title = row['title'].strip()
    if not title:
        continue
    norm_str, tokens = normalize(title)
    recs.append({
        'rid': row['record_id'], 'title': title, 'year': row['year'],
        'authors': row['authors'][:60], 'db': row['database'],
        'norm': norm_str, 'tokens': frozenset(tokens),
    })

print("records with non-empty title:", len(recs))

# --- Pass 1: exact normalized-title match (order-preserving string) ---
from collections import defaultdict
by_norm = defaultdict(list)
for r in recs:
    if r['norm']:
        by_norm[r['norm']].append(r)

exact_groups = {k: v for k, v in by_norm.items() if len(v) > 1}
print("\n=== PASS 1: exact normalized-title duplicate groups:", len(exact_groups), "===")

t0 = time.time()

# --- Pass 2: near-duplicate via token-Jaccard, blocked by (year, min significant token) ---
def min_token(tokens):
    return min(tokens) if tokens else None

blocks = defaultdict(list)
for r in recs:
    if not r['tokens']:
        continue
    mt = min_token(r['tokens'])
    blocks[(r['year'], mt)].append(r)
    # also block on year-1 and year+1 min token to catch preprint/final-pub year drift
    try:
        y = int(r['year'])
        blocks[(str(y-1), mt)].append(r)
        blocks[(str(y+1), mt)].append(r)
    except ValueError:
        pass

def jaccard(a, b):
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0

seen_pairs = set()
near_dupes = []
THRESHOLD = 0.75

for key, group in blocks.items():
    if len(group) < 2 or len(group) > 60:  # skip pathologically large blocks (common min-token, low signal)
        continue
    n = len(group)
    for i in range(n):
        for j in range(i+1, n):
            a, b = group[i], group[j]
            if a['rid'] == b['rid']:
                continue
            pair_key = tuple(sorted([a['rid'], b['rid']]))
            if pair_key in seen_pairs:
                continue
            sim = jaccard(a['tokens'], b['tokens'])
            if sim >= THRESHOLD and a['norm'] != b['norm']:  # exact matches already caught in pass 1
                seen_pairs.add(pair_key)
                near_dupes.append((sim, a, b))

near_dupes.sort(key=lambda x: -x[0])
elapsed = time.time() - t0
print(f"\n=== PASS 2: near-duplicate candidate pairs (Jaccard >= {THRESHOLD}): {len(near_dupes)} === (blocking+compare took {elapsed:.1f}s)")

# Write full output to file for review
import json
with open("/tmp/claude-0/-home-user-water-law-dataset/13a4d716-bf67-5f8e-b123-127698a45259/scratchpad/title_dup_results.txt", "w") as out:
    out.write(f"=== PASS 1: exact normalized-title duplicate groups: {len(exact_groups)} ===\n")
    for norm, group in exact_groups.items():
        out.write(f"-- {norm!r}\n")
        for r in group:
            out.write(f"     {r['rid']} | {r['year']} | {r['db']} | {r['authors']} | {r['title']}\n")
    out.write(f"\n=== PASS 2: near-duplicate candidate pairs: {len(near_dupes)} ===\n")
    for sim, a, b in near_dupes:
        out.write(f"-- sim={sim:.3f}\n")
        out.write(f"   A: {a['rid']} | {a['year']} | {a['db']} | {a['authors']} | {a['title']}\n")
        out.write(f"   B: {b['rid']} | {b['year']} | {b['db']} | {b['authors']} | {b['title']}\n")

print("Full results written to title_dup_results.txt")
