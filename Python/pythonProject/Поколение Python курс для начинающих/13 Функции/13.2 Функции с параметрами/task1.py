def draw_triangle(fill, base):
    # for i in range(1, base + 1):
    for j in range(1, base // 2 + 2):
        print(fill * j)
    for k in range(base // 2, 0, -1):
        print(fill * k)


fill = input()
base = int(input())


draw_triangle(fill, base)