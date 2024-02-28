class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def func(self):
        return self.x, self.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(*map(lambda x, y: x + y, self.func(), other.func()))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(*map(lambda x, y: x - y, self.func(), other.func()))
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return Vector(*map(lambda x: x * n, self.func()))
        return NotImplemented

    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            return Vector(*map(lambda x: x / n, self.func()))
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        return self.__truediv__(other)


vector = Vector(10, 20)
print(vector.__add__([]))
print(vector.__sub__(()))
print(vector.__mul__({}))
print(vector.__truediv__(set()))