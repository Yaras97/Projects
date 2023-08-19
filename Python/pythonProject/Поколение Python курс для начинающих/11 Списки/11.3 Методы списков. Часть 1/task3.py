spisok = []
count = 1
for i in range(97, 123):
    spisok += [chr(i) * count]
    count += 1
print(spisok)