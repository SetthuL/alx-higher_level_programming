#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Public instance method
        that prints the list, but sorted (ascending sort)."""
        print(sorted(self))
