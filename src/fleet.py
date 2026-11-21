"""@file fleet.py
@brief The grid of alien ships.
"""

import constants
import rules
from alien import Alien


class Fleet:
    """@brief All aliens, laid out as rows of different colours."""

    def __init__(self) -> None:
        """@brief Create the aliens row by row."""
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
