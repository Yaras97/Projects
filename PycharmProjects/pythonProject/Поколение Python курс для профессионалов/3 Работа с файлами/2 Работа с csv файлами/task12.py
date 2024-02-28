import csv

with open('wifi.csv', encoding='utf-8') as file:
    rows = csv.reader(file, quotechar='"', delimiter=';')
    file.readline()
    wifi_dict = {}
    for row in rows:
        if row[1] not in wifi_dict:
            wifi_dict[row[1]] = int(row[-1])
        else:
            wifi_dict[row[1]] = wifi_dict[row[1]] + int(row[-1])

    for i in sorted(sorted(wifi_dict.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True):
        print(f'{i[0]}: {i[1]}')
