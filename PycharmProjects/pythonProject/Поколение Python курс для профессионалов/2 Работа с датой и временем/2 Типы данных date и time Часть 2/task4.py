n = 'python'
try:
    n = int(n)
    print(n * 2)
except ValueError:
    print('Произошла ошибка')