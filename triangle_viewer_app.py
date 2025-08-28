import streamlit as st
import matplotlib.pyplot as plt
import json
import numpy as np
from triangle_utility import isosceles_triangle
# Load lore
with open("data/lore.json", encoding="utf-8") as f:
    lore_data = json.load(f)["triangles"]

st.title("🔺 Elemental Triangle Visualizer")

# Select triangle
selected = st.selectbox("Choose a triangle:", lore_data, format_func=lambda x: x["name"])

# Extract data
rotation = selected["rotation"]
symbol = selected["symbol"]
mantra = selected["mantra"]
lore = selected["lore"]
element = selected["element"]

# Display info
st.markdown(f"### {symbol} {selected['name']}")
st.markdown(f"**Element:** {element}")
st.markdown(f"**Mantra:** _{mantra}_")
st.markdown(f"**Lore:** {lore}")

# Draw triangle
triangle = isosceles_triangle(center=(0, 0), base=100, height=150, rotation=rotation)
triangle_closed = np.vstack([triangle, triangle[0]])

fig, ax = plt.subplots()
ax.plot(triangle_closed[:, 0], triangle_closed[:, 1], color="orange", linewidth=2)
ax.fill(triangle_closed[:, 0], triangle_closed[:, 1], color="gold", alpha=0.3)
ax.set_aspect("equal")
ax.axis("off")
st.pyplot(fig)
