from math import pi


def make_area(d, h):
    circle = pi * d ** 2 / 4
    side = pi * d * h
    return round(circle * 2 + side, 2)


class Cylinder:
    def __init__(self, diameter, high):
        self.dia = diameter
        self.h = high



a = Cylinder(1, 2)
print(make_area(a.dia, a.h))

print(make_area(2, 2))
print(make_area(2.5, 0.5))