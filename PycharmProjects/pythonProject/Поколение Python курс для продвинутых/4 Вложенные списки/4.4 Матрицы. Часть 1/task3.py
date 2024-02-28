n = int(input())
mtx = []

# Создаем матрицу
for i in range(n):
    mtx.append(input().split())

# Считаем сумму чисел гавной диагонали (след матрицы)
sled = 0
for i in range(n):
    sled += int(mtx[i][i])

print(sled)