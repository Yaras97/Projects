import json

with open('9/people.json', encoding='utf-8') as file:
    people_list = json.load(file)
    print(people_list)
    new_list = people_list.copy()
    for n_dict in people_list:
        for key, item in n_dict.items():
            for other_dict in range(len(people_list)):
                if key not in new_list[other_dict]:
                    new_list[other_dict][key] = None
    print(new_list)

with open('updated_people.json', 'w', encoding='utf-8') as file:
    json.dump(new_list, file, indent=3)