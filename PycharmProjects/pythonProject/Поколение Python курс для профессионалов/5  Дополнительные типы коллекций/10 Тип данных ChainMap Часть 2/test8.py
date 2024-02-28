from collections import ChainMap

team = ChainMap({'name': 'Timur', 'city': 'Moscow'},
                {'name': 'Anri', 'city': 'Saint-Petersburg'},
                {'name': 'Arthur', 'city': 'Almetyevsk'})
print(team.parents == ChainMap(*team.maps[1:]))
