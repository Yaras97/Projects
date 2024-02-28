class ElectricCar:
    def __init__(self, color):
        self._color = color
    @property
    def color(self):
        return self._color

car = ElectricCar('black')
print(car.color)
