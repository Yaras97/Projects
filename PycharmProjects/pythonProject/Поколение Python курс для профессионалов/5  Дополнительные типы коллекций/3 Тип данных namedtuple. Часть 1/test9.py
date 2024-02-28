from collections import namedtuple
unknowntype = namedtuple('Car', ['model', 'color', 'price'])
obj = unknowntype('Audi A5', 'white', 52900)
print(obj)
print(type(obj))
obj.m