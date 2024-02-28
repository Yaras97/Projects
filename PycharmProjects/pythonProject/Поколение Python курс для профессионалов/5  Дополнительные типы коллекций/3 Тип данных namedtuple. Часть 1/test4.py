from collections import namedtuple
Tree = namedtuple('Tree', 'name,colors,height')
cruenta = Tree(height=2, name='Cruenta', colors=('red', 'green'))
print(cruenta)