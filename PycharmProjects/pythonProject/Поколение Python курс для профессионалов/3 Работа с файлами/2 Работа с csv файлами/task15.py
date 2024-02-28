import csv

with open('15/deniro.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=',')
    sort_number = int(input()) - 1
    file_list = []
    for row in rows:
        new_row = []
        for i in row:
            if i.isdigit():
                new_row.append(int(i))
            else:
                new_row.append(i)
        file_list.append(new_row)

    for item in sorted(file_list, key=lambda x: x[sort_number]):
        print(*item, sep=',')