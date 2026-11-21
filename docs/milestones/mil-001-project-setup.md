# Project setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [587a239] |
| 2026-11-21 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Accepted with a Go (RC-004); reviewed in autonomous mode, not independent | [587a239] |

---

## Purpose

Decide whether the repository is ready for the game to be built in steps.

## Deliverable

A repository with project configuration, constants, Doxygen set-up, README, the screenshot harness, the local scan and a described, topic-tagged git host repository.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` runs on the scaffold in a `.venv` and passes | Passes | Fails |
| 2 | `pyproject.toml` requires Python newer than 3.14 and lists no runtime dependencies | Both hold | Either fails |
| 3 | `doxygen Doxyfile` builds without warnings | No warnings | Warnings |
| 4 | README follows the framework template and `bash framework/scripts/check-readme.sh` exits 0 | Exit 0 | Non-zero |
| 5 | Repository description and topics are set on the git host | Both set | Either missing |
| 6 | `opengrep` reports no findings on the branch | None | Any finding |

## Dependencies

| Depends on | Reason |
| --- | --- |
| BC-001 | Scope and objectives |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 3 and 5 (set-up part) | [BC-001] |
| Success criteria 2, 3, 4, 7 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-22 — one day from the start; no external deadline in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Project scaffolding | Add `pyproject.toml` (Python newer than 3.14, pytest dev extra, no runtime dependencies), Python `.gitignore` (including `.env` and `.venv`), `Doxyfile`, `src/` and `tests/` layout, `constants.py` and the root `.editorconfig`. One branch, one pull request. | No | |
| 2 | README and venv instructions | Write `README.md` from the framework template: how to create and use a local `.venv`, `python -m pip install --upgrade pip`, install the dev extra, run the game and the tests, install Tk on Linux. | No | |
| 3 | Repository description and topics | Set the description and topics of the git host repository with the token from `.env` (read from the environment only; never imported, tested or committed). | No | |
| 4 | Screenshot harness | Add a Docker image with `xvfb`, Tk and Python, and a script that runs the game for a fixed number of frames and writes a PNG to `docs/images/`. Environment: Docker container; never the host desktop. | No | |
| 5 | Local scan and CI | Document the local scan with the opengrep CLI (`~/.opengrep/cli/latest/opengrep.exe`) before each push, and add a CI workflow that runs the tests. | No | |

---

[BC-001]: ../business-case.md
[587a239]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/commit/587a2399dcf6574753ed41a81dc5fec6f6f3e9c0
