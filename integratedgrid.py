import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import json

# --- Triangle Geometry ---
def isosceles_triangle(center=(0, 0), base=100, height=150, rotation=0):
    cx, cy = center
    points = np.array([
        [cx - base / 2, cy],
        [cx + base / 2, cy],
        [cx, cy + height]
    ])
    theta = np.radians(rotation)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    rotated = np.dot(points - center, rotation_matrix) + center
    return rotated

# --- Load Lore Data ---
@st.cache_data
def load_lore():
    with open("data/lore.json", encoding="utf-8") as f:
        data = json.load(f)
    return data["triangles"]

triangles = load_lore()

# --- UI Setup ---
st.set_page_config(page_title="Unified Triangle Codex", layout="wide")
st.title("🌌 Unified Elemental Triangle Codex")

# --- Grid Layout Parameters ---
cols = 3
spacing_x = 300
spacing_y = 300
fig, ax = plt.subplots(figsize=(12, 8))

for i, tri in enumerate(triangles):
    row = i // cols
    col = i % cols
    center = (col * spacing_x, -row * spacing_y)

    # Draw triangle
    triangle = isosceles_triangle(center=center, base=100, height=150, rotation=tri["rotation"])
    triangle_closed = np.vstack([triangle, triangle[0]])
    ax.plot(triangle_closed[:, 0], triangle_closed[:, 1], color="darkorange", linewidth=2)
    ax.fill(triangle_closed[:, 0], triangle_closed[:, 1], color="gold", alpha=0.4)

    # Add labels
    ax.text(center[0], center[1] - 100, f"{tri['symbol']} {tri['name']}", ha="center", fontsize=10, weight="bold")
    ax.text(center[0], center[1] - 120, f"Element: {tri['element']}", ha="center", fontsize=8)
    ax.text(center[0], center[1] - 140, f"“{tri['mantra']}”", ha="center", fontsize=7, style="italic")

ax.set_aspect("equal")
ax.axis("off")
st.pyplot(fig)
