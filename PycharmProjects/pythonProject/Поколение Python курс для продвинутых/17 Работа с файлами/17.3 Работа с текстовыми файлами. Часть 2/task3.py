with open('lines.txt') as file:
    lst = sorted([i.strip() for i in file.readlines()], key=len)
    s = lst[-1]
    for i in lst:
        if len(s) == len(i):
            print(i)