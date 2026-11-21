"""@file scoreboard.py
@brief The score and the lives, written at the top of the screen.
"""

from turtle import Turtle

import constants


class Scoreboard(Turtle):
    """@brief Keeps and shows the score and the lives."""

    def __init__(self) -> None:
        """@brief Create the scoreboard with no points and all lives."""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(constants.SCOREBOARD_COLOR)
        self.goto(constants.SCOREBOARD_POSITION)
        self.score = 0
        self.lives = constants.LIVES_START
        self.refresh()

    def add_points(self, points: int) -> None:
        """@brief Add points to the score.

        @param points Points scored.
        """
        self.score += points
        self.refresh()

    def lose_life(self) -> int:
        """@brief Take one life from the player.

        @return The lives left.
        """
        self.lives -= 1
        self.refresh()
        return self.lives

    def refresh(self) -> None:
        """@brief Write the current score and lives."""
        self.clear()
        self.write(
            f"SCORE {self.score:04d}   LIVES {self.lives}",
            font=constants.SCOREBOARD_FONT,
        )
