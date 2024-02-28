class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(self.proteins + other.proteins, self.fats + other.proteins, self.carbohydrates + other.carbohydrates)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(self.proteins * n, self.fats * n, self.carbohydrates * n)
        return NotImplemented

    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(self.proteins / n, self.fats / n, self.carbohydrates / n)
        return NotImplemented


    def __floordiv__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(self.proteins // n, self.fats // n, self.carbohydrates // n)
        return NotImplemented


food = FoodInfo(10, 20, 30)

print(food.__add__(1))
print(food.__mul__(range(5)))
print(food.__truediv__([1, 2, 3]))
print(food.__floordiv__({4, 5, 6}))