"""Render a cube without displaying axes."""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def main() -> None:
    """Display a cube in a Matplotlib window."""

    # Define the eight vertices of the cube.
    r = [0, 1]
    vertices = [[x, y, z] for x in r for y in r for z in r]

    # Define the six faces using the vertices above.
    faces = [
        [vertices[0], vertices[1], vertices[3], vertices[2]],
        [vertices[4], vertices[5], vertices[7], vertices[6]],
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[1], vertices[3], vertices[7], vertices[5]],
        [vertices[0], vertices[2], vertices[6], vertices[4]],
    ]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Add the cube's faces to the plot.
    ax.add_collection3d(
        Poly3DCollection(
            faces,
            facecolors="skyblue",
            edgecolors="black",
            linewidths=1,
            alpha=0.8,
        )
    )

    # Keep the cube proportional and hide axes completely.
    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()

    plt.show()


if __name__ == "__main__":
    main()
