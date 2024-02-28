# put your python code here
a = int(input())
if a % 10 + a % 10000//1000 == (a % 1000) // 100 - (a % 100) // 10:
    print('ДА')
else:
    print('НЕТ')