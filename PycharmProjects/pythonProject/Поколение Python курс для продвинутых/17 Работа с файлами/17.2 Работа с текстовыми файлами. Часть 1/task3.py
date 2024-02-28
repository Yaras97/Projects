import random
file = open('lines.txt', encoding='utf-8')
ln = list(map(str.strip, file.readlines()))
print(random.choice(ln))
file.close()