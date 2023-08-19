n = int(input())
dict1 = {}

for i in range(n):
    m = input().split()
    dict1[m[0]] = dict1.get(m[1], m[1])
    dict1[m[1]] = dict1.get(m[1], m[0])

print(dict1[input()])