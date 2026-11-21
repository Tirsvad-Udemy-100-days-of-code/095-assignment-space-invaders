"""Tests of the game constants."""

import constants


def test_screen_is_larger_than_zero() -> None:
    assert constants.SCREEN_WIDTH > 0
    assert constants.SCREEN_HEIGHT > 0


def test_title_is_set() -> None:
    assert constants.SCREEN_TITLE == "Space Invaders"


def test_frame_delay_is_positive() -> None:
    assert constants.FRAME_DELAY_MS > 0
