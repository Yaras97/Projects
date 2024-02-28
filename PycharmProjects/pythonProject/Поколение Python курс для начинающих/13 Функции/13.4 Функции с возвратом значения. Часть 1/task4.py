# объявление функции
def number_of_factors(num):
    return len([i for i in range(1, n + 1) if n % i == 0])

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))