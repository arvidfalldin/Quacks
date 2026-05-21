"""
This holds all the chips in the game, and their properties.
"""

from enum import Enum


class ChipColor(Enum):
    ORANGE = 0
    BLACK = 1
    RED = 2
    BLUE = 3
    GREEN = 4
    YELLOW = 5
    PURPLE = 6
    WHITE = 7


class Chip:
    def __init__(self, value: int, color: ChipColor):
        self.value = value
        self.color = color

    def __str__(self):
        if self.color == ChipColor.BLACK:
            return f"K{self.value}"
        else:
            return f"{self.color.name[0]}{self.value}"

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    """
    Just a quick test to print out all the chips in the game.
    """
    for color in ChipColor:
        for value in [1, 2, 4]:
            print(Chip(value, color))
