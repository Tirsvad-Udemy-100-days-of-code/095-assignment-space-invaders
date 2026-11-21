# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-015 |
| CrossReference | [QC-PY-001], [MIL-002] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: `src/` and `tests/` of step 8 of [MIL-002] (`banner.py`: `Banner`; `game.py`: `Game.check_state`; `rules.py`: `game_state`; `tools/scenarios/`)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (Stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules and functions are snake_case, classes (Ship, Bullet, Alien, Fleet, BarrierBlock, BarrierWall, Banner, Game) PascalCase, constants UPPER_SNAKE. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state their purpose in the game's terms; no abbreviations or single-letter names outside tiny scopes. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | Lines are at most 88 characters in the style of `ruff format`; no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function and method is annotated, `-> None` included. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No `except:`; the test fixture catches only `tkinter.TclError` and turns it into a skip with the cause in the message. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default arguments; no builtins shadowed. |
| 7 | Files, locks and connections are managed with context managers | N-A | No files, locks or connections are opened. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | All modules, classes and public functions have Doxygen docstrings that say what they do. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No logging and no `print` in the game; no secrets handled. `.env` is neither read nor imported by the project. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No DCD exists: the plan has only plain technical tasks and no use case. The classes follow the assignment's names. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `tests/test_rules.py` (24 tests), `tests/test_game.py` (4 tests) and `tests/test_banner.py` (1 test), the last two run in the container; screenshots `docs/images/step-8-game-over.png` and `step-8-win.png`; named for the behaviour, independent of order and the network; `python -m pytest` passes. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | The type checker was not run; optional criterion. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | No runtime dependencies; `pytest>=8` is declared in the `dev` extra; none unused. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Every number and colour is defined once in `constants.py`; other modules import it. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | Game-rule logic imports no `turtle`; only the turtle subclasses and `main.py` use it; no import cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Each class has one reason to change; the fleet and bullet logic are extended by methods, not by type tests. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | The project is small: flat modules in `src/` and tests in `tests/`, the same shape as the course assignment; a layered folder structure is not needed for a single-screen game. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All file and folder names are English, lowercase and use only letters, digits, `-`, `_` and `.`. |

## Overall Verdict

Go — every Mandatory criterion of QC-PY-001 passes or is not applicable (rows 7, 10 and 12 are N-A, each with a reason). Stand-in review, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[MIL-002]: ../../milestones/mil-002-game-build.md
