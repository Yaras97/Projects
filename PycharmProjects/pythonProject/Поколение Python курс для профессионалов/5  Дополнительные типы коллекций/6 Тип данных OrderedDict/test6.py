from collections import OrderedDict
flower = OrderedDict([('name', 'Rose'), ('family', 'Rosaceae'), ('kingdom', 'Plantae')])
flower.move_to_end('family')
for key, value in flower.items():
    print(f'{key}: {value}')