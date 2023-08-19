n = input()
s = 'Цифр нет'
for i in range(len(n)):
    if n[i] in '0123456789':
        s = 'Цифра'
        break
print(s)