def pascal(num):
    triangle = []
    s = []
    for i in range(num + 1):
        triangle.append([1] + [0] * num)

    for i in range(1, num + 1):
        for j in range(1, i + 1):
            triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]

    for i in range(num, num + 1):
        for j in range(0, i + 1):
            s.append(triangle[i][j])
    return s


n = int(input())
print(pascal(n))