#!/usr/bin/python3
"""This module defines a function for checking class inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class, but is not exactly it."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
