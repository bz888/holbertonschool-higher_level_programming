#!/usr/bin/python3
"""This module defines a VerboseList class."""


class VerboseList(list):
    """Represent a list that prints messages when modified."""

    def append(self, item):
        """Append item to the list and print a message."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Extend the list with iterable and print a message."""
        length = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {length} items.")

    def remove(self, item):
        """Remove item from the list and print a message."""
        super().remove(item)
        print(f"Removed {item} from the list.")

    def pop(self, index=-1):
        """Pop item from the list and print a message."""
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
