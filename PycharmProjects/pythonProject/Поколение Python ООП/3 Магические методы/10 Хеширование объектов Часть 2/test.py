class ColoredPoint:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def x_y_color(self):
        return self.x, self.y, self.color

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y

    @property
    def color(self):
        return self.color

    def __repr__(self):
        return f'ColoredPoint({self.x}, {self.y}, {self.color})'

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self.x_y_color() == other.x_y_color()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, ColoredPoint):
            return self.x_y_color() != other.x_y_color()
        return NotImplemented

    def __hash__(self):
        return hash(self.x_y_color())


