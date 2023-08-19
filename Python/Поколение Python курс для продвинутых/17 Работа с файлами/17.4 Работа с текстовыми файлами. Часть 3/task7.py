with open('logfile.txt', encoding='utf-8') as inp, open('output.txt', 'a', encoding='utf-8') as out:
    for line in inp:
        name, t1, t2 = line.split(', ')
        if int(t2.replace(':', '')) - int(t1.replace(':', '')) >= 100:
            print(name, file=out)