from collections import ChainMap

authors = ChainMap({'name': 'Timur', 'city': 'Moscow'})
authors.new_child({'name': 'Arthur', 'city': 'Almetyevsk', 'lol': 'kek'})
print(authors)
