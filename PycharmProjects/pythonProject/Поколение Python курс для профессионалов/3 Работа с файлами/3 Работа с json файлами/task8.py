import json

with open('8/data1.json', encoding='utf-8') as file:
    json_data1 = json.load(file)

with open('8/data2.json', encoding='utf-8') as file:
    json_data2 = json.load(file)

with open('data_merge.json', 'w', encoding='utf-8') as file:
    copy_dict = dict(json_data1)
    for key, item in json_data2.items():
        copy_dict[key] = item
    json.dump(copy_dict, file, indent=3)
