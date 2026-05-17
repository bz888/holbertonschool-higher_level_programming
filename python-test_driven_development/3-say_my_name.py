#!/usr/bin/python3
"""Module that provides a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a full name using first_name and last_name."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
