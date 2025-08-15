import streamlit as st
from triangle_utils import isosceles_triangle, svg_triangle
#from metadata import TRIANGLE_META
from metadata import load_triangle_meta
TRIANGLE_META = load_triangle_meta()

st.set_page_config(layout="wide")
st.markdown("<style>" + open("assets/style.css").read() + "</style>", unsafe_allow_html=True)

view = st.radio("Choose view", ["Disintegrated", "Integrated", "Symbolic"])

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

elif view == "Symbolic":
    st.markdown("### 🧬 Symbolic Lore of the Nine Triangles")
    for meta in TRIANGLE_META:
        st.markdown(render_symbolic_card(meta), unsafe_allow_html=True)

st.markdown("<style>" + open("assets/style.css").read() + "</style>", unsafe_allow_html=True)
st.markdown("<script>" + open("assets/triangle_cards.js").read() + "</script>", unsafe_allow_html=True)

st.markdown("""
<div id="symbolic-card" class="symbolic-card">
    <h3>Click a triangle to reveal its lore</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("<script>" + open("assets/triangle_cards.js").read() + "</script>", unsafe_allow_html=True)
