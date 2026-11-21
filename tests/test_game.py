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


def test_shooting_an_alien_scores_its_points(screen) -> None:
    from game import Game

    game = Game(screen)
    alien = game.fleet.aliens[0]
    game.bullet.fire(alien.xcor(), alien.ycor() - constants.BULLET_START_OFFSET)
    game.check_bullet_hit()
    assert game.scoreboard.score == constants.ALIEN_POINTS[0]
    assert not game.bullet.active


def test_an_alien_bullet_on_the_ship_costs_a_life(screen) -> None:
    from game import Game

    game = Game(screen)
    game.alien_bullet.fire(
        game.ship.xcor(), game.ship.ycor() + constants.BULLET_START_OFFSET
    )
    game.check_alien_bullet_hit()
    assert game.scoreboard.lives == constants.LIVES_START - 1
    assert not game.alien_bullet.active


def test_a_barrier_stops_an_alien_bullet(screen) -> None:
    from game import Game

    game = Game(screen)
    block = game.barriers.blocks[0]
    game.alien_bullet.fire(block.xcor(), block.ycor() + constants.BULLET_START_OFFSET)
    game.check_alien_bullet_hit()
    assert game.scoreboard.lives == constants.LIVES_START
    assert not game.alien_bullet.active


def test_the_aliens_fire_once_their_interval_has_passed(screen) -> None:
    import random

    from game import Game

    game = Game(screen, random.Random(1))
    game.alien_fire(game.last_alien_fire + constants.ALIEN_FIRE_INTERVAL / 2)
    assert not game.alien_bullet.active
    game.alien_fire(game.last_alien_fire + constants.ALIEN_FIRE_INTERVAL)
    assert game.alien_bullet.active
    assert game.alien_bullet.step < 0


def test_the_game_is_lost_when_the_last_life_is_gone(screen) -> None:
    from game import Game

    game = Game(screen)
    for _ in range(constants.LIVES_START):
        game.scoreboard.lose_life()
    game.check_state()
    assert game.state == constants.STATE_LOST
