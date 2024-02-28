def get_id(names, name):
    try:
        if type(name) is not str:
            raise TypeError('Имя не является строкой')
        if type(name) is str:
            if name != name.capitalize():
                raise ValueError('Имя не является корректным')
            for letter in name:
                if not letter.isalpha():
                    raise ValueError('Имя не является корректным')
        names.append(name)
        st_id = [i for i in enumerate(names, 1)]
        return st_id[-1][0]
    except TypeError:
        raise TypeError('Имя не является строкой')
    except ValueError:
        raise ValueError('Имя не является корректным')
    except Exception:
        raise TypeError('Имя не является строкой')


names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = False

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)