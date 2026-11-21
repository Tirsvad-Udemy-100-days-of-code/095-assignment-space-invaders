"""@file game.py
@brief The game: it owns the objects, reads the keys and runs the frame loop.
"""

import time
import turtle

import constants
from bullet import Bullet
from fleet import Fleet
from ship import Ship


class Game:
    """@brief Ties the screen, the ship, the bullet and the fleet together."""

    def __init__(self, screen: turtle.Screen) -> None:
        """@brief Create the objects and bind the keys.

        @param screen The game window.
        """
        self.screen = screen
        self.ship = Ship()
        self.bullet = Bullet()
        self.fleet = Fleet()
        screen.listen()
        screen.onkeypress(self.ship.go_left, "Left")
        screen.onkeypress(self.ship.go_right, "Right")
        screen.onkeypress(self.fire, "space")

    def fire(self) -> None:
        """@brief Fire a bullet from the ship."""
        self.bullet.fire(self.ship.xcor(), self.ship.ycor())

    def tick(self) -> None:
        """@brief Advance the game by one frame and schedule the next one."""
        self.bullet.move()
        self.fleet.update(time.monotonic())
        self.screen.update()
        self.screen.ontimer(self.tick, constants.FRAME_DELAY_MS)

    def run(self) -> None:
        """@brief Run the game until the window is closed."""
        self.tick()
        self.screen.mainloop()
