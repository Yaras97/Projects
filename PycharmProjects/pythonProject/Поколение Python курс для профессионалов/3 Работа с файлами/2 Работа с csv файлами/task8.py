import csv
with open('sales.csv', encoding='utf-8', newline='') as file:
    rows = csv.reader(file, delimiter=';')
    file.readline()
    for row in rows:
        if int(row[1]) > int(row[2]):
            print(row[0])