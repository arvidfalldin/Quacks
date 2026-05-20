import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import rcParams
import os


class BoardPlotter():
    def __init__(self,
                 tile_radius=.75):
        self.fig, self.ax = plt.subplots(
            1,
            1,
            figsize=(8, 8)
        )
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        self.tile_radius = tile_radius

        self.n_tiles = 53
        self.coins = [*range(1, 16), 15, 16, 16, 17, 17, 18, 18, 19, 19, 20,
                      20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27,
                      27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 35]
        self.victory_points = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3,
                               3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8,
                               8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12,
                               12, 12, 13, 13, 13, 14, 14, 15]
        self.ruby = [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
                     1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0,
                     0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0]

    def plot_empty_board(self):

        # Init curve paramtrization as all zeros
        self.t = np.zeros((self.n_tiles))

        # some carfully chosen params :)
        d = 2
        r = .5
        self.t[0] = 2.2
        self.t[1] = 4.4

        # Create each tile, and store the (x, y) coord
        for i in range(0, self.n_tiles):
            if i > 1:
                kappa = np.sqrt(self.t[i-1]**2 + 1)
                self.t[i] = -0.001*self.t[i-1] + np.sqrt(2*d/r + kappa*self.t[i-1] + np.log(kappa + self.t[i-1])) + 1/(1 + 1*self.t[i-1])
            x = r*self.t[i]*np.cos(self.t[i])
            y = r*self.t[i]*np.sin(self.t[i])
            patch = patches.Circle((x, y),
                                   2*self.tile_radius,
                                   color=[0, 0.6, 0.6],
                                   facecolor=None)
            self.ax.add_patch(patch)
            coin_string = f"{self.coins[i]}"
            self.ax.text(x-0.4*len(coin_string),
                         y-0.07,
                         coin_string,
                         fontsize=18,
                         color='white')

        self.ax.set_xlim([-15, 15])
        self.ax.set_ylim([-15, 15])

    def save_plot(self, path='Quacks_board.png'):
        self.fig.savefig(os.path.join(path), bbox_inches='tight')


if __name__ == "__main__":
    rcParams['font.weight'] = 'bold'

    board_plotter = BoardPlotter()
    board_plotter.plot_empty_board()

    board_plotter.save_plot()
