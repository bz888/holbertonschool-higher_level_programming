#!/usr/bin/python3
"""This module defines Fish, Bird, and FlyingFish classes."""


class Fish:
    """Represent a fish."""

    def swim(self):
        """Print the fish swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish habitat."""
        print("The fish lives in water")


class Bird:
    """Represent a bird."""

    def fly(self):
        """Print the bird flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represent a flying fish."""

    def fly(self):
        """Print the flying fish flying behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print the flying fish swimming behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the flying fish habitat."""
        print("The flying fish lives both in water and the sky!")
