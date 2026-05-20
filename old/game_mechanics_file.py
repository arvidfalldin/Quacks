from dataclasses import dataclass

from game_mechanics.bag import Bag
from game_mechanics.chips import Chip, ChipColor
from game_mechanics.pot import Pot


@dataclass
class PlayerState:
    name: str
    bag: Bag
    pot: Pot
    rubys: int
    victory_points: int
    droplet: int
    exploded: bool
    has_potion: bool
    coins: int

    def __str__(self):
        return self.name


@dataclass
class GameState:
    round: int
    players: list[PlayerState]
    # ingredient_books: dict  # Not sure what this is atm...
