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
