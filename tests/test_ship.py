"""Tests of the spaceship; they need the GUI test environment."""

import constants


def test_ship_starts_at_the_bottom_centre(screen) -> None:
    from ship import Ship

    ship = Ship()
    assert (ship.xcor(), ship.ycor()) == (0, constants.SHIP_Y)


def test_ship_moves_one_step_left_and_right(screen) -> None:
    from ship import Ship

    ship = Ship()
    ship.go_right()
    assert ship.xcor() == constants.SHIP_STEP
    ship.go_left()
    ship.go_left()
    assert ship.xcor() == -constants.SHIP_STEP


def test_ship_stops_at_the_screen_edges(screen) -> None:
    from ship import Ship

    ship = Ship()
    for _ in range(100):
        ship.go_right()
    assert ship.xcor() <= constants.SHIP_MAX_X
    for _ in range(200):
        ship.go_left()
    assert ship.xcor() >= -constants.SHIP_MAX_X
