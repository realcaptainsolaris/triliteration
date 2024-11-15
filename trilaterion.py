import matplotlib.pyplot as plt
import numpy as np

# Define satellite positions and distances (example)
satellite_positions = np.array(
    [[0, 0], [10, 0], [5, 8.66]]
)  # Triangle vertices for satellites
distances = np.array([6, 7, 5])  # Example distances

# Create a grid for plotting
x = np.linspace(-2, 12, 400)
y = np.linspace(-2, 12, 400)
X, Y = np.meshgrid(x, y)

# Calculate circles for trilateration
circle1 = (
    (X - satellite_positions[0, 0]) ** 2
    + (Y - satellite_positions[0, 1]) ** 2
    - distances[0] ** 2
)
circle2 = (
    (X - satellite_positions[1, 0]) ** 2
    + (Y - satellite_positions[1, 1]) ** 2
    - distances[1] ** 2
)
circle3 = (
    (X - satellite_positions[2, 0]) ** 2
    + (Y - satellite_positions[2, 1]) ** 2
    - distances[2] ** 2
)

# Plot the satellites and circles
plt.figure(figsize=(8, 8))
plt.contour(
    X,
    Y,
    circle1,
    levels=[0],
    colors="r",
    linestyles="dashed",
    label="Satellite 1 Distance",
)
plt.contour(
    X,
    Y,
    circle2,
    levels=[0],
    colors="g",
    linestyles="dashed",
    label="Satellite 2 Distance",
)
plt.contour(
    X,
    Y,
    circle3,
    levels=[0],
    colors="b",
    linestyles="dashed",
    label="Satellite 3 Distance",
)

# Plot the satellite positions
for i, pos in enumerate(satellite_positions):
    plt.scatter(pos[0], pos[1], label=f"Satellite {i+1}", s=100)

# Add labels and legend
plt.title("Trilateration: Intersection of Circles")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.legend(
    ["Satellite 1 Circle", "Satellite 2 Circle", "Satellite 3 Circle", "Satellites"]
)
plt.grid()
plt.show()
