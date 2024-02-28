# keys = ['name', 'age', 'job']
# values = ['Timur', 28, 'Teacher']
#
# info = dict(zip(keys, values))
#
# print(info)


capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}

for key, value in sorted(capitals.items(), key=lambda x: x[1]):
    print(key)