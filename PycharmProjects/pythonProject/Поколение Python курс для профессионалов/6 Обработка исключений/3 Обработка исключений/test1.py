numbers = list(filter(int, ['1', '2', '3', '4', '5']))
try:
    total = sum(numbers)
    print(total)
except:
    print('Произошла ошибка')
else:
    print('Ошибок не произошло')
finally:
    print('Завершение программы')