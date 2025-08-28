import numpy as np

def isosceles_triangle(center=(0, 0), base=100, height=150, rotation=0):
    cx, cy = center
    points = np.array([
        [cx - base / 2, cy],
        [cx + base / 2, cy],
        [cx, cy + height]
    ])
    # Apply rotation
    theta = np.radians(rotation)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    rotated = np.dot(points - center, rotation_matrix) + center
    return rotated
