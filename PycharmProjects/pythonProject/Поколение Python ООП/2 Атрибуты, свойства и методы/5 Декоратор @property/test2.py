class ElectricCar:
    def __init__(self, owner):
        self._owner = owner
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def set_owner(self, owner):
        self._owner = owner

car = ElectricCar('Elon')
car.owner = 'Gvido'
car.set_owner = 'lol'
print(car._owner)