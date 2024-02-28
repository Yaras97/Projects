# Если объект итератором не является, то есть у него нет метода __next__,
# то вызов функции next() приведет к ошибке:

# a = [1, 2]
# next(a)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'list' object is not an iterator

# Внутренний механизм работы цикла for так устроен, что на каждой итерации
# он вызывает функцию next() и передает ей в качестве аргумента объект,
# указанный после in в заголовке. Как только next() возвращает StopIteration,
# цикл for ловит это исключение и завершает свою работу.
#
# Напишем собственный класс с методом __next__:

class A:
    def __init__(self, qty):
        self.qty = qty

    def __next__(self):
        if self.qty > 0:
            self.qty -= 1
            return '+'
        else:
            raise StopIteration


a = A(3)
print(next(a))
print(next(a))
print(next(a))
# print(next(a))

# Вызов next() работает, но если мы попробуем передать объект циклу for, получим ошибку:
b = A(5)
for i in b:
    print(i)



