import json
import os

def load_triangle_meta():
    path = "lore.json"
    try:
        if not os.path.exists(path):
            raise FileNotFoundError("lore.json not found.")

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            if not content.strip():
                raise ValueError("Empty JSON file.")
            meta = json.loads(content)

        # Ensure each triangle has a rotation angle
        for i, item in enumerate(meta):
            item["rotation"] = i * 40

        return meta

    except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
        print(f"⚠️ Failed to load lore.json: {e}. Falling back to default metadata.")
        return default_triangle_meta()

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
            "lore": lore,
            "rotation": i * 40
        }
        for i, (sym, elem, lore) in enumerate(symbols)
    ]
