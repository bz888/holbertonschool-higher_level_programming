#!/usr/bin/python3
"""Module for converting an object to a JSON-serializable dictionary."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON."""
    return obj.__dict__
