from collections import ChainMap

authors = ChainMap({'name': 'Timur', 'city': 'Moscow'})
new_authors = authors.new_child()
print(new_authors)
