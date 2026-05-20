from engine.chips import Chip, ChipColor


NUM_TILES = 53
COINS = [*range(1, 16), 15, 16, 16, 17, 17, 18, 18, 19, 19, 20,
         20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27,
         27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 35]
VICTORY_POINTS = [
    0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3,
    3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8,
    8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12,
    12, 12, 13, 13, 13, 14, 14, 15]
RUBY = [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
        1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0]
EXPLOTION_THRESHOLD = 7

class Pot():
    def __init__(self, droplet_index=0):
        self.chips = []
        self.droplet_index = droplet_index
        self.current_index = droplet_index
        self.white_count = 0
    
    def __str__(self):
        msg = "Pot: "
        for chip in self.chips:
            msg += f"{chip}, "
        
        # Remove trailing comma and space
        msg = msg[:-2] + "\n"

        msg += f"White count: {self.white_count}"

        if self.has_exploded():
            msg += " (Exploded)"
        msg += "\n"

        msg += f"Coins: {self.current_coins()}\n"
        msg += f"Victory pts: {self.current_victory_points()}\n"
        msg += f"Ruby: {self.at_ruby()}\n"
        return msg

    def __repr__(self):
        return self.__str__()

    def add(self, chip):
        
        if self.has_exploded():
            raise ValueError("Cannot add chips to an exploded pot.")

        # Add the chip to the pot
        self.chips.append(chip)
        
        # Add the value of the chip to the current index
        self.current_index += chip.value

        # Increment the white count if the chip is white
        self.white_count += chip.value * (chip.color == ChipColor.WHITE)
    
    def has_exploded(self) -> bool:
        return self.white_count > EXPLOTION_THRESHOLD

    def at_ruby(self) -> bool:
        return RUBY[self.current_index]

    def current_coins(self) -> int:
        return COINS[self.current_index]

    def current_victory_points(self) -> int:
        return VICTORY_POINTS[self.current_index]
    
    def get_white_count(self) -> int:
        return self.white_count

    def reset(self) -> list[Chip]:
        """
        Resets the pot and returns the chips that were in it.
        """
        # Reset white count
        self.white_count = 0

        # Reset current index to droplet index
        self.current_index = self.droplet_index

        # Return the chips that were in the pot and clear the pot
        chips = self.chips.copy()
        self.chips = []
        return chips