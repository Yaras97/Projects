class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        for key, value in kwargs.items():
            self.__dict__.setdefault(key, value)

    def __getattr__(self, item):
        return self.default


god = DefaultObject(name='Kratos', mythology='greek')
print('name' in god.__dict__)
print('mythology' in god.__dict__)

# class DefaultObject:
#
#     def __init__(self, default=None, **kwargs):
#         self.default = default
#         for k, v in kwargs.items():
#             self.__setattr__(k, v)
#
#     def __getattr__(self, item):
#         return self.default
#
#     def __setattr__(self, key, value):
#         self.__dict__[key] = value
