with open('class_scores.txt', encoding='utf-8') as inp, open('new_scores.txt', 'w', encoding='utf-8') as out:
    for i in inp.readlines():
        x, y = i.strip().split()
        print(f'{x} {int(y) + 5 if int(y) + 5 < 100 else 100}', file=out)
