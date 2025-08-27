import streamlit as st
from metadata import load_triangle_meta

def test_metadata_structure():
    triangles = load_triangle_meta()
    required_keys = {"id", "name", "symbol", "element", "lore", "rotation"}
    errors = []

    for t in triangles:
        missing = required_keys - t.keys()
        if missing:
            errors.append(f"Triangle {t.get('id')} is missing: {missing}")
        elif not isinstance(t["rotation"], int):
            errors.append(f"Triangle {t.get('id')} has invalid rotation.")

            # errors.append(f"Triangle {t.get('id")} has invalid rotation.")

    if errors:
        for e in errors:
            st.error(e)
    else:
        st.success("✅ Metadata validation passed.")

if __name__ == "__main__":
    test_metadata_structure()

# from metadata import load_triangle_meta

# def test_metadata_structure():
#     triangles = load_triangle_meta()

#     assert isinstance(triangles, list), "'triangles' should be a list."

#     required_keys = {"id", "name", "symbol", "element", "lore", "rotation"}
#     for t in triangles:
#         missing = required_keys - t.keys()
#         assert not missing, f"Missing keys in triangle {t.get('id')}: {missing}"
#         assert isinstance(t["id"], int), "'id' must be an integer."
#         assert isinstance(t["rotation"], int), "'rotation' must be an integer."

#     print("✅ Metadata validation passed.")

# if __name__ == "__main__":
#     test_metadata_structure()
