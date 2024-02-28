n = input()
file = open(n)
print(file.readlines()[-2].rstrip())
file.close()




