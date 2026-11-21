"""Tests of the game rules that need no display."""

import rules


def test_clamp_keeps_a_value_inside_the_range() -> None:
    assert rules.clamp(5, 0, 10) == 5


def test_clamp_raises_a_value_below_the_range() -> None:
    assert rules.clamp(-5, 0, 10) == 0


def test_clamp_lowers_a_value_above_the_range() -> None:
    assert rules.clamp(15, 0, 10) == 10


def test_a_bullet_below_the_top_edge_is_still_on_screen() -> None:
    assert not rules.has_left_screen_top(100, 300)


def test_a_bullet_above_the_top_edge_has_left_the_screen() -> None:
    assert rules.has_left_screen_top(301, 300)


def test_fleet_has_one_position_per_alien() -> None:
    positions = rules.fleet_positions(5, 8, 70, 45, 260)
    assert len(positions) == 40


def test_fleet_is_centred_and_laid_out_row_by_row() -> None:
    positions = rules.fleet_positions(2, 3, 100, 50, 200)
    assert positions == [
        (-100, 200),
        (0, 200),
        (100, 200),
        (-100, 150),
        (0, 150),
        (100, 150),
    ]
