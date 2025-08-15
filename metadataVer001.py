import json

def load_triangle_meta(from_json=True):
    if from_json:
        try:
            with open("data/lore.json", "r") as f:
                meta = json.load(f)
        except FileNotFoundError:
            print("⚠️ lore.json not found. Falling back to default metadata.")
            meta = default_triangle_meta()
    else:
        meta = default_triangle_meta()

    for i, item in enumerate(meta):
        item["rotation"] = i * 40
    return meta

def default_triangle_meta():
    symbols = [
        ("Wisdom", "Air", "Clarity of thought and the breath of insight."),
        ("Courage", "Fire", "The spark that ignites transformation."),
        ("Harmony", "Water", "Flowing unity and emotional resonance."),
        ("Structure", "Earth", "Foundation, form, and sacred geometry."),
        ("Vision", "Aether", "The unseen pattern behind all things."),
        ("Balance", "Metal", "Precision, reflection, and inner alignment."),
        ("Flow", "Wood", "Growth, adaptability, and creative expansion."),
        ("Truth", "Light", "Illumination, revelation, and integrity."),
        ("Mystery", "Shadow", "The unknown, the hidden, the fertile void.")
    ]
    return [
        {
            "id": i,
            "symbol": sym,
            "element": elem,
            "lore": lore
        }
        for i, (sym, elem, lore) in enumerate(symbols)
    ]
