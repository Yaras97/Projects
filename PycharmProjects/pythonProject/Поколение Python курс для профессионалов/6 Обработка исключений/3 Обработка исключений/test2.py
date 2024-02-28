letters = {'a': 'A', 'b': 'B', 'c': 'C'}
try:
    print(letters['b'])
except:
    print('Произошла ошибка')
else:
    print('Ошибок не произошло')
finally:
    print('Завершение программы')