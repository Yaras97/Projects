import csv
from collections import defaultdict
from collections import OrderedDict

text = '''ball,color,purple
ball,size,4
ball,notes,it's round
cup,color,blue
cup,size,1
cup,notes,none'''


def condense_csv(filename, id_name):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

    with open(filename, 'r', encoding='utf-8') as file:
        rows = csv.reader(file)
        file_dict = defaultdict(list)

        for row in rows:
            file_dict.setdefault(id_name, []).append(row[0])
            file_dict.setdefault(row[1], []).append(row[2])
        file_dict = dict(file_dict)
        file_dict[id_name] = list(OrderedDict.fromkeys(file_dict[id_name]))
        finally_list = []
        for i in range(len(file_dict[id_name])):
            interim_list = []
            for value in file_dict:
                interim_list.append(file_dict[value][i])
                continue
            finally_list.append(interim_list)

    with open('condensed.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        first_line = [i for i in file_dict]
        writer.writerow(first_line)
        for string in finally_list:
            writer.writerow(string)


condense_csv('data.csv', id_name='ID')

