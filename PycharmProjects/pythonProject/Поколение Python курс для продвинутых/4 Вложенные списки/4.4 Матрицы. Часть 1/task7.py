n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
ma = [[], [], [], []]
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:  # Верхний треугольник
            ma[0].append(matrix[i][j])
        if i < j and i > n - 1 - j:  # Правый треугольник
            ma[1].append(matrix[i][j])
        if i > j and i > n - 1 - j:  # Нижний треугольник
            ma[2].append(matrix[i][j])
        if i > j and i < n - 1 - j:  # Левый треугольник
            ma[3].append(matrix[i][j])

print("Верхняя четверть:", sum(ma[0]))
print("Правая четверть:", sum(ma[1]))
print("Нижняя четверть:", sum(ma[2]))
print("Левая четверть:", sum(ma[3]))