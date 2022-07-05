#!/usr/bin/python3
"""Module 6-load_from_json_file.
Creates an Object from a “JSON file”.
"""


def load_from_json_file(filename):
    """Creates an object from filename.
    Returns: the object
    """

    with open(filename) as f:
        return json.load(f)
