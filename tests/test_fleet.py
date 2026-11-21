"""Tests of the alien fleet; they need the GUI test environment."""

import constants


def test_fleet_has_all_aliens(screen) -> None:
    from fleet import Fleet

    fleet = Fleet()
    assert len(fleet.aliens) == constants.ALIEN_ROWS * constants.ALIEN_COLUMNS


def test_every_row_has_its_own_colour(screen) -> None:
    from fleet import Fleet

    fleet = Fleet()
    first_of_each_row = fleet.aliens[:: constants.ALIEN_COLUMNS]
    colours = [alien.color()[0] for alien in first_of_each_row]
    assert colours == list(constants.ALIEN_COLORS)


def test_fleet_waits_for_the_interval_before_it_moves(screen) -> None:
    from fleet import Fleet

    fleet = Fleet()
    start = fleet.aliens[0].xcor()
    assert not fleet.update(fleet.last_move + constants.FLEET_MOVE_INTERVAL / 2)
    assert fleet.aliens[0].xcor() == start


def test_fleet_moves_sideways_once_the_interval_has_passed(screen) -> None:
    from fleet import Fleet

    fleet = Fleet()
    start = fleet.aliens[0].xcor()
    assert fleet.update(fleet.last_move + constants.FLEET_MOVE_INTERVAL)
    assert fleet.aliens[0].xcor() == start + constants.FLEET_STEP_X


def test_fleet_drops_closer_when_it_reaches_the_edge(screen) -> None:
    from fleet import Fleet

    fleet = Fleet()
    top = fleet.aliens[0].ycor()
    for _ in range(40):
        fleet.move()
        if fleet.aliens[0].ycor() < top:
            break
    assert fleet.aliens[0].ycor() == top - constants.FLEET_DROP
    assert fleet.direction == -1


def test_a_bullet_on_an_alien_removes_it(screen) -> None:
    from fleet import Fleet

    fleet = Fleet()
    target = fleet.aliens[0]
    assert fleet.remove_hit(target.xcor(), target.ycor())
    assert len(fleet.aliens) == constants.ALIEN_ROWS * constants.ALIEN_COLUMNS - 1
    assert target not in fleet.aliens


def test_a_bullet_in_empty_space_hits_nothing(screen) -> None:
    from fleet import Fleet

    fleet = Fleet()
    assert not fleet.remove_hit(0, constants.SHIP_Y)
    assert len(fleet.aliens) == constants.ALIEN_ROWS * constants.ALIEN_COLUMNS


def test_the_fleet_moves_faster_when_aliens_are_gone(screen) -> None:
    from fleet import Fleet

    fleet = Fleet()
    for alien in fleet.aliens[: len(fleet.aliens) // 2]:
        fleet.remove_hit(alien.xcor(), alien.ycor())
    start = fleet.aliens[0].xcor()
    assert fleet.update(fleet.last_move + constants.FLEET_MOVE_INTERVAL / 2)
    assert fleet.aliens[0].xcor() == start + constants.FLEET_STEP_X


def test_a_hit_returns_the_points_of_the_alien(screen) -> None:
    from fleet import Fleet

    fleet = Fleet()
    top = fleet.aliens[0]
    assert fleet.remove_hit(top.xcor(), top.ycor()) == constants.ALIEN_POINTS[0]


def test_the_shooter_is_the_lowest_alien_of_its_column(screen) -> None:
    import random

    from fleet import Fleet

    fleet = Fleet()
    shooter = fleet.choose_shooter(random.Random(1))
    column = [alien for alien in fleet.aliens if alien.column == shooter.column]
    assert shooter.ycor() == min(alien.ycor() for alien in column)


def test_nobody_shoots_when_no_alien_is_left(screen) -> None:
    import random

    from fleet import Fleet

    fleet = Fleet()
    for alien in list(fleet.aliens):
        fleet.remove_hit(alien.xcor(), alien.ycor())
    assert fleet.choose_shooter(random.Random(1)) is None
