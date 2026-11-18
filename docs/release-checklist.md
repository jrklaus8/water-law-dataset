# Release-readiness checklist

Use this before tagging a version, creating a GitHub release, depositing a new version of the data, or telling anyone the work is public and final. The state shown is the state on 2026-10-27, as found by the AI-assisted self-audit in [`audit-report.md`](audit-report.md). It is **not** a statement that the project is ready to release: items that need a decision by the researcher, the library, the data steward or the privacy contact are open.

**Two release mechanics to know first.** (1) `.github/workflows/python-publish.yml` runs when a GitHub *release is published*; it builds the package and publishes it to PyPI. Creating a release is therefore an irreversible public act. (2) `docs/` is the GitHub Pages root: anything merged into `main` under `docs/` (including this page and the audit report) becomes web-readable.

Legend: ☑ done and checked · ☐ open · ❓ cannot be decided from the repository (someone must confirm).

## A. Rights, terms and licences

| State | Item | Reference |
|---|---|---|
| ❓ | Terms of every court source read and recorded (collection, storage, republication, personal data) | [`source-register.md`](source-register.md); F-11 |
| ❓ | Redistribution of subscription-database exports confirmed, or exports replaced by IDs and hashes | F-04 |
| ☐ | Licence stated for each component (code, dataset, review documents, third-party data), consistently | F-18 |
| ☐ | Origin, author and permission of the hand-coded 2021 TJSP spreadsheet documented | F-30 |
| ❓ | University rights in the work confirmed | [`standards-matrix.md`](standards-matrix.md) |

## B. Privacy and confidential material

| State | Item | Reference |
|---|---|---|
| ☑ | Pattern scan of code, configuration and documents for credentials: none found | `tests/test_repository_hygiene.py` |
| ☐ | Author e-mail addresses removed from, or justified in, public data files | F-05 |
| ☐ | Institutional account identifier removed from stored URLs | F-06 |
| ❓ | Drive folder named in a brief is not link-shared | F-07 |
| ❓ | Whether decisions in the deposits name parties; anonymisation where needed | F-11 |
| ❓ | Data-protection contact consulted | S-06, S-08, S-09 |

## C. Research integrity and claims

| State | Item | Reference |
|---|---|---|
| ☐ | Outcome-coding defects corrected and the data re-coded, or the outcome variable withdrawn / labelled unreliable in the release notes | F-08, F-09 |
| ☐ | "Absorbed before litigation" reworded as interpretation, separate from the classifier result | F-10 |
| ☐ | κ and precision figures labelled as author-vs-LLM and single-coder wherever quoted | F-22 |
| ☐ | Starting residual (69% vs 89.2%) reconciled in `validation/README.md` | [`research-protocol.md`](research-protocol.md) §5 |
| ☐ | Review: open items A6 tiers 2–3, A30, A32, second extractor, retrospective registration | review `00_admin/DECISIONS_AND_OPEN_ITEMS.md`; F-26, F-27 |

## D. AI use

| State | Item | Reference |
|---|---|---|
| ☑ | AI use inventoried in one place | [`ai-use-and-disclosure.md`](ai-use-and-disclosure.md) |
| ❓ | Terms of the AI services and publishers' text-and-data-mining terms read for the dates of use | F-19 |
| ❓ | University generative-AI guidance and the doctoral-school AI policy compared with practice | S-04, S-05 |
| ☐ | AI tools moved from "author" to acknowledgement unless the venue allows AI authors | F-17 |
| ☐ | Model identifier, date and instruction file recorded for every AI task from now on | F-20 |

## E. Reproducibility and quality

| State | Item | Reference |
|---|---|---|
| ☑ | Offline tests pass (expected failures are documented defects) | `python3 -m unittest discover -s tests` |
| ☑ | Review verifier passes | `verify_repository.py` |
| ☑ | `CITATION.cff` files validate against the CFF 1.2.0 schema | F-29 |
| ☐ | Package versions recorded and pinned from the author's environment | F-15 |
| ☐ | SHA-256 and row counts of the deposited data files recorded; code commit recorded | F-12 |
| ☐ | TLS verification, User-Agent and path defaults decided | F-01, F-02, F-03 |
| ☐ | Request log and rate limits added to the scrapers, if collection is repeated | F-23 |
| ☐ | Packaging metadata consistent (`setuptools`, `license`) | F-16 |
| ❓ | CI run on GitHub after merging the new tests and permissions | F-13, F-14 |

## F. Documentation and metadata

| State | Item | Reference |
|---|---|---|
| ☑ | Protocol, data management, source register, AI use, reproducibility, limitations, standards matrix and audit report exist | `docs/` |
| ☐ | README tree and script-to-subset mapping corrected | F-31 |
| ☐ | Version number identical in `pyproject.toml`, `CITATION.cff`, README and the release tag (the test checks the first two) | `tests/test_repository_hygiene.py` |
| ☐ | `CHANGELOG.md` entry written for the release | [`../CHANGELOG.md`](../CHANGELOG.md) |
| ☐ | Decision recorded on whether audit documents under `docs/` should be public | F-25 |
| ☐ | Contact for take-down and security reports confirmed | [`../SECURITY.md`](../SECURITY.md) |

## G. Institutional

| State | Item | Reference |
|---|---|---|
| ❓ | Research ethics review or documented exemption | S-03 |
| ❓ | Data management plan exists and matches `data-management.md` | S-01, S-02 |
| ❓ | Supervisor has read the audit report and the open decisions | audit report, section H |

A release should not go ahead while an item in sections A, B or C that is marked ☐ or ❓ is unresolved, unless the researcher decides to proceed and records why.
