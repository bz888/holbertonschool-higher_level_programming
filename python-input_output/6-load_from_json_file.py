#!/usr/bin/python3
"""Module for loading Python objects from JSON files."""

import json


def load_from_json_file(filename):
    """Return a Python object loaded from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
