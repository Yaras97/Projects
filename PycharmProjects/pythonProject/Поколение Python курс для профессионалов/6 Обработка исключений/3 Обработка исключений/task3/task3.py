try:
    with open('sample.csv', encoding='utf-8') as file:
        for line in file.readlines():
            print(line.rstrip())
except FileNotFoundError:
    print('Файл не найден')