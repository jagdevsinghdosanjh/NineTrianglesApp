import streamlit as st
from triangle_utils import isosceles_triangle, svg_triangle, render_symbolic_card # noqa
from metadata import load_triangle_meta
from streamlit_option_menu import option_menu
import json # noqa

# Load triangle metadata
TRIANGLE_META = load_triangle_meta()

# Page config
st.set_page_config(layout="wide")

# Inject CSS
def local_css(file_name):
    try:
        with open(file_name, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Missing {file_name}")

local_css("assets/style.css")

# Inject JS
try:
    with open("assets/triangle_cards.js") as f:
        st.markdown(f"<script>{f.read()}</script>", unsafe_allow_html=True)
except FileNotFoundError:
    st.error("Missing triangle_cards.js in assets folder.")

# Sidebar navigation
selected_element = option_menu(
    menu_title="Elemental Realms",
    options=["All", "Air", "Fire", "Water", "Earth", "Aether", "Metal", "Wood", "Light", "Shadow"],
    icons=["globe", "wind", "fire", "droplet", "tree", "stars", "gear", "leaf", "sun", "moon"],
    orientation="vertical"
)

# Filter triangles by element
if selected_element == "All":
    filtered_meta = TRIANGLE_META
else:
    filtered_meta = [m for m in TRIANGLE_META if m["element"] == selected_element]

# View selector
view = st.radio("Choose view", ["Disintegrated", "Integrated", "Symbolic"])

# Render SVG triangles
svg_elements = []
for meta in filtered_meta:
    center = (200 + meta["id"] * 20, 200 + meta["id"] * 10) if view == "Disintegrated" else (300, 300)
    points = isosceles_triangle(center=center, rotation=meta["rotation"])
    triangle_svg = svg_triangle(points, meta["symbol"], meta["element"], meta["name"], meta["lore"])
    svg_elements.append(triangle_svg)

st.markdown(f"""
<svg width="600" height="600">
    {' '.join(svg_elements)}
</svg>
""", unsafe_allow_html=True)

# Symbolic lore cards
if view == "Symbolic":
    st.markdown("### 🧬 Symbolic Lore of the Nine Triangles")
    st.markdown("""
    <div id="symbolic-card" class="symbolic-card">
        <h3>Click a triangle to reveal its lore</h3>
    </div>
    """, unsafe_allow_html=True)
