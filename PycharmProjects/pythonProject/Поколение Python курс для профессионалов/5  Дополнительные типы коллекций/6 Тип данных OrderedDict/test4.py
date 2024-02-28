from collections import OrderedDict
country1 = dict(name='Finland', capital='Helsinki', currency='euro')
country2 = OrderedDict(currency='euro', capital='Helsinki', name='Finland')
print(country1 == country2)