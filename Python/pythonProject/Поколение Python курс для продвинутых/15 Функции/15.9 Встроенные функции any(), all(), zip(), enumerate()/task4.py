n = input().split('.')
func = all(map(lambda x: True if x.isdigit() and int(x) <= 255 else False, n))
print(func)




