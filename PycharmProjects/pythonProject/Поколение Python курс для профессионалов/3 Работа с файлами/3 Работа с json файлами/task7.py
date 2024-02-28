import json

with open('7/data.json', encoding='utf-8') as file:
    json_file = json.load(file)
    copy_file = []
    for item in json_file:
        if type(item) is str:
            copy_file.append(item + '!')
        elif type(item) is None:
            continue
        elif type(item) is int:
            copy_file.append(item + 1)
        elif type(item) is float:
            copy_file.append(item + 1)
        elif type(item) is bool:
            copy_file.append(not item)
        elif type(item) is list:
            copy_file.append(item*2)
        elif type(item) is dict:
            new_dict = dict(item)
            new_dict["newkey"] = None
            copy_file.append(new_dict)

with open('updated_data.json', 'w', encoding='utf-8') as file:
    json.dump(copy_file, file, indent=3)
    print(json_file)
    print(copy_file)