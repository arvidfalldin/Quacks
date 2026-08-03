import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

from engine.constants import COINS, NUM_TILES, RUBY, VICTORY_POINTS

SPIRAL_COLOR = [187 / 255, 227 / 255, 213 / 255]
TILE_COLOR = [124 / 255, 208 / 255, 162 / 255]
VICTORY_POINT_COLOR = "#f2deaaff"


def theta2xy(theta, a=0.1, bx=0.21, by=0.21):
    """
    tmp
    """
    x = (a + theta * bx) * np.cos(theta)
    y = (a + theta * by) * np.sin(theta)
    return [x, y]


def make_spiral_points(a, bx, by, theta_0, spacing=1.0, delta_theta=0.01):

    theta = theta_0

    tile_points = [theta2xy(theta, a=a, bx=bx, by=by)]
    spiral_points = [theta2xy(theta, a=a, bx=bx, by=by)]

    while len(tile_points) < NUM_TILES:
        theta += delta_theta
        spiral_points.append(theta2xy(theta, a=a, bx=bx, by=by))

        # Check the straight line distance between the last tile point and the current spiral point
        last_tile_point = tile_points[-1]
        current_spiral_point = spiral_points[-1]
        distance = np.linalg.norm(
            np.array(current_spiral_point) - np.array(last_tile_point)
        )

        if distance >= spacing:
            tile_points.append(current_spiral_point)

    return np.array(spiral_points), np.array(tile_points)


def draw_tile(ax, index, xy, scale=1.0):
    radius = 0.2 * scale
    circle = patches.Circle(xy, radius=radius, color=TILE_COLOR, fill=True)
    ax.add_patch(circle)

    width = 0.15 * scale
    height = 0.13 * scale
    xy_anchor = (
        xy[0] + np.cos(np.deg2rad(225)) * radius,
        xy[1] + np.sin(np.deg2rad(225)) * radius,
    )

    # Add number indicating how many victory points the tile is worth
    xy_text = (
        xy[0] + 0.55 * np.cos(np.deg2rad(225)) * radius,
        xy[1] + 0.45 * np.sin(np.deg2rad(225)) * radius,
    )

    ax.text(
        xy_text[0],
        xy_text[1],
        str(VICTORY_POINTS[index]),
        ha="center",
        va="center",
        fontsize=10,
        color="black",
        rasterized=False,
        rotation=10,
    )

    rectangle = patches.Rectangle(
        xy=xy_anchor,
        angle=10,
        width=width,
        height=height,
        color=VICTORY_POINT_COLOR,
        fill=True,
    )
    ax.add_patch(rectangle)

    if RUBY[index]:
        ruby_radius = 0.05 * scale
        radial_offset_factor = 1.0
        xy_ruby = (
            xy[0] + radial_offset_factor * np.sqrt(3) / 2 * radius,
            xy[1] + radial_offset_factor * 0.5 * radius,
        )
        ruby_hexagon = patches.RegularPolygon(
            xy_ruby, numVertices=6, radius=ruby_radius, color="red", fill=True
        )
        ax.add_patch(ruby_hexagon)

    # Write the coin value of the tile in the top center of the circle
    xy_coin = (xy[0], xy[1] + 0.5 * radius)
    ax.text(
        xy_coin[0],
        xy_coin[1],
        str(COINS[index]),
        ha="center",
        va="center",
        fontsize=10,
        color="black",
        rasterized=False,
        rotation=0,
        fontweight="bold",
    )


if __name__ == "__main__":
    points, tile_points = make_spiral_points(
        theta_0=1.2 * np.pi, spacing=0.5, a=0.0, bx=0.09, by=0.08
    )

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.plot(
        points[:, 0],
        points[:, 1],
        "-",
        markersize=5,
        linewidth=25,
        color=SPIRAL_COLOR,
        zorder=1,
    )

    for index, point in enumerate(tile_points):
        draw_tile(ax, index=index, xy=point, scale=1.0)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal", adjustable="box")

    ax.set_zorder(0)  # Set the z-order of the main axes to 0

    # Transparent overlay
    ax1 = fig.add_axes(ax.get_position(), frameon=False)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_xlim(ax.get_xlim())
    ax1.set_ylim(ax.get_ylim())

    ax1.set_zorder(1)
    ax1.plot(points[:, 0], points[:, 1], color="black")

    fig.savefig("spiral.png", dpi=300, bbox_inches="tight", pad_inches=0)
