import matplotlib.pyplot as plt

from engine.chips import Chip, ChipColor
from render.board_plotter_utils import SpiralParams, draw_tile, make_board_spiral
from render.colors import SPIRAL_COLOR


class BoardPlotter:
    fig: plt.Figure  # The main figure for the board
    bg_ax: plt.Axes  # Background axis for the board
    fg_ax: plt.Axes  # Foreground axis for the chips and other dynamic elements

    def __init__(self):
        # self.board = board
        self.droplet_index = 0
        self._current_index = 0

        self._make_background()

        self.fig.savefig("spiral.png", dpi=300, bbox_inches="tight", pad_inches=0)

    def _make_background(self):
        """
        Create the background of the board, including the spiral and tiles.
        """

        # Create the spiral and tile coordinates (doesn't draw anything yet)
        spiral_coords, tile_coords = make_board_spiral(
            SpiralParams(
                spacing=0.5,
                a=0.0,
                bx=0.09,
                by=0.08,
                theta_0=1.2 * 3.14159,
            )
        )

        # Create the figure and axes for the board
        self.fig, self.bg_ax = plt.subplots(figsize=(8, 8))

        # Draw the background spiral
        self.bg_ax.plot(
            spiral_coords[:, 0],
            spiral_coords[:, 1],
            "-",
            markersize=5,
            linewidth=25,
            color=SPIRAL_COLOR,
            zorder=1,
        )

        # Draw each tile as a circle on the board
        for index, point in enumerate(tile_coords):
            draw_tile(self.bg_ax, index=index, xy=point, scale=1.0)

        # Set the background axis properties
        self.bg_ax.set_xticks([])
        self.bg_ax.set_yticks([])
        self.bg_ax.set_aspect("equal", adjustable="box")
        self.bg_ax.set_zorder(0)  # Set the z-order of the main axes to 0

        # Transparent overlay
        self.fg_ax = self.fig.add_axes(self.bg_ax.get_position(), frameon=False)
        self.fg_ax.set_xticks([])
        self.fg_ax.set_yticks([])
        self.fg_ax.set_xlim(self.bg_ax.get_xlim())
        self.fg_ax.set_ylim(self.bg_ax.get_ylim())

        self.fg_ax.set_zorder(1)
        self.fg_ax.plot(spiral_coords[:, 0], spiral_coords[:, 1], color="black")

    def clear(self):
        """
        Clear the board of all dynamic elements, such as chips and droplets,
        while keeping the background intact.
        """
        raise NotImplementedError

    def add(self, chip: Chip):
        """
        Add a chip to the board.
        """
        raise NotImplementedError

    def undo(self):
        """
        Undo the last placed chip on the board.
        """
        raise NotImplementedError
