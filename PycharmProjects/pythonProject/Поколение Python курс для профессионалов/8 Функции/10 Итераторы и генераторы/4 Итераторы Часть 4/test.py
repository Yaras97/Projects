class Counter:
    def __init__(self, low, high):  # конструктор принимает два аргумента low и high (помимо self)
        self.low = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.low > self.high:
            raise StopIteration
        else:
            self.low += 1
            return self.low - 1


counter1 = Counter(3, 10)      # создаем итератор Counter, передавая значения low=3, high = 10
for i in counter1:                      # неявно вызываем функцию next()
    print(i)
counter2 = Counter(100, 103)   # создаем итератор Counter, передавая значения low=100, high = 103
print(next(counter2))                    # явно вызываем функцию next()
print(next(counter2))                    # явно вызываем функцию next()
