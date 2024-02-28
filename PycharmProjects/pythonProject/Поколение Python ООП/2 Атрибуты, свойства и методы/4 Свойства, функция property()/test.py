class Cat:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        self._info = None
    def get_info(self):
        if self._info is None:
            self._info = self.breed + ' ' + self.name
        return self._info
    info = property(get_info)

cat = Cat('Британский', 'Кемаль')
print(cat.info)
print(cat.info)
cat = Cat('df', 'afd')
print(cat.info)