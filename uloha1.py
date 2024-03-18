import math

def calculate_pipe_length(cube_size, point1, point2=None):
    # Kontrola nesmyslného zadání rozměrů místnosti
    if cube_size <= 0:
        print("Nespravny vstup.")
        return

    # Kontrola nesmyslného zadání bodů
    for point in [point1, point2]:
        if point is not None:
            if len(point) != 3 or not all(isinstance(coord, int) for coord in point):
                print("Nespravny vstup.")
                return
            
            # Kontrola, zda bod leží na stěně místnosti
            if not (0 <= point[0] <= cube_size or 0 <= point[1] <= cube_size or 0 <= point[2] <= cube_size):
                print("Nespravny vstup.")
                return
            
            # Kontrola, zda bod není příliš blízko rohu
            if any(coord < 20 for coord in point):
                print("Nespravny vstup.")
                return

    # Výpočet délky potrubí
    if point2 is not None:
        pipe_length = sum(abs(point1[i] - point2[i]) for i in range(3))
        print(f"Delka potrubi: {pipe_length}")

    # Výpočet délky hadice
    if point2 is not None:
        min_coord = [min(point1[i], point2[i]) for i in range(3)]
        max_coord = [max(point1[i], point2[i]) for i in range(3)]
        hose_length = math.sqrt(sum((max_coord[i] - min_coord[i]) ** 2 for i in range(3)))
        print(f"Delka hadice: {hose_length}")

# Ukázkové vstupy
inputs = [
    (300, (100, 100, 0), (20, 0, 200)),
    (300, (100, 100, 0), (300, 100, 200)),
    (300, (130, 100, 0), (200, 280, 300)),
    (184, (21, 37, 0), (96, 55, 184)),
    (300, (100, 400, 0)),
    (300, (100, 100, 0), (10, 100, 300)),
    (300, (100, 100, 0), (50, 50, 'test'))
]

for i, inp in enumerate(inputs):
    print(f"Rozmer mistnosti:")
    print(inp[0])
    print(f"Bod #{i + 1}:")
    print(" ".join(map(str, inp[1])))
    if len(inp) > 2:
        print(f"Bod #{i + 2}:")
        print(" ".join(map(str, inp[2])))
    # Předání druhého bodu pouze v případě, že je k dispozici
    if len(inp) > 2:
        calculate_pipe_length(*inp)
    else:
        calculate_pipe_length(inp[0], inp[1])

    print()