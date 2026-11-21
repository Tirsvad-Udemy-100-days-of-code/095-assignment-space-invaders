"""@file fleet.py
@brief The grid of alien ships.
"""

import time

import constants
import rules
from alien import Alien


class Fleet:
    """@brief All aliens, laid out as rows of different colours, moving closer."""

    def __init__(self) -> None:
        """@brief Create the aliens row by row."""
        self.direction = 1
        self.last_move = time.monotonic()
        positions = rules.fleet_positions(
            constants.ALIEN_ROWS,
            constants.ALIEN_COLUMNS,
            constants.ALIEN_SPACING_X,
            constants.ALIEN_SPACING_Y,
            constants.FLEET_TOP_Y,
        )
        self.aliens: list[Alien] = []
        for index, (x, y) in enumerate(positions):
            row = index // constants.ALIEN_COLUMNS
            color = constants.ALIEN_COLORS[row % len(constants.ALIEN_COLORS)]
            self.aliens.append(Alien(x, y, color))

    def update(self, now: float) -> bool:
        """@brief Move the fleet when a second has passed.

        @param now Current time in seconds.
        @return True when the fleet moved.
        """
        if not rules.is_due(now, self.last_move, constants.FLEET_MOVE_INTERVAL):
            return False
        self.last_move = now
        self.move()
        return True

    def move(self) -> None:
        """@brief Move every alien one step sideways, or down at an edge."""
        change_x, change_y, self.direction = rules.next_fleet_move(
            [alien.xcor() for alien in self.aliens],
            self.direction,
            constants.FLEET_STEP_X,
            constants.FLEET_EDGE_X,
            constants.FLEET_DROP,
        )
        for alien in self.aliens:
            alien.goto(alien.xcor() + change_x, alien.ycor() + change_y)
