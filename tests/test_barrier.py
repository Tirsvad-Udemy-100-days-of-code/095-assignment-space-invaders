"""Tests of the barriers; they need the GUI test environment."""

import constants


def test_barrier_wall_has_all_blocks(screen) -> None:
    from barrier import BarrierWall

    wall = BarrierWall()
    expected = (
        constants.BARRIER_GROUPS * constants.BARRIER_COLUMNS * constants.BARRIER_ROWS
    )
    assert len(wall.blocks) == expected


def test_a_block_wears_out_after_its_health_in_hits(screen) -> None:
    from barrier import BarrierBlock

    block = BarrierBlock(0, 0)
    for _ in range(constants.BARRIER_HEALTH - 1):
        assert not block.hit()
    assert block.hit()


def test_a_block_changes_colour_as_it_wears(screen) -> None:
    from barrier import BarrierBlock

    block = BarrierBlock(0, 0)
    full = block.color()[0]
    block.hit()
    assert block.color()[0] != full


def test_a_bullet_on_a_block_is_absorbed(screen) -> None:
    from barrier import BarrierWall

    wall = BarrierWall()
    block = wall.blocks[0]
    assert wall.absorb(block.xcor(), block.ycor())
    assert block.health == constants.BARRIER_HEALTH - 1


def test_a_bullet_between_barriers_passes(screen) -> None:
    from barrier import BarrierWall

    wall = BarrierWall()
    assert not wall.absorb(0, constants.BARRIER_Y)
    assert not wall.absorb(1000, 0)


def test_a_destroyed_block_leaves_the_wall(screen) -> None:
    from barrier import BarrierWall

    wall = BarrierWall()
    block = wall.blocks[0]
    for _ in range(constants.BARRIER_HEALTH):
        wall.absorb(block.xcor(), block.ycor())
    assert block not in wall.blocks
