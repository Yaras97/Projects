from collections import OrderedDict
OrderedDict()
OrderedDict(name='Timur', surname='Guev', hobby='math')
OrderedDict({'name': 'Timur', 'surname': 'Guev', 'hobby': 'math'})
# OrderedDict((['name', 'Timur'], ['surname', 'Guev'], ['hobby', 'math']))
# OrderedDict(int, {'name': 'Timur', 'surname': 'Guev', 'hobby': 'math'})
OrderedDict.fromkeys(('name', 'surname', 'hobby'), 'Empty')