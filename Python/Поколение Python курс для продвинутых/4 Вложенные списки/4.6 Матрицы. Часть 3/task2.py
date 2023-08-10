n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
lst = []
for i in range(n):
    for j in range(n):
        if i + j + 1 >= n:
            lst.append(matrix[i][j])
print(max(lst))