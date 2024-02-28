from collections import namedtuple
headers = ('_name', 'surname', 'age', 'class')
Student = namedtuple('Student', headers, rename=True)
spidey = Student('Peter', 'Parker', 15, 10)
print(spidey)