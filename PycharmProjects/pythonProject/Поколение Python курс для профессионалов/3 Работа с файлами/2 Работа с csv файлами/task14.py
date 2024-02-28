import csv

with open('14/name_log.csv', encoding='utf-8') as file:
    rows = csv.reader(file, quotechar='"', delimiter=',')
    first_line = file.readline()
    first_line = [i.strip() for i in first_line.split(',')]

    new_dict = {}
    for name, mail, date in rows:
        if mail not in new_dict:
            new_dict[mail] = [name, mail, date]
        elif date > new_dict[mail][2]:
            new_dict[mail] = [name, mail, date]

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(first_line)
    for key, item in sorted(new_dict.items(), key=lambda x: x[0]):
        writer.writerow(item)