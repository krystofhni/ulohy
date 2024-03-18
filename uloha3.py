def next_palindrome(from_num, radix, next):
    # Kontrola platnosti číselné soustavy
    if not 2 <= radix <= 36:
        return 0

    # Hledání nejbližšího většího palindromu
    for i in range(from_num + 1, 2 ** 64):
        num_str = str(int(str(i), 10)) if radix == 10 else str(i)
        reversed_num_str = num_str[::-1]

        if num_str == reversed_num_str:
            *next, = map(int, num_str, (radix,) * len(num_str))
            return 1

    return 0

# Ukázkové použití
next_palindrome_num = 0
result = next_palindrome(10, 10, next_palindrome_num)
if result:
    print("Nejbližší větší palindrom od 10 v desítkové soustavě je:", next_palindrome_num)
else:
    print("Nelze najít palindrom v desítkové soustavě větší než 10.")