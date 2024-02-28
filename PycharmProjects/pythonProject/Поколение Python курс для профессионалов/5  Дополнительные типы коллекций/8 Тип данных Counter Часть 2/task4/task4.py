from collections import Counter

counter = Counter()
for word in input().split():
    counter.update([len(word)])

for i in sorted(counter.items(), key=lambda x: x[1]):
    print(f'Слов длины {i[0]}: {i[1]}')