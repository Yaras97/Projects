from contextlib import contextmanager
import shutil

@contextmanager
def safe_write(filename):
    filename_copy = filename + ".bak"  # Создаем копию файла
    try:
        shutil.copyfile(filename, filename_copy)  # Создаем копию файла
        with open(filename, 'w') as file:
            yield file
    except Exception as e:
        print(f"Во время записи в файл было возбуждено исключение {type(e).__name__}")
        shutil.copyfile(filename_copy, filename)  # Восстанавливаем оригинальное состояние файла


with safe_write('under_tale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')

with safe_write('under_tale.txt') as file:
    print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file)
    raise ValueError

with open('under_tale.txt') as file:
    print(file.read())