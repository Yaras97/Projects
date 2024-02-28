from collections import OrderedDict
data = OrderedDict(key1='value1')
data['key2'] = 'value2'
data['key3'] = 'value3'
for key, value in data.items():
    print(f'{key} -> {value}')