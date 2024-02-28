from collections import OrderedDict
planets1 = OrderedDict(Mercury=2, Venues=2, Earth=None, Mars=4, Jupiter=5)
planets2 = OrderedDict(Mercury=3, Saturn=6, Uranus=7, Neptune=8, Earth=3)
solar_system = planets1 | planets2
print(*solar_system)
print(solar_system)