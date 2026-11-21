"""Tests of the scoreboard; they need the GUI test environment."""

import constants


def test_scoreboard_starts_with_no_points_and_all_lives(screen) -> None:
    from scoreboard import Scoreboard

    scoreboard = Scoreboard()
    assert scoreboard.score == 0
    assert scoreboard.lives == constants.LIVES_START


def test_points_are_added_to_the_score(screen) -> None:
    from scoreboard import Scoreboard

    scoreboard = Scoreboard()
    scoreboard.add_points(30)
    scoreboard.add_points(10)
    assert scoreboard.score == 40


def test_losing_a_life_returns_the_lives_left(screen) -> None:
    from scoreboard import Scoreboard

    scoreboard = Scoreboard()
    assert scoreboard.lose_life() == constants.LIVES_START - 1
