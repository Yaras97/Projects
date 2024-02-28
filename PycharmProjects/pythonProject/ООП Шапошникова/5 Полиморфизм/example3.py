class Rectangle:
    def __init__(self, width, height, sign):
        self.w = int(width)
        self.h = int(height)
        self.s = str(sign)

    def __str__(self):
        rect = []
        # количество строк
        for i in range(self.h):
            # знак повторяется w раз
            rect.append(self.s * self.w)
            # превращаем список в строку
        rect = '\n'.join(rect)
        return rect


b = Rectangle(10, 3, '*')
print(b)