from collections import OrderedDict
country1 = OrderedDict(name='Finland', capital='Helsinki', currency='euro')
country2 = OrderedDict(name='Finland', capital='Helsinki', currency='euro')
country2.move_to_end('name')
print(country1 == country2)