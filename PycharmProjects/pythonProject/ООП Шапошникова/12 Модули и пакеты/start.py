from geometry import planimetry, stereometry
# from geometry import *

a = planimetry.Rectangle(3, 4)
print(a.square())

b = planimetry.Circle(6)
print(b.length())

c = stereometry.Ball(13)
print(c.V())