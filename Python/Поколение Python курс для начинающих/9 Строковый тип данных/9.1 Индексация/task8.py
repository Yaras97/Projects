n = input()
count1 = 0
count2 = 0
for i in range(len(n)):
    if n[i] in '+':
        count1 += 1
    if n[i] in '*':
        count2 += 1
print('Символ + встречается', count1, 'раз')
print('Символ * встречается', count2, 'раз')