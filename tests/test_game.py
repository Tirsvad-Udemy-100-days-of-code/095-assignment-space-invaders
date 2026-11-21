"""Tests of the game flow; they need the GUI test environment."""

import constants


def test_the_game_starts_in_the_playing_state(screen) -> None:
    from game import Game

    assert Game(screen).state == constants.STATE_PLAYING


def test_the_game_is_lost_when_an_alien_touches_the_ship(screen) -> None:
    from game import Game

    game = Game(screen)
    game.fleet.aliens[0].goto(game.ship.xcor(), game.ship.ycor())
    game.check_state()
    assert game.state == constants.STATE_LOST


def test_the_game_is_won_when_the_last_alien_is_shot(screen) -> None:
    from game import Game

    game = Game(screen)
    for alien in list(game.fleet.aliens):
        game.fleet.remove_hit(alien.xcor(), alien.ycor())
    game.check_state()
    assert game.state == constants.STATE_WON


def test_the_ship_does_not_move_after_the_game_is_over(screen) -> None:
    from game import Game

    game = Game(screen)
    game.state = constants.STATE_LOST
    start = game.ship.xcor()
    game.move_left()
    game.move_right()
    game.fire()
    assert game.ship.xcor() == start
    assert not game.bullet.active
