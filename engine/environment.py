from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING

from engine.bag import Bag
from engine.player import Player
from engine.pot import Pot

if TYPE_CHECKING:
    from policy.brewing import BrewingAction
    from policy.shopping import ShoppingAction


class GamePhase(Enum):
    BREWING = "brewing"
    CHIPS = "chips"
    RUBIES = "rubies"


# You can buy a potion for 2 rubies
POTION_COST = 2


@dataclass
class Observation:
    phase: GamePhase
    pot: Pot
    bag: Bag
    potion_available: bool
    victory_points: int
    rubies: int
    coins: int


class QuacksEnvironment:
    def __init__(self, player: Player):
        self.player = player
        self.pot = Pot()

        self.marketplace = None  # This will be set externally, as it may depend on the ingredient set used in the game

    def step(self, action: ShoppingAction | BrewingAction) -> tuple:
        """
        Step the environment with the given action. Action must be 0 (stop) or
        1 (draw).
        Return:
            - observation: An Observation object containing the current state of the
              pot and bag.
            - done: A boolean indicating whether the episode has ended (i.e. the
              pot has exploded or the player has stopped).
        """
        if isinstance(action, BrewingAction):
            return self._brewing_step(action)
        elif isinstance(action, ShoppingAction):
            return self._shopping_step(action)
        else:
            raise ValueError(
                "Invalid action type. Action must be BrewingAction or ShoppingAction."
            )

    def _brewing_step(self, action: BrewingAction) -> tuple:
        """
        Step the environment during the brewing phase. Action must be 0 (stop) or
        1 (draw).
        Return:
            - observation: An Observation object containing the current state of the
                pot and bag.
        """

        if action == 0:  # stop
            return Observation(
                pot=self.pot,
                bag=self.player.bag,
                potion_available=self.player.potion_available,
                victory_points=self.player.victory_points,
                rubies=self.player.rubies,
                phase=GamePhase.BREWING,
                coins=self.player.coins,
            ), True
        elif action == 1:  # draw a chip
            self.pot.add(self.player.bag.draw())
            # Return the observation and whether the pot has exploded
            obs = Observation(
                pot=self.pot,
                bag=self.player.bag,
                potion_available=self.player.potion_available,
                victory_points=self.player.victory_points,
                rubies=self.player.rubies,
                phase=GamePhase.BREWING,
                coins=self.player.coins,
            )
            return obs, self.pot.has_exploded()
        else:
            raise ValueError("Invalid action. Action must be 0 (stop) or 1 (draw).")

    def _shopping_step(self, action: ShoppingAction) -> tuple:
        """
        Step the environment during the shopping phase. Action must be a
        ShoppingAction object.
        Return:
            - observation: An Observation object containing the current state of the
                pot and bag.
            - done: A boolean indicating whether the episode has ended (i.e. the
                player has bought an item).
        """
        # Check if the player can afford to buy either a chip or a ruby
        chip_cost = self.marketplace.get_chip_cost(chip=action.chip)

    def reset(self) -> tuple:
        """
        Resets the environment to the initial state and returns the initial
        observation.
        """
        # Reset the pot and return the chips to the player's bag
        chips = self.pot.reset()
        self.player.bag.add(chips)

        # Return the initial observation
        return Observation(
            pot=self.pot,
            bag=self.player.bag,
            potion_available=self.player.potion_available,
            victory_points=self.player.victory_points,
            rubies=self.player.rubies,
            phase=GamePhase.BREWING,
        ), False
