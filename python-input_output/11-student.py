#!/usr/bin/python3
"""Module defining a Student class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student."""
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }

        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student."""
        for key, value in json.items():
            setattr(self, key, value)
