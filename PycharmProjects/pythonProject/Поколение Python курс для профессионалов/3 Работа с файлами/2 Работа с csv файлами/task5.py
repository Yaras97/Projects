import csv

with open('data.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter='\t', quotechar='"')
    for row in rows:
        print(*row)