from dataclasses import dataclass
from .enums import ChipColor


@dataclass(frozen=True)
class Chip:
    value: int
    color: ChipColor

    def __str__(self):
        return self.color.value[0] + str(self.value)

    def __eq__(self, other):
        return self.value == other.value and self.color == other.color


    STARTING_CHIPS = [
    Chip(1, ChipColor.WHITE),
    Chip(1, ChipColor.WHITE),
    Chip(1, ChipColor.WHITE),
    Chip(1, ChipColor.WHITE),
    Chip(2, ChipColor.WHITE),
    Chip(2, ChipColor.WHITE),
    Chip(3, ChipColor.WHITE),
    Chip(1, ChipColor.GREEN),
    Chip(1, ChipColor.ORANGE),
]
