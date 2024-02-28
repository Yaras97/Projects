import json
from collections import defaultdict

with open('10/countries.json', encoding='utf-8') as file:
    file_list = json.load(file)
    new_dict = defaultdict(list)
    for n_dict in file_list:
        new_dict.setdefault(n_dict['religion'], []).append(n_dict['country'])

with open('religion.json', 'w', encoding='utf-8') as file:
    json.dump(new_dict, file, indent=3)
