"""@file banner.py
@brief The message shown when the game ends.
"""

from turtle import Turtle

import constants


class Banner(Turtle):
    """@brief Writes a large centred message on the screen."""

    def __init__(self) -> None:
        """@brief Create the banner, with nothing written yet."""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, constants.BANNER_Y)

    def show(self, text: str, color: str) -> None:
        """@brief Write a message.

        @param text The message.
        @param color Colour of the message.
        """
        self.color(color)
        self.write(text, align="center", font=constants.BANNER_FONT)
