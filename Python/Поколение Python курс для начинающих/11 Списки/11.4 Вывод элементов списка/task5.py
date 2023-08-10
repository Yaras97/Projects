lst = [input() for j in range(int(input()))]
search = input().lower()
for i in lst:
    if search in i.lower():
        print(i)