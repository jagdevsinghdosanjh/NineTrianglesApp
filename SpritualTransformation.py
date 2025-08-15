import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from matplotlib import font_manager

# Optional: Load a Unicode-friendly font if available
font_path = "Symbola.ttf"
font_prop = None

if os.path.exists(font_path):
    font_prop = font_manager.FontProperties(fname=font_path)
else:
    print("Symbola.ttf not found. Using default font.")

# Set style for aesthetics
sns.set_style("whitegrid")
plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})

# Create output directory
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Define stages of spiritual transformation
stages = [
    "Fear of Death",
    "Seeking Guidance",
    "Inner Awakening",
    "Divine Connection",
    "Ultimate Bliss"
]
progress = np.arange(1, len(stages) + 1)
colors = sns.color_palette("plasma", len(stages))

# Define symbolic glyphs and mantras
symbols = ["☠", "🔍", "💡", "🔱", "🕉"]
mantras = ["Waheguru", "Satnam", "Ik Onkar", "Nirankar", "Anand"]

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plot gradient path
for i in range(len(progress) - 1):
    ax.plot([progress[i], progress[i + 1]], [i, i + 1], color=colors[i], linewidth=4)

# Add symbolic badges and mantra unlocks
for i, (stage, symbol, mantra) in enumerate(zip(stages, symbols, mantras)):
    ax.text(
        progress[i], i,
        f"{symbol}\n{stage}",
        fontsize=14,
        ha='center',
        va='center',
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'),
        fontproperties=font_prop if font_prop else None
    )
    ax.text(
        progress[i], i - 0.5,
        f"Unlock: {mantra}",
        fontsize=10,
        ha='center',
        va='center',
        color='gray'
    )

# Final touches
ax.set_xlim(0.5, len(stages) + 0.5)
ax.set_ylim(-1, len(stages))
ax.axis('off')
plt.title("Spiritual Transformation in Gurbani", fontsize=16, weight='bold')

# Save visualization
output_path = os.path.join(output_dir, "gurbani_spiritual_transformation_interface.png")
plt.savefig(output_path, bbox_inches='tight')
plt.close()

print(f"Spiritual transformation interface saved as '{output_path}'")

# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# import os
# from matplotlib import font_manager

# # Optional: Load a Unicode-friendly font if available
# try:
#     font_path = "Symbola.ttf"  # Replace with actual path if installed
#     font_prop = font_manager.FontProperties(fname=font_path)
# except:
#     font_prop = None  # Fallback to default

# # Set style for aesthetics
# sns.set_style("whitegrid")
# plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})

# # Create output directory
# output_dir = "output"
# os.makedirs(output_dir, exist_ok=True)

# # Define stages and symbolic elements
# stages = ["Fear of Death", "Seeking Guidance", "Inner Awakening", "Divine Connection", "Ultimate Bliss"]
# progress = np.arange(1, len(stages) + 1)
# colors = sns.color_palette("plasma", len(stages))
# symbols = ["☠", "🔍", "💡", "🔱", "🕉"]
# mantras = ["Waheguru", "Satnam", "Ik Onkar", "Nirankar", "Anand"]

# # Create figure
# fig, ax = plt.subplots(figsize=(12, 6))

# # Plot transformation path
# for i in range(len(progress) - 1):
#     ax.plot([progress[i], progress[i + 1]], [i, i + 1], color=colors[i], linewidth=4)

# # Add symbolic badges and mantras
# for i, (stage, symbol, mantra) in enumerate(zip(stages, symbols, mantras)):
#     ax.text(progress[i], i, f"{symbol}\n{stage}", fontsize=14, ha='center', va='center',
#             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'),
#             fontproperties=font_prop)
#     ax.text(progress[i], i - 0.5, f"Unlock: {mantra}", fontsize=10, ha='center', va='center', color='gray')

# # Final touches
# ax.set_xlim(0.5, len(stages) + 0.5)
# ax.set_ylim(-1, len(stages))
# ax.axis('off')
# plt.title("Spiritual Transformation in Gurbani", fontsize=16, weight='bold')

# # Save visualization
# output_path = os.path.join(output_dir, "gurbani_spiritual_transformation_interface.png")
# plt.savefig(output_path, bbox_inches='tight')
# plt.close()

# print(f"Spiritual transformation interface saved as '{output_path}'")
