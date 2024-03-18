def are_collinear(x1, y1, x2, y2, x3, y3):
    # Kontrola, zda jsou všechny souřadnice čísla
    try:
        x1, y1, x2, y2, x3, y3 = float(x1), float(y1), float(x2), float(y2), float(x3), float(y3)
    except ValueError:
        print("Nespravny vstup.")
        return

    # Vypočet determinantu
    det = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    # Bodu jsou různé a neleží na jedné přímce
    if det != 0:
        print("Body nelezi na jedne prime.")
    else:
        # Kontrola, zda všechny body splývají
        if x1 == x2 == x3 and y1 == y2 == y3:
            print("Body splyvaji.")
        else:
            print("Body lezi na jedne prime.")

# Ukázkové vstupy
inputs = [
    (1, 2, 3, 4, 5, 6),
    (0.1, 0.2, 0.3, 0.4, 0.5, 0.6),
    (10, 10, 0, 10, 10, 0),
    (0, 1, 0, 3, 0, 2),
    ('a', 0, 1, 1, 2, 2),
    (0, 0, 1, 'b', 2, 2),
    (0, 0, 1, 1, 2, 'c')
]

for i, inp in enumerate(inputs):
    print(f"Test {i + 1}:")
    are_collinear(*inp)
    print()