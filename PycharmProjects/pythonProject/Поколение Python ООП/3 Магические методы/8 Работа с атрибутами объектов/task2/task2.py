class Logger:
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        print(f'Изменение значения атрибута {key} на {value}')
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        print(f'Удаление атрибута {item}')
        object.__delattr__(self, item)


# class Logger:
#     def __setattr__(self, name, value):
#         print(f'Изменение значения атрибута {name} на {value}')
#         self.__dict__[name] = value
#
#     def __delattr__(self, name):
#         print(f'Удаление атрибута {name}')
#         del self.__dict__[name]


obj = Logger()

excluded = ['explain', 'much', 'determine', 'response', 'realize', 'wait', 'television', 'million', 'think', 'water',
            'purpose', 'treat', 'both', 'land', 'condition', 'mission', 'air', 'public', 'cultural', 'ok', 'ever',
            'run', 'institution', 'smile', 'industry', 'person', 'leave', 'watch', 'tell', 'while', 'total',
            'interview', 'whom', 'staff', 'technology', 'successful', 'measure', 'country', 'let', 'every', 'design',
            'control', 'realize', 'rather', 'citizen', 'food', 'return', 'pass', 'person', 'week']

for item in excluded:
    try:
        delattr(obj, item)
    except (KeyError, AttributeError):
        print('Класс', obj.__class__.__name__, 'не имеет атрибута', item)