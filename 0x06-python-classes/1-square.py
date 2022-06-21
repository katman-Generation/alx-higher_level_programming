#!/usr/bin/python3
""" Module for task 0 of 0x06-Python-classes project -
write an empty class Square that defines a square """


class Square:
    """Represents a square.
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """Initializes the data."""
        self.__size = size
