n = int(input())
centr = n // 2 + 1  # находим середину
count = 0  # кол-во звезд в строке
for i in range(1, n + 1):
    if i > centr:
        count -= 1  # если перешли за середину то убавляем кол-во звезд
    else:
        count += 1  # иначе прибавляем кол-во звезд

    for j in range(count):  # выполняем цикл сколько нужно звезд
        print('*', end='')
    print()