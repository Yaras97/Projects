expression = input()
line = input().split()
min_v = int(line[0])
max_v = int(line[1])
result = []
for i in range(min_v, max_v + 1):
    x = i
    result.append(eval(expression))
print(f'Минимальное значение функции {expression} на отрезке [{min_v}; {max_v}] равно {min(result)}')
print(f'Максимальное значение функции {expression} на отрезке [{min_v}; {max_v}] равно {max(result)}')
