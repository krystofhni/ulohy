import sys

def read_regals():
    regals = {}
    while True:
        line = input().strip()
        if not line:
            break
        regal_number, *items = line.split()
        regals[int(regal_number)] = items
    return regals

def find_item(regals, item):
    for regal_number, items in regals.items():
        for regal_item in items:
            if item.lower() in regal_item.lower():
                return regal_number, regal_item
    return None, None

def optimize_shopping_list(regals, shopping_list):
    sorted_shopping_list = sorted(shopping_list, key=lambda item: item[0].lower())
    optimized_list = []
    for item, _ in sorted_shopping_list:
        regal_number, regal_item = find_item(regals, item)
        if regal_number is not None:
            optimized_list.append((regal_number, regal_item))
        else:
            print(f"Zboží '{item}' nenalezeno v žádném regálu.")
    return optimized_list

def main():
    regals = read_regals()
    for line in sys.stdin:
        shopping_list = []
        while line.strip():
            item, *rest = line.split()
            shopping_list.append((item, ' '.join(rest)))
            line = input().strip()
        optimized_list = optimize_shopping_list(regals, shopping_list)
        for regal_number, item in optimized_list:
            print(f"Regál {regal_number}: {item}")

if __name__ == "__main__":
    main()