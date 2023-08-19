n, m, k = set(input().split()), set(input().split()), set(input().split())
a = set()
for i in n:
    for j in m:
        if j not in k:
            if i not in k:
                if i in n:
                    if i in m:
                        if j in n:
                            if j in m:
                                a.add((int(i)))
print(*sorted(a, reverse=True))