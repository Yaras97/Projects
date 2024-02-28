class Shape:
    pass

class Polygon(Shape):
    pass

class Circle(Shape):
    pass

class Quadrilateral(Polygon):
    pass

class Triangle(Polygon):
    pass

class IsoscelesTriangle(Triangle):
    pass

class EquilateralTriangle(Triangle):
    pass

class Parallelogram(Quadrilateral):
    pass

class Rectangle(Parallelogram):
    pass

class Square(Rectangle):
    pass

print(issubclass(Square, Shape))
print(issubclass(IsoscelesTriangle, Shape))
print(issubclass(EquilateralTriangle, Shape))
print(issubclass(Circle, Shape))