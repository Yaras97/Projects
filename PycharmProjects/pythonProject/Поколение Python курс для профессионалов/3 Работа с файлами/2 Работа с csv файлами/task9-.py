import csv
from collections import defaultdict

with (open('salary_data.csv', encoding='utf-8') as file):
    rows = csv.reader(file, delimiter=';', quotechar='"')
    new_dict = defaultdict(list)
    file.readline()
    for name, salary in rows:
        new_dict[name].append(int(salary))

    finish_dict = {}
    for key, value in new_dict.items():
        finish_dict[key] = int(sum(value)/len(value))
    for key, value in sorted(finish_dict.items(), key=lambda x: x[1]):
        print(key)
