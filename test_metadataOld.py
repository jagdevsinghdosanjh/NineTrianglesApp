import json
import os

def test_metadata_structure():
    path = os.path.join("data", "lore.json")
    assert os.path.exists(path), "lore.json not found."

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    triangles = data.get("triangles", [])
    assert isinstance(triangles, list), "'triangles' should be a list."

    required_keys = {"id", "name", "symbol", "element", "lore"}
    for t in triangles:
        assert required_keys.issubset(t.keys()), f"Missing keys in triangle {t.get('id')}"
        assert isinstance(t["id"], int), "ID must be integer."
        assert isinstance(t["rotation"], int), "Rotation must be integer."

    print("✅ Metadata validation passed.")

if __name__ == "__main__":
    test_metadata_structure()
