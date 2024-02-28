class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, obj):
        return cls(*obj)

    @classmethod
    def from_str(cls, string):
        string = map(float, string.split())
        return cls(*string)


polynom = QuadraticPolynomial.from_iterable([2.5, 13.2, -1.8])

print(polynom.a)
print(polynom.b)
print(polynom.c)