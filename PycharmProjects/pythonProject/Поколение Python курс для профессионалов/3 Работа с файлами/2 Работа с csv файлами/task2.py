import csv
with open('biostats.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)
        break