#!/usr/bin/python3
"""This module defines a MyList class."""


class MyList(list):
    """A custom list class with a method to print a sorted copy."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
