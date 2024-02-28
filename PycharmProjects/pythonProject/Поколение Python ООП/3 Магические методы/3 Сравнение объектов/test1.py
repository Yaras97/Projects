class Fruit:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
fruit1 = Fruit('банан', 150)
fruit2 = Fruit('яблоко', 180)
print(fruit1 == fruit2)
print(fruit1 < fruit2)