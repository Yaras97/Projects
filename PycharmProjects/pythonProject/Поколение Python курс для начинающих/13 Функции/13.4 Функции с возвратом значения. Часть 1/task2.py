# объявление функции
def get_days(month):

    if num == 1 or num == 3 or num == 5 or num == 7 or num == 8 or num == 10 or num == 12:
        return 31
    if num == 4 or num == 6 or num == 9 or num == 11:
        return 30
    if num == 2:
        return 28


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))