#!/usr/bin/env python3
"""Does Legal Data Hunter hold full text for the Canadian rows of the deposited dataset?

Samples citations stratified by court, calls the LDH `resolve_reference` tool, records resolved yes/no, the source, and the size of the full text.
Stores NO decision text. It stops at the first "usage limit reached" reply: the free plan allows 20 searches per 24 hours, so a 140-citation test needs a paid plan
(or several days). A run that hits the limit must be discarded, not read as zero coverage. The API key is read from the environment (LDH_API_KEY) and is never written anywhere.

Usage: LDH_API_KEY=... python validation/canada_ldh/ldh_coverage_test.py CODED_CSV OUT_CSV [PER_COURT=6] [MAX_COURTS=25]
"""
import collections
import csv
import json
import os
import random
import re
import sys
import time
import urllib.request

csv.field_size_limit(10 ** 9)
KEY = os.environ.get("LDH_API_KEY", "")
if not KEY:
    sys.exit("set LDH_API_KEY")
URL = "https://legaldatahunter.com/mcp"
H = {"Content-Type": "application/json", "Authorization": "Bearer " + KEY, "Accept": "application/json, text/event-stream"}


def rpc(method, params, i=1):
    body = json.dumps({"jsonrpc": "2.0", "id": i, "method": method, "params": params}).encode()
    req = urllib.request.Request(URL, data=body, headers=H, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read().decode("utf-8", errors="replace")
    for line in reversed(raw.split("\n")):
        if line.startswith("data: ") and line[6:] != "[DONE]":
            p = json.loads(line[6:])
            if "error" in p:
                return {"_error": p["error"]}
            sc = p.get("result", {}).get("structuredContent", {})
            if sc.get("limit_reached"):
                sys.exit("LDH usage limit reached (%s plan, resets %s). Stopping; no result is valid after this point." % (sc.get("plan"), sc.get("resets_at")))
            t = p.get("result", {}).get("content", [{}])[0].get("text", "{}")
            try:
                return json.loads(t)
            except Exception:  # noqa: BLE001
                return {"_raw": t[:200]}
    try:
        return json.loads(raw)
    except Exception:  # noqa: BLE001
        return {"_raw": raw[:200]}


rows = [r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8-sig")) if r["country"] == "Canada"]
per = int(sys.argv[3]) if len(sys.argv) > 3 else 6
maxc = int(sys.argv[4]) if len(sys.argv) > 4 else 25
by = collections.defaultdict(list)
for r in rows:
    by[r["tribunal"]].append(r)
random.seed(2027)
courts = [c for c, _ in sorted(by.items(), key=lambda x: -len(x[1]))][:maxc]
sample = [r for c in courts for r in random.sample(by[c], min(per, len(by[c])))]
rpc("initialize", {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "research", "version": "1.0"}})
time.sleep(1)
from concurrent.futures import ThreadPoolExecutor  # noqa: E402


def one(args):
    n, r = args
    cit = re.sub(r"\s*\(CanLII\)\s*$", "", r["case_id"]).strip()
    res = {"_error": "timeout_or_network"}
    for attempt in range(3):
        try:
            res = rpc("tools/call", {"name": "resolve_reference", "arguments": {"reference": cit, "hint_country": "CA", "hint_type": "case_law"}}, n + 1)
            break
        except SystemExit:
            raise
        except Exception:  # noqa: BLE001
            time.sleep(5 * (attempt + 1))
    docs = res.get("documents") or []
    d = docs[0] if docs else {}
    return {"tribunal": r["tribunal"], "citation": cit, "resolved": int(bool(res.get("resolved"))), "reason": res.get("reason", "") or ("ERROR" if res.get("_error") else ""),
            "source": d.get("source", ""), "full_text_size": d.get("full_text_size", ""), "date": d.get("date", "")}


with ThreadPoolExecutor(max_workers=3) as ex:
    out = list(ex.map(one, enumerate(sample, 1)))
with open(sys.argv[2], "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
    w.writeheader()
    w.writerows(out)
errors = [o for o in out if o["reason"] == "ERROR"]
out_ok = [o for o in out if o["reason"] != "ERROR"]
print("errors excluded from the rate:", len(errors))
t = collections.defaultdict(lambda: [0, 0])
for o in out_ok:
    t[o["tribunal"]][0] += 1
    t[o["tribunal"]][1] += o["resolved"]
print("overall resolved:", sum(o["resolved"] for o in out_ok), "of", len(out_ok), "(errors excluded)")
for c, (n, k) in sorted(t.items(), key=lambda x: -x[1][0]):
    print("  %-8s %2d of %2d" % (c, k, n))
print("reasons:", collections.Counter(o["reason"] for o in out if not o["resolved"]))
