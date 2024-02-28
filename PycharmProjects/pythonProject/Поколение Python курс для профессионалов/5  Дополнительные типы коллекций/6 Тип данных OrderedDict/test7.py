from collections import OrderedDict
flower = OrderedDict([('name', 'Viola'), ('family', 'Violaceae'), ('kingdom',
'Plantae')])
flower.move_to_end('kingdom', last=False)
for key, value in flower.items():
    print(f'{key}: {value}')