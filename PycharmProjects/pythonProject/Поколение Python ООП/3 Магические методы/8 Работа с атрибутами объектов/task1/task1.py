class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, item):
        if item == 'name':
            return object.__getattribute__(self, item).capitalize()
        elif item == 'total':
            return self.price * self.quantity
        return object.__getattribute__(self, item)


goods = [
    Item('Морковь', 257, 20),
    Item('Лук', 251, 10),
    Item('Свекла', 120, 11),
    Item('Капуста', 280, 2),
    Item('Огурцы', 87, 5),
    Item('Помидоры', 123, 3),
    Item('Болгарский', 192, 2),
    Item('Перец', 197, 9),
    Item('Яблоки', 261, 3),
    Item('Груши', 103, 15),
    Item('Лимон', 166, 7),
    Item('Апельсины', 213, 2),
    Item('Бананы', 71, 13),
    Item('Виноград', 247, 10),
    Item('Киви', 226, 20)
]

for product in goods:
    print(product.name, product.total, 'руб.')