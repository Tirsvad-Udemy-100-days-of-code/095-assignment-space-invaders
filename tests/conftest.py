"""Shared fixtures.

Tests that open a `turtle` window run only when `SPACE_INVADERS_GUI_TESTS=1` is
set, which the Docker image of `tools/` does under a virtual display. On the
host they are skipped, so a test run never takes over the desktop.
"""

import os

import pytest


@pytest.fixture(scope="session")
def screen():
    """Yield a turtle screen; skip when GUI tests are off or no display exists."""
    if os.environ.get("SPACE_INVADERS_GUI_TESTS") != "1":
        pytest.skip("GUI tests run in the container (SPACE_INVADERS_GUI_TESTS=1)")
    try:
        import tkinter
        import turtle
    except ImportError as error:  # Tk libraries missing
        pytest.skip(f"turtle needs Tk: {error}")
    try:
        game_screen = turtle.Screen()
    except tkinter.TclError as error:  # no display
        pytest.skip(f"no usable display: {error}")
    game_screen.tracer(0)
    yield game_screen
    game_screen.bye()
