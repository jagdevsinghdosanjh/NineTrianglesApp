import streamlit as st
import numpy as np
import json
import os
import matplotlib.pyplot as plt

# --- Triangle Generator ---
def isosceles_triangle(center=(0, 0), base=1.0, height=1.0):
    cx, cy = center
    half_base = base / 2
    return np.array([
        [cx - half_base, cy],
        [cx + half_base, cy],
        [cx, cy + height]
    ])

# --- Lore Loader ---
path = os.path.join("data", "lore.json")
       
def load_lore(path):
    if not os.path.exists(path):
        st.error(f"Missing lore file at: {path}")
        return None
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            st.success("Lore loaded successfully.")
            return data
    except Exception as e:
        st.error(f"Error loading lore: {e}")
        return None

# --- Diagnostic Panel ---
st.title("🔍 Triangle App Diagnostic")

# 1. Triangle Generation Test
st.subheader("1️⃣ Triangle Generation")
triangle = isosceles_triangle(center=(0, 0), base=2.0, height=3.0)
if triangle is not None and triangle.shape == (3, 2):
    st.success("Triangle generated correctly.")
    st.write("Triangle coordinates:", triangle)
else:
    st.error("Triangle generation failed.")

# 2. Lore File Test
st.subheader("2️⃣ Lore File Check")
lore = load_lore(path)
if lore:
    st.write("Sample lore entry:", lore[0] if isinstance(lore, list) else list(lore.items())[0])

# 3. View Mode Logic
st.subheader("3️⃣ View Mode Selection")
view_mode = st.radio("Choose view mode:", ["Integrated", "Stacked", "Horizontal"])
st.write("Selected view mode:", view_mode)

# 4. Triangle Plot Test
st.subheader("4️⃣ Triangle Plot Preview")
fig, ax = plt.subplots()
triangle_closed = np.vstack([triangle, triangle[0]])  # Close the triangle
ax.plot(triangle_closed[:, 0], triangle_closed[:, 1], 'r-')
ax.set_title("Triangle Preview")
st.pyplot(fig)

# 5. Fallback Message
if triangle is None or lore is None:
    st.warning("Some components failed to load. Check triangle logic and lore file.")
