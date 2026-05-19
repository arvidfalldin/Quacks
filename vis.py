import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Circle, Rectangle

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


class SquareIllustrator():
    def __init__(self):
        pass


class MarkerIllustrator():
    def __init__(self):
        pass


class BoardIllustrator():
    def __init__(self):
        self.squares = []

    def draw_empty_board(self):
        pass

    def draw_rollout(self, droplet_position: int, rat_tails: int, rollout: list):
        pass

    def clear_rollout(self):
        pass

    def index2xy(self, index: int):
        pass

    def save(self, filename: str):
        pass


class Droplet:
    def __init__(self, position: int = 0, rat_tails: int = 0):
        self.default_position = position
        self.rat_tails = rat_tails

    def draw(self, ax):
        pass


class Square:
    """
    class to represent a square on the game board
    """
    def __init__(self, index: int, victory_points: int, coins: int, ruby: bool):
        self.index = index
        self.victory_points = victory_points
        self.coins = coins
        self.ruby = ruby

    def draw(self, ax, x, y, show_index=False, text_epsilon=0.01):
        """
        draw the square on the given axes at the specified coordinates
        """
        bg_color = '#7cd0a2'

        radius = 0.4
        circle_patch = Circle((x, y), radius, color=bg_color, fill=True)
        ax.add_patch(circle_patch)
        if show_index:
            ax.text(x, y, str(self.index), fontsize=8, ha='center', va='center')

        if self.ruby:
            # Place it at North East of the square
            xruby = x + radius / np.sqrt(2)
            yruby = y + radius / np.sqrt(2)

            ruby_patch = Circle((xruby, yruby), 0.1, color='red', fill=True)
            ax.add_patch(ruby_patch)

        # Display the victory points at the West/South-West of the square
        vp_x = x + radius * np.cos(7*np.pi/6)
        vp_y = y + radius * np.sin(7*np.pi/6)

        vp_patch = Rectangle((vp_x - 0.15, vp_y - 0.15),
                             0.3,
                             0.3,
                             color='#dcbb89',
                             fill=True)
        # Add text for victory points
        text = ax.text(vp_x, vp_y,
                       str(self.victory_points),
                       fontsize=5,
                       ha='center',
                       va='center',
                       color='#000000',
                       weight='bold',)

        text = ax.text(vp_x + text_epsilon, vp_y + text_epsilon,
                       str(self.victory_points),
                       fontsize=5,
                       ha='center',
                       va='center',
                       color='#a97a38',
                       weight='bold',)


        text.set_visible(False)

        text.set_visible(True)

        ax.add_patch(vp_patch)

        # North, inside the square, display the number of coins
        ax.text(x, y + 0.25 * radius, str(self.coins),
                fontsize=6,
                ha='center',
                va='center',
                weight='bold',
                color='black')

        # North, inside the square, display the number of coins
        ax.text(x + text_epsilon,
                y + 0.25 * radius + text_epsilon,
                str(self.coins),
                fontsize=6,
                ha='center',
                va='center',
                weight='bold',
                color='white')



a = 0.1
b = 0.21
spacing = 1.2   # distance between circles

epsilon = 0.05  # small value to prevent circles from touching
radius = spacing / 2 - epsilon

theta_0 = 3

theta = theta_0
dtheta = 0.001

points = []

arc_length = 0

r0 = a + b * theta_0
x0 = r0 * np.cos(theta_0)
y0 = r0 * np.sin(theta_0)
last_point = np.array([x0, y0])

tiles = 0

while tiles < NUM_TILES:
    rx = a + b * theta
    ry = rx * 0.9
    x = rx * np.cos(theta)
    y = ry * np.sin(theta)
    point = np.array([x, y])

    ds = np.linalg.norm(point - last_point)
    arc_length += ds

    if arc_length >= spacing:
        points.append(point)
        arc_length = 0
        tiles += 1

    last_point = point
    theta += dtheta

points = np.array(points)

# Plot circles

fig, ax = plt.subplots()
# Plot the spiral as a think line in the background
spiral_theta = np.linspace(theta_0 + 1.5 , theta, 1000)
spiral_r = a + b * spiral_theta
spiral_x = spiral_r * np.cos(spiral_theta)
spiral_y = 0.9 * spiral_r * np.sin(spiral_theta)
ax.plot(spiral_x, spiral_y, color='#b9e3d5', linewidth=10, zorder=0)

for i, p in enumerate(points):
    # circle = plt.Circle(p, radius, fill=False)
    # ax.add_patch(circle)
    # ax.text(p[0], p[1], str(i), fontsize=8, ha='center', va='center')
    square = Square(i+1, victory_points=VICTORY_POINTS[i], ruby=RUBY[i],
                    coins=COINS[i])
    square.draw(ax, p[0], p[1], show_index=False)


# droplet_position = 1

# x, y = points[droplet_position - 1]
# droplet_patch = Circle((x, y), 0.4, color='red', fill=True)
# ax.add_patch(droplet_patch)

# droplet_symbol_patch1 = Circle((x, y), 0.2, color='white', fill=True)
# ax.add_patch(droplet_symbol_patch1)

# droplet_symbol_patch2 = Rectangle((x-0.1, y-0.1 + np.sqrt(2)*0.1),
#                                   0.2,
#                                   0.2,
#                                   rotation_point='center',
#                                   angle=45,
#                                   color='white', fill=True)
# ax.add_patch(droplet_symbol_patch2)


# shrink_factor = 0.6
# droplet_symbol_patch3 = Circle((x, y), 0.2*shrink_factor, color='red', fill=True)
# ax.add_patch(droplet_symbol_patch3)

# droplet_symbol_patch4 = Rectangle((x-0.1*shrink_factor,
#                                    y-(0.1 - np.sqrt(2)*0.1)*shrink_factor),
#                                   0.2*shrink_factor,
#                                   0.2*shrink_factor,
#                                   rotation_point='center',
#                                   angle=45,
#                                   color='red', fill=True)
# ax.add_patch(droplet_symbol_patch4)

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.axis('off')

ax.set_aspect('equal')

fig.savefig('spiral_circles.png', bbox_inches='tight', dpi=600)
fig.savefig('spiral_circles.jpg', bbox_inches='tight', dpi=600)
fig.savefig('spiral_circles.pdf', bbox_inches='tight', dpi=600)
fig.savefig('spiral_circles.svg', bbox_inches='tight', dpi=600)
