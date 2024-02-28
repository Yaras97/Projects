# Вам доступен список numbers, содержащий целые числа.
# Дополните приведенный ниже код с использованием функций iter() и next(),
# чтобы он вывел последний элемент данного списка.

numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64,
           -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]

iterator = iter(numbers)
for i in range(len(numbers)):
    if i + 1 == len(numbers):
        print(next(iterator))
    else:
        next(iterator)


# numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64,
#            -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]
#
# iterator = iter(numbers)
# last_element = None
#
# while True:
#     try:
#         last_element = next(iterator)
#     except StopIteration:
#         break
#
# print(last_element)