n = int(input())
s = ''
for i in range(1, n + 1):
    s += chr(96 + i)
print(list(s))