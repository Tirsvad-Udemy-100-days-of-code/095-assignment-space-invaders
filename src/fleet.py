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
        self.total = constants.ALIEN_ROWS * constants.ALIEN_COLUMNS
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
        interval = rules.move_interval(
            constants.FLEET_MOVE_INTERVAL,
            len(self.aliens),
            self.total,
            constants.FLEET_MIN_INTERVAL,
        )
        if not rules.is_due(now, self.last_move, interval):
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

    def remove_hit(self, x: float, y: float) -> bool:
        """@brief Remove the alien that a bullet at a position hits, if any.

        @param x Horizontal position of the bullet.
        @param y Vertical position of the bullet.
        @return True when an alien was hit and removed.
        """
        hit = next(
            (
                alien
                for alien in self.aliens
                if rules.is_hit(
                    x, y, alien.xcor(), alien.ycor(), constants.HIT_DISTANCE
                )
            ),
            None,
        )
        if hit is None:
            return False
        hit.hideturtle()
        self.aliens.remove(hit)
        return True
