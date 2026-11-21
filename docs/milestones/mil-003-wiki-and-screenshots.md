# Wiki and screenshots

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [587a239] |
| 2026-11-21 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Accepted with a Go (RC-006); reviewed in autonomous mode, not independent | [587a239] |

---

## Purpose

Decide whether the documentation lets S02 and S03 follow every step of the build in their language.

## Deliverable

A README with a screenshot per step, a wiki in English, Danish and Bahasa Malaysia that explains what each step taught, and the reflection journal of the assignment.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `docs/wiki/` has the same page set in English, `-da` and `-ms` files, with a sidebar listing the languages | Same set in three languages | A page missing |
| 2 | Every build step has its screenshot in the README and in each wiki language | Nine images linked everywhere | Any missing |
| 3 | Each wiki step page says what was gained in that step | Present in all languages | Missing |
| 4 | The reflection journal (approach, hard, easy, learning, what to do differently) is in the wiki | Present | Missing |
| 5 | `bash framework/scripts/check-readme.sh` exits 0 and `opengrep` reports no findings | Both | Either fails |
| 6 | No artifact contains the abbreviation for artificial intelligence | None found by search | Any found |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The game and its screenshots exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 4 and 5 | [BC-001] |
| Success criteria 5 and 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-28 — two days after the game milestone.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | README screenshots | Add each step's screenshot with a one-line caption to the README. | No | |
| 2 | Wiki in English | Write `Home`, `Getting-Started`, one page per build step with screenshot and what was gained, `Reflection` and `Project-Documents`, plus `_Sidebar`. | No | |
| 3 | Wiki in Danish | Translate every English wiki page into Danish (`-da` files), same page set. | No | |
| 4 | Wiki in Bahasa Malaysia | Translate every English wiki page into Bahasa Malaysia (`-ms` files), same page set. | No | |
| 5 | Reflection journal | Write the course reflection: approach, what was hard and easy, what to improve, biggest learning, what to do differently. | No | |
| 6 | Doxygen output and final check | Generate the Doxygen output, run the README check, the language check and the opengrep scan. | No | |

---

[BC-001]: ../business-case.md
[587a239]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/commit/587a2399dcf6574753ed41a81dc5fec6f6f3e9c0
