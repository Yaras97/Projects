class Cat:
    def __init__(self, name):
        self._name = name
    @property
    def name(self): # первое свойство name, доступное только для чтения
        return self._name
    @name.setter
    def name(self, name): # второе свойство set_name, доступное для чтения и записи
        self._name = name
    @name.deleter
    def name(self): # третье свойство del_name, доступное для чтения и удаления
        del self._name

cat = Cat('Кемаль')

print(cat.name)
cat.name = 'lol'
print(cat.name)
print(cat.__dict__)
del cat.name
print(cat.__dict__)