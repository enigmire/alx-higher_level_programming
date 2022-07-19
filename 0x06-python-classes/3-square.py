#!/usr/bin/python3

class Square:
    """ Square with size """
    def __init__(self, size=0):
        self.size = size
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        elif self.size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.size * self.size
