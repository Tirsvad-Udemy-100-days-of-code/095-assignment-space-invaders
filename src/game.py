"""@file game.py
@brief The game: it owns the objects, reads the keys and runs the frame loop.
"""

import time
import turtle

import constants
import rules
from banner import Banner
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
        self.banner = Banner()
        self.state = constants.STATE_PLAYING
        screen.listen()
        screen.onkeypress(self.move_left, "Left")
        screen.onkeypress(self.move_right, "Right")
        screen.onkeypress(self.fire, "space")

    def move_left(self) -> None:
        """@brief Move the ship left while the game is running."""
        if self.state == constants.STATE_PLAYING:
            self.ship.go_left()

    def move_right(self) -> None:
        """@brief Move the ship right while the game is running."""
        if self.state == constants.STATE_PLAYING:
            self.ship.go_right()

    def fire(self) -> None:
        """@brief Fire a bullet from the ship while the game is running."""
        if self.state == constants.STATE_PLAYING:
            self.bullet.fire(self.ship.xcor(), self.ship.ycor())

    def check_bullet_hit(self) -> None:
        """@brief Let the bullet hit an alien or a barrier and fire again."""
        if not self.bullet.active:
            return
        x, y = self.bullet.xcor(), self.bullet.ycor()
        if self.barriers.absorb(x, y) or self.fleet.remove_hit(x, y):
            self.bullet.reset_bullet()

    def check_state(self) -> None:
        """@brief End the game with a message when it is lost or won."""
        self.state = rules.game_state(
            [(alien.xcor(), alien.ycor()) for alien in self.fleet.aliens],
            (self.ship.xcor(), self.ship.ycor()),
            constants.GAME_OVER_DISTANCE,
            constants.GAME_OVER_LINE,
        )
        if self.state == constants.STATE_LOST:
            self.banner.show(constants.LOST_TEXT, constants.LOST_COLOR)
        elif self.state == constants.STATE_WON:
            self.banner.show(constants.WON_TEXT, constants.WON_COLOR)

    def step(self) -> None:
        """@brief Advance the game by one frame of game logic."""
        self.bullet.move()
        self.fleet.update(time.monotonic())
        self.check_bullet_hit()
        self.check_state()

    def tick(self) -> None:
        """@brief Advance the game by one frame; stop when the game has ended."""
        self.step()
        self.screen.update()
        if self.state == constants.STATE_PLAYING:
            self.screen.ontimer(self.tick, constants.FRAME_DELAY_MS)

    def run(self) -> None:
        """@brief Run the game until the window is closed."""
        self.tick()
        self.screen.mainloop()
