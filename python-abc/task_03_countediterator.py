#!/usr/bin/python3
"""This module defines a CountedIterator class."""


class CountedIterator:
    """Represent an iterator that counts how many items were retrieved."""

    def __init__(self, iterable):
        """Initialize the iterator and counter."""
        self.__counter = 0
        self.__iterator = iter(iterable)

    def get_count(self):
        """Return the number of items retrieved so far."""
        return self.__counter

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next item and increment the counter."""
        item = next(self.__iterator)
        self.__counter += 1
        return item
