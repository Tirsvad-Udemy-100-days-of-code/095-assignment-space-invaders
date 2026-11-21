# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [587a239] |
| 2026-11-21 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Accepted with a Go (RC-002); reviewed in autonomous mode, not independent | [587a239] |

---

## Purpose

Identify who the Space Invaders project serves and what each of them needs, using a Power/Interest grid.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Finishes the assignment with a clean, reviewed result |
| S02 | Udemy coursists | Course participants | Udemy | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, plus README instructions to run it |
| S03 | GitHub viewers | Repository visitors | Public | LOW | MEDIUM | Keep Informed | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

S01 decides scope and accepts every artifact, so power and interest are both
high. S02 and S03 have no say in the project but use its output.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Complete, tested game built step by step | Functionality, Reliability |
| CN-002 | S02 | Readable code, assignment names, run instructions, screenshots and explanations of each step in their own language | Usability, Supportability |
| CN-003 | S03 | Description, topics, README, no runtime dependencies | Usability, Implementation |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per milestone and per step | Reviewed artifacts and code | All |
| S02 | README and wiki (English, Danish, Bahasa Malaysia) | At release | Run instructions, screenshots, what each step taught | MIL-002, MIL-003 |
| S03 | Repository page | At release | Description, topics, README | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 is author and reviewer, so review is not independent | S01 | S01 accepts the plan; each review record states its mode, and the end-of-run summary lists every stand-in decision so S01 can challenge it |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Complete, tested game built step by step (CN-001) | Objectives 1, 2 and 3 |
| S02 | Readable code, screenshots, explanations (CN-002) | Objectives 3, 4 and 5 |
| S03 | Discoverable, dependency-free repository (CN-003) | Objectives 1 and 3 |

## Sign-Off

Accepted by the stand-in for S01 after RC-002 (Go).

---

[BC-001]: ./business-case.md
[587a239]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/commit/587a2399dcf6574753ed41a81dc5fec6f6f3e9c0
