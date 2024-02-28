# Если такое поведение нежелательно, его можно запретить с помощью __setattr__ –
# метода, перегружающего оператор присваивания атрибуту:

class A:
    def __init__(self, value):
        self.a = value

    def __setattr__(self, key, value):
        if key == 'a':
            self.__dict__['a'] = value
        else:
            raise AttributeError


first = A(10)

first.a = "Hello"
first.a2 = "2"
print(first.__dict__)

