n = int(input())
k = int(input())
skip = 0
for i in range(1, n + 1):

    skip = (skip + k) % i
    # print("Шаг: ", skip)


print(skip + 1)