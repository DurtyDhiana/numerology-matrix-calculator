"""
Comprehensive Destiny Matrix Calculator
Based on samwega's Destiny-Matrix-Calculator
Jolie Andonian: 03/30/1997
"""

def reduce_to_22(num):
    """Reduces a number to <= 22 by summing its digits repeatedly"""
    n = abs(int(num))
    if n == 0:
        return 22
    while n > 22:
        n = sum(int(d) for d in str(n))
    return n if n != 0 else 22

def sum_digits(num):
    """Sum all digits of a number"""
    return sum(int(d) for d in str(num))

def calculate_side_points(p1_val, p2_val, prefix, points):
    """Calculate intermediate points between two main points"""
    mid_val = reduce_to_22(p1_val + p2_val)
    q1_val = reduce_to_22(p1_val + mid_val)
    q2_val = reduce_to_22(mid_val + p2_val)
    e1_val = reduce_to_22(p1_val + q1_val)
    e2_val = reduce_to_22(q1_val + mid_val)
    e3_val = reduce_to_22(mid_val + q2_val)
    e4_val = reduce_to_22(q2_val + p2_val)

    points[f'{prefix}point'] = mid_val
    points[f'{prefix}1point'] = q1_val
    points[f'{prefix}4point'] = q2_val
    points[f'{prefix}2point'] = e1_val
    points[f'{prefix}3point'] = e2_val
    points[f'{prefix}5point'] = e3_val
    points[f'{prefix}6point'] = e4_val

