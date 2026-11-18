import csv, sys, re
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
    recs.append({'rid': row['record_id'], 'title': title, 'year': row['year'], 'db': row['database'], 'norm': norm_str})

from collections import defaultdict
by_norm = defaultdict(list)
for r in recs:
    if r['norm']:
        by_norm[r['norm']].append(r)
exact_groups = {k: v for k, v in by_norm.items() if len(v) > 1}

double_count_risk = []       # 2+ members ft_final == include
unretrieved_dup_of_included = []  # exactly 1 include, others not_retrievable/wrong_file_retrieved
already_e08_resolved = []    # 1 include, other(s) explicitly excluded E08 (duplicate)
excluded_other_reason = []   # 1 include, other(s) excluded but not E08
no_include_in_group = []     # zero members reached ft_final==include

for norm, group in exact_groups.items():
    statuses = []
    for r in group:
        f = ft.get(r['rid'], {})
        statuses.append((r, f.get('final_decision',''), f.get('exclusion_reason',''), f.get('full_text_status','')))
    includes = [s for s in statuses if s[1] == 'include']
    if len(includes) >= 2:
        double_count_risk.append((norm, statuses))
    elif len(includes) == 1:
        others = [s for s in statuses if s[1] != 'include']
        if all(s[3] in ('not_retrievable','wrong_file_retrieved') for s in others):
            unretrieved_dup_of_included.append((norm, statuses))
        elif any(s[2] == 'E08' for s in others):
            already_e08_resolved.append((norm, statuses))
        else:
            excluded_other_reason.append((norm, statuses))
    else:
        no_include_in_group.append((norm, statuses))

print(f"Total exact-title duplicate groups: {len(exact_groups)}")
print(f"  DOUBLE-COUNT RISK (2+ members currently 'include'): {len(double_count_risk)}")
print(f"  Unretrieved duplicate of an included study (1 include, rest not_retrievable/wrong_file_retrieved): {len(unretrieved_dup_of_included)}")
print(f"  Already E08-resolved duplicate (1 include, other explicitly excluded as duplicate): {len(already_e08_resolved)}")
print(f"  1 include, other(s) excluded for an unrelated reason: {len(excluded_other_reason)}")
print(f"  No member reached 'include' (not yet operationally relevant, or both/all excluded): {len(no_include_in_group)}")

print("\n=== DOUBLE-COUNT RISK groups (should be investigated if any) ===")
for norm, statuses in double_count_risk:
    print(f"-- {norm!r}")
    for r, fd, er, fs in statuses:
        print(f"   {r['rid']} | {r['year']} | {r['db']} | final={fd} | excl={er} | status={fs}")

def fmt(s):
    return f"{s[0]['rid']} ({s[0]['year']}, {s[0]['db']}, {s[3]})"

def fmt2(s):
    return f"{s[0]['rid']} (excl={s[2]}, status={s[3]})"

print("\n=== Unretrieved duplicates of an included study (full list) ===")
for norm, statuses in unretrieved_dup_of_included:
    inc = [s for s in statuses if s[1]=='include'][0]
    dups = [s for s in statuses if s[1]!='include']
    dup_str = ", ".join(fmt(s) for s in dups)
    print(f"-- {norm!r} | included: {inc[0]['rid']} ({inc[0]['year']}, {inc[0]['db']}) | unretrieved duplicate(s): {dup_str}")

print("\n=== Already E08-resolved duplicates (full list) ===")
for norm, statuses in already_e08_resolved:
    inc = [s for s in statuses if s[1]=='include'][0]
    dups = [s for s in statuses if s[1]!='include']
    print(f"-- {norm!r} | included: {inc[0]['rid']} | E08-excluded duplicate(s): " + ", ".join(s[0]['rid'] for s in dups))

print("\n=== 1 include, other(s) excluded for unrelated reason (worth a quick sanity look) ===")
for norm, statuses in excluded_other_reason:
    inc = [s for s in statuses if s[1]=='include'][0]
    others = [s for s in statuses if s[1]!='include']
    other_str = ", ".join(fmt2(s) for s in others)
    print(f"-- {norm!r} | included: {inc[0]['rid']} | other(s): {other_str}")
