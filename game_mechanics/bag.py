from typing import List, Union
import random
from game_mechanics.enums import ChipColor

from .chips import Chip

# Data on the rewards associated with each slot on the board
COINS = [*range(1, 16), 15, 16, 16, 17, 17, 18, 18, 19, 19, 20,
         20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27,
         27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 35]

VICTORY_POINTS = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3,
                  3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8,
                  8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12,
                  12, 12, 13, 13, 13, 14, 14, 15]

RUBY = [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
        1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0]


class Bag():
    def __init__(self):
        self._chips = []

    def __str__(self):
        """
        Format bag contents in a short, human-readable way
        """
        s = '['
        for chip in self._chips:
            s += str(chip) + ', '
        return s[:-2] + ']'
    
    def __iter__(self):
        return iter(self._chips)

    def add(self, chip: Union[Chip, List[Chip]]):
        """
        Add a chip to a player's bag. This method is use both during
        the buying phase and when resetting the bag after a round
        """

        if isinstance(chip, list):
            self._chips.extend(chip)
        else:
            self._chips.append(chip)

    def remove(self, chip: Union[Chip, List[Chip]]):
        """
        Remove a chip or list of chips from the bag.
        """
        if isinstance(chip, list):
            for t in chip:
                self._chips.remove(t)
        else:
            self._chips.remove(chip)

    def draw(self):
        """
        Draw a chip from the bag uniformly at random and remove it from the
        bag
        """

        # Sample a chip from the bag uniformly at random
        chip = random.choice(self._chips)

        # Remove the chip from the bag
        self.remove(chip)

        # Return the drawn chip
        return chip


class Pot():
    def __init__(self):
        self.white_count = 0
        self.position = 0
        self.has_exploded = False

        self._chips = []
        self._chip_multiplier = 1
        self._explode_threshold = 7

    def __iter__(self):
        return iter(self._chips)

    def eval

    def place(self, chip: Chip):
        # Add the value of the chip to the current position
        self.position += chip.value * self.get_current_multiplier()

        # Check if the chip is white
        if chip.color == ChipColor.WHITE:
            self.white_count += chip.value

            # If the new chip makes us go over threshold we explode
            if self.white_count > self._explode_threshold:
                self.has_exploded = True

        # Add chip to the internal list of chips
        self._chips.append(chip)

    def remove_latest(self):
        # Remove chip from the pot
        chip = self._chips.pop()

        self.position -= self.get_current_multiplier() * chip.value

        return chip

    def empty(self):
        # Empty the pot but keep a copy
        chips = self._chips
        self._chips = []
        return chips

    def reset(self):
        assert len(self._chips) == 0
        """ Err"""

        # Reset white count and has_exploded)
        self.white_count = 0
        self.has_exploded = False

    def get_current_multiplier(self):
        # Check if the chip preceeding it was yellow, if so, we need to
        # subtract the double
        if len(self._chips) == 0:
            return 1
        elif self._chips[-1].color is not ChipColor.YELLOW:
            return 1
        else:
            return 2


