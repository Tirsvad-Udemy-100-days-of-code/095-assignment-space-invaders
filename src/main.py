"""@file main.py
@brief Entry point of the Space Invaders game: the screen and the game loop.
"""

import turtle

import constants
from ship import Ship


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


def run_frame(screen: turtle.Screen) -> None:
    """@brief Draw one frame and schedule the next one.

    @param screen The game window.
    """
    screen.update()
    screen.ontimer(lambda: run_frame(screen), constants.FRAME_DELAY_MS)


def main() -> None:
    """@brief Open the window and run the game until the window is closed."""
    screen = create_screen()
    ship = Ship()
    screen.listen()
    screen.onkeypress(ship.go_left, "Left")
    screen.onkeypress(ship.go_right, "Right")
    run_frame(screen)
    screen.mainloop()


if __name__ == "__main__":
    main()
