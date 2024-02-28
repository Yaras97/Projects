class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        self.length = l
        self.width = w
        self.height = h
        self.places = p


t4 = KitchenTable(1.5, 2, 0.75, 6)


# Поскольку существенная часть кода конструктора подкласса является такой же как в надклассе,
# правильнее будет вызвать метод другого класса, а не дублировать код:
class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        Table.__init__(self, l, w, h)
        self.places = p


t4 = KitchenTable(1.5, 2, 0.75, 6)


# В Python с целью улучшения так называемой обслуживаемости кода можно использовать
# встроенную в язык функцию super. Наиболее распространенным вариантом ее применения
# является вызов метода родительского класса из метода подкласса:

class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        super().__init__(l, w, h)
        self.places = p