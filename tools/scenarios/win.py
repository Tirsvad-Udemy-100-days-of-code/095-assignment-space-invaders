"""Screenshot scenario: the last alien is gone, so the game is won."""

import sys

sys.path.insert(0, "src")

import main  # noqa: E402
from game import Game  # noqa: E402

game = Game(main.create_screen())
for alien in list(game.fleet.aliens):
    game.fleet.remove_hit(alien.xcor(), alien.ycor())
game.run()
