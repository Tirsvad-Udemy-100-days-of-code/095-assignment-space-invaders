"""Tests of the game rules that need no display."""

import rules


def test_clamp_keeps_a_value_inside_the_range() -> None:
    assert rules.clamp(5, 0, 10) == 5


def test_clamp_raises_a_value_below_the_range() -> None:
    assert rules.clamp(-5, 0, 10) == 0


def test_clamp_lowers_a_value_above_the_range() -> None:
    assert rules.clamp(15, 0, 10) == 10
