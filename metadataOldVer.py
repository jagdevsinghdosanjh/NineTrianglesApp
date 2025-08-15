import json

def load_triangle_meta():
    with open("data/lore.json", "r") as f:
        meta = json.load(f)
    for i, item in enumerate(meta):
        item["rotation"] = i * 40
    return meta

# TRIANGLE_META = [
#     {
#         "id": i,
#         "symbol": sym,
#         "element": elem,
#         "rotation": i * 40,
#         "lore": lore
#     }

    for i, (sym, elem, lore) in enumerate([
        ("Wisdom", "Air", "Clarity of thought and the breath of insight."),
        ("Courage", "Fire", "The spark that ignites transformation."),
        ("Harmony", "Water", "Flowing unity and emotional resonance."),
        ("Structure", "Earth", "Foundation, form, and sacred geometry."),
        ("Vision", "Aether", "The unseen pattern behind all things."),
        ("Balance", "Metal", "Precision, reflection, and inner alignment."),
        ("Flow", "Wood", "Growth, adaptability, and creative expansion."),
        ("Truth", "Light", "Illumination, revelation, and integrity."),
        ("Mystery", "Shadow", "The unknown, the hidden, the fertile void.")
    ])
]

# TRIANGLE_META = [
#     {"id": i, "symbol": sym, "element": elem, "rotation": i * 40}
#     for i, (sym, elem) in enumerate([
#         ("Wisdom", "Air"), ("Courage", "Fire"), ("Harmony", "Water"),
#         ("Structure", "Earth"), ("Vision", "Aether"), ("Balance", "Metal"),
#         ("Flow", "Wood"), ("Truth", "Light"), ("Mystery", "Shadow")
#     ])
# ]
