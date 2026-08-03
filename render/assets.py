"""
Here we collect function for generating visuial assets for the pygame view,
such as the background image or token markers
"""

import numpy as np
import matplotlib.pyplot as plt

from engine.constants import NUM_TILES

def make_spiral_points(
        a: float = 0.1,
        b: float = 0.21,
        dtheta: float = 0.001,
        spacing: float = 1.2,
        theta_0: float = 3,
        num_tiles: int = 53
        ) -> np.ndarray:

    theta = theta_0

    arc_length = 0

    r0 = a + b * theta_0
    x0 = r0 * np.cos(theta_0)
    y0 = r0 * np.sin(theta_0)
    last_point = np.array([x0, y0])

    points = []

    while len(points) < num_tiles:
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

        last_point = point
        theta += dtheta

        theta_span = np.array([theta_0, theta])

    return np.array(points), theta_span

def make_background_image(
        filename: str,
        width: int = 1024,
        height: int = 1024,
        dpi: int = 100,
        spiral_a: float = 0.1,
        spiral_b: float = 0.21,
        square_spacing: float = 1.2):
    
    fig, ax = plt.subplots(figsize=(width/dpi, height/dpi), dpi=dpi)

    # Create a spiral pattern
    theta = np.linspace(0, 10 * np.pi, 1000)
    r = np.linspace(0.1, 5, 1000)
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    ax.plot(x, y, color='black', linewidth=0.5)
    ax.set_aspect('equal')
    ax.axis('off')

    fig.savefig(filename, bbox_inches='tight', dpi=dpi)