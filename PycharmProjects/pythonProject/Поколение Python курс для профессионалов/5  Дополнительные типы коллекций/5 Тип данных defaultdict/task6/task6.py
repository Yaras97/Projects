from collections import defaultdict


def best_sender(messages, senders):
    new_dict = defaultdict(int)
    for i in range(len(messages)):
        new_dict[senders[i]] += len(messages[i].split())
    sort_list = sorted(new_dict.items(), key=lambda x: (x[1], x[0]))
    return sort_list[-1][0]


messages = ['bu bu da', 'bu bu da', 'bu bu da', 'bu bu da', 'bu bu da', 'bu bu net']
senders = ['dima', 'anri', 'timur', 'timur', 'anri', 'dima']

print(best_sender(messages, senders))