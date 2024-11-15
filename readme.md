# README: Trilateration Visualization Script

## What Does This Script Do?

This Python script visualizes the concept of **trilateration**, a key principle used in GPS for determining a position based on distances from multiple reference points (satellites). The script:

- Simulates three satellites with known positions.
- Represents their respective distances from an unknown point (receiver) as circles.
- Visualizes how the intersection of these circles determines the receiver's location.

## How Does It Work?

1. **Satellite Positions**: The satellites are defined as points in a 2D space, each having a fixed coordinate.
2. **Distances**: Example distances are provided for each satellite to the receiver.
3. **Visualization**: Using Python's `matplotlib`:
   - Circles are drawn to represent the area around each satellite where the receiver could be.
   - The intersection of these circles is the estimated receiver position.

### Steps to Run the Script

- Ensure Python 3 is installed along with `matplotlib` and `numpy`.
- Copy and run the script in any Python environment (e.g., Jupyter Notebook, VS Code).
- The script will generate a graph showing the satellites, their coverage areas (circles), and their overlap.

## Learning Source

The concept of trilateration is widely used in GPS and other positioning systems. To deepen your understanding:

- [Introduction to GPS and Trilateration](https://captain-solaris.medium.com/understanding-how-smartphone-location-tracking-works-0bf9ba6d0fe0) (Example Medium blog to reference)
- Research resources on satellite-based navigation and geolocation algorithms.

This script is a simplified 2D representation to help beginners grasp the mathematical and visual foundation of trilateration.
