'''
m, n = int(input()), int(input())
if m % 2 == 1:
    for i in range(m, n - 1, -2):
        print(i)
elif m % 2 == 0:
    for i in range(m - 1, n - 1, -2):
        print(i)
'''
m, n = int(input()), int(input())
for i in range(m, n, -2):
    print(i + m % 2 - 1)  # m % 2 проверяет четное число или нет, если нечетное то 1 - 1 = 0, если четное, то 0 и смещение старта на -1, так как убывающая прогрессия.
