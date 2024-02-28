class Cat:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        print('Получение значения атрибута name')
        return self._name
    @name.setter
    def name(self, value):
        print('Изменение значения атрибута name')
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError('Некорректное имя')
    @name.deleter
    def name(self):
        print('Удаление атрибута name')
        del self._name


cat = Cat('Кемаль')

name_property = Cat.name # свойство name, он же объект типа property, он же дескриптор
name_property.__get__(cat, Cat) # равнозначно cat.name
name_property.__set__(cat, 'Роджер') # равнозначно cat.name = 'Роджер'
name_property.__delete__(cat) # равнозначно del cat.name