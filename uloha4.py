def find_interval_sums(numbers):
    # Pomocná funkce pro výpočet součtu intervalu
    def interval_sum(nums, start, end):
        return sum(nums[start:end+1])

    # Seznam pro ukládání součtů intervalů
    sums = []

    # Výpočet součtů pro všechny možné intervaly délky alespoň 2
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            sums.append(interval_sum(numbers, i, j))

    return sums

def count_same_sum_pairs(numbers):
    # Získání všech součtů intervalů
    sums = find_interval_sums(numbers)

    # Seznam pro ukládání počtu součtů
    sum_counts = {}

    # Počítání počtu výskytů jednotlivých součtů
    for sum_ in sums:
        if sum_ in sum_counts:
            sum_counts[sum_] += 1
        else:
            sum_counts[sum_] = 1

    # Počítání dvojic s stejným součtem
    pairs_count = 0
    for count in sum_counts.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2

    return pairs_count

def main():
    numbers = []
    
    # Načítání číselné posloupnosti
    try:
        while True:
            number = int(input())
            numbers.append(number)
    except EOFError:
        pass
    
    # Kontrola délky posloupnosti
    if len(numbers) == 0:
        print("Nespravny vstup: prazdna posloupnost.")
        return
    elif len(numbers) > 2000:
        print("Nespravny vstup: posloupnost je prilis dlouha.")
        return

    # Výpočet počtu dvojic s stejným součtem
    pairs_count = count_same_sum_pairs(numbers)
    print("Pocet dvojic intervalu se stejnym souctem:", pairs_count)

if __name__ == "__main__":
    main()