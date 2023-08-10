m, n = int(input()), int(input())
lst1 = set(input() for _ in range(m))
lst2 = set(input() for _ in range(n))
print(len(lst1.difference(lst2)))




