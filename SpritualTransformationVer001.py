import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Set style for aesthetics
sns.set_style("whitegrid")
plt.rcParams.update({'font.size': 12, 'font.family': 'serif'})

# Create output directory if it doesn't exist
output_dir = "/data"
os.makedirs(output_dir, exist_ok=True)

# Define stages of spiritual transformation
stages = ["Fear of Death", "Seeking Guidance", "Inner Awakening", "Divine Connection", "Ultimate Bliss"]
progress = [1, 2, 3, 4, 5]
colors = sns.color_palette("plasma", len(stages))

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plot gradient path
for i in range(len(progress)-1):
    ax.plot([progress[i], progress[i+1]], [i, i+1], color=colors[i], linewidth=4)

# Add symbolic badges at each stage
symbols = ["☠", "🔍", "💡", "🔱", "🕉"]
for i, (stage, symbol) in enumerate(zip(stages, symbols)):
    ax.text(progress[i], i, f"{symbol}\n{stage}", fontsize=14, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

# Add mantra-triggered unlock sequence
mantras = ["Waheguru", "Satnam", "Ik Onkar", "Nirankar", "Anand"]
for i, mantra in enumerate(mantras):
    ax.text(progress[i], i-0.5, f"Unlock: {mantra}", fontsize=10, ha='center', va='center', color='gray')

# Final touches
ax.set_xlim(0.5, 5.5)
ax.set_ylim(-1, len(stages))
ax.axis('off')
plt.title("Spiritual Transformation in Gurbani", fontsize=16, weight='bold')

# Save the visualization
output_path = os.path.join(output_dir, "gurbani_spiritual_transformation_interface.png")
plt.savefig(output_path, bbox_inches='tight')
plt.close()

print("Spiritual transformation interface saved as 'gurbani_spiritual_transformation_interface.png'")
