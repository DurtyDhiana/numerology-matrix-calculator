import matplotlib.pyplot as plt

# Input for Jolie Andonian
birth = "30.03.1997"
parts = birth.split('.')
day = int(parts[0])
month = int(parts[1])
year = int(parts[2])

def reduce_to_22(n):
    """
    Reduces a number to a value ≤ 22 by repeatedly summing its digits.
    """
    while n > 22:
        n = sum(int(d) for d in str(n))
    return n

# Calculate core numbers
day_num = reduce_to_22(day)
month_num = reduce_to_22(month)
year_num = reduce_to_22(sum(int(d) for d in str(year)))
karmic_num = reduce_to_22(day_num + month_num + year_num)
comfort_num = reduce_to_22(day_num + month_num + year_num + karmic_num)

matrix_values = {
    "Top": month_num,
    "Right": year_num,
    "Bottom": karmic_num,
    "Left": day_num,
    "Center": comfort_num
}

corners = [
    reduce_to_22(matrix_values["Top"] + matrix_values["Right"]),
    reduce_to_22(matrix_values["Right"] + matrix_values["Bottom"]),
    reduce_to_22(matrix_values["Bottom"] + matrix_values["Left"]),
    reduce_to_22(matrix_values["Left"] + matrix_values["Top"])
]

# Visualization
colors = {
    "Top": "skyblue",
    "Right": "lightpink",
    "Bottom": "mediumaquamarine",
    "Left": "plum",
    "Center": "gold",
    "Corners": "lavender"
}

outer_x = [0, 1, 0, -1, 0]
outer_y = [1, 0, -1, 0, 1]
inner_x = [0.7, 0.7, -0.7, -0.7, 0.7]
inner_y = [0.7, -0.7, -0.7, 0.7, 0.7]

positions = {
    "Top": (0, 1),
    "Right": (1, 0),
    "Bottom": (0, -1),
    "Left": (-1, 0),
    "Center": (0, 0)
}
corner_positions = [(0.7, 0.7), (0.7, -0.7), (-0.7, -0.7), (-0.7, 0.7)]

plt.figure(figsize=(6, 6))
plt.plot(outer_x, outer_y, color="black", lw=1)
plt.plot(inner_x, inner_y, color="black", lw=0.75)

# Main circles
for key, (x, y) in positions.items():
    plt.plot(x, y, 'o', markersize=30, color=colors[key])
    plt.text(x, y, str(matrix_values[key]), ha='center', va='center',
             fontsize=12, fontweight='bold', color='black')

# Corner circles
for i, (x, y) in enumerate(corner_positions):
    plt.plot(x, y, 'o', markersize=25, color=colors["Corners"])
    plt.text(x, y, str(corners[i]), ha='center', va='center',
             fontsize=11, fontweight='bold', color='black')

plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
plt.gca().set_aspect('equal')
plt.xticks([]); plt.yticks([])
plt.gca().set_frame_on(False)
plt.title(f"Matrix of Destiny — Jolie Andonian\n{birth}", fontsize=14, pad=20)
plt.tight_layout()

# Save the figure
filename = f"Matrix_of_Destiny_{birth.replace('.', '-')}.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
print(f"\n✓ Matrix visualization saved as: {filename}")

# Arcana Interpretation
arcana_file = "data/matrix_interpretation.txt"

arcana_data = {}
with open(arcana_file, encoding='latin-1') as f:
    lines = f.readlines()
    for line in lines[1:]:
        parts = line.split('\t')
        num = int(parts[0])
        arcana_data[num] = {
            "name": parts[1],
            "general": parts[2],
            "center": parts[3],
            "birth_card": parts[4]
        }

center_num = matrix_values["Center"]
birth_card_num = matrix_values["Left"]

print("\n" + "="*60)
print("MATRIX OF DESTINY — JOLIE ANDONIAN")
print(f"Birth Date: 03/30/1997")
print("="*60)

print("\n=== CORE NUMBERS ===")
print(f"Day Number (Portrait/Left): {day_num}")
print(f"Month Number (Hidden Talents/Top): {month_num}")
print(f"Year Number (Material Karma/Right): {year_num}")
print(f"Karmic Number (Spiritual Karma/Bottom): {karmic_num}")
print(f"Comfort Number (Core Energy/Center): {comfort_num}")

print("\n=== ARCANA INTERPRETATION ===\n")
print(f"CENTER ({center_num} - {arcana_data[center_num]['name']})")
print(f"   {arcana_data[center_num]['center']}")

print(f"\nPORTRAIT/LEFT ({birth_card_num} - {arcana_data[birth_card_num]['name']})")
print(f"   {arcana_data[birth_card_num]['birth_card']}")

print("\n=== OTHER MAIN ARCANAS ===")
print(f"\nTOP — Hidden Talents ({matrix_values['Top']} - {arcana_data[matrix_values['Top']]['name']})")
print(f"   {arcana_data[matrix_values['Top']]['general']}")

print(f"\nRIGHT — Material Karma ({matrix_values['Right']} - {arcana_data[matrix_values['Right']]['name']})")
print(f"   {arcana_data[matrix_values['Right']]['general']}")

print(f"\nBOTTOM — Spiritual Karma ({matrix_values['Bottom']} - {arcana_data[matrix_values['Bottom']]['name']})")
print(f"   {arcana_data[matrix_values['Bottom']]['general']}")

print("\n=== ANCESTRAL PROGRAMS (Big Square Corners) ===")
corner_names = [
    "TOP LEFT (Father's Spiritual Lineage)",
    "TOP RIGHT (Mother's Spiritual Lineage)",
    "BOTTOM LEFT (Father's Material Lineage)",
    "BOTTOM RIGHT (Mother's Material Lineage)"
]

for i in range(len(corners)):
    num = corners[i]
    print(f"\n{corner_names[i]} ({num} - {arcana_data[num]['name']})")
    print(f"   {arcana_data[num]['general']}")

print("\n" + "="*60)
