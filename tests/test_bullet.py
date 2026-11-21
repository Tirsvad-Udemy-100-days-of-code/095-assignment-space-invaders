"""Tests of the bullet; they need the GUI test environment."""

import constants


def test_bullet_is_hidden_until_it_is_fired(screen) -> None:
    from bullet import Bullet

    bullet = Bullet()
    assert not bullet.active
    assert not bullet.isvisible()


def test_bullet_appears_above_the_ship_and_flies_up(screen) -> None:
    from bullet import Bullet

    bullet = Bullet()
    bullet.fire(40, constants.SHIP_Y)
    assert bullet.active
    start = bullet.ycor()
    assert bullet.xcor() == 40
    assert start == constants.SHIP_Y + constants.BULLET_START_OFFSET
    bullet.move()
    assert bullet.ycor() == start + constants.BULLET_STEP


def test_only_one_bullet_flies_at_a_time(screen) -> None:
    from bullet import Bullet

    bullet = Bullet()
    bullet.fire(0, constants.SHIP_Y)
    bullet.move()
    flying_at = bullet.ycor()
    bullet.fire(100, constants.SHIP_Y)
    assert (bullet.xcor(), bullet.ycor()) == (0, flying_at)


def test_bullet_resets_after_leaving_the_top(screen) -> None:
    from bullet import Bullet

    bullet = Bullet()
    bullet.fire(0, constants.SCREEN_TOP)
    bullet.move()
    assert not bullet.active
    assert not bullet.isvisible()
