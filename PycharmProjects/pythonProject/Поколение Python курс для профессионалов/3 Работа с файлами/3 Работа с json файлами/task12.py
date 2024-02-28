import csv
import json

with open('12/students.json', encoding='utf8') as file:
    json_file = json.load(file)
    new_list = []
    for d_key in json_file:
        if d_key['age'] >= 18 and d_key['progress'] >= 75:
            new_list.append(d_key)

with open('12/data.csv', 'w', encoding='utf8', newline='') as file:
    first_row = ['name', 'phone']
    writer = csv.writer(file)
    writer.writerow(first_row)
    for d_key in sorted(new_list, key=lambda x: x['name']):
        writer.writerow([d_key['name'], d_key['phone']])
