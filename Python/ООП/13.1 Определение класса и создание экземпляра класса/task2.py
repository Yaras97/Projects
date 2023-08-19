class Class:
    def __init__(self):
        self.x = 10
    def get_x(self):
        return self.x
c = Class()
c.get_x()
print(c.x)
print(getattr(c, "x"))
print(getattr(c, "get_x")())
print(getattr(c, 'y', 0))
setattr(c, 'y', 20)
print(getattr(c, 'y', 0))
delattr(c, 'y')
print(getattr(c, 'y', 0))
print(hasattr(c, 'x'))
print(hasattr(c, 'y'))