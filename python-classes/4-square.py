#!/usr/bin/python3
"""This module defines a class Square that represents a square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        self.size = size  # Use setter to validate

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
