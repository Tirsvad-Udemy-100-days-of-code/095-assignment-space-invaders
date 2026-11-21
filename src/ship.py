"""@file ship.py
@brief The player's spaceship.
"""

from turtle import Turtle

import constants
import rules


class Ship(Turtle):
    """@brief A triangle at the bottom of the screen that moves left and right."""

    def __init__(self) -> None:
        """@brief Create the ship at the centre of the bottom row."""
        super().__init__(shape="triangle")
        self.color(constants.SHIP_COLOR)
        self.penup()
        self.setheading(90)
        self.shapesize(*constants.SHIP_STRETCH)
        self.goto(0, constants.SHIP_Y)

    def go_left(self) -> None:
        """@brief Move one step to the left, not past the left edge."""
        self._move_by(-constants.SHIP_STEP)

    def go_right(self) -> None:
        """@brief Move one step to the right, not past the right edge."""
        self._move_by(constants.SHIP_STEP)

    def _move_by(self, step: int) -> None:
        """@brief Move horizontally by `step`, kept inside the screen.

        @param step Pixels to move; negative moves left.
        """
        new_x = rules.clamp(
            self.xcor() + step, -constants.SHIP_MAX_X, constants.SHIP_MAX_X
        )
        self.goto(new_x, self.ycor())
