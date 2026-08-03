import matplotlib.pyplot as plt

from engine.chips import Chip, ChipColor

# Map the ChipColor enum to hex color codes for visualization
CHIP_PALETTE = {
    ChipColor.WHITE: "#ffffff",
    ChipColor.ORANGE: "#ff7f00",
    ChipColor.BLACK: "#000000",
    ChipColor.RED: "#ff0000",
    ChipColor.BLUE: "#0000ff",
    ChipColor.YELLOW: "#f7ef08ff",
    ChipColor.GREEN: "#00ff00",
    ChipColor.PURPLE: "#800080",
}


class BoardPlotter:
    bg_ax: plt.Axes
    fg_ax: plt.Axes

    def __init__(self, board):
        self.board = board
        self.droplet_index = 0
        self._current_index = 0

    def _make_background(self):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def add(self, chip: Chip):
        raise NotImplementedError
