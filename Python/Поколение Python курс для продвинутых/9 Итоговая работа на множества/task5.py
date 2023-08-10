n = int(input())
m = int(input())
st1 = [input() for _ in range(n)]
st2 = [input() for _ in range(m)]
for i in st2:
    if i in st1:
        print("YES")
    else:
        print("NO")