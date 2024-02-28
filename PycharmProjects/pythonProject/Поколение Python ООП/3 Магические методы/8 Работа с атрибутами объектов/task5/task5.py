class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)):
            if value < 0:
                value = -value
        self.__dict__[key] = value


# class NonNegativeObject:
#     def __init__(self, **kwargs):
#         for name, value in kwargs.items():
#             setattr(self, name, value)
#
#     def __setattr__(self, name, value):
#         if isinstance(value, (int, float)):
#             value = abs(value)
#         object.__setattr__(self, name, value)

point = NonNegativeObject(x=1, y=-2, z=0, color='black')

print(point.x)
print(point.y)
print(point.z)
print(point.color)