import json

with open('13/pools.json', encoding='utf-8') as file:
    json_list = json.load(file)
    new_list = []

    for d_key in json_list:
        time_key = d_key['WorkingHoursSummer']['Понедельник'].split('-')
        if int(time_key[0][:2]) <= 10 and int(time_key[1][:2]) >= 12:
            new_list.append(d_key)
    last_list = sorted(new_list, key=lambda x: (x['DimensionsSummer']['Length'], x['DimensionsSummer']['Width']), reverse=True)
    biggest = last_list[0]
    print(f'{biggest["DimensionsSummer"]["Length"]}x{biggest["DimensionsSummer"]["Width"]}\n'
          f'{biggest["Address"]}')