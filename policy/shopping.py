from dataclasses import dataclass

import numpy as np

from engine.chips import Chip, ChipColor
from engine.environment import Observation
from engine.marketplace import Marketplace


@dataclass
class ShoppingAction:
    chip: Chip
    ruby: bool


class ShoppingPolicy:
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwds):
        raise NotImplementedError("This method should be implemented by subclasses")


class RandomShopperPolicy(ShoppingPolicy):
    def __init__(self, marketplace: Marketplace, *args, **kwargs):
        super().__init__(name="RandomShopper")
        self.marketplace = marketplace

    def __call__(self, observation: Observation):
        # Get a boolean matrix of which items are available for purchase
        coins = observation.coins
        affordability_matrix = self.marketplace.get_affordability_matrix(coins)

        # Generate a matrix of random values
        random_matrix = np.random.rand(*affordability_matrix.shape)

        # Mask the random matrix with the affordability matrix
        masked_random_matrix = random_matrix * affordability_matrix

        # Get the indices of the maximum value in the masked random matrix
        max_indices = np.argwhere(masked_random_matrix == np.max(masked_random_matrix))

        color = ChipColor(max_indices[0][0])
        value = 2 ** max_indices[1][0]

        chip = Chip(color=color, value=value)
        return chip
