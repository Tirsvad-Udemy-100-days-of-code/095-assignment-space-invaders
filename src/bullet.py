"""@file bullet.py
@brief The bullet the ship fires.
"""

from turtle import Turtle

import constants
import rules


class Bullet(Turtle):
    """@brief A small bar that flies up or down; each shooter has one at a time."""

    def __init__(
        self, color: str = constants.BULLET_COLOR, step: int = constants.BULLET_STEP
    ) -> None:
        """@brief Create the bullet, hidden and not flying.

        @param color Colour of the bullet.
        @param step Pixels per frame; positive flies up, negative flies down.
        """
        super().__init__(shape="square")
        self.step = step
        self.color(color)
        self.penup()
        self.setheading(90)
        self.shapesize(*constants.BULLET_STRETCH)
        self.hideturtle()
        self.active = False

    def fire(self, x: float, y: float) -> None:
        """@brief Fire from a position, unless the bullet is already flying.

        @param x Horizontal position of the shooter.
        @param y Vertical position of the shooter.
        """
        if self.active:
            return
        direction = 1 if self.step > 0 else -1
        self.goto(x, y + direction * constants.BULLET_START_OFFSET)
        self.showturtle()
        self.active = True

    def move(self) -> None:
        """@brief Fly one step; disappear after leaving the screen."""
        if not self.active:
            return
        self.sety(self.ycor() + self.step)
        if rules.has_left_screen(self.ycor(), constants.SCREEN_TOP):
            self.reset_bullet()

    def reset_bullet(self) -> None:
        """@brief Hide the bullet so the ship can fire again."""
        self.hideturtle()
        self.active = False
