from math import inf

import numpy as np

from engine.chips import Chip, ChipColor


class IngredientSet2:
    def __init__(self):
        # Define the costs of each ingredient
        self.ingredient_costs = {color: {} for color in ChipColor}

        # Define cost of each ingredient for each color (colors that cannot be bought
        # have cost of inf)

        # --- ORANGE ---
        self.ingredient_costs[ChipColor.ORANGE] = {1: 3, 2: inf, 4: inf}
        # --- BLACK ---
        self.ingredient_costs[ChipColor.BLACK] = {1: 10, 2: inf, 4: inf}
        # --- RED ---
        self.ingredient_costs[ChipColor.RED] = {1: 6, 2: 10, 4: 16}
        # --- BLUE ---
        self.ingredient_costs[ChipColor.BLUE] = {1: 5, 2: 10, 4: 19}
        # --- GREEN ---
        self.ingredient_costs[ChipColor.GREEN] = {1: 6, 2: 11, 4: 18}
        # --- YELLOW ---
        self.ingredient_costs[ChipColor.YELLOW] = {1: 9, 2: 13, 4: 19}
        # --- PURPLE ---
        self.ingredient_costs[ChipColor.PURPLE] = {1: 12, 2: inf, 4: inf}
        # --- WHITE ---
        self.ingredient_costs[ChipColor.WHITE] = {1: inf, 2: inf, 4: inf}

        # Construct a matrix of costs for easier access
        self.cost_matrix = np.array(
            [
                [self.ingredient_costs[color][value] for value in [1, 2, 4]]
                for color in ChipColor
            ]
        )

    def get_chip_cost(
        self, chip: Chip = None, color: ChipColor = None, value: int = None
    ):
        if chip is None and (color is None or value is None):
            raise ValueError("Must provide either a chip or both color and value.")

        if chip is not None:
            color = chip.color
            value = chip.value
        return self.ingredient_costs[color][value]


class Marketplace:
    def __init__(self, round: int = 0, ingredient_set: IngredientSet2 = None):
        self.round = round
        self.ingredient_set = ingredient_set

    def get_affordability_matrix(self, player_coins: int):
        return self.ingredient_set.cost_matrix <= player_coins


if __name__ == "__main__":
    ingredients = IngredientSet2()

    marketplace = Marketplace(ingredient_set=ingredients)
    print("Affordability matrix for player with 10 coins:")
    print(marketplace.get_affordability_matrix(player_coins=10))