def calculate_matrix(day, month, year):
    """Main calculation function for Destiny Matrix"""
    points = {}

    # Validate input
    if not all([day, month, year]) or year < 1 or day < 1 or day > 31 or month < 1 or month > 12:
        raise ValueError("Invalid date input")

    # Convert to numbers
    day = int(day)
    month = int(month)
    year = int(year)

    # Calculate year sum
    year_sum = sum_digits(year)

    # Main points (A, B, C, D, E)
    points['apoint'] = reduce_to_22(day)
    points['bpoint'] = reduce_to_22(month)
    points['cpoint'] = reduce_to_22(year_sum)
    points['dpoint'] = reduce_to_22(points['apoint'] + points['bpoint'] + points['cpoint'])
    points['epoint'] = reduce_to_22(points['apoint'] + points['bpoint'] + points['cpoint'] + points['dpoint'])

    # Square corners (F, G, H, I)
    points['fpoint'] = reduce_to_22(points['apoint'] + points['bpoint'])
    points['gpoint'] = reduce_to_22(points['bpoint'] + points['cpoint'])
    points['hpoint'] = reduce_to_22(points['apoint'] + points['dpoint'])
    points['ipoint'] = reduce_to_22(points['cpoint'] + points['dpoint'])

    # Additional core points
    points['jpoint'] = reduce_to_22(points['dpoint'] + points['epoint'])
    points['npoint'] = reduce_to_22(points['cpoint'] + points['epoint'])
    points['spoint'] = reduce_to_22(points['epoint'] + points['apoint'])
    points['tpoint'] = reduce_to_22(points['bpoint'] + points['epoint'])

    # More derived points
    points['lpoint'] = reduce_to_22(points['jpoint'] + points['npoint'])
    points['kpoint'] = reduce_to_22(points['jpoint'] + points['lpoint'])
    points['mpoint'] = reduce_to_22(points['lpoint'] + points['npoint'])
    points['opoint'] = reduce_to_22(points['apoint'] + points['spoint'])
    points['ppoint'] = reduce_to_22(points['bpoint'] + points['tpoint'])
    points['qpoint'] = reduce_to_22(points['cpoint'] + points['npoint'])
    points['rpoint'] = reduce_to_22(points['dpoint'] + points['jpoint'])

    # Union and special points
    points['upoint'] = reduce_to_22(points['fpoint'] + points['gpoint'] + points['ipoint'] + points['hpoint'])
    points['vpoint'] = reduce_to_22(points['epoint'] + points['upoint'])
    points['wpoint'] = reduce_to_22(points['epoint'] + points['spoint'])
    points['xpoint'] = reduce_to_22(points['epoint'] + points['tpoint'])

    # F, G, H, I extended points
    points['f2point'] = reduce_to_22(points['upoint'] + points['fpoint'])
    points['f1point'] = reduce_to_22(points['fpoint'] + points['f2point'])
    points['g2point'] = reduce_to_22(points['upoint'] + points['gpoint'])
    points['g1point'] = reduce_to_22(points['gpoint'] + points['g2point'])
    points['h2point'] = reduce_to_22(points['upoint'] + points['hpoint'])
    points['h1point'] = reduce_to_22(points['hpoint'] + points['h2point'])
    points['i2point'] = reduce_to_22(points['upoint'] + points['ipoint'])
    points['i1point'] = reduce_to_22(points['ipoint'] + points['i2point'])

    # Calculate side points
    calculate_side_points(points['apoint'], points['fpoint'], 'af', points)
    calculate_side_points(points['fpoint'], points['bpoint'], 'fb', points)
    calculate_side_points(points['bpoint'], points['gpoint'], 'bg', points)
    calculate_side_points(points['gpoint'], points['cpoint'], 'gc', points)
    calculate_side_points(points['cpoint'], points['ipoint'], 'ci', points)
    calculate_side_points(points['ipoint'], points['dpoint'], 'id', points)
    calculate_side_points(points['dpoint'], points['hpoint'], 'dh', points)
    calculate_side_points(points['hpoint'], points['apoint'], 'ha', points)

    # Sky, Earth, Male, Female, Purpose
    points['sky'] = reduce_to_22(points['bpoint'] + points['dpoint'])
    points['earth'] = reduce_to_22(points['apoint'] + points['cpoint'])
    points['male'] = reduce_to_22(points['fpoint'] + points['ipoint'])
    points['female'] = reduce_to_22(points['gpoint'] + points['hpoint'])
    points['purpose'] = reduce_to_22(points['sky'] + points['earth'])
    points['social'] = reduce_to_22(points['male'] + points['female'])
    points['generalpurpose'] = reduce_to_22(points['purpose'] + points['social'])

    # Chakras calculations
    # Crown
    points['crownPhysics'] = points['apoint']
    points['crownEnergy'] = points['bpoint']
    points['crownEmotions'] = reduce_to_22(points['crownPhysics'] + points['crownEnergy'])

    # Third Eye
    points['thirdeyePhysics'] = points['opoint']
    points['thirdeyeEnergy'] = points['ppoint']
    points['thirdeyeEmotions'] = reduce_to_22(points['thirdeyePhysics'] + points['thirdeyeEnergy'])

    # Throat
    points['throatPhysics'] = points['spoint']
    points['throatEnergy'] = points['tpoint']
    points['throatEmotions'] = reduce_to_22(points['throatPhysics'] + points['throatEnergy'])

    # Heart
    points['heartPhysics'] = points['wpoint']
    points['heartEnergy'] = points['xpoint']
    points['heartEmotions'] = reduce_to_22(points['heartPhysics'] + points['heartEnergy'])

    # Solar Plexus
    points['solarplexusPhysics'] = points['epoint']
    points['solarplexusEnergy'] = points['epoint']
    points['solarplexusEmotions'] = reduce_to_22(points['solarplexusPhysics'] + points['solarplexusEnergy'])

    # Sacral
    points['sacralPhysics'] = points['npoint']
    points['sacralEnergy'] = points['jpoint']
    points['sacralEmotions'] = reduce_to_22(points['sacralPhysics'] + points['sacralEnergy'])

    # Root
    points['rootPhysics'] = points['cpoint']
    points['rootEnergy'] = points['dpoint']
    points['rootEmotions'] = reduce_to_22(points['rootPhysics'] + points['rootEnergy'])

    return points

