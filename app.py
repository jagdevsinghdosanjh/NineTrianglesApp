import streamlit as st
from triangle_utils import isosceles_triangle,svg_triangle
from metadata import load_triangle_meta
from streamlit_option_menu import option_menu

# 🔺 Sacred Geometry SVG Generator
# def svg_triangle(points, symbol, element, name, lore):
#     point_str = " ".join([f"{x},{y}" for x, y in points])
#     cx, cy = points[2]  # tip of triangle

#     return f"""
#     <g class="triangle-group">
#       <polygon points="{point_str}" class="triangle"
#         data-symbol="{symbol}"
#         data-element="{element}"
#         data-name="{name}"
#         data-lore="{lore.replace('"', '&quot;')}" />
#       <circle cx="{cx}" cy="{cy}" r="10" fill="none" stroke="gold" stroke-width="2" />
#       <text x="{cx}" y="{cy + 4}" text-anchor="middle">{symbol}</text>
#     </g>
#     """

# 🔧 Page config
st.set_page_config(layout="wide")

# 📦 Load triangle metadata
TRIANGLE_META = load_triangle_meta()

# 🎨 Inject CSS
def local_css(file_name):
    try:
        with open(file_name, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Missing CSS file: {file_name}")

local_css("assets/style.css")

# 🌌 Sidebar navigation
selected_element = option_menu(
    menu_title="Elemental Realms",
    options=["All", "Air", "Fire", "Water", "Earth", "Aether", "Metal", "Wood", "Light", "Shadow"],
    icons=["globe", "wind", "fire", "droplet", "tree", "stars", "gear", "leaf", "sun", "moon"],
    orientation="vertical",
    key="element_selector"
)

# 🔍 Filter triangles by element
filtered_meta = (
    TRIANGLE_META if selected_element == "All"
    else [m for m in TRIANGLE_META if m["element"] == selected_element]
)

if not filtered_meta:
    st.warning(f"No triangles found for {selected_element} realm.")

# 🧭 View selector
view = st.radio("Choose view", ["Disintegrated", "Integrated", "Symbolic"], key="view_selector")

# 🔺 Triangle rendering
svg_elements = []
for meta in filtered_meta:
    center = (300, 300) if view == "Symbolic" else (200 + meta["id"] * 20, 200 + meta["id"] * 10)
    points = isosceles_triangle(center=center, rotation=meta["rotation"])
    triangle_svg = svg_triangle(
        points,
        symbol=meta["symbol"],
        element=meta["element"],
        name=meta["name"],
        lore=meta["lore"]
    )
    svg_elements.append(triangle_svg)

# 🖼️ Render SVG
st.markdown(f"""
<svg width="600" height="600">
    {' '.join(svg_elements)}
</svg>
""", unsafe_allow_html=True)

# 📜 Symbolic lore display
if view == "Symbolic":
    st.markdown("### 🧬 Symbolic Lore of the Nine Triangles")

    triangle_names = [meta["name"] for meta in filtered_meta]
    selected_triangle = st.selectbox("Choose a triangle to reveal its lore", triangle_names, key="triangle_selector")

    selected_meta = next((m for m in filtered_meta if m["name"] == selected_triangle), None)
    if selected_meta:
        st.markdown(f"""
        <div class="symbolic-card">
            <h3>{selected_meta['symbol']} ({selected_meta['element']})</h3>
            <h4>{selected_meta['name']}</h4>
            <p>{selected_meta['lore']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<svg width="1200" height="1200">
  <polygon points="100,100 200,100 150,50" stroke="white" fill="red" />
</svg>
""", unsafe_allow_html=True)
