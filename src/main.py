"""@file main.py
@brief Entry point of the Space Invaders game.
"""

import turtle

import constants
from game import Game


def create_screen() -> turtle.Screen:
    """@brief Create the black game window.

    Animation is switched off (`tracer(0)`), so the game decides when a frame is
    drawn by calling `update()`.

    @return The configured screen.
    """
    screen = turtle.Screen()
    screen.setup(width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT)
    screen.bgcolor(constants.SCREEN_COLOR)
    screen.title(constants.SCREEN_TITLE)
    screen.tracer(0)
    return screen


def main() -> None:
    """@brief Open the window and run the game until the window is closed."""
    Game(create_screen()).run()


if __name__ == "__main__":
    main()
