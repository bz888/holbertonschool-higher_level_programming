#!/usr/bin/python3
"""This module defines a Dragon class using mixins."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon that can swim, fly, and roar."""

    def roar(self):
        """Print roaring behavior."""
        print("The dragon roars!")


if __name__ == "__main__":
    draco = Dragon()

    draco.fly()
    draco.swim()
    draco.roar()
