def distance(d1, d2, d3):
    return min(d1 + d3 + d2, d1 + d1 + d2 + d2, d2 + d3 + d3 + d2, d1 + d3 + d3 + d1)


a, b, c = [int(input()) for _ in range(3)]
print(distance(a, b, c))


# d1, d2, d3 = [int(input() for _ in range(3))]
# print(min(d1 + d3 + d2, d1 + d1 + d2 + d2, d2 + d3 + d3 + d2, d1 + d3 + d3 + d1))