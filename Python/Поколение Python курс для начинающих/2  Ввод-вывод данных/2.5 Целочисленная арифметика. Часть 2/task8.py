a1 = int(input())
c = a1 % 10
b = (a1 % 100) // 10
a = a1 // 100
print(str(a) + str(b) + str(c), sep='')
print(str(a) + str(c) + str(b), sep='')
print(str(b) + str(a) + str(c), sep='')
print(str(b) + str(c) + str(a), sep='')
print(str(c) + str(a) + str(b), sep='')
print(str(c) + str(b) + str(a), sep='')