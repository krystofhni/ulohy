import sys
import math

def parse_coordinates(input_str):
    try:
        x, y, name = input_str.strip().split(',')
        x = float(x)
        y = float(y)
        return x, y, name
    except ValueError:
        return None

def calculate_distance(coord1, coord2):
    x1, y1, _ = coord1
    x2, y2, _ = coord2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    # Načítání souřadnic letadel
    coordinates = []
    try:
        while True:
            input_str = input()
            coord = parse_coordinates(input_str)
            if coord:
                coordinates.append(coord)
            else:
                print("Nespravny vstup: neplatne souradnice.")
                return
    except EOFError:
        pass

    # Kontrola počtu letadel
    if len(coordinates) < 2:
        print("Nespravny vstup: mene nez dve letadla.")
        return

    # Výpočet nejkratší vzdálenosti mezi letadly
    min_distance = float('inf')
    closest_pairs = []
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            distance = calculate_distance(coordinates[i], coordinates[j])
            if distance < min_distance:
                min_distance = distance
                closest_pairs = [(coordinates[i][2], coordinates[j][2])]
            elif distance == min_distance:
                closest_pairs.append((coordinates[i][2], coordinates[j][2]))

    # Výstup
    print("Nejmensi vzdalenost:", min_distance)
    print("Pocet dvojic s nejmensi vzdalenosti:", len(closest_pairs))
    for pair in closest_pairs:
        print(*pair)

if __name__ == "__main__":
    main()