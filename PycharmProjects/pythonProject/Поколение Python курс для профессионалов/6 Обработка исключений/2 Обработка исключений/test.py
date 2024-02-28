persons = [{'name': 'Timur', 'city': 'Moscow'},
           {'name': 'Arthur', 'city': 'Almetyevsk'},
           {'name': 'Dima', 'city': 'Moscow'}]

try:
    result = Persons[2]['city']
    print(result)
except (IndexError, KeyError, NameError):
    print('Произошла ошибка')