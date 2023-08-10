# put your python code here
a, b, c = int(input()), int(input()), input()
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(a / b)
else:
    print('Неверная операция')