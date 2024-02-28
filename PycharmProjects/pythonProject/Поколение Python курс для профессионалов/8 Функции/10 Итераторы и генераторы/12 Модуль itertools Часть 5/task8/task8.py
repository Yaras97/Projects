from itertools import product

def generate_numbers(base, length):

    # Генерация чисел в системе счисления
    digits = [str(i) if i < 10 else chr(ord('A') + i - 10) for i in range(base)]
    numbers = [''.join(combination) for combination in product(digits, repeat=length)]

    return numbers

# Ввод данных
base = 16
length = 2

# Генерация чисел и вывод результата
result = generate_numbers(base, length)
print(" ".join(result))