# Атрибуты класса

class Person:
    name = 'Ivan'
    age = 30


Person.name = 'Misha'
Person.x = [1, 2, 3]
Person.__dict__
getattr(Person, 'name')
setattr(Person, 'x', 200)
del Person.x
delattr(Person, 'y')


"""
class Person:
    name = 'Ivan'
    age = 30

Person.name
'Ivan'

Person.age
30

Person.__dict__
mappingproxy({'__module__': '__main__', 'name': 'Ivan', 'age': 30, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None, '__annotations__': {}})


getattr(Person, 'name')
error
getattr(Person, 'x', 100)
100
getattr(Person, 'name', 200)
'Ivan'

Person.name = 'Misha'
Person.name
'Misha'

Person.x = 100
Person.x
100

Person.x = [1, 2, 3]
Person.x
[1, 2, 3]

setattr(Person, 'x', 200)
Person.x

setattr(Person, 'y', 10)
Person.y
10

del Person.x
Person.__dict__
mappingproxy({'__module__': '__main__', 'name': 'Misha', 'age': 30, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None, '__annotations__': {}, 'y': 10})

delattr(Person, 'y')
Person.__dict__
mappingproxy({'__module__': '__main__', 'name': 'Misha', 'age': 30, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None, '__annotations__': {}})

Person()
<__main__.Person object at 0x00000262650A72D0>

a = Person()
b = Person()
c = Person()

Person.z = 100
del Person.age

a.b = 200

"""