def print_results(points, name, birthdate):
    """Print comprehensive results"""
    print("=" * 70)
    print(f"COMPREHENSIVE DESTINY MATRIX — {name.upper()}")
    print(f"Birth Date: {birthdate}")
    print("=" * 70)

    print("\n=== CORE POINTS (Diamond) ===")
    print(f"A (Left/Portrait - Day): {points['apoint']}")
    print(f"B (Top/Hidden Talents - Month): {points['bpoint']}")
    print(f"C (Right/Material Karma - Year): {points['cpoint']}")
    print(f"D (Bottom/Spiritual Karma): {points['dpoint']}")
    print(f"E (Center/Core Energy - Comfort): {points['epoint']}")

    print("\n=== SQUARE CORNERS (Ancestral Programs) ===")
    print(f"F (Top Left - Father's Spiritual): {points['fpoint']}")
    print(f"G (Top Right - Mother's Spiritual): {points['gpoint']}")
    print(f"H (Bottom Left - Father's Material): {points['hpoint']}")
    print(f"I (Bottom Right - Mother's Material): {points['ipoint']}")

    print("\n=== EXTENDED POINTS ===")
    print(f"J Point: {points['jpoint']}")
    print(f"K Point: {points['kpoint']}")
    print(f"L Point: {points['lpoint']}")
    print(f"M Point: {points['mpoint']}")
    print(f"N Point: {points['npoint']}")
    print(f"O Point: {points['opoint']}")
    print(f"P Point: {points['ppoint']}")
    print(f"Q Point: {points['qpoint']}")
    print(f"R Point: {points['rpoint']}")
    print(f"S Point: {points['spoint']}")
    print(f"T Point: {points['tpoint']}")
    print(f"U Point (Union): {points['upoint']}")
    print(f"V Point: {points['vpoint']}")
    print(f"W Point: {points['wpoint']}")
    print(f"X Point: {points['xpoint']}")

    print("\n=== PURPOSE & DESTINY ===")
    print(f"Sky (Heaven): {points['sky']}")
    print(f"Earth: {points['earth']}")
    print(f"Male Energy: {points['male']}")
    print(f"Female Energy: {points['female']}")
    print(f"Life Purpose: {points['purpose']}")
    print(f"Social Purpose: {points['social']}")
    print(f"General Purpose: {points['generalpurpose']}")

    print("\n=== CHAKRAS (Physics | Energy | Emotions) ===")
    print(f"Crown Chakra: {points['crownPhysics']} | {points['crownEnergy']} | {points['crownEmotions']}")
    print(f"Third Eye Chakra: {points['thirdeyePhysics']} | {points['thirdeyeEnergy']} | {points['thirdeyeEmotions']}")
    print(f"Throat Chakra: {points['throatPhysics']} | {points['throatEnergy']} | {points['throatEmotions']}")
    print(f"Heart Chakra: {points['heartPhysics']} | {points['heartEnergy']} | {points['heartEmotions']}")
    print(f"Solar Plexus: {points['solarplexusPhysics']} | {points['solarplexusEnergy']} | {points['solarplexusEmotions']}")
    print(f"Sacral Chakra: {points['sacralPhysics']} | {points['sacralEnergy']} | {points['sacralEmotions']}")
    print(f"Root Chakra: {points['rootPhysics']} | {points['rootEnergy']} | {points['rootEmotions']}")

    print("\n=== EXTENDED ANCESTRAL LINEAGES ===")
    print(f"F Extended (Father Spiritual): F={points['fpoint']}, F1={points['f1point']}, F2={points['f2point']}")
    print(f"G Extended (Mother Spiritual): G={points['gpoint']}, G1={points['g1point']}, G2={points['g2point']}")
    print(f"H Extended (Father Material): H={points['hpoint']}, H1={points['h1point']}, H2={points['h2point']}")
    print(f"I Extended (Mother Material): I={points['ipoint']}, I1={points['i1point']}, I2={points['i2point']}")

    print("\n" + "=" * 70)
    print(f"Total points calculated: {len(points)}")
    print("=" * 70)

if __name__ == "__main__":
    # Jolie Andonian's information
    name = "Jolie Andonian"
    day = 30
    month = 3
    year = 1997
    birthdate = "03/30/1997"

    print("\n🔮 Running Comprehensive Destiny Matrix Calculator...")
    print("(Based on samwega's Destiny-Matrix-Calculator-and-Tools)\n")

    points = calculate_matrix(day, month, year)
    print_results(points, name, birthdate)
