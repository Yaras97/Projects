# В Python атрибуты объекту можно назначать за пределами класса:

class A:
    def __init__(self, value):
        self.a = value


first = A(10)
second = A(25)

first.b = 'Hello'


print(first.__dict__)   # {'a': 10, 'b': 'Hello'}
print(second.__dict__)  # {'a': 25}


