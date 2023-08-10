# объявление функции
def is_prime(num):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    if len(lst) == 2:
        return True
    else:
        return False

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))