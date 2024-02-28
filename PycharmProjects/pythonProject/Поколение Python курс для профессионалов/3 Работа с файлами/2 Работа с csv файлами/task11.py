'''
Популярные домены
Вам доступен файл data.csv , который содержит неповторяющиеся данные о пользователях
некоторого ресурса. В первом столбце записано имя пользователя, во втором — фамилия, в
третьем — адрес электронной почты:
first_name,surname,email
John,Wilson,johnwilson@outlook.com
Mary,Wilson,marywilson@list.ru
...
Напишите программу, которая создает файл domain_usage.csv , имеющий следующее
содержание:
domain,count
rambler.ru,24
iCloud.com,29
...
где в первом столбце записано название почтового домена, а во втором — количество
пользователей, использующих данный домен. Домены в файле должны быть расположены в
порядке возрастания количества их использований, при совпадении количества
использований — в лексикографическом порядке.
'''

import csv

with open('data1.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=',')
    file.readline()
    file_dict = {}
    for row in rows:
        post = row[2].split('@')[1]
        file_dict[post] = file_dict.get(post, 0) + 1
    sorted_list = sorted(file_dict.items(), key=lambda x: (int(x[1]), x[0]))


with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
    columns = ['domain', 'count']
    writer = csv.writer(file, delimiter=',')
    writer.writerow(columns)
    for key, value in sorted_list:
        writer.writerow([key, value])

