#!/usr/bin/python3
"""This module defines abstract shapes and concrete shape classes."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Represent an abstract shape."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius):
        """Initialize a circle with a radius."""
        self.__radius = abs(radius)

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with width and height."""
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Print the area and perimeter of a shape."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
