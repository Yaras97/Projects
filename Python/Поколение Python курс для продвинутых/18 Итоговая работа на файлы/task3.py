with open('grades.txt') as file:
    count2 = 0
    for i in file.readlines():
        count = 0
        for j in i.strip().split()[1::]:
            if int(j) >= 65:
                count += 1
        if count == 3:
            count2 += 1
    print(count2)