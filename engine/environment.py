from dataclasses import dataclass

from engine.player import Player
from engine.pot import Pot
from engine.bag import Bag


@dataclass
class Observation:
    pot: Pot
    bag: Bag

class QuacksEnvironment:
    def __init__(self, player: Player):
        self.player = player
        self.pot = Pot()

    def step(self, action) -> tuple:
        """
        Step the environment with the given action. Action must be 0 (stop) or
        1 (draw).
        Return:
            - observation: An Observation object containing the current state of the
              pot and bag.
            - done: A boolean indicating whether the episode has ended (i.e. the
              pot has exploded or the player has stopped).
        """
        if action == 0:  # stop
            return Observation(pot=self.pot, bag=self.player.bag), True
        elif action == 1:  # draw a chip
            self.pot.add(self.player.bag.draw())
            # Return the observation and whether the pot has exploded
            obs = Observation(pot=self.pot, bag=self.player.bag)
            return obs, self.pot.has_exploded()
        else:
            raise ValueError("Invalid action. Action must be 0 (stop) or 1 (draw).")
        
    def reset(self) -> tuple:
        """
        Resets the environment to the initial state and returns the initial
        observation.
        """
        # Reset the pot and return the chips to the player's bag
        chips = self.pot.reset()
        self.player.bag.add(chips)

        # Return the initial observation
        return Observation(pot=self.pot, bag=self.player.bag), False
