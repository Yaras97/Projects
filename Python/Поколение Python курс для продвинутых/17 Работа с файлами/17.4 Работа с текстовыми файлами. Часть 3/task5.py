with open('goats.txt') as inp, open('answer.txt', 'w') as out:
    file1 = inp.readlines()
    colors = [file1[i].strip() for i in range(1, len(file1) - 101)]
    goats = [file1[i].strip() for i in range(8, len(file1))]
    d = {}
    count = 0
    lst = []
    for i in goats:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    s = 0
    for i in d:
        s += d[i]
    for i in d:
        if d[i] > 7:
            lst.append(i)
    print(*sorted(lst), sep='\n', file=out)

