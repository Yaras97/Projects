# На самом деле цикл for ожидает, что у объекта есть не только метод __next__,
# но и __iter__. Задача метода __iter__ – "превращать" итерируемый объект в итератор.
# Если в цикл for передается уже итератор, то метод __iter__() этого объекта должен возвращать сам объект:

class A:
    def __init__(self, qty):
        self.qty = qty

    def __iter__(self):
        return self

    def __next__(self):
        if self.qty > 0:
            self.qty -= 1
            return '+'

        else:
            raise StopIteration


a = A(4)
for i in a:
    print(i)
