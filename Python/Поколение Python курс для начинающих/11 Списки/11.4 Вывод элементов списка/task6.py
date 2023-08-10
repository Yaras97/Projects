s = []
p = []
for _ in range(int(input())):
    s.append(input())

for _ in range(int(input())):
    p.append(input())

for i in s:
    n = 0
    for k in p:
        if k.lower() in i.lower():
            n += 1
    if n >= len(p):
        print(i)