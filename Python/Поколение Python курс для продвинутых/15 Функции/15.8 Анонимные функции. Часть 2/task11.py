n = [int(i) for i in input().split()]
func = list(map(lambda x: 255 - x, n))
print(*func)


