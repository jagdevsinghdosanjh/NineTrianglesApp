# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np

# # Define triangle drawing function
# def draw_triangle(ax, center, size, rotation, color):
#     # Create an isosceles triangle
#     h = size * np.sqrt(3) / 2
#     points = np.array([
#         [0, h / 2],
#         [-size / 2, -h / 2],
#         [size / 2, -h / 2]
#     ])
#     # Rotate
#     theta = np.radians(rotation)
#     rot_matrix = np.array([
#         [np.cos(theta), -np.sin(theta)],
#         [np.sin(theta),  np.cos(theta)]
#     ])
#     rotated = points @ rot_matrix.T
#     # Translate
#     translated = rotated + np.array(center)
#     triangle = plt.Polygon(translated, color=color, edgecolor='black')
#     ax.add_patch(triangle)

# # Element definitions
# elements = [
#     {"name": "Fire", "color": "#FF4500", "rotation": 0},
#     {"name": "Water", "color": "#1E90FF", "rotation": 45},
#     {"name": "Earth", "color": "#8B4513", "rotation": 90},
#     {"name": "Air", "color": "#B0E0E6", "rotation": 135},
#     {"name": "Aether", "color": "#DA70D6", "rotation": 180},
#     {"name": "Light", "color": "#FFFF00", "rotation": 225},
#     {"name": "Shadow", "color": "#2F4F4F", "rotation": 270},
#     {"name": "Ice", "color": "#00CED1", "rotation": 315},
#     {"name": "Metal", "color": "#C0C0C0", "rotation": 30}
# ]

# # Streamlit UI
# st.set_page_config(page_title="Elemental Yantra", layout="centered")
# st.title("🔺 Elemental Yantra Mandala")
# st.write("A symbolic arrangement of nine elemental triangles inspired by the Sri Yantra.")

# # Plot setup
# fig, ax = plt.subplots(figsize=(8, 8))
# ax.set_aspect('equal')
# ax.axis('off')

# # Draw concentric circles (lotus petals)
# for r in [2.5, 3.5]:
#     circle = plt.Circle((0, 0), r, color='lightgray', fill=False, linestyle='dashed')
#     ax.add_patch(circle)

# # Draw outer square (temple gates)
# square_size = 5
# square = plt.Rectangle((-square_size/2, -square_size/2), square_size, square_size,
#                        fill=False, edgecolor='gray', linewidth=2)
# ax.add_patch(square)

# # Draw triangles radially
# radius = 2.8
# angle_step = 360 / len(elements)
# for i, elem in enumerate(elements):
#     angle = i * angle_step
#     x = radius * np.cos(np.radians(angle))
#     y = radius * np.sin(np.radians(angle))
#     draw_triangle(ax, (x, y), size=1.2, rotation=elem["rotation"], color=elem["color"])
#     ax.text(x, y + 0.9, elem["name"], ha='center', va='center', fontsize=10)

# # Draw central triangle (bindu)
# draw_triangle(ax, (0, 0), size=1.5, rotation=elements[4]["rotation"], color=elements[4]["color"])
# ax.text(0, -0.8, elements[4]["name"], ha='center', va='center', fontsize=12, fontweight='bold')

# # Display
# st.pyplot(fig)
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

# Triangle drawing function
def draw_triangle(center, size, rotation, facecolor):
    angle_rad = np.deg2rad(rotation)
    vertices = []
    for i in range(3):
        theta = angle_rad + i * 2 * np.pi / 3
        x = center[0] + size * np.cos(theta)
        y = center[1] + size * np.sin(theta)
        vertices.append((x, y))
    triangle = patches.Polygon(vertices, closed=True, facecolor=facecolor, edgecolor='black')
    ax.add_patch(triangle)

# Draw central triangle
draw_triangle((0, 0), 2, 0, 'gold')
ax.text(0, 0, 'Center', ha='center', va='center', fontsize=10, color='black')

# Define colors and labels for 8 surrounding triangles
colors = ['red', 'blue', 'green', 'purple', 'orange', 'cyan', 'magenta', 'lime']
labels = ['Fire', 'Water', 'Earth', 'Air', 'Ether', 'Light', 'Darkness', 'Spirit']

# Draw 8 surrounding triangles in polar coordinates
radius = 5
for i in range(8):
    angle = i * 2 * np.pi / 8
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    draw_triangle((x, y), 1.5, np.rad2deg(angle), colors[i])
    ax.text(x, y, labels[i], ha='center', va='center', fontsize=9, color='black')

# Draw concentric circles for lotus petals
for r in [6, 7, 8]:
    circle = patches.Circle((0, 0), r, fill=False, edgecolor='pink', linestyle='dashed')
    ax.add_patch(circle)

# Draw outer square for temple gates
square = patches.Rectangle((-9, -9), 18, 18, fill=False, edgecolor='brown', linewidth=2)
ax.add_patch(square)

# Save the figure
output_path = '/data/elemental_yantra.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, bbox_inches='tight')
plt.close()

print("Elemental Yantra image saved as 'elemental_yantra.png'")
