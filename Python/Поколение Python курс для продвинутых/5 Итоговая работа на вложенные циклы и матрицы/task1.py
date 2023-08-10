n = input().split()
matrix = [["." for i in range(int(n[1]))] for j in range(int(n[0]))]
for i in range(int(n[0])):
    for j in range(int(n[1])):
        if i % 2 == 1 and j % 2 == 0:
            matrix[i][j] = "*"
        if i % 2 == 0 and j % 2 == 1:
            matrix[i][j] = "*"
for i in matrix:
    print(*i)