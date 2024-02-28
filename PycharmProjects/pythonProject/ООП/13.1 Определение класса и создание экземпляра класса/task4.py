class MyClass:
    x = 10                  # Атрибут объекта класса
    def __init__(self):
        self.y = 20         # Атрибут экземпляра класса

c1 = MyClass()              # Создаем экземпляр класса
c2 = MyClass()              # Создаем экземпляр класса

print(c1.x, c2.x)
MyClass.x = 88
print(c1.x, c2.x)

print(c1.y, c1.y)
c1.y = 88
print(c1.y, c1.y)

MyClass.x = 88             # Изменяем атрибут объекта класса

c1.x = 200                  # Создаем атрибут экземпляра

print(c1.x, MyClass.x)


