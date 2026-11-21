"""@file game.py
@brief The game: it owns the objects, reads the keys and runs the frame loop.
"""

import random
import time
import turtle

import constants
import rules
from banner import Banner
from barrier import BarrierWall
from bullet import Bullet
from fleet import Fleet
from scoreboard import Scoreboard
from ship import Ship


class Game:
    """@brief Ties screen, ship, bullets, fleet, barriers and score together."""

    def __init__(
        self, screen: turtle.Screen, rng: random.Random | None = None
    ) -> None:
        """@brief Create the objects and bind the keys.

        @param screen The game window.
        @param rng Source of randomness for the alien shots; a new one by default.
        """
        self.screen = screen
        self.rng = rng or random.Random()
        self.ship = Ship()
        self.bullet = Bullet()
        self.alien_bullet = Bullet(
            constants.ALIEN_BULLET_COLOR, -constants.ALIEN_BULLET_STEP
        )
        self.fleet = Fleet()
        self.barriers = BarrierWall()
        self.scoreboard = Scoreboard()
        self.banner = Banner()
        self.state = constants.STATE_PLAYING
        self.last_alien_fire = time.monotonic()
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

    def alien_fire(self, now: float) -> None:
        """@brief Let an alien shoot when its time has come.

        @param now Current time in seconds.
        """
        if self.alien_bullet.active:
            return
        if not rules.is_due(now, self.last_alien_fire, constants.ALIEN_FIRE_INTERVAL):
            return
        shooter = self.fleet.choose_shooter(self.rng)
        if shooter is not None:
            self.last_alien_fire = now
            self.alien_bullet.fire(shooter.xcor(), shooter.ycor())

    def check_bullet_hit(self) -> None:
        """@brief Let the ship's bullet hit a barrier or an alien."""
        if not self.bullet.active:
            return
        x, y = self.bullet.xcor(), self.bullet.ycor()
        if self.barriers.absorb(x, y):
            self.bullet.reset_bullet()
            return
        points = self.fleet.remove_hit(x, y)
        if points:
            self.scoreboard.add_points(points)
            self.bullet.reset_bullet()

    def check_alien_bullet_hit(self) -> None:
        """@brief Let an alien bullet hit a barrier or the ship, which costs a life."""
        if not self.alien_bullet.active:
            return
        x, y = self.alien_bullet.xcor(), self.alien_bullet.ycor()
        if self.barriers.absorb(x, y):
            self.alien_bullet.reset_bullet()
        elif rules.is_hit(
            x, y, self.ship.xcor(), self.ship.ycor(), constants.SHIP_HIT_DISTANCE
        ):
            self.scoreboard.lose_life()
            self.alien_bullet.reset_bullet()

    def check_state(self) -> None:
        """@brief End the game with a message when it is lost or won."""
        self.state = rules.game_state(
            [(alien.xcor(), alien.ycor()) for alien in self.fleet.aliens],
            (self.ship.xcor(), self.ship.ycor()),
            constants.GAME_OVER_DISTANCE,
            constants.GAME_OVER_LINE,
            self.scoreboard.lives,
        )
        if self.state == constants.STATE_LOST:
            self.banner.show(constants.LOST_TEXT, constants.LOST_COLOR)
        elif self.state == constants.STATE_WON:
            self.banner.show(constants.WON_TEXT, constants.WON_COLOR)

    def step(self, now: float | None = None) -> None:
        """@brief Advance the game by one frame of game logic.

        @param now Current time in seconds; the clock by default.
        """
        now = time.monotonic() if now is None else now
        self.bullet.move()
        self.alien_bullet.move()
        self.fleet.update(now)
        self.alien_fire(now)
        self.check_bullet_hit()
        self.check_alien_bullet_hit()
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
