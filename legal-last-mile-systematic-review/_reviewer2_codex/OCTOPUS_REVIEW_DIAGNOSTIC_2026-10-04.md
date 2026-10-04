# Diagnostic record: running the packaged `/octo:review` multi-LLM pipeline (2026-10-04)

This repository's own reviewer_2 pipeline (`run_codex_reviewer2.py`, `run_second_extractor.py`, `run_debate.py`
— documented in `AI_USE_AND_TOOLS_DISCLOSURE.md`) is a set of custom dispatch scripts written for this project.
Separately, the Claude Code session doing this work has the **Claude Octopus** plugin (`octo@nyldn-plugins`)
installed, which ships its own packaged multi-LLM code-review command, `/octo:review` (invoked via
`${HOME}/.claude-octopus/plugin/scripts/orchestrate.sh code-review`). This note records a genuine attempt to run
that packaged tool — not the project's own scripts — against a real, small, uncommitted change in this
repository, as a methodological transparency exercise: trying another layer of AI tooling and reporting exactly
what happened, success or failure.

## What was reviewed

A genuine bug found while comparing the three `_reviewer2_codex/*.py` dispatch scripts: `run_codex_reviewer2.py`'s
Gemini-branch `subprocess.run()` call used `shell=(os.name == "nt")` together with a list `cmd` argument — a
fragile, unnecessary Windows `subprocess` pattern, inconsistent with the otherwise-identical Gemini branches in
`run_second_extractor.py` and `run_debate.py`, which omit `shell=` entirely and already work correctly in this
environment. The fix removed that argument:

```diff
         cmd = [EXE, "-m", MODEL, "-p", "Follow the instructions in the input above and respond with ONLY the JSON object."]
         p = subprocess.run(cmd, input=prompt, text=True, encoding="utf-8", errors="replace",
-                           capture_output=True, timeout=1500, cwd=HERE, shell=(os.name == "nt"))
+                           capture_output=True, timeout=1500, cwd=HERE)
```

This 1-line, 13-line-diff change was staged (`git add` only, not committed) and used as the `target:"staged"` diff
for `/octo:review`.

## Command run

```bash
${HOME}/.claude-octopus/plugin/scripts/orchestrate.sh code-review '{"target":"staged","focus":["correctness","security","architecture"],"provenance":"ai-assisted","autonomy":"autonomous","publish":"never","debate":"auto","history":"fresh"}'
```

## Result: all 4 Round-1 providers failed

The orchestrator's own proof packet (`~/.claude-octopus/runs/bd0496f7-9d55-4751-ad1e-04410e79b921/`) recorded
verdict `fail` with the claim "Code was reviewed by at least one provider" marked **contradicted**. Per-provider
root causes, read directly from each agent's captured output file:

| Role | Provider | Exit | Root cause (verbatim from output file) |
|---|---|---|---|
| arch-reviewer | claude-sonnet (Octopus's own internal `claude` subprocess, distinct from this session) | 1 | `Failed to authenticate. API Error: 401 {"type":"error","error":{"type":"authentication_error","message":"OAuth access token is invalid."}}` — Octopus spawns its own `claude` CLI subprocess with its own OAuth token, separate from the interactive session running this review; that token is expired/invalid. |
| logic-reviewer | codex | 1 | `{"type":"error","status":400,"error":{"type":"invalid_request_error","message":"The 'gpt-5.4' model is not supported when using Codex with a ChatGPT account."}}` — Octopus's internal model-resolver selected `gpt-5.4` for the codex role on this account. This project's own working scripts use `gpt-5.6-sol` (`run_codex_reviewer2.py` line 31, `R2_MODEL` default) successfully with the same Codex CLI (0.160.0) and the same ChatGPT-account login, so the failure is Octopus's hardcoded model choice, not a broken Codex installation. |
| security-reviewer | gemini | 41 | "(no output captured)" — the gemini subprocess produced no stdout/stderr before exiting. |
| cve-reviewer | gemini | 41 | Same as above. |

Supporting diagnosis for the two Gemini failures: `orchestrate.sh`'s own log line during the run —
`model-resolver.sh: line 232: /tmp/octo-model-cache-....json: No such file or directory` — shows the resolver's
model-cache write already failing on a hardcoded `/tmp` path (this Windows Git Bash environment does not reliably
back `/tmp`; the same class of path issue was hit and fixed elsewhere in this project's own scripts earlier, e.g.
`verify_repository.py`'s git-path-separator fix). Separately, a direct same-session test of the gemini CLI itself
(`gemini -m gemini-3.1-flash-lite -p "Reply with exactly: OK"`) failed with `Please set an Auth method... specify
... GEMINI_API_KEY` — this interactive agent's own Bash tool process does not have `GEMINI_API_KEY` in its
environment, even though the user set it earlier this session via `[System.Environment]::SetEnvironmentVariable(
"GEMINI_API_KEY", ..., "User")`. A registry-level "User" environment variable set that way does not propagate
into already-open or freshly spawned shells until a fresh login/terminal session picks it up; this agent's
sandboxed shell evidently predates that propagation. `orchestrate.sh detect-providers` independently confirms this
from its own probe: `Gemini: Installed but not authenticated`.

## Why no further workaround was attempted

- The Claude-sonnet 401 and the hardcoded `gpt-5.4` selection live inside the Octopus plugin's own code
  (`~/.claude-octopus/plugin/`, `~/.claude/plugins/cache/nyldn-plugins/octo/...`), not in this repository. Patching
  a third-party plugin's internals is out of scope for a systematic-review data repository and would not be
  reproducible by another researcher who installs the plugin normally.
- The Gemini auth gap is an environment/session propagation issue (a Windows user-env-var change needing a fresh
  login to reach this shell), not a flaw in the Gemini CLI, this repository's scripts, or the API key itself. It
  does not justify re-entering the API key value into a command in this session.
- Working around all three by hand-selecting a different Codex model or wiring a fresh Gemini auth path for the
  Octopus subprocess specifically would amount to re-implementing this project's own already-working, already-
  disclosed `run_codex_reviewer2.py`/`run_second_extractor.py`/`run_debate.py` pipeline a second time, inside a
  third-party plugin, for no added audit value.

## Conclusion

The packaged `/octo:review` tool is installed and was genuinely invoked against a real staged diff in this
repository, but could not complete a review in this environment: 0 of 4 providers returned usable output, for
three distinct, independently-diagnosed causes (stale internal OAuth token, an unsupported hardcoded model name
for this account's Codex login, and a Gemini CLI auth/env-propagation gap). This is reported here rather than
silently discarded, consistent with the project's commitment to disclosing every AI tool actually tried, including
ones that did not work. **The reviewer_2 methodology this systematic review relies on remains the project's own
custom dispatch scripts** (`AI_USE_AND_TOOLS_DISCLOSURE.md`), which do not depend on the Octopus plugin and have
already completed 121/121 available full-text reviews across both Codex and Gemini. The one concrete, durable
output of this exercise is the `shell=True` fix itself (above), which is a genuine, independently-motivated
correctness improvement to `run_codex_reviewer2.py`, found by comparing it against its two sibling scripts rather
than by any of the four review providers (none of which returned findings).
