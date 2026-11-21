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


def test_a_move_is_not_due_before_the_interval() -> None:
    assert not rules.is_due(10.5, 10.0, 1.0)


def test_a_move_is_due_after_the_interval() -> None:
    assert rules.is_due(11.0, 10.0, 1.0)


def test_fleet_moves_sideways_in_its_direction() -> None:
    assert rules.next_fleet_move([-100, 0, 100], 1, 20, 360, 25) == (20, 0, 1)
    assert rules.next_fleet_move([-100, 0, 100], -1, 20, 360, 25) == (-20, 0, -1)


def test_fleet_drops_and_turns_at_the_right_edge() -> None:
    assert rules.next_fleet_move([-100, 350], 1, 20, 360, 25) == (0, -25, -1)


def test_fleet_drops_and_turns_at_the_left_edge() -> None:
    assert rules.next_fleet_move([-350, 100], -1, 20, 360, 25) == (0, -25, 1)


def test_objects_close_together_are_a_hit() -> None:
    assert rules.is_hit(0, 0, 10, 10, 22)


def test_objects_far_apart_are_not_a_hit() -> None:
    assert not rules.is_hit(0, 0, 30, 0, 22)


def test_a_full_fleet_moves_at_the_base_interval() -> None:
    assert rules.move_interval(1.0, 40, 40, 0.2) == 1.0


def test_a_smaller_fleet_moves_faster() -> None:
    assert rules.move_interval(1.0, 20, 40, 0.2) == 0.5


def test_the_interval_never_drops_below_the_minimum() -> None:
    assert rules.move_interval(1.0, 1, 40, 0.2) == 0.2
