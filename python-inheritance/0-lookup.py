#!/usr/bin/python3
"""This module defines a function for object attribute lookup."""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)
