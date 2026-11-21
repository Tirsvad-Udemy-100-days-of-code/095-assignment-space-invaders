# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-21 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Accepted with a Go (RC-001); reviewed in autonomous mode, not independent | pending |

---

## Executive Summary

Build the classic Space Invaders shoot 'em up in Python as the Day 95
assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp".
The player steers a spaceship left and right and shoots alien ships. Every
second the aliens move closer; when they touch the ship the game is over, and
barriers offer defensive positions. The result is a small, readable, runnable
repository with a wiki in three languages and a screenshot for every build step.

## Methodological and Standards Foundation

ISO/IEC 25010:2023 quality characteristics and the SQA/QC framework in
`framework/`. Code follows the `coding-conventions` skill (Python) and the
`clean-architecture` skill.

## Problem Statement

The assignment needs a finished, documented Space Invaders implementation that
others can run and read. Without a structured repository the solution is a loose
set of scripts that is hard to share, run, verify or learn from. The belief that
would kill the idea if false: the game can be built with the standard library
only (`turtle`), with logic kept apart from the screen so it can be tested
without a display.

## Business Opportunity

A reusable reference solution for the course community, and a portfolio piece
that shows planned, tested and documented work, with each lecture step visible
as a screenshot and an explanation of what was learned.

## Objectives

1. Deliver a playable Space Invaders game using only the Python standard library (`turtle`).
2. Build it in small steps, one branch and one pull request per step, so the history shows how the game grew.
3. Provide pytest tests, Doxygen source documentation and a README with instructions to create and use a local `.venv` and to run the game and its tests.
4. Show a screenshot of every build step in the README and the wiki, and explain in the wiki what each step taught.
5. Publish the wiki in English, Danish and Bahasa Malaysia.

## Scope

### In Scope

- Game window, spaceship moving left and right, bullets, a grid of aliens that move closer every second, collisions, barriers, game over when the aliens touch the ship, score and lives.
- `constants.py` for constants, Doxygen comments in the source and a `Doxyfile`.
- `pyproject.toml` (Python newer than 3.14, `venv`, `pytest` as development extra), a Python `.gitignore`, README from the framework template, tests.
- A screenshot per build step, produced in an isolated environment (a Docker container with a virtual display).
- Wiki pages in English, Danish and Bahasa Malaysia, and the reflection journal the assignment asks for.
- Repository description and topics on the git host; a local opengrep scan before every push.

### Out of Scope

- Sound, menus, high-score storage, network play, packaging for PyPI.
- Runtime dependencies beyond the standard library.
- Tests that open a window on the host desktop.

## Expected Benefits

### Tangible Benefits

- A runnable game, a test suite and a trilingual wiki that others can reuse.

### Intangible Benefits

- Practice in object-oriented design and in working plan-first with reviews and one pull request per step.

## Strategic Alignment

Supports the personal learning goal of completing the 100 Days of Code course
with a process-driven repository.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Game is playable | Window opens; ship moves; bullets destroy aliens; aliens advance every second; touching the ship ends the game | Manual run following the README, in the container for the screenshots |
| 2 | Tests pass | All pytest tests green | `python -m pytest` |
| 3 | No runtime dependencies | `dependencies = []` in `pyproject.toml` | Inspection |
| 4 | Repository is discoverable | Description and topics set | Inspection on the git host |
| 5 | Every build step has a screenshot | One image per step in README and in each wiki language | Files in `docs/images/` and links in the pages |
| 6 | Wiki in three languages | Same page set in English, Danish and Bahasa Malaysia | Files in `docs/wiki/` |
| 7 | Security scan clean | opengrep reports no findings before each push | Scan output |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| `turtle` needs Tk, absent on some Linux installs | Game does not start | README documents installing `python3-tk` |
| Game loop is hard to unit-test | Low test coverage | Keep logic in classes and functions with no `Screen` dependency where possible |
| Screenshots could take over the desktop | Interrupts the Product Owner | Screenshots are taken only in a Docker container under a virtual display |
| Python newer than 3.14 is not installed on a visitor's machine | Game does not start | README states the version and how to create the `.venv` with it |
| Tokens in `.env` leak | Credential exposure | `.env` is ignored by git, never imported or tested by the project, used only for personal repository setup |

## Assumptions

- S01 is the Product Owner, developer and reviewer; S02 and S03 cannot be reached for interviews and need no input.
- The Product Owner's language is English and the domain is IT.
- Python 3.14 or newer with Tk, Docker and the opengrep CLI are available on S01's machine.
- Each milestone is reviewed and accepted before its code is written.

## Constraints

- Python newer than 3.14, `venv`, `pytest`, folders `src/`, `tests/`, `docs/`, `constants.py` for constants, Doxygen comments.
- No runtime dependencies unless needed.
- One branch and one pull request per step to keep track of the steps.
- Artifacts avoid the abbreviation for artificial intelligence; a stand-in reviewer is named as "stand-in for S01".
- Target repository: `Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders` on `git.tirsystem.com`.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| A few days of the Product Owner's time | Shareable reference solution, trilingual learning notes and a portfolio piece |

The assessment is qualitative on purpose: no money is spent and the benefits (learning, sharing) have no market value to measure.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Completes the assignment; owns, builds and reviews it |
| S02 | Readable, runnable code with the assignment's function names, plus README instructions |
| S03 | Clear description, topics and README, and no runtime dependencies |

## Recommendation

Proceed — small scope, no cost, and a clear learning and sharing benefit.

---

[SA-001]: ./stakeholder-analysis.md
[PP-001]: ./project-plan.md
[MIL-001]: ./milestones/mil-001-project-setup.md
[MIL-002]: ./milestones/mil-002-game-build.md
[MIL-003]: ./milestones/mil-003-wiki-and-screenshots.md
