#!/usr/bin/python3
"""Module for appending UTF-8 text to a file."""


def append_write(filename="", text=""):
    """Append """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
