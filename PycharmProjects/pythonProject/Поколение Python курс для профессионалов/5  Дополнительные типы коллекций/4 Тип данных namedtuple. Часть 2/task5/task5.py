import csv
from datetime import datetime

with open('meetings.csv', encoding='utf-8') as file:
    file.readline()
    obj = tuple(sorted(csv.reader(file, delimiter=','), key=lambda x: datetime.strptime(x[2]+';'+x[3], '%d.%m.%Y;%H:%M')))
    for field in obj:
        print(field[0], field[1])
