from collections import ChainMap
authors = ChainMap({'name': 'Timur', 'city': 'Moscow'},
{'name': 'Arthur', 'city': 'Almetyevsk'})
print(authors.maps)