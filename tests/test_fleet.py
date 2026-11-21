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
