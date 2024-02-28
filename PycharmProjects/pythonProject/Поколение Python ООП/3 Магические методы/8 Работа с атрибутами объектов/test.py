class Cat:
    def __getattribute__(self, attr):
        print(f'Возвращаю значение атрибута {attr}')
        return object.__getattribute__(self, attr)
    def __getattr__(self, attr):
        print(f'Возвращаю значение по умолчанию')
        return None
    def __setattr__(self, attr, value):
        print(f'Устанавливаю атрибуту {attr} значение {value}')
        self.__dict__[attr] = value
    def __delattr__(self, attr):
        print(f'Удаляю атрибут {attr}')
        del self.__dict__[attr]
cat = Cat()
setattr(cat, 'name', 'Кемаль')
print()
getattr(cat, 'name')
print()
getattr(cat, 'breed')
print()
delattr(cat, 'name')