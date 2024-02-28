from collections import ChainMap, defaultdict, Counter
import json

with open('zoo.json', encoding='utf-8') as file:
    # chain = ChainMap(defaultdict(int, {}))
    # data = json.load(file)
    # for i_dict in data:
    #     for i in i_dict:
    #         chain[i] += i_dict[i]
    # print(*chain.items(), sep='\n')
    data = json.load(file)
    counter = 0
    for i_dict in data:
        counter += Counter(i_dict).total()
    print(counter)


