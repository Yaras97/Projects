class ElectricCar:
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return f'ElectricCar >> color: {self.color}'
    
car = ElectricCar('black')
print(car)
print(str(car))