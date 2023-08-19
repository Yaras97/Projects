n = input()
if n.count(".com", -4) >= 1 or n.count(".ru", -3) >= 1:
    print("YES")
else:
    print("NO")