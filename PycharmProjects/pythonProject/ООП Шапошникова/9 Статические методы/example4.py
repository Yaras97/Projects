from math import pi


class Cylinder:
    def __init__(self, diameter, high):
        self.dia = diameter
        self.h = high

    def make_area(self):
        circle = pi * self.dia ** 2 / 4
        side = pi * self.dia * self.h
        return round(circle * 2 + side, 2)




a = Cylinder(1,2)

print(a.make_area())