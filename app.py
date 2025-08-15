import streamlit as st
from triangle_utils import isosceles_triangle, svg_triangle, render_symbolic_card
from metadata import load_triangle_meta


def local_css(file_name):
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        local_css("assets/style.css")

# Load triangle metadata
TRIANGLE_META = load_triangle_meta()

# Page config
st.set_page_config(layout="wide")

# Inject CSS
try:
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.error("Missing style.css in assets folder.")

# Inject JS
try:
    with open("assets/triangle_cards.js") as f:
        st.markdown(f"<script>{f.read()}</script>", unsafe_allow_html=True)
except FileNotFoundError:
    st.error("Missing triangle_cards.js in assets folder.")

# View selector
view = st.radio("Choose view", ["Disintegrated", "Integrated", "Symbolic"])

# Render SVG triangles
if view in ["Disintegrated", "Integrated"]:
    svg_elements = []
    for meta in TRIANGLE_META:
        center = (200 + meta["id"] * 20, 200 + meta["id"] * 10) if view == "Disintegrated" else (300, 300)
        points = isosceles_triangle(center=center, rotation=meta["rotation"])
        svg_elements.append(svg_triangle(points, meta["symbol"], meta["element"]))

    st.markdown(f"""
    <svg width="600" height="600">
        {' '.join(svg_elements)}
    </svg>
    """, unsafe_allow_html=True)

# Render symbolic lore cards
elif view == "Symbolic":
    st.markdown("### 🧬 Symbolic Lore of the Nine Triangles")
    for meta in TRIANGLE_META:
        st.markdown(render_symbolic_card(meta), unsafe_allow_html=True)

    # Add interactive card container
    st.markdown("""
    <div id="symbolic-card" class="symbolic-card">
        <h3>Click a triangle to reveal its lore</h3>
    </div>
    """, unsafe_allow_html=True)
