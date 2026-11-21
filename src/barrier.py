"""@file barrier.py
@brief The barriers between the ship and the aliens.
"""

from turtle import Turtle

import constants
import rules


class BarrierBlock(Turtle):
    """@brief One block of a barrier; it changes colour as it wears out."""

    def __init__(self, x: float, y: float) -> None:
        """@brief Create a block with full health.

        @param x Horizontal position.
        @param y Vertical position.
        """
        super().__init__(shape="square")
        self.penup()
        factor = constants.BARRIER_BLOCK / 20
        self.shapesize(factor, factor)
        self.health = constants.BARRIER_HEALTH
        self.goto(x, y)
        self._show_health()

    def hit(self) -> bool:
        """@brief Take one hit.

        @return True when the block is gone.
        """
        self.health -= 1
        if self.health <= 0:
            self.hideturtle()
            return True
        self._show_health()
        return False

    def _show_health(self) -> None:
        """@brief Colour the block by its remaining health."""
        self.color(constants.BARRIER_COLORS[self.health - 1])


class BarrierWall:
    """@brief All barrier blocks."""

    def __init__(self) -> None:
        """@brief Build every barrier."""
        positions = rules.barrier_positions(
            constants.BARRIER_GROUPS,
            constants.BARRIER_COLUMNS,
            constants.BARRIER_ROWS,
            constants.BARRIER_BLOCK,
            constants.BARRIER_GROUP_SPACING,
            constants.BARRIER_Y,
        )
        self.blocks = [BarrierBlock(x, y) for x, y in positions]

    def absorb(self, x: float, y: float) -> bool:
        """@brief Let a block take a bullet at a position.

        @param x Horizontal position of the bullet.
        @param y Vertical position of the bullet.
        @return True when a block took the bullet.
        """
        target = next(
            (
                block
                for block in self.blocks
                if rules.is_hit(
                    x, y, block.xcor(), block.ycor(), constants.BARRIER_HIT_DISTANCE
                )
            ),
            None,
        )
        if target is None:
            return False
        if target.hit():
            self.blocks.remove(target)
        return True
