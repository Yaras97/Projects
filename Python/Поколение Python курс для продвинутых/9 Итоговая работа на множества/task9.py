m, n = int(input()), int(input())
lst1 = set(input() for _ in range(m))
lst2 = set(input() for _ in range(n))
if len(lst1 - lst2) != 0 or len(lst2 - lst1) != 0:
    if len(lst1 - lst2) > len(lst2 - lst1):
        print(len(lst1 ^ lst2))
    if len(lst2 - lst1) > len(lst1 - lst2):
        print(len(lst2 ^ lst1))
else:
    print("NO")