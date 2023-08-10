n = int(input())
mtx = []
# Создаем матрицу
for i in range(n):
    mtx.append(input().split())

# Перебираем числа матрицы
for i in range(n):
    schet = 0                      # Счетчик вывода чисел больше ср. ар.
    cnt = 0                        # Счетчик количества чисел в строке
    for j in range(n):             # Считаем сумму чисел строки
        cnt += int(mtx[i][j])
    sr = cnt / n                   # Среднее арифмитическое чисел строки
    for j in range(n):             # Подсчет чисел больших ср. ар.
        if int(mtx[i][j]) > sr:
            schet += 1
    print(schet)