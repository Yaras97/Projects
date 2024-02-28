class Cat:
    def __init__(self, name):
        self.name = name # имя кошки
    def __call__(self):
        print('Меня зовут', self.name)
cat = Cat('Кемаль')
cat()