def quick_merge(n):
    a = list()
    for i in range(n):
        a.extend(input().split())
    for i in range(len(a)):
        a[i] = int(a[i])
    a.sort()

    return a

num = int(input())

print(*quick_merge(num))