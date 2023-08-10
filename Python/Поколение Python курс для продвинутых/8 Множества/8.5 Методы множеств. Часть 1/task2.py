cnt = ''
n = [input().lower() for _ in range(int(input()))]
for i in n:
    cnt += i
print(len(set(cnt)))