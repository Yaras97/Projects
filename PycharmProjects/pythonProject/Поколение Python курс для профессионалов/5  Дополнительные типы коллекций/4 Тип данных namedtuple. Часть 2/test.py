from collections import namedtuple
Person = namedtuple('Person', ['name', 'age', 'height'])
ExtendedPerson = namedtuple('ExtendedPerson', [*Person._fields, 'weight']) # распаковка полей старого кортежа
timur = ExtendedPerson('Тимур', 29, 170, 65)
print(timur)
print(ExtendedPerson._fields)
print(type(Person._fields))
