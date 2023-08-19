# put your python code here
a = int(input())
a1 = a % 10  # цифра из единиц
a2 = (a % 100) // 10  # цифра из десятков
a3 = a // 100  # цифра из сотен
if (a1 + a2 + a3) - min(a1, a2, a3) - max(a1, a2, a3) == max(a1, a2, a3) - min(a1, a2, a3):
    print('Число интересное')
else:
    print('Число неинтересное')