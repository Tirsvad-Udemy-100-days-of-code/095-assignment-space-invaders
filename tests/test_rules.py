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


def test_barrier_has_a_position_for_every_block() -> None:
    positions = rules.barrier_positions(4, 4, 2, 20, 170, -140)
    assert len(positions) == 32


def test_barriers_are_spread_evenly_around_the_centre() -> None:
    positions = rules.barrier_positions(2, 1, 1, 20, 100, -140)
    assert positions == [(-50, -140), (50, -140)]


def test_barrier_blocks_are_laid_out_row_by_row() -> None:
    positions = rules.barrier_positions(1, 2, 2, 20, 100, -140)
    assert positions == [(-10, -140), (10, -140), (-10, -160), (10, -160)]


def test_the_game_goes_on_while_aliens_are_far_away() -> None:
    state = rules.game_state([(0, 200)], (0, -250), 30, -230)
    assert state == "playing"


def test_the_game_is_lost_when_an_alien_touches_the_ship() -> None:
    state = rules.game_state([(0, 200), (10, -240)], (0, -250), 30, -300)
    assert state == "lost"


def test_the_game_is_lost_when_an_alien_reaches_the_ship_row() -> None:
    state = rules.game_state([(300, -230)], (0, -250), 30, -230)
    assert state == "lost"


def test_the_game_is_won_when_no_alien_is_left() -> None:
    assert rules.game_state([], (0, -250), 30, -230) == "won"
