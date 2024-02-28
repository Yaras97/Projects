letters = {'a': 'A', 'b': 'B', 'c': 'C'}
result = None
try:
    result = letters['B']
except:
    print('Произошла ошибка')
else:
    print('Ошибок не произошло')
finally:
    print('Завершение программы')
print(result)