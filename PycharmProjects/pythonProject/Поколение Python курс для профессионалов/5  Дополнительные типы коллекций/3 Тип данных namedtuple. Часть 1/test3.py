from collections import namedtuple
Weather = namedtuple('Weather', ['temp', 'wind', 'rain', 'cloud'])
tokyo_weather = Weather(11, 6, 0.0, 25)
for x in tokyo_weather:
    print(x)