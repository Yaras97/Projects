from collections import namedtuple
Person = namedtuple('Person', ['name', 'surname', 'age', 'country', 'city'], defaults=
[None] * 3)
timur = Person('Timur', 'Guev', 29)
print(timur)