with open('numbers.txt') as file:
    for i in file:
        st = i.strip().split()
        print(sum(map(int, st)))





