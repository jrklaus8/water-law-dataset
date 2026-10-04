"""Two-model adversarial debate on open judgment calls (A3, A5, and the narrative-review scope
question), using the Codex CLI and Gemini CLI as independent, non-Claude voices. Round 1: each model
states its position cold. Round 2: each model sees the other's round-1 position and gives a final
verdict, explicitly agreeing or disagreeing. Nothing in the repository's data is changed; output is a
report for the researcher.
"""
import json, os, re, subprocess, sys, time, datetime, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "debate")
os.makedirs(OUT, exist_ok=True)

CODEX_EXE = shutil.which("codex") or "codex"
GEMINI_EXE = shutil.which("gemini") or "gemini"
CODEX_MODEL = "gpt-5.6-sol"
GEMINI_MODEL = os.environ.get("R2_GEMINI_MODEL", "gemini-3.1-flash-lite")
if not os.environ.get("GEMINI_API_KEY"):
    k = subprocess.run(["powershell", "-NoProfile", "-Command", "(Get-ItemProperty HKCU:\\Environment).GEMINI_API_KEY"],
                       capture_output=True, text=True).stdout.strip()
    if k:
        os.environ["GEMINI_API_KEY"] = k
os.environ["GEMINI_CLI_TRUST_WORKSPACE"] = "true"


