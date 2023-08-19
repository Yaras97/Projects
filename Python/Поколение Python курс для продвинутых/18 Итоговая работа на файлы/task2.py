with open('ledger.txt') as file:
    c = 0
    for i in file.readlines():
        c += int(i.lstrip('$').strip())
    print("$" + str(c))