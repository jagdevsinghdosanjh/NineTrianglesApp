import streamlit as st
import json
import math

# Load triangle data from JSON
@st.cache_data
def load_triangles():
    with open("lore.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("triangles", [])

# Generate triangle points based on rotation
def generate_triangle_points(rotation, radius=100, center=(300, 300)):
    cx, cy = center
    angle_rad = math.radians(rotation)
    tip_x = cx + radius * math.cos(angle_rad)
    tip_y = cy + radius * math.sin(angle_rad)

    base_angle1 = math.radians(rotation + 120)
    base_angle2 = math.radians(rotation + 240)

    base_x1 = cx + radius * 0.6 * math.cos(base_angle1)
    base_y1 = cy + radius * 0.6 * math.sin(base_angle1)

    base_x2 = cx + radius * 0.6 * math.cos(base_angle2)
    base_y2 = cy + radius * 0.6 * math.sin(base_angle2)

    return f"{tip_x:.1f},{tip_y:.1f} {base_x1:.1f},{base_y1:.1f} {base_x2:.1f},{base_y2:.1f}"

# Render a single triangle as SVG
def render_svg_triangle(triangle):
    points = generate_triangle_points(triangle["rotation"])
    svg = f"""
    <svg width="600" height="600" xmlns="http://www.w3.org/2000/svg">
        <polygon points="{points}" 
                 style="fill:lightblue;stroke:black;stroke-width:2"
                 data-symbol="{triangle['symbol']}"
                 data-element="{triangle['element']}"
                 data-name="{triangle['name']}"
                 data-lore="{triangle['lore']}" />
        <text x="10" y="20" font-size="16">{triangle['symbol']} {triangle['name']}</text>
        <text x="10" y="40" font-size="12" fill="gray">{triangle['lore']}</text>
    </svg>
    """
    st.components.v1.html(svg, height=300)

# Disintegrated view: one triangle at a time
def render_disintegrated_view(triangles):
    st.subheader("🔹 Disintegrated Triangles")
    for triangle in triangles:
        st.markdown(f"### {triangle['symbol']} {triangle['name']}")
        render_svg_triangle(triangle)
        st.divider()

# Integrated view: all triangles in one SVG
def render_integrated_view(triangles):
    st.subheader("🔸 Integrated Mandala")
    svg_parts = []
    for t in triangles:
        points = generate_triangle_points(t["rotation"])
        svg_parts.append(
            f'<polygon points="{points}" style="fill:none;stroke:black;stroke-width:2"/>'
        )
    svg = f"""
    <svg width="600" height="600" xmlns="http://www.w3.org/2000/svg">
        {''.join(svg_parts)}
    </svg>
    """
    st.components.v1.html(svg, height=600)

# Symbolic view: lore and overlays
def render_symbolic_view(triangles):
    st.subheader("🔺 Symbolic Overlays & Lore")
    for triangle in triangles:
        st.markdown(f"### {triangle['symbol']} {triangle['name']}")
        st.markdown(f"**Element**: {triangle['element']}")
        st.markdown(f"**Mantra**: `{triangle['mantra']}`")
        st.markdown(f"**Lore**: {triangle['lore']}")
        render_svg_triangle(triangle)
        st.divider()

# View selector
def render_view_selector():
    st.sidebar.title("🔻 View Options")
    selected_view = st.sidebar.radio("Choose a view", ["Integrated", "Disintegrated", "Symbolic"])
    triangles = load_triangles()

    if selected_view == "Integrated":
        render_integrated_view(triangles)
    elif selected_view == "Disintegrated":
        render_disintegrated_view(triangles)
    elif selected_view == "Symbolic":
        render_symbolic_view(triangles)

# Entry point
if __name__ == "__main__":
    st.set_page_config(page_title="Nine Triangles", layout="wide")
    st.title("🔷 Nine Triangles of Elemental Lore")
    render_view_selector()

# import streamlit as st
# import json

# # Load triangle data from JSON
# @st.cache_data
# def load_triangles():
#     with open("lore.json", "r", encoding="utf-8") as f:
#         data = json.load(f)
#     return data.get("triangles", [])

# # Render a single triangle as SVG
# def render_svg_triangle(triangle):
#     points = triangle.get("points", "50,15 100,100 0,100")  # Default if missing
#     svg = f"""
#     <svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
#         <polygon points="{points}" 
#                  style="fill:lightblue;stroke:black;stroke-width:2"
#                  data-symbol="{triangle['symbol']}"
#                  data-element="{triangle['element']}"
#                  data-name="{triangle['name']}"
#                  data-lore="{triangle['lore']}" />
#         <text x="10" y="20" font-size="16">{triangle['symbol']} {triangle['name']}</text>
#         <text x="10" y="40" font-size="12" fill="gray">{triangle['lore']}</text>
#     </svg>
#     """
#     st.components.v1.html(svg, height=300)

# # Disintegrated view: one triangle at a time
# def render_disintegrated_view(triangles):
#     st.subheader("🔹 Disintegrated Triangles")
#     for triangle in triangles:
#         st.markdown(f"### {triangle['symbol']} {triangle['name']}")
#         render_svg_triangle(triangle)
#         st.divider()

# # Integrated view: all triangles in one SVG
# def render_integrated_view(triangles):
#     st.subheader("🔸 Integrated Mandala")
#     svg_parts = []
#     for t in triangles:
#         points = t.get("points", "")
#         if points:
#             svg_parts.append(
#                 f'<polygon points="{points}" style="fill:none;stroke:black;stroke-width:2"/>'
#             )
#     svg = f"""
#     <svg width="600" height="600" xmlns="http://www.w3.org/2000/svg">
#         {''.join(svg_parts)}
#     </svg>
#     """
#     st.components.v1.html(svg, height=600)

# # Symbolic view: lore and overlays
# def render_symbolic_view(triangles):
#     st.subheader("🔺 Symbolic Overlays & Lore")
#     for triangle in triangles:
#         st.markdown(f"### {triangle['symbol']} {triangle['name']}")
#         st.markdown(f"**Element**: {triangle['element']}")
#         st.markdown(f"**Mantra**: `{triangle['mantra']}`")
#         st.markdown(f"**Lore**: {triangle['lore']}")
#         render_svg_triangle(triangle)
#         st.divider()

# # View selector
# def render_view_selector():
#     st.sidebar.title("🔻 View Options")
#     selected_view = st.sidebar.radio("Choose a view", ["Integrated", "Disintegrated", "Symbolic"])
#     triangles = load_triangles()

#     if selected_view == "Integrated":
#         render_integrated_view(triangles)
#     elif selected_view == "Disintegrated":
#         render_disintegrated_view(triangles)
#     elif selected_view == "Symbolic":
#         render_symbolic_view(triangles)

# # Entry point
# if __name__ == "__main__":
#     st.set_page_config(page_title="Nine Triangles", layout="wide")
#     st.title("🔷 Nine Triangles of Elemental Lore")
#     render_view_selector()
