"""@file game.py
@brief The game: it owns the objects, reads the keys and runs the frame loop.
"""

import time
import turtle

import constants
from barrier import BarrierWall
from bullet import Bullet
from fleet import Fleet
from ship import Ship


class Game:
    """@brief Ties screen, ship, bullet, fleet and barriers together."""

    def __init__(self, screen: turtle.Screen) -> None:
        """@brief Create the objects and bind the keys.

        @param screen The game window.
        """
        self.screen = screen
        self.ship = Ship()
        self.bullet = Bullet()
        self.fleet = Fleet()
        self.barriers = BarrierWall()
        screen.listen()
        screen.onkeypress(self.ship.go_left, "Left")
        screen.onkeypress(self.ship.go_right, "Right")
        screen.onkeypress(self.fire, "space")

    def fire(self) -> None:
        """@brief Fire a bullet from the ship."""
        self.bullet.fire(self.ship.xcor(), self.ship.ycor())

    def check_bullet_hit(self) -> None:
        """@brief Let the bullet hit an alien or a barrier and fire again."""
        if not self.bullet.active:
            return
        x, y = self.bullet.xcor(), self.bullet.ycor()
        if self.barriers.absorb(x, y) or self.fleet.remove_hit(x, y):
            self.bullet.reset_bullet()

    def tick(self) -> None:
        """@brief Advance the game by one frame and schedule the next one."""
        self.bullet.move()
        self.fleet.update(time.monotonic())
        self.check_bullet_hit()
        self.screen.update()
        self.screen.ontimer(self.tick, constants.FRAME_DELAY_MS)

    def run(self) -> None:
        """@brief Run the game until the window is closed."""
        self.tick()
        self.screen.mainloop()
