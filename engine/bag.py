from engine.chips import Chip, ChipColor
import random

def get_starting_chips():
    """
    Returns a list of the starting chips for each player.
    """
    chips = []
    chips.extend([Chip(1, ChipColor.WHITE)] * 4)
    chips.extend([Chip(2, ChipColor.WHITE)] * 2)
    chips.extend([Chip(3, ChipColor.WHITE)] * 1)
    chips.extend([Chip(1, ChipColor.ORANGE)] * 1)
    chips.extend([Chip(1, ChipColor.GREEN)] * 1)
    return chips


class Bag:
    def __init__(self, chips=None):
        self.chips = chips if chips is not None else []

    def __iter__(self):
        return iter(self.chips)
    
    def __len__(self):
        return len(self.chips)

    def add(self, chip: Chip | list[Chip]):
        """Add a chip to the bag."""        
        if isinstance(chip, list):
            self.chips.extend(chip)
        else:
            self.chips.append(chip)
    
    def draw(self):
        """
        Draw a random chip from the bag and return it. If the bag is empty,
        return None.
        """
        if not self.chips:
            return None
        
        chip = random.choice(self.chips)
        self.chips.remove(chip)
        return chip
