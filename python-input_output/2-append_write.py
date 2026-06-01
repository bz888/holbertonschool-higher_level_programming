#!/usr/bin/python3
"""Module for appending UTF-8 text to a file."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file and return the number of characters added."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
