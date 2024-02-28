def filter_names(names, ignore_char, max_names):
        for name in names:
            if all(map(lambda x: not x.isdigit(), name)):
                if name[0].lower() != ignore_char.lower():
                    yield name
                    if names.index(name) > max_names:
                        break

data = ['Dima', 'Timur', 'Arthur', 'Anri', 'Arina', 'German', 'Ruslan', 'Roma5', 'Jenya', 'Anna']

print(*filter_names(data, 'A', 8))