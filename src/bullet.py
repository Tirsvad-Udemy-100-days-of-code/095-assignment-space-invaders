"""@file bullet.py
@brief The bullet the ship fires.
"""

from turtle import Turtle

import constants
import rules


class Bullet(Turtle):
    """@brief A small bar that flies up from the ship; only one exists at a time."""

    def __init__(self) -> None:
        """@brief Create the bullet, hidden and not flying."""
        super().__init__(shape="square")
        self.color(constants.BULLET_COLOR)
        self.penup()
        self.setheading(90)
        self.shapesize(*constants.BULLET_STRETCH)
        self.hideturtle()
        self.active = False

    def fire(self, x: float, y: float) -> None:
        """@brief Fire from a position, unless the bullet is already flying.

        @param x Horizontal position of the ship.
        @param y Vertical position of the ship.
        """
        if self.active:
            return
        self.goto(x, y + constants.BULLET_START_OFFSET)
        self.showturtle()
        self.active = True

    def move(self) -> None:
        """@brief Fly one step up; disappear after leaving the top of the screen."""
        if not self.active:
            return
        self.sety(self.ycor() + constants.BULLET_STEP)
        if rules.has_left_screen_top(self.ycor(), constants.SCREEN_TOP):
            self.reset_bullet()

    def reset_bullet(self) -> None:
        """@brief Hide the bullet so the ship can fire again."""
        self.hideturtle()
        self.active = False
