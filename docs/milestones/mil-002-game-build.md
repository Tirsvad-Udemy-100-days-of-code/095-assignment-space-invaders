# Game build in lecture steps

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-21 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Accepted with a Go (RC-005); reviewed in autonomous mode, not independent | pending |

---

## Purpose

Decide whether the Space Invaders game is complete enough to share with S02 and S03.

## Deliverable

A playable Space Invaders game in `src/` with tests in `tests/`, built in nine steps, each with its own branch, pull request, Doxygen comments and screenshot.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` passes | All tests pass | Any test fails |
| 2 | `python src/main.py` opens a window titled "Space Invaders" with a ship, aliens, barriers, score and lives | Observed in the container | Any element missing |
| 3 | Aliens move closer every second and touching the ship ends the game | Observed | Not observed |
| 4 | All constants are in `constants.py` | No magic numbers in other modules | Any found in review |
| 5 | `doxygen Doxyfile` builds without warnings | No warnings | Warnings |
| 6 | A screenshot exists in `docs/images/` for each of the nine steps | Nine images | Any missing |
| 7 | `opengrep` reports no findings | None | Any finding |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Scaffolding, constants, screenshot harness and README exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 and 2 | [BC-001] |
| Success criteria 1, 2, 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-26 — four days from the start of the milestone.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Step 1: game screen | Create `main.py` with a black `Screen` titled "Space Invaders" and a game loop with tracer off. Test the loop-free logic. Screenshot in the Docker container. | No | |
| 2 | Step 2: spaceship | Add `Ship` (turtle subclass) moving left and right with the arrow keys inside the screen edges. Screenshot. | No | |
| 3 | Step 3: shooting | Add `Bullet` fired from the ship with the space key, one at a time, flying up and reset at the top. Screenshot. | No | |
| 4 | Step 4: alien fleet | Add `Alien` and `Fleet`: a grid of alien rows in different colours. Screenshot. | No | |
| 5 | Step 5: alien movement | Move the fleet sideways every second, reverse at the edges and drop closer. Pure movement logic is tested without a display. Screenshot. | No | |
| 6 | Step 6: shooting aliens | Detect bullet and alien collisions by distance, remove the alien and speed the fleet up as it shrinks. Screenshot. | No | |
| 7 | Step 7: barriers | Add `Barrier` blocks between ship and aliens that absorb bullets and wear out. Screenshot. | No | |
| 8 | Step 8: game over and win | End the game when the aliens touch the ship or reach the bottom; show a win message when the fleet is gone. Screenshot. | No | |
| 9 | Step 9: scoreboard and lives | Add `Scoreboard` with score and lives, and the alien return fire that costs a life. Screenshot. | No | |
| 10 | Tests for game logic | pytest tests for movement, collision, fleet and scoring logic that need no display; GUI paths skip when Tk is missing. | No | |

---

[BC-001]: ../business-case.md
