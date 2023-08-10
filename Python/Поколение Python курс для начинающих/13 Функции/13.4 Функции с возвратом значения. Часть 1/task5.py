# объявление функции
def find_all(target, symbol):
    lst = list(target)
    lst2 = list()
    for i in range(len(lst)):
        if lst[i] == symbol:
            lst2.append(i)
    return lst2

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))