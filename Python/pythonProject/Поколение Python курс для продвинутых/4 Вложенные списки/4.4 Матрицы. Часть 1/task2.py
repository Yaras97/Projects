n, m = int(input()), int(input())
mtx = []

 # Создаем матрицу
for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    mtx.append(row)


# Выводим стандартную матрицу по строкам и столбцам
for i in range(n):
    for j in range(m):
        print(mtx[i][j], end=' ')
    print()

print()

# Выводим матрицу по размерам столбцов и строк
for i in range(m):
    for j in range(n):
        print(mtx[j][i], end=' ')
    print()