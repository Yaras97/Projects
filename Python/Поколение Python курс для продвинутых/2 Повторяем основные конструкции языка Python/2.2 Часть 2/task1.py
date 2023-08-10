n = int(input())
chet1, chet2, chet3, chet4 = 0, 0, 0, 0

for i in range(n):
    x, y = (int(i) for i in input().split())
    if x > 0 and y > 0:
        chet1 += 1
    if x < 0 and y > 0:
        chet2 += 1
    if x < 0 and y < 0:
        chet3 += 1
    if x > 0 and y < 0:
        chet4 += 1
print("Первая четверть:", chet1)
print("Вторая четверть:", chet2)
print("Третья четверть:", chet3)
print("Четвертая четверть:", chet4)