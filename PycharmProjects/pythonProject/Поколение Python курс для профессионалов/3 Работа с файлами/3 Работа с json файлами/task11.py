import csv
import json
from collections import defaultdict

with open('11/playgrounds.csv', encoding='utf-8') as file:
    list_file = csv.reader(file, delimiter=';')
    file.readline()
    areas = defaultdict(lambda: defaultdict(list))
    for row in list_file:
        areas[row[1]][row[2]].append(row[3])

with open('addresses.json', 'w', encoding='utf-8') as file:
    json.dump(areas, file, indent=3, ensure_ascii=False)

