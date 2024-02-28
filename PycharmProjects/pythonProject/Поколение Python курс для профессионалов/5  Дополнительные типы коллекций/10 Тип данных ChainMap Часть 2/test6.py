from collections import ChainMap

authors = ChainMap({'name': 'Timur', 'city': 'Moscow'})
new_authors = authors.new_child({'name': 'Arthur', 'city': 'Almetyevsk'})
print(new_authors)
