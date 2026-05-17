#!/usr/bin/python3
"""Module that provides integer addition."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Args:
        a: First integer or float.
        b: Second integer or float. Defaults to 98.

    Raises:
        TypeError: If a or b is not an integer or float.

    Returns:
        The sum of a and b after casting floats to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
