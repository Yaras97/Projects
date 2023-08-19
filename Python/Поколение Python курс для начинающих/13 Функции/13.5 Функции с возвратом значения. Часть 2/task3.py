# объявление функции
def is_prime(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2


def get_next_prime(num):
    x = num + 1
    while is_prime(x) == False:
        x += 1
    return x

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))