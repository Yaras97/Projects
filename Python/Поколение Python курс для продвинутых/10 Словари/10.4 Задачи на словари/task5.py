d = {}
for _ in range(int(input())):
    m = input().split()
    for j in m[1:]:
        d[j] = m[0]

for _ in range(int(input())):
    print(d[input()])
