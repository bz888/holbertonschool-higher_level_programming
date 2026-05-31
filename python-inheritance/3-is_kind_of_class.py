#!/usr/bin/python3
"""This module defines a function for checking class inheritance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclass."""
    return isinstance(obj, a_class)
