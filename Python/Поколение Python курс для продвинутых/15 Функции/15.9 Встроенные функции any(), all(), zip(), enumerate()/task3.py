pos = list(zip(input().split(), input().split(), input().split()))
func = all(map(lambda x: float(x[0])**2 + float(x[1])**2 + float(x[2])**2 <= 4, pos))
print(func)




