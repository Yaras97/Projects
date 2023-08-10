with open('nums.txt') as file:
    lst = [i.split() for i in file.readlines()]
    sm = []
    for ls in lst:
        for word in ls:
            w = ''
            for alf in word:
                if alf.isdigit():
                    w += alf
                if alf.isalpha():
                    sm.append(w)
                    w = ''
            sm.append(w)


a = list(map(int, filter(lambda x: x.isdigit(), sm)))
print(sum(a))
