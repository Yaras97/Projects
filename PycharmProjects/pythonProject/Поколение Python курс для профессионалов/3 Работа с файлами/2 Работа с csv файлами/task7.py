import csv

with open('writing_test.csv', 'w', encoding='utf-8', newline='') as csv_file:
    # создаем writer объект и указываем названия столбцов
    writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'], delimiter=',')
    # записываем первую строку с названиями столбцов
    print(writer.writeheader())
    # записываем строку с данными
    writer.writerow({'first_col': 'value1', 'second_col': 'value2'})
