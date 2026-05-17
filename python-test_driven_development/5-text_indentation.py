#!/usr/bin/python3
"""Module that provides text indentation."""


def text_indentation(text):
    """Print text with two new lines after '.', '?', and ':' characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0

    for i in range(len(text)):
        if text[i] in ".?:":
            print(text[start:i + 1].strip())
            print()
            start = i + 1

    if start < len(text):
        print(text[start:].strip(), end="")
