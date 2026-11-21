"""@file rules.py
@brief Game rules that need no screen, so they can be tested without a display.
"""


def clamp(value: float, low: float, high: float) -> float:
    """@brief Limit a value to a range.

    @param value The value to limit.
    @param low The smallest allowed value.
    @param high The largest allowed value.
    @return `low` if the value is below it, `high` if above it, else the value.
    """
    return max(low, min(high, value))


def has_left_screen_top(y: float, top: float) -> bool:
    """@brief Tell whether something moving up has passed the top edge.

    @param y Vertical position.
    @param top Vertical position of the top edge.
    @return True when `y` is above `top`.
    """
    return y > top


def fleet_positions(
    rows: int, columns: int, spacing_x: float, spacing_y: float, top_y: float
) -> list[tuple[float, float]]:
    """@brief Work out where each alien of a centred grid starts.

    @param rows Number of rows.
    @param columns Number of aliens per row.
    @param spacing_x Horizontal distance between aliens.
    @param spacing_y Vertical distance between rows.
    @param top_y Vertical position of the top row.
    @return Positions row by row, each row from left to right.
    """
    left = -spacing_x * (columns - 1) / 2
    return [
        (left + column * spacing_x, top_y - row * spacing_y)
        for row in range(rows)
        for column in range(columns)
    ]


def is_due(now: float, last: float, interval: float) -> bool:
    """@brief Tell whether an interval has passed since the last time.

    @param now Current time in seconds.
    @param last Time of the previous move in seconds.
    @param interval Seconds between two moves.
    @return True when at least `interval` seconds have passed.
    """
    return now - last >= interval


def next_fleet_move(
    xs: list[float], direction: int, step: float, edge: float, drop: float
) -> tuple[float, float, int]:
    """@brief Decide the next move of the fleet.

    The fleet keeps going sideways. When the next step would take an alien past
    the edge, it drops instead and turns around.

    @param xs Horizontal positions of all aliens.
    @param direction 1 for right, -1 for left.
    @param step Pixels to move sideways.
    @param edge Largest allowed distance from the centre.
    @param drop Pixels to move down when turning.
    @return The change in x, the change in y (negative is down) and the new direction.
    """
    if xs and max(abs(x + step * direction) for x in xs) > edge:
        return 0, -drop, -direction
    return step * direction, 0, direction
