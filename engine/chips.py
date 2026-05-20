"""
This holds all the chips in the game, and their properties.
"""

from enum import Enum

class ChipColor(Enum):
    WHITE = 0
    ORANGE = 1
    BLACK = 2
    RED = 3
    BLUE = 4
    YELLOW = 5
    GREEN = 6
    PURPLE = 7


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
