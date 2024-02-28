class Table:
    def __init__(self, l=1, w=1, h=1):
        self.length = l
        self.width = w
        self.height = h


class KitchenTable(Table):
    def __init__(self, l=1, w=1, h=0.7, p=4):
        Table.__init__(self, l, w, h)
        self.places = p


# Другой вариант – отказаться от конструктора в дочернем классе,
# а значение для поля places устанавливать отдельным вызовом метода:

class Table:
    def __init__(self, l=1, w=1, h=1):
        self.length = l
        self.width = w
        self.height = h


class KitchenTable(Table):
    places = 4

    def set_places(self, p):
        self.places = p


# Если все же требуется указывать места при создании объекта,
# это можно сделать и в конструкторе родителя:

class Table:
    def __init__(self, l=1, w=1, h=1):
        self.length = l
        self.width = w
        self.height = h
        if isinstance(self, KitchenTable):
            p = int(input("Сколько мест: "))
            self.places = p