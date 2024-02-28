import json
try:
    with open(input(), encoding='utf-8') as file:
        data = json.load(file)
        for line in data:
            print(line)
except FileNotFoundError:
    print('Файл не найден')
except json.decoder.JSONDecodeError:
    print('Ошибка при десериализации')
