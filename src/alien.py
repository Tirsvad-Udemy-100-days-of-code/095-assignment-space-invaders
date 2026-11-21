"""@file alien.py
@brief One alien ship.
"""

from turtle import Turtle

import constants


class Alien(Turtle):
    """@brief An alien ship that sits at a fixed place in the fleet."""

    def __init__(
        self, x: float, y: float, color: str, points: int, column: int
    ) -> None:
        """@brief Create an alien.

        @param x Horizontal start position.
        @param y Vertical start position.
        @param color Colour of the alien.
        @param points Points scored for shooting it.
        @param column Column of the fleet it belongs to.
        """
        super().__init__(shape="turtle")
        self.color(color)
        self.points = points
        self.column = column
        self.penup()
        self.setheading(270)
        self.shapesize(*constants.ALIEN_STRETCH)
        self.goto(x, y)
