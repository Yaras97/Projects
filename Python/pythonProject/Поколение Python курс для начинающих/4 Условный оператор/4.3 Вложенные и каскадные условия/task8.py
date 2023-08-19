# put your python code here
a = int(input())
if a == 0:
    print('зеленый')
elif 1 <= a <= 10:
    if a % 2 == 1:
        print('красный')
    else:
        print('черный')
elif 11 <= a <= 18:
    if a % 2 == 1:
        print('черный')
    else:
        print('красный')
elif 19 <= a <= 28:
    if a % 2 == 1:
        print('красный')
    else:
        print('черный')
elif 29 <= a <= 36:
    if a % 2 == 1:
        print('черный')
    else:
        print('красный')
else:
    print('ошибка ввода')