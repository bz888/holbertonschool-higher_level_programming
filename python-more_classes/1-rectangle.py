#!/usr/bin/python3
"""Defines a rectangle."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
