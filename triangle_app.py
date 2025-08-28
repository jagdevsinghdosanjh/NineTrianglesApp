import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from triangle_utils import isosceles_triangle

st.title("Isosceles Triangle Visualizer")

# User inputs
base = st.slider("Base Length", 50, 300, 100)
height = st.slider("Height", 50, 300, 150)
rotation = st.slider("Rotation (degrees)", 0, 360, 0)
center_x = st.slider("Center X", 0, 400, 200)
center_y = st.slider("Center Y", 0, 400, 200)

# Get triangle points
triangle = isosceles_triangle(base, height, center=(center_x, center_y), rotation=rotation)

# Plotting
fig, ax = plt.subplots()
triangle_closed = np.vstack([triangle, triangle[0]])  # Close the triangle
ax.plot(triangle_closed[:, 0], triangle_closed[:, 1], 'b-')
ax.fill(triangle_closed[:, 0], triangle_closed[:, 1], 'skyblue', alpha=0.5)
ax.set_aspect('equal')
ax.set_xlim(0, 400)
ax.set_ylim(0, 400)
st.pyplot(fig)
