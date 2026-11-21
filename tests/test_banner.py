"""Tests of the end message; they need the GUI test environment."""

import constants


def test_banner_is_centred_and_hidden(screen) -> None:
    from banner import Banner

    banner = Banner()
    assert (banner.xcor(), banner.ycor()) == (0, constants.BANNER_Y)
    assert not banner.isvisible()
