#!/usr/bin/python3
"""This module defines a Rectangle class."""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using width and height."""

    def __init__(self, width, height):
        """Initialize a rectangle with validated width and height."""
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
