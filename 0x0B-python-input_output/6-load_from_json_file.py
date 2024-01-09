#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """A function that create a Python object from a JSON file."""
    with open(filename) as sl:
        return json.load(sl)
