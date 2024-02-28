class Cat:
    def __init__(self, name):
        self._name = name # имя кошки
    def get_name(self): # геттер, используется для получения имени
        return self._name
cat = Cat('Кемаль')
print(cat.get_name())