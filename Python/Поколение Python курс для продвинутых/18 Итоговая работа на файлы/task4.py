with open('words.txt') as file:
    sp = []
    for i in file.readlines():
        sp += i.strip().split()
    sp = sorted(sp, key=len, reverse=True)
    sp = [i for i in sp if len(i) == len(sp[0])]
    print(*sp, sep='\n')