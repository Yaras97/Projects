class Car:
    model = 'BMW' # Атрибуты
    engine = 1.6


'''
Car
<class '__main__.Car'>
Car()
<__main__.Car object at 0x00000193ACFC81D0>

a1 = Car()
a2 = Car()
Car.__dict__
mappingproxy({'__module__': '__main__', 'model': 'BMW', 'engine': 1.6, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None, '__annotations__': {}})

a1.model
'BMW'
a2.engine
1.6

a1.__dict__
{}

a1.seat = 4
a1.__dict__
{'seat': 4}

a2.__dict__
{}

a1.model = "Lada"
a1.__dict__
{'seat': 4, 'model': 'Lada'}

a1.model
'Lada'

a1.engine
1.6

a2.size = 80
a2.size
80
Car.size
error

Car.r = 100
a1.r
100
a2.r
100
a1.__dict__
{'seat': 4, 'model': 'Lada'}

del a1.model
a1.__dict__
{'seat': 4}
a1.model
'BMW'



'''