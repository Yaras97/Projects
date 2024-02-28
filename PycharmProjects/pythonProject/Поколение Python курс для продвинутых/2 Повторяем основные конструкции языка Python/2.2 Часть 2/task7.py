tim = input()
rus = input()
k = 'камень'
n = 'ножницы'
b = 'бумага'
if tim == rus:
    print('ничья')
if tim == k and rus == n:
    print('Тимур')
if tim == k and rus == b:
    print('Руслан')
if tim == n and rus == k:
    print('Руслан')
if tim == n and rus == b:
    print('Тимур')
if tim == b and rus == k:
    print('Тимур')
if tim == b and rus == n:
    print('Руслан')