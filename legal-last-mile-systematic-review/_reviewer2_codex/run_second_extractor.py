"""Fill the second-extractor sheet (03_extraction/second_extractor) for studies whose PDF text is
already available, using a non-Claude model (Codex CLI by default). Reads the BLANK sheet rows for
the target studies, groups by study_id, asks the model to check all 9 fields against the paper in one
call, and writes a FILLED copy plus per-study raw JSON for audit. Never edits the BLANK file.

Usage: python run_second_extractor.py [--provider codex|gemini] [study_id ...]
"""
import csv, json, os, re, subprocess, sys, time, datetime, shutil, argparse
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BLANK = os.path.join(ROOT, "03_extraction/second_extractor/second_extractor_sheet_BLANK_2026-09-29.csv")
MAP_CSV = os.path.join(ROOT, "03_extraction/extracted_data/study_record_map.csv")

ap = argparse.ArgumentParser()
ap.add_argument("--provider", choices=["codex", "gemini"], default="codex")
ap.add_argument("studies", nargs="*")
A = ap.parse_args()
PROVIDER = A.provider
if PROVIDER == "codex":
    MODEL = os.environ.get("R2_MODEL", "gpt-5.6-sol")
    EXE = shutil.which("codex") or "codex"
    LABEL = "Codex-%s-second-extractor-%s" % (MODEL, datetime.date.today().isoformat())
else:
    MODEL = os.environ.get("R2_MODEL", "gemini-2.5-flash")
    EXE = shutil.which("gemini") or "gemini"
    LABEL = "Gemini-%s-second-extractor-%s" % (MODEL, datetime.date.today().isoformat())
    os.environ["GEMINI_CLI_TRUST_WORKSPACE"] = "true"
    if not os.environ.get("GEMINI_API_KEY"):
        k = subprocess.run(["powershell", "-NoProfile", "-Command", "(Get-ItemProperty HKCU:\\Environment).GEMINI_API_KEY"],
                           capture_output=True, text=True).stdout.strip()
        if k:
            os.environ["GEMINI_API_KEY"] = k

RES = os.path.join(HERE, "results_2ndextractor_%s" % PROVIDER)
os.makedirs(RES, exist_ok=True)
MAX_CHARS = 160_000

csv.field_size_limit(sys.maxsize)
rows = list(csv.DictReader(open(BLANK, encoding="utf-8")))
sid2rid = {r["study_id"]: r["record_id"] for r in csv.DictReader(open(MAP_CSV, encoding="utf-8"))}
texts = {}
for f in os.listdir(os.path.join(HERE, "text")):
    m = re.match(r"(R[0-9A-F]{12})", f)
    if m and m.group(1) not in texts:
        texts[m.group(1)] = os.path.join(HERE, "text", f)

by_study = {}
for r in rows:
    by_study.setdefault(r["study_id"], []).append(r)

target = A.studies or [s for s in by_study if sid2rid.get(s, "") in texts]
target = [s for s in target if sid2rid.get(s, "") in texts]

PROMPT = """You are an independent second extractor checking a first extractor's work for a systematic review
("The Legal Last Mile": legal/administrative/institutional factors in household water and sanitation access).
Read the paper below, THEN look at each field the first extractor recorded and the citation/DOI metadata that
goes with it. For EACH field say whether the paper supports the first extractor's value:
"Y" = same substance (wording/rounding may differ), "N" = a real difference, "cannot_tell" = the paper does not
let you decide. Give the value you find in the paper (or your best read) and where (page/section).

== PAPER (study {sid}, record {rid}) ==
{paper}
== END PAPER ==

== FIELDS TO CHECK ==
{fields}

Respond with ONLY a JSON object:
{{"study_id": "{sid}",
 "checks": {{
   "<field_name>": {{"agrees": "Y|N|cannot_tell", "second_extractor_value": "your reading of the paper on this field",
                      "where": "page/section", "comment": "one clause if N or cannot_tell, else empty"}},
   ...
 }}
}}
Use exactly these field names as keys: {field_names}
"""


def run_model(prompt, out_path):
    tmp = out_path + ".last.txt"
    t0 = time.time()
    if PROVIDER == "codex":
        cmd = [EXE, "exec", "--skip-git-repo-check", "-s", "read-only", "-m", MODEL,
               "-c", 'model_reasoning_effort="high"', "-o", tmp, "-"]
        p = subprocess.run(cmd, input=prompt, text=True, encoding="utf-8", errors="replace",
                           capture_output=True, timeout=1500, cwd=HERE)
        last = open(tmp, encoding="utf-8", errors="replace").read() if os.path.exists(tmp) else ""
    else:
        cmd = [EXE, "-m", MODEL, "-p", "Follow the instructions in the input above and respond with ONLY the JSON object."]
        p = subprocess.run(cmd, input=prompt, text=True, encoding="utf-8", errors="replace",
                           capture_output=True, timeout=1500, cwd=HERE)
        last = p.stdout or ""
        open(tmp, "w", encoding="utf-8").write(last)
    dur = time.time() - t0
    m = re.search(r"\{.*\}", last, re.S)
    data = None
    if m:
        try:
            data = json.loads(m.group(0))
        except Exception:
            data = None
    return data, last, p.returncode, dur, (p.stderr or "")[-1500:]


def paper_text(rid):
    t = open(texts[rid], encoding="utf-8", errors="replace").read()
    return t[:MAX_CHARS] + ("\n[TRUNCATED]" if len(t) > MAX_CHARS else "")


def do_study(sid):
    out = os.path.join(RES, sid + ".json")
    if os.path.exists(out):
        return sid, "cached"
    rid = sid2rid[sid]
    srows = by_study[sid]
    field_list = "\n".join('- %s ("%s"): first extractor recorded "%s"' % (r["field"], r["what_to_check"], r["ai_value"]) for r in srows)
    field_names = ", ".join(r["field"] for r in srows)
    prompt = PROMPT.format(sid=sid, rid=rid, paper=paper_text(rid), fields=field_list, field_names=field_names)
    data, raw, rc, dur, err = run_model(prompt, out)
    rec = {"study_id": sid, "record_id": rid, "provider": PROVIDER, "model": MODEL, "label": LABEL,
           "seconds": round(dur), "exit_code": rc, "parsed": data, "raw_last_message": raw, "stderr_tail": err}
    json.dump(rec, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    n = sum(1 for v in ((data or {}).get("checks") or {}).values() if isinstance(v, dict) and v.get("agrees") == "N")
    return sid, "done, %d disagreements" % n


def log(msg):
    line = "[%s] %s" % (datetime.datetime.now().strftime("%H:%M:%S"), msg)
    print(line, flush=True)
    open(os.path.join(HERE, "run_2ndextractor_%s.log" % PROVIDER), "a", encoding="utf-8").write(line + "\n")


if __name__ == "__main__":
    log("provider=%s model=%s label=%s studies=%d" % (PROVIDER, MODEL, LABEL, len(target)))
    with ThreadPoolExecutor(3) as ex:
        for sid, res in ex.map(do_study, target):
            log("%s: %s" % (sid, res))
    log("ALL DONE")
