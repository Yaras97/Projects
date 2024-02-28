import pickle
from collections import namedtuple
Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    obj = pickle.load(file)
    for named_tuple in obj:
        field = named_tuple._fields
        print(f'{field[0]}: {named_tuple.name}')
        print(f'{field[1]}: {named_tuple.family}')
        print(f'{field[2]}: {named_tuple.sex}')
        print(f'{field[3]}: {named_tuple.color}')
        print()




