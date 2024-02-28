from collections import defaultdict
messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']
new_dict = defaultdict(int)
for i in range(len(messages)):
    new_dict[senders[i]] += len(messages[i].split())

print(new_dict)

