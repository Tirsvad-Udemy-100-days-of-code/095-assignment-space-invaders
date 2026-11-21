"""Screenshot scenario: the fleet has reached the ship, so the game is lost."""

import sys

sys.path.insert(0, "src")

import main  # noqa: E402
from game import Game  # noqa: E402

game = Game(main.create_screen())
for alien in game.fleet.aliens:
    alien.sety(alien.ycor() - 480)
game.run()
