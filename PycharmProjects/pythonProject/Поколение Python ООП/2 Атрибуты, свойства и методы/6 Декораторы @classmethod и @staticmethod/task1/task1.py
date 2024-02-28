class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

circle = Circle.from_diameter(120)
print(hasattr(circle, 'radius'))