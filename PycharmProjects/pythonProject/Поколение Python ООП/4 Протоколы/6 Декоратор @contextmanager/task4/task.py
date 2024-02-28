from contextlib import contextmanager

@contextmanager
def safe_open(filename, mode='r',):
    try:
        file = open(filename, mode=mode, encoding='utf8')
    except Exception as err:
        yield None, err
    else:
        try:
            yield file, None
        finally:
            file.close()


text = '''Кричит ворона в небе: – Кар-р!
В лесу пожар-р, в лесу пожар-р!
А было просто очень:
В нём поселилась осень.'''

with open('file.txt', 'w', encoding='utf-8') as file:
    file.write(text)

with safe_open('file.txt', 'r') as file:
    file, error = file
    print(file.read())
    print(error)