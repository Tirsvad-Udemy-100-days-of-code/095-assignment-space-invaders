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
