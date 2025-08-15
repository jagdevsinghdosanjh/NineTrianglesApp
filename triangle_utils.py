import numpy as np

def isosceles_triangle(base=100, height=150, center=(200, 200), rotation=0):
    cx, cy = center
    points = np.array([
        [cx - base / 2, cy],
        [cx + base / 2, cy],
        [cx, cy - height]
    ])
    theta = np.radians(rotation)
    rot_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    rotated = np.dot(points - [cx, cy], rot_matrix) + [cx, cy]
    return rotated.tolist()

def svg_triangle(points, symbol, element, opacity=0.6):
    p_str = " ".join([f"{x},{y}" for x, y in points])
    css_class = f"triangle-{element.lower()}"
    return f'<polygon points="{p_str}" class="{css_class}" opacity="{opacity}" title="{symbol}" />'

def render_symbolic_card(meta):
    return f"""
    <div class="symbolic-card">
        <h3>{meta['symbol']} ({meta['element']})</h3>
        <p>{meta['lore']}</p>
    </div>
    """
