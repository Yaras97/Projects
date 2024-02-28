# объявление функции
def is_magic(date):
    tr = int(date[2][2:4])
    if int(date[0]) * int(date[1]) == tr:
        return True
    else:
        return False

# считываем данные
date = input().split(".")

# вызываем функцию
print(is_magic(date))