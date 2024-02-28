import csv

with open('13/titanic.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=';')
    file.readline()
    male = []
    female = []
    for row in rows:
        if float(row[-1]) < 18 and int(row[0]) == 1 and row[-2] == 'male':
            male.append(row[1])
        elif float(row[-1]) < 18 and int(row[0]) == 1 and row[-2] == 'female':
            female.append(row[1])
    print(*male, *female, sep='\n')
