"""Tests of the game window; they need the GUI test environment."""

import constants
import main


def test_screen_is_black_and_has_the_game_title(screen) -> None:
    configured = main.create_screen()
    assert configured.bgcolor() == constants.SCREEN_COLOR
    assert configured.getcanvas().winfo_toplevel().title() == constants.SCREEN_TITLE
