import numpy as np

from engine.bag import Bag
from engine.pot import EXPLOTION_THRESHOLD as ET
from engine.pot import Pot
from engine.chips import ChipColor


def explosion_probability(pot: Pot, bag: Bag) -> float:
    """
    Calculate the probability of the pot exploding on the next draw.
    This is a simple heuristic based on the current state of the pot and the bag.
    
    When playing by the original rules it is impossible to empty the bag
    without exploding but in the special case of an empty bag the function
    will return 0.0 since there are no chips to draw.
    """

    white_count = pot.get_white_count()
    
    # Case 1: Immune to explosion
    if white_count < ET - 2:
        return 0.0

    # Case 2: Only white-3 chips will cause explosion
    elif white_count == ET - 2:
        # Count the number of white-3 chips in the bag
        w3_chips = [c for c in bag if c.color == ChipColor.WHITE and c.value >= 3]
        return len(w3_chips) / len(bag) if len(bag) > 0 else 0.0

    # Case 3: White-2 and white-3 chips will cause explosion    
    elif white_count == ET - 1:
        # Count the number of w3 and w2 chips in the bag
        w23_chips = [c for c in bag if c.color == ChipColor.WHITE and c.value >= 2]
        return len(w23_chips) / len(bag) if len(bag) > 0 else 0.0

    # Case 4: Any white chip will cause explosion
    elif white_count == ET:
        # Count the number of white chips in the bag
        w_chips = [c for c in bag if c.color == ChipColor.WHITE]
        return len(w_chips) / len(bag) if len(bag) > 0 else 0.0