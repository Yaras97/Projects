from collections import Counter

with open('name_log.csv', encoding='utf-8') as file:
    counter = Counter()
    file.readline()
    for line in file.readlines():
        email = line.strip().split(',')[1]
        counter.update([email])
    for mail in sorted(counter):
        print(f'{mail}: {counter[mail]}')