def ask(provider, prompt, tag):
    tmp = os.path.join(OUT, tag + ".last.txt")
    t0 = time.time()
    if provider == "codex":
        cmd = [CODEX_EXE, "exec", "--skip-git-repo-check", "-s", "read-only", "-m", CODEX_MODEL,
               "-c", 'model_reasoning_effort="high"', "-o", tmp, "-"]
        p = subprocess.run(cmd, input=prompt, text=True, encoding="utf-8", errors="replace",
                           capture_output=True, timeout=1200, cwd=HERE)
        last = open(tmp, encoding="utf-8", errors="replace").read() if os.path.exists(tmp) else ""
    else:
        cmd = [GEMINI_EXE, "-m", GEMINI_MODEL, "-p", "Follow the instructions in the input above."]
        p = subprocess.run(cmd, input=prompt, text=True, encoding="utf-8", errors="replace",
                           capture_output=True, timeout=1200, cwd=HERE)
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
    rec = {"provider": provider, "model": CODEX_MODEL if provider == "codex" else GEMINI_MODEL,
           "seconds": round(dur), "exit_code": p.returncode, "parsed": data, "raw": last,
           "stderr_tail": (p.stderr or "")[-1000:]}
    json.dump(rec, open(os.path.join(OUT, tag + ".json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return data, last


QUESTIONS = {}

QUESTIONS["narrative_reviews"] = {
    "title": "Do the 13 narrative/non-systematic reviews (tool NONE) satisfy inclusion criterion 3?",
    "context": open(os.path.join(ROOT, "INCLUSION_EXCLUSION.md"), encoding="utf-8").read() + """

== THE OPEN ITEM (from 00_admin/DECISIONS_AND_OPEN_ITEMS.md) ==
13 included studies (S079, S320, S321, S322, S326, S429, S430, S436, S440, S466, S479, S480, S482) are
self-described narrative or non-systematic reviews with risk-of-bias tool NONE. Do they satisfy inclusion
criterion 3 ("empirical evidence or a systematic empirical synthesis")? For comparison: S356, a
method-less policy overview with no primary data, WAS excluded under code E05 on 2026-09-28. These 13 are
narrative reviews OF empirical studies (i.e. secondary literature, not primary data collection, but each
reviews primary empirical studies rather than being pure commentary). Options on the table: (a) keep them
as secondary context, not counted as evidence in the synthesis; (b) exclude them under E05 to be
consistent with S356; (c) keep them and report them separately from the primary-study evidence base.
Also relevant: S329 and S418 are "hybrid" reviews with a stated multi-database search but a narrative
(non-systematic) synthesis method — should they join this NONE group or be treated differently again?
""",
    "ask": "Which option (a/b/c) is most consistent with the protocol's own criterion 3 and with how S356 was already excluded? Should S329/S418 be grouped with these 13 or kept separate? State your recommendation plainly.",
}

QUESTIONS["linked_reports"] = {
    "title": "Should linked (companion) reports be collapsed, kept-and-linked, or left as separate counted studies?",
    "context": open(os.path.join(ROOT, "03_extraction/extracted_data/linked_reports_2026-09-28.csv"), encoding="utf-8").read() + """

== THE OPEN ITEM ==
12 pairs of records are flagged as reporting on the same or overlapping underlying data/fieldwork (same
trial, same interview sample, same author/dataset). 2 pairs are the same underlying data for sure
(`same_underlying_data=yes`: LR01 S294/S366; LR02 S097/S098), 2 are partial overlap, the rest are
"possible" or lower confidence. Today EVERY row in these pairs is still counted as a separate included
study in every figure the repository reports (1,159 includes). Treating linked reports as one study each
would give 1,157 distinct studies (or 1,155 counting the partial-overlap pairs too). The question is
whether to: (a) collapse each linked pair into one study for counting purposes (keeping both rows in the
database but flagging one as the 'primary' record for any count or synthesis); (b) keep both rows as
separate counted studies but note the link everywhere it matters (current practice, partially); (c) leave
it entirely as is with no further action. This matters concretely for Family B of the quantitative
synthesis, which currently has 6 effect-size rows and would have different effective weight if S294 and
S366 (both tagged to the trial) were treated as one study's two outcome papers rather than two.
""",
    "ask": "Given the stated confidence levels (high/medium/low) and that LR01 and LR02 are confirmed same-data pairs while most others are only 'possible' same-author/topic overlaps, what is the methodologically correct policy? Should confidence level determine different treatment (e.g. collapse only 'high' confidence, keep-and-link the rest)? State your recommendation plainly, and say what should happen specifically to LR01 (S294/S366) which is cited in Family B of the quantitative synthesis.",
}

QUESTIONS["family_vocabulary"] = {
    "title": "Should the draft controlled vocabulary for mechanism_family/outcome_family be adopted?",
    "context": open(os.path.join(ROOT, "05_analysis/descriptive/FAMILY_VOCABULARY_PROPOSAL_2026-09-28.md"), encoding="utf-8").read()[:8000] + """

== THE OPEN ITEM ==
`mechanism_family` holds 236 distinct free-text labels and `outcome_family` 127, across 1,159 studies,
making any tabulation by family unreliable as-is. A mechanical, keyword-based draft vocabulary was
generated (shown above) that maps the booleans extracted for each study to 9 mechanism families and the
4 already-documented outcome families. It flags 45 studies needing manual review (32 mechanism-unmapped +
13 others) and leaves `multiple` as a catch-all for studies matching more than one family's keywords (520
of 1,159 studies, nearly half). The proposal was deliberately not applied to evidence_map.csv because a
mechanical overwrite risks destroying richer thematic labels that a human curator wrote.
""",
    "ask": "Is a keyword-to-boolean-derived vocabulary with ~45% of studies landing in a 'multiple' bucket actually useful for synthesis, or does it just relabel the same granularity problem? Would you adopt this draft as-is, adopt it with modifications (name which), or reject it in favor of a different approach (name which) for getting a usable family-level tabulation? State your recommendation plainly.",
}

PROMPT1 = """You are an independent methodological reviewer for a PRISMA 2020 systematic review ("The Legal
Last Mile": legal, administrative and institutional factors in household water/sanitation access). You
are being asked to give your own first-principles judgment on an open methodological question — you have
NOT seen any other reviewer's opinion yet.

QUESTION: {title}

== CONTEXT ==
{context}

== YOUR TASK ==
{ask}

Respond with ONLY a JSON object:
{{"position": "one clear sentence stating your recommendation",
 "reasoning": "3-6 sentences of supporting argument",
 "confidence": "high|medium|low"}}
"""

PROMPT2 = """You previously gave this position on the question "{title}":
{own}

A second, independent reviewer looking at the same question gave this position:
{other}

== YOUR TASK ==
Reconsider in light of the other reviewer's argument. Do you still agree with your own position, partially
agree, or change your mind? Be honest — if their argument is better, say so.

Respond with ONLY a JSON object:
{{"final_position": "one clear sentence",
 "changed_mind": "yes|no|partially",
 "reasoning": "2-5 sentences explaining why you did or didn't change your mind, specifically engaging with the other reviewer's argument",
 "confidence": "high|medium|low"}}
"""


def run_question(key, q):
    print("=== %s ===" % key, flush=True)
    r1_codex, _ = ask("codex", PROMPT1.format(title=q["title"], context=q["context"], ask=q["ask"]), key + "_r1_codex")
    print("codex round1 done", flush=True)
    r1_gemini, _ = ask("gemini", PROMPT1.format(title=q["title"], context=q["context"], ask=q["ask"]), key + "_r1_gemini")
    print("gemini round1 done", flush=True)
    r2_codex, _ = ask("codex", PROMPT2.format(title=q["title"], own=json.dumps(r1_codex), other=json.dumps(r1_gemini)), key + "_r2_codex")
    print("codex round2 done", flush=True)
    r2_gemini, _ = ask("gemini", PROMPT2.format(title=q["title"], own=json.dumps(r1_gemini), other=json.dumps(r1_codex)), key + "_r2_gemini")
    print("gemini round2 done", flush=True)
    return {"question": q["title"], "r1_codex": r1_codex, "r1_gemini": r1_gemini, "r2_codex": r2_codex, "r2_gemini": r2_gemini}


if __name__ == "__main__":
    only = sys.argv[1:] or list(QUESTIONS.keys())
    results = {}
    for k in only:
        results[k] = run_question(k, QUESTIONS[k])
    json.dump(results, open(os.path.join(OUT, "debate_summary.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("ALL DONE